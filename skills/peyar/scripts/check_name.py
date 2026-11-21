#!/usr/bin/env python3
"""Peyar availability checker: domains and social handles, plus manual-check links.

Uses only the Python standard library. Needs no API keys.

Results are HINTS, not guarantees:
  likely-free  the registry or site says the name does not exist
  taken        a record or profile exists
  unknown      blocked, rate-limited or not checkable; check by hand

Usage:
    python3 check_name.py peyar
    python3 check_name.py "Paper Boat" --tlds com,in,co.in,ai --json
"""
from __future__ import annotations

import argparse
import json
import re
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36 peyar-skill"
TIMEOUT = 15

# RDAP endpoints. .in/.co.in come from the IANA bootstrap (NIXI); rdap.org redirects the rest.
RDAP = {
    "in": "https://rdap.nixiregistry.in/rdap/domain/{d}",
    "co.in": "https://rdap.nixiregistry.in/rdap/domain/{d}",
    "default": "https://rdap.org/domain/{d}",
}

# TLDs with no working RDAP: use port-43 WHOIS. Value = (server, "not found" marker).
WHOIS = {
    "io": ("whois.nic.io", "domain not found"),
    "co": ("whois.registry.co", "no data found"),
    "me": ("whois.nic.me", "not found"),
}

# WHOIS used only when RDAP fails (throttled / down).
WHOIS_FALLBACK = {
    "in": ("whois.nixiregistry.in", "is available for registration"),
    "co.in": ("whois.nixiregistry.in", "is available for registration"),
    "com": ("whois.verisign-grs.com", "no match for"),
}

# Sites where a 404 reliably means "no such handle".
HANDLE_SITES = {
    "youtube": "https://www.youtube.com/@{h}",
    "x": "https://x.com/{h}",
    "github": "https://github.com/{h}",
}
DEFAULT_SITES = ["youtube", "x"]  # add github for dev tools: --sites youtube,x,github
# Sites that block bots: we only print a manual-check link.
MANUAL_SITES = {
    "instagram": "https://www.instagram.com/{h}/",
    "linkedin": "https://www.linkedin.com/company/{h}/",
    "facebook": "https://www.facebook.com/{h}",
    "threads": "https://www.threads.net/@{h}",
}


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9-]", "", name.lower().replace(" ", ""))


def handle(name: str) -> str:
    return re.sub(r"[^a-z0-9_]", "", name.lower().replace(" ", ""))


def _status_once(url: str) -> int | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return None


def http_status(url: str, retries: int = 3) -> int | None:
    """GET with backoff on rate limits / server errors (registries throttle bursts)."""
    code = None
    for attempt in range(retries):
        code = _status_once(url)
        if code is not None and code != 429 and code < 500:
            return code
        time.sleep(1.5 * (attempt + 1))
    return code


PARKED_HINTS = ("/lander", "parking", "for sale", "buy this domain", "domain is for sale", "parked", "sedo", "dan.com",
                "afternic", "hugedomains", "godaddy", "this domain", "domain name", "is available")


def site_probe(d: str) -> dict:
    """For a taken domain: is there a live site, a parked/for-sale page, or nothing?"""
    req = urllib.request.Request(f"https://{d}", headers={"User-Agent": UA, "Accept": "text/html"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            html = r.read(60000).decode("utf-8", "ignore")
            final = r.geturl()
    except urllib.error.HTTPError as e:
        return {"site": f"http-{e.code}", "title": "", "final_url": ""}
    except Exception:
        return {"site": "no-site", "title": "", "final_url": ""}
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    title = re.sub(r"\s+", " ", m.group(1)).strip()[:90] if m else ""
    low = (title + " " + final).lower()
    host = urllib.parse.urlparse(final).hostname or ""
    if any(k in low for k in PARKED_HINTS):
        kind = "parked/for-sale"
    elif host and d not in host:
        kind = f"redirects to {host}"
    else:
        kind = "live"
    return {"site": kind, "title": title, "final_url": final}


def whois_status(d: str, server: str, marker: str) -> str:
    try:
        with socket.create_connection((server, 43), timeout=TIMEOUT) as sock:
            sock.sendall((d + "\r\n").encode())
            buf = b""
            while chunk := sock.recv(4096):
                buf += chunk
        text = buf.decode("utf-8", "ignore").lower()
    except Exception:
        return "unknown"
    if not text.strip():
        return "unknown"
    return "likely-free" if marker in text else "taken"


def check_domain(d: str, probe: bool = True) -> dict:
    tld = d.split(".", 1)[1]
    code = None
    if tld in WHOIS:
        status = whois_status(d, *WHOIS[tld])
    else:
        code = http_status(RDAP.get(tld, RDAP["default"]).format(d=d))
        status = "taken" if code == 200 else "likely-free" if code == 404 else "unknown"
        if status == "unknown" and tld in WHOIS_FALLBACK:
            status = whois_status(d, *WHOIS_FALLBACK[tld])
    out = {"type": "domain", "target": d, "status": status, "http": code,
           "manual": f"https://www.whois.com/whois/{d}"}
    if status == "taken" and probe:
        out.update(site_probe(d))
    return out


def youtube_meta(url: str, tries: int = 3) -> dict:
    """Channel name + bio for a taken YouTube handle. Retries: YouTube serves a bot page under parallel load."""
    for i in range(tries):
        m = _youtube_meta_once(url)
        if m.get("title"):
            return m
        time.sleep(2 * (i + 1))
    return {"title": "", "about": "", "note": "owner not readable: open the link"}


def _youtube_meta_once(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Cookie": "SOCS=CAI", "Accept-Language": "en"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            html = r.read(3_000_000).decode("utf-8", "ignore")  # og tags sit ~900 KB in
    except Exception:
        return {}
    t = re.search(r'<meta property="og:title" content="([^"]*)', html)
    d = re.search(r'<meta property="og:description" content="([^"]{0,140})', html)
    return {"title": (t.group(1) if t else "")[:60], "about": (d.group(1) if d else "").replace("\n", " ")[:90]}


def check_handle(site: str, h: str) -> dict:
    url = HANDLE_SITES[site].format(h=h)
    code = http_status(url)
    status = "taken" if code == 200 else "likely-free" if code == 404 else "unknown"
    out = {"type": "handle", "site": site, "target": h, "status": status, "http": code, "manual": url}
    if status == "taken" and site == "youtube":
        out.update(youtube_meta(url))
    return out


def manual_links(name: str) -> dict:
    q = urllib.parse.quote_plus(name)
    return {
        "IP India trade mark public search (wordmark + phonetic, per class)": "https://tmrsearch.ipindia.gov.in/tmrpublicsearch/",
        "MCA company/LLP name check (MCA Services > Check Company Name)": "https://www.mca.gov.in/",
        "Google exact match": f"https://www.google.com/search?q=%22{q}%22",
        "Google Maps (local businesses with this name)": f"https://www.google.com/maps/search/{q}",
        "Play Store": f"https://play.google.com/store/search?q={q}&c=apps",
        "Amazon.in brand search": f"https://www.amazon.in/s?k={q}",
        "Zauba Corp (company names)": f"https://www.zaubacorp.com/companysearchresults/{urllib.parse.quote(name)}",
    }


def run(name: str, tlds: list[str], delay: float, sites: list[str] | None = None, probe: bool = True) -> dict:
    s, h = slug(name), handle(name)
    out: dict = {"name": name, "slug": s, "handle": h, "results": [], "manual_handles": {}, "manual_checks": {}}
    for t in tlds:
        out["results"].append(check_domain(f"{s}.{t}", probe))
        time.sleep(delay)
    for site in (sites if sites is not None else DEFAULT_SITES):
        out["results"].append(check_handle(site, h))
        time.sleep(delay)
    out["manual_handles"] = {k: v.format(h=h) for k, v in MANUAL_SITES.items()}
    out["manual_checks"] = manual_links(name)
    return out


def render(r: dict) -> str:
    icon = {"likely-free": "✅", "taken": "❌", "unknown": "❔"}
    lines = [f"\n=== {r['name']}  (domain slug: {r['slug']}, handle: @{r['handle']}) ==="]
    for x in r["results"]:
        label = x["target"] if x["type"] == "domain" else f"{x['site']}: @{x['target']}"
        extra = ""
        if x.get("site") and x["type"] == "domain":
            extra = f"  → {x['site']}" + (f" | {x['title']}" if x.get("title") else "")
        lines.append(f"  {icon[x['status']]} {x['status']:<11} {label}{extra}")
    lines.append("  Check by hand (these sites block automated checks):")
    for k, v in r["manual_handles"].items():
        lines.append(f"    - {k}: {v}")
    lines.append("  Legal / market checks (manual):")
    for k, v in r["manual_checks"].items():
        lines.append(f"    - {k}: {v}")
    lines.append("  Note: 'likely-free' is a hint. Confirm at a registrar before you buy.")
    lines.append("  'taken' handles: open the link and check whether it is a SAME-CATEGORY brand (FAIL) or unrelated/dormant (WARN).")
    return "\n".join(lines)


def render_compact(r: dict) -> str:
    icon = {"likely-free": "✅", "taken": "❌", "unknown": "❔"}
    parts = []
    for x in r["results"]:
        tag = ""
        site = x.get("site", "")
        if x["type"] == "domain" and x["status"] == "taken" and site:
            tag = "(P)" if site.startswith("parked") else "(L)" if site == "live" else "(R)" if site.startswith("redirect") else "(-)"
        label = x["target"].split(".", 1)[1] if x["type"] == "domain" else x["site"]
        parts.append(f"{label}{icon[x['status']]}{tag}")
    line = f"{r['name']:<18} " + "  ".join(parts)
    owners = []
    for x in r["results"]:
        if x["status"] != "taken":
            continue
        if x["type"] == "domain" and x.get("site"):
            owners.append(f"{x['target']}: {x['site']}" + (f' "{x["title"][:50]}"' if x.get("title") else ""))
        elif x["type"] == "handle" and x.get("title"):
            owners.append(f"youtube: \"{x['title']}\"" + (f" ({x['about'][:60]})" if x.get("about") else ""))
        elif x["type"] == "handle" and x.get("note"):
            owners.append(f"youtube: {x['note']}: {x['manual']}")
    if owners:
        line += "\n" + "\n".join(f"{'':<19}↳ {o}" for o in owners)
    return line


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("names", nargs="+")
    ap.add_argument("--tlds", default="com,in,co.in", help="comma list, e.g. com,in,co.in,ai,io")
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between requests (be polite)")
    ap.add_argument("--sites", default=",".join(DEFAULT_SITES), help=f"handle sites to check: {','.join(HANDLE_SITES)}")
    ap.add_argument("--no-probe", action="store_true", help="skip fetching taken domains' landing pages")
    ap.add_argument("--compact", action="store_true", help="one line per name, no manual links")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    sites = [x.strip() for x in a.sites.split(",") if x.strip() in HANDLE_SITES]
    tlds = [t.strip().lstrip(".") for t in a.tlds.split(",") if t.strip()]
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=min(4, len(a.names))) as ex:
        results = list(ex.map(lambda n: run(n, tlds, a.delay, sites, not a.no_probe), a.names))
    if a.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    elif a.compact:
        for r in results:
            print(render_compact(r))
        print("\n✅ likely-free  ❌ taken  ❔ unknown  (P)=parked/for-sale  (L)=live site  (R)=redirects elsewhere  (-)=no site")
        print("↳ = who holds it. Same-category holder = FAIL, unrelated/parked/no-site = WARN.")
        print("X/Instagram/LinkedIn owners can't be read automatically: open the link and check by hand. Run without --compact for IP India / MCA links.")
    else:
        for r in results:
            print(render(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())

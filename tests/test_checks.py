"""Peyar acceptance checks: skill-content integrity + live availability against real brands.

Run:  python3 tests/test_checks.py            (all, needs internet)
      python3 tests/test_checks.py --offline  (skip live network checks)
Prints a table and writes tests/checks-result.json.
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "peyar"
REF = SKILL / "references"
sys.path.insert(0, str(SKILL / "scripts"))

import check_name  # noqa: E402
import score  # noqa: E402

CHECKS = []


def check(cid, title, live=False):
    def deco(fn):
        CHECKS.append((cid, title, live, fn))
        return fn
    return deco


def read(p):
    return Path(p).read_text(encoding="utf-8")


# ---------- Skill content integrity ----------

@check("C01", "Checklist has exactly 36 points, A1-F6")
def c01():
    ids = re.findall(r"^\| ([A-F][1-6]) \|", read(REF / "checklist-36.md"), re.M)
    expected = [f"{g}{n}" for g in "ABCDEF" for n in range(1, 7)]
    assert ids == expected, f"got {len(ids)}: {ids}"
    return "36/36 ids in order"


@check("C02", "Every checklist point carries a source tag [V] or [R]")
def c02():
    rows = [l for l in read(REF / "checklist-36.md").splitlines() if re.match(r"^\| [A-F][1-6] \|", l)]
    tags = [l.rstrip(" |").rsplit("|", 1)[-1].strip() for l in rows]
    bad = [r.split("|")[1].strip() for r, t in zip(rows, tags) if t not in ("V", "R")]
    assert not bad, f"untagged: {bad}"
    v = tags.count("V")
    return f"{v} from video [V], {len(tags) - v} research [R]"


@check("C03", "SKILL.md frontmatter valid; every referenced file exists")
def c03():
    s = read(SKILL / "SKILL.md")
    m = re.match(r"^---\nname: (\S+)\ndescription: (.+?)\n---\n", s, re.S)
    assert m and m.group(1) == "peyar", "bad frontmatter"
    assert len(m.group(2)) <= 1024, f"description {len(m.group(2))} chars"
    refs = set(re.findall(r"(references/[\w-]+\.md|scripts/[\w_]+\.py)", s))
    missing = [r for r in refs if not (SKILL / r).exists()]
    assert not missing, f"missing: {missing}"
    return f"{len(refs)} referenced files all present; description {len(m.group(2))} chars"


@check("C04", "Every industry playbook has Type/Norm/Works/Traps/Classes")
def c04():
    blocks = re.split(r"^### ", read(REF / "industry-playbooks.md"), flags=re.M)[1:]
    bad = [b.splitlines()[0] for b in blocks
           if not all(f"**{k}:**" in b for k in ("Type", "Norm", "Works", "Traps", "Classes"))]
    assert not bad, f"incomplete: {bad}"
    return f"{len(blocks)} playbooks complete"


@check("C05", "Legal reference covers MCA Rule 8B words, Emblems Act names, TM s.9/s.11")
def c05():
    s = read(REF / "legal-india.md")
    need = ["National", "Union", "Central", "Board", "Commission", "Authority", "Republic", "Federal",
            "Gandhi", "Nehru", "Shivaji", "s.9", "s.11", "University"]
    miss = [w for w in need if w not in s]
    assert not miss, f"missing: {miss}"
    return f"{len(need)} key legal terms present"


@check("C06", "Slang red-flag list covers >= 9 Indian languages")
def c06():
    s = read(REF / "indian-languages.md")
    langs = ["Hindi", "Tamil", "Telugu", "Kannada", "Malayalam", "Marathi", "Bengali", "Punjabi", "Urdu"]
    sec = s.split("Starter red-flag list", 1)[1].split("## 2.", 1)[0]
    miss = [l for l in langs if l not in sec]
    assert not miss, f"missing: {miss}"
    return f"{len(langs)} languages in red-flag table"


@check("C07", "Plugin manifest passes `claude plugin validate`")
def c07():
    try:
        r = subprocess.run(["claude", "plugin", "validate", str(ROOT)], capture_output=True, text=True, timeout=90)
    except FileNotFoundError:
        return "SKIP: claude CLI not installed"
    assert "Validation passed" in r.stdout + r.stderr, (r.stdout + r.stderr)[-300:]
    return "validation passed"


# ---------- Scorer behaviour on real Indian brands ----------

@check("C08", "Famous short Indian brands score >= 85 on sound")
def c08():
    names = ["Zomato", "Swiggy", "Amul", "Ola", "Zepto", "Nykaa", "Dabur", "Tanishq"]
    res = {n: score.analyse(n)["score"] for n in names}
    low = {n: s for n, s in res.items() if s < 85}
    assert not low, f"too low: {low}"
    return ", ".join(f"{n} {s}" for n, s in res.items())


@check("C09", "Long descriptive names score < 50 and rank below short brands")
def c09():
    long_ = ["Sri Lakshmi Premium Quality Jewellers", "Best Dental Care And Implant Centre", "Chennai Premium Quality Idli Company"]
    res = {n: score.analyse(n)["score"] for n in long_}
    hi = {n: s for n, s in res.items() if s >= 50}
    assert not hi, f"too high: {hi}"
    assert min(score.analyse(n)["score"] for n in ["Become", "Zepto"]) > max(res.values())
    return ", ".join(f"{s}" for s in res.values()) + " (all < 50)"


# ---------- Live availability against real registries ----------

@check("C10", "Live: .com of big Indian brands reported taken (zomato, amul, flipkart)", live=True)
def c10():
    out = {d: check_name.check_domain(d, probe=False)["status"] for d in ["zomato.com", "amul.com", "flipkart.com"]}
    assert all(v == "taken" for v in out.values()), out
    return "3/3 taken"


@check("C11", "Live: .in / .co.in via NIXI RDAP reported taken (nykaa.in, swiggy.in, tatamotors.co.in)", live=True)
def c11():
    out = {d: check_name.check_domain(d, probe=False)["status"] for d in ["nykaa.in", "swiggy.in", "tatamotors.co.in"]}
    assert all(v == "taken" for v in out.values()), out
    return "3/3 taken"


@check("C12", "Live: random strings free on all 5 TLDs (com, in, co.in, ai, io)", live=True)
def c12():
    rnd = f"pyrtst{int(time.time()) % 100000}qz"
    out = {t: check_name.check_domain(f"{rnd}.{t}", probe=False)["status"] for t in ["com", "in", "co.in", "ai", "io"]}
    assert all(v == "likely-free" for v in out.values()), out
    return f"{rnd}: 5/5 likely-free"


@check("C13", "Live: .io WHOIS regression - google.io taken, not falsely free", live=True)
def c13():
    st = check_name.check_domain("google.io", probe=False)["status"]
    assert st == "taken", st
    return "google.io taken"


@check("C14", "Live: handles - @zomato taken on YouTube and X; random handle free", live=True)
def c14():
    taken = {s: check_name.check_handle(s, "zomato")["status"] for s in ["youtube", "x"]}
    free = {s: check_name.check_handle(s, "pyrtstzz90871")["status"] for s in ["youtube", "x"]}
    assert all(v == "taken" for v in taken.values()), taken
    assert all(v == "likely-free" for v in free.values()), free
    return "taken 2/2, free 2/2"


@check("C15", "Live: site probe labels zomato.com as live; --compact and --json outputs well-formed", live=True)
def c15():
    p = check_name.check_domain("zomato.com", probe=True)
    assert p.get("site") in ("live",) or p.get("site", "").startswith("redirects"), p
    script = SKILL / "scripts" / "check_name.py"
    r = subprocess.run([sys.executable, str(script), "zomato", "--compact", "--delay", "0.3", "--no-probe"],
                       capture_output=True, text=True, timeout=120)
    assert r.stdout.startswith("zomato") and "com❌" in r.stdout, r.stdout[:200]
    j = subprocess.run([sys.executable, str(script), "amul", "--json", "--delay", "0.3", "--no-probe", "--tlds", "com"],
                       capture_output=True, text=True, timeout=120)
    data = json.loads(j.stdout)
    assert data[0]["name"] == "amul" and data[0]["results"][0]["status"] == "taken"
    return f"probe: {p['site']} ('{p.get('title', '')[:40]}'); compact + json OK"


@check("C17", "Name-reach quotas + alphanumeric guide present (names not India-only by default)")
def c17():
    sk = read(SKILL / "SKILL.md"); nm = read(REF / "naming-methods.md")
    assert "Default = mix" in sk and "Alphanumeric is always in the pool" in sk and "Finalist spread" in sk
    pats = re.findall(r"^\| \*\*(.+?)\*\* \|", nm.split("## Alphanumeric names", 1)[1].split("## Global-neutral", 1)[0], re.M)
    assert len(pats) >= 6, pats
    return f"mix default + quotas + {len(pats)} alphanumeric patterns"


@check("C16", "Live: taken YouTube handle shows owner name (who holds @zomato)", live=True)
def c16():
    r = check_name.check_handle("youtube", "zomato")
    assert r["status"] == "taken" and "zomato" in r.get("title", "").lower(), r
    return f'owner: "{r["title"]}"'


def main():
    offline = "--offline" in sys.argv
    rows, fails = [], 0
    for cid, title, live, fn in CHECKS:
        if live and offline:
            rows.append((cid, title, "SKIP", "offline"))
            continue
        t0 = time.time()
        try:
            detail = fn()
            status = "SKIP" if str(detail).startswith("SKIP") else "PASS"
        except AssertionError as e:
            status, detail = "FAIL", str(e)
            fails += 1
        except Exception as e:  # network etc.
            status, detail = "ERROR", f"{type(e).__name__}: {e}"
            fails += 1
        rows.append((cid, title, status, f"{detail} [{time.time() - t0:.1f}s]"))
    for r in rows:
        print(f"{r[0]}  {r[2]:<5}  {r[1]}\n         {r[3]}")
    (ROOT / "tests" / "checks-result.json").write_text(json.dumps(
        [dict(zip(("id", "title", "status", "detail"), r)) for r in rows], indent=2, ensure_ascii=False))
    print(f"\n{sum(r[2] == 'PASS' for r in rows)}/{len(rows)} passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

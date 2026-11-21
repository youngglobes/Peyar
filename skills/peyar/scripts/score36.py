#!/usr/bin/env python3
"""Compute the Peyar 36-point checklist score from per-point letters.

Letters: P=PASS(2) W=WARN(1) F=FAIL(0) U=UNVERIFIED (excluded) N=N-A (excluded)

Usage (36 letters, groups A-F, spaces/pipes ignored):
    python3 score36.py Mullai "PPWPPP PPWPWP PWPPPW UPWUPP WWUWPW PPPPUU"
    python3 score36.py --json Mullai "<36 letters>" Kuyil "<36 letters>"
Output: score as "N (k unverified)", group subtotals, D-group verdict, weakest points.
"""
from __future__ import annotations

import json
import re
import sys

POINTS = {"P": 2, "W": 1, "F": 0}
GROUPS = "ABCDEF"


def parse(letters: str) -> list[str]:
    s = re.sub(r"[\s|,/-]", "", letters.upper())
    if len(s) != 36 or set(s) - set("PWFUN"):
        raise ValueError(f"need exactly 36 letters from P/W/F/U/N, got {len(s)}: {s!r}")
    return list(s)


def compute(name: str, letters: str) -> dict:
    v = parse(letters)
    ids = [f"{g}{n}" for g in GROUPS for n in range(1, 7)]
    scored = [(i, x) for i, x in zip(ids, v) if x in POINTS]
    earned = sum(POINTS[x] for _, x in scored)
    possible = 2 * len(scored)
    unverified = sum(x == "U" for x in v)
    groups = {}
    for gi, g in enumerate(GROUPS):
        chunk = v[gi * 6:(gi + 1) * 6]
        sc = [x for x in chunk if x in POINTS]
        groups[g] = {"letters": "".join(chunk), "earned": sum(POINTS[x] for x in sc), "possible": 2 * len(sc),
                     "unverified": chunk.count("U")}
    d_fail = [i for i, x in zip(ids, v) if i.startswith("D") and x == "F"]
    score = round(100 * earned / possible) if possible else 0
    return {
        "name": name,
        "score": score,
        "unverified": unverified,
        "display": f"{score} ({unverified} unverified)",
        "verdict": "OUT (D-group FAIL: " + ", ".join(d_fail) + ")" if d_fail
        else "strong" if score >= 80 else "workable" if score >= 65 else "rework",
        "fails": [i for i, x in zip(ids, v) if x == "F"],
        "warns": [i for i, x in zip(ids, v) if x == "W"],
        "groups": groups,
    }


def main(argv: list[str]) -> int:
    as_json = "--json" in argv
    args = [a for a in argv if a != "--json"]
    if len(args) < 2 or len(args) % 2:
        print(__doc__)
        return 2
    res = [compute(args[i], args[i + 1]) for i in range(0, len(args), 2)]
    if as_json:
        print(json.dumps(res, indent=2))
        return 0
    for r in res:
        gs = "  ".join(f"{g}:{d['earned']}/{d['possible']}" + (f"+{d['unverified']}U" if d["unverified"] else "")
                       for g, d in r["groups"].items())
        print(f"{r['name']:<18} {r['display']:<18} {r['verdict']}")
        print(f"{'':<19}{gs}")
        if r["groups"]["D"]["unverified"]:
            print(f"{'':<19}⚠ legal group has {r['groups']['D']['unverified']} unverified point(s): not legally cleared")
        if r["fails"] or r["warns"]:
            print(f"{'':<19}FAIL: {', '.join(r['fails']) or '-'}   WARN: {', '.join(r['warns']) or '-'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

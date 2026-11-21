#!/usr/bin/env python3
"""Peyar sound-and-spelling scorer for brand name candidates.

Heuristic only. It approximates checklist points B1-B4 and F2 so that a long
candidate list can be cut down quickly. It does NOT judge meaning, legal risk
or availability.

Usage:
    python3 score.py Become "Frozen Iris" Zepto
    python3 score.py --json Become Zepto
"""
from __future__ import annotations

import argparse
import json
import re
import sys

VOWELS = set("aeiouy")
OPEN_VOWEL_SOUNDS = ("a", "o", "aa", "oo", "u")

# Spellings that split the way people type or say the name (checklist B4).
AMBIGUOUS = [
    (r"ph", "ph/f: people may spell it with an f"),
    (r"(?<![aeiou])y(?=[aeiou])|(?<=[aeiou])y(?![aeiou])", "y as a vowel or consonant: unclear"),
    (r"([bcdfgklmnprstz])\1", "double letter: often typed single"),
    (r"q(?!u)", "q without u: unusual"),
    (r"ee|ea|ie|ei", "ee/ea/ie/ei: people can't tell which spelling"),
    (r"ck|kh|gh", "ck/kh/gh: spelling ambiguity"),
    (r"x", "x: ks/z/sh pronunciation varies"),
    (r"c(?=[eiy])", "soft c: may be read as k or spelt with s"),
    (r"^(kn|ps|wr|gn)", "silent first letter"),
]

# Sound mergers in Indian English (checklist B3).
INDIAN_ACCENT_TRAPS = [
    (r"w|v", "v/w: these merge in many Indian accents"),
    (r"z", "z/j: often said as j"),
    (r"th", "th: said as t or d"),
    (r"^(st|sk|sp|sm|sn|sl)", "initial s-cluster: often gets a vowel added in front (istation)"),
    (r"sh", "sh/s: these merge in parts of East India"),
    (r"f", "f/ph/p: drifts in some regions"),
]

CONFUSABLE_GLYPHS = re.compile(r"rn|vv|cl|l1|0o|o0")
# 3-consonant runs that are normal in English and Indian-English speech.
OK_CLUSTERS = {"str", "spl", "spr", "scr", "nch", "tch", "ght", "nst", "rst", "nds", "nts", "ndl",
               "ckl", "mpl", "mbl", "ngl", "nkl", "rtl", "stl", "thr", "shr", "chr", "phr", "sch",
               "nth", "rth", "lth", "ngs", "nks", "rch", "lch", "rds", "rks", "lks"}
HIATUS = re.compile(r"i[aou]|eo|ua|uo")


def syllables(word: str) -> int:
    """Rough English syllable count, good enough to rank names."""
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    w = re.sub(r"y(?=[aeiou])", "j", w)  # y before a vowel is a consonant (Peyar = pe-yar)
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups) + sum(len(HIATUS.findall(g)) for g in groups)  # Lekhio = lek-hi-o
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and n > 1:
        n -= 1  # silent final e
    return max(n, 1)


def analyse(name: str) -> dict:
    raw = name.strip()
    letters = re.sub(r"[^a-zA-Z]", "", raw).lower()
    words = re.findall(r"[A-Za-z]+", raw)
    syl = sum(syllables(w) for w in words) + len(re.findall(r"\d", raw))
    vowel_ratio = (sum(c in VOWELS for c in letters) / len(letters)) if letters else 0
    flags: list[str] = []
    score = 100

    # B1 syllables
    if syl <= 2:
        pass
    elif syl == 3:
        score -= 5
    elif syl == 4:
        score -= 15
        flags.append(f"{syl} syllables: harder to remember")
    else:
        score -= 30
        flags.append(f"{syl} syllables: too long to remember")

    # F2 length / wordmark
    L = len(letters)
    if L > 12:
        score -= 20
        flags.append(f"{L} letters: long wordmark, weak at icon size")
    elif L > 8:
        score -= 8
        flags.append(f"{L} letters: medium-long")
    if len(words) > 2:
        score -= 10
        flags.append(f"{len(words)} words: people will shorten it themselves")

    # B4 spelling ambiguity
    for pat, msg in AMBIGUOUS:
        if re.search(pat, letters):
            score -= 6
            flags.append(msg)

    # B3 Indian accent traps (lighter penalty: they are traps, not fatal)
    for pat, msg in INDIAN_ACCENT_TRAPS:
        if re.search(pat, letters):
            score -= 3
            flags.append(msg)

    dedup = re.sub(r"(.)\1", r"\1", letters)  # Pebble -> peble
    # Romanised digraphs are ONE sound in Indian languages (Tanishq, Bhakti, Khadi): count them once.
    dedup = re.sub(r"(sh|ch|th|ph|kh|gh|bh|dh|jh|zh)", "C", dedup)
    clusters = [c for c in re.findall(r"[bcdfghjklmnpqrstvwxzC]{3,}", dedup)
                if len(c) > 3 or (c not in OK_CLUSTERS and not re.fullmatch(r"[bcdfgkpt][lr].|.[bcdfgkpt][lr]", c))]
    if clusters:
        score -= 10
        flags.append("3+ consonant cluster: hard to say across Indian languages")
    if CONFUSABLE_GLYPHS.search(letters):
        score -= 4
        flags.append("letter shapes confusable in a logo (rn/m, l/1, ...)")
    if re.search(r"\d", raw):
        flags.append("alphanumeric: make sure the number means something and is easy to say aloud")

    # B2 vowel feel (informational, no penalty)
    if vowel_ratio >= 0.45:
        feel = "light/open (premium, soft)"
    elif vowel_ratio <= 0.28:
        feel = "hard/dense (strong, techy), but check that it is pronounceable"
        if vowel_ratio < 0.2 and L > 4:
            score -= 10
            flags.append("very few vowels: hard to pronounce")
    else:
        feel = "balanced"
    ends_vowel = bool(letters) and letters[-1] in VOWELS

    return {
        "name": raw,
        "score": max(0, min(100, score)),
        "syllables": syl,
        "letters": L,
        "vowel_ratio": round(vowel_ratio, 2),
        "sound_feel": feel,
        "ends_in_vowel": ends_vowel,
        "flags": flags,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("names", nargs="+")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    res = sorted((analyse(n) for n in a.names), key=lambda r: -r["score"])
    if a.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0
    for r in res:
        print(f"{r['score']:>3}  {r['name']}  [{r['syllables']} syl, {r['letters']} letters, {r['sound_feel']}]")
        for f in r["flags"]:
            print(f"       - {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Peyar test report

**Latest:** v3 (2026-11-21) · **Rounds:** v1 baseline → v2 (6 fixes) → v3 (global/alphanumeric mix)

## Summary across rounds

| Metric | v1 | v2 | v3 |
|---|---|---|---|
| Automated checks | 15/15 | 16/16 | **17/17** |
| Unit tests | 13/13 | 16/16 | **16/16** |
| Graded skill runs (avg /10)* | 9.4 | 8.8 | — (mix test, see below) |
| Founder trap names caught | 5/5 | 5/5 | — |
| Top-pick quality (/5) | 3.2 | **4.0** | — |
| 36-pt scores correct vs recompute | 2 slips | **24/24** | script-computed |
| Availability errors vs recheck | 0 | 0 | 0 |
| Finalists that are global-neutral or alphanumeric | ~0% | **0/24** | **12/15 (80%)** |

*v2 was graded on a stricter rubric: R5–R7 now require the new candidate list, survivors table and pasted score36 output, so its total isn't directly comparable to v1. The quality and accuracy metrics did improve.

---

## v3: global / alphanumeric mix (2026-11-21)

**Why:** in v2, all 24 finalists were Indian-language words. Causes: the test briefs invited Indian languages, the skill *required* an Indian-language method with no quota for global names, and the examples were India-heavy.

**Fix:** a name-reach intake item (global-neutral / India-rooted / **mix by default**), method quotas (≥50% global-neutral, ≥3 alphanumeric under mix), a finalist-spread rule (≥3 methods, ≥2 global-neutral) and a new alphanumeric guide with 7 patterns.

**Test:** 3 new briefs that say nothing about language.

| Run | Finalists (method) | Global/alnum share |
|---|---|---|
| Cold brew, Bengaluru | Jetbrew (compound), Coldfuse (compound), Vega (Sanskrit), **560 Cold** (alnum: PIN prefix), Kovo (coined) | 4/5 |
| EV charging, Hyderabad | Kilovo (coined), **Amp23** (alnum: 2W+3W), **Volt78** (alnum: 78°E meridian), Zaptu (coined), Plugwala (Hinglish) | 4/5 |
| Pet food, Mumbai | Tailpot (compound), **Tail91** (alnum: +91), Ladle (English), Larder (English), Katori (Hindi) | 4/5 |

The availability recheck (`tests/runs-v3/_recheck.txt`) matches the runs' claims. India-rooted names still appear (3/15) wherever they fit, as intended for "mix".

### v2 → v3 fixes also applied
- `score36.py`: per-group unverified counts (`D:8/8+2U`) and a "legal group not cleared" warning.
- `check_name.py`: YouTube owner names on taken handles (with retry under load); parked "/lander" pages detected; retry/backoff + WHOIS fallback for throttled registries.
- SKILL.md: survivors table, fit gate, honest "reserve (not screened)" bucket, verbatim score36 output, cells copied from script output, no tool jargon in the founder-facing deliverable, flag-based sound cut, "crowded word" cut.
- Checklist: "cure"/"University"/"Bank" are always FAIL under D6; Emblems Act surname case is WARN-verify; holder-aware E1/E2.

### Known limitations (still open)
- X, Instagram and LinkedIn owners can't be read automatically. Check by hand.
- Web search is weak for small Indian businesses: "no results" ≠ free name. The registry checks remain the real test.
- IP India and MCA have captchas, so D1/D4 stay UNVERIFIED until the founder runs them.
- Most finalists land within 5 points (many points are unverifiable), so the final ranking is judgement guided by the tie-break order.

---

## v2: 6 fixes retest (graded)

| Run | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | Total | Top pick | Quality |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jewellery | 1 | 1 | 1 | 1 | 1 | 0.5 | 0.5 | 1 | 1 | 1 | 9.0 | Aabha | 3.5 |
| Ayurveda | 1 | 1 | 1 | 1 | 1 | 0.5 | 0.5 | 1 | 1 | 0.5 | 8.5 | Nilavu | 4 |
| Cafe | 1 | 1 | 1 | 1 | 1 | 0.5 | 1 | 1 | 1 | 0.5 | 9.0 | Chaigiri | 4 |
| Edtech | 1 | 1 | 1 | 1 | 1 | 0.5 | 0.5 | 1 | 1 | 0.5 | 8.5 | Hausla | 4.5 |
| Streetwear | 1 | 1 | 1 | 1 | 1 | 1 | 0.5 | 1 | 1 | 0.5 | 9.0 | Tashan | 4 |

The grader recomputed every 36-point score with score36.py, and all 24 finalists plus the 5 founder names match. The remaining deductions (taste cuts, partial score36 paste, tool jargon in deliverables) were fixed in v3's SKILL.md.

---

# v1 baseline (2026-11-20)


**Date:** 2026-11-20 · **Version:** 0.1.0 (plus fixes made during testing) · **Tests:** 20 = 15 automated checks + 5 graded end-to-end skill runs

## Summary

| Suite | Result |
|---|---|
| Automated checks (C01–C15) | **15 / 15 pass** (after 2 bugs found and fixed) |
| Unit tests (`tests/test_score.py`) | **13 / 13 pass** |
| Skill runs (5 industries, graded /10 by an independent agent) | **avg 9.4 / 10** (9.0 – 9.5) |
| Trap names caught (founder's bad name planted in every brief) | **5 / 5** |
| Availability claims contradicted by recheck | **0** |
| Average top-pick quality (grader judgement) | **3.2 / 5**, the main weakness |

---

## Part 1: Automated checks (`tests/test_checks.py`)

Run: `python3 tests/test_checks.py` (live) or `--offline`. Results are in `tests/checks-result.json`.

| ID | Check | Result | Detail |
|---|---|---|---|
| C01 | Checklist has exactly 36 points, A1–F6 | ✅ PASS | 36/36 in order |
| C02 | Every point tagged [V] video / [R] research | ✅ PASS | 19 [V], 17 [R] |
| C03 | SKILL.md frontmatter valid; referenced files exist | ✅ PASS | 7/7 files; description 595 chars |
| C04 | Every industry playbook complete (Type/Norm/Works/Traps/Classes) | ✅ PASS | 17 playbooks |
| C05 | Legal ref covers Rule 8B words, Emblems Act, TM s.9/s.11, "University" | ✅ PASS | 14/14 terms |
| C06 | Slang red-flag list covers ≥9 languages | ✅ PASS | 9 |
| C07 | `claude plugin validate` | ✅ PASS | |
| C08 | Famous short brands (Zomato, Swiggy, Amul, Ola, Zepto, Nykaa, Dabur, Tanishq) score ≥85 | ✅ PASS* | *First run FAILED: Tanishq scored 81 |
| C09 | Long descriptive names score <50 | ✅ PASS | 18, 18, 28 |
| C10 | Live: zomato.com, amul.com, flipkart.com → taken | ✅ PASS | 3/3 |
| C11 | Live: nykaa.in, swiggy.in, tatamotors.co.in → taken (NIXI) | ✅ PASS* | *Second run FAILED: registry throttled |
| C12 | Live: random string free on .com/.in/.co.in/.ai/.io | ✅ PASS* | *Second run FAILED: same throttling |
| C13 | Live: google.io → taken (regression for the old .io false-free bug) | ✅ PASS | |
| C14 | Live: @zomato taken on YouTube + X; random handle free | ✅ PASS | 2/2 + 2/2 |
| C15 | Live: zomato.com probed as live site; `--compact` / `--json` output well-formed | ✅ PASS | |

### Bugs the checks found (both fixed)

1. **Romanised Indian digraphs were counted as consonant clusters.** In "Tanishq", "shq" was flagged as hard to say. This would wrongly penalise many regional names (Bhakti, Khadi, Dhruv). **Fix:** sh/ch/th/ph/kh/gh/bh/dh/jh/zh now count as one sound. A regression test was added.
2. **The NIXI .in registry throttles bursts**, so results came back "unknown" while 5 agents checked in parallel. **Fix:** the script now retries with backoff on 429/5xx, then falls back to WHOIS (`whois.nixiregistry.in`, Verisign for .com). After the fix, a recheck of all 24 finalists returned **zero unknowns**.

---

## Part 2: End-to-end skill runs (`tests/runs/`)

Each brief named a different industry and city, and included a **founder's favourite name with a hidden legal trap**. A fresh agent ran the skill using only `SKILL.md`. A separate agent graded each run on 10 criteria and compared every finalist's availability against an independent recheck (`tests/runs/_recheck.txt`).

### Trap results: 5 / 5 caught

| Run | Founder's name | Expected catch | Peyar verdict |
|---|---|---|---|
| Jewellery, Madurai | National Gold House | MCA Rule 8B "National" + descriptive | ❌ Rejected: D4 FAIL (8B) + D3 FAIL (descriptive), 61/100 |
| Ayurveda, Kerala | CureVeda | "Cure" claim (Drugs & Magic Remedies) | ❌ Rejected: an existing same-category brand found (D1 FAIL); "cure" flagged D6 WARN (should be FAIL) |
| Chai cafe, Pune | Gandhi Chai Adda | Emblems & Names Act | ❌ Rejected: D5 FAIL, with an honest hedge on the exact Schedule wording |
| Govt-exam edtech | Bharat Digital University | "University" restricted (UGC Act s.23) | ❌ Rejected: D6 FAIL + D3 FAIL, 59/100 |
| Streetwear, Delhi | Adidesi | Too close to the well-known mark Adidas (s.11) | ❌ Rejected: D2 FAIL, plus B6/E6 |

### Scores (each criterion is worth 1 point)

| Run | Trap | Assump. | Brand type | Norm scan | ≥25 cands, ≥5 methods | Cut log | Scripts run | Availability accurate | 36-pt rules | Format | **Total** | Top pick | Quality |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jewellery | 1 | 1 | 1 | 1 | 0.5 | 0.5 | 1 | 1 | 1 | 1 | **9.0** | Mullai | 4/5 |
| Ayurveda | 1 | 1 | 1 | 1 | 1 | 0.5 | 1 | 1 | 1 | 1 | **9.5** | Kuliru | 3/5 |
| Cafe | 1 | 1 | 1 | 1 | 1 | 0.5 | 1 | 1 | 1 | 1 | **9.5** | Chahatra | 3/5 |
| Edtech | 1 | 1 | 1 | 1 | 1 | 0.5 | 1 | 1 | 1 | 1 | **9.5** | Ummeed | 3/5 |
| Streetwear | 1 | 1 | 1 | 1 | 1 | 0.5 | 1 | 1 | 1 | 1 | **9.5** | Tapori | 3/5 |

Runs produced 34–43 candidates each, across 6–8 methods. Each included a regional-language method: Tamil, Malayalam, Marathi, Hindi and Punjabi.

### What worked
- **Legal screening is the strongest part.** Every trap was caught, with the correct statute, and the runs hedged where they couldn't verify.
- **Meaning screening caught real issues.** For example, Tamil "thanal" = embers, Finnish "kalma" = death, Kuyil/"koyil" and Arumbu/"erumbu" near-homophones.
- **No hallucinated availability.** Every claim was consistent with the recheck.
- **The UNVERIFIED discipline held.** D1/D4 were never marked PASS without a registry search.

### What didn't
- **Cut log (0.5 in every run).** No run showed the required 8–10 survivor table. Some cuts were "from knowledge" instead of a search, and some had no reason logged.
- **Top-pick quality averages 3.2/5.** Weak picks included:
  - "Tapori": Mumbai slang for a Delhi brand.
  - "Ummeed": generic, with every domain taken.
  - "Chahatra": needs a descriptor.

  The process is sound, but the final taste and fit judgement is thin.
- **Hand-computed 36-point scores.** There was a 2-point arithmetic slip on 2 names (ayurveda run).
- **Owners of taken domains and handles are unknown.** No run could tell whether a taken handle belonged to a same-category business.
- **Score clustering.** Finalists land at 78–89, so the tie-break rule decides most rankings.

### Recommended fixes (not yet applied)

| # | Fix | Impact |
|---|---|---|
| 1 | Require a `## Survivors` table in step 4 (name, meaning, one search hit, sound, domains), and ban "from knowledge" as an existing-use reason | Fixes the cut-log gap in every run |
| 2 | Add a step-5 **"founder on stage" fit gate**: does the name fit the brief's city, tone and audience? Reject if not | Raises pick quality |
| 3 | Add `score36.py`: P/W/F/U/N letters → "N (k unverified)" | Removes arithmetic errors |
| 4 | `check_name.py`: print the page/handle title for taken items in compact mode | Lets runs judge same-category vs unrelated |
| 5 | Make "cure"/disease claims D6 **FAIL** (not WARN) for supplements and ayurveda | Matches legal-india.md |
| 6 | Make `## Candidates (by method)` a required output section | Makes R5 verifiable |

---

## Reproduce

```bash
python3 tests/test_score.py           # 13 unit tests
python3 tests/test_checks.py          # 15 acceptance checks (needs internet)
python3 tests/test_checks.py --offline
```
The skill runs are in `tests/runs/*.md`. The availability recheck is in `tests/runs/_recheck.txt`.

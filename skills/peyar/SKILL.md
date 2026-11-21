---
name: peyar
description: Name an Indian brand, product, startup, shop, clinic or app the way branding studios do. Covers intake, category-norm scan, generation across 12 naming methods (including regional Indian languages), a sound/spelling score, and a 36-point checklist (strategy, sound, meaning in 11 Indian languages, IP India trade mark, MCA Rule 8/8A/8B, Emblems Act, domains/handles, execution). It also checks live .com/.in/.ai domain and handle availability. Use when someone asks to name or rename a brand, company or product, check whether a brand name is good, or compare name options, especially for India.
---

# Peyar (பெயர், "name")

Brand naming for India, inspired by Harish Venkatesh's naming talk on the Nuke It podcast. **"Name is your perennial ad."** Renaming later costs you legally, operationally and emotionally, so get it right now.

`SKILL_DIR` = the folder this file is in. Scripts need only Python 3.9+ (stdlib).

## Workflow

### 1. Intake
If the user gave a full brief, **don't ask**. List your assumptions in 3–5 bullets and go to step 2. Otherwise, ask once, in ONE message, only for what's missing:
1. What you sell, and to whom
2. Industry and sub-category
3. Start location, and where you'll sell in 5 years (state / pan-India / global)
4. Price tier
5. Tone (trustworthy, premium, playful, bold, warm, techy)
6. **Name reach**: *global-neutral* (works anywhere, no Indian context needed), *India-rooted* (proudly Indian words), or *mix*. **Default = mix** unless the user says otherwise. Plus any languages to draw from or avoid
7. Must-have or must-avoid words
8. Hard constraints: is a .com/.ai **required** or just nice? Founder name okay? Numerology?

### 2. Strategy (`references/brand-types.md`, `references/industry-playbooks.md`)
- Classify the brand as **search, experience or credence**, and say what job the name must do.
- **Category-norm scan:** 8–10 real competitor names (web search if available; otherwise use the playbook and say so). State the norm in one sentence.
- Decide **inside the norm** or **contrarian**, and why. Then write a 2–3 line **naming brief** (idea, feel, sound, no-go zones).

### 3. Generate (`references/naming-methods.md`)
- **25–40 candidates** across **≥5 methods**, grouped by method, with a 3–6 word rationale each.
- **Method mix by name reach.** "Global-neutral" methods = real word, compound, coined, alphanumeric, evocative, acronym. "India-rooted" methods = regional language, Sanskrit/classical, Hinglish.

  | Reach | Global-neutral share | India-rooted share | Alphanumeric |
  |---|---|---|---|
  | mix (default) | ≥50% | ≤50% | ≥3 candidates |
  | global-neutral | ≥85% | ≤15% (only if easy to say worldwide) | ≥4 candidates |
  | India-rooted | ≥25% | ≤75% | ≥2 candidates |

- **Alphanumeric is always in the pool.** Read the alphanumeric section of `naming-methods.md` and build names with **meaningful** numbers or letters for the industry (dial code 91, coordinates, founding year, pin code, a spec/model number, a count like 99 or 1mg).
- Inviting a language in the brief ("Tamil welcome") **allows** it. It does not make it the default. Keep the quota unless the user asks for India-rooted names.
- Never make an abstract claim word (quality, best, premium, world-class) the core of a name.

### 4. Screen and cut to 8–10. Cut in this order and log the reason for every cut
Every cut needs **evidence**: a search result, script output or a stated meaning. "From my knowledge" or "weaker story" is **not** a valid reason at this step (taste comes in step 5).
1. **Meaning / slang** (`references/indian-languages.md`): full word, halves and sub-strings. Output a mini table: `name | languages checked | concern | confidence`, and list the languages you can't vouch for.
2. **Descriptive / generic (D3):** the plain word for the product or ingredient in that category (for example "Thinai" for millet snacks, "Nalam" for a clinic). Usually can't be trade marked, and it is crowded.
3. **Existing use:** one web search per survivor ("<name> <category> India"), plus the domain-holder lines (↳) from `check_name.py`. Drop it if a same-category business already uses the name. Also drop it (reason: "crowded word") if the exact .com **and** .in are both held by **live** businesses of any category **and** the word is a common dictionary word. You'll never own its search results. Note that web search is weak for small Indian businesses, so **no results is weak evidence** of a free name. Say so, and lean on the registry checks in step 6.
4. **Sound:** run `python3 SKILL_DIR/scripts/score.py <names>`. Most real names score 85+, so **cut on the flags, not just the number**: drop a name if it scores under 75, **or** has 2+ spelling/accent flags, **or** has a "consonant cluster" / "very few vowels" flag. The score measures sound and spelling only. It says nothing about meaning or availability, and long founder-name formats ("Dr X Dental Care") score low by design, so judge those on the norm instead.
5. **If a domain is a HARD constraint:** run `check_name.py --compact --no-probe` on the ~15–20 survivors **now**, and keep only those that pass.
- **Reserve bucket:** once you have ≥8 evidence-backed survivors, any candidates you didn't screen go in a `Reserve (not screened)` line. That is honest: never present them as cuts, and never write "taste cut" or "weaker story" at this step.
- **Write the `## Survivors` table (required, 8–10 rows)** before picking finalists:
  `| Name | Method | Meaning screen (langs, concern, confidence) | Existing-use evidence (search/↳ result) | Sound | .com/.in |`
- **If fewer than 5 survive:** generate 10–15 more using the methods that survived best (or with modifiers: get-, -hq, -labs, -foods, a place suffix), then re-screen. Say that you looped.

### 5. Deep check: top 4–5 only
- **Finalist spread (required):** the 4–5 finalists span **≥3 methods**. Under *mix* or *global-neutral* reach, include **≥2 global-neutral names**, and at least one alphanumeric name if any survived. If none survived, say why in one line.
- **Fit gate first.** For each survivor ask: "Would this founder say it on stage, in this city, to this audience, without explaining it?" Check the brief's **city/region** (no Mumbai slang for a Delhi brand), **tone**, **audience** and **price tier**. Reject failures in one line each. Then pick the 4–5 finalists.
- Run `python3 SKILL_DIR/scripts/check_name.py <names> --compact --tlds com,in,co.in` (tech: `com,in,ai,io`; add `--sites youtube,x,github` for developer tools). For taken domains, the probe shows live (L), parked/for-sale (P), redirect (R) or no site (-). Parked or no-site domains = WARN, not FAIL.
- For every taken handle, open it and decide: same-category brand = FAIL, unrelated or dormant = WARN.
- Score **all 36 points** in `references/checklist-36.md` for each finalist. Use **UNVERIFIED** for anything you couldn't check live: IP India, MCA and Instagram are always UNVERIFIED unless the user pastes results. UNVERIFIED is excluded from the score and counted separately. **D1 and D4 can never be PASS without a live registry search.**
- Compute scores with `python3 SKILL_DIR/scripts/score36.py <Name> "<36 letters P/W/F/U/N>" ...` for **all finalists plus the founder's own name in one call**. **Never add them up by hand.** Paste the **full output verbatim in one fenced code block** under the ranking table.
- Fill the domain/handle cells by **copying `check_name.py --compact` output**, not by retyping. Run it with `--sites youtube,x` and use the ↳ lines for holder notes.
- Any D-group **FAIL** removes the name.
- **Ranking is judgement, informed by the evidence.** Scores within 5 points are a tie. Break ties in this order: lower legal risk → stronger story/positioning → better availability → better recall and sound.

### 6. Deliver (use this exact structure)

```
## Assumptions            (only if you didn't ask)
## Naming brief
<brand type · category norm · inside/contrarian · feel>

## Candidates (by method)        (all 25–40, grouped by method, 3–6 word rationale each)

## Survivors                     (the step-4 table, 8–10 rows, then one line per fit-gate rejection)

## Top 3–5 names (ranked)
| Rank | Name | Method | Why it works | Checklist /100 (n unverified, from score36.py) | Sound /100 | .com | .in | .co.in or .ai | YouTube | X |
Cell format for domains/handles: ✅ free · ❌ live · ❌P parked/for-sale · ❌- no site · ❔ unknown

### 1. <Name>
- Pronunciation: <respelling, e.g. PAY-yar> · Scripts: <Tamil / Devanagari forms>
- Story: <one line the founder can say on stage>
- Scorecard:
  | Group | Points (P/W/F/U/N) | Key evidence |
  | A Strategy | A1 P · A2 P · A3 W · ... | ... |
  ... one row per group A–F
- Weakest 3 points and how to fix them:

## Also considered (cut and why)
<one line each, grouped by the reason cut>

## Next steps
1. Native-speaker check: top 3 names to 1 person per target language
2. 5-second recall test with 10–20 target buyers (script below)
3. IP India search in classes <N, N> → TM agent's opinion → file TM-A
4. Reserve the company name on MCA (SPICe+ Part A / RUN)
5. Buy domains and claim handles the same day
Expect weeks, not days. Unhype took a studio ~3 months (strategy → shortlist → market test → TM → multi-geography → stakeholder sign-off).
```

**Recall test script:** show each name for 5 seconds, talk about something else for 2 minutes, then ask: "Which names do you remember? Spell one. What do you think it sells?" Recall + correct spelling + right category guess wins.

End with: *Peyar gives heuristics, not legal advice. Have a registered trade mark agent confirm before filing.*

## Rules
- Every heuristic is a **hypothesis** (vowels feel premium, short names aid recall). The market test decides.
- Be honest about limits: availability is a hint; slang knowledge is incomplete; legal checks need a professional.
- Numerology/vastu: respect it, but it never overrides a legal, meaning or availability FAIL.
- **Evaluating the user's own name:** run score.py, the meaning screen, an existing-use search and check_name.py on it, then score it on the 36 points. If it scores <65 or has a D-FAIL, the full workflow's top picks are the alternatives (no separate list is needed).
- Multi-word names are joined for domains and handles ("Ek Seat" becomes ekseat). Say so in the table.
- The deliverable is for the founder. Keep notes about the skill itself out of it. **Don't use** "Peyar", "skill", "step N", "per the process" or "the reference says" in the deliverable text. Script names may appear only as code-block labels. Title it `# Brand name options: <business>`.
- Worked examples are in `SKILL_DIR/../../examples/` if the repo is cloned.

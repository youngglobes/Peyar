# Peyar (பெயர்)

**A Claude skill that names Indian brands the way branding studios do.**

*Peyar* is Tamil for "name". Tell Claude what you're building. Peyar walks through strategy, generates names across 12 methods (global English words, coined words, alphanumeric like Bira 91 or 82°E, and regional Indian languages, mixed by default), scores how they sound, screens their meaning across 11 Indian languages, checks live `.com` / `.in` / `.co.in` domains and social handles, and grades the shortlist on a **36-point checklist** with India-specific legal checks (IP India trade marks, MCA name rules, the Emblems Act).

```
/peyar  D2C millet snacks brand from Coimbatore, going pan-India, mid-premium, warm and modern
```

## Why

> "Name is your perennial ad." — Harish Venkatesh, founder of Become (formerly Frozen Iris)

Most Indian founders pick a name in an afternoon, then find out about the trade mark objection, the taken Instagram handle or the awkward Hindi meaning after the logo is printed. Renaming is expensive: Grofers became Blinkit, UrbanClap became Urban Company, and Frozen Iris became Become. Peyar puts a studio-grade process in a skill anyone can run for free.

## What it does

1. **Intake**: product, audience, geography, price tier, tone, languages
2. **Strategy**: classifies the brand as search, experience or credence, scans the category norm, and decides between playing inside the norm or against it
3. **Generate**: 25–40 names across 12 methods, with a default mix of ≥50% global-neutral names, ≥3 alphanumeric names and Indian-language options where they fit. Choose global-neutral, India-rooted or mix at intake
4. **Quick screen**: `score.py` (syllables, vowel feel, spelling ambiguity, Indian accent traps such as v/w, z/j, th) plus a meaning screen
5. **Deep check**: `check_name.py` (RDAP domains, YouTube/X/GitHub handles) plus the **36-point checklist** in 6 groups:

| Group | Checks |
|---|---|
| A. Strategy fit | brand type, category norm, positioning, audience, geography, room to grow |
| B. Sound & memory | syllables, vowel feel, pan-Indian pronunciation, phone-dictation test, Truecaller test, confusables |
| C. Meaning & culture | 11-language meaning, slang, religious/caste/political sensitivity, positivity, known vs invented word, no claim words |
| D. Legal (India) | IP India TM by Nice class, well-known marks (s.11), distinctiveness (s.9), MCA Rule 8/8A/8B, Emblems Act 1950, sector regulators |
| E. Digital | .com, .in/.co.in, Instagram, YouTube, X/LinkedIn/WhatsApp, search & app-store clash |
| F. Execution | script rendering, wordmark, display-name limits, export check, recall test, founder fit |

6. **Deliver**: ranked top 3–5 with scorecards, pronunciation guide, risks and next steps (TM classes, MCA reservation, recall-test script)

17 industry playbooks are included: skincare, food (with millets), restaurants, jewellery, fashion, SaaS, fintech, healthcare/dental, edtech, real estate, ayurveda, logistics, dairy/agri, local services, pet care, professional services and B2B finance ops.

## Install

**Claude Code (plugin marketplace):**
```
/plugin marketplace add youngglobes/Peyar
/plugin install peyar@peyar
```

**Claude Code (manual):**
```bash
git clone https://github.com/youngglobes/Peyar.git
ln -s "$PWD/Peyar/skills/peyar" ~/.claude/skills/peyar
```

**Claude.ai / Claude Desktop:** zip the `skills/peyar` folder and upload it under Settings → Capabilities → Skills.

Then ask: *"Name my brand: …"* or run `/peyar`.

## Scripts (usable standalone)

Both scripts use only the Python standard library (3.9+) and need no API keys.

```bash
python3 skills/peyar/scripts/score.py Become Zepto "Frozen Iris"
python3 skills/peyar/scripts/check_name.py peyar netoff --tlds com,in,co.in,ai,io --compact
python3 tests/test_score.py   # or: pytest tests/
```

Domains are checked through RDAP (WHOIS for .io), and taken domains are probed to tell live, parked and dead sites apart. Handles are checked on YouTube and X (add GitHub with `--sites`). Results are **hints**. Instagram and LinkedIn block automated checks, so Peyar prints direct links for you to check by hand.

## Credits & disclaimer

- Inspired by Harish Venkatesh's conversation on the **Nuke It** podcast, ["80 Minutes to Understand Branding Like a Pro"](https://www.youtube.com/watch?v=FXm5rV_bKfs). He describes his studio's 36-parameter naming process. **This checklist is our own reconstruction, not his official list**; each point is tagged as from the video `[V]` or from India-specific research `[R]`.
- **Not legal advice.** Have a registered Trade Marks Agent or IP lawyer confirm before you file or spend money.
- Slang screening by an LLM is incomplete. Always check final names with native speakers.

## Contributing

PRs welcome, especially:
- more industry playbooks (`references/industry-playbooks.md`)
- language notes from native speakers (`references/indian-languages.md`)
- corrections to legal rules as they change (`references/legal-india.md`)
- better availability checks (Instagram and LinkedIn in particular)

## License

MIT

# Peyar test run: Kerala Ayurvedic stress/sleep supplements and teas

## Assumptions
- Credence brand (supplements) with a search layer (Amazon/own site). Premium, urban 28-45, calm and modern.
- GCC and UK exports within 5 years, so the name must survive Malayalam, Arabic and British English speakers.
- Domain: .com/.in are "nice", not a hard constraint (so no early domain screen at step 4.5).
- Nice classes for the TM agent: 5 (supplements), 30 (herbal tea; tea is class 30), 35 (retail). Class 3 only if you add skincare later.
- Web search was available and used for the category scan and existing-use checks. IP India, MCA and Instagram were NOT checked (no live registry access).

## Naming brief
- **Brand type:** credence (nobody can judge a sleep supplement after using it once) with a search layer on Amazon. The name must signal calm and trust, not a medical promise.
- **Category norm:** Indian Ayurveda/wellness = Sanskrit or Himalayan heritage words or "-Veda/-Ayur" compounds, or doctor/founder brands. Scan (8-10 real names): Kerala Ayurveda, Maharishi Ayurveda, Life Aveda, Jeena Sikho (Dr Sukoon), Curae Health (Calmnezz), Nirogam, Kapiva, Planet Ayurveda, Namhya, Vahdam, Sama, Barnaa. Pattern: Sanskrit/Veda compounds, "Dr" or founder names, English-functional names. Sources: [Kerala Ayurveda sleep range](https://keralaayurveda.com/collections/sleep-support), [Tribune India on the sector](https://www.tribuneindia.com/news/business/how-indias-ayurvedic-supplement-industry-is-rebuilding-itself-for-a-global-consumer/), [Namhya on 1mg](https://www.1mg.com/otc/namhya-ayurvedic-tea-otc705722). The search found no Kerala-origin premium D2C herbal-tea brand besides Kerala Ayurveda, which is a large legacy manufacturer. That gap is the opening.
- **Inside or contrarian:** contrarian on language (a soft Malayalam nature word, not Sanskrit/Veda), inside the norm on tone (credible, calm). Avoid "Veda", "Ayur", "Cure" and saffron imagery.
- **Feel/sound:** 2-3 syllables, open vowels, no claim words, easy for a Londoner and a Dubai-based Malayali to say.
- **No-go zones:** "Veda/Ayur" compounds, disease or cure words (Drugs and Magic Remedies Act, FSSAI), deity names, plain words for sleep or rest (descriptive, s.9).

## Candidates (step 3), 34 names, 6 methods
- **Malayalam / regional:** Urakkam (sleep, literal), Thanal (shade), Nilavu (moonlight), Thennal (soft breeze), Kuliru (coolness), Mounam (silence), Ormma (memory), Thaniya (alone), Tharavad (ancestral home)
- **Sanskrit / classical:** Nidra (sleep), Yamini (night), Saumya (gentle), Shama (calm), Vishrama (rest), Manasa (mind), Soma, Sattva, Shanthi
- **Real word:** Hush, Lull, Vesper, Ebb, Dusk
- **Place-based:** Sahya (Sahyadri/Western Ghats), Vembanad, Periyar
- **Coined:** Aurava, Somaya, Kalma, Ilora, Veyla, Senara, Nilaya
- **Founder's own (evaluated separately):** CureVeda (compound, method 4)

## Step 4: screen log
### Sound (score.py, real output; all candidates plus CureVeda)
```
100  Olam  [2 syl, 4 letters, light/open (premium, soft)]
100  Mounam  [2 syl, 6 letters, light/open (premium, soft)]
100  Nidra  [2 syl, 5 letters, balanced]
100  Soma  [2 syl, 4 letters, light/open (premium, soft)]
100  Dusk  [1 syl, 4 letters, hard/dense (strong, techy), but check that it is pronounceable]
100  Kalma  [2 syl, 5 letters, balanced]
 97  Thanal  [2 syl, 6 letters, balanced]
       - th: said as t or d
 97  Shama  [2 syl, 5 letters, balanced]
       - sh/s: these merge in parts of East India
 97  Hush  [1 syl, 4 letters, hard/dense (strong, techy), but check that it is pronounceable]
       - sh/s: these merge in parts of East India
 97  Vesper  [2 syl, 6 letters, balanced]
       - v/w: these merge in many Indian accents
 95  Kuliru  [3 syl, 6 letters, light/open (premium, soft)]
 95  Manasa  [3 syl, 6 letters, light/open (premium, soft)]
 95  Periyar  [3 syl, 7 letters, light/open (premium, soft)]
 95  Somaya  [3 syl, 6 letters, light/open (premium, soft)]
 95  Ilora  [3 syl, 5 letters, light/open (premium, soft)]
 95  Senara  [3 syl, 6 letters, light/open (premium, soft)]
 95  Nilaya  [3 syl, 6 letters, light/open (premium, soft)]
 94  Shanthi  [2 syl, 7 letters, balanced]
       - th: said as t or d
       - sh/s: these merge in parts of East India
 94  Ormma  [2 syl, 5 letters, balanced]
       - double letter: often typed single
 94  Saumya  [2 syl, 6 letters, light/open (premium, soft)]
       - y as a vowel or consonant: unclear
 94  Lull  [1 syl, 4 letters, hard/dense (strong, techy), but check that it is pronounceable]
       - double letter: often typed single
 94  Ebb  [1 syl, 3 letters, balanced]
       - double letter: often typed single
 94  Sahya  [2 syl, 5 letters, light/open (premium, soft)]
       - y as a vowel or consonant: unclear
 92  Nilavu  [3 syl, 6 letters, light/open (premium, soft)]
       - v/w: these merge in many Indian accents
 92  Vembanad  [3 syl, 8 letters, balanced]
       - v/w: these merge in many Indian accents
 92  Aurava  [3 syl, 6 letters, light/open (premium, soft)]
       - v/w: these merge in many Indian accents
 92  Thaniya  [3 syl, 7 letters, light/open (premium, soft)]
       - th: said as t or d
 91  Thennal  [2 syl, 7 letters, balanced]
       - double letter: often typed single
       - th: said as t or d
 91  Sattva  [2 syl, 6 letters, balanced]
       - double letter: often typed single
       - v/w: these merge in many Indian accents
 91  Veyla  [2 syl, 5 letters, light/open (premium, soft)]
       - y as a vowel or consonant: unclear
       - v/w: these merge in many Indian accents
 89  Urakkam  [3 syl, 7 letters, balanced]
       - double letter: often typed single
 89  Tharavad  [3 syl, 8 letters, balanced]
       - v/w: these merge in many Indian accents
       - th: said as t or d
 89  Yamini  [3 syl, 6 letters, light/open (premium, soft)]
       - y as a vowel or consonant: unclear
 89  Vishrama  [3 syl, 8 letters, balanced]
       - v/w: these merge in many Indian accents
       - sh/s: these merge in parts of East India
 82  CureVeda  [4 syl, 8 letters, light/open (premium, soft)]
       - 4 syllables: harder to remember
       - v/w: these merge in many Indian accents
```
All scored 82+ (nothing cut on sound). Note: score.py gives CureVeda 82 only because it ignores meaning, claims and existing use.

### Meaning/slang (mini table, my reading, not native-verified)
| Name | Languages checked | Concern | Confidence |
|---|---|---|---|
| Kuliru | Mal, Tam, Tel, Kan, Hin, Urdu, Ben, Mar, Guj, Pun, Odia, Eng, Arabic | None found; "kulir" = cold/cool in Malayalam/Tamil | Medium |
| Nilavu | same | None; "nilavu" = moon/moonlight in Malayalam/Tamil | High (Mal/Tam), medium others |
| Thennal | same | None; "thennal" = soft breeze, also a girl's name | High (Mal/Tam), medium others |
| Mounam | same | None; "mounam" = silence. Mild religious tone (vow of silence) | High (Mal/Tam), medium others |
| Thanal | same | None; "thanal" = shade/cool shelter | Medium |
| Kalma | same | Islamic creed (kalima); also Finnish word for death/grave | Medium |
| Soma | same | Sanskrit ritual drink; US prescription muscle relaxant brand | High |

**Cannot vouch for:** Odia, Punjabi, Gujarati, Bengali street slang, Arabic dialects. Send the final 3 to one native speaker each (Malayalam, Tamil, Hindi, Gulf Arabic, British English).

### Cuts, in order, with reasons
- **Meaning/political/religious:** Kalma (kalima, Finnish "death"), Periyar (political figure and river, polarising), Soma (drug brand in US, ritual drink), Shama (candle/Urdu, thin), Sattva (overused in wellness).
- **Descriptive D3 (plain word for the product's job):** Urakkam (sleep), Nidra (sleep), Vishrama (rest), Shanthi (peace), Manasa (mind), Hush/Lull/Dusk/Ebb (generic English).
- **Well-known/crowded:** Vesper (crowded), Tharavad (heritage-hotel/home cliché), Vembanad (place, s.9 geographic), Sahya (reads unclear, geographic).
- **Existing use (one web search each):** no same-category brand found for Thanal, Nilavu, Thennal, Kuliru, Mounam, Saumya, Somaya, Yamini (search results showed unrelated brands only; absence in search is NOT proof). Saumya, Somaya, Yamini, Aurava, Ilora, Veyla, Senara, Nilaya, Thaniya, Ormma were cut to keep the shortlist to 5: weaker story or thinner Malayalam rooting (Sanskrit generic, or coinages that must be taught from zero). Not looped; 5 survived.
- **CureVeda:** handled in its own section below.

## Top 5 names (ranked)
Scores within 5 points are a tie (all five are, at 83-85). Ranked by: lower legal risk, then story, then availability, then recall. Kuliru and Thennal tie on score; Kuliru wins on availability. Thanal ranks last: possible Tamil meaning clash, unknown .in/.co.in and a Kerala NGO of the same name.

| Rank | Name | Method | Why it works | Checklist /100 (n unverified) | Sound /100 | .com | .in | .co.in | YouTube | X |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Kuliru | Regional (Malayalam) | "Coolness" for stress; the only fully free domain set | 85 (6) | 95 | ✅ | ✅ | ✅ | ✅ | ❌ |
| 2 | Nilavu | Regional (Malayalam) | Moonlight = night, sleep; strongest story | 83 (6) | 92 | ❌- | ❌L | ✅ | ❌ | ❌ |
| 3 | Thennal | Regional (Malayalam) | Soft breeze, calm, warm | 85 (6) | 91 | ❌L | ❌L | ✅ | ❌ | ❌ |
| 4 | Mounam | Regional (Malayalam/Tamil) | Silence; fits stress relief | 83 (6) | 100 | ❌- | ❌L | ✅ | ❌ | ❌ |
| 5 | Thanal | Regional (Malayalam) | Shade, a cool place to rest | 84 (7) | 97 | ❌- | ❔ | ❔ | ❌ | ❌ |

Real script output (`check_name.py --compact --tlds com,in,co.in --sites youtube,x`):
```
Nilavu             com❌(-)  in❌(L)  co.in✅  youtube❌  x❌
Thennal            com❌(L)  in❌(L)  co.in✅  youtube❌  x❌
Thanal             com❌(-)  in❔  co.in❔  youtube❌  x❌
Mounam             com❌(-)  in❌(L)  co.in✅  youtube❌  x❌
Kuliru             com✅  in✅  co.in✅  youtube✅  x❌
CureVeda           com❌(L)  in❔  co.in❔  youtube✅  x✅

✅ likely-free  ❌ taken  ❔ unknown  (P)=parked/for-sale  (L)=live site  (R)=redirects elsewhere  (-)=no site
Instagram/LinkedIn: check by hand. Run without --compact for IP India / MCA links.
```
Caveat: ❌ for YouTube/X means the script found the handle taken. I tried to open YouTube handles with curl but got no readable page title, so I could not decide same-category vs unrelated. Open each by hand. Domain "(L)" means a live site; I did not read those sites either, so every ❌L is a WARN pending a look. No ❌P (parked) results appeared.

### 1. Kuliru
- Pronunciation: KOO-li-roo · Scripts: Malayalam കുളിരു, Tamil குளிரு (reads as "cold"; check the nuance), Devanagari कुलिरु
- Story: "Kulir is the cool you feel at dawn in the Kerala hills. We make the cool for your evenings."
- Scorecard:

  | Group | Points (P/W/F/U/N) | Key evidence |
  |---|---|---|
  | A Strategy | A1 P · A2 P · A3 W · A4 P · A5 W · A6 P | Calm, credence-appropriate; "cool" implies calm only after being taught; GCC/UK need a pronunciation hint |
  | B Sound | B1 P · B2 P · B3 P · B4 W · B5 W · B6 P | 3 syllables, open vowels; spelled Kuliru/Kulir/Kooliru; may be saved as "Kulir" |
  | C Meaning | C1 W · C2 P · C3 P · C4 P · C5 W · C6 P | Medium confidence, no native check; semi-invented form |
  | D Legal | D1 U · D2 P · D3 P · D4 U · D5 P · D6 P | Not a claim word; IP India and MCA not searched |
  | E Digital | E1 P · E2 P · E3 U · E4 P · E5 U · E6 W | .com/.in/.co.in free per script; X taken (not opened); Google page not reviewed beyond one search |
  | F Execution | F1 P · F2 P · F3 P · F4 W · F5 U · F6 U | 6 letters; SMS sender ID "KULIRU" fits; Arabic not checked by a native |
- Weakest 3 points and fixes: **C5** (semi-invented; budget to teach it, tagline "calm, the Kerala way"); **B4** (hint spelling on pack and Amazon title, add "Kulir" as a keyword); **A5** (add phonetic respelling on export packs).

### 2. Nilavu
- Pronunciation: NI-la-vu (v softens to "w" in some accents) · Scripts: Malayalam നിലാവ്, Tamil நிலவு, Devanagari निलावु
- Story: "Nilavu is the Malayalam word for moonlight. We make what you reach for when the day is over."
- Scorecard:

  | Group | Points | Key evidence |
  |---|---|---|
  | A Strategy | A1 P · A2 P · A3 P · A4 P · A5 W · A6 P | Strong sleep story; Malayalam-only meaning abroad |
  | B Sound | B1 P · B2 P · B3 W · B4 W · B5 P · B6 W | v/w split; close to "Nila Ayurveda" (a small wellness site in the search) |
  | C Meaning | C1 P · C2 P · C3 P · C4 P · C5 W · C6 P | Known word to Malayalis/Tamils, to be taught elsewhere |
  | D Legal | D1 U · D2 P · D3 P · D4 U · D5 P · D6 P | Not searched |
  | E Digital | E1 W · E2 W · E3 U · E4 W · E5 U · E6 W | .com no site (maybe buyable); .in live (not read) |
  | F Execution | F1 P · F2 P · F3 P · F4 W · F5 U · F6 U | |
- Weakest 3: **E1/E2** (domains taken; contact owner or use get-/-wellness variant); **B3** (v/w); **B6** (Nila Ayurveda proximity, check TM).

### 3. Thennal
- Pronunciation: THEN-nal · Scripts: Malayalam തെന്നൽ, Tamil தென்னல், Devanagari थेन्नल
- Story: "Thennal is the breeze that comes off the backwaters at dusk."
- Scorecard:

  | Group | Points | Key evidence |
  |---|---|---|
  | A Strategy | A1 P · A2 P · A3 P · A4 P · A5 W · A6 P | Calm, gentle |
  | B Sound | B1 P · B2 P · B3 W · B4 W · B5 W · B6 P | "th" and double n vary in spelling (Thenal/Thennal) |
  | C Meaning | C1 P · C2 P · C3 P · C4 P · C5 W · C6 P | Also a common girl's name |
  | D Legal | D1 U · D2 P · D3 P · D4 U · D5 P · D6 P | Not searched |
  | E Digital | E1 W · E2 W · E3 U · E4 W · E5 U · E6 W | .com and .in live sites, not read |
  | F Execution | F1 P · F2 P · F3 P · F4 W · F5 U · F6 U | |
- Weakest 3: **E1/E2** (both live), **B3/B4** (spelling split), **E6** (personal-name results crowd search).

### 4. Mounam
- Pronunciation: MOW-num · Scripts: Malayalam മൗനം, Tamil மௌனம், Devanagari मौनम्
- Story: "Mounam is silence. A good night starts with the noise turning off."
- Scorecard:

  | Group | Points | Key evidence |
  |---|---|---|
  | A Strategy | A1 P · A2 P · A3 P · A4 P · A5 W · A6 P | |
  | B Sound | B1 P · B2 P · B3 P · B4 W · B5 W · B6 P | "Mounam/Maunam" spelling split |
  | C Meaning | C1 P · C2 P · C3 W · C4 P · C5 W · C6 P | Ascetic vow of silence adds a faint religious tone |
  | D Legal | D1 U · D2 P · D3 P · D4 U · D5 P · D6 P | Not searched |
  | E Digital | E1 W · E2 W · E3 U · E4 W · E5 U · E6 W | .in live, not read |
  | F Execution | F1 P · F2 P · F3 P · F4 W · F5 U · F6 U | |
- Weakest 3: **E2**, **B4**, **C3**.

### 5. Thanal
- Pronunciation: THA-nal · Scripts: Malayalam തണൽ, Tamil தணல் (I believe this means embers in Tamil, medium confidence: possible clash), Devanagari थनल
- Story: "Thanal is the shade of a tree on a hot day. We make that shade for your mind."
- Scorecard:

  | Group | Points | Key evidence |
  |---|---|---|
  | A Strategy | A1 P · A2 P · A3 P · A4 P · A5 W · A6 P | |
  | B Sound | B1 P · B2 P · B3 W · B4 W · B5 P · B6 P | "th" variants |
  | C Meaning | C1 W · C2 P · C3 P · C4 P · C5 W · C6 P | Possible Tamil "embers" reading vs Malayalam "shade"; unverified |
  | D Legal | D1 U · D2 P · D3 P · D4 U · D5 P · D6 P | |
  | E Digital | E1 W · E2 U · E3 U · E4 W · E5 U · E6 W | .in/.co.in unknown (script could not check); a Kerala NGO "Thanal" exists, not opened |
  | F Execution | F1 P · F2 P · F3 P · F4 W · F5 U · F6 U | |
- Weakest 3: **C1** (Tamil meaning), **E2** (unknown), **E6** (NGO).

## Also considered (cut and why)
- **Meaning/religion/political:** Kalma, Periyar, Soma, Shama, Sattva
- **Descriptive D3:** Urakkam, Nidra, Vishrama, Shanthi, Manasa, Hush, Lull, Dusk, Ebb
- **Crowded/geographic:** Vesper, Tharavad, Vembanad, Sahya
- **Shortlist trimmed (no conflict found, weaker story):** Saumya, Somaya, Yamini, Aurava, Ilora, Veyla, Senara, Nilaya, Thaniya, Ormma
- **Founder's name:** CureVeda, see below

## Founder's name: CureVeda
Evaluated straight at step 5, alongside my picks.

**Verdict: do not use it. It scores 58 (5 unverified), below the 65 bar, with a D-group FAIL, because a brand called Cureveda already sells herbal supplements in India.**

Real script output:
```
CureVeda           com❌(L)  in❔  co.in❔  youtube✅  x✅
 82  CureVeda  [4 syl, 8 letters, light/open (premium, soft)]
```

Findings:
- **Existing use (D1 FAIL on evidence, not on the registry):** Cureveda is a Nagpur-based herbal and therapeutic dietary-supplement brand, covered by [YourStory](https://yourstory.com/smbstory/herbal-supplements-cureveda-common-ailments-heart-health/amp) and sold as a brand page on [Cureka](https://cureka.com/product-brands/cureveda). That is the same category and the identical name. Even without a registered mark, it exposes you to passing-off claims and a refused TM-A. I did NOT search IP India (not available), so the registry result is UNVERIFIED, but the market evidence alone is disqualifying.
- **Domains (script):** cureveda.com is taken and live; .in/.co.in unknown; YouTube and X handles appear free but that is irrelevant if the brand is taken. E6 (search) FAIL: Cureveda would not own page 1.
- **Claims (D6 WARN):** "Cure" in a name for supplements and teas is claim-adjacent: Drugs and Magic Remedies Act and FSSAI in India; MHRA/ASA (UK) and GCC regulators treat "cure" as a medicinal claim. This blocks the UK/GCC plan even if the name were free.
- **Fit:** it is the saffron/Veda compound you asked to avoid (A2/A4 WARN), 4 syllables (B1 WARN), "Veda" is descriptive and crowded in Ayurveda (D3 WARN), Veda is also a sacred word (C3 WARN), and "cure" is the opposite of the calm, modern tone for stress/sleep (A1 WARN).
- **Scorecard:** A WWWWWW · B WPWWWF (B6 FAIL: it is a competitor's name) · C WPWWPW · D FPWUPW · E FUUPUF · F WPPWUP. Score 58 (5 unverified).
- **What the founder may like in it:** the "Veda" heritage. If the founder wants that link, keep it in a descriptor ("Kuliru, Ayurvedic sleep and calm") rather than the name.
- **Five alternatives (<65, so offered per SKILL.md):** Kuliru, Nilavu, Thennal, Mounam, Thanal (above).

## Next steps
1. Native-speaker check: top 3 names to 1 person per target language (Malayalam, Tamil, Hindi, Gulf Arabic, British English). Ask specifically about Tamil "thanal" and "kulir".
2. 5-second recall test with 10-20 target buyers (script below)
3. IP India search in classes 5, 30, 35 (add 3 if skincare) → TM agent's opinion → file TM-A
4. Reserve the company name on MCA (SPICe+ Part A / RUN)
5. Buy domains and claim handles the same day; open the taken YouTube and X handles and read the .in/.com live sites first. Also check Instagram.
Expect weeks, not days. Unhype took a studio ~3 months (strategy → shortlist → market test → TM → multi-geography → stakeholder sign-off).

**Recall test script:** show each name for 5 seconds, talk about something else for 2 minutes, then ask: "Which names do you remember? Spell one. What do you think it sells?" Recall + correct spelling + right category guess wins.

*Peyar gives heuristics, not legal advice. Have a registered trade mark agent confirm before filing.*

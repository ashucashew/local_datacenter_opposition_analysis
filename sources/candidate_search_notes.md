# Candidate search notes (first pass, 2026-11-16)

AI first pass. Nothing here is human-verified.

## How the candidates were found

- **Tool constraint (first pass):** the first pass was built from web-search summaries only, because network access was blocked.
- **Verification pass (same day, after network access was opened):** pages were downloaded and read directly. In `data/projects.csv` notes, `[page]` marks a fact read on the source page and `[search]` marks one seen only in a search summary. `[search]` facts need a human check before the essay relies on them. Pages that blocked automated access (Axios, Inside Climate News, DCD, WDRB) are listed as sources but were not read.
- **Data Center Watch:** the project-level lists sit in paid reports. Press coverage of the Q1 2026 report gives totals (75 projects, ~$130B) but names almost no projects, so most candidates came from project-specific news searches plus the trackers below.
- **Other aggregate counts found:**
  - Heatmap Pro: at least 20 projects cancelled after local pushback in Q1 2026, >$41.7B and ≥3.5 GW; ~$260B cancelled year-to-date in 2026. This is a third estimate worth citing beside DCW and SemiAnalysis, and it counts *cancellations* only. https://heatmap.news/politics/local-opposition-data-center-cancellations
  - Trackers: Programs.com, suedatacenters.org (125 sites, 12.7 GW cancelled), isadatacentercoming.com, Baxtel. These are secondary; use them only as leads. One tracker attributed a "$12B Culpeper County" denial that appears to be St. Joseph County, IN, which is a small example of how unreliable tracker data can be (C22).

## Decision codes in `candidates_log.csv`

| decision | meaning |
|---|---|
| `shortlist` | Proposed for the ~20-project sample |
| `candidate` | Eligible, but probably below the size cut or thinly sourced |
| `hold` | Needs a key fact (date, size, identity) before deciding |
| `exclude` | Out of the time window, too small, or unverifiable; reason given |

`mechanism_prelim` and `outcome_prelim` are first guesses using the schema's vocabulary. They are not codings.

## Shortlist as it stands

- **2025 (14):** C01 PW Digital Gateway, C02 Project Blue, C03 Google Franklin Twp, C04 Microsoft Caledonia, C05 Mooresville, C06 Project Cumulus, C08 New Carlisle, C09 Bolingbroke, C11 Tarboro, C13 Project Lincoln, C14 Balico, C15 Saline Twp, C16 Hermantown, C17 Project Sail. This needs trimming to about 10.
- **2026 Q1–Q2 (10):** C23 Project Jarvis, C24 Montour/Talen, C25 Highlander SM One, C26 New Hill (Apex), C27 Lordstown, C28 Barrington Hills, C29 Project Delta, C30 Mountain Road (Tract), C31 Project Scott (Archbald), C32 STAMP. Several lack MW and $ figures.

## Decisions needed from the human

1. **2026 window.** The brief says Q1–Q2 2026, but several of the largest 2026 cases fall in Q3–Q4: La Osa (1 GW, $33B), Kingsboro ($19B), Quantum Frederick, NY state EO / STAMP, Wilmington AWS, and Lighthouse (700 MW). Option A: keep Q1–Q2 and put these in the essay as anecdotes. Option B: widen to "2026 YTD" and say so.
2. **Ranking metric.** Generation MW (Balico 3.5 GW gas plant), "power needed" (Hermantown 700 MW) and campus MW are not comparable. Proposal: rank by reported campus/IT MW, fall back to $, and treat Balico's MW as blank.
3. **Period rule for multi-year fights** (C01 PWDG, C25 San Marcos, C17 Sail, C32 STAMP). Proposal: use the date of the decisive event (the ruling, denial or withdrawal that actually stopped the project), and record both dates in notes.
4. **Proceeding-despite-opposition cases** (C02 Project Blue, C15 Saline, C17 Sail). These are useful because DCW-style counts would likely include them, and they ended up built or approved. Keep them in the sample. Do not drop them for "not being blocked".

## Most useful leads for the essay's argument

- **Moratoriums that actually bound:** C17 Project Sail (moratorium May–Dec 2025, approved Apr 2026), C27 Lordstown (Ohio Supreme Court ruled 7-0 that a filed site plan did not vest against a later moratorium), and C13 Oldham County (moratorium deliberately removed the pending-application carve-out). These are the closest tests of SemiAnalysis's vested-rights and carve-out filters.
- **Jurisdiction:** C02 Tucson said no and Pima County said yes on the same site.
- **Litigation reverses outcomes in both directions:** C15 Saline (developer sued and won), C01 PWDG and C29 Stokes (opponents sued and won; Stokes was then re-approved about 8 months later).
- **Multi-option developers:** Tract (C05, C30, C21), Cloverleaf (C34), Karis (C35/C44), Microsoft (C04, "looking for a new site").
- **Speculative scale:** C37 Stratos (9 GW, no tenant), C39 La Osa (no end user, half its power unsecured), C42 Lighthouse (withdrawn about 2 weeks after announcement, no filing).

## Still to search

- Identify SemiAnalysis's three delayed projects (C46–C48) from public reporting only.
- Dates and sizes for C18 Douglas County, C38 Kingsboro, C19 Matthews, C49 Forsyth.
- MW figures for C03, C08, C11, C13, C27, C28 from utility filings or planning records.
- Citable utility/grid-operator statements that large-load requests far exceed what will be built (Hypothesis 2).

## Verification pass: what changed

- **SemiAnalysis public portion read directly.** It names one of its three delayed projects: **NorthPoint's campus in Hazle Township, PA** (moratorium June 2026, delay into 2027) → P16. Its Ohio discussion names the **Sunbury** moratorium (Apr 2026), and the AWS Delaware County North campus is the likely Ohio case → P20 (low confidence; the article does not say they're the same). The Colorado site is still unnamed. The public text also gives New York's order as ~1.4 GW touched, ~0.8 GW meaningfully delayed, and cites Saline Township as a project that advanced via consent judgment.
- **Status changes:** Hermantown got final approval Oct 30 2026 → proceeding. Project Blue got a signed TEP energy supply agreement (286 MW) after Tucson's rejection → committed / proceeding.
- **Corrected sizes:** Tract's Hanover County project is 900 MW. Oldham County was 600 MW announced, then a 100 MW application. Tarboro is 300 MW. Bolingbroke is 900 MW, not 1.2 GW. Mooresville's 350 MW was dropped (it came only from a video). Project Blue is 286 MW.
- **Relocation checks:** CRG's Festus site (after St. Charles) and ESS's Kingsboro site (after Tarboro) are both *not* explicitly linked in press → not coded as relocated. Microsoft said it is seeking another SE Wisconsin site, but no site has been named.
- **New candidates:** Red Wolf, KCK ($12B, lawsuit; selected as P10), Lebanon County PA ($1.7B), Menomonie WI ($1.6B), Amazon Bridgefield in Loudoun (Q4 2026, anecdote). DCW Q2 2026 headline: 45 projects, ~$68B.

## Sample as selected (`data/projects.csv`, 21 rows, all `human_verified = no`)

**Selection rule applied:** rank by reported MW, falling back to $ when no MW was reported. Within each period I took the largest projects, plus Project Blue for the jurisdiction case. Alternates that missed the size cut are marked `alternate` in the log.

First look at the counts (not yet the analysis script; these will change after human review):
- **Realness tier:** 16 of 21 projects are speculative, holding 7,730 of the 9,716 MW coded (~80%).
- **Outcome:** 7 cancelled, 5 dormant, 6 delayed, 3 proceeding. The proceeding three (Saline, Hermantown, Project Blue) total ~2 GW.
- **Primary mechanism:** formal moratoriums are primary in only 4 of 21.
- **Passes SemiAnalysis filter:** yes = 2 (Hazle Twp, Lordstown), unclear = 4, no = 15.
- **Unknowns:** 56 of 105 values in the five status fields (tenant, land, power, permits/financing, other sites) are `unknown`. That is itself a finding about how thin public evidence is.

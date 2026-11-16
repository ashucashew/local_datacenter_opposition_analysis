# Candidate search notes (first pass, 2026-11-16)

AI first pass. Nothing here is human-verified.

## How the candidates were found

- **Tool constraint:** this session's network policy blocked direct page fetches, including datacenterwatch.org, NBC, Newsweek, Wikipedia and the SemiAnalysis page. Every fact in `data/candidates_log.csv` therefore comes from **web-search result summaries**, not from reading the source pages. Each row's `sources` lists the URLs the search returned. All of them need to be opened and checked before a row moves into `data/projects.csv`.
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

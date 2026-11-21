# Outline: Can data center opposition be an AI safety lever?

Target: ~2,000 words. Deadline: Sun Nov 22 (London track 23:59 UK / 6:59 pm ET; DC track 11:59 pm ET).

Source tags: **[read]** = page read directly in this project. **[search]** = seen in search results only; open before citing. **[bg]** = background knowledge; find and cite a source or cut.

---

## 0. Question and thesis (~200 words)

**Framing (conditional, even-handed):** Some in the AI safety community favor slowing frontier AI development (cite one or two: the 2023 FLI pause letter, PauseAI). Frontier capability has tracked compute: training compute for frontier models has grown 4–5x a year ([Epoch][epoch-compute], [read]). Meanwhile, data center opposition is the most visible public resistance to AI infrastructure. So: *could riding that wave pace the frontier?*

**Thesis:** No. US data center opposition is an unreliable and poorly aimed lever, both today and structurally. (1) It mostly costs developers time and money, not capacity, and they have escape routes. (2) The coalition's grievances can be bought off in ways that do not slow AI. (3) Its effects fall on the wrong part of the system: the best-funded frontier labs are the last to be squeezed. Targeted compute-governance tools aim at the actual risk.

> Logic check: the argument needs both "it's weak" (sections 1–2) *and* "even where it works, it hits the wrong thing" (section 3). Either alone is rebuttable. Together they make the case.

---

## 1. How strong is the brake today? (~550 words)

**Claim:** Opposition is real and growing, but it acts mainly on time and cost, early in the development funnel.

**1a. The headline numbers measure different parts of the funnel** (one short paragraph, one small table)
- Funnel (US, rough): ~700–780 GW publicly known → ~430 GW pipeline → ~200 GW with signed utility/construction agreements → ~60–80 GW under construction → ~25–40 GW delivered a year → ~50 GW operating (end 2025). Sources: SynMax citing Aurora [read][synmax]; Wood Mackenzie [read][woodmac]; FERC via press [search]; DC Market Insights [read][dcmi].
- Data Center Watch: ≥75 projects, ~$130B "blocked or delayed" in Q1 2026, any mechanism, early stages, dollars, no public definitions [read][dcw]. Heatmap: ≥20 cancellations, >$41.7B, ≥3.5 GW in Q1 2026 [read][heatmap]. SemiAnalysis: only ~2.3 GW actually delayed (moratoriums plus the NY order; active, near-term projects whose delivery date moves) [read][semi-mor].

**1b. What our project data shows** (`data/projects.csv`, 21 rows; `data/broad_list.csv`, 68 projects from DCW's free briefings)
- Most losses occur at the first local-approval step (rezoning / special use permit). Developers routinely lose sites at this stage.
- Few blocked projects had a public tenant or power deal at the time. Broad list: 3 of 42 blocked/delayed named an end user.
- Moratoriums were the main cause in only ~4 of 21 (core) and 4 of 42 (broad). Withdrawals and rezoning denials dominate.
- Projects with real demand behind them got through: Saline (OpenAI/Oracle, by lawsuit and settlement), Project Blue (approved by Pima County after Tucson said no), Hermantown (Google, approved after ~1 year).
- Delays where measurable: ~8–15 months (Stokes ~8; Hermantown ~12; Project Sail ~15).
- ⚠️ Re-run `analysis/summarize.py` after the human check of the 21 rows. Drop the old "speculative vs committed" result: it relied on information that became public after the opposition.

**1c. Size of the effect**
- SemiAnalysis's 2.3 GW ≈ ~5 weeks of US buildout growth (≈ ln(1 + 2.3/70) / ln(1.4) × 52; assumes ~70 GW stock end 2026 and ~40%/yr growth). Order of magnitude only.
- The total is still rising: pipeline +54 GW in Q2 2026, +29% year on year; ~80 GW under construction [read][woodmac].

**1d. Link to AI progress: the chip constraint**
- Rough global comparison: power needed for chips shipped ≈ 15–30 GW (2026) and 30–45 GW (2027), vs data center additions ≈ 25 GW (2026) and 43–51 GW (2027). Chip units from JPMorgan [search]; per-chip power [bg]; DC additions from SemiAnalysis [read][semi-27].
- Market indicators show buildings were tight in 2026: 1.4% vacancy (CBRE) [search]; 95% of capacity under construction pre-leased (JLL) [read][jll].
- SemiAnalysis argues memory and logic chips become the binding constraint in 2027–28 [read][semi-27]. If so, delaying buildings mostly delays capacity that would have waited for chips.
- State this conditionally: the ranges overlap, and the estimates are rough.

---

## 2. Why the brake won't get much stronger (~400 words)

**2a. Developers build wherever value exceeds cost, and value is very high**
- Leases ≈ $30–50B TCV per GW over 15–20 years ≈ $1.5–3.3B per GW per year; ~$1T of binding leases signed in 2026 [read][semi-27].
- Costs opposition imposes are small by comparison: NorthPoint's $165M package for ~300 MW ≈ 2–4 months of lease revenue, paid once [search][hazelnut]; Tract's $15M for water in Hanover [read][rbs]; developers spend only ~5–10% of project capital before a lease [read][semi-27].

**2b. Escape valves**
- Off-grid / on-site power: GW Ranch, Pecos County TX (Amazon, 7.65 GW gas, "off-grid initially") [search][gwranch]; Microsoft–Chevron near Pecos (~2 GW) [search]. SemiAnalysis expects 40 GW+ of behind-the-meter US data centers by 2028 [search]. On-site power costs ~$100–165/MWh vs $90–95 from the grid [search][rabobank]. Caveats: ~90 GW announced but ~2 GW operating [search][cleanview]; Fermi America has struggled to find a tenant [search][latitude].
- Abroad: SemiAnalysis says the ex-US buildout is accelerating, "largely driven by US challenges" [read][semi-27]. BIS moved the UAE into Country Group A:5 in July 2026 (license-free access for approved entities) [search][uae]. Limits: rest-of-world additions are only ~4–8 GW/yr; GovAI finds no intrinsic UAE cost advantage [read][govai-uae].
- Within the US: the buildout concentrates where building is possible. PJM + ERCOT hold ~half of capacity under development [read][woodmac]; 77% of NA under-construction capacity is in "frontier markets" [read][jll].

**2c. The coalition's grievances are negotiable**
- What opponents want: lower bills, less noise, water protection, fair payment, transparency.
- Fixes that don't slow AI: large-load tariffs (Kansas ≥75 MW tariff; Oregon POWER Act; Georgia SB 34; Texas SB 6) [read: DCW briefings]; Microsoft's Jan 2026 pledge to pay full grid costs [read: DCW briefing]; community benefits (NorthPoint $165M; Saline ~$14M) [read]; on-site power (avoids sharing grid costs); noise studies and setbacks.
- Honest caveat: not all fully solved. Low-frequency hum falls outside A-weighted noise rules (Great Oak, VA) [search][noise]; regional capacity-price effects persist. But every remedy *reduces* opposition without *reducing* compute.

**2d. What would make it bind** (brief; links to counterarguments)
- Restrictions in the few key states (Texas's Sept 2026 permit pause puts 60+ GW under scrutiny [read][woodmac]), sustained, plus federal inaction.

---

## 3. It aims at the wrong target (~400 words)

**3a. The squeeze falls last on frontier labs**
- The largest single campuses are ~1–2 GW, against ~25–40 GW of US additions a year. The best-funded labs (OpenAI, Anthropic, Meta, Google, etc. all leasing GW-scale [read][semi-27]) can outbid others for the sites that remain.
- Tighter supply hits smaller firms, inference capacity and academic users first. A blunt brake may *concentrate* frontier compute among fewer, better-resourced actors.

**3b. It can push compute somewhere harder to govern**
- Offshoring to jurisdictions with weaker oversight (the UAE example). This may be backlash's most important governance effect.

**3c. Progress isn't only compute scale**
- Algorithmic efficiency ≈ ~3x a year (Epoch estimate; other estimates 2–6x) [search][epoch-compute]. RL rollouts and inference can be spread across sites [bg; cite Epoch's decentralized training piece][epoch-decentral].

**3d. Levers that target the risk instead**
- **Compute thresholds and reporting:** obligations triggered above a training-compute threshold (e.g., EU AI Act's 10^25 FLOP presumption [bg]). See Heim on training compute thresholds [heim-thresholds].
- **Know-your-customer (KYC) for compute providers:** cloud providers verify who is renting very large amounts of compute and flag frontier-scale training runs, like bank KYC rules [govai-kyc].
- **Export controls:** limit frontier compute in rival states and keep frontier clusters in jurisdictions where other oversight applies. Note the tension: loosening controls (UAE) is also an escape valve.
- Overview: Sastry, Heim et al., "Computing Power and the Governance of AI" (GovAI, 2024) [govai-compute].

---

## 4. Counterarguments and rebuttals (~300 words)

| Counterargument | Rebuttal |
|---|---|
| **(Lead) Today's effects understate the future: if opposition keeps growing, it could significantly slow capacity** | Concede that it *could* slow the buildout, especially via state-level restrictions in key states. But (1) the safety community can't control it: it rises and falls with local grievances that developers can pay down, so it's a hope, not a lever; (2) the mistargeting gets *worse* with scale: a bigger squeeze concentrates compute among the best-funded labs and pushes it abroad. Separate "can it slow the buildout?" (possibly) from "is it an effective safety lever?" (no). Evidence on escalation is mixed: 400+ moratoriums on ~18% of tracked sites, record cancellations, ballot wins, the Texas pause; vs DCW Q2 ($68B) below Q1 ($130B), 13 statewide bills died, pipeline +29% yoy. **Signposts:** state-level restrictions in TX/VA/GA/OH/PA; projects *with signed tenants* failing; time-to-construction lengthening; cancellations exceeding new pipeline entries; offshore share rising fast. |
| Opposition is the most powerful grassroots AI politics right now (restrictions won in nearly all of ~41 local ballot measures on Nov 3, 2026 [search][ballot]; bipartisan) | Concede the power. But it is aimed at local costs, and developers can pay those down. Better to channel it into shared policies (section 5) than to rely on it as a brake. |
| Delays compound if construction is the bottleneck (delayed projects push the queue back) | True only in years when buildings, not chips, bind. Chips likely bind in 2027–28. Even with buildings binding, today's measured delay is ~weeks of growth. |
| State action in key states could bind (Texas pause; NY order) | The most credible path. But it's slow, politically contested (13 statewide bills died in 2026 [read][semi-mor]), and escape valves exist (federal land, off-grid, allied sites). Give signposts. |
| Even weeks or months matter if timelines are short | Concede that weeks matter more under short timelines. But an unreliable lever that delivers weeks, falls on the wrong actors and may push compute abroad is worse than targeted tools. |

Also (short paragraph, strategic cost): safety arguments about dangerous models get muddled with zoning and bills; obstructing the buildout costs credibility in a Washington that frames it as competition with China; instrumentalizing local grievances risks trust. Do **not** claim foreign actors are stoking backlash (no evidence found).

---

## 5. Conclusion: shared policies (~200 words)

Policies that serve both local opponents and AI safety. The common thread is **transparency about who is building what, where**:
- **Public registries and disclosure of large data centers and loads** (size, power, operator). Citizens get information; safety gets visibility into where large clusters are (useful for thresholds, KYC and export enforcement). Examples: FERC backing a PJM data center registry [search]; NJ's quarterly energy/water disclosure bill [read: DCW briefing].
- **Limits on secrecy:** e.g., Florida SB 484's restrictions on local-government NDAs [read][baxtel-jarvis]. This addresses a top local grievance and helps establish who the end users are.
- **Ratepayer protection / large-load tariffs:** chiefly a fairness win. Modest safety relevance, but it keeps the coalition focused on solvable problems.
- Possibly: **security standards** for very large facilities (physical security and model-weight protection) [bg; check for a source].

Close: backlash is an unreliable brake on AI, but a real force on *where* compute is built and *who* can afford to build it. That is where safety advocates should engage it.

---

## 6. Limitations and methods (~150 words, or a box)
- 21 hand-coded projects plus 68 from DCW's free briefings. The sample is biased toward large, publicized fights; ~10 per period; suggestive only.
- Paywalled analyses (SemiAnalysis, DCW) used only in their public portions. DCW's definitions are undisclosed (note whether DCW replied to the email).
- Capacity and chip figures mix definitions (IT vs facility power; US vs global). Presented as ranges.
- Human verification status of the 21 rows.

---

## Evidence to-do before drafting is final
1. Check the six judgment fields on the 21 rows; re-run `python3 analysis/summarize.py --md analysis/summary.md`.
2. Find citations for the [bg] items or cut them: per-chip power, EU 10^25 threshold, decentralized RL, security standards.
3. Open the [search] pages you cite (especially: UAE rule, GW Ranch, ballot tallies, CBRE vacancy).
4. Pick 1–2 citations for "some in the AI safety community favor slowing."

[epoch-compute]: https://epoch.ai/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year
[epoch-decentral]: https://epoch.ai/publications/could-decentralized-training-solve-ais-power-problem
[synmax]: https://blog.synmax.com/vulcan/placing-the-bust-why-the-ai-infrastructure-glut-lands-on-silicon
[woodmac]: https://www.woodmac.com/press-releases/us-data-centre-additions-return-to-growth-in-q2-2026-as-developers-push-construction-and-pipeline-continues-to-expand2
[dcmi]: https://www.dcmarketinsights.com/data/global-data-center-capacity
[dcw]: https://datacenterwatch.org/q1-2026
[heatmap]: https://heatmap.news/politics/local-opposition-data-center-cancellations
[semi-mor]: https://newsletter.semianalysis.com/p/everyone-says-datacenter-moratoriums
[semi-27]: https://newsletter.semianalysis.com/p/datacenters-2027-the-year-of-acceleration
[jll]: https://www.jll.com/en-us/insights/market-dynamics/north-america-data-centers
[hazelnut]: https://www.timesleader.com/news/1746909/project-hazlenut-developer-anounces-165-million-community-benefits-package-proposal
[rbs]: https://richmondbizsense.com/2026/05/28/hanover-supervisors-reject-data-center-project-on-mountain-road/
[gwranch]: https://constructionreviewonline.com/amazon-backs-7-65-gw-gas-plant-in-texas-to-power-new-ai-data-center-campus/
[rabobank]: https://www.rabobank.com/knowledge/d011524694-the-sprint-data-centers-are-building-a-parallel-energy-system-in-the-us
[cleanview]: https://www.cleanview.co/reports/behind-the-meter-data-centers
[latitude]: https://www.latitudemedia.com/news/developers-say-off-grid-data-centers-wont-be-a-huge-part-of-the-market/
[uae]: https://www.morganlewis.com/pubs/2026/07/bis-upgrades-uae-export-control-status-with-ai-chip-access-limited-to-approved-entities
[govai-uae]: https://www.governance.ai/research-paper/does-the-uae-have-an-advantage-in-building-data-centers
[noise]: https://www.potomaclocal.com/2025/06/11/data-center-noise-still-shakes-homes-in-great-oak-county-slow-to-act
[ballot]: https://www.planetizen.com/news/2026/11/138808-voters-across-country-reject-data-centers
[heim-thresholds]: https://blog.heim.xyz/training-compute-thresholds/
[govai-kyc]: https://www.governance.ai/research-paper/oversight-for-frontier-ai-through-kyc-scheme-for-compute-providers
[govai-compute]: https://www.governance.ai/research-paper/computing-power-and-the-governance-of-artificial-intelligence
[baxtel-jarvis]: https://baxtel.com/data-center/sentinel-grove-technology-park

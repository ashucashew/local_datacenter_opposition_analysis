# Outline: Can data center opposition be an AI safety lever?

Target: ~2,000 words. Deadline: Sun Nov 22 (London track 23:59 UK / 6:59 pm ET; DC track 11:59 pm ET).

Source tags: **[read]** = page read directly in this project. **[search]** = seen in search results only; open before citing. **[bg]** = background knowledge; find a source or cut.

Writing rules for every paragraph: open with the claim → give one or two numbers that carry it → close by tying back to the thesis. Sources go in footnotes. Anything that doesn't support the paragraph's claim gets cut.

---

## Intro: question and thesis (~200 words)

- **Framing (conditional, even-handed):** Some in the AI safety community favor slowing frontier AI development (cite one or two: the 2023 FLI pause letter; PauseAI) [bg: find sources]. Frontier progress has tracked compute: training compute for frontier models has grown ~4–5x a year [search][epoch-compute]. Data center opposition is the most visible public resistance to AI infrastructure. *Could riding that wave pace the frontier?*
- **Thesis:** No. US data center opposition is an unreliable and poorly aimed lever:
  1. It mostly costs developers time and money, not capacity, and they have backup options.
  2. The coalition's grievances can be bought off in ways that do not slow AI.
  3. Its effects fall on the wrong part of the system. The best-funded frontier labs are the last to be squeezed, while targeted compute-governance tools aim at the actual risk.

---

## Section 1. Developers route around opposition (~750 words)

**Section claim:** Opposition removes sites, not capacity. Developers have backup options and use them, and demand is strong enough that they keep paying to.

### ¶1.1 Concession: the delays are real, but small in aggregate
- **Topic sentence:** Opposition does impose measurable delays.
- **Evidence:** delays of ~8–15 months where measurable (Stokes County ~8 months; Hermantown ~12; Project Sail ~15, including a 180-day moratorium) [read: project rows P04, P05, P29 notes].
- **Scale:** SemiAnalysis finds only ~2.3 GW of US capacity actually delayed by moratoriums and New York's order [read][semi-mor], roughly **five weeks** of US buildout growth (≈ ln(1 + 2.3/70) / ln(1.4) × 52; assumes ~70 GW stock at end 2026 and ~40%/yr growth; order of magnitude only).
- **Tie-back:** real friction, but small next to the pace of the buildout.

### ¶1.2 Why the alarming headlines don't measure lost capacity: the funnel
- **Topic sentence:** The headline counts measure different stages of a development funnel in which most proposals never get built, opposition or not.
- **Evidence (one line or one small table):** ~700–780 GW publicly proposed → ~430 GW pipeline → ~200 GW with signed utility/construction agreements → ~60–80 GW under construction → ~25–40 GW delivered a year [read: SynMax citing Aurora][synmax]; [read][woodmac]; [read][semi-27].
- **The logic:**
  - **Early-stage counts** (Data Center Watch: ≥75 projects, ~$130B in Q1 2026, any mechanism, in dollars [read][dcw]; Heatmap: ≥20 cancellations, ≥3.5 GW [read][heatmap]) capture sites developers routinely lose. Losing them doesn't mean the capacity isn't built elsewhere.
  - **Late-stage counts** (SemiAnalysis's 2.3 GW) look at projects that have mostly cleared local hoops already, so they find little delay.
- **Tie-back:** neither count measures the thing that matters, which is whether capacity gets built somewhere.

### ¶1.3 Evidence: developers hold backup sites and route around opposition
- **Topic sentence:** The projects in Data Center Watch's own coverage show developers losing sites and continuing.
- **Our data:** 21 hand-coded projects plus 68 from DCW's free briefings. Most losses come at the first local-approval step (rezoning or special use permit). Few had a public tenant or power deal at the time: in the broad list, 3 of the 42 blocked or delayed projects named an end user. [read: data/projects.csv, data/broad_list.csv]
- **Several sites at once:**
  - **Tract** lost Mooresville (withdrawn Aug 2025) and Hanover Mountain Road (900 MW, denied May 2026) while continuing to develop its 1,200-acre Ashland campus [read][rbs].
  - **Prologis** was denied in Kosciusko County, IN (Apr 2025), then won approval for Project Sail, GA (900 MW, $17B, Apr 2026) [read][ajc-sail].
- **Routes around opposition** (word carefully, with NO causal claim about demand):
  - **lawsuit and settlement:** Saline Township, MI (denied Sept 2025, consent judgment Oct 2025, now under construction) [read][pd-saline];
  - **a different approving government:** Project Blue (Tucson said no; Pima County approved; but no confirmed tenant since AWS left in Dec 2025) [search][kold-blue];
  - **a delayed approval:** Hermantown, MN (Google; final approval Oct 2026, ~1 year after the pause) [read][mpr-herm].
- **Suggested sentence:** "Whether real demand drove these outcomes or followed them can't be determined from public records. Developers typically sign tenants after a site is approved."
- **Tie-back:** a lost site is usually a lost option, not lost capacity.

### ¶1.4 Escape valves when nearby sites get harder
- **Topic sentence:** Where opposition makes populated areas hard, developers are already moving to remote sites with their own power, and, at the margin, abroad.
- **Off-grid:** GW Ranch, Pecos County, TX: Amazon, 7.65 GW gas, "off-grid initially and designed for future grid interconnection" [search][gwranch]. SemiAnalysis expects 40 GW+ of US behind-the-meter data centers by 2028 [search]. On-site power costs ~$100–165/MWh vs ~$90–95 from the grid [search][rabobank]: more expensive, but affordable given the value of capacity (¶1.5). *Caveat (one clause):* ~90 GW announced, ~2 GW operating [search][cleanview]; off-grid still needs state air permits.
- **Abroad:** BIS moved the UAE into Country Group A:5 in July 2026, giving approved entities license-free access to advanced chips [search][uae]. SemiAnalysis says the ex-US buildout is accelerating, "largely driven by US challenges" [read][semi-27]. *Caveat (one clause):* rest-of-world additions are only ~4–8 GW a year; GovAI finds no intrinsic UAE cost advantage [read][govai-uae].
- **Tie-back:** each escape valve costs more, but stays open.

### ¶1.5 Why developers keep paying: value far exceeds cost, and the real limit is chips
- **Topic sentence:** Developers absorb these costs because capacity is worth far more, and the binding constraint on compute is increasingly chips, not buildings.
- **Value vs cost:**
  - Leases are worth ~$30–50B per GW over 15–20 years (~$1.5–3.3B per GW per year); ~$1T of binding leases were signed in 2026 [read][semi-27].
  - NorthPoint's $165M community-benefits package for ~300 MW ≈ 2–4 months of lease revenue, paid once [search][hazelnut].
- **Keeping pace with chips (rough):** power needed for chips shipped ≈ 15–30 GW (2026) and 30–45 GW (2027), against data center additions of ≈ 25 GW and 43–51 GW [search: JPMorgan units; bg: per-chip power; read: SemiAnalysis additions]. SemiAnalysis expects memory and logic chips to become the binding constraint in 2027–28 [read][semi-27]. State this conditionally: the ranges overlap.
- **Closing sentence:** "If data centers keep pace with chip supply, opposition delays buildings, not compute."

---

## Section 2. The coalition's grievances are negotiable (~200–250 words)

- **Signpost/topic sentence:** "Even where opposition bites, it is a brake the safety community can't steer, because its demands can be met without slowing AI."
- **What opponents want:** lower electricity bills, less noise, water protection, fair payment, transparency.
- **What developers and regulators are already doing:**
  - large-load tariffs that make data centers pay their own grid costs (Kansas ≥75 MW tariff; Oregon POWER Act; Georgia SB 34; Texas SB 6) [read: DCW briefings];
  - Microsoft's Jan 2026 pledge to pay rates covering its infrastructure and grid costs [read: DCW briefing];
  - community benefits (NorthPoint $165M; Saline ~$14M; Tract $15M for water) [read];
  - on-site power, which avoids sharing grid costs;
  - noise studies and setbacks (Tract's proffer in Hanover) [read][rbs].
- **Honest caveat (one sentence):** not all solved. Low-frequency hum falls outside A-weighted noise rules (Great Oak, VA) [search][noise], and regional capacity-market price effects persist. But every fix reduces opposition without reducing compute.
- **The "so what" for a lever:** a lever must be steerable. This one weakens on its own as developers pay their way through, whatever safety advocates want.

---

## Section 3. It aims at the wrong target (~400 words)

- **Topic sentence:** Even if opposition did tighten supply, the squeeze would fall last on the actors safety advocates care most about.
- **Frontier labs outbid everyone:** the largest single campuses are ~1–2 GW, against ~25–40 GW of US additions a year. OpenAI, Anthropic, Meta, Google, Microsoft and AWS are all signing gigawatt-scale leases [read][semi-27]. Remaining sites go to the highest bidders.
- **The squeeze falls on smaller players:** in our data, the developers that didn't recover were smaller ones: Energy Storage Solutions (lost Tarboro, then withdrew from Kingsboro) [read][cpp]; Karis Critical (denied in Naperville, withdrew in Hoffman Estates) [search]. Tighter supply also hits inference capacity and academic users first. A blunt brake may **concentrate** frontier compute among fewer, better-funded actors.
- **It can push compute somewhere harder to govern:** offshoring to jurisdictions with weaker oversight (the UAE). Arguably backlash's most important governance effect.
- **Progress isn't only compute scale:** algorithmic efficiency improves ~3x a year (Epoch; other estimates 2–6x) [search][epoch-compute]; RL rollouts and inference can be spread across many sites [bg; cite Epoch's decentralized-training piece][epoch-decentral].
- **Levers that target the risk** (brief here; expanded in the conclusion):
  - compute thresholds and reporting for large training runs [heim-thresholds];
  - know-your-customer rules for compute providers: cloud providers verify who rents frontier-scale compute and flag large training runs [govai-kyc];
  - export controls, which limit rivals' frontier compute and keep frontier clusters under oversight. Note the tension: loosening them (the UAE) is also an escape valve.
  - Overview: Sastry, Heim et al. [govai-compute].

---

## Counterarguments and rebuttals (~250 words)

| Counterargument | Rebuttal |
|---|---|
| **(Lead) Opposition is growing; future effects could be much larger.** | Concede it *could* slow the buildout, especially through state-level restrictions in the few key states (Texas's Sept 2026 permit pause puts 60+ GW under review [read][woodmac]). But it isn't steerable (Section 2), and the mistargeting gets *worse* with scale (Section 3). Separate "can it slow the buildout?" (possibly) from "is it an effective safety lever?" (no). Escalation evidence is mixed: 400+ moratoriums on ~18% of tracked sites [read][woodmac], record cancellations, restrictions winning in nearly all ~41 November ballot measures [search][ballot]; vs DCW Q2 ($68B) below Q1 ($130B) [search], 13 statewide bills died in 2026 [read][semi-mor], pipeline +29% a year [read][woodmac]. |
| **It's the most powerful grassroots AI politics right now.** | True, but aimed at local costs that developers can pay down. Channel it into shared policies (conclusion) rather than relying on it as a brake. |
| **Delays compound if construction is the bottleneck.** | Only in years when buildings, not chips, bind. Chips likely bind in 2027–28. Even with buildings binding, today's measured delay is weeks of growth. |
| **Even weeks matter if timelines are short.** | Concede that weeks matter more. But an unreliable lever that delivers weeks, falls on the wrong actors and may push compute abroad is worse than targeted tools. |

**Optional one-line strategic cost:** tying safety arguments to zoning fights muddles the safety case and costs credibility in a Washington that frames the buildout as competition with China. Do **not** claim foreign actors are stoking backlash (no evidence found).

**Signposts that opposition is becoming a real brake** (could close this section): state-level restrictions in TX, VA, GA, OH, PA; projects *with signed tenants* failing; time to construction lengthening year after year; cancellations exceeding new pipeline entries; the offshore share rising fast.

---

## Conclusion: what might work (~200 words)

- **Restate:** backlash is an unreliable brake on AI, but a real force on *where* compute is built and *who* can afford to build it.
- **Shared policies that serve both local opponents and safety; the common thread is transparency about who is building what, where:**
  - **public registries and disclosure for large data centers and loads** (size, power, operator): citizens get information; safety gets visibility into large clusters, which supports thresholds, KYC and export enforcement. Examples: FERC backing a PJM data center registry [search]; New Jersey's quarterly energy and water disclosure bill [read: DCW briefing];
  - **limits on secrecy**, e.g., Florida SB 484's restrictions on local-government NDAs [read][baxtel-jarvis]: answers a top local grievance and helps establish who the end users are;
  - **ratepayer protection and large-load tariffs**: mainly a fairness win, which keeps the coalition focused on solvable problems.
- **Final line:** point back to targeted compute governance as the lever that actually aims at the risk.

---

## Limitations (~50–100 words, short paragraph or footnote)
- 21 hand-coded projects plus 68 named in DCW's free briefings; biased toward large, publicized fights; suggestive only.
- Paywalled analyses (SemiAnalysis, DCW) used in their public portions only. DCW's definitions are undisclosed (note whether DCW replied to the email).
- Capacity and chip figures mix definitions (IT vs facility power; US vs global), so they're presented as ranges.

---

## To-do before submitting
1. Check the judgment fields on the 21 rows; rerun `python3 analysis/summarize.py --md analysis/summary.md` if any numbers above change.
2. Find citations for the [bg] items or cut them: pause-letter/PauseAI framing, per-chip power, decentralized RL.
3. Open the [search] pages you cite, especially the UAE rule, GW Ranch, ballot tallies and Hazelnut's $165M.
4. Confirm the Hermantown, Stokes and Sail delay figures against their sources.

[epoch-compute]: https://epoch.ai/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year
[epoch-decentral]: https://epoch.ai/publications/could-decentralized-training-solve-ais-power-problem
[synmax]: https://blog.synmax.com/vulcan/placing-the-bust-why-the-ai-infrastructure-glut-lands-on-silicon
[woodmac]: https://www.woodmac.com/press-releases/us-data-centre-additions-return-to-growth-in-q2-2026-as-developers-push-construction-and-pipeline-continues-to-expand2
[dcw]: https://datacenterwatch.org/q1-2026
[heatmap]: https://heatmap.news/politics/local-opposition-data-center-cancellations
[semi-mor]: https://newsletter.semianalysis.com/p/everyone-says-datacenter-moratoriums
[semi-27]: https://newsletter.semianalysis.com/p/datacenters-2027-the-year-of-acceleration
[rbs]: https://richmondbizsense.com/2026/05/28/hanover-supervisors-reject-data-center-project-on-mountain-road/
[ajc-sail]: https://www.ajc.com/business/2026/04/coweta-votes-to-turn-this-800-acre-forest-into-17b-data-center-campus
[pd-saline]: https://planetdetroit.org/2025/12/saline-data-center-settlement-challenge/
[kold-blue]: https://www.kold.com/2025/12/02/county-city-leaders-amazon-pulls-out-embattled-project-blue/?outputType=amp
[mpr-herm]: https://www.mprnews.org/story/2026/04/29/hermantown-residents-sue-to-block-proposed-google-data-center
[gwranch]: https://constructionreviewonline.com/amazon-backs-7-65-gw-gas-plant-in-texas-to-power-new-ai-data-center-campus/
[rabobank]: https://www.rabobank.com/knowledge/d011524694-the-sprint-data-centers-are-building-a-parallel-energy-system-in-the-us
[cleanview]: https://www.cleanview.co/reports/behind-the-meter-data-centers
[uae]: https://www.morganlewis.com/pubs/2026/07/bis-upgrades-uae-export-control-status-with-ai-chip-access-limited-to-approved-entities
[govai-uae]: https://www.governance.ai/research-paper/does-the-uae-have-an-advantage-in-building-data-centers
[hazelnut]: https://www.timesleader.com/news/1746909/project-hazlenut-developer-anounces-165-million-community-benefits-package-proposal
[noise]: https://www.potomaclocal.com/2025/06/11/data-center-noise-still-shakes-homes-in-great-oak-county-slow-to-act
[cpp]: https://carolinapublicpress.org/?p=73434
[ballot]: https://www.planetizen.com/news/2026/11/138808-voters-across-country-reject-data-centers
[heim-thresholds]: https://blog.heim.xyz/training-compute-thresholds/
[govai-kyc]: https://www.governance.ai/research-paper/oversight-for-frontier-ai-through-kyc-scheme-for-compute-providers
[govai-compute]: https://www.governance.ai/research-paper/computing-power-and-the-governance-of-artificial-intelligence
[baxtel-jarvis]: https://baxtel.com/data-center/sentinel-grove-technology-park

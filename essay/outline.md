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

## Section 1. Opposition acts on time and cost, not compute (~850 words)

**Section claim:** Opposition is real and growing, but it acts mainly on time and cost, early in the development funnel. Developers have backup options, and both the market and federal policy push the buildout forward.

### ¶1.1 Start with incentives: value far exceeds cost, and chips set the ceiling
- **Topic sentence:** What matters for AI progress is compute, and data centers only constrain it if buildings fall behind the chips available to fill them.
- **Value vs cost:**
  - Leases are worth ~$30–50B per GW over 15–20 years (~$1.5–3.3B per GW per year); ~$1T of binding leases were signed in 2026 [read][semi-27].
  - The costs opposition imposes are small by comparison: NorthPoint's $165M community-benefits package for ~300 MW ≈ 2–4 months of lease revenue, paid once [search][hazelnut]; on-site power at ~$100–165/MWh vs ~$90–95 from the grid [search][rabobank].
- **The ceiling is chips:** power needed for chips shipped ≈ 15–30 GW (2026) and 30–45 GW (2027), against data center additions of ≈ 25 GW and 43–51 GW [search: JPMorgan units; bg: per-chip power; read: SemiAnalysis additions]. SemiAnalysis expects memory and logic chips to become the binding constraint in 2027–28 [read][semi-27]. State this conditionally: the ranges overlap.
- **Closing sentence:** "As long as data centers keep pace with chip supply, opposition delays empty buildings, not compute."

### ¶1.2 Concession: real delays, but the industry keeps its pace
- **Topic sentence:** Opposition does impose measurable delays.
- **Evidence:**
  - Stokes County, NC: ~8 months (rezoned Jan 2026, voided Apr 2026 after a lawsuit, re-approved Sept 2026) [read][wfae-stokes] (candidate log C29);
  - Hermantown, MN: ~11–12 months (developer paused Nov 2025, final approval Oct 30 2026) [read][mpr-herm] (P05);
  - Project Sail, GA: approval took ~15 months from filing, including a 180-day moratorium [read][ajc-sail] (P04). That's total time to approval, not delay beyond a baseline, so word it that way.
- **Scale:** SemiAnalysis finds only ~2.3 GW actually delayed by moratoriums and New York's order [read][semi-mor], roughly **five weeks** of US buildout growth (≈ ln(1 + 2.3/70) / ln(1.4) × 52; ~70 GW stock at end 2026, ~40%/yr growth; order of magnitude only).
- **The industry keeps accelerating (verified):** capacity under construction rose from ~44 GW (end Q1 2026) to ~80 GW; the pipeline grew 54 GW in Q2 2026, +29% year on year [read][woodmac]. US hyperscaler construction starts are "going parabolic"; ~25 GW was delivered globally in 2026, with ~51 GW forecast for 2027 [read][semi-27]. *Nuance (one clause):* 2026 was tight (1.4% vacancy [search]), but mainly from grid-connection delays, not opposition.
- **Forward pointer (one sentence):** "Opposition is growing, so the question is whether these routes stay open. The rest of this section argues they do."

### ¶1.3 Why the alarming headlines don't measure lost capacity
- **Topic sentence:** The headline counts measure a development funnel in which most proposals never get built, opposition or not.
- **The funnel (one line):** ~700–780 GW publicly proposed → ~430 GW pipeline → ~200 GW with signed utility/construction agreements → ~60–80 GW under construction → ~25–40 GW delivered a year [read][synmax]; [read][woodmac].
- **The logic:**
  - **Early-stage counts** (Data Center Watch: ≥75 projects, ~$130B in Q1 2026, any mechanism, in dollars [read][dcw]; Heatmap: ≥20 cancellations, ≥3.5 GW [read][heatmap]) capture sites developers routinely lose. Our data agrees: most losses come at the first local-approval step, and few blocked projects had a public tenant or power deal (3 of 42 in the broad list named an end user) [read: data/broad_list.csv].
  - **The question that matters** is whether the capacity still gets built somewhere. That depends on backup options.

### ¶1.4 Backup options: routing around, moving away, and why not every developer needs to succeed
- **Topic sentence:** Developers hold many sites and have several ways around opposition.
- **Several sites at once:**
  - **Tract** lost Mooresville (Aug 2025) and Hanover Mountain Road (900 MW, May 2026) while continuing its 1,200-acre Ashland campus [read][rbs];
  - **Prologis** was denied in Kosciusko County, IN (Apr 2025), then won Project Sail, GA (900 MW, $17B, Apr 2026) [read][ajc-sail].
- **Routes around opposition** (NO causal claim about demand):
  - **lawsuit and settlement:** Saline Township, MI (denied Sept 2025, consent judgment Oct 2025, now under construction) [read][pd-saline];
  - **a different approving government:** Project Blue (Tucson said no; Pima County approved; no confirmed tenant since AWS left in Dec 2025) [search][kold-blue];
  - **a delayed approval:** Hermantown, MN (Google; ~1 year) [read][mpr-herm].
  - **Suggested sentence:** "Whether real demand drove these outcomes or followed them can't be determined from public records. Developers typically sign tenants after a site is approved."
- **Moving away and building their own power:** GW Ranch, Pecos County, TX: Amazon, 7.65 GW gas, "off-grid initially" [search][gwranch]. SemiAnalysis expects 40 GW+ of US behind-the-meter data centers by 2028 [search]. *Caveat (one clause):* ~90 GW announced, ~2 GW operating [search][cleanview]; still needs state air permits.
- **Counter → rebuttal:** "Some developers found alternatives, but not all will." True: the failures in our data were smaller developers (Energy Storage Solutions: Tarboro, then Kingsboro [read][cpp]; Karis: Naperville, then Hoffman Estates). **But the buildout doesn't need every developer to succeed, only enough sites to house the chips being made.** Developers hold ~10x more sites than get built each year, and others can absorb a failed developer's demand. (Point forward: who gets squeezed is the subject of Section 3.)

### ¶1.5 If routes narrow everywhere: the federal backstop
- **Topic sentence:** Even if local and state opposition spread widely, federal policy treats the buildout as a national priority and has tools that don't need state approval.
- **Executive tools (no Congress needed):**
  - **Allied sites abroad:** BIS moved the UAE into Country Group A:5 in July 2026, giving approved entities license-free access to advanced chips [search][uae]. SemiAnalysis says the ex-US buildout is accelerating, "largely driven by US challenges" [read][semi-27].
  - **Federal land and federal permitting:** state and local zoning generally doesn't apply on federal property [bg: cite DOE/federal-sites program and the 2025 permitting order, or cut].
- **Overriding states needs Congress:** legally possible (precedents: gas pipelines under the Natural Gas Act; cell towers under the 1996 Telecommunications Act [bg]), but politically hard now. Current bills *protect* local control: H.R. 10119, Protecting Local Control of Data Centers Act [read: congress.gov][hr10119]; Burchett's Community Control of Data Centers Act [search][burchett].
- **Caveats (one clause each):** rest-of-world additions are only ~4–8 GW a year; GovAI finds no intrinsic UAE cost advantage [read][govai-uae]; offshoring has its own governance costs (Section 3).

### ¶1.6 Tie together
- **Closing:** Compute gains are unlikely to be slowed much by opposition. Developers have many backup options, the value of capacity dwarfs the costs, the binding limit is increasingly chips, and federal policy backs the buildout, even though Congress has not moved to override local control.

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

## Counterarguments and rebuttals (~150–200 words)

| Counterargument | Rebuttal |
|---|---|
| *(Escalation is handled in Section 1, ¶1.2 and ¶1.4–1.5.)* | Escalation evidence to cite there if needed: 400+ moratoriums on ~18% of tracked sites [read][woodmac]; Texas's Sept 2026 permit pause (60+ GW under review) [read][woodmac]; restrictions won in nearly all ~41 Nov ballot measures [search][ballot]; vs DCW Q2 ($68B) below Q1 ($130B) [search]; 13 statewide bills died in 2026 [read][semi-mor]. |
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
[wfae-stokes]: https://www.wfae.org/2026-09-15/inside-stokes-countys-latest-vote-on-the-project-delta-data-center
[hr10119]: https://www.congress.gov/bill/119th-congress/house-bill/10119/text/ih
[burchett]: https://burchett.house.gov/media/press-releases/immediate-release-rep-burchett-introduces-bill-give-municipalities-control

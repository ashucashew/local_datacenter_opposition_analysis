# Project Brief: Does Local Opposition Slow US Compute Buildout?

## Purpose

Produce a short analytical essay (~2,000 words, PDF) as the writing sample for the GovAI Summer Fellowship 2027 application. It may later become the basis of a larger grant-funded project, so build the dataset to be reusable and extendable.

**Deadline:** Sunday Nov 22, 2026. DC track closes 11:59 pm ET; London research track closes 23:59 UK time (6:59 pm ET). Target: dataset done by Thursday Nov 19, draft by Saturday Nov 21.

## Research question

Two prominent estimates of how much local opposition is slowing US data center buildout disagree sharply. Why, and what does the answer imply for whether public backlash can meaningfully slow AI compute growth?

## Context: the two estimates

**SemiAnalysis (Sept 2026)**, "Everyone Says Datacenter Moratoriums Are Killing the US Buildout. We Mapped All 300 of Them."
https://newsletter.semianalysis.com/p/everyone-says-datacenter-moratoriums
- Mapped 400+ local instruments (300+ enacted moratoriums/bans) across 17 states against a pipeline of 6,000+ facilities.
- About 20 GW of planned capacity sits inside restricted local boundaries; only ~1,525 MW (7.6%) is genuinely delayed, almost entirely from three projects: an AWS campus in Ohio, a Pennsylvania powered-land campus, and a Colorado site.
- Including New York's state action, ~2.3 GW delayed nationally, against 38 GW of US IT capacity forecast for 2027.
- A project counts as delayed only if the moratorium passes all of roughly ten filters: it reaches the parcel, is in force, overlaps the project timeline, covers the use, blocks an approval the project still needs, can't be designed around, the project is still active, and no vested rights or carve-outs apply.
- Reasons most projects aren't affected: county moratoriums often don't reach incorporated cities; moratoriums usually freeze new applications, not existing approvals; vested rights and development agreements; annexation/deannexation (e.g., 444 acres removed from Brownsville, TX jurisdiction); short pauses that expire before later approvals are needed.
- **We only have the public (non-paywalled) portion.** Do not attempt to access paywalled content. Cite it as "the public portion of SemiAnalysis's analysis."

**Data Center Watch (10a Labs), Q1 2026 report**
https://datacenterwatch.org/q1-2026
- At least 75 projects worth ~$130B "blocked or delayed" by local opposition in Q1 2026 alone.
- The public page does not define "blocked," "delayed," what counts as a project, how dollar values are assigned, or the blocked/delayed split. Methodology is in a paid report.
- Earlier reports: Q2 2025 (~$98B blocked or delayed across 11 states), and others. Press coverage of these reports names individual projects; use that coverage to build the sample.

## Hypotheses for the gap

1. **Mechanism:** Data Center Watch counts all opposition (rezoning denials, withdrawn applications, lawsuits, public pressure); SemiAnalysis counts only formal moratoriums. SemiAnalysis may understate opposition's total effect.
2. **Project realness (likely the most important):** Developers often file applications and interconnection requests at many sites, expecting most to be cancelled or stall. A cancelled speculative project doesn't remove capacity anyone actually planned to build. Utilities and grid operators have publicly said large-load requests far exceed what will be built; find citable sources for this.
3. **Units:** announced dollar values vs megawatts of IT capacity.
4. **Relocation:** a project blocked in one jurisdiction may be built in another, so it counts as blocked locally but not as lost national capacity.

## Sample

- **Size:** ~20 projects.
- **Selection:** the largest named projects (by MW, or by announced dollar value if MW not reported) identified as blocked or delayed by local opposition, from Data Center Watch reports and press coverage of them, supplemented by other news coverage.
- **Period split:** ~10 projects whose opposition occurred in 2025 and ~10 from Q1–Q2 2026. The political landscape shifted significantly in 2026 (more moratoriums, the New York statewide moratorium, midterm ballot measures), so period is a variable, not something to pool over.
- **Document the selection:** keep a log of every candidate project considered and why it was included or excluded. The sample is biased toward large, publicized projects; the essay must say so.

## Data schema

One row per project. Save as `data/projects.csv`. Every non-obvious value needs a source link in the sources column.

| Column | Values / format | Notes |
|---|---|---|
| `project_id` | P01, P02, ... | |
| `project_name` | text | As commonly reported |
| `developer` | text | |
| `end_user` | text or `unknown` | Hyperscaler/tenant if named |
| `state`, `jurisdiction` | text | Jurisdiction = the city/county/township whose decision mattered |
| `period` | `2025` / `2026` | When the decisive opposition occurred |
| `size_mw` | number or blank | Reported IT or facility MW; note which in `notes`. Do **not** convert from dollars |
| `announced_value_usd` | number or blank | |
| `mechanism` | `moratorium` / `rezoning_denied` / `application_withdrawn` / `lawsuit` / `state_action` / `utility_or_power` / `other` | The proximate cause. If several, list primary first, separated by `;` |
| `stage_at_opposition` | `announced` / `land_optioned` / `land_closed` / `rezoning_filed` / `rezoning_approved` / `permitted` / `under_construction` | Furthest stage reached when opposition hit |
| `tenant_named` | `yes` / `no` / `unknown` | |
| `land_status` | `optioned` / `closed` / `unknown` | |
| `power_status` | `none` / `requested` / `studied` / `signed` / `unknown` | Only `signed` (interconnection or power agreement) counts as committed |
| `permits_or_financing` | `yes` / `no` / `unknown` | Building permits issued or construction financing announced |
| `developer_other_regional_sites` | `yes` / `no` / `unknown` | Same developer pursuing other sites in the region: evidence of a multi-option strategy |
| `realness_tier` | `speculative` / `committed` / `under_construction` | Derived; see definitions |
| `outcome` | `cancelled` / `delayed` / `dormant` / `proceeding` / `relocated` | See definitions |
| `delay_months` | number or blank | Only if `delayed` and a timeline is reported |
| `relocated_to` | text or blank | Only if `relocated` |
| `passes_semianalysis_filter` | `yes` / `no` / `unclear` | Would this case count as delayed under SemiAnalysis's published criteria? |
| `confidence` | `high` / `medium` / `low` | Overall confidence in the row |
| `human_verified` | `yes` / `no` | Set by the human reviewer only |
| `sources` | URLs separated by `;` | |
| `notes` | text | Ambiguities, judgment calls |

## Definitions and coding rules

**Realness tier**
- `speculative`: only applications, rezoning filings, or interconnection requests; no named tenant, no signed power agreement.
- `committed`: a named tenant/end user **or** a signed power/interconnection agreement, but not yet under construction.
- `under_construction`: construction had begun.

**Outcome** (as of the date of coding)
- `cancelled`: the developer withdrew or announced the end of the project.
- `delayed`: still active, but behind its originally stated timeline.
- `dormant`: no public activity for 6+ months, and no announcement of cancellation.
- `proceeding`: moving forward roughly on schedule despite opposition.
- `relocated`: **only** if the developer or credible press explicitly links a new site to the lost one. Do not infer relocation from timing or from the same developer announcing a project elsewhere. Without an explicit link, code the original outcome and note the possible relocation in `notes`. Any relocation share found is therefore a lower bound.

**Passes SemiAnalysis filter**: `yes` only if the mechanism is a formal moratorium (or state action) that applied to the parcel and blocked an approval the project still needed, with no vested rights or carve-outs. Rezoning denials, withdrawals, and lawsuits are `no` by construction, which is the point: it shows what their method excludes.

**Unknowns**: use `unknown` honestly. Never fill a field from inference alone. A high share of unknowns is itself a finding about how thin the evidence behind headline totals is.

## Sources and constraints

- **Public sources only:** news, local government meeting minutes and agendas, developer and utility announcements, court records, public reports.
- **Do not use any data, code, notes, or client information from my former employer (Paces).** General knowledge of how permitting and interconnection work is fine.
- Do not access paywalled content by circumventing paywalls.
- Prefer primary sources (meeting minutes, filings, developer statements) over aggregator articles where possible.

## Division of labor

- **AI (first pass):** find candidate projects, gather sources, fill in a first pass of every row, flag uncertainty in `notes` and `confidence`.
- **Human (verification):** personally review and confirm the judgment-heavy fields for every row: `mechanism`, `stage_at_opposition`, `power_status`, `realness_tier`, `outcome`, `passes_semianalysis_filter`. Set `human_verified = yes` only after review.

## Analysis to produce

1. Counts and MW/$ totals by `mechanism`, `realness_tier`, `outcome`, and `passes_semianalysis_filter`.
2. The same broken out by `period` (2025 vs 2026). With ~10 per group, treat differences as suggestive, not conclusive.
3. The share of sampled blocked/delayed capacity that is (a) speculative, (b) caused by non-moratorium mechanisms, (c) explicitly relocated.
4. A short table suitable for the essay, plus a one-paragraph plain-language summary of what the sample shows.

Keep analysis in a script (e.g., `analysis/summarize.py`) that reads `data/projects.csv`, so it reruns when rows change.

## Essay outline (~2,000 words)

**Working title:** Counting moratoriums is not counting megawatts: what local opposition does and doesn't do to US compute

1. **Reconcile the numbers (~800 words).** The two estimates measure different things. Present the hypotheses, then the hand-coded sample as evidence on which explains the gap.
2. **Why local restrictions rarely bind (~400 words).** Jurisdiction, development stage, vested rights, annexation, redesign; add domain knowledge of permitting.
3. **What could bind (~400 words).** State executive actions (New York environmental permits, Texas interconnection pause), state legislation (SemiAnalysis counts 13 statewide bills that died in 2026; the midterms may change that), countervailing trends such as behind-the-meter power from 2028.
4. **Implications for AI governance (~400 words).** Backlash as an unreliable brake on AI progress in the near term; its likelier effect on where compute is built and who can afford to build it; whether relocation is getting harder in 2026 (discussion point, not a claim the sample can settle); what evidence would change the conclusion.

Include a short methods note and a limitations paragraph (sample size, selection bias toward large/publicized projects, reliance on public portions of paywalled analyses, Data Center Watch's undisclosed methodology).

## Open follow-ups (not required for the deadline)

- Email Data Center Watch (info@datacenterwatch.org) asking for their definitions of "blocked" and "delayed" and their inclusion threshold; note in the essay whether they replied.
- After submission: publish the essay, then consider extending the dataset (more projects, megawatt-weighted tracking of the largest announced campuses) as the grant project.

## Suggested repo layout

```
PROJECT_BRIEF.md
data/projects.csv
data/candidates_log.csv     # every project considered, included or not, and why
sources/                    # saved copies or notes for key sources
analysis/summarize.py
essay/draft.md
```

---
title: "Skillit Construction Wage Data"
type: source
created: 2026-05-05
updated: 2026-06-12
status: good
tags: [data-provider, employment, alternative-data, ai-trading, construction]
aliases: ["Skillit", "Skillit Wage Platform", "Skillit Construction Labor Pricing"]
source_type: data
source_url: "https://www.skillit.com/"
confidence: medium
related: ["[[skilled-trades-wage-boom]]", "[[ai-data-center-power-demand]]", "[[capital-vs-labor-asymmetry]]", "[[wage-compression-vs-job-loss]]", "[[employment]]", "[[alternative-data-providers]]", "[[macro-data-sources]]", "[[data-sources-overview]]", "[[randstad-job-postings]]", "[[bls-benchmark-revisions]]"]
---

# Skillit Construction Wage Data

**Skillit** is a construction-industry labor-pricing and workforce-platform provider whose wage data is referenced in AI-recession research as the cleanest tape for the **AI infrastructure labor scarcity** narrative. While [[randstad-job-postings|Randstad]] tracks job-posting volumes, Skillit tracks **what construction workers are actually paid** — the price-side complement to Randstad's quantity-side data. (Source: [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]])

## What It Tracks

Skillit captures construction labor pricing at the project, role, and regional level. The headline data point most relevant for AI-recession traders (Source: [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]]):

| Metric | Value |
|--------|-------|
| **Average data-center construction worker pay** | $81,800 / year |
| **Equivalent hourly rate** | $39.33 / hour |
| **Premium vs. non-data-center construction work** | **~32%** |

This 32% premium is the direct, dollarized measurement of the [[ai-data-center-power-demand|AI data-center buildout]] bidding skilled trades labor away from non-AI construction projects (housing, commercial, transportation). It is the sharpest single number documenting [[capital-vs-labor-asymmetry|capital-biased AI capex]] flowing into wages — but only for the narrow slice of labor working on hyperscaler sites.

## Why It Matters for AI-Recession Analysis

The AI-recession thesis hinges on two simultaneous claims:

1. **White-collar roles** are seeing employment fall and wages compress (15–40% pay cuts on re-employment per [[wage-compression-vs-job-loss]]).
2. **Skilled trades on AI infrastructure** are seeing wages explode (electricians at $240K–$280K under-30 in Plano data centers per [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]]).

Skillit provides the empirical price tape for claim #2 at industry granularity, not anecdote. It also makes the divergence visible: a construction worker on a residential project earns ~$62,000; the same skill set on a data-center project earns $81,800 — a 32% premium that exists not because the work is harder but because hyperscalers can outbid traditional construction. That outbidding is the [[ai-data-center-power-demand]] thesis in dollar-per-hour form.

For traders, Skillit data:

- **Confirms or breaks the trades-wage-boom thesis.** If the data-center premium narrows toward zero, hyperscaler capex is decelerating before earnings reveal it.
- **Quantifies the inverse trade.** When the premium widens, contractors and electrical-services equities exposed to hyperscaler buildouts (e.g., EMCOR, Quanta Services, Comfort Systems) gain pricing power.
- **Cross-checks [[randstad-job-postings|Randstad]] posting demand.** Postings can rise without wages rising if employers fail to fill them; Skillit closes the loop.
- **Maps to [[bls-benchmark-revisions|BLS]] OEWS occupation wage data.** Skillit leads the BLS annual OEWS release because it is project-priced in real time.

## Access

| Detail | Value |
|--------|-------|
| **Provider** | Skillit, Inc. |
| **URL** | [skillit.com](https://www.skillit.com/) |
| **Primary product** | Construction workforce / labor-pricing platform for general contractors and project owners |
| **Public data distribution** | Periodic blog posts, press releases, and reports referenced by financial press |
| **Cost** | Platform is paid (enterprise SaaS for contractors); aggregate wage stats released free |
| **API** | No standardized public API for wage data; aggregate prints are released in report form |

Skillit's full per-project data is proprietary. Traders should expect to consume it through:

1. Skillit's published industry reports and blog
2. Coverage in financial / construction press (Fortune, ENR, Construction Dive)
3. Citations in AI-infrastructure research notes (e.g., the source feeding this wiki)

## Gotchas / Caveats

- **Confidence: medium.** Skillit is a private platform; the methodology behind its wage averages and the size of its data-center sample are not fully transparent in public materials.
- **Sample bias toward platform users.** Skillit's data reflects projects that use its platform — likely larger, more sophisticated general contractors. Wages on smaller / informal jobs may diverge.
- **Geographic skew.** Data-center premiums are concentrated in specific metros (Northern Virginia, Plano/Dallas, Phoenix, Columbus, Atlanta). National averages can mask local wage explosions of 60–100%.
- **Wage ≠ total comp.** Reported figures are typically base wages; data-center contractors often pay overtime, per-diem, and completion bonuses on top. Total comp can exceed published averages by 20–40%.
- **Thin time series.** As a relatively young platform, Skillit's historical depth is limited compared to BLS OEWS (annual since the 1990s). Trend extrapolation should be cautious.
- **Cycle sensitivity.** If hyperscaler capex pauses, the 32% premium can collapse quickly. The data is highly cyclical, not structural.

## Use Cases

- **Size positions in electrical / mechanical contractors** (Quanta Services, EMCOR, Comfort Systems, MasTec) using the data-center premium as a pricing-power proxy.
- **Time the capex cycle.** A narrowing premium signals the AI buildout is hitting a soft patch before quarterly capex guidance from Microsoft, Meta, Amazon, or Google reveals it.
- **Validate the [[skilled-trades-wage-boom]] inverse-trade thesis.** Combine Skillit (price) + [[randstad-job-postings|Randstad]] (quantity) + [[bls-benchmark-revisions|BLS]] OEWS (lagging confirmation) for a three-source picture.
- **Map regional municipal-bond exposure.** Metros with the largest data-center premiums also generate the largest local payroll-tax bases — relevant for fiscal-strength assessments offsetting [[capital-vs-labor-asymmetry|tech-hub fiscal drag]] elsewhere.

## Related

- [[skilled-trades-wage-boom]]
- [[ai-data-center-power-demand]]
- [[capital-vs-labor-asymmetry]]
- [[wage-compression-vs-job-loss]]
- [[employment]]
- [[randstad-job-postings]]
- [[bls-benchmark-revisions]]
- [[alternative-data-providers]]
- [[macro-data-sources]]
- [[data-sources-overview]]

## Sources

- (Source: [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]])
- Skillit corporate site — [skillit.com](https://www.skillit.com/)

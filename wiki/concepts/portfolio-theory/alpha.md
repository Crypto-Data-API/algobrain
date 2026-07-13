---
title: "Alpha"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [portfolio-theory, quantitative, risk-management]
aliases: ["Alpha", "Jensen's Alpha", "Excess Return"]
related: ["[[beta]]", "[[capital-asset-pricing-model]]", "[[alpha-model]]", "[[alpha-decay]]", "[[sharpe-ratio]]", "[[edge-taxonomy]]", "[[multi-factor-portfolio]]", "[[market-timing]]", "[[benchmark]]", "[[information-ratio]]"]
domain: [portfolio-theory]
prerequisites: ["[[capital-asset-pricing-model]]", "[[beta]]"]
difficulty: intermediate
---

**Alpha** is the return of an investment in excess of what a risk model predicts — the part of performance attributable to skill, an exploited [[edge-taxonomy|edge]], or mispricing rather than to passive exposure to market or factor risk ([[beta]]). It is the central object of active management: beta can be bought cheaply through index funds, so the only thing worth paying active fees for is genuine, persistent alpha measured against an appropriate [[benchmark]].

## Definition

In the single-factor [[capital-asset-pricing-model|CAPM]] world, **Jensen's alpha** is the intercept of the regression of an asset's excess returns on the market's excess returns:

$$ \alpha_i = \big(R_p - R_f\big) - \beta_i \big(R_m - R_f\big) $$

Equivalently, written out as "actual return minus CAPM-required return":

$$ \alpha = R_p - \big[\, R_f + \beta(R_m - R_f) \,\big] $$

where $R_p$ is the portfolio (or asset) return, $R_f$ the risk-free rate, $R_m$ the market/[[benchmark]] return, and $\beta$ the portfolio's [[beta]] to the market. A positive $\alpha$ means the asset returned more than its beta-implied compensation for systematic risk; a negative $\alpha$ means it underperformed for the risk taken. In a [[multi-factor-portfolio|multi-factor model]] (Fama-French, Carhart), alpha is the intercept *after* controlling for size, [[value-factor|value]], momentum, and quality — a much higher bar, because returns that look like "skill" under CAPM often turn out to be uncompensated factor tilts.

## Worked Example — Jensen's Alpha

Suppose a fund delivered the following over a year:

| Input | Symbol | Value |
|-------|--------|-------|
| Portfolio return | $R_p$ | 14% |
| Risk-free rate | $R_f$ | 3% |
| Market (benchmark) return | $R_m$ | 10% |
| Portfolio beta | $\beta$ | 1.2 |

CAPM-required return = $R_f + \beta(R_m - R_f) = 3\% + 1.2 \times (10\% - 3\%) = 3\% + 8.4\% = 11.4\%$.

Jensen's alpha = $R_p - 11.4\% = 14\% - 11.4\% = \mathbf{+2.6\%}$.

The fund beat the index by 4 percentage points (14% vs 10%) in raw terms, but **most of that outperformance was just leverage to the market** (beta of 1.2). After charging for the extra systematic risk taken, only **+2.6%** is genuine alpha. Note how fragile this is: if the manager charges a 2% fee, net alpha is just +0.6%; raise the beta estimate to 1.5 and the CAPM-required return becomes 13.5%, collapsing alpha to +0.5%. Alpha conclusions are extremely sensitive to the beta estimate and the chosen [[benchmark]].

## Alpha vs. Beta

- **Beta** is exposure to a known, priced risk — owning the market, a sector, a factor. It is cheap and replicable.
- **Alpha** is return that survives after stripping out all known betas. It is scarce, capacity-constrained, and tends to erode (see [[alpha-decay]]).

A fund returning 12% when its factor exposures imply 11% has 1% of gross alpha — which fees, costs, and slippage can easily turn negative. This is why most active managers underperform their benchmark net of costs: their gross alpha is real but smaller than their fee.

| Dimension | Beta | Alpha |
|-----------|------|-------|
| What it is | Exposure to priced risk (market/factor) | Return after stripping out all known betas |
| Source | Owning the market, sector, or factor | Skill, edge, mispricing |
| Cost to obtain | Cheap — index funds, futures | Expensive — active fees, research, infrastructure |
| Replicable? | Yes, trivially | No, scarce and contested |
| Capacity | Effectively unlimited | Finite; decays with AUM and crowding |
| Persistence | Permanent (the risk premium) | Erodes ([[alpha-decay]]) |
| Fair fee | ~basis points | Performance fee territory (if real) |

## Trading and Portfolio Relevance

- **Attribution.** Decomposing returns into alpha and beta tells you whether a strategy is genuinely adding value or just levering up market exposure. The same logic flags closet indexers — funds charging active fees for what is mostly beta.
- **The [[information-ratio|Information Ratio]]** ($\alpha$ divided by tracking error) measures alpha *per unit of active risk* — the cleanest scorecard for an active manager, analogous to a [[sharpe-ratio]] for active bets. The **Fundamental Law of Active Management** (Grinold) states IR ≈ IC × √(breadth): skill per bet times the number of independent bets, so even a small edge applied across many uncorrelated positions can compound into a high information ratio.
- **Sources of alpha** map to the [[edge-taxonomy]]: behavioral, structural, informational, analytical, and latency edges. Each is contestable and finite.
- **Portable alpha.** A skill that produces alpha in one market can be combined with cheap beta elsewhere (e.g. earn alpha in a market-neutral book, overlay S&P futures for beta), separating the two return streams.
- **Where alpha hides.** Genuine alpha tends to live in less-efficient corners — small caps, distressed credit, niche derivatives, fast-moving event-driven situations — where fewer analysts compete and information is harder to acquire.

## Caveats and Common Pitfalls

Apparent alpha is frequently disguised risk — illiquidity premium, tail risk, leverage, or survivorship bias — that has not yet shown up as a loss. "Picking up nickels in front of a steamroller" earns smooth positive alpha until the steamroller arrives. Specific traps:

- **Wrong benchmark.** Alpha is meaningless without the right [[benchmark]]. Measure a small-cap value fund against the S&P 500 and you will credit a factor tilt as skill.
- **Beta misestimation.** As the worked example shows, alpha swings hard with the beta input; a noisy or rolling beta can manufacture or erase alpha.
- **Uncompensated factor tilts.** CAPM alpha that vanishes once you control for size/[[value-factor|value]]/momentum/quality was never skill — it was a factor bet in disguise.
- **Short samples and luck.** With high return volatility, several years are needed before alpha is statistically distinguishable from luck (Fama-French, 2010). Beware [[alpha-decay]] and data-mined backtests.
- **Costs and capacity.** Gross alpha that does not survive realistic transaction costs, slippage, and the fee load is not investable alpha. Crowding shrinks it further as AUM grows.

Robust alpha must survive realistic cost overlays, out-of-sample testing, and a [[multi-factor-portfolio|multi-factor]] control set before it should be trusted.

## Related

- [[beta]] — the exposure alpha is measured against
- [[capital-asset-pricing-model]] — the model that defines Jensen's alpha
- [[alpha-model]] — the engine that forecasts alpha in a quant system
- [[alpha-decay]] — the erosion of alpha over time
- [[edge-taxonomy]] — the categories of genuine alpha sources
- [[benchmark]] — the reference return alpha is measured against
- [[information-ratio]] — alpha per unit of active risk; the active-management scorecard
- [[sharpe-ratio]] — risk-adjusted return; the Information Ratio is its active-management analogue

## Sources

- Jensen, Michael C. "The Performance of Mutual Funds in the Period 1945-1964." *Journal of Finance* (1968).
- Grinold, Richard, and Ronald Kahn. *Active Portfolio Management* (2000) — the canonical treatment of alpha, the Information Ratio, and the Fundamental Law.
- Fama, Eugene F., and Kenneth R. French. "Luck versus Skill in the Cross-Section of Mutual Fund Returns." *Journal of Finance* (2010).

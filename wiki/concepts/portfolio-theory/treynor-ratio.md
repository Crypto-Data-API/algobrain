---
title: "Treynor Ratio"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [portfolio-theory, risk-management, quantitative]
aliases: ["Treynor Ratio", "Treynor Measure", "Reward-to-Volatility Ratio"]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[beta]]", "[[capm]]", "[[expected-return]]"]
difficulty: intermediate
related: ["[[sharpe-ratio]]", "[[information-ratio]]", "[[sortino-ratio]]", "[[capm]]", "[[beta]]", "[[alpha]]", "[[modern-portfolio-theory]]", "[[diversification]]"]
---

The **Treynor ratio** measures the excess return a portfolio earns per unit of *systematic* risk, where systematic risk is captured by [[beta]] rather than total volatility. Developed by Jack Treynor (see [[jack-treynor]]), it is the [[capm|CAPM]]-native risk-adjusted return metric: it rewards a portfolio for return earned above the risk-free rate relative to how much undiversifiable market risk it carries. It is the close cousin of the [[sharpe-ratio|Sharpe ratio]] — same numerator, different denominator — and the choice between them hinges on whether the portfolio's risk is mostly market risk or also includes diversifiable, idiosyncratic risk.

## Formula

```
Treynor Ratio = (R_p − R_f) / β_p
```

Where:
- **R_p** = portfolio return
- **R_f** = risk-free rate (e.g. a short-dated [[treasury-bonds|Treasury]] yield)
- **β_p** = the portfolio's [[beta]] — its sensitivity to the benchmark/market

The numerator is the **risk premium** the portfolio actually earned; the denominator scales it by the portfolio's exposure to systematic market movements. Geometrically, the Treynor ratio is the slope of the line from the risk-free asset to the portfolio in **return-vs-beta** space — exactly the security-market-line view of [[capm|CAPM]], whereas the Sharpe ratio is the slope in return-vs-total-volatility space.

## Sharpe vs Treynor: the key distinction

| | Numerator | Denominator (risk) | Assumes |
|---|---|---|---|
| **[[sharpe-ratio\|Sharpe]]** | excess return | total [[standard-deviation\|standard deviation]] | risk = all volatility |
| **Treynor** | excess return | [[beta]] (systematic risk only) | idiosyncratic risk already [[diversification\|diversified]] away |

- Use **Treynor** when the portfolio is **well-diversified** and forms part of a larger book, so that only its market risk matters (its idiosyncratic risk has been diversified away at the portfolio level). This is the natural metric for ranking sub-portfolios or funds that will be combined.
- Use **Sharpe** when the portfolio is held in isolation or is **not** fully diversified, so total volatility — not just beta — is the relevant risk.

For a perfectly diversified portfolio the two rankings agree; the more idiosyncratic (single-name, concentrated) risk a portfolio carries, the more the two diverge.

## Interpretation

- **Higher is better** — more reward per unit of market risk borne.
- Like the Sharpe ratio, the absolute number is only meaningful **in comparison** to other portfolios or to the market itself, measured over the same period with the same risk-free rate.
- A negative Treynor ratio usually means the portfolio underperformed the risk-free rate (negative numerator) — but beware: if β is negative, the sign flips and the ratio becomes hard to interpret, one of its known weaknesses.
- The benchmark Treynor ratio is the **[[equity-risk-premium|market risk premium]]** itself, since the market has β = 1 by definition: `(R_m − R_f) / 1`. A portfolio beating that ratio delivered more excess return per unit of beta than simply holding the index.

## Worked example (hypothetical)

*Illustrative arithmetic, not a forecast.* Compare two funds against a risk-free rate of **4%**:

| Fund | Return R_p | Beta β | Treynor = (R_p − R_f) / β |
|---|---|---|---|
| A | 14% | 1.25 | (0.14 − 0.04) / 1.25 = **0.080** |
| B | 11% | 0.70 | (0.11 − 0.04) / 0.70 = **0.100** |

Fund A earns the higher *raw* return, but Fund B delivers more excess return per unit of market risk (0.100 vs 0.080), so on a Treynor basis **B is the superior risk-adjusted performer**. An allocator who can lever exposure up or down cares about this per-unit-of-beta efficiency, not the headline return. Note that Sharpe and Treynor could disagree here if the funds differ in idiosyncratic risk — that disagreement is itself informative about how concentrated each book is.

## Limitations

1. **Relies on beta being meaningful.** Treynor assumes a single-factor [[capm|CAPM]] world where market beta captures the relevant risk. If returns are driven by other factors (value, momentum, credit) or the relationship to the market is non-linear, beta is an incomplete risk measure.
2. **Beta is estimated and unstable.** β is computed from historical regression and varies with the window, the benchmark chosen, and the regime — estimation error flows straight into the ratio.
3. **Breaks down for low or negative beta.** A near-zero beta makes the ratio explode; a negative beta makes its sign ambiguous. Market-neutral and long-short books are poorly served by Treynor.
4. **Ignores idiosyncratic risk entirely.** For a concentrated or undiversified portfolio this is exactly the wrong assumption — the [[sharpe-ratio|Sharpe ratio]] is more appropriate there.
5. **Backward-looking and benchmark-dependent.** Like all such ratios it summarizes the past and depends on the choice of benchmark and risk-free rate.

## Related

- [[sharpe-ratio]] — same numerator, uses total volatility instead of beta
- [[information-ratio]] — benchmark-relative skill measure (active return / tracking error)
- [[sortino-ratio]] — downside-only risk-adjusted return
- [[capm]] — the equilibrium model Treynor is built on
- [[beta]] — the systematic-risk denominator
- [[alpha]] / [[jack-treynor]] — Jensen's alpha and the metric's originator
- [[diversification]] — the assumption that justifies ignoring idiosyncratic risk

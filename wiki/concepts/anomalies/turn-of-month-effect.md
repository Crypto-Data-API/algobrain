---
title: "Turn-of-the-Month Effect"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, stocks, quantitative, liquidity]
aliases: ["Turn-of-the-Month Effect", "Turn-of-Month Effect", "TOM Effect", "Month-End Rally"]
domain: [anomalies]
prerequisites: ["[[anomalies-overview]]", "[[calendar-effects-anomalies]]"]
difficulty: beginner
related: ["[[anomalies-overview]]", "[[calendar-effects-anomalies]]", "[[rebalancing-flows]]"]
---

# Turn-of-the-Month Effect

Equity returns are disproportionately concentrated in the last few trading days of one month and the first few of the next — roughly a 4-5 day window spanning month-end. Across several decades of US data, this window accounts for essentially *all* of the cumulative return on the S&P 500, while the rest of the month averages zero. It is one of the more persistent calendar effects and, unlike most, has held up out-of-sample.

## What

Define the turn-of-month window as the last trading day of month M through the first three trading days of month M+1 (sometimes 4 trading days total, sometimes 5 depending on the study). Compute average returns in this window versus all other trading days. In Ariel's original US sample (1963-1981), the turn-of-month window earned 0.8% per 4-day window while the rest of the month averaged zero.

## Original Paper

Ariel, R. (1987) "A Monthly Effect in Stock Returns" — *Journal of Financial Economics*. Refined by Lakonishok & Smidt (1988) and extended internationally by Agrawal & Tandon (1994).

## Mechanism

Persistent cash flows at month-end drive predictable demand for equities:

- **Pension and 401(k) contributions** — employer and employee retirement contributions are typically invested at or shortly after month-end, producing mechanical buy pressure
- **Monthly dividend reinvestment** from income-oriented mutual funds
- **Month-end window dressing** by institutional managers
- **Index fund rebalancing** at month-end to track benchmarks
- **Corporate pension funding** on a monthly schedule

Because the underlying flows are structural and mandatory, the effect has proven harder to arbitrage away than behavioral calendar anomalies like the Monday effect.

## Edge Category

**Structural** — flow-driven price pressure. See [[edge-taxonomy]] and [[rebalancing-flows]].

## Replication Status

Robustly replicated. McConnell & Xu (2008) confirmed the effect persists in US data through 2005. International replications (Cadsby & Ratner 1992, Agrawal & Tandon 1994) show it in most developed markets.

## Decay History

Mild decay but the effect survives. McConnell & Xu (2008) found that in the 1987-2005 post-Ariel period the turn-of-month window still accounted for the bulk of cumulative equity returns. This is surprising given publication-driven decay in most other calendar effects.

## Current Viability

Still detectable as a small positive bias. Magnitude (10-30 bps per window) is too small to justify dedicated trading after costs, but:

- Long-only portfolios that are *slightly* overweight equities in the 4-day window outperform passive holdings on a risk-adjusted basis
- Market-makers and intraday strategies can tilt inventory to capture the flow
- Useful as a feature in multi-factor intraday models

## Related Strategies

- [[rebalancing-flows]] — month-end pension and index flows are the mechanism
- [[calendar-effects-anomalies]] — broader family
- Closing-auction strategies that capture the end-of-day index fund flows

## Sources

- Ariel (1987) — original paper
- Lakonishok & Smidt (1988) "Are Seasonal Anomalies Real? A Ninety-Year Perspective"
- McConnell & Xu (2008) "Equity Returns at the Turn of the Month"
- Agrawal & Tandon (1994) international replication

## Related

- [[anomalies-overview]]
- [[calendar-effects-anomalies]]
- [[rebalancing-flows]]

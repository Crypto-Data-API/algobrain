---
title: "Sector Neutrality"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [portfolio-theory, quantitative, risk-management, factor-investing, correlation]
aliases: ["Sector Neutral", "Sector-Neutral", "Industry Neutrality", "Sector Hedging"]
related: ["[[long-short-equity]]", "[[factor-investing]]", "[[gics-sector]]", "[[risk-budgeting]]", "[[correlation]]", "[[statistical-arbitrage]]", "[[pairs-trading]]", "[[momentum]]"]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[long-short-equity]]", "[[correlation]]"]
difficulty: advanced
---

Sector neutrality is a portfolio-construction constraint that holds the net exposure to each industry sector at (or near) zero, so that the portfolio's returns are driven by *within-sector* stock selection rather than by bets on which sectors rise or fall. It is a standard discipline in [[long-short-equity|long-short equity]] and quantitative factor strategies, where the goal is to isolate stock-specific alpha and strip out the large, slow-moving sector factor that would otherwise dominate the return stream.

## Overview

A long-short book that simply buys the highest-ranked stocks and shorts the lowest-ranked ones will often, by accident, become a giant sector bet. If a [[value-investing-strategy|value]] signal ranks energy and financials cheap and ranks technology expensive, the unconstrained portfolio ends up long energy/financials and short tech — and its day-to-day P&L is then dominated by the energy-vs-tech sector spread, not by the manager's stock-picking skill. Sector neutrality forces the long and short dollar (or beta) exposure within each sector to offset.

Mechanically, sectors are usually defined by a classification scheme such as [[gics-sector|GICS]] (11 sectors) or its finer industry-group / industry levels, or by statistically estimated factors. The constraint can be imposed at several strengths:

- **Dollar-neutral by sector** — equal long and short dollar value within each sector.
- **Beta-neutral by sector** — equal beta-weighted exposure, accounting for the fact that high-beta and low-beta names contribute unequally to risk.
- **Soft neutrality** — a penalty term in the optimizer that discourages, but does not forbid, sector tilts (allows small deliberate sector views while keeping them bounded).

In an optimizer this appears as a linear constraint:

```
for each sector s:
    sum(w_i for i in s) = 0          # dollar-neutral
    # or
    sum(w_i * beta_i for i in s) = 0 # beta-neutral
```

## Why it matters

- **Risk isolation.** Sector returns are highly [[correlation|correlated]] within a sector and represent a large common factor. Removing the sector bet shrinks portfolio variance that is not compensated by the manager's edge.
- **Cleaner attribution.** With sector neutrality, performance attribution can credibly claim "this is stock selection," not "we got lucky being overweight tech in a tech rally."
- **Avoiding crowded macro bets.** Many quant signals load on the same sectors at the same time; an unhedged sector tilt is a hidden, crowded factor exposure shared across the industry (a [[crowding-risk|crowding]] hazard).
- **Drawdown control.** Sector rotations and sector-specific shocks (e.g. a regulatory action on banks, an oil price collapse) can cause large losses for a book that is implicitly long one sector and short another.

## Trade-offs and limits

Sector neutrality is not free:

- **It can hedge away real alpha.** If a signal genuinely predicts sector returns (some momentum and macro signals do), neutralizing sectors discards that information. The choice is whether sector predictability is part of the edge or part of the noise.
- **Classification is imperfect.** GICS assigns each company to one sector, but conglomerates and platform companies span several; mis-classification leaks unintended exposure. Statistical/risk-model sector factors (e.g. Barra, Axioma) can capture this better than hard GICS buckets.
- **Neutral to sectors ≠ neutral to factors.** A sector-neutral book can still be heavily exposed to size, value, momentum, or volatility factors. Full risk control usually layers sector neutrality *with* style-factor neutrality in a [[risk-budgeting|risk-budgeted]] optimizer.
- **Turnover cost.** Enforcing tight neutrality at each rebalance forces extra trades to rebalance sectors back to zero, adding transaction costs.

## Trading relevance

Sector neutrality is the default risk posture for institutional [[long-short-equity|market-neutral]] and [[statistical-arbitrage|stat-arb]] desks. A practitioner deciding whether to impose it asks: *does my signal have a view on sectors, or only on individual stocks within sectors?* If only the latter, neutralize. [[pairs-trading|Pairs trades]] are the simplest sector-neutral structure — long and short two names in the same industry so the sector exposure cancels and only the relative-value spread remains. At the portfolio level, the same logic generalizes to the full optimizer constraint above. Most multi-factor equity products report both gross and sector-neutral backtests, and a large gap between them is a warning that the apparent edge is really a sector bet in disguise.

## Related

- [[long-short-equity]] — the strategy family where sector neutrality is standard
- [[factor-investing]] — sector neutrality is one of several neutralization choices
- [[gics-sector]] — the classification scheme most commonly used to define sectors
- [[risk-budgeting]] — the broader optimizer framework that combines sector and style constraints
- [[correlation]] — why unhedged sector exposure dominates variance
- [[pairs-trading]] — the simplest sector-neutral structure
- [[statistical-arbitrage]] — where sector/factor neutralization is routine
- [[crowding-risk]] — the hazard of shared, unhedged sector tilts

## Sources

- Grinold, R. and Kahn, R. *Active Portfolio Management* (2nd ed., 1999) — neutralization, factor constraints, and attribution.
- MSCI — Global Industry Classification Standard (GICS) methodology.
- Qian, E., Hua, R., and Sorensen, E. *Quantitative Equity Portfolio Management* (2007) — sector and factor neutralization in optimizers.

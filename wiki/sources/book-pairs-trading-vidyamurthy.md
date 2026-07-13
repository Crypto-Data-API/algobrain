---
title: "Pairs Trading — Ganapathy Vidyamurthy (2004)"
type: source
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [book, pairs-trading, cointegration, mean-reversion, quantitative]
aliases: ["Pairs Trading Vidyamurthy"]
related: ["[[pairs-trading]]", "[[ornstein-uhlenbeck]]", "[[cointegration]]", "[[mean-reversion]]", "[[pairs-trading-vidyamurthy]]"]
source_type: book
source_author: "Ganapathy Vidyamurthy"
source_date: 2004
confidence: high
claims_count: 10
---

Ganapathy Vidyamurthy's *Pairs Trading* is the definitive practical guide to pairs trading as a quantitative strategy. It covers three methods — distance, [[cointegration]], and stochastic spread modeling via the [[ornstein-uhlenbeck]] process — with full mathematical derivations and practical implementation guidance. The book traces pairs trading from its origins at Morgan Stanley through its evolution into a fully quantitative discipline.

## Key Claims

1. [HIGH] The distance method (tracking cumulative normalized price differences) was the original [[pairs-trading]] approach developed at Morgan Stanley in the 1980s — the earliest systematic implementation of the strategy.

2. [HIGH] The [[cointegration]] method (Engle-Granger two-step or Johansen test) is statistically more rigorous than simple correlation-based pairing — correlation measures co-movement, while cointegration measures mean-reverting spread behavior.

3. [HIGH] The stochastic spread model uses the [[ornstein-uhlenbeck]] process to model the mean-reverting dynamics of the spread between cointegrated assets, enabling analytical solutions for trading parameters.

4. [HIGH] Optimal entry and exit thresholds can be determined by maximizing the Sharpe ratio of the spread trading strategy — providing a principled alternative to arbitrary z-score cutoffs.

5. [HIGH] The half-life of [[mean-reversion]] determines appropriate holding periods and trade frequency — faster reversion enables higher trade frequency and generally produces better risk-adjusted returns.

6. [HIGH] Pair selection should combine quantitative screening ([[cointegration]] tests, distance measures) with fundamental analysis (industry matching, business model similarity) for robust pair identification.

7. [HIGH] The hedge ratio (beta) must be dynamically estimated using rolling windows or Kalman filters — static ratios lead to hedge drift and unintended directional exposure over time.

8. [HIGH] Sector neutrality across the pairs portfolio reduces exposure to systematic risk factors — concentrated sector bets introduce uncompensated market risk.

9. [HIGH] [[pairs-trading]] profits declined significantly after 2002 as the strategy became widely known and adopted, demonstrating alpha decay from strategy crowding.

10. [HIGH] Extending from pairs to baskets (multiple assets per leg) improves diversification and increases strategy capacity beyond what single-pair trading allows.

## Concepts Referenced

- [[pairs-trading]]
- [[cointegration]]
- [[ornstein-uhlenbeck]]
- [[mean-reversion]]
- [[correlation]]
- [[hedge-ratio]]
- [[sharpe-ratio]]
- [[sector-neutrality]]
- [[alpha-decay]]

## Pages Backed

- [[pairs-trading]] — three-method framework (distance, cointegration, stochastic), Morgan Stanley origins, basket extension
- [[cointegration]] — Engle-Granger and Johansen methods for pair validation
- [[ornstein-uhlenbeck]] — stochastic spread modeling, half-life estimation, optimal threshold derivation
- [[mean-reversion]] — half-life as determinant of trade frequency and holding period
- [[pairs-trading-vidyamurthy]] — primary source for education/book page

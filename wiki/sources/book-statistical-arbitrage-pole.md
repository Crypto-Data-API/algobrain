---
title: "Statistical Arbitrage — Andrew Pole (2007)"
type: source
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [book, arbitrage, quantitative, mean-reversion, pairs-trading]
aliases: ["Statistical Arbitrage Pole"]
related: ["[[pairs-trading]]", "[[mean-reversion]]", "[[ornstein-uhlenbeck]]", "[[cointegration]]", "[[arbitrage]]", "[[statistical-arbitrage-pole]]"]
source_type: book
source_author: "Andrew Pole"
source_date: 2007
confidence: high
claims_count: 10
---

Andrew Pole's *Statistical Arbitrage* is the first book-length treatment of stat arb as a trading discipline. It covers the mathematics of [[pairs-trading]], spread modeling using the [[ornstein-uhlenbeck]] process, portfolio construction across multiple pairs, and risk management for market-neutral strategies. Published in 2007, it captures the state of stat arb just before the quant meltdown that stress-tested these strategies.

## Key Claims

1. [HIGH] Statistical [[arbitrage]] exploits temporary mispricings between statistically related securities — the edge derives from [[mean-reversion]] of the spread, not directional prediction.

2. [HIGH] Pairs selection requires both economic rationale (same sector, similar business model) AND statistical confirmation ([[cointegration]]) — one without the other produces unreliable trading signals.

3. [HIGH] The spread between cointegrated pairs follows a mean-reverting process that can be modeled using the [[ornstein-uhlenbeck]] process, enabling systematic signal generation and parameter estimation.

4. [HIGH] Entry signals based on z-score deviations from the mean (typically >2 sigma) with exits at mean reversion provide a robust, quantifiable trading framework for stat arb.

5. [HIGH] Portfolio-level stat arb diversifies across many pairs simultaneously to reduce single-pair risk — individual pair failures are absorbed by the portfolio's diversification benefit.

6. [HIGH] Risk management for stat arb requires stop losses based on spread divergence exceeding historical maximums — traditional price-based stops are inappropriate for spread trading.

7. [HIGH] Transaction costs are the primary enemy of stat arb — high-frequency rebalancing to maintain hedge ratios erodes the thin per-trade edge that defines the strategy.

8. [HIGH] Stat arb suffered catastrophic losses during the August 2007 quant meltdown when crowded strategies simultaneously unwound, demonstrating the systemic risk of strategy crowding.

9. [HIGH] Model decay requires continuous re-estimation of pair relationships and [[cointegration]] parameters — static models degrade as market structure and asset fundamentals evolve.

10. [HIGH] Stat arb is capacity-constrained — large positions move prices and destroy the edge being exploited, creating a natural ceiling on strategy assets under management.

## Concepts Referenced

- [[pairs-trading]]
- [[mean-reversion]]
- [[ornstein-uhlenbeck]]
- [[cointegration]]
- [[arbitrage]]
- [[cross-exchange-arbitrage]]
- [[risk-management]]
- [[transaction-costs]]
- [[market-neutral]]

## Pages Backed

- [[pairs-trading]] — z-score entry/exit framework, pair selection methodology
- [[mean-reversion]] — mathematical modeling via Ornstein-Uhlenbeck, model decay dynamics
- [[ornstein-uhlenbeck]] — spread modeling and parameter estimation for mean-reverting processes
- [[cointegration]] — dual requirement of economic rationale and statistical confirmation
- [[arbitrage]] — stat arb as capacity-constrained, mean-reversion-based arbitrage
- [[statistical-arbitrage-pole]] — primary source for education/book page

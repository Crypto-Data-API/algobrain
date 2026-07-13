---
title: "Algorithmic Trading — Ernest Chan (2013)"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [education, book, algorithmic, quantitative]
related:
  - "[[pairs-trading]]"
  - "[[ornstein-uhlenbeck]]"
  - "[[quantitative-trading-ernest-chan]]"
  - "[[mean-reversion]]"
---

## Overview

**Algorithmic Trading** by Ernest Chan (2013) is the advanced sequel to his earlier [[quantitative-trading-ernest-chan]]. While the first book covered the business of algorithmic trading, this one dives into specific strategy types with practical code examples. Chan covers mean reversion strategies (pairs trading, cointegration, Ornstein-Uhlenbeck process), momentum strategies (time series and cross-sectional), and statistical arbitrage across equities, ETFs, futures, and currencies. The book is heavily practical, with MATLAB code examples that translate easily to Python, and provides the statistical tests and mathematical framework needed to implement each strategy class.

## Key Takeaways

- **Mean reversion and momentum are the two fundamental strategy archetypes.** Almost every trading strategy is a variant of one or the other.
- **Cointegration is more useful than correlation for [[pairs-trading]].** Two assets can be uncorrelated but cointegrated — and cointegration is what you need for profitable pairs trading.
- **The Augmented Dickey-Fuller (ADF) test** determines if a price series is mean-reverting. Apply it to spread series, not individual prices.
- **The Hurst exponent** measures persistence: H < 0.5 = mean-reverting, H = 0.5 = random walk, H > 0.5 = trending.
- **The [[ornstein-uhlenbeck]] process** models mean reversion mathematically and provides the half-life of reversion — critical for setting holding periods and stop-losses.
- **Johansen test** extends cointegration to multiple assets simultaneously, enabling more robust statistical arbitrage portfolios.
- **Momentum strategies benefit from risk management overlays.** Time series momentum (trend following) is more robust than cross-sectional momentum in most markets.
- **Transaction costs destroy mean reversion strategies first.** Mean reversion trades more frequently and has smaller edge per trade, making execution costs critical.

## Who Should Read This

Intermediate algorithmic traders who have read the first Chan book or equivalent. Quants looking for specific, implementable strategy frameworks. Anyone building [[pairs-trading]] or statistical arbitrage systems.

## How It Applies to AI Trading

The statistical tests and mathematical models Chan covers — ADF, Hurst exponent, Johansen cointegration, Ornstein-Uhlenbeck half-life — are not just standalone strategies but features and building blocks for machine learning systems. A Hurst exponent becomes a feature in an ML model that predicts regime. A cointegration z-score becomes input to a neural network that learns optimal entry timing. The strategy archetypes (mean reversion, momentum) provide the structural priors that keep ML models grounded in economic reality rather than mining noise. Chan's practical approach to testing these strategies also directly informs how you validate ML-based versions of the same ideas.

## Rating

**8/10** — Excellent practical sequel. More focused and technical than the first book. Essential for anyone building mean reversion or statistical arbitrage systems. The MATLAB code is the only weakness — but translation to Python is straightforward.

## Related

- [[quantitative-trading-ernest-chan]] — The prerequisite first book
- [[pairs-trading]] — The core strategy covered in depth
- [[ornstein-uhlenbeck]] — Mean reversion model with half-life estimation
- [[mean-reversion]] — The strategy archetype this book primarily addresses

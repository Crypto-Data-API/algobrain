---
title: "Algorithmic Trading — Ernest Chan (2013)"
type: source
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [book, algorithmic, quantitative, mean-reversion]
aliases: ["Algorithmic Trading Ernest Chan"]
related: ["[[pairs-trading]]", "[[ornstein-uhlenbeck]]", "[[mean-reversion]]", "[[algorithmic-trading-ernest-chan]]"]
source_type: book
source_author: "Ernest Chan"
source_date: 2013
confidence: high
claims_count: 10
---

Ernest Chan's *Algorithmic Trading* is a practitioner's guide to building quantitative trading systems, with a strong focus on mean reversion and momentum as the two fundamental strategy archetypes. Chan provides statistical tools (ADF test, Hurst exponent, Johansen test) for identifying and validating mean-reverting price series, and walks through implementation of pairs trading and other spread-based strategies. The book bridges academic finance and real-world algo trading with concrete examples and MATLAB/Python code.

## Key Claims

1. [HIGH] [[mean-reversion]] and [[momentum]] are the two fundamental strategy archetypes — virtually all quantitative strategies derive from one or both of these principles.

2. [HIGH] [[cointegration]] is more useful than [[correlation]] for [[pairs-trading]] — two assets can be highly correlated but not cointegrated, meaning their spread will not mean-revert.

3. [HIGH] The Augmented Dickey-Fuller (ADF) test determines whether a price series is mean-reverting by testing for a unit root — rejection of the null hypothesis implies mean reversion.

4. [HIGH] The [[hurst-exponent]] measures persistence in a time series: H < 0.5 indicates mean-reverting behavior, H = 0.5 indicates a random walk, and H > 0.5 indicates trending behavior.

5. [HIGH] The [[ornstein-uhlenbeck]] process models mean reversion mathematically and provides the half-life of reversion, which determines optimal holding period and trade frequency.

6. [HIGH] The Johansen test extends [[cointegration]] analysis to multiple assets simultaneously, enabling construction of mean-reverting portfolios from more than two instruments.

7. [HIGH] Time series [[momentum]] (trend following) is more robust than cross-sectional momentum because it does not depend on relative asset ranking, which is sensitive to universe selection.

8. [HIGH] [[transaction-costs]] destroy [[mean-reversion]] strategies first due to their higher trade frequency — a strategy that is profitable before costs may be unprofitable after costs.

9. [HIGH] Spread trading (long one asset, short another) isolates the mean-reverting component by hedging out common market factors, creating a synthetic stationary series.

10. [HIGH] Statistical tests must confirm mean reversion before trading it — visual inspection of a price chart is insufficient and leads to false identification of mean-reverting behavior.

## Concepts Referenced

- [[mean-reversion]]
- [[momentum]]
- [[pairs-trading]]
- [[cointegration]]
- [[correlation]]
- [[ornstein-uhlenbeck]]
- [[hurst-exponent]]
- [[transaction-costs]]
- [[backtesting-pitfalls]]
- [[algorithmic-trading]]

## Pages Backed

- [[pairs-trading]] — cointegration vs correlation distinction, spread construction methodology
- [[ornstein-uhlenbeck]] — mathematical model and half-life estimation
- [[mean-reversion]] — statistical validation framework (ADF, Hurst, Johansen)
- [[algorithmic-trading-ernest-chan]] — primary source for entity/concept page

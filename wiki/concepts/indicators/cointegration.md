---
title: "Cointegration"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [quantitative, pairs-trading, mean-reversion, statistics]
aliases: ["Cointegrated", "Cointegration Test"]
related: ["[[pairs-trading]]", "[[ornstein-uhlenbeck]]", "[[mean-reversion]]", "[[correlation]]", "[[statistical-arbitrage]]", "[[stationarity]]"]
domain: [quantitative, market-microstructure]
difficulty: advanced
---

Cointegration is a statistical property of two or more non-stationary time series whose linear combination produces a stationary series. Unlike [[correlation]], which measures the tendency of two series to move together in the short term, cointegration captures a long-run equilibrium relationship -- the series may diverge temporarily but are pulled back together over time. This makes cointegration the proper foundation for [[pairs-trading]] and [[statistical-arbitrage]] strategies.

## Overview

The concept was formalized by Clive Granger and Robert Engle in the 1980s (earning them the 2003 Nobel Prize in Economics). The key insight is that two individually non-stationary (random walk) price series can share a common stochastic trend. When they do, the spread between them is mean-reverting, creating a tradeable signal.

**Why correlation is insufficient**: Two stock prices can have a high correlation (e.g., 0.95) over a sample period yet drift arbitrarily far apart. Correlation measures co-movement of returns, not prices. A pairs trade based solely on correlation can suffer permanent divergence. Cointegration, by contrast, guarantees that the spread is stationary and will revert to its mean -- precisely the property a [[mean-reversion]] trader needs.

**Formal definition**: Time series X(t) and Y(t), both integrated of order 1 (I(1)), are cointegrated if there exists a coefficient beta such that Z(t) = Y(t) - beta * X(t) is stationary (I(0)). The coefficient beta is called the cointegrating vector, and Z(t) is the spread.

## How It Works

### Testing for Cointegration

Three primary methods are used:

**1. Engle-Granger Two-Step Method**
1. Regress Y on X using OLS to estimate beta: Y(t) = alpha + beta * X(t) + epsilon(t)
2. Test the residuals epsilon(t) for stationarity using the Augmented Dickey-Fuller (ADF) test
3. If residuals are stationary, the series are cointegrated

This method is simple but limited to testing one cointegrating relationship at a time and suffers from small-sample bias due to the two-step procedure.

**2. Johansen Test**
A multivariate approach using Vector Autoregression (VAR) that can identify multiple cointegrating relationships among N series simultaneously. Produces both trace and maximum eigenvalue test statistics. Preferred for baskets of three or more assets.

**3. Phillips-Ouliaris Test**
Similar to Engle-Granger but uses Phillips-Perron style adjustments for autocorrelation and heteroskedasticity in the residuals. More robust in certain settings.

### The Spread and Mean Reversion

Once cointegration is established, the spread Z(t) = Y(t) - beta * X(t) behaves like an [[ornstein-uhlenbeck]] process -- it fluctuates around a long-run mean and is pulled back when it deviates. Key parameters of this spread:

- **Half-life of mean reversion** -- how quickly the spread reverts; shorter half-lives mean more trading opportunities
- **Spread volatility** -- determines position sizing and stop-loss levels
- **Mean and bounds** -- typically trade when spread exceeds +/- 1-2 standard deviations

### Cointegration vs. Correlation

| Property | Correlation | Cointegration |
|----------|------------|---------------|
| Measures | Co-movement of returns | Long-run price equilibrium |
| Time horizon | Short-term | Long-term |
| Stationarity | Does not require | Requires I(1) series |
| Spread behavior | Can diverge permanently | Mean-reverting |
| Trading use | Directional hedging | [[pairs-trading]], [[statistical-arbitrage]] |

## Trading Applications

### Pairs Trading

The classic application. Identify two stocks (or ETFs, futures) that are cointegrated, then:
1. Go long the underperformer and short the outperformer when the spread widens beyond a threshold
2. Close the position when the spread reverts to its mean
3. Stop out if the spread exceeds a maximum threshold (cointegration breakdown)

Common pairs include related companies in the same sector (e.g., Coca-Cola/Pepsi), ETFs tracking similar indices, or futures contracts on related commodities.

### Statistical Arbitrage

Extension of pairs trading to large portfolios. Identify clusters of cointegrated assets and construct market-neutral portfolios that profit from spread reversion. This is the approach used by firms like [[d-e-shaw]] and [[renaissance-technologies]].

### Risk Management Considerations

- **Cointegration can break down** -- structural changes (mergers, regulatory shifts, business model changes) can permanently destroy the relationship
- **Regime changes** -- cointegration parameters (beta, half-life) can shift over time; rolling window estimation is essential
- **Transaction costs** -- frequent mean-reversion trades must overcome [[slippage]] and commissions
- **Survivorship bias** -- in-sample cointegration may not persist out-of-sample; always validate on held-out data

## Related

- [[pairs-trading]] -- the primary trading strategy built on cointegration
- [[mean-reversion]] -- the broader class of strategies that exploit stationarity
- [[ornstein-uhlenbeck]] -- the stochastic process model for mean-reverting spreads
- [[correlation]] -- related but distinct statistical measure
- [[statistical-arbitrage]] -- portfolio-scale application of cointegration

## Sources

- [[book-algorithmic-trading-ernest-chan]] -- practical implementation of cointegration-based strategies
- [[book-pairs-trading-vidyamurthy]] -- comprehensive treatment of pairs trading theory
- [[book-statistical-arbitrage-pole]] -- advanced cointegration applications in stat arb

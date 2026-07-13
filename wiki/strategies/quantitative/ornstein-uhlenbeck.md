---
title: "Ornstein-Uhlenbeck Process"
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [ornstein-uhlenbeck, mean-reversion, stochastic-process, half-life, statistical-arbitrage, quantitative, pairs-trading]
aliases: ["OU Process Trading", "Mean-Reverting Stochastic Process", "OU Model"]
strategy_type: quantitative
timeframe: intraday|swing
markets: [stocks, crypto]
complexity: advanced
backtest_status: untested
related: ["[[pairs-trading]]", "[[statistical-arbitrage]]", "[[kalman-filter-trading]]", "[[mean-reversion]]", "[[bollinger-band-reversion]]", "[[book-algorithmic-trading-ernest-chan]]", "[[book-pairs-trading-vidyamurthy]]", "[[book-statistical-arbitrage-pole]]"]
---

# Ornstein-Uhlenbeck Process

## Overview

The Ornstein-Uhlenbeck (OU) process is a continuous-time stochastic model that describes mean-reverting dynamics -- a price (or spread) that is pulled toward a long-run equilibrium level, with random fluctuations around it. It is the mathematical foundation of [[statistical-arbitrage]] and [[pairs-trading]], providing a rigorous framework for estimating how fast and how strongly a spread will revert to its mean.

Named after Leonard Ornstein and George Uhlenbeck who described it in 1930 for modeling particle velocity in physics (Source: [[book-pairs-trading-vidyamurthy]]), the OU process has three parameters that directly inform trading decisions:

- **theta (mean-reversion speed):** How quickly the process reverts to its mean. Higher theta = faster reversion = shorter holding periods.
- **mu (long-run mean):** The equilibrium level the process is attracted to. This is where you expect the spread to settle.
- **sigma (volatility):** The intensity of random fluctuations around the mean. Higher sigma = wider deviations = larger potential profits (and losses).

The **half-life** of mean reversion -- the time it takes for a deviation to decay by half -- is calculated as **t_half = ln(2) / theta** (Source: [[book-algorithmic-trading-ernest-chan]]). This is arguably the most important practical output: it tells you how long a typical trade will take to play out. If the half-life is 5 days, you should expect a pairs trade to close in roughly 5-15 days. If it is 60 days, the capital is tied up far too long for most strategies.

## How It Works

The OU process is described by the stochastic differential equation:

**dX_t = theta * (mu - X_t) * dt + sigma * dW_t**

In discrete time (for practical estimation), this becomes an AR(1) regression:

**X_t = a + b * X_(t-1) + epsilon_t**

Where:
- **theta = -ln(b) / dt** (mean-reversion speed, extracted from the AR(1) coefficient)
- **mu = a / (1 - b)** (long-run mean)
- **sigma** is derived from the regression residual standard deviation, adjusted for theta

**Estimation procedure:**
1. Compute the spread between two cointegrated assets (from [[pairs-trading]] setup).
2. Run OLS regression of X_t on X_(t-1) to get coefficients a and b.
3. Verify that b < 1 (confirming mean reversion; b >= 1 means the spread is non-stationary).
4. Extract theta, mu, and sigma. Compute half-life = ln(2) / theta.
5. Validate with [[augmented-dickey-fuller]] test for stationarity.

The OU model also gives the **stationary distribution** of the spread: Normal(mu, sigma^2 / (2*theta)). This defines the expected range of the spread and the z-score thresholds for entry and exit.

## Rules / Application

### Pair Selection Filter
1. For each candidate pair, estimate the OU parameters on the spread.
2. **Reject pairs with half-life > 30 days** (too slow for practical trading) or **< 1 day** (too fast, likely microstructure noise).
3. Ideal half-life range: **3-20 days** for swing trading, **1-4 hours** for intraday.
4. Rank remaining pairs by the ratio sigma / theta (higher = more profitable mean reversion opportunities).

### Entry Rules
1. Compute the current spread deviation from mu in units of the stationary standard deviation: **z = (X_t - mu) / sqrt(sigma^2 / (2*theta))**.
2. **Enter long the spread** when z < -1.5 to -2.0 (spread is below equilibrium).
3. **Enter short the spread** when z > +1.5 to +2.0 (spread is above equilibrium).
4. Use the OU model's expected time to reversion (approximately 2-3 half-lives for full reversion) to set **time-based exits**.

### Exit Rules
1. **Mean-reversion exit:** Close when z returns to 0 (spread at equilibrium).
2. **Partial exit:** Take half off at z = +/- 0.5 on the way back.
3. **Stop-loss:** Close if z exceeds +/- 3.5 (model may be breaking down, regime change in progress).
4. **Time stop:** If the trade has not reverted within 3-4 half-lives, close and re-estimate parameters.

### Position Sizing
Size positions proportionally to the z-score magnitude and inversely to sigma. Larger deviations warrant larger positions (higher reversion probability), but higher sigma warrants smaller sizes (wider fluctuations).

## Example

**Setup:** BTC/ETH spread, 4-hour bars, OU model estimation.

1. Spread = log(BTC) - 15.2 * log(ETH) computed over 90 days of 4-hour data.
2. AR(1) regression yields b = 0.987, a = 0.013. Therefore: theta = -ln(0.987)/1 = 0.0131 per bar. Half-life = ln(2)/0.0131 = **53 bars = ~8.8 days**.
3. Long-run mean mu = 0.013 / (1 - 0.987) = 1.0. Stationary std = 0.42.
4. Current spread = 0.12. Z-score = (0.12 - 1.0) / 0.42 = **-2.1**. ETH is cheap relative to BTC.
5. **Enter:** Long ETH, short BTC at the dynamic hedge ratio. Position sized for 1% portfolio risk.
6. Over 7 days (40 bars), the spread reverts to 0.85 (z = -0.36). **Exit** near equilibrium.
7. Profit: $1,200 on $50K position. Holding time closely matched the OU model's predicted half-life.

## Advantages

- Provides **quantitative estimates** of mean-reversion speed, equilibrium level, and volatility -- far more informative than simply testing for stationarity
- The **half-life** directly informs holding period expectations and capital allocation decisions
- Mathematically rigorous: the OU process is the continuous-time analog of the AR(1) process with well-understood properties
- Enables **optimal entry/exit** based on the stationary distribution rather than arbitrary z-score thresholds
- Pairs naturally with [[kalman-filter-trading]] -- the Kalman filter can estimate OU parameters in real-time as they evolve
- Foundation of academic [[statistical-arbitrage]] -- used in the original stat arb models at D.E. Shaw, Renaissance, and other quant firms (Source: [[book-algorithmic-trading-ernest-chan]])

## Disadvantages

- Assumes **constant parameters** (theta, mu, sigma) -- in reality, mean-reversion speed and equilibrium shift over time, requiring periodic re-estimation
- The **Gaussian assumption** underestimates tail risk: real spread moves can be far larger than the OU model predicts
- Estimation requires sufficient data: too short a window produces unreliable parameters, too long includes stale regime data
- The model says nothing about **why** the spread mean-reverts -- fundamental changes can permanently shift mu, causing the model to generate losing signals
- Half-life estimation has wide confidence intervals, especially for longer half-lives; a point estimate of 10 days might have a 95% CI of 5-25 days
- Only models **linear** mean reversion -- nonlinear dynamics (threshold effects, asymmetric reversion) require more complex models (Source: [[book-statistical-arbitrage-pole]])

## Sources

- [[book-algorithmic-trading-ernest-chan]] — the primary practical reference for the OU process in trading, including half-life estimation, Hurst exponent analysis, and the connection between cointegration and mean-reversion speed
- [[book-pairs-trading-vidyamurthy]] — Vidyamurthy (2004) provides the theoretical foundation for the OU process in pairs trading, including spread modeling and parameter estimation for cointegrated pairs
- [[book-statistical-arbitrage-pole]] — Pole (2007) covers the OU process within the stat arb framework, including extensions to nonlinear mean reversion and portfolio-level spread construction

## See Also

- [[pairs-trading]] -- the primary strategy built on OU process modeling
- [[statistical-arbitrage]] -- the broader framework where OU processes provide the mathematical backbone
- [[kalman-filter-trading]] -- dynamic estimation of OU parameters as they evolve
- [[mean-reversion]] -- the market behavior the OU process formalizes
- [[bollinger-band-reversion]] -- a simplified, indicator-based approach to the same concept

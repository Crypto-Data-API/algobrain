---
title: "GARCH Volatility Modeling"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [garch, volatility, volatility-forecasting, volatility-clustering, quantitative, options, position-sizing]
aliases: ["GARCH Trading", "GARCH Volatility Forecasting", "Conditional Heteroskedasticity"]
strategy_type: quantitative
timeframe: swing|position
markets: [stocks, forex]
complexity: advanced
backtest_status: untested
related: ["[[vix-trading]]", "[[regime-detection]]", "[[tail-risk-hedging]]", "[[bollinger-band-reversion]]", "[[risk-budgeting]]"]
---

# GARCH Volatility Modeling

## Overview

GARCH (Generalized Autoregressive Conditional Heteroskedasticity) models forecast **time-varying volatility** by capturing the empirical fact that market volatility **clusters** -- large moves tend to follow large moves, and calm periods follow calm periods. Developed by Bollerslev (1986) as an extension of Engle's ARCH (1982), GARCH models have become the standard tool for volatility forecasting in quantitative finance.

The core insight is that volatility is **not constant**. Traditional models assume returns have fixed variance, but in reality, a 3% daily drop in the S&P 500 is far more likely to be followed by another large move (up or down) than by a calm 0.2% day. GARCH formalizes this by modeling tomorrow's variance as a function of today's variance and today's squared return. The resulting forecast gives a **conditional volatility** estimate that adapts to recent market behavior.

In trading, GARCH volatility forecasts feed into [[position-sizing]] (scale positions inversely to forecasted vol), dynamic stop-loss placement (wider stops in high-vol regimes), [[options]] pricing (compare GARCH-forecasted vol to implied vol for trading edges), and [[risk-budgeting]] (regime-aware risk allocation). Any strategy that uses a fixed volatility assumption can be improved by substituting a GARCH forecast.

## How It Works

The standard GARCH(1,1) model specifies:

**sigma_t^2 = omega + alpha * r_(t-1)^2 + beta * sigma_(t-1)^2**

Where:
- **sigma_t^2** = forecasted variance for period t
- **omega** = long-run variance weight (constant)
- **alpha** = reaction coefficient -- how much today's squared return affects tomorrow's forecast (typically 0.05-0.15)
- **beta** = persistence coefficient -- how much yesterday's variance carries forward (typically 0.80-0.95)
- **alpha + beta** = volatility persistence. Values near 1.0 mean volatility shocks decay slowly.

The model is estimated via **maximum likelihood** on historical returns. Popular extensions include:
- **EGARCH:** Captures the [[leverage-effect]] (negative returns increase vol more than positive returns of the same magnitude).
- **GJR-GARCH:** Adds an asymmetric term for negative shocks.
- **GARCH-M:** Includes the volatility forecast directly in the return equation (risk premium).

## Rules / Application

### For Position Sizing
1. Estimate a GARCH(1,1) model on 2-5 years of daily returns for the target asset.
2. Each day, generate a one-step-ahead volatility forecast (sigma_t).
3. Scale position size inversely: **Position = Target_Risk / sigma_t**. When GARCH forecasts high vol, reduce size; when low, increase.
4. This produces a **volatility-targeted portfolio** with more stable realized risk over time.

### For Option Trading
1. Generate a GARCH multi-step volatility forecast (e.g., 30-day ahead) and annualize it.
2. Compare GARCH-forecasted volatility to **implied volatility** from the options market.
3. If GARCH forecast > implied vol: buy options (vol is underpriced). Deploy long straddles or strangles.
4. If GARCH forecast < implied vol: sell options (vol is overpriced). Deploy short strangles, iron condors, or [[covered-calls]].
5. This creates a systematic **volatility arbitrage** framework.

### For Dynamic Stops
1. Set stop-loss distances as a multiple of the GARCH-forecasted daily volatility: Stop = Entry +/- (k * sigma_t), where k = 2-3.
2. In low-vol regimes, stops are tight (protecting profits). In high-vol regimes, stops are wide (avoiding noise-induced exits).
3. Combine with [[atr-trailing-stop]] concepts but using the forward-looking GARCH estimate instead of backward-looking ATR.

## Example

**Setup:** EUR/USD daily, GARCH(1,1) for position sizing.

1. GARCH model estimated on 2020-2025 data. Parameters: alpha=0.08, beta=0.90, omega=0.000002. Long-run vol = sqrt(omega/(1-alpha-beta)) = 10% annualized.
2. After a calm Q1, GARCH forecasts daily vol = 0.45% (7.1% annualized). Target risk = 1% of account per day. Position size = 1% / 0.45% = **2.2x leverage**.
3. An ECB surprise triggers a 1.8% daily move. GARCH immediately ratchets up: next-day forecast = 0.85% daily vol.
4. Position size recalculates: 1% / 0.85% = **1.18x leverage** -- nearly halved. Stops widen proportionally.
5. Over the next 2 weeks, vol decays as GARCH persistence gradually brings the forecast back toward the long-run mean.
6. **Result:** The vol-targeted approach avoided an outsized loss during the shock and gradually re-levered as conditions normalized.

## Advantages

- Captures **volatility clustering**, the most robust empirical regularity in financial returns
- Forward-looking forecast (unlike [[historical-volatility]] which is purely backward-looking)
- Improves [[position-sizing]] by scaling exposure to current risk conditions -- reduces drawdowns in volatile periods
- Creates systematic edge in options trading by comparing forecast vol to implied vol
- Well-established with robust estimation procedures (MLE), available in all major quant libraries (Python's `arch`, R's `rugarch`)
- Extensions (EGARCH, GJR) capture asymmetric vol response to positive vs negative shocks

## Disadvantages

- **Assumes parametric distributions** (typically Gaussian) for return innovations -- underestimates tail risk from truly extreme events
- Model estimates are sensitive to the **training window** -- too short captures noise, too long includes stale regimes
- GARCH forecasts are **mean-reverting by construction**, which can underestimate sustained volatility increases during [[regime-detection|regime changes]]
- Cannot capture **jumps** or discontinuous price moves (jump-diffusion models or realized volatility methods may be needed)
- Multi-step-ahead forecasts degrade rapidly -- GARCH is most reliable for 1-5 day horizons
- Computationally more demanding than simple [[historical-volatility]] or [[atr]] calculations
- The GARCH family has dozens of variants; selecting the best specification requires careful model comparison and risks overfitting

## See Also

- [[vix-trading]] -- market-implied volatility that GARCH forecasts can be compared against
- [[regime-detection]] -- complementary approach to identifying volatility states
- [[risk-budgeting]] -- uses volatility forecasts for risk allocation
- [[bollinger-band-reversion]] -- a simpler volatility-band approach that GARCH can enhance
- [[tail-risk-hedging]] -- protection against the extreme events GARCH may underestimate

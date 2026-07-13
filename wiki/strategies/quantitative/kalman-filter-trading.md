---
title: "Kalman Filter Trading"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [kalman-filter, adaptive, signal-processing, noise-reduction, quantitative, pairs-trading, dynamic-estimation]
aliases: ["Kalman Filter Strategy", "Adaptive Filter Trading", "KF Signal Extraction"]
strategy_type: quantitative
timeframe: intraday|swing
markets: [stocks, crypto, forex]
complexity: advanced
backtest_status: untested
related: ["[[pairs-trading]]", "[[mean-reversion]]", "[[statistical-arbitrage]]", "[[moving-averages]]", "[[regime-detection]]"]
---

# Kalman Filter Trading

## Overview

The Kalman filter is a recursive Bayesian estimation algorithm that extracts the true underlying price or trend from noisy market data. Originally developed by Rudolf Kalman in 1960 for aerospace navigation, it has become a cornerstone of [[quantitative-trading]] signal processing. Unlike traditional [[moving-averages]] that use fixed lookback windows, the Kalman filter **adapts in real-time** -- it continuously updates its estimate of the hidden state (true price, trend slope, spread) as each new observation arrives, weighting recent data more heavily when the signal is clear and smoothing more aggressively when noise dominates.

The filter maintains two key quantities: a **state estimate** (e.g., the "true" price) and an **uncertainty estimate** (how confident the filter is). At each time step, it makes a prediction based on its model, observes the actual price, and then updates its estimate by blending prediction and observation according to the **Kalman gain** -- a ratio that balances process noise (how much the true price changes) against observation noise (how much market microstructure distorts the price). When process noise is high relative to observation noise, the filter tracks price closely. When observation noise dominates, it smooths aggressively.

In trading, the Kalman filter is used for [[pairs-trading]] spread estimation, dynamic hedge ratio calculation, trend extraction, and as an adaptive replacement for exponential moving averages. It adapts its smoothing automatically, making it faster than traditional MAs in trending markets and smoother in choppy conditions.

## How It Works

The Kalman filter operates in a two-step **predict-update** cycle:

1. **Predict Step:** Project the current state forward using a transition model. For a simple price-tracking filter: predicted_price = last_estimated_price. For a trend model: predicted_price = last_price + last_slope.
2. **Update Step:** When the new observation (market price) arrives, compute the **Kalman gain** K = predicted_uncertainty / (predicted_uncertainty + observation_noise). Then update: new_estimate = predicted_price + K * (observed_price - predicted_price).

The Kalman gain K ranges from 0 to 1. When K is near 1, the filter trusts the new observation heavily (fast tracking). When K is near 0, it trusts its internal model (heavy smoothing). The filter automatically adjusts K as market conditions change, giving it an inherent **adaptive** quality that fixed-window indicators lack.

For [[pairs-trading]], a Kalman filter can dynamically estimate the hedge ratio between two assets, replacing the static regression approach. The state becomes the hedge ratio itself, and the filter updates it as the relationship between assets evolves -- capturing structural shifts that a fixed-window OLS regression would miss.

## Rules / Application

### As Adaptive Moving Average
1. Configure the filter with a **state transition model** (random walk or random walk with drift) and tune the **process noise (Q)** and **observation noise (R)** parameters.
2. High Q/R ratio = fast, responsive filter (similar to short-period EMA). Low Q/R ratio = slow, smooth filter (similar to long-period EMA).
3. **Long signal:** Price crosses above the Kalman filter estimate (similar to price crossing above a moving average).
4. **Short signal:** Price crosses below the Kalman filter estimate.
5. Use the **slope of the Kalman estimate** as a trend indicator -- positive slope = bullish, negative = bearish.

### For Pairs Trading Spread
1. Model the spread between Asset A and Asset B where the hedge ratio is the hidden state.
2. The Kalman filter dynamically updates the hedge ratio at each time step instead of using a fixed regression window.
3. Compute the **residual** (observed spread - Kalman-estimated spread) as the trading signal.
4. Enter when the residual exceeds +/- 2 standard deviations of the filter's innovation sequence.
5. Exit when the residual returns to zero.

### Parameter Tuning
- **Q (process noise covariance):** Controls how much the hidden state is expected to change each step. Higher Q = more responsive.
- **R (observation noise covariance):** Controls how noisy you believe market prices are. Higher R = more smoothing.
- Use **maximum likelihood estimation** on historical data to optimize Q and R, or set them heuristically and validate on out-of-sample data.

## Example Trade

**Setup:** BTC/ETH pairs trade on 1-hour charts using Kalman filter for dynamic hedge ratio estimation.

1. Initialize the Kalman filter with state = hedge ratio (starting at 15.0 ETH per BTC from OLS regression).
2. At hour 100, the Kalman filter estimates hedge ratio = 14.8, with the residual (actual spread - estimated) at +2.3 standard deviations -- ETH is relatively cheap vs BTC.
3. **Enter:** Short 0.1 BTC ($6,500), long 1.48 ETH ($6,500) -- dollar-neutral using Kalman hedge ratio.
4. Over 18 hours, the spread mean-reverts. The Kalman residual returns to 0.
5. **Exit:** Close both legs. Profit from convergence: +$340 net after fees.
6. Note: A static OLS hedge ratio of 15.0 would have produced a delayed signal and $80 less profit because it failed to capture the evolving relationship.

## Advantages

- **Adaptive:** Automatically adjusts smoothing speed to current market conditions -- no manual lookback tuning
- Provides **uncertainty estimates** alongside price estimates, enabling confidence-based [[position-sizing]]
- Superior to fixed-window methods for [[pairs-trading]] hedge ratio estimation -- captures structural drift
- Computationally efficient: O(1) per update, easily runs in real-time even at tick-level frequency
- Theoretically optimal estimator under linear Gaussian assumptions (and robust even when those assumptions are violated)
- Natural framework for combining multiple signals via multi-dimensional state vectors

## Disadvantages

- **Parameter sensitivity:** Q and R tuning significantly affects performance; poor calibration produces either laggy or noisy estimates
- Assumes **linear dynamics** -- nonlinear price behavior may require extended Kalman filters (EKF) or unscented Kalman filters (UKF), adding complexity
- The Gaussian noise assumption is violated by fat-tailed market returns -- extreme moves can cause filter divergence
- More complex to implement and debug than simple [[moving-averages]] or [[bollinger-bands]]
- **Overfitting risk:** Maximum likelihood parameter optimization can overfit to in-sample data
- Does not inherently model [[regime-detection]] -- a single filter may struggle across fundamentally different market states

## See Also

- [[pairs-trading]] -- primary application of Kalman filters in spread estimation
- [[statistical-arbitrage]] -- broader framework where Kalman filters provide signal extraction
- [[moving-averages]] -- the simpler, fixed-window alternative the Kalman filter improves upon
- [[regime-detection]] -- can be combined with Kalman filtering for state-aware adaptation
- [[ornstein-uhlenbeck]] -- mean-reversion model often paired with Kalman estimation

---
title: "Realized Volatility"
type: concept
created: 2026-04-07
updated: 2026-07-19
status: excellent
tags: [volatility, quantitative, risk-management]
aliases: ["Historical Volatility", "Realized Vol", "RV", "Realized Variance"]
related: ["[[implied-volatility]]", "[[vix]]", "[[volatility-risk-premium]]", "[[standard-deviation]]", "[[volatility-trading]]", "[[volatility-cone]]", "[[variance-swap]]", "[[variance]]"]
domain: [volatility, risk-management]
difficulty: intermediate
---

**Realized volatility** (RV), also called historical volatility, is the actual observed volatility of an asset measured from past price returns over a specific lookback period. Unlike [[implied-volatility]], which is forward-looking and derived from [[options-pricing|options prices]], realized volatility is a backward-looking statistical measure that tells you how much an asset *actually* moved.

## Overview

Realized volatility is the most fundamental measure of risk in finance. It quantifies the degree of price variation an asset has exhibited and is expressed as an annualized percentage. A stock with 20% realized volatility has historically moved about 20% per year (one standard deviation), or roughly 1.25% per day (20% / sqrt(252)).

RV serves as the benchmark against which [[implied-volatility]] is compared. If IV is consistently higher than RV, options are "expensive" relative to actual movement -- the [[volatility-risk-premium]] is positive. This comparison is central to every options strategy decision, from hedging to speculation.

## How It Works

The standard **close-to-close** calculation for realized volatility involves these steps:

1. **Collect closing prices** over the lookback period (e.g., 20 trading days for monthly RV)
2. **Calculate log returns**: $r_t = \ln(P_t / P_{t-1})$
3. **Compute the [[standard-deviation|standard deviation]]** of those log returns
4. **Annualize**: multiply by $\sqrt{252}$ for daily data (252 trading days per year)

Formally, the annualized close-to-close estimator is:

$$\sigma_{cc} = \sqrt{\frac{252}{n-1}\sum_{t=1}^{n}\left(r_t - \bar{r}\right)^2}$$

Many desks drop the mean term ($\bar{r} \approx 0$ over short windows) and use the simpler $\sigma = \sqrt{\frac{252}{n}\sum r_t^2}$, which is the [[variance|realized-variance]] form that underlies [[variance-swap|variance swaps]].

### Worked Example (close-to-close)

Five daily closes: 100.0 → 101.0 → 100.0 → 102.0 → 101.0 → 102.5.

1. Log returns: $\ln(101/100)=+0.995\%$, $\ln(100/101)=-0.995\%$, $\ln(102/100)=+1.980\%$, $\ln(101/102)=-0.985\%$, $\ln(102.5/101)=+1.474\%$
2. Treating the mean as ≈0, $\sum r_t^2 = (0.995^2 + 0.995^2 + 1.980^2 + 0.985^2 + 1.474^2)\times10^{-4} \approx 8.84\times10^{-4}$
3. Daily variance $= 8.84\times10^{-4}/5 = 1.768\times10^{-4}$; daily vol $=\sqrt{1.768\times10^{-4}}\approx 1.33\%$
4. Annualized: $1.33\% \times \sqrt{252} \approx 21.1\%$

A ~21% annualized realized vol is typical for a single large-cap equity. Five points is far too few in practice; 20–60 observations are standard.

**Common lookback periods:**
- **10-day RV** -- captures very recent movement, useful for short-term trading
- **20-day RV** -- approximately one trading month, most commonly compared to 30-day IV
- **60-day RV** -- three-month view, smooths out short-term noise
- **252-day RV** -- full-year historical volatility

**Alternative Estimators:** The close-to-close method above ignores intraday price action — it sees only the difference between two closes and throws away the entire path in between. More efficient estimators use the open (O), high (H), low (L), and close (C) of each bar. "Efficiency" here means a lower-variance estimate from the same number of days, so the vol number is steadier and converges faster.

The **Parkinson estimator** (1980) uses the high-low range of each day, which captures intraday movement the close-to-close measure misses:

$$\sigma_{P}^2 = \frac{1}{4\ln 2}\cdot\frac{1}{n}\sum_{t=1}^{n}\left(\ln\frac{H_t}{L_t}\right)^2$$

It is roughly **5× more efficient** than close-to-close but assumes continuous trading with no drift and no overnight gaps — so it *understates* vol when much of the move happens overnight.

The **Garman-Klass estimator** (1980) adds the open and close to the range, improving efficiency further (~7–8×):

$$\sigma_{GK}^2 = \frac{1}{n}\sum_{t=1}^{n}\left[\tfrac{1}{2}\left(\ln\frac{H_t}{L_t}\right)^2 - (2\ln 2 - 1)\left(\ln\frac{C_t}{O_t}\right)^2\right]$$

Both Parkinson and Garman-Klass ignore the **overnight gap** (close-to-next-open), so they systematically under-measure assets that move on overnight news. The **Yang-Zhang estimator** (2000) is the modern standard because it is drift-independent *and* handles overnight jumps by combining an overnight-variance term, an open-to-close term, and a Rogers-Satchell intraday term — it is the estimator most often used to build a [[volatility-cone]].

Finally, **realized variance from tick/high-frequency data** sums squared intraday returns over very fine intervals (e.g., 5-minute bars): $RV = \sum_i r_i^2$. As the sampling frequency rises, $RV$ converges to the true integrated variance of the underlying diffusion — the most accurate measure — though microstructure noise (bid-ask bounce) biases it upward at the very highest frequencies, which is why 5-minute (not tick-level) sampling is the practical sweet spot.

| Estimator | Inputs | Relative efficiency vs C-to-C | Handles overnight gap? | Drift-independent? |
|-----------|--------|-------------------------------|------------------------|--------------------|
| Close-to-close | C only | 1× (baseline) | Yes (implicitly) | No |
| Parkinson | H, L | ~5× | No | Yes |
| Garman-Klass | O, H, L, C | ~7–8× | No | No |
| Rogers-Satchell | O, H, L, C | ~6× | No | **Yes** |
| Yang-Zhang | O, H, L, C (+ prev C) | ~8–14× | **Yes** | **Yes** |
| High-frequency RV | intraday ticks | highest | depends on sampling | Yes |

## Trading Applications

**IV vs. RV Comparison:** The single most important use of realized volatility is comparing it to [[implied-volatility]]:

- **IV > RV** -- options are priced above recent actual movement; favor selling premium ([[short-straddle|straddles]], [[iron-condor|iron condors]], etc.)
- **IV < RV** -- options are cheap relative to actual movement; favor buying premium (long straddles, strangles)
- **IV / RV ratio** -- a ratio above 1.0 suggests options are expensive; ratios persistently above 1.2 indicate a strong [[volatility-risk-premium]]

The table below maps the IV-vs-RV relationship to the typical positioning. The crucial subtlety is that you must compare **like horizons** — 30-day IV against 20–30-day RV, not against a 252-day number (this is exactly what the [[volatility-cone]] enforces) — and remember IV is forward-looking while RV is backward-looking, so a gap can simply mean the market expects a known event (earnings, FOMC):

| Relationship | Interpretation | Typical positioning | Caveat |
|--------------|----------------|---------------------|--------|
| IV ≫ RV (ratio > 1.2) | Strong [[volatility-risk-premium]]; options rich | Sell premium / short vega | A pending catalyst can justify the premium |
| IV ≈ RV (ratio ≈ 1.0) | Fairly priced | No vol edge; trade direction instead | — |
| IV < RV (ratio < 1.0) | Options cheap vs actual movement | Buy premium / long gamma | Often precedes a vol spike already underway |
| RV rising, IV flat | Realized catching up to implied | Long gamma can pay via delta-hedging | Whipsaw risk if it reverts |

**Volatility Cones:** Plotting the distribution of RV at various lookback periods creates a "volatility cone" that shows the typical range of realized vol. Comparing current IV against this cone reveals whether options are cheap or expensive relative to historical norms.

**Risk Management:** RV is used to set [[position-sizing|position sizes]], calculate [[value-at-risk|Value at Risk (VaR)]], and calibrate [[stop-loss]] levels. Higher RV means wider stops and smaller positions to maintain consistent risk.

**Regime Detection:** Sudden spikes in RV signal regime changes -- transitions from low-volatility trending markets to high-volatility choppy markets. [[trend-following]] strategies often scale down exposure when RV rises, while [[mean-reversion]] strategies may scale up.

**Volatility Targeting:** Volatility-targeting and risk-parity overlays scale position size inversely to trailing RV ($\text{weight} \propto \text{target vol} / \text{realized vol}$), so portfolio risk stays roughly constant across regimes — the position auto-deleverages as RV rises.

## Pitfalls and Limitations

- **It is backward-looking.** RV tells you how the asset *did* move, not how it *will* move. It is a noisy forecast of future vol; the market's [[implied-volatility|IV]] often forecasts better around known catalysts.
- **Window-length sensitivity.** 10-day RV and 252-day RV of the same name can differ 3×. Quoting "the realized vol" without the window is meaningless. Short windows react fast but are jumpy; long windows are stable but lag regime changes. The [[volatility-cone]] is the horizon-aware fix.
- **The overnight-gap blind spot.** Parkinson and Garman-Klass ignore close-to-open moves and under-measure gap-prone names; use Yang-Zhang for those.
- **Single bad prints dominate.** Because returns are squared, one un-split-adjusted or stale close creates a huge spurious term. Always clean and split/dividend-adjust the series first.
- **Stale / illiquid prices bias RV down.** Thinly traded assets with stale marks show artificially low RV — the price simply isn't updating, not that risk is low.
- **Microstructure noise** inflates high-frequency RV (bid-ask bounce); 5-minute sampling is the practical compromise.
- **Overlapping windows are autocorrelated**, so a series of rolling RVs is not a set of independent samples — relevant when building percentile bands for a cone.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=60` — OHLC bars for close-to-close or range-based RV estimators
- `GET /api/v1/volatility/regime` — per-asset volatility state (compressed / expanding / vol_shock / mean_reverting / normal) built server-side
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)

**Historical data:**
- `GET /api/v1/backtesting/klines` — deep kline archive for multi-year RV series
- `GET /api/v1/volatility/regime/{symbol}` — per-asset detail with rolling 60d history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=252"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — klines carry full OHLC, so any estimator in the table above is available: close-to-close from closes, Parkinson from high/low, Yang-Zhang from all four columns plus the prior close; annualize with √365 for crypto's continuous calendar, not √252
- **Live state** — `GET /api/v1/volatility/regime/{symbol}` gives a pre-classified vol state with 60d history when the agent needs a label rather than a number
- **Backtest** — RV-conditioned rules (vol targeting, RV-spike de-risking) replay against `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08); high-frequency RV from 1m klines is only possible since 2026-03-30, when the minute archive starts
- **Tip** — clean the series first per the pitfalls list: one stale or missing bar enters the sum squared, and crypto's 24/7 tape means no overnight gap — Parkinson/Garman-Klass lose their usual blind spot but still assume continuous trading through low-liquidity weekend hours

## Related

- [[implied-volatility]] -- forward-looking vol from options prices, the natural complement to RV
- [[vix]] -- the most widely followed measure of implied volatility
- [[volatility-risk-premium]] -- the persistent gap between IV and RV
- [[standard-deviation]] -- the statistical foundation of volatility measurement
- [[variance]] -- realized variance is the squared form that underlies [[variance-swap|variance swaps]]
- [[volatility-cone]] -- plots the RV distribution across horizons to judge whether IV is cheap or rich
- [[variance-swap]] -- the instrument that pays out on realized variance directly
- [[volatility-trading]] -- strategies that trade the spread between IV and RV
- [[options-greeks]] -- sensitivity measures, especially [[vega]]

## Sources

- (Source: [[book-option-volatility-and-pricing]]) -- detailed treatment of historical volatility calculation methods and their use in options trading
- Parkinson, M. (1980). *The Extreme Value Method for Estimating the Variance of the Rate of Return*. Journal of Business 53(1) — the high-low range estimator.
- Garman, M. and Klass, M. (1980). *On the Estimation of Security Price Volatilities from Historical Data*. Journal of Business 53(1).
- Yang, D. and Zhang, Q. (2000). *Drift-Independent Volatility Estimation Based on High, Low, Open, and Close Prices*. Journal of Business 73(3).
- General market knowledge for the IV/RV comparison framework; no further specific wiki source ingested yet.

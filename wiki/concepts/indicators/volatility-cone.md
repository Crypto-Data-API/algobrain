---
title: "Volatility Cone"
type: concept
created: 2026-04-15
updated: 2026-07-19
status: excellent
tags: [options, derivatives, volatility, indicators]
aliases: ["Volatility Cone", "Vol Cone", "Volatility Cones"]
related: ["[[realized-volatility]]", "[[implied-volatility]]", "[[iv-rank-and-iv-percentile]]", "[[volatility-term-structure]]", "[[volatility-regime-classification]]", "[[variance-risk-premium]]", "[[options-pricing]]", "[[mean-reversion]]"]
domain: [indicators, derivatives]
prerequisites: ["[[realized-volatility]]", "[[implied-volatility]]"]
difficulty: intermediate
---

A **volatility cone** is a chart that plots the historical distribution of [[realized-volatility|realized volatility]] across a range of measurement windows (e.g. 10-day, 30-day, 60-day, 90-day, 180-day), producing a funnel ("cone") shape that narrows as the lookback window lengthens. It is the canonical tool for answering "is current [[implied-volatility|implied volatility]] high or low relative to what this underlying has actually realized in the past?" — by overlaying the current IV term structure on the cone of historical realized-vol percentiles. The concept was introduced by Burghardt and Lane (1990) and remains a staple of options-desk and volatility-trader workflow.

## How It Works

For a chosen underlying, compute rolling [[realized-volatility|realized volatility]] over several fixed windows. For each window length `n` (in trading days), the procedure is:

1. Take a long history of returns (often 1–5 years).
2. Compute every overlapping `n`-day annualized realized vol: `σ_n = std(log returns over n days) × √252`.
3. From the resulting distribution of `σ_n` values, extract summary percentiles — typically the min, 25th, median, 75th, and max (some desks use 5th/95th instead of min/max to suppress outliers).

The annualized realized vol for each overlapping window is the [[realized-volatility|close-to-close estimator]] (or a higher-efficiency one):

$$\sigma_n = \sqrt{\frac{252}{n-1}\sum_{t=1}^{n}\left(r_t - \bar r\right)^2}, \qquad r_t = \ln\frac{P_t}{P_{t-1}}$$

Plotting these percentiles against window length `n` on the x-axis produces five lines that all converge toward the long-run mean as `n` grows — short windows have a wide spread (vol can be very low or very high over 10 days), long windows have a narrow spread (a 180-day realized vol is itself an average and varies little). The visual result is a sideways funnel: wide at the left (short horizons), narrow at the right (long horizons). This narrowing is a direct consequence of the [[mean-reversion|mean-reverting]] character of volatility and the central-limit averaging of longer windows.

### Illustrative cone (hypothetical large-cap, 3-year sample)

The numbers below are illustrative, not real data — they show the characteristic shape: wide spread at short horizons, narrowing at long horizons.

| Window (days) | Min | 25th pct | Median | 75th pct | Max | Current IV |
|---------------|-----|----------|--------|----------|-----|------------|
| 10 | 8% | 14% | 19% | 26% | 62% | 22% |
| 30 | 11% | 16% | 20% | 25% | 48% | **29%** |
| 60 | 13% | 17% | 20% | 24% | 39% | 23% |
| 90 | 14% | 18% | 21% | 23% | 34% | 21% |
| 180 | 16% | 19% | 21% | 23% | 29% | 20% |

Reading this cone: 30-day IV at **29%** plots *above* the 30-day 75th percentile (25%), so one-month options are rich versus this name's own one-month history — a sell-premium bias at that tenor. Every other tenor's IV sits inside the inter-quartile band (fairly priced). The cone has isolated a single expensive leg: a [[calendar-spread]] selling the 30-day and buying a cheaper tenor captures exactly this dislocation. Note how the Min-to-Max spread collapses from 8–62% at 10 days to 16–29% at 180 days — the funnel.

### Reading the cone

The cone is most useful when the **current implied-volatility [[volatility-term-structure|term structure]]** is overlaid on it. For each option expiration (mapped to the corresponding window length), plot the ATM IV as a single point:

- IV plotting **above the 75th-percentile line** of realized vol for that horizon → options are expensive relative to history; the underlying would have to realize in the top quartile of its own distribution to justify the price. Bias: sell premium.
- IV plotting **below the 25th-percentile line** → options are cheap; bias toward buying premium / long convexity.
- IV inside the inter-quartile band → fairly priced relative to history; no strong signal from the cone alone.

The cone thereby converts the abstract "IV looks high" intuition into a percentile statement anchored to the *same horizon* — a 30-day IV must be compared against 30-day realized-vol history, not against 10-day or annual numbers.

## Trading Relevance

The volatility cone is fundamentally a richer, horizon-aware version of [[iv-rank-and-iv-percentile|IV rank and IV percentile]]. Where IV rank collapses everything to a single number (where today's 30-day IV sits in its own 1-year range), the cone shows the *entire term structure* against the *full realized-vol distribution at each horizon* simultaneously. This matters because:

- **It separates "expensive vol" from "expensive vol at this tenor."** Front-month IV can be elevated while back-month IV is cheap; the cone reveals which leg of a [[volatility-term-structure|term-structure]] or [[calendar-spread|calendar]] trade carries the edge.
- **It frames the [[variance-risk-premium]] empirically.** Because IV is, on average, a forecast that exceeds subsequent realized vol, IV tends to plot in the upper half of the realized cone most of the time — visualizing the structural premium that premium-sellers harvest. When IV plots *below* the realized median, the premium has inverted, a stressed-regime tell (see [[volatility-regime-classification]]).
- **It informs strike and expiration selection.** A trader sizing a short strangle can read off the realized-vol percentile the breakeven move corresponds to, sanity-checking whether the implied breakeven is genuinely conservative versus the underlying's own history.

### Limitations and pitfalls

- **Overlapping windows induce autocorrelation.** Overlapping `n`-day realized-vol observations are highly serially correlated, so the percentile bands are not independent samples; treat them as descriptive, not as rigorous confidence intervals.
- **Regime dependence.** A cone built on a calm-dominated history understates the realized-vol distribution available in a [[volatility-regime|stressed regime]]. A cone fit through 2017 would not contain the [[covid-crash|March 2020]] tail. Always note the sample period.
- **Estimator choice matters.** Close-to-close realized vol ignores intraday range; Parkinson, Garman-Klass, and Yang-Zhang estimators use highs/lows/opens and give tighter, often more accurate cones for the same sample.
- **IV vs RV are not the same object.** The cone compares implied vol (a forward expectation) to realized vol (a backward measurement) — a useful relative-value frame, but not a strict apples-to-apples comparison, since IV legitimately embeds the [[variance-risk-premium]].

## Getting the Data (CryptoDataAPI)

The realized-volatility half of the cone builds entirely from klines; the API does not serve options IV, so the IV overlay must come from an options venue.

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — daily closes (and OHLC for range estimators) for rolling realized-vol windows
- `GET /api/v1/volatility/regime/{symbol}` — current per-asset vol state to note which regime the live reading sits in

**Historical data:**
- `GET /api/v1/backtesting/klines` — multi-year kline archive so the cone's sample spans full calm-and-crisis cycles

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — pull daily klines, compute every overlapping n-day annualized realized vol for n ∈ {10, 30, 60, 90, 180} (√365 annualization for crypto), and take the 5th/25th/50th/75th/95th percentiles per window — that is the whole cone
- **Sample depth** — `GET /api/v1/backtesting/klines` reaches back to 2017-08 on Binance spot, so a BTC cone can include the 2018, 2020, and 2022 vol tails rather than a calm-only sample — the regime-dependence pitfall above
- **Backtest** — replay "current 30d RV vs its own cone percentile" signals (e.g. vol-expansion entries from below the 25th percentile) against the same archive
- **Tip** — overlapping windows are serially correlated: treat cone percentile bands as descriptive context in agent decisions, never as independent confidence intervals for statistical tests

## Related

- [[realized-volatility]] — the input the cone is built from
- [[implied-volatility]] — the line overlaid on the cone for relative-value reading
- [[iv-rank-and-iv-percentile]] — the single-number cousin of the cone
- [[volatility-term-structure]] — the IV curve the cone is read against
- [[volatility-regime-classification]] — regime context that determines which cone sample is relevant
- [[variance-risk-premium]] — the structural gap the cone visualizes
- [[options-pricing]] — the framework relative value feeds into
- [[mean-reversion]] — why the cone narrows at longer horizons
- [[calendar-spread]] — the trade that exploits a single rich tenor the cone reveals
- [[standard-deviation]] — the statistical basis of each realized-vol point
- [[volatility-trading]] — the broader workflow the cone supports

## Sources

- Burghardt, G. and Lane, M. (1990). *How to Tell if Options Are Cheap*. Journal of Portfolio Management 16(2). The paper that introduced the volatility-cone construction.
- Natenberg, S. (1994). *Option Volatility and Pricing*. McGraw-Hill. Standard practitioner treatment of realized-vs-implied relative value.
- Yang, D. and Zhang, Q. (2000). *Drift-Independent Volatility Estimation Based on High, Low, Open, and Close Prices*. Journal of Business 73(3). The Yang-Zhang realized-vol estimator used in modern cones.
- Sinclair, E. (2013). *Volatility Trading* (2nd ed.). Wiley. Practical use of volatility cones in a systematic vol-trading workflow.

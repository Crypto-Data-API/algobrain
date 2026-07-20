---
title: "Laguerre Filter"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, crypto]
aliases: ["Laguerre", "Ehlers Laguerre Filter", "Laguerre RSI Filter", "Four-Element Laguerre"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[z-score]]", "[[hurst-exponent]]", "[[overfitting]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[john-ehlers]]", "[[microstructure-noise-low-timeframe]]", "[[supersmoother-filter]]", "[[jurik-moving-average]]", "[[alma]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[least-squares-moving-average]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[kalman-filter-trading]]", "[[bid-ask-spread]]", "[[false-signals]]", "[[standard-deviation]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis]
prerequisites: ["[[moving-averages]]", "[[exponential-moving-average]]"]
difficulty: advanced
---

# Laguerre Filter

The Laguerre Filter is a smoothing filter built from a four-stage cascade of Laguerre polynomial sections, introduced by [[john-ehlers|John Ehlers]] in the 2004 article "Time Warp – Without Space Travel" and in *Cybernetic Analysis for Stocks and Futures*. Its defining property is that it achieves heavy smoothing from a **very short data window** — a single damping coefficient, gamma, stretches the filter's effective lookback without requiring more bars of history. In the [[stretch-revert]] family it is the baseline used by `laguerre_stretch_revert`, chosen because it delivers roughly EMA-grade smoothness at lower lag.

Along with the [[supersmoother-filter|SuperSmoother]] and the proprietary [[jurik-moving-average|JMA]], it belongs to the **signal-processing group** of baselines: estimators designed as digital filters with an explicit frequency response, rather than as weighted averages of past prices.

## Construction

Four cascaded stages, each fed by the previous one, combined with binomial weights:

```
# gamma: damping factor, typically 0.4 - 0.8
L0 = (1-gamma)*price + gamma*L0[prev]
L1 = -gamma*L0 + L0[prev] + gamma*L1[prev]
L2 = -gamma*L1 + L1[prev] + gamma*L2[prev]
L3 = -gamma*L2 + L2[prev] + gamma*L3[prev]

Filt = (L0 + 2*L1 + 2*L2 + L3) / 6
```

Read the stages structurally:

- **L0** is an ordinary [[exponential-moving-average|EMA]] with smoothing constant `1-gamma`. At gamma = 0.8 that is an EMA with alpha = 0.2, roughly a 9-period EMA.
- **L1**, **L2**, **L3** are *all-pass* sections. Each one has unity gain — it does not attenuate anything — but delays lower frequencies more than higher ones. This is the "time warp": the stages manufacture the equivalent of extra history out of a handful of bars.
- The **1:2:2:1** combination is a binomial (FIR) smoother applied across the four time-warped taps, and is what turns the cascade into a low-pass filter.

Only four state variables need to be carried between bars. There is no rolling window, no `period` parameter, and no array of past closes — the entire memory of the filter is four floats, which is why it is cheap to run across a large perp universe on every 15m close.

## Filter behaviour

An averaging framing asks "how many bars do I include, and with what weights?" A DSP framing asks "which frequencies do I pass, and which do I attenuate, and what phase delay do I incur doing it?" The Laguerre Filter is designed in the second frame.

- **Low-pass with a gamma-controlled corner.** As gamma rises, the corner frequency drops: fewer cycles get through, and the output tracks only slower structure. At gamma = 0.4 the filter passes fairly short oscillations; at gamma = 0.8 it is stiff and only responds to multi-hour swings on a 15m chart.
- **Phase delay is frequency-dependent, not constant.** The all-pass stages delay low frequencies substantially while delaying high frequencies less. This is the mechanism trick and also the caveat: the filter's lag is not a single number you can quote, it depends on what is happening in the price.
- **It attenuates, it does not cancel.** Unlike the lag-cancelling designs ([[zero-lag-exponential-moving-average|ZLEMA]], [[triple-exponential-moving-average|TEMA]]) which subtract an estimate of the lag and thereby *amplify* high-frequency content, Laguerre only ever removes energy. It cannot overshoot the way a lag-cancelling filter can, which matters when the baseline is used as a reversion target rather than a trend signal.
- **Impulse response is short and non-negative in effect.** A single bad print decays out over a handful of bars rather than sitting in a window for N bars and then dropping out abruptly the way it does with an [[simple-moving-average|SMA]] (the "drop-off effect", where the SMA moves because an old bar left the window, not because anything happened now).

## Lag and smoothing trade-off

Concretely, at 15m bars:

| Baseline | Approximate smoothness | Approximate lag | Bars of state |
|---|---|---|---|
| SMA(20) | moderate, with drop-off artifacts | ~9.5 bars (fixed, (N-1)/2) | 20 |
| EMA(20) | moderate | ~9-10 bars at low frequencies | 1 |
| Laguerre, gamma = 0.5 | comparable to EMA(10-14) | notably less than the EMA it matches for smoothness | 4 |
| Laguerre, gamma = 0.8 | comparable to EMA(40-50) | high — approaching the EMA it matches | 4 |

The useful region is the middle: **gamma 0.5-0.7 buys smoothing that would otherwise cost a much longer EMA, at meaningfully less delay.** At the top of the range that advantage erodes — gamma = 0.9 is simply a very slow, very laggy filter, and you gain nothing over a long EMA except a smaller state footprint.

Gamma is not a period. There is no clean "gamma 0.6 equals a 27-period EMA" identity, because the effective lookback depends on the frequency content of the input. This is worth internalising before tuning: you cannot map gamma onto a bar count and reason about it the way you reason about SMA(20).

## Use as a mean-reversion baseline

In [[stretch-revert]], the baseline defines the mean and the residual defines the stretch. Everything the filter does to lag and noise propagates directly into which bars register as [[z-score|z-score]] extremes.

**Where Laguerre sits: middle-fast, and quiet.** It flags stretch **earlier than an SMA of comparable smoothness and slightly earlier than an equivalently-smooth EMA**, but far later than [[hull-moving-average|HMA]] or ZLEMA. That is deliberate for a fade: an over-eager baseline generates a stretch reading on every minor wobble, and the [[stretch-revert]] family's dominant failure mode is fading things that were never dislocations.

The mechanically important property is that **the residual `price - Filt` is clean**. Because the filter attenuates without overshoot, the residual series does not carry ringing artifacts of its own, so the rolling [[standard-deviation]] used to normalise the z-score is measuring price dispersion rather than filter dispersion. Filters that overshoot inflate their own residual sigma and quietly raise the entry threshold in a way nobody notices.

**Regimes that flatter it:**

- **Range-bound chop with periodic flushes.** The filter sits flat through the range; a liquidation flush produces a large, clean residual; the fade triggers on a genuine dislocation. This is the family's home regime ([[hurst-exponent|Hurst]] below ~0.5).
- **Noisy-but-mean-reverting mid-caps.** Gamma absorbs single-bar spikes without the SMA's drop-off wobble, so fewer entries are triggered by one print.

**Regimes that expose it:**

- **Persistent trends.** Nothing about Laguerre solves the walking-the-bands problem. A rising trend keeps price above the filter, generating a continuous short-stretch signal that keeps losing. The regime gate, not the filter, is what protects the strategy here.
- **Volatility regime shifts.** Gamma is fixed. When realised vol doubles, the filter does not adapt; the residual distribution widens and a fixed z threshold starts firing on ordinary bars. The adaptive members ([[frama|FRAMA]], [[vidya|VIDYA]], [[kama|KAMA]]) are the intended answer to this, which is exactly why the family runs them alongside.
- **Sharp regime turns.** Frequency-dependent delay means the filter's response to a genuine trend inception is slower than its response to noise — it will hold its old level for several bars into a real break, which reads as maximum stretch precisely when fading is worst.

Against its two group siblings: [[supersmoother-filter|SuperSmoother]] is the better *noise* rejector (it is built specifically to kill high-frequency content including [[microstructure-noise-low-timeframe|bid-ask bounce]]), while Laguerre is the better *low-state, low-lag* smoother. [[jurik-moving-average|JMA]] claims to dominate both, but its algorithm is proprietary and unverifiable.

## Parameters and tuning

| Parameter | Typical | Effect |
|---|---|---|
| `gamma` | 0.4 - 0.8 | Damping. Higher = smoother and laggier. Below 0.3 the filter is barely smoothing; above 0.85 it is a slow EMA with extra steps. |
| `entry_z` | 2.0 - 3.0 | Stretch threshold on the residual |
| `z_window` | 50 - 200 bars | Window for the residual sigma |

**Overfitting warning.** Gamma is a continuous knob on a filter that is already one of fourteen baselines being tested against the same history. Sweeping gamma in 0.05 steps across 0.30-0.85 is twelve variants of one member, on top of the family's fourteen members — the multiple-comparisons burden compounds multiplicatively, and the best (member, gamma) pair from that grid is nearly guaranteed to look good in-sample whether or not any edge exists. See [[overfitting]].

Practical discipline:

- Pick gamma from **filter characteristics** (how smooth do I want the mean to be?) rather than from **backtest P/L**. If the P/L surface across gamma is sharply peaked rather than a broad plateau, that is evidence of fitting, not of a correct setting.
- Prefer a single gamma across the whole traded universe. Per-asset gamma is a per-asset free parameter and multiplies the search space by the universe size.
- Any gamma chosen by optimisation must be deflated for the search before its Sharpe means anything.

## Advantages

- **Heavy smoothing from four state variables.** No rolling window, no warm-up array, trivially cheap across a wide perp universe and easy to keep identical between backtest and live.
- **Better smoothness-per-unit-lag than an EMA** in the useful gamma range — the actual reason it earns a slot in [[stretch-revert]].
- **No overshoot or ringing**, so the residual used for the z-score is uncontaminated by filter artifacts.
- **No drop-off effect** — the baseline never moves merely because an old bar aged out of a window, which is a real source of [[false-signals]] with SMA baselines.
- **Single intuitive knob.** One parameter is easier to defend against overfitting than a multi-parameter adaptive scheme.
- Published, fully specified, and reproducible — unlike [[jurik-moving-average|JMA]].

## Limitations

- **Gamma is not interpretable as a period**, so it cannot be compared like-for-like with the rest of the baseline stack, and cross-estimator "equal lookback" comparisons in the family are approximate at best.
- **Non-adaptive.** Fixed gamma through a volatility regime change means the residual distribution shifts under a static threshold.
- **Frequency-dependent phase delay** makes lag hard to quote or to reason about analytically; you have to measure it empirically on the actual series.
- **Does not solve the family's core risk.** Trend-regime fading kills the strategy regardless of the smoother; the filter choice changes the timing of the loss, not its existence.
- **Implementation variance.** Some published versions filter `(high+low)/2` rather than the close, and some apply the filter to a normalised series before computing a Laguerre RSI. Backtest and live must use the identical input series or the residuals will not agree.
- Warm-up matters: the four state variables need a few dozen bars to settle, and a filter seeded mid-history will disagree with one seeded from the same anchor date.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the closes the four-stage cascade is run over; 500 bars is far more than the filter needs but gives a stable residual sigma
- `GET /api/v1/hyperliquid/l2-book?coin=X` — spread check before acting on a residual; Laguerre smooths noise but does not tell you the stretch is bigger than the spread
- `GET /api/v1/derivatives/funding-rates?coin=X` — carry drag on a held reversion
- `GET /api/v1/derivatives/open-interest?coin=X` — OI expanding into the stretch argues trend, not dislocation

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for replaying the filter across full cycles
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels for scoring fades only inside historically-labelled range states

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [funding rates](https://cryptodataapi.com/funding-rates) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can compute and stress-test this filter directly:

- **Compute** — pull candles once, run the four-stage recursion forward over the closes, and carry `L0..L3` in state between polls; only the newest close is needed per bar, so the live update is O(1) and needs no window refetch.
- **Warm-up check** — recompute the filter from two different start offsets on the same `GET /api/v1/backtesting/klines` pull; if the outputs have not converged within ~50 bars, the backtest's early signals are seed artifacts and must be discarded.
- **Gamma sensitivity, not gamma optimisation** — evaluate gamma across 0.4/0.5/0.6/0.7 and check the result is a *plateau*. A sharp peak at one value is the [[overfitting]] signature; report the plateau, not the peak.
- **Cross-estimator diff** — compute Laguerre alongside [[supersmoother-filter|SuperSmoother]] on the identical bar set and flag bars where their z-scores disagree in sign. Those disagreements are where the estimator choice, not the reversion premium, is driving the trade.
- **Regime gate** — `GET /api/v1/quant/market` before acting; Laguerre's fixed gamma gives no protection against a trending regime, so the gate has to do that work.

## Related

[[stretch-revert]] · [[supersmoother-filter]] · [[jurik-moving-average]] · [[john-ehlers]] · [[moving-averages]] · [[adaptive-moving-averages]] · [[simple-moving-average]] · [[exponential-moving-average]] · [[alma]] · [[frama]] · [[vidya]] · [[kama]] · [[hull-moving-average]] · [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] · [[least-squares-moving-average]] · [[theil-sen-regression]] · [[quadratic-regression]] · [[kalman-filter-trading]] · [[mean-reversion]] · [[bollinger-bands]] · [[z-score]] · [[standard-deviation]] · [[hurst-exponent]] · [[microstructure-noise-low-timeframe]] · [[bid-ask-spread]] · [[false-signals]] · [[overfitting]] · [[cryptodataapi-hyperliquid]] · [[cryptodataapi-mcp]]

## Sources

- John Ehlers, "Time Warp – Without Space Travel" (2004) — the original presentation of the four-element Laguerre filter and the gamma time-warp argument.
- John Ehlers, *Cybernetic Analysis for Stocks and Futures* (2004) — book-length treatment, including the Laguerre RSI variant.
- Trading application, regime framing, and failure modes on this page are drawn from vault pages: [[stretch-revert]], [[mean-reversion]], [[moving-averages]], [[microstructure-noise-low-timeframe]], [[overfitting]].

No source-summary page exists for the Ehlers material in this vault yet, and no independent backtest of a Laguerre baseline has been reviewed here.

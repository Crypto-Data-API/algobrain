---
title: "Hull Moving Average (HMA)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, crypto]
aliases: ["HMA", "Hull Moving Average", "Hull MA"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[z-score]]", "[[hurst-exponent]]", "[[overfitting]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[alma]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[jurik-moving-average]]", "[[least-squares-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[kalman-filter-trading]]", "[[weighted-moving-average]]", "[[standard-deviation]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis]
prerequisites: ["[[moving-averages]]", "[[exponential-moving-average]]"]
difficulty: intermediate
---

# Hull Moving Average (HMA)

The Hull Moving Average, developed by Alan Hull in 2005, combines three weighted moving averages so that the lag of one cancels the lag of another, then re-smooths the noisy result with a short final pass. It is among the fastest-responding common moving averages — near-zero lag under a linear trend — and pays for that speed by **overshooting at turning points**, sometimes extrapolating past a reversal that has already happened.

## Construction

```python
import numpy as np

def wma(price, n):
    """Linearly weighted MA: newest bar gets weight n, oldest gets weight 1."""
    w = np.arange(1, n + 1, dtype=float)
    out = np.full(len(price), np.nan)
    for t in range(n - 1, len(price)):
        out[t] = np.dot(w, price[t - n + 1 : t + 1]) / w.sum()
    return out

def hma(price, n=20):
    """Hull Moving Average.

        HMA(n) = WMA( 2*WMA(price, n/2) - WMA(price, n),  sqrt(n) )

    The inner term is a lag-cancelling EXTRAPOLATION; the outer WMA
    re-smooths the noise that extrapolation creates.
    """
    half = int(round(n / 2))
    root = int(round(np.sqrt(n)))
    raw = 2.0 * wma(price, half) - wma(price, n)   # can lie OUTSIDE the price range
    return wma(raw, root)
```

There is only one parameter, `n`. Typical values are 9, 16, 20, and 55. The half-period and square-root period are derived, not tuned — `n = 20` gives `WMA(10)`, `WMA(20)`, and a final `WMA(4)`. Rounding convention for `n/2` and `√n` varies between implementations and produces small numerical differences; pin it explicitly if you are comparing platforms.

## Lag and smoothing trade-off

The inner term is the whole trick. A linearly weighted MA of length `n` has a centre-of-mass lag of `(n-1)/3` bars. At `n = 20`:

- `WMA(10)` lags **3.0** bars
- `WMA(20)` lags **6.33** bars
- `2 x WMA(10) - WMA(20)` lags `2(3.0) - 6.33 =` **−0.33** bars — it *leads* price
- the outer `WMA(4)` adds **1.0** bar back

Net lag ≈ **0.67 bars** under a constant-slope trend, versus 9.5 bars for a 20-bar [[simple-moving-average|SMA]]. That is a fourteen-fold reduction in lag from a one-line formula, which is why HMA is popular.

The cost is visible in the coefficients. The inner expression has weights `+2` and `−1`, so the absolute coefficient sum is 3 rather than 1. **Negative coefficients are what buy the speed, and negative coefficients amplify noise.** The raw inner series is markedly noisier than either input; the outer `WMA(√n)` exists solely to clean that up, and it only partly succeeds.

| Estimator (n = 20) | Approx. lag (bars) | Noise gain | Can overshoot? |
|---|---|---|---|
| [[simple-moving-average\|SMA]] | 9.5 | low | no |
| [[exponential-moving-average\|EMA]] | ~9.5 | low | no |
| [[alma\|ALMA]] (0.85, 6) | ~2.9 | low-moderate | no |
| **HMA** | **~0.7** | **>1** | **yes** |
| [[triple-exponential-moving-average\|TEMA]] | ~0 under linear trend | high | yes |
| [[zero-lag-exponential-moving-average\|ZLEMA]] | ~0 under linear trend | moderate-high | yes |

HMA sits in a narrow band: much faster than ALMA, but noticeably smoother than TEMA, because the outer re-smoothing pass has no analogue in TEMA's construction. In practice HMA traces a visually clean curve that nonetheless leads price — the combination that made it popular for trend-following, and the combination that makes it awkward as a mean-reversion baseline.

**The overshoot is not a bug, it is the mechanism.** Lag cancellation works by assuming the recent slope continues. When the slope reverses, the extrapolation points the wrong way, and HMA continues past the turn before curling back. On a sharp V-bottom, HMA will typically print a low *below* the actual low, one to two bars late.

## Use as a mean-reversion baseline

In [[stretch-revert]], `hma_stretch_revert` measures `resid = close - hma(close)`, converts it to a [[z-score]], and fades extremes. HMA's character as a baseline is dominated by two facts: it hugs price, and it overshoots.

**Stretch registers early, and rarely.** With ~0.7 bars of lag, essentially none of the residual is accumulated lag — every unit of deviation is genuinely new information. That is the good half: an HMA 2σ reading is a much stronger claim about dislocation than an SMA 2σ reading. The bad half is recall. Because the baseline tracks price so closely, the *typical* residual is small, so the residual σ used in the z-score is small too, and the estimator spends most of its life near z = 0. HMA fires seldom, and when it fires it is usually on a genuinely fast impulse — a liquidation flush, a news gap, a thin-book sweep. Fewer signals, higher average signal quality.

**The overshoot creates a specific, nameable failure at exactly the wrong moment.** The family's exit condition is "residual back through zero". At a genuine reversal HMA extrapolates past the turn, so the baseline can cross *through* price rather than price crossing through the baseline. Two consequences for the `hma_stretch_revert` member:

- **Premature scratch.** You enter on a −2.5σ flush; HMA overshoots downward chasing the move; the residual collapses toward zero within a bar or two without price having recovered anything. The exit fires, the trade books flat or slightly negative, and the actual reversion happens after you are out.
- **Sign inversion near the turn.** For a bar or two around a sharp pivot, `close - hma(close)` can flip sign purely because of the extrapolation. An entry taken on that flip is fading a stretch that does not exist. Requiring the residual to hold its sign for two consecutive bars before entry removes most of this, at the cost of a bar of lag — which is a defensible trade when the estimator's whole selling point is that it had none to spare.

**Which regimes flatter it:**

- *Range-bound chop punctuated by fast spikes.* This is HMA's best case. The baseline sits calmly in the middle of the range; a violent one- to three-bar displacement is far faster than even a 0.7-bar filter can track, so it registers cleanly and reverts fast enough that the overshoot has no time to distort the exit.
- *Liquid majors on 15m bars.* The noise amplification is survivable when the underlying series is clean.

**Which regimes expose it:**

- *Smooth, curving trends.* Where price accelerates and decelerates gradually, HMA's extrapolation is continuously slightly wrong in the direction of the prior slope, producing small persistent residuals with the wrong sign. This is the quiet, hard-to-notice failure — no dramatic loss, just a signal that is subtly anti-correlated with reality.
- *Thin alt perps.* Noise gain > 1 means HMA amplifies exactly the [[bid-ask-spread|bid-ask bounce]] the family most needs to reject. On an illiquid book, a fraction of the measured stretch is manufactured by the filter itself. The depth check via `l2-book` is not optional for this member.
- *Choppy reversals in sequence.* Repeated pivots mean repeated overshoots, and the residual becomes dominated by filter artefact rather than by price displacement.

Net: HMA is the family's **high-precision, low-recall** member on entries, but its exits are structurally unreliable and are the first thing to inspect if the member shows a high win rate with a small average win — the [[stretch-revert]] page's `theilsen` cautionary pattern, arriving by a different route.

## Parameters and tuning

`n` is the only parameter, which is HMA's main practical virtue over [[alma|ALMA]] (three parameters) and the adaptive estimators. But the single knob is coupled to everything:

| `n` | `WMA(n/2)` | `WMA(n)` | Final `WMA(√n)` | Character |
|---|---|---|---|---|
| 9 | 4 (rounded) | 9 | 3 | Very fast, very jittery; on 15m crypto this is mostly noise |
| 16 | 8 | 16 | 4 | Common compromise |
| 20 | 10 | 20 | 4 | Reasonable 15m default |
| 55 | 27 | 55 | 7 | Slow enough that stretch actually registers regularly |

Because the sub-periods derive from `n`, changing `n` changes the lag, the noise gain, and the overshoot magnitude simultaneously — you cannot trade one off against another. If you want more stretch signals, the only lever is a longer `n`, and a longer `n` also means a larger overshoot in absolute price terms.

Two secondary decisions matter more than they look:

- **Rounding.** `round()` vs `floor()` on `n/2` and `√n` changes values enough to shift marginal entries. Different platforms disagree. Pick one and record it.
- **Residual σ window.** The z-score denominator is computed over the residual series, and HMA residuals are small and heteroskedastic. Too short a window and σ tracks the current burst, so nothing ever looks extreme; too long and a vol regime change makes everything look extreme at once.

> **Overfitting warning.** One parameter is not protection. The searchable surface here is `n` × entry z × exit z × stop multiple × time-stop length × σ window, and [[stretch-revert]] runs fourteen estimators over that same surface. Finding the `n` that maximises historical P/L for HMA is a textbook multiple-comparisons exercise — see [[overfitting]], [[probability-of-backtest-overfitting]], and [[deflated-sharpe-ratio]]. **The commonly cited HMA periods (9, 16, 55) are folklore, not derived optima**; no study establishing an optimal HMA period for crypto perpetuals has been reviewed for this vault. Prefer a broad plateau over a sharp peak, and validate per [[regime-conditional-validation]].

## Advantages

- **Very low lag from a simple, deterministic formula** — ~0.7 bars at `n = 20` versus 9.5 for the SMA.
- **Single parameter**, so a much smaller overfitting surface than ALMA, KAMA, or the Kalman filter.
- **Smoother than the other lag-cancellers** — the outer `WMA(√n)` pass is real smoothing that TEMA and ZLEMA do not have.
- **Stateless FIR filter** — no seed dependence, so backtest and live values agree exactly given identical bars.
- As a mean-reversion baseline it is **high-precision**: a large HMA residual is nearly always real displacement, not accumulated lag.

## Limitations

- **Overshoots at turning points** — the defining flaw. It can extrapolate past a reversal, which is precisely where a mean-reversion strategy cares most.
- **Residual sign can invert** near pivots for filter reasons alone, producing phantom entries and premature exits.
- **Noise gain above 1** — it amplifies the microstructure noise that thin crypto books are full of.
- **Low recall as a stretch baseline** — hugs price closely enough that extremes rarely register, so the member accumulates trades slowly and statistical power arrives late.
- **Sub-periods are not independently tunable**; every property moves together with `n`.
- **Rounding conventions differ across platforms**, so "HMA(20)" is not a fully specified object.
- No peer-reviewed derivation exists; the construction is a heuristic that works, not a result.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — closes for the three nested WMAs; HMA needs only `n` bars of warm-up, but the residual σ wants the long history
- `GET /api/v1/hyperliquid/l2-book?coin=X` — mandatory for this member: HMA's noise gain > 1 means it amplifies bid-ask bounce into apparent stretch
- `GET /api/v1/derivatives/funding-rates?coin=X` — carry drag on held reversions
- `GET /api/v1/derivatives/open-interest?coin=X` — OI expanding into the move argues continuation, which is the case HMA's overshoot handles worst

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for sweeping `n` and measuring overshoot frequency at pivots
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels, for scoring HMA fades only inside historically range-labelled states

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=BTC&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with HMA specifically:

- **Measure the overshoot directly.** On history from `GET /api/v1/backtesting/klines`, flag every bar where `hma` falls outside `[min(low), max(high)]` of its own window. The frequency of that event, and its clustering around pivots, is the single most useful diagnostic for whether HMA is safe as a baseline on a given asset and timeframe.
- **Audit exits, not entries.** For each `hma_stretch_revert` trade, record whether the residual returned to zero because *price* moved or because *the baseline* moved. If the baseline is doing most of the work, the exit rule is reporting a reversion that did not happen.
- **Require sign persistence before entry.** Compute the residual on the latest two closed candles from `GET /api/v1/hyperliquid/candles`; skip entries where the sign has just flipped. This costs one bar of the ~0.7 bars of lag HMA saved, and removes most pivot-artefact entries.
- **Spread-gate harder than the other members.** Because noise gain exceeds 1, compare the measured stretch against several multiples of the current spread from `GET /api/v1/hyperliquid/l2-book?coin=X`, not one.
- **Stand down on trend.** `GET /api/v1/quant/market` and `GET /api/v1/volatility/regime/{symbol}` — HMA's extrapolation is *most* confident exactly when a trend is smooth and persistent, which is when the fade is most dangerous.

## Related

- [[stretch-revert]] — the family where HMA is the `hma_stretch_revert` baseline
- [[moving-averages]] · [[adaptive-moving-averages]] — the estimator landscape
- [[weighted-moving-average]] — the building block HMA is assembled from
- [[simple-moving-average]] · [[exponential-moving-average]] — reference points on the lag/noise frontier
- [[alma]] — achieves low lag *without* overshoot, using positive weights only
- [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] — the other lag-cancelling estimators, with the same overshoot pathology
- [[frama]] · [[vidya]] · [[kama]] · [[jurik-moving-average]] — data-adaptive alternatives
- [[least-squares-moving-average]] · [[theil-sen-regression]] · [[quadratic-regression]] — regression baselines
- [[laguerre-filter]] · [[supersmoother-filter]] · [[kalman-filter-trading]] — signal-processing and state-space baselines
- [[mean-reversion]] — the underlying thesis
- [[bollinger-bands]] — band formulation of the same deviation idea
- [[z-score]] · [[standard-deviation]] — turning the residual into a signal
- [[hurst-exponent]] — the mandatory regime gate
- [[overfitting]] — the risk in tuning `n`

## Sources

- **Alan Hull (2005)** — original specification of the Hull Moving Average, published by Hull as a trading indicator rather than as academic work.
- Lag figures on this page are derived from the centre-of-mass lag of a linearly weighted MA, `(n-1)/3`, applied to the nested construction above — not quoted from a source.

*Verification note: no peer-reviewed publication or independent empirical evaluation of HMA has been reviewed for this vault. Statements about "best" periods circulating in trading communities are convention, not evidence, and the overshoot behaviour described here follows from the formula rather than from a published study.*

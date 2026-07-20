---
title: "ALMA (Arnaud Legoux Moving Average)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, crypto]
aliases: ["ALMA", "Arnaud Legoux Moving Average", "Gaussian Offset Moving Average"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[z-score]]", "[[hurst-exponent]]", "[[overfitting]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[jurik-moving-average]]", "[[least-squares-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[kalman-filter-trading]]", "[[standard-deviation]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis]
prerequisites: ["[[moving-averages]]", "[[exponential-moving-average]]"]
difficulty: intermediate
---

# ALMA (Arnaud Legoux Moving Average)

The Arnaud Legoux Moving Average (ALMA) applies **Gaussian weights** to a fixed lookback window, but shifts the peak of the Gaussian away from the centre of the window and toward the most recent bar. That shift is controlled by an explicit `offset` parameter, which turns the usual lag-versus-smoothness compromise into a dial the user sets directly rather than a fixed property of the formula. It was developed by Arnaud Legoux and Dimitrios Kouzis-Loukas and released in 2009.

## Construction

ALMA takes three parameters: the window `n`, the `offset` (0..1, default **0.85**), and `sigma` (default **6**).

```python
import numpy as np

def alma(price, n=20, offset=0.85, sigma=6.0):
    """Arnaud Legoux Moving Average.

    offset : 0..1 — where the Gaussian peak sits in the window.
             1.0 -> peak fully on the newest bar (minimum lag)
             0.0 -> peak on the oldest bar
             0.5 -> centred, i.e. a symmetric Gaussian (maximum smoothness)
    sigma  : width/sharpness of the Gaussian. Larger sigma -> narrower bell
             (s = n / sigma), so fewer bars carry meaningful weight.
    """
    m = offset * (n - 1)          # index of the Gaussian peak within the window
    s = n / sigma                 # standard deviation of the Gaussian, in bars
    i = np.arange(n)              # i = 0 is the OLDEST bar, i = n-1 the newest
    w = np.exp(-((i - m) ** 2) / (2 * s * s))

    out = np.full(len(price), np.nan)
    for t in range(n - 1, len(price)):
        window = price[t - n + 1 : t + 1]
        out[t] = np.dot(w, window) / w.sum()
    return out
```

The weights are computed once and reused — ALMA is a fixed-coefficient FIR filter, not a recursive one. It has no state and no warm-up dependence beyond the `n` bars in the window, which makes backtest and live values identical given the same bars (unlike the [[exponential-moving-average|EMA]], whose value depends on its seed).

With the defaults at `n = 20`: `m = 0.85 x 19 = 16.15` and `s = 20/6 = 3.33` bars. The bell therefore peaks about **3 bars back** from the newest bar and has an effective width of roughly ±6 bars. Bars older than about index 5 receive weights below 1% of peak and contribute essentially nothing — the nominal window of 20 is much longer than the effective one.

## Lag and smoothing trade-off

Because the weights are strictly positive and sum to one, ALMA is a **convex combination** of prices. Two consequences follow, and they are the whole reason it sits where it does on the frontier:

1. **It can never overshoot the price range in its window.** Unlike [[hull-moving-average|HMA]], [[triple-exponential-moving-average|TEMA]], and [[zero-lag-exponential-moving-average|ZLEMA]] — all of which use negative coefficients to cancel lag — ALMA cannot extrapolate past a turning point. It buys its speed by *reweighting*, not by *extrapolating*.
2. **It never amplifies noise.** Its variance gain is strictly below 1. TEMA's coefficients sum to 1 but their absolute values sum to 7; ALMA's absolute values sum to exactly 1.

Approximate lag at `n = 20`, measured as the centre of mass of the weights relative to the newest bar:

| Estimator (n = 20) | Approx. lag (bars) | Noise gain | Can overshoot? |
|---|---|---|---|
| [[simple-moving-average\|SMA]] | 9.5 | low (1/√20) | no |
| [[exponential-moving-average\|EMA]] | ~9.5 | low | no |
| **ALMA (0.85, 6)** | **~2.9** | low-moderate | **no** |
| ALMA (0.99, 6) | ~0.2 | high (few bars carry weight) | no |
| [[hull-moving-average\|HMA]] | ~0.7 | >1 | yes |
| [[triple-exponential-moving-average\|TEMA]] | ~0 under linear trend | high | yes |

At the defaults the weights are worth roughly **8–9 "effective bars"** of averaging (Kish effective sample size, `(Σw)² / Σw²`), so residual noise is suppressed to about 1/√8.6 ≈ 0.34 of the raw series — versus 0.22 for a 20-bar SMA. ALMA gives up about a third of the SMA's noise suppression to remove roughly two thirds of its lag. That is a genuinely good exchange rate, and it is why ALMA is a common default choice among the adaptive family (see [[adaptive-moving-averages]]).

Note that ALMA is only "adaptive" in the sense that the *user* can tune the shape. Unlike [[kama|KAMA]], [[frama|FRAMA]], or [[vidya|VIDYA]], its coefficients do not change with the data. It is a fixed filter with an unusually good shape.

## Use as a mean-reversion baseline

In the [[stretch-revert]] family (`alma_stretch_revert`), ALMA is the baseline from which the deviation is measured: `resid = close - alma(close)`, then a [[z-score]] over the residual series, and a fade when `|z|` exceeds the entry threshold. Its behaviour as a baseline is distinctive on three counts.

**Stretch registers on genuine displacement, not on accumulated lag.** With a laggy baseline like a 20-bar [[simple-moving-average|SMA]], most of the residual at any given moment is simply "the baseline has not caught up yet". A 2σ reading is largely a statement about drift, not about dislocation. ALMA's ~3-bar lag strips most of that out, so a 2σ ALMA residual is far more likely to be a real, fast displacement — the forced-flow overshoot the family is actually trying to fade. Precision rises; trade count falls.

**It does not manufacture the "walking the bands" failure.** The dominant killer of the family is fading a trend that keeps going. A laggy baseline generates a persistent one-sided residual for the entire duration of a trend, so it fires repeatedly into the move. ALMA follows the drift closely enough that a steady trend produces only a modest, non-growing residual — the signal quietly stops firing rather than firing wrongly. This is protection *by construction*, and it is complementary to (not a substitute for) the mandatory [[hurst-exponent]] regime gate.

**It never flips the residual sign at a turn.** Because ALMA cannot overshoot, the residual crosses zero only when price actually crosses the baseline. The exit condition ("z back through zero") therefore means what it says. Compare [[hull-moving-average|HMA]] and [[zero-lag-exponential-moving-average|ZLEMA]], whose extrapolation can flip the residual sign a bar after entry and scratch a trade that had not gone anywhere.

**Which regimes flatter it:**

- *Range-bound chop with a stable level* — the home regime. ALMA sits near the middle of the range, residuals are roughly symmetric, and the fade thesis matches the data-generating process.
- *Sharp liquidation flushes inside a range* — the ideal case. Price displaces several bars faster than a 3-bar-lag filter can follow, producing a large, honest residual.

**Which regimes expose it:**

- *Sustained directional trends* — as above, ALMA under-signals rather than mis-signals, but the family's real risk here is the trades it does take: a trend that pauses, produces a stretch, and then resumes.
- *Very thin books* — ALMA's low lag means it responds quickly to a single wide print. On an illiquid alt perp, bid-ask bounce can register as a residual. This is a data-quality problem, not an ALMA problem, and the fix is the depth check, not a slower filter.
- *Volatility regime shifts* — the residual σ used for the z-score is backward-looking. When realised vol steps up, ALMA residuals inflate and every threshold fires at once. Recompute σ over a window matched to the current [[volatility-regime-classification|vol regime]].

## Parameters and tuning

| Parameter | Default | Effect of increasing |
|---|---|---|
| `n` (window) | 9–21 typical | More bars in the bell; smoother, laggier, fewer stretch signals |
| `offset` | 0.85 | Peak moves toward the newest bar: less lag, less smoothing, **more** raw-price hugging and **fewer** stretch triggers |
| `sigma` | 6 | Narrower bell (`s = n/sigma`): fewer bars carry weight, so the filter gets faster and noisier |

`offset` and `sigma` interact — raising `sigma` narrows the bell, which makes `offset` matter less because there are fewer bars to shift across. Treat them as one two-dimensional knob, not two independent ones.

For [[stretch-revert]] specifically, the counter-intuitive move is worth stating: **lowering `offset` increases the trade count**, because a laggier baseline produces larger residuals. Whether those extra trades are edge or noise is exactly the question the regime gate and the cost model exist to answer — do not assume more signals is better.

> **Overfitting warning.** ALMA gives you three continuous parameters on top of the entry threshold, the exit threshold, the stop multiple, and the time-stop length. A grid search over all of them on crypto's short history will find a combination that looks excellent and means nothing — see [[overfitting]] and [[probability-of-backtest-overfitting]]. The published defaults (0.85 / 6) have no theoretical derivation that this vault has verified; they are convention, i.e. **folklore**, and should be treated as a prior rather than an optimum. If a parameter set only works in a narrow neighbourhood of itself, it is fitted. Prefer a broad plateau in the parameter surface over a sharp peak, and validate per [[regime-conditional-validation]] before believing any of it.

## Advantages

- **The lag/smoothness trade-off is an explicit parameter**, not a fixed property. No other common estimator exposes it this directly.
- **Cannot overshoot or invert the residual sign** — positive weights only. Residual-zero-crossings are meaningful exits.
- **Never amplifies noise** (variance gain < 1), unlike TEMA, ZLEMA, and HMA.
- **Stateless and reproducible** — no seed dependence, so backtest and live values agree exactly given identical bars.
- Achieves roughly a 3-bar lag at `n = 20` while retaining ~8–9 effective bars of averaging — a favourable point on the frontier.

## Limitations

- **Not genuinely adaptive.** The coefficients are fixed at configuration time. In a regime shift it does not change speed the way [[kama|KAMA]], [[frama|FRAMA]], or [[vidya|VIDYA]] attempt to.
- **Three parameters is three degrees of freedom** and a large overfitting surface.
- **The nominal window overstates the real one.** ALMA(20, 0.85, 6) uses maybe 9 bars meaningfully; comparing "ALMA(20)" to "SMA(20)" as if the lookbacks match is misleading.
- **The defaults are unverified convention.** No peer-reviewed derivation of `offset = 0.85, sigma = 6` is known to this vault.
- **O(n) per bar**, not O(1) recursive. Irrelevant at 15m bars; relevant if you are computing hundreds of assets on a 1s loop.
- Being a low-lag filter, it responds quickly to bad ticks as well as to good information.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the OHLCV closes ALMA is computed over; 500 bars is far more than the ~9 effective bars the filter needs, but the residual σ for the [[z-score]] wants the longer history
- `GET /api/v1/hyperliquid/l2-book?coin=X` — spread/depth check before treating a low-lag residual as a real dislocation
- `GET /api/v1/derivatives/funding-rates?coin=X` — carry cost on any reversion held past a funding stamp
- `GET /api/v1/derivatives/open-interest?coin=X` — OI building into the stretch argues trend, not fade

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for sweeping `offset`/`sigma` over long history
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels for scoring ALMA residuals only inside range-labelled states

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books) · [funding rates](https://cryptodataapi.com/funding-rates)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with ALMA specifically:

- **Sweep the offset, not the window.** Compute ALMA at `offset` ∈ {0.6, 0.75, 0.85, 0.95} over one pull of `GET /api/v1/hyperliquid/candles` and plot trade count against net P/L. The shape of that curve — plateau or spike — is the fastest available read on whether the parameter is fitted.
- **Verify the no-overshoot property empirically.** Assert `min(window) <= alma <= max(window)` on live bars. Any violation means a coding error (usually an index-direction bug where `i = 0` was treated as the newest bar, which silently inverts `offset`).
- **Cross-check against the fast siblings.** Compute ALMA alongside [[hull-moving-average|HMA]], [[triple-exponential-moving-average|TEMA]], and [[zero-lag-exponential-moving-average|ZLEMA]] on the same bars. When ALMA shows stretch and the extrapolating filters do not, the deviation is probably genuine displacement rather than curvature artefact.
- **Gate before sizing.** `GET /api/v1/quant/market` and `GET /api/v1/volatility/regime/{symbol}` decide whether an ALMA residual should be traded at all — a clean 2.5σ reading inside a strong-trend regime is a good signal to stand down, per [[stretch-revert]].
- **Reconcile backtest to live.** ALMA is stateless, so any divergence between replayed and live values is a bar-alignment or timezone problem, never a warm-up problem. Compare `GET /api/v1/backtesting/klines` against the live candle series before blaming the filter.

## Related

- [[stretch-revert]] — the strategy family where ALMA serves as the `alma_stretch_revert` baseline
- [[moving-averages]] — the estimator landscape
- [[adaptive-moving-averages]] — the family ALMA is usually grouped with
- [[simple-moving-average]] · [[exponential-moving-average]] — the reference points on the lag/noise frontier
- [[hull-moving-average]] · [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] — the lag-cancelling alternatives that *can* overshoot
- [[frama]] · [[vidya]] · [[kama]] · [[jurik-moving-average]] — genuinely data-adaptive estimators
- [[least-squares-moving-average]] · [[theil-sen-regression]] · [[quadratic-regression]] — regression-based baselines
- [[laguerre-filter]] · [[supersmoother-filter]] · [[kalman-filter-trading]] — signal-processing and state-space baselines
- [[mean-reversion]] — the underlying thesis
- [[bollinger-bands]] — the band formulation of the same deviation idea
- [[z-score]] · [[standard-deviation]] — how the residual becomes a signal
- [[hurst-exponent]] — the regime gate that must pass before any fade
- [[overfitting]] — the main risk in tuning `n`, `offset`, and `sigma`

## Sources

- **Arnaud Legoux and Dimitrios Kouzis-Loukas (2009)** — original ALMA specification, released publicly as an indicator rather than as a peer-reviewed paper. The `offset = 0.85, sigma = 6` defaults trace to that release.
- Filter properties on this page (centre-of-mass lag, effective sample size, variance gain) are derived directly from the weight formula above rather than quoted from a source.

*Verification note: no peer-reviewed publication for ALMA has been located, and no empirical study of its default parameters has been reviewed for this vault. Claims about optimal `offset`/`sigma` values circulating in trading communities should be treated as convention, not evidence.*

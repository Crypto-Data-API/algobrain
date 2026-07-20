---
title: "FRAMA (Fractal Adaptive Moving Average)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, crypto, market-regime, regime-detection]
aliases: ["FRAMA", "Fractal Adaptive Moving Average", "Ehlers FRAMA"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[z-score]]", "[[hurst-exponent]]", "[[overfitting]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[regime-detection]]", "[[technical-structural-regime]]", "[[kama]]", "[[vidya]]", "[[alma]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[jurik-moving-average]]", "[[least-squares-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[kalman-filter-trading]]", "[[john-ehlers]]", "[[fractal-dimension]]", "[[standard-deviation]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis]
prerequisites: ["[[moving-averages]]", "[[exponential-moving-average]]"]
difficulty: intermediate
---

# FRAMA (Fractal Adaptive Moving Average)

FRAMA is an [[exponential-moving-average|EMA]] whose smoothing constant is recomputed every bar from an estimate of the **fractal dimension** of recent price. Introduced by [[john-ehlers|John Ehlers]] in "FRAMA – Fractal Adaptive Moving Average" (2005), it is built on a geometric intuition: a trending price path is close to a straight line (dimension near 1), while a choppy path folds back on itself and begins to fill the plane (dimension near 2). FRAMA turns that measured roughness directly into filter speed, so the same line tracks price tightly in a trend and smooths heavily in chop — no parameter change required.

It is one of the three members of the [[adaptive-moving-averages|adaptive family]] used as baselines in [[stretch-revert]], alongside [[vidya|VIDYA]] (which adapts to volatility/momentum) and [[kama|KAMA]] (which adapts to an efficiency ratio). All three vary the smoothing constant; they differ entirely in *what they measure* to do it.

## Construction

Over a window of `n` bars (`n` even), split the window into two halves and compare the normalised price range of each half against the range of the whole:

```python
import math

def frama(price_high, price_low, price_close, n=16,
          alpha_min=0.01, alpha_max=1.0):
    """Ehlers (2005) Fractal Adaptive Moving Average.

    n           : lookback window, must be even (default 16)
    alpha_min   : smoothing floor  (default 0.01 -> ~ 200-bar EMA)
    alpha_max   : smoothing ceiling (default 1.00 -> price itself)
    """
    half = n // 2
    out = [price_close[0]] * len(price_close)

    for t in range(n, len(price_close)):
        h1 = max(price_high[t-n     : t-half]); l1 = min(price_low[t-n     : t-half])
        h2 = max(price_high[t-half  : t     ]); l2 = min(price_low[t-half  : t     ])
        h3 = max(price_high[t-n     : t     ]); l3 = min(price_low[t-n     : t     ])

        N1 = (h1 - l1) / half          # normalised range, first half
        N2 = (h2 - l2) / half          # normalised range, second half
        N3 = (h3 - l3) / n             # normalised range, whole window
        if N1 <= 0 or N2 <= 0 or N3 <= 0:
            out[t] = out[t-1]
            continue

        # Fractal dimension estimate: D in [1, 2]
        D = (math.log(N1 + N2) - math.log(N3)) / math.log(2)

        alpha = math.exp(-4.6 * (D - 1.0))
        alpha = min(max(alpha, alpha_min), alpha_max)

        out[t] = alpha * price_close[t] + (1 - alpha) * out[t-1]

    return out
```

The constant **4.6** is not arbitrary: it is chosen so the mapping spans the useful range of EMA speeds. At `D = 1` (perfectly straight path) `alpha = exp(0) = 1`, and the filter simply *is* price. At `D = 2` (maximally jagged) `alpha = exp(-4.6) ≈ 0.010`, equivalent to roughly a 200-period EMA. Everything between interpolates geometrically: `D = 1.5` gives `alpha ≈ 0.10` (~19-period EMA), `D = 1.8` gives `alpha ≈ 0.033` (~60-period EMA).

Common defaults: `n = 16` on 15m bars, clamp `[0.01, 1.0]`. Many implementations use closes only rather than high/low for the range terms; this makes the estimate noisier and biases `D` upward slightly, but is acceptable when only close data is available.

## What it adapts to

FRAMA adapts to **path roughness** — how much distance price travelled relative to how much ground it covered, measured geometrically through box ranges at two scales.

What that signal *does* capture:

- **Trend vs. chop, direction-agnostic.** A clean move up and a clean move down both produce low `D`. FRAMA speeds up for either.
- **Scale-invariance of the wiggle.** Because it compares a half-window range to a full-window range, it responds to the *structure* of the move, not its magnitude. A 0.4% clean drift and a 12% clean drift both register as low `D`.
- **Onset of consolidation.** When two halves of the window each cover nearly the full range of the whole, `N1 + N2 ≈ 2·N3` and `D → 2`. Price is thrashing inside a box.

What it does **not** capture:

- **Volatility level.** FRAMA is blind to whether the market is quiet or violent, provided the path shape is the same. A low-vol grind and a high-vol trend both look like `D ≈ 1.2`. This is the sharpest contrast with [[vidya|VIDYA]], which adapts to precisely the quantity FRAMA ignores.
- **True Hausdorff dimension.** Be explicit about this: the two-half box-range estimator is a **heuristic**, not a rigorous fractal dimension. It uses exactly two scales, on a window of 16–32 bars, with `high`/`low` as a crude proxy for box occupancy. Real dimension estimation requires many scales and far more data. The number is useful as a *regime indicator*, and misleading if treated as a measured physical property.
- **Long-memory / persistence.** The [[hurst-exponent]] measures a related but distinct property — the autocorrelation structure of increments over many scales — and the textbook relation `D = 2 − H` holds only for idealised fractional Brownian motion, not for a 16-bar range heuristic on financial prices. Use Hurst for the regime gate in [[stretch-revert]]; use FRAMA's `D` as an internal filter control, not as a substitute Hurst estimate.

## Lag and smoothing trade-off

Ordinary filters occupy a single point on the lag/noise frontier: an [[simple-moving-average|SMA(20)]] has ~9.5 bars of lag and strong noise rejection; an [[exponential-moving-average|EMA(20)]] has ~9.5 bars of effective lag with a longer tail and slightly worse whipsaw behaviour. You pick one and live with it in every regime.

FRAMA does not sit at a point — it **travels along the frontier**:

| Regime | Estimated `D` | `alpha` | Effective EMA period |
|---|---|---|---|
| Sharp directional impulse | ~1.05 | ~0.79 | ~1.5 bars |
| Clean trend | ~1.3 | ~0.25 | ~7 bars |
| Mild drift | ~1.5 | ~0.10 | ~19 bars |
| Choppy range | ~1.8 | ~0.033 | ~60 bars |
| Dead chop | ~2.0 | 0.01 | ~200 bars |

Compared with the fixed alternatives: in a trend FRAMA is *faster* than a same-`n` EMA, often dramatically; in a range it is far *slower* than either the SMA or EMA of the same window. The realised lag is therefore state-dependent, and that is the point.

The cost is that FRAMA's response is **discontinuous in character**. `alpha` can jump from 0.03 to 0.6 between consecutive bars when a range breaks, producing a visible kink in the line. Fixed-weight smoothers like [[alma|ALMA]] or the [[supersmoother-filter|SuperSmoother]] never do this; their output is smooth by construction. FRAMA trades output smoothness for regime adaptivity.

## Use as a mean-reversion baseline

In [[stretch-revert]], the baseline defines "fair value" and the trade is a fade of the residual `price − baseline`, normalised into a [[z-score]] against a rolling [[standard-deviation]]. FRAMA is the `frama_stretch_revert` member's estimator.

**The case for it.** The strategy's dominant failure mode is fading a genuine trend ("walking the bands"). FRAMA is structurally sympathetic to that problem: when the market turns directional, `D` falls, `alpha` rises, and the baseline chases price. The residual collapses toward zero and the z-score stops firing. The filter itself functions as a soft trend gate, layered underneath the explicit [[hurst-exponent]] and [[technical-structural-regime]] gates.

**The problem — adaptive-baseline suppression.** That same behaviour is a liability, and it is the central trade-off of every adaptive baseline. The stretch you most want to trade is a *fast, violent* move — a liquidation flush that overshoots and snaps back. But a fast move is exactly a low-`D` move. FRAMA reads the flush as "clean trending path", raises `alpha` toward 0.5–0.9, and the baseline **runs down with the price**. The measured deviation is mechanically suppressed at the precise moment the real dislocation is largest.

Concretely: a 3% one-bar flush against a `D = 1.9` baseline (`alpha = 0.017`) leaves nearly the whole 3% in the residual. The same flush after `D` has dropped to 1.15 (`alpha ≈ 0.50`) leaves roughly half of it. Same dislocation, half the signal — and if the flush persists two or three bars, the baseline can arrive at the new price before the fade ever triggers.

There is a second-order version of the same issue: the rolling σ used for the z-score is computed on `price − baseline`. When the baseline speeds up, residuals shrink, σ shrinks, and z-scores get *re-inflated* on a lag. The result is an entry threshold that drifts around for reasons unrelated to market dislocation.

**Regimes that flatter FRAMA as a baseline:**
- Sustained range with sharp, brief excursions — high `D` holds the baseline still, so the excursion registers at full size and reverts into a stationary reference.
- Post-flush consolidation, where the fade target does not move under the position.
- Assets whose chop is genuinely mean-reverting on the trade horizon (Hurst < 0.45).

**Regimes that expose it:**
- Multi-bar directional expansion. FRAMA suppresses the signal on the way out and then, if a fade does trigger, the baseline keeps travelling — so the exit target moves *away* mid-trade.
- Volatility regime shifts with unchanged path shape. Because FRAMA ignores volatility level, a doubling of realised vol at constant `D` leaves `alpha` untouched while every residual doubles. The z-score absorbs some of this via σ, but only with the σ window's lag.
- Very short windows on 1m bars, where high/low ranges are dominated by [[bid-ask-spread|spread]] and the `D` estimate is mostly microstructure noise.

The honest summary: FRAMA reduces the trend-fade failure mode and, by the same mechanism, reduces measured stretch during the fastest dislocations. Whether that is a net gain is an empirical question specific to the asset and timeframe, and it is why [[stretch-revert]] runs fixed-lag estimators alongside adaptive ones rather than choosing between them.

## Parameters and tuning

| Parameter | Typical | Notes |
|---|---|---|
| `n` (window) | 16 (range 10–40, must be even) | Below ~10 the `D` estimate is noise; above ~40 it stops distinguishing regimes within the trade horizon |
| `alpha_min` | 0.01 | The floor matters more than it looks — it sets the slowest the baseline can be, i.e. how "sticky" the fair value is in chop |
| `alpha_max` | 1.0 | Some implementations cap at 0.5 to stop the baseline from collapsing onto price during impulses; this directly mitigates the suppression problem above |
| Decay constant | 4.6 | Ehlers' original. Lowering it to ~3.0 compresses the speed range; raising it makes chop-mode slower still |
| Range input | high/low | Close-only is common but noisier and biases `D` up |
| σ window (z-score) | 50–100 bars | Set independently of `n`; coupling them creates a hidden extra degree of freedom |

**Overfitting warning.** FRAMA presents an unusually rich surface to tune: `n`, both clamps, the decay constant, the range input, and then the z-score window, entry threshold, exit threshold, stop multiple, and time stop on top. That is easily eight or nine free parameters on a single strategy member. Sweeping them all against a few years of crypto history will produce an impressive equity curve for reasons that have nothing to do with edge — see [[overfitting]] and [[probability-of-backtest-overfitting]]. Practical discipline:

- Hold the decay constant at 4.6 and the clamps at Ehlers' defaults. Treat them as fixed, not as parameters.
- Tune `n` on a coarse grid only (12 / 16 / 24 / 32) and require the result to be a plateau, not a spike.
- Never tune FRAMA's internals and the z-score thresholds in the same sweep — the two interact strongly and the joint search space is where curve-fitting lives.
- Remember that [[stretch-revert]] already runs fourteen estimators. A per-estimator parameter search compounds that multiple-comparisons problem; deflate accordingly ([[deflated-sharpe-ratio]]).

## Advantages

- Genuinely regime-adaptive with **one** primary parameter (`n`) — fewer knobs than most adaptive filters.
- Direction-agnostic: reacts to trend structure regardless of sign, so it does not need a separate trend filter to behave.
- The dimension estimate is cheap: three max/min scans per bar, no matrix algebra, no iteration. Trivial to run across a wide universe on 1m bars.
- Speeds up in trends without the overshoot artifacts of lag-cancelling filters like [[triple-exponential-moving-average|TEMA]] or [[zero-lag-exponential-moving-average|ZLEMA]].
- The internal `D` series is independently useful as a cheap chop/trend diagnostic, complementary to [[regime-detection]] overlays.

## Limitations

- **The fractal dimension is a heuristic, not a measurement.** Two scales, a short window, and high/low as a box proxy. It correlates with roughness; it is not the Hausdorff dimension and should never be reported as one.
- Blind to volatility level — see [[vidya|VIDYA]] for the complementary blindness (VIDYA sees volatility and not path efficiency).
- `alpha` can jump sharply between bars, producing kinks that look like signal but are filter artifacts.
- Gappy or illiquid series break the range estimator: a single wick can dominate `N1`, `N2`, or `N3` and swing `D` by 0.3 or more.
- Requires high/low data for the standard formulation, which rules out some derived or synthetic series.
- The suppression problem above makes it a structurally awkward baseline for measuring fast dislocations, which is the very thing [[stretch-revert]] trades.
- Little independent published validation. Ehlers' presentation is a design rationale, not a study; there is no widely replicated evidence that FRAMA outperforms a well-chosen fixed filter net of costs.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — OHLC bars; FRAMA needs high/low, not just closes, for the `N1`/`N2`/`N3` range terms
- `GET /api/v1/quant/market` — current HMM regime probabilities, for cross-checking FRAMA's implied regime against an independent classifier
- `GET /api/v1/volatility/regime/{symbol}` — volatility state, which FRAMA is structurally blind to
- `GET /api/v1/hyperliquid/l2-book?coin=X` — spread/depth check before acting on a low-timeframe `D` reading
- `GET /api/v1/derivatives/open-interest?coin=X` — OI expansion alongside falling `D` distinguishes a real trend from a range break that will fail

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for replaying `D` and `alpha` across full cycles
- `GET /api/v1/quant/regimes/history` — hourly regime labels since 2020, for scoring FRAMA's `D` against labelled trend/range states

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can compute and, more usefully, audit FRAMA:

- **Compute** — pull 500 bars of `GET /api/v1/hyperliquid/candles`, emit the `D` and `alpha` series alongside the FRAMA line. Log `alpha` explicitly; a FRAMA plot without its smoothing constant hides the only interesting thing about it.
- **Cross-check the implied regime** — FRAMA claims a regime every bar via `D`. Compare it against `GET /api/v1/quant/market`: `D < 1.4` while the HMM reports range, or `D > 1.8` while it reports strong trend, is a disagreement worth resolving before trading either.
- **Test the volatility blind spot** — pair `D` with `GET /api/v1/volatility/regime/{symbol}`. Buckets where volatility is high but `D` is low are where FRAMA's baseline runs fastest and stretch suppression is worst; check the member's fills against that bucket specifically.
- **Measure suppression directly** — recompute the residual for the same bars against both FRAMA and a fixed [[exponential-moving-average|EMA]] of matched average period. The ratio of the two residuals during large moves *is* the suppression effect, quantified.
- **Backtest honestly** — `GET /api/v1/backtesting/klines` for the bars, `GET /api/v1/quant/regimes/history` to stratify results by regime, and resist tuning `n` per-regime; that is where [[overfitting]] enters.

## Related

- [[kama]] — sibling adaptive filter; adapts to an efficiency ratio (net move / path length) rather than path dimension
- [[vidya]] — sibling adaptive filter; adapts to volatility/momentum, the quantity FRAMA ignores
- [[adaptive-moving-averages]] — the family overview
- [[stretch-revert]] — the strategy family this page supports; `frama_stretch_revert` uses this estimator
- [[moving-averages]] · [[simple-moving-average]] · [[exponential-moving-average]] — the fixed-weight baselines FRAMA departs from
- [[hurst-exponent]] — measures long-memory persistence; related to but distinct from FRAMA's `D`
- [[mean-reversion]] · [[bollinger-bands]] · [[z-score]] — the deviation framework FRAMA feeds
- [[regime-detection]] · [[technical-structural-regime]] — independent regime classifiers to cross-check `D` against
- [[alma]] · [[hull-moving-average]] · [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] · [[jurik-moving-average]] · [[least-squares-moving-average]] · [[laguerre-filter]] · [[supersmoother-filter]] · [[theil-sen-regression]] · [[quadratic-regression]] · [[kalman-filter-trading]] — the other baseline estimators in the family
- [[overfitting]] — the parameter-tuning hazard
- [[john-ehlers]] — the author

## Sources

- Ehlers, John F. — "FRAMA – Fractal Adaptive Moving Average" (2005). The original presentation: the two-half range estimator for `D`, the `alpha = exp(-4.6·(D−1))` mapping, and the design rationale for the 4.6 constant.
- Ehlers, John F. — *Rocket Science for Traders* (2001) and *Cybernetic Analysis for Stocks and Futures* (2004). Background on the digital-filter approach to price smoothing that FRAMA sits within.

No independent validation study of FRAMA has been reviewed in this vault. Comparative claims about lag and regime behaviour on this page follow from the arithmetic of the smoothing constant, not from a measured backtest.

---
title: "Fractal Dimension"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, statistics, crypto, market-regime, regime-detection]
aliases: ["Fractal Dimension", "Fractal Dimension Index", "FDI", "Box-Counting Dimension", "Path Roughness"]
related: ["[[frama]]", "[[stretch-revert]]", "[[hurst-exponent]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[regime-detection]]", "[[technical-structural-regime]]", "[[volatility-regime-classification]]", "[[z-score]]", "[[standard-deviation]]", "[[overfitting]]", "[[john-ehlers]]", "[[kama]]", "[[vidya]]", "[[alma]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[jurik-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[least-squares-moving-average]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[kalman-filter-trading]]", "[[random-walk]]", "[[autocorrelation]]", "[[microstructure-noise-low-timeframe]]", "[[bid-ask-spread]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis, quantitative]
prerequisites: ["[[moving-averages]]", "[[hurst-exponent]]"]
difficulty: advanced
---

# Fractal Dimension

Fractal dimension (`D`) measures **how thoroughly a path fills the space it moves through**. A perfectly straight line has `D = 1`; a path so convoluted that it effectively covers a two-dimensional area has `D = 2`. Applied to a price series, `D` is a geometric read on roughness — a clean directional move is nearly a line, while chop folds back on itself repeatedly and starts to fill its box.

In this vault, fractal dimension matters almost entirely because it is the mechanism inside [[frama|FRAMA]], the fractal adaptive moving average used as one of the fourteen baselines in [[stretch-revert]]. FRAMA measures `D` every bar and converts it directly into filter speed. Understanding `D` — and, more importantly, understanding how crude the trading estimator of it is — is the difference between reading FRAMA as a principled adaptive filter and reading it as a heuristic that happens to work sometimes.

## What the quantity means

The intuition is a measurement problem. Measure a coastline with a 100 km ruler and you get one length; measure it with a 1 km ruler and you get a much longer one, because the shorter ruler resolves inlets the long one stepped over. How fast the measured length grows as the ruler shrinks *is* the dimension. A straight road gives the same length at any ruler size (`D = 1`); a maximally crinkled path gives length growing as fast as the ruler shrinks (`D = 2`).

For a price path plotted against time:

| `D` | Path character | Market reading |
|---|---|---|
| ~1.0 | Straight line | Pure directional move, no retracement |
| ~1.2–1.4 | Gently wandering line | Clean trend with minor pullbacks |
| ~1.5 | Classic [[random-walk]] Brownian path | No structure either way |
| ~1.7–1.9 | Densely folded | Choppy range, price revisiting levels |
| ~2.0 | Space-filling | Dead chop; every bar reverses the last |

Note that `D` is **direction-agnostic**. A clean rally and a clean crash both give low `D`. That is a feature for an adaptive filter — it wants to speed up for either — and a limitation for anything that needs to know which way the market is going.

## Box counting: the textbook estimator

The rigorous construction is box counting. Overlay a grid of boxes of side `ε` on the plotted path, count the boxes `N(ε)` the path passes through, then shrink `ε` and count again. If the relationship is a power law,

```
N(ε) ∝ ε^(−D)      =>      D = − lim(ε→0) log N(ε) / log ε
```

`D` is the slope of `log N(ε)` regressed on `log(1/ε)` across many box sizes. This is the box-counting dimension (Minkowski-Bouligand dimension), which coincides with the Hausdorff dimension for well-behaved sets but is not identical to it in general.

Two immediate problems when you point this at a candle chart:

1. **The limit does not exist for real data.** `ε → 0` requires infinite resolution. A price series bottoms out at tick granularity, and below the [[bid-ask-spread|spread]] there is nothing but [[microstructure-noise-low-timeframe|microstructure noise]]. The power law breaks down long before `ε` gets small.
2. **The axes have different units.** A price path is plotted in (time, price) space, and the "dimension" you measure depends on how you scale the price axis against the time axis. Rescaling the chart changes the answer. Rigorous treatments normalise explicitly; trading indicators typically normalise by the window range, which is a choice, not a derivation.

## The two-scale range estimator FRAMA actually uses

[[frama|FRAMA]] does not do box counting. Ehlers (2005) uses a two-point shortcut: split an `n`-bar window in half, take the high-low range of each half and of the whole, normalise each by its own bar count, and compare.

```python
N1 = (max(high[first half])  - min(low[first half]))  / (n/2)
N2 = (max(high[second half]) - min(low[second half])) / (n/2)
N3 = (max(high[whole])       - min(low[whole]))       / n

D = (log(N1 + N2) - log(N3)) / log(2)
```

The logic: if the two halves each cover roughly the same range as the whole window, the path is thrashing inside a box — `N1 + N2 ≈ 2·N3`, so `D ≈ log(2)/log(2) = 2`. If instead the two halves each cover half the total range, price travelled monotonically — `N1 + N2 ≈ N3` in normalised terms, giving `D ≈ 1`. It is box counting at exactly **two** scales (`ε = n` and `ε = n/2`), with the vertical range of a candle standing in for box occupancy.

FRAMA then maps it to a smoothing constant: `alpha = exp(−4.6·(D − 1))`, so `D = 1` gives `alpha = 1` (the filter is price) and `D = 2` gives `alpha ≈ 0.01` (roughly a 200-bar EMA).

## Be rigorous about the limits

This is the section that matters most, because "fractal dimension" carries a scientific authority the trading estimator has not earned.

**It is a cheap heuristic, not a Hausdorff dimension.** The FRAMA estimator uses two scales on a 16-to-32-bar window. Genuine dimension estimation needs many scales, a clean power-law regression across them, thousands of points, and a check that the scaling region is actually linear in log-log space. None of that is present. The output is a bounded roughness score that happens to be constructed from a log-ratio; calling it a fractal dimension is a naming convention, not a measurement claim. The same caveat is stated on [[frama]] and it is worth repeating wherever `D` is quoted.

**It uses ranges, not path length.** High-minus-low over a half-window discards the order in which prices arrived. Two windows with identical highs and lows but completely different internal paths — one a clean ramp, one a violent oscillation — can produce the same `N1`, `N2`, `N3` and therefore the same `D`. The estimator is blind to exactly the structure it is supposed to be measuring, in cases where the extremes happen to land the same way.

**A single wick can move it 0.3 or more.** `max(high)` and `min(low)` are the least robust statistics available — breakdown point 0, in the sense of [[theil-sen-regression#Robustness and breakdown point]]. One bad print on a thin alt perp redefines `N1` or `N3` and swings the dimension estimate, which swings `alpha`, which moves the whole FRAMA baseline. Robustness is not something the estimator has, and there is no standard robust variant in circulation.

**`D = 2 − H` is a theorem about idealised processes, not about prices.** The textbook relation to the [[hurst-exponent]] holds for **fractional Brownian motion** — a specific mathematical object that is self-similar at every scale, has stationary Gaussian increments, and is defined on a continuum. Real price series are none of those things: they have volatility clustering, fat tails, regime shifts, a finite tick size, and gaps. The relation is a useful mnemonic for orientation (`H = 0.5` ↔ `D = 1.5`, both meaning "no structure") and it is **not** licence to convert one estimate into the other. Converting a 16-bar range heuristic into a claimed Hurst exponent, or vice versa, produces a number with no defensible interpretation.

## Fractal dimension versus the Hurst exponent

The two are often described as the same information restated. On real data they capture different things, measured differently, over different horizons.

| | Fractal dimension (`D`, FRAMA estimator) | [[hurst-exponent]] (`H`) |
|---|---|---|
| What it measures | Local geometric roughness of the plotted path | Long-range dependence / autocorrelation structure of increments |
| Estimated from | Two high-low ranges on a short window | R/S analysis or variance-of-lagged-differences across many lags |
| Typical window | 16–32 bars | 100s of bars minimum; often 250+ |
| Scales used | Two | Many — the estimate *is* a regression across scales |
| Sensitivity to outliers | Extreme (min/max based) | Moderate |
| Direction-aware | No | No |
| Statistical machinery | None — no confidence interval, no null distribution | Small-sample bias corrections, bootstrapped intervals, a known `H = 0.5` null |
| Cost | Three min/max scans per bar | Substantially more; usually not per-bar |

The practical division of labour follows directly, and it is the arrangement [[stretch-revert]] uses:

- **[[hurst-exponent]] is the regime gate.** It is estimated across many scales, has an interpretable null (`H = 0.5`, the [[random-walk]]), carries known small-sample bias corrections, and is measured over a horizon long enough to describe a *regime* rather than a moment. The family's kill criteria are written in terms of Hurst for that reason — `H > 0.55` for ten sessions stands the whole family down. That is a statement about market state.
- **`D` is an internal filter control.** It is fast, cheap, and local — a per-bar dial that tells FRAMA how hard to smooth right now. It is well suited to that job precisely because it does not need to be statistically defensible; it only needs to correlate with roughness well enough to move a smoothing constant in the right direction.

Using `D` as a regime gate would be a mistake: a 16-bar window is too short to describe a regime, a single wick can flip it, and there is no null hypothesis to test it against. Using Hurst as a per-bar filter control would also be a mistake — too slow, too laggy, and it does not change fast enough to be a smoothing dial. They are not interchangeable, and the `D = 2 − H` relation is the reason people wrongly assume they are.

## Other trading uses

Beyond FRAMA, `D`-style roughness estimators appear in a few places:

- **Fractal Dimension Index (FDI)** — a standalone chop/trend oscillator, usually built on the same two-scale range logic or on a normalised path-length ratio. Read as: above ~1.5 the market is ranging, below ~1.5 it is trending. It suffers every limitation above.
- **Adaptive filter speed generally** — the same role FRAMA gives it. [[kama|KAMA]]'s efficiency ratio (net displacement / total path length) is a closely related idea reached by a different route, and is arguably the better-behaved of the two because path length is a sum rather than an extremum and therefore far less outlier-sensitive.
- **Regime overlays** — as one feature among many in a [[regime-detection]] model, where its noise can be averaged against better-behaved inputs.

Compare [[vidya|VIDYA]], which adapts to volatility level and is blind to path shape — the exact complement of FRAMA's blindness to volatility level. Running both is a partial hedge against either estimator's blind spot.

## Parameters and tuning

| Parameter | Typical | Notes |
|---|---|---|
| Window `n` | 16 (even; range 10–40) | Below ~10 the estimate is noise; above ~40 it stops resolving anything within the trade horizon |
| Range input | high/low | Close-only variants are common, noisier, and bias `D` upward |
| Number of scales | 2 (FRAMA) | More scales would be more defensible and are essentially never implemented |
| Interpretation threshold | ~1.5 | The Brownian midpoint; used as the chop/trend divider in FDI-style readings |

**Overfitting warning.** `D` is not a free-standing signal and should not be tuned as though it were. Its window interacts with FRAMA's clamps and decay constant, and then with the [[stretch-revert]] z-score window and entry threshold on top. Sweeping `n` until the dimension series "looks right" against a specific history is curve-fitting a diagnostic — see [[overfitting]]. Treat the window as a fixed design choice, validate on a coarse grid, and require a plateau rather than a spike.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the highs and lows the `N1`/`N2`/`N3` ranges are built from; close-only data cannot support the standard estimator
- `GET /api/v1/quant/market` — HMM regime probabilities, the independent classifier to check a `D` reading against
- `GET /api/v1/volatility/regime/{symbol}` — volatility state, which `D` is structurally blind to
- `GET /api/v1/hyperliquid/l2-book?coin=X` — spread and depth; on thin books the high-low ranges driving `D` are partly spread, not price structure

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for replaying the `D` series across full cycles
- `GET /api/v1/quant/regimes/history` — hourly regime labels since 2020, for scoring `D` against labelled trend/range states

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can compute `D` and, more usefully, establish how much to trust it:

- **Emit `D` alongside the FRAMA line, never instead of it.** From one `GET /api/v1/hyperliquid/candles` pull, log the `D` series and the resulting `alpha`. A FRAMA plot without its dimension series hides the only moving part.
- **Test the wick sensitivity directly.** Recompute `D` with the single most extreme high and low in each window winsorised. If the two series diverge materially on a given coin, `D` on that market is measuring bad prints, and the FRAMA baseline built on it is doing the same.
- **Do not convert `D` into a Hurst estimate.** `H = 2 − D` is valid for fractional Brownian motion and not for a two-scale range heuristic. Compute [[hurst-exponent]] separately from returns if a regime gate is needed; report both, reconcile neither by formula.
- **Check `D` against an independent regime label.** `GET /api/v1/quant/market` disagreeing persistently with `D` (low `D` under a range label, or high `D` under a strong-trend label) means the estimator is not tracking regime on that asset, and FRAMA's adaptivity there is noise.
- **Stratify before believing.** `GET /api/v1/backtesting/klines` with `GET /api/v1/quant/regimes/history` shows whether `D` actually separates historically-labelled trend from range states, per-asset. If it does not, the adaptive machinery is decoration.

## Related

- [[frama]] — the filter this quantity exists to drive; `frama_stretch_revert` is its live consumer
- [[hurst-exponent]] — the related but distinct long-memory statistic, and the correct regime gate
- [[stretch-revert]] — the strategy family; `D` is an internal control, Hurst is the gate
- [[kama]] — the efficiency ratio, a closely related and more outlier-robust roughness proxy
- [[vidya]] — adapts to volatility level instead; the complementary blind spot
- [[random-walk]] · [[autocorrelation]] — the `D = 1.5` / `H = 0.5` null and the property it summarises
- [[regime-detection]] · [[technical-structural-regime]] · [[volatility-regime-classification]] — where roughness features belong
- [[moving-averages]] · [[adaptive-moving-averages]] — the estimator landscape
- [[alma]] · [[hull-moving-average]] · [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] · [[jurik-moving-average]] · [[laguerre-filter]] · [[supersmoother-filter]] · [[least-squares-moving-average]] · [[theil-sen-regression]] · [[quadratic-regression]] · [[kalman-filter-trading]] — sibling baselines
- [[microstructure-noise-low-timeframe]] · [[bid-ask-spread]] — why the `ε → 0` limit is meaningless on price data
- [[overfitting]] — the tuning hazard
- [[john-ehlers]] — author of the FRAMA estimator

## Sources

- Mandelbrot, B. B. (1967). How long is the coast of Britain? Statistical self-similarity and fractional dimension. *Science* 156(3775). The coastline argument and the origin of fractal dimension as a measurement-scale concept.
- Mandelbrot, B. B. (1982). *The Fractal Geometry of Nature*. The general framework, including the relation between fractal dimension and the self-similarity parameter of fractional Brownian motion.
- Ehlers, John F. (2005). "FRAMA – Fractal Adaptive Moving Average." Source of the two-scale high-low range estimator and the `alpha = exp(−4.6·(D − 1))` mapping documented here.
- The `D = 2 − H` relation for fractional Brownian motion is standard in the fractal-geometry literature; its inapplicability to short-window financial estimators is an observation made on this page and on [[frama]], not a cited result.

No vault source-summary page covers fractal dimension. No independent validation of the two-scale estimator's accuracy on financial data has been reviewed here; the limitations described above follow from the construction of the estimator rather than from a measured study.

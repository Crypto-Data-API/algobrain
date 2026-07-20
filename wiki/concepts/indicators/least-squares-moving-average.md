---
title: "Least Squares Moving Average (LSMA)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, statistics, crypto]
aliases: ["LSMA", "Linear Regression Curve", "Least Squares Moving Average", "End-Point Moving Average", "Linear Regression Line", "LRC"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[z-score]]", "[[standard-deviation]]", "[[hurst-exponent]]", "[[overfitting]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[stationarity]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[alma]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[jurik-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[kalman-filter-trading]]", "[[linear-regression]]", "[[keltner-channels]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis, quantitative]
prerequisites: ["[[moving-averages]]", "[[standard-deviation]]"]
difficulty: intermediate
---

# Least Squares Moving Average (LSMA)

The Least Squares Moving Average fits an ordinary least-squares straight line to the last *n* bars of price and plots the fitted value **at the most recent bar** — the endpoint of the line, not its midpoint. Unlike every weighted-average smoother, it does not average the window; it *models* the window, which means the distance between price and the LSMA is a genuine regression residual with statistical machinery attached to it. It is also known as the Linear Regression Curve, the Least Squares MA, or the End-Point Moving Average.

Together with [[theil-sen-regression]] and [[quadratic-regression]], the LSMA forms the **regression group** of baseline estimators in [[stretch-revert]]. All three share the same defining property — fit a model, read off its endpoint value, treat the leftover as signal.

## Construction

```python
def lsma(close, period=25):
    """Least Squares Moving Average — OLS line fitted to the window,
    evaluated at the most recent bar (x = n-1).

    period : window length in bars. Common defaults: 20-25 (classic),
             14-32 in crypto intraday work. `stretch_revert` uses the
             family-wide `cfg.period`.
    """
    out = [None] * len(close)
    n = period
    x = list(range(n))                      # 0, 1, ..., n-1
    x_bar = (n - 1) / 2                     # mean of 0..n-1
    sxx = sum((xi - x_bar) ** 2 for xi in x)  # constant: n(n^2-1)/12

    for t in range(n - 1, len(close)):
        y = close[t - n + 1 : t + 1]
        y_bar = sum(y) / n
        sxy = sum((x[i] - x_bar) * (y[i] - y_bar) for i in range(n))
        b = sxy / sxx                       # slope
        a = y_bar - b * x_bar               # intercept
        out[t] = a + b * (n - 1)            # ENDPOINT, not midpoint
    return out
```

The two quantities that matter:

- **Slope** `b = Σ((x−x̄)(y−ȳ)) / Σ((x−x̄)²)` — the fitted trend rate, in price units per bar.
- **Intercept** `a = ȳ − b·x̄`, and the plotted value `LSMA = a + b·(n−1)`.

Because `x` is a fixed integer sequence, `Σ(x−x̄)² = n(n²−1)/12` is a constant — the whole fit reduces to a fixed-weight linear combination of the closes, so an LSMA is computationally as cheap as an SMA despite being a regression. The equivalent weight vector is linearly increasing and, notably, **negative on the oldest bars** of the window; that negative lobe is where the lag reduction comes from.

**Residual:** `resid_t = close_t − LSMA_t`. This is the object the rest of the page is about.

## Fitting versus averaging

An [[simple-moving-average|SMA]] or [[exponential-moving-average|EMA]] answers "what has price been, on average, recently?" A regression answers "what linear process best explains this window, and where does it say we should be right now?" The difference is not cosmetic — it changes what the deviation *means*.

When price sits 2% above a 25-period SMA, that gap is a mixture of two things you cannot separate: genuine displacement, and the simple fact that the SMA is dragged backwards by a trend. In a steadily rising market, price is *always* above the SMA. The gap is structurally biased and there is no principled scale on which to measure it — you end up choosing a band width by eye.

A regression removes the trend component by construction: the fitted line already absorbs the drift, so the residual `y − ŷ` is what the linear model **could not** explain. That gives you the standard toolkit:

- **Residual standard error** — `s = sqrt(Σ(y_i − ŷ_i)² / (n − 2))`, the natural scale for "how far is far". Divide the residual by `s` and you have a [[z-score]] whose denominator is derived, not chosen. This is a materially stronger footing than an ad-hoc band multiple.
- **Prediction interval at the endpoint** — the endpoint is the highest-leverage point in the window, so its interval is wider than the in-sample average by the factor `sqrt(1 + 1/n + (x−x̄)²/Σ(x−x̄)²)`. At `x = n−1` that leverage term is at its maximum. The honest reading: the LSMA endpoint is the *least* certain point on the fitted line, and any band drawn from `s` alone slightly understates uncertainty there.
- **R²** — how much of the window's variance the linear trend explains. Low R² means the window has no coherent trend and the "residual" is mostly noise; high R² with a large residual is a much more interesting configuration. R² is a free regime filter that averaging smoothers cannot produce.
- **Slope t-statistic** — `b / SE(b)` tests whether the fitted trend is distinguishable from zero, which is a cleaner trend gate than eyeballing whether the line looks like it is going up.

Building channels from `s` around the LSMA gives the **linear regression channel**, the regression-native cousin of [[bollinger-bands]]. Bollinger bands measure dispersion around a flat mean; a regression channel measures dispersion around a *sloped* mean. In a trending market these are very different objects, and the regression version is the one that does not manufacture false stretch simply because price is trending.

## Lag and smoothing trade-off

An SMA of period *n* plots at the window's centre of mass, which sits `(n−1)/2` bars in the past — a 25-period SMA lags by roughly 12 bars. The LSMA plots the fitted line *projected forward* to the current bar, which removes that centroid lag entirely for any price path that is genuinely linear over the window. For a constant-slope ramp, the LSMA sits exactly on price while the SMA trails by `b·(n−1)/2`.

Concretely, ranked by lag on the same window:

| Estimator | Lag character | Noise character |
|---|---|---|
| [[simple-moving-average\|SMA]](n) | ~(n−1)/2 bars | smoothest, most damped |
| [[exponential-moving-average\|EMA]](n) | ~(n−1)/2 bars, decaying kernel | smooth, single-pole |
| [[hull-moving-average\|HMA]](n) | very low | overshoots turns |
| **LSMA(n)** | ~0 for linear paths | **noisier than SMA — amplifies at turns** |
| [[zero-lag-exponential-moving-average\|ZLEMA]](n) | very low | noisy, hugs price |

The cost is unavoidable and worth stating plainly: **the LSMA is not a low-pass filter, it is an extrapolator.** Its negative weights on old bars mean it can amplify noise rather than suppress it, and at a sharp turn it overshoots — the line is still projecting the pre-turn slope forward while price has already reversed. The LSMA is *smoother than price* but *less smooth than an SMA of the same window*. It buys lag reduction with variance, which is the same trade every fast estimator makes; it just makes it in a statistically legible way.

## Use as a mean-reversion baseline

This is the reason the page exists. In [[stretch-revert]], `lsma_stretch_revert` (prod tier) uses the LSMA as its baseline, and the family's "stretch" becomes exactly the regression residual:

```
stretch_t = (close_t − LSMA_t) / s_t        # s = residual standard error
```

Three consequences follow, and they are what separates the regression group from the eleven averaging-based members:

1. **The scale is principled, not chosen.** Every other member computes σ as a rolling standard deviation of `close − baseline` — a serviceable quantity, but one with no model behind it. The LSMA gives you `s`, the residual standard error of an actual fit, with `n−2` degrees of freedom. A 2.5σ stretch on an LSMA baseline is a statement about a fitted model's error distribution. A 2.5σ stretch on an ALMA baseline is a statement about how far price has moved from a weighted average. The first can be falsified; the second is a convention.

2. **Trend drift is already netted out.** The dominant failure of the whole family is "walking the bands" — price rides an extreme through a trend and oversold gets more oversold. A big part of *why* a trend generates persistent apparent stretch on SMA/EMA baselines is centroid lag: the baseline is mechanically behind, so the residual is mechanically positive. The LSMA absorbs the linear component of the trend into the fit, so a steady, straight-line trend produces **near-zero** stretch. That is a real structural improvement over averaging baselines, and it means the LSMA member should fire less often but on better-conditioned setups.

3. **R² is available as a free gate.** Fade only when the window's linear fit is *poor* (low R², i.e. chop with no coherent direction) and stand down when it is strong (high R² plus a significant slope t-stat, i.e. a clean trend). This is a regime filter derived from the same fit that produces the signal, and it complements the family's mandatory [[hurst-exponent]] gate rather than duplicating it.

**Which regimes flatter it.** Range-bound chop with drift — a market oscillating around a gently sloping path. The SMA baseline reads that drift as permanent stretch; the LSMA reads it as trend and only flags the oscillation. Also: markets where the dominant move is a clean impulse followed by consolidation, since the fit adapts its slope immediately rather than waiting for old bars to roll off.

**Which regimes expose it.**

- **Accelerating trends.** A straight line cannot track curvature. In a parabolic advance the linear fit persistently underestimates price, generating large positive residuals that look like extreme stretch and are actually model misspecification. Fading them is fading the acceleration itself. This is precisely the gap [[quadratic-regression]] exists to close.
- **Sharp reversals.** The LSMA overshoots at turns, so at exactly the moment a dislocation resolves, the baseline is still pointing the wrong way and the residual is inflated in the wrong direction.
- **Single bad prints.** OLS has a breakdown point of **zero**. One wick, one bad exchange print, one 30-second glitch on a thin alt book, and the fitted line — and therefore the residual and therefore the z-score — moves without bound. This is a live, recurring problem in crypto, and it is the entire motivation for [[theil-sen-regression]] as a sibling estimator. If you run an LSMA baseline on Hyperliquid alt perps, winsorise the window or you are trading exchange artifacts.
- **Non-[[stationarity|stationary]] residuals.** The z-score assumes the residual distribution is stable enough that today's `s` describes tomorrow's dispersion. In a volatility regime shift it does not, and the threshold silently changes meaning.

## Parameters and tuning

| Parameter | Typical | Effect |
|---|---|---|
| `period` (n) | 14–32 bars; 20–25 classic | Longer = smoother fit, wider prediction interval, less frequent but larger stretch readings |
| Entry z | 2.0–3.0 | Threshold on `resid / s` |
| Exit z | 0.0–0.5 | Reversion to the fitted line |
| Price input | close | HL2/HLC3 reduce single-print sensitivity marginally; they do not fix the breakdown-point problem |
| R² gate | fade below ~0.3–0.5 | Optional regime filter from the same fit |

The LSMA has exactly **one** structural parameter, which is genuinely unusual and genuinely valuable. Compare [[jurik-moving-average|JMA]] (period, phase, power) or [[frama|FRAMA]] (period plus fractal-dimension bounds). Fewer knobs is fewer degrees of freedom is less [[overfitting]] surface.

**Overfitting warning.** That advantage evaporates the moment you sweep `period` over a grid and keep the best. Fourteen estimators, each with a tuned window, an entry z, an exit z, and a stop multiple is a very large search space, and the best cell of that grid will look excellent on any history. The specific traps here:

- **Period sweeps.** LSMA performance is not smooth in `n` — the negative-weight structure means adjacent windows can behave quite differently. That roughness makes a grid search *more* likely to find a lucky cell, not less. Prefer a period justified by the trading horizon (a 15m member fading intraday dislocations wants a window covering hours, not days) over one selected by backtest score.
- **In-sample residual scale.** If you fit `s` on the same data you evaluate on, the z-scores are optimistically tight. Compute `s` on a rolling basis, out-of-sample.
- **Multiple comparisons across the family.** [[stretch-revert]] runs fourteen baselines. If LSMA is the winner, that result must be deflated for the thirteen others before it means anything — see the family page's treatment of this.
- **R² threshold.** Adding an R² gate adds a parameter. It is a well-motivated one, but it is still a knob, and "well-motivated" is not the same as "free".

Sanity check: an LSMA member's edge should degrade *gracefully* as `n` moves. A performance cliff between n=20 and n=22 is not a discovery.

## Advantages

- **Materially less lag than an SMA of the same window** — near zero on linear price paths, versus ~(n−1)/2 bars of centroid lag.
- **The deviation is a real residual**, with residual standard error, prediction intervals, R², and a slope t-statistic available for free. No other member of the [[stretch-revert]] family except its two regression siblings can say this.
- **Trend drift is netted out**, so a steady trend does not manufacture spurious stretch the way it does on averaging baselines.
- **One structural parameter** — small [[overfitting]] surface relative to adaptive smoothers.
- **Cheap** — O(n) per bar with constant weights, effectively free; scales fine across a wide perp universe.
- **Slope is directly interpretable** as price-units-per-bar, usable as a trend gate in its own right.
- **Natural channel construction** — the linear regression channel is a sloped-mean analogue of [[bollinger-bands]] that does not penalise trending markets.

## Limitations

- **Zero breakdown point.** A single outlier moves the fit arbitrarily far. In crypto — wicks, bad prints, thin books — this is not hypothetical. [[theil-sen-regression]] exists because of it.
- **Cannot track curvature.** Accelerating or decelerating moves are systematically mis-fit, producing residuals that reflect model error rather than dislocation. [[quadratic-regression]] addresses this, at its own cost.
- **Endpoint is the highest-leverage point** of the fit — the place where the model is least certain is exactly where the indicator reads its value. Bands built from `s` alone understate uncertainty there.
- **Noisier than an SMA** of the same window; negative weights on old bars can amplify rather than suppress noise.
- **Overshoots at turns**, projecting a stale slope through the reversal.
- **Assumes a stable residual distribution.** Volatility regime shifts break the z-score's calibration without any visible warning ([[stationarity]]).
- **The statistical machinery is only as good as its assumptions.** OLS inference assumes independent, homoskedastic, roughly normal errors. Financial returns are none of these. Treat `s` as a well-motivated *scale*, not as a licence to quote p-values — the R² and t-statistics are useful ordinal signals, not valid hypothesis tests on this data.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the OHLCV closes the regression window is fitted to; `limit` should exceed `period` by a wide margin so the residual standard error has a stable rolling sample
- `GET /api/v1/hyperliquid/l2-book?coin=X` — spread and depth check; a residual smaller than a couple of spreads is not a dislocation
- `GET /api/v1/derivatives/funding-rates?coin=X` — carry cost on any reversion held beyond a bar or two
- `GET /api/v1/derivatives/open-interest?coin=X` — OI expanding into a large residual argues trend, not stretch

**Historical data:**
- `GET /api/v1/backtesting/klines` — kline archive for fitting the LSMA over long histories and studying residual stability
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels, for scoring LSMA residuals only inside range-labelled states
- `GET /api/v1/volatility/regime/{symbol}` — volatility regime, the main thing that breaks residual-scale calibration

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [funding rates](https://cryptodataapi.com/funding-rates) · [order-book depth](https://cryptodataapi.com/quant-order-books) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with the LSMA directly:

- **Compute and report the full fit, not just the line.** Pull `GET /api/v1/hyperliquid/candles`, fit OLS over the last `period` closes, and emit slope, intercept, endpoint value, residual, residual standard error, and R² together. The endpoint alone throws away most of what makes this estimator worth using.
- **Scale the stretch off `s`, not off a rolling price σ.** Report `(close − LSMA) / s`. Cross-check it against the rolling-σ z-score the averaging members use — a large disagreement between the two is itself informative, and usually means the window has strong trend the averaging baselines are misreading as stretch.
- **Winsorise before fitting.** OLS has zero breakdown point, so clip or median-filter the window before the fit on any coin outside the majors. Compare the fit with and without clipping; if they differ materially the raw signal was an exchange artifact, and [[theil-sen-regression]] is the right estimator for that coin.
- **Gate on R² and slope significance.** Low R² plus a large residual is the configuration to fade; high R² with a significant slope t-statistic is a trend the family should stand down on. Combine with `GET /api/v1/quant/market` rather than replacing it.
- **Validate the residual scale out-of-sample.** Replay via `GET /api/v1/backtesting/klines`, computing `s` on a strictly trailing window, and check that the realised frequency of |z| > 2.5 events matches the assumed distribution. It generally will not — crypto residuals are fat-tailed — and knowing the true exceedance rate is worth more than the nominal threshold.
- **Stratify by volatility regime.** Score LSMA residuals separately inside each `GET /api/v1/volatility/regime/{symbol}` state; a single global z-threshold is quietly a different signal in each regime.

## Related

- [[stretch-revert]] — the strategy family this baseline serves; `lsma_stretch_revert` is the prod-tier member
- [[theil-sen-regression]] — robust sibling; same fit-a-line idea, median-of-slopes instead of least squares
- [[quadratic-regression]] — curved sibling; same endpoint-read idea, second-order fit
- [[moving-averages]] · [[adaptive-moving-averages]] — the wider estimator landscape
- [[simple-moving-average]] · [[exponential-moving-average]] — the averaging baselines the LSMA is contrasted against
- [[alma]] · [[frama]] · [[vidya]] · [[kama]] · [[hull-moving-average]] · [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] · [[jurik-moving-average]] · [[laguerre-filter]] · [[supersmoother-filter]] · [[kalman-filter-trading]] — sibling estimators in the same family
- [[bollinger-bands]] — dispersion around a flat mean; the regression channel is its sloped-mean analogue
- [[keltner-channels]] — ATR-based envelope alternative
- [[z-score]] · [[standard-deviation]] — the scale the residual is measured on
- [[mean-reversion]] — the trade the residual is used for
- [[hurst-exponent]] — the regime gate that must pass before any fade
- [[stationarity]] — the assumption underneath the residual z-score
- [[overfitting]] — why a swept `period` is not a discovery
- [[linear-regression]] — the underlying method

## Sources

- Ordinary least squares regression is standard statistical method; no single attribution applies. Any regression text covers the endpoint-leverage and prediction-interval results used above.
- The "linear regression curve" / "end-point moving average" framing entered technical analysis through the trading-software literature of the late 1980s and 1990s; it is a display convention on a standard OLS fit rather than a novel estimator.
- Family context, live status, and the multiple-comparisons caveat: [[stretch-revert]].
- No vault source-summary page covers the LSMA specifically. This page is derived from the method itself plus existing vault pages ([[moving-averages]], [[bollinger-bands]], [[overfitting]]); its performance claims are analytic, not measured.

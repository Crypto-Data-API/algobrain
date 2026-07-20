---
title: "Quadratic Regression (Polynomial Baseline)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, statistics, crypto]
aliases: ["Quadratic Regression", "QuadReg", "Polynomial Regression Baseline", "Second-Order Regression", "Parabolic Regression Curve", "Polynomial Moving Average"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[z-score]]", "[[standard-deviation]]", "[[hurst-exponent]]", "[[overfitting]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[stationarity]]", "[[least-squares-moving-average]]", "[[theil-sen-regression]]", "[[alma]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[jurik-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[kalman-filter-trading]]", "[[linear-regression]]", "[[bias-variance-tradeoff]]", "[[curve-fitting]]", "[[momentum]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis, quantitative]
prerequisites: ["[[moving-averages]]", "[[standard-deviation]]"]
difficulty: intermediate
---

# Quadratic Regression (Polynomial Baseline)

Quadratic regression fits a second-order polynomial `y = a + b·x + c·x²` to the last *n* bars by least squares and reads the fitted value at the most recent bar. Because the fit can **curve**, the baseline tracks accelerating and decelerating moves that a straight line structurally cannot — so a strong but smoothly-accelerating trend produces far less spurious "stretch" than it would against an [[least-squares-moving-average|LSMA]]. The price of that extra flexibility is the classic bias-variance trade, plus a specific and serious problem: polynomial fits are notoriously unstable at the endpoints of their window, which is exactly where this indicator reads its value.

Quadratic regression, [[least-squares-moving-average|LSMA]], and [[theil-sen-regression]] form the **regression group** of baselines in [[stretch-revert]] — the three that fit a model to the window rather than averaging it, and therefore the three whose "stretch" is a genuine regression residual with standard statistical machinery behind it.

## Construction

```python
import numpy as np

def quadreg(close, period=25, degree=2):
    """Quadratic (2nd-order polynomial) regression baseline, endpoint-evaluated.

    period : window length in bars. Typical 20-40; needs to be LONGER than
             a comparable LSMA window, because a 3-parameter fit on a short
             window is mostly fitting noise.
    degree : 2. Do not raise this. See 'Limitations' (Runge's phenomenon).
    """
    out = [None] * len(close)
    n = period
    x = np.arange(n, dtype=float)          # 0, 1, ..., n-1

    for t in range(n - 1, len(close)):
        y = np.asarray(close[t - n + 1 : t + 1], dtype=float)
        # least-squares fit of y = a + b*x + c*x^2
        c2, c1, c0 = np.polyfit(x, y, 2)   # returns highest order first
        out[t] = c0 + c1 * (n - 1) + c2 * (n - 1) ** 2   # ENDPOINT
    return out
```

Solved directly, the coefficients come from the normal equations `(XᵀX)β = Xᵀy` with design matrix `X = [1, x, x²]`. Because `x` is a fixed integer sequence, `XᵀX` is a constant 3×3 matrix for a given `n` and can be inverted once — the per-bar cost is then O(n), no worse than an LSMA. **Numerical note:** naively forming `x²` for large `n` makes `XᵀX` badly conditioned. Centre `x` on the window (use `x − x̄`, i.e. `−(n−1)/2 … (n−1)/2`) or fit in an orthogonal polynomial basis; otherwise a 60-bar window can produce visibly wrong coefficients in single precision.

Quantities of interest:

- **`c`** — the curvature coefficient. `c > 0` is an accelerating/convex path, `c < 0` a decelerating/concave one. This is a second-derivative estimate, directly interpretable as a [[momentum|momentum]] change rate, and it has no analogue in any averaging smoother.
- **Baseline** — `a + b·(n−1) + c·(n−1)²` (or the centred equivalent), the fit read at the current bar.
- **Residual** — `resid_t = close_t − QuadReg_t`, the stretch.
- **Residual standard error** — `s = sqrt(Σ(y − ŷ)² / (n − 3))`. Note the denominator: three fitted parameters, so `n − 3` degrees of freedom, not `n − 2`.

Defaults in the `stretch_revert` context: `period` 20–40, entry z 2.0–3.0, exit z near 0. The member `quadreg_stretch_revert` is currently **sim tier** with zero completed trades.

## Fitting versus averaging

The regression group's defining property is that a model produces a **residual**, and a residual is a far better-defined object than "distance from a moving average".

Distance from an [[simple-moving-average|SMA]] or [[exponential-moving-average|EMA]] is a mixture you cannot decompose: some genuine displacement, plus the mechanical lag of the smoother, plus — for a curved price path — the smoother's inability to represent the shape at all. There is no model, so there is no defined scale for the deviation and no way to ask whether it is large. You choose a band multiple by convention.

A regression explicitly splits the window into explained and unexplained parts, and the unexplained part comes with machinery:

- **Residual standard error** `s` (with `n−3` d.o.f.) — the natural scale for the stretch. `z = resid / s` has a denominator derived from the fit, not chosen by hand. This is what makes the regression group's [[z-score]] principled rather than ad hoc.
- **Prediction interval at the endpoint** — width scales with `sqrt(1 + hᵢᵢ)` where `hᵢᵢ` is the leverage of that point. For a quadratic fit, endpoint leverage is **substantially higher** than for a linear fit on the same window: the quadratic term's influence grows as the square of distance from the window centre, so the extreme bars dominate the curvature estimate. The endpoint is where the model is least certain, and it is where the indicator reads. Quantifying this is a benefit of the regression framing — the interval tells you honestly how unreliable the reading is — but it is also the warning label.
- **R² and adjusted R²** — how much of the window's variance the curve explains. **Use adjusted R²** when comparing against a linear fit; raw R² always improves when you add a parameter, so a naive comparison always prefers the quadratic and tells you nothing.
- **The F-test on the quadratic term** — is `c` significantly different from zero? This is the principled way to ask "does this window actually have curvature, or am I fitting noise?" It is a genuine model-selection tool that no averaging smoother can offer, and it is the single most useful diagnostic on this page. Treat it as an ordinal signal rather than a valid p-value — financial residuals violate the test's assumptions — but a `c` that is small relative to its standard error means the quadratic is doing nothing and the [[least-squares-moving-average|LSMA]] is the better estimator for that window.

Building bands from `s` around the quadratic fit gives a **curved regression channel** — the polynomial analogue of [[bollinger-bands]] and of the LSMA's straight linear regression channel. Its centreline bends with the move, so a parabolic advance does not automatically pin price to the upper band.

## Lag and smoothing trade-off

The quadratic baseline sits at a distinct point in the estimator space, and the cleanest way to see it is by what each smoother can represent exactly:

| Baseline | Represents exactly | Lag on that shape | Behaviour on curvature |
|---|---|---|---|
| [[simple-moving-average\|SMA]](n) | a constant | ~(n−1)/2 bars even on a constant slope | large systematic error |
| [[exponential-moving-average\|EMA]](n) | a constant | ~(n−1)/2 bars | large systematic error |
| [[least-squares-moving-average\|LSMA]](n) | a straight line | ~0 on a linear ramp | **systematic error grows with c** |
| **QuadReg(n)** | a parabola | **~0 on a curved path** | tracks it |
| [[hull-moving-average\|HMA]] / [[zero-lag-exponential-moving-average\|ZLEMA]] | — (heuristic lag cancels) | very low | approximately tracks, noisily |

The LSMA removed the SMA's centroid lag by modelling slope. Quadratic regression removes the LSMA's *curvature* lag by modelling acceleration. Each step up in order buys the ability to track a richer class of paths with near-zero lag.

Each step also costs variance. This is the [[bias-variance-tradeoff]] stated in its most literal form: three parameters fit more real structure than two, and they also fit more noise than two. On a given window, the quadratic baseline will be **noisier** than the LSMA and considerably noisier than the SMA. The practical compensation is to run a longer window — a 3-parameter fit on 15 bars is largely noise-fitting, whereas on 40 bars it has something to work with. So the honest comparison is not "QuadReg(25) versus LSMA(25)" but "QuadReg(35) versus LSMA(25)", where both have comparable effective smoothness and the quadratic retains a real advantage only on genuinely curved paths.

And the endpoint problem, which deserves its own statement: **a polynomial's fitted value is least reliable at the edges of its fitting range, and this indicator reads exactly there.** Interior points are constrained by data on both sides; the endpoint is constrained on one side only, so the curvature term extrapolates freely. When `c` is estimated with any noise at all, that noise is multiplied by `(n−1)²` at the endpoint. A small error in curvature becomes a large error in the plotted baseline. This is not a minor caveat — it is the central structural weakness of the estimator.

## Use as a mean-reversion baseline

`quadreg_stretch_revert` is a **sim-tier** member of [[stretch-revert]] with **zero completed trades**. Everything below is design reasoning, not evidence.

**The design intent — and it is a good one.** The family's dominant failure is walking the bands: price rides an extreme through a trend, and "oversold" gets more oversold. A significant contributor to that failure on straight-line baselines is *model misspecification*, not just lag. In an accelerating move, an LSMA fits the average slope of the window; price, moving faster than that average, sits persistently above the line. The residual grows every bar and eventually crosses the entry threshold — but it is measuring the fit's inability to represent curvature, not a dislocation. The strategy then fades an acceleration, which is close to the worst available trade.

A quadratic baseline absorbs the acceleration into the model. On a smoothly parabolic advance, `c` picks up the curvature, the fitted line bends with price, and the residual stays near zero. **No signal fires.** That is the correct behaviour, and it is a real structural improvement over the LSMA in exactly the regime that hurts the family most.

**The stretch is still a residual.** `z = (close − QuadReg) / s` with `s` the residual standard error on `n−3` degrees of freedom. Same principled footing as the other two regression-group members, and the same advantage over the eleven averaging baselines, whose σ is a rolling standard deviation with no model behind it.

**Which regimes flatter it.**

- **Smooth accelerating or decelerating trends.** The headline case. Where the LSMA manufactures false stretch, the quadratic reports approximately none.
- **Rounded tops and bottoms.** A market decelerating into a turn has genuine curvature; `c` flips sign through the turn, giving an interpretable read that no averaging smoother produces.
- **Post-impulse consolidation** with a curved settling path, common after a liquidation flush.
- **Windows with real, statistically significant curvature.** Trivially, but the point is that the F-test tells you when you are in one, so the estimator can be used selectively rather than always.

**Which regimes expose it.**

- **Choppy ranges — and this is severe.** With no genuine curvature, `c` is fitting noise. Because the endpoint amplifies `c` by `(n−1)²`, a noise-driven curvature estimate throws the baseline around, and the residual becomes erratic. The estimator is *worst* in exactly the range-bound regime where the family's edge is supposed to live. This is the deepest tension in the design and it should be resolved with an explicit curvature-significance gate, not ignored.
- **Sharp reversals and V-shaped turns.** A parabola through a V fits neither leg. The endpoint value can swing wildly bar to bar as the fit reorients, generating large spurious residuals at precisely the moment a real dislocation is resolving.
- **Single outliers.** OLS breakdown point is 0%, same as the LSMA — and *worse* in effect, because a leverage point near the window edge has outsized influence on the curvature coefficient. One wick at bar 1 or bar n can bend the whole parabola. See [[theil-sen-regression]] for the robust alternative; note there is no widely-used robust quadratic in this vault's estimator set, which is a real gap.
- **Regime transitions.** The fit will happily extrapolate a curve straight through a structural break.
- **Non-[[stationarity|stationary]] residual dispersion.** The z-threshold silently changes meaning across volatility regimes, as with every member.

The design conclusion: quadratic regression is a **specialist**. It should be preferred over the LSMA when the F-test says the window has real curvature, and it should defer to the LSMA when it does not. Running it unconditionally as a fourteenth always-on member is likely to concede more in chop than it gains in accelerating trends.

## Parameters and tuning

| Parameter | Typical | Effect |
|---|---|---|
| `degree` | **2** | The one parameter you should not tune. See below |
| `period` (n) | 20–40 bars | Longer than a comparable LSMA window; a 3-parameter fit needs data. Too long and the parabola misses recent structure entirely |
| Entry z | 2.0–3.0 | On `resid / s`, `s` computed with n−3 d.o.f. |
| Exit z | 0.0–0.5 | Reversion to the fitted curve |
| Curvature gate | F-test on `c`, or \|c\|/SE(c) | **Strongly recommended.** Fall back to the LSMA when curvature is insignificant |
| Basis | centred or orthogonal | Numerical conditioning, not a tuning knob — always centre |

**Overfitting warning — this page's most important section.** Quadratic regression is where the [[stretch-revert]] family's overfitting exposure is most concentrated, for three compounding reasons.

*First, at the estimator level.* Adding a parameter to a fit **always** improves in-sample fit. Raw R² will always favour the quadratic over the linear. If you select between the LSMA and QuadReg by in-sample fit quality, you will always choose QuadReg, and you will be choosing a noise-fitter. Use adjusted R² or the F-test on `c`. This is the textbook [[curve-fitting]] trap operating inside a single indicator.

*Second, the degree parameter.* Raising `degree` is the most seductive and most destructive knob available. A cubic tracks price better than a quadratic; a quintic better still; a degree-(n−1) polynomial passes exactly through every point and predicts nothing. And the failure is not gradual — it is **Runge's phenomenon**: high-order polynomial fits develop violent oscillations near the interval edges, with amplitude growing rapidly in the degree. Since this indicator reads at the edge, higher orders degrade its output faster than they degrade the fit as a whole. A degree-5 endpoint read is not a slightly-better degree-2 read; it can be qualitatively unusable. **Keep degree at 2.** If a quadratic is not enough, the right answer is a different model class ([[kalman-filter-trading|state-space]], adaptive smoothers), not a higher polynomial.

*Third, at the family level.* [[stretch-revert]] runs fourteen baselines. Testing fourteen estimators and reporting the best is a textbook multiple-comparisons problem, and the family page is explicit that the winner's record must be deflated for the other thirteen before it means anything. A quadratic member with a tuned `period`, a tuned degree, a tuned curvature gate, and tuned z-thresholds contributes disproportionately many degrees of freedom to that search. It is the member most likely to produce a spuriously good backtest.

Practical safeguards: fix `degree = 2` before any search; justify `period` by trading horizon rather than by backtest score; require the edge to degrade *gracefully* in `period` (a cliff between n=30 and n=32 is noise, not a finding); and compare against the LSMA on the same bars — if the quadratic's advantage is not concentrated in windows the F-test flags as genuinely curved, the extra parameter is not earning its keep.

## Advantages

- **Tracks curvature.** The only baseline in the [[stretch-revert]] family that can represent acceleration exactly, so smoothly-accelerating trends generate far less spurious stretch than against a straight-line fit.
- **Directly attacks the family's worst failure mode.** Walking the bands during an accelerating trend is partly model misspecification on linear/averaging baselines; the quadratic removes that component.
- **The deviation is a genuine regression residual**, with residual standard error, prediction intervals, adjusted R², and an F-test on the curvature term — shared only with [[least-squares-moving-average|LSMA]] and [[theil-sen-regression]].
- **`c` is an interpretable second-derivative estimate** — a direct read on whether a move is accelerating or decelerating, with no counterpart in any averaging smoother.
- **A real model-selection test is available.** The F-test on `c` says when the quadratic is warranted and when it should defer to the LSMA. Few indicators come with a built-in "am I appropriate here?" diagnostic.
- **Near-zero lag on curved paths**, where the LSMA carries systematic error and the SMA carries both lag and shape error.
- **Cheap** — O(n) per bar with a precomputed constant normal-equations inverse.
- **Curved regression channel** — a bands construction whose centreline bends with the move.

## Limitations

- **Endpoint extrapolation instability is the central weakness.** A polynomial is least reliable at the edge of its fitting range, and this indicator reads at the edge. Noise in `c` is amplified by `(n−1)²` at the endpoint. Everything else on this list is downstream of this.
- **Noise-fitting in ranges.** With no genuine curvature, `c` fits noise, and the amplified endpoint makes the baseline erratic — worst behaviour in exactly the range regime the family depends on.
- **Bias-variance cost is real and unavoidable.** Three parameters fit more structure *and* more noise than two ([[bias-variance-tradeoff]]).
- **Zero breakdown point, with extra leverage sensitivity.** OLS, so one outlier moves the fit without limit; a leverage point near the window edge distorts curvature disproportionately. Worse in this respect than the LSMA. No robust quadratic is deployed in this vault.
- **Higher degrees get rapidly worse** via Runge's phenomenon, and the degradation is concentrated at the endpoints. Degree 2 is a ceiling, not a starting point.
- **Numerical conditioning.** An uncentred `[1, x, x²]` design matrix is badly conditioned for moderate `n`; a silent precision failure is possible.
- **Largest overfitting surface in the regression group** — degree, period, curvature gate, z-thresholds — and it sits inside a fourteen-way family search.
- **Fails through V-shaped turns**, where a parabola fits neither leg and the endpoint swings.
- **Non-stationary residual dispersion** breaks z-score calibration ([[stationarity]]).
- **No evidence whatsoever in this vault.** `quadreg_stretch_revert` is sim tier with zero trades. No backtest, no walk-forward, no cost-corrected record. The entire case for it is analytic.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the closes the polynomial is fitted to; pull well beyond `period` so `s` has a stable rolling sample and so curvature can be compared across windows
- `GET /api/v1/hyperliquid/l2-book?coin=X` — spread and depth check; an endpoint-instability artifact plus a wide spread is the worst combination this member can trade
- `GET /api/v1/derivatives/funding-rates?coin=X` — carry drag on held reversions
- `GET /api/v1/derivatives/open-interest?coin=X` — OI expanding alongside positive curvature is an accelerating trend, the configuration this member is specifically built *not* to fade

**Historical data:**
- `GET /api/v1/backtesting/klines` — kline archive for fitting the quadratic over long histories and, critically, for measuring how often windows contain statistically significant curvature at all
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels, for scoring residuals only inside range-labelled states
- `GET /api/v1/volatility/regime/{symbol}` — volatility regime; endpoint instability scales with volatility, so calibration is regime-specific

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [funding rates](https://cryptodataapi.com/funding-rates) · [order-book depth](https://cryptodataapi.com/quant-order-books) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with the quadratic baseline directly:

- **Test the curvature before trusting the curve.** On every `GET /api/v1/hyperliquid/candles` pull, fit the quadratic and report `c`, `SE(c)`, and the F-statistic against the linear fit. When `c` is insignificant, the quadratic is fitting noise and the agent should fall back to the [[least-squares-moving-average|LSMA]] baseline. This gate is the difference between a specialist estimator and a noise generator.
- **Measure the endpoint instability explicitly.** Recompute the baseline as each new bar arrives and log how much the *previous* bar's fitted endpoint revises. Large bar-to-bar revision of a supposedly-settled value is the endpoint-extrapolation problem showing itself, and it is directly observable — an agent that tracks revision magnitude knows when the reading is untrustworthy without any theory.
- **Always fit on centred `x`.** Use `x − x̄` or an orthogonal basis. An uncentred `[1, x, x²]` design is badly conditioned and can fail silently in single precision on longer windows.
- **Never raise `degree`.** Fix it at 2. Runge's phenomenon makes higher orders oscillate violently near the window edge, which is where the value is read — a cubic or quintic endpoint read degrades faster than the fit as a whole. If an agent is sweeping degree, it is manufacturing [[overfitting]], not improving the estimator.
- **Cross-check against the LSMA on the same bars.** Report both endpoints and the gap. The quadratic's advantage should be concentrated in windows the F-test flags as curved; if the two baselines diverge most in flat chop, that divergence is noise-fitting, not signal.
- **Validate on curvature-stratified history.** Replay `GET /api/v1/backtesting/klines` and score the member separately in high-curvature and low-curvature windows, with regime labels from `GET /api/v1/quant/regimes/history`. Aggregate performance will hide the fact that this estimator has two completely different behaviours.

## Related

- [[stretch-revert]] — the strategy family; `quadreg_stretch_revert` is the sim-tier member with zero trades to date
- [[least-squares-moving-average]] — the linear sibling; the estimator the quadratic should defer to when curvature is insignificant
- [[theil-sen-regression]] — the robust sibling; solves the outlier problem the quadratic makes worse
- [[bias-variance-tradeoff]] — the trade the extra parameter makes, in its most literal form
- [[curve-fitting]] — the failure mode a flexible model class invites
- [[moving-averages]] · [[adaptive-moving-averages]] — the wider estimator landscape
- [[simple-moving-average]] · [[exponential-moving-average]] — the averaging baselines, which represent neither slope nor curvature
- [[alma]] · [[frama]] · [[vidya]] · [[kama]] · [[hull-moving-average]] · [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] · [[jurik-moving-average]] · [[laguerre-filter]] · [[supersmoother-filter]] · [[kalman-filter-trading]] — sibling estimators; the Kalman filter is the principled alternative when a quadratic is not enough
- [[bollinger-bands]] — flat-mean band construction; the curved regression channel is its polynomial analogue
- [[z-score]] · [[standard-deviation]] — the scale the residual is measured on
- [[momentum]] — what the curvature coefficient `c` is measuring
- [[mean-reversion]] — the trade
- [[hurst-exponent]] — the mandatory regime gate
- [[stationarity]] — the assumption underneath the residual z-score
- [[overfitting]] — the dominant risk for this estimator specifically
- [[linear-regression]] — the first-order case

## Sources

- Polynomial least-squares regression is standard statistical method; no single attribution applies. Any regression text covers the leverage, adjusted-R², and nested F-test results used above.
- Runge, C. (1901). *Über empirische Funktionen und die Interpolation zwischen äquidistanten Ordinaten*. The original demonstration that high-order polynomial interpolation oscillates near interval edges — the phenomenon that caps the usable degree here.
- Family context, sim-tier status, the fourteen-member multiple-comparisons problem, and the walking-the-bands failure mode: [[stretch-revert]].
- No vault source-summary page covers polynomial regression baselines specifically. This page is derived from the method itself plus existing vault pages ([[moving-averages]], [[overfitting]], [[bollinger-bands]]). Every performance claim on it is analytic; `quadreg_stretch_revert` has no live or backtested record.

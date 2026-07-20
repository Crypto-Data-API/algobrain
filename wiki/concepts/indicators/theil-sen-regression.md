---
title: "Theil-Sen Regression"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, statistics, crypto]
aliases: ["Theil-Sen", "Theil-Sen Estimator", "Sen's Slope", "Kendall-Theil Robust Line", "Median Slope Regression", "Robust Regression Baseline"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[z-score]]", "[[standard-deviation]]", "[[hurst-exponent]]", "[[overfitting]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[stationarity]]", "[[least-squares-moving-average]]", "[[quadratic-regression]]", "[[alma]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[jurik-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[kalman-filter-trading]]", "[[linear-regression]]", "[[outliers]]", "[[median-absolute-deviation]]", "[[failure-modes]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis, quantitative]
prerequisites: ["[[moving-averages]]", "[[standard-deviation]]"]
difficulty: advanced
---

# Theil-Sen Regression

Theil-Sen is a non-parametric robust regression: instead of minimising squared error, it takes the **median of the slopes of every pairwise combination of points** in the window. Introduced by Theil (1950) and extended by Sen (1968), it produces a fitted line whose slope survives up to roughly 29% of the data being arbitrarily corrupted — where an ordinary least-squares fit can be destroyed by a single bad point. In crypto, where one wick, one bad print, or one exchange glitch routinely appears in a 15-minute window, that difference is not academic.

Used as a baseline, the Theil-Sen fit is evaluated at the most recent bar exactly as the [[least-squares-moving-average|LSMA]] is, and the deviation of price from it is a regression residual. Theil-Sen, LSMA, and [[quadratic-regression]] form the **regression group** in [[stretch-revert]]: the three estimators that fit a model to the window rather than averaging it, and therefore the three whose "stretch" is a residual with real statistical machinery behind it.

## Construction

```python
from itertools import combinations
from statistics import median

def theil_sen(close, period=25):
    """Theil-Sen robust regression baseline, evaluated at the endpoint.

    period : window length in bars. Keep it SHORT — the pairwise slope
             computation is O(n^2). n=25 -> 300 pairs; n=100 -> 4,950.
    """
    out = [None] * len(close)
    n = period

    for t in range(n - 1, len(close)):
        y = close[t - n + 1 : t + 1]
        x = list(range(n))

        # slope = median over all i < j of (y_j - y_i) / (x_j - x_i)
        slopes = [(y[j] - y[i]) / (x[j] - x[i]) for i, j in combinations(range(n), 2)]
        b = median(slopes)

        # intercept = median of (y_i - b * x_i)
        a = median(y[i] - b * x[i] for i in range(n))

        out[t] = a + b * (n - 1)            # ENDPOINT, as with the LSMA
    return out
```

- **Slope** — `b = median over all i<j of (y_j − y_i)/(x_j − x_i)`. There are `n(n−1)/2` such pairs.
- **Intercept** — `a = median(y_i − b·x_i)`, the conventional Sen choice. (An alternative places the line through the point `(x̄_med, ȳ_med)`; both are in use and they differ slightly.)
- **Baseline value** — `a + b·(n−1)`, the fitted line read at the most recent bar.
- **Residual** — `resid_t = close_t − TheilSen_t`, the stretch.

Parameter defaults for the `stretch_revert` context: `period` in the 14–32 bar range, entry z around 2.0–3.0, exit z near 0. Note the family member `theilsen_stretch_revert` runs at **1× leverage**, unlike the 3–5× used by most siblings — see [Use as a mean-reversion baseline](#use-as-a-mean-reversion-baseline).

## Robustness and breakdown point

The **breakdown point** of an estimator is the fraction of the data that can be replaced by arbitrary values before the estimate can be driven anywhere. It is the cleanest single number for comparing robustness.

| Estimator | Breakdown point | Meaning |
|---|---|---|
| OLS slope ([[least-squares-moving-average\|LSMA]]) | **0%** | One point, moved far enough, moves the fit without limit |
| Sample mean ([[simple-moving-average\|SMA]]) | **0%** | Same — one bad print drags the average |
| Theil-Sen slope | **~29.3%** | Up to ~29% of points can be arbitrary before the slope is unbounded |
| Median | 50% | The theoretical maximum for a location estimator |

The 29.3% figure is `1 − 1/√2 ≈ 0.293`. The intuition: corrupting a fraction *p* of the *points* corrupts roughly `1 − (1−p)²` of the *pairs*, and the median slope only breaks once more than half the pairs are corrupted — which requires `(1−p)² < 0.5`, i.e. `p > 1 − 1/√2`.

Why this matters concretely in crypto:

- **A single 1-tick wick to an absurd price** in a 25-bar window is 4% of the points and roughly 8% of the pairs. Theil-Sen does not notice. OLS tilts the fitted line, shifts the endpoint, and — because the same outlier also inflates the residual standard error — quietly recalibrates the entire z-score.
- **Thin alt-perp books** produce bad prints regularly. On Hyperliquid mid-caps, a fill through a gap in the book can print several percent away from fair value and revert on the next tick.
- **The compounding failure with OLS is the nastiest part.** An outlier corrupts both the numerator (the baseline, hence the residual) and the denominator (the residual standard error) of the z-score. The two errors do not reliably cancel. Theil-Sen fixes the numerator; pairing it with a robust scale such as [[median-absolute-deviation|MAD]] fixes the denominator too, and only then is the whole signal outlier-resistant.

**What robustness does not buy you.** Theil-Sen is a *statement about the estimator's sensitivity to contaminated inputs*. It says nothing about whether the underlying model is right, and it certainly says nothing about whether a trade based on it will work. A robust fit to a window that is genuinely trending is a robust estimate of a trend — and fading a trend is a losing trade no matter how well you measured it. This distinction turns out to be the single most important thing on this page; see below.

**Cost.** `n(n−1)/2` pairwise slopes per bar is **O(n²)**. At n=25 that is 300 slopes; at n=50, 1,225; at n=200, 19,900 — per bar, per asset. Across a 40-coin perp universe on 15m bars this becomes the dominant compute cost in the strategy. Exact O(n log n) algorithms exist (Cole et al. 1989) but are rarely implemented; the practical answers are to keep windows short, subsample the pairs (a random sample of a few thousand pairs approximates the median well), or use an incremental update. Slower recomputation also means a longer signal-to-fill latency, which on a fade is real cost.

## Fitting versus averaging

The regression group's shared property: a fitted model produces a **residual**, and a residual is a fundamentally better-defined object than "distance from a moving average".

An [[simple-moving-average|SMA]] or [[exponential-moving-average|EMA]] gives you a number, and price's distance from that number is a mixture of genuine displacement and the mechanical lag of the smoother. There is no model, so there is no notion of what the deviation *should* look like — you pick a band multiple by convention. A regression, by contrast, explicitly decomposes the window into "what the model explains" and "what it does not", and the leftover has a defined scale.

For OLS that scale is the residual standard error, with R² and slope t-statistics available alongside. Theil-Sen's non-parametric character changes which of these tools apply, and it is worth being precise rather than hand-waving:

- **Residual scale — use a robust one.** Computing the ordinary standard deviation of Theil-Sen residuals reintroduces exactly the sensitivity the estimator was chosen to avoid: the residual at the outlier bar is large, and squaring it dominates the scale. Use [[median-absolute-deviation|MAD]] instead, scaled by 1.4826 to be consistent with σ under normality. `z = resid / (1.4826 · MAD)` is the coherent Theil-Sen z-score; anything else is a robust numerator with a fragile denominator.
- **Confidence interval on the slope** — available, and non-parametric. The standard construction uses Kendall's tau: rank the `n(n−1)/2` pairwise slopes and take order statistics at positions determined by the variance of the tau statistic. This gives a distribution-free interval, which is genuinely nicer than the normality-assuming OLS interval on fat-tailed financial data.
- **R² — does not transfer cleanly.** R² is defined by a least-squares decomposition of variance. Theil-Sen does not minimise squared error, so its "R²" can be computed but is not the quantity it is in OLS and can even be negative. If you want a goodness-of-fit gate on a Theil-Sen baseline, use a robust analogue (e.g. the ratio of residual MAD to raw MAD) and label it honestly.
- **Prediction interval at the endpoint** — the same leverage caution as the LSMA applies. The endpoint is the extrapolated edge of the fit, the point of maximum uncertainty, and it is where the indicator reads its value.

The net: Theil-Sen keeps the *conceptual* benefit of the regression group — a genuine residual with a principled scale — while trading some of OLS's convenient closed-form machinery for distribution-free robustness. That is usually the right trade on crypto data, where the OLS machinery's assumptions (normal, homoskedastic, independent errors) are all false anyway.

## Lag and smoothing trade-off

Like the [[least-squares-moving-average|LSMA]], Theil-Sen plots the fitted line at the **endpoint**, so it does not carry the `(n−1)/2` centroid lag of an SMA. For a clean linear ramp both sit essentially on price while the SMA trails.

Where they diverge is behaviour at genuine structural change:

| Situation | SMA(25) | LSMA(25) | Theil-Sen(25) |
|---|---|---|---|
| Steady linear trend | lags ~12 bars | tracks | tracks |
| Single outlier bar | shifts by outlier/25 | **shifts substantially, line tilts** | essentially unmoved |
| Sharp genuine reversal | slow to turn | overshoots, then turns | **slowest of the three to turn** |
| Choppy range | smooth | noisier | smooth, steps discretely |

The last two rows are the honest cost. **Robustness and responsiveness are the same dial.** An estimator that ignores points inconsistent with the bulk of the window cannot distinguish "outlier" from "first bar of a real regime change" — because at the moment it arrives, a regime change looks exactly like an outlier. Theil-Sen will keep reporting the old slope for several bars into a genuine break, which is precisely the wrong behaviour if the break is real.

A second, subtler property: the median of a discrete set of pairwise slopes is a **step function** of the data. Small price changes often leave the median slope on the same pair, so the Theil-Sen baseline moves in small discrete jumps rather than continuously. It looks slightly blocky compared to an [[exponential-moving-average|EMA]] or [[supersmoother-filter|SuperSmoother]]. This is cosmetic for most purposes but can matter for exit logic keyed on the baseline crossing a level.

Relative to siblings: Theil-Sen is *smoother and slower* than the LSMA, far more robust than any of the averaging family, and much more expensive than all of them. It sits at the "trust the bulk of the window, ignore the extremes" end of the estimator spectrum — the opposite corner from [[zero-lag-exponential-moving-average|ZLEMA]] and [[triple-exponential-moving-average|TEMA]].

## Use as a mean-reversion baseline

`theilsen_stretch_revert` is a **prod-tier** member of [[stretch-revert]], and it is the family's most instructive member — not because it works, but because of how it fails.

**The design intent.** Fading a stretch requires trusting the baseline. If a bad print corrupts the baseline, the strategy fades a dislocation that never existed and pays the spread to discover it. On thin alt perps this is a recurring, mechanical loss. A robust baseline removes that failure mode: the fit ignores the wick, so no false signal is generated. The residual it does report reflects a displacement of the *bulk* of the window's price action, which is a much better definition of "stretch". This is a real and well-founded argument.

**The live record, and what it actually says.** From the family's dashboard snapshot: `theilsen_stretch_revert` has **10 trades, an 80% win rate, and net P/L of −$3.00**. Eight winners and two losers, where the two losers exceed all eight winners combined.

This is the family's canonical cautionary signature, and it is worth being blunt about the lesson, because the naive reading is exactly wrong:

> **A robust baseline makes the *measurement* robust. It does nothing to make the *position* robust.**

The two failure modes are completely separate:

1. **Measurement failure** — the baseline is wrong because the input was corrupted, so you enter on a stretch that was never there. Theil-Sen fixes this. That is plausibly *why* the win rate is 80%: the signals it does emit are better-conditioned, so most of them revert.
2. **Position failure** — the measurement was correct, price really was displaced, and then it kept going. The dislocation was information, not noise. Theil-Sen has nothing to say about this. Neither does any other estimator. It is a property of the market, not of the smoother.

The 80%/−$3.00 combination is these two effects in the same ten trades: better entries raising the hit rate, and one or two unreverting moves taking more than the eight small wins returned. That payoff shape — win small and often, lose large and rarely — is the *expected* shape of a reversion strategy, not a malfunction. It is why the family tracks net P/L rather than win rate, and why "win rate > 70% with negative net P/L over ≥ 20 trades" is an explicit kill criterion in [[stretch-revert]]. Win rate is close to uninformative here.

**The 1× leverage.** `theilsen_stretch_revert` runs at 1× while most siblings run 3–5×. Two readings, and both should be held simultaneously:

- *Charitable:* the position-failure mode is untouched by estimator robustness, so the sensible response is to reduce leverage — accepting that an unreverting move will happen and ensuring it is a drawdown rather than a liquidation. This is coherent risk logic.
- *Uncharitable:* it also means the member cannot earn its way out. Eight small wins at 1× do not offset two losses of the same character, and at 1× the strategy has a much thinner margin over funding and spread costs. A member that is de-risked because its tail is known to be bad may simply not have positive expectancy.

Ten trades cannot distinguish these. Nothing on this page should be read as evidence either way — the sample is far too small, and the family page is explicit that its whole live record is a point-in-time snapshot, not a validated result.

**Which regimes flatter it.** Illiquid or glitch-prone books; mid-cap alt perps where bad prints are frequent; markets that oscillate around a level with occasional violent spikes that revert within a bar or two. Precisely the environments where OLS baselines generate the most false signals.

**Which regimes expose it.**

- **Genuine regime breaks.** The estimator is *designed* to ignore points that disagree with the bulk of the window. The first several bars of a real breakout look exactly like that. Theil-Sen will report "no meaningful change in slope" while a real trend establishes, then read a large residual and fire a fade into it. This is walking-the-bands with extra steps, and it is the structural reason the family's [[hurst-exponent]] regime gate is mandatory rather than advisory.
- **Sustained trends of any kind.** As with every member. Robustness does not create edge where there is none.
- **Long windows.** O(n²) forces short windows, and short windows mean a smaller pool of pairs, which means a noisier median slope. The robustness advantage narrows as n shrinks.
- **Non-[[stationarity|stationary]] residual dispersion.** If MAD is estimated over a window spanning a volatility regime change, the z-threshold silently changes meaning — the same problem every member has.

## Parameters and tuning

| Parameter | Typical | Effect |
|---|---|---|
| `period` (n) | 14–32 bars | Hard-capped by O(n²) cost. Longer = more pairs = more stable median, but quadratically more compute |
| Scale estimator | MAD × 1.4826 | **Use a robust scale.** Ordinary σ on robust residuals reintroduces outlier sensitivity through the back door |
| Entry z | 2.0–3.0 | On the MAD-scaled residual |
| Exit z | 0.0–0.5 | Reversion to the fitted line |
| Intercept convention | `median(y − b·x)` | The alternative (median-point) convention gives slightly different values; pick one and never mix |
| Pair subsampling | full, or ~2,000 sampled pairs | Subsampling trades a little slope precision for large speedups on long windows |
| Leverage | 1× in the live member | Deliberately below the family's 3–5× |

**Overfitting warning.** Theil-Sen looks parameter-light — really just `period` — and that is a genuine advantage over [[jurik-moving-average|JMA]] or [[frama|FRAMA]]. But the [[overfitting]] surface is larger than it appears once the surrounding choices are counted: window, scale estimator, scale window, intercept convention, entry z, exit z, stop multiple, time-stop length, leverage. That is a substantial grid, and its best cell will look good on any history.

Specific traps:

- **Robustness is not validation.** A statistically well-behaved estimator with a tidy theoretical pedigree feels more trustworthy than a heuristic smoother, and that feeling is not evidence. Theil-Sen's 29.3% breakdown point is a fact about contaminated inputs; it implies nothing about whether fading its residuals is profitable.
- **Multiple comparisons across the family.** Fourteen baselines were tried. If Theil-Sen had won, its result would need deflating for the other thirteen. It did not win, which is itself worth recording — but nor is a ten-trade loss evidence that the estimator is bad.
- **Tuning to rescue a losing member.** With `theilsen_stretch_revert` at −$3.00, the temptation is to sweep parameters until it turns positive. On ten trades, almost any parameter set can be made to show a profit. That is curve-fitting to noise, and it is the single most likely way this member gets "fixed" into something worse.
- **Interaction with the leverage choice.** Changing leverage changes which trades hit stops and liquidations, so it is not a free multiplier on the P/L curve — it is another parameter with its own overfitting surface.

## Advantages

- **~29.3% breakdown point** versus 0% for OLS and the SMA — the highest robustness of any estimator in the [[stretch-revert]] family.
- **Immune to single bad prints, wicks, and exchange glitches**, which are a real and recurring feature of crypto perp data rather than a textbook hypothetical.
- **Non-parametric** — makes no distributional assumption about errors, which is a better fit for fat-tailed financial residuals than OLS's normality assumption.
- **Distribution-free confidence interval on the slope**, via the Kendall's-tau construction.
- **The deviation is a genuine regression residual**, with a principled robust scale (MAD) — shared with [[least-squares-moving-average|LSMA]] and [[quadratic-regression]], and unavailable to the eleven averaging-based members.
- **Endpoint evaluation removes SMA centroid lag** on linear price paths.
- **Few structural parameters** — essentially just `period`.
- **Well-established literature** — Theil (1950), Sen (1968), and decades of use in environmental trend detection, where noisy contaminated series are the norm.

## Limitations

- **O(n²) cost.** `n(n−1)/2` pairwise slopes per bar per asset. This caps window length, caps universe breadth, and adds signal-to-fill latency on a strategy where latency is cost.
- **Slow at genuine regime changes.** The mechanism that ignores outliers also ignores the first bars of a real break — the failure mode that matters most for a fade strategy.
- **Robustness protects the baseline, not the trade.** The central point of this page. It removes measurement error; it does not remove the risk that a correctly-measured dislocation simply keeps going. The live 80%-win-rate/negative-P/L record is that distinction made concrete.
- **Requires a matching robust scale.** Pairing a Theil-Sen numerator with a standard-deviation denominator reintroduces outlier sensitivity and is a common implementation error.
- **R² does not transfer.** Goodness-of-fit gating needs a robust analogue; the OLS quantity is not meaningful here.
- **Discrete, slightly blocky output** — the median slope is a step function of the data.
- **Cannot track curvature**, same as the LSMA. Accelerating moves are systematically mis-fit; see [[quadratic-regression]].
- **Two intercept conventions** in common use, producing slightly different baselines — a real reproducibility hazard between a backtest and a live implementation.
- **No evidence of edge in this vault.** Ten trades, negative net P/L, no backtest, no walk-forward, no cost-corrected record. See [[failure-modes]] and the family page's performance section.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the closes the pairwise slopes are computed over; keep `period` short given O(n²), but pull a long history so the MAD scale has a stable rolling sample
- `GET /api/v1/hyperliquid/l2-book?coin=X` — the complement to a robust fit: robustness removes bad prints from the *baseline*, this removes bad *fills* by rejecting entries when the residual is within a couple of spreads
- `GET /api/v1/derivatives/funding-rates?coin=X` — at 1× leverage, funding is a proportionally larger drag on held reversions than it is for the 3–5× members
- `GET /api/v1/derivatives/open-interest?coin=X` — OI expanding into a large robust residual argues the displacement is real flow, not noise

**Historical data:**
- `GET /api/v1/backtesting/klines` — kline archive for replaying the estimator and, importantly, for measuring how often raw data actually contains the outliers robustness is meant to defend against
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels, for scoring residuals only inside range-labelled states
- `GET /api/v1/volatility/regime/{symbol}` — volatility regime; MAD calibration is regime-dependent

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [funding rates](https://cryptodataapi.com/funding-rates) · [order-book depth](https://cryptodataapi.com/quant-order-books) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with Theil-Sen directly:

- **Quantify the robustness benefit before paying for it.** Fit both Theil-Sen and [[least-squares-moving-average|OLS]] on the same window from `GET /api/v1/hyperliquid/candles` and report the gap between the two endpoints. If the two agree to within a few basis points on a given coin, the O(n²) cost is buying nothing and the LSMA is the better estimator for that market. The gap is the decision variable.
- **Always pair with a robust scale.** Report `resid / (1.4826 × MAD)`, never `resid / σ`. An agent computing a standard-deviation z-score on Theil-Sen residuals has silently undone the entire point of the estimator, and the error is invisible in the output.
- **Budget the compute explicitly.** `n(n−1)/2` slopes per bar per asset — at n=25 across 40 coins that is 12,000 slope computations per bar. Either cap `period`, subsample pairs, or narrow the universe; do not let the window grow silently.
- **Separate the two failure modes when reviewing losses.** For each losing trade, check whether the baseline was corrupted (a measurement failure Theil-Sen should have prevented) or whether the dislocation was real and simply continued (a position failure no estimator prevents). The live 80%-WR/negative-P/L record predicts almost all losses fall in the second bucket; confirming that is the useful diagnostic, and it points at sizing and stops rather than at the smoother.
- **Do not tune on the live sample.** Ten trades. Any parameter sweep that turns −$3.00 positive is fitting noise. Validate against `GET /api/v1/backtesting/klines` with regime stratification from `GET /api/v1/quant/regimes/history` before changing anything, per [[overfitting]].

## Related

- [[stretch-revert]] — the strategy family; `theilsen_stretch_revert` is the 1× prod-tier member and the family's cautionary case
- [[least-squares-moving-average]] — the non-robust sibling; same endpoint-read idea, least squares instead of median-of-slopes
- [[quadratic-regression]] — the curved sibling; second-order fit, also endpoint-evaluated
- [[median-absolute-deviation]] — the robust scale that must accompany a robust fit
- [[outliers]] — what the breakdown point is defending against
- [[moving-averages]] · [[adaptive-moving-averages]] — the wider estimator landscape
- [[simple-moving-average]] · [[exponential-moving-average]] — the averaging baselines, both with 0% breakdown point
- [[alma]] · [[frama]] · [[vidya]] · [[kama]] · [[hull-moving-average]] · [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] · [[jurik-moving-average]] · [[laguerre-filter]] · [[supersmoother-filter]] · [[kalman-filter-trading]] — sibling estimators
- [[bollinger-bands]] — the band formulation of the same deviation idea, on a non-robust mean and scale
- [[z-score]] · [[standard-deviation]] — the scale the residual is measured on, and why the robust variant is required here
- [[mean-reversion]] — the trade
- [[hurst-exponent]] — the mandatory regime gate; especially load-bearing given Theil-Sen's slowness at genuine breaks
- [[stationarity]] — the assumption underneath any residual z-score
- [[overfitting]] — why a ten-trade sample must not be tuned on
- [[failure-modes]] — the family's catalogue, of which this member is a live example
- [[linear-regression]] — the underlying method

## Sources

- Theil, H. (1950). A rank-invariant method of linear and polynomial regression analysis. *Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen*. Original statement of the median-of-pairwise-slopes estimator.
- Sen, P. K. (1968). Estimates of the regression coefficient based on Kendall's tau. *Journal of the American Statistical Association* 63(324). Extends the estimator to tied data and provides the tau-based confidence interval.
- Cole, R., Salowe, J. S., Steiger, W. L., Szemerédi, E. (1989). An optimal-time algorithm for slope selection. *SIAM Journal on Computing*. The O(n log n) construction that avoids enumerating all pairs.
- The 1 − 1/√2 ≈ 29.3% breakdown point is a standard result in the robust statistics literature (see Rousseeuw and Leroy, *Robust Regression and Outlier Detection*, 1987, for the general framework).
- Live figures for `theilsen_stretch_revert` (10 trades, 80% win rate, −$3.00) are quoted from the dashboard snapshot recorded on [[stretch-revert]], dated 2026-07-20. That snapshot is not a backtest and no source-summary page exists for it.
- No vault source-summary page covers Theil-Sen specifically. The analysis on this page is derived from the method and from existing vault pages ([[moving-averages]], [[overfitting]], [[failure-modes]]).

---
title: "Triple Exponential Moving Average (TEMA)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, crypto]
aliases: ["TEMA", "Triple Exponential Moving Average", "Mulloy TEMA", "DEMA", "Double Exponential Moving Average"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[z-score]]", "[[hurst-exponent]]", "[[overfitting]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[alma]]", "[[hull-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[dema]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[jurik-moving-average]]", "[[least-squares-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[kalman-filter-trading]]", "[[standard-deviation]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis]
prerequisites: ["[[moving-averages]]", "[[exponential-moving-average]]"]
difficulty: intermediate
---

# Triple Exponential Moving Average (TEMA)

The Triple Exponential Moving Average, introduced by [[patrick-mulloy|Patrick Mulloy]] in *Technical Analysis of Stocks & Commodities* in early 1994 (see [Sources](#sources) — the exact article of the two is contested), removes lag by **estimating the smoothing error and subtracting it**, using three nested [[exponential-moving-average|EMAs]]. Despite the name, it is *not* a triple-smoothed EMA — it is a lag-cancelling linear combination that is faster than a single EMA, not slower. The same article introduced DEMA, its two-EMA sibling.

## Construction

```python
def ema(price, n):
    """Standard EMA, alpha = 2/(n+1). Seed with SMA over the first n values."""
    a = 2.0 / (n + 1)
    out = [None] * len(price)
    out[n - 1] = sum(price[:n]) / n
    for t in range(n, len(price)):
        out[t] = a * price[t] + (1 - a) * out[t - 1]
    return out

def tema(price, n=20):
    """Triple Exponential Moving Average (Mulloy 1994).

        EMA1 = EMA(price, n)
        EMA2 = EMA(EMA1,  n)     # EMA of the EMA
        EMA3 = EMA(EMA2,  n)     # EMA of that
        TEMA = 3*EMA1 - 3*EMA2 + EMA3

    NOT a triple-smoothed average. The 3/-3/+1 combination cancels the
    lag of the smoothing rather than compounding it.
    """
    e1 = ema(price, n)
    e2 = ema(e1, n)
    e3 = ema(e2, n)
    return [3 * a - 3 * b + c for a, b, c in zip(e1, e2, e3)]

def dema(price, n=20):
    """Mulloy's two-EMA sibling from the same article: DEMA = 2*EMA1 - EMA2."""
    e1 = ema(price, n)
    e2 = ema(e1, n)
    return [2 * a - b for a, b in zip(e1, e2)]
```

One parameter, `n`, with `alpha = 2/(n+1)` as usual. Typical values are 9, 14, 20, and 50.

**Why the coefficients are 3, −3, 1.** `EMA1` lags price. `EMA2` lags `EMA1` by roughly the same amount, so `EMA1 − EMA2` estimates the lag itself. DEMA adds that estimate back once: `EMA1 + (EMA1 − EMA2) = 2*EMA1 − EMA2`. TEMA applies the same correction one order higher, which is why the coefficients are the alternating binomial pattern `3, −3, +1`. The coefficients sum to 1 (so a constant input passes through unchanged), but their **absolute values sum to 7** — and that is the whole story of TEMA's noise behaviour.

## Lag and smoothing trade-off

An EMA of length `n` has a centre-of-mass lag of about `L = (n-1)/2` bars. Under a constant-slope trend, `price[t] = p`, each nested EMA lags proportionally: `EMA1 = p − L·s`, `EMA2 = p − 2L·s`, `EMA3 = p − 3L·s`, where `s` is the slope per bar. Substituting:

```
TEMA = 3(p − L·s) − 3(p − 2L·s) + (p − 3L·s)
     = p·(3 − 3 + 1) + s·(−3L + 6L − 3L)
     = p + 0
```

**TEMA has exactly zero lag under a constant-slope trend**, for any `n`. The same algebra gives DEMA zero lag too. This is not an approximation — it is an identity, and it is the point of the construction.

The price is paid in two places:

1. **Noise amplification.** With absolute coefficients summing to 7, high-frequency noise present in the input is magnified rather than suppressed. TEMA is visibly jagged where an EMA of the same `n` is smooth. This is a direct, unavoidable consequence of lag cancellation, not an implementation shortcoming.
2. **Overshoot at curvature.** The lag correction assumes constant slope. Where the second derivative is large — reversals, accelerations, gaps — the correction is wrong in the direction of the prior slope, and TEMA extrapolates past the turn. It can and routinely does print outside the recent price range.

| Estimator (n = 20) | Approx. lag (bars) | Noise gain | Can overshoot? |
|---|---|---|---|
| [[simple-moving-average\|SMA]] | 9.5 | low | no |
| [[exponential-moving-average\|EMA]] | ~9.5 | low | no |
| [[alma\|ALMA]] (0.85, 6) | ~2.9 | low-moderate | no |
| [[hull-moving-average\|HMA]] | ~0.7 | >1 (Σ\|c\| = 3) | yes |
| [[zero-lag-exponential-moving-average\|ZLEMA]] | ~0 under linear trend | moderate-high | yes |
| **TEMA** | **0 under linear trend** | **high (Σ\|c\| = 7)** | **yes, strongly** |
| DEMA | 0 under linear trend | moderate (Σ\|c\| = 3) | yes |

TEMA is the most aggressive of the common lag-cancellers. **DEMA is the same idea at lower intensity** and is often the better practical choice: identical zero-lag property, roughly half the coefficient magnitude, materially less jitter. If TEMA is being used and the noise is a problem, DEMA is the first thing to try rather than a longer `n`.

Because the nested EMAs are recursive, TEMA is also **seed-dependent**: values depend on how far back the calculation started. Three levels of recursion make this worse than for a plain EMA. Backtest and live values will disagree near the warm-up boundary unless both are anchored to the same start date — allow roughly `3n` bars of warm-up per level, so on the order of `6n`–`9n` bars in total before treating values as settled.

## Use as a mean-reversion baseline

In [[stretch-revert]], `tema_stretch_revert` uses TEMA as the baseline. The [[stretch-revert]] estimator table characterises it as *"only sharp extensions register"*, and the algebra above explains exactly why.

**In a trend, the residual collapses to noise.** Zero lag under constant slope means that during any steady directional move, TEMA sits essentially *on* price. `close - tema(close)` is then not a measure of displacement at all — it is a measure of the deviation of price from its own local linear extrapolation, i.e. curvature plus noise. Two implications:

- **This is genuinely protective.** The family's dominant failure mode is fading a trend that keeps going ("walking the bands"). A baseline with zero lag in trends structurally refuses to produce the persistent one-sided residual that drives that failure. TEMA does not fire into a clean trend, which is the single most valuable property a stretch baseline can have.
- **It is also why the member barely trades.** In [[stretch-revert]]'s live snapshot, `tema_stretch_revert` sits in the simulation tier with zero fills. That is not necessarily a defect; it is the expected consequence of a near-zero-lag baseline. **Extremely low recall is the design, not a bug — but it also means the member will take a very long time to accumulate enough trades to say anything statistically, per [[crypto-short-history-statistical-power]].**

**What does register: curvature, not displacement.** Because the linear component is cancelled, only *acceleration* produces meaningful residual. A liquidation flush — a sharp non-linear break from the prior slope — is exactly that, and it produces a large TEMA residual immediately, with no lag delay. TEMA is therefore a curvature detector wearing a moving-average costume, and as a fade trigger it fires on impulses rather than on extensions.

**The noise term is a serious contaminant of the z-score.** The residual σ used as the [[z-score]] denominator is inflated by TEMA's own jitter, not only by price volatility. That has a compounding effect on recall: the denominator is large because the baseline is noisy, so the numerator has to be very large to reach the entry threshold. Signals become rare *twice over*. On thin books the situation inverts and becomes dangerous — filter jitter can push the residual past the threshold on its own, producing entries backed by nothing but coefficient amplification.

**The overshoot damages exits.** As with [[hull-moving-average|HMA]], the "residual back through zero" exit can be satisfied by the *baseline* moving rather than by price reverting. TEMA's overshoot is larger than HMA's (no outer re-smoothing pass), so this is the more acute case. Audit whether exits are driven by price or by baseline before drawing any conclusion from the member's win rate.

**Which regimes flatter it:**

- *Range-bound markets with occasional violent impulses.* The regime where curvature and dislocation coincide.
- *Liquid majors on 15m+ bars,* where the input is clean enough that a 7× coefficient magnitude does not dominate.

**Which regimes expose it:**

- *Thin alt perps and low timeframes.* Noise amplification meets [[microstructure-noise-low-timeframe|microstructure noise]]. This is the worst pairing of any member in the family.
- *Choppy, high-curvature sideways action.* Every wiggle is curvature; TEMA generates residuals continuously and the "sharp extension" filter stops filtering.
- *Accelerating trends.* The dangerous case: acceleration is curvature, so TEMA reads a strong stretch precisely when a trend is picking up speed — the fade most likely to be run over. The [[hurst-exponent]] gate is doing load-bearing work here, not decorative work.

## Parameters and tuning

`n` is the only parameter, but it does not behave the way it does for an EMA:

| `n` | Effect on TEMA |
|---|---|
| Small (5–9) | Extremely jittery; residual is mostly filter noise. On 15m crypto, largely unusable as a baseline |
| Medium (14–21) | Common range; a reasonable 15m default |
| Large (50+) | Smoother, but zero-lag-in-trend still holds — a longer `n` does **not** make stretch register more often the way it would for an SMA |

That last row is the key non-obvious point: **lengthening `n` is not a lever for increasing trade count.** For a lagging baseline, a longer window means a bigger residual. For TEMA, the lag is cancelled at every `n`, so a longer window mostly just smooths the curvature signal. If a TEMA member is not trading and you want it to, the correct moves are to lower the entry z-threshold, switch to DEMA (weaker cancellation, some lag returns), or accept that this member is a low-frequency specialist and size the expectation accordingly.

Other decisions that matter:

- **Seed convention.** SMA seed vs first-value seed, and how many warm-up bars, both change early values. Triple recursion makes this more consequential than for a plain EMA.
- **Residual σ window.** Inflated by baseline jitter; a window matched to the current [[volatility-regime-classification|vol regime]] is better than a fixed one.

> **Overfitting warning.** TEMA's single parameter understates the real search space: `n` × DEMA-vs-TEMA × entry z × exit z × stop multiple × time-stop × σ window, and [[stretch-revert]] searches that space across fourteen estimators at once. A TEMA member that shows profit at `n = 17` and nowhere else is fitted, not edged. **The commonly cited TEMA periods have no derivation known to this vault — they are folklore inherited from EMA convention**, and there is no reason `2/(n+1)` calibration carries over cleanly to a filter with 7× coefficient magnitude. See [[overfitting]], [[probability-of-backtest-overfitting]], and [[deflated-sharpe-ratio]]; validate per [[regime-conditional-validation]]. TEMA's low fill rate makes this worse, not better: fewer trades means a wider confidence interval means an easier surface to fool yourself on.

## Advantages

- **Exactly zero lag under a constant-slope trend** — a provable identity, not an approximation, and it holds for every `n`.
- **Structurally refuses to fade clean trends** — the most valuable protective property a stretch baseline can have against the family's dominant failure mode.
- **Single parameter**, small nominal tuning surface.
- **O(1) per bar** — three recursive updates, no window scan; cheap at scale.
- **Fires on curvature, so its signals are impulses** — when TEMA does register stretch, it is a genuinely non-linear break, which is the flow the family is built to fade.
- DEMA offers the same zero-lag property at roughly half the noise, giving a natural dial-back option.

## Limitations

- **Strong noise amplification** (Σ|c| = 7) — the highest of the common estimators, and a direct consequence of the lag cancellation.
- **Overshoots hard at turning points**; the residual can flip sign for filter reasons and satisfy the exit condition without price reverting.
- **Very low recall as a stretch baseline** — near-zero residual in trends means few signals and slow accumulation of statistical evidence.
- **Reads acceleration as stretch**, so it can fire into an accelerating trend — the exact fade the family must avoid.
- **Seed-dependent through three levels of recursion**; backtest and live values diverge near warm-up boundaries. Budget ~6n–9n bars.
- **Poorly suited to thin books and low timeframes**, where amplified microstructure noise becomes a meaningful share of the measured stretch.
- The name is actively misleading — many practitioners assume it is *smoother* than an EMA when it is substantially faster and noisier.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — closes for the three nested EMAs; the deep pull matters here because triple recursion needs a long warm-up before values settle
- `GET /api/v1/hyperliquid/l2-book?coin=X` — critical for this member: TEMA's 7× coefficient magnitude turns spread noise into apparent stretch
- `GET /api/v1/derivatives/funding-rates?coin=X` — carry drag on held reversions
- `GET /api/v1/derivatives/open-interest?coin=X` — OI expanding into a curvature spike argues acceleration, i.e. the fade TEMA is most likely to get wrong

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive, deep enough to warm up three recursion levels before scoring
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels, so TEMA fades are scored only inside historically range-labelled states

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=SOL&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with TEMA specifically:

- **Warm up properly before trusting a value.** Pull the full 500 bars from `GET /api/v1/hyperliquid/candles` and discard the first ~6n–9n; three levels of EMA recursion carry seed bias much further than one. Signals computed on a short pull are an artefact of the seed, and this is the most common TEMA implementation error.
- **Decompose the residual into curvature and noise.** Compare `close - tema(close)` against `close - ema(close, n)` on the same bars. When the TEMA residual is large and the EMA residual is not, the reading is curvature or jitter — not the sustained displacement the fade thesis assumes.
- **Run DEMA in parallel as the control.** Same zero-lag property, Σ|c| = 3 instead of 7. If TEMA fires and DEMA does not, the extra signal came from coefficient amplification, not from the market.
- **Measure the overshoot rate.** On `GET /api/v1/backtesting/klines` history, count bars where TEMA prints outside its own recent price range, and check how many `tema_stretch_revert` exits coincide with them — those exits are baseline motion, not reversion.
- **Treat the acceleration case as a hard veto.** `GET /api/v1/quant/market` plus `GET /api/v1/volatility/regime/{symbol}`: TEMA reads acceleration as stretch, so a large residual arriving with a rising strong-trend probability is the single most dangerous configuration for this member.

## Related

- [[stretch-revert]] — the family where TEMA is the `tema_stretch_revert` baseline
- [[dema]] — Mulloy's two-EMA sibling from the same 1994 article; same zero-lag property, less noise
- [[moving-averages]] · [[adaptive-moving-averages]] — the estimator landscape
- [[exponential-moving-average]] — the building block; TEMA is three of them combined
- [[simple-moving-average]] — the slow reference point on the frontier
- [[alma]] — low lag *without* negative coefficients or overshoot
- [[hull-moving-average]] · [[zero-lag-exponential-moving-average]] — the other lag-cancellers, same pathology at lower intensity
- [[frama]] · [[vidya]] · [[kama]] · [[jurik-moving-average]] — data-adaptive alternatives
- [[least-squares-moving-average]] · [[theil-sen-regression]] · [[quadratic-regression]] — regression baselines
- [[laguerre-filter]] · [[supersmoother-filter]] · [[kalman-filter-trading]] — signal-processing and state-space baselines
- [[mean-reversion]] — the underlying thesis
- [[bollinger-bands]] — band formulation of the same deviation idea
- [[z-score]] · [[standard-deviation]] — turning the residual into a signal
- [[hurst-exponent]] — the mandatory regime gate, doing real work for this member
- [[overfitting]] — the risk in tuning `n`

## Sources

- **Patrick Mulloy, "Smoothing Data With Faster Moving Averages," *Technical Analysis of Stocks & Commodities* V.12:1, January 1994, pp. 11–19** — usually cited as the original TEMA and DEMA specification.
- **Patrick Mulloy, "Smoothing Data With Less Lag," *Technical Analysis of Stocks & Commodities* V.12:2, February 1994, pp. 72–80** — a second article also covering TEMA/DEMA and applying them to [[macd|MACD]].

> **Contested attribution.** Sources disagree on which of these two articles introduced TEMA. Encyclopedic sources credit the January article with both DEMA and TEMA; other sources credit the February article with TEMA specifically. Both articles exist and both are listed above; neither has been read for this vault. See [[patrick-mulloy]].
- The zero-lag identity, coefficient-magnitude figures, and warm-up requirements on this page are derived from the formulas above rather than quoted from a source.

*Verification note: the Mulloy attribution is well established; the specific article is not (see above). Neither article has been read for this vault. No independent empirical evaluation of TEMA on crypto perpetuals has been reviewed, and claims about preferred periods are convention rather than evidence.*

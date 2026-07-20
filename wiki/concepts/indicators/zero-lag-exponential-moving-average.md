---
title: "Zero-Lag Exponential Moving Average (ZLEMA)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, crypto]
aliases: ["ZLEMA", "Zero-Lag EMA", "Zero Lag Exponential Moving Average", "ZLEMA (Ehlers-Way)"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[z-score]]", "[[hurst-exponent]]", "[[overfitting]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[alma]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[jurik-moving-average]]", "[[least-squares-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[kalman-filter-trading]]", "[[john-ehlers]]", "[[standard-deviation]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis]
prerequisites: ["[[moving-averages]]", "[[exponential-moving-average]]"]
difficulty: intermediate
---

# Zero-Lag Exponential Moving Average (ZLEMA)

The Zero-Lag Exponential Moving Average, developed by [[john-ehlers|John Ehlers]] and Ric Way, removes lag by **de-lagging the input before smoothing it** rather than by modifying the smoother. It adds the recent price change back onto the current price to synthesise a series that leads the market by roughly the EMA's own lag, then runs a standard [[exponential-moving-average|EMA]] over that synthetic series. The correction assumes the recent trend is linear, so ZLEMA overshoots wherever curvature is high — most notably at reversals and during accelerating moves.

## Construction

```python
def ema(price, n):
    a = 2.0 / (n + 1)
    out = [None] * len(price)
    out[n - 1] = sum(price[:n]) / n          # SMA seed
    for t in range(n, len(price)):
        out[t] = a * price[t] + (1 - a) * out[t - 1]
    return out

def zlema(price, n=20):
    """Zero-Lag EMA (Ehlers & Way).

        lag       = (n - 1) // 2
        de_lagged = price + (price - price[t - lag])
                  = 2*price[t] - price[t - lag]
        ZLEMA     = EMA(de_lagged, n)

    The de-lagging step is a linear extrapolation: it assumes the move
    over the last `lag` bars continues at the same slope.
    """
    lag = (n - 1) // 2
    de_lagged = [None] * len(price)
    for t in range(lag, len(price)):
        de_lagged[t] = price[t] + (price[t] - price[t - lag])
    return ema(de_lagged[lag:], n)
```

One parameter, `n`, with `alpha = 2/(n+1)` and `lag = (n-1)/2`. Typical values are 14, 20, and 34. Integer-rounding of `lag` differs between implementations (`floor` vs `round`), which shifts values slightly; pin the convention if comparing platforms.

**Why `(n-1)/2`.** An EMA with `alpha = 2/(n+1)` has a centre-of-mass lag of about `(n-1)/2` bars. The de-lagging step deliberately pushes the input forward by that same amount, so the EMA's lag consumes the artificial lead and the output lands on the current price. It is a cancellation by construction, aimed at exactly the right magnitude.

## Lag and smoothing trade-off

Take a constant-slope trend, `price[t] = p` with slope `s` per bar. Then `price[t-lag] = p − lag·s`, so:

```
de_lagged = 2p − (p − lag·s) = p + lag·s
EMA(de_lagged, n) = (p + lag·s) − lag·s = p
```

**ZLEMA has zero lag under a constant-slope trend** — the same identity that [[triple-exponential-moving-average|TEMA]] and DEMA achieve, reached by a different route. TEMA cancels lag *inside* the smoother by combining nested EMAs; ZLEMA cancels it *outside*, by pre-distorting the input.

That difference in route shows up in the noise arithmetic. The de-lagged series is `2*price[t] − price[t-lag]`. If the raw bars carry independent noise of variance σ², the de-lagged series carries `4σ² + σ² = 5σ²` — a **five-fold variance inflation before any smoothing happens**. The subsequent EMA(n) then attenuates it, so ZLEMA lands between HMA and TEMA on jitter: noticeably noisier than a plain EMA, meaningfully calmer than TEMA.

| Estimator (n = 20) | Approx. lag (bars) | Noise gain | Can overshoot? |
|---|---|---|---|
| [[simple-moving-average\|SMA]] | 9.5 | low | no |
| [[exponential-moving-average\|EMA]] | ~9.5 | low | no |
| [[alma\|ALMA]] (0.85, 6) | ~2.9 | low-moderate | no |
| [[hull-moving-average\|HMA]] | ~0.7 | >1 (Σ\|c\| = 3) | yes |
| **ZLEMA** | **0 under linear trend** | **moderate-high (5σ² pre-smoothing)** | **yes** |
| [[triple-exponential-moving-average\|TEMA]] | 0 under linear trend | high (Σ\|c\| = 7) | yes, strongly |

**The overshoot mechanism is specific and worth naming precisely.** The de-lag term `price[t] − price[t-lag]` is a first-difference over `lag` bars — a slope estimate that is only valid if the path between those two points was straight. Where the second derivative is large, the estimate is wrong in the direction of the *prior* slope:

- **At a V-reversal**, ZLEMA is still extrapolating the old trend and keeps going past the turn, curling back only after the reversal has propagated through `lag` bars.
- **In an accelerating trend**, the slope over the last `lag` bars understates the current slope, so ZLEMA runs ahead of price in the trend direction.
- **In a decelerating trend**, the reverse: ZLEMA lags the flattening and sits beyond price.

ZLEMA also has a subtle artefact the other estimators do not share: it references a **single bar** `lag` periods ago, not a weighted set. One bad print at exactly `t − lag` distorts the de-lagged input for that bar and propagates through the EMA recursion. On thin books, a single wide wick can leave a visible mark.

Like TEMA, ZLEMA is recursive and therefore **seed-dependent**; allow roughly `3n` bars of warm-up plus `lag` before treating values as settled.

## Use as a mean-reversion baseline

In [[stretch-revert]], `zlema_stretch_revert` runs on the production tier and the estimator table describes it as *"filters slow drift"*. The zero-lag identity is precisely that description restated: any component of price motion that is locally linear is subtracted out before the residual is formed.

**Slow drift is invisible; only curvature registers.** `close - zlema(close)` is close to zero whenever price is moving at a steady rate, regardless of how far it has travelled. A 40% grind over three weeks produces no stretch signal at all. What remains in the residual is deviation from local linearity — impulses, gaps, flushes — plus noise. This makes ZLEMA a **high-precision, low-recall** baseline in the same family position as [[triple-exponential-moving-average|TEMA]], but less extreme: its lower noise gain means the [[z-score]] denominator is less inflated by filter jitter, so genuine displacement clears the threshold more readily. That is plausibly why `zlema_stretch_revert` sits in prod while `tema_stretch_revert` sits in sim — though with the family's current sample that ordering is not something the live record can actually establish.

**The protective property.** Refusing to signal during steady trends directly counters "walking the bands", the family's dominant failure mode. A [[simple-moving-average|SMA]] baseline fires repeatedly into a trend because the residual grows with the trend; ZLEMA's residual does not grow with the trend at all. This protection is structural and complements the mandatory [[hurst-exponent]] gate rather than replacing it.

**The dangerous inversion: acceleration reads as stretch.** The de-lag correction is *wrong in the trend direction* when a move is accelerating. So during a trend that is picking up speed, ZLEMA overshoots ahead of price and the residual points **against** the acceleration — the fade signal fires into a strengthening trend. This is the single most important thing to understand about ZLEMA as a mean-reversion baseline, because the error is not random: it is systematically biased toward the worst possible trade. Crypto liquidation cascades are accelerating moves by definition, so the setup arises regularly and in the exact conditions the family calls its home regime.

The practical mitigations are the ones the family already specifies, applied with more weight for this member: the [[hurst-exponent]] gate, an [[open-interest]] check (expanding OI into the move argues acceleration rather than exhaustion), and the [[stretch-revert]] time stop, which cashes out of a fade that has not reverted before the acceleration resolves.

**Exits are contaminated by the same mechanism.** At a genuine reversal ZLEMA overshoots past the turn, so the "residual back through zero" condition can be met by the baseline moving rather than price reverting. As with [[hull-moving-average|HMA]], this can scratch a trade a bar or two after entry, before the reversion it was waiting for occurs — the entry thesis was right and the exit rule cashed out anyway.

**Which regimes flatter it:**

- *Range-bound chop with occasional sharp flushes.* Curvature and dislocation coincide, and the drift-filtering suppresses everything else.
- *Slow-grinding markets that occasionally break.* ZLEMA stays silent through the grind and fires on the break — a genuinely useful selectivity.
- *Liquid majors on 15m bars,* where the single-bar `t − lag` reference is not distorted by wicks.

**Which regimes expose it:**

- *Accelerating trends and cascades* — the systematic-bias case above. This is where ZLEMA fails, and it fails in the same direction every time.
- *Thin alt perps.* Fivefold pre-smoothing noise inflation plus single-bar `t − lag` sensitivity make it vulnerable to the [[microstructure-noise-low-timeframe|bid-ask bounce]] the family must reject.
- *Sequences of sharp pivots.* Each pivot produces an overshoot; the residual becomes dominated by filter artefact.
- *Post-warm-up boundary conditions,* where the seed still influences values and backtest/live signals disagree.

## Parameters and tuning

`n` is the only parameter, but it controls two coupled things: the EMA smoothing constant and the de-lag distance `(n-1)/2`.

| `n` | `lag` | Character as a stretch baseline |
|---|---|---|
| 9 | 4 | Very fast, jittery; residual is largely noise on 15m crypto |
| 14 | 6 | Fast; short de-lag window means the slope estimate is fresh but noisy |
| 20 | 9 | Reasonable 15m default |
| 34 | 16 | Smoother, but the slope estimate spans 16 bars — the linearity assumption is much weaker over that distance, so overshoot grows |

The non-obvious consequence: **increasing `n` makes ZLEMA worse at the thing it is for, not better.** A longer de-lag distance means the linear-path assumption has to hold over more bars, so the correction is more often wrong and the overshoot is larger. Unlike a lagging baseline — where a longer window straightforwardly means a bigger, better-behaved residual — ZLEMA's error term grows with `n`. If the member is not producing enough signals, lowering the entry z-threshold is safer than lengthening the window.

Also worth pinning:

- **`lag` rounding** — `floor((n-1)/2)` vs `round`. Changes marginal entries.
- **Price input** — close vs HL2 vs HLC3. Because the de-lag references a single bar, wick-inclusive inputs are materially noisier here than for a window-averaging filter.
- **Seed and warm-up** — recursive, so anchor backtest and live to the same start bar; budget ~3n + lag bars.
- **Residual σ window** — inflated by baseline jitter; match it to the current [[volatility-regime-classification|vol regime]] rather than fixing it.

> **Overfitting warning.** One nominal parameter, but the real surface is `n` × lag-rounding × price input × entry z × exit z × stop multiple × time-stop × σ window — and [[stretch-revert]] explores it across fourteen estimators simultaneously, which is a multiple-comparisons problem before a single trade is placed. A ZLEMA configuration that is profitable at `n = 21` and unprofitable at 19 and 23 is fitted noise. **The commonly cited ZLEMA periods are folklore carried over from EMA convention; no derivation or empirical study establishing an optimal period for crypto perpetuals has been reviewed for this vault.** See [[overfitting]], [[probability-of-backtest-overfitting]], and [[deflated-sharpe-ratio]]; validate per [[regime-conditional-validation]].

## Advantages

- **Zero lag under a constant-slope trend** — a clean identity, achieved with a much simpler construction than TEMA's.
- **Structurally filters slow drift**, so it will not manufacture the persistent one-sided residual that drives the family's "walking the bands" failure.
- **Lower noise gain than TEMA** while sharing the zero-lag property — a better practical point on the frontier for stretch measurement, which is likely why it holds a prod slot.
- **Conceptually transparent** — the de-lagging step is one line and its failure mode is directly readable from the formula.
- **Single parameter** and **O(1) per bar** after the de-lag.
- Signals it does produce are impulse-driven, matching the forced-flow overshoots [[stretch-revert]] targets.

## Limitations

- **Systematically biased toward the worst trade in an accelerating move** — the residual points against the acceleration, so the fade fires into strengthening trends. This is the defining risk.
- **Overshoots at reversals**, so the residual can cross zero for filter reasons and satisfy the exit rule without price having reverted.
- **Fivefold noise variance inflation** before smoothing, from the `2p − p[lag]` term.
- **Single-bar sensitivity** at `t − lag` — one bad print distorts the input and propagates through the recursion. Unique to ZLEMA among the family's baselines.
- **Longer `n` degrades the correction**, so the usual "smooth it more" remedy makes the core mechanism less valid.
- **Low recall** as a stretch baseline — steady moves produce no signal at all, so evidence accumulates slowly.
- **Seed-dependent**; backtest and live values diverge near warm-up boundaries.
- Implementations differ on `lag` rounding, so "ZLEMA(20)" is not fully specified without stating the convention.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — closes for the de-lag term and the EMA; the pull must extend at least `n + lag` bars past the warm-up before values are usable
- `GET /api/v1/hyperliquid/l2-book?coin=X` — important for this member: the single-bar `t − lag` reference makes ZLEMA unusually sensitive to one wide print on a thin book
- `GET /api/v1/derivatives/open-interest?coin=X` — the key acceleration check; OI expanding into the move is the signature of the case ZLEMA reads backwards
- `GET /api/v1/derivatives/funding-rates?coin=X` — carry drag on held reversions

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for measuring overshoot frequency and separating curvature signals from noise
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels, so ZLEMA fades are scored only inside historically range-labelled states

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [open interest](https://cryptodataapi.com/open-interest) · [order-book depth](https://cryptodataapi.com/quant-order-books) · [funding rates](https://cryptodataapi.com/funding-rates)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with ZLEMA specifically:

- **Detect the acceleration trap before entering.** Estimate curvature from the candles — compare the slope over the last `lag` bars with the slope over the `lag` bars before that. When the recent slope is steeper and the ZLEMA residual points against it, the "stretch" is the de-lag correction being wrong, not a dislocation. This is the highest-value check on the page and should be a hard veto.
- **Cross-check the OI signature.** Pair that curvature read with `GET /api/v1/derivatives/open-interest?coin=X`: accelerating price plus expanding OI is a trend building, and it is exactly the configuration ZLEMA misreads as a fade setup.
- **Guard the single-bar reference.** Before trusting a residual, inspect the bar at `t − lag` in the candle series for an outlier wick. Unlike window-averaging baselines, ZLEMA has no averaging to dilute one bad print — a wick-driven residual is a filter artefact.
- **Warm up and anchor.** Discard the first `3n + lag` bars of any `GET /api/v1/hyperliquid/candles` pull, and anchor backtest replays from `GET /api/v1/backtesting/klines` to the same start bar; otherwise live and replayed signals will disagree near the boundary for recursion reasons rather than market reasons.
- **Compare against a lagging control.** Compute `close - sma(close, n)` alongside the ZLEMA residual. Where ZLEMA is silent and the SMA shows large stretch, the move is drift — correctly filtered. Where both fire, the displacement is real and the trade is the family's best case.

## Related

- [[stretch-revert]] — the family where ZLEMA is the `zlema_stretch_revert` baseline
- [[john-ehlers]] — co-author, and the source of several other baselines in the family
- [[moving-averages]] · [[adaptive-moving-averages]] — the estimator landscape
- [[exponential-moving-average]] — the smoother ZLEMA wraps
- [[simple-moving-average]] — the lagging control worth computing alongside it
- [[alma]] — low lag *without* extrapolation or overshoot
- [[hull-moving-average]] · [[triple-exponential-moving-average]] — the other lag-cancellers; same overshoot pathology, different constructions
- [[frama]] · [[vidya]] · [[kama]] · [[jurik-moving-average]] — data-adaptive alternatives
- [[least-squares-moving-average]] · [[theil-sen-regression]] · [[quadratic-regression]] — regression baselines; [[quadratic-regression]] explicitly models the curvature ZLEMA assumes away
- [[laguerre-filter]] · [[supersmoother-filter]] · [[kalman-filter-trading]] — signal-processing and state-space baselines
- [[mean-reversion]] — the underlying thesis
- [[bollinger-bands]] — band formulation of the same deviation idea
- [[z-score]] · [[standard-deviation]] — turning the residual into a signal
- [[hurst-exponent]] — the mandatory regime gate
- [[overfitting]] — the risk in tuning `n`

## Sources

- **John Ehlers and Ric Way** — original ZLEMA specification, published as trading-systems work rather than as peer-reviewed research.
- The zero-lag identity, the `5σ²` noise inflation figure, and the curvature-bias analysis on this page are derived from the formula above rather than quoted from a source.

*Verification note: the Ehlers & Way attribution is the standard one, but the original publication has not been located or read for this vault, and no publication date has been confirmed. No independent empirical evaluation of ZLEMA on crypto perpetuals has been reviewed. Statements about preferred periods are convention, not evidence.*

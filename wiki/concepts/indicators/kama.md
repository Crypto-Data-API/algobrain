---
title: "KAMA (Kaufman's Adaptive Moving Average)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, crypto, market-regime, regime-detection, scalping]
aliases: ["KAMA", "Kaufman's Adaptive Moving Average", "Kaufman Adaptive Moving Average", "Efficiency Ratio"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[z-score]]", "[[hurst-exponent]]", "[[overfitting]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[regime-detection]]", "[[technical-structural-regime]]", "[[frama]]", "[[vidya]]", "[[alma]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[jurik-moving-average]]", "[[least-squares-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[kalman-filter-trading]]", "[[perry-kaufman]]", "[[standard-deviation]]", "[[microstructure-noise-low-timeframe]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis]
prerequisites: ["[[moving-averages]]", "[[exponential-moving-average]]"]
difficulty: intermediate
---

# KAMA (Kaufman's Adaptive Moving Average)

KAMA is an [[exponential-moving-average|EMA]] whose smoothing constant is driven by an **Efficiency Ratio** — the net distance price travelled over `n` bars divided by the total length of the path it took to get there. Presented by [[perry-kaufman|Perry Kaufman]] in *Smarter Trading* (1995), it encodes a single idea very directly: a market that covered ground efficiently deserves a fast filter, and a market that thrashed a long way to end up where it started deserves a slow one.

KAMA is the efficiency-driven member of the [[adaptive-moving-averages|adaptive family]] used as a baseline in [[stretch-revert]]. Its siblings adapt to different signals: [[frama|FRAMA]] to a fractal-dimension estimate of path roughness, and [[vidya|VIDYA]] to a volatility/momentum ratio. Of the three, KAMA's adaptation signal is the most direct and the easiest to reason about — it is literally "how much of the movement was useful".

## Construction

```python
def kama(price, n=10, fast=2, slow=30):
    """Kaufman (1995) Adaptive Moving Average.

    n     : efficiency-ratio lookback (default 10)
    fast  : fastest EMA equivalent    (default 2  -> alpha 0.6667)
    slow  : slowest EMA equivalent    (default 30 -> alpha 0.0645)
    """
    fast_sc = 2.0 / (fast + 1)      # 0.66667
    slow_sc = 2.0 / (slow + 1)      # 0.06452
    out = [price[0]] * len(price)

    for t in range(n, len(price)):
        change = abs(price[t] - price[t - n])                       # net move
        volatility = sum(abs(price[i] - price[i-1])                 # path length
                         for i in range(t - n + 1, t + 1))
        er = (change / volatility) if volatility else 0.0           # ER in [0, 1]

        sc = (er * (fast_sc - slow_sc) + slow_sc) ** 2              # note the square
        out[t] = out[t-1] + sc * (price[t] - out[t-1])

    return out
```

**ER = |price(t) − price(t−n)| / Σ |price(i) − price(i−1)|** over the last `n` bars, bounded to `[0, 1]`.

**SC = ( ER·(2/(fast+1) − 2/(slow+1)) + 2/(slow+1) )²**, with defaults `fast = 2`, `slow = 30`, `n = 10`.

**KAMA(t) = KAMA(t−1) + SC·(price(t) − KAMA(t−1))**

The **squaring is deliberate and is the most important design decision in the formula.** Before squaring, `SC` interpolates linearly between 0.0645 and 0.6667. Squaring maps that to `0.00416` to `0.4444`, and it does so non-uniformly: the low end is compressed hard while the high end is only halved. The effect is that KAMA becomes *disproportionately* slow when efficiency is poor. At `ER = 0` the effective EMA period is ~479 bars — the filter is essentially frozen. That asymmetry is the whole point: Kaufman wanted the filter to refuse to move in chop, not merely to slow down.

Note also that KAMA's `slow` floor already yields extreme stickiness *before* the square, so the parameter that actually governs chop behaviour is `slow`, not `n`.

## What it adapts to

KAMA adapts to **path efficiency**: net displacement divided by total distance travelled. This is a directional-persistence measure, sign-blind (the numerator is an absolute value).

What the Efficiency Ratio captures:

- **Directional cleanliness.** `ER = 1.0` means every bar in the window moved the same direction — a monotone run. `ER = 0.0` means the window ended exactly where it started regardless of how far price wandered.
- **Trend quality rather than trend size.** A slow, orderly 1% grind over 10 bars with no retracement scores `ER ≈ 1.0`. A violent 8% move that retraced 6% of it scores far lower. KAMA rewards orderliness.
- **Retracement structure.** ER falls whenever a trend takes back ground, so it degrades smoothly as a trend gets choppier rather than flipping states.

What it does **not** capture:

- **Volatility level.** ER is a ratio of two distances measured on the same series, so it is scale-free. A 0.2% move and a 20% move with identical shape produce identical ER. This is the same blind spot [[frama|FRAMA]] has and the opposite of [[vidya|VIDYA]]'s stdev form, which sees nothing but volatility.
- **Direction.** `|change|` discards sign; ER is high for clean moves either way.
- **Structure below the bar.** ER's denominator is the sum of *bar-to-bar close changes*. Intrabar path is invisible, so on 15m bars a violently whipsawing 15 minutes that closes near its open contributes almost nothing to the denominator. On low timeframes the opposite problem appears: [[microstructure-noise-low-timeframe|bid-ask bounce]] inflates the denominator and crushes ER toward zero, freezing KAMA for reasons that have nothing to do with market structure.
- **Anything about *why* a move was efficient.** A short squeeze and a fundamental repricing produce the same ER.

Relationship to [[hurst-exponent|Hurst]]: ER and the Hurst exponent both measure persistence, but ER is a single-window, single-scale ratio computed over 10 bars, while Hurst is a multi-scale estimate of the scaling of dispersion. They correlate in obvious cases and diverge in interesting ones. ER is a filter control; Hurst is the regime gate in [[stretch-revert]]. Do not substitute one for the other.

## Lag and smoothing trade-off

With defaults `fast = 2`, `slow = 30`, `n = 10`:

| Market state | ER | Pre-square SC | `SC` (squared) | Equivalent EMA |
|---|---|---|---|---|
| Monotone run | 1.00 | 0.667 | 0.444 | ~3.5 bars |
| Clean trend | 0.70 | 0.487 | 0.237 | ~7.4 bars |
| Ordinary drift | 0.40 | 0.306 | 0.094 | ~20 bars |
| Choppy | 0.20 | 0.185 | 0.034 | ~57 bars |
| Directionless | 0.05 | 0.095 | 0.009 | ~220 bars |
| Perfect chop | 0.00 | 0.065 | 0.0042 | ~479 bars |

The range is enormous — roughly 3.5 to 479 equivalent bars from one filter with one parameter set. Against fixed alternatives, an [[simple-moving-average|SMA(10)]] has ~4.5 bars of lag always; an [[exponential-moving-average|EMA(10)]] roughly the same. KAMA is *faster* than either when ER exceeds about 0.85, comparable around ER ≈ 0.5, and vastly slower below that. Because typical crypto 15m ER sits in the 0.15–0.45 band, **KAMA's default configuration spends most of its life behaving like a 20–60 bar EMA**, punctuated by brief episodes of near-price tracking.

That distribution — mostly very slow, occasionally very fast — is the KAMA signature, and it is markedly different from FRAMA (whose `alpha` distribution is smoother, because `exp(-4.6(D−1))` is a gentler map) and from CMO-form VIDYA (which can never exceed its nominal speed at all). Anyone comparing the three should compare realised `SC`/`alpha` distributions, not nominal periods.

## Use as a mean-reversion baseline

KAMA drives `fast_kama_stretch_revert`, which runs on [[stretch-revert]]'s 1–5m fast loop rather than the 15m loop most members use.

**The case for it.** The squared smoothing constant makes KAMA an exceptionally sticky baseline in chop — the regime where the strategy's edge actually lives. At `ER = 0.15` the baseline is moving at roughly an EMA(80) pace; at `ER = 0.05` it is effectively pinned. A pinned fair-value reference is the ideal case for stretch measurement: the residual is a clean read on how far price has wandered from a stable level, and the reversion target does not move under the position. None of the other thirteen estimators are as reliably immobile in a range as KAMA with default `slow = 30`.

**The problem — adaptive-baseline suppression.** KAMA has the most severe version of the family's central trade-off, and it is worth being blunt about it. A liquidation flush is, by ER's definition, a **maximally efficient move**: every bar in the same direction, net displacement equal to path length, `ER → 1.0`. KAMA responds by jumping `SC` to 0.444 — an EMA(3.5) — and the baseline **sprints after the price**.

The arithmetic is stark. On a three-bar flush with `SC = 0.444`, the baseline closes roughly 83% of the gap to price (`1 − 0.556³`). A dislocation that would read as a 3σ stretch against a static mean can read under 1σ against a KAMA that has already chased it. The signal is not merely reduced; it can be eliminated. And the transition is fast — ER moves from 0.2 to 0.9 within a couple of bars of a clean impulse, so KAMA switches from frozen to sprinting exactly at the onset of the event the strategy exists to trade.

This is the sharpest statement of the adaptive-baseline problem in the whole family: **the property that makes an adaptive baseline safe in trends (it chases, so it will not fade a runaway) is the same property that blinds it to fast dislocations.** FRAMA has the issue via low `D`; stdev-VIDYA has it via high `k`; KAMA has it most acutely because ER's definition of "efficient" and a flush's definition of "violent one-way move" are the same thing.

The z-score denominator compounds it in the same way as the other two: shrinking residuals shrink the rolling σ on a lag, so thresholds wander for non-market reasons. Log raw residual next to z on any KAMA-based member.

**Regimes that flatter KAMA as a baseline:**
- Grinding, low-ER ranges. The baseline is pinned, excursions register at full magnitude, and the fade target is genuinely static.
- Mean-reverting assets on the fast loop where the *shape* of moves is oscillatory — ER stays low even when volatility is high, so KAMA stays slow through the noise.
- Post-event consolidation, where ER has decayed back to the chop band and the reference has re-stabilised.

**Regimes that expose it:**
- Any clean impulse. This is the failure case, and it is not a corner case in crypto perps — it is Tuesday.
- Low-timeframe operation on thin books, which is exactly where `fast_kama_stretch_revert` runs. Spread bounce inflates ER's denominator and pins the baseline; the stretch it then measures may be the [[microstructure-noise-low-timeframe|spread itself]] rather than a dislocation. The `l2-book` pre-entry check is not optional for this member.
- Trends that grind rather than impulse. ER hovers near 0.5, `SC ≈ 0.13`, and KAMA lands in the worst of both worlds: fast enough to have followed the trend partway, slow enough to still show a residual. The strategy fades a trend at reduced size — the most expensive combination.

Mitigation used in practice: cap `SC` (equivalently, raise `fast` from 2 to 5–8) so the baseline cannot sprint. This trades away some trend protection to recover stretch sensitivity, and is a real, deliberate choice — not a free improvement.

## Parameters and tuning

| Parameter | Typical | Notes |
|---|---|---|
| `n` (ER lookback) | 10 (range 8–20) | Shorter reacts faster and is noisier; on 1m bars, values under ~10 make ER largely a spread artifact |
| `slow` | 30 (range 20–50) | Governs chop behaviour. Raising it makes the pinned state stickier — usually what a mean-reversion baseline wants |
| `fast` | 2 (range 2–10) | Governs impulse behaviour. **Raising `fast` is the direct lever on the suppression problem**; `fast = 6` caps `SC` at ~0.082 and stops the baseline sprinting |
| Squaring exponent | 2 | Kaufman's original. Treat as fixed. Tuning the exponent is tuning the shape of the whole filter and is not a parameter in any meaningful sense |
| σ window (z-score) | 50–100 bars | Set independently of `n` |

**Overfitting warning.** KAMA looks like a three-parameter filter and behaves like more, because `fast`, `slow`, and the exponent interact multiplicatively through the square. A grid over `n × fast × slow`, layered on [[stretch-revert]]'s entry threshold, exit threshold, stop multiple and time stop, is a large enough search space to manufacture an excellent-looking equity curve from noise. See [[overfitting]] and [[probability-of-backtest-overfitting]]. Discipline:

- Hold the exponent at 2. It is structure, not a knob.
- Change `fast` only for the stated structural reason above (capping baseline sprint), and record the reason. Do not sweep it for performance.
- Tune `n` on a coarse grid (8 / 10 / 14 / 20) and require a plateau rather than a peak.
- Because `fast_kama_stretch_revert` runs on 1–5m bars, any tuning result is especially vulnerable to fitting microstructure. Validate on out-of-sample bars with a realistic cost overlay before believing anything.
- [[stretch-revert]] already tests fourteen estimators; per-estimator tuning multiplies the comparison count and demands [[deflated-sharpe-ratio]] deflation.

## Advantages

- The clearest and most interpretable adaptation signal of the three: ER has an unambiguous meaning that can be read off a chart and sanity-checked by hand.
- The squared smoothing constant makes KAMA exceptionally sticky in chop — the single best "pinned fair value" of the family, which is what stretch measurement wants.
- Enormous dynamic range (~3.5 to ~479 equivalent bars) from one parameter set, so a single configuration covers regimes that would otherwise need multiple filters.
- Scale-free: ER is unitless, so the same parameters transfer across assets with very different volatility profiles without rescaling.
- Cheap and recursive; one rolling sum and one EMA update per bar, viable on 1m bars across a wide universe.
- Well-documented original source with an explicit rationale from [[perry-kaufman|Kaufman]], and long enough in circulation to have known behaviour.

## Limitations

- **The most severe suppression problem in the adaptive family.** A liquidation flush is definitionally a maximum-ER event, so KAMA accelerates hardest precisely when a mean-reversion strategy most needs a static reference.
- ER is computed on close-to-close changes only; intrabar path is invisible, and on low timeframes spread bounce dominates the denominator.
- The near-frozen state at low ER is not always benign — a pinned baseline sitting at a stale level biases every residual computed against it, and there is no mechanism that notices.
- Blind to volatility level, so it cannot distinguish a quiet efficient drift from a violent efficient move; both get the same fast filter.
- The mid-ER band (~0.4–0.6) is the worst zone: partially chased trend plus a residual still large enough to trigger a fade.
- The single-scale ER is a much cruder persistence estimate than [[hurst-exponent|Hurst]] and should not be used as a regime gate on its own.
- No independent validation reviewed in this vault. Kaufman's presentation is a design rationale; there is no widely replicated evidence that KAMA beats a well-chosen fixed filter net of costs.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — closes for the ER lookback and the KAMA recursion; use `interval=1m` for the `fast_kama_stretch_revert` loop
- `GET /api/v1/hyperliquid/l2-book?coin=X` — mandatory for the fast-loop member: on thin books an inflated ER denominator pins the baseline and the measured stretch may just be the spread
- `GET /api/v1/quant/market` — HMM regime probabilities, for cross-checking the regime KAMA's ER implies against an independent classifier
- `GET /api/v1/volatility/regime/{symbol}` — volatility state, which ER is scale-free to and therefore cannot see
- `GET /api/v1/derivatives/funding-rates?coin=X` — carry drag on reversions held through a low-ER stall

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for replaying the ER and `SC` series across full cycles
- `GET /api/v1/quant/regimes/history` — hourly regime labels since 2020, for scoring ER against labelled trend/range states

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=BTC&interval=1m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books) · [funding rates](https://cryptodataapi.com/funding-rates)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can compute KAMA and, more importantly, measure how much stretch it is eating:

- **Compute and expose ER** — from one `GET /api/v1/hyperliquid/candles` pull, emit ER, `SC`, and the equivalent-EMA period alongside the KAMA line. ER is the interpretable part; a KAMA plot without it hides the filter's entire state.
- **Cross-check the implied regime** — KAMA asserts a regime every bar through ER. Compare against `GET /api/v1/quant/market`: sustained `ER > 0.7` while the HMM reports range, or `ER < 0.2` during a labelled strong trend, is a disagreement that should be resolved before either signal is traded.
- **Probe the volatility blind spot** — pair ER with `GET /api/v1/volatility/regime/{symbol}`. The high-volatility / high-ER bucket is where the baseline sprints hardest; audit the member's fills in that bucket specifically, since that is where suppression destroys the signal.
- **Quantify suppression numerically** — recompute the residual over identical bars against KAMA and against a fixed EMA of matched *realised* period. Track the residual ratio during the largest 1% of moves; that number is the cost of the adaptive baseline, stated in the strategy's own units.
- **Guard the fast loop** — call `GET /api/v1/hyperliquid/l2-book` before every 1m entry and reject when the measured stretch is within a couple of spreads. On low timeframes ER is spread-contaminated in both directions, and this check is the difference between a dislocation and a rounding error.

## Related

- [[frama]] — sibling adaptive filter; adapts to a fractal-dimension estimate of path roughness
- [[vidya]] — sibling adaptive filter; adapts to a volatility/momentum ratio rather than efficiency
- [[adaptive-moving-averages]] — the family overview
- [[stretch-revert]] — the strategy family this page supports; `fast_kama_stretch_revert` uses this estimator on the 1–5m loop
- [[perry-kaufman]] — the author
- [[moving-averages]] · [[simple-moving-average]] · [[exponential-moving-average]] — the fixed-weight baselines KAMA modifies
- [[hurst-exponent]] — multi-scale persistence measure; related to ER but not a substitute
- [[mean-reversion]] · [[bollinger-bands]] · [[z-score]] · [[standard-deviation]] — the deviation framework KAMA feeds
- [[regime-detection]] · [[technical-structural-regime]] — independent regime classifiers to cross-check ER against
- [[microstructure-noise-low-timeframe]] — the ER-contamination hazard on the fast loop
- [[alma]] · [[hull-moving-average]] · [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] · [[jurik-moving-average]] · [[least-squares-moving-average]] · [[laguerre-filter]] · [[supersmoother-filter]] · [[theil-sen-regression]] · [[quadratic-regression]] · [[kalman-filter-trading]] — the other baseline estimators in the family
- [[overfitting]] — the parameter-tuning hazard

## Sources

- Kaufman, Perry J. — *Smarter Trading: Improving Performance in Changing Markets* (McGraw-Hill, 1995). Original presentation of the Efficiency Ratio, the squared smoothing-constant mapping, and the `fast = 2` / `slow = 30` / `n = 10` defaults.
- Kaufman, Perry J. — *Trading Systems and Methods* (Wiley, multiple editions). Extended treatment of KAMA within the broader adaptive-filter and trend-system literature.

No independent validation study of KAMA has been reviewed in this vault. The equivalent-EMA figures in the lag table are computed directly from the smoothing-constant formula, not measured from a backtest, and the suppression arithmetic is likewise a property of the recursion rather than an empirical result.

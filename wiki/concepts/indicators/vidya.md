---
title: "VIDYA (Variable Index Dynamic Average)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, crypto, volatility, market-regime, regime-detection]
aliases: ["VIDYA", "Variable Index Dynamic Average", "Chande VIDYA", "Volatility Index Dynamic Average"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[z-score]]", "[[hurst-exponent]]", "[[overfitting]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[regime-detection]]", "[[technical-structural-regime]]", "[[frama]]", "[[kama]]", "[[alma]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[jurik-moving-average]]", "[[least-squares-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[kalman-filter-trading]]", "[[tushar-chande]]", "[[chande-momentum-oscillator]]", "[[standard-deviation]]", "[[volatility]]", "[[volatility-regime-classification]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis]
prerequisites: ["[[moving-averages]]", "[[exponential-moving-average]]"]
difficulty: intermediate
---

# VIDYA (Variable Index Dynamic Average)

VIDYA is an [[exponential-moving-average|EMA]] whose smoothing constant is scaled bar by bar by a **volatility/momentum ratio**. Introduced by [[tushar-chande|Tushar Chande]] in 1992 and developed further in Chande & Kroll, *The New Technical Trader* (1994), it starts from a simple observation: a fixed EMA is too slow when the market is moving hard and unnecessarily jumpy when it is quiet. VIDYA multiplies the standard EMA constant `2/(n+1)` by a bounded index `k` that rises with market activity, so the filter speeds up when there is something to track and slows down when there is not.

It is the volatility-driven member of the [[adaptive-moving-averages|adaptive family]] behind [[stretch-revert]]. Its two siblings adapt to different things entirely: [[frama|FRAMA]] to path roughness (fractal dimension) and [[kama|KAMA]] to an efficiency ratio. VIDYA is the only one of the three that responds to how *big* moves are rather than what *shape* they have.

## Construction

```python
def vidya(price, n=14, k_mode="cmo", cmo_period=9,
          short=10, long=40):
    """Chande (1992) Variable Index Dynamic Average.

    n          : nominal EMA period -> alpha = 2/(n+1)   (default 14)
    k_mode     : "cmo"    -> k = |CMO(cmo_period)| / 100     (Chande's original)
                 "stdev"  -> k = stdev(price, short) / stdev(price, long)
    """
    alpha = 2.0 / (n + 1)
    out = [price[0]] * len(price)
    warmup = max(cmo_period, long) + 1

    for t in range(warmup, len(price)):
        if k_mode == "cmo":
            # Chande Momentum Oscillator over cmo_period bars
            ups = sum(max(price[i] - price[i-1], 0)
                      for i in range(t - cmo_period + 1, t + 1))
            dns = sum(max(price[i-1] - price[i], 0)
                      for i in range(t - cmo_period + 1, t + 1))
            cmo = 100.0 * (ups - dns) / (ups + dns) if (ups + dns) else 0.0
            k = abs(cmo) / 100.0                     # k in [0, 1]
        else:
            s_short = stdev(price[t-short+1 : t+1])
            s_long  = stdev(price[t-long+1  : t+1])
            k = (s_short / s_long) if s_long else 0.0   # typically ~[0.3, 2.5]

        a = alpha * k                                # effective smoothing constant
        a = min(max(a, 0.0), 1.0)                    # clamp for the stdev variant
        out[t] = a * price[t] + (1 - a) * out[t-1]

    return out
```

The recursion is the plain EMA update with `alpha` replaced by `alpha·k`:

**VIDYA(t) = alpha·k·price(t) + (1 − alpha·k)·VIDYA(t−1)**, where **alpha = 2/(n+1)**

Two formulations of `k` are in common use:

- **(a) The original — Chande Momentum Oscillator.** `k = |CMO(period)| / 100`. The [[chande-momentum-oscillator|CMO]] is Chande's own oscillator: `100·(up_sum − down_sum)/(up_sum + down_sum)` over the lookback. It is bounded to `[−100, 100]`, so `k ∈ [0, 1]` and the effective smoothing constant never exceeds `2/(n+1)`. VIDYA in this form is **never faster than its nominal EMA — only equal or slower.**
- **(b) The standard-deviation variant.** `k = stdev(price, short)/stdev(price, long)`, typically `short = 10`, `long = 40`. This ratio is unbounded above; in a volatility expansion it routinely reaches 1.8–2.5, so the effective constant can exceed `2/(n+1)` and VIDYA becomes *faster* than its nominal EMA. This variant is the one most crypto implementations ship, and it behaves materially differently from the original. Which one is running matters and should be stated wherever VIDYA is quoted.

Defaults used in [[stretch-revert]]'s `vidya_stretch_revert` member: `n = 14` on 15m bars with the stdev formulation, `short = 10`, `long = 40`.

## What it adapts to

VIDYA adapts to **activity level** — either directional imbalance (CMO form) or the ratio of recent to baseline dispersion (stdev form).

What the signal captures:

- **Volatility expansion and contraction.** The stdev form is a direct short/long volatility ratio. When realised vol doubles against its own recent baseline, `k` roughly doubles and the filter roughly doubles in speed.
- **Momentum imbalance** (CMO form). `|CMO|` is near 100 when nearly every bar in the lookback moved the same direction, and near 0 when ups and downs are balanced in magnitude. This is a directional-persistence measure, closer in spirit to KAMA's efficiency ratio than to volatility.
- **Regime transitions at the volatility level.** VIDYA reacts quickly to a vol shock — faster than FRAMA, which can sit at `D ≈ 1.9` through a large but choppy expansion.

What it does **not** capture:

- **Path efficiency.** In the stdev form, a violent whipsaw that ends where it started produces the same `k` as a violent clean trend. Both are high-dispersion. VIDYA speeds up for both, which means it can accelerate into exactly the chop it should be smoothing through. This is the mirror image of FRAMA's blind spot, and it is why the two are worth running together.
- **Direction.** `k` uses `|CMO|` and a dispersion ratio; both are sign-blind by construction.
- **Absolute volatility.** The stdev form is a *ratio*. A market in sustained high volatility with a stable profile has `s_short ≈ s_long` and `k ≈ 1` — VIDYA reverts to being an ordinary EMA(n). It responds to volatility *changes*, not volatility *levels*, which surprises people who expect it to be permanently fast in crypto.
- **Anything, when `k` collapses.** In the CMO form, a balanced range drives `|CMO| → 0`, `k → 0`, and the filter freezes: `VIDYA(t) ≈ VIDYA(t−1)`. A frozen baseline is not the same as a smooth one; it can sit at a stale level for many bars.

## Lag and smoothing trade-off

For the CMO form with `n = 14` (`alpha = 0.133`):

| Market state | `\|CMO\|` | `k` | Effective `alpha` | Equivalent EMA |
|---|---|---|---|---|
| Strong one-way run | 85 | 0.85 | 0.113 | ~17 bars |
| Moderate trend | 50 | 0.50 | 0.067 | ~30 bars |
| Mild drift | 25 | 0.25 | 0.033 | ~60 bars |
| Balanced chop | 8 | 0.08 | 0.011 | ~187 bars |
| Perfect balance | 0 | 0.00 | 0.000 | frozen |

For the stdev form with `n = 14`, `k` typically ranges ~0.5 to ~2.2, giving effective periods roughly from EMA(28) in a vol contraction down to EMA(6) in a vol expansion.

Against the fixed alternatives: an [[simple-moving-average|SMA(14)]] has ~6.5 bars of lag in every regime. VIDYA in CMO form is **never faster than EMA(14)** and is usually considerably slower — it is best understood as an EMA with a variable brake, not a variable accelerator. The stdev form does accelerate, but only relative to its own recent volatility baseline.

The practical consequence: VIDYA is smoother than an equivalently-labelled EMA most of the time, which is attractive for a fair-value baseline. The cost is that its *nominal* period badly understates its typical effective period. A "VIDYA(14)" is, on average across a normal crypto session in CMO form, behaving somewhere around a 40–70 bar EMA. Comparing it like-for-like against an EMA(14) is a category error, and comparisons in the [[stretch-revert]] estimator table should be made on *realised* average `alpha`, not nominal `n`.

## Use as a mean-reversion baseline

VIDYA is the estimator behind `vidya_stretch_revert`. The trade fades `price − baseline` normalised by rolling [[standard-deviation]] into a [[z-score]]; see [[stretch-revert]] for the full spec.

**The case for it.** Because the CMO form can only ever slow down, VIDYA is a comparatively *sticky* baseline. Sticky is exactly what a stretch measurement wants: a fair-value reference that does not chase the dislocation is one against which the dislocation is fully measurable. In balanced chop — the family's home regime — `k` collapses, the baseline nearly freezes, and every excursion registers at close to its full size. Of the three adaptive estimators, the CMO-form VIDYA is the least prone to the suppression problem below.

**The problem — adaptive-baseline suppression, stdev form.** The stdev variant inverts that advantage and is the clearer illustration of the family-wide trade-off. A liquidation flush *is* a volatility expansion: `s_short` spikes against `s_long`, `k` jumps to 2.0+, the effective `alpha` doubles or triples, and the baseline accelerates **downward into the flush**. The residual — the very quantity the strategy trades — is compressed at the exact moment the dislocation is largest.

Concretely: a 3% flush against a quiet-market VIDYA (`k = 0.7`, effective `alpha ≈ 0.093`) leaves ~2.7% in the residual on the impulse bar. If the vol expansion has already pushed `k` to 2.2 (`alpha ≈ 0.293`), the same flush leaves ~2.1% — and after three bars of expansion the baseline has travelled most of the way to the new price. The signal fades as the opportunity grows. This is the central trade-off of using an adaptive baseline in [[stretch-revert]] and it is worst in precisely the volatility-driven formulation that crypto implementations default to.

There is a compounding effect with the z-score denominator. The rolling σ of `price − baseline` and the `k` that drives the baseline both respond to volatility, so during an expansion the numerator is being suppressed while the denominator is being inflated. The z-score can *fall* through a widening real dislocation. Any VIDYA-based stretch member should log raw residual alongside z, because the two can disagree in sign of change.

**Regimes that flatter VIDYA as a baseline:**
- Balanced, low-momentum ranges (CMO form): `k → 0`, baseline near-frozen, clean stationary fade reference.
- Volatility *contraction* into a range, where the stdev ratio falls below 1 and the baseline slows exactly as the excursions get more mean-reverting.
- Assets with stable volatility profiles, where `k` hovers near 1 and VIDYA behaves as a predictable EMA.

**Regimes that expose it:**
- Volatility shocks with no directional resolution (stdev form): `k` spikes on a whipsaw, the baseline accelerates into noise, and it can end up chasing the very oscillation it should be averaging. This is VIDYA's characteristic failure and FRAMA does not share it.
- Sustained one-way trends: `k` stays elevated, the baseline tracks, and z-scores stay small — the strategy simply does not fire. Safe, but it also means the member contributes nothing during long stretches, which is why `vidya_stretch_revert` shows so few trades.
- Dead ranges in CMO form. `k ≈ 0` freezes the baseline at whatever level it last held. If the range has since shifted, every residual carries a constant bias and the z-score is measuring staleness, not stretch.

## Parameters and tuning

| Parameter | Typical | Notes |
|---|---|---|
| `n` (nominal period) | 9–21 (default 14) | Sets the ceiling on speed in the CMO form; the *realised* period is much longer |
| `k` formulation | CMO or stdev | Not a tuning knob — a design choice with opposite failure modes. Pick on reasoning, then leave it |
| `cmo_period` | 9 (range 5–20) | Shorter = twitchier `k`; below ~5 it is noise |
| `short` / `long` (stdev form) | 10 / 40 | The ratio's sensitivity. Ratios near 1:4 are conventional; 1:2 makes `k` sluggish, 1:8 makes it erratic |
| `k` clamp | none, or `[0, 1.5]` | Capping `k` in the stdev form directly limits the suppression problem above and is worth considering |
| σ window (z-score) | 50–100 bars | Keep independent of `n`, `short`, and `long` |

**Overfitting warning.** VIDYA has more genuine degrees of freedom than it appears to: a formulation choice, `n`, plus either `cmo_period` or the `short`/`long` pair, plus an optional clamp — before the strategy's own entry threshold, exit threshold, stop multiple and time stop. Sweeping the formulation *as if it were a parameter* is especially dangerous, because the CMO and stdev forms are structurally different filters and picking whichever backtested better is a two-model selection dressed up as tuning. See [[overfitting]] and [[probability-of-backtest-overfitting]]. Discipline:

- Fix the formulation on a stated rationale before any backtest, and record which one is running wherever results are quoted.
- Tune `n` on a coarse grid (9 / 14 / 21) and require a plateau.
- Leave `short`/`long` at 10/40 unless there is a specific reason; that ratio is not a source of edge.
- [[stretch-revert]] already tests fourteen estimators; a per-estimator sweep multiplies that comparison count and needs [[deflated-sharpe-ratio]] deflation before any result is believable.

## Advantages

- Directly responsive to the quantity that most obviously should govern filter speed — market activity — with a single bounded multiplier bolted onto a standard EMA.
- The CMO form is **structurally conservative**: it can only slow down, never speed up past its nominal period, which makes it a comparatively stable and sticky fair-value reference.
- Cheap and fully recursive. One `k` calculation plus one EMA update per bar; suitable for wide universes on fast loops.
- Reacts to volatility regime changes faster than [[frama|FRAMA]], which can miss a large but choppy expansion entirely.
- The `k` series is a usable standalone volatility-regime diagnostic, complementary to [[volatility-regime-classification]].
- Long-established (1992) with a documented original formulation from [[tushar-chande|Chande]] himself, unlike several later adaptive filters.

## Limitations

- **Two incompatible formulations share one name.** CMO-form and stdev-form VIDYA behave differently enough that results from one say little about the other. Most published VIDYA discussion does not specify which is meant.
- **Blind to path efficiency.** High dispersion from a clean trend and high dispersion from a violent whipsaw produce the same `k`. VIDYA can accelerate into chop.
- **`k → 0` freezes the filter** (CMO form). A frozen baseline drifts out of date and quietly biases every residual computed against it.
- Nominal period is misleading: "VIDYA(14)" typically behaves far slower than EMA(14). Like-for-like comparisons need realised `alpha`, not the label.
- The stdev form suffers the suppression problem acutely — it accelerates into exactly the volatility expansions a mean-reversion strategy wants to measure against a stationary reference.
- No independent validation. Chande's presentation is a design rationale; this vault has reviewed no study showing VIDYA beats a well-chosen fixed filter net of costs.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — closes for both the EMA recursion and the CMO / stdev computation of `k`
- `GET /api/v1/volatility/regime/{symbol}` — the API's own volatility-regime read; VIDYA's `k` is a homegrown version of the same idea and the two should broadly agree
- `GET /api/v1/quant/market` — HMM regime probabilities, for checking whether a `k` spike corresponds to a trend or to chop
- `GET /api/v1/hyperliquid/l2-book?coin=X` — spread check; on thin books a `k` spike can be book noise rather than real volatility
- `GET /api/v1/derivatives/funding-rates?coin=X` — funding extremes often coincide with the `k` spikes that most suppress the baseline

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for replaying `k` and the effective `alpha` series across cycles
- `GET /api/v1/quant/regimes/history` — hourly regime labels since 2020, for stratifying VIDYA behaviour by labelled regime

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/BTCUSDT"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [funding rates](https://cryptodataapi.com/funding-rates) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can compute and stress-test VIDYA:

- **Compute both forms side by side** — from one `GET /api/v1/hyperliquid/candles` pull, emit CMO-form and stdev-form VIDYA on the identical bars. Where the two lines diverge is where the formulation choice is doing the work, and it is the first thing to inspect before trusting either.
- **Validate `k` against the API's volatility regime** — `GET /api/v1/volatility/regime/{symbol}` is an independent read of the same underlying quantity. Persistent disagreement between a high `k` and a calm regime label means `k` is picking up microstructure, not volatility.
- **Separate trend from chop in `k` spikes** — cross `k` against `GET /api/v1/quant/market`. High `k` with high trend probability is VIDYA working as designed; high `k` with a range label is the accelerate-into-chop failure, and stretch signals from those bars deserve a much higher bar.
- **Quantify suppression** — recompute the residual against stdev-form VIDYA and a fixed EMA of matched realised period over the same bars. The residual ratio during vol expansions measures how much stretch the adaptive baseline is eating.
- **Report realised, not nominal, speed** — log mean and percentile effective `alpha` per asset. This is the only fair way to place VIDYA next to the other thirteen estimators in [[stretch-revert]]'s comparison table.

## Related

- [[frama]] — sibling adaptive filter; adapts to path roughness, blind to the volatility level VIDYA keys on
- [[kama]] — sibling adaptive filter; adapts to an efficiency ratio, which is closer to VIDYA's CMO form than to its stdev form
- [[adaptive-moving-averages]] — the family overview
- [[stretch-revert]] — the strategy family this page supports; `vidya_stretch_revert` uses this estimator
- [[tushar-chande]] — the author
- [[chande-momentum-oscillator]] — the oscillator driving `k` in the original formulation
- [[moving-averages]] · [[simple-moving-average]] · [[exponential-moving-average]] — the fixed-weight baselines VIDYA modifies
- [[volatility]] · [[standard-deviation]] · [[volatility-regime-classification]] — the quantity `k` measures
- [[mean-reversion]] · [[bollinger-bands]] · [[z-score]] — the deviation framework VIDYA feeds
- [[hurst-exponent]] · [[regime-detection]] · [[technical-structural-regime]] — regime gates that run alongside the baseline
- [[alma]] · [[hull-moving-average]] · [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] · [[jurik-moving-average]] · [[least-squares-moving-average]] · [[laguerre-filter]] · [[supersmoother-filter]] · [[theil-sen-regression]] · [[quadratic-regression]] · [[kalman-filter-trading]] — the other baseline estimators in the family
- [[overfitting]] — the parameter-tuning hazard

## Sources

- Chande, Tushar — original presentation of the Variable Index Dynamic Average, 1992. Source of the `VIDYA = alpha·k·price + (1 − alpha·k)·VIDYA[prev]` recursion with `k = |CMO|/100`.
- Chande, Tushar & Kroll, Stanley — *The New Technical Trader* (Wiley, 1994). Fuller treatment of VIDYA alongside the Chande Momentum Oscillator that supplies `k`.

The `stdev(short)/stdev(long)` formulation of `k` is a later, widely-deployed variant rather than Chande's original; it is documented here because it is what most crypto implementations run, not because it carries the same authority. No independent validation study of VIDYA has been reviewed in this vault; the lag figures on this page follow from the arithmetic of the effective smoothing constant, not from a measured backtest.

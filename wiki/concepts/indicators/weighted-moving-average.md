---
title: "Weighted Moving Average (WMA)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, crypto, mean-reversion, trend-following]
aliases: ["WMA", "Weighted Moving Average", "Linearly Weighted Moving Average", "LWMA", "Linear Weighted MA"]
related: ["[[moving-averages]]", "[[adaptive-moving-averages]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[hull-moving-average]]", "[[least-squares-moving-average]]", "[[alma]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[jurik-moving-average]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[stretch-revert]]", "[[mean-reversion]]", "[[z-score]]", "[[standard-deviation]]", "[[bollinger-bands]]", "[[keltner-channels]]", "[[hurst-exponent]]", "[[overfitting]]", "[[false-signals]]", "[[outliers]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis, indicators]
prerequisites: ["[[moving-averages]]", "[[simple-moving-average]]"]
difficulty: beginner
---

# Weighted Moving Average (WMA)

The weighted moving average assigns **linearly increasing weights** to the prices in its window: the oldest bar gets weight 1, the next gets 2, and the most recent gets *n*. It sits between the [[simple-moving-average|SMA]], which weights every bar equally, and the [[exponential-moving-average|EMA]], which decays weights geometrically over an unbounded history.

The WMA is not itself an adaptive estimator and it rarely appears as a standalone signal in modern systematic trading. It earns a page because it is a **structural building block**: the [[hull-moving-average|HMA]] is a WMA of WMAs, and the WMA is the discrete cousin of the endpoint-fitted [[least-squares-moving-average|LSMA]]. Understanding what linear weighting does to lag is the cleanest entry point to the whole [[adaptive-moving-averages|estimator taxonomy]].

## Construction

$$\text{WMA}_t = \frac{\sum_{i=1}^{n} w_i \, p_{t-n+i}}{\sum_{i=1}^{n} w_i}, \qquad w_i = i$$

The denominator is the triangular number `n(n+1)/2`, so for `n = 5` the weights are 1, 2, 3, 4, 5 over a divisor of 15 — the newest bar carries a third of the total weight, the oldest carries one fifteenth.

```python
def wma(close, period=20):
    """Linearly weighted moving average. Newest bar gets weight `period`."""
    w = list(range(1, period + 1))          # [1, 2, ..., n]
    denom = period * (period + 1) / 2       # triangular number
    out = [None] * len(close)

    for t in range(period - 1, len(close)):
        window = close[t - period + 1 : t + 1]
        out[t] = sum(wi * p for wi, p in zip(w, window)) / denom
    return out
```

Two properties follow immediately from the finite triangular kernel:

- **The window is hard-bounded.** Unlike the EMA, a price drops out of the WMA entirely once it is `n` bars old. There is no tail.
- **The weights are fixed.** Nothing varies with market state, which puts the WMA in the weighted / lag-cancelling group of the [[adaptive-moving-averages|estimator taxonomy]] — weighted, not adaptive.

## The lag result

The useful fact about the WMA is its **centre of mass**, which is where the effective lag comes from.

For any finite-weight average, the effective lag on a constant-slope input is the weighted mean of the bar offsets:

$$\text{lag} = \frac{\sum_i w_i \cdot (\text{age}_i)}{\sum_i w_i}$$

- **SMA** — equal weights, so the centre of mass sits at the midpoint of the window: $$\text{lag}_{SMA} = \frac{n-1}{2}$$
- **WMA** — linear weights pull the centre of mass toward the recent end. Evaluating the triangular kernel gives: $$\text{lag}_{WMA} = \frac{n-1}{3}$$

So a WMA(30) sits about 9.7 bars behind a linear trend where an SMA(30) sits about 14.5 — **a one-third reduction in lag for the same window length**, obtained by nothing more than rearranging the weights.

| Estimator | Weight profile | Effective lag (constant slope) | WMA(n) equivalent |
|---|---|---|---|
| [[simple-moving-average\|SMA]](n) | Flat | `(n−1)/2` | WMA of ~1.5n |
| **WMA(n)** | Linear ramp | **`(n−1)/3`** | — |
| [[exponential-moving-average\|EMA]](n) | Geometric decay | ~`(n−1)/2` | roughly SMA-like |
| [[least-squares-moving-average\|LSMA]](n) | OLS endpoint | ~0 on a linear path | — |

Two caveats worth stating, because the `(n−1)/3` figure is often quoted as though it were universal:

1. **It holds for a constant slope.** Under acceleration or at a pivot, all of these estimators behave differently and the single-number lag characterisation stops applying. This is the same caveat that makes [[triple-exponential-moving-average|TEMA]]'s "zero lag" claim conditional.
2. **Less lag is not free.** Concentrating weight on fewer effective bars means averaging over less data, so the WMA is noisier than an SMA of the same period. It sits slightly further along the lag-versus-noise frontier, not off it. There is no estimator on this page or in the [[adaptive-moving-averages|taxonomy]] that escapes that frontier.

## Comparison to SMA and EMA

| | [[simple-moving-average\|SMA]] | **WMA** | [[exponential-moving-average\|EMA]] |
|---|---|---|---|
| Weights | Equal | Linear ramp (1…n) | Geometric decay |
| Window | Finite, hard cut | Finite, hard cut | **Infinite** — old data never fully leaves |
| Lag (constant slope) | `(n−1)/2` | `(n−1)/3` | ~`(n−1)/2` |
| Noise | Lowest of the three | Moderate | Moderate |
| Recursive? | No | No | **Yes** — O(1) update |
| Cost per bar | O(n), or O(1) incremental | O(n) | O(1) |
| Response to a dropped bar | Small step | Small step | Smooth, no step |

The behavioural differences that matter in practice:

- **The drop-off artifact.** Both the SMA and the WMA move when a bar *leaves* the window, not only when a new one arrives. A large price exiting the back of an SMA window shifts the average by `outlier/n` with no new information involved. The WMA suffers this less at the tail — the departing bar has weight 1 of `n(n+1)/2` — which is a genuine, under-appreciated advantage. The EMA has no such artifact at all, since nothing ever fully leaves.
- **[[outliers]].** All three have a 0% breakdown point. But the WMA's linear ramp means a bad print does the most damage when it is *fresh*, at weight `n`, and fades quickly. An SMA spreads the same damage evenly across `n` bars. Neither is robust; see [[theil-sen-regression]] for what actually is.
- **Compute.** The EMA is recursive and updates in O(1) with a single stored value. The WMA needs the full window each bar. On a 40-coin universe this is a negligible cost compared to something like Theil-Sen's O(n²), but it is not free and it needs a full window of warm-up before the output is valid.

The WMA is rarely the right final answer on its own. It is a mild improvement over the SMA on lag, a mild degradation on noise, and it lacks the EMA's computational convenience. Its importance is what gets built on top of it.

## What builds on the WMA

**[[hull-moving-average|HMA]] — a WMA of WMAs.** Alan Hull's construction is the most direct consumer:

$$\text{HMA}(n) = \text{WMA}\Big(\,2 \cdot \text{WMA}(n/2) - \text{WMA}(n),\ \sqrt{n}\,\Big)$$

The inner term `2·WMA(n/2) − WMA(n)` is a **lag-cancelling difference**: taking twice a fast WMA minus a slow one subtracts out the linear-lag component, leaving something that tracks a constant slope with near-zero delay. The outer `WMA(√n)` re-smooths the noisy result. The whole thing is three WMAs, and its behaviour — very low lag, visually smooth, and **overshooting at pivots** — is a direct consequence of the linear-weight structure examined above. The overshoot is not a flaw in the implementation; extrapolating a recent slope is exactly what the difference term does.

**[[least-squares-moving-average|LSMA]] — the continuous analogue.** An OLS line fitted over the window and read at the endpoint produces a weighting of the window's prices that is also linear-ish in structure, but with *negative* weights at the far end — the fit is allowed to lean against old data to set the slope. That is what buys the LSMA its ~zero lag on a linear path, and what makes it more aggressive and less stable than the WMA. The WMA is the "all weights positive" version of the same intuition, and is correspondingly tamer.

**[[alma|ALMA]]** replaces the linear ramp with a Gaussian kernel whose peak is offset toward the newest bar — the same "shift the centre of mass forward" idea with the shift exposed as an explicit parameter rather than fixed by the weight formula.

**Volume-weighted variants** substitute traded volume for the positional weights. Despite the shared name these are a different estimator answering a different question (where did trading actually occur) and their properties do not follow from anything on this page.

## Use as a mean-reversion baseline

In [[stretch-revert]] terms, a WMA baseline gives a residual `close − WMA` that is then standardised into a [[z-score]] and faded. The WMA's position in that design space:

**What it offers.** Less lag than the SMA, so a stretch registers earlier and the fade has a longer runway before the move exhausts. No overshoot, so it does not manufacture apparent stretch at pivots the way [[hull-moving-average|HMA]], [[triple-exponential-moving-average|TEMA]], and [[quadratic-regression]] do — a real advantage for a fade strategy, whose [[false-signals]] otherwise concentrate at exactly the bars it trades. And it is simple: one parameter, no folklore constants, fully transparent, trivially reproducible between a backtest and a live implementation.

**What it does not offer.** The residual has **no principled scale**. Like every averaging estimator, the WMA produces a number, and price's distance from that number mixes genuine displacement with the smoother's mechanical lag. The σ used to standardise it is a rolling [[standard-deviation]] of a quantity with no defined null distribution — the threshold is convention. Only the regression group ([[least-squares-moving-average|LSMA]], [[theil-sen-regression|Theil-Sen]], [[quadratic-regression]]) gives the z-score a denominator that means something in the model's own terms; see [[z-score#Why the regression baselines are different]].

It is also **not robust**, **not adaptive**, and — critically — **not a regime filter**. No baseline tells you whether reverting is the right model. That remains the [[hurst-exponent]] gate's job, and in [[stretch-revert]] it is mandatory rather than advisory.

**Where the WMA is genuinely the right choice:** as a control. Per [[moving-averages]], the simple filter should be tested before reaching for adaptive variants, which add parameters and [[overfitting]] surface. The WMA is the cheapest possible step up from an SMA — one weighting change, no new parameters — and if a complicated estimator cannot beat a WMA baseline on out-of-sample data, the complication is not earning its keep.

## Parameters

| Parameter | Typical | Effect |
|---|---|---|
| `period` (n) | 10–50 bars | The only structural parameter. Lag is `(n−1)/3`; noise falls with n |
| Price input | close | HL2 or HLC3 reduce close-print noise on thin books, at the cost of comparability with published values |
| Scale window (if z-scored) | 50–200 bars | A **separate** parameter from `period` and an independent source of fit; see [[z-score]] |

The WMA's headline virtue is that this table is short. An SMA has one knob and a WMA has one knob; [[jurik-moving-average|JMA]] has three, [[frama|FRAMA]] has several plus alpha bounds. Every added knob multiplies the search space and the best cell of any grid looks good on any history.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the closes the weighted sum is computed over; the WMA is non-recursive so it needs a **full** `period` window before the first valid output, and a partially-filled window silently returns a wrong value rather than an error
- `GET /api/v1/hyperliquid/l2-book?coin=X` — the WMA is noisier than an SMA of the same period, so on wide-spread alt books a larger share of the measured stretch is spread rather than displacement

**Historical data:**
- `GET /api/v1/backtesting/klines` — kline archive for measuring the WMA's actual lag against realised price on your own instrument, rather than assuming the `(n−1)/3` constant-slope figure holds
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels, for checking whether the WMA's mild lag advantage over the SMA survives regime stratification or was a single-regime artifact

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] should treat the WMA primarily as a control rather than a candidate:

- **Use it as the null.** Whenever comparing exotic estimators, include WMA and SMA baselines computed on the same `GET /api/v1/hyperliquid/candles` pull. An agent that reports only the adaptive estimators has removed the null hypothesis from its own experiment.
- **Verify the lag empirically, do not assume it.** `(n−1)/3` is a constant-slope result. Measure the realised offset between WMA and price on `GET /api/v1/backtesting/klines` for the specific coin and interval; on choppy alt data it will not match the formula.
- **Warm up the window explicitly.** Pull at least 2× `period` and discard the first `period − 1` outputs. Unlike a recursive EMA, a WMA on a short pull produces a plausible-looking number from an incomplete window — a silent error that survives into backtests.
- **Decompose the HMA when debugging it.** [[hull-moving-average|HMA]] is three WMAs; when its output looks wrong, plot `WMA(n/2)`, `WMA(n)`, and the lag-cancelling difference separately. Overshoot at pivots is expected behaviour from the difference term, not a bug to fix.
- **Report the WMA-versus-SMA endpoint gap in basis points.** If the two agree to within a few bps on a given coin, the weighting choice is not the variable that matters there, and effort belongs on the regime gate or the scale estimator instead.

## Related

- [[moving-averages]] — the parent page; SMA, EMA, and WMA as the classic trio
- [[adaptive-moving-averages]] — the four-group taxonomy the WMA anchors group 1
- [[simple-moving-average]] — equal weights, `(n−1)/2` lag, the direct comparison
- [[exponential-moving-average]] — geometric weights, infinite window, recursive
- [[hull-moving-average]] — a WMA of WMAs; the WMA's most important consumer
- [[least-squares-moving-average]] — the endpoint-fitted continuous analogue
- [[alma]] — Gaussian weights with the offset exposed as a parameter
- [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] — the other lag-cancelling designs, both with more overshoot
- [[theil-sen-regression]] · [[quadratic-regression]] — the regression baselines, whose residuals have a defined scale
- [[frama]] · [[vidya]] · [[kama]] · [[laguerre-filter]] · [[supersmoother-filter]] · [[jurik-moving-average]] — the adaptive and filter groups
- [[stretch-revert]] — the strategy family; a WMA baseline is the simple control the exotic members must beat
- [[z-score]] · [[standard-deviation]] — how the residual becomes a signal, and why an averaging baseline gives it no principled scale
- [[bollinger-bands]] · [[keltner-channels]] — bands built around a baseline
- [[mean-reversion]] — the trade
- [[hurst-exponent]] — the regime gate no baseline substitutes for
- [[outliers]] — the 0% breakdown point shared with the SMA and EMA
- [[overfitting]] · [[false-signals]] — why a one-parameter estimator is worth keeping in the comparison set

## Sources

- Murphy, John J. *Technical Analysis of the Financial Markets* — covers the SMA, EMA, and WMA as the standard trio; see the vault's [[moving-averages]] page, which draws on it.
- Hull, Alan (2005) — the Hull Moving Average, defined as `WMA(2·WMA(n/2) − WMA(n), √n)`; the WMA is its sole component.
- Legoux, Arnaud and Kouzis-Loukas, Dimitrios (2009) — ALMA, the Gaussian-kernel generalisation of the "shift the centre of mass toward recent bars" idea.
- The `(n−1)/3` effective-lag figure follows directly from the centre of mass of a triangular kernel and is a standard result in filter design; it is a constant-slope characterisation and does not hold at pivots or under acceleration.
- The "test the simple filter first" framing and the caution that adaptive variants add overfitting surface are drawn from the vault's [[moving-averages]] page.
- No vault source-summary page covers the WMA specifically. No backtest comparing WMA and SMA baselines on crypto perpetuals exists in this vault; the claims about its suitability as a reversion baseline are analytical, not measured.

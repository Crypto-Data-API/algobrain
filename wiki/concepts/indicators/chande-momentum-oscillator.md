---
title: "Chande Momentum Oscillator (CMO)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, momentum, quantitative, crypto]
aliases: ["CMO", "Chande Momentum Oscillator", "Chande Momentum"]
related: ["[[tushar-chande]]", "[[vidya]]", "[[rsi]]", "[[stochrsi]]", "[[momentum-(indicator)]]", "[[stochastic-oscillator]]", "[[adaptive-indicators]]", "[[adaptive-moving-averages]]", "[[stretch-revert]]", "[[mean-reversion]]", "[[moving-averages]]", "[[exponential-moving-average]]", "[[simple-moving-average]]", "[[aroon]]", "[[frama]]", "[[kama]]", "[[alma]]", "[[hull-moving-average]]", "[[jurik-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[least-squares-moving-average]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[kalman-filter-trading]]", "[[z-score]]", "[[standard-deviation]]", "[[hurst-exponent]]", "[[overfitting]]", "[[false-signals]]", "[[contrarian-extremes]]", "[[volatility]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis, indicators]
prerequisites: ["[[momentum-(indicator)]]", "[[rsi]]"]
difficulty: intermediate
---

# Chande Momentum Oscillator (CMO)

The Chande Momentum Oscillator is a bounded pure-momentum indicator built from the raw sums of up-moves and down-moves over a lookback window. Created by [[tushar-chande|Tushar Chande]] and presented in Chande & Kroll, *The New Technical Trader* (Wiley, 1994), it was designed as a more direct and more responsive alternative to [[rsi|RSI]] — no smoothing, and both up and down momentum appearing in the numerator rather than only in the ratio.

In this vault CMO matters for two reasons. It is a legible overbought/oversold read in its own right, and — more importantly — it is the `k` term in the original formulation of [[vidya|VIDYA]], one of the fourteen baselines in [[stretch-revert]]. You cannot understand what VIDYA is adapting to without understanding CMO.

## Formula

Over `n` periods, let `SU` be the sum of all up-day price changes and `SD` the sum of the absolute values of all down-day changes:

```
CMO = 100 × (SU − SD) / (SU + SD)
```

```python
def cmo(close, n=9):
    """Chande Momentum Oscillator. Range [-100, +100]."""
    out = [None] * len(close)
    for t in range(n, len(close)):
        su = sum(max(close[i] - close[i-1], 0) for i in range(t - n + 1, t + 1))
        sd = sum(max(close[i-1] - close[i], 0) for i in range(t - n + 1, t + 1))
        out[t] = 100.0 * (su - sd) / (su + sd) if (su + sd) else 0.0
    return out
```

The range is **−100 to +100**, and the bounds are attainable rather than asymptotic:

- **CMO = +100** — every bar in the window closed up. `SD = 0`, so the ratio is exactly 1.
- **CMO = 0** — up-moves and down-moves are equal in *total magnitude*. Note this is a magnitude balance, not a count balance: nine small up-bars and one large down-bar of equal aggregate size read zero.
- **CMO = −100** — every bar closed down.

Chande's typical lookback was 9 or 20 periods; 14 is also common by analogy with RSI. Shorter windows make the reading twitchier and drive it to the extremes more often.

## How it differs from RSI

The two indicators are built from the same raw material — up-move and down-move sums — and differ in three ways that between them account for all of CMO's behaviour.

| | [[rsi\|RSI]] | CMO |
|---|---|---|
| Smoothing | Wilder smoothing (an EMA with `alpha = 1/n`) on the up/down averages | **None** — raw sums over the window |
| Numerator | Up-average only, via `100 − 100/(1 + AU/AD)` | **Both** up and down: `SU − SD` |
| Range | 0 to 100, centred at 50 | **−100 to +100, centred at 0** |
| Extremes | Reached rarely; the smoothing resists them | Reached often, and the bounds are attainable |
| Character | Damped, slower to turn | Sharper, swings harder |

**Unsmoothed.** RSI's Wilder smoothing gives every past bar a decaying influence that persists well beyond the nominal lookback. CMO uses a flat window that drops bars entirely when they age out. A single large bar therefore enters CMO at full weight and leaves abruptly, producing sharper moves and occasional discontinuities that RSI's exponential tail smooths away.

**Both directions in the numerator.** RSI's numerator is effectively driven by the up-average; the down-average enters through the ratio. CMO differences them directly, which is what makes zero the natural centre and makes the oscillator symmetric about it. This is a genuine interpretive improvement — a CMO of −40 and +40 are exactly mirrored states, whereas RSI's 30 and 70 are mirrored only by convention.

**Consequence: it reaches extremes more often.** Because it is unsmoothed and centred, CMO spends more time near its bounds than RSI spends near 30/70. That is by design, and it is a double-edged property. It flags momentum extremes earlier, and it flags a great many more of them — a straightforward source of [[false-signals]] if the readings are traded naively.

## Reading it

**As an overbought/oversold gauge.** Conventional thresholds are ±50, with ±70 or ±100 as stronger readings. Chande's own framing treats readings near +50 and above as strong upside momentum and −50 and below as strong downside.

The standard, essential caveat applies with more force than it does to RSI: **an extreme momentum reading is not a reversal signal.** CMO at +80 says the last `n` bars were overwhelmingly up. In a genuine trend that condition persists — CMO can pin near +100 for extended stretches while price keeps going. Fading it is walking the bands with a different indicator, and it is the same failure mode [[stretch-revert]] gates against with [[hurst-exponent]]. See [[contrarian-extremes]] for the general form of the argument.

**As a trend-strength gauge.** `|CMO|` near 100 means near-unanimous directional agreement in the window; near 0 means a balanced, directionless market. Used this way — magnitude only, sign discarded — it is a chop/trend classifier rather than a reversal signal, and this is much closer to how it earns its keep. It is exactly the reading VIDYA uses.

**Zero-line and signal-line crosses.** Crossing zero marks a shift in which side of the window dominates in aggregate. Some implementations overlay a moving average of CMO as a signal line, in the manner of [[macd]]. Neither is treated as authoritative here; both are common conventions rather than validated rules.

## The `k` term in VIDYA

This is the reason CMO is a prerequisite for the [[stretch-revert]] estimator cluster.

[[tushar-chande|Chande]] introduced VIDYA in 1992 as an [[exponential-moving-average|EMA]] whose smoothing constant varies bar by bar. The recursion is the plain EMA update with `alpha` scaled by a bounded index `k`:

```
VIDYA(t) = alpha·k·price(t) + (1 − alpha·k)·VIDYA(t−1),    alpha = 2/(n+1)
```

Chande's original `k` is CMO magnitude, rescaled to the unit interval:

```
k = |CMO(period)| / 100
```

This is a tidy piece of design and worth appreciating on its own terms. Because CMO is bounded to `[−100, +100]`, `k` is automatically bounded to `[0, 1]` — **no clamping required**, unlike the later standard-deviation formulation of `k`, which is unbounded above and routinely needs capping. The bound has a direct structural consequence: `alpha·k ≤ alpha`, so **CMO-form VIDYA is never faster than its nominal EMA, only equal or slower.** It is an EMA with a variable brake rather than a variable accelerator.

The behaviour that produces:

| Market state | `\|CMO\|` | `k` | Effective `alpha` (n=14) | Equivalent EMA |
|---|---|---|---|---|
| Strong one-way run | 85 | 0.85 | 0.113 | ~17 bars |
| Moderate trend | 50 | 0.50 | 0.067 | ~30 bars |
| Mild drift | 25 | 0.25 | 0.033 | ~60 bars |
| Balanced chop | 8 | 0.08 | 0.011 | ~187 bars |
| Perfect balance | 0 | 0.00 | 0.000 | **frozen** |

Two properties of CMO carry straight through into VIDYA and become the filter's defining characteristics:

1. **Directional-persistence sensing, not volatility sensing.** `|CMO|` is high when the window's moves *agree in direction*, regardless of their size. This makes CMO-form VIDYA closer in spirit to [[kama|KAMA]]'s efficiency ratio than to a volatility measure — a point often lost when VIDYA is described loosely as "volatility-adaptive". The widely-shipped `stdev(short)/stdev(long)` variant genuinely is volatility-adaptive; the original is not.
2. **`k → 0` freezes the filter.** In a perfectly balanced range, `SU ≈ SD`, CMO goes to zero, and `VIDYA(t) ≈ VIDYA(t−1)`. The baseline stops updating entirely. For a mean-reversion baseline this is arguably desirable — a stationary fair-value reference against which every excursion registers at full size — but a frozen baseline is not the same as a smooth one. It can sit at a stale level for many bars, and if the range has since shifted, every residual computed against it carries a constant bias.

See [[vidya]] for the full treatment of both formulations and their opposite failure modes.

## Parameters and tuning

| Parameter | Typical | Notes |
|---|---|---|
| `n` (lookback) | 9 (Chande's default), also 14 or 20 | Below ~5 the reading is dominated by single bars; above ~20 it stops resolving anything within a short trade horizon |
| Overbought / oversold | ±50, sometimes ±70 | Conventions, not validated levels. CMO hits them far more often than RSI hits 30/70 |
| Input series | close | High/low or typical-price variants exist and shift the reading slightly |
| Signal line | none, or a 9-period MA of CMO | A convention borrowed from [[macd]]; no independent validation here |
| Use in [[vidya]] | `cmo_period = 9` | Shorter makes `k` twitchier and the baseline's speed jumpier |

**Overfitting warning.** CMO's threshold levels are the obvious tuning target and the most dangerous one. A ±50 rule and a ±62 rule will produce visibly different equity curves on any fixed history, and the difference is almost entirely sample-specific. Because CMO reaches extremes frequently, threshold sweeps generate many trades and therefore very confident-looking, very overfitted results. Combine that with a lookback sweep and you have a two-dimensional grid whose best cell means nothing without deflation — see [[overfitting]]. When CMO is used inside [[vidya]], its period is *also* a VIDYA parameter, compounding the estimator's own surface; [[stretch-revert]] already runs fourteen estimators, and per-estimator sweeps multiply that comparison count.

## Advantages

- **Symmetric and centred at zero**, so positive and negative readings are directly comparable — cleaner than RSI's 0–100 scale with a 50 midpoint.
- **Bounded to `[−100, +100]` with attainable bounds**, which makes it directly usable as a normalised scaler; this is precisely why it works as VIDYA's `k`.
- **Unsmoothed**, so it responds to the window's actual content without an exponential tail from bars that aged out long ago.
- **Cheap** — two rolling sums per bar, trivially computed across a wide universe on fast loops.
- **`|CMO|` is a usable standalone chop/trend diagnostic**, complementary to [[kama|KAMA]]'s efficiency ratio and [[frama|FRAMA]]'s fractal-dimension estimate.
- Long-established with a documented original formulation from [[tushar-chande|Chande]] himself, and shipped by default on most charting platforms.

## Limitations

- **Reaches extremes frequently**, so an "overbought" reading carries far less information than the same word implies on RSI. Traded naively it is a [[false-signals|false-signal]] generator.
- **Pins at the bounds in trends.** CMO can sit near ±100 for long stretches while price continues. It is a momentum measure, not a reversal signal, and nothing about the bounded range changes that.
- **Discontinuous window edge.** Bars leave the flat window abruptly, so a single large bar aging out can move the reading sharply for reasons unrelated to current price action.
- **Magnitude balance, not count balance.** CMO = 0 does not mean equal numbers of up and down bars; one large move can offset many small opposite ones. This surprises people who read it as a breadth measure.
- **Zero denominator on a stalled book.** If `SU + SD = 0` — an illiquid market with no change across the whole window — the ratio is undefined and implementations must guard it. In [[vidya]] this is the same condition that freezes the filter.
- **Threshold levels are conventions.** ±50 has no derivation behind it, and this vault has reviewed no study establishing that CMO thresholds carry edge net of costs.
- **No independent validation reviewed here.** Chande's presentation is a design rationale.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the closes the `SU`/`SD` sums are built from; pull well beyond `n` so the rolling window is fully warmed
- `GET /api/v1/quant/market` — HMM regime probabilities; the check that separates a pinned CMO in a real trend from a pinned CMO in noise
- `GET /api/v1/volatility/regime/{symbol}` — volatility state, which CMO is structurally blind to since it is a directional-agreement measure, not a dispersion measure
- `GET /api/v1/hyperliquid/l2-book?coin=X` — on thin books, much of what `SU` and `SD` accumulate is [[bid-ask-spread|spread]] bounce rather than price movement

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for measuring how often CMO actually pins at the bounds per asset, and for how long
- `GET /api/v1/quant/regimes/history` — hourly regime labels since 2020, for scoring extreme CMO readings only inside range-labelled states

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can compute CMO trivially; the useful work is calibrating it:

- **Measure the pinning rate per asset before trusting any threshold.** From `GET /api/v1/backtesting/klines`, report what fraction of bars sit beyond ±50 and ±70, and the distribution of consecutive-bar runs at those levels. On a trending alt this can be a large share of all bars, which tells you immediately that "overbought" is not actionable there.
- **Report `|CMO|` separately from signed CMO.** The magnitude is the trend/chop diagnostic and the sign is the direction call; they answer different questions and conflating them is the most common misreading of this indicator.
- **When feeding [[vidya]], log `k` and the effective `alpha`, not just CMO.** `k = |CMO|/100` and `alpha·k` are what actually move the baseline. A VIDYA line reported without its realised smoothing constant hides the only interesting thing about it.
- **Watch for the frozen-filter condition.** `|CMO| → 0` drives `k → 0` and stalls CMO-form VIDYA. Flag any run of bars where `|CMO| < 5`, because every residual computed against a frozen baseline during that stretch is measuring staleness rather than stretch.
- **Cross-check extremes against regime.** A CMO of +85 with high strong-trend probability from `GET /api/v1/quant/market` is momentum working as designed; the same reading under a range label is where a fade has any business being considered at all — and even then, only behind the [[hurst-exponent]] gate.

## Related

- [[tushar-chande]] — the author; see his entity page for the wider indicator catalogue
- [[vidya]] — the adaptive moving average whose original `k = |CMO|/100`
- [[rsi]] — the smoothed, 0-to-100 oscillator CMO was designed as an alternative to
- [[stochrsi]] · [[aroon]] · [[momentum-(indicator)]] · [[stochastic-oscillator]] — neighbouring momentum tools
- [[adaptive-indicators]] · [[adaptive-moving-averages]] — the category CMO feeds
- [[stretch-revert]] — the strategy family; `vidya_stretch_revert` is the downstream consumer
- [[kama]] — the efficiency ratio, the closest conceptual relative to `|CMO|`
- [[frama]] — the fractal-dimension route to the same chop/trend question
- [[contrarian-extremes]] · [[false-signals]] — why an extreme momentum reading is not a reversal signal
- [[hurst-exponent]] — the regime gate that must sit in front of any fade of a CMO extreme
- [[mean-reversion]] · [[z-score]] · [[standard-deviation]] — the deviation framework the family trades
- [[moving-averages]] · [[simple-moving-average]] · [[exponential-moving-average]] — the smoothing baseline VIDYA modifies
- [[alma]] · [[hull-moving-average]] · [[jurik-moving-average]] · [[laguerre-filter]] · [[supersmoother-filter]] · [[least-squares-moving-average]] · [[theil-sen-regression]] · [[quadratic-regression]] · [[kalman-filter-trading]] — sibling baselines
- [[overfitting]] — the threshold-tuning hazard

## Sources

- Chande, T. S. & Kroll, S. (1994). *The New Technical Trader: Boost Your Profit by Plugging into the Latest Indicators*. Wiley (ISBN 978-0471597803). Original presentation of the CMO, alongside StochRSI, QStick and the Dynamic Momentum Index.
- Chande, T. S. (1992). Variable Index Dynamic Average. *Technical Analysis of Stocks & Commodities*, March 1992. Source of the `k = |CMO|/100` scaling documented above.
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — vault source summary covering Chande's indicator catalogue and the CMO/RSI construction difference (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).
- [[tushar-chande]] — vault entity page, for biography and indicator dates.

No independent validation study of CMO has been reviewed in this vault. The effective-EMA figures in the VIDYA table follow from the arithmetic of `alpha·k`, not from a measured backtest, and the ±50 / ±70 threshold levels are conventions rather than tested rules.

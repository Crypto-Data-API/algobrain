---
title: "Swing High"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [indicators, technical-analysis, price-action]
aliases: ["Swing High", "Pivot High", "Local High"]
domain: [indicators]
prerequisites: ["[[price-action]]"]
difficulty: beginner
related:
  - "[[swing-low]]"
  - "[[support-and-resistance]]"
  - "[[resistance]]"
  - "[[price-action]]"
  - "[[dow-theory]]"
  - "[[trend-following]]"
  - "[[market-structure]]"
  - "[[chart-patterns]]"
  - "[[breakout-trading]]"
  - "[[head-and-shoulders]]"
  - "[[stop-loss]]"
  - "[[confluence]]"
---

# Swing High

A **swing high** (or *pivot high*) is a local price peak — a bar (or candle) whose high is greater than the highs of a defined number of bars on either side of it. Swing highs and their mirror image, [[swing-low|swing lows]], are the fundamental pivots from which traders read [[market-structure|market structure]], trends, and horizontal [[support-and-resistance|resistance]].

## How It Works

The most common definition uses a symmetric **fractal** window of `n` bars on each side:

```
bar i is a swing high if  high[i] > high[i-k]  for all k in 1..n
                     and  high[i] > high[i+k]  for all k in 1..n
```

A 2-bar swing high (`n = 2`, the Bill Williams "fractal") requires the peak bar's high to exceed the two bars before and the two bars after — meaning a swing high cannot be confirmed until `n` bars have *closed after* it. This look-ahead lag is the price paid for filtering out noise: a larger `n` produces fewer, more significant swing highs; a smaller `n` produces more, noisier ones.

Variants in common use:
- **Close-based** swing highs (use `close` instead of `high`) to ignore wicks.
- **Asymmetric** windows (more bars required on the left than the right) for earlier detection.
- **ATR- or percentage-filtered** swings (e.g., ZigZag) that require a minimum retracement before registering a new pivot, suppressing minor wiggles.

### Choosing the Window `n`

| `n` (bars each side) | Pivot count | Significance | Confirmation lag | Typical use |
|---|---|---|---|---|
| 1 | Very high | Very low (noisy) | 1 bar | Micro-structure, [[scalping]] |
| 2 (Williams fractal) | High | Low–medium | 2 bars | Intraday structure |
| 3–5 | Medium | Medium | 3–5 bars | Swing trading, trendlines |
| 10+ | Low | High (major pivots) | 10+ bars | Position trading, key [[resistance]] |

Larger `n` = fewer, more meaningful swing highs but later confirmation; smaller `n` = more, noisier pivots confirmed sooner. There is no universally correct value — it is a trade-off matched to timeframe and strategy.

## Worked Example (illustrative)

Take a 2-bar fractal (`n = 2`) on these seven consecutive daily highs:

| Bar | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| High | 41.0 | 42.5 | **44.0** | 43.2 | 42.8 | 43.5 | 42.0 |

Bar 3 (high 44.0) is a **confirmed swing high**: its high exceeds bars 1–2 (41.0, 42.5) on the left *and* bars 4–5 (43.2, 42.8) on the right. Confirmation only arrives at the close of bar 5 — the `n = 2` lag. Bar 6 (43.5) is *not* a swing high: it fails to exceed bar 3, so the structure is now a **lower high** (44.0 → 43.5), an early [[market-structure|change-of-character]] warning if a [[swing-low|lower low]] follows. A short-seller would anchor a [[stop-loss]] just above 44.0 (the confirmed swing high) and treat a close above it as invalidation.

## Trading Relevance

Swing highs are load-bearing in several ways:

- **Trend definition.** Under [[dow-theory|Dow Theory]], an uptrend is a sequence of *higher highs and higher lows*; a downtrend is *lower highs and lower lows*. The swing high is literally the "high" in that definition. A failure to make a higher swing high, followed by a lower one, is the classic signal of a trend turning down — a "change of character" in [[smart-money-concepts|market-structure]] language.
- **[[resistance|Resistance]] levels.** A prior swing high is the most natural horizontal [[support-and-resistance|resistance]] level: it marks a price where supply previously overwhelmed demand. Round-tripped swing highs become favoured [[stop-loss]] and take-profit anchors, especially at [[confluence]] with other levels.
- **Breakout triggers.** Many [[breakout-trading|breakout]] and trend-following systems enter when price closes above the most recent confirmed swing high (a "break of structure"). Donchian-channel and turtle-style systems are a generalisation of this idea.
- **Stop placement.** In a short trade, the [[stop-loss|stop]] typically sits just above the last swing high; in a long, swing highs mark logical scale-out levels.
- **Pattern construction.** Swing highs are the vertices used to draw trendlines, [[chart-patterns|chart patterns]] (double tops, [[head-and-shoulders]]), and [[elliott-wave|Elliott wave]] / [[harmonic-patterns|harmonic]] structures.

Because confirmation lags by `n` bars, traders distinguish a *provisional* swing high (price is pulling back but not yet confirmed) from a *confirmed* one, and size their reliance accordingly.

## Common Pitfalls and Risks

- **Acting before confirmation.** A "swing high" is not real until `n` bars close after it; a provisional pivot that gets exceeded was never a swing high, and trading it early invites [[false-signals]].
- **Window mismatch.** Too small an `n` floods the chart with noise pivots; too large an `n` misses the actionable turn. Match `n` to timeframe.
- **Equal/cluster highs.** When several bars share near-identical highs (a "liquidity pool"), price often sweeps just above before reversing — placing a stop *exactly* at the swing high invites [[false-signals|stop-hunting]] / [[whipsaw]]. A small buffer helps.
- **Subjectivity creep.** Eyeballing swings without a fixed rule leads to inconsistent levels; a defined `n` (or ZigZag) keeps it objective.
- **Wick vs close ambiguity.** A long upper wick can register a high-based swing that a close-based definition ignores; decide which you use and stay consistent.

## Related

- [[swing-low]] — the symmetric counterpart (local trough); mirror every rule here
- [[support-and-resistance]] / [[resistance]] — prior swing highs act as resistance
- [[dow-theory]] — higher-highs/lower-highs trend framework
- [[price-action]] — reading structure directly from bars
- [[market-structure]] — break-of-structure and change-of-character
- [[breakout-trading]] — entries triggered on swing-high breaks
- [[chart-patterns]] / [[head-and-shoulders]] — patterns built from swing pivots
- [[stop-loss]] — swing highs anchor short-trade stops
- [[confluence]] — swing highs are stronger when stacked with other levels
- [[false-signals]] — swept swing highs are a classic stop-hunt fakeout

## Sources

- Murphy, John J. *Technical Analysis of the Financial Markets* — swing points, trend structure, and Dow Theory (see [[technical-analysis-of-the-financial-markets]]).
- Williams, Bill. *Trading Chaos* — origin of the 5-bar "fractal" swing-point definition.
- Edwards, R. & Magee, J. *Technical Analysis of Stock Trends* — swing highs/lows as the basis of trendlines and patterns.
- General market knowledge; worked example above is illustrative, not from a specific ingested wiki source.

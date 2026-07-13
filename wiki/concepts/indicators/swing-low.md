---
title: "Swing Low"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [indicators, technical-analysis, price-action]
aliases: ["Swing Low", "Pivot Low", "Local Low"]
domain: [indicators]
prerequisites: ["[[price-action]]"]
difficulty: beginner
related:
  - "[[swing-high]]"
  - "[[support-and-resistance]]"
  - "[[support]]"
  - "[[price-action]]"
  - "[[dow-theory]]"
  - "[[trend-following]]"
  - "[[market-structure]]"
  - "[[chart-patterns]]"
  - "[[stop-loss]]"
  - "[[breakout-trading]]"
  - "[[confluence]]"
  - "[[head-and-shoulders]]"
---

# Swing Low

A **swing low** (or *pivot low*) is a local price trough — a bar (or candle) whose low is lower than the lows of a defined number of bars on either side of it. Swing lows and their mirror image, [[swing-high|swing highs]], are the fundamental pivots from which traders read [[market-structure|market structure]], trends, and horizontal [[support-and-resistance|support]].

## How It Works

The most common definition uses a symmetric **fractal** window of `n` bars on each side:

```
bar i is a swing low if  low[i] < low[i-k]  for all k in 1..n
                    and  low[i] < low[i+k]  for all k in 1..n
```

A 2-bar swing low (`n = 2`, the Bill Williams "fractal") requires the trough bar's low to be below the two bars before and the two bars after — so a swing low cannot be *confirmed* until `n` bars have closed after it. A larger `n` yields fewer, more significant swing lows; a smaller `n` yields more, noisier ones.

Common variants:
- **Close-based** swing lows (use `close` rather than `low`) to ignore wicks.
- **Asymmetric** windows for earlier detection at the cost of more [[false-signals|false signals]].
- **ATR- or percentage-filtered** swings (e.g., ZigZag) that require a minimum bounce before registering a pivot.

(The `n`-window trade-offs are symmetric with the [[swing-high]] page — a larger `n` gives fewer, more significant lows with later confirmation; a smaller `n` gives more, noisier lows confirmed sooner.)

### Swing Low vs Swing High (mirror summary)

| Dimension | Swing low (this page) | [[swing-high\|Swing high]] |
|---|---|---|
| Geometry | Local trough; low below `n` bars each side | Local peak; high above `n` bars each side |
| Acts as | [[support]] | [[resistance]] |
| Side of book | Demand absorbed selling | Supply overwhelmed buying |
| Trend role | The "low" in higher-low / lower-low | The "high" in higher-high / lower-high |
| Stop usage | Below it for a **long** | Above it for a **short** |
| Break of structure | Close *below* = bearish BOS | Close *above* = bullish BOS |

## Worked Example (illustrative)

A trader is long a stock in an [[trend|uptrend]]. Using a 2-bar fractal (`n = 2`), these consecutive daily lows print:

| Bar | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Low | 30.5 | 29.8 | **28.6** | 29.4 | 29.9 | 30.6 |

Bar 3 (low 28.6) is a **confirmed swing low**: its low is below bars 1–2 (30.5, 29.8) and below bars 4–5 (29.4, 29.9). Confirmation lands at the close of bar 5. The trader places the [[stop-loss|stop]] at **28.50**, just below the swing low — a close beneath it would mark a [[market-structure|lower low]] and invalidate the bullish structure. If entry was at 29.90 (bar 5 close), the structural risk is 29.90 − 28.50 = **$1.40 per share**, the natural unit for [[position-sizing|sizing the position]]. As long as each pullback prints a *higher* swing low, the [[dow-theory|uptrend structure]] is intact and the stop trails up beneath each new confirmed low.

## Trading Relevance

Swing lows carry the same structural weight as swing highs, on the demand side:

- **Trend definition.** Under [[dow-theory|Dow Theory]], an uptrend requires *higher highs and higher lows*; the swing low is the "low" in that rule. The first *lower* swing low after a run of higher lows is a primary warning that an uptrend is breaking down.
- **[[support|Support]] levels.** A prior swing low is the most natural horizontal [[support-and-resistance|support]] level — a price where demand previously absorbed selling. These become favoured entry and stop anchors, especially at [[confluence]] with other levels.
- **Stop placement.** In a long trade, the [[stop-loss|stop]] typically sits just below the most recent swing low: a break of that low invalidates the bullish structure. In a short, swing lows mark logical take-profit / scale-out levels.
- **Breakout / breakdown triggers.** Trend and [[breakout-trading|breakout]] systems short (or exit longs) when price closes below the latest confirmed swing low — a "break of structure" to the downside. Donchian-channel systems generalise this.
- **Pattern construction.** Swing lows are the vertices for ascending trendlines, double bottoms, [[head-and-shoulders]] necklines (and the troughs of an inverse H&S), and [[elliott-wave|Elliott wave]] / [[harmonic-patterns|harmonic]] counts.

As with swing highs, confirmation lags by `n` bars, so traders separate a *provisional* swing low (price is bouncing but unconfirmed) from a *confirmed* one.

## Common Pitfalls and Risks

- **Acting before confirmation.** A bounce is not a swing low until `n` bars close above it; a provisional low that is later broken was never a pivot, and front-running it produces [[false-signals]].
- **Stops sitting on equal lows.** Clusters of near-identical lows are a [[stop-loss|liquidity pool]]; price routinely spikes just below to trigger stops before reversing ([[false-signals|stop-hunting]] / [[whipsaw]]). A small buffer below the swing low mitigates this.
- **Window mismatch.** Too small an `n` = noise; too large an `n` = late, far-away stops. Match `n` to the timeframe and the strategy's risk budget.
- **Wick vs close.** A long lower wick registers a low-based swing that a close-based rule would ignore; pick one convention and apply it consistently.
- **Mistaking a deeper low for support.** The *first* lower swing low after a run of higher lows is a breakdown warning, not a dip to buy — distinguish trend continuation from [[market-structure|change of character]].

## Related

- [[swing-high]] — the symmetric counterpart (local peak); mirror every rule here
- [[support-and-resistance]] / [[support]] — prior swing lows act as support
- [[dow-theory]] — higher-lows/lower-lows trend framework
- [[price-action]] — reading structure directly from bars
- [[market-structure]] — break-of-structure and change-of-character
- [[stop-loss]] — swing lows anchor long-trade stops
- [[breakout-trading]] — breakdowns trigger on swing-low breaks
- [[confluence]] — swing lows are stronger when stacked with other levels
- [[chart-patterns]] / [[head-and-shoulders]] — patterns built from swing pivots
- [[false-signals]] — swept swing lows are a classic stop-hunt fakeout

## Sources

- Murphy, John J. *Technical Analysis of the Financial Markets* — swing points, trend structure, and Dow Theory (see [[technical-analysis-of-the-financial-markets]]).
- Williams, Bill. *Trading Chaos* — origin of the 5-bar "fractal" swing-point definition.
- Edwards, R. & Magee, J. *Technical Analysis of Stock Trends* — swing highs/lows as the basis of trendlines and patterns.
- General market knowledge; worked example above is illustrative, not from a specific ingested wiki source.

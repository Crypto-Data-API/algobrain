---
title: "Trailing Stop"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [order-types, risk-management]
aliases: ["Trailing Stop Loss", "Trailing Stop", "Chandelier Exit"]
related: ["[[stop-loss]]", "[[risk-management]]", "[[atr]]", "[[average-true-range]]", "[[position-sizing]]", "[[trend-following]]", "[[turtle-traders]]", "[[volatility]]", "[[breakout]]", "[[consolidation]]"]
domain: [risk-management]
difficulty: beginner
---

A trailing stop is a dynamic [[stop-loss]] order that automatically adjusts in the direction of a profitable trade, locking in gains while allowing the position to remain open as long as the trend continues. Unlike a fixed stop-loss, which stays at a static price, the trailing stop "trails" behind the market price by a specified distance and only moves in the favorable direction — it never moves backward.

## Overview

Trailing stops solve a core tension in trading: the desire to let winners run while still protecting accumulated profits. A fixed stop-loss set at entry protects against initial loss but does nothing to lock in gains as a trade moves favorably. A trailing stop rises (for long positions) or falls (for short positions) as the market moves in your favor, but holds firm if the market reverses, triggering an exit when the price retraces by the specified trail amount.

The concept is central to [[trend-following]] strategies and was popularized by traders like [[ed-seykota]] and the [[turtle-traders]], who used systematic trailing exits to capture large trend moves while cutting losses quickly.

## How It Works

There are several common methods for setting the trail distance:

- **Fixed dollar/point amount**: The stop trails by a set number of points or dollars (e.g., $2 below the highest price reached). Simple but does not adapt to changing [[volatility]].
- **Percentage-based**: The stop trails by a fixed percentage (e.g., 5% below the highest close). Scales with the asset's price level.
- **ATR-based**: The stop trails by a multiple of the [[atr|Average True Range]] (e.g., 2x ATR). This is the most sophisticated common approach because it adapts to the asset's current volatility — wider stops in volatile markets, tighter stops in calm markets. Chandelier exits are a well-known ATR-based trailing stop method.
- **Moving average trail**: The stop is set at a [[moving-averages|moving average]] level (e.g., the 20-day EMA). The position is held as long as price remains above the average.

When a long position's trailing stop is triggered, it becomes a market or limit sell order. The key rule is that the stop only moves in one direction — upward for longs, downward for shorts — and never retreats. This **ratchet** behaviour is what distinguishes a trailing stop from a static [[stop-loss]].

### Methods Compared

| Method | How the trail is set (long) | Adapts to [[volatility]]? | Pros | Cons |
|--------|----------------------------|---------------------------|------|------|
| Fixed point/$ | High − $X | No | Dead simple, predictable | Too tight on volatile names, too loose on quiet ones |
| Percentage | High × (1 − p%) | Partially (scales with price) | Scales across price levels | Same % may be wrong for the asset's volatility |
| [[average-true-range\|ATR]] multiple | High − (k × ATR) | Yes | Self-adjusting; the professional default | Needs ATR calc; widens after volatility spikes |
| Moving-average | Below the N-period MA | Indirectly | Rides the trend visually | Lags; gives back more on sharp reversals |
| Chandelier exit | Highest high since entry − (k × ATR, k≈3) | Yes | Anchored to the trade's *peak*, not just last bar | Wide by design; large give-back near tops |

### Worked Example — Percentage Trail (15%)

You buy a stock at **$100** and set a **15% trailing stop**.

| Event | Price | Stop (15% below the peak) |
|-------|-------|----------------------------|
| Entry | $100 | $85.00 |
| Rallies | $120 | $102.00 (new peak → stop ratchets up) |
| Rallies | $150 | $127.50 (new peak) |
| Pulls back | $135 | $127.50 (stop **holds** — never retreats) |
| Reverses | $127.50 | **Triggered** — exit ≈ $127.50 |

You captured a $27.50 gain (+27.5%) while giving back the last 15% from the $150 peak. Note the stop never moved down when price fell from $150 to $135.

### Worked Example — ATR Trail (3× ATR)

Same $100 entry. Daily [[average-true-range|ATR]] = $4, multiplier k = 3, so the trail distance is **$12**.

- Day 0: peak $100 → stop = 100 − 12 = **$88**.
- Stock climbs to $130 over several weeks; peak $130 → stop = 130 − 12 = **$118**.
- A volatility spike pushes ATR to $7; trail distance widens to $21, so from a fresh $135 peak the stop sits at **$114** — automatically giving the trade more room precisely when the market is noisier.
- Price reverses through $114 → exit. The ATR stop tolerated the larger swings instead of whipsawing out, which is the whole point of volatility-scaled trailing.

This is the **Chandelier exit** logic the [[turtle-traders|Turtle traders]] and other [[trend-following]] systems use, anchoring the stop to a multiple of N (Wilder's ATR) below the highest high since entry.

## Trading Applications

- **Trend capture**: Trailing stops are the primary exit mechanism for trend-following systems. They allow a trader to stay in a winning position through normal pullbacks while exiting when the trend genuinely reverses.
- **Profit protection**: After a position has moved significantly in your favor, a trailing stop ensures you keep a meaningful portion of gains even if a sharp reversal occurs.
- **Position management**: Some traders tighten the trail distance as profits grow — starting with a wide 3x ATR trail and narrowing to 1.5x ATR after the position is well in profit.
- **Automated discipline**: Because trailing stops are mechanical, they remove the emotional temptation to hold a winning position too long or exit too early. This is especially valuable for discretionary traders who struggle with [[behavioral-finance|behavioral biases]].

**Limitations**: Trailing stops can be triggered by normal market noise, especially if set too tight. In choppy, range-bound markets they tend to produce frequent whipsaw exits. The ATR-based approach mitigates this but does not eliminate it. Trailing stops also guarantee slippage in fast-moving markets since the exit becomes a market order once triggered.

## How Traders Use It

- **Set the trail to the asset's volatility, not a round number.** A 2–3× [[average-true-range|ATR]] trail is the standard starting point; tighten only with evidence the trend is maturing.
- **Activate after a profit cushion.** Many traders run a fixed initial [[stop-loss]] at entry and only switch to a trailing stop once the trade is up ~1R, so early noise can't knock them out of a good idea.
- **Two-stage tightening.** Start wide (e.g. 3× ATR) to ride the bulk of a [[trend-following|trend]], then narrow (e.g. 1.5× ATR) once the move is extended to protect the lion's share of gains.
- **Re-anchor after a [[consolidation]].** When a trend pauses and then resolves with a fresh [[breakout]], move the trail up to just below the new range floor.

## Common Pitfalls

- **Trailing too tight.** A stop closer than ~1× ATR gets picked off by ordinary intraday noise — you exit a healthy trend at the first pullback. This is the single most common mistake.
- **Whipsaw in ranges.** Trailing stops are a *trend* tool. Inside a [[consolidation]] they whipsaw; recognise the regime and either widen them dramatically or switch to range tactics.
- **Placing the stop on an obvious round number.** Clustered stops below $100 or below a visible swing low are a magnet for stop-runs; offset slightly.
- **Slippage and gaps.** Once triggered the order becomes a market order; in a fast move or overnight gap you can fill far below the stop level. The stop is a *trigger*, not a guaranteed exit price.
- **Mental trailing stops.** A stop you "keep in your head" relies on the [[behavioral-finance|behavioral discipline]] the order was meant to remove — defeating the purpose. Use a resting order where the venue allows it.
- **Over-tightening on a winner.** Strangling a strong position to "lock in" gains caps the very fat-tailed moves that pay for a trend-following book's losers.

## Related

- [[stop-loss]] — Fixed stop-loss orders
- [[risk-management]] — Broader risk control framework
- [[atr]] / [[average-true-range]] — Average True Range, commonly used to set trail distance
- [[position-sizing]] — Determining how much to risk per trade
- [[trend-following]] — Strategy family that relies heavily on trailing stops
- [[turtle-traders]] — Used ATR-anchored trailing exits to ride long trends
- [[consolidation]] — Re-anchor the trail after a range resolves
- [[breakout]] — Entries that trailing stops are designed to manage

## Sources

- (Source: [[book-market-wizards]]) — Multiple Market Wizards describe trailing stop methodology
- (Source: [[book-technical-analysis-of-the-financial-markets]]) — Murphy covers trailing stop techniques in trend-following context

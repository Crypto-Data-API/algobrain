---
title: "John Wick Candle"
type: concept
created: 2026-06-19
updated: 2026-06-20
status: good
tags: [technical-analysis, indicators, day-trading, behavioral-finance]
aliases: ["John Wick Candle", "Long Wick Candle", "Wick Rejection", "Liquidity Sweep Candle"]
related: ["[[arc-strategy]]", "[[liquidity-pools]]", "[[candlestick-patterns]]", "[[box-and-swing-structure]]", "[[support-and-resistance]]", "[[order-flow]]"]
domain: [technical-analysis, behavioral-finance]
difficulty: beginner
---

A **"John Wick" candle** is the informal nickname for a long-wick reversal candle — a **hammer** or **inverted hammer** with a long shadow — that appears at a key level after a directional move and signals strong rejection of price beyond that level. It is the entry trigger of the [[arc-strategy|ARC strategy]] and a widely shared idea in modern price-action trading (Source: [[2026-06-19-gap-finder-arc-strategy]]).

## Overview

The name comes from the long "wick" (shadow) of the candle. The pattern is interpreted as the footprint of aggressive order flow that pushed price into a level, met opposing liquidity, and was rejected — leaving a long tail where price probed but could not hold (Source: [[2026-06-19-gap-finder-arc-strategy]]).

The standard description: a sequence of strong candles in one direction (for example, several green candles showing aggressive buying), followed by a small candle with a **large wick**. What happens next is the signal:

- If subsequent price trades **above the wick's high**, buyers remain in control (continuation up).
- If subsequent price trades **below the wick's low**, sellers have stepped back in (reversal down) (Source: [[2026-06-19-gap-finder-arc-strategy]]).

## Anatomy

| Component | Bullish (at support) | Bearish (at resistance) |
|-----------|----------------------|--------------------------|
| Shape | Hammer (long *lower* wick) | Inverted hammer / shooting-star-like (long *upper* wick) |
| Wick meaning | Rejection of lower prices; sellers' push absorbed | Rejection of higher prices; buyers' push absorbed |
| Body | Small relative to the wick | Small relative to the wick |
| Context required | Appears *at a level* after a down move | Appears *at a level* after an up move |

The pattern is only meaningful **in context**: the same candle shape in the middle of a range carries little information. It must form at a reference level — in ARC, at the [[box-and-swing-structure|box high/low or swing high/low]] — and after a sufficient one-way move (ARC requires ~20% of the box range) (Source: [[2026-06-19-gap-finder-arc-strategy]]).

## Wick as Liquidity

The deeper explanation is microstructural. A long wick marks a price zone where **stop orders and resting liquidity clustered**, and where one side briefly overwhelmed the other before being absorbed. These zones behave as **[[liquidity-pools]]** — magnets for future price — because they represent prices where a large flow of orders was transacted and where trapped participants must later cover (Source: [[2026-06-19-gap-finder-arc-strategy]]).

This is why "liquidity pool" indicators specifically flag long-shadow zones: a sweep of stops just beyond a level produces the long wick, and the swept liquidity often becomes the fuel for the reversal back into the range. Reading the wick is therefore a proxy for reading intra-bar [[order-flow]] when full footprint data is not available.

## How to Trade It (ARC usage)

In the [[arc-strategy]], the John Wick candle is the **"Candle" step** — the final confirmation after Area and Range are established:

- **Short setup:** at a box/swing high, after price has moved ≥20% of the box range up, a long-upper-wick candle prints. Enter short; place the **stop just above the wick high**. A trade *below the wick low* confirms; a break *above the wick high* invalidates.
- **Long setup:** at a box/swing low, after a comparable down move, a long-lower-wick candle prints. Enter long; place the **stop just below the wick low**.

The "trade above the wick-high / below the wick-low" rule gives an objective continuation-vs-reversal test and a natural stop location (Source: [[2026-06-19-gap-finder-arc-strategy]]).

## Worked Example (illustrative)

The prices below are hypothetical, used only to show the read — they are not real market data.

A stock's prior session set a box high at $80.00. The next day, price rallies hard into that level: five strong green candles push from $78.00 up through $80.00, having travelled well over 20% of the box range in one un-pulled-back leg, satisfying the ARC range filter. At the level, a candle spikes to a high of $80.90 but then sells off and closes near $80.05, leaving a long **upper wick** (a roughly $0.85 shadow over a small body) — a bearish "John Wick" rejection. The wick marks where buy stops above the box high were swept and where resting sell liquidity overwhelmed the late buyers.

The trader takes a short: entry near $80.00 on the close of the wick candle, **stop just above the wick high** at, say, $81.00. The objective test now runs: if the next candles trade *below the wick's low*, sellers are confirmed in control and the trade works toward the box low; if price instead trades back *above the wick high* ($80.90), the rejection failed (buyers reclaimed the sweep) and the stop takes the trader out. The mirror setup at a box *low* — a long *lower* wick (hammer) after a qualifying down-move — is the long version, stop just below the wick low.

This worked example shows why context is everything: the identical long-upper-wick candle printed in the middle of the range, with no prior one-way move and no level, would carry almost no information.

## Relation to Classic Candlestick Patterns

The John Wick candle is a context-specific application of standard [[candlestick-patterns]]:

- **Hammer** — long lower wick at support (bullish rejection).
- **Inverted hammer / shooting star** — long upper wick at resistance (bearish rejection).
- It sits alongside compression patterns (harami, inside bars) and expansion patterns (outside/engulfing bars) in the broader candle-pattern toolkit, but differs in that its *defining feature is the wick*, read explicitly as a liquidity signature rather than as a body relationship.

## Caveats

Short-form social-media pedagogy ("five greens then a John Wick") condenses this into a heuristic and risks oversimplification (Source: [[2026-06-19-gap-finder-arc-strategy]]). A single candle should not be traded in isolation — wick signals are far more reliable when combined with level context ([[support-and-resistance]]), a prior range move, and ideally volume or order-flow confirmation. As with the [[arc-strategy]] itself, there is limited independent statistical evidence isolating the long-wick candle as a standalone edge.

## Related Concepts

- [[arc-strategy]] — the strategy this candle triggers
- [[liquidity-pools]] — the microstructural explanation for wicks
- [[box-and-swing-structure]] — the levels where John Wick candles are traded
- [[candlestick-patterns]] — the hammer / inverted-hammer family
- [[price-action]] — the broader discipline this signal belongs to
- [[engulfing-candle]] — a body-based reversal trigger that complements wick rejection
- [[harami]] / [[inside-bar]] — compression triggers that pair with wick rejection at levels
- [[breakout]] — a failed breakout (sweep) is often what produces the rejection wick
- [[support-and-resistance]] — required context for the signal
- [[order-flow]] — what the wick proxies for

## Sources

- [[2026-06-19-gap-finder-arc-strategy]] — gap-finder Perplexity deep research (2026-06-19)
- Reference video: https://www.youtube.com/watch?v=T7QN-yqryr4
- General market knowledge

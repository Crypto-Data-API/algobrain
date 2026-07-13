---
title: "Box and Swing Structure"
type: concept
created: 2026-06-19
updated: 2026-06-20
status: good
tags: [technical-analysis, day-trading, support, resistance]
aliases: ["Box and Swing", "Box High Box Low", "Swing High Swing Low", "Gap-Adjusted Box", "Four ARC Levels"]
related: ["[[arc-strategy]]", "[[support-and-resistance]]", "[[john-wick-candle]]", "[[initial-balance]]", "[[liquidity-pools]]", "[[candlestick-patterns]]"]
domain: [technical-analysis]
difficulty: intermediate
---

**Box and swing structure** is the level-construction framework at the heart of the [[arc-strategy|ARC (Area-Range-Candle) strategy]]. It reduces a chart to just **four levels** — the prior-day box high and box low, plus the nearest swing high and swing low beyond them — and treats the space between as "no man's land" to be avoided (Source: [[2026-06-19-gap-finder-arc-strategy]]).

## Overview

The premise is minimalist: rather than cluttering a chart with dozens of historical highs and lows, the trader marks only the levels where the highest institutional flow concentrated and where the best opportunities arise. Everything else is treated as noise (Source: [[2026-06-19-gap-finder-arc-strategy]]).

The four levels split into two classes:

- **Box levels** — session-specific high and low (the prior regular session, or a pre-market box on gap days).
- **Swing levels** — the *nearest prominent* high above the box and low below it, found by scanning back on the chart.

## The Four Levels

| Level | Definition | Role |
|-------|------------|------|
| **Box high** | Prior session's regular-hours high | Primary resistance / sell zone |
| **Box low** | Prior session's regular-hours low | Primary support / buy zone |
| **Swing high** | The *next* prominent high above the box high — "the very next highest price above the box high, no matter where or when it occurred" | Extended resistance / target |
| **Swing low** | The *next* prominent low below the box low | Extended support / target |

The decision rule that follows from this structure: **sell at, above, or near the box high or swing high; buy at, below, or near the box low or swing low.** Stay out of the middle "no man's land" between the box edges (Source: [[2026-06-19-gap-finder-arc-strategy]]).

## "No Man's Land"

The middle of the box is explicitly deprioritised. Inside it, price has no obvious institutional reference to react to, so signals there are treated as low-quality. Trades are taken only where price interacts with one of the four levels — analogous to how [[support-and-resistance]] traders ignore mid-range chop and focus on the edges. This is a discipline mechanism as much as an analytical one: it keeps the trader out of the most ambiguous price action.

## Gap-Adjusted Box

Markets do not always open inside the prior day's range, so the box construction adapts to gaps (Source: [[2026-06-19-gap-finder-arc-strategy]]):

- **Gap up** (open above the prior box): treat the prior box as obsolete. Draw a **new box from the pre-market high and pre-market low**, which captures where overnight/pre-market liquidity concentrated. Then find new swing levels beyond the pre-market box.
- **Gap down** (open below the prior box): mirror the logic — a fresh pre-market box, then new swings located by scanning back for the next major high/low.

The rationale is that pre-market trading forms a distinct liquidity zone, often with different participants and order flow than the prior cash session. On a gap day, the pre-market box is a better map of "where business is being done" than yesterday's stale range.

> **Edge case:** on days with extremely thin pre-market volume, the pre-market box may be unreliable — its high/low can be set by a handful of trades and may not represent meaningful liquidity.

## Finding Swing Levels

A swing level in this framework is *not* every local pivot — it is the **single closest major** high (or low) beyond the box. The trader scans left on the chart and takes the first prominent turning point encountered, which might be a multi-day high, a news spike, or a prior pivot. Prioritising the nearest major level (rather than overlaying many historical highs) keeps the chart clean and the analysis decisive.

## Worked Example (illustrative)

The figures below are hypothetical and used only to illustrate the construction — they are not real market data.

Suppose a stock's prior regular session traded between a high of $52.00 and a low of $49.00. Those become the **box high ($52.00)** and **box low ($49.00)**, a $3.00 box. Scanning left, the nearest prominent high above $52.00 is a pivot at $54.50 (the **swing high**); the nearest prominent low below $49.00 is $47.20 (the **swing low**). The chart now carries just four lines, and the $49.00–$52.00 interior is "no man's land."

The next day the stock opens flat at $50.50 (inside the box) and drifts up toward $52.00. As price tags the box high, the trader is on alert for a sell setup *at the level* — they ignore any signals that fired earlier in the no-man's-land interior. If price pushes slightly past $52.00 and then prints a long-upper-[[john-wick-candle|wick rejection candle]] (often the footprint of stops being swept just above the box high), that is the trigger; the stop sits just above the wick high, and the first target is back toward the box low / swing low.

Now a **gap-up** variant: the stock instead gaps open to $55.00, well above the prior $52.00 box high. The prior box is now stale. The trader discards it and draws a **fresh pre-market box** from the pre-market high and low (say $55.80 / $54.40), then finds new swing levels beyond that pre-market box. Trading decisions key off the pre-market box and its swings, not yesterday's irrelevant range.

## Comparison to Other Level Frameworks

| Framework | How it defines the day's zones |
|-----------|--------------------------------|
| **Box & swing (ARC)** | Prior-day box (or pre-market box on gaps) + nearest swings |
| [[initial-balance]] | First-hour high/low of the *current* session |
| Opening Range Breakout (ORB) | First N-minute high/low of the current session |
| [[volume-profile]] POC / VAH / VAL | Levels derived from where volume transacted |

Box-and-swing differs from IB and ORB in that it anchors primarily on the *prior* session and on swing structure, only switching to current-session pre-market data when a gap invalidates the prior range.

## Relevance

This structure is the "Area" step of the [[arc-strategy]]. Once the four levels are drawn, the strategy measures the box **range** (filter and target) and waits for a [[john-wick-candle|long-wick candle]] at a level for entry. The long wicks that trigger entries are often the footprint of [[liquidity-pools|stop-order liquidity]] being swept just beyond these exact levels.

## Limitations and False Signals

Box-and-swing is a discretionary level-drawing framework, and its weaknesses are those of any [[support-and-resistance]] method plus a few specific to its construction:

- **Subjective swing definition.** "The nearest *prominent* high/low" is judgment-dependent. Two traders scanning the same chart can pick different swing levels, and a level chosen too far back loses relevance while one too close is just noise.
- **Thin pre-market boxes.** On gap days, a pre-market box set by a handful of trades can be unreliable (noted above), producing levels that do not represent meaningful liquidity.
- **Stale levels in fast markets.** A trending instrument can blow through both the box and the swing in a single impulse; rigidly fading every level into a strong trend is a classic way to be repeatedly stopped out.
- **Level "magnetism" cuts both ways.** Because so many traders watch obvious prior highs/lows, price is both attracted to them *and* prone to false breaks (stop runs) just beyond them — which is exactly why the [[john-wick-candle|wick]] confirmation step exists. Trading the level touch *without* confirmation invites being caught on the wrong side of a sweep.
- **Limited independent validation.** The four-level/no-man's-land discipline is a teaching heuristic; there is little published, instrument-independent statistical evidence that it constitutes a standalone edge versus generic support/resistance trading.

## Related

- [[arc-strategy]] — the method this framework anchors
- [[support-and-resistance]] — the general concept box/swing levels specialise
- [[john-wick-candle]] — the entry trigger that fires at these levels
- [[liquidity-pools]] — why price reacts at swept levels
- [[initial-balance]] — an alternative current-session level framework
- [[breakout]] — what happens when price clears a box edge with conviction
- [[average-candle-range]] — the box range used as filter and target scale
- [[candlestick-patterns]] — confirmation patterns at the levels

## Sources

- [[2026-06-19-gap-finder-arc-strategy]] — gap-finder Perplexity deep research (2026-06-19)
- Reference video: https://www.youtube.com/watch?v=T7QN-yqryr4
- General market knowledge

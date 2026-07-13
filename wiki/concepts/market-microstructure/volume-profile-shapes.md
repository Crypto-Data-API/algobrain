---
title: "Volume Profile Shapes (D, P, b, B)"
type: concept
created: 2026-06-19
updated: 2026-06-20
status: good
tags: [market-microstructure, technical-analysis, indicators, volume, market-regime]
aliases: ["Profile Shapes", "D-Profile", "P-Profile", "b-Profile", "B-Profile", "Double Distribution", "Day Types"]
related: ["[[market-profile]]", "[[volume-profile]]", "[[value-area]]", "[[point-of-control]]", "[[volume-nodes]]", "[[short-covering]]", "[[volume-profile-trading-strategy]]"]
domain: [market-microstructure, technical-analysis]
prerequisites: ["[[volume-profile]]", "[[market-profile]]"]
difficulty: intermediate
---

**Volume profile shapes** classify the overall silhouette of a session's [[volume-profile]] (or [[market-profile]]) into a small set of archetypes — most commonly **D**, **P**, **b**, and **B (double distribution)**. The shape compresses *where volume concentrated relative to the day's range* into a single read of the day's character: balance, short-covering, long-liquidation, or a two-phase session. Recognising the shape tells a trader which family of [[volume-profile-trading-strategy|setups]] is appropriate — rotation in balance, continuation/fade in imbalance.

## Overview

A profile is a horizontal histogram of volume by price. Its silhouette depends on whether volume piled up in the middle of the range (a balanced bell), at the top (volume skewed up), at the bottom (volume skewed down), or in two separate clusters. Each silhouette maps to a story about who was in control and what is likely next.

| Shape | Silhouette | Story | Bias |
|-------|-----------|-------|------|
| **D** | Symmetric bell, fat middle, thin tails | Balance; two-sided rotation around the [[point-of-control|POC]] | Mean reversion |
| **P** | Fat top, thin lower tail | Rally then acceptance up high; short-covering / squeeze | Bullish-to-neutral |
| **b** | Fat bottom, thin upper tail | Drop then acceptance down low; long-liquidation | Bearish-to-neutral |
| **B** | Two bulges split by a low-volume gap | Two distinct phases / value shift mid-session | Two-sided, watch the gap |

## D-profile — balance

A **D-shaped** profile is roughly normal: heavy volume in the centre, thin tails top and bottom, POC near the middle. It signals a **balanced, range-bound** session where neither side took control. The auction found a fair price and rotated around it.

- **Strategy:** value-area rotation / mean reversion — fade the [[value-area-high-and-low|VAH and VAL]], target the [[point-of-control|POC]].
- **Caveat:** a D-profile is a *completed* read; an early-session normal shape can still break into a trend.

## P-profile — short-covering / squeeze

A **P-shaped** profile has its volume bulge at the **top** with a thin tail trailing **below**. Price rallied up from lower levels (the thin tail = a fast, low-volume impulse up) and then built value high. Classically this is a **short-covering** session: shorts buying to close drive the initial impulse, and the market then balances at the higher prices. (See [[short-covering]].)

- **Read:** the lower thin tail is a single-print-like fast-move zone; the upper bulge is new accepted value.
- **Strategy:** in an uptrend, the upper bulge is support to buy pullbacks into; but if the rally was purely short-covering and fresh buyers don't appear, the move can stall — confirm with [[cumulative-volume-delta|CVD]].

## b-profile — long-liquidation

A **b-shaped** profile is the mirror: volume bulge at the **bottom**, thin tail trailing **above**. Price dropped from higher levels (thin tail = fast impulse down) and built value low. Classically a **long-liquidation** session — longs selling to exit drive the drop, then the market balances lower.

- **Read:** the upper thin tail is a fast-move zone; the lower bulge is new accepted value.
- **Strategy:** in a downtrend, the lower bulge is resistance to sell rallies into; confirm whether selling is genuine initiative or just liquidation drying up.

## B-profile — double distribution

A **B-shaped** (double-distribution) profile shows **two separate volume bulges separated by a low-volume gap** ([[volume-nodes|LVN]]). It signals a session with **two phases of auctioning at different price levels** — the market accepted one area, then shifted its perception of value and built a second area elsewhere.

- **Read:** the low-volume gap between the two distributions is the critical inflection. It is a [[volume-nodes|low-volume node]] / single-print zone — price moves fast through it and it acts as support/resistance on a retest.
- **Strategy:** trade rotations *within* whichever distribution price is in; treat the gap as a fast-move barrier. A move back into the gap that fails to hold often snaps to the far distribution.

## How traders use shapes

The shape is a **regime filter** placed on top of the level-based [[volume-profile-trading-strategy]]:

1. Classify the prior session (or the developing session) as D / P / b / B.
2. **D →** expect balance; deploy rotation/fade setups around POC and value edges.
3. **P / b →** expect directional bias; favour continuation in the trend direction, fade only with confirmation.
4. **B →** treat the inter-distribution gap as the key level; rotate inside the active distribution.

The shape also frames the *next* session: a P or b day suggests the prior balance broke and value is migrating; a string of D days confirms range conditions where rotation strategies thrive.

## Worked Example (illustrative)

The following numbers are hypothetical, used only to show the reasoning — they are not drawn from any real instrument or session.

Suppose an index future opens, sells off early to make the day's low, then spends the rest of the session grinding back up and accepting value near the highs. By close, the profile shows a thin tail at the bottom (the early flush, transacted on low volume) and a fat bulge of volume across the upper third of the range — a textbook **P-profile**.

A trader reads this as a likely **short-covering / squeeze** session: the lower thin tail is a fast-move zone that will offer little support if revisited, while the upper bulge is freshly accepted value that should act as support on pullbacks. The plan for the *next* session: if price opens inside the upper bulge and holds, treat the bulge as support and look to buy dips toward the [[point-of-control|POC]] (now positioned high). If price instead falls back into the thin lower tail and cannot reclaim the bulge, the "value migration up" thesis is wrong — the squeeze had no follow-through buying, and the trader stands aside or flips to the short side. Crucially, the trader does not assume "P = short-covering" from the silhouette alone; they corroborate with [[cumulative-volume-delta|CVD]] or [[order-flow]] to confirm whether the rally was genuine initiative buying or merely shorts covering.

A **B-profile** example: imagine price builds value around one level for the morning, news hits at midday, price jumps to a higher level and builds a second cluster of volume there, leaving a low-volume gap between the two. The trader treats the gap as the inflection — they rotate inside whichever distribution price currently occupies and expect price to travel *fast* through the gap, snapping to the far distribution if it enters and fails to hold.

## Limitations and risks

- **Hindsight bias** — a profile's final shape is only known at session close; classifying mid-session is error-prone, and an "in-progress D" can morph into a P/b.
- **Folklore content** — "P = short-covering, b = long-liquidation" is a useful heuristic, not a law; the same silhouette can arise from different flow. Confirm the *cause* with [[order-flow]] / [[cumulative-volume-delta|CVD]] rather than assuming it from shape.
- **Session dependence** — shape is defined relative to a session; on 24/7 crypto an arbitrary cut produces an arbitrary shape.
- **Subjectivity** — where one trader sees a clean D another sees a developing B; the taxonomy is a guide, not a precise classifier.

## Related

- [[market-profile]] — the TPO framework these day-types originate in
- [[volume-profile]] — the histogram whose silhouette is being read
- [[value-area]] / [[point-of-control]] — levels the shape positions
- [[volume-nodes]] — the LVN gap that defines a B-profile
- [[short-covering]] — the flow behind a classic P-profile
- [[volume-profile-trading-strategy]] — shape selects which setups apply

## Sources

- Gap-finder Perplexity deep research, "Volume profile indicator as a trading strategy" (2026-06-19).
- Reference video: https://www.youtube.com/watch?v=YmygDgtoxO8
- General market knowledge.

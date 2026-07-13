---
title: "Value Area High and Low (VAH / VAL)"
type: concept
created: 2026-06-19
updated: 2026-06-20
status: good
tags: [market-microstructure, technical-analysis, indicators, volume, futures, mean-reversion, breakout]
aliases: ["VAH", "VAL", "Value Area High", "Value Area Low", "Value Area Edges", "Value Area Boundaries"]
related: ["[[value-area]]", "[[point-of-control]]", "[[volume-profile]]", "[[market-profile]]", "[[volume-nodes]]", "[[support-and-resistance]]", "[[volume-profile-shapes]]", "[[volume-profile-trading-strategy]]"]
domain: [market-microstructure, technical-analysis]
prerequisites: ["[[value-area]]", "[[point-of-control]]"]
difficulty: intermediate
---

The **Value Area High (VAH)** and **Value Area Low (VAL)** are the upper and lower boundaries of the [[value-area]] — the contiguous price band, centred on the [[point-of-control]], that contains roughly **70% of a period's traded volume** (or time, in [[market-profile]]). They define the edges of "accepted value" and behave as dynamic [[support-and-resistance]]: inside them price rotates and consolidates; beyond them the market is exploring prices it has not yet accepted.

## Overview

The [[value-area]] page covers the band as a whole and the 70% construction. This page focuses on the **two edges** specifically, because traders treat VAH and VAL as concrete, actionable levels — places to fade, to break out from, and to set stops and targets. They are the boundary between two regimes:

- **Inside the value area** → *balance*. Two-sided trade, mean-reverting rotation, POC as magnet.
- **Outside VAH / VAL** → *imbalance*. One-sided exploration, potential trend, prior edge becomes a reference.

## How the edges are derived

VAH and VAL fall directly out of the value-area construction (see [[value-area]]):

1. Start at the [[point-of-control]].
2. Accrete the higher-volume of the two adjacent price pairs, stepping outward.
3. Stop when ~70% of total volume is enclosed.
4. The highest enclosed price is the **VAH**; the lowest is the **VAL**.

Because the band grows toward whichever side has more volume, the POC is usually *not* centred between VAH and VAL — the asymmetry itself is informative (a POC sitting near the VAL with a long upper value area hints at acceptance built on the way up).

## Rotation vs breakout

The two edges drive the two core day-types of [[volume-profile-trading-strategy|profile trading]]:

| Behaviour at the edge | Interpretation | Typical play |
|-----------------------|----------------|--------------|
| Price reaches VAH/VAL and **rejects** back inside | Balance holding | Fade the edge, target [[point-of-control|POC]] then opposite edge |
| Price **accepts** beyond VAH/VAL (trades and holds outside) | Imbalance / value migration | Breakout / continuation in the break direction |
| Price opens **outside** prior VA, returns inside, holds two periods | "80% rule" setup (see [[value-area]]) | Trade across the VA to the far edge |

**Acceptance vs rejection** is the crucial distinction. A quick wick beyond VAH that snaps back is *rejection* (balance intact). Trading and building volume beyond VAH is *acceptance* — the auction has decided the old value area is too low, and a new value area will form higher. [[cumulative-volume-delta|CVD]] and the [[footprint-chart]] help tell absorption (rejection) from genuine initiative (acceptance) at the edge.

## Balance and imbalance

- **Balanced market** — successive sessions' value areas overlap heavily; VAH/VAL of one day sit near the next. Price oscillates between the edges. This favours rotation/fade strategies.
- **Imbalanced (trending) market** — value areas step in one direction (each day's VAL above the prior day's VAH in an uptrend, and vice versa). Fading the edges here is fighting the trend and is the classic way value-rotation traders blow up. Recognising the shift from overlapping to stepping value areas — i.e. value migration — is what keeps a trader on the right side.

## How traders use VAH / VAL

- **Stop placement** — stops for rotation trades go just *outside* the relevant edge; a clean break of VAL invalidates a long taken near it.
- **Targets** — the opposite edge is the natural target of a rotation; the originating edge becomes a target when a failed breakout reverses.
- **Open location** — where today opens relative to the *prior* day's VAH/VAL frames the session: inside → rotational expectation; outside and accepted → trend expectation.
- **Confluence** — a VAH/VAL that lines up with a [[volume-nodes|high-volume node]], a naked [[point-of-control|POC]], or [[vwap]] is a stronger, more defended level.

## Worked Example

The following is a qualitative, hypothetical illustration — no real prices are implied.

A trader maps the *prior* session's profile and carries forward three reference lines: the VAH, the [[point-of-control|POC]], and the VAL. Today's session opens **inside** the prior value area, which biases the read toward **balance / rotation** rather than trend.

1. **Rotation fade (balance holding).** Price rises through the session and reaches the prior **VAH**. A wick pokes just above it and snaps back inside; [[cumulative-volume-delta|CVD]] shows buying aggression being **absorbed** at the edge ([[absorption]]) rather than expanding. This is **rejection** — balance is intact. The trader fades the VAH (short), stop just *outside* the edge where a clean break would invalidate the idea, first target the POC, second target the opposite edge (VAL).

2. **Breakout (acceptance / value migration).** Instead, price trades above the VAH and *builds volume there* — successive periods hold outside and a new mini-distribution forms above the old edge. CVD expands with price. This is **acceptance**: the auction has decided the old value area was too low, and a new, higher value area is forming. Fading here would be fighting confirmed value migration — the dominant way rotation traders blow up. The trader instead treats the old VAH as new support and looks for continuation.

3. **The "80% rule."** On another day price opens *outside* the prior value area, then trades back inside and holds for two periods. By the 80% rule (see [[value-area]]) the trader expects price to traverse the full value area to the *far* edge, so a long taken on re-entry near the VAL targets the VAH.

The edge is the same line each time; whether it is a fade, a breakout, or an 80%-rule traverse depends entirely on **acceptance vs rejection**, which CVD and the [[footprint-chart]] help disambiguate.

## Limitations and risks

- **Edges are zones, not lines** — exact ticks shift with row size and session definition; treat VAH/VAL as small zones, not precise prices.
- **Regime misread** — fading edges in a trending (imbalanced) market is the dominant failure mode; the edge "should" hold under balance assumptions but does not.
- **Stop clustering** — because the edges are obvious and widely watched, stops pile up just beyond them, inviting liquidity-seeking pushes through VAH/VAL before reversal.
- **Session convention** — on 24/7 crypto, the edges depend on an arbitrary daily cut; composite or fixed-range value edges are often more reliable.

## Related

- [[value-area]] — the band these are the edges of, and the 70% construction
- [[point-of-control]] — the POC the value area is built around
- [[volume-profile]] — the histogram VAH/VAL are read from
- [[volume-nodes]] — HVNs/LVNs that often coincide with or sit beyond the edges
- [[composite-profile]] — multi-session value edges that out-rank intraday ones
- [[initial-balance]] — session edges that develop alongside the value area
- [[order-flow]] / [[cumulative-volume-delta]] — tell acceptance from rejection at the edges
- [[volume-profile-shapes]] — profile shape determines whether to fade or break the edges
- [[vwap]] — confluence anchor often near the edges
- [[liquidity]] — stops cluster just beyond the edges, inviting liquidity-seeking pushes
- [[support-and-resistance]] — VAH/VAL act as structural levels
- [[volume-profile-trading-strategy]] — rotation and breakout setups at the edges

## Sources

- Gap-finder Perplexity deep research, "Volume profile indicator as a trading strategy" (2026-06-19).
- Reference video: https://www.youtube.com/watch?v=YmygDgtoxO8
- General market knowledge.

---
title: "Absorption"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [market-microstructure, liquidity, volume, indicators]
aliases: ["absorption pattern", "passive absorption", "order flow absorption"]
domain: [market-microstructure]
prerequisites: ["[[order-flow]]", "[[order-book]]", "[[liquidity]]"]
difficulty: advanced
related: ["[[order-flow]]", "[[delta]]", "[[iceberg-orders]]", "[[footprint-charts]]", "[[market-maker]]", "[[order-book]]", "[[liquidity]]", "[[tape-reading]]"]
---

**Absorption** occurs when large passive (limit) orders absorb aggressive (market) orders at a price level without allowing price to move through it. It is one of the clearest [[order-flow]] signatures of institutional participation and reveals where significant capital is being deployed to defend a price level.

## Overview

In any market, price moves when aggressive orders consume all available resting [[liquidity]] at a price level. If aggressive sellers hit the bid and exhaust all resting buy orders at that price, the bid drops and price ticks down. Absorption is the exception: aggressive orders keep hitting the level, but price does not move because a large passive participant continues to reload or maintain resting orders that match the incoming aggression.

This creates a distinctive pattern on [[footprint-charts]]: exceptionally high volume at a single price level (or a tight cluster of 2-3 ticks) with minimal or no price displacement. The aggressive side burns through volume but makes no progress. The passive side -- typically an institution, [[market-maker]], or algorithm -- is quietly accumulating or distributing a large position.

## Types of Absorption

### Buy-Side Absorption (Bullish)

Aggressive sellers drive price down into a support zone. At the level, large passive buy limit orders absorb the selling. On the footprint chart, you see heavy volume at the bid with delta remaining negative (sellers are aggressive), yet price holds or barely moves lower. This indicates a large buyer is accumulating without chasing price, and the selling pressure will eventually exhaust. When it does, price typically reverses sharply upward because the seller pool has been drained while the buyer has built a position.

### Sell-Side Absorption (Bearish)

Aggressive buyers push price up into a resistance zone. Passive sell limit orders absorb the buying at the level. Footprint shows heavy ask volume with positive delta, but price stalls. A large seller is distributing into the buying enthusiasm. When buyers exhaust, price drops as no further buying supports the level. This commonly occurs at [[order-blocks]] from previous distribution phases or near round numbers where institutions take profits.

## How to Identify Absorption

1. **High volume, low displacement**: The most basic signal. Look for price levels on the [[footprint-charts|footprint chart]] where traded volume is 3-5x or more the average for that session, but the candle body is small or the level shows no price movement.
2. **Delta vs. price disagreement**: During buy-side absorption, delta is negative (more aggressive selling) but price is not falling. During sell-side absorption, delta is positive but price is not rising. This divergence between aggression and result is the hallmark of absorption.
3. **Repeated prints at the same price**: On the time-and-sales (tape), you see the same bid price being hit over and over with large or rapid fills. The passive order is being "reloaded" -- each time a clip fills, a new one appears. This may also indicate [[iceberg-orders]].
4. **Order book behavior**: On bookmap or depth-of-market tools, you may see a large resting order that does not deplete despite sustained aggressive flow. However, sophisticated participants often hide their orders (see [[iceberg-orders]]), so the order book alone is unreliable.

## Significance

Absorption is one of the few order flow patterns that reveals genuine institutional intent. Unlike price patterns that can be faked with relatively small capital, sustaining absorption requires committing significant capital to defend a level against real market orders. When absorption appears at a [[smart-money-concepts]] zone -- an [[order-blocks|order block]], the edge of a [[fair-value-gaps|fair value gap]], or a [[liquidity-sweeps|liquidity sweep]] terminus -- it provides high-conviction confirmation that the level will hold.

In the [[smart-money-orderflow-combo]] framework, absorption at an SMC zone is considered a primary entry trigger: the structure tells you where to look, and absorption tells you that real capital is defending that level right now.

## Related

- [[order-flow]] -- the broader discipline of analyzing market transactions
- [[delta]] -- measures net aggression; absorption creates a delta-vs-price disagreement
- [[iceberg-orders]] -- the mechanism institutions often use to execute absorption
- [[footprint-charts]] -- the primary tool for visualizing absorption
- [[market-maker]] -- market makers routinely absorb flow as part of their role
- [[order-book]] -- shows resting orders, though institutional absorption is often hidden

## Sources

This page is built from established order-flow and market-microstructure knowledge; no proprietary raw source has been ingested. General references:

- Harris, L. — *Trading and Exchanges: Market Microstructure for Practitioners* (resting liquidity, the role of passive participants, and how aggressive order flow consumes the book)
- Weis, D. & Williams, T. — Wyckoff-tradition writing on effort-versus-result, the conceptual ancestor of the absorption (high effort / low result) signal
- O'Hara, M. — *Market Microstructure Theory* (price impact of order flow and the economics of liquidity provision)

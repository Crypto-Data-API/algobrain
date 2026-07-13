---
title: "Fair Value Gaps"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [technical-analysis, market-microstructure, liquidity]
aliases: ["fair value gap", "fair-value-gap", "FVG", "imbalance"]
domain: [market-microstructure, technical-analysis]
prerequisites: ["[[smart-money-concepts]]", "[[order-flow]]"]
difficulty: intermediate
related: ["[[smart-money-concepts]]", "[[order-blocks]]", "[[liquidity]]", "[[break-of-structure]]", "[[price-action-trading]]", "[[order-flow]]"]
---

A fair value gap (FVG) is a three-candle price pattern where the wicks of the first and third candles do not overlap, leaving a gap in price that was traded through too quickly for orders to be efficiently filled on both sides. In [[smart-money-concepts]] trading, FVGs represent imbalances in the market that price tends to revisit and fill.

## How Fair Value Gaps Form

FVGs are created by aggressive, one-sided order flow. When institutional buying or selling is so strong that price moves rapidly through a range, the market does not allow sufficient time for opposing orders to fill. This leaves behind an inefficiency -- a zone where price was offered but not fully transacted.

A **bullish FVG** forms during an upward impulse: the low of candle 3 is above the high of candle 1, creating a gap between them. This gap represents unfilled sell orders and is expected to act as support when price returns. A **bearish FVG** forms during a downward impulse: the high of candle 3 is below the low of candle 1, creating a gap that represents unfilled buy orders and is expected to act as resistance.

## Key Concepts

### Consequent Encroachment

Consequent encroachment (CE) refers to the 50% level (midpoint) of a fair value gap. In [[smart-money-concepts|SMC]] methodology, this level is considered a significant reaction point. Price filling to the CE -- rather than the full FVG -- is often treated as a valid mitigation. Traders use the CE as a precision entry point, placing limit orders at the 50% fill level with stops beyond the full gap.

### Full Fill vs. Partial Fill

When price returns and trades through the entire FVG range, the gap is **fully filled** and is considered resolved -- the imbalance has been corrected. A **partial fill** occurs when price enters the FVG zone but reverses before completing it, suggesting strong demand (or supply) at that level. Some traders view partial fills as a sign of trend strength -- the market is not even willing to fully revisit the imbalance before continuing.

### Inversion

An FVG that has been fully filled can become an **inverted FVG** -- a zone that now acts as the opposite type of support/resistance. A bullish FVG, once filled, may flip to act as resistance on a retest from below. This concept adds a second layer of utility to identified gaps.

## Trading with Fair Value Gaps

FVGs serve two primary roles in SMC trading: **entry zones** and **target zones**.

**As entry zones**: after a [[break-of-structure]] establishes directional bias, traders wait for price to retrace into a FVG aligned with the trend direction. The FVG provides a logical zone for limit order placement, with the consequent encroachment as the preferred entry and the far edge of the gap as the stop-loss level. Confluence increases when the FVG overlaps with an [[order-blocks|order block]].

**As target zones**: unfilled FVGs on higher timeframes serve as draw targets. Price is expected to gravitate toward open FVGs, making them useful for setting take-profit levels. In [[smart-money-concepts|ICT methodology]], the concept of "draw on liquidity" often points to unfilled FVGs as the magnet pulling price.

## FVGs and Market Microstructure

From a [[market-microstructure]] perspective, FVGs align with the concept of price inefficiency. Efficient markets tend to revisit price levels where [[liquidity]] was thin, as [[market-maker]]s and institutional participants seek to fill orders that were left behind during rapid moves. The tendency of price to return to FVGs is consistent with the broader principle that markets move toward [[liquidity]] and away from vacuums.

However, not all FVGs are created equal. Gaps formed on higher timeframes (4H, daily, weekly) carry more significance than those on 1-minute or 5-minute charts. FVGs accompanied by high [[volume]] and strong displacement are more likely to act as meaningful support or resistance upon retest.

## Related

- [[smart-money-concepts]] -- the methodology framework where FVGs are a core tool
- [[order-blocks]] -- institutional accumulation zones that often overlap with FVGs
- [[break-of-structure]] -- the structural shift that creates the impulse forming FVGs
- [[liquidity]] -- FVGs represent zones of thin liquidity that the market seeks to rebalance
- [[order-flow]] -- real-time data that can confirm whether an FVG is being respected or violated

## Sources

- Michael J. Huddleston (ICT), *Inner Circle Trader* concepts — original popularization of fair value gaps, consequent encroachment, and "draw on liquidity" in retail smart-money methodology
- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* — the underlying microstructure principle that price revisits levels where [[liquidity]] was thin and orders were left unfilled ([[book-trading-and-exchanges]])
- General [[order-flow]] and [[price-action-trading]] practitioner literature on imbalances and inefficiency

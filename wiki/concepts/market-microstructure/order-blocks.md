---
title: "Order Blocks"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [technical-analysis, price-action, market-microstructure, swing-trading]
aliases: ["Order Blocks", "order block", "order-block", "OB", "bullish order block", "bearish order block"]
domain: [market-microstructure, technical-analysis]
prerequisites: ["[[smart-money-concepts]]", "[[supply-demand-zones]]"]
difficulty: intermediate
related: ["[[smart-money-concepts]]", "[[fair-value-gaps]]", "[[break-of-structure]]", "[[liquidity-sweeps]]", "[[supply-demand-zones]]", "[[market-structure]]", "[[order-flow]]"]
---

An order block (OB) is the last opposing candlestick before a significant impulsive price move, representing a zone where institutional players accumulated or distributed large positions. In [[smart-money-concepts]] trading, order blocks serve as high-probability supply and demand zones where price is expected to react on a retest.

## How Order Blocks Form

Institutions cannot fill large orders at a single price without moving the market against themselves. Instead, they accumulate positions gradually within a price range, leaving a footprint in the form of the last opposing candle before the impulsive move. The logic is that unfilled institutional orders remain at that price level, creating a zone where price is likely to react when it returns.

A **bullish order block** is the last bearish (down-close) candle before a strong bullish impulse that breaks structure to the upside. It marks a zone where institutional buying overwhelmed selling pressure. A **bearish order block** is the last bullish (up-close) candle before a strong bearish impulse that breaks structure to the downside, marking a distribution zone where selling overwhelmed buying.

## Identifying Valid Order Blocks

Not every opposing candle qualifies as an order block. The following criteria improve reliability:

- **Must precede a [[break-of-structure]]**: the impulsive move following the OB should break a significant swing high (bullish) or swing low (bearish), confirming institutional intent
- **Displacement**: the move away from the OB should be strong and impulsive -- large-bodied candles with minimal wicks, ideally creating a [[fair-value-gaps|fair value gap]] in the process
- **Liquidity taken**: the strongest OBs form after a [[liquidity-sweeps|liquidity sweep]], where price first takes out stops before reversing aggressively
- **Timeframe alignment**: OBs identified on higher timeframes (4H, daily) carry more significance than those on lower timeframes

## Mitigation

When price returns to an order block and reacts (bounces or reverses), the OB is said to be **mitigated** -- the remaining institutional orders at that level have been filled. A mitigated order block loses its significance and should not be expected to hold again. Unmitigated OBs -- those that price has not yet revisited -- are the zones of interest for entries.

## Trading with Order Blocks

In [[smart-money-concepts]] methodology, traders use order blocks as precision entry zones:

1. Identify a higher-timeframe directional bias using [[break-of-structure]] or [[market-structure]] analysis
2. Locate an unmitigated OB aligned with the bias (bullish OB in an uptrend, bearish OB in a downtrend)
3. Wait for price to retrace into the OB zone -- ideally overlapping with a [[fair-value-gaps|fair value gap]] for added confluence
4. Enter at or near the OB zone with a stop-loss just beyond the OB's extreme
5. Target the next [[liquidity-sweeps|liquidity pool]] or opposing OB

The overlap of an order block with a fair value gap is considered one of the highest-probability setups in SMC trading, as it combines an institutional accumulation zone with a price imbalance that the market is drawn to fill.

## Comparison with Supply and Demand Zones

Order blocks are conceptually related to [[supply-demand-zones]], but differ in specificity. Traditional supply and demand zones encompass broader price ranges where buying or selling pressure was evident. Order blocks narrow this down to a single candle (or its body/wick range), providing a more precise entry zone with tighter stop-loss placement. Critics note that this precision can be illusory, as different traders may identify different candles as the "true" OB on the same chart.

## Critical Perspective

Order blocks are a core construct of [[smart-money-concepts]] (SMC/ICT) trading, and like the rest of that framework they are **discretionary and not empirically validated** in the academic literature. The "institutional accumulation" narrative is a useful heuristic for reasoning about where resting [[liquidity]] and unfilled orders may sit, but the same zones can be described in conventional terms as prior [[supply-demand-zones]] or [[support-and-resistance]]. The well-documented weakness is **subjectivity**: different traders identify different candles as the "true" OB on the same chart, which makes rule-based backtesting difficult and invites hindsight bias. Traders should treat order blocks as one confluence factor among many, validated by [[break-of-structure]] and ideally confirmed in real time by [[order-flow]], rather than as a standalone edge.

## Related

- [[smart-money-concepts]] -- the broader methodology that uses order blocks as a core component
- [[fair-value-gaps]] -- imbalances that often form alongside order blocks during impulsive moves
- [[break-of-structure]] -- the structural confirmation that validates an order block
- [[liquidity-sweeps]] -- sweeps that often precede the formation of the strongest order blocks
- [[order-flow]] -- real-time confirmation of institutional activity at order block zones
- [[supply-demand-zones]] -- the traditional concept that order blocks refine
- [[market-structure]] -- the higher-timeframe context that sets directional bias

## Sources

- ICT (Inner Circle Trader) mentorship materials — the originating source of the order-block construct within smart-money-concepts trading.
- Concept overlaps with classical Wyckoff accumulation/distribution and Sam Seiden's supply-and-demand zone methodology; no peer-reviewed validation exists for order blocks specifically.

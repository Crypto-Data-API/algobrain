---
title: "Market Microstructure Overview"
type: index
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [market-microstructure, indicators]
aliases: ["market-microstructure-overview"]
related: ["[[market-microstructure]]", "[[order-book]]", "[[market-maker]]", "[[liquidity]]"]
---

# Market Microstructure

How markets work at the mechanical level -- order books, matching engines, market makers, and price formation.

Market microstructure is the study of how trades actually happen. Understanding [[order-book]] dynamics, the role of the [[market-maker]], and how [[liquidity]] is created and consumed gives you an edge that pure chart analysis cannot. These mechanics explain why slippage occurs, why spreads widen during volatility, and how [[price-discovery]] emerges from the continuous interaction of buyers and sellers.

This knowledge is essential for anyone building execution algorithms, running market-making bots, or simply trying to get better fills on large orders.

## Start Here

- [[market-microstructure]] -- The concept page: what the field studies and why it matters
- [[order-book]] -- How buy and sell orders are organized and matched
- [[market-maker]] -- The participants who provide liquidity and earn the spread
- [[market-making]] -- The practice: quoting, inventory risk, options market making
- [[liquidity]] -- What it is, why it matters, and how to measure it
- [[market-impact]] -- How large orders move price; the square-root law
- [[price-discovery]] -- How markets arrive at a fair price

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/concepts/market-microstructure"
WHERE type != "index"
SORT updated DESC
```

## Arbitrage Execution

- [[leg-risk]] -- The #1 operational risk in multi-leg arbitrage: one side fills, the other doesn't
- [[execution-sequencing]] -- Which leg first, order types, partial fills, unwind logic
- [[crowding-indicators]] -- How to measure strategy crowding quantitatively

## Related Strategies

- [[stop-hunting-and-liquidity-sweeps]] -- how large players exploit resting orders and trigger stop cascades

## Key Topics to Cover

- Order book mechanics
- Bid-ask spread
- Market makers and liquidity providers
- Price discovery and formation
- Matching engines
- Dark pools and alternative trading systems
- Slippage and market impact

---
title: "Basis Risk"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [commodities, futures, risk-management]
aliases: ["Basis Exposure"]
related: ["[[basis-trading]]", "[[hedging-pressure]]", "[[futures-overview]]", "[[spot-price]]", "[[cost-of-carry]]", "[[commodities]]"]
domain: risk-management
prerequisites: ["[[futures-overview]]", "[[spot-price]]"]
difficulty: intermediate
---

Basis risk is the risk that the difference between the spot price of an asset and the futures price used to hedge it (the "basis") changes unfavorably over time. The basis is defined as **Basis = Spot Price - Futures Price**, and while hedging eliminates most directional price risk, it replaces it with basis risk — the risk that the hedge does not perfectly track the underlying exposure being hedged.

## Why Basis Risk Matters

A perfect hedge would eliminate all price risk. In practice, perfect hedges are rare because the hedging instrument (a standardized futures contract) rarely matches the hedger's actual physical exposure exactly. A farmer growing corn in Iowa faces a local cash price that may diverge from the CBOT corn futures contract (which specifies delivery at approved facilities along the Illinois River). The farmer's hedge removes most of the risk of a corn price collapse, but the spread between Iowa cash corn and CBOT futures can still move against them (Source: [[2026-04-14-commodities-research-framework]]).

## Types of Basis Risk

### Locational Basis
The physical commodity is in a different location than the futures contract's delivery point. Prices at different locations diverge due to transportation costs, local supply-demand conditions, and infrastructure constraints.

**Examples:**
- WTI crude oil: Cushing, Oklahoma (futures delivery point) vs Midland, Texas (Permian Basin production point). When pipeline capacity is constrained, Midland crude trades at a steep discount to Cushing — a locational basis blow-out.
- LME metals: warehouse delivery points in Rotterdam vs actual mine output in Chile. Shipping, tariffs, and logistics create basis volatility.

### Temporal Basis
The hedge expires at a different time than the physical exposure. A producer hedging June production with a July futures contract faces basis risk from the timing mismatch between when they sell physically and when the futures contract settles.

### Quality/Grade Basis
The physical commodity differs in quality or specification from the futures contract's deliverable grade. Examples include:
- Different crude oil grades (Brent vs WTI vs Dubai) hedged against a single futures benchmark
- Different wheat classes (hard red winter vs soft red winter)
- Refined products (jet fuel) hedged with crude oil futures

### Cross-Commodity Basis
Hedging one commodity with futures on a correlated but different commodity — such as hedging jet fuel exposure with crude oil futures (the "crack spread" basis) or hedging feed costs with corn futures when the actual feed blend includes soy and other components.

## Basis Behavior

In well-functioning markets, the basis tends to converge toward zero as the futures contract approaches expiration — the spot and futures prices must meet at delivery. However, between now and expiration, the basis can widen, narrow, or flip sign:

- **Strengthening basis** (basis becomes more positive / less negative): benefits a short hedger (producer), hurts a long hedger (consumer)
- **Weakening basis** (basis becomes more negative / less positive): benefits a long hedger, hurts a short hedger

Basis risk is generally much smaller than outright price risk, which is why hedging is still worthwhile — but it is not zero, and for commercial hedgers it can represent a material P&L impact (Source: [[2026-04-14-commodities-research-framework]]).

## Managing Basis Risk

- **Location swaps**: OTC contracts that pay the difference between two delivery points, isolating and transferring locational basis risk
- **Calendar spreads**: Adjusting hedge timing to minimize temporal mismatch
- **Basis trading**: Actively trading the basis itself as a strategy (see [[basis-trading]])
- **Diversification of hedge instruments**: Using multiple contracts or OTC products to better match the physical exposure

## Related

- [[basis-trading]]
- [[hedging-pressure]]
- [[futures-overview]]
- [[spot-price]]
- [[cost-of-carry]]
- [[commodities]]
- [[crude-oil]]

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])

---
title: Backwardation
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [futures, derivatives, commodities]
aliases: [backwardated market, futures discount, normal backwardation]
domain: [market-microstructure]
prerequisites: ["[[futures]]", "[[spot-price]]", "[[contango]]"]
difficulty: intermediate
related:
  - "[[contango]]"
  - "[[spot-price]]"
  - "[[speculation]]"
  - "[[roll-yield]]"
  - "[[convenience-yield]]"
  - "[[hedging-pressure]]"
  - "[[commodity-curve-rolls]]"
---

# Backwardation

Backwardation is a market condition where the [[spot-price]] of a commodity or asset is higher than the futures price, creating a downward-sloping term structure across expiration dates. It is the inverse of [[contango]] and, in commodities, is associated with physical tightness and a positive [[roll-yield]] for long futures holders.

## Definition

Formally, a market is in backwardation when the futures price for later delivery is below the spot (or nearer-dated futures) price:

```
F(t, T2) < F(t, T1) < S    for T2 > T1 > t
```

The cost-of-carry relationship makes the source explicit. For a storable commodity:

```
F = S × e^((r + u − y) × T)
```

where `r` is the risk-free rate, `u` the storage cost, and `y` the [[convenience-yield]]. Backwardation (`F < S`) arises when the convenience yield `y` exceeds the financing-plus-storage cost `r + u` — i.e., the market pays a premium to hold the physical good *now*. Note the distinction: **backwardation** describes the observed price curve (spot > futures), while **"normal backwardation"** (Keynes) is a theory about the *expected* path, asserting futures are priced below expected future spot because producer hedgers pay speculators a [[hedging-pressure|risk premium]].

## Why Backwardation Occurs

- **Immediate supply shortage** - Strong current demand or supply disruption drives the [[spot-price]] above futures. Buyers will pay a premium for immediate delivery. Low inventory levels are the typical cause.
- **High [[convenience-yield]]** - Holding the physical [[commodities|commodity]] provides benefits (e.g., keeping production running) that outweigh [[storage-economics|storage costs]]. The Theory of Storage (Kaldor/Working/Brennan) formalizes this relationship.
- **[[hedging-pressure|Risk premium]]** - Producers hedge by selling futures at a discount, compensating speculators for taking on price risk (Keynes's theory of "normal backwardation"). This is the [[hedging-pressure]] hypothesis.

## Impact on Traders

- **Positive [[roll-yield]]** - Long futures holders benefit when rolling from expiring contracts to cheaper later-dated contracts, creating a tailwind for returns. The [[commodity-curve-rolls|Erb-Harvey anomaly]] shows that backwardated commodities historically outperform.
- **Supply signal** - Persistent backwardation often indicates tight physical [[supply-demand-balance|supply/demand balance]] and can be bullish for the underlying commodity.
- **ETF benefit** - Futures-based ETFs earn positive [[roll-yield]] in backwardation, the opposite of [[contango]] decay.

## Trading Relevance

Backwardation signals that the market values the asset more today than in the future, which is typically a bullish supply/demand indicator. Commodity traders pay close attention to the shift between [[contango]] and backwardation as a gauge of market tightness. Energy markets frequently oscillate between the two states based on OPEC decisions, inventory data, and geopolitical events.

## Opposite

The inverse condition is [[contango]], where futures trade above spot.

## Related

- [[contango]]
- [[roll-yield]]
- [[convenience-yield]]
- [[hedging-pressure]]
- [[commodity-curve-rolls]]
- [[carry-anomaly]]
- [[commodity-carry-strategy]]
- [[futures-curve-structure-analysis]]

## Sources

- Hull, J. — *Options, Futures, and Other Derivatives* (cost-of-carry, contango vs backwardation)
- Keynes, J.M. — *A Treatise on Money* (1930), origin of "normal backwardation"
- Kaldor, N. (1939) / Working, H. (1949) / Brennan, M. (1958) — the Theory of Storage and convenience yield
- Erb, C. & Harvey, C. — "The Strategic and Tactical Value of Commodity Futures" (2006), roll yield and the carry anomaly in commodities

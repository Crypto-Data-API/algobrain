---
title: "Cost of Carry"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [commodities, futures, derivatives]
aliases: ["Carrying Cost", "Carry Cost", "Cost of Carry Model", "Cost of Carry"]
related: ["[[contango]]", "[[backwardation]]", "[[convenience-yield]]", "[[storage-economics]]", "[[roll-yield]]", "[[futures-overview]]"]
domain: [market-microstructure]
prerequisites: ["[[futures-overview]]", "[[spot-price]]"]
difficulty: intermediate
---

Cost of carry is the total expense incurred by holding a physical commodity or financial asset over time, encompassing storage fees, insurance, financing costs, and any spoilage or depreciation, minus the [[convenience-yield]] of having the physical asset on hand. It is the foundational concept linking [[spot-price|spot prices]] to [[futures-overview|futures prices]] and determines the theoretical fair value of a futures contract.

## The Cost-of-Carry Model

The cost-of-carry model expresses the relationship between the spot price and the futures price as:

**F = S x e^(r + c - y)t**

Where:
- **F** = futures price
- **S** = current [[spot-price|spot price]]
- **r** = risk-free interest rate (financing cost)
- **c** = storage and insurance costs (as a continuous rate)
- **y** = [[convenience-yield]] (benefit of holding physical inventory)
- **t** = time to expiration (in years)

When `r + c > y`, futures trade at a premium to spot ([[contango]]). When `y > r + c`, futures trade at a discount to spot ([[backwardation]]). This arbitrage relationship holds tightly for financial futures (where storage costs are negligible) and approximately for physical commodities (where practical constraints limit arbitrage) (Source: [[2026-04-14-commodities-research-framework]]).

## Components of Carry Cost

### Storage and Warehousing
Physical commodities require storage — tank farms for [[crude-oil]], grain elevators for wheat, vaults for [[gold]], warehouses for metals. These costs vary widely: gold is cheap to store per unit of value, while natural gas requires expensive pressurized facilities. See [[storage-economics]] for how storage capacity and costs shape the futures curve.

### Financing
Holding a physical position ties up capital. The financing cost is the opportunity cost of that capital, typically approximated by the risk-free rate. For leveraged positions, the actual borrowing cost applies.

### Insurance
Physical commodities face risks of damage, theft, or loss. Insurance costs are a component of carry, though they are often bundled into warehouse or storage fees.

### Convenience Yield (Offset)
The [[convenience-yield]] offsets the costs above. A refiner holding crude oil inventory can respond immediately to demand spikes or supply disruptions — this optionality has real economic value. High convenience yield reduces the net cost of carry, potentially driving it negative and creating [[backwardation]].

## Fair Value and Arbitrage

The cost-of-carry model defines the fair value of a futures contract. Deviations create arbitrage opportunities:

- **Futures too expensive** (above fair value): a [[cash-and-carry]] arbitrageur buys the physical commodity, stores it, finances the position, and sells the futures contract — locking in a risk-free profit.
- **Futures too cheap** (below fair value): a reverse cash-and-carry trade — sell (or lend) the physical, buy futures — captures the mispricing.

In practice, these arbitrages are imperfect for physical commodities because storage capacity is finite, delivery logistics are complex, and [[basis-risk]] exists between the delivery specification and the actual physical commodity held (Source: [[2026-04-14-commodities-research-framework]]).

## Implications for Futures Traders

Understanding cost of carry is essential for:

- **Evaluating futures curves**: Is the curve shape justified by carry costs, or does it reflect supply-demand imbalances?
- **[[roll-yield]] estimation**: The cost of carry determines whether rolling futures positions will be a tailwind or headwind.
- **[[basis-trading]]**: Trading the spread between spot and futures requires understanding what fair carry should be.
- **Hedging costs**: For commercial hedgers, the carry structure determines the cost (or benefit) of maintaining a hedge position.

## Related

- [[contango]]
- [[backwardation]]
- [[convenience-yield]]
- [[storage-economics]]
- [[roll-yield]]
- [[basis-trading]]
- [[cash-and-carry]]
- [[basis-risk]]
- [[futures-overview]]
- [[spot-price]]

## Sources

- Hull, J. C. *Options, Futures, and Other Derivatives* (forward/futures pricing and the cost-of-carry relationship).
- Working, H. (1949). "The Theory of Price of Storage." *American Economic Review.*
- (Source: [[2026-04-14-commodities-research-framework]])

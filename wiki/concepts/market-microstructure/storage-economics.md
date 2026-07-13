---
title: "Storage Economics"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [commodities, futures, market-microstructure]
aliases: ["Storage Costs", "Physical Storage"]
related: ["[[contango]]", "[[backwardation]]", "[[cost-of-carry]]", "[[convenience-yield]]", "[[crude-oil]]", "[[natural-gas]]", "[[commodities]]"]
domain: market-microstructure
prerequisites: ["[[cost-of-carry]]", "[[contango]]"]
difficulty: intermediate
---

Storage economics describes how the costs, capacity, and logistics of physically storing commodities shape futures curve structure, basis relationships, and trading opportunities. Storage is the mechanism that links spot and futures markets — the ability (or inability) to buy a commodity today, store it, and deliver it against a futures contract is what enforces the [[cost-of-carry]] relationship between spot and forward prices.

## Storable vs Non-Storable Commodities

The storability of a commodity fundamentally determines its futures curve behavior:

- **Storable commodities** (crude oil, gold, copper, wheat, natural gas): Can be held in inventory, enabling cash-and-carry arbitrage. Their futures curves are bounded by the cost-of-carry model — [[contango]] cannot exceed storage + financing costs without triggering arbitrage.
- **Non-storable commodities** (electricity, fresh produce): Cannot be economically stored, so spot and futures prices are only loosely connected. Electricity prices can go negative during oversupply or spike 100x during peak demand with no arbitrage mechanism to smooth the curve.

The degree of storability exists on a spectrum. Gold is nearly costless to store relative to its value. [[natural-gas|Natural gas]] requires expensive pressurized caverns or LNG facilities. Livestock can be "stored" only briefly and at increasing cost (feed, care). This storability spectrum directly correlates with how well the [[cost-of-carry]] model explains each commodity's futures curve (Source: [[2026-04-14-commodities-research-framework]]).

## Components of Storage Costs

### Warehouse and Tank Fees
The direct cost of physical space — tank farms for oil, grain elevators for agriculture, LME-approved warehouses for metals. These fees can be fixed (monthly lease) or variable (per-unit-per-day).

### Insurance
Coverage against fire, flood, theft, contamination, and other risks to stored inventory. Insurance costs scale with the value and volatility of the commodity.

### Financing
Capital tied up in physical inventory has an opportunity cost. For leveraged storage plays, this is the actual borrowing cost. Even for well-capitalized firms, internal hurdle rates apply.

### Spoilage and Degradation
Some commodities deteriorate over time — grain can develop mold, crude oil can lose lighter fractions, certain chemicals degrade. These losses are an implicit storage cost.

## How Storage Capacity Shapes the Curve

Storage capacity acts as a constraint that can amplify or collapse [[contango]]:

- **Ample storage, low utilization**: Contango can persist at its full theoretical width (storage cost + financing). Arbitrageurs absorb excess near-term supply by storing it and selling forward.
- **Storage nearing capacity**: Contango collapses as the marginal storage cost rises sharply. New supply cannot be absorbed and must clear in the spot market, pushing spot prices down (or forcing distressed selling).
- **Storage completely full**: The curve can invert to [[backwardation]] even with surplus supply — there is physically nowhere to put the commodity. This creates extreme spot price dislocation.

## Case Study: 2020 Oil Storage Crisis

The most dramatic example of storage economics driving prices occurred in April 2020. COVID-19 lockdowns caused global oil demand to collapse by ~30%, but production cuts lagged. The resulting oversupply rapidly filled storage worldwide:

- Cushing, Oklahoma storage (the WTI delivery hub) approached its ~76 million barrel capacity
- Traders resorted to floating storage on tankers — at one point, over 160 million barrels of oil sat on ships at sea
- On April 20, 2020, the May WTI futures contract went **negative**, settling at -$37.63/barrel — holders were willing to pay others to take delivery because there was physically no room to store it

This event demonstrated that storage capacity is not merely a cost input but a hard physical constraint that, when breached, can produce price outcomes far outside historical norms. See [[2020-negative-oil-price]] for full details (Source: [[2026-04-14-commodities-research-framework]]).

## Storage as a Trading Signal

- **Rising storage utilization** in a commodity signals weakening fundamentals and potential contango widening
- **Falling storage** suggests tightening supply and potential backwardation — rising [[convenience-yield]]
- **Storage reports** (EIA weekly petroleum status, USDA grain stocks, LME warehouse reports) are key data releases for commodity traders
- **Seasonal storage patterns** matter — natural gas storage follows a predictable injection/withdrawal cycle that drives seasonal curve shapes

## Related

- [[contango]]
- [[backwardation]]
- [[cost-of-carry]]
- [[convenience-yield]]
- [[crude-oil]]
- [[natural-gas]]
- [[2020-negative-oil-price]]
- [[commodities]]
- [[roll-yield]]

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])

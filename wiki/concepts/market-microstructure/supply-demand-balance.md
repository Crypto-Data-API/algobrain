---
title: "Supply-Demand Balance Modeling"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [commodities, fundamental-analysis, market-microstructure]
aliases: ["S&D Balance", "Supply-Demand Model", "Commodity Balance Sheet", "Fundamental Balance", "Supply-Demand Balance Modeling"]
domain: [market-microstructure, fundamental-analysis]
difficulty: advanced
prerequisites: ["[[commodities]]", "[[inventory-cycle-analysis]]"]
related: ["[[inventory-cycle-analysis]]", "[[commodities]]", "[[eia]]", "[[usda]]", "[[capex-cycle]]", "[[commodity-super-cycle]]", "[[convenience-yield]]", "[[storage-economics]]"]
---

# Supply-Demand Balance Modeling

The core quantitative output of commodity fundamental analysis. A supply-demand (S&D) balance sheet tallies total supply against total demand for a specific commodity over a defined time period, with the residual flowing into or out of inventories. Persistent surplus (supply > demand) builds inventories and depresses prices. Persistent deficit (demand > supply) draws inventories and supports prices. Normalized excess supply models show strong inverse correlation to spot and futures prices across virtually all physical commodity markets (Source: [[2026-04-14-commodities-research-framework]]).

## Overview

Every commodity has a balance sheet, conceptually identical to a corporate income statement but expressed in physical units (barrels, tonnes, bushels). The structure is:

**Supply = Production + Imports + Inventory Draws**
**Demand = Consumption + Exports + Inventory Builds**
**Balance = Supply - Demand = Change in Inventories**

When the balance is negative (deficit), inventories draw down, and prices tend to rise as buyers compete for scarce supply. When the balance is positive (surplus), inventories build, storage fills, and prices tend to fall as sellers compete for limited demand. The relationship between the balance and price is the central mechanism of commodity fundamental-analysis (Source: [[2026-04-14-commodities-research-framework]]).

## Key Components

### Supply Side
- **Production**: mine output (metals), well output (oil/gas), harvest (agriculture), refinery throughput (products)
- **Imports**: international trade flows into the region of analysis
- **Secondary supply**: recycling (copper, aluminum, gold), refined product re-exports, strategic reserve releases

### Demand Side
- **Consumption**: industrial use, consumer use, power generation, transportation fuel
- **Exports**: international trade flows out of the region
- **Strategic/government purchases**: government stockpile builds (SPR for oil, state reserve purchases for metals/grains)

### Inventory (Stocks)
- **Reported inventories**: EIA weekly petroleum status (crude + products), LME warehouse stocks (base metals), USDA ending stocks (grains/oilseeds), SHFE warehouse stocks
- **Unreported/floating inventories**: oil in transit (floating storage), private/commercial stockpiles not captured in official data
- **Days of supply** = inventories / daily consumption rate (normalizes across different commodities)

## Stocks-to-Use Ratio

The most important normalized metric for comparing supply tightness across commodities and time periods:

**Stocks-to-Use = Ending Inventories / Annual Consumption**

Low stocks-to-use → tight market → high prices, high [[convenience-yield]], [[backwardation]].
High stocks-to-use → loose market → low prices, low convenience yield, [[contango]].

Stocks-to-use is particularly powerful in agricultural commodities where USDA publishes official estimates in the monthly [[usda|WASDE]] report. For grains, a stocks-to-use ratio below ~15% is considered critically tight and historically associated with price spikes (Source: [[2026-04-14-commodities-research-framework]]).

## Data Sources by Commodity Sector

| Sector | Primary S&D Source | Frequency | Key Metric |
|--------|-------------------|-----------|------------|
| Crude oil & products | [[eia]] STEO, IEA OMR, OPEC MOMR | Monthly | OECD commercial inventories, days of forward cover |
| Natural gas | EIA Natural Gas Weekly, NGSA | Weekly | Working gas in storage (Bcf), days of supply |
| Base metals | ICSG (copper), INSG (nickel), ILZSG (zinc/lead), IAI (aluminum) | Monthly/Quarterly | LME + SHFE warehouse stocks, refined surplus/deficit |
| Precious metals | World Gold Council, Silver Institute, GFMS | Quarterly | Above-ground stocks, mine supply vs. fabrication + investment demand |
| Grains & oilseeds | [[usda]] WASDE, USDA PSDR | Monthly | Ending stocks, stocks-to-use ratio |
| Softs (coffee, cocoa, sugar) | ICO, ICCO, ISO | Quarterly | Production surplus/deficit, certified stocks |
| Livestock | USDA WASDE, Cattle on Feed | Monthly | Herd size, placements, slaughter rates |

## Analytical Framework

### Building a Balance Sheet
1. Start with **beginning stocks** (known from previous period).
2. Add **production** estimates (from national statistics, trade bodies, or proprietary research).
3. Add **imports** (customs data, trade flow databases).
4. Subtract **consumption** (estimated from industrial production data, GDP proxies, utility data).
5. Subtract **exports**.
6. The residual = **ending stocks** = beginning stocks + production + imports - consumption - exports.
7. Compare ending stocks estimate to official reported inventories for validation.

### Interpreting the Balance
- **Size of surplus/deficit matters**: a 100,000 barrel/day deficit in a 100 million barrel/day global oil market is marginal; a 2 million barrel/day deficit is significant.
- **Trajectory matters more than level**: a market moving from surplus to deficit (even if still in small surplus) is bullish because the trend is tightening.
- **Speed of inventory change**: rapid draws signal acute tightness; slow draws signal gradual tightening.
- **Quality of supply/demand data**: production data is generally more reliable than consumption data (consumption is often estimated as a residual).

### S&D Balance and Futures Curve Shape
The balance has direct implications for the [[futures-curve-structure-analysis|futures curve]]:
- **Tight balance (deficit)** → inventory draws → high [[convenience-yield]] → [[backwardation]]
- **Loose balance (surplus)** → inventory builds → [[storage-economics|storage cost]] dominates → [[contango]]
- **Transition periods** (surplus to deficit or vice versa) often coincide with major shifts in curve shape and outright price direction (Source: [[2026-04-14-commodities-research-framework]])

## Limitations

- **Data lags**: most S&D data is published monthly with 1-2 month lags; the market may have already priced in the information.
- **Estimation uncertainty**: consumption is often the least reliable variable, estimated as a residual (production + imports - exports - inventory change).
- **Unreported inventories**: significant commodity stocks are held outside of official reporting systems (Chinese government reserves, private commercial stocks, floating storage).
- **Policy unpredictability**: government interventions (export bans, strategic reserve releases, tariffs) can override S&D fundamentals.
- **Elasticity assumptions**: models assume price elasticity of supply and demand, but short-run elasticity in commodities is very low, leading to outsized price moves for small balance changes.

## Practical Application

S&D balance modeling is used by:
- **Physical commodity trading firms** (Vitol, Trafigura, Glencore) as their primary analytical framework
- **Commodity hedge funds** (fundamental discretionary and systematic)
- **Research platforms** (Wood Mackenzie, S&P Global Platts, CRU, ICIS) which maintain proprietary S&D models
- **Government agencies** ([[eia]], [[usda]], IEA) which publish official S&D estimates

For traders, the most actionable framework is to compare the **consensus S&D estimate** (e.g., IEA forecast) against your own model. If your model shows a tighter balance than consensus, go long (and vice versa). The edge comes from having a more accurate or timelier S&D model than the market average (Source: [[2026-04-14-commodities-research-framework]]).

## Related

- [[inventory-cycle-analysis]] -- closely related; inventories are the key output variable of S&D modeling
- [[commodities]] -- market overview for all commodity sectors
- [[eia]] -- primary data source for petroleum S&D
- [[usda]] -- primary data source for agricultural S&D
- [[capex-cycle]] -- the investment cycle that drives the supply side of the balance
- [[commodity-super-cycle]] -- long-duration supply/demand imbalances
- [[convenience-yield]] -- the benefit of holding physical inventory, linked to S&D tightness
- [[futures-curve-structure-analysis]] -- curve shape reflects S&D balance
- [[commodity-momentum]] -- momentum is driven by persistent S&D imbalances
- [[commodity-carry-strategy]] -- carry reflects the curve shape driven by S&D

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])

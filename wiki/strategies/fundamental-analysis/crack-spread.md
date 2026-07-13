---
title: "Crack Spread"
type: strategy
created: 2026-04-06
updated: 2026-04-14
status: good
tags: [crack-spread, petroleum, refining-margin, commodity-spread, crude-oil, gasoline, heating-oil, energy]
aliases: ["Crack Spread Trading", "Refinery Margin Trade", "3:2:1 Crack Spread"]
strategy_type: fundamental
timeframe: swing|position
markets: [commodities]
complexity: intermediate
backtest_status: untested
related: ["[[spark-spread]]", "[[crush-spread]]", "[[seasonal-spread-trading]]", "[[basis-trading]]", "[[event-driven-trading]]", "[[crude-oil]]", "[[gasoline]]", "[[heating-oil]]", "[[eia-data]]", "[[inventory-cycle-analysis]]", "[[geopolitical-risk-premium]]", "[[commodities]]"]
---

# Crack Spread

## Overview

The crack spread represents the **refining margin** -- the profit a refinery earns by "cracking" [[crude-oil]] into refined products like [[gasoline]] and [[heating-oil]] (distillate). Trading the crack spread means going long crude oil futures and short refined product futures (or vice versa) to profit from changes in refining economics. When refining margins expand (products become expensive relative to crude), the crack spread widens. When margins compress (crude rises faster than products, or product demand falls), the spread narrows.

The name "crack" comes from the catalytic cracking process used in petroleum refining. The most common variant is the **3:2:1 crack spread**, reflecting the approximate yield of a typical refinery: 3 barrels of [[crude-oil]] produce 2 barrels of [[gasoline]] and 1 barrel of [[heating-oil]] (or diesel). Other ratios exist -- the 5:3:2 and 2:1:1 are also traded, depending on the refinery configuration and regional product mix.

Crack spreads are traded by **refiners** (as hedges to lock in processing margins), **speculators** (to profit from expected margin changes), and **macro traders** (as indicators of energy market supply/demand balance). A surging crack spread signals strong product demand relative to crude supply -- bullish for refiners' earnings. A collapsing spread signals oversupply of products or a crude oil spike that refiners cannot pass through.

## How It Works

### 3:2:1 Crack Spread Calculation
**Crack Spread = (2 x [[gasoline|Gasoline]] Price + 1 x [[heating-oil|Heating Oil]] Price) - (3 x [[crude-oil|Crude Oil]] Price)**

All prices converted to the same unit (typically $/barrel). Since NYMEX [[gasoline]] and [[heating-oil]] are quoted per gallon (42 gallons per barrel), the conversion is:

**Crack = (2 x RBOB_gasoline x 42 + 1 x Heating_oil x 42) - (3 x WTI_crude)**

The spread is expressed in dollars per barrel, representing the gross refining margin before operating costs. A typical range is $10-30/barrel, but it can spike to $50+ during supply disruptions (e.g., Hurricane Katrina, 2022 post-Russia sanctions) or collapse to near zero when product markets are oversupplied.

### Who Trades It
- **Refiners:** Sell (short) the crack spread to hedge their processing margin. If they lock in a $25/bbl crack spread, they are guaranteed that margin regardless of where crude and product prices go individually.
- **Speculators:** Buy the crack spread when they expect refining margins to widen (summer driving season, refinery outages, product demand surge). Sell when they expect margins to compress (crude price spike, demand destruction).
- **Relative value traders:** Compare crack spreads across regions (Gulf Coast vs. Midwest vs. Europe) or across time (front month vs. deferred) for arbitrage opportunities.

## Rules / Application

### Going Long the Crack Spread (Expecting Wider Margins)
1. **Buy 3 [[crude-oil]] futures** (e.g., WTI CL contracts on NYMEX).
2. **Sell 2 RBOB [[gasoline]] futures** and **sell 1 [[heating-oil]] (ULSD) futures** in the same contract month.
3. **Rationale:** You profit if products rise faster than crude, or crude falls faster than products.
4. **Timing:** Enter before peak demand seasons (late spring for summer driving season) or when refinery outages are expected.

### Going Short the Crack Spread (Expecting Narrower Margins)
1. **Sell 3 [[crude-oil]] futures.**
2. **Buy 2 RBOB [[gasoline]] futures** and **buy 1 [[heating-oil]] futures.**
3. **Rationale:** You profit if crude rises faster than products (e.g., OPEC supply cut without corresponding demand increase).

### Key Drivers to Monitor
- **Refinery utilization rates:** Low utilization (maintenance season, outages) reduces product supply, widening the crack spread.
- **Inventory reports:** Weekly [[eia-data|EIA petroleum status report]] ([[crude-oil|crude]] inventories vs. product inventories) — see [[inventory-cycle-analysis]].
- **Seasonal demand:** [[gasoline|Gasoline]] demand peaks in summer (driving season). [[heating-oil|Heating oil]] demand peaks in winter.
- **[[crude-oil|Crude oil]] supply shocks:** [[opec|OPEC]] decisions, [[geopolitical-risk-premium|geopolitical disruptions]] (sanctions, wars) affect crude more than products.
- **Regulatory changes:** IMO 2020 shipping fuel rules dramatically affected distillate crack spreads.

## Example

**Setup:** Long 3:2:1 crack spread entering May, targeting summer gasoline season.

1. **May 1:** WTI crude at $75/bbl, RBOB gasoline at $2.50/gal, heating oil at $2.40/gal.
2. **Crack spread:** (2 x $2.50 x 42 + 1 x $2.40 x 42) - (3 x $75) = ($210 + $100.80) - $225 = **$85.80 for 3 barrels = $28.60/bbl**.
3. **Enter:** Buy 3 CL (crude) contracts, sell 2 RB (gasoline) contracts, sell 1 HO (heating oil) contracts.
4. **July 15:** Summer demand peaks. Gasoline rises to $2.85/gal, heating oil to $2.55/gal, crude rises modestly to $78/bbl.
5. **New crack spread:** (2 x $2.85 x 42 + $2.55 x 42) - (3 x $78) = ($239.40 + $107.10) - $234 = **$112.50 for 3 barrels = $37.50/bbl**.
6. **Exit:** Close all legs. Profit = ($37.50 - $28.60) x 1,000 barrels (per 3-lot) = **$8,900 per 3:2:1 unit**.

## Advantages

- **Isolates refining economics** from outright crude oil price risk -- a more targeted, lower-risk bet than directional crude trades
- Strong **seasonal patterns** provide recurring trade setups (especially the summer gasoline crack)
- Used by actual industry participants (refiners) for hedging, providing deep liquidity and well-understood fundamentals
- The spread has well-defined fundamental drivers (utilization rates, inventories, seasonal demand) that are publicly reported weekly
- Can be traded as a single spread order on NYMEX/ICE, reducing execution complexity
- Lower margin requirements than outright futures positions because the exchange recognizes the spread's reduced risk

## Disadvantages

- Requires understanding of **petroleum refining economics** -- not a strategy for traders unfamiliar with energy markets
- **Basis risk:** The 3:2:1 ratio is an approximation; actual refinery yields vary, and the spread may not perfectly track a specific refiner's margin
- Large contract sizes ($75 x 1,000 barrels = $75K per crude contract) require significant capital even with reduced margin
- **Gap risk:** Geopolitical events (wars, sanctions, OPEC emergency meetings) can cause overnight gaps in crude prices that the product leg does not offset
- Weather events (hurricanes in the Gulf of Mexico) can simultaneously disrupt both crude supply and refining capacity, making the spread behave unpredictably
- **Roll costs:** Futures contracts expire monthly; rolling all three legs incurs transaction costs and potential slippage

## See Also

- [[crush-spread]] -- the agricultural equivalent (soybean processing margin)
- [[spark-spread]] -- the power generation equivalent (natural gas to electricity)
- [[seasonal-spread-trading]] -- seasonal patterns that drive crack spread opportunities
- [[basis-trading]] -- related commodity spread strategies
- [[event-driven-trading]] -- geopolitical and weather events that drive crack spread moves

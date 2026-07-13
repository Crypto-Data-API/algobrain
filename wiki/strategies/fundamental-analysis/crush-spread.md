---
title: "Crush Spread"
type: strategy
created: 2026-04-06
updated: 2026-04-14
status: good
tags: [crush-spread, soybeans, soybean-oil, soybean-meal, agricultural, commodity-spread, processing-margin]
aliases: ["Soybean Crush Spread", "Crush Margin Trade", "Soy Processing Spread"]
strategy_type: fundamental
timeframe: swing|position
markets: [commodities]
complexity: intermediate
backtest_status: untested
related: ["[[crack-spread]]", "[[spark-spread]]", "[[seasonal-spread-trading]]", "[[basis-trading]]", "[[event-driven-trading]]", "[[soybeans]]", "[[corn]]", "[[usda-data]]", "[[commodity-seasonality-patterns]]"]
---

# Crush Spread

## Overview

The crush spread represents the **[[soybeans|soybean]] processing margin** -- the profit earned by crushing raw [[soybeans]] into their two primary products: soybean oil and soybean meal. Trading the crush spread involves going long soybeans (the input) and short soybean oil and soybean meal (the outputs), or vice versa, to profit from changes in the processing margin. When the margin widens, processors are more profitable; when it narrows, processing becomes uneconomical.

The term "crush" refers to the physical process of crushing soybeans to extract oil (used for cooking, biodiesel, and industrial applications) and meal (used as high-protein animal feed -- the dominant revenue source, accounting for roughly 65-70% of the crush value). The standard crush ratio reflects approximate processing yields: **1 bushel of soybeans (60 lbs) produces approximately 11 lbs of soybean oil and 44 lbs of soybean meal** (with ~5 lbs of waste).

The crush spread is a fundamental trade in agricultural commodity markets, used by **processors** (ADM, Bunge, Cargill) for margin hedging, by **farmers** for forward planning, and by **speculators** for profit opportunities. The CBOT (CME Group) hosts all three contracts: soybeans (ZS), soybean oil (ZL), and soybean meal (ZM).

## How It Works

### Crush Spread Calculation
**Crush Spread ($/bushel) = (Soybean Meal Value + Soybean Oil Value) - Soybean Cost**

Using standard conversion factors:
- Soybean meal: price per short ton / 2000 x 44 lbs = meal value per bushel
- Soybean oil: price per lb x 11 lbs = oil value per bushel
- Soybeans: price per bushel (60 lbs)

**Board Crush** (simplified, using futures directly):
**Crush = (ZM price / 2000 x 44) + (ZL price x 11) - ZS price**

Typical crush spread range: $0.50-$2.50 per bushel. Values above $2.00 are highly profitable for processors; below $0.50 may trigger reduced crushing activity.

### Crush vs. Reverse Crush
- **Long the crush (buy crush):** Long soybeans, short soybean oil + soybean meal. Profits when the processing margin **narrows** (soybeans rise relative to products). This is a bet that processor demand for beans will increase.
- **Short the crush (sell crush / reverse crush):** Short soybeans, long soybean oil + soybean meal. Profits when the processing margin **widens** (products rise relative to beans). This is the processor's natural hedge and the speculator's bet on strong product demand.

Most speculative traders are interested in the **reverse crush** (selling the crush) to profit from expanding margins, particularly ahead of strong demand seasons for meal (livestock feeding) or oil (biodiesel mandates).

## Rules / Application

### Going Long the Reverse Crush (Expecting Wider Margins)
1. **Sell 10 soybean futures** (ZS, 5,000 bushels each = 50,000 bushels).
2. **Buy 11 soybean meal futures** (ZM, 100 short tons each = 1,100 tons).
3. **Buy 9 soybean oil futures** (ZL, 60,000 lbs each = 540,000 lbs).
4. These ratios approximate the actual processing yields from 50,000 bushels of soybeans.
5. **Profit:** If meal and oil prices rise faster than soybean prices, the margin expands.

### Key Drivers to Monitor
- **[[usda-data|USDA crop reports]]:** Planted acreage, yield estimates, and ending stocks for [[soybeans]] directly affect the input cost.
- **Livestock demand:** Meal demand is driven by [[lean-hogs|hog]], poultry, and [[live-cattle|cattle]] herd sizes. Chinese hog herd rebuilding (post-ASF) dramatically increased meal demand in 2020-2023.
- **Biodiesel mandates:** Renewable Fuel Standard (RFS) and Sustainable Aviation Fuel (SAF) policies drive soybean oil demand. Policy changes can shift the oil share of the crush value dramatically.
- **South American harvest:** Brazil and Argentina are major [[soybeans|soybean]] producers. Their crop size affects global supply and US crush margins.
- **Crush capacity utilization:** NOPA (National Oilseed Processors Association) monthly crush data indicates actual demand for soybeans by processors.

### Seasonal Patterns
- Crush margins tend to be **tightest** during harvest (September-November) when [[soybeans|soybean]] supply peaks and depresses bean-to-product spreads.
- Margins tend to **widen** in spring/summer when soybean supplies are drawn down and meal demand for animal feeding is strong.
- Monitor the [[seasonal-spread-trading]] calendar and [[commodity-seasonality-patterns]] for optimal entry timing.

## Example

**Setup:** Reverse crush (expecting wider margins) entering March ahead of spring livestock demand.

1. **March 1:** Soybeans (ZS) at $11.50/bu. Soybean meal (ZM) at $340/ton. Soybean oil (ZL) at $0.48/lb.
2. **Crush spread:** ($340/2000 x 44) + ($0.48 x 11) - $11.50 = $7.48 + $5.28 - $11.50 = **$1.26/bushel**.
3. **Enter reverse crush:** Sell 10 ZS, buy 11 ZM, buy 9 ZL.
4. **June 1:** Strong livestock feeding demand and biodiesel pull drive products higher. ZM rises to $380/ton, ZL to $0.54/lb, while ZS rises only modestly to $12.00/bu.
5. **New crush spread:** ($380/2000 x 44) + ($0.54 x 11) - $12.00 = $8.36 + $5.94 - $12.00 = **$2.30/bushel**.
6. **Exit:** Spread widened from $1.26 to $2.30 = **$1.04/bushel gain**. On 50,000 bushels: **$52,000 profit**.

## Advantages

- **Isolates processing economics** from outright soybean price risk -- hedged against directional commodity moves
- Well-understood fundamental drivers with publicly available data (USDA reports, NOPA crush data, export inspections)
- **Seasonal patterns** provide recurring, data-backed trade setups
- Used by actual processors (ADM, Bunge, Cargill) for hedging, ensuring deep liquidity in the spread
- Lower margin requirements than outright positions due to the hedged nature of the spread
- The spread relationship is anchored by physical processing economics, providing a fundamental floor and ceiling

## Disadvantages

- Requires understanding of **agricultural commodity fundamentals** -- not suitable for traders without knowledge of soybean supply chains
- **Multiple legs** (3 different contracts) increase execution complexity and transaction costs
- Contract sizes are large and non-uniform, making precise ratio matching difficult for smaller accounts
- **Policy risk:** Biodiesel mandates and tariffs (e.g., China soybean tariffs in 2018) can cause sudden, unpredictable shifts in the spread
- **Weather risk:** Drought, floods, or early frost can simultaneously affect all three contracts in unpredictable ways
- The "board crush" (futures-based) may diverge from actual physical crush margins due to basis, transportation costs, and quality differentials

## See Also

- [[crack-spread]] -- the petroleum refining equivalent
- [[spark-spread]] -- the power generation equivalent
- [[seasonal-spread-trading]] -- seasonal patterns in agricultural commodities
- [[basis-trading]] -- related commodity spread and basis strategies
- [[event-driven-trading]] -- USDA report and policy events driving crush spread moves
- [[soybeans]] -- the input commodity for the crush spread
- [[corn]] -- competing acreage crop and ethanol feedstock
- [[usda-data]] -- USDA reports that move the soybean complex
- [[commodity-seasonality-patterns]] -- seasonal patterns in agricultural commodities

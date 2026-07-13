---
title: "Cotton"
type: market
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [commodities, agricultural, futures]
aliases: ["Cotton", "CT", "Cotton No. 2"]
related: ["[[corn]]", "[[soybeans]]", "[[commodities]]", "[[usda]]", "[[usda-data]]", "[[commodity-seasonality-patterns]]", "[[seasonal-spread-trading]]", "[[cot-report-analysis]]", "[[contango]]", "[[backwardation]]", "[[crude-oil]]"]
---

Cotton is a **dual agricultural/textile commodity** traded on ICE as Cotton No. 2 futures (CT). It bridges the agricultural and industrial/consumer sectors -- demand is driven by the global textile and apparel industry rather than food consumption. Major producers include China, India, the US, and Brazil, with the US as the world's largest exporter. Texas is the dominant US growing region, making **drought risk** the key weather variable. A distinctive feature of cotton is the **cotton-polyester substitution** effect: at high enough prices, textile manufacturers switch to synthetic fibers, creating a natural price ceiling. (Source: [[2026-04-14-commodities-research-framework]])

## Key Specifications

| Attribute | Detail |
|-----------|--------|
| **Exchange** | ICE US |
| **Ticker** | CT (Cotton No. 2) |
| **Contract size** | 50,000 lbs (~100 bales) |
| **Tick size** | $0.01/lb = $5.00 |
| **Trading months** | Mar (H), May (K), Jul (N), Oct (V), Dec (Z) |
| **Settlement** | Physical delivery (certified US warehouses) |
| **Typical price range** | CT: $0.55-$1.20/lb (2015-2025) |

The price is quoted in **US cents per pound**; a one-cent move on a 50,000 lb contract is $500. Cotton's value-per-tick and notional are smaller than the grain or energy complex, which keeps a single contract accessible but also means liquidity thins quickly in back months.

## How Cotton Trades: Microstructure

Cotton has two structural quirks that distinguish it from the grain board and that every cotton trader must understand:

| Feature | What it is | Why it matters |
|---------|-----------|----------------|
| **On-call sales** | Mills buy physical cotton at a fixed basis but leave the futures-price leg "unfixed" -- to be priced later by buying futures | A large **unfixed on-call** position is a known overhang of forced future buying; the CFTC publishes on-call data weekly and traders watch it as a coiled-spring indicator |
| **Certificated stock** | Cotton inspected and tendered into ICE-approved warehouses, eligible for delivery | Rising certificated stock signals deliverable supply and pressures the front month; low stock into delivery can force short-covering squeezes |
| **Limit + dynamic limits** | $0.04/lb base daily limit, expandable | Consecutive limit days during a Texas drought scare can lock out leveraged positions |
| **Liquidity concentration** | Volume clusters in Mar/May/Jul/Oct/**Dec** | Dec is the new-crop benchmark; the Jul (old crop) vs Dec (new crop) spread is the key intra-year structure |

The **old-crop / new-crop spread** (e.g. July vs December) is the most-watched calendar structure: when old-crop supply is tight it trades in steep [[backwardation]] (Jul over Dec); a comfortable carry market shows [[contango]] (Dec over Jul) and rewards storage. See [[seasonal-spread-trading]].

## Production and Supply

### Global Production (~120 million 480-lb bales annually)

| Country | Role | Notes |
|---------|------|-------|
| **China** | #1 producer, #1 consumer, #1 importer | Produces ~27 million bales; consumes ~38 million; strategic reserves can absorb/release massive quantities |
| **India** | #2 producer | ~25 million bales; highly variable due to monsoon dependence |
| **US** | #3 producer, #1 exporter | ~15 million bales; Texas grows ~40% of US cotton |
| **Brazil** | #4 producer, #2 exporter | Rising production; Mato Grosso state is the key growing region |
| **Pakistan** | #5 producer | ~5 million bales; often affected by flooding |

### US Cotton: Texas Dominance

The US cotton crop is heavily concentrated in **Texas**, which produces ~40% of US output (primarily in the High Plains/Lubbock area). This concentration means:

- Texas drought = US cotton supply shock
- USDA Crop Progress reports for Texas are the most watched condition data
- The rest of US production is spread across the "Cotton Belt" (Georgia, Mississippi, Arkansas, North Carolina)

### Chinese Strategic Reserves

China maintains enormous **state cotton reserves** (estimated at 5-10 million tonnes at various times) and uses them to manage domestic prices:

- **Stockpiling (2011-2013):** China purchased massive quantities, accumulating over 10 million tonnes and pulling global supply tight
- **Destocking (2014-2018):** Gradual sales from state reserves added supply and capped prices
- **Policy-driven:** Reserve purchases and sales are announced by the National Development and Reform Commission (NDRC); these decisions override market fundamentals

(Source: [[2026-04-14-commodities-research-framework]])

## Demand Drivers

### Textile and Apparel Industry

Cotton demand is fundamentally driven by the **global textile cycle**:

- **Consumer spending:** Apparel sales are cyclical; recession reduces cotton demand
- **Fashion cycles:** The shift between natural and synthetic fibers affects cotton's market share
- **E-commerce:** Has accelerated "fast fashion" trends, increasing overall textile demand but also polyester substitution
- **Sustainable sourcing:** Growing demand for organic and sustainably sourced cotton (BCI -- Better Cotton Initiative)

### Cotton-Polyester Substitution

This is cotton's most important demand-side dynamic:

- **Polyester** (made from petroleum) is cotton's primary competitor in the textile market
- At **high cotton prices** ($1.00+/lb), textile manufacturers increase the polyester blend ratio, reducing cotton demand
- This substitution creates a **natural price ceiling** for cotton -- above a certain level, demand destruction accelerates
- The crossover point varies by oil/polyester prices, but historically $1.00-$1.20/lb triggers significant substitution
- Conversely, when cotton is cheap relative to polyester, it gains market share

**The cotton-polyester-oil chain.** Polyester is a petroleum derivative (PTA/MEG from naphtha), so its cost floor tracks [[crude-oil]] and refined-product prices. The practical relationship:

| Cotton vs polyester | Crude oil regime | Effect on cotton demand |
|---------------------|------------------|--------------------------|
| Cotton expensive | Oil cheap (polyester cheap) | Maximum substitution pressure -- bearish cotton demand |
| Cotton expensive | Oil expensive (polyester dear) | Substitution muted -- cotton holds share better |
| Cotton cheap | Oil expensive | Cotton gains share aggressively |

This makes the **cotton/polyester price ratio** (and indirectly the cotton/crude relationship) a structural demand-side gauge that traders monitor alongside the textile cycle.

### Other Demand Components

- **Industrial use:** Cotton is used in medical products, industrial filtration, and other non-textile applications
- **Cottonseed:** A byproduct -- cottonseed oil (cooking) and cottonseed meal (animal feed) provide additional revenue to cotton farmers

## Key Reports and Data

| Report | Frequency | Why It Matters |
|--------|-----------|----------------|
| **[[usda-data|USDA WASDE]]** | Monthly | US and global supply/demand, ending stocks |
| **USDA Crop Progress** | Weekly (May-Nov) | Texas cotton condition; planting/harvest progress |
| **USDA Cotton Ginnings** | Periodic | Actual production data |
| **CFTC [[cot-report-analysis|COT]]** | Weekly | Speculative and commercial positioning |
| **ICAC (International Cotton Advisory Committee)** | Monthly | Global supply/demand estimates |
| **China NDRC** | Periodic | State reserve purchases/sales announcements |
| **USDA Export Sales** | Weekly | US cotton export commitments and shipments |

## Price Drivers

1. **Texas weather (drought):** The single largest near-term price driver for US cotton. Severe drought in 2011 and 2022 caused sharp price rallies
2. **Chinese reserves and policy:** Purchases, sales, and import quota decisions by China's NDRC can shift global balance dramatically
3. **Global stocks-to-use ratio:** Below 50% signals tightness; above 70% signals surplus
4. **Consumer spending/textile demand:** Cotton is a consumer discretionary commodity -- recession reduces demand
5. **Cotton-polyester price ratio:** High cotton prices trigger substitution to synthetics, capping upside
6. **Indian monsoon and policy:** India's monsoon affects its crop, and export restrictions (taxes, bans) can tighten global supply
7. **US dollar:** Cotton is priced in USD; a strong dollar reduces competitiveness of US exports
8. **Oil/polyester prices:** Lower oil prices reduce polyester costs, increasing competitive pressure on cotton

## Seasonal Patterns

Cotton follows [[commodity-seasonality-patterns|seasonal patterns]] tied to the Northern Hemisphere growing cycle:

- **March-April:** US planting decisions and USDA Prospective Plantings data
- **May-July:** US growing season. Texas drought risk is highest in June-July
- **August-September:** Crop Progress reports become critical as the crop matures
- **October-December:** US harvest. New supply typically pressures prices
- **January-February:** Post-harvest; focus shifts to demand and export pace

The 15-year seasonal average shows cotton prices tend to be strongest in late spring/early summer (weather premium) and weakest in the fall (harvest pressure). (Source: [[2026-04-14-commodities-research-framework]])

## Historical Price Events

- **2010-2011 Spike:** Cotton surged from $0.60 to $2.27/lb (all-time high) driven by Chinese stockpiling, tight global supply, and Pakistan flooding. Triggered massive textile substitution to polyester
- **2014-2020 Range Trade:** Chinese reserve destocking and adequate global supply kept prices in a $0.55-$0.85 range
- **2022 Rally and Crash:** Prices surged to $1.55 on Texas drought + tight supply, then crashed to $0.70 in months as demand destruction and recession fears took hold
- **1860s Cotton Famine:** The US Civil War cut off Southern cotton exports, devastating the British textile industry and demonstrating cotton's geopolitical importance

## Trading Considerations

- **Texas weather:** A single weather system can move the market; drought monitors, NOAA forecasts, and crop tours are essential
- **China factor:** State reserve actions are unpredictable and can override fundamentals
- **Demand cyclicality:** Cotton is more sensitive to the economic cycle than food commodities
- **Contract size:** 50,000 lbs ($27,500-$60,000 notional); smaller than grain contracts
- **Limit moves:** $0.04/lb ($2,000/contract) daily limit
- **Options:** Active options market on CT; implied volatility peaks during the US growing season

## Advantages of Trading Cotton

- Clear fundamental framework (supply: Texas weather + China policy; demand: textile cycle + polyester substitution)
- Well-defined seasonal patterns with decades of data
- Extensive public data from [[usda-data|USDA]] and ICAC
- Cotton-polyester substitution provides a natural price ceiling for risk management
- Active options market enables structured trades

## Disadvantages and Risks

- Chinese state reserve policy is opaque and unpredictable
- Demand is cyclical -- recession risk directly affects cotton prices
- Less liquid than grain or energy futures; wider bid-ask spreads
- Concentrated production (Texas drought risk, India monsoon risk) creates supply volatility
- Polyester substitution caps upside potential
- Trade policy (tariffs, Xinjiang cotton sanctions) adds geopolitical complexity

## Related

- [[corn]] -- competing acreage in some Southern US regions
- [[soybeans]] -- agricultural commodity complex
- [[coffee]] -- fellow ICE-traded soft commodity
- [[sugar]] -- soft commodity complex
- [[cocoa]] -- soft commodity complex
- [[crude-oil]] -- cost floor for polyester, cotton's substitute fiber
- [[commodity-seasonality-patterns]] -- seasonal trading analysis
- [[seasonal-spread-trading]] -- old-crop/new-crop (Jul vs Dec) calendar spreads
- [[cot-report-analysis]] -- speculative/commercial positioning and on-call data
- [[usda-data]] -- USDA cotton reports
- [[commodities]] -- commodity markets overview

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])

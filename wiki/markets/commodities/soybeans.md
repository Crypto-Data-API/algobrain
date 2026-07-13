---
title: "Soybeans"
type: market
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [commodities, agricultural, futures]
aliases: ["Soybeans", "Soy", "ZS"]
related: ["[[corn]]", "[[wheat]]", "[[crush-spread]]", "[[commodities]]", "[[cme-group]]", "[[usda]]", "[[usda-data]]", "[[commodity-seasonality-patterns]]", "[[seasonal-spread-trading]]", "[[grain-futures-basis-arbitrage]]", "[[cot-report-analysis]]", "[[contango]]", "[[backwardation]]"]
---

Soybeans are the world's most important oilseed, traded on the [[cme-group|CBOT]] as soybean futures (ZS) at 5,000 bushels per contract. When crushed, soybeans yield two products: **soybean meal** (ZM, high-protein animal feed, ~80% of crush value) and **soybean oil** (ZL, cooking oil, biodiesel). The [[crush-spread]] -- buying soybeans and selling meal plus oil -- is one of the most fundamental commodity spread trades. The US and Brazil are the two dominant producers (~70% combined), with Brazil having overtaken the US as the world's largest producer. China is by far the largest importer, absorbing ~60% of all globally traded soybeans. (Source: [[2026-04-14-commodities-research-framework]])

## Key Specifications

| Attribute | Detail |
|-----------|--------|
| **Exchange** | [[cme-group|CBOT (CME Group)]] |
| **Tickers** | ZS (soybeans), ZM (soybean meal), ZL (soybean oil) |
| **Contract size** | ZS: 5,000 bu; ZM: 100 short tons; ZL: 60,000 lbs |
| **Tick size** | ZS: 1/4 cent/bu = $12.50; ZM: $0.10/ton = $10; ZL: $0.01/lb = $6 |
| **Trading months** | Jan (F), Mar (H), May (K), Jul (N), Aug (Q), Sep (U), Nov (X) |
| **Settlement** | Physical delivery |
| **Typical price range** | $8.00-$17.00/bushel (2015-2025) |

## The Soybean Complex

Soybeans trade as a **complex of three interrelated contracts**:

- **Soybeans (ZS):** The raw commodity -- the input
- **Soybean Meal (ZM):** High-protein feed ingredient; drives demand from [[live-cattle|cattle]], [[lean-hogs|hog]], and poultry sectors
- **Soybean Oil (ZL):** Cooking oil and increasingly biodiesel feedstock; connects soybeans to energy markets via the Renewable Fuel Standard

The processing relationship is fixed by chemistry: 1 bushel of soybeans (60 lbs) yields approximately **44 lbs of meal**, **11 lbs of oil**, and ~5 lbs of waste. This creates the [[crush-spread]], which is the soybean processor's (ADM, Bunge, Cargill) profit margin. NOPA (National Oilseed Processors Association) monthly crush data is the key demand indicator for soybeans. (Source: [[2026-04-14-commodities-research-framework]])

## Production and Global Trade

### Two Hemispheres, Two Harvests

The soybean market's most distinctive feature is its **dual-hemisphere production cycle**:

| Region | Planting | Harvest | Share of Global |
|--------|----------|---------|-----------------|
| **US** | May-June | Sep-Nov | ~30% |
| **Brazil** | Oct-Dec | Feb-May | ~35% |
| **Argentina** | Oct-Dec | Mar-Jun | ~15% |
| **China** | May | Sep-Oct | ~5% (mostly consumed) |

This means the global soybean market has **two major supply injections per year**: the US harvest (Sep-Nov) and the South American harvest (Feb-May). The price relationship between old-crop (current supply) and new-crop (next harvest) is critical.

### The China Factor

China imports approximately 100 million metric tonnes of soybeans annually -- roughly 60% of all globally traded soybeans. This makes Chinese demand **the single largest swing factor** in the soybean market:

- Chinese crushing demand is driven by pork production ([[lean-hogs|hog]] herd size)
- The US-China trade war (2018) and subsequent tariffs diverted Chinese buying to Brazil
- African Swine Fever (2018-2019) decimated the Chinese hog herd, temporarily cratering demand, followed by a massive restocking cycle
- USDA FAS attaché reports and Chinese customs data are key tracking sources

(Source: [[2026-04-14-commodities-research-framework]])

## Cash Market, Basis, and Delivery

Futures are only half the picture. The physical soybean market trades on a **basis** -- the difference between the local cash price an elevator pays a farmer and the nearby [[cme-group|CBOT]] futures price:

**Cash price = nearby futures + basis**

- A **strong (narrow/positive) basis** signals tight local supply or strong demand (e.g. an exporter or crusher bidding aggressively near the Gulf or at a Midwest processing plant).
- A **weak (wide/negative) basis** signals abundant local supply, harvest gluts, or logistics bottlenecks (low river levels on the Mississippi widen interior basis dramatically).
- Basis is far less volatile than flat price and mean-reverts seasonally, which is the foundation of [[grain-futures-basis-arbitrage|grain basis arbitrage]] -- commercials lock in storage and transport margins by going long cash / short futures (or vice versa) and capturing convergence into delivery.

The ZS contract is **physically deliverable** against CBOT-licensed shipping stations along the Illinois River and at designated regular facilities. At expiry, futures and the deliverable cash price converge; persistent failure to converge (a delivery-mechanism breakdown) is a recurring concern across the CBOT grain complex and is monitored by the exchange and CFTC. The shape of the curve -- [[contango]] (carry market, storage incentivized) vs [[backwardation]] (inverse, immediate supply prized) -- tells storers whether the market will pay them to hold beans.

## Key Reports and Data

| Report | Frequency | Why It Matters |
|--------|-----------|----------------|
| **[[usda-data|WASDE]]** | Monthly | US and global supply/demand, ending stocks |
| **NOPA Crush** | Monthly (15th) | Actual soybean crush volumes; demand indicator |
| **Prospective Plantings** | Annual (March) | Acreage intentions; corn-soybean competition |
| **Crop Progress** | Weekly (May-Nov) | Condition ratings, planting/harvest progress |
| **Brazil CONAB** | Monthly | Brazilian crop estimates (rival to USDA) |
| **Export Sales** | Weekly (Thursday) | New sales and shipments to each destination |
| **Chinese Customs** | Monthly | Actual import volumes; demand verification |

## Price Drivers

1. **South American weather:** Brazilian and Argentine soybean production is now larger than US. La Nina droughts in Argentina (2018, 2023) and excessive rain in Brazil have been major price catalysts
2. **Chinese import demand:** Volume, pace, and source (US vs Brazil) of Chinese purchases dominate trade flows
3. **Corn-soybean acreage competition:** Farmers decide spring planting based on the corn-soybean price ratio. Ratio above 2.4:1 pulls acres to soybeans; below 2.2:1 favors [[corn]]
4. **Biodiesel/RD demand for soybean oil:** The Renewable Fuel Standard (RFS) and renewable diesel (RD) capacity expansion have been a structural tailwind for soybean oil since 2020
5. **US Midwest weather during August:** Pod fill is the critical yield determination period for soybeans; stress during August reduces yields
6. **Ending stocks-to-use ratio:** Below 5% signals extreme tightness; above 10% signals comfortable supply
7. **US dollar and freight rates:** Affect competitive positioning of US vs Brazilian exports
8. **Crush margins:** Strong [[crush-spread|crush margins]] incentivize processors to bid up soybeans; weak margins reduce demand

## Seasonal Patterns

Soybeans exhibit [[commodity-seasonality-patterns|seasonal patterns]] with a dual-hemisphere twist:

- **January-March:** South American crop uncertainty dominates. Brazilian harvest begins (Feb-Mar); Argentine weather risk peaks (Jan-Feb, La Nina drought potential)
- **April-May:** US planting. Prospective Plantings (March) and Acreage (June) reports set acreage expectations. Corn-soybean ratio determines competitive allocation
- **June-August:** US growing season. Weather premium builds; August pod fill is the critical yield window
- **September-November:** US harvest pressure. Prices tend to decline as new-crop supply overwhelms
- **November-December:** Post-harvest. Attention shifts to South American planting conditions

The 15-year seasonal average shows soybeans typically peak in May-July and trough in September-October. (Source: [[2026-04-14-commodities-research-framework]])

## The Crush Spread

The [[crush-spread]] is one of the most important concepts in soybean trading:

**Crush Spread ($/bu) = (ZM price / 2000 x 44) + (ZL price x 11) - ZS price**

- **Typical range:** $0.50-$2.50/bushel
- **Wide margins (>$2.00):** Incentivize processors to increase crush, bidding up soybean prices
- **Tight margins (<$0.75):** May cause processors to reduce throughput, reducing soybean demand
- **Reverse crush:** Speculators often trade the reverse crush (long products, short beans) to profit from margin expansion

**The "board crush" ratio.** Because the three contracts have different units, the spread is traded in a fixed leg ratio that the [[cme-group|CME]] supports as a single exchange-recognized spread instrument. The conventional **10:11:9** crush packages 10 soybean contracts against 11 meal and 9 oil contracts to balance the bushel equivalents -- this is how processors and spread traders execute the crush as one order with margin offsets rather than three separate outrights.

**Worked example (illustrative, not live prices).** Suppose ZS = $12.00/bu, ZM = $360/short ton, ZL = $0.45/lb. Then the gross crush per bushel is approximately `(360 / 2000 x 44) + (0.45 x 11) - 12.00 = 7.92 + 4.95 - 12.00 = $0.87/bu`. A processor with cash conversion costs below ~$0.50/bu is profitable at this margin; a margin compressing toward $0.50 signals the market is rationing crush demand. (Numbers chosen only to demonstrate the arithmetic.)

NOPA monthly crush data directly measures how many soybeans are being processed, making it the most timely demand indicator.

## Key Spread Relationships

- **Corn-soybean ratio:** The most watched ratio in ag trading. Determines spring acreage allocation
- **Soybean oil-palm oil spread:** Palm oil is the competing vegetable oil globally. Malaysian and Indonesian palm production affects soybean oil pricing
- **Old-crop vs new-crop:** The July-November spread in soybeans reflects supply tightness before the new harvest
- **Meal-oil ratio (ZM/ZL):** Reflects the relative demand for feed vs fuel uses of the crush

## Trading Considerations

- **Three-legged complex:** Trading the soybean complex requires understanding meal and oil dynamics, not just outright bean prices
- **South American news flow:** Brazilian and Argentine weather, CONAB estimates, and port logistics drive off-season price action
- **Limit moves:** $0.70/bushel daily limit for soybeans ($3,500/contract)
- **Options market:** Active options on ZS, ZM, and ZL; IV tends to peak during the US growing season
- **Managed money positioning:** [[cot-report-analysis|COT data]] shows soybean speculative positioning is heavily influenced by fund flow momentum
- **Expanded daily limits:** CBOT uses a variable price-limit mechanism -- the $0.70/bu limit can expand to ~$1.05 the day after a limit move, which can trap leveraged positions across consecutive sessions during a USDA or weather shock
- **Report-day gap risk:** WASDE (typically ~noon ET) and the year's marquee reports (Prospective Plantings late March, Grain Stocks and Acreage late June, January Final) routinely gap the board through stop levels; many traders flatten or hedge with options into these releases
- **Basis vs flat-price separation:** A hedger who is long cash beans and short futures is exposed only to [[grain-futures-basis-arbitrage|basis]], not flat price -- a fundamentally lower-variance position than an outright directional bet

## Historical Price Events

- **2012 US Drought:** Soybeans surged from $13 to $17.89/bushel (then all-time high) as Midwest drought devastated yields
- **2018 US-China Trade War:** Soybeans fell from $10.50 to $8.12 after China imposed retaliatory tariffs, redirecting purchases to Brazil
- **2020-2021 Bull Run:** China restocking + La Nina pushed soybeans from $8.50 to $16.77
- **2022 Russian Invasion:** Initial spike above $17.50, followed by demand destruction and recession fears
- **1973 Nixon Soybean Export Embargo:** President Nixon briefly embargoed soybean exports, prompting Japan to diversify to Brazil -- permanently altering global trade flows

## Advantages of Trading Soybeans

- Deep liquidity across all three contracts (ZS, ZM, ZL)
- Multiple spread opportunities ([[crush-spread]], corn-soybean, oil-meal, calendar)
- Two distinct supply cycles (US and South America) provide year-round trade setups
- Extensive public data from [[usda-data|USDA]], NOPA, Brazilian CONAB, and Chinese customs
- Strong fundamental anchoring via crush economics

## Disadvantages and Risks

- Three-legged complex requires broader knowledge than single-commodity trading
- South American weather data can be unreliable or delayed
- Chinese policy (tariffs, state purchasing, strategic reserves) can shift demand abruptly
- US-Brazil competition means the US is not always the marginal supplier
- Biodiesel policy changes (RFS, blenders tax credits) can cause sudden oil/meal ratio shifts
- Contract sizes are large ($40,000-$85,000 notional); mini contracts available but less liquid

## Related

- [[corn]] -- acreage competitor; co-planted in the Corn Belt
- [[wheat]] -- competing grain; different demand profile
- [[crush-spread]] -- the fundamental processing margin trade
- [[live-cattle]] -- meal demand for cattle feeding
- [[lean-hogs]] -- meal demand for hog feeding; China link
- [[commodity-seasonality-patterns]] -- seasonal analysis
- [[seasonal-spread-trading]] -- calendar and old-crop/new-crop spreads
- [[grain-futures-basis-arbitrage]] -- cash-vs-futures basis trade central to the grain complex
- [[cot-report-analysis]] -- managed-money positioning in the soybean complex
- [[usda-data]] -- key reports and data
- [[cme-group]] -- exchange listing soybean complex futures
- [[contango]] / [[backwardation]] -- futures curve dynamics

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])

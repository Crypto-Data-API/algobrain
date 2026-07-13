---
title: "Live Cattle"
type: market
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [commodities, futures]
aliases: ["Live Cattle", "LE", "Cattle", "Feeder Cattle"]
related: ["[[lean-hogs]]", "[[corn]]", "[[soybeans]]", "[[commodities]]", "[[cme-group]]", "[[usda]]", "[[usda-data]]", "[[commodity-seasonality-patterns]]"]
---

Live Cattle futures (LE) trade on the [[cme-group|CME]] and represent one of the most fundamentally distinctive commodity markets. The **cattle cycle** -- an 8-12 year cycle driven by the biology of cattle reproduction -- is one of the best-documented long-duration cycles in any commodity market. Unlike [[corn]], [[wheat]], or [[soybeans]], where farmers can adjust supply within a single growing season, cattle producers **cannot quickly ramp supply** in response to high prices: it takes 2+ years for a heifer to reach market weight. This biological constraint creates slow, predictable supply cycles that are well-suited to fundamental trading. (Source: [[2026-04-14-commodities-research-framework]])

## Key Specifications

| Attribute | Detail |
|-----------|--------|
| **Exchange** | [[cme-group|CME]] |
| **Tickers** | LE (Live Cattle), GF (Feeder Cattle) |
| **Contract size** | LE: 40,000 lbs; GF: 50,000 lbs |
| **Tick size** | LE: $0.025/lb = $10; GF: $0.025/lb = $12.50 |
| **Trading months** | Feb, Apr, Jun, Aug, Oct, Dec |
| **Settlement** | LE: Physical delivery; GF: Cash-settled |
| **Typical price range** | LE: $1.10-$2.00/lb (2015-2025) |

## The Cattle Cycle

The cattle cycle is a well-known 8-12 year cycle driven by biological and economic constraints:

### Why It Exists

1. **Long gestation:** Cattle have a ~9-month gestation period
2. **Time to market weight:** Calves take 18-24 months to reach slaughter weight
3. **Herd building requires retaining heifers:** To expand the herd, ranchers must retain heifers (young females) for breeding rather than selling them for slaughter. This **reduces** near-term supply even as it builds future supply
4. **Liquidation phase:** When ranchers decide to reduce herd size (due to drought, low prices, or high feed costs), they sell cows and heifers, **increasing** near-term supply while reducing future supply

### Cycle Phases

| Phase | Duration | Characteristics | Price Tendency |
|-------|----------|----------------|----------------|
| **Expansion** | 3-5 years | Ranchers retain heifers; herd grows; fewer cattle at market | Rising prices |
| **Peak herd** | 1-2 years | Maximum herd size; large calf crop coming | Prices plateau |
| **Contraction** | 3-5 years | Ranchers liquidate; more cattle at market; herd shrinks | Declining prices |
| **Trough herd** | 1-2 years | Minimum herd size; few calves; stage set for next expansion | Prices bottom, begin to recover |

The current US cattle herd (as of 2025) is near cycle lows, with January 1 inventory at its lowest since the early 1960s. As of mid-2026 the market remained in this tight-herd phase, with the US herd rebuilding only slowly from its multi-year contraction — historically a multi-year price-support setup (Source: [[2026-04-14-commodities-research-framework]]; Perplexity sonar, June 2026).

## Production Chain

### From Ranch to Plate

1. **Cow-calf operations:** Ranchers maintain breeding herds and produce calves (primarily in western US -- Texas, Kansas, Nebraska, Montana)
2. **Stocker/backgrounder:** Calves graze on grass to gain weight (400-800 lbs)
3. **Feedlots:** Cattle are "finished" on [[corn]]-based rations for 120-180 days to reach slaughter weight (~1,300 lbs)
4. **Packers:** Slaughter and processing (Tyson, JBS, Cargill, National Beef -- the "Big Four" control ~85% of US beef packing)

### Fed Cattle vs Feeder Cattle

- **Fed cattle (LE):** Finished cattle ready for slaughter. Price reflects the value of beef at the wholesale level
- **Feeder cattle (GF):** Younger cattle going to feedlots. Price is driven by expected future fed cattle prices minus feed costs
- **The cattle crush:** Feedlot margin = Fed cattle revenue - (Feeder cattle cost + Feed cost). This is analogous to the [[crush-spread]] in soybeans

**Feed cost linkage:** Because feedlot rations are primarily [[corn]], the feeder-to-fed cattle spread is directly affected by corn prices. When corn is expensive, feedlot margins compress and feeder cattle prices decline (the "placement margin").

## The Cattle Crush and the Cattle Complex

The "cattle complex" is the set of related futures -- live cattle (LE), feeder cattle (GF), and corn (ZC) -- whose relationship defines feedlot economics. The **cattle crush spread** replicates the feedlot's actual P&L:

```
Cattle crush margin = Fed cattle revenue (LE) - Feeder cattle cost (GF) - Feed cost (corn, ZC)
```

A feedlot buys a feeder animal, feeds it corn for 120-180 days, and sells a finished (fed) animal. The crush spread lets a trader take a view on whether feedlot margins will be profitable, analogous to the soybean [[crush-spread]] or the energy crack spread. The standard ratio approximates the input/output weights (roughly a multi-leg combination buying LE and selling GF + corn, or the reverse), reflecting that one finished steer requires one feeder plus a quantity of corn.

| Spread | Legs | What it expresses |
|--------|------|-------------------|
| **Cattle crush** | Long LE, short GF + [[corn\|ZC]] | Feedlot finishing margin |
| **Feeder-to-fed (placement margin)** | GF vs LE | Whether feedlots can profitably place cattle |
| **Live cattle calendar** | e.g. Jun (M) vs Oct (V) | Seasonal demand + on-feed supply timing |
| **Cattle vs [[lean-hogs\|hogs]] (meat spread)** | LE vs HE | Relative protein value; beef vs pork substitution |
| **Cattle vs [[corn]] (gross feeding margin)** | LE vs ZC | Output price vs primary input cost |

When corn is expensive, the crush compresses and feedlots reduce placements -- which tightens future fed-cattle supply and is bullish for deferred LE even as it is bearish for GF today. This feed-cost transmission is one of the cleanest fundamentally-anchored spread relationships in agriculture and connects to [[commodity-seasonality-patterns]] and [[seasonal-spread-trading]].

## Key Reports and Data

| Report | Frequency | Why It Matters |
|--------|-----------|----------------|
| **USDA Cattle on Feed** | Monthly (3rd Friday) | Placements, marketings, and on-feed inventory at feedlots with 1,000+ head capacity |
| **USDA Cattle Inventory** | Semi-annual (Jan 1, Jul 1) | Total US herd size, calf crop, breeding herd -- the primary cycle indicator |
| **Cold Storage** | Monthly | Beef in cold storage; indicates demand pipeline |
| **Weekly Slaughter** | Weekly | Head count by species; indicates current supply flow |
| **USDA Boxed Beef Cutout** | Daily | Wholesale beef prices (Choice and Select grades); demand indicator |
| **COT Report** | Weekly | [[cot-report-analysis|Commercial and speculative positioning]] |

## Price Drivers

1. **Cattle cycle phase:** The dominant long-term driver. Low herd inventory = structurally higher prices
2. **Feed costs ([[corn]]):** High corn prices compress feedlot margins and reduce placements, eventually tightening cattle supply
3. **Consumer beef demand:** Retail beef prices affect demand; competition from chicken and pork matters
4. **Packer margins:** The spread between live cattle prices and boxed beef cutout values reflects packer profitability. When packers are profitable, they bid aggressively for cattle
5. **Drought:** Severe drought forces ranchers to liquidate herds early (near-term bearish, long-term bullish as future supply is reduced)
6. **Exports:** US beef exports to Japan, South Korea, China, and Mexico are a significant demand component
7. **Seasonal demand:** Grilling season (May-September) increases beef demand
8. **Imports:** Australian, Brazilian, and Canadian beef compete with US product, especially for ground beef (trim)

## Seasonal Patterns

Live cattle follow [[commodity-seasonality-patterns|seasonal patterns]] driven by demand and supply cycles:

- **January-March:** Post-holiday demand lull. Cash cattle prices often softer
- **April-May:** Pre-grilling season demand builds. Prices typically rally
- **June-August:** Peak grilling season demand. Prices tend to be strongest
- **September-October:** Demand eases; large placements from spring calving enter feedlots
- **November-December:** Holiday demand (Thanksgiving, Christmas) can provide support

The feeder cattle market has its own seasonal: spring-born calves are typically weaned and sold in the fall (September-November), creating seasonal supply pressure on feeder prices.

## Cash-Futures Convergence

A well-known issue in live cattle markets is the **cash-futures basis** -- the difference between negotiated cash cattle prices and the nearby futures contract:

- Unlike grains (which converge at delivery), live cattle basis can be volatile and unpredictable
- The "Fed Cattle Exchange" and mandatory price reporting have been debated as solutions
- Basis risk makes hedging less precise for producers and feedlots than in grain markets
- CME has periodically adjusted delivery specifications to improve convergence

(Source: [[2026-04-14-commodities-research-framework]])

## Packer Margins and the Beef Cutout

The packer's margin is the spread between the **boxed beef cutout** (wholesale beef value, reported daily by USDA in Choice and Select grades) and the live cattle price they pay. This spread is a real-time profitability signal:

- **Wide packer margin:** packers are profitable, slaughter aggressively, and bid up cash cattle -- bullish for LE.
- **Narrow / negative packer margin:** packers slow kills and pull bids -- bearish for cash cattle.
- **Choice-Select spread:** the premium of Choice over Select grade widens seasonally (grilling season) and signals demand for higher-quality cuts.

Because the "Big Four" packers (Tyson, JBS, Cargill, National Beef) control ~85% of US capacity, packer behavior can dominate cash-futures dynamics for stretches -- a structural feature that distinguishes cattle from the more atomized grain markets.

## Notable Cycle and Price Episodes

| Period | Move | Driver |
|--------|------|--------|
| 2014-2015 | Record highs | Post-drought herd contraction; tight supply, strong demand |
| 2016-2020 | Decline / range | Herd rebuilt to cycle highs; ample supply |
| 2020 | COVID dislocation | Packing-plant shutdowns; cash collapsed while boxed beef spiked, blowing out packer margins |
| 2022-2025 | Sustained rally | Multi-year drought-driven herd liquidation; Jan 1 inventory fell to lowest since the early 1960s |
| Mid-2026 | Tight-herd phase | Herd rebuilding only slowly; structurally supportive (Source: [[2026-04-14-commodities-research-framework]]; Perplexity sonar, June 2026) |

These reflect the cattle cycle thesis: low herd inventory is a multi-year price-support setup, while drought accelerates near-term liquidation (bearish short-term, bullish long-term).

## Trading Considerations

- **Cattle on Feed report:** The most market-moving event for cattle futures. Surprises in placements or on-feed numbers can cause limit moves
- **Long-cycle thinking:** The cattle cycle operates on years, not weeks. Position traders and longer-term strategies are better suited than short-term trading
- **Packer concentration:** The Big Four packers have significant market power, which can affect cash-futures dynamics
- **Limit moves:** $0.0475/lb ($1,900/contract) for LE; can expand after limit days
- **Physical delivery:** LE is physically delivered (cattle are presented for inspection at approved facilities); most traders exit before delivery
- **Weather as a long-term driver:** Drought in ranching country (Texas, Great Plains) affects the cattle cycle but plays out over months/years, not days

## Advantages of Trading Cattle

- The cattle cycle provides a long-duration, fundamentally anchored trading framework
- Extensive public data from [[usda-data|USDA]] reports
- Well-defined seasonal patterns
- Feed cost linkage ([[corn]]) creates spread trading opportunities
- The biological supply constraint (cannot quickly increase production) makes the market more analytically tractable than crops

## Disadvantages and Risks

- Less liquid than grains or energy; wider bid-ask spreads
- Cash-futures basis risk complicates hedging
- Packer concentration (Big Four) can distort pricing dynamics
- Disease risk (bovine spongiform encephalopathy/BSE, foot-and-mouth) is rare but catastrophic
- Cattle on Feed report surprises can cause limit moves
- Physical delivery logistics are complex
- Ethical and environmental concerns (methane emissions, land use) may create long-term policy headwinds

## Related

- [[lean-hogs]] -- competing protein; different cycle dynamics
- [[corn]] -- primary feed ingredient; feed cost linkage
- [[soybeans]] -- soybean meal as protein supplement in rations
- [[commodity-seasonality-patterns]] -- seasonal trading patterns
- [[usda-data]] -- USDA cattle reports
- [[crush-spread]] -- the analogous soybean processing margin
- [[seasonal-spread-trading]] -- spread strategies including the cattle crush
- [[cot-report-analysis]] -- commercial vs speculative positioning
- [[cme-group]] -- exchange listing cattle futures
- [[commodities]] -- commodity markets overview

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])
- Perplexity sonar query, June 2026 (US herd still in tight/slow-rebuild cycle).

---
title: "Crude Oil"
type: market
created: 2026-04-14
updated: 2026-06-12
status: good
tags: [commodities, energy, futures]
aliases: ["Crude Oil", "Oil", "WTI", "Brent Crude", "Petroleum"]
related: ["[[natural-gas]]", "[[gasoline]]", "[[heating-oil]]", "[[coal]]", "[[commodities]]", "[[opec]]", "[[eia]]", "[[cme-group]]", "[[intercontinental-exchange]]", "[[crack-spread]]", "[[contango]]", "[[backwardation]]", "[[geopolitical-risk-premium]]", "[[inventory-cycle-analysis]]", "[[eia-data]]"]
---

# Crude Oil

Crude oil is the most important commodity market by dollar volume and the backbone of global energy markets. It serves as the primary input for transportation fuels, petrochemicals, and plastics, and its price ripples through virtually every sector of the global economy. Two benchmark grades dominate pricing: **WTI (West Texas Intermediate)** traded on [[cme-group|NYMEX]] and **Brent Crude** traded on [[intercontinental-exchange|ICE]]. (Source: [[2026-04-14-commodities-research-framework]])

## Benchmark Grades

### WTI (West Texas Intermediate)

- **Exchange**: [[cme-group|NYMEX]] — ticker **CL**
- **Contract size**: 1,000 barrels
- **Delivery point**: Cushing, Oklahoma — a landlocked hub with ~90 million barrels of storage capacity
- **Quality**: Light (API gravity ~39.6) and sweet (sulfur ~0.24%) — easier and cheaper to refine
- **Primary use**: U.S. domestic benchmark; historically the most actively traded crude contract in the world
- **Limitation**: Cushing's landlocked location means WTI can disconnect from global pricing when pipeline or storage constraints arise (as dramatically demonstrated in [[2020-negative-oil-price|April 2020]])

### Brent Crude

- **Exchange**: [[intercontinental-exchange|ICE]] — ticker **B**
- **Delivery**: Waterborne delivery from North Sea fields (Brent, Forties, Oseberg, Ekofisk, Troll — the "BFOET" basket)
- **Quality**: Light and sweet, though slightly heavier than WTI
- **Primary use**: Global pricing reference — approximately **60% of the world's crude oil** is priced relative to Brent
- **Advantage**: Waterborne delivery avoids the landlocked constraints that periodically distort WTI pricing

### WTI-Brent Spread

The price difference between WTI and Brent is known as the **geographic spread** or **transatlantic spread**. Historically WTI traded at a slight premium to Brent (higher quality), but since 2010-2011 it has frequently traded at a discount due to Cushing storage dynamics and U.S. production surges. The WTI-Brent spread is itself an actively traded instrument and a key component of [[geographic-spread-trading]] strategies. (Source: [[2026-04-14-commodities-research-framework]])

## Key Price Drivers

| Driver | Mechanism | Data Source |
|--------|-----------|-------------|
| [[opec]] production decisions | Supply management via quotas; OPEC+ (with Russia) controls ~40% of global output | OPEC monthly reports, JMMC meetings |
| [[eia]] inventory data | Weekly U.S. petroleum stocks — surprise vs consensus moves the market | Wednesday 10:30 AM ET release |
| Geopolitics | Strait of Hormuz (~20% of global supply), sanctions (Iran, Russia, Venezuela), wars | Real-time news flow |
| USD strength | Oil priced in USD — stronger dollar makes oil more expensive for non-USD buyers, suppressing demand | [[dxy]], Fed policy |
| Global demand | China and India account for growing share of incremental demand; [[gdp]] growth drives consumption | IEA monthly Oil Market Report |
| [[shale-oil]] production | U.S. shale (Permian Basin) acts as swing supply; responds to price with ~6 month lag | EIA Drilling Productivity Report |
| Refinery utilization | Seasonal maintenance turnarounds reduce crude demand temporarily | EIA weekly report |

(Source: [[2026-04-14-commodities-research-framework]])

## How It Trades

### Futures

- **WTI (CL)**: [[cme-group|NYMEX]], 1,000 barrels/contract, monthly expiry, physically delivered to Cushing
- **Brent (B/BZ)**: [[intercontinental-exchange|ICE]], 1,000 barrels, cash-settled against ICE Brent Index
- **E-mini Crude (QM)**: 500 barrels, electronically traded, popular with smaller accounts
- **Micro WTI (MCL)**: 100 barrels, introduced for retail accessibility

### Options

Actively traded options on CL and Brent futures. Key for hedging and strategies like [[crack-spread]]. Weekly options available for event-driven trading around [[eia]] releases and [[opec]] meetings.

### Spreads

- **Calendar spreads**: Front month vs deferred — directly trades the [[contango]] or [[backwardation]] term structure
- **WTI-Brent spread**: Geographic arbitrage (see [[geographic-spread-trading]])
- **Crack spread**: Crude vs refined products (see [[crack-spread]])

### ETFs and Related Instruments

- **USO** (United States Oil Fund): Front-month WTI futures — suffers significant [[contango]] roll drag
- **BNO** (United States Brent Oil Fund): Brent equivalent
- **XLE** (Energy Select Sector SPDR): Equity exposure to oil majors
- Leveraged and inverse products exist but carry significant tracking error over time

## Term Structure

Crude oil frequently oscillates between [[contango]] (future prices > spot) and [[backwardation]] (spot > future prices):

- **Contango**: Typical when storage is abundant and near-term demand is weak. The cost of carry (storage + financing) creates upward-sloping curve. Extreme contango occurred in spring 2020 during COVID demand collapse.
- **Backwardation**: Typical when spot demand is strong or supply is disrupted. Signals a tight physical market. Backwardation rewards long futures holders via positive [[roll-yield]].

The shape of the crude oil curve is a critical signal for [[trend-following-cta]] strategies and [[basis-trading]] approaches. (Source: [[2026-04-14-commodities-research-framework]])

## Seasonality

| Period | Effect | Driver |
|--------|--------|--------|
| February-April | Refinery maintenance (turnaround season) | Reduced crude demand, inventory builds |
| May-September | **Driving season** — gasoline demand peaks | Supports crude prices, widens [[crack-spread]] |
| September-October | Hurricane season peak (Gulf of Mexico) | Supply disruption risk premium |
| November-February | Heating oil demand peaks (Northeast US) | Supports distillate cracks and crude demand |
| Year-end | Tax-related selling, budget positioning | Can create seasonal weakness |

## Risk Factors

### Extreme Volatility Events

- **[[2020-negative-oil-price]]**: On April 20, 2020, WTI May futures settled at **-$37.63/barrel** — the first time a major commodity traded at a negative price. Caused by COVID demand destruction + Cushing storage at capacity + expiring contracts with no storage available.
- **[[1973-oil-crisis]]**: OPEC embargo quadrupled prices from ~$3 to ~$12/barrel, demonstrating [[geopolitical-risk-premium]] in energy markets.
- **2008 spike and crash**: Oil hit $147/barrel in July 2008, then collapsed to $32 by December — one of the most dramatic price collapses in commodity history.
- **2022 Russia-Ukraine**: Brent spiked above $130 after Russia's invasion, then fell back as supply rerouted and demand weakened.

### Structural Risks

- [[opec]] cartel dynamics — production cut compliance varies, member cheating is endemic
- [[geopolitical-risk-premium]] — wars, sanctions, chokepoints (Strait of Hormuz, Red Sea, Suez Canal)
- Energy transition — long-term demand destruction from EVs, renewables, policy changes
- [[storage-economics]] — physical constraints can decouple futures from economic fundamentals

## Related Strategies

- [[crack-spread]] — Trade refining margins (crude vs products)
- [[geographic-spread-trading]] — WTI-Brent and other geographic arbitrage
- [[basis-trading]] — Cash vs futures convergence
- [[trend-following-cta]] — Crude oil is a core holding in most CTA trend-following programs
- [[seasonal-spread-trading]] — Calendar spreads exploiting seasonal demand patterns
- [[commodity-seasonality-patterns]] — Broader seasonal framework

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])

---
title: "Natural Gas"
type: market
created: 2026-04-06
updated: 2026-06-12
status: good
tags: [commodities, energy, volatility, seasonal]
aliases: ["nat gas", "NG", "Henry Hub"]
related: ["[[commodities]]", "[[futures]]", "[[volatility]]", "[[seasonal-trading]]", "[[cftc]]", "[[crude-oil]]", "[[heating-oil]]", "[[cot-report-analysis]]", "[[commodity-seasonality-patterns]]", "[[eia-data]]", "[[inventory-cycle-analysis]]", "[[geopolitical-risk-premium]]"]
---

# Natural Gas

Natural gas is one of the most volatile and actively traded energy commodities, known for extreme price swings driven by weather, seasonal demand patterns, and storage dynamics. It is a favorite among futures traders who thrive on volatility but also a graveyard for those who underestimate its risk. As of 2026-06-08 the Henry Hub spot price was around **US$3.10/MMBtu**, with the US market well supplied and storage near or above seasonal norms (Source: Perplexity sonar / FRED DHHNGSP, June 2026).

## Contract Specifications

| Attribute | Detail |
|-----------|--------|
| **Exchange** | NYMEX ([[cme-group|CME Group]]) |
| **Ticker** | NG (full), QG (e-mini), MNG (micro) |
| **Contract size** | NG: 10,000 MMBtu |
| **Delivery point** | Henry Hub, Erath, Louisiana (physically delivered) |
| **Quote** | US$/MMBtu |
| **Tick size** | $0.001/MMBtu = $10 per NG contract |
| **Recent price (2026-06-08)** | ~$3.10/MMBtu |

## How Natural Gas Is Traded

- **Futures**: Henry Hub natural gas futures (NG) on the NYMEX/CME are the benchmark contract, representing 10,000 MMBtu. The Henry Hub delivery point in Louisiana serves as the U.S. pricing reference.
- **ETFs**: UNG (United States Natural Gas Fund) tracks near-month futures but suffers significant losses from contango roll costs over time.
- **Options**: Nat gas options are actively traded and offer defined-risk exposure to this volatile market.
- **Related Equities**: Companies like EQT, Chesapeake Energy, and Antero Resources provide equity exposure to gas prices.

## Price Drivers

- **Weather**: The dominant short-term driver. Cold winter forecasts spike prices (heating demand), while mild winters crush them. Hurricane season can disrupt Gulf of Mexico production.
- **Storage Reports**: The weekly EIA Natural Gas Storage Report (released every Thursday) is one of the most market-moving data points in commodities. Inventory levels relative to 5-year averages drive sentiment.
- **Seasonality**: Gas prices typically peak in winter (heating season, November-February) and have a secondary peak in summer (cooling/electricity demand). Shoulder months (spring/fall) tend to see lower prices.
- **LNG Exports**: Growing U.S. liquefied natural gas exports have increasingly linked domestic prices to global markets.

## Volatility Profile

Natural gas routinely makes 5-10% daily moves and has experienced 30%+ moves in single sessions. The "Widowmaker" spread (March-April futures) is famous for its extreme volatility around the heating-to-cooling season transition.

## COT Positioning

Natural gas is one of the most volatile energy commodities and frequently exhibits extreme speculative positioning visible in the [[cot-report-analysis|Commitments of Traders (COT) report]]. Key patterns:

- **Managed money (hedge funds/CTAs)**: Net positioning swings between extreme long and extreme short more dramatically in nat gas than in [[crude-oil]] or most other commodities. Extreme net short positioning by managed money has historically coincided with seasonal lows (late March/early April shoulder season) and can signal contrarian buying opportunities.
- **Producer/merchant hedging**: Commercial hedgers (natural gas producers and utilities) provide the other side of speculative bets. When producer hedging (net short) reaches extreme levels, it can signal that producers expect higher prices and are locking in forward sales.
- **Swap dealer positioning**: Swap dealers intermediate between commercial hedgers and speculators. Their net position changes can signal shifts in commercial demand for hedging.
- **Open interest extremes**: Periods of unusually high open interest combined with extreme net speculative positioning often precede major price reversals.
- **Seasonal COT patterns**: Speculative positioning tends to follow [[commodity-seasonality-patterns]] — shorts build during injection season (spring/summer), longs build ahead of winter withdrawal season. Deviations from this seasonal COT pattern are informative.

The weekly COT report is released every Friday at 3:30 PM ET (data as of Tuesday close) by the [[cftc]]. For natural gas, the most actionable signals come from comparing current managed money positioning against its 3-year range — readings above the 90th percentile (extreme long) or below the 10th percentile (extreme short) warrant attention.

The [[eia-data|EIA weekly storage report]] on Thursdays is the fundamental catalyst that most often triggers position unwinds when the data surprises against the direction of speculative positioning. (Source: [[2026-04-14-commodities-research-framework]])

## Trading Relevance

Natural gas is favored by experienced [[futures]] traders for its volatility, clear seasonal patterns, and well-defined fundamental drivers. However, its extreme price swings demand rigorous [[risk-management]] and [[position-sizing]]. The contango in futures curves makes long-term holding via ETFs like UNG a losing proposition — understanding futures roll mechanics is essential before trading this market.

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])
- Perplexity sonar query, June 2026 (Henry Hub spot ~$3.10/MMBtu on 2026-06-08; FRED DHHNGSP, EIA weekly storage).

## Related

- [[crude-oil]] — fellow energy benchmark; crack and spread relationships
- [[heating-oil]] — competing winter heating fuel
- [[eia-data]] — weekly storage report (Thursdays)
- [[cot-report-analysis]] — speculative positioning extremes
- [[commodity-seasonality-patterns]] — winter/summer demand seasonality
- [[commodities]] — sector overview

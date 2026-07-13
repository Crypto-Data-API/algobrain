---
title: "USDA"
type: entity
created: 2026-04-14
updated: 2026-06-10
status: good
tags: [data-provider, commodities]
aliases: ["USDA", "United States Department of Agriculture"]
related: ["[[corn]]", "[[wheat]]", "[[soybeans]]", "[[usda-data]]", "[[commodity-data-sources]]", "[[commodities]]", "[[supply-demand-balance]]", "[[commodity-seasonality-patterns]]"]
entity_type: regulator
founded: 1862
headquarters: "Washington, D.C., USA"
website: "https://www.usda.gov"
---

The United States Department of Agriculture (USDA) is the primary source of supply and demand data for agricultural [[commodities]] worldwide. Its monthly WASDE report is the single most market-moving publication in grain and oilseed markets — the agricultural equivalent of earnings reports in equities.

## History

The USDA was established in 1862 by President Abraham Lincoln, who called it "the people's department" since approximately half of Americans were farmers at the time. Its statistical and forecasting role in commodity markets developed over the following century as US agricultural exports became a dominant force in global food supply. Today, the USDA's crop estimates and trade data are the benchmark reference for agricultural commodity traders, governments, and international organizations worldwide.

The department's data functions are spread across several agencies, most notably the **National Agricultural Statistics Service (NASS)**, the **Economic Research Service (ERS)**, the **Foreign Agricultural Service (FAS)**, and the **World Agricultural Outlook Board (WAOB)** which produces the WASDE report.

(Source: [[2026-04-14-commodities-research-framework]])

## Key Reports and Data Products

### WASDE Report (highest market impact)

The **World Agricultural Supply and Demand Estimates (WASDE)** is released monthly (typically around the 10th-12th). It is the single most important scheduled data release for agricultural commodity futures. The report covers:

- **US and global production estimates** — [[corn]], [[wheat]], [[soybeans]], cotton, rice, and other crops
- **Ending stocks** — The most critically watched figure. Ending stocks (or carryout) represent the surplus after consumption. Low ending stocks signal tight supply and support prices; high stocks signal surplus
- **Yield estimates** (bushels per acre) — Revised throughout the growing season as crop conditions evolve
- **Demand components** — Feed, food, industrial (including ethanol), and export demand
- **Global trade flows** — Country-level production and import/export estimates

### Other Major Reports

- **Prospective Plantings** (late March) — Survey-based estimate of farmers' planting intentions. Sets the initial acreage framework for the crop year and frequently causes large moves in [[corn]], [[soybeans]], and [[wheat]] futures
- **Crop Progress** (weekly, Monday afternoons during growing season, April-November) — Reports crop condition ratings (excellent/good/fair/poor/very poor) and planting/harvest progress percentages. Weekly condition changes drive intra-week price action
- **Grain Stocks** (quarterly, released with Prospective Plantings in March and separately in June, September, and December) — Physical inventory of grain in all storage positions. Resolves accumulated demand uncertainty
- **Crop Production** (monthly during growing season) — Updated yield and production estimates

### Data Access

USDA data is freely available through the **Economic Research Service (ERS)** and **Foreign Agricultural Service (FAS)** APIs and bulk download portals. The **USDA PSD (Production, Supply, and Distribution)** database provides historical supply/demand data for all major crops globally.

(Source: [[2026-04-14-commodities-research-framework]])

## Market Impact

USDA report releases are among the most volatile moments in agricultural futures markets:

- **WASDE day** — [[corn]], [[wheat]], and [[soybeans]] futures routinely move 2-5% in minutes following the report. The key driver is the deviation of ending stocks estimates from trade consensus. A 50 million bushel surprise in corn ending stocks can move the market 10-20 cents/bushel instantly
- **Prospective Plantings** — The March acreage report often generates the largest single-day moves of the crop year, as it sets the baseline for supply expectations. A shift of 1-2 million acres between [[corn]] and [[soybeans]] can reprice both markets significantly
- **Crop Progress ratings** — Weekly condition ratings during the critical July pollination period for corn drive significant intra-week volatility. A 3-5 percentage point drop in good/excellent ratings can add 10+ cents to corn prices within hours
- **[[supply-demand-balance]]** — USDA data forms the foundation of balance sheet analysis in agricultural markets, where traders model the trajectory of ending stocks relative to use (the stocks-to-use ratio) to identify mispricings
- **[[commodity-seasonality-patterns]]** — USDA report dates create predictable volatility clusters that inform seasonal trading strategies

(Source: [[2026-04-14-commodities-research-framework]])

## 2025–2026: Shutdown Disruption and Current Schedule

The 2025–2026 period demonstrated both the market dependence on USDA data and its fragility:

- **October 2025 WASDE cancelled.** The federal government shutdown (October 1 – November 12, 2025) forced USDA to cancel the October 2025 WASDE and Crop Production reports outright — leaving grain markets without an official balance-sheet update for roughly two months during harvest, an unusually long data blackout. Weekly Export Sales, daily export "flash" sales, and government ethanol production/consumption reporting were also suspended during the shutdown
- **November 2025 WASDE delayed.** The first post-shutdown WASDE was released November 14, 2025 (delayed from the scheduled November 10), alongside Crop Production. USDA noted some standard input data sources were unavailable for that report, increasing estimate uncertainty
- **Trading implication:** the blackout period forced markets to rely on private estimates (StoneX, satellite-based crop analytics, export lineup data), and the November 14 catch-up report carried elevated event risk. Shutdown risk is now a recognized tail scenario in agricultural data calendars
- **2026 schedule normal.** The 2026 calendar resumed the standard cadence of 12 monthly WASDE releases — the June 2026 WASDE is scheduled for June 11, 2026 at 12:00 p.m. ET, with subsequent releases July 10, August 12, September 11, October 9, November 10, and December 10. Crop Progress runs weekly on the first business day, April through November
- **Archive hosting change.** Effective October 1, 2025, historical WASDE archives moved from Cornell's Mann Library to the USDA National Agricultural Library (esmis.nal.usda.gov)

## Related

- [[corn]] — Most actively traded US agricultural commodity
- [[wheat]] — Global staple grain tracked by USDA
- [[soybeans]] — Major oilseed with USDA as primary data source
- [[usda-data]] — Detailed guide to using USDA data for trading
- [[commodity-data-sources]] — Catalog of commodity data providers
- [[commodities]] — Broader commodity market context
- [[supply-demand-balance]] — Analytical framework built on USDA data
- [[commodity-seasonality-patterns]] — Seasonal patterns around USDA report dates
- [[eia]] — Analogous data agency for energy commodities

## Sources

- [[2026-04-14-commodities-research-framework]]
- USDA Office of the Chief Economist, WASDE report page and 2026 release calendar — https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report
- CME Group, "Understanding Major USDA Reports in 2026" — https://www.cmegroup.com/articles/2026/understanding-major-usda-reports-in-2026.html
- Farm Policy News (University of Illinois), "USDA Will Release Nov. WASDE, Crop Production Reports" (Nov 2025) — https://farmpolicynews.illinois.edu/2025/11/usda-will-release-nov-wasde-crop-production-reports/
- Farm Progress, "November WASDE shows mixed results after government shutdown" (Nov 2025) — https://www.farmprogress.com/crops/november-wasde-shows-mixed-results-after-government-shutdown
- USDA National Agricultural Library, WASDE archive — https://esmis.nal.usda.gov/publication/world-agricultural-supply-and-demand-estimates
- Verified via Perplexity (sonar) and web search, 2026-06-10

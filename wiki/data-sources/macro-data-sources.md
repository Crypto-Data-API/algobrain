---
title: "Macro Data Sources"
type: reference
created: 2026-04-10
updated: 2026-06-20
status: excellent
tags: [data, macro, economic-data]
aliases: ["Economic Data Sources", "Macro Data Providers"]
related: ["[[data-sources-overview]]", "[[free-data-sources]]", "[[lookahead-bias]]", "[[economic-indicators]]", "[[cot-data]]", "[[eia-data]]", "[[usda-data]]", "[[commodity-data-sources]]"]
---

# Macro Data Sources

Where to get macroeconomic data — GDP, CPI, employment, rates, money supply, trade, central bank actions — for use in trading strategies. The single most important caveat for macro data: **almost every series gets revised after first release**. A backtest that uses the *current* value of a historical series is using information that didn't exist at the time, which is a form of [[lookahead-bias]]. The defense is to use *vintage* data (the values as originally reported on each release date), not current data.

## The Vintage Data Problem

When you fetch "US GDP for Q1 2010" from FRED today, you get the latest revised value — possibly the third or fourth revision since the original 2010 print. The original print was different. The market reacted to the original print, not the revised value.

Magnitudes are non-trivial:
- GDP revisions of 50-100 bps are routine
- Nonfarm payroll revisions of 50-100k jobs are common, sometimes much larger
- CPI revisions are smaller but exist
- Industrial production and inventory data revise substantially

For any strategy that trades macro releases, vintage data is mandatory. For strategies that use macro features as slow-moving inputs (e.g., monthly GDP as a regime indicator), the bias is smaller but still present.

## Provider Quick-Reference

The catalog below is detailed source-by-source in the sections that follow. This table is the at-a-glance comparison for choosing a provider: cost, whether it carries *vintage* (point-in-time) data, the API/access style, and the primary coverage. "Vintage" is the single most important column for backtesting — see [[lookahead-bias]].

| Provider | Cost | Vintage? | Access | Primary Coverage |
|----------|------|----------|--------|------------------|
| [[fred|FRED]] | Free | No (latest revision) | REST API, bulk CSV | US + broad international, 800k+ series |
| ALFRED | Free | **Yes** | REST API (same as FRED) | Vintage subset of FRED series |
| BEA | Free | Yes (with revisions) | REST API (clunky) | GDP, income, trade, regional |
| BLS | Free | Yes | REST API | Employment, CPI, PPI, wages |
| Federal Reserve Board | Free | Initial-print on release | Web / data download | Rates (H.15), money (H.6), bank assets (H.8) |
| Treasury.gov | Free | Yes (source archive) | Web / CSV / API | Yield curve, auctions, debt, TIC |
| [[cftc]] | Free | Yes (weekly archive) | Web / CSV | COT positioning ([[cot-data]]) |
| [[eia-data\|EIA]] | Free | Yes (weekly archive) | REST API | Petroleum, natural gas, energy outlook |
| [[usda-data\|USDA]] | Free | Yes (report archive) | Web / API | WASDE, crop stocks, plantings |
| IMF | Free | Partial | REST API (SDMX) | ~190 countries, GDP/inflation/reserves |
| World Bank | Free | Partial | REST API | Development + macro indicators |
| OECD | Free | Partial | REST API (SDMX) | OECD + major EM, harmonized |
| Eurostat | Free | Partial | REST API (SDMX) | EU / euro area statistics |
| Trading Economics | Free + paid | Limited | API (paid) | Aggregated global macro + calendar |
| Haver Analytics | ~$10K+/yr | **Yes** | API | Comprehensive global macro |
| Bloomberg / Refinitiv | Terminal | Yes (reasonable) | Terminal API | Integrated macro + markets |
| Macrobond | Institutional | Yes | App + API | Workflow, time-series management |

Practical default: prototype on [[fred|FRED]], backtest on ALFRED (vintage), reach for BEA/BLS first-print archives when precision matters, and add Haver / Bloomberg only at institutional scale. The free stack (ALFRED + BEA/BLS + central bank sites + [[cftc]]/[[eia-data|EIA]]/[[usda-data|USDA]]) covers the overwhelming majority of serious quant-macro research.

## US Sources

### FRED (Federal Reserve Economic Data)

Maintained by the St. Louis Fed. The most popular free macro database.

**Pros:** Free, hundreds of thousands of series, clean API, broad coverage from US Treasury rates to international data.

**Cons:** **Most series are the latest revision, not vintage.** Lookahead bias if used in backtests where release timing matters.

**Use for:** Background research, slow-moving features where revisions don't matter much, prototyping.

### ALFRED (Archival FRED)

The vintage version of FRED. Each series stored as a sequence of (release date, value) pairs.

**Pros:** **Free and vintage-correct.** Same API style as FRED.

**Cons:** Smaller coverage than FRED — not every series has vintage data, and historical depth varies by series.

**Use for:** **Any macro backtest where the publication date matters.** Default to ALFRED over FRED for serious quant work.

### BEA (Bureau of Economic Analysis)

Direct source for GDP, personal income, trade, regional accounts.

**Pros:** Authoritative, includes vintages and methodology notes.

**Cons:** API is functional but clunky.

**Best for:** When you need detailed BEA data with full revision history.

### BLS (Bureau of Labor Statistics)

Direct source for employment, CPI, PPI, productivity, wages.

**Pros:** Authoritative, free API, vintage data available.

**Cons:** Series IDs are obscure; documentation requires patience.

### Federal Reserve Board (H.15, H.6, H.8, etc.)

Direct source for interest rates, money supply, bank assets.

**Pros:** Authoritative.

**Cons:** Many series are also in FRED with the same revisions; direct access mostly useful for getting initial-print data on the release date.

### Treasury.gov

Historical Treasury yield curve, auction results, debt outstanding, TIC flows.

**Pros:** Direct from source.

**Cons:** Inconsistent formats across data products.

### CFTC

Commitments of Traders (COT) reports — weekly position data for futures markets, by trader category. Free.

**Use for:** Positioning analysis, sentiment, [[trend-following-cta|trend following]] research.

## International / Global Sources

### IMF

International Monetary Fund — global GDP, inflation, current accounts, reserves.

**Pros:** Free, covers ~190 countries, broad macro indicators.

**Cons:** Quarterly or annual frequency, long publication lag, some country data is unreliable.

### World Bank

Similar coverage to IMF, more focused on development indicators.

### OECD

Detailed macro data for OECD member countries plus major emerging economies.

**Pros:** High quality, harmonized cross-country definitions.

**Cons:** Lower frequency (mostly quarterly), longer lag.

### Eurostat

EU and euro area statistics. Similar role to BEA/BLS for the eurozone.

### Trading Economics

Aggregated global macro database with both free and paid tiers.

**Pros:** Easy multi-country comparisons.

**Cons:** Free tier is limited; paid tier needed for serious use.

### National Statistics Offices

ONS (UK), Destatis (Germany), Insee (France), Statistics Canada, ABS (Australia), etc. — direct national sources.

## Central Bank Data

- **Federal Reserve** — H.4.1 (balance sheet), H.6 (money supply), H.15 (rates), Fed minutes and statements
- **ECB Statistical Data Warehouse**
- **Bank of England statistical interactive database**
- **Bank of Japan statistics**
- **People's Bank of China** — limited transparency, partial English coverage

All free and authoritative for their respective jurisdictions.

## Commercial Macro Data

### Haver Analytics

Range: institutional pricing, ~$10K+/year.

**Pros:** Comprehensive global macro database, vintage data, clean API, used widely in macro hedge funds and academic research.

**Cons:** Expensive, institutional only.

**Best for:** Macro funds and serious quant macro research.

### Bloomberg / Refinitiv (ECON Functions)

Both terminals provide deep macro data with reasonable vintage tracking.

**Pros:** Integrated with the rest of the terminal data.

**Cons:** Expensive.

### Macrobond

Range: institutional pricing.

**Pros:** Strong workflow integration, time series management, charting.

**Cons:** Expensive.

## Sentiment and Survey Data

### Conference Board (Consumer Confidence, LEI)

Conference Board Leading Economic Indicators, Consumer Confidence Index, etc.

### University of Michigan Consumer Sentiment

Monthly survey of US consumer sentiment, widely watched.

### NFIB Small Business Optimism Index

US small business sentiment.

### Sentix / ZEW

European sentiment surveys.

## Calendar Data

For event-driven macro strategies, you also need a *release calendar*: the schedule of when each economic release will be published.

- **Forex Factory** — free, popular among retail FX traders
- **Investing.com Economic Calendar** — free
- **Trading Economics** — free + paid tiers
- **Bloomberg ECO** — paid, institutional standard
- **Econoday** — paid, used by many trading desks

For systematic event-driven backtesting, store the release schedule alongside the data so you can identify which observations correspond to which scheduled releases.

## Common Macro Data Pitfalls

1. **Using FRED instead of ALFRED.** The most common bias. Catastrophic for any release-day strategy.

2. **Aligning by reference date instead of release date.** "Q1 2010 GDP" is timestamped Q1 2010 in many datasets but wasn't released until late April 2010. Use release dates for backtesting.

3. **Mixing seasonal adjustment methodologies.** Some series are SA (seasonally adjusted), some are NSA. Different versions of the same series can be inconsistent — pick one and stick with it.

4. **Combining series from sources with different revision policies.** GDP from BEA, CPI from BLS, and unemployment from BLS may all have different vintage handling.

5. **Forgetting that "real-time" data isn't.** Even ALFRED has occasional gaps and edge cases. Compare to BEA/BLS first-release archives if precision matters.

6. **Holiday and release-time edge cases.** US releases happen at specific times (e.g., 8:30 ET for many BLS releases). Backtests that use daily macro features without time alignment can leak future information into the same trading day.

## Recommended Stack

### Personal research, no budget
ALFRED for vintage US macro + FRED for prototyping + central bank websites for deep dives. Sufficient for most research.

### Serious retail
ALFRED + BEA/BLS direct for first-print archives + Haver if budget allows.

### Institutional
Haver + Bloomberg/Refinitiv ECON + custom calendar tracking.

## How Trading Systems Consume Macro Data

Macro data feeds trading systems in three distinct modes, each with different latency, vintage, and storage requirements:

| Consumption Mode | Latency Need | Vintage Need | Typical Use | Storage Pattern |
|------------------|-------------|--------------|-------------|-----------------|
| **Release-day event trading** | Milliseconds–seconds | Critical (initial print) | Trade the surprise vs consensus on NFP, CPI, FOMC | Tick-stamped first print + consensus + release timestamp |
| **Regime / feature input** | Hours–days | Moderate | Slow-moving features (GDP trend, yield-curve slope, ISM) for [[market-regime]] models | Monthly/quarterly panel, aligned by release date |
| **Research / backtest** | Batch | Critical | Full historical vintage panels for systematic strategies | (release_date, reference_date, value) triples |

Key engineering practices that separate correct from biased macro pipelines:

1. **Store the triple, not the value.** Every observation needs `(reference_date, release_date, value, vintage_id)`. Joining on `release_date` is what prevents [[lookahead-bias]].
2. **Keep consensus alongside the print.** For event trading, the market reacts to *actual minus expected*. Store the consensus forecast (from a calendar provider) and compute the surprise.
3. **Align to release timestamps, not calendar dates.** A series timestamped "Q1" was released months later, often at a specific minute (e.g., 8:30 ET for many BLS releases). Daily-bar models that ignore intraday release timing leak future information into the same session.
4. **Normalize seasonal-adjustment basis.** Decide SA vs NSA per series and never mix versions of the same series.
5. **Pin the vintage in ML feature stores.** When macro features feed an [[ml-trading-pipeline|ML pipeline]], the feature store must serve the value *as it would have been known* at the training timestamp, or cross-validation results are inflated. See [[cross-validation-trading]].

For AI / LLM-assisted research, macro series are typically pulled via the provider API into a tidy frame and summarized; the same vintage caveats apply — an agent that fetches "current" GDP from [[fred|FRED]] and reasons about a 2010 backtest is reasoning on revised data.

## Data-Quality Caveats Summary

| Caveat | Affected Sources | Severity | Mitigation |
|--------|------------------|----------|------------|
| Latest-revision-only (no vintage) | [[fred\|FRED]], Trading Economics free tier | High for backtests | Use ALFRED / BEA / BLS archives |
| Reference-date vs release-date misalignment | Most datasets | High | Join on release date; store release timestamps |
| SA vs NSA inconsistency | BLS, BEA, FRED mirrors | Medium | Pick one basis per series and lock it |
| Long publication lag | IMF, World Bank, OECD | Medium | Treat as low-frequency regime inputs only |
| Cross-source revision-policy mismatch | Mixing BEA + BLS + Fed | Medium | Track each series' vintage handling separately |
| Country data reliability | IMF, some national offices | Variable | Cross-check against primary national sources |
| Release-time edge cases (holidays, exact minute) | All event-driven uses | High for HFT | Align to authoritative release calendars |

## Sources

- FRED documentation (research.stlouisfed.org/docs/api/fred/) — see [[fred]]
- ALFRED documentation (research.stlouisfed.org/docs/api/alfred/)
- BEA, BLS, and Federal Reserve Board public API documentation
- [[lookahead-bias]] — why vintage data matters
- [[economic-indicators]] — concept page
- [[cot-data]], [[eia-data]], [[usda-data]] — commodity-specific macro guides
- (Source: [[2026-04-14-commodities-research-framework]]) — commodity macro section

## Commodity-Specific Macro Data

Several specialized data sources provide macro-relevant commodity data that feeds directly into inflation, trade balance, and growth analysis:

### CFTC Commitments of Traders (COT) Reports
Weekly positioning data for all US-traded futures markets, broken down by trader category (commercial hedgers, managed money, swap dealers). Essential for sentiment and positioning analysis in [[commodities]], currencies, and interest rate futures. See [[cot-data]] for a detailed guide to accessing, normalizing, and interpreting COT data.

### EIA (Energy Information Administration) Reports
The [[eia-data|EIA]] publishes weekly petroleum status reports (Wednesday 10:30 AM ET), weekly natural gas storage reports (Thursday 10:30 AM ET), monthly Short-Term Energy Outlook, and annual Energy Outlook. EIA weekly crude oil inventory data is one of the most market-moving data releases in commodity markets. Critical for energy-inflation linkage analysis.

### USDA WASDE and Crop Reports
The [[usda-data|USDA]] publishes monthly WASDE (World Agricultural Supply and Demand Estimates) reports and quarterly Grain Stocks / Prospective Plantings reports. USDA data on crop production, stocks-to-use ratios, and export sales is the primary fundamental data source for agricultural commodity markets. Agricultural price moves feed directly into food CPI.

### Comprehensive Commodity Data Guide
For the full catalog of commodity-specific data sources — including exchange data, physical market data, seasonal tools, and commercial providers — see [[commodity-data-sources]].

(Source: [[2026-04-14-commodities-research-framework]])

## Related

- [[data-sources-overview]]
- [[free-data-sources]]
- [[fred]]
- [[lookahead-bias]]
- [[economic-indicators]]
- [[ism-pmi]]
- [[yield-curve]]
- [[market-regime]]
- [[ml-trading-pipeline]]
- [[cross-validation-trading]]
- [[cot-data]]
- [[eia-data]]
- [[usda-data]]
- [[commodity-data-sources]]

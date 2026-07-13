---
title: "USDA Data Sources"
type: concept
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [commodities, data-provider, agricultural]
aliases: ["USDA Data Sources", "USDA Data", "USDA Reports"]
related: ["[[usda]]", "[[corn]]", "[[wheat]]", "[[soybeans]]", "[[rice]]", "[[cotton]]", "[[live-cattle]]", "[[lean-hogs]]", "[[commodity-data-sources]]", "[[commodities]]", "[[supply-demand-balance]]", "[[commodity-free-tools]]", "[[eia-data]]", "[[cot-report-analysis]]", "[[seasonality]]", "[[event-driven]]", "[[implied-volatility]]"]
domain: [data-provider]
prerequisites: ["[[commodities]]"]
difficulty: beginner
---

The **United States Department of Agriculture ([[usda|USDA]])** is the single most important data source for agricultural commodity traders. USDA reports move markets -- the monthly WASDE release is arguably the most market-moving regularly scheduled data event in agricultural futures. Understanding what USDA publishes, when, and how to interpret it is foundational to trading [[corn]], [[wheat]], [[soybeans]], [[cotton]], [[live-cattle]], [[lean-hogs]], and other agricultural markets. (Source: [[2026-04-14-commodities-research-framework]])

## Report Cheat-Sheet

The USDA report calendar is itself a trading schedule. These are the releases worth marking, ranked by typical market impact:

| Report | Frequency | Typical timing | Impact | Primary markets |
|--------|-----------|----------------|--------|-----------------|
| **WASDE** | Monthly | ~10th-12th, 12:00 PM ET | Very high | All grains, oilseeds, cotton, livestock |
| **Prospective Plantings** | Annual | ~Mar 31 | Very high (year's biggest) | [[corn]], [[soybeans]], [[wheat]] |
| **Acreage** | Annual | ~Jun 30 | Very high | Grains, oilseeds, cotton |
| **Grain Stocks** | Quarterly | late Jan/Mar/Jun/Sep | High (esp. Sep "double day") | Grains, soybeans |
| **Crop Progress & Condition** | Weekly (May-Nov) | Mon 4:00 PM ET | Medium (cumulative) | Growing-season grains/softs |
| **Export Sales** | Weekly | Thu 8:30 AM ET | Medium | Grains, soy, cotton |
| **Export Inspections** | Weekly | Mon AM | Low-medium | Grains, soy |
| **Cattle on Feed** | Monthly | 3rd Friday | Medium | [[live-cattle]] |
| **Hogs and Pigs** | Quarterly | late Mar/Jun/Sep/Dec | Medium-high | [[lean-hogs]] |
| **Cattle Inventory** | Semi-annual | Jan 1 / Jul 1 | Medium | [[live-cattle]] |
| **Cold Storage** | Monthly | — | Low-medium | Meats |

> **The single rule:** the market trades the **surprise vs consensus**, not the absolute number. A bullish report that merely confirms expectations often sells off ("buy the rumor, sell the fact"). See [[#Trading Around USDA Reports]] and [[event-driven]].

## Major USDA Reports

### WASDE (World Agricultural Supply and Demand Estimates)

The **WASDE** is the single most market-moving agricultural report, period.

| Attribute | Detail |
|-----------|--------|
| **Frequency** | Monthly (~10th-12th of each month) |
| **Release time** | 12:00 PM ET (noon) |
| **Coverage** | US and global supply/demand for all major crops (corn, soybeans, wheat, rice, cotton) plus livestock and dairy |
| **Key metric** | **Ending stocks-to-use ratio** -- the percentage of annual consumption that remains in inventory at the end of the marketing year |

**How to interpret WASDE:**

- **Ending stocks** is the key number. Compare the USDA estimate to the market consensus (pre-report surveys from Reuters, Bloomberg, and Allendale)
- **Surprise = move.** A stocks estimate 50 million bushels below expectations for corn can move the market 2-5%
- **Revisions matter:** USDA frequently revises prior estimates. Look at the direction of revisions (are they consistently tightening or loosening?)
- **Global vs US:** Both matter, but US ending stocks tend to move CBOT futures most directly

**Stocks-to-use ratio benchmarks:**

| Crop | Tight | Comfortable | Surplus |
|------|-------|-------------|---------|
| [[corn]] | <10% | 10-15% | >15% |
| [[soybeans]] | <5% | 5-10% | >10% |
| [[wheat]] | <25% | 25-35% | >35% |
| [[cotton]] | <30% | 30-50% | >50% |

### Prospective Plantings

| Attribute | Detail |
|-----------|--------|
| **Frequency** | Annual (late March, typically March 31) |
| **What it is** | Survey-based estimate of intended planted acreage for all major crops |
| **Why it matters** | The first major signal for new-crop supply. Sets the acreage baseline for the entire growing season |

- The [[corn]]-[[soybeans]] acreage battle is the main event: acres going to corn vs soybeans determines the relative supply outlook
- Surprises of 1-2 million acres (vs expectations) in corn or soybeans regularly cause 3-5% price moves
- This report often triggers the biggest single-day moves of the year in grain futures

### Acreage Report

| Attribute | Detail |
|-----------|--------|
| **Frequency** | Annual (late June, typically June 30) |
| **What it is** | Updated acreage estimate based on actual planting data (vs March intentions) |
| **Why it matters** | Confirms or revises Prospective Plantings. Weather-delayed planting can cause significant acreage shifts |

### Crop Progress and Condition

| Attribute | Detail |
|-----------|--------|
| **Frequency** | Weekly (Monday 4:00 PM ET, May through November) |
| **What it is** | State-by-state planting progress, crop condition ratings, and harvest progress |
| **Why it matters** | Real-time supply monitoring during the growing season |

**Condition ratings** are reported as percentage of crop rated Excellent, Good, Fair, Poor, and Very Poor. The **Good-to-Excellent (G/E) rating** is the widely followed composite:

- Corn G/E > 65% = strong crop, bearish for prices
- Corn G/E < 55% = stressed crop, bullish for prices
- Week-over-week declines during pollination (July) are particularly alarming

The **Crop Condition Index (CCI)** weights the five categories (E=5, G=4, F=3, P=2, VP=1) into a single number for easier tracking.

### Grain Stocks

| Attribute | Detail |
|-----------|--------|
| **Frequency** | Quarterly (late January, March, June, September) |
| **What it is** | Actual measured stocks of corn, soybeans, wheat, and other grains in all positions (farm, off-farm) |
| **Why it matters** | Provides a reality check on WASDE implied disappearance. Deviations between Grain Stocks and WASDE projections can cause large moves |

The September 30 Grain Stocks report (released in late September) is often released on the same day as the Acreage report, creating a "double report day" that can produce extreme volatility.

### Export Inspections and Export Sales

| Report | Frequency | What It Tracks |
|--------|-----------|----------------|
| **Export Inspections** | Weekly (Monday AM) | Grain physically inspected for export at ports |
| **Export Sales** | Weekly (Thursday 8:30 AM ET) | New sales commitments and actual shipments by country |

These reports track the pace of US agricultural exports vs USDA projections. If cumulative sales/shipments are running ahead of the USDA forecast, it signals the USDA may raise export estimates (and thus lower ending stocks) in the next WASDE.

### Livestock Reports

| Report | Frequency | Coverage |
|--------|-----------|----------|
| **Cattle on Feed** | Monthly (3rd Friday) | Placements, marketings, on-feed inventory (1,000+ head feedlots) |
| **Cattle Inventory** | Semi-annual (Jan 1, Jul 1) | Total US herd, calf crop, breeding herd |
| **Hogs and Pigs** | Quarterly (late Mar, Jun, Sep, Dec) | Breeding herd, market hog inventory, pig crop, farrowing intentions |
| **Cold Storage** | Monthly | Meat in cold storage by species |
| **Weekly Slaughter** | Weekly | Head slaughtered by species |

See [[live-cattle]] and [[lean-hogs]] for detailed interpretation guidance.

(Source: [[2026-04-14-commodities-research-framework]])

## USDA Foreign Agricultural Service (FAS)

The **FAS** provides international agricultural data, essential for global supply/demand analysis:

- **Production, Supply, and Distribution (PSD) database:** Free, comprehensive database of production, consumption, trade, and stocks for all major agricultural commodities in every country. Available at apps.fas.usda.gov
- **Attaché reports:** In-country analysis from USDA agricultural attachés stationed in major producing/consuming countries
- **Global Agricultural Trade System (GATS):** US agricultural trade data by commodity and country
- **Commodity Intelligence Reports:** Satellite-based crop monitoring for major global growing regions

### API and Programmatic Access

USDA exposes several free, key-based APIs — the backbone for any systematic ag-trading pipeline:

| Portal / API | Endpoint | Auth | What it serves | Notes |
|--------------|----------|------|----------------|-------|
| **NASS Quick Stats** | quickstats.nass.usda.gov/api | Free API key | US acreage, production, stocks, yields, prices | Most granular US ag data; large queries may need pagination |
| **FAS Open Data (PSD)** | apps.fas.usda.gov/OpenData | Free API key | Global Production, Supply & Distribution; export sales | The source for non-US balance data |
| **ESR (Export Sales)** | apps.fas.usda.gov/OpenData/api/esr | Free API key | Weekly export sales by commodity and destination | Pairs with weekly Export Sales report |
| **ERS (Economic Research Service)** | ers.usda.gov | Download / API | Commodity outlook, cost-of-production, research datasets | Less real-time; analytical |
| **GATS** | apps.fas.usda.gov/gats | Web / download | US ag trade by commodity and country | Trade-flow detail |

### How Trading Systems Consume USDA Data

A typical systematic workflow consumes USDA data in three modes:

1. **Scheduled fundamental signal** — pull WASDE ending stocks and stocks-to-use via NASS/FAS APIs on release, compute the surprise vs the stored consensus, and update the fundamental score for each crop. This is a *low-frequency* signal aligned to the release calendar.
2. **In-season nowcast** — ingest weekly Crop Progress condition ratings (or the [[#Crop Progress and Condition\|CCI]]) to track the crop's trajectory between WASDE updates; week-over-week deterioration during pollination is a leading bullish signal.
3. **Event/volatility overlay** — flag known release dates from the calendar to scale risk down into reports (where [[implied-volatility]] is rich) and capture the post-report repricing. See [[event-driven]].

Because every USDA series is a *report* (weekly to annual), USDA data drives swing/position and seasonal strategies, not intraday execution. For price data to backtest the reaction, join USDA fundamentals to a futures series from [[commodity-free-tools]].

## Trading Around USDA Reports

### Pre-Report

- **Consensus estimates:** Major services (Reuters, Bloomberg, Allendale, Barchart) survey analysts before WASDE, Prospective Plantings, Grain Stocks, Cattle on Feed, and Hogs and Pigs
- **Option implied volatility:** IV typically rises 1-3 days before major USDA reports and collapses after
- **Straddle pricing:** The cost of an at-the-money straddle before a WASDE release prices the expected move

### Post-Report

- **Initial reaction vs follow-through:** The first 15-30 minutes after a USDA report often sees a knee-jerk move that may reverse. The close on report day is more significant than the first print
- **Revision tracking:** Watch how USDA revises prior estimates. Consistent one-direction revisions suggest the USDA is behind the curve
- **"Buy the rumor, sell the fact":** Markets often position ahead of expected bullish reports; if the report confirms expectations, profit-taking can reverse the initial rally

### Report Release Calendar

USDA publishes a calendar of all major report release dates at the beginning of each year:
- usda.gov/oce/commodity/wasde/wasde-report-calendar
- nass.usda.gov/Publications/Calendar

(Source: [[2026-04-14-commodities-research-framework]])

## Comparison with Other Agricultural Data Sources

| Source | Geography | Strengths | Limitations |
|--------|-----------|-----------|-------------|
| **USDA** | US-focused, global estimates | Most comprehensive, most followed | US-centric bias; global estimates can lag |
| **CONAB (Brazil)** | Brazil | Best Brazilian crop data | Portuguese-language; methodology differs from USDA |
| **ABIOVE (Brazil)** | Brazil soybeans | Detailed crush and export data | Narrower scope |
| **ROSSTAT / IKAR (Russia)** | Russia | Local crop estimates | Less transparent methodology |
| **IGC** | Global grains | Independent of USDA; different methodology | Less frequent; less granular |
| **FAO** | Global | Broadest geographic coverage | Slower publication; less trading-relevant |
| **EU MARS** | European Union | Satellite crop monitoring | EU only |

## Caveats and Data Pitfalls

USDA data is authoritative but not infallible. Trade it with these in mind:

- **Revisions and lookahead bias** — USDA revises prior estimates frequently. A backtest using only final, revised numbers leaks information that was not known at the time; use **as-released (point-in-time)** values for honest reaction studies.
- **The surprise is the signal** — the absolute level rarely matters for the immediate move; the gap to consensus (Reuters/Bloomberg/Allendale surveys) drives price. Always store the pre-report consensus.
- **Survey vs measured** — Prospective Plantings and Acreage are *survey-based intentions/estimates* and can diverge sharply from reality; Grain Stocks is *measured* and acts as a reality check that can blow up WASDE-implied disappearance.
- **Double-report days** — late-September Grain Stocks + Acreage, and overlapping WASDE/NASS releases, compound volatility; do not size as if it were a single normal report.
- **US-centric bias** — USDA's global estimates can lag local sources (CONAB for Brazil, IGC for global grains); cross-check for non-US balances. See [[#Comparison with Other Agricultural Data Sources]].
- **Methodology breaks** — definitions and survey frames change over time; long USDA histories are not always apples-to-apples.
- **Government continuity risk** — shutdowns or schedule changes can delay releases; confirm the live calendar each year.

## Related

- [[usda]] -- the agency itself
- [[corn]] -- most actively traded USDA-covered commodity
- [[wheat]] -- USDA global wheat estimates
- [[soybeans]] -- USDA soybean complex data
- [[cotton]] -- USDA cotton reports
- [[live-cattle]] -- Cattle on Feed, Cattle Inventory
- [[lean-hogs]] -- Hogs and Pigs report
- [[commodity-data-sources]] -- broader commodity data overview
- [[commodity-free-tools]] -- free tools for analysis
- [[eia-data]] -- analogous data source for energy commodities
- [[cot-report-analysis]] -- positioning overlay to pair with fundamentals
- [[seasonality]] -- seasonal patterns USDA reports anchor
- [[event-driven]] -- trading the report-day repricing
- [[implied-volatility]] -- IV behavior into and out of USDA reports
- [[supply-demand-balance]] -- the balance-sheet framework WASDE expresses

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])

---
title: "Retail Sales"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [indicators, fundamental-analysis, event-driven, market-regime]
aliases: ["Retail Sales", "Advance Retail Sales", "US Retail Sales", "Retail Sales Report"]
domain: [indicators]
prerequisites: ["[[economic-indicators]]", "[[business-cycle]]"]
difficulty: beginner
related: ["[[economic-indicators]]", "[[business-cycle]]", "[[consumer-confidence]]", "[[ism-pmi]]", "[[non-farm-payrolls]]", "[[fed-policy]]", "[[inflation]]"]
---

Retail Sales measures the total monthly dollar value of merchandise sold by retail and food-services establishments. In the United States it is published by the Census Bureau (the "Advance Monthly Retail Trade Report") around the middle of each month for the prior month. Because consumer spending drives roughly two-thirds of US GDP, retail sales is one of the most market-moving [[economic-indicators|economic indicators]] and a timely read on the health of the [[business-cycle|business cycle]].

## Key Facts

| Attribute | Detail |
|---|---|
| **Publisher** | US Census Bureau (Advance Monthly Retail Trade Report) |
| **Frequency** | Monthly, ~13 business days after month-end (mid-month) |
| **Reference period** | Prior calendar month |
| **Headline format** | Month-over-month % change, seasonally adjusted, *nominal* dollars |
| **Coverage** | Retail + food-services sales; goods + restaurants, not most services |
| **Sample** | Subsample of retailers (advance estimate), revised twice |
| **Key sub-series** | Headline, ex-autos, ex-autos-and-gas, control group ("core") |
| **GDP link** | Control group feeds the PCE goods component of GDP |
| **Type** | Coincident-to-slightly-leading; very high market sensitivity |
| **Typical reaction window** | Equities, USD, and rates move within seconds of the 8:30 ET release |

## What It Measures and How It Is Reported

The report is released as a **month-over-month percentage change**, seasonally adjusted, and is closely tracked against consensus forecasts — markets react to the *surprise*, not the absolute level. Several cuts are watched:

- **Headline retail sales** — all categories including autos and gasoline. Volatile because auto and gas spending swing with prices and incentives.
- **Ex-autos** — strips out motor-vehicle sales, which are large and lumpy.
- **Ex-autos and gas** — removes the two most price-driven categories for a cleaner demand read.
- **Control group ("core retail sales")** — excludes autos, gasoline, building materials, and food services. This is the cleanest measure of underlying consumer demand and **feeds directly into the GDP consumption estimate**, so analysts weight it heavily.

The data is reported in *nominal* dollars, so in high-[[inflation]] periods a positive headline can mask flat or falling *real* (volume) spending — a critical interpretive nuance.

## Where Retail Sales Fits Among Consumer Indicators

| Indicator | What it captures | Lead/lag vs. spending |
|---|---|---|
| **[[consumer-confidence]]** (Conference Board / UMich) | Sentiment, willingness to spend | Leads |
| **[[non-farm-payrolls]]** & wages | Income that funds spending | Coincident-to-leading |
| **Retail Sales** (this page) | Actual goods + restaurant outlays | Coincident |
| **Personal Consumption Expenditures (PCE)** | Total consumption incl. services; Fed's preferred deflator | Lags retail sales by ~2 weeks |
| **Redbook / card-spending trackers** | High-frequency same-store sales | Real-time, noisy |
| **[[ism-pmi]]** | Broad manufacturing/services activity | Leading |

Retail sales is the most *timely hard* read on the consumer — sentiment surveys come first but are soft, while PCE is broader but later. Traders use retail sales to "nowcast" the PCE and GDP prints that follow.

## Worked Example: Trading the Surprise

Suppose consensus is for **+0.3% MoM** headline retail sales and the print comes in at **+0.7%**, with the control group at **+0.6%** vs. **+0.3%** expected. The market reads this as a strong, broad-based consumer:

1. **Rates** — 2-year Treasury yields jump as traders price a more hawkish [[fed-policy|Fed]] (fewer/later cuts). Bond prices fall (see [[us-treasury-bonds]]).
2. **USD** — the dollar strengthens on the higher-rate expectation.
3. **Equities** — index reaction is regime-dependent: in a *growth-scare* regime stocks rally on the good news ("good news is good news"); in an *inflation-fighting* regime they can fall ("good news is bad news" because it delays rate cuts). Consumer-discretionary names typically outperform staples regardless.
4. **The fade** — because the advance estimate is a subsample, a big surprise is often partly reversed in next month's revision, so disciplined traders avoid over-extrapolating a single print.

The mirror case — a **−0.2%** miss against **+0.3%** expected — flips all of the above and can stoke recession fears, especially if the control group is also soft.

## Trading and Market Impact

A stronger-than-expected report signals robust consumer demand: typically bullish for equities (especially [[consumer-confidence|consumer discretionary]] retailers and cyclicals), supportive of the US dollar, and bearish for bonds as it raises growth and rate-hike expectations. A weak print does the opposite and can stoke recession fears. In an inflationary regime the reaction is more nuanced — a hot number can be read as evidence the [[fed-policy|Federal Reserve]] must stay restrictive, pressuring both stocks and bonds.

Retail sales sits within a cluster of consumer indicators. It is best read alongside [[consumer-confidence]] (sentiment, which leads spending), [[non-farm-payrolls]] (income, which funds spending), and [[ism-pmi]] (broader activity). Single months are noisy; the 3-month moving average and the year-over-year trend in the control group give a more reliable signal of consumer momentum for [[sector-rotation]] and macro positioning.

## Limitations

The advance estimate is based on a subsample and is revised in subsequent months, sometimes materially. It captures goods and food services but excludes most services spending (housing, healthcare, travel), which dominates the modern consumer economy — so it is an incomplete proxy for total consumption. Seasonal adjustment around holidays and shifting promotional calendars (e.g., the migration of holiday shopping into October) can distort month-to-month readings.

## Sources

- US Census Bureau — *Advance Monthly Sales for Retail and Food Services* (official release and methodology), census.gov.
- Federal Reserve Bank of St. Louis (FRED) — Advance Retail Sales historical series (RSAFS, RSXFS control group).
- US Bureau of Economic Analysis — documentation linking retail control-group data to the Personal Consumption Expenditures component of GDP.

## Related

- [[economic-indicators]] -- broader catalog of macro indicators
- [[consumer-confidence]] -- sentiment that leads spending
- [[non-farm-payrolls]] -- the income side of consumer demand
- [[ism-pmi]] -- complementary leading activity indicator
- [[business-cycle]] -- the cycle retail sales helps track
- [[fed-policy]] -- the Fed watches consumer strength for rate decisions

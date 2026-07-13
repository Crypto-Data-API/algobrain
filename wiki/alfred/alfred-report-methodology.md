---
title: "Alfred Report Methodology"
type: concept
created: 2026-04-09
updated: 2026-04-09
status: good
tags: [alfred, fundamental-analysis, valuation, methodology, education]
aliases: ["Alfred Report Template", "Alfred Verdict System"]
domain: [fundamental-analysis, valuation]
difficulty: intermediate
related: ["[[alfred]]", "[[alfred-fundamental-analysis]]", "[[alfred-reports-overview]]", "[[fundamental-analysis]]", "[[exchange-data-sources]]"]
---

How Alfred produces investment reports — the verdict system, report templates, and analysis framework. For metric formulas and calculations, see [[alfred-fundamental-analysis]].

## Alfred Verdict System

Every company report includes an Alfred Verdict — a multi-dimensional rating summarising the investment case:

| Dimension | Possible Values | What It Measures |
|-----------|----------------|------------------|
| **VALUATION** | Undervalued / Fair Value / Fully Priced / Overvalued | Whether the stock price reflects intrinsic value (DCF, relative valuation, P/E vs history) |
| **FORECASTS** | Good / Uncertain / Poor | Analyst consensus and Alfred's projection confidence |
| **OWNER** (already holds) | Buy More / Hold / Sell | Recommended action for current shareholders |
| **NON-OWNER** (considering) | Buy / Wait / Avoid | Recommended action for prospective buyers |
| **RISK** | Low / Medium / High | Overall risk assessment (financial strength, sector, geographic, currency) |

The verdict is derived from the quantitative analysis across all report sections — it is not a standalone opinion but a summary of the data.

Some reports also include a **Poker Hand** analogy (e.g. "Pocket Jacks" = strong holding but not all-in material), adding a qualitative flavour to the rating.

## Full Report Template (17 Sections)

The full report is Alfred's comprehensive analysis format, typically 10-15 pages. For worked examples, see [[alfred-report-maq-asx|Macquarie Technology (most detailed)]], [[alfred-report-nst-asx|Northern Star]], or [[alfred-report-clg-asx|Close The Loop]]. Sections:

1. **Header** — Report date, company name, ticker, GICS industry classification, services, operating locations
2. **Alfred Verdict** — The 5-dimension rating grid (see above)
3. **Company Description** — Business model, founding, recent developments, strategic questions
4. **Valuation Metrics** — Historical table (typically 2020-2024): Price, DCF Price, P/E Ratio, Dividend Yield %, Franking %, with sector/benchmark comparisons. Narrative analysis of each metric.
5. **Management Matters** — ROE %, ROA %, management compensation, tenure, insider transactions. Assessment of management effectiveness.
6. **Financial Strength (Solvency)** — D/E Ratio, Cash on Hand, Current Ratio, Quick Ratio, Net Interest Cover Ratio, Net Operating Cash Flow. Narrative analysis of financial health.
7. **Profit & Loss Statement** — Gross Profit %, Operating Margin %, Revenue (TTM with growth %), EBITDA (TTM with growth %), EPS (with CAGR). Growth rate analysis.
8. **Acquisitions Table** — Date, cost, locations, financial impact of each acquisition (if applicable)
9. **Geographic/Segment Distribution** — Revenue breakdown by country/segment with trend analysis
10. **Shares Information** — Shares outstanding, dilution %, insider ownership %, institutional ownership %, top 20 holdings %, ETF participation count, top shareholders listing
11. **Sector/Industry Information** — Market size, growth projections, top ASX competitors, peer comparison overview
12. **Peer Comparisons** — Detailed tables grouped by sub-sector (e.g. Data Centres, Cloud Services, Telecoms). Metrics: P/E, Gross Margin, Dividend Yield, ROE, ROA, D/E, Interest Cover, Current Ratio, Free Cash Flow, Revenue Share, CAGR metrics, trailing returns.
13. **Risk Analysis** — Currency risk, geographic concentration, market-specific risks, risk-adjusted returns vs benchmarks
14. **Technical Analysis** — Volatility (Beta, Standard Deviation), Liquidity (Volume, RSI, Bid/Ask spread), Trend, Range, Support/Resistance levels
15. **Forecasts** — 4-5 year forward projections: Price, Revenue, EBITDA, EPS, P/E (median analyst values)
16. **Company Calendar** — Upcoming reporting dates and events
17. **Appendix** — Data sources with URLs, disclaimers, methodology notes

### Data Sources

Full reports cite their data from:
- Company annual and interim reports (via [[exchange-data-sources|ASX/EDGAR]])
- TradingView fundamentals
- EOD Historical Data API
- MarketIndex statistics
- SelfWealth ratios
- AlphaSpread DCF/relative valuations
- Simply Wall St share information
- Yahoo Finance price history
- Morningstar trailing returns

## 1-Pager Template

The condensed format for quick analysis:

1. **Header** — "1 PAGE REPORT" with date, company name, ticker, GICS classification
2. **Company Overview** — 2-3 paragraphs: business description, sector trends, competitive advantage/moat, share count, reporting currencies, dividend status
3. **Fundamentals Summary Table** — Compact table spanning 2020-Current with CAGR:
   - Valuation: Price, DCF Est, Intrinsic Est, P/E, Dividend Yield %
   - Profitability: Revenue, EPS
   - Management: ROE %
   - Solvency: D/E Ratio
4. **Alfred's Analysis** — Brief narrative analysis per section
5. **Pros / Cons** — Two-column summary of bull vs bear case

## Sector/Commodity Report Template

For industry-level analysis:

1. **Sector Snapshot Header** — Date, GICS classification
2. **Sector Definition** — What companies in the sector do
3. **Industry Averages Table** — Key metrics averaged across all sector stocks: P/E, GP %, Dividend Yield, ROE, ROA, D/E, Current Ratio, Revenue/EBITDA/EPS CAGR
4. **Company Comparison Matrix** — All stocks listed with individual metrics for direct comparison
5. **Commentary** — Sector observations, data quality notes, notable outliers

For commodity reports specifically, additional sections cover:
- Commodity overview and history
- Price performance (historical tables, comparison to inflation)
- Supply and demand analysis (production by country, demand by use case)
- Peer comparisons (major global producers)
- Alternatives analysis
- Forecast and Alfred's verdict

## Benchmarks Framework

Alfred uses a tiered benchmarking approach:

| Benchmark | Purpose |
|-----------|---------|
| **ASX Average** | Baseline comparison for Australian stocks (e.g. ASX avg ROE 13.4%, Dividend Yield 3.8%) |
| **Sector Average** | Industry-specific benchmark (e.g. Gold sub-industry P/E 39.19) |
| **Peer Group** | Company-specific peers chosen by business segment overlap |
| **Alfred Default** | Standard thresholds: P/E < 20, D/E < 0.5, ROE > 13.4%, Current Ratio > 2.0, Net Cover > 2.0 |

The GICS (Global Industry Classification Standard) framework is used for sector taxonomy — 11 sectors, 25 industry groups, 74 industries, 163 sub-industries.

## Confidence and Disclaimers

All data is provided for information purposes only, not investment advice. Key conventions:
- Financial data is actual as at fiscal year end unless stated otherwise
- "Current" means YTD, else latest reported TTM
- All prices in AUD unless stated (USD for US stocks)
- Forecasts use median analyst values
- CAGR calculations are 5-year unless stated

## Related

- [[alfred]] — Alfred AI assistant overview
- [[alfred-fundamental-analysis]] — Metric formulas and worked example
- [[alfred-reports-overview]] — Index of all Alfred reports
- [[fundamental-analysis]] — General fundamental analysis concepts
- [[exchange-data-sources]] — Official data endpoints used by Alfred

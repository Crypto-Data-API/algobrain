---
title: "OptionMetrics"
type: entity
created: 2026-05-06
updated: 2026-06-10
status: good
tags: [data-provider, options, stocks, backtesting]
entity_type: company
founded: 1999
headquarters: "New York, USA"
website: https://optionmetrics.com
aliases: ["IvyDB", "OptionMetrics IvyDB"]
related:
  - "[[opra]]"
  - "[[orats]]"
  - "[[polygon-io]]"
  - "[[databento]]"
  - "[[algoseek]]"
---

# OptionMetrics

OptionMetrics is the institutional historical options data vendor behind IvyDB, the de facto reference dataset for academic and quantitative options research. Founded in 1999 by David J. Hait, Ph.D. and headquartered in New York, it matters to traders because nearly every published finding about options anomalies, volatility risk premia, and skew dynamics — the research that strategies are built on — was derived from this data.

## Overview

OptionMetrics is the institutional-grade historical options database widely regarded as the gold standard for academic and quantitative options research. The company was founded in 1999 by David J. Hait, who remains CEO; in April 2021, private equity firm Leeds Equity Partners made a growth investment in OptionMetrics (the first platform investment of Leeds Equity Partners VII, L.P.), with Hait continuing as CEO and board member. The firm marked 25 years of operation in 2024. Its flagship product, IvyDB US, provides cleaned end-of-day US equity and index options data going back to January 1996, with pre-calculated implied volatilities, Greeks, interest rate curves, dividend forecasts, and corporate-action adjustments. The company has expanded coverage to Europe (IvyDB Europe), Asia (IvyDB Asia), and futures options (IvyDB Futures), and now offers an intraday product with snapshots taken at 10:00, 14:00, and 15:45 ET, plus a signed-volume dataset estimating customer-initiated buy/sell flow.

## Pricing

- **Institutional-only**: no public price list; access is sold via annual licenses to hedge funds, banks, asset managers, and academic institutions
- **Typical academic license**: ~$15K–$25K/year for a single university with student access through WRDS (Wharton Research Data Services)
- **Commercial license**: ~$50K–$200K+/year depending on dataset breadth, history depth, intraday vs end-of-day, and number of users
- **WRDS access**: most quantitative finance PhD programs subscribe via WRDS, providing students free access during research
- **No retail tier**: not accessible to individual traders directly

## What You Get

- **IvyDB US**: end-of-day options prices, OI, volume, and Greeks for every listed US equity and index option since 1996
- **Pre-calculated Greeks and IV**: delta, gamma, vega, theta, and implied volatility computed using a consistent methodology across the full history
- **Volatility surface**: standardized constant-maturity volatilities for skew, term structure, and surface analysis
- **Corporate action adjustments**: clean splits, mergers, special dividends, and option contract adjustments — critical for backtesting
- **Interest rate curves**: zero-coupon yield curves needed for accurate option pricing
- **Dividend forecasts**: projected and historical dividends used in pricing models
- **IvyDB Intraday**: snapshots at 10:00 AM, 2:00 PM, and 3:45 PM ET for intraday research without the cost of full tick data
- **Signed Volume**: customer buy/sell flow estimates derived from quote-rule classification — useful for order-flow research

## Use Cases / Who Uses It

- **Academic researchers**: virtually every published options-pricing paper since the early 2000s uses IvyDB; cited in thousands of journal articles
- **Quantitative hedge funds**: AQR, Two Sigma, Citadel, Millennium, and similar shops use OptionMetrics as their historical research baseline
- **Asset managers and pensions**: long-horizon volatility risk premium and tail-hedging research
- **Risk teams**: stress testing and historical scenario analysis on options books
- **Volatility arbitrage funds**: skew, term structure, and dispersion strategy research
- **Universities**: Wharton, MIT, Chicago Booth, NYU Stern, and most top finance programs subscribe via WRDS

## Strengths and Limitations

**Strengths:**
- **Deepest clean history**: 30 years of survivor-bias-free options data — no other commercial product matches this
- **Methodological consistency**: Greeks and IV computed the same way for the entire history, enabling apples-to-apples cross-time comparisons
- **Academic credibility**: the de facto reference dataset for peer-reviewed options research
- **Corporate action handling**: the painful work of adjusting for splits, special dividends, and contract adjustments is already done
- **Coverage breadth**: US, Europe, Asia, and futures options under one consistent schema

**Limitations:**
- **Cost**: institutional pricing puts it out of reach for individual traders and small firms (compare with [[orats]] or [[polygon-io]] for retail-accessible options data)
- **End-of-day primary**: even the intraday product has only 3 snapshots per day — not suitable for tick-level microstructure or HFT research
- **Lag**: data is delivered T+1 or later, not real-time
- **No execution layer**: research-only; you still need a separate broker, OMS, and live data feed to trade
- **Vendor lock-in**: schemas and methodologies are proprietary; migrating away is non-trivial

## Related

- [[opra]] — the underlying source feed OptionMetrics processes
- [[orats]] — more affordable proprietary options analytics with intraday data
- [[polygon-io]] — retail-accessible alternative for raw OPRA-derived options data
- [[databento]] — institutional historical and real-time tick data
- [[algoseek]] — competing institutional historical options data vendor
- [[implied-volatility]] — IvyDB's IV calculation is a research standard
- [[volatility-surface]] — built directly from OptionMetrics standardized vol grids
- [[options-greeks]] — pre-calculated in every IvyDB record
- [[backtesting]] — IvyDB is the default historical dataset for options strategy backtests

## Sources

- OptionMetrics corporate site, About Us: https://optionmetrics.com/about-us/ (founding 1999, David J. Hait, IvyDB product line)
- Business Wire / PR Newswire, "Leeds Equity Partners and OptionMetrics Partner to Expand Options and Futures Data Solutions", 30 April 2021: https://www.businesswire.com/news/home/20210430005117/en/Leeds-Equity-Partners-and-OptionMetrics-Partner-to-Expand-Options-and-Futures-Data-Solutions
- Yahoo Finance, "OptionMetrics Celebrates Quarter of a Century..." (2024 25th-anniversary release): https://finance.yahoo.com/news/optionmetrics-celebrates-quarter-century-providing-123500838.html
- Traders Magazine, "CEO CHAT: David Hait, OptionMetrics": https://www.tradersmagazine.com/departments/options/ceo-chat-david-hait-optionmetrics/
- Verified via Perplexity and web search, 2026-06-10

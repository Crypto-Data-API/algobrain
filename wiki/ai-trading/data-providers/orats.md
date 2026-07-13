---
title: "ORATS (Option Research & Technology Services)"
type: entity
created: 2026-05-06
updated: 2026-06-10
status: good
tags: [data-provider, options, stocks, volatility, backtesting]
entity_type: company
founded: 2001
headquarters: "Chicago, Illinois, USA"
website: https://orats.com
aliases: ["ORATS", "Option Research and Technology Services"]
related:
  - "[[optionmetrics]]"
  - "[[opra]]"
  - "[[polygon-io]]"
  - "[[unusual-whales]]"
  - "[[market-chameleon]]"
---

# ORATS (Option Research & Technology Services)

ORATS is a Chicago-based options data and analytics firm founded in 2001 by former CBOE floor market maker Matt Amberson. For traders it occupies a sweet spot: institutional-quality smoothed implied volatility surfaces, scanners, and a backtester at prices a serious retail or small-fund options trader can justify.

## Overview

ORATS is a proprietary options analytics platform that bridges the gap between institutional-pricing vendors like [[optionmetrics]] and free retail tools. Founded in 2001 by veteran options market maker Matt Amberson — who built the methodology out of procedures developed for his CBOE market-making operation — ORATS specializes in cleaned options data, proprietary smoothed implied volatilities, and customizable scanners covering 5,000+ optionable US symbols. Since August 2020, ORATS has delivered 1-minute intraday Greeks, IVs, and theoretical values — a granularity that previously required institutional infrastructure. The platform combines a research-grade historical archive with real-time scanning, an API that integrates with backtesting and execution systems, and an "ORATS University" education arm. As of 2025–2026 ORATS has served thousands of retail traders, hedge funds, and institutional clients over two-plus decades, sources underlying market data from Barchart, and has added broker integrations and paper trading alongside its strategy optimizer and trade-ideas tooling; it also publishes widely-referenced industry comparisons such as its "Best Option Scanners of 2025" review.

## Pricing

- **Data API – Backtest**: ~$129/mo for end-of-day historical chains and Greeks back to 2007
- **Data API – Live**: ~$199/mo for delayed real-time data feeds with Greeks and IV
- **Data API – Real-Time**: ~$499/mo+ for streaming real-time Greeks and IV
- **Wheel & Scanner subscriptions**: $30–$100/mo retail tiers with web-based scanners and educational content
- **Intraday history**: separate add-on for 1-minute Greeks history since August 2020
- **Enterprise / institutional**: custom pricing for funds and prop desks
- Free trials are typically available on most tiers

## What You Get

- **Smoothed implied volatility surface**: proprietary fitting that filters quote noise and produces stable IVs across strikes and expiries
- **1-minute intraday Greeks**: delta, gamma, vega, theta and theoretical values updated every minute, archived since August 2020
- **Historical end-of-day chains**: cleaned options data back to 2007 with corporate-action adjustments
- **Scanner**: rank/filter 5,000+ symbols by IV rank, IV percentile, skew, term structure, earnings dates, dividend dates, and dozens of proprietary metrics
- **Proprietary indicators**: delta cost analytics, slope-of-skew, contango/backwardation measures, IV term structure ratios
- **Backtester**: built-in options strategy backtester for spreads, condors, calendars, and custom multi-leg structures
- **API access**: REST endpoints used by quant researchers, fintech apps, and execution platforms
- **ORATS University**: structured education on options analytics, IV trading, and strategy construction

## Use Cases / Who Uses It

- **Active retail options traders**: scanning thousands of symbols for IV-based opportunities daily
- **Volatility traders**: identifying skew, term structure, and surface mispricings on individual names
- **Earnings traders**: ORATS is widely used for ranking earnings IV crush opportunities
- **Quantitative researchers at small funds**: institutional-quality smoothed IV without an OptionMetrics budget
- **Options education businesses**: many YouTube and newsletter educators reference ORATS data and screenshots
- **Backtesting developers**: minute-level Greeks since 2020 enable realistic intraday backtests of 0DTE and short-dated strategies — see [[0dte-trading]]
- **Fintech apps**: integrate ORATS API for options analytics in consumer-facing products

## Strengths and Limitations

**Strengths:**
- **Smoothed IVs are research-grade**: proprietary surface fitting reduces noise compared with raw OPRA mid-quote IVs
- **Minute-level Greeks history**: rare at this price point — competitors charge multiples for similar granularity
- **Scanner depth**: dozens of pre-built filters and the ability to build custom screens across 5,000+ underlyings
- **Strong API and documentation**: well-suited to programmatic workflows and automation
- **Founder credibility**: Matt Amberson's market-making background informs the methodology

**Limitations:**
- **Not a substitute for OPRA tick data**: 1-minute resolution is excellent for strategy work but inadequate for microstructure or HFT research — see [[databento]] or [[polygon-io]] for tick-level
- **US equity options focus**: limited coverage of futures options, FX options, or international markets
- **Pricing climbs quickly**: stacking real-time, intraday history, and scanner tiers can reach $700+/mo
- **No execution layer**: analytics only; pair with [[interactive-brokers]] or similar for trading
- **Smaller ecosystem**: less third-party tooling around ORATS than around [[polygon-io]] or [[bloomberg-terminal]]

## Related

- [[optionmetrics]] — institutional alternative with deeper history but EOD-focused
- [[opra]] — the underlying consolidated feed ORATS processes
- [[polygon-io]] — alternative for raw OPRA data without ORATS analytics
- [[unusual-whales]] — complementary retail options-flow tool
- [[market-chameleon]] — competing options analytics platform
- [[spotgamma]] — gamma exposure analytics, complements ORATS for index options
- [[implied-volatility]] — ORATS smoothed IV is a key product
- [[volatility-surface]] — ORATS surface fitting is its core differentiator
- [[options-greeks]] — minute-level Greeks since 2020
- [[backtesting]] — ORATS includes a built-in options strategy backtester
- [[0dte-trading]] — intraday Greeks history enables 0DTE research

## Sources

- ORATS corporate site, About: https://orats.com/about (founded 2001 by Matt Amberson, Chicago; market-making origins)
- Barchart case study on ORATS: https://www.barchart.com/solutions/case-studies/orats (Barchart as underlying market-data source)
- John Lothian News interview, "Understanding Market Movements to Make Options Trades: Matt Amberson, Founder of ORATS and Cboe trader": https://johnlothiannews.com/matt-amberson/
- ORATS pricing and API documentation: https://orats.com (tier pricing as listed; check current rates)
- ORATS blog, "Best Option Scanners of 2025": https://orats.com/blog/best-option-scanners-of-2025
- Verified via Perplexity and web search, 2026-06-10

---
title: "Finnhub"
type: entity
created: 2026-05-06
updated: 2026-06-10
status: good
tags: [data-provider, stocks, options, crypto, forex]
entity_type: company
founded: 2018
headquarters: "New York, USA"
website: https://finnhub.io
aliases: ["Finnhub.io"]
related:
  - "[[polygon-io]]"
  - "[[alpha-vantage]]"
  - "[[yahoo-finance]]"
  - "[[eod-historical-data]]"
  - "[[opra]]"
---

# Finnhub

Finnhub is a freemium financial data API founded in 2018 and headquartered in New York, serving real-time and historical equities, options, fundamentals, news, and alternative data to developers and quant traders. For traders it is one of the most common "first APIs" — the free tier (60 calls/minute, including WebSocket streaming for up to 50 symbols) is generous enough to power real screeners and bots, while paid bundles scale into production fintech use.

## Overview

Finnhub is a freemium financial data API providing real-time and historical US equity quotes, options chains, fundamentals, news, alternative data, and global market coverage through REST and WebSocket endpoints. It occupies the middle ground between free providers like [[yahoo-finance]] and institutional vendors like [[bloomberg-terminal]] or [[optionmetrics]] — affordable enough for solo developers and small quant shops, but with broad enough coverage to power production fintech apps. The API surfaces US options chains with bid/ask, volume, open interest, and implied volatility, sourced downstream from [[opra]] via licensed redistributors.

## Pricing

(Verified June 2026 against finnhub.io/pricing — Finnhub sells data as per-market/per-dataset bundles rather than simple tiers.)

- **Free**: 60 API calls/minute, real-time US quotes, company news, basic fundamentals, SEC filings, WebSocket streaming for up to 50 symbols — no credit card required; usable for prototyping and low-volume production
- **Individual data bundles**: from ~$49.99/month per market or dataset (billed quarterly), e.g. real-time US stock market data
- **Larger stock-data bundles**: ~$129.99/month for broader US market data packages (billed quarterly)
- **Fundamentals, estimates, and alternative-data bundles**: priced separately per dataset; stacking bundles is how costs grow
- **Enterprise**: custom pricing for white-label, redistribution, and high-volume use cases
- Annual plans typically discounted vs monthly/quarterly billing

## What You Get

- **US equity options chains**: bid/ask, last, volume, OI, implied volatility, Greeks for all listed strikes and expiries
- **Real-time and historical equities**: quotes, trades, candles at tick/minute/daily resolution
- **Global coverage**: 60+ stock exchanges including European, Asian, and emerging markets
- **Fundamentals**: company financials, earnings, ownership, insider transactions, ESG scores
- **Alternative data**: earnings call transcripts, sentiment scores, lobbying, government spending, patent filings
- **News API**: real-time company and market news with sentiment classification
- **Crypto and forex**: spot prices and historical data alongside equities
- **WebSocket streaming**: real-time trade and quote feeds
- **Python, Go, and JavaScript SDKs**: official client libraries with good documentation

## Use Cases / Who Uses It

- **Solo algo traders**: build personal trading bots and screeners without enterprise data costs
- **Fintech startups**: power MVP and early-stage products before justifying [[polygon-io]] or [[bloomberg-terminal]] spend
- **Small quant shops**: combine Finnhub equities and options with proprietary models
- **Research and education**: free tier is generous enough for tutorials, courses, and academic prototypes
- **Sentiment and alt-data researchers**: leverage transcripts, lobbying, and patent data not available on most retail platforms
- **App developers**: financial dashboards, portfolio trackers, and news aggregators consume Finnhub via REST
- **Backtesting workflows**: pair with local storage for historical strategy research — see [[backtesting]]

## Strengths and Limitations

**Strengths:**
- **Generous free tier**: 60 calls/minute and broad endpoint coverage make it one of the best free APIs for prototyping
- **Breadth of data types**: combines equities, options, fundamentals, alternative data, and news under one API
- **Global coverage**: more international exchanges than [[polygon-io]] or [[alpha-vantage]]
- **Modern API design**: REST and WebSocket with well-documented SDKs
- **Alternative datasets**: transcripts, sentiment, and government data are unusual at this price point

**Limitations:**
- **Not OPRA tick-grade for options**: options data is closer to consolidated/snapshot quality than raw [[opra]] tick stream — for microstructure work use [[polygon-io]], [[databento]], or direct OPRA
- **Rate limits bite quickly above the free tier**: high-volume scanning often pushes you to Standard or Premium
- **Latency**: not designed for sub-second execution decisions; better for analytics and signal generation
- **Data quality variability**: occasional gaps and corrections compared with institutional vendors
- **Smaller historical depth on some endpoints**: years of options history are limited compared with [[optionmetrics]] or [[orats]]

## Related

- [[polygon-io]] — direct competitor, deeper OPRA-derived options data
- [[alpha-vantage]] — similar freemium tier, weaker on options
- [[yahoo-finance]] — free baseline, less reliable and no formal SLA
- [[eod-historical-data]] — affordable EOD-focused alternative
- [[opra]] — upstream source of US options data
- [[options-greeks]] — Finnhub returns Greeks for chain endpoints
- [[implied-volatility]] — included in options snapshots
- [[backtesting]] — Finnhub is a common data source for retail backtesting
- [[interactive-brokers]] — pair with Finnhub for execution

## Sources

- Finnhub pricing page: https://finnhub.io/pricing (plan structure and bundle pricing)
- Finnhub API rate-limit documentation: https://finnhub.io/docs/api/rate-limit (free tier 60 calls/minute)
- Finnhub API documentation: https://finnhub.io/docs/api (endpoint coverage: equities, options, fundamentals, alternative data, WebSocket)
- Third-party API comparisons (2025–2026) confirming free-tier scope and 60+ exchange coverage, e.g. ksred.com "Financial Data APIs Compared" and DataGlobeHub Finnhub profile
- Verified via Perplexity and web search, 2026-06-10

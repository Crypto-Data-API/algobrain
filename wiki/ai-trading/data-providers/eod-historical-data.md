---
title: "EOD Historical Data"
type: entity
created: 2026-05-06
updated: 2026-06-10
status: good
tags: [data-provider, options]
entity_type: company
website: https://eodhd.com
aliases: ["EOD HD", "EODHD", "EODHistoricalData", "eodhistoricaldata.com"]
related:
  - "[[finnhub]]"
  - "[[polygon-io]]"
  - "[[alpha-vantage]]"
  - "[[yahoo-finance]]"
---

# EOD Historical Data

## Overview

EOD Historical Data (now branded **EODHD**, primary domain eodhd.com) is an affordable subscription-based market data API focused on end-of-day equities, ETFs, indices, and US options data. Coverage spans 70+ global exchanges with 30+ years of price history on US equities, plus daily options chains for US-listed underlyings. It targets the cost-conscious segment of the market: traders who do not need tick-level data, but want clean, reliable daily summaries delivered through a developer-friendly API at a fraction of the cost of optionmetrics, [[databento]], or [[bloomberg-terminal]].

## Pricing (verified June 2026, eodhd.com/pricing)

- **Free**: $0 — 20 API calls/day, limited data, for prototyping only
- **EOD Historical Data (All World)**: $19.99/mo ($199/yr) — end-of-day prices on all supported exchanges, 100,000 API calls/day
- **EOD + Intraday (All World Extended)**: $29.99/mo ($299.90/yr) — adds intraday history
- **Fundamentals Data Feed**: $59.99/mo ($599.90/yr) — global fundamentals
- **All-In-One Package**: $99.99/mo ($999.90/yr) — bundles EOD, intraday, fundamentals, calendar, and bonds data (was promoted around $80/mo in earlier years; prices have risen)
- **Options Data add-on**: separate subscription tier for US options EOD chains and Greeks
- **API call quotas**: 100,000 calls/day on paid plans

EODHD has also added AI/developer tooling: an **EODHD ChatGPT Assistant** and an **MCP (Model Context Protocol) server**, making it one of the first budget data vendors with first-class LLM-agent integration — relevant for AI-driven research pipelines.

## What You Get

- **End-of-day prices**: open/high/low/close/volume for 70+ global exchanges and 150,000+ tickers worldwide. US history runs from the earliest available data (e.g., Ford from June 1972); most non-US exchanges from January 2000; US 1-minute intraday from 2004; major US company fundamentals from 1985
- **US options EOD**: daily snapshots of full options chains with bid/ask, volume, OI, implied volatility, and Greeks
- **Fundamentals**: income statements, balance sheets, cash flows, ratios, earnings, splits, and dividends
- **Corporate actions**: splits, dividends, mergers, and ticker changes — adjusted price series available
- **Index constituents**: S&P 500, Nasdaq 100, Russell, FTSE, DAX, Nikkei, and many other index memberships with history
- **Intraday history**: 1-minute bars for many tickers, useful for swing-strategy research
- **Macro and economic data**: GDP, CPI, employment, central bank rates across major economies
- **Bulk download endpoints**: efficient for backfilling local databases without hitting per-call limits
- **REST API with broad SDK support**: Python, R, Excel, Google Sheets connectors

## Use Cases / Who Uses It

- **Daily-bar systematic traders**: build EOD strategies on US and international equities without paying for tick data
- **Swing and position traders**: end-of-day data is sufficient for multi-day to multi-week timeframes
- **Fundamentals-driven quants**: combine global fundamentals with EOD prices for value, quality, and momentum factor research
- **Options swing traders**: daily chain snapshots support trend-following and IV-rank strategies — see [[implied-volatility]]
- **Index and ETF researchers**: historical constituents enable accurate survivor-bias-free backtests
- **Cost-conscious developers**: those building paid tools where data cost must stay below a small fraction of revenue
- **Academic and student projects**: cheap enough for personal research budgets
- **Backfill for proprietary databases**: bulk endpoints make it practical for one-time historical loads — see [[backtesting]]

## Strengths and Limitations

**Strengths:**
- **Price-to-coverage ratio**: hard to beat for global EOD breadth at the price point
- **Bulk download support**: efficient backfilling without choking on per-call rate limits
- **Long history**: 30+ years on US equities, with corporate-action adjustments
- **Broad ecosystem connectors**: official integrations with Excel, Google Sheets, R, Python make adoption frictionless
- **Stable, mature API**: been operating since 2018 with consistent endpoints

**Limitations:**
- **Not real-time**: "live" endpoints are delayed; for real-time use [[polygon-io]], [[finnhub]], or direct opra vendors
- **No tick or sub-minute data**: 1-minute bars are the highest resolution
- **Options coverage is daily-only**: insufficient for intraday options strategies, 0DTE work (see [[0dte-trading]]), or microstructure research
- **Greeks are computed at end-of-day snapshots**: less precise than orats smoothed-surface methodology
- **Rate limits on smaller plans**: 100K calls/day is generous for EOD work but tight for high-frequency scanning
- **No execution layer**: pair with interactive-brokers or another broker for trading

## Related

- [[finnhub]] — overlapping freemium competitor with broader real-time coverage
- [[polygon-io]] — step up for tick-level and real-time options
- [[alpha-vantage]] — similar tier, more limited international coverage
- [[yahoo-finance]] — free baseline that EOD HD improves on with reliability and SLAs
- [[backtesting]] — EOD HD is a common cost-effective historical data source
- [[implied-volatility]] — included in daily options snapshots
- [[options-greeks]] — computed at EOD on chain data

## Sources

- EODHD pricing page (plans and quotas verified) — https://eodhd.com/pricing
- EODHD documentation (coverage, history depth, ChatGPT Assistant, MCP server) — https://eodhd.com
- Verified via web fetch, 2026-06-10

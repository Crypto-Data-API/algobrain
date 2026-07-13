---
title: "Free Data Sources"
type: reference
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [data, data-providers, free]
aliases: ["Free Market Data"]
related: ["[[data-sources-overview]]", "[[paid-data-providers]]", "[[crypto-data-sources]]", "[[macro-data-sources]]"]
---

# Free Data Sources

Free providers, ranked by usefulness for serious research. Most are usable for prototyping but have one or more biases that disqualify them for production research. The biases are documented per-source so you can decide when each one is acceptable.

This page is the free-tier slice of the [[data-sources-overview]] hub. For paid/institutional vendors see [[paid-data-providers]]; for the crypto-specific catalog (which is unusually free-friendly) see [[crypto-data-sources]]; for macro detail see [[macro-data-sources]]; for fundamentals see [[fundamental-data-sources]].

## The Free-Data Bargain

Free data is a genuine accelerant for learning and prototyping, but almost every free source carries at least one structural bias that silently corrupts a backtest. The two that kill the most strategies are **[[survivorship-bias]]** (dead instruments are missing) and **[[lookahead-bias]]** (the value you fetch is the latest revision, not what was knowable on the date). The discipline is simple: prototype on free data, but re-validate on a clean, point-in-time, survivorship-free dataset before allocating capital (see [Common Free-Data Pitfalls](#common-free-data-pitfalls)).

## Provider Quick-Reference

A consolidated index of every free provider on this page, with its asset class, what you actually get, the dominant bias to watch, and whether it is safe for deployable backtests. Detail follows in the sections below.

| Provider | Asset class | What you get | Dominant bias / caveat | Backtest-safe? |
|---|---|---|---|---|
| Yahoo Finance / `yfinance` | Equities | Daily OHLCV, some intraday, basic fundamentals | Survivorship + restated fundamentals | No |
| Stooq | Equities | CSV history, some delisted | Inconsistent quality, no API | Partial (backfill) |
| Alpha Vantage (free) | Equities/FX/crypto | OHLCV, indicators, basic fundamentals | Severe rate limits, restated | No |
| IEX Cloud | Equities | (Discontinued Aug 2024) | Defunct | No |
| Tiingo (free) | Equities | EOD US, IEX intraday, news | Universe limits, restated | Prototype |
| EOD Historical Data (free) | Equities (global) | EOD prices, fundamentals | Free tier too thin | No |
| SEC EDGAR | Fundamentals | Raw filings (10-K/Q, 8-K, 13F) | Hard to parse; XBRL/HTML | Yes (point-in-time) |
| FRED | Macro | Hundreds of thousands of series | Revised series (lookahead) | No (use ALFRED) |
| ALFRED | Macro (vintage) | Point-in-time series | Smaller coverage, complex | Yes (point-in-time) |
| BEA | Macro | GDP, income, trade | Clunky API | Yes (vintages) |
| BLS | Macro | Employment, CPI, PPI, wages | Obscure series IDs | Partial |
| World Bank / IMF / OECD | Macro (intl) | Cross-country series | Low frequency, lagged | Background |
| Exchange public APIs | Crypto | Full depth + trades per venue | Single-venue, depth varies | Yes (live), partial (history) |
| CoinGecko / CoinMarketCap | Crypto | Aggregated price, market cap | Aggregated, some interpolation | No (execution) |
| CoinAPI / CryptoCompare (free) | Crypto | Normalized cross-venue | Free tier too thin | Prototype |
| Block explorers + analytics free tiers | Crypto (on-chain) | Wallet/flow/TVL queries | Free tiers limited | Prototype |
| Yahoo options chains | Options | Fragmentary chains | No history, laggy | No (see [[options-data-sources]]) |
| NewsAPI / GDELT / Google News RSS | News | Headlines, some full text | No entity tagging, rate limits | Prototype |
| Reddit / Twitter (X) | Sentiment | Restricted public APIs | Free tiers heavily gated (2024-26) | No |

## Equities

### Yahoo Finance / `yfinance`

The default. Easy to access via the `yfinance` Python library. Provides daily OHLCV plus some intraday and limited fundamentals.

**Pros:** Free, fast, broad coverage, easy to use, decades of history.

**Cons (critical):**
- **Survivorship-biased universe** — you can only fetch tickers that currently exist. Delisted, bankrupt, and renamed companies are silently absent.
- **Adjustment errors** — split/dividend adjustments are sometimes wrong on edge cases
- **Restated fundamentals** — financial data is the latest version, not point-in-time
- **No corporate action history**
- **Rate limited** — heavy use will get you throttled or blocked
- **Inconsistent timezone handling**

**Use for:** Prototyping, learning, single-stock analysis, quick checks. Never for backtesting a long-only equity strategy you intend to deploy.

### Stooq

Free historical data including some delisted symbols. CSV downloads.

**Pros:** Free, includes some delisted history, broader coverage than Yahoo for some markets.

**Cons:** Inconsistent quality, no API, no fundamentals, formats vary by market.

**Use for:** Spot-checking Yahoo data, historical backfill where Yahoo is missing.

### Alpha Vantage (Free Tier)

Free API with rate limits (5 calls/minute, 500/day on free tier). Provides OHLCV, FX, crypto, basic fundamentals, technical indicators.

**Pros:** Real API with documentation, broader than Yahoo, includes some intraday.

**Cons:** Severe rate limits on free tier, survivorship issues, fundamentals are restated.

**Use for:** Small-scale automated retrieval, learning API patterns. Upgrade to paid tier for serious work.

### IEX Cloud (Free / Pay-as-you-go)

Free tier and very cheap usage-based pricing. Real-time and historical market data sourced from the IEX exchange plus consolidated tape.

**Pros:** Clean API, real-time available, fair pricing.

**Cons:** **Discontinued** — IEX Cloud shut down August 2024. Mentioned because it was a popular free option and you may see it referenced in older tutorials.

### Tiingo (Free Tier)

Free tier provides EOD US equity data, historical IEX intraday, basic news.

**Pros:** Cleaner than Yahoo, real API, decent free tier.

**Cons:** Universe limitations, fundamentals are restated.

**Use for:** Better-than-Yahoo prototyping. Worth paying for the cheap tier ($10-$30/mo) for serious retail research.

### EOD Historical Data (Free Tier)

Limited free tier; broader paid tiers. Provides EOD prices, fundamentals, ETFs across global markets.

**Pros:** Wide global coverage, decent quality on developed markets.

**Cons:** Free tier is too limited for serious work; paid tiers needed.

### SEC EDGAR

Not data per se but the source-of-truth for US fundamentals. Direct download of filings (10-K, 10-Q, 8-K, 13F).

**Pros:** Free, authoritative, point-in-time by definition (filings are dated when filed)

**Cons:** Painful to parse — XBRL or HTML, schema changes over time, no convenience layer.

**Use for:** When you absolutely need point-in-time fundamentals and can't pay for Compustat. The `python-edgar` and similar libraries make this slightly easier.

## Macro / Economic Data

### FRED (Federal Reserve Economic Data)

Maintained by the St. Louis Fed. Hundreds of thousands of US and global economic series.

**Pros:** Free, clean API, great documentation, covers everything from CPI to housing to international rates.

**Cons:** **Most series are revised** — the value you fetch is the latest revision, not the value that was originally published. This is a *severe lookahead bias* for any strategy that trades macro releases.

**Use for:** Background research, understanding macro context, slow-moving macro features. Never for backtests where the publication date matters.

### ALFRED (Archival FRED)

The vintage version of FRED. Provides each series as it was originally reported on each release date.

**Pros:** Free, point-in-time, clean API.

**Cons:** Smaller coverage than FRED (not every series has vintage data), more complex to query.

**Use for:** Macro backtests where you need to use what was actually known on each historical date. ALFRED is usually the right choice over FRED for serious quant research.

### BEA (Bureau of Economic Analysis)

GDP, personal income, trade flows, regional accounts. Direct from the source.

**Pros:** Authoritative, includes vintages and revisions.

**Cons:** API exists but is clunky.

### BLS (Bureau of Labor Statistics)

Employment, CPI, PPI, wages, productivity.

**Pros:** Authoritative, free API.

**Cons:** Series IDs are obscure; documentation requires patience.

### World Bank / IMF / OECD

International macro data. Free APIs.

**Pros:** Broad cross-country coverage.

**Cons:** Lower frequency, longer publication lag, less granular.

## Crypto

### Exchange Public APIs

Binance, Coinbase, Kraken, OKX, Bybit, Bitfinex, etc. all expose public REST and WebSocket APIs that return historical and real-time market data without authentication.

**Pros:** Free, complete depth of book and trades for the venue, real-time WebSocket feeds.

**Cons:** Single-venue (you have to query multiple to get a full picture), historical depth varies (some only keep 1-3 years), rate limits, schema differences across venues.

**Use for:** Most crypto research can be done entirely on free exchange APIs. The cost of a paid crypto data vendor is mostly buying *normalized* historical, not new information.

### CoinGecko / CoinMarketCap

Free APIs for price aggregation across exchanges, market cap, supply data.

**Pros:** Free, clean API, broad coin coverage.

**Cons:** Aggregated only — no per-venue depth or trades. Unsuitable for execution research. Some data is interpolated.

**Use for:** Portfolio-level price tracking, market cap sorting, universe construction.

### CoinAPI / CryptoCompare (Free Tiers)

Aggregated multi-venue crypto data. Free tiers exist with rate limits.

**Pros:** Already-normalized cross-venue data.

**Cons:** Free tiers are too limited for serious work; quality varies.

### On-Chain Data

Blockchain explorers (Etherscan, Blockchair, Solscan) and free tiers of analytics platforms (Glassnode free, Dune Analytics, Nansen public dashboards) provide free on-chain data for major chains.

**Use for:** Wallet tracking, exchange flow analysis, DeFi TVL, NFT activity. The free tiers are usually enough for individual research; production strategies often need paid tiers.

## Options

There are no good free options data sources. The free options chains on Yahoo Finance are fragmentary, often lag, and have no historical depth. Anyone serious about options research has to pay for OPRA-derived data — see [[options-data-sources]].

## News and Sentiment

### News APIs (Free Tiers)
NewsAPI, GDELT, Google News RSS — all provide some level of free news access.

**Pros:** Free, broad coverage.

**Cons:** Rate limits, no entity tagging, quality varies.

### Reddit / Twitter (X)
Public APIs — both have heavily restricted free tiers as of 2024-2026. Twitter's free tier is essentially unusable; Reddit has limited free API access via the data dump or PRAW with rate limits.

## How Trading and AI Systems Consume Free Data

Free data is the default fuel for prototypes, dashboards, and AI research agents. Matching the consumer to the source avoids both wasted effort and silent bias.

| Consumer | Latency need | Preferred free sources | Trap to avoid |
|---|---|---|---|
| **Prototype backtests** | Offline | Yahoo/Tiingo (equities), exchange APIs (crypto), ALFRED (macro) | Treating FRED/Yahoo results as deployable |
| **AI/LLM research agents** | Seconds | FRED API, CoinGecko, DefiLlama, news RSS, SEC EDGAR full-text | Feeding raw XBRL/L2 instead of summaries |
| **Live monitoring dashboards** | Seconds–min | Exchange APIs, CoinGecko, BLS/BEA release calendars | Hitting rate limits with naive polling |
| **Fundamental screens** | Hours–days | SEC EDGAR (point-in-time), Tiingo | Restated fundamentals from convenience APIs |

Practical notes:

- **Point-in-time vs. convenience.** For anything where *when you knew it* matters, prefer the authoritative point-in-time source: ALFRED over FRED for macro (see the [ALFRED](#alfred-archival-fred) section below), SEC EDGAR over restated-fundamentals APIs. Convenience APIs trade correctness for ease.
- **AI agents prefer summarized, low-cardinality inputs.** An LLM reasons better over FRED's CPI series or a DefiLlama TVL snapshot than over a 10-K's raw XBRL. Pre-summarize before feeding a model. Alfred's own pipelines lean on REST JSON endpoints (FRED, CoinGecko, DefiLlama) for exactly this reason.
- **Rate limits force caching.** Free tiers throttle aggressively (Alpha Vantage 5/min, Yahoo soft-blocks heavy use). A local cache or scheduled batch pull is mandatory past prototyping.
- **Always cross-source.** Free adjusted prices and corporate actions are error-prone; spot-check against a second free source before trusting any single one.

## Common Free-Data Pitfalls

If you build a strategy on free data and intend to deploy it, *always* re-validate on a point-in-time, survivorship-free dataset before allocating capital. Specifically:

1. Re-test the universe with delisted instruments included
2. Re-test fundamentals with point-in-time vintages
3. Re-test macro features with ALFRED-style vintage data
4. Compare adjusted prices to a second source
5. Spot-check corporate actions

Strategies that survive this re-validation are real. Strategies that don't were artifacts of the free-data biases.

### Bias → Source → Fix

| Bias | Where it bites | Fix |
|---|---|---|
| [[survivorship-bias]] | Yahoo, Alpha Vantage universes | Use a delisting-inclusive dataset; add dead tickers |
| [[lookahead-bias]] | FRED (revised series) | Use ALFRED vintages |
| Restated fundamentals | Convenience APIs (Yahoo, AV) | Use SEC EDGAR point-in-time filings |
| Adjustment errors | Yahoo split/dividend edge cases | Cross-check against a second source |
| Missing corporate actions | Most free equity sources | Spot-check; supplement from EDGAR |
| Aggregation/interpolation | CoinGecko/CMC crypto prices | Use per-venue exchange APIs for execution |
| Rate-limit gaps | Heavy free-tier pulls | Cache; schedule; or upgrade tier |

## Sources

- [[book-quantitative-trading-ernest-chan]] — Chan on retail data sources
- [[lookahead-bias]] — why FRED is dangerous
- [[survivorship-bias]] — why Yahoo is dangerous
- General market knowledge; no specific wiki source ingested yet.

## Related

- [[data-sources-overview]]
- [[paid-data-providers]]
- [[crypto-data-sources]]
- [[macro-data-sources]]
- [[fundamental-data-sources]]
- [[options-data-sources]]
- [[survivorship-bias]], [[lookahead-bias]]

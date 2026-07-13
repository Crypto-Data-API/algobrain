---
title: "CryptoQuant"
type: source
created: 2026-04-22
updated: 2026-06-12
status: good
tags: [data-provider, on-chain-analytics, crypto, bitcoin]
source_type: data
source_url: "https://cryptoquant.com"
source_author: "Ki Young Ju"
aliases: ["CryptoQuant", "Crypto Quant"]
related: ["[[crypto-data-sources]]", "[[bitcoin]]", "[[ethereum]]", "[[on-chain-analysis]]", "[[exchange-api-reference]]", "[[alternative-me]]", "[[fundamental-analysis]]"]
---

CryptoQuant is a leading on-chain analytics platform founded by Ki Young Ju that provides exchange flow data, miner metrics, whale tracking, and derivative indicators for cryptocurrency markets. The platform aggregates blockchain data from major exchanges and mining pools to produce metrics that serve as leading indicators for [[bitcoin|BTC]] and [[ethereum|ETH]] price movements. CryptoQuant offers both free and paid tiers, with the free tier providing access to a subset of charts and indicators.

## Overview

On-chain analytics leverages the transparency of public blockchains to track fund flows that would be invisible in traditional markets. CryptoQuant specializes in translating raw blockchain data into actionable trading metrics — particularly exchange inflow/outflow data, which can signal buying or selling pressure before it appears in price action.

## Key Metrics for Traders

### Exchange Flow Metrics

| Metric | Definition | Trading Signal |
|--------|-----------|---------------|
| **Exchange Reserve** | Total BTC/ETH held on exchange wallets | Declining reserves = accumulation (bullish); rising reserves = distribution (bearish) |
| **Exchange Inflow** | BTC/ETH being deposited to exchanges | Spike in inflows = potential sell pressure incoming |
| **Exchange Outflow** | BTC/ETH being withdrawn from exchanges | Large outflows = holders moving to cold storage (bullish) |
| **Exchange Whale Ratio** | Top-10 inflow transactions / total inflows | High ratio (>0.5) = whales driving deposits, potential selling |
| **Exchange Netflow** | Inflows minus outflows | Persistent negative netflow = supply leaving exchanges (bullish) |
| **Stablecoin Exchange Flow** | USDT/USDC flowing onto exchanges | Stablecoin inflows = dry powder ready to buy (bullish) |

### Miner Metrics

| Metric | Definition | Trading Signal |
|--------|-----------|---------------|
| **Miners' Position Index (MPI)** | Miner outflows relative to 1-year moving average | MPI > 2 signals miners selling heavily (bearish pressure) |
| **Hash Rate** | Total network computational power | Sustained hash rate growth = miner confidence (bullish long-term) |
| **Miner Revenue** | Block rewards + transaction fees | Miner revenue stress → potential forced selling after [[bitcoin-halving\|halving]] events |

### Profitability Metrics

| Metric | Definition | Trading Signal |
|--------|-----------|---------------|
| **SOPR (Spent Output Profit Ratio)** | Ratio of sold price vs. paid price for moved coins | SOPR < 1 = coins moving at a loss (capitulation signal); SOPR > 1 = profit-taking |
| **aSOPR (Adjusted SOPR)** | SOPR excluding coins moved within 1 hour | Filters out exchange internal transfers for cleaner signal |
| **NUPL (Net Unrealized Profit/Loss)** | Aggregate unrealized P&L of all BTC holders | NUPL > 0.75 = euphoria zone; NUPL < 0 = capitulation zone |
| **MVRV Ratio** | Market Value / Realized Value | MVRV > 3.5 historically signals tops; MVRV < 1 signals bottoms |

### Fund Flow & Institutional Metrics

| Metric | Definition | Trading Signal |
|--------|-----------|---------------|
| **Fund Flow Ratio** | Exchange inflows / total on-chain volume | High ratio = more activity directed at exchanges (distribution) |
| **Stablecoin Supply Ratio (SSR)** | BTC market cap / stablecoin market cap | Low SSR = high stablecoin buying power relative to BTC (bullish) |
| **Coinbase Premium** | BTC price on Coinbase vs. Binance | Positive premium = US institutional buying; negative = US selling |

## Trading Applications

### 1. Exchange Reserve Strategy

Track the 30-day moving average of total [[bitcoin|BTC]] exchange reserves:
- **Declining reserves** (BTC leaving exchanges) combined with rising price = confirmed accumulation trend. This preceded major rallies in 2020-2021.
- **Rising reserves** (BTC entering exchanges) combined with declining price = distribution phase. This characterized the mid-2022 bear market.

### 2. Whale Alert Trading

Monitor the **Exchange Whale Ratio** alongside [[funding-rate|funding rates]] on [[perpetual-futures]]:
- Whale ratio spike + positive funding = leveraged longs may be about to get dumped on
- Whale ratio low + negative funding = potential short squeeze setup

### 3. SOPR Retest Strategy

During bull markets, SOPR dipping to 1.0 (break-even) and bouncing has historically indicated a buying opportunity — holders refuse to sell at a loss, confirming the bull trend. A sustained break below 1.0 in a bull market may signal trend reversal.

### 4. Stablecoin Inflow Divergence

If [[bitcoin]] price is declining but stablecoin exchange inflows are rising, this divergence suggests buyers are positioning. Combined with [[alternative-me|Fear & Greed Index]] readings below 20, this produces a higher-conviction contrarian buy signal.

## Data Access

| Tier | Price | Features |
|------|-------|----------|
| **Basic** | $0 | Limited chart access, delayed/lower-resolution data, basic indicators |
| **Advanced** | ~$39/month | Pro charts, full historical data, 5 custom alerts |
| **Professional** | ~$109/month | Adds 20 alerts + Data API access (up to 24H resolution) |
| **Premium** | ~$799/month | 100 alerts + Data API at block-level resolution, institutional metrics |

Pricing as of June 2026 (verify current rates at cryptoquant.com/pricing — annual billing is cheaper than monthly). API documentation: `https://cryptoquant.com/docs`

## Limitations

1. **BTC-centric**: Most robust data is for [[bitcoin]]; [[ethereum]] coverage is growing but less comprehensive; altcoin coverage is limited
2. **Exchange coverage gaps**: Not all exchanges share wallet data; some flows are estimated
3. **Lag**: On-chain data reflects completed transactions — by the time a whale deposit confirms, the sell may already be executing
4. **Privacy coins**: Cannot track flows for Monero, Zcash (shielded), and other [[privacy-coins|privacy-focused]] assets
5. **Exchange wallet misidentification**: Occasionally, wallet labeling can be incorrect, producing false signals

## Founder

**Ki Young Ju** — Founded CryptoQuant and is active on [[twitter|X/Twitter]] where he shares on-chain analysis and has become one of the most followed crypto analysts. His exchange flow analysis during major market moves has driven significant attention to CryptoQuant as a platform.

## Related

- [[crypto-data-sources]] — Full catalog of crypto data providers
- [[bitcoin]] — Primary asset tracked by CryptoQuant
- [[ethereum]] — Second most-tracked asset
- [[on-chain-analysis]] — The analytical framework underlying CryptoQuant's data
- [[alternative-me]] — Sentiment data to combine with on-chain signals
- [[exchange-api-reference]] — Exchange APIs for direct data access
- [[deribit]] — Options data to cross-reference with on-chain flows

## Sources

_Content based on CryptoQuant public documentation, platform interface, and on-chain analytics methodology. No raw sources ingested._

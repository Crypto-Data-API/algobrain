---
title: "Mira"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["MIRA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://mira.network/"
related: ["[[crypto-markets]]", "[[base]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]"]
---

# Mira

**Mira** (MIRA) is the decentralized verification network that makes AI outputs trustworthy. By transforming AI-generated content into verifiable claims and using blockchain consensus across multiple AI models, Mira eliminates the need for human verification. It ranks **#956** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MIRA |
| **Market Cap Rank** | #956 |
| **Market Cap** | $15.02M |
| **Current Price** | $0.053155 |
| **Categories** | Artificial Intelligence (AI), BNB Chain Ecosystem, Base Ecosystem, Binance Alpha Spotlight, AI Framework, Base Native |
| **Website** | [https://mira.network/](https://mira.network/) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Overview

Mira is the decentralized verification network that makes AI outputs trustworthy. By transforming AI-generated content into verifiable claims and using blockchain consensus across multiple AI models, Mira eliminates the need for human verification. This breakthrough enables AI to operate autonomously in high-stakes domains like healthcare, finance, and legal services. With over 1M users across ecosystem apps like Klok and Learnrite, Mira is building the essential trust layer for the AI revolution.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 268.44M MIRA |
| **Total Supply** | 1.00B MIRA |
| **Max Supply** | 1.00B MIRA |
| **Fully Diluted Valuation** | $78.46M |
| **Market Cap / FDV Ratio** | 0.27 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2.68 (2025-09-26) |
| **Current vs ATH** | -97.07% |
| **All-Time Low** | $0.0724 (2026-03-30) |
| **Current vs ATL** | +8.32% |
| **24h Change** | -3.24% |
| **7d Change** | +1.65% |
| **30d Change** | -4.67% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Base

### Contract Addresses

| Chain | Address |
|---|---|
| Base | `0x7aafd31a321d3627b30a8e2171264b56852187fe` |
| Binance Smart Chain | `0x7839fbfd09dae4d0f15bfb36b8f16f7898fbe684` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | MIRA/USDT | N/A |
| Kraken | MIRA/EUR | N/A |
| Upbit | MIRA/KRW | N/A |
| Bitget | MIRA/USDT | N/A |
| KuCoin | MIRA/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://mira.network/](https://mira.network/) |
| **Twitter** | [@miranetwork](https://twitter.com/miranetwork) |
| **Telegram** | [1](https://t.me/1) |
| **Discord** | [https://discord.com/invite/mira-network](https://discord.com/invite/mira-network) |
| **Whitepaper** | [https://mira.network/research/mira-whitepaper.pdf](https://mira.network/research/mira-whitepaper.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.20M |
| **Market Cap Rank** | #956 |
| **24h Range** | $0.0782 — $0.0812 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

MIRA is tradable on **Binance** — both **spot** (MIRA/USDT) and a **USD-margined perpetual** with funding, open interest, and liquidation data. It is **not listed on Hyperliquid**, so Binance is the primary leveraged venue for the token. With a small market cap (rank ~1020) and thin 24h volume, leveraged books are shallow: large orders move price, and available notional/OI caps are modest. This concentration means execution should lean on spot for size, use limit orders to avoid slippage, and keep perp position sizing conservative — a single venue outage or listing change materially affects liquidity, and crowded leverage clears quickly through liquidation clusters.

### Applicable strategies

- [[liquidation-cascade-fade]] — thin perp depth means forced-liquidation wicks overshoot on MIRA, offering mean-revert entries after cascades exhaust.
- [[crowded-long-funding-fade]] — as a small AI-narrative token, MIRA is prone to over-leveraged longs; persistently positive funding flags fade setups.
- [[breakout-and-retest]] — low float and narrative-driven demand produce clean breakouts from range that can be entered on the retest.
- [[rsi-mean-reversion]] — down ~97% from ATH and range-bound, MIRA oscillates sharply, favoring oversold/overbought reversion on spot.
- [[news-trading]] — price is highly sensitive to AI-verification narrative headlines, ecosystem app (Klok/Learnrite) milestones, and Binance Alpha attention.
- [[token-unlock-supply-event]] — with MC/FDV ~0.27 and ~732M MIRA still to enter circulation, unlock schedules are a recurring supply-driven catalyst.

### Volatility & regime character

MIRA is a small-cap AI-infrastructure token with high beta to broad crypto risk and pronounced reflexivity around the AI narrative. It is heavily correlated to BTC/ETH risk-on/risk-off swings but amplifies moves given its low float and thin liquidity. Expect large intraday ranges, sharp narrative-driven spikes, and rapid mean reversion — closer in behavior to a speculative altcoin than an established large-cap.

### Risk flags

- **Liquidity/venue concentration** — Binance dominates leveraged trading; no Hyperliquid listing limits venue redundancy and cross-venue arbitrage.
- **Unlocks/emissions** — MC/FDV ~0.27 implies substantial future supply; scheduled unlocks can pressure price and funding.
- **Narrative dependence** — valuation hinges on the AI-verification thesis and ecosystem adoption; narrative fatigue can trigger sustained drawdowns.
- **Small-cap fragility** — thin depth makes the token vulnerable to manipulation, gap risk, and liquidation-driven volatility.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=MIRAUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=MIRAUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=MIRA` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=MIRA` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=MIRAUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=MIRAUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=MIRA"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[base]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

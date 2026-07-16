---
title: "OpenEden"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["EDEN"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://openeden.com/"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[cash-and-carry]]", "[[funding-rate-harvest]]"]
---

# OpenEden

**OpenEden** (EDEN) offers 24/7, on-chain access to tokenized US Treasury securities for Web3 CFOs, DAO treasury managers, and buy-side institutional investors seeking low-risk, highly liquid crypto cash management solutions.

We are the first tokenized real-world asset (RWA) issuer to receive a Moody's "A-bf" bond fund rating. It ranks **#878** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | EDEN |
| **Market Cap Rank** | #878 |
| **Market Cap** | $17.36M |
| **Current Price** | $0.0432 |
| **Categories** | Real World Assets (RWA), RWA Protocol |
| **Website** | [https://openeden.com/](https://openeden.com/) |

---

## Overview

OpenEden offers 24/7, on-chain access to tokenized US Treasury securities for Web3 CFOs, DAO treasury managers, and buy-side institutional investors seeking low-risk, highly liquid crypto cash management solutions.

We are the first tokenized real-world asset (RWA) issuer to receive a Moody's "A-bf" bond fund rating. Since launching in early 2023, OpenEden has already become the largest issuer of tokenied US Treasuries in Asia and Europe.

As part of our end-to-end tokenization stack, OpenEden is directly involved through its licensed investment management entity which manages its BVI-registered professional fund, which issues the $TBILL tokens and custodises the underlying assets with licensed third party custodians.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 401.57M EDEN |
| **Total Supply** | 1.00B EDEN |
| **Max Supply** | 1.00B EDEN |
| **Fully Diluted Valuation** | $43.23M |
| **Market Cap / FDV Ratio** | 0.40 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.31 (2025-09-30) |
| **Current vs ATH** | -96.71% |
| **All-Time Low** | $0.0259 (2026-03-30) |
| **Current vs ATL** | +66.97% |
| **24h Change** | +1.27% |
| **7d Change** | +0.02% |
| **30d Change** | -4.78% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0x235b6fe22b4642ada16d311855c49ce7de260841` |
| Ethereum | `0x24a3d725c37a8d1a66eb87f0e5d07fe67c120035` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | EDEN/USDT | N/A |
| Bitget | EDEN/USDT | N/A |
| KuCoin | EDEN/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://openeden.com/](https://openeden.com/) |
| **Twitter** | [@OpenEden_X](https://twitter.com/OpenEden_X) |
| **Telegram** | [openeden](https://t.me/openeden) (2,443 members) |
| **Whitepaper** | [https://docs.openeden.com/](https://docs.openeden.com/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.53M |
| **Market Cap Rank** | #878 |
| **24h Range** | $0.0424 — $0.0441 |
| **CoinGecko Sentiment** | 0% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

EDEN is tradable on **Binance** — both spot (EDEN/USDT) and a **USD-margined perpetual** carrying funding, open interest, and liquidation dynamics. It is **NOT** listed on Hyperliquid, so Binance is the **primary leveraged venue** and the reference for funding/OI/liquidation signals. Secondary spot listings exist on Bitget and KuCoin, but leveraged flow, price discovery, and derivatives data concentrate on Binance. With a sub-$20M market cap and thin ~$1.5M/day spot volume, the perp order book is shallow: leverage should be modest, sizing kept small, and entries staged with limit orders to avoid slippage. Funding and OI on the Binance perp are the cleanest read on positioning, and liquidation clusters can move a book this size disproportionately.

### Applicable strategies

- [[funding-rate-harvest]] — a low-float RWA microcap perp often prints persistently skewed funding; harvest it by holding the opposite side while delta-hedging spot.
- [[cash-and-carry]] — buy Binance spot EDEN against a short in the USD-M perp to capture positive basis/funding with market-neutral exposure.
- [[crowded-long-funding-fade]] — RWA-narrative pumps in a thin book draw crowded longs; fade extended positive funding for mean-reversion.
- [[liquidation-cascade-fade]] — low liquidity makes stop runs violent; fade forced-liquidation flushes when OI drops sharply into a wick.
- [[rsi-mean-reversion]] — with EDEN pinned far below ATH and range-bound recently, RSI extremes on the daily offer reversion entries.
- [[breakout-and-retest]] — narrative-driven RWA moves can trigger clean breakouts from the tight range; enter on the retest to control risk.

### Volatility & regime character

EDEN is a **small-cap RWA/DeFi infrastructure token** (rank ~881, ~$17M cap) with high idiosyncratic volatility and reflexive, narrative-driven moves tied to the tokenized-Treasury/RWA theme rather than steady BTC/ETH beta. Sitting ~97% below its ATH and range-bound recently, it behaves like a low-liquidity microcap: sharp squeezes on RWA catalysts, quick fades once flow exhausts. Correlation to majors is loose; moves are dominated by token-specific supply and narrative rotation.

### Risk flags

- **Liquidity/venue concentration** — leveraged trading and derivatives data are concentrated on Binance; a delisting or venue outage would sharply impair execution.
- **Unlocks/emissions** — only ~40% of supply circulates (MC/FDV ~0.40); future unlocks toward the 1B max supply are a persistent overhang.
- **Narrative dependence** — price hinges on the RWA/tokenized-Treasury narrative; sentiment reversals hit a thin book hard (CoinGecko sentiment 0% positive).
- **Regulatory** — as a tokenized-securities/RWA issuer, EDEN carries elevated regulatory sensitivity that can drive abrupt repricing.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=EDENUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=EDENUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=EDEN` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=EDEN` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=EDENUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=EDENUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=EDEN"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

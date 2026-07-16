---
title: "Newton Protocol"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["NEWT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://newt.foundation/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Newton Protocol

**Newton Protocol** (NEWT) is a cryptocurrency. It ranks **#975** by market capitalization. The Newton Protocol is a decentralized infrastructure layer for verifiable onchain automation and secure agent authorization. It enables protocols, DAOs, and users to execute complex actions through verifiable agents, without relying on centralized bots or offchain coordination.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NEWT |
| **Market Cap Rank** | #975 |
| **Market Cap** | $14.44M |
| **Current Price** | $0.0672 |
| **Categories** | Artificial Intelligence (AI), BNB Chain Ecosystem, Ethereum Ecosystem, Binance HODLer Airdrops, DeFAI |
| **Website** | [https://newt.foundation/](https://newt.foundation/) |

---

## Overview

The Newton Protocol is a decentralized infrastructure layer for verifiable onchain automation and secure agent authorization. It enables protocols, DAOs, and users to execute complex actions through verifiable agents, without relying on centralized bots or offchain coordination. Users can securely authorize agents to act on their behalf using programmable permissions, ensuring that actions occur only under conditions they approve. By combining trusted execution environments (TEEs), zero-knowledge proofs, and a modular agent architecture, Newton Protocol brings automation fully onchain, enhancing transparency, composability, and trust.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 215.00M NEWT |
| **Total Supply** | 1.00B NEWT |
| **Max Supply** | 1.00B NEWT |
| **Fully Diluted Valuation** | $67.14M |
| **Market Cap / FDV Ratio** | 0.22 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.8206 (2025-06-24) |
| **Current vs ATH** | -91.82% |
| **All-Time Low** | $0.0605 (2026-02-06) |
| **Current vs ATL** | +11.00% |
| **24h Change** | -0.52% |
| **7d Change** | -2.26% |
| **30d Change** | -1.65% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xd0ec028a3d21533fdd200838f39c85b03679285d` |
| Binance Smart Chain | `0xb8a677e6d805c8d743e6f14c8bc9c19305b5defc` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | NEWT/USDT | N/A |
| Upbit | NEWT/KRW | N/A |
| Bitget | NEWT/USDT | N/A |
| KuCoin | NEWT/USDT | N/A |
| Crypto.com Exchange | NEWT/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://newt.foundation/](https://newt.foundation/) |
| **Twitter** | [@newtfoundation](https://twitter.com/newtfoundation) |
| **Whitepaper** | [https://blog.newt.foundation/the-litepaper/](https://blog.newt.foundation/the-litepaper/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.80M |
| **Market Cap Rank** | #975 |
| **24h Range** | $0.0667 — $0.0684 |
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

NEWT is tradable on **Binance** across both **spot** (NEWT/USDT) and a **USD-margined perpetual**, giving access to funding rates, open interest, and liquidation data. It is **not** listed on Hyperliquid, so **Binance is the primary leveraged venue**. With a sub-$5M daily volume and a market-cap rank near #1173, on-book depth is thin: leverage is available but order-book slippage and liquidation-driven gaps are the binding constraints. Because leveraged flow, funding, and OI all concentrate on a single venue (Binance USD-M), execution and position sizing should assume limited depth — scale in with limit orders, keep clip sizes small relative to visible book, and treat Binance funding/OI as the definitive derivatives signal rather than a cross-venue composite.

### Applicable strategies

- [[funding-rate-harvest]] — a single deep perp venue (Binance) makes systematic funding collection on NEWT straightforward when the perp trades at a persistent premium/discount to spot.
- [[cash-and-carry]] — long Binance spot NEWT against a short USD-M perp captures basis while neutralizing directional risk in a thin, high-FDV token.
- [[liquidation-cascade-fade]] — low float and concentrated leverage make NEWT prone to sharp liquidation wicks that mean-revert, offering fade entries after forced-selling exhausts.
- [[oi-confirmed-trend]] — pairing Binance open-interest expansion with price direction helps separate genuine NEWT moves from thin-book noise.
- [[volatility-breakout]] — a tight recent range near the ATL sets up clean volatility-expansion breakouts once momentum returns to this low-cap.
- [[token-unlock-supply-event]] — with only ~22% of max supply circulating (MC/FDV 0.22), scheduled emissions and unlocks are a recurring, tradable supply catalyst.

### Volatility & regime character

NEWT is a **small-cap** ($14M MC) infrastructure/DeFAI token (verifiable onchain automation, AI-agent narrative) that trades with high beta to BTC/ETH risk appetite and amplified reflexivity typical of low-float alts. Price sits ~92% below its 2025 ATH and just above its ATL, so regime is currently range-bound and liquidity-starved, punctuated by narrative-driven (AI/DeFAI) impulse moves. Directional conviction should be sized down given the wide MC/FDV gap and thin book.

### Risk flags

- **Liquidity/venue concentration** — leveraged trading, funding, and OI concentrate on Binance USD-M; a single-venue disruption removes the primary market.
- **Unlocks/emissions** — MC/FDV of 0.22 means ~78% of supply is not yet circulating; future unlocks are a structural sell-pressure risk.
- **Narrative dependence** — valuation leans on the AI-agent/DeFAI narrative; rotation out of that theme can compress the token sharply.
- **Stale/low data quality** — asset is outside the CoinGecko top 1000 with cached figures; treat on-page snapshots as potentially stale when sizing.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=NEWTUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=NEWTUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=NEWT` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=NEWT` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=NEWTUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=NEWTUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=NEWT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

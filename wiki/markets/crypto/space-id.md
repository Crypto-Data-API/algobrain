---
title: "SPACE ID"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, nft, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["ID"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://space.id/"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]"]
---

# SPACE ID

**SPACE ID** (ID) is building a universal name service network with a one-stop identity platform to discover, register, trade, manage web3 domains. It ranks **#947** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ID |
| **Market Cap Rank** | #947 |
| **Market Cap** | $15.27M |
| **Current Price** | $0.0355 |
| **Categories** | NFT, Binance Launchpad |
| **Website** | [https://space.id/](https://space.id/) |

---

## Overview

SPACE ID is building a universal name service network with a one-stop identity platform to discover, register, trade, manage web3 domains. It also includes a Web3 Name SDK &amp; API for developers across blockchains and provides a multi-chain name service for everyone to easily build and create a web3 identity.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 430.51M ID |
| **Total Supply** | 2.00B ID |
| **Max Supply** | 2.00B ID |
| **Fully Diluted Valuation** | $70.82M |
| **Market Cap / FDV Ratio** | 0.22 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.84 (2024-03-17) |
| **Current vs ATH** | -98.07% |
| **All-Time Low** | $0.0232 (2026-06-06) |
| **Current vs ATL** | +53.45% |
| **24h Change** | +5.84% |
| **7d Change** | -4.89% |
| **30d Change** | +28.49% |
| **1y Change** | -80.42% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0x2dff88a56767223a5529ea5960da7a3f5f766406` |
| Ethereum | `0x2dff88a56767223a5529ea5960da7a3f5f766406` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ID/USDT | N/A |
| Upbit | ID/KRW | N/A |
| KuCoin | ID/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://space.id/](https://space.id/) |
| **Twitter** | [@SpaceIDProtocol](https://twitter.com/SpaceIDProtocol) |
| **Telegram** | [spaceid_news](https://t.me/spaceid_news) (32,946 members) |
| **Whitepaper** | [https://docs.space.id/](https://docs.space.id/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $10.92M |
| **Market Cap Rank** | #947 |
| **24h Range** | $0.0333 — $0.0356 |
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

ID is tradable on **Binance** with both **spot** (ID/USDT) and a **USD-margined perpetual** contract that exposes funding, open interest, and liquidation data. It is **NOT listed on Hyperliquid**, so Binance is the primary leveraged venue and the anchor for derivatives-based execution. Additional spot liquidity sits on Upbit (ID/KRW) and KuCoin, but leveraged flow, price discovery, and funding pressure concentrate on Binance USD-M. With a small ~$15M cap and ~$11M daily volume, book depth is thin: size positions modestly, prefer limit/VWAP execution over aggressive market orders, and expect wider slippage and sharper liquidation-driven wicks than in large-caps. Concentration on a single perp venue means Binance funding and OI are the cleanest signals for positioning and crowding.

### Applicable strategies

- [[funding-rate-harvest]] — collect funding on the Binance USD-M perp when the small-cap ID contract skews persistently positive or negative.
- [[crowded-long-funding-fade]] — fade over-leveraged longs when Binance funding spikes rich against thin spot demand for a low-cap name-service token.
- [[liquidation-cascade-fade]] — thin ID books amplify cascade wicks; fade forced liquidations back toward the mean after over-extended flushes.
- [[oi-confirmed-trend]] — use rising Binance open interest to confirm directional moves and distinguish real trends from low-liquidity noise.
- [[range-mean-reversion]] — ID chops in defined ranges between catalysts; mean-revert extremes toward the range midpoint.
- [[narrative-trading]] — position around web3-domain / decentralized-identity narrative cycles and ecosystem announcements that drive ID demand.

### Volatility & regime character

ID is a **small-cap** altcoin (rank ~950) in the web3 identity / name-service niche with high beta to broad crypto risk. Price action is reflexive and news-sensitive: it trades ~98% below its 2024 ATH and prints large percentage swings on thin depth. As a BNB-Chain-native token it correlates strongly with BTC/ETH risk-on/risk-off regimes and BNB-ecosystem sentiment, tending to amplify moves in both directions. Expect low-liquidity gap risk, sharp squeeze-and-flush cycles, and elevated realized volatility relative to majors.

### Risk flags

- **Liquidity & venue concentration** — leveraged trading and price discovery hinge on Binance; a single-venue disruption or delisting would sharply impair execution.
- **Supply overhang** — circulating supply (~430M) is a fraction of the 2.00B max supply (MC/FDV ~0.22), leaving substantial emission/unlock dilution risk over time.
- **Narrative dependence** — valuation leans on the web3-domain/identity thesis; fading narrative interest can drain volume and liquidity quickly.
- **Small-cap fragility** — thin books make it vulnerable to liquidation cascades, manipulation, and outsized slippage on large orders.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=IDUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=IDUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=ID` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=ID` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=IDUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=IDUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=ID"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

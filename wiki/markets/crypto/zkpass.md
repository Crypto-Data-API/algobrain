---
title: "zkPass"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["ZKP"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://zkpass.org/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# zkPass

**zkPass** (ZKP) is a decentralized oracle protocol that transforms private internet data into verifiable proofs on-chain. It ranks **#981** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ZKP |
| **Market Cap Rank** | #981 |
| **Market Cap** | $14.18M |
| **Current Price** | $0.0703 |
| **Categories** | Infrastructure, Oracle, BNB Chain Ecosystem, Ethereum Ecosystem, Zero Knowledge (ZK), Animoca Brands Portfolio, Binance Alpha Spotlight, Binance Buildkey TGE, Privacy Infrastructure, Privacy |
| **Website** | [https://zkpass.org/](https://zkpass.org/) |

---

## Overview

zkPass is a decentralized oracle protocol that transforms private internet data into verifiable proofs on-chain. Built on zkTLS — a novel integration of 3P-TLS and Hybrid-ZK cryptography — zkPass enables users and applications to prove facts derived from any HTTPS website without requiring OAuth, API keys, or trusted intermediaries.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 201.67M ZKP |
| **Total Supply** | 1.00B ZKP |
| **Max Supply** | 1.00B ZKP |
| **Fully Diluted Valuation** | $70.29M |
| **Market Cap / FDV Ratio** | 0.20 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2329 (2025-12-19) |
| **Current vs ATH** | -69.81% |
| **All-Time Low** | $0.0661 (2026-03-30) |
| **Current vs ATL** | +6.28% |
| **24h Change** | -3.36% |
| **7d Change** | -1.51% |
| **30d Change** | -17.86% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xe1be424f442d0687129128c6c38aace44f8c8dbc` |
| Binance Smart Chain | `0xd89b7dd376e671c124352267516bef1c2cc231a3` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ZKP/USDT | N/A |
| Kraken | ZKP/USD | N/A |
| Upbit | ZKP/KRW | N/A |
| KuCoin | ZKP/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://zkpass.org/](https://zkpass.org/) |
| **Twitter** | [@zkPass](https://twitter.com/zkPass) |
| **GitHub** | [https://github.com/zkPassOfficial](https://github.com/zkPassOfficial) |
| **Whitepaper** | [https://docs.zkpass.org/](https://docs.zkpass.org/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.30M |
| **Market Cap Rank** | #981 |
| **24h Range** | $0.0701 — $0.0728 |
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

ZKP trades on **Binance** — both spot (ZKP/USDT) and a **USD-margined perpetual** with the full derivatives surface (funding, open interest, liquidations). It is **not listed on Hyperliquid**, so Binance is the primary leveraged venue. With a small-cap footprint and thin 24h volume, order books are shallow relative to majors: leverage is available but effective liquidity is limited, so slippage and funding volatility are elevated. Position sizing should be scaled down to account for wide spreads and gappy fills, and any perp-vs-spot strategy must route both legs through Binance rather than splitting venues.

### Applicable strategies

- [[funding-rate-harvest]] — periodic funding swings on a low-cap perp can be harvested delta-neutral while Binance remains the sole funding venue.
- [[cash-and-carry]] — Binance spot plus its USD-M perp allow a same-venue long-spot/short-perp carry when the perp trades at a premium.
- [[crowded-long-funding-fade]] — narrative-driven ZK/privacy hype can push crowded longs and stretched positive funding, offering a fade setup.
- [[liquidation-cascade-fade]] — thin books make ZKP prone to sharp liquidation-driven wicks that mean-revert, favoring a cascade fade.
- [[breakout-and-retest]] — the deep ATH-to-ATL drawdown leaves clear range boundaries whose breakouts can be traded on retest confirmation.
- [[token-unlock-supply-event]] — a low MC/FDV ratio (~0.20) implies large future unlocks that can be positioned around as scheduled supply events.

### Volatility & regime character

ZKP is a **small-cap infrastructure/ZK-oracle token** with high beta to broad crypto risk and to the ZK/privacy narrative specifically. It is highly correlated to BTC/ETH direction but amplifies moves on the downside, as shown by its steep decline from ATH. Reflexivity is narrative-driven (privacy, zkTLS, Binance Alpha/BuildKey momentum) rather than memecoin-style, so regimes swing between quiet illiquid drift and violent hype-driven expansion.

### Risk flags

- **Liquidity/venue concentration** — leveraged exposure depends almost entirely on Binance; a delisting or listing change would sharply impair execution.
- **Unlocks/emissions** — MC/FDV ~0.20 signals substantial locked supply and future emission overhang.
- **Narrative dependence** — price action leans heavily on ZK/privacy and Binance-ecosystem attention; fading narratives can drain liquidity.
- **Small-cap fragility** — thin depth means gap risk, funding spikes, and outsized impact from single large orders.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ZKPUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=ZKPUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=ZKP` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=ZKP` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ZKPUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=ZKPUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=ZKP"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

---
title: "OG Fan Token"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["OG"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://ogs.gg/"
related: ["[[crypto-markets]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[narrative-trading]]"]
---

# OG Fan Token

**OG Fan Token** (OG) is a cryptocurrency. It ranks **#1038** by market capitalization. Not only did OG win the first ever Dota 2 Valve major, they also were the first team to claim four of them.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | OG |
| **Market Cap Rank** | #1038 |
| **Market Cap** | $12.58M |
| **Current Price** | $2.65 |
| **Categories** | Entertainment, Sports, Binance Launchpool, Fan Token |
| **Website** | [https://ogs.gg/](https://ogs.gg/) |

---

## Overview

Not only did OG win the first ever Dota 2 Valve major, they also were the first team to claim four of them. They’re also currently the only team to ever be crowned World Dota 2 Champions twice.

Willing to take a step further in becoming an esports powerhouse, we decided to create OG Seed, to help grow Dota 2 players, and welcomed an amazing CS:GO roster as well.
We may be skilled, but the true strength of OG is its people.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 4.75M OG |
| **Total Supply** | 5.00M OG |
| **Max Supply** | 5.00M OG |
| **Fully Diluted Valuation** | $13.25M |
| **Market Cap / FDV Ratio** | 0.95 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $24.78 (2025-09-10) |
| **Current vs ATH** | -89.35% |
| **All-Time Low** | $1.18 (2022-05-12) |
| **Current vs ATL** | +123.32% |
| **24h Change** | -1.00% |
| **7d Change** | +2.34% |
| **30d Change** | -3.09% |
| **1y Change** | -42.66% |

---

## Platform & Chain Information

**Native Chain:** Chiliz

### Contract Addresses

| Chain | Address |
|---|---|
| Chiliz | `0xb3f2e39acc68f98229b2587361a8ce30acdf0442` |
| Solana | `BtjXf3LA7Z3jxAcQkKUqKYpLFS5B7GuB7pfjzeas1tdB` |
| Base | `0xccd6ee493ce30ba25291f563f8b6892af4ba202a` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | OG/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://ogs.gg/](https://ogs.gg/) |
| **Twitter** | [@OGesports](https://twitter.com/OGesports) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.77M |
| **Market Cap Rank** | #1038 |
| **24h Range** | $2.60 — $2.71 |
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

OG is tradable on **Binance** — both spot (OG/USDT) and a **USD-margined perpetual** with funding, open interest, and liquidation data. It is **not listed on Hyperliquid**, so Binance is the primary (effectively sole) leveraged venue. This single-venue concentration means all leveraged flow, funding signals, and liquidation cascades originate from one order book: execution and sizing should account for thin depth relative to majors (sub-$4M 24h volume, ~$13M market cap), where large market orders can move price meaningfully and slippage rises quickly. Cross-exchange arbitrage is limited by the absence of a second deep perp venue, and position sizing should be scaled down versus large-caps to avoid becoming a dominant share of the book.

### Applicable strategies

- [[funding-rate-harvest]] — a small-cap fan token perp on Binance can carry persistent funding skews that can be harvested delta-neutral (spot vs perp).
- [[crowded-long-funding-fade]] — narrative-driven spikes in OG often crowd longs, pushing funding positive and setting up fade entries.
- [[liquidation-cascade-fade]] — thin single-venue liquidity makes OG prone to sharp liquidation wicks that mean-revert, favoring cascade fades.
- [[cash-and-carry]] — spot + short perp on Binance captures basis/funding carry when the perp trades rich to spot.
- [[narrative-trading]] — as a sports/esports fan token, OG price is driven by team results, events, and fan-engagement narratives.
- [[volatility-breakout]] — low float and event-driven demand produce episodic volatility expansions tradable as breakouts.

### Volatility & regime character

OG is a **small-cap fan token** (rank ~1035, ~$13M market cap) built on Chiliz with a fixed 5M max supply and ~95% circulating. It behaves as a high-beta, reflexive small-cap: illiquidity amplifies moves in both directions, and price is strongly driven by sports/esports narrative and fan-engagement cycles rather than broad DeFi or infra flows. Correlation to BTC/ETH exists during risk-on/risk-off regimes but is loose; idiosyncratic team-event catalysts frequently dominate. Expect wide intraday ranges and low baseline liquidity between catalysts.

### Risk flags

- **Liquidity & venue concentration** — Binance is effectively the only meaningful venue for spot and the sole leveraged venue; a delisting or venue disruption would be severe.
- **Narrative dependence** — value hinges on esports team performance, fan engagement, and Chiliz/Socios ecosystem health rather than protocol fundamentals.
- **Thin float & reflexivity** — small market cap and low volume make OG vulnerable to sharp squeezes, liquidation cascades, and slippage on size.
- **Regulatory** — fan tokens face evolving regulatory scrutiny in some jurisdictions, which can affect listing access and demand.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=OGUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=OGUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=OG` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=OG` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=OGUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=OGUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=OG"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

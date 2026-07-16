---
title: "Alpine F1 Team Fan Token"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["ALPINE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.binance.com/en/support/announcement/14f033f78d174d5e8ab0cabfd56dffb8"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[narrative-trading]]", "[[liquidation-cascade-fade]]"]
---

# Alpine F1 Team Fan Token

**Alpine F1 Team Fan Token** (ALPINE) is a cryptocurrency. It ranks **#1773** by market capitalization. Binance is excited to announce a pioneering partnership with BWT Alpine F1® Team, the first Formula 1 team to join the Binance Fan Token Platform. This partnership sees Binance become the official Fan Token partner of BWT Alpine F1® Team and the Alpine Esports partner from 2022 onwards.

The Alpine F1® Team Fan Token (ALPINE) is a BEP-20 utility token to be launched first via the Binance Launchpad.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ALPINE |
| **Market Cap Rank** | #1773 |
| **Market Cap** | $3.68M |
| **Current Price** | $0.3238 |
| **Categories** | Sports, Fan Token, Binance Launchpad |
| **Website** | [https://www.binance.com/en/support/announcement/14f033f78d174d5e8ab0cabfd56dffb8](https://www.binance.com/en/support/announcement/14f033f78d174d5e8ab0cabfd56dffb8) |

---

## Overview

Binance is excited to announce a pioneering partnership with BWT Alpine F1® Team, the first Formula 1 team to join the Binance Fan Token Platform. This partnership sees Binance become the official Fan Token partner of BWT Alpine F1® Team and the Alpine Esports partner from 2022 onwards.

The Alpine F1® Team Fan Token (ALPINE) is a BEP-20 utility token to be launched first via the Binance Launchpad. ALPINE will then be available to all Binance users and the Binance Fan Token community via spot, bank card purchases, and P2P.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 11.36M ALPINE |
| **Total Supply** | 40.00M ALPINE |
| **Max Supply** | 40.00M ALPINE |
| **Fully Diluted Valuation** | $12.95M |
| **Market Cap / FDV Ratio** | 0.28 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $12.71 (2025-09-30) |
| **Current vs ATH** | -97.45% |
| **All-Time Low** | $0.2938 (2026-07-13) |
| **Current vs ATL** | +10.22% |
| **24h Change** | -2.54% |
| **7d Change** | +5.63% |
| **30d Change** | -8.57% |
| **1y Change** | -62.27% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0x287880ea252b52b63cc5f40a2d3e5a44aa665a76` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ALPINE/USDT | N/A |
| Bitget | ALPINE/USDT | N/A |
| KuCoin | ALPINE/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.binance.com/en/support/announcement/14f033f78d174d5e8ab0cabfd56dffb8](https://www.binance.com/en/support/announcement/14f033f78d174d5e8ab0cabfd56dffb8) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.41M |
| **Market Cap Rank** | #1773 |
| **24h Range** | $0.3197 — $0.3473 |
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

ALPINE trades on Binance as both a spot pair (ALPINE/USDT) and a USD-margined perpetual, giving access to funding rates, open interest and liquidation data. It is **not** listed on Hyperliquid, so Binance is the primary — and effectively sole — venue for leveraged exposure. With a sub-$5M market cap and thin 24h volume, the perp order book is shallow: available leverage tiers are conservative, spreads widen quickly, and even modest position sizes can move price or trigger liquidation cascades. Traders should size small, favor limit orders, and treat single-venue concentration as a structural execution risk since there is no cross-exchange perp to hedge or arbitrage against.

### Applicable strategies

- [[funding-rate-harvest]] — a lone Binance perp with a small, sentiment-driven crowd can produce persistently skewed funding, harvestable spot-vs-perp.
- [[crowded-long-funding-fade]] — fan-token hype and F1 event spikes often crowd longs, pushing funding rich enough to fade.
- [[liquidation-cascade-fade]] — thin depth means stop runs and forced liquidations overshoot, offering mean-reversion entries after cascades.
- [[narrative-trading]] — price is driven by Alpine F1 team news, race weekends and sponsorship narratives rather than fundamentals.
- [[event-driven-trading]] — race results, partnership announcements and Binance fan-token campaigns act as discrete, tradable catalysts.
- [[rsi-mean-reversion]] — low-liquidity, range-bound drift between catalysts produces frequent oversold/overbought reversion setups.

### Volatility & regime character

ALPINE is a micro-cap (rank ~1767) fan token with high, reflexive volatility more akin to a memecoin than an infrastructure or DeFi asset. Its price is loosely correlated to BTC/ETH beta and instead swings on Alpine F1 sporting calendar events, sponsorship news and Binance fan-token promotions. Expect sharp, low-liquidity spikes and equally fast reversions, with extended quiet drift in between.

### Risk flags

- **Liquidity & venue concentration** — trading is concentrated on Binance; no Hyperliquid or deep secondary perp market, so exit liquidity can vanish in stress.
- **Narrative dependence** — value hinges on the Alpine F1 team's performance and Binance's continued fan-token support, not on protocol usage.
- **Supply overhang** — circulating supply (~11.4M) is well below max supply (40M), leaving room for future unlocks/emissions to pressure price.
- **Regulatory** — fan tokens face evolving scrutiny in some jurisdictions, which can affect listings and accessibility.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ALPINEUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=ALPINEUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=ALPINE` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=ALPINE` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ALPINEUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=ALPINEUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=ALPINE"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

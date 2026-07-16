---
title: "Radworks"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, altcoins, defi]
aliases: ["RAD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://radworks.org/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[range-mean-reversion]]", "[[dca-strategy]]"]
---

# Radworks

**Radworks** (RAD) is building a sovereign developer stack that enables developers to securely host, collaborate, and reward open-source code. It ranks **#1132** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | RAD |
| **Market Cap Rank** | #1132 |
| **Market Cap** | $10.57M |
| **Current Price** | $0.2130 |
| **Categories** | Infrastructure, DePIN |
| **Website** | [https://radworks.org/](https://radworks.org/) |

---

## Overview

Radworks is building a sovereign developer stack that enables developers to securely host, collaborate, and reward open-source code. It’s composed of Radicle, an open source, peer-to-peer code collaboration stack, and Drips, a decentralized toolkit for continuously funding critical software dependencies.
​​​​​​​
$RAD is the native token of the Radworks Network, used as the primary means to coordinate all actors, govern the treasury, and reward infrastructure providers on top of the Radicle network.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 49.83M RAD |
| **Total Supply** | 100.00M RAD |
| **Max Supply** | 100.00M RAD |
| **Fully Diluted Valuation** | $21.22M |
| **Market Cap / FDV Ratio** | 0.50 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $27.61 (2021-04-15) |
| **Current vs ATH** | -99.23% |
| **All-Time Low** | $0.2021 (2026-06-06) |
| **Current vs ATL** | +4.99% |
| **24h Change** | -0.88% |
| **7d Change** | -0.15% |
| **30d Change** | -8.00% |
| **1y Change** | -68.11% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x31c8eacbffdd875c74b94b077895bd78cf1e64a3` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | RAD/USDT | N/A |
| Kraken | RAD/USD | N/A |
| Crypto.com Exchange | RAD/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X31C8EACBFFDD875C74B94B077895BD78CF1E64A3/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://radworks.org/](https://radworks.org/) |
| **Twitter** | [@radicle](https://twitter.com/radicle) |
| **GitHub** | [https://github.com/radicle-dev](https://github.com/radicle-dev) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.19M |
| **Market Cap Rank** | #1132 |
| **24h Range** | $0.2111 — $0.2170 |
| **CoinGecko Sentiment** | 100% positive |
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

RAD is tradable on **Binance SPOT only** — no liquid perpetual venue exists, so leverage and short access are limited and this is a **spot-primary** asset. Perp funding/basis/liquidation strategies do **not** apply. With thin 24h turnover and a sub-$15M market cap concentrated on a single primary venue, execution should assume wide spreads and shallow order-book depth: size positions small, favor limit orders over market orders, and stagger entries/exits to avoid slippage. Venue concentration also means listing/delisting or maintenance events on Binance can dominate short-term liquidity and price.

### Applicable strategies

- [[range-mean-reversion]] — RAD trades near multi-year lows in a compressed band, so fading extremes within the established range fits a low-momentum, spot-only microcap.
- [[rsi-mean-reversion]] — oversold bounces on a beaten-down infra token can be scalped with RSI oscillator triggers where trend signals are unreliable.
- [[bollinger-band-reversion]] — low-cap volatility contractions and expansions around the mean suit band-reversion entries on the daily chart.
- [[dca-strategy]] — for spot accumulation of a deeply drawn-down (~-99% from ATH) token, dollar-cost averaging removes timing risk on an illiquid single-venue asset.
- [[breakout-and-retest]] — occasional narrative-driven volume spikes offer breakout-and-retest setups above range highs, confirmed on spot volume.
- [[narrative-trading]] — as a developer-infra/DePIN token, RAD is sensitive to open-source funding and DePIN narrative rotations that can drive episodic repricing.

### Volatility & regime character

Micro-cap (rank ~1131) infrastructure/DeFi-adjacent token with high idiosyncratic volatility and low, patchy liquidity. Behaves as a high-beta altcoin: it tends to underperform in risk-off regimes and lag BTC/ETH majors, while rallying sharply only on token-specific or DePIN-sector narrative catalysts. Correlation to BTC/ETH is meaningful on broad market moves but noisy at the single-token level given thin depth, producing reflexive, gap-prone price action.

### Risk flags

- **Liquidity/venue concentration** — spot-primary on a single main venue (Binance); thin depth amplifies slippage and gap risk.
- **Emissions/supply** — circulating supply is roughly half of max supply (MC/FDV ~0.50), leaving latent dilution as more tokens enter circulation.
- **Narrative dependence** — price action hinges on developer-infra/DePIN sentiment rather than steady fundamentals, making rallies fragile.
- **Depressed regime** — trades ~99% below ATH near all-time lows; low absolute price and low cap raise reflexivity and delisting risk.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=RADUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=RADUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=RADUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=RADUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

---
title: "Manchester City Fan Token"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, altcoins]
aliases: ["CITY"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://socios.com"
related: ["[[crypto-markets]]", "[[binance]]", "[[narrative-trading]]", "[[dca-strategy]]"]
---

# Manchester City Fan Token

**Manchester City Fan Token** (CITY) is a cryptocurrency. It ranks **#1506** by market capitalization. The Manchester City Fan Token allows CITY fans to have a tokenized share of influence on club decisions, purchased through the consumer facing platform, Socios.com, fans can engage in a wide variety of club decisions for example, choosing a goal celebration song or deciding team bus design, earn rewards and money can't buy experiences. Experiences like...

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CITY |
| **Market Cap Rank** | #1506 |
| **Market Cap** | $5.47M |
| **Current Price** | $0.3995 |
| **Categories** | Sports, Binance Launchpool, Fan Token |
| **Website** | [https://socios.com](https://socios.com) |

---

## Overview

The Manchester City Fan Token allows CITY fans to have a tokenized share of influence on club decisions, purchased through the consumer facing platform, Socios.com, fans can engage in a wide variety of club decisions for example, choosing a goal celebration song or deciding team bus design, earn rewards and money can't buy experiences. Experiences like... having the opportunity to meet and greet with your favourite players, receiving VIP treatment at the stadium &amp; much much more.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 13.68M CITY |
| **Total Supply** | 19.74M CITY |
| **Max Supply** | 19.74M CITY |
| **Fully Diluted Valuation** | $7.89M |
| **Market Cap / FDV Ratio** | 0.69 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $36.19 (2021-08-27) |
| **Current vs ATH** | -98.89% |
| **All-Time Low** | $0.3562 (2026-06-24) |
| **Current vs ATL** | +12.75% |
| **24h Change** | +0.23% |
| **7d Change** | +2.15% |
| **30d Change** | -0.60% |
| **1y Change** | -56.60% |

---

## Platform & Chain Information

**Native Chain:** Chiliz

### Contract Addresses

| Chain | Address |
|---|---|
| Chiliz | `0x7bd6242d775faef1d50b2aa18c2fbf329bddf295` |
| Base | `0x02300475d1edd5b2e88efdebd3ffb549110d8aa6` |
| Solana | `8WbNQtY7QmXMVKJFTSqFudierVZZtbuoyeepZEqJ1B2w` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | CITY/USDT | N/A |
| Upbit | CITY/BTC | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://socios.com](https://socios.com) |
| **Twitter** | [@socios](https://twitter.com/socios) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.43M |
| **Market Cap Rank** | #1506 |
| **24h Range** | $0.3894 — $0.4089 |
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

CITY is tradable on **Binance SPOT only** — there is no liquid perpetual venue, so leverage and short access are limited and this is a **spot-primary** asset. Perp funding, basis, and liquidation strategies do **not** apply. With liquidity concentrated in the single Binance CITY/USDT spot book (plus a thin Upbit CITY/BTC pair), execution should assume shallow depth: size positions modestly, prefer limit orders over market orders, and expect slippage to widen quickly on larger clips. Venue concentration also means Binance-specific events (maintenance, delisting, or margin-policy changes) directly gate all practical access.

### Applicable strategies

- [[narrative-trading]] — CITY is a fan token whose demand tracks Manchester City club news, results, and Socios.com engagement cycles rather than crypto fundamentals.
- [[event-driven-trading]] — discrete club and platform events (matches, signings, Fan Token Offering-style promotions) create tradable spot catalysts.
- [[dca-strategy]] — a spot-primary, low-cap token with no leverage is well suited to averaging in over time rather than levered timing.
- [[breakout-and-retest]] — thin single-venue liquidity produces sharp range breaks on volume that can be confirmed on retest before committing spot size.
- [[range-trading]] — outside of catalysts CITY tends to oscillate in a defined spot range, tradable with disciplined limit entries around support/resistance.
- [[atr-trailing-stop]] — volatility-scaled trailing stops help manage the gap-prone, low-liquidity spot moves without a fixed stop being run.

### Volatility & regime character

Small-cap (rank ~#1499), low-float fan token with high idiosyncratic volatility and reflexive, sentiment-driven price action tied to a single sports club. Correlation to BTC/ETH is loose and episodic: broad crypto beta matters less than club-specific narrative, so CITY can move independently of the majors. It is neither an infra nor a DeFi token — its regime is dominated by fan/narrative flow and thin-book mechanics.

### Risk flags

- **Liquidity/venue concentration** — effectively a single-venue (Binance spot) asset; any venue disruption removes practical access.
- **Narrative dependence** — value hinges on continued club engagement and the Socios.com platform; fading fan interest is a structural downside.
- **Low market cap / thin depth** — small cap and low circulating float make the book easy to move, amplifying slippage and volatility.
- **No leverage/short access** — absence of a liquid perp venue limits hedging and directional short expression.
- **Regulatory** — fan tokens face evolving regulatory scrutiny over their promotional and utility framing in some jurisdictions.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=CITYUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=CITYUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=CITYUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=CITYUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

---
title: "Bubblemaps"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["BMT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://bubblemaps.io"
related: ["[[crypto-markets]]", "[[solana]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]", "[[oi-confirmed-trend]]"]
---

# Bubblemaps

**Bubblemaps** (BMT) is a cryptocurrency. It ranks **#1902** by market capitalization. Blockchain data is inherently cluttered, noisy, and highly technical.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BMT |
| **Market Cap Rank** | #1902 |
| **Market Cap** | $3.03M |
| **Current Price** | $0.0118 |
| **Categories** | Analytics, Binance HODLer Airdrops, Binance Wallet IDO, InfoFi |
| **Website** | [https://bubblemaps.io](https://bubblemaps.io) |

---

## Overview

Blockchain data is inherently cluttered, noisy, and highly technical. 

Bubblemaps transforms this complexity into a visual experience, making analysis engaging and efficient —allowing users to address modern crypto challenges:

- Tokenomics being difficult to analyse and understand
- Memecoins bundling their supply and dumping on the retail
- Celebrities launching tokens while secretly holding massive amounts
- Launchpads, KOLs, and VCs exploiting the lack of transparency for profit

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 256.18M BMT |
| **Total Supply** | 1.00B BMT |
| **Max Supply** | 1.00B BMT |
| **Fully Diluted Valuation** | $11.82M |
| **Market Cap / FDV Ratio** | 0.26 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.3173 (2025-03-18) |
| **Current vs ATH** | -96.28% |
| **All-Time Low** | $0.0112 (2026-07-01) |
| **Current vs ATL** | +5.75% |
| **24h Change** | -0.02% |
| **7d Change** | -2.33% |
| **30d Change** | -10.93% |
| **1y Change** | -86.26% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `FQgtfugBdpFN7PZ6NdPrZpVLDBrPGxXesi4gVu3vErhY` |
| Binance Smart Chain | `0x7d814b9ed370ec0a502edc3267393bf62d891b62` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | BMT/USDT | N/A |
| Kraken | BMT/USD | N/A |
| Bitget | BMT/USDT | N/A |
| KuCoin | BMT/USDT | N/A |
| Crypto.com Exchange | BMT/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://bubblemaps.io](https://bubblemaps.io) |
| **Twitter** | [@bubblemaps](https://twitter.com/bubblemaps) |
| **Telegram** | [bubblemaps](https://t.me/bubblemaps) (8,542 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.58M |
| **Market Cap Rank** | #1902 |
| **24h Range** | $0.0118 — $0.0120 |
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

BMT is tradable on **Binance** — both spot (BMT/USDT) and a **USD-margined perpetual** with the associated derivatives surface (funding, open interest, liquidations). It is **NOT listed on Hyperliquid**, so Binance is the primary leveraged venue. With a small market cap (~#1902) and thin spot depth, leverage and directional exposure are concentrated on a single perp venue. This means execution should favor limit orders and staged fills to avoid slippage, position sizing must account for shallow order books, and traders should watch Binance funding/OI as the dominant signal — there is no cross-venue perp to hedge or arbitrage against, raising single-venue liquidation and squeeze risk.

### Applicable strategies

- [[liquidation-cascade-fade]] — thin BMT perp depth on Binance makes forced-liquidation wicks overshoot, offering mean-reversion entries once the cascade exhausts.
- [[funding-rate-harvest]] — a single-venue perp with periodic funding lets traders collect payments by holding the side opposite crowded positioning when funding skews.
- [[oi-confirmed-trend]] — pairing Binance open-interest changes with BMT price filters real breakouts from low-conviction moves in an illiquid microcap.
- [[range-mean-reversion]] — with BMT pinned near its all-time low in a tight band, fading extremes of the range suits the current low-momentum regime.
- [[breakout-and-retest]] — narrative-driven analytics/InfoFi microcaps can gap violently, so waiting for a breakout to retest confirms follow-through before committing size.
- [[token-unlock-supply-event]] — with circulating supply only ~26% of max, scheduled unlocks create tradable supply-overhang events to position around.

### Volatility & regime character

BMT is a small-cap (~#1902) analytics/InfoFi infra token on Solana with high beta to broader crypto risk sentiment. Price sits deep below its all-time high and near its all-time low, indicating a prolonged downtrend and low-momentum, chop-prone regime. As a low-liquidity microcap it exhibits reflexive, narrative-sensitive moves and tends to amplify BTC/ETH directional swings while underperforming on the way up. Realized volatility can spike sharply on thin volume despite muted recent daily ranges.

### Risk flags

- **Venue concentration** — leveraged exposure is confined to Binance; no Hyperliquid or secondary perp venue to hedge, so single-venue outages, funding spikes, or liquidation cascades hit hard.
- **Low liquidity** — small market cap and thin spot/perp depth mean slippage and squeeze risk on any meaningful size.
- **Supply overhang / unlocks** — circulating supply is a fraction of max supply, leaving future emissions and unlocks as a persistent dilution and sell-pressure risk.
- **Narrative dependence** — as an analytics/InfoFi token, valuation leans on sector attention; fading narrative can drain liquidity quickly.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BMTUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=BMTUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=BMT` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=BMT` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BMTUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BMTUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=BMT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

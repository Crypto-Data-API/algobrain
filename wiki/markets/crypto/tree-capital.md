---
title: "Tree"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, defi, altcoins, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["TREE"]
entity_type: protocol
headquarters: "Decentralized"
website: "http://news.treeofalpha.com"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]", "[[momentum-investing]]"]
---

# Tree

**Tree** (TREE) is a cryptocurrency. It ranks **#903** by market capitalization. Utility token for Tree News. The token can be used for a new subscription tier that lets users unlock all advantages that only TreeNFT holders could get until now.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TREE |
| **Market Cap Rank** | #903 |
| **Market Cap** | $16.78M |
| **Current Price** | $0.165528 |
| **Categories** | Analytics, Ethereum Ecosystem, Base Ecosystem, Base Native |
| **Website** | [http://news.treeofalpha.com](http://news.treeofalpha.com) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Overview

Utility token for Tree News. The token can be used for a new subscription tier that lets users unlock all advantages that only TreeNFT holders could get until now.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 101.36M TREE |
| **Total Supply** | 114.57M TREE |
| **Max Supply** | 200.00M TREE |
| **Fully Diluted Valuation** | $23.26M |
| **Market Cap / FDV Ratio** | 0.88 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.4293 (2025-08-12) |
| **Current vs ATH** | -52.68% |
| **All-Time Low** | $0.0474 (2024-01-22) |
| **Current vs ATL** | +329.06% |
| **24h Change** | +1.84% |
| **7d Change** | -2.24% |
| **30d Change** | +2.52% |
| **1y Change** | -7.19% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xba25b2281214300e4e649fead9a6d6acd25f1c0a` |
| Base | `0x52c2b317eb0bb61e650683d2f287f56c413e4cf6` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XBA25B2281214300E4E649FEAD9A6D6ACD25F1C0A/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [http://news.treeofalpha.com](http://news.treeofalpha.com) |
| **Twitter** | [@TreeTokenEth](https://twitter.com/TreeTokenEth) |
| **Telegram** | [treetokeneth](https://t.me/treetokeneth) (893 members) |
| **Whitepaper** | [https://news.treeofalpha.com/litepaper](https://news.treeofalpha.com/litepaper) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $58,664.00 |
| **Market Cap Rank** | #903 |
| **24h Range** | $0.1963 — $0.2083 |
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

TREE is tradable on [[binance]] — spot plus a USD-margined [[perpetual-futures]] contract (TREEUSDT) with funding, open interest, and liquidation data. It is **NOT** listed on Hyperliquid, so Binance is effectively the primary — and only major — leveraged venue for the asset. This concentration means the Binance perp defines price discovery for leveraged flow: funding and open interest read straight off one book, and there is no cross-venue perp to hedge against or arbitrage. As a low-cap (rank ~1379) with thin reported spot volume, order books are shallow, so leverage should be modest and position sizing conservative — market orders can move price meaningfully and slippage on entries/exits is a first-order cost. Single-venue availability also raises execution and gap risk: a listing/delisting change or a maintenance halt on Binance removes the only deep pool at once.

### Applicable strategies

- [[liquidation-cascade-fade]] — thin single-venue perp liquidity makes stop-driven liquidation wicks common on TREE; fading exhausted cascades can capture sharp mean-reversion snapbacks.
- [[funding-rate-harvest]] — a lone Binance perp with a small float can push funding to extremes as directional traders crowd in, letting a delta-hedged spot-vs-perp position collect the carry.
- [[oi-price-exhaustion]] — with all leveraged flow on one book, rising open interest into a stalling price is a clean local signal that a crowded move is running out of fuel.
- [[breakout-and-retest]] — TREE's low-cap, news-driven character produces range compression then expansion; trading confirmed breakouts with a retest filter reduces false starts in a choppy tape.
- [[rsi-mean-reversion]] — reflexive low-float swings frequently overshoot; RSI-based reversion around range extremes suits a small-cap that lacks sustained trend depth.
- [[news-trading]] — TREE is the utility token of a crypto-news service (Tree News), so its price is unusually sensitive to platform announcements and narrative catalysts.

### Volatility & regime character

TREE is a small-cap (rank ~1379) DeFi/analytics utility token on Ethereum and Base with a modest float and low liquidity, so it exhibits high, reflexive volatility and low-float swing behavior rather than the smoother beta of a large-cap. It tends to be high-beta to broad crypto risk-on/risk-off — moving with BTC/ETH direction but with amplified magnitude — while idiosyncratic, narrative-driven moves tied to the Tree News product can decouple it from the majors. Expect regime shifts between quiet, range-bound drift and sudden expansion around catalysts.

### Risk flags

- **Liquidity & venue concentration** — thin spot volume and a single major leveraged venue (Binance) mean wide spreads, slippage, and elevated gap/halt risk with no perp hedge elsewhere.
- **Emissions/supply overhang** — circulating supply sits below total and max supply, so future unlocks or emissions can add sell pressure; watch the schedule before sizing.
- **Narrative dependence** — value is closely tied to adoption of the Tree News platform and subscription tier, making the token sensitive to product traction and sentiment shifts.
- **Small-cap fragility** — low market cap and depth make TREE susceptible to manipulation, outsized moves on modest flow, and delisting risk if volume stays thin.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=TREEUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=TREEUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=TREE` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=TREE` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=TREEUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=TREEUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=TREE"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

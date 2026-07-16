---
title: "Pixels"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, nft, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, altcoins]
aliases: ["PIXEL"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.pixels.xyz/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# Pixels

**Pixels** (PIXEL) is a captivating, open-ended world of farming and exploration, built one pixel at a time. It ranks **#1786** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PIXEL |
| **Market Cap Rank** | #1786 |
| **Market Cap** | $3.58M |
| **Current Price** | $0.00463743 |
| **Categories** | Gaming (GameFi), NFT, Binance Launchpool, Gaming Utility Token, Made in USA, Governance |
| **Website** | [https://www.pixels.xyz/](https://www.pixels.xyz/) |

---

## Overview

Pixels is a captivating, open-ended world of farming and exploration, built one pixel at a time. Gathering resources, advancing skills, and building relationships while exploring the story and quests woven throughout the Pixels Universe, you’ll be submerged in a mesmerizing blend of managing, creating, and exploring in a world that marries blockchain ownership with your progression and accomplishments.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 771.04M PIXEL |
| **Total Supply** | 5.00B PIXEL |
| **Max Supply** | 5.00B PIXEL |
| **Fully Diluted Valuation** | $23.19M |
| **Market Cap / FDV Ratio** | 0.15 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.02 (2024-03-11) |
| **Current vs ATH** | -99.54% |
| **All-Time Low** | $0.00447081 (2026-07-01) |
| **Current vs ATL** | +3.75% |
| **24h Change** | -1.38% |
| **7d Change** | -3.34% |
| **30d Change** | -18.76% |
| **1y Change** | -89.10% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x3429d03c6f7521aec737a0bbf2e5ddcef2c3ae31` |
| Ronin | `0x7eae20d11ef8c779433eb24503def900b9d28ad7` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | PIXEL/USDT | N/A |
| Bitget | PIXEL/USDT | N/A |
| KuCoin | PIXEL/USDT | N/A |
| Crypto.com Exchange | PIXEL/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.pixels.xyz/](https://www.pixels.xyz/) |
| **Twitter** | [@pixels_online](https://twitter.com/pixels_online) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $6.47M |
| **Market Cap Rank** | #1786 |
| **24h Range** | $0.00459358 — $0.00479380 |
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

PIXEL trades on **both Binance** (spot **PIXEL/USDT** plus a USD-margined perpetual) **and Hyperliquid** (**PIXEL-PERP**, leverage up to roughly **40-50x**). This two-venue structure gives a comparatively deep, liquid market for a coin of this rank: Binance provides the primary spot venue and a large-book USD-M perp, while Hyperliquid contributes a transparent on-chain order book with its own funding stream. Because the same instrument is priced on a centralized venue and an on-chain venue, execution can be split across books to reduce slippage, and the dual availability supports both cash-and-carry (Binance spot vs. perp) and CEX-vs-DEX funding/basis plays. Sizing should still respect that this is a micro-cap (rank ~1786) — depth is real relative to peers but thin in absolute terms, so large clips will move the book on either venue and are best worked with limit orders rather than market sweeps.

### Applicable strategies

- [[funding-rate-harvest]] — collect the perp funding stream on PIXEL, which as a low-float GameFi alt tends to swing to persistent one-sided (often positive) funding during reflexive rallies.
- [[hl-vs-cex-funding-divergence]] — Binance USD-M perp and Hyperliquid PIXEL-PERP fund independently, so the same coin can carry meaningfully different rates to arbitrage across the two venues.
- [[cash-and-carry]] — long Binance spot PIXEL against a short perp to lock the basis when funding is richly positive, using the deep dual-venue liquidity to enter and unwind.
- [[liquidation-cascade-fade]] — thin absolute depth plus high perp leverage makes PIXEL prone to sharp liquidation wicks that overshoot, offering fade entries against forced flow.
- [[breakout-and-retest]] — as a narrative-driven GameFi token, PIXEL trends impulsively on catalysts; entering on the retest of a broken level filters false starts on a low-liquidity book.
- [[oi-price-exhaustion]] — rising open interest into a stalling price on this reflexive micro-cap flags crowded positioning that often precedes a mean-reverting flush.

### Volatility & regime character

PIXEL is a **high-beta GameFi / NFT-adjacent micro-cap** with pronounced reflexivity: low circulating float versus a much larger total supply means price moves are amplified by thin depth and narrative flows. It carries strong **positive beta to broad crypto risk (BTC/ETH)** in direction, but with far larger amplitude than large caps — it tends to underperform on the way down (see the multi-year drawdown from ATH) and can spike violently on gaming-sector or Binance-ecosystem catalysts. Regime is dominated by GameFi/alt-season sentiment cycles rather than PIXEL-specific fundamentals, so it behaves as a leveraged proxy for altcoin risk appetite.

### Risk flags

- **Micro-cap liquidity / venue concentration** — real depth concentrates on Binance and Hyperliquid; away from these venues books are thin and slippage rises sharply.
- **Emissions / low float** — circulating supply is a small fraction of the 5.00B total/max supply, so ongoing unlocks and emissions are a structural supply overhang that can pressure price.
- **Narrative dependence** — moves hinge on GameFi/NFT sentiment and Binance-ecosystem newsflow; interest can evaporate quickly, leaving positions illiquid.
- **Perp funding dislocations** — high available leverage on a low-float name can drive extreme funding and liquidation cascades, hazardous for leveraged carry and momentum positions.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=PIXEL` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=PIXEL` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=PIXEL&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=PIXEL&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=PIXEL"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

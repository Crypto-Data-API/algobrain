---
title: "BOOK OF MEME"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, derivatives, altcoins, memecoins]
aliases: ["BOME"]
entity_type: protocol
headquarters: "Decentralized"
related: ["[[crypto-markets]]", "[[solana]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[meme-coin-cycle]]"]
---

# BOOK OF MEME

**BOOK OF MEME** (BOME) is a cryptocurrency. It ranks **#639** by market capitalization. The Book of Meme (BOME) is a memecoin built on the Solana blockchain.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BOME |
| **Market Cap Rank** | #639 |
| **Market Cap** | $29.74M |
| **Current Price** | $0.000431 |
| **Categories** | Solana Ecosystem, Meme, Frog-Themed, Solana Meme, GMCI Meme Index, GMCI Index |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Overview

The Book of Meme (BOME) is a memecoin built on the Solana blockchain. Created by an artist known as Darkfarms, BOME is designed to serve as a digital archive for memes, aiming to preserve meme culture by storing these digital creations on blockchain technology, ensuring they are never lost and remain accessible indefinitely.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 69.00B BOME |
| **Total Supply** | 69.00B BOME |
| **Max Supply** | 69.00B BOME |
| **Fully Diluted Valuation** | $26.56M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0269 (2024-03-16) |
| **Current vs ATH** | -98.57% |
| **All-Time Low** | $0.00005848 (2024-03-14) |
| **Current vs ATL** | +558.24% |
| **24h Change** | -2.79% |
| **7d Change** | -1.24% |
| **30d Change** | -3.70% |
| **1y Change** | -60.96% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | BOME/USDT | N/A |
| Bitget | BOME/USDT | N/A |
| KuCoin | BOME/USDT | N/A |
| Crypto.com Exchange | BOME/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | BOME-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Twitter** | [@Darkfarms1](https://twitter.com/Darkfarms1) |
| **Telegram** | [BOOK_OF_MEME](https://t.me/BOOK_OF_MEME) (30,139 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $9.47M |
| **Market Cap Rank** | #639 |
| **24h Range** | $0.00038344 — $0.00040638 |
| **CoinGecko Sentiment** | 100% positive |
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

BOME trades on a deep, liquid two-venue derivatives market. It is available on **Binance** (spot BOME/USDT plus a USD-margined perpetual) and on **[[hyperliquid|Hyperliquid]]** (BOME-PERP, with leverage up to roughly 40-50x). The dual-venue footprint — a large centralized order book alongside an on-chain perp — means execution can be split across venues and sizing benefits from aggregated depth, though the small ~$29M market cap keeps absolute depth modest for a memecoin. The parallel Binance and Hyperliquid perps create a persistent cross-venue funding and basis relationship that active traders can lean on, but large orders on either book still move price, so slicing execution and watching combined depth is prudent.

### Applicable strategies

- [[hl-vs-cex-funding-divergence]] — BOME runs simultaneously on Binance and Hyperliquid perps, so funding can diverge between the two books, offering a clean long-one/short-the-other spread capture.
- [[funding-rate-harvest]] — memecoin perps like BOME often carry persistently skewed funding, letting a delta-neutral position collect the premium.
- [[liquidation-cascade-fade]] — thin memecoin depth makes BOME prone to sharp leverage-driven flushes that frequently overshoot and revert.
- [[meme-coin-cycle]] — as a Solana memecoin, BOME's price is driven by attention and reflexive meme-cycle dynamics rather than fundamentals.
- [[volatility-breakout]] — BOME's high realized volatility produces frequent range expansions that reward breakout entries with defined risk.
- [[narrative-trading]] — moves are tightly coupled to Solana-ecosystem and broader memecoin narrative flows.

### Volatility & regime character

BOME is a high-beta Solana memecoin whose price action is dominated by reflexivity, attention flows, and sentiment rather than cash-flow fundamentals. Realized volatility is well above large-cap crypto, with large drawdowns (currently ~99% below its 2024 ATH) and sharp attention-driven spikes. It broadly carries positive beta to BTC/ETH risk-on regimes but amplifies both up and down moves, and it is especially sensitive to Solana-ecosystem strength and the wider memecoin risk appetite.

### Risk flags

- **Liquidity / venue concentration** — a small ~$29M cap and modest 24h volume mean depth is shallow; liquidity is concentrated across a few venues (Binance, Hyperliquid) and can thin quickly.
- **Narrative dependence** — value rests almost entirely on meme narrative and attention; sentiment reversals can be abrupt and severe.
- **Perp funding dislocations** — leveraged crowding produces volatile, sometimes extreme funding on both perp venues, which can invert quickly and squeeze one-sided positioning.
- **Reflexive drawdown risk** — memecoin reflexivity cuts both ways; the deep decline from ATH illustrates how fast attention (and price) can drain.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=BOME` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=BOME` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=BOME&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=BOME&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=BOME"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

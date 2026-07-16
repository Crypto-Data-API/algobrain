---
title: "TROLL"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, altcoins, memecoins]
aliases: ["TROLL"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://trololol.io"
related: ["[[crypto-markets]]", "[[solana]]", "[[binance]]", "[[momentum-investing]]", "[[meme-coin-cycle]]"]
---

# TROLL

**TROLL** (TROLL) is a cryptocurrency. It ranks **#476** by market capitalization. The TROLL token on the Solana network is a meme coin inspired by internet trolling culture, designed for entertainment and community engagement with no intrinsic value. Built on Solana’s blockchain, it leverages the network’s fast transactions and low fees to appeal to meme enthusiasts.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TROLL |
| **Market Cap Rank** | #476 |
| **Market Cap** | $43.91M |
| **Current Price** | $0.0440 |
| **Categories** | Meme, Solana Meme, Parody Meme, Binance Alpha Spotlight, 4chan-Themed, IP Meme |
| **Website** | [https://trololol.io](https://trololol.io) |

---

## Overview

The TROLL token on the Solana network is a meme coin inspired by internet trolling culture, designed for entertainment and community engagement with no intrinsic value. Built on Solana’s blockchain, it leverages the network’s fast transactions and low fees to appeal to meme enthusiasts. Launched on decentralized exchanges, TROLL aims to foster a fun, community-driven ecosystem through social media, influencer partnerships, and viral marketing, embodying the playful spirit of online trolling.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 998.77M TROLL |
| **Total Supply** | 998.77M TROLL |
| **Max Supply** | 1.00B TROLL |
| **Fully Diluted Valuation** | $43.91M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2826 (2025-08-22) |
| **Current vs ATH** | -84.45% |
| **All-Time Low** | $0.00387003 (2025-04-22) |
| **Current vs ATL** | +1035.38% |
| **24h Change** | -11.90% |
| **7d Change** | -13.73% |
| **30d Change** | -42.06% |
| **1y Change** | +245.70% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| KuCoin | TROLL/USDT | N/A |
| Crypto.com Exchange | TROLL/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | 5UUH9RTDISPQ6HKS6BP4NDU9PNJPXRXUIW6SHBTBHGH2/8ADSF2QXFA8QKFUQ9TRQW6NEYM4E6YT4AWQGZ5CTPUMP | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://trololol.io](https://trololol.io) |
| **Twitter** | [@trololol_io](https://twitter.com/trololol_io) |
| **Telegram** | [trollsolog](https://t.me/trollsolog) (4,567 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.08M |
| **Market Cap Rank** | #476 |
| **24h Range** | $0.0438 — $0.0505 |
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

Tradable on Binance SPOT only — no liquid perpetual venue, so leverage/short access is limited and this is a spot-primary asset. Perp funding/basis/liquidation strategies do NOT apply. With execution concentrated on a single spot venue (plus thin DEX/Orca and secondary CEX pairs), depth is shallow and slippage-prone: size positions to available order-book depth, prefer limit/VWAP-style entries, and expect wide effective spreads during volatility. The absence of a deep perp market means directional exposure is long-biased (no cheap shorting), so risk is managed primarily through position sizing and stops rather than hedges.

### Applicable strategies

- [[momentum-investing]] — TROLL's memecoin reflexivity produces sharp trending impulses (e.g. +245% 1y) that momentum can ride while narrative and volume persist.
- [[breakout-trading]] — thin liquidity and a wide historical range (ATL $0.0039 to ATH $0.2826) create clean breakout/breakdown levels off consolidation.
- [[atr-trailing-stop]] — high intraday volatility (24h range spanning ~15%) makes ATR-based trailing exits essential for locking gains and capping drawdown on a spot-only asset.
- [[dca-strategy]] — for conviction accumulation, staggered buys smooth the extreme volatility and single-venue slippage of a small-cap memecoin.
- [[volatility-targeting]] — scaling exposure inversely to realized volatility keeps risk bounded given TROLL's erratic swings and shallow depth.
- [[meme-coin-cycle]] — TROLL is a parody/4chan-themed meme token whose price is driven by attention cycles, aligning with meme-cycle timing frameworks.

### Volatility & regime character

Small-cap (rank ~477) Solana memecoin with high beta and pronounced reflexivity: moves are attention- and flow-driven rather than fundamental, with no intrinsic cash flows. Correlation to BTC/ETH is loose in trends but tends to spike during broad risk-off deleveraging, when small-cap memes typically underperform. Expect fat-tailed returns, sharp mean-reverting spikes, and regime shifts tied to social/narrative momentum rather than macro data.

### Risk flags

- Liquidity/venue concentration: spot-only with thin depth; single-venue execution risk and elevated slippage on size.
- Narrative dependence: value is purely meme/attention-driven ("no intrinsic value"), so sentiment reversals can be abrupt and severe.
- Supply/emissions: near-fully-circulating (MC/FDV ~1.00) limits unlock overhang, but concentrated holders on-chain remain a distribution risk.
- Drawdown risk: currently ~84% below ATH, illustrating the deep, durable drawdowns characteristic of the category.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=TROLLUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=TROLLUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=TROLLUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=TROLLUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

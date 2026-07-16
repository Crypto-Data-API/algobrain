---
title: "LOFI"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, altcoins, memecoins]
aliases: ["LOFI"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://lofitheyeti.com/"
related: ["[[crypto-markets]]", "[[binance]]", "[[dca-strategy]]", "[[narrative-trading]]"]
---

# LOFI

**LOFI** (LOFI) is a cryptocurrency. It ranks **#1777** by market capitalization. My name is LOFI. I was frozen in the Himalayas for centuries, but I've awakened and am ready to build a brighter future 

Born again in the 21st century, Lofi embodies optimism, courage, and vision for a better tomorrow.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LOFI |
| **Market Cap Rank** | #1777 |
| **Market Cap** | $3.64M |
| **Current Price** | $0.00364327 |
| **Categories** | Meme, Sui Meme |
| **Website** | [https://lofitheyeti.com/](https://lofitheyeti.com/) |

---

## Overview

My name is LOFI. I was frozen in the Himalayas for centuries, but I've awakened and am ready to build a brighter future 

Born again in the 21st century, Lofi embodies optimism, courage, and vision for a better tomorrow. Lofi is not just an avatar for a new dawn in finance, but a movement. Lofi represents a collective mission to build a thriving, forward-thinking ecosystem on the Sui blockchain. Together, we are Lofi. Together, we are building the future. The future of decentralized finance is bright–build it with us.

Why Lofi?
Lofi isn’t just a brand; it’s a movement.
Optimistic by Nature: Lofi sees the brighter side of the future and is determined to build it right.

‍Bold Yet Brave: Unafraid to challenge norms, Lofi stands for progress, collaboration, and action.

‍Impact-Driven: Lofi recognizes the power of decentralized finance can make a tangible difference in the world.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.00B LOFI |
| **Total Supply** | 1.00B LOFI |
| **Max Supply** | 1.00B LOFI |
| **Fully Diluted Valuation** | $3.64M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2503 (2024-12-15) |
| **Current vs ATH** | -98.54% |
| **All-Time Low** | $0.00262668 (2026-03-29) |
| **Current vs ATL** | +38.71% |
| **24h Change** | -6.07% |
| **7d Change** | -3.49% |
| **30d Change** | -14.03% |
| **1y Change** | -91.63% |

---

## Platform & Chain Information

**Native Chain:** Sui

### Contract Addresses

| Chain | Address |
|---|---|
| Sui | `0xf22da9a24ad027cccb5f2d496cbe91de953d363513db08a3a734d361c7c17503::LOFI::LOFI` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | LOFI/USD | N/A |
| KuCoin | LOFI/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://lofitheyeti.com/](https://lofitheyeti.com/) |
| **Twitter** | [@lofitheyeti](https://twitter.com/lofitheyeti) |
| **Telegram** | [LofiOnSui](https://t.me/LofiOnSui) (6,788 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $136,689.00 |
| **Market Cap Rank** | #1777 |
| **24h Range** | $0.00361304 — $0.00389579 |
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

Tradable on Binance SPOT only — no liquid perpetual venue, so leverage/short access is limited and this is a spot-primary asset. Perp funding/basis/liquidation strategies do NOT apply. With no listed perp, positions must be built and unwound in spot, so directional exposure is constrained to what free-float liquidity supports and shorting is effectively unavailable. Thin depth relative to a small-cap market cap means execution should lean on limit/passive orders, staged entries, and modest position sizing to avoid moving the book; slippage — not fees — is the dominant cost, and size should be scaled to observed 24h volume rather than notional conviction.

### Applicable strategies

- [[dca-strategy]] — spot-only, small-cap microcap with no shorting; averaging in over time smooths entry across a highly volatile, illiquid tape.
- [[breakout-and-retest]] — low-float memecoins trade in long compressions punctuated by sharp expansions; waiting for a retest filters false breaks in thin liquidity.
- [[atr-trailing-stop]] — wide, reflexive swings demand a volatility-scaled trailing exit rather than fixed stops to survive noise while locking gains.
- [[rsi-mean-reversion]] — deep drawdown from ATH and choppy ranges produce frequent oversold spikes that snap back in spot.
- [[narrative-trading]] — as a Sui-ecosystem meme token, price is driven by chain/meme narrative cycles more than fundamentals.
- [[volatility-targeting]] — sizing to a volatility budget keeps risk bounded given the coin's outsized daily swings and shallow depth.

### Volatility & regime character

Small-cap (sub-$5M) Sui-ecosystem memecoin with high reflexivity: sentiment- and narrative-driven, prone to sharp, low-liquidity swings and mean-reverting chop between events. Down heavily from its 2024 all-time high, it behaves as a high-beta risk asset that amplifies broader crypto moves and is loosely correlated to BTC/ETH risk-on/risk-off regimes while dominated by Sui-meme narrative flows.

### Risk flags

- Liquidity/venue concentration: thin 24h volume and few spot venues make entries/exits slippage-prone and vulnerable to venue-specific outages or delistings.
- No perp market: no shorting or hedging via perps; downside must be managed by sizing and spot exits.
- Narrative dependence: value hinges on meme/Sui-ecosystem sentiment with limited fundamental support, so momentum can reverse abruptly.
- Supply/holder concentration: microcap float can be dominated by a few holders, raising the risk of outsized moves on large transfers.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=LOFIUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=LOFIUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=LOFIUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=LOFIUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

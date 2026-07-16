---
title: "Alien Worlds"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, nft, defi, altcoins, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["TLM"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://alienworlds.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[narrative-trading]]"]
---

# Alien Worlds

**Alien Worlds** (TLM) is a DeFi NFT metaverse where you can collect and play with unique digital items.

It is the 19th project on Binance Launchpad, for more information, please refer to Binance Announcement Post. It ranks **#1119** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TLM |
| **Market Cap Rank** | #1119 |
| **Market Cap** | $10.78M |
| **Current Price** | $0.00154447 |
| **Categories** | Gaming (GameFi), NFT, Binance Launchpool, Play To Earn, Card Games, Gaming Governance Token, MMO |
| **Website** | [https://alienworlds.io/](https://alienworlds.io/) |

---

## Overview

Alien Worlds is a DeFi NFT metaverse where you can collect and play with unique digital items.

It is the 19th project on Binance Launchpad, for more information, please refer to Binance Announcement Post.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 6.98B TLM |
| **Total Supply** | 7.04B TLM |
| **Max Supply** | 10.00B TLM |
| **Fully Diluted Valuation** | $10.88M |
| **Market Cap / FDV Ratio** | 0.99 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.7397 (2021-05-03) |
| **Current vs ATH** | -99.79% |
| **All-Time Low** | $0.00081743 (2026-07-01) |
| **Current vs ATL** | +88.69% |
| **24h Change** | -7.84% |
| **7d Change** | -34.99% |
| **30d Change** | +53.23% |
| **1y Change** | -71.32% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x888888848b652b3e3a0f34c96e00eec0f3a23f72` |
| Wax | `TLM-wax-alien.worlds` |
| Binance Smart Chain | `0x2222227e22102fe3322098e4cbfe18cfebd57c95` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | TLM/USDT | N/A |
| Kraken | TLM/USD | N/A |
| Bitget | TLM/USDT | N/A |
| KuCoin | TLM/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://alienworlds.io/](https://alienworlds.io/) |
| **Twitter** | [@alienworlds](https://twitter.com/alienworlds) |
| **Telegram** | [AlienWorldsOffical](https://t.me/AlienWorldsOffical) (12,387 members) |
| **Discord** | [https://discord.com/invite/QHPJxuq](https://discord.com/invite/QHPJxuq) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $11.54M |
| **Market Cap Rank** | #1119 |
| **24h Range** | $0.00153884 — $0.00169045 |
| **CoinGecko Sentiment** | 67% positive |
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

TLM is tradable on **Binance** as both a spot pair (TLM/USDT) and a **USD-margined perpetual**, exposing funding rates, open interest, and liquidation flow. It is **not** listed on Hyperliquid, so Binance is the primary — effectively sole — venue for leveraged exposure. This concentration means the Binance USD-M perp order book and funding schedule dictate execution quality for any levered position; there is no deep alternative perp venue to arbitrage against or fall back on. As a low-market-cap token, spot and perp liquidity is thin relative to majors, so slippage widens quickly on size. Position sizing should be scaled down accordingly, orders worked patiently (limit/VWAP rather than aggressive market fills), and traders should assume that crowded funding or a liquidation sweep can move price disproportionately given the shallow book.

### Applicable strategies

- [[funding-rate-harvest]] — capture recurring funding on the Binance TLM perp when the rate is persistently one-sided, a common pattern in speculative small-cap GameFi tokens.
- [[crowded-long-funding-fade]] — TLM's reflexive rallies attract crowded longs; fading richly positive funding into exhaustion is a repeatable edge.
- [[liquidation-cascade-fade]] — thin liquidity makes TLM prone to sharp liquidation sweeps that overshoot, offering mean-reversion entries after forced flushes.
- [[oi-confirmed-trend]] — pairing rising open interest with directional moves helps separate genuine trend from thin-book noise on this low-cap perp.
- [[volatility-breakout]] — TLM's high realized volatility and frequent range compressions make ATR/volatility-triggered breakouts well suited to its regime.
- [[narrative-trading]] — as a GameFi/NFT metaverse token, TLM trades heavily on gaming and metaverse narrative cycles rather than fundamentals.

### Volatility & regime character

TLM is a small-cap (rank ~1117) GameFi/NFT token with high realized volatility and strong reflexive, memecoin-like behaviour on gaming and metaverse narratives. It carries high beta to BTC/ETH risk-on/risk-off swings but can decouple violently on token-specific catalysts. Deeply off its all-time high, price action tends to be range-bound with periodic sharp squeezes rather than sustained trends, so regime tends to alternate between low-liquidity chop and narrative-driven volatility spikes.

### Risk flags

- **Venue concentration** — leveraged trading is effectively Binance-only; a delisting, funding regime shift, or outage removes the primary market.
- **Thin liquidity** — low market cap and modest volume mean wide spreads, high slippage, and outsized impact from liquidation cascades.
- **Supply/emissions** — circulating supply is a large share of a 10B max supply; ongoing emissions and unlocks can pressure price.
- **Narrative dependence** — valuation hinges on GameFi/metaverse sentiment cycles; fading narratives can drain liquidity and volume rapidly.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=TLMUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=TLMUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=TLM` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=TLM` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=TLMUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=TLMUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=TLM"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

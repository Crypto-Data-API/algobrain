---
title: "Dogs"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, derivatives, memecoins, altcoins]
aliases: ["DOGS"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://t.me/dogshouse_bot"
related: ["[[crypto-markets]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[meme-coin-cycle]]", "[[funding-rate-harvest]]"]
---

# Dogs

**Dogs** (DOGS) is community is a vibrant, community-driven initiative built on the TON Blockchain, designed to leverage Telegram's vast user base and native meme culture. It ranks **#764** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | DOGS |
| **Market Cap Rank** | #764 |
| **Market Cap** | $22.34M |
| **Current Price** | $0.00004324 |
| **Categories** | Meme, Dog-Themed, TON Ecosystem, TON Meme |
| **Website** | [https://t.me/dogshouse_bot](https://t.me/dogshouse_bot) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Overview

Dogs Community is a vibrant, community-driven initiative built on the TON Blockchain, designed to leverage Telegram's vast user base and native meme culture. Centered around a beloved dog mascot originally created by Telegram's founder, the project aims to introduce millions to blockchain technology through tokenized stickers, fostering a fun and engaging ecosystem with a focus on community ownership and fair rewards distribution.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 516.75B DOGS |
| **Total Supply** | 550.00B DOGS |
| **Max Supply** | 550.00B DOGS |
| **Fully Diluted Valuation** | $15.08M |
| **Market Cap / FDV Ratio** | 0.94 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.00163299 (2024-08-28) |
| **Current vs ATH** | -98.32% |
| **All-Time Low** | $0.00002375 (2026-02-28) |
| **Current vs ATL** | +15.47% |
| **24h Change** | -5.00% |
| **7d Change** | -0.24% |
| **30d Change** | -25.38% |
| **1y Change** | -74.25% |

---

## Platform & Chain Information

**Native Chain:** The Open Network

### Contract Addresses

| Chain | Address |
|---|---|
| The Open Network | `EQCvxJy4eG8hyHBFsZ7eePxrRsUQSFE_jpptRAYBmcG_DOGS` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | DOGS/USDT | N/A |
| Kraken | DOGS/USD | N/A |
| Bitget | DOGS/USDT | N/A |
| KuCoin | DOGS/USDT | N/A |
| Crypto.com Exchange | DOGS/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://t.me/dogshouse_bot](https://t.me/dogshouse_bot) |
| **Twitter** | [@realDogsHouse](https://twitter.com/realDogsHouse) |
| **Telegram** | [dogs_community](https://t.me/dogs_community) (9.15M members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.99M |
| **Market Cap Rank** | #764 |
| **24h Range** | $0.00002715 — $0.00002921 |
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

DOGS is a genuinely two-venue derivatives market. It trades on **Binance** (DOGS/USDT spot plus a USD-margined perpetual) and on **Hyperliquid** as **DOGS-PERP**, where leverage runs up to roughly 40-50x. Because the perp is quoted per-thousand tokens (Hyperliquid ticker `kDOGS`), size and margin math should be done in the kDOGS unit to avoid mis-sized positions on a sub-penny asset. Having deep CEX spot on Binance alongside a liquid on-chain perp gives reasonably tight two-sided depth, but a sub-$25M-cap memecoin still thins out fast in size — split large clips across venues, work limit orders rather than sweeping the book, and treat displayed depth as fragile during volatility. The dual-venue setup is what makes spot-vs-perp and cross-venue funding/basis trades practical here.

### Applicable strategies

- [[funding-rate-harvest]] — collect perp funding on a memecoin that swings between crowded-long and crowded-short, where funding frequently runs rich in one direction.
- [[hl-vs-cex-funding-divergence]] — arbitrage funding gaps between the Hyperliquid DOGS-PERP and Binance's USD-margined perp, which can decouple on a thin sub-$25M-cap name.
- [[cash-and-carry]] — pair Binance DOGS/USDT spot against a short perp to capture basis when the perp trades at a premium during meme-driven pumps.
- [[liquidation-cascade-fade]] — fade the over-extended flushes that a 40-50x-levered, low-cap memecoin routinely produces on both venues.
- [[breakout-trading]] — trade decisive moves out of the long, grinding consolidations typical of a post-ATH memecoin far below its highs.
- [[meme-coin-cycle]] — position around the narrative/attention pulses that drive DOGS, a Telegram/TON meme token whose flows are sentiment-led.

### Volatility & regime character

DOGS is a low-cap **memecoin** (TON ecosystem, Telegram-native, dog-themed) and trades with classic memecoin reflexivity: attention-driven pumps, sharp reversals, and stretches of grinding decay — it sits ~98% below its 2024 ATH. Realized volatility is high and event-clustered rather than steady. Directionally it carries high beta to broad crypto risk (BTC/ETH) but its largest moves are idiosyncratic, driven by memecoin-sector rotation and Telegram/TON-community sentiment rather than macro. Expect it to overshoot in both directions relative to majors.

### Risk flags

- **Liquidity / venue concentration** — thin sub-$25M-cap market; depth is concentrated on Binance spot and the two perps, so slippage and gap risk rise quickly in size or during stress.
- **Perp funding dislocations** — with high leverage available, funding can spike and flip fast; carry and basis trades can be whipsawed by sudden funding resets.
- **Narrative dependence** — value is largely attention-driven (Telegram/TON meme cycle); fading engagement can drive persistent, low-liquidity decay.
- **Supply / emissions** — very large token count (hundreds of billions of units) and near-full FDV mean any incremental unlocks or distribution shifts weigh directly on a shallow float.
- **Reflexive cascades** — high-leverage positioning makes DOGS prone to self-reinforcing liquidation cascades in both directions.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=kDOGS` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=kDOGS` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=kDOGS&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=kDOGS&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=kDOGS"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

---
title: "Hashflow"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, defi, altcoins, derivatives, perpetual-futures, funding-rate, open-interest, liquidations]
aliases: ["HFT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://hashflow.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]"]
---

# Hashflow

**Hashflow** (HFT) is a multichain decentralized exchange (DEX) that enables users to trade digital assets on leading blockchains including Ethereum, Arbitrum, Avalanche, BNB Chain, Optimism, Polygon, and Solana in just a matter of seconds. Hashflow leverages an intent-based smart order routing architecture to offer traders the best prices, access to over $8B in liquidity, and the ability to trade every token. It ranks **#1314** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | HFT |
| **Market Cap Rank** | #1314 |
| **Market Cap** | $7.49M |
| **Current Price** | $0.00882555 |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), Binance Launchpool, MEV Protection |
| **Website** | [https://hashflow.com/](https://hashflow.com/) |

---

## Overview

Hashflow is a multichain decentralized exchange (DEX) that enables users to trade digital assets on leading blockchains including Ethereum, Arbitrum, Avalanche, BNB Chain, Optimism, Polygon, and Solana in just a matter of seconds. Hashflow leverages an intent-based smart order routing architecture to offer traders the best prices, access to over $8B in liquidity, and the ability to trade every token. Since launching in April 2021, Hashflow has facilitated over $18B in total trade volume, making it a top 10 DEX.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 849.00M HFT |
| **Total Supply** | 1.00B HFT |
| **Max Supply** | 1.00B HFT |
| **Fully Diluted Valuation** | $8.83M |
| **Market Cap / FDV Ratio** | 0.85 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.61 (2022-11-07) |
| **Current vs ATH** | -99.76% |
| **All-Time Low** | $0.00762618 (2026-07-01) |
| **Current vs ATL** | +15.87% |
| **24h Change** | -1.22% |
| **7d Change** | -0.09% |
| **30d Change** | -16.45% |
| **1y Change** | -89.26% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xb3999f658c0391d94a37f7ff328f3fec942bcadc` |
| Binance Smart Chain | `0x44ec807ce2f4a6f2737a92e985f318d035883e47` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | HFT/USDT | N/A |
| Kraken | HFT/USD | N/A |
| Bitget | HFT/USDT | N/A |
| KuCoin | HFT/USDT | N/A |
| Crypto.com Exchange | HFT/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XB3999F658C0391D94A37F7FF328F3FEC942BCADC/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://hashflow.com/](https://hashflow.com/) |
| **Twitter** | [@hashflow](https://twitter.com/hashflow) |
| **Reddit** | [https://www.reddit.com/r/Hashflow](https://www.reddit.com/r/Hashflow) |
| **Telegram** | [hashflowdex](https://t.me/hashflowdex) (4,370 members) |
| **Discord** | [https://discord.com/invite/hashflow](https://discord.com/invite/hashflow) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.05M |
| **Market Cap Rank** | #1314 |
| **24h Range** | $0.00874525 — $0.00914836 |
| **CoinGecko Sentiment** | 0% positive |
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

HFT is tradable on **Binance** as both **spot** (HFT/USDT) and a **USD-margined perpetual**, which surfaces funding, open interest, and liquidation data for the token. It is **not listed on Hyperliquid**, so **Binance is the primary leveraged venue** and the reference market for both price discovery and derivatives flow. With a small ~$7M market cap and thin ($2M-class) 24h volume, order books are shallow: leverage should be conservative, position sizing kept small relative to depth, and entries/exits worked with limit orders to avoid slippage. Venue concentration on Binance means funding and liquidation dynamics on that single perp dominate execution — a spot fill on Kraken, Bitget, KuCoin, or Crypto.com will not carry the same depth, so most leveraged and carry strategies must route through Binance.

### Applicable strategies

- [[funding-rate-harvest]] — Collect the Binance perp funding stream on HFT when the rate is persistently skewed, sizing small given thin liquidity.
- [[crowded-long-funding-fade]] — Fade over-leveraged longs on this low-cap DEX token when funding turns sharply positive and OI builds into a stalled price.
- [[liquidation-cascade-fade]] — Shallow books make HFT prone to violent liquidation wicks on the Binance perp; fade the flush after forced selling exhausts.
- [[cash-and-carry]] — Harvest spot-vs-perp basis by pairing Binance HFT spot against the USD-M perp when the term structure pays enough to cover fees.
- [[rsi-mean-reversion]] — A range-bound, low-momentum micro-cap; mean-revert oversold/overbought extremes on the Binance chart.
- [[oi-price-exhaustion]] — Watch Binance open interest diverging from price to flag exhausted moves before a reversal in this thin market.

### Volatility & regime character

HFT is a **small-cap DeFi / DEX infrastructure token** with high idiosyncratic volatility and pronounced reflexivity typical of low-liquidity altcoins. It trades with strong high-beta correlation to BTC/ETH risk-on/risk-off swings while amplifying moves on the downside — reflected in its deep drawdown from the 2022 all-time high. Absent a fresh DeFi or DEX-sector narrative, price action tends to be range-bound and drift-lower, punctuated by sharp liquidity-driven spikes.

### Risk flags

- **Liquidity & venue concentration** — Very thin volume with leveraged flow concentrated on the single Binance perp; slippage and gap risk are elevated.
- **Emissions / supply** — Circulating supply (~849M) is a large share of the 1B max supply; remaining unlocks and reward emissions can pressure price.
- **Narrative dependence** — As a DEX/DeFi infra token, performance hinges on the DeFi narrative and Hashflow protocol traction rather than broad demand.
- **Micro-cap fragility** — At a ~$7M market cap, the token is exposed to delisting risk, wash-trading distortions, and single-actor manipulation.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=HFTUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=HFTUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=HFT` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=HFT` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=HFTUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=HFTUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=HFT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

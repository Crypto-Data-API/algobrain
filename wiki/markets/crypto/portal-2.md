---
title: "Portal"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["PORTAL"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.portalgaming.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]"]
---

# Portal

**Portal** (PORTAL) is a cryptocurrency. It ranks **#1223** by market capitalization. Onboarding the first billion gamers into Web3.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PORTAL |
| **Market Cap Rank** | #1223 |
| **Market Cap** | $8.90M |
| **Current Price** | $0.0111 |
| **Categories** | Gaming (GameFi), Gaming Platform |
| **Website** | [https://www.portalgaming.com/](https://www.portalgaming.com/) |

---

## Overview

Onboarding the first billion gamers into Web3.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 800.73M PORTAL |
| **Total Supply** | 1.00B PORTAL |
| **Max Supply** | 1.00B PORTAL |
| **Fully Diluted Valuation** | $11.11M |
| **Market Cap / FDV Ratio** | 0.80 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.36 (2024-02-29) |
| **Current vs ATH** | -99.67% |
| **All-Time Low** | $0.00734734 (2026-05-29) |
| **Current vs ATL** | +51.18% |
| **24h Change** | +2.31% |
| **7d Change** | -1.76% |
| **30d Change** | -31.93% |
| **1y Change** | -80.72% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x1bbe973bef3a977fc51cbed703e8ffdefe001fed` |
| Base | `0x0ffebc403f2d3dd9ea5501ca03916e98967acb2d` |
| Solana | `FMQjDvT1GztVxdvYgMBEde4L54fftFGx9m5GmbqeJGM5` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | PORTAL/USDT | N/A |
| Kraken | PORTAL/USD | N/A |
| Bitget | PORTAL/USDT | N/A |
| KuCoin | PORTAL/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X1BBE973BEF3A977FC51CBED703E8FFDEFE001FED/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.portalgaming.com/](https://www.portalgaming.com/) |
| **Twitter** | [@Portalcoin](https://twitter.com/Portalcoin) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $7.48M |
| **Market Cap Rank** | #1223 |
| **24h Range** | $0.0108 — $0.0113 |
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

PORTAL is tradable on **Binance** as both spot (PORTAL/USDT) and a **USD-margined perpetual**, giving access to funding, open interest, and liquidation data on a single deep venue. It is **NOT on Hyperliquid**, so Binance is the primary — effectively sole tier-1 — leveraged venue. With a sub-$10M market cap and thin 24h volume, the perpetual is the main source of leverage and price discovery, but order books are shallow: even modest size can move price, funding can swing sharply, and stops/liquidations can chain. Venue concentration means execution should assume wide spreads, conservative position sizing, and reliance on Binance depth for entries/exits; cross-venue arbitrage is limited by fragmented, low-liquidity listings (Kraken, Bitget, KuCoin).

### Applicable strategies

- [[liquidation-cascade-fade]] — thin book plus leveraged Binance perp makes PORTAL prone to over-extended liquidation wicks that snap back, offering fade entries.
- [[funding-rate-harvest]] — a low-cap gaming token can sustain persistently skewed perp funding, letting a delta-neutral spot/perp position collect the carry.
- [[crowded-long-funding-fade]] — narrative-driven long crowding into a micro-cap often prints extreme positive funding, flagging exhausted longs to fade.
- [[breakout-and-retest]] — with price pinned near all-time lows in a tight range, clean breakouts followed by a retest give structured, defined-risk entries.
- [[rsi-mean-reversion]] — low liquidity produces sharp, mean-reverting swings well-suited to oscillator-based reversion around range extremes.
- [[oi-confirmed-trend]] — pairing Binance open-interest changes with price helps distinguish real, OI-backed moves from thin-liquidity noise.

### Volatility & regime character

PORTAL is a **small/micro-cap GameFi (Gaming) infrastructure token** on Ethereum with high beta to broad crypto risk sentiment and to BTC/ETH direction. Down more than 99% from its all-time high, it trades with reflexive, narrative-driven bursts typical of low-cap gaming/altcoin plays: illiquid ranges punctuated by violent expansion on catalysts. Realized volatility is elevated relative to majors, and moves are amplified by leverage on the Binance perp. Correlation to BTC/ETH is meaningful in risk-off regimes (it sells off with beta) but decoupling occurs on token-specific gaming or ecosystem news.

### Risk flags

- **Liquidity & venue concentration** — sub-$10M cap and thin volume, with leveraged trading concentrated on Binance; slippage and gap risk are high.
- **Emissions/unlocks** — circulating supply is ~80% of max (MC/FDV 0.80); remaining supply and any vesting can pressure price on new unlocks.
- **Narrative dependence** — value is tied to GameFi/Web3-gaming adoption momentum; fading interest can drain liquidity quickly.
- **Multi-chain fragmentation** — tokens across Ethereum, Base, and Solana can split liquidity and complicate on-chain positioning.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=PORTALUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=PORTALUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=PORTAL` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=PORTAL` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=PORTALUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=PORTALUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=PORTAL"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

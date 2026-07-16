---
title: "Vanar Chain"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["VANRY"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://vanarchain.com"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[momentum-investing]]"]
---

# Vanar Chain

**Vanar Chain** (VANRY) is a cryptocurrency. It ranks **#1089** by market capitalization. Vanar, a L1 designed from the ground up, builds upon our technological expertise to foster practical real-world adoption.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | VANRY |
| **Market Cap Rank** | #1089 |
| **Market Cap** | $11.48M |
| **Current Price** | $0.00533862 |
| **Categories** | Artificial Intelligence (AI), Smart Contract Platform, Layer 1 (L1) |
| **Website** | [https://vanarchain.com](https://vanarchain.com) |

---

## Overview

Vanar, a L1 designed from the ground up, builds upon our technological expertise to foster practical real-world adoption. Drawing upon years of experience working with the gaming, entertainment, and brand sectors, our primary focus is on ushering billions of consumers into the world of web3.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.15B VANRY |
| **Total Supply** | 2.38B VANRY |
| **Max Supply** | 2.40B VANRY |
| **Fully Diluted Valuation** | $12.69M |
| **Market Cap / FDV Ratio** | 0.90 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.3723 (2024-03-13) |
| **Current vs ATH** | -98.57% |
| **All-Time Low** | $0.00288034 (2026-07-03) |
| **Current vs ATL** | +85.08% |
| **24h Change** | -5.76% |
| **7d Change** | -30.13% |
| **30d Change** | +46.50% |
| **1y Change** | -85.21% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x8de5b80a0c1b02fe4976851d030b36122dbb8624` |
| Vanar Chain | `0x8de5b80a0c1b02fe4976851d030b36122dbb8624` |
| Polygon Pos | `0x8de5b80a0c1b02fe4976851d030b36122dbb8624` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | VANRY/USDT | N/A |
| Kraken | VANRY/USD | N/A |
| Bitget | VANRY/USDT | N/A |
| KuCoin | VANRY/USDT | N/A |
| Crypto.com Exchange | VANRY/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X8DE5B80A0C1B02FE4976851D030B36122DBB8624/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://vanarchain.com](https://vanarchain.com) |
| **Twitter** | [@Vanarchain](https://twitter.com/Vanarchain) |
| **Telegram** | [vanarofficial](https://t.me/vanarofficial) (15,245 members) |
| **Whitepaper** | [https://cdn.vanarchain.com/vanarchain/vanar_whitepaper.pdf](https://cdn.vanarchain.com/vanarchain/vanar_whitepaper.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $10.54M |
| **Market Cap Rank** | #1089 |
| **24h Range** | $0.00533082 — $0.00582372 |
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

VANRY trades on **Binance** as both **spot (VANRY/USDT)** and a **USD-margined perpetual**, exposing funding, open interest, and liquidation data. It is **NOT listed on Hyperliquid**, so Binance is the primary — effectively sole — leveraged venue for this name. With a sub-$15M market cap and thin ~$10M daily volume, the perp order book is shallow: leverage and liquidity are concentrated on one exchange, so large or aggressive orders will move price and incur slippage. Position sizing must account for this single-venue concentration — there is no deep secondary perp market to hedge across, and execution should lean on limit/passive fills and smaller clips to avoid signalling into a thin book.

### Applicable strategies

- [[funding-rate-harvest]] — collect perp funding on a delta-neutral spot-vs-perp position while VANRY funding swings on Binance, the only funding venue.
- [[liquidation-cascade-fade]] — a thin single-venue perp book makes VANRY prone to sharp forced-liquidation wicks that mean-revert; fade the flush.
- [[breakout-and-retest]] — low-float, low-cap tokens like VANRY trend hard on catalysts; enter breakouts only after a confirmed retest to filter fakeouts in a thin book.
- [[oi-confirmed-trend]] — pair Binance open-interest expansion with price to confirm genuine trend legs versus low-liquidity noise in VANRY.
- [[rsi-mean-reversion]] — after -30% weekly swings VANRY reaches oversold/overbought extremes that revert; RSI bands time entries in its range chop.
- [[atr-trailing-stop]] — high intraday range (~10% 24h band) demands volatility-scaled trailing stops rather than fixed levels to survive VANRY's whippy moves.

### Volatility & regime character

VANRY is a small-cap L1/infra token (rank ~1089) with high-beta, reflexive behaviour: it amplifies broad crypto moves and swings on AI/gaming narrative flows rather than trading independently. Expect strong positive correlation to BTC/ETH risk-on/risk-off regimes, with sharp idiosyncratic spikes on chain-specific catalysts. Realized volatility is elevated (30d +46%, 7d -30% in recent windows), typical of a low-float altcoin far below its all-time high.

### Risk flags

- **Venue concentration** — leveraged exposure lives almost entirely on Binance; a delisting, funding spike, or outage removes the main hedging/trading rail.
- **Liquidity** — ~$10M daily volume and an $11M cap mean wide spreads, slippage, and vulnerability to liquidation cascades and stop hunts.
- **Supply/emissions** — circulating supply is ~90% of max (MC/FDV 0.90), so dilution risk is modest but ongoing unlocks/emissions toward the 2.40B cap still add sell pressure.
- **Narrative dependence** — price is tightly tied to AI/gaming/consumer-web3 narrative cycles; sentiment reversals can drive rapid drawdowns disconnected from fundamentals.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=VANRYUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=VANRYUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=VANRY` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=VANRY` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=VANRYUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=VANRYUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=VANRY"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

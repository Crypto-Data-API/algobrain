---
title: "Moonriver"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["MOVR"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://moonbeam.network/networks/moonriver/"
related: ["[[crypto-markets]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

# Moonriver

**Moonriver** (MOVR) is a fully Ethereum-compatible smart contract parachain on Kusama. Due to this Ethereum-like design and developer-friendly approach, Moonriver has attracted dozens of projects to build on it: https://moonbeam.network/community/projects/. It ranks **#912** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MOVR |
| **Market Cap Rank** | #912 |
| **Market Cap** | $16.42M |
| **Current Price** | $1.32 |
| **Categories** | Smart Contract Platform, Layer 1 (L1) |
| **Website** | [https://moonbeam.network/networks/moonriver/](https://moonbeam.network/networks/moonriver/) |

---

## Overview

Moonriver is a fully Ethereum-compatible smart contract parachain on Kusama. Due to this Ethereum-like design and developer-friendly approach, Moonriver has attracted dozens of projects to build on it: https://moonbeam.network/community/projects/. It does this by providing a full EVM implementation, a Web3-compatible API, and bridges that connect Moonriver to existing Ethereum networks. This allows developers to deploy existing Solidity/Vyper smart contracts and DApp frontends to Moonriver with minimal changes.

It is intended to be a companion network to Moonbeam (on Polkadot), where it will provide a permanently incentivized canary network. New code will ship to Moonriver first, where it can be tested and verified under real economic conditions. Once proven, the same code will ship to Moonbeam on Polkadot.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 12.48M MOVR |
| **Total Supply** | 12.59M MOVR |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $16.57M |
| **Market Cap / FDV Ratio** | 0.99 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $494.26 (2021-09-11) |
| **Current vs ATH** | -99.73% |
| **All-Time Low** | $0.9894 (2026-03-29) |
| **Current vs ATL** | +33.32% |
| **24h Change** | +0.15% |
| **7d Change** | -2.88% |
| **30d Change** | -9.05% |
| **1y Change** | -80.48% |

---

## Platform & Chain Information

**Native Chain:** Moonriver

### Contract Addresses

| Chain | Address |
|---|---|
| Moonriver | `0x98878b06940ae243284ca214f92bb71a2b032b8a` |
| Base | `0x43feb74608334dda8c1a6500d185cfc3ea962b83` |
| Meter | `0xb158870beb809ad955bf56065c5c10d7fd957cc0` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | MOVR/USDT | N/A |
| Kraken | MOVR/USD | N/A |
| Bitget | MOVR/USDT | N/A |
| KuCoin | MOVR/USDT | N/A |
| Crypto.com Exchange | MOVR/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://moonbeam.network/networks/moonriver/](https://moonbeam.network/networks/moonriver/) |
| **Twitter** | [@MoonriverNW](https://twitter.com/MoonriverNW) |
| **Reddit** | [https://www.reddit.com/r/moonbeam/](https://www.reddit.com/r/moonbeam/) |
| **Telegram** | [Moonbeam_Official](https://t.me/Moonbeam_Official) (16,243 members) |
| **GitHub** | [https://github.com/PureStake/moonbeam/](https://github.com/PureStake/moonbeam/) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 937 |
| **GitHub Forks** | 384 |
| **Commits (4 weeks)** | 8 |
| **Pull Requests Merged** | 2,593 |
| **Contributors** | 78 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.78M |
| **Market Cap Rank** | #912 |
| **24h Range** | $1.30 — $1.38 |
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

MOVR is tradable on [[binance]] — both spot (MOVR/USDT) and a USD-margined [[perpetual-futures|perpetual]] contract carrying funding, open interest, and liquidation data. It is NOT listed on Hyperliquid, so Binance is the primary leveraged venue and the reference point for derivatives-based signals. With a small-cap profile (rank ~#912) and thin spot depth (~$2.78M 24h volume), the single dominant perp venue means order books are shallow: leverage amplifies slippage, funding can swing sharply, and liquidation clusters concentrate on one exchange. Size positions modestly, favor limit/maker execution, and treat Binance funding/OI as the effective market-wide gauge since there is no cross-venue perp to arbitrage against.

### Applicable strategies

- [[funding-rate-harvest]] — a single-venue Binance perp with sparse depth tends to produce persistent funding skews harvestable against a spot hedge.
- [[crowded-long-funding-fade]] — low-float, low-liquidity MOVR is prone to crowded leveraged longs that push funding rich; fade the extreme.
- [[cash-and-carry]] — hold spot MOVR versus short the USD-M perp to capture basis/funding when the perp trades at a premium.
- [[liquidation-cascade-fade]] — thin single-venue books make MOVR susceptible to sharp liquidation flushes that overshoot and snap back.
- [[oi-confirmed-trend]] — pairing Binance open-interest changes with price filters low-conviction moves in an illiquid name.
- [[breakout-and-retest]] — wide, jumpy ranges reward waiting for a confirmed breakout retest rather than chasing the initial spike.

### Volatility & regime character

MOVR is a small-cap infrastructure/L1 token (Kusama parachain, EVM-compatible canary network for Moonbeam) that sits far below its 2021 ATH. It behaves as a high-beta altcoin: it is broadly correlated to BTC/ETH risk-on/risk-off swings but with amplified drawdowns and low idiosyncratic liquidity, so moves are reflexive and can gap on thin volume. Expect elevated realized volatility relative to majors and regime shifts driven more by broad-market flows than by protocol-specific catalysts.

### Risk flags

- Liquidity/venue concentration: Binance is the sole meaningful leveraged venue; a delisting, listing change, or exchange-specific disruption would sharply impair execution and hedging.
- Thin depth: low 24h volume and small circulating float make MOVR vulnerable to slippage and short-lived price manipulation.
- Emissions/supply: max supply is uncensored/unlimited, so ongoing inflation is a structural headwind to hold.
- Narrative dependence: as a Kusama/Moonbeam canary network, sustained interest hinges on the Polkadot/Kusama ecosystem narrative remaining relevant.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=MOVRUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=MOVRUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=MOVR` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=MOVR` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=MOVRUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=MOVRUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=MOVR"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

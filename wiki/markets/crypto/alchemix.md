---
title: "Alchemix"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, defi, altcoins]
aliases: ["ALCX"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://alchemix.fi/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[mean-reversion]]", "[[dca-strategy]]"]
---

# Alchemix

**Alchemix** (ALCX) is token is the governance token for the Alchemix protocol. It ranks **#1532** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ALCX |
| **Market Cap Rank** | #1532 |
| **Market Cap** | $5.21M |
| **Current Price** | $2.06 |
| **Categories** | Decentralized Finance (DeFi), Yield Farming, Governance |
| **Website** | [https://alchemix.fi/](https://alchemix.fi/) |

---

## Overview

Alchemix token is the governance token for the Alchemix protocol.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.53M ALCX |
| **Total Supply** | 3.17M ALCX |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $6.54M |
| **Market Cap / FDV Ratio** | 0.80 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2,066.20 (2021-03-20) |
| **Current vs ATH** | -99.90% |
| **All-Time Low** | $1.84 (2026-07-09) |
| **Current vs ATL** | +12.17% |
| **24h Change** | +3.28% |
| **7d Change** | +4.78% |
| **30d Change** | -45.59% |
| **1y Change** | -76.78% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xdbdb4d16eda451d0503b854cf79d55697f90c8df` |
| Near Protocol | `dbdb4d16eda451d0503b854cf79d55697f90c8df.factory.bridge.near` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ALCX/USDT | N/A |
| Kraken | ALCX/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Balancer V2 | 0XDBDB4D16EDA451D0503B854CF79D55697F90C8DF/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://alchemix.fi/](https://alchemix.fi/) |
| **Twitter** | [@alchemixfi](https://twitter.com/alchemixfi) |
| **Discord** | [https://discord.gg/zAd6dzgwaj](https://discord.gg/zAd6dzgwaj) |
| **GitHub** | [https://github.com/alchemix-finance](https://github.com/alchemix-finance) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $220,416.00 |
| **Market Cap Rank** | #1532 |
| **24h Range** | $2.00 — $2.13 |
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

ALCX is tradable on **Binance SPOT only** — there is no liquid perpetual venue, so leverage and short access are limited and this is a **spot-primary asset**. Perp funding, basis, and liquidation strategies do **not** apply. With a single primary CEX venue and thin 24h turnover, order flow concentrates on the Binance ALCXUSDT book (plus a Kraken USD pair and a Balancer V2 DEX pool for spot swaps). Execution should assume shallow depth: size positions small relative to daily volume, prefer limit/passive fills over market sweeps, and avoid stops clustered at obvious levels that thin books can wick through. Absence of a perp means no built-in short/hedge — directional risk is one-sided unless offset via correlated liquid assets.

### Applicable strategies

- [[dca-strategy]] — spot-only, low-cap token deep in a multi-year drawdown; averaging in over time smooths entry risk without needing leverage or short access.
- [[mean-reversion]] — thin-book microcap prone to sharp overshoots and snapbacks around a compressed range, favoring fade entries at extremes.
- [[rsi-mean-reversion]] — momentum-oscillator extremes on the daily are frequent on a low-liquidity name like ALCX, giving reversion signals when the book overreacts.
- [[range-trading]] — recent price action hugs a tight band (24h range roughly $2.00–$2.13), suiting bounded buy-support / sell-resistance rotation on spot.
- [[buy-and-hold]] — a governance token for an established DeFi protocol trading near all-time lows; a small spot allocation is a straightforward long-only expression for conviction holders.
- [[atr-trailing-stop]] — volatility-scaled trailing exits help manage the wide intraday swings and gap risk typical of a low-cap spot asset with no hedge venue.

### Volatility & regime character

Small-cap DeFi/infra governance token (rank ~1524) with high idiosyncratic volatility and strong reflexivity typical of thin microcaps. Broadly high-beta to BTC/ETH risk regimes — it tends to amplify altcoin risk-on/risk-off moves — but price is also heavily driven by protocol-specific narrative and yield/DeFi rotation rather than pure market beta. Liquidity is low enough that single large orders can move the tape, producing outsized wicks in both directions.

### Risk flags

- **Liquidity / venue concentration** — effectively one primary CEX venue (Binance spot) plus a Kraken pair and a DEX pool; a listing/delisting or venue outage is a material single point of failure.
- **No perp / one-sided exposure** — no liquid perpetual means no native short or hedge; risk is directional and must be managed with position sizing and stops.
- **Small-cap slippage** — thin depth and modest 24h turnover mean market orders and stop cascades can cause significant slippage.
- **Emissions / unlimited max supply** — ALCX has an unlimited max supply with ongoing emissions; monitor circulating-supply growth and governance changes to inflation.
- **Narrative dependence** — value is tied to the Alchemix protocol's DeFi/yield thesis; protocol, TVL, or DeFi-sentiment shocks can dominate price independent of the broader market.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ALCXUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=ALCXUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ALCXUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ALCXUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

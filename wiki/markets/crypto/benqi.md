---
title: "BENQI"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, defi, altcoins]
aliases: ["QI"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://app.benqi.fi/"
related: ["[[crypto-markets]]", "[[avalanche]]", "[[binance]]", "[[dca-strategy]]", "[[narrative-trading]]"]
---

# BENQI

**BENQI** (QI) is a decentralized non-custodial liquidity market protocol, built on Avalanche. The protocol enables users to effortlessly lend, borrow, and earn interest with their digital assets. It ranks **#1291** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | QI |
| **Market Cap Rank** | #1291 |
| **Market Cap** | $7.86M |
| **Current Price** | $0.00109229 |
| **Categories** | Decentralized Finance (DeFi), Yield Farming, Binance Launchpool, Lending/Borrowing Protocols, Liquid Staking Governance Tokens, Liquid Staking |
| **Website** | [https://app.benqi.fi/](https://app.benqi.fi/) |

---

## Overview

BENQI is a decentralized non-custodial liquidity market protocol, built on Avalanche. The protocol enables users to effortlessly lend, borrow, and earn interest with their digital assets. Depositors providing liquidity to the protocol may earn passive income, while borrowers are able to borrow in an over-collateralized manner.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 7.20B QI |
| **Total Supply** | 7.20B QI |
| **Max Supply** | 7.20B QI |
| **Fully Diluted Valuation** | $7.86M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.3942 (2021-08-24) |
| **Current vs ATH** | -99.72% |
| **All-Time Low** | $0.00107105 (2026-06-28) |
| **Current vs ATL** | +2.33% |
| **24h Change** | -6.93% |
| **7d Change** | -5.28% |
| **30d Change** | -21.65% |
| **1y Change** | -84.31% |

---

## Platform & Chain Information

**Native Chain:** Avalanche

### Contract Addresses

| Chain | Address |
|---|---|
| Avalanche | `0x8729438eb15e2c8b576fcc6aecda6a148776c0f5` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | QI/USDT | N/A |
| Kraken | QI/USD | N/A |
| KuCoin | QI/USDT | N/A |
| Crypto.com Exchange | QI/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://app.benqi.fi/](https://app.benqi.fi/) |
| **Twitter** | [@BenqiFinance](https://twitter.com/BenqiFinance) |
| **Telegram** | [BenqiFinance](https://t.me/BenqiFinance) (7,744 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.56M |
| **Market Cap Rank** | #1291 |
| **24h Range** | $0.00108217 — $0.00132390 |
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

QI is tradable on **Binance SPOT only** (QIUSDT) among liquid venues — there is **no liquid perpetual venue**, so leverage/short access is limited and this is a **spot-primary asset**. Perp funding/basis/liquidation strategies do NOT apply. With a sub-$10M market cap and roughly seven-figure daily volume concentrated on a single primary book, order books are thin: position sizing must stay small relative to volume, and execution should favor patient limit orders and time-slicing (VWAP-style) to avoid moving the market. Short exposure is effectively unavailable, so the tradable strategy set is long/flat only.

### Applicable strategies

- [[dca-strategy]] — spot-only, deeply drawn-down microcap where scheduled accumulation smooths the thin, volatile fills better than a single market order.
- [[vwap-trading]] — slicing entries/exits against volume is essential given a single thin book where large clips would slip badly.
- [[breakout-and-retest]] — long/flat microcap that trades in extended ranges; waiting for a confirmed break and retest filters false moves on low liquidity.
- [[rsi-mean-reversion]] — sharp low-cap swings around the range create oversold/overbought extremes suited to spot mean-reversion.
- [[narrative-trading]] — as an Avalanche DeFi lending/liquid-staking token, price is highly sensitive to Avalanche ecosystem and DeFi narrative flows.
- [[atr-trailing-stop]] — volatility-scaled trailing exits protect gains on a low-liquidity name prone to fast reversals.

### Volatility & regime character

Small/micro-cap (rank ~1292) infrastructure/DeFi token on Avalanche with high beta to BTC/ETH and to the broader altcoin risk cycle. Price is reflexive and narrative-driven, amplified by thin liquidity, and trades far below its all-time high with pronounced multi-week drawdown regimes. Expect elevated realized volatility and correlation that spikes during broad crypto risk-off moves.

### Risk flags

- **Liquidity/venue concentration** — primary liquidity sits on a single Binance spot pair; venue delisting or volume decay would sharply impair exit ability.
- **No perp/short access** — long/flat only; no efficient hedge or short expression.
- **Narrative dependence** — returns hinge on Avalanche and DeFi-lending narrative rather than idiosyncratic fundamentals.
- **Emissions/supply** — monitor protocol emissions and governance-token distribution that can pressure spot supply.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=QIUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=QIUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=QIUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=QIUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[avalanche]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

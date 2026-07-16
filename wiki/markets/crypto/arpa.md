---
title: "ARPA"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["ARPA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.arpanetwork.io/en-US"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# ARPA

**ARPA** (ARPA) is a cryptocurrency. It ranks **#1249** by market capitalization. Network (ARPA) is a decentralized secure computation network built to improve the fairness, security, and privacy of blockchains. ARPA threshold BLS signature network serves as the infrastructure of verifiable Random Number Generator (RNG), secure wallet, cross-chain bridge, and decentralized custody across multiple blockchains.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ARPA |
| **Market Cap Rank** | #1249 |
| **Market Cap** | $8.45M |
| **Current Price** | $0.00860501 |
| **Categories** | Privacy Infrastructure, Privacy |
| **Website** | [https://www.arpanetwork.io/en-US](https://www.arpanetwork.io/en-US) |

---

## Overview

ARPA Network (ARPA) is a decentralized secure computation network built to improve the fairness, security, and privacy of blockchains. ARPA threshold BLS signature network serves as the infrastructure of verifiable Random Number Generator (RNG), secure wallet, cross-chain bridge, and decentralized custody across multiple blockchains. 

ARPA was previously known as ARPA Chain, a privacy-preserving Multi-party Computation (MPC) network founded in 2018. ARPA Mainnet has completed over 224,000 computation tasks in the past years. Our experience in MPC and other cryptography laid the foundation for our innovative threshold BLS signature schemes (TSS-BLS) system design and led us to today’s ARPA Network. 

Randcast, a verifiable Random Number Generator (RNG), is the first application that leverages ARPA as infrastructure. Randcast offers a cryptographically generated random source with superior security and low cost compared to other solutions. Metaverse, game, lottery, NFT minting and whitelisting, key generation, and blockchain validator task distribution can benefit from Randcast’s tamper-proof randomness.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 982.17M ARPA |
| **Total Supply** | 2.00B ARPA |
| **Max Supply** | 2.00B ARPA |
| **Fully Diluted Valuation** | $17.21M |
| **Market Cap / FDV Ratio** | 0.49 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2686 (2021-11-03) |
| **Current vs ATH** | -96.80% |
| **All-Time Low** | $0.00339441 (2020-03-13) |
| **Current vs ATL** | +153.38% |
| **24h Change** | -0.49% |
| **7d Change** | -0.92% |
| **30d Change** | -1.29% |
| **1y Change** | -62.90% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xba50933c268f567bdc86e1ac131be072c6b0b71a` |
| Binance Smart Chain | `0x6f769e65c14ebd1f68817f5f1dcdb61cfa2d6f7e` |
| Polygon Pos | `0xee800b277a96b0f490a1a732e1d6395fad960a26` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ARPA/USDT | N/A |
| Kraken | ARPA/USD | N/A |
| Upbit | ARPA/BTC | N/A |
| Bitget | ARPA/USDT | N/A |
| KuCoin | ARPA/USDT | N/A |
| Crypto.com Exchange | ARPA/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.arpanetwork.io/en-US](https://www.arpanetwork.io/en-US) |
| **Twitter** | [@arpaofficial](https://twitter.com/arpaofficial) |
| **Telegram** | [arpa_community](https://t.me/arpa_community) (4,281 members) |
| **GitHub** | [https://github.com/ARPA-Network/mpc-mainnet](https://github.com/ARPA-Network/mpc-mainnet) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 8 |
| **GitHub Forks** | 2 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.22M |
| **Market Cap Rank** | #1249 |
| **24h Range** | $0.00858841 — $0.00874853 |
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

ARPA is tradable on **Binance** — both **spot** (ARPA/USDT) and a **USD-margined perpetual**, which surfaces funding, open interest, and liquidation data. It is **NOT listed on Hyperliquid**, so Binance is the primary leveraged venue for ARPA. As a very small-cap token (~#1247, thin 24h volume), leverage on ARPA carries elevated slippage and liquidation-wick risk: order books are shallow and a single perp venue concentrates price discovery on Binance. Practically, this means execution should lean on limit/VWAP fills, position sizing must stay small relative to depth, and any carry/basis structure depends on Binance funding and spot liquidity rather than a diversified venue set.

### Applicable strategies

- [[funding-rate-harvest]] — collect Binance USD-M perp funding on ARPA when the rate runs persistently positive or negative, sized small given thin liquidity.
- [[crowded-long-funding-fade]] — fade over-leveraged longs when ARPA funding spikes positive on a low-float, retail-driven small-cap.
- [[liquidation-cascade-fade]] — thin books make ARPA prone to over-extended liquidation wicks on the single Binance perp; fade the flush and mean-revert.
- [[cash-and-carry]] — capture spot-vs-perp basis using Binance spot ARPA/USDT against the USD-M perpetual when the basis is favorable.
- [[oi-confirmed-trend]] — use Binance open-interest confirmation to validate ARPA breakouts and avoid low-conviction, liquidity-driven fakeouts.
- [[rsi-mean-reversion]] — ARPA's range-bound, deeply-drawn-down price action suits mean-reversion off oversold/overbought extremes.

### Volatility & regime character

ARPA is a small-cap infrastructure/privacy token (secure MPC/threshold-BLS RNG) with high beta to BTC/ETH risk sentiment and pronounced reflexivity typical of low-float alts. Price is deep in drawdown from its 2021 cycle high and trades in a low-volatility grind punctuated by sharp, liquidity-driven spikes. Correlation to broad crypto risk-on/risk-off dominates idiosyncratic protocol news; expect thin-book amplification of moves during BTC-led volatility.

### Risk flags

- **Liquidity/venue concentration** — very low market cap and 24h volume, with Binance as the sole meaningful leveraged venue; slippage and gap risk are elevated.
- **Emissions/supply** — circulating supply is roughly half of a 2.0B max supply, leaving unlock/dilution overhang that can pressure price.
- **Narrative dependence** — value is tied to privacy/RNG infrastructure adoption (Randcast); demand is sensitive to shifts in narrative and broad alt sentiment.
- **Small-cap fragility** — reflexive liquidation dynamics on a single perp make leveraged positions vulnerable to cascade wicks.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ARPAUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=ARPAUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=ARPA` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=ARPA` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ARPAUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=ARPAUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=ARPA"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

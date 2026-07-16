---
title: "Gravity (by Galxe)"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["G"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://gravity.xyz/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[oi-confirmed-trend]]"]
---

# Gravity (by Galxe)

**Gravity (by Galxe)** (G) is a cryptocurrency. It ranks **#831** by market capitalization. About G, Galxe, and Gravity

G is the native utility token that powers both the Gravity blockchain and the broader Galxe ecosystem. It functions as the gas token for transactions, enables network security through staking, and plays a central role in governance, payments, and incentivized growth across platforms.

Galxe is web3’s leading growth platform, empowering millions of users and thousands of projects worldwide.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | G |
| **Market Cap Rank** | #831 |
| **Market Cap** | $19.56M |
| **Current Price** | $0.002705 |
| **Categories** | Smart Contract Platform, BNB Chain Ecosystem, Layer 1 (L1), Ethereum Ecosystem, Decentralized Identifier (DID), Zero Knowledge (ZK), Base Ecosystem, Gravity Alpha Ecosystem, CoinList Launchpad, Base Native |
| **Website** | [https://gravity.xyz/](https://gravity.xyz/) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Overview

About G, Galxe, and Gravity

G is the native utility token that powers both the Gravity blockchain and the broader Galxe ecosystem. It functions as the gas token for transactions, enables network security through staking, and plays a central role in governance, payments, and incentivized growth across platforms.

Galxe is web3’s leading growth platform, empowering millions of users and thousands of projects worldwide. It brings onboarding, identity verification, and engagement together in one seamless experience—built entirely on Gravity, Galxe’s high-performance Layer 1 blockchain.

Delivering speeds of 1 gigagas per second and subsecond finality, Gravity has served millions of users. Designed to solve web3’s toughest infrastructure challenges, Gravity enhances scalability, performance, security, and cross-chain interoperability.

To learn more visit:
https://gravity.xyz/
https://www.galxe.com/

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 7.23B G |
| **Total Supply** | 12.00B G |
| **Max Supply** | 12.00B G |
| **Fully Diluted Valuation** | $43.92M |
| **Market Cap / FDV Ratio** | 0.60 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0917 (2024-07-18) |
| **Current vs ATH** | -96.01% |
| **All-Time Low** | $0.00317090 (2026-03-08) |
| **Current vs ATL** | +15.36% |
| **24h Change** | -1.63% |
| **7d Change** | -3.16% |
| **30d Change** | +13.31% |
| **1y Change** | -69.13% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x9c7beba8f6ef6643abd725e45a4e8387ef260649` |
| Base | `0x9c7beba8f6ef6643abd725e45a4e8387ef260649` |
| Binance Smart Chain | `0x9c7beba8f6ef6643abd725e45a4e8387ef260649` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | G/USDT | N/A |
| Kraken | G/USD | N/A |
| Upbit | G/KRW | N/A |
| Bitget | G/USDT | N/A |
| KuCoin | G/USDT | N/A |
| Crypto.com Exchange | G/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X9C7BEBA8F6EF6643ABD725E45A4E8387EF260649/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://gravity.xyz/](https://gravity.xyz/) |
| **Twitter** | [@gravitychain](https://twitter.com/gravitychain) |
| **Telegram** | [gravitychain](https://t.me/gravitychain) (207,725 members) |
| **Whitepaper** | [https://docs.gravity.xyz/](https://docs.gravity.xyz/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.72M |
| **Market Cap Rank** | #831 |
| **24h Range** | $0.00363875 — $0.00375321 |
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

G is tradable on **Binance** — both spot (G/USDT) and a **USD-margined perpetual** contract exposing funding, open interest, and liquidation data. It is **not** listed on Hyperliquid, so Binance is the primary leveraged venue. As a small-cap token (rank ~716), on-venue depth is thin relative to majors: available leverage plus concentrated liquidity on a single perp venue means slippage and liquidation risk scale quickly with size, and funding/OI signals derive almost entirely from Binance flow. Size positions conservatively, work orders rather than crossing the book, and treat Binance funding/OI as the dominant read on positioning.

### Applicable strategies

- [[funding-rate-harvest]] — collect perp funding on the Binance USD-M contract when the rate is persistently one-sided, a common pattern for low-cap alts with skewed retail positioning.
- [[crowded-long-funding-fade]] — fade over-extended longs when Binance funding spikes positive on a thin-liquidity token like G that lacks fresh fundamental catalysts.
- [[liquidation-cascade-fade]] — a small-cap perp with limited depth is prone to sharp liquidation flushes; fade the wick once the cascade exhausts.
- [[oi-confirmed-trend]] — use Binance open-interest changes to confirm whether directional moves in G are backed by real positioning versus spot-only drift.
- [[breakout-and-retest]] — trade range breaks off G's compressed, low-cap price structure, entering on the retest to control slippage on a thin book.
- [[volatility-targeting]] — scale exposure inversely to G's realized volatility, essential given the outsized swings typical of a sub-$100M-cap token.

### Volatility & regime character

Small-cap (rank ~716) infra/L1 token tied to the Galxe/Gravity ecosystem. High beta to BTC/ETH risk sentiment with amplified drawdowns — the token sits ~96% below its all-time high and shows strong reflexivity to broad altcoin risk-on/risk-off swings. Price action is narrative- and liquidity-driven rather than deeply fundamentals-anchored, so regimes can flip abruptly between illiquid chop and momentum bursts.

### Risk flags

- **Liquidity/venue concentration** — leveraged exposure is concentrated on Binance; a single-venue outage, delisting, or depth shock materially affects execution.
- **Unlocks/emissions** — circulating supply (~7.2B) is well below max (12B), leaving meaningful future emission/unlock overhang that can pressure price.
- **Narrative dependence** — value is tethered to Galxe/Gravity adoption and broader L1/DID/ZK narratives; sentiment shifts drive disproportionate moves.
- **Small-cap fragility** — thin depth makes G vulnerable to slippage, stop-hunts, and liquidation cascades on modest flow.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=GUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=GUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=G` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=G` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=GUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=GUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=G"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

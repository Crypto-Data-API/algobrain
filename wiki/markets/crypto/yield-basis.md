---
title: "Yield Basis"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, defi, altcoins, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["YB"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://yieldbasis.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# Yield Basis

**Yield Basis** (YB) is a cryptocurrency. It ranks **#888** by market capitalization. YieldBasis enables users to provide BTC as liquidity in an AMM pool without impermanent loss (IL), while still earning trading fees.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | YB |
| **Market Cap Rank** | #888 |
| **Market Cap** | $17.24M |
| **Current Price** | $0.0739 |
| **Categories** | Decentralized Finance (DeFi), Binance Wallet IDO |
| **Website** | [https://yieldbasis.com/](https://yieldbasis.com/) |

---

## Overview

YieldBasis enables users to provide BTC as liquidity in an AMM pool without impermanent loss (IL), while still earning trading fees.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 233.23M YB |
| **Total Supply** | 742.51M YB |
| **Max Supply** | 1.00B YB |
| **Fully Diluted Valuation** | $54.89M |
| **Market Cap / FDV Ratio** | 0.31 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.8185 (2025-10-15) |
| **Current vs ATH** | -90.97% |
| **All-Time Low** | $0.0653 (2026-06-25) |
| **Current vs ATL** | +13.22% |
| **24h Change** | -2.48% |
| **7d Change** | +3.45% |
| **30d Change** | -19.04% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x01791f726b4103694969820be083196cc7c045ff` |
| Binance Smart Chain | `0xfb93ee8152dd0a0e6f4b49c66c06d800cf1db72d` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | YB/USDT | N/A |
| Kraken | YB/USD | N/A |
| Upbit | YB/BTC | N/A |
| Bitget | YB/USDT | N/A |
| KuCoin | YB/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X01791F726B4103694969820BE083196CC7C045FF/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://yieldbasis.com/](https://yieldbasis.com/) |
| **Twitter** | [@yieldbasis](https://twitter.com/yieldbasis) |
| **Telegram** | [yieldbasis](https://t.me/yieldbasis) (833 members) |
| **GitHub** | [https://github.com/yield-basis](https://github.com/yield-basis) |
| **Whitepaper** | [https://docs.yieldbasis.com/](https://docs.yieldbasis.com/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $8.17M |
| **Market Cap Rank** | #888 |
| **24h Range** | $0.0732 — $0.0769 |
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

YB is tradable on **Binance** — both **spot** (YB/USDT) and a **USD-margined perpetual** with published funding, open interest, and liquidations. It is **not listed on Hyperliquid**, so **Binance is the primary leveraged venue**. With YB a small-cap (rank ~884) carrying thin depth and a modest 24h volume, the single dominant perp venue means order books are shallow and slippage-prone: leverage and directional sizing should be conservative, execution scaled into limit tranches rather than market orders, and stops set wide enough to survive wick-driven liquidation flushes. Venue concentration also implies that Binance funding and OI are the reference signals for positioning — there is little cross-venue redundancy to hedge against a single-exchange outage or listing change.

### Applicable strategies

- [[funding-rate-harvest]] — thin single-venue YB perp funding can run persistently one-sided; harvesting it delta-neutral (spot long vs perp short on Binance) monetizes the skew without directional risk.
- [[cash-and-carry]] — pair Binance spot YB against the USD-M perp to capture basis/funding when the perp trades at a premium, a fit for a low-cap where carry can be rich.
- [[crowded-long-funding-fade]] — after DeFi/BTC-yield narrative pumps, YB longs crowd and funding spikes; fading the overheated long into mean reversion exploits the reflexive small-cap unwind.
- [[liquidation-cascade-fade]] — low liquidity makes YB prone to cascading forced liquidations that overshoot; fading exhaustion after a cascade targets the snap-back.
- [[oi-confirmed-trend]] — using Binance OI to confirm that a YB move is backed by real positioning (not a hollow wick) filters false breakouts on a thin book.
- [[rsi-mean-reversion]] — YB's wide, choppy small-cap range rewards fading statistical extremes back toward the mean between narrative catalysts.

### Volatility & regime character

Small-cap DeFi/infrastructure token (BTC-yield AMM protocol) with high beta to the broader alt and BTC/ETH complex. Price action is reflexive and headline-driven: sharp narrative-led rallies followed by deep drawdowns (down ~91% from its 2025 ATH). Expect elevated realized volatility, low baseline liquidity, and amplified moves during risk-on/risk-off rotations. As a BTC-collateral yield protocol its narrative correlates with BTC DeFi sentiment, but its thin float makes idiosyncratic, supply-driven swings common.

### Risk flags

- **Liquidity & venue concentration** — Binance is the sole meaningful leveraged venue; thin spot depth means high slippage and gap risk, and any listing or funding-regime change on Binance disproportionately impacts tradability.
- **Unlocks & emissions** — circulating supply (~233M) is well below total (~742M) and max (1.0B), with Market Cap / FDV near 0.31, implying substantial future dilution and potential supply-driven downside.
- **Narrative dependence** — valuation leans on the BTC-yield/impermanent-loss-free AMM story; fading interest or a mechanism failure can compress the token sharply.
- **Regulatory & smart-contract** — as a DeFi protocol token it carries smart-contract/protocol risk and evolving DeFi regulatory uncertainty.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=YBUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=YBUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=YB` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=YB` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=YBUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=YBUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=YB"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

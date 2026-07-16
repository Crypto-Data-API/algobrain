---
title: "Gitcoin"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["GTC"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://gitcoin.co/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# Gitcoin

**Gitcoin** (GTC) is a platform to fund builders looking for meaningful, open source work. It ranks **#1457** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | GTC |
| **Market Cap Rank** | #1457 |
| **Market Cap** | $5.96M |
| **Current Price** | $0.0682 |
| **Categories** | Governance |
| **Website** | [https://gitcoin.co/](https://gitcoin.co/) |

---

## Overview

Gitcoin is a platform to fund builders looking for meaningful, open source work.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 87.49M GTC |
| **Total Supply** | 100.00M GTC |
| **Max Supply** | 100.00M GTC |
| **Fully Diluted Valuation** | $6.82M |
| **Market Cap / FDV Ratio** | 0.87 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $22.37 (2021-11-27) |
| **Current vs ATH** | -99.69% |
| **All-Time Low** | $0.0644 (2026-06-30) |
| **Current vs ATL** | +6.22% |
| **24h Change** | -3.11% |
| **7d Change** | -1.70% |
| **30d Change** | -17.06% |
| **1y Change** | -77.15% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xde30da39c46104798bb5aa3fe8b9e0e1f348163f` |
| Near Protocol | `de30da39c46104798bb5aa3fe8b9e0e1f348163f.factory.bridge.near` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | GTC/USDT | N/A |
| Kraken | GTC/USD | N/A |
| Upbit | GTC/BTC | N/A |
| KuCoin | GTC/USDT | N/A |
| Crypto.com Exchange | GTC/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XDE30DA39C46104798BB5AA3FE8B9E0E1F348163F/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0XDE30DA39C46104798BB5AA3FE8B9E0E1F348163F/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Balancer V2 | 0XDE30DA39C46104798BB5AA3FE8B9E0E1F348163F/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://gitcoin.co/](https://gitcoin.co/) |
| **Twitter** | [@gitcoin](https://twitter.com/gitcoin) |
| **Reddit** | [https://www.reddit.com/r/gitcoincommunity](https://www.reddit.com/r/gitcoincommunity) |
| **Discord** | [https://discord.com/invite/gitcoin](https://discord.com/invite/gitcoin) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.80M |
| **Market Cap Rank** | #1457 |
| **24h Range** | $0.0675 — $0.0716 |
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

GTC is tradable on **Binance** with both **spot** (GTC/USDT) and a **USD-margined perpetual** contract carrying funding, open interest, and liquidation data. It is **NOT listed on Hyperliquid**, so Binance is the primary — effectively the only deep — leveraged venue for this name. Because GTC is a low-cap token (~#1455) with thin 24h volume, the perp order book is shallow: leverage should be kept modest, position sizing conservative, and entries/exits scaled with limit orders to avoid slippage. Venue concentration means funding, OI, and liquidation signals are dominated by Binance flow, and any Binance-specific listing/maintenance event can dislocate price with little arbitrage backstop elsewhere.

### Applicable strategies

- [[funding-rate-harvest]] — collect the perp funding premium/discount on the Binance GTC-USDT contract, sizing to the thin book to avoid moving the mark.
- [[crowded-long-funding-fade]] — fade over-extended long positioning when GTC funding spikes positive during low-cap pumps, a common pattern in illiquid governance tokens.
- [[liquidation-cascade-fade]] — low-cap perps like GTC see sharp liquidation flushes; fade the wick once the cascade exhausts and OI resets.
- [[cash-and-carry]] — capture basis between Binance spot GTC and the USD-M perp when funding runs persistently rich, hedging spot inventory against the short perp.
- [[oi-confirmed-trend]] — use Binance open-interest changes to confirm whether a GTC breakout is backed by real positioning versus a hollow spot move.
- [[breakout-and-retest]] — trade range breakouts on GTC's compressed low-cap chart, requiring a retest to filter the frequent false breaks in thin liquidity.

### Volatility & regime character

GTC is a small-cap Ethereum-based governance/DeFi-adjacent token with high realized volatility and strong high-beta behavior versus BTC/ETH — it tends to amplify broad-market moves on the way up and down while underperforming in risk-off regimes (see its steep multi-year drawdown from ATH). Price action is reflexive and narrative-sensitive: liquidity is thin enough that modest flows drive outsized swings, and rallies are typically driven by ecosystem/governance narratives or broad altcoin risk appetite rather than independent fundamentals. Correlation to ETH is elevated given its native chain and DeFi/infra positioning.

### Risk flags

- **Liquidity & venue concentration** — very low market cap and 24h volume; Binance is the dominant leveraged venue, so venue-specific risk (listing/delisting, maintenance) is concentrated with limited arbitrage backstop.
- **Supply/emissions** — circulating supply is a high share of max supply (Market Cap / FDV ~0.87), limiting dilution overhang, but governance-allocation movements can still add sell pressure.
- **Narrative dependence** — moves lean heavily on ecosystem/governance narratives and general altcoin sentiment rather than standalone demand, raising the risk of sharp reversals.
- **Slippage & liquidation risk** — thin perp depth makes large or highly-leveraged positions prone to cascade liquidations and adverse fills.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=GTCUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=GTCUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=GTC` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=GTC` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=GTCUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=GTCUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=GTC"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

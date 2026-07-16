---
title: "Convex Finance"
type: redirect
created: 2026-04-09
updated: 2026-07-16
status: good
aliases: ["CVX", "convex-finance"]
tags: [crypto, defi, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.convexfinance.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

See [[convex]].

(Merged: market-data snapshot — CVX price/supply, Ethereum contract address, ATH/ATL — into the canonical Convex page.)

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CVX |
| **Market Cap Rank** | #232 |
| **Market Cap** | $115.59M |
| **Current Price** | $1.26 |
| **Categories** | Decentralized Finance (DeFi), Yield Farming, Yield Aggregator, Metagovernance, Yield Optimizer, Governance |
| **Website** | [https://www.convexfinance.com/](https://www.convexfinance.com/) |

---

## Overview

Convex is a protocol that simplifies Curve boosting experience in order to maximize yields. Convex allows Curve liquidity providers to earn trading fees and claim boosted CRV without locking CRV themselves. Liquidity providers can receive boosted CRV and liquidity mining rewards with minimal effort.
If you would like to stake CRV, Convex lets users receive trading fees as well as a share of boosted CRV received by liquidity providers. This allows for a better balance between liquidity providers and CRV stakers as well as better capital efficiency.

Curve liquidity providers can deposit their LP tokens into Convex to maximize their CRV earnings with a more efficient boost.

Curve DAO token stakers will be able to earn additional boosted CRV and CVX tokens through the protocol.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 92.02M CVX |
| **Total Supply** | 99.98M CVX |
| **Max Supply** | 100.00M CVX |
| **Fully Diluted Valuation** | $125.59M |
| **Market Cap / FDV Ratio** | 0.92 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $60.09 (2022-01-01) |
| **Current vs ATH** | -97.91% |
| **All-Time Low** | $1.04 (2026-07-01) |
| **Current vs ATL** | +20.11% |
| **24h Change** | -4.77% |
| **7d Change** | +6.45% |
| **30d Change** | -10.06% |
| **1y Change** | -73.41% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x4e3fbd56cd56c3e72c1403e103b45db9da5b9d2b` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | CVX/USDT | N/A |
| Kraken | CVX/USD | N/A |
| KuCoin | CVX/USDT | N/A |
| Crypto.com Exchange | CVX/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X4E3FBD56CD56C3E72C1403E103B45DB9DA5B9D2B/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.convexfinance.com/](https://www.convexfinance.com/) |
| **Twitter** | [@convexfinance](https://twitter.com/convexfinance) |
| **Telegram** | [convexEthChat](https://t.me/convexEthChat) (1,050 members) |
| **Discord** | [https://discord.com/invite/WHwgFwRG6h](https://discord.com/invite/WHwgFwRG6h) |
| **GitHub** | [https://github.com/convex-eth/platform](https://github.com/convex-eth/platform) |
| **Whitepaper** | [https://docs.convexfinance.com/convexfinance/](https://docs.convexfinance.com/convexfinance/) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 186 |
| **GitHub Forks** | 98 |
| **Pull Requests Merged** | 1 |
| **Contributors** | 1 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.96M |
| **Market Cap Rank** | #232 |
| **24h Range** | $1.25 — $1.35 |
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

CVX is tradable on [[binance]] as both spot (CVX/USDT) and a USD-margined [[perpetual-futures|perpetual]] contract, exposing funding rates, open interest, and liquidation flow. It is NOT listed on Hyperliquid, so Binance is the primary — effectively the sole major — leveraged venue for CVX. This venue concentration means perp liquidity, order-book depth, and funding are dominated by a single exchange: leverage is available but sizing must respect thin depth relative to majors, and large orders should be worked (VWAP/limit) to avoid slippage. Cross-venue hedging options are limited, so basis and carry setups lean on the Binance spot-vs-perp pair rather than multi-exchange legs.

### Applicable strategies

- [[funding-rate-harvest]] — collect Binance perp funding on CVX when the perpetual trades at a persistent premium/discount to spot, delta-hedged against the CVX/USDT spot leg.
- [[cash-and-carry]] — long CVX spot on Binance versus short the USD-M perp to lock the basis when the perpetual carries positive funding.
- [[crypto-spot-perp-futures-triangle]] — exploit dislocations between CVX Binance spot and its USD-M perp within a single venue where the only tradable legs live.
- [[liquidation-cascade-fade]] — fade forced-liquidation wicks in a thin, single-venue perp book where cascades overshoot CVX's fair value.
- [[oi-confirmed-trend]] — use Binance open-interest expansion to confirm directional CVX moves and filter low-conviction breakouts.
- [[rsi-mean-reversion]] — trade CVX's range-bound, low-cap behavior back toward the mean from oversold/overbought extremes.

### Volatility & regime character

CVX is a small-cap (rank ~234) DeFi governance/infrastructure token tightly coupled to the Curve ecosystem and its metagovernance ("Curve wars") narrative. It carries high beta to BTC/ETH risk-on/risk-off swings with amplified downside typical of low-cap DeFi tokens; it is not a memecoin but exhibits narrative-driven reflexivity around Curve/CRV emissions and yield cycles. Extended drawdown regime relative to its cycle high, with volatility clustered around DeFi-yield and broader-market catalysts.

### Risk flags

- **Venue concentration** — Binance is the primary leveraged venue and dominant liquidity source; a single-exchange outage, delisting, or funding spike disproportionately affects tradability.
- **Thin liquidity** — modest market cap and volume mean wider spreads, slippage, and cascade-prone perp liquidations under stress.
- **Narrative dependence** — price is sensitive to Curve/CRV ecosystem health, metagovernance dynamics, and DeFi-yield sentiment rather than standalone fundamentals.
- **Emissions/supply** — token supply and emissions tied to protocol incentives can pressure price; monitor circulating-supply and reward-schedule changes.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=CVXUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=CVXUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=CVX` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=CVX` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=CVXUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=CVXUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=CVX"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

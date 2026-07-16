---
title: "Biconomy"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["BICO"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.biconomy.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# Biconomy

**Biconomy** (BICO) provides plug-n-play APIs to make web3.0 user-friendly &amp; frictionless. 

Biconomy is on a mission to make the decentralized web accessible to everyone. It ranks **#998** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BICO |
| **Market Cap Rank** | #998 |
| **Market Cap** | $13.73M |
| **Current Price** | $0.01908 |
| **Categories** | Infrastructure, Account Abstraction, CoinList Launchpad |
| **Website** | [https://www.biconomy.io/](https://www.biconomy.io/) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Overview

Biconomy provides plug-n-play APIs to make web3.0 user-friendly &amp; frictionless. 

Biconomy is on a mission to make the decentralized web accessible to everyone. We are the missing piece to crypto adoption for onboarding the next billion. Our APIs &amp; SDKs transform any dAapp to become usable for anyone regardless of their crypto knowledge and experience. Our multi-chain relayer infrastructure processes almost 50K daily transactions for 40+ DApps to ensure all the benefits of web3.0 come with the intuitiveness of web2.0.

Biconomy provides a simple &amp; quick way for Dapps to abstract away web3 complexities for their users.

With Biconomy, users get a simple multi-chain experience where they connect their wallet to any dApp, instantly access their funds on any chain or L2/rollup, and enjoy a completely gasless experience. We enable this superior experience though powerful features:

1) Free gasless transactions
2) Instant cross-chain transfers
3) Flexible options to pay gas
4) Assured successful transactions
5) Simple instant onboarding to scaling solutions
6) Automatically connect to any L2 &amp; EVM compatible chains
7) Cheap and instant cross-chain contract calls

The future of the internet is decentralized, and Biconomy is a critical infrastructure on which it will stand. We make web3.0 more usable, interoperable &amp; composable.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 726.38M BICO |
| **Total Supply** | 1.00B BICO |
| **Max Supply** | 1.00B BICO |
| **Fully Diluted Valuation** | $22.97M |
| **Market Cap / FDV Ratio** | 0.73 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $21.45 (2021-12-02) |
| **Current vs ATH** | -99.89% |
| **All-Time Low** | $0.0185 (2026-03-08) |
| **Current vs ATL** | +24.04% |
| **24h Change** | -4.23% |
| **7d Change** | +3.76% |
| **30d Change** | +15.15% |
| **1y Change** | -72.90% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xf17e65822b568b3903685a7c9f496cf7656cc6c2` |
| Arbitrum One | `0xa68ec98d7ca870cf1dd0b00ebbb7c4bf60a8e74d` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | BICO/USDT | N/A |
| Kraken | BICO/USD | N/A |
| Bitget | BICO/USDT | N/A |
| KuCoin | BICO/USDT | N/A |
| Crypto.com Exchange | BICO/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Sushiswap | 0XF17E65822B568B3903685A7C9F496CF7656CC6C2/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Balancer V2 | 0XF17E65822B568B3903685A7C9F496CF7656CC6C2/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.biconomy.io/](https://www.biconomy.io/) |
| **Twitter** | [@biconomy](https://twitter.com/biconomy) |
| **Telegram** | [biconomy](https://t.me/biconomy) (5 members) |
| **GitHub** | [https://github.com/bcnmy](https://github.com/bcnmy) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.40M |
| **Market Cap Rank** | #998 |
| **24h Range** | $0.0229 — $0.0244 |
| **CoinGecko Sentiment** | 0% positive |
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

BICO is tradable on Binance — spot (BICO/USDT) plus a USD-margined perpetual that exposes funding, open interest, and liquidation flow. It is NOT listed on Hyperliquid, so Binance is the primary leveraged venue and the reference for funding/OI signals. With a sub-$15M market cap and thin 24h volume, the perp order book is shallow: available leverage is capped tighter than for majors, spreads widen quickly, and even modest size can move price. This concentration means execution should lean on limit orders, staged entries, and small position sizing; cross-venue funding/basis arbitrage is constrained because Binance is effectively the only deep leveraged market, with the remaining CEX/DEX liquidity spot-only.

### Applicable strategies

- [[funding-rate-harvest]] — thin BICO perp funding can spike to extremes, letting a delta-neutral spot-vs-perp position collect the carry.
- [[crowded-long-funding-fade]] — narrative-driven pops in a micro-cap infra token often leave longs over-crowded and funding stretched, setting up a fade.
- [[liquidation-cascade-fade]] — a shallow book makes BICO prone to sharp liquidation wicks that overshoot and mean-revert, favoring fades of the cascade.
- [[rsi-mean-reversion]] — low-liquidity churn around a depressed price produces frequent oversold/overbought extremes suited to mean-reversion entries.
- [[breakout-and-retest]] — with price pinned near all-time lows, a volume-backed break of range highs and clean retest offers defined-risk momentum trades.
- [[token-unlock-supply-event]] — with a large gap between circulating and total supply, scheduled emissions/unlocks create tradable supply-driven pressure.

### Volatility & regime character

BICO is a small-cap infrastructure/account-abstraction token trading at a deep discount to its cycle high, so it behaves as a high-beta altcoin: it tends to lag on BTC/ETH strength and drop harder on risk-off moves. Price action is reflexive and thin-book driven, with outsized moves on low volume and strong dependence on the broader alt and account-abstraction/infra narrative rather than idiosyncratic fundamentals. Correlation to BTC/ETH is directional but amplified in drawdowns.

### Risk flags

- Liquidity and venue concentration: Binance dominates leveraged trading; a listing/parameter change there would sharply degrade tradability.
- Supply overhang: circulating supply is well below total/max supply, so emissions and unlocks can pressure price.
- Narrative dependence: performance hinges on infra/account-abstraction sentiment and general altcoin risk appetite, not standalone catalysts.
- Micro-cap fragility: low market cap and volume amplify slippage, gap risk, and susceptibility to liquidation-driven wicks.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BICOUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=BICOUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=BICO` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=BICO` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BICOUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BICOUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=BICO"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

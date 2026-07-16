---
title: "Badger"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, defi, hyperliquid, perpetual-futures, funding-rate, open-interest, altcoins]
aliases: ["BADGER"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://badger.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]"]
---

# Badger

**Badger** (BADGER) aims to create an ecosystem of DeFi products with the ultimate goal of bringing Bitcoin into Ethereum. It ranks **#1350** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BADGER |
| **Market Cap Rank** | #1350 |
| **Market Cap** | $7.00M |
| **Current Price** | $0.3512 |
| **Categories** | Decentralized Finance (DeFi), Yield Farming, Yield Aggregator, Governance |
| **Website** | [https://badger.com/](https://badger.com/) |

---

## Overview

Badger aims to create an ecosystem of DeFi products with the ultimate goal of bringing Bitcoin into Ethereum. It is the first DeFi project that chose to focus on BTC as the main reserve asset rather than using ETH.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 19.93M BADGER |
| **Total Supply** | 21.00M BADGER |
| **Max Supply** | 21.00M BADGER |
| **Fully Diluted Valuation** | $7.37M |
| **Market Cap / FDV Ratio** | 0.95 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $89.08 (2021-02-09) |
| **Current vs ATH** | -99.61% |
| **All-Time Low** | $0.3111 (2026-06-26) |
| **Current vs ATL** | +12.88% |
| **24h Change** | +0.65% |
| **7d Change** | +1.17% |
| **30d Change** | -5.12% |
| **1y Change** | -71.09% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x3472a5a71965499acd81997a54bba8d852c6e53d` |
| Fantom | `0x753fbc5800a8c8e3fb6dc6415810d627a387dfc9` |
| Xdai | `0xdfc20ae04ed70bd9c7d720f449eedae19f659d65` |
| Harmony Shard 0 | `0x06b19a0ce12dc71f1c7a6dd39e8983e089c40e0d` |
| Energi | `0x32e6842a6ea6a913687885ac856c2493b5b12f6f` |
| Arbitrum One | `0xbfa641051ba0a0ad1b0acf549a89536a0d76472e` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | BADGER/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X3472A5A71965499ACD81997A54BBA8D852C6E53D/0X2260FAC5E5542A773AA44FBCFEDF7C193BC2C599 | Spot |
| Uniswap V2 (Ethereum) | 0X3472A5A71965499ACD81997A54BBA8D852C6E53D/0X2260FAC5E5542A773AA44FBCFEDF7C193BC2C599 | Spot |
| Balancer V2 | 0X3472A5A71965499ACD81997A54BBA8D852C6E53D/0X2260FAC5E5542A773AA44FBCFEDF7C193BC2C599 | Spot |
| Sushiswap | 0X3472A5A71965499ACD81997A54BBA8D852C6E53D/0X2260FAC5E5542A773AA44FBCFEDF7C193BC2C599 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://badger.com/](https://badger.com/) |
| **Twitter** | [@badgerdao](https://twitter.com/badgerdao) |
| **Telegram** | [badger_dao](https://t.me/badger_dao) (3,210 members) |
| **Discord** | [https://discord.com/invite/badgerdao](https://discord.com/invite/badgerdao) |
| **GitHub** | [https://github.com/Badger-Finance](https://github.com/Badger-Finance) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.02M |
| **Market Cap Rank** | #1350 |
| **24h Range** | $0.3459 — $0.3607 |
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

BADGER is a **PERP-FIRST** asset: it trades as **BADGER-PERP on Hyperliquid** (up to ~40-50x leverage) but is **not listed on Binance**, and spot access is limited to a handful of offshore/DeFi venues (Kraken spot, plus Uniswap/Balancer/Sushiswap DEX pools). As a result, price discovery and directional flow concentrate on the Hyperliquid perp rather than on fragmented, thin spot books. Practical implications:

- **Depth is shallow.** With a small market cap and ~$1M daily spot turnover, the HL order book is thin; large orders move price, so size positions modestly and favor limit/passive fills over market orders.
- **Execution is venue-concentrated.** Because there is no deep CEX spot leg, cross-venue hedging is awkward and true cash-and-carry requires the offshore/DEX spot leg — factor borrow/withdrawal frictions into any carry structure.
- **High leverage amplifies risk.** 40-50x on a thin book means small moves can trigger liquidations; keep effective leverage well below the cap.

### Applicable strategies

- [[funding-rate-harvest]] — on a low-liquidity perp-first alt, funding can run persistently positive/negative; collect the carry while delta-hedging where a spot leg is feasible.
- [[crowded-long-funding-fade]] — thin OI and retail chasing on the HL perp can push funding to extremes; fade over-crowded longs when funding spikes.
- [[liquidation-cascade-fade]] — high leverage on a shallow book produces sharp liquidation wicks; fade the overshoot after forced-selling exhausts.
- [[post-liquidation-rebound]] — after a cascade flushes leveraged positions on BADGER-PERP, the snap-back is often outsized given how few resting bids exist.
- [[oi-price-exhaustion]] — with concentrated flow on one venue, rising OI into a stalling price is a clean exhaustion signal on this perp.
- [[range-mean-reversion]] — outside of narrative spikes BADGER tends to grind in ranges near cycle lows; fade the band edges with tight risk.

### Volatility & regime character

BADGER is a **small-cap DeFi / infrastructure token** (a BTC-in-DeFi / yield-aggregator governance token) trading at a deep drawdown from its ATH. It behaves as a **high-beta altcoin**: it is largely correlated to BTC/ETH risk-on/risk-off swings but with amplified moves, and it can decouple sharply on DeFi-sector narratives or protocol-specific news. Realized volatility is elevated and reflexive because thin liquidity magnifies both rallies and flushes.

### Risk flags

- **Liquidity & venue concentration** — flow is concentrated on a single perp venue (Hyperliquid); a listing/delisting or an HL outage would strand positions.
- **Thin spot / limited CEX access** — no Binance listing means weaker price discovery and harder hedging; slippage risk is high.
- **Narrative dependence** — as a DeFi-sector token far below ATH, price is sensitive to broad DeFi sentiment and protocol news.
- **Perp funding dislocations** — low OI can produce erratic, spiky funding on the HL perp; monitor before holding carry.
- **Emissions/governance** — capped near 21M supply with a high MC/FDV ratio limits dilution, but treasury/governance actions can still shift supply dynamics.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=BADGER` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=BADGER` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=BADGER&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=BADGER&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=BADGER"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

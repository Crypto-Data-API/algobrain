---
title: "Bluzelle"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, altcoins]
aliases: ["BLZ"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "https://bluzelle.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]"]
---

# Bluzelle

**Bluzelle** (BLZ) is a cryptocurrency. It ranks **#1828** by market capitalization. At Bluzelle, we see technology as a powerful tool to solve humanity's most pressing challenges. As creators of a robust decentralized blockchain ecosystem—including the Bluzelle Chain, BLZ token, and NFT marketplace Capella—we are uniquely positioned to revolutionize how science is conducted, funded, and shared.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BLZ |
| **Market Cap Rank** | #1828 |
| **Market Cap** | $3.35M |
| **Current Price** | $0.00708275 |
| **Genesis Date** | 2018-01-15 |
| **Categories** | Smart Contract Platform, DePIN, Decentralized Science (DeSci) |
| **Website** | [https://bluzelle.com/](https://bluzelle.com/) |

---

## Overview

At Bluzelle, we see technology as a powerful tool to solve humanity's most pressing challenges. As creators of a robust decentralized blockchain ecosystem—including the Bluzelle Chain, BLZ token, and NFT marketplace Capella—we are uniquely positioned to revolutionize how science is conducted, funded, and shared. Our DeSci (Decentralized Science) platform is designed to empower all scientific fields, fostering innovation across disciplines.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 472.62M BLZ |
| **Total Supply** | 500.00M BLZ |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $3.54M |
| **Market Cap / FDV Ratio** | 0.95 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.7831 (2018-02-10) |
| **Current vs ATH** | -99.10% |
| **All-Time Low** | $0.00654948 (2020-03-13) |
| **Current vs ATL** | +8.15% |
| **24h Change** | +0.58% |
| **7d Change** | -4.44% |
| **30d Change** | -15.22% |
| **1y Change** | -79.95% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x5732046a883704404f284ce41ffadd5b007fd668` |
| Osmosis | `ibc/63CDD51098FD99E04E5F5610A3882CBE7614C441607BA6FCD7F3A3C1CD5325F8` |
| Energi | `0x3fa2c976654a6ba6dcb1e532a4b1e31fd4dcd3b9` |
| Binance Smart Chain | `0x935a544bf5816e3a7c13db2efe3009ffda0acda2` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | BLZ/USD | N/A |
| KuCoin | BLZ/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X5732046A883704404F284CE41FFADD5B007FD668/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://bluzelle.com/](https://bluzelle.com/) |
| **Twitter** | [@BluzelleHQ](https://twitter.com/BluzelleHQ) |
| **Reddit** | [https://www.reddit.com/r/Bluzelle/](https://www.reddit.com/r/Bluzelle/) |
| **Telegram** | [bluzelle](https://t.me/bluzelle) (3,387 members) |
| **GitHub** | [https://github.com/njmurarka/bluzelle](https://github.com/njmurarka/bluzelle) |
| **Whitepaper** | [https://bluzelle.com/wp-content/uploads/2017/10/Bluzelle-White-Paper-v-1.2.pdf](https://bluzelle.com/wp-content/uploads/2017/10/Bluzelle-White-Paper-v-1.2.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $53,458.00 |
| **Market Cap Rank** | #1828 |
| **24h Range** | $0.00704211 — $0.00714297 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

**Venues & liquidity** — BLZ is a **PERP-FIRST** asset: it trades on **Hyperliquid** (BLZ-PERP, leverage up to ~40-50x) but is **NOT listed on Binance**, and spot access is limited/offshore (a handful of CEX pairs like Kraken and KuCoin plus thin Uniswap V2 liquidity). Consequently, price discovery and directional flow concentrate on the HL perp rather than spot. Order-book depth is shallow given the sub-$5M market cap and tiny reported 24h volume, so slippage rises quickly with size — position sizing must stay small, use limit/passive fills, and avoid market orders that can walk the book. The absence of a deep spot venue also makes true cash-and-carry hard to run cleanly; most edge is captured on-perp.

**Applicable strategies**
- [[funding-rate-harvest]] — thin, retail-driven perp funding on an illiquid micro-cap can run persistently rich or cheap, letting a delta-hedged holder collect the carry.
- [[crowded-long-funding-fade]] — sharp bursts of leveraged longs on a low-float name push funding to extremes that mean-revert, offering a fade against overheated positioning.
- [[liquidation-cascade-fade]] — with high leverage on a shallow book, forced liquidations overshoot violently; fading the flush targets the snap-back once stops clear.
- [[post-liquidation-rebound]] — after a cascade exhausts sell/buy pressure on the HL perp, the vacuum bounce is tradable given how few resting orders remain.
- [[oi-price-exhaustion]] — rising open interest into a stalling price on a micro-cap flags an exhausted, over-positioned move ripe for reversal.
- [[volatility-breakout]] — long dormant ranges punctuated by sudden expansion make ATR/volatility-triggered breakouts a fit for BLZ's reflexive, low-liquidity moves.

**Volatility & regime character** — BLZ is a deep-drawdown, low-float **infra/DeSci small-cap** (>99% below its 2018 ATH). It behaves as a **high-beta, low-liquidity altcoin**: quiet drift punctuated by reflexive spikes, amplified by thin depth and high perp leverage. Directionally it is a beta follower of BTC/ETH risk appetite — it tends to lag on the way up and overshoot on the way down — with little idiosyncratic catalyst flow, so realized volatility is driven more by leverage/liquidity mechanics than by fundamentals.

**Risk flags**
- **Venue concentration** — liquidity and leverage are centered on a single perp venue (Hyperliquid); an HL delist, funding dislocation, or downtime would strand exposure with no deep spot fallback.
- **Liquidity/slippage** — micro-cap depth means large fills move price and stops can gap; illiquidity is the dominant execution risk.
- **Supply/emissions** — max supply is uncapped ("Unlimited"), so ongoing emissions/dilution can pressure price independent of trading flow.
- **Narrative dependence** — value hinges on the DeSci/DePIN narrative; interest can evaporate quickly, leaving no bid.
- **Perp funding dislocations** — extreme or sign-flipping funding on a thin book can invert carry assumptions and squeeze hedged positions.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=BLZ` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=BLZ` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=BLZ&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=BLZ&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=BLZ"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

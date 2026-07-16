---
title: "Hamster Kombat"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, memecoins, altcoins]
aliases: ["HMSTR"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://hamsterkombat.io/"
related: ["[[crypto-markets]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]", "[[crowded-long-funding-fade]]"]
---

# Hamster Kombat

**Hamster Kombat** (HMSTR) is a crypto exchange CEO simulator game built on Telegram with 300 million players. It ranks **#1060** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | HMSTR |
| **Market Cap Rank** | #1060 |
| **Market Cap** | $12.07M |
| **Current Price** | $0.00018751 |
| **Categories** | Gaming (GameFi), Play To Earn, Telegram Apps, Tap to Earn, Arcade Games |
| **Website** | [https://hamsterkombat.io/](https://hamsterkombat.io/) |

---

## Overview

Hamster Kombat is a crypto exchange CEO simulator game built on Telegram with 300 million players. Its mission is to smoothly onboard 1,000,000,000 Web2 users into Web3.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 64.38B HMSTR |
| **Total Supply** | 100.00B HMSTR |
| **Max Supply** | 100.00B HMSTR |
| **Fully Diluted Valuation** | $18.75M |
| **Market Cap / FDV Ratio** | 0.64 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.00722201 (2024-09-27) |
| **Current vs ATH** | -97.40% |
| **All-Time Low** | $0.00012639 (2026-06-04) |
| **Current vs ATL** | +48.28% |
| **24h Change** | -3.02% |
| **7d Change** | -5.24% |
| **30d Change** | +10.49% |
| **1y Change** | -75.83% |

---

## Platform & Chain Information

**Native Chain:** The Open Network

### Contract Addresses

| Chain | Address |
|---|---|
| The Open Network | `EQAJ8uWd7EBqsmpSWaRdf_I-8R8-XHwh3gsNKhy-UrdrPcUo` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | HMSTR/USDT | N/A |
| Kraken | HMSTR/USD | N/A |
| Bitget | HMSTR/USDT | N/A |
| KuCoin | HMSTR/USDT | N/A |
| Crypto.com Exchange | HMSTR/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://hamsterkombat.io/](https://hamsterkombat.io/) |
| **Twitter** | [@hamster_kombat](https://twitter.com/hamster_kombat) |
| **Telegram** | [hamster_kombat](https://t.me/hamster_kombat) (23.06M members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $10.95M |
| **Market Cap Rank** | #1060 |
| **24h Range** | $0.00018389 — $0.00019470 |
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

HMSTR trades on **both** major venue types, giving it a deep, liquid two-venue market:

- **Binance** — spot (HMSTR/USDT) plus a USD-margined perpetual, providing the primary price-discovery and reference-funding venue with the deepest CEX order-book depth.
- **Hyperliquid** — the **HMSTR-PERP** contract with leverage up to roughly **40-50x**, offering on-chain perp exposure and a transparent funding/OI feed.

The parallel CEX + DEX availability means the same directional or funding view can be expressed on either venue, and the two order books can be cross-referenced. Because HMSTR is a low-priced (sub-cent), small-cap memecoin, book depth is thinner than large-caps, so size execution should be staged and slippage-aware even though top-of-book liquidity is generally serviceable. Two-venue availability supports basis and funding-divergence structures (spot/perp and CEX-vs-DEX), while sizing should stay modest relative to visible depth to avoid moving a shallow book.

### Applicable strategies

- [[crowded-long-funding-fade]] — memecoin rallies in HMSTR routinely produce crowded, over-leveraged long positioning; fading richly positive funding captures the mean-reversion when late longs get squeezed.
- [[liquidation-cascade-fade]] — thin depth on a sub-cent memecoin makes HMSTR prone to sharp liquidation-driven wicks; fading the flush after forced selling exhausts is a repeatable setup.
- [[funding-rate-arbitrage]] — with a Binance USD-margined perp and Hyperliquid HMSTR-PERP quoting independent funding, funding differentials between the two venues can be harvested market-neutral.
- [[hl-vs-cex-funding-divergence]] — Hyperliquid funding on HMSTR-PERP frequently diverges from Binance's, so trading the spread between the two perps is a direct expression of that dislocation.
- [[cash-and-carry]] — Binance spot plus perp lets a long-spot / short-perp carry structure monetize persistently positive funding on this high-beta memecoin.
- [[narrative-trading]] — HMSTR price action is highly reflexive to GameFi/Tap-to-Earn and Telegram-ecosystem narrative flow, making narrative-driven entries and exits well suited to the token.

### Volatility & regime character

HMSTR is a **high-beta GameFi memecoin** with strong reflexivity: moves are amplified by leverage, social/narrative sentiment, and thin depth rather than fundamentals. It trades as a high-beta altcoin, tending to over-react to broad BTC/ETH risk swings — rallying harder in risk-on regimes and selling off faster in risk-off drawdowns — so realized volatility clusters and regime shifts are pronounced. Its low absolute price and large token supply add to the memecoin reflexivity profile.

### Risk flags

- **Liquidity / small-cap concentration** — a ~#1053 market-cap memecoin with thin book depth; large orders can slip badly and gaps are common.
- **Emissions / supply overhang** — circulating supply is a fraction of a 100B max supply, so ongoing unlocks/emissions are a persistent dilution and supply-pressure risk.
- **Narrative dependence** — valuation is tied to GameFi/Tap-to-Earn and Telegram-ecosystem attention; fading interest can drive sustained decline independent of the broad market.
- **Perp funding dislocations** — leverage-driven crowding can push funding to extremes and trigger liquidation cascades, which is both an opportunity and a tail risk for directional exposure.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=HMSTR` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=HMSTR` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=HMSTR&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=HMSTR&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=HMSTR"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

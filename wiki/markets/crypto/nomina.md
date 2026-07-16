---
title: "Nomina"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, defi, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["NOM"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.nomina.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Nomina

**Nomina** (NOM) is $NOM is the primary network token of the Nomina, a unified trading platform built to execute complex trading strategies across DEXs. It ranks **#900** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NOM |
| **Market Cap Rank** | #900 |
| **Market Cap** | $16.94M |
| **Current Price** | $0.00582226 |
| **Categories** | Smart Contract Platform, Decentralized Finance (DeFi), Perpetuals, Ethereum Ecosystem |
| **Website** | [https://www.nomina.io/](https://www.nomina.io/) |

---

## Overview

$NOM is the primary network token of the Nomina, a unified trading platform built to execute complex trading strategies across DEXs.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.90B NOM |
| **Total Supply** | 7.27B NOM |
| **Max Supply** | 7.50B NOM |
| **Fully Diluted Valuation** | $42.49M |
| **Market Cap / FDV Ratio** | 0.40 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0454 (2025-10-01) |
| **Current vs ATH** | -87.06% |
| **All-Time Low** | $0.00173954 (2026-03-27) |
| **Current vs ATL** | +237.98% |
| **24h Change** | -10.45% |
| **7d Change** | -1.10% |
| **30d Change** | +72.39% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x6e6f6d696e61decd6605bd4a57836c5db6923340` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | NOM/USDT | N/A |
| Bitget | NOM/USDT | N/A |
| Crypto.com Exchange | NOM/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.nomina.io/](https://www.nomina.io/) |
| **Twitter** | [@nomina](https://twitter.com/nomina) |
| **Telegram** | [nominaannouncements](https://t.me/nominaannouncements) (615 members) |
| **Discord** | [https://discord.com/invite/nomina](https://discord.com/invite/nomina) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $59.32M |
| **Market Cap Rank** | #900 |
| **24h Range** | $0.00582422 — $0.00769704 |
| **CoinGecko Sentiment** | 100% positive |
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

NOM is tradable on **Binance** — both **spot** (NOM/USDT) and a **USD-margined perpetual** with the full derivatives stack (funding, open interest, liquidations). It is **NOT listed on Hyperliquid**, so Binance is the primary leveraged venue. As a small-cap (rank ~1641), the perp order book is thin relative to majors: leverage amplifies slippage on entries/exits, funding can swing hard when positioning gets one-sided, and forced liquidations move price disproportionately. Because leveraged flow concentrates on a single venue, execution should lean on Binance spot and perp liquidity, size positions to the realistic depth (not headline volume), and avoid market orders during low-liquidity windows. Cross-venue basis is available against Bitget/Crypto.com spot but only Binance offers a deep perp for hedging.

### Applicable strategies

- [[funding-rate-harvest]] — collect funding on the Binance NOM perp when a persistent long or short bias skews the rate; the single-venue perp makes the carry clean to isolate.
- [[crowded-long-funding-fade]] — after a +72% 30d run, over-leveraged longs paying rich funding set up fade entries when the perp gets stretched.
- [[liquidation-cascade-fade]] — thin small-cap depth means liquidation clusters overshoot; fade the wick once the cascade exhausts on Binance liquidations.
- [[oi-confirmed-trend]] — use Binance open-interest expansion to confirm genuine trend legs versus low-conviction spot-only moves in a low-cap DeFi token.
- [[volatility-breakout]] — NOM's high realized volatility and wide daily ranges favor breakout entries out of consolidation with volatility-scaled sizing.
- [[cash-and-carry]] — hedge Binance spot against the USD-M perp to harvest basis when the perp trades at a premium, sidestepping directional small-cap risk.

### Volatility & regime character

NOM is a **small-cap DeFi/perp-DEX infrastructure token** with high reflexive volatility — an ATH drawdown near -87% alongside a +72% 30d bounce shows sharp, sentiment-driven swings. It carries high beta to BTC/ETH risk-on/risk-off cycles and, being an Ethereum-ecosystem DeFi asset, tends to amplify broader altcoin and DeFi-narrative rotations. Liquidity is venue-concentrated, so regime shifts (funding flips, OI unwinds) can be abrupt.

### Risk flags

- **Liquidity/venue concentration** — leveraged trading depends on Binance; a delisting or depth reduction would sharply raise slippage and gap risk.
- **Unlocks/emissions** — circulating supply (~2.90B) is well below max (~7.50B) with MC/FDV ~0.40, so future emissions/unlocks are a persistent supply overhang.
- **Narrative dependence** — value is tied to DeFi/perp-DEX narrative momentum; sentiment reversals hit small-caps first and hardest.
- **Small-cap manipulation risk** — thin books make the perp susceptible to stop-hunts, funding spikes, and liquidation-driven wicks.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=NOMUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=NOMUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=NOM` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=NOM` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=NOMUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=NOMUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=NOM"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

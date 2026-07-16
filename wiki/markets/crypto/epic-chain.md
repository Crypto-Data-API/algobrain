---
title: "Epic Chain"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["EPIC"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.epicchain.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[narrative-trading]]", "[[liquidation-cascade-fade]]"]
---

# Epic Chain

**Epic Chain** (EPIC) is a cryptocurrency. It ranks **#962** by market capitalization. Epic is the travel layer for crypto, giving crypto holders access to hotels and flights at up to 30% discount vs Booking.com.

Inventory is sourced directly from over 100 wholesale travel suppliers, providing access to pricing that has historically been unavailable to retail consumers. The platform covers 2M+ hotels worldwide including Marriott, Aman, and Hilton properties, alongside flights across 180 countries.

Every booking earns up to 8% cashback paid in XRP.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | EPIC |
| **Market Cap Rank** | #962 |
| **Market Cap** | $14.77M |
| **Current Price** | $0.4399 |
| **Categories** | Tourism, Real World Assets (RWA), Payment Solutions, RWA Protocol |
| **Website** | [https://www.epicchain.io/](https://www.epicchain.io/) |

---

## Overview

Epic is the travel layer for crypto, giving crypto holders access to hotels and flights at up to 30% discount vs Booking.com.

Inventory is sourced directly from over 100 wholesale travel suppliers, providing access to pricing that has historically been unavailable to retail consumers. The platform covers 2M+ hotels worldwide including Marriott, Aman, and Hilton properties, alongside flights across 180 countries.

Every booking earns up to 8% cashback paid in XRP. All major cryptocurrencies are accepted alongside traditional payment methods including Visa, Mastercard, and Apple Pay.

EPIC holders with $10,000 or more access Epic Concierge, a dedicated travel service providing end-to-end trip planning and further discounted rates, at no additional cost.

Epic was founded as Ethernity, having advised the United States Space Force, Lionel Messi, Shaquille O'Neal, and Toys R Us on digital asset distribution at scale. The company has raised more than $20 million and is backed by Ripple, Algorand, Polygon, Chainlink, CEFFU, and BRINKS.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 33.60M EPIC |
| **Total Supply** | 33.60M EPIC |
| **Max Supply** | 33.60M EPIC |
| **Fully Diluted Valuation** | $14.77M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.20 (2025-08-20) |
| **Current vs ATH** | -86.20% |
| **All-Time Low** | $0.1922 (2026-05-29) |
| **Current vs ATL** | +129.60% |
| **24h Change** | +5.70% |
| **7d Change** | +40.07% |
| **30d Change** | -30.47% |
| **1y Change** | -55.14% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x94314a14df63779c99c0764a30e0cd22fa78fc0e` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | EPIC/USDT | N/A |
| KuCoin | EPIC/USDT | N/A |
| Crypto.com Exchange | EPIC/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.epicchain.io/](https://www.epicchain.io/) |
| **Twitter** | [@EpicOnChain](https://twitter.com/EpicOnChain) |
| **Reddit** | [https://www.reddit.com/r/EPIC_Travel/](https://www.reddit.com/r/EPIC_Travel/) |
| **Telegram** | [epiconchain](https://t.me/epiconchain) (15,637 members) |
| **GitHub** | [https://github.com/epiconchain](https://github.com/epiconchain) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $15.31M |
| **Market Cap Rank** | #962 |
| **24h Range** | $0.4129 — $0.4550 |
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

EPIC is tradable on **Binance** — both **spot** (EPIC/USDT) and a **USD-margined perpetual** carrying funding, open interest, and liquidation data. It is **NOT listed on Hyperliquid**, so Binance is the primary (effectively sole major) leveraged venue. This concentration means perp funding, OI, and liquidation flows all originate from one book, so the derivatives signal is clean but fragile — a single venue outage, delisting, or margin-tier change can dislocate the entire leveraged market. With a small-cap ~$15M market cap and thin depth, size positions conservatively: available leverage may be attractive but slippage on entry/exit and forced-liquidation air-pockets are the dominant execution risks. Cross-venue arbitrage is limited because spot lives across a handful of CEXs (Binance, KuCoin, Crypto.com) while the perp is Binance-only.

### Applicable strategies

- [[funding-rate-harvest]] — single-venue Binance perp funding on a low-float name can run persistently rich or negative; harvest the carry while delta-hedging against Binance spot.
- [[liquidation-cascade-fade]] — thin EPIC order books make stop-runs and forced-liquidation wicks violent and mean-reverting; fade the flush once the cascade exhausts.
- [[narrative-trading]] — EPIC is an RWA/travel-payments narrative token (XRP cashback, Ripple/Algorand backing); position around narrative rotation rather than fundamentals.
- [[oi-price-exhaustion]] — with all OI concentrated on Binance, rising open interest into a stalling price flags an exhausted, crowded position ripe for reversal.
- [[breakout-and-retest]] — post-ATH downtrend leaves clear range boundaries; trade confirmed breaks with a retest to avoid low-liquidity fakeouts.
- [[volatility-targeting]] — high, uneven realized volatility on a micro-cap demands size scaled inversely to ATR to keep risk-per-trade stable.

### Volatility & regime character

Small-cap altcoin (rank ~966, ~$15M cap) with high reflexive volatility and low float (33.6M supply, MC/FDV = 1.00, so no dilution overhang). Price is roughly 86% below its 2025 ATH and driven more by RWA/travel narrative flows and thin-book reflexivity than by BTC/ETH beta, though it still tends to amplify broad-market risk-on/risk-off moves. Expect sharp, sentiment-led swings and elevated funding-rate variance rather than steady trend.

### Risk flags

- **Venue concentration:** leveraged exposure is Binance-only; a delisting or margin-tier change could dislocate the perp with no alternative venue.
- **Liquidity:** micro-cap with thin depth — wide spreads, high slippage, and liquidation air-pockets on size.
- **Narrative dependence:** valuation hinges on RWA/travel adoption and XRP-cashback narrative; momentum can evaporate quickly if the story stalls.
- **Supply/utility risk:** full float already circulating removes unlock overhang but also means no future demand catalyst from vesting cliffs; RWA/payments tokens carry latent regulatory sensitivity.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=EPICUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=EPICUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=EPIC` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=EPIC` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=EPICUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=EPICUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=EPIC"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

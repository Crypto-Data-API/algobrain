---
title: "FC Porto"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, altcoins]
aliases: ["PORTO"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.fcporto.pt/pt"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]", "[[narrative-trading]]", "[[breakout-trading]]"]
---

# FC Porto

**FC Porto** (PORTO) is a cryptocurrency. It ranks **#1498** by market capitalization. Fan Token is built on the Binance Smart Chain empowering FC Porto fans with broader accessibility, more functionalities and lower fees.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PORTO |
| **Market Cap Rank** | #1498 |
| **Market Cap** | $5.54M |
| **Current Price** | $0.4889 |
| **Categories** | Sports, Fan Token, Binance Launchpad |
| **Website** | [https://www.fcporto.pt/pt](https://www.fcporto.pt/pt) |

---

## Overview

FC Porto Fan Token is built on the Binance Smart Chain empowering FC Porto fans with broader accessibility, more functionalities and lower fees.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 11.33M PORTO |
| **Total Supply** | 40.00M PORTO |
| **Max Supply** | 40.00M PORTO |
| **Fully Diluted Valuation** | $19.56M |
| **Market Cap / FDV Ratio** | 0.28 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $14.64 (2021-11-16) |
| **Current vs ATH** | -96.64% |
| **All-Time Low** | $0.3850 (2026-07-13) |
| **Current vs ATL** | +27.74% |
| **24h Change** | -11.89% |
| **7d Change** | +17.48% |
| **30d Change** | -12.19% |
| **1y Change** | -42.97% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0x49f2145d6366099e13b10fbf80646c0f377ee7f6` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | PORTO/TRY | N/A |
| Bitget | PORTO/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.fcporto.pt/pt](https://www.fcporto.pt/pt) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $11.52M |
| **Market Cap Rank** | #1498 |
| **24h Range** | $0.4649 — $0.5975 |
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

PORTO is tradable on Binance SPOT only — there is no liquid perpetual venue, so leverage and short access are limited and this is a spot-primary asset. Perp funding, basis, and liquidation strategies do NOT apply. As a low-cap fan token (rank ~1492) concentrated on a single centralized venue, order books are thin relative to majors: expect wider spreads and slippage on larger clips, so size positions modestly and prefer limit/VWAP-style execution over aggressive market orders. Venue concentration also means any Binance listing/pair change or maintenance directly gates all liquidity.

### Applicable strategies

- [[narrative-trading]] — PORTO is a football fan token; price responds to FC Porto match results, sponsorship, and fan-engagement narratives more than fundamentals.
- [[event-driven-trading]] — discrete catalysts (fixtures, cup runs, transfers, club announcements) drive reflexive spot moves worth positioning around.
- [[breakout-trading]] — thin low-cap books produce sharp, clean breakouts from consolidation on catalyst-driven volume spikes.
- [[range-trading]] — outside catalyst windows PORTO tends to chop within a spot range, favoring buy-low/sell-high mean-reversion around support/resistance.
- [[dca-strategy]] — for spot-only accumulation, averaging in smooths the high single-venue volatility without needing leverage.
- [[atr-trailing-stop]] — volatility-scaled trailing stops help lock gains and cap downside on erratic, catalyst-prone spot swings.

### Volatility & regime character

Small-cap, high-beta fan token with pronounced reflexivity around sports events rather than DeFi/infra fundamentals. Built on BNB Smart Chain, it broadly tracks BTC/ETH risk regimes but is dominated by idiosyncratic, sentiment-driven spikes and rapid mean-reversion. Liquidity and volatility cluster tightly around match days and club news; between catalysts it can drift and decay.

### Risk flags

- Liquidity/venue concentration: spot liquidity is concentrated on Binance, creating single-venue dependence and slippage risk.
- Narrative dependence: value is tethered to FC Porto sporting performance and fan sentiment, which can fade quickly.
- Supply/emissions: circulating supply is a fraction of max supply (MC/FDV ~0.28), leaving overhang from future unlocks/issuance.
- No perp/leverage venue: hedging and shorting are constrained; risk must be managed via spot sizing and stops.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=PORTOUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=PORTOUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=PORTOUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=PORTOUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

---
title: "Sleepless AI"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, altcoins, ai-trading]
aliases: ["AI"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.sleeplessai.net/home"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]", "[[narrative-trading]]", "[[breakout-trading]]"]
---

# Sleepless AI

**Sleepless AI** (AI) is a Artificial Intelligence (AI), BNB Chain Ecosystem, Binance Launchpool, YZi Labs (Prev. Binance Labs) Portfolio project. It ranks **#1982** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | AI |
| **Market Cap Rank** | #1982 |
| **Market Cap** | $2.75M |
| **Current Price** | $0.0212 |
| **Categories** | Artificial Intelligence (AI), Binance Launchpool |
| **Website** | [https://www.sleeplessai.net/home](https://www.sleeplessai.net/home) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 130.00M AI |
| **Total Supply** | 1.00B AI |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $21.17M |
| **Market Cap / FDV Ratio** | 0.13 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2.34 (2024-03-09) |
| **Current vs ATH** | -99.11% |
| **All-Time Low** | $0.0170 (2026-04-28) |
| **Current vs ATL** | +22.63% |
| **24h Change** | +3.50% |
| **7d Change** | +2.44% |
| **30d Change** | -4.83% |
| **1y Change** | -86.11% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xbda011d7f8ec00f66c1923b049b94c67d148d8b2` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | AI/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.sleeplessai.net/home](https://www.sleeplessai.net/home) |
| **Twitter** | [@SleeplessAI_Lab](https://twitter.com/SleeplessAI_Lab) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $5.12M |
| **Market Cap Rank** | #1982 |
| **24h Range** | $0.0202 — $0.0213 |
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

Sleepless AI (AI) trades primarily on **Binance spot** (AI/USDT), with occasional listings on other CEX spot venues. As a small-cap (rank ~#1982) with a modest 24h volume, its order books are **thin**, so market orders and larger positions can incur meaningful **slippage**. There is **no deep native perpetual venue**, so leverage and short access are effectively limited to spot; strategies relying on borrowing/shorting the token are constrained. Size positions conservatively, prefer limit orders, and expect wider effective spreads during low-liquidity hours.

### Applicable strategies

- [[narrative-trading]] — price is heavily driven by the AI/gaming (SleeplessAI) narrative; rotations in AI-token sentiment move this coin sharply.
- [[breakout-trading]] — thin books mean range breakouts on volume can extend quickly; useful for catching narrative-driven expansions.
- [[breakout-and-retest]] — after a breakout, waiting for a retest of the broken level improves entry quality given the erratic small-cap follow-through.
- [[momentum-rotation]] — AI treats well as a high-beta leg to rotate into when the AI/gaming sector leads, and out of when it lags.
- [[range-trading]] — outside catalyst windows AI often chops in a defined band (e.g. near recent lows), making mean-band entries/exits viable.
- [[event-driven-trading]] — Binance Launchpool origin and listing/announcement flow create discrete catalysts to trade around.

*Note: perp funding/basis/carry strategies do NOT reliably apply — there is no liquid native perpetual market for AI.*

### Volatility & regime character

Small-cap, **high-beta** token whose regime is dominated by the **AI/gaming narrative** and **Binance-listing/flow** dynamics. It exhibits large percentage swings on low notional volume, deep drawdowns from its all-time high, and long directionless stretches punctuated by sharp narrative- or catalyst-driven moves. Behaves more like a sentiment/flow instrument than a fundamentals-anchored asset.

### Risk flags

- **Thin liquidity** — shallow order books; slippage and gap risk on size.
- **Small-cap drawdown risk** — history of severe multi-order-of-magnitude declines from highs.
- **Unlock / emissions** — large gap between circulating and total supply (low MC/FDV ratio) implies ongoing dilution/unlock pressure.
- **Narrative dependence** — performance is tethered to AI/gaming sentiment cycles that can reverse abruptly.
- **Spot-only shorting constraints** — no liquid perp venue, so hedging and downside expression are limited.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=AIUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=AIUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=AIUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=AIUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

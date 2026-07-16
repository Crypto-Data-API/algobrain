---
title: "CZ's Dog"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, memecoins, altcoins]
aliases: ["BROCCOLI"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.broccoli714.site/"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]", "[[meme-coin-cycle]]", "[[narrative-trading]]"]
---

# CZ's Dog

**CZ's Dog** (BROCCOLI) is a BNB Chain Ecosystem, Meme, Dog-Themed, Binance Alpha Spotlight, Four.meme Ecosystem (BNB Memes) project. It ranks **#1076** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BROCCOLI |
| **Market Cap Rank** | #1076 |
| **Market Cap** | $11.72M |
| **Current Price** | $0.0121 |
| **Categories** | Meme, Dog-Themed, Binance Alpha Spotlight |
| **Website** | [https://www.broccoli714.site/](https://www.broccoli714.site/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 967.13M BROCCOLI |
| **Total Supply** | 967.13M BROCCOLI |
| **Max Supply** | 1.00B BROCCOLI |
| **Fully Diluted Valuation** | $11.72M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2580 (2025-02-14) |
| **Current vs ATH** | -95.29% |
| **All-Time Low** | $0.0103 (2026-06-06) |
| **Current vs ATL** | +18.43% |
| **24h Change** | -2.34% |
| **7d Change** | -2.24% |
| **30d Change** | -8.93% |
| **1y Change** | -75.92% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0x6d5ad1592ed9d6d1df9b93c793ab759573ed6714` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | BROCCOLI714/USDT | N/A |
| Bitget | BROCCOLI/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.broccoli714.site/](https://www.broccoli714.site/) |
| **Twitter** | [@broccoli714bnb](https://twitter.com/broccoli714bnb) |
| **Telegram** | [BROCCOLI714_CTO](https://t.me/BROCCOLI714_CTO) (82 members) |
| **GitHub** | [https://github.com/Broccoli-CTO/BroccoliNGO-Dapp](https://github.com/Broccoli-CTO/BroccoliNGO-Dapp) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $7.41M |
| **Market Cap Rank** | #1076 |
| **24h Range** | $0.0120 — $0.0126 |
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

Tradable on Binance SPOT only — no liquid perpetual venue, so leverage/short access is limited and this is a spot-primary asset. Perp funding/basis/liquidation strategies do NOT apply. With a single primary CEX venue (Binance spot, plus secondary Bitget spot) and a small-cap footprint, order-book depth is thin: size positions conservatively, expect slippage on market orders, and prefer limit/VWAP-style execution. Absence of a deep perp market means shorting and leverage are effectively unavailable, so the tradeable expression is long-only spot with cash-managed sizing.

### Applicable strategies

- [[meme-coin-cycle]] — BROCCOLI is a BNB-chain dog-themed memecoin whose price is driven by hype/attention cycles rather than fundamentals.
- [[narrative-trading]] — moves track BNB-ecosystem and CZ/Binance-Alpha narratives; trade the story, not a valuation.
- [[breakout-trading]] — thin small-cap tape can gap on attention spikes; range breakouts capture the impulsive expansion phases.
- [[dca-strategy]] — for long-only spot accumulation, averaging in smooths the extreme drawdowns typical of a coin ~95% off its ATH.
- [[atr-trailing-stop]] — high realized volatility makes a volatility-scaled trailing stop essential for protecting long spot exposure.
- [[range-mean-reversion]] — during quiet regimes the coin oscillates in a tight band, favoring fade-the-extremes entries on spot.

### Volatility & regime character

Small-cap memecoin (rank ~1075) with high reflexive volatility: sharp attention-driven pumps and steep decays. Beta to BTC/ETH is present but secondary to memecoin/BNB-ecosystem sentiment; correlation rises in broad risk-off flushes and decouples during idiosyncratic hype. Regime alternates between low-liquidity chop and violent momentum bursts.

### Risk flags

- Venue/liquidity concentration: Binance spot is the primary venue; thin depth amplifies slippage and gap risk.
- Narrative dependence: value hinges on meme/ecosystem attention, which can evaporate abruptly.
- No hedging venue: absence of a liquid perp limits shorting/hedging — downside is managed only via sizing and stops.
- Small-cap fragility: coin trades ~95% below ATH; recovery is speculative and drawdowns can be severe.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BROCCOLIUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=BROCCOLIUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BROCCOLIUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BROCCOLIUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

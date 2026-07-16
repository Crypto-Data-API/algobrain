---
title: "Juventus Fan Token"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, altcoins]
aliases: ["JUV"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.socios.com/juventus/"
related: ["[[crypto-markets]]", "[[binance]]", "[[momentum-investing]]", "[[breakout-trading]]", "[[event-driven-trading]]"]
---

# Juventus Fan Token

**Juventus Fan Token** (JUV) is a Sports, Binance Launchpool, Fan Token, Solana Ecosystem, Base Ecosystem, Chiliz Ecosystem, YZi Labs (Prev. Binance Labs) Portfolio project. It ranks **#1520** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | JUV |
| **Market Cap Rank** | #1520 |
| **Market Cap** | $5.29M |
| **Current Price** | $0.3354 |
| **Categories** | Sports, Binance Launchpool, Fan Token |
| **Website** | [https://www.socios.com/juventus/](https://www.socios.com/juventus/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 15.75M JUV |
| **Total Supply** | 19.96M JUV |
| **Max Supply** | 19.96M JUV |
| **Fully Diluted Valuation** | $6.70M |
| **Market Cap / FDV Ratio** | 0.79 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $37.83 (2020-12-21) |
| **Current vs ATH** | -99.11% |
| **All-Time Low** | $0.3076 (2026-07-08) |
| **Current vs ATL** | +9.97% |
| **24h Change** | +2.26% |
| **7d Change** | +6.94% |
| **30d Change** | -5.61% |
| **1y Change** | -65.21% |

---

## Platform & Chain Information

**Native Chain:** Chiliz

### Contract Addresses

| Chain | Address |
|---|---|
| Chiliz | `0xeaf368dadc22524def47e8a1c26bfc17ac16e6f5` |
| Solana | `HE6bLNs16qgQo2jVSMXDSCnxQahjdVrww7qQPrHrZtEw` |
| Base | `0x68504b889978f8f2a7ff0e29cdd8830856e4dcba` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | JUV/USDT | N/A |
| Upbit | JUV/BTC | N/A |
| Bitget | JUV/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.socios.com/juventus/](https://www.socios.com/juventus/) |
| **Twitter** | [@juventusfcen](https://twitter.com/juventusfcen) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.54M |
| **Market Cap Rank** | #1520 |
| **24h Range** | $0.3238 — $0.3429 |
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

Tradable on Binance SPOT only — no liquid perpetual venue, so leverage/short access is limited and this is a spot-primary asset. Perp funding/basis/liquidation strategies do NOT apply. With a single deep venue (JUV/USDT on Binance) plus thinner secondary CEX pairs, execution risk is concentrated: position sizing should account for shallow order books, wider slippage on market orders, and the absence of borrow/short inventory. Prefer limit orders, scale entries/exits, and size to what spot depth can absorb rather than leveraged notional. Directional exposure is effectively long-only; risk is managed by cash-vs-token allocation and stops, not by shorting.

### Applicable strategies

- [[breakout-trading]] — thin fan-token order books mean price gaps hard on real demand; clean breaks above range highs can run before liquidity refills.
- [[breakout-and-retest]] — waiting for a retest of a broken level filters false breaks common in low-cap, low-float JUV moves.
- [[event-driven-trading]] — Juventus match results, trophies, transfers, and Socios/Chiliz product news are discrete catalysts that repeatedly move fan tokens.
- [[news-trading]] — sports and club headlines drive short, sharp JUV spikes tradable on the initial reaction window.
- [[dca-strategy]] — for a spot-only, illiquid low-cap, averaging in over time reduces single-entry slippage and timing risk.
- [[atr-trailing-stop]] — volatility-scaled trailing stops adapt to JUV's erratic ranges and lock gains from event-driven pops without fixed levels.

### Volatility & regime character

Small-cap fan token with high, reflexive volatility driven more by club-specific sports events than by broad crypto beta. Correlation to BTC/ETH is loose and episodic — JUV can decouple entirely around match days or club announcements, then revert to low-liquidity drift. Behaves closer to a sentiment/event-reflexive memecoin-style asset than an infra or DeFi token, with sharp illiquidity-amplified spikes and deep, prolonged drawdowns (currently ~99% below its 2020 ATH).

### Risk flags

- **Liquidity/venue concentration** — depth is dominated by Binance spot; a listing change or volume dry-up sharply raises slippage and exit risk.
- **Narrative dependence** — value hinges on club performance and Socios/Chiliz fan-engagement demand rather than protocol fundamentals or cash flows.
- **Structural drawdown** — deeply below ATH with a small circulating base; low-cap fan tokens can bleed for extended periods between catalysts.
- **Regulatory** — fan tokens face evolving scrutiny over consumer-protection and promotion rules in some jurisdictions, which can affect access or listings.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=JUVUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=JUVUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=JUVUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=JUVUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

---
title: "AS Roma Fan Token"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["ASR"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.asroma.com/it"
related: ["[[crypto-markets]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[event-driven-trading]]"]
---

# AS Roma Fan Token

**AS Roma Fan Token** (ASR) is a Sports, Binance Launchpool, Fan Token, Solana Ecosystem, Base Ecosystem, Chiliz Ecosystem, YZi Labs (Prev. Binance Labs) Portfolio project. It ranks **#1303** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ASR |
| **Market Cap Rank** | #1303 |
| **Market Cap** | $7.65M |
| **Current Price** | $0.8798 |
| **Categories** | Sports, Binance Launchpool, Fan Token |
| **Website** | [https://www.asroma.com/it](https://www.asroma.com/it) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 8.69M ASR |
| **Total Supply** | 9.99M ASR |
| **Max Supply** | 9.99M ASR |
| **Fully Diluted Valuation** | $8.79M |
| **Market Cap / FDV Ratio** | 0.87 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $26.64 (2020-12-29) |
| **Current vs ATH** | -96.71% |
| **All-Time Low** | $0.7780 (2026-06-05) |
| **Current vs ATL** | +12.81% |
| **24h Change** | +0.84% |
| **7d Change** | +2.72% |
| **30d Change** | -24.18% |
| **1y Change** | -62.03% |

---

## Platform & Chain Information

**Native Chain:** Chiliz

### Contract Addresses

| Chain | Address |
|---|---|
| Chiliz | `0x0ac7bf9783ca1dcd86a39b5a2607160d29256eb0` |
| Solana | `3cVuTnMj8FeqK82PDgK4JzKnLP7LM6GauqTyqnxtcSk1` |
| Base | `0x53838837f258f8ef337c8b4ceb60a89190ecba8b` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ASR/USDT | N/A |
| Bitget | ASR/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.asroma.com/it](https://www.asroma.com/it) |
| **Twitter** | [@OfficialASRoma](https://twitter.com/OfficialASRoma) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.91M |
| **Market Cap Rank** | #1303 |
| **24h Range** | $0.8644 — $0.9232 |
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

ASR trades on **Binance** as both **spot (ASR/USDT)** and a **USD-margined perpetual**, giving access to funding, open interest, and liquidation data. It is **not listed on Hyperliquid**, so Binance is the primary leveraged venue. With a ~$5M daily volume and a small ~$8M market cap, order-book depth is thin: leveraged sizing must stay small relative to available liquidity, slippage on market orders can be material, and venue concentration on Binance means execution, funding, and liquidation dynamics are effectively dictated by a single exchange. Scale into positions with limit orders and treat the perp's funding/OI as the main real-time positioning signal.

### Applicable strategies

- [[funding-rate-harvest]] — collect funding on the Binance ASR perp when persistent long/short bias skews the rate, sizing modestly given thin depth.
- [[crowded-long-funding-fade]] — fade over-extended longs when funding turns sharply positive on fan-token hype (e.g. match results, sponsorship news).
- [[liquidation-cascade-fade]] — a low-float, thin-book perp is prone to stop-run cascades; fade capitulation wicks into liquidation clusters.
- [[cash-and-carry]] — harvest perp-vs-spot basis on Binance while holding spot ASR, exploiting funding without directional exposure.
- [[event-driven-trading]] — trade around discrete catalysts (AS Roma match outcomes, Launchpool/utility announcements) that drive fan-token flows.
- [[rsi-mean-reversion]] — the small-cap fan token overshoots on low liquidity; mean-revert stretched RSI extremes within its trading range.

### Volatility & regime character

Small-cap fan token (rank ~#1300) with pronounced reflexivity: price is driven far more by AS Roma sporting/brand catalysts and Chiliz-ecosystem sentiment than by broad crypto beta. Correlation to BTC/ETH is loose and episodic. Low float (~8.7M circulating of ~10M supply) and thin liquidity amplify moves in both directions, producing sharp, news-triggered volatility spikes followed by long drift periods. Deep drawdown from ATH (-96%) reflects a structurally declining, event-dependent regime rather than a trending one.

### Risk flags

- **Liquidity/venue concentration** — trading is concentrated on Binance (plus Bitget); thin depth makes the token vulnerable to slippage, wicks, and single-venue outages.
- **Narrative dependence** — value hinges on AS Roma performance and fan-engagement demand, not protocol fundamentals; interest can evaporate between catalysts.
- **Supply structure** — near-fully-diluted (MC/FDV ~0.87) limits unlock overhang, but a small max supply and low float make the market easy to move.
- **Regulatory** — fan tokens face evolving scrutiny over consumer-protection and promotional framing in several jurisdictions.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ASRUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=ASRUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=ASR` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=ASR` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ASRUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=ASRUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=ASR"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

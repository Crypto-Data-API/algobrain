---
title: "Act I The AI Prophecy"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, memecoins, altcoins]
aliases: ["ACT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://pump.fun/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump"
related: ["[[crypto-markets]]", "[[solana]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]", "[[narrative-trading]]"]
---

# Act I The AI Prophecy

**Act I The AI Prophecy** (ACT) is a Solana Ecosystem, Meme, Solana Meme, AI Meme, Pump.fun Ecosystem project. It ranks **#1262** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ACT |
| **Market Cap Rank** | #1262 |
| **Market Cap** | $8.28M |
| **Current Price** | $0.00872757 |
| **Categories** | Meme, Solana Meme, AI Meme |
| **Website** | [https://pump.fun/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump](https://pump.fun/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 948.24M ACT |
| **Total Supply** | 948.24M ACT |
| **Max Supply** | 1.00B ACT |
| **Fully Diluted Valuation** | $8.28M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.9198 (2024-11-14) |
| **Current vs ATH** | -99.05% |
| **All-Time Low** | $0.00709075 (2025-10-10) |
| **Current vs ATL** | +23.17% |
| **24h Change** | +1.61% |
| **7d Change** | +0.32% |
| **30d Change** | -16.39% |
| **1y Change** | -80.57% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ACT/TRY | N/A |
| Kraken | ACT/USD | N/A |
| Bitget | ACT/USDT | N/A |
| KuCoin | ACTSOL/USDT | N/A |
| Crypto.com Exchange | ACT/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://pump.fun/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump](https://pump.fun/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) |
| **Twitter** | [@ACTICOMMUNITY](https://twitter.com/ACTICOMMUNITY) |
| **Telegram** | [actportal](https://t.me/actportal) (8,911 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $8.08M |
| **Market Cap Rank** | #1262 |
| **24h Range** | $0.00850821 — $0.00895143 |
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

ACT is tradable on [[binance]] — spot plus a USD-margined [[perpetual-futures]] contract that exposes [[funding-rate]], [[open-interest]], and [[liquidations]] data. It is **not** listed on Hyperliquid, so Binance is the primary leveraged venue and the reference point for perp-based signals. With a sub-$10M market cap and roughly comparable daily volume, order books are thin: leverage concentrated on a single venue means liquidation flushes and funding swings are amplified, and even modest notional can move price. Execution should assume material slippage — favor limit orders, scale entries, and size well below what a mega-cap perp would allow. The lack of a second deep leveraged venue removes cross-exchange redundancy, so venue-specific outages or funding dislocations hit the whole book at once.

### Applicable strategies

- [[liquidation-cascade-fade]] — thin ACT perp liquidity means over-leveraged flushes overshoot; fading forced liquidations into support can capture the snap-back.
- [[crowded-long-funding-fade]] — memecoin rallies routinely drive ACT perp funding sharply positive; fading a crowded, expensive long book targets the funding-driven mean reversion.
- [[narrative-trading]] — ACT is an AI-meme on Solana/Pump.fun; price is driven far more by AI-narrative rotation than fundamentals, making narrative timing a core edge.
- [[volatility-breakout]] — low float and reflexive memecoin behavior produce sharp, tradable expansions out of quiet ranges on Binance spot/perp.
- [[rsi-mean-reversion]] — after parabolic moves ACT frequently reverts; RSI extremes on the daily flag exhaustion for counter-trend entries.
- [[oi-confirmed-trend]] — rising Binance open interest alongside price confirms genuine leveraged participation versus a hollow spot-only pop.

### Volatility & regime character

Small-cap (rank ~1253) Solana AI-memecoin with extreme, high-beta reflexivity: it amplifies broad crypto risk-on/risk-off moves and is acutely sensitive to Solana ecosystem and AI-narrative flows. Correlation to BTC/ETH is loose and situational — ACT can decouple violently on narrative catalysts, then round-trip just as fast. Expect wide intraday ranges, funding that whipsaws with sentiment, and long drawdowns punctuated by sharp squeezes.

### Risk flags

- **Liquidity & venue concentration** — thin books; leveraged exposure hinges on a single Binance perp with no Hyperliquid backstop.
- **Narrative dependence** — value is tied to the AI-meme narrative; fading interest can bleed price with no fundamental floor (currently ~99% below ATH).
- **Supply/float dynamics** — near-fully-circulating Pump.fun memecoin; concentrated holders and low float make it prone to reflexive pumps and dumps.
- **Regulatory/venue risk** — memecoin status and reliance on one primary leveraged venue leave it exposed to listing, delisting, or compliance actions.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ACTUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=ACTUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=ACT` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=ACT` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ACTUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=ACTUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=ACT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

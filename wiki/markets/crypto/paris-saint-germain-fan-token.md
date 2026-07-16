---
title: "Paris Saint-Germain Fan Token"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, altcoins]
aliases: ["PSG"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.psg.fr/"
related: ["[[crypto-markets]]", "[[binance]]", "[[narrative-trading]]", "[[event-driven-trading]]"]
---

# Paris Saint-Germain Fan Token

**Paris Saint-Germain Fan Token** (PSG) is a Sports, Binance Launchpool, Fan Token, Solana Ecosystem, Base Ecosystem, Chiliz Ecosystem, YZi Labs (Prev. Binance Labs) Portfolio project. It ranks **#1220** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PSG |
| **Market Cap Rank** | #1220 |
| **Market Cap** | $8.90M |
| **Current Price** | $0.5445 |
| **Categories** | Sports, Binance Launchpool, Fan Token |
| **Website** | [https://www.psg.fr/](https://www.psg.fr/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 16.35M PSG |
| **Total Supply** | 19.89M PSG |
| **Max Supply** | 19.89M PSG |
| **Fully Diluted Valuation** | $10.83M |
| **Market Cap / FDV Ratio** | 0.82 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $58.79 (2021-04-27) |
| **Current vs ATH** | -99.07% |
| **All-Time Low** | $0.5094 (2026-06-24) |
| **Current vs ATL** | +7.05% |
| **24h Change** | +1.96% |
| **7d Change** | +2.99% |
| **30d Change** | -1.49% |
| **1y Change** | -66.22% |

---

## Platform & Chain Information

**Native Chain:** Chiliz

### Contract Addresses

| Chain | Address |
|---|---|
| Chiliz | `0xfe1d4a935df7a4a52f835f6104c97af9d72217f2` |
| Solana | `5eyib4qghYGHNh7VvxSFGYLFJSanjq9hug9fR52kksnm` |
| Base | `0xdd15623d107c639af0c5127affa26d3f20327ec8` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | PSG/TRY | N/A |
| Upbit | PSG/BTC | N/A |
| Bitget | PSG/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.psg.fr/](https://www.psg.fr/) |
| **Twitter** | [@PSG_inside](https://twitter.com/PSG_inside) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $7.44M |
| **Market Cap Rank** | #1220 |
| **24h Range** | $0.5276 — $0.5706 |
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

PSG is tradable on **Binance SPOT only** — there is no liquid perpetual venue for this fan token, so leverage and short access are limited and this is effectively a **spot-primary asset**. Perp funding, basis, and liquidation strategies do **not** apply. With a thin market cap (~#1215) and volume concentrated on a single primary venue, execution should assume shallow order books: size positions conservatively, prefer limit orders, and expect meaningful slippage on market orders. Venue concentration also means Binance listing/pair changes (e.g., PSG/TRY, PSG/USDT availability) directly shape where and how PSG can be traded.

### Applicable strategies

- [[breakout-and-retest]] — thin single-venue fan tokens can gap on match/roster news; entering on a confirmed breakout that holds a retest filters false spikes.
- [[range-mean-reversion]] — PSG spends long stretches oscillating in a tight band near its ATL, favoring fades of range extremes over trend chasing.
- [[rsi-mean-reversion]] — low-liquidity spot names overshoot on sentiment; RSI extremes flag exhausted moves for reversion entries.
- [[narrative-trading]] — as a football club fan token, price is driven by club-specific narratives (signings, trophies, Fan Token ecosystem hype) rather than fundamentals.
- [[event-driven-trading]] — discrete catalysts (matches, transfers, Chiliz/Socios promotions) create tradable spikes around scheduled or announced events.
- [[dca-strategy]] — for spot-only accumulation, cost-averaging smooths entry into an illiquid, high-volatility name without relying on precise timing.

### Volatility & regime character

PSG is a **small-cap fan token** with high idiosyncratic volatility and strong reflexivity around club news, closer in behavior to a niche sentiment/narrative asset than to infra or DeFi tokens. Its beta to BTC/ETH is loose and event-dependent: broad crypto risk-on phases can lift it, but club-specific catalysts frequently dominate and decouple it from majors. Deep drawdown from ATH (a fan-token-cycle characteristic) leaves it trading near cycle lows with sharp, short-lived rallies.

### Risk flags

- **Liquidity & venue concentration** — Binance-spot-primary with no liquid perp; single-venue dependence raises slippage and delisting/pair-availability risk.
- **Narrative dependence** — value is tied to club performance and Fan Token sentiment, not cash flows; hype fades quickly and can reverse sharply.
- **Emissions/supply** — max supply is nearly fully circulating, limiting future dilution but also capping structural demand drivers.
- **Regulatory** — fan tokens face evolving scrutiny in some jurisdictions; regional trading pairs may appear or disappear based on compliance.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=PSGUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=PSGUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=PSGUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=PSGUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

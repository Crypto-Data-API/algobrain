---
title: "AC Milan Fan Token"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, altcoins]
aliases: ["ACM"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.socios.com/"
related: ["[[crypto-markets]]", "[[binance]]", "[[range-trading]]", "[[dca-strategy]]"]
---

# AC Milan Fan Token

**AC Milan Fan Token** (ACM) is a Sports, Fan Token, Solana Ecosystem, Base Ecosystem, Binance Launchpad, Chiliz Ecosystem project. It ranks **#1696** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ACM |
| **Market Cap Rank** | #1696 |
| **Market Cap** | $4.10M |
| **Current Price** | $0.2970 |
| **Categories** | Sports, Fan Token, Binance Launchpad |
| **Website** | [https://www.socios.com/](https://www.socios.com/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 13.83M ACM |
| **Total Supply** | 19.92M ACM |
| **Max Supply** | 19.92M ACM |
| **Fully Diluted Valuation** | $5.91M |
| **Market Cap / FDV Ratio** | 0.69 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $23.20 (2021-02-24) |
| **Current vs ATH** | -98.72% |
| **All-Time Low** | $0.2776 (2026-07-13) |
| **Current vs ATL** | +7.02% |
| **24h Change** | +3.81% |
| **7d Change** | +4.29% |
| **30d Change** | -4.78% |
| **1y Change** | -64.06% |

---

## Platform & Chain Information

**Native Chain:** Chiliz

### Contract Addresses

| Chain | Address |
|---|---|
| Chiliz | `0x062f6004fd0bf204d272ff115e5b84f7a01489d1` |
| Solana | `H5qGPniSX2uCNtAnxr7RpdfFAZcGkr6dknjgpa1AKHe1` |
| Base | `0x886edf4ce5d879667bb62271bb9d59227b689cdc` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ACM/USDT | N/A |
| Upbit | ACM/BTC | N/A |
| Bitget | ACM/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.socios.com/](https://www.socios.com/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.88M |
| **Market Cap Rank** | #1696 |
| **24h Range** | $0.2832 — $0.3025 |
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

ACM is tradable on **Binance SPOT only** — there is no liquid perpetual venue, so leverage and short access are limited and this is a **spot-primary** asset. Perp funding, basis, and liquidation strategies do **not** apply. With liquidity concentrated on a single primary venue and a thin market cap, execution must lean on limit orders rather than market sweeps; the shallow book and single-venue dependence argue for small clip sizes, patience around fills, and awareness that Binance availability effectively defines tradability. Sizing should be conservative relative to 24h volume to avoid moving the book against yourself.

### Applicable strategies

- [[range-trading]] — ACM has spent extended stretches chopping in a tight band near its ATL; fading defined support/resistance suits a spot-only, low-momentum fan token.
- [[range-mean-reversion]] — with no perp leverage and a mean-reverting price near lows, buying weakness toward support and trimming into strength fits the market structure.
- [[rsi-mean-reversion]] — oversold/overbought RSI extremes on a thin, headline-driven fan token often snap back, making momentum-oscillator reversion practical for spot entries.
- [[breakout-trading]] — fan tokens react sharply to club news and campaigns; capturing breakouts out of the ACM base can catch event-driven expansion.
- [[dca-strategy]] — for spot accumulation of a small-cap with no leverage, averaging in dampens single-fill timing risk in an illiquid book.
- [[news-trading]] — ACM price is tied to AC Milan sporting results, sponsorships, and Socios/fan-engagement announcements, which are discrete tradable catalysts.

### Volatility & regime character

ACM is a **small-cap fan token** (rank ~1702) with low, sporadic liquidity and high idiosyncratic risk. Its price is driven more by club-specific narrative and fan-engagement cycles than by broad crypto beta, though it still tends to bleed with BTC/ETH risk-off regimes while under-participating in market rallies. Expect reflexive, event-clustered volatility — quiet drift punctuated by sharp moves around football-season and announcement catalysts — rather than steady trend.

### Risk flags

- **Liquidity / venue concentration** — Binance-spot primary; single-venue dependence and a thin order book create slippage and delisting exposure.
- **Narrative dependence** — value is tethered to AC Milan performance, sponsorships, and Socios platform relevance; utility can fade if fan-engagement demand wanes.
- **Small-cap fragility** — low market cap and FDV make the token vulnerable to outsized swings on modest flow.
- **Sector/regulatory** — fan tokens face evolving regulatory scrutiny and platform-dependency risk (Socios/Chiliz ecosystem).

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ACMUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=ACMUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ACMUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ACMUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

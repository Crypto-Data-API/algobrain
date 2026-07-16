---
title: "Atletico Madrid Fan Token"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, altcoins]
aliases: ["ATM"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.atleticodemadrid.com/"
related: ["[[crypto-markets]]", "[[binance]]", "[[narrative-trading]]", "[[event-driven-trading]]"]
---

# Atletico Madrid Fan Token

**Atletico Madrid Fan Token** (ATM) is a Sports, Binance Launchpool, Fan Token, Solana Ecosystem, Base Ecosystem, Chiliz Ecosystem, YZi Labs (Prev. Binance Labs) Portfolio project. It ranks **#716** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ATM |
| **Market Cap Rank** | #716 |
| **Market Cap** | $25.28M |
| **Current Price** | $2.87 |
| **Categories** | Sports, Binance Launchpool, Fan Token |
| **Website** | [https://www.atleticodemadrid.com/](https://www.atleticodemadrid.com/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 8.80M ATM |
| **Total Supply** | 10.00M ATM |
| **Max Supply** | 10.00M ATM |
| **Fully Diluted Valuation** | $28.73M |
| **Market Cap / FDV Ratio** | 0.88 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $58.46 (2021-05-16) |
| **Current vs ATH** | -95.10% |
| **All-Time Low** | $0.7523 (2026-02-06) |
| **Current vs ATL** | +280.58% |
| **24h Change** | +0.79% |
| **7d Change** | +22.32% |
| **30d Change** | +149.56% |
| **1y Change** | +168.51% |

---

## Platform & Chain Information

**Native Chain:** Chiliz

### Contract Addresses

| Chain | Address |
|---|---|
| Chiliz | `0x7da0eb973d982ffca095e80437f5e37459a95c67` |
| Solana | `6VdpC1hcx7byFtJ5M6Xhspa6Uup5rZHruzXvuJhXAyXm` |
| Base | `0xb46357d8ed050d35d3a24154c39d7236dae86187` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ATM/USDT | N/A |
| Upbit | ATM/BTC | N/A |
| Bitget | ATM/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.atleticodemadrid.com/](https://www.atleticodemadrid.com/) |
| **Twitter** | [@Atleti](https://twitter.com/Atleti) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.92M |
| **Market Cap Rank** | #716 |
| **24h Range** | $2.80 — $2.88 |
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

ATM is tradable on **Binance SPOT only** — there is no liquid perpetual venue, so leverage and short access are limited and this is a **spot-primary asset**. Perp funding, basis, and liquidation strategies do **not** apply. With a thin ~$25M market cap and modest daily turnover, liquidity is concentrated on a single primary venue; this makes execution sensitive to slippage on larger orders. Practical implications: size positions small relative to daily volume, favor limit orders and TWAP/VWAP-style entries over aggressive market fills, and expect wider effective spreads during off-peak hours. Directional exposure is long-biased since borrow-to-short liquidity is scarce; risk must be managed by position sizing and stops rather than by hedging with derivatives.

### Applicable strategies

- [[breakout-trading]] — the +149% 30d and +22% 7d moves show ATM can trend hard off consolidation, making spot breakouts above prior ranges tradable.
- [[donchian-channel-breakout]] — with no perps, a channel-breakout rule on daily klines offers a mechanical long-only entry/exit for the fan-token's episodic thrusts.
- [[atr-trailing-stop]] — high realized volatility and single-venue liquidity make an ATR-based trailing stop the primary risk tool in the absence of hedging.
- [[event-driven-trading]] — as an Atletico Madrid fan token, price reacts to club match results, transfers, and sporting events, a distinct catalyst calendar.
- [[narrative-trading]] — fan-token demand is sentiment- and fandom-driven, so narrative flow (fixtures, sponsorships, Chiliz ecosystem hype) dominates moves.
- [[dca-strategy]] — for spot-only accumulation of a low-cap, illiquid token, averaging in reduces single-fill slippage and timing risk.

### Volatility & regime character

Small-cap (~#716) fan token with high reflexivity: sharp, event-clustered rallies (recent multi-month gains well over 100%) interspersed with deep drawdowns (currently ~95% below its 2021 ATH). It is a Chiliz-ecosystem sports/fan token rather than a DeFi or infrastructure play, so its beta to BTC/ETH is loose and intermittent — moves are often idiosyncratic, driven by club-specific and fan sentiment rather than broad crypto regime. Expect low correlation during quiet periods and elevated correlation only in broad risk-off flushes.

### Risk flags

- **Venue/liquidity concentration** — Binance-spot-primary with thin turnover; execution and exit liquidity depend heavily on one venue.
- **No perp/hedging market** — leverage and shorting are limited; long-biased exposure cannot be easily hedged.
- **Narrative/event dependence** — value is tied to club performance and fan sentiment, not fundamentals or cash flows; catalysts can reverse quickly.
- **Small-cap fragility** — low market cap and near-full supply (MC/FDV 0.88) mean large orders and sentiment shifts can move price sharply.
- **Regulatory** — fan tokens face evolving scrutiny in some jurisdictions over their classification and marketing.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ATMUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=ATMUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ATMUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ATMUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

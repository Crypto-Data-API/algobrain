---
title: "Four"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["FORM"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://linktr.ee/Four_FORM_"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# Four

**Four** (FORM) is a Gaming (GameFi), BNB Chain Ecosystem, Launchpad project. It ranks **#282** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FORM |
| **Market Cap Rank** | #282 |
| **Market Cap** | $89.69M |
| **Current Price** | $0.234864 |
| **Categories** | Gaming (GameFi), BNB Chain Ecosystem, Launchpad |
| **Website** | [https://linktr.ee/Four_FORM_](https://linktr.ee/Four_FORM_) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 381.87M FORM |
| **Total Supply** | 572.30M FORM |
| **Max Supply** | 580.00M FORM |
| **Fully Diluted Valuation** | $118.71M |
| **Market Cap / FDV Ratio** | 0.67 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $4.19 (2025-09-08) |
| **Current vs ATH** | -95.04% |
| **All-Time Low** | $0.1809 (2026-02-28) |
| **Current vs ATL** | +14.78% |
| **24h Change** | -2.96% |
| **7d Change** | -8.00% |
| **30d Change** | -24.75% |
| **1y Change** | -89.31% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0x5b73a93b4e5e4f1fd27d8b3f8c97d69908b5e284` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | FORM/USDT | N/A |
| Bitget | FORM/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://linktr.ee/Four_FORM_](https://linktr.ee/Four_FORM_) |
| **Twitter** | [@Four_FORM_](https://twitter.com/Four_FORM_) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.78M |
| **Market Cap Rank** | #282 |
| **24h Range** | $0.2074 — $0.2213 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

FORM is tradable on **Binance** — both spot (FORM/USDT) and a **USD-margined perpetual** with funding, open interest, and liquidation data. It is **not listed on Hyperliquid**, so Binance is the primary leveraged venue. With a thin 24h spot volume for a small-cap altcoin, order books are shallow: large market orders can slip meaningfully, and the concentration of leveraged activity on a single perp venue means funding and liquidation dynamics are dominated by Binance flow. Practically, size positions conservatively, favor limit/VWAP-style execution over aggressive market fills, and treat Binance funding and OI as the canonical read on positioning. The absence of a second deep leveraged venue removes cross-exchange perp arbitrage and makes basis/carry trades dependent on Binance's single funding stream.

### Applicable strategies

- [[funding-rate-harvest]] — collect Binance perp funding when FORM's single-venue perp swings to a persistent premium or discount.
- [[cash-and-carry]] — hold Binance spot FORM against the short USD-M perp to capture basis when the perp trades rich to spot.
- [[liquidation-cascade-fade]] — thin books plus concentrated leverage make FORM prone to sharp liquidation wicks that overshoot and mean-revert.
- [[breakout-and-retest]] — low-liquidity small-cap that trends hard on GameFi/launchpad narrative catalysts, then retests broken levels.
- [[oi-confirmed-trend]] — use Binance open-interest changes to separate real trend legs from low-conviction, low-volume drifts.
- [[narrative-trading]] — price is highly sensitive to BNB Chain ecosystem and GameFi/launchpad narrative rotation.

### Volatility & regime character

FORM is a small-cap (rank ~325) GameFi/launchpad token on BNB Chain, and trades with high-beta, reflexive volatility typical of that cohort. It is down heavily from its ATH and exhibits amplified moves relative to BTC/ETH — rallying and bleeding faster in both directions. Correlation to majors is loose day-to-day but tends to spike (toward high positive beta) during broad risk-off flushes, while idiosyncratic, narrative-driven pumps dominate in risk-on windows. Regime is dominated by liquidity conditions: in thin tape, single large orders and liquidation cascades set the range.

### Risk flags

- **Liquidity & venue concentration** — thin spot volume and a single leveraged venue (Binance) concentrate execution and liquidation risk; delisting or venue disruption would be severe.
- **Emissions / unlocks** — circulating supply is well below max supply (MC/FDV ~0.67), so future token unlocks and emissions add persistent sell-side pressure risk.
- **Narrative dependence** — valuation leans on GameFi and BNB Chain launchpad narratives; rotation out of those themes can drive sustained drawdowns.
- **Small-cap fragility** — low market cap and shallow books make FORM vulnerable to manipulation, gap moves, and outsized liquidation-driven wicks.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=FORMUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=FORMUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=FORM` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=FORM` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=FORMUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=FORMUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=FORM"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

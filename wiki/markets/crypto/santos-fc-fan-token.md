---
title: "Santos FC Fan Token"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["SANTOS"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.santosfc.com.br/en/"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[event-driven-trading]]", "[[funding-rate-harvest]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Santos FC Fan Token

**Santos FC Fan Token** (SANTOS) is a Sports, BNB Chain Ecosystem, Binance Launchpool, Fan Token project. It ranks **#915** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SANTOS |
| **Market Cap Rank** | #915 |
| **Market Cap** | $16.35M |
| **Current Price** | $1.02 |
| **Categories** | Sports, BNB Chain Ecosystem, Binance Launchpool, Fan Token |
| **Website** | [https://www.santosfc.com.br/en/](https://www.santosfc.com.br/en/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 16.09M SANTOS |
| **Total Supply** | 30.00M SANTOS |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $30.47M |
| **Market Cap / FDV Ratio** | 0.54 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $22.34 (2022-09-25) |
| **Current vs ATH** | -95.42% |
| **All-Time Low** | $0.7340 (2025-10-10) |
| **Current vs ATL** | +39.56% |
| **24h Change** | -3.28% |
| **7d Change** | -9.04% |
| **30d Change** | -18.87% |
| **1y Change** | -57.88% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xa64455a4553c9034236734faddaddbb64ace4cc7` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SANTOS/USDT | N/A |
| Bitget | SANTOS/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.santosfc.com.br/en/](https://www.santosfc.com.br/en/) |
| **Twitter** | [@SantosFC](https://twitter.com/SantosFC) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.11M |
| **Market Cap Rank** | #915 |
| **24h Range** | $1.01 — $1.08 |
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

SANTOS trades on [[binance]] as both spot (SANTOS/USDT) and a USD-margined [[perpetual-futures|perpetual]] contract, so the full derivatives stack — [[funding-rate|funding]], [[open-interest]], and [[liquidations]] — is observable and tradable there. It is **not** listed on Hyperliquid, making Binance the primary (effectively sole) leveraged venue. This venue concentration means execution and sizing depend entirely on Binance depth: as a low-market-cap fan token with thin 24h volume, order books are shallow, leveraged positions must be kept small to avoid slippage, and funding/OI signals reflect a single venue rather than a broad cross-exchange consensus.

### Applicable strategies

- [[funding-rate-harvest]] — collect perp funding on a delta-neutral spot-vs-perp position when SANTOS funding runs persistently positive around fan-token hype events.
- [[crowded-long-funding-fade]] — fade over-leveraged longs when funding spikes hard on a matchday or roster-news pump, a common pattern in sports fan tokens.
- [[cash-and-carry]] — capture basis by holding SANTOS spot against a short perp when the perpetual trades at a premium during retail-driven rallies.
- [[liquidation-cascade-fade]] — thin Binance depth makes SANTOS prone to sharp liquidation wicks; fade the flush once the cascade exhausts.
- [[event-driven-trading]] — trade around discrete catalysts (Santos FC match results, transfers, club announcements) that drive most of this token's directional moves.
- [[breakout-and-retest]] — trade confirmed breakouts from the tight low-volatility ranges this token forms between catalysts.

### Volatility & regime character

Small-cap (rank ~1230) fan token with high reflexivity: long, quiet low-volatility drift punctuated by violent catalyst-driven spikes tied to club performance and Binance Launchpool/promotional activity. Correlation to BTC/ETH is loose — idiosyncratic sports and hype narratives dominate over broad crypto beta, though it still sells off in market-wide risk-off moves. Deep drawdown from ATH and shrinking market cap point to a structurally weak, sentiment-driven regime.

### Risk flags

- **Liquidity/venue concentration** — Binance is effectively the only meaningful venue; thin volume amplifies slippage and gap risk, and any Binance policy change (delisting, promo end) is an outsized risk.
- **Unlimited max supply** — no hard cap on emissions; new fan-token issuance can dilute holders.
- **Narrative dependence** — price is tightly coupled to Santos FC results and hype cycles rather than fundamentals, making moves hard to hedge and prone to reversal.
- **Fan-token/regulatory** — sports fan tokens face evolving regulatory scrutiny in several jurisdictions, adding headline and access risk.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=SANTOSUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=SANTOSUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=SANTOS` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=SANTOS` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=SANTOSUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=SANTOSUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=SANTOS"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

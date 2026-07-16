---
title: "Katana"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, defi, altcoins, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["KAT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://katana.network/"
related: ["[[crypto-markets]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[oi-confirmed-trend]]", "[[token-unlock-supply-event]]"]
---

# Katana

**Katana** (KAT) is a cryptocurrency. It ranks **#920** by market capitalization. KAT is a defi token with governance-like mechanics for Katana.

It is designed to function as a lever for directing capital: users that lock KAT receive a voting version of KAT — vKAT — in return. vKAT underpins key aspects of the chain’s economy, providing rewards to those users that participate.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | KAT |
| **Market Cap Rank** | #920 |
| **Market Cap** | $16.37M |
| **Current Price** | $0.00699 |
| **Categories** | Decentralized Finance (DeFi), Yield Farming, Layer 2 (L2), Binance Alpha Spotlight, Katana Ecosystem |
| **Website** | [https://katana.network/](https://katana.network/) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Overview

KAT is a defi token with governance-like mechanics for Katana.

It is designed to function as a lever for directing capital: users that lock KAT receive a voting version of KAT — vKAT — in return. vKAT underpins key aspects of the chain’s economy, providing rewards to those users that participate. these fee-based rewards function as an incentive for KAT holders to engage in cooperative, positive-sum behavior.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.34B KAT |
| **Total Supply** | 10.00B KAT |
| **Max Supply** | 10.00B KAT |
| **Fully Diluted Valuation** | $86.87M |
| **Market Cap / FDV Ratio** | 0.23 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0185 (2026-03-18) |
| **Current vs ATH** | -52.81% |
| **All-Time Low** | $0.00842540 (2026-04-05) |
| **Current vs ATL** | +3.60% |
| **24h Change** | -3.68% |
| **7d Change** | -14.19% |
| **30d Change** | +0.00% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Katana

### Contract Addresses

| Chain | Address |
|---|---|
| Katana | `0x7f1f4b4b29f5058fa32cc7a97141b8d7e5abdc2d` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | KAT/USDT | N/A |
| Kraken | KAT/USD | N/A |
| Upbit | KAT/KRW | N/A |
| Bitget | KAT/USDT | N/A |
| KuCoin | KAT/USDT | N/A |
| Crypto.com Exchange | KAT/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://katana.network/](https://katana.network/) |
| **Twitter** | [@katana](https://twitter.com/katana) |
| **GitHub** | [https://github.com/katana-network/](https://github.com/katana-network/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $12.23M |
| **Market Cap Rank** | #920 |
| **24h Range** | $0.00867659 — $0.00903063 |
| **CoinGecko Sentiment** | 100% positive |
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

KAT is tradable on **Binance** — both spot (KAT/USDT) and a **USD-margined perpetual** exposing funding, open interest, and liquidation data. It is **NOT listed on Hyperliquid**, so Binance is the primary leveraged venue and effectively the single source of on-exchange derivatives price discovery. With a sub-$20M cap and thin (~$12M/24h) volume, the perp order book is shallow: available leverage is capped and small-notional sizing is essential, since even modest market orders can move price and trigger cascade liquidations. Concentration on one leveraged venue means execution, funding, and basis are all anchored to Binance — cross-venue hedging or arbitrage requires spot legs on secondary CEXs (Kraken, Bitget, KuCoin, Upbit) that carry their own liquidity fragmentation.

### Applicable strategies

- [[funding-rate-harvest]] — a low-cap, retail-driven perp like KAT often runs persistently skewed funding, letting a delta-neutral spot-vs-perp position collect the carry.
- [[crowded-long-funding-fade]] — narrative-led spikes (Binance Alpha / L2 DeFi hype) tend to crowd longs and push funding to extremes, offering a fade edge when perp premium overheats.
- [[liquidation-cascade-fade]] — the shallow single-venue book makes KAT prone to over-shoot liquidation flushes that mean-revert, favoring disciplined fade entries.
- [[token-unlock-supply-event]] — with only ~23% of the 10B supply circulating (MC/FDV 0.23), scheduled unlocks are a recurring, tradable supply catalyst.
- [[oi-confirmed-trend]] — pairing Binance open-interest growth with price confirms genuine leveraged trends versus low-conviction chop in a thin market.
- [[narrative-trading]] — KAT's price is tightly coupled to the Katana ecosystem / DeFi-L2 narrative, so catalyst-driven positioning around ecosystem news is a primary driver.

### Volatility & regime character

Small-cap DeFi/L2 infrastructure token with high idiosyncratic volatility and strong reflexivity typical of low-float, high-FDV names. Beta to BTC/ETH is elevated in risk-off moves (it sells off with the broad alt complex) but decouples upward on Katana-ecosystem or Binance-listing catalysts. Regime is narrative- and liquidity-sensitive rather than macro-driven; expect sharp expansion/contraction cycles around unlocks and hype phases.

### Risk flags

- **Venue concentration:** Binance is effectively the only meaningful leveraged venue; a listing change or downtime removes derivatives price discovery.
- **Liquidity/slippage:** thin volume and shallow perp depth amplify slippage and liquidation-cascade risk; keep leverage and size conservative.
- **Supply overhang:** low circulating-to-total ratio (~23%) means ongoing emissions/unlocks can pressure price regardless of demand.
- **Narrative dependence:** value is anchored to the Katana ecosystem story; fading hype or reduced incentives can compress liquidity quickly.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=KATUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=KATUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=KAT` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=KAT` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=KATUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=KATUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=KAT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

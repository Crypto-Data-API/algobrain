---
title: "Dolomite"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, defi, altcoins, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["DOLO"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://dolomite.io/"
related: ["[[crypto-markets]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Dolomite

**Dolomite** (DOLO) is a Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), Automated Market Maker (AMM), Lending/Borrowing Protocols, Ethereum Ecosystem, Coinbase Ventures Portfolio, Dex Aggregator project. It ranks **#934** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | DOLO |
| **Market Cap Rank** | #934 |
| **Market Cap** | $15.69M |
| **Current Price** | $0.0339 |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), Automated Market Maker (AMM), Lending/Borrowing Protocols, Ethereum Ecosystem, Coinbase Ventures Portfolio, Dex Aggregator |
| **Website** | [https://dolomite.io/](https://dolomite.io/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 463.49M DOLO |
| **Total Supply** | 998.25M DOLO |
| **Max Supply** | 1.00B DOLO |
| **Fully Diluted Valuation** | $33.79M |
| **Market Cap / FDV Ratio** | 0.46 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.3664 (2025-08-31) |
| **Current vs ATH** | -90.75% |
| **All-Time Low** | $0.0290 (2025-06-22) |
| **Current vs ATL** | +16.80% |
| **24h Change** | +1.30% |
| **7d Change** | +0.49% |
| **30d Change** | +2.37% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Berachain

### Contract Addresses

| Chain | Address |
|---|---|
| Berachain | `0x0f81001ef0a83ecce5ccebf63eb302c70a39a654` |
| Ethereum | `0x0f81001ef0a83ecce5ccebf63eb302c70a39a654` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | DOLO/USDT | N/A |
| Kraken | DOLO/USD | N/A |
| KuCoin | DOLO/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X0F81001EF0A83ECCE5CCEBF63EB302C70A39A654/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://dolomite.io/](https://dolomite.io/) |
| **Twitter** | [@Dolomite_io](https://twitter.com/Dolomite_io) |
| **Telegram** | [dolomite_official](https://t.me/dolomite_official) (2,760 members) |
| **GitHub** | [https://github.com/dolomite-exchange](https://github.com/dolomite-exchange) |
| **Whitepaper** | [https://dolomite.io/Dolomite-v2-Protocol-Whitepaper-v2.0.pdf](https://dolomite.io/Dolomite-v2-Protocol-Whitepaper-v2.0.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.69M |
| **Market Cap Rank** | #934 |
| **24h Range** | $0.0329 — $0.0352 |
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

DOLO is tradable on **Binance** — both spot (DOLO/USDT) and a **USD-margined perpetual** contract, which exposes funding, open interest, and liquidation data. It is **NOT** listed on Hyperliquid, so Binance is the primary leveraged venue for this token. With a sub-$5M 24h volume and a small-cap market position (rank ~1099), the perpetual order book is thin: leverage amplifies slippage, funding can swing sharply on modest flow, and stacked liquidations can gap price. Practical implication — size conservatively, favor limit/maker entries, split large orders, and lean on Binance's spot+perp pairing (rather than fragmented DEX/CEX venues) to keep execution tight.

### Applicable strategies

- [[funding-rate-harvest]] — harvest recurring funding on the Binance DOLO perp when the rate is persistently one-sided, hedged against spot.
- [[cash-and-carry]] — pair long Binance spot DOLO against a short perp to capture positive basis with market-neutral exposure.
- [[crowded-long-funding-fade]] — fade over-leveraged longs when funding spikes positive during small-cap DeFi pumps.
- [[liquidation-cascade-fade]] — thin DOLO perp liquidity makes forced-liquidation flushes prone to overshoot and snap-back reversion.
- [[oi-confirmed-trend]] — use Binance open-interest expansion to confirm genuine directional moves versus low-conviction chop.
- [[breakout-and-retest]] — trade breakouts from DOLO's tight consolidation ranges, waiting for a retest to filter thin-book false moves.

### Volatility & regime character

DOLO is a **small-cap DeFi / DEX infrastructure token** (Berachain-native, Ethereum-deployed) with high beta to broader crypto risk sentiment. It trades far below its ATH and clusters near historic lows, giving it reflexive, headline-sensitive swings typical of low-float DeFi names. Directionally it tends to correlate with BTC/ETH risk-on/risk-off cycles but with exaggerated amplitude and shallower liquidity, so idiosyncratic protocol news and DeFi-sector rotation can dominate short-term price action.

### Risk flags

- **Liquidity / venue concentration** — leveraged trading is effectively Binance-only; a listing or venue change materially alters execution and funding dynamics.
- **Emissions / unlocks** — circulating supply (~463M) is well below max supply (1B), so ongoing emissions and future unlocks are a persistent supply-overhang risk.
- **Narrative dependence** — price is sensitive to DeFi/DEX-sector sentiment and Berachain ecosystem momentum rather than standalone fundamentals.
- **Thin small-cap tape** — low volume and small market cap raise slippage, gap, and manipulation risk, especially into leveraged liquidation zones.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=DOLOUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=DOLOUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=DOLO` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=DOLO` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=DOLOUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=DOLOUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=DOLO"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

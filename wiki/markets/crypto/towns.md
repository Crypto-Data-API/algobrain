---
title: "Towns"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["TOWNS"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.towns.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# Towns

**Towns** (TOWNS) is a Communication, Smart Contract Platform, SocialFi, BNB Chain Ecosystem, Layer 2 (L2), Base Ecosystem, Binance HODLer Airdrops, Binance Alpha Spotlight, Base Native project. It ranks **#1658** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TOWNS |
| **Market Cap Rank** | #1658 |
| **Market Cap** | $4.39M |
| **Current Price** | $0.00207940 |
| **Categories** | Communication, Smart Contract Platform, SocialFi, Layer 2 (L2), Binance HODLer Airdrops, Binance Alpha Spotlight, Base Native |
| **Website** | [https://www.towns.com/](https://www.towns.com/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.11B TOWNS |
| **Total Supply** | 10.13B TOWNS |
| **Max Supply** | 15.33B TOWNS |
| **Fully Diluted Valuation** | $21.06M |
| **Market Cap / FDV Ratio** | 0.21 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0701 (2025-08-05) |
| **Current vs ATH** | -97.03% |
| **All-Time Low** | $0.00171606 (2026-06-30) |
| **Current vs ATL** | +21.45% |
| **24h Change** | -0.89% |
| **7d Change** | +3.39% |
| **30d Change** | -10.48% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x000000fa00b200406de700041cfc6b19bbfb4d13` |
| Binance Smart Chain | `0x00000000bca93b25a6694ca3d2109d545988b13b` |
| Base | `0x00000000a22c618fd6b4d7e9a335c4b96b189a38` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | TOWNS/USDT | N/A |
| Bitget | TOWNS/USDT | N/A |
| KuCoin | TOWNS/USDT | N/A |
| Crypto.com Exchange | TOWNS/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.towns.com/](https://www.towns.com/) |
| **Twitter** | [@townsxyz](https://twitter.com/townsxyz) |
| **GitHub** | [https://github.com/towns-protocol](https://github.com/towns-protocol) |
| **Whitepaper** | [https://docs.towns.com/introduction](https://docs.towns.com/introduction) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $27.22M |
| **Market Cap Rank** | #1658 |
| **24h Range** | $0.00206396 — $0.00223665 |
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

TOWNS is tradable on **Binance** — both **spot** and a **USD-margined perpetual** with the full derivatives surface (funding rate, open interest, liquidations). It is **NOT** listed on Hyperliquid, so Binance is the primary leveraged venue. As a micro-cap (rank ~1643), spot depth is thin and concentrated across a handful of CEXs (Binance, Bitget, KuCoin, Crypto.com), so the Binance perp is the main source of leverage and price discovery. Practical implications: order books are shallow and slippage-prone, so size positions to a fraction of visible depth, favor limit orders, and expect wide effective spreads. Funding and open-interest data on the perp are the cleanest read on positioning; concentrated venue availability means execution risk and funding volatility are elevated, and de-listing/liquidity-migration risk should be factored into sizing.

### Applicable strategies

- [[funding-rate-harvest]] — the Binance USD-M perp lets you collect funding when TOWNS funding runs persistently positive/negative, delta-hedging with spot.
- [[crowded-long-funding-fade]] — post-airdrop micro-caps like TOWNS often see reflexive long crowding; fade extended positive funding when OI spikes.
- [[liquidation-cascade-fade]] — thin depth makes TOWNS prone to cascading liquidations; fade the overshoot once the liquidation flush exhausts.
- [[oi-price-exhaustion]] — divergences between rising open interest and stalling price flag exhaustion in a low-float name.
- [[volatility-breakout]] — low-priced, low-cap TOWNS produces sharp expansion moves; trade confirmed breakouts from compression.
- [[range-mean-reversion]] — outside of catalysts TOWNS oscillates in tight ranges near its ATL, suiting reversion at range extremes.

### Volatility & regime character

Micro-cap SocialFi/L2 infra token with high reflexivity typical of recent Binance-airdrop names. Trades ~97% below its 2025 ATH and near all-time lows, so realized volatility is high and moves are dominated by low float and thin liquidity rather than fundamentals. High beta to broad crypto risk (BTC/ETH) on down-moves, with idiosyncratic pumps on Binance Alpha / listing-driven attention. Regime flips quickly between dead-range chop and violent expansion.

### Risk flags

- **Liquidity & venue concentration** — micro-cap with shallow books concentrated on a few CEXs; Binance is the dominant leveraged venue, creating single-venue dependence.
- **Unlocks / emissions** — large gap between circulating (~2.1B) and total/max supply (10.1B / 15.3B); ongoing emissions and unlocks are a structural sell-pressure and dilution risk.
- **Narrative dependence** — price hinges on SocialFi/airdrop attention and Binance Alpha spotlight flows rather than durable usage; narrative fade can drain liquidity fast.
- **Leverage fragility** — thin depth plus perp leverage makes TOWNS highly liquidation-cascade prone; funding can swing sharply.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=TOWNSUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=TOWNSUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=TOWNS` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=TOWNS` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=TOWNSUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=TOWNSUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=TOWNS"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

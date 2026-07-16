---
title: "Thena"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, defi, altcoins, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["THE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://thena.fi/"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# Thena

**Thena** (THE) is a cryptocurrency. It ranks **#1315** by market capitalization. Inspired by the vote-escrow model from Curve and the anti-dilution mechanism from Olympus, veTHE holders control 100% of Thena’s emissions allocated to gauges and benefit from weekly rebases, reducing dilution from emissions over time.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | THE |
| **Market Cap Rank** | #1315 |
| **Market Cap** | $7.48M |
| **Current Price** | $0.0555 |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), Perpetuals, Binance HODLer Airdrops |
| **Website** | [https://thena.fi/](https://thena.fi/) |

---

## Overview

Inspired by the vote-escrow model from Curve and the anti-dilution mechanism from Olympus, veTHE holders control 100% of Thena’s emissions allocated to gauges and benefit from weekly rebases, reducing dilution from emissions over time. THE Model rewards long-term supporters, and aligns stakeholders interests by incentivizing fee generation.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 134.79M THE |
| **Total Supply** | 286.27M THE |
| **Max Supply** | 326.12M THE |
| **Fully Diluted Valuation** | $15.89M |
| **Market Cap / FDV Ratio** | 0.47 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $4.03 (2024-11-27) |
| **Current vs ATH** | -98.62% |
| **All-Time Low** | $0.0459 (2026-07-01) |
| **Current vs ATL** | +21.17% |
| **24h Change** | +1.57% |
| **7d Change** | -17.17% |
| **30d Change** | -19.90% |
| **1y Change** | -88.08% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xf4c8e32eadec4bfe97e0f595add0f4450a863a11` |
| Opbnb | `0x9d94a7ff461e83f161c8c040e78557e31d8cba72` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | THE/TRY | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://thena.fi/](https://thena.fi/) |
| **Twitter** | [@ThenaFi_](https://twitter.com/ThenaFi_) |
| **Telegram** | [Thena_Fi](https://t.me/Thena_Fi) (11,570 members) |
| **Discord** | [https://discord.gg/thena](https://discord.gg/thena) |
| **GitHub** | [https://github.com/ThenafiBNB/THENA-Contracts](https://github.com/ThenafiBNB/THENA-Contracts) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 31 |
| **GitHub Forks** | 48 |
| **Pull Requests Merged** | 11 |
| **Contributors** | 1 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $6.61M |
| **Market Cap Rank** | #1315 |
| **24h Range** | $0.0546 — $0.0586 |
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

THE is tradable on **Binance** — both **spot** and a **USD-margined (USDT) perpetual** with funding, open interest, and liquidation data. It is **NOT** listed on Hyperliquid, so Binance is the primary leveraged venue and the reference market for price discovery. Because leveraged flow is concentrated on a single perp venue, funding, open interest, and liquidation prints are effectively Binance-driven; there is no deep cross-venue perp market to diffuse crowding. With a small market cap (~#1318) and thin 24h volume, spot order books are shallow — position sizing should stay small relative to visible depth, and execution should favor limit/VWAP-style fills over aggressive market orders to avoid slippage and self-inflicted liquidation risk. Cross-exchange or spot-vs-perp arbitrage is feasible mainly against the Binance spot pair.

### Applicable strategies

- [[funding-rate-harvest]] — single-venue Binance THE perp means funding swings can be persistent; a delta-neutral spot-long / perp-short harvest captures elevated funding when longs crowd the only leveraged market.
- [[crowded-long-funding-fade]] — with leverage concentrated on one venue, over-extended long funding on THE is a clean signal to fade froth after upside spikes.
- [[cash-and-carry]] — hold Binance spot THE against a short perp to lock the basis; the small-cap, single-venue structure often produces exploitable spot-perp spreads.
- [[liquidation-cascade-fade]] — thin liquidity makes THE prone to sharp liquidation flushes; fading the overshoot after a forced-selling cascade targets the snap-back.
- [[rsi-mean-reversion]] — a beaten-down small-cap (far below ATH) that whipsaws inside ranges suits oscillator-based reversion entries at stretched extremes.
- [[breakout-and-retest]] — low float and narrative-driven bursts give THE explosive breakouts; entering on the retest filters false moves in a low-liquidity name.

### Volatility & regime character

THE is a **small-cap DeFi / DEX infrastructure token** on BNB Chain with high realized volatility and strong reflexivity — low float and thin books amplify moves in both directions. It trades with high beta to broad crypto risk sentiment and to BTC/ETH direction, but idiosyncratic DeFi/BNB-ecosystem narratives and ve-tokenomics dynamics can dominate short-term price action. Expect regime shifts between quiet, range-bound drift and sharp momentum bursts on catalysts.

### Risk flags

- **Liquidity & venue concentration** — Binance is effectively the only meaningful CEX venue for spot and the sole perp venue; a listing/delisting change or venue outage would materially impair exit liquidity.
- **Emissions & unlock supply** — MC/FDV ratio well below 1 with ongoing gauge emissions and a max supply above circulating means persistent dilution/unlock pressure to monitor.
- **Narrative dependence** — price is sensitive to DeFi/DEX and BNB-ecosystem narrative cycles; momentum can reverse quickly when the narrative fades.
- **Small-cap fragility** — shallow depth makes THE vulnerable to slippage, stop-runs, and liquidation cascades; size conservatively and use hard risk limits.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=THEUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=THEUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=THE` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=THE` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=THEUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=THEUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=THE"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

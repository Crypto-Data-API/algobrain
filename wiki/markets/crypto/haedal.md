---
title: "Haedal Protocol"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, defi, altcoins, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["HAEDAL"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.haedal.xyz/"
related: ["[[crypto-markets]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]", "[[oi-confirmed-trend]]"]
---

# Haedal Protocol

**Haedal Protocol** (HAEDAL) is a Decentralized Finance (DeFi), BNB Chain Ecosystem, Liquid Staking Governance Tokens, Liquid Staking, Binance Alpha Spotlight project. It ranks **#1881** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | HAEDAL |
| **Market Cap Rank** | #1881 |
| **Market Cap** | $3.14M |
| **Current Price** | $0.0161 |
| **Categories** | Decentralized Finance (DeFi), Liquid Staking Governance Tokens, Liquid Staking, Binance Alpha Spotlight |
| **Website** | [https://www.haedal.xyz/](https://www.haedal.xyz/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 195.00M HAEDAL |
| **Total Supply** | 1.00B HAEDAL |
| **Max Supply** | 1.00B HAEDAL |
| **Fully Diluted Valuation** | $16.09M |
| **Market Cap / FDV Ratio** | 0.20 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.3003 (2025-07-17) |
| **Current vs ATH** | -94.65% |
| **All-Time Low** | $0.0154 (2026-06-26) |
| **Current vs ATL** | +4.08% |
| **24h Change** | -0.52% |
| **7d Change** | -1.21% |
| **30d Change** | -17.78% |
| **1y Change** | -92.47% |

---

## Platform & Chain Information

**Native Chain:** Sui

### Contract Addresses

| Chain | Address |
|---|---|
| Sui | `0x3a304c7feba2d819ea57c3542d68439ca2c386ba02159c740f7b406e592c62ea::haedal::HAEDAL` |
| Binance Smart Chain | `0x3d9be0ac1001cd81c32464276d863d2ffdca4967` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | HAEDAL/USDT | N/A |
| Upbit | HAEDAL/BTC | N/A |
| Bitget | HAEDAL/USDT | N/A |
| KuCoin | HAEDAL/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.haedal.xyz/](https://www.haedal.xyz/) |
| **Twitter** | [@haedalprotocol](https://twitter.com/haedalprotocol) |
| **Discord** | [https://discord.com/invite/haedalprotocol](https://discord.com/invite/haedalprotocol) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.09M |
| **Market Cap Rank** | #1881 |
| **24h Range** | $0.0160 — $0.0165 |
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

HAEDAL is tradable on **Binance** as both a spot pair (HAEDAL/USDT) and a **USD-margined perpetual**, which exposes live funding, open interest, and liquidation data — the core inputs for derivatives strategies. It is **NOT listed on Hyperliquid**, so Binance is the primary (and effectively sole major) leveraged venue. With a sub-$5M market cap and roughly $1M in daily spot volume, book depth is thin: leverage should be kept modest, position sizing conservative, and execution should lean on limit orders or TWAP/VWAP slicing to avoid slippage and self-inflicted liquidations. Venue concentration on Binance also means funding and basis signals derive from a single order book, so cross-exchange dispersion is limited and slippage risk on exits is elevated.

### Applicable strategies

- [[funding-rate-harvest]] — a low-cap alt like HAEDAL frequently prints persistently skewed perp funding; collecting the funding while delta-hedging spot can be a repeatable edge.
- [[crowded-long-funding-fade]] — thin liquidity makes HAEDAL prone to leveraged long crowding into bounces; fade the crowd when funding spikes richly positive.
- [[liquidation-cascade-fade]] — its small book means leverage flushes overshoot hard, so fading the wick after a cascade offers mean-reversion into fair value.
- [[oi-confirmed-trend]] — pairing Binance open-interest expansion with HAEDAL price moves helps separate genuine trend from low-liquidity noise.
- [[cash-and-carry]] — when the perp trades at a rich premium to spot, a long-spot / short-perp carry captures basis on this Binance-only pair.
- [[breakout-and-retest]] — deeply discounted near its ATL, HAEDAL trades in tight ranges; breakout-and-retest structures the low-volume range expansions.

### Volatility & regime character

HAEDAL is a small-cap DeFi/liquid-staking governance token (Sui-native, also bridged to BNB Chain) with high-beta, reflexive price behavior typical of low-float alts. It is down heavily from its ATH and sits near its ATL, so realized volatility is regime-dependent: quiet, low-volume drift punctuated by sharp leverage-driven spikes. Directional beta to BTC/ETH is high during risk-on/risk-off swings, but idiosyncratic moves are dominated by narrative flows (liquid staking, Sui ecosystem, Binance Alpha spotlight) and thin-book mechanics rather than macro correlation.

### Risk flags

- **Liquidity & venue concentration** — very low market cap and volume, with Binance as the only major leveraged venue; slippage and gap risk on exits are material.
- **Emissions / supply overhang** — circulating supply (~195M) is a small fraction of the 1B max supply (MC/FDV ~0.20), implying substantial future unlocks/emissions that can pressure price.
- **Narrative dependence** — valuation is tied to liquid-staking and Sui-ecosystem sentiment plus Binance Alpha attention; fading narratives can drain liquidity quickly.
- **Reflexivity** — thin books make the token vulnerable to liquidation cascades and stop runs; keep leverage low and stops wide enough to survive noise.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=HAEDALUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=HAEDALUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=HAEDAL` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=HAEDAL` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=HAEDALUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=HAEDALUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=HAEDAL"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

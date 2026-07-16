---
title: "Unstable Coin"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, memecoins, altcoins]
aliases: ["USDUC"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.usduc.io/"
related: ["[[crypto-markets]]", "[[solana]]", "[[binance]]", "[[breakout-trading]]", "[[meme-coin-cycle]]"]
---

# Unstable Coin

**Unstable Coin** (USDUC) is a Solana Ecosystem, Meme, Ethereum Ecosystem, Base Ecosystem, Solana Meme, Base Meme, Pump.fun Ecosystem, HyperEVM Ecosystem, Base Native project. It ranks **#1631** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDUC |
| **Market Cap Rank** | #1631 |
| **Market Cap** | $4.50M |
| **Current Price** | $0.00449715 |
| **Categories** | Meme, Solana Meme, Base Meme, Base Native |
| **Website** | [https://www.usduc.io/](https://www.usduc.io/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 999.89M USDUC |
| **Total Supply** | 999.89M USDUC |
| **Max Supply** | 1.00B USDUC |
| **Fully Diluted Valuation** | $4.50M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0745 (2025-09-01) |
| **Current vs ATH** | -93.85% |
| **All-Time Low** | $0.00113082 (2026-04-07) |
| **Current vs ATL** | +305.10% |
| **24h Change** | +2.93% |
| **7d Change** | +11.26% |
| **30d Change** | -7.39% |
| **1y Change** | -45.14% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `CB9dDufT3ZuQXqqSfa1c5kY935TEreyBw9XJXxHKpump` |
| Ethereum | `0xecedb6f8108b9f7bbf499da843dced6c2bb6e270` |
| Base | `0xecedb6f8108b9f7bbf499da843dced6c2bb6e270` |
| Hyperevm | `0x61ef9543f8919bb06e374b3bb58a17725e34f9d9` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | USDUC/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | CB9DDUFT3ZUQXQQSFA1C5KY935TEREYBW9XJXXHKPUMP/SO11111111111111111111111111111111111111112 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.usduc.io/](https://www.usduc.io/) |
| **Twitter** | [@usduc_official](https://twitter.com/usduc_official) |
| **Telegram** | [USDUC_safeguard](https://t.me/USDUC_safeguard) (482 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $891,873.00 |
| **Market Cap Rank** | #1631 |
| **24h Range** | $0.00434344 — $0.00468858 |
| **CoinGecko Sentiment** | 0% positive |
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

Tradable on Binance SPOT only — no liquid perpetual venue, so leverage/short access is limited and this is a spot-primary asset. Perp funding/basis/liquidation strategies do NOT apply. With a single primary CEX venue and a thin market-cap-rank ~1628 float, order-book depth is shallow: large market orders will move price and slippage rises quickly. Size positions small, favor limit/maker fills over aggressive taker orders, and expect execution to be spot-directional only (no built-in short leg or leverage). Venue concentration also means listing/delisting or liquidity migrations on Binance can dominate tradability.

### Applicable strategies

- [[breakout-trading]] — USDUC is a low-cap memecoin prone to sharp reflexive rallies off a base; clean breakouts above consolidation offer defined spot entries.
- [[volatility-breakout]] — high intraday range relative to cap makes ATR/volatility-expansion triggers well suited to catching impulsive moves.
- [[dca-strategy]] — for a spot-only, deeply drawn-down (>90% off ATH) memecoin, scaling in over time smooths the volatile, uncertain price path without leverage.
- [[range-trading]] — between narrative catalysts USDUC often oscillates in a band; fading the edges of the established range suits its spot-primary profile.
- [[atr-trailing-stop]] — with no short/leverage hedge available, an ATR-based trailing stop is the primary way to protect spot gains during volatile swings.
- [[meme-coin-cycle]] — as a Solana/Base meme token, its price is driven by hype/rotation cycles that this playbook is built to trade.

### Volatility & regime character

Micro-cap (rank ~1628, ~$4-5M cap) memecoin with high reflexivity: moves are sentiment- and narrative-driven rather than fundamental, producing large percentage swings on low absolute liquidity. As a Solana/Base/Ethereum meme asset it tends to have elevated beta to the broader memecoin and Solana-ecosystem risk appetite, and correlation to BTC/ETH mainly appears through overall crypto risk-on/risk-off regimes; in idiosyncratic hype phases it can decouple entirely from majors.

### Risk flags

- Liquidity/venue concentration: spot-only, single primary CEX (Binance) plus DEX pools — thin depth, high slippage, and delisting/liquidity-migration risk.
- Narrative dependence: value is driven by meme/hype cycles and social momentum; catalysts fade fast and drawdowns can be severe (already >90% below ATH).
- Supply/emissions: near-fully-circulating (~1B max supply) reduces unlock overhang, but concentrated holder distribution raises whale-dump risk.
- No hedge tooling: absence of a liquid perpetual venue means no easy shorting or leverage-based hedging — risk must be managed via sizing and stops.
- Regulatory: memecoins face heightened regulatory and platform-listing scrutiny that can abruptly impair venue access.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=USDUCUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=USDUCUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=USDUCUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=USDUCUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

---
title: "Viction"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins, defi]
aliases: ["VIC"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "https://viction.xyz/"
related: ["[[crypto-markets]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]"]
---

# Viction

**Viction** (VIC) is a Smart Contract Platform, Masternodes, Layer 1 (L1), DWF Labs Portfolio project. It ranks **#1595** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | VIC |
| **Market Cap Rank** | #1595 |
| **Market Cap** | $4.87M |
| **Current Price** | $0.0382 |
| **Genesis Date** | 2018-02-28 |
| **Categories** | Smart Contract Platform, Masternodes, Layer 1 (L1) |
| **Website** | [https://viction.xyz/](https://viction.xyz/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 127.31M VIC |
| **Total Supply** | 210.00M VIC |
| **Max Supply** | 210.00M VIC |
| **Fully Diluted Valuation** | $8.03M |
| **Market Cap / FDV Ratio** | 0.61 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.88 (2021-09-06) |
| **Current vs ATH** | -99.01% |
| **All-Time Low** | $0.0318 (2026-06-10) |
| **Current vs ATL** | +20.31% |
| **24h Change** | -1.09% |
| **7d Change** | -4.25% |
| **30d Change** | +4.34% |
| **1y Change** | -86.72% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | VIC/USDT | N/A |
| Bitget | VIC/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://viction.xyz/](https://viction.xyz/) |
| **Twitter** | [@BuildOnViction](https://twitter.com/BuildOnViction) |
| **Telegram** | [buildonviction](https://t.me/buildonviction) (4,195 members) |
| **Discord** | [https://discord.com/invite/vCEJV44knr](https://discord.com/invite/vCEJV44knr) |
| **GitHub** | [https://github.com/BuildOnViction](https://github.com/BuildOnViction) |
| **Whitepaper** | [https://tomochain.com/docs/technical-whitepaper--1.0.pdf](https://tomochain.com/docs/technical-whitepaper--1.0.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 47 |
| **GitHub Forks** | 56 |
| **Pull Requests Merged** | 503 |
| **Contributors** | 9 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $407,725.00 |
| **Market Cap Rank** | #1595 |
| **24h Range** | $0.0382 — $0.0394 |
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

VIC is tradable on **Binance** — both **spot** (VIC/USDT) and a **USD-margined perpetual** exposing funding, open interest, and liquidation flow. It is **NOT** listed on Hyperliquid, so Binance is the primary (effectively sole major) leveraged venue. With a sub-$5M market cap and thin ~$400K daily spot volume, VIC is a deep-microcap: the perp order book is shallow relative to majors, so meaningful leverage can move price and trigger cascades quickly. Practically, venue concentration means execution and sizing must assume wide slippage, low fill depth, and that both hedging and price discovery route through Binance — position sizes should be scaled down and worked patiently rather than taken at market.

### Applicable strategies

- [[liquidation-cascade-fade]] — thin VIC perp depth lets leveraged flushes overshoot; fading forced-liquidation spikes back toward spot can capture the snap-back.
- [[post-liquidation-rebound]] — after a long-liquidation cascade in a microcap this illiquid, mean-reversion bounces are pronounced and tradable.
- [[funding-rate-harvest]] — Binance USD-M funding on a low-cap alt can run persistently skewed, letting a delta-neutral spot-vs-perp position collect the carry.
- [[crowded-long-funding-fade]] — reflexive retail longs on a decayed microcap frequently overcrowd, so fading extreme positive funding is a repeatable edge.
- [[rsi-mean-reversion]] — low float and erratic swings around the ATL make oscillator-based reversion effective inside VIC's choppy range.
- [[breakout-and-retest]] — with tiny liquidity, genuine range breaks are rare but clean; requiring a retest filters the many false moves.

### Volatility & regime character

Deep small-cap / microcap L1 (#1595, ~$4.9M cap) with high idiosyncratic volatility and elevated beta to BTC/ETH risk-on/off swings. As a low-float, low-liquidity token trading near its all-time low (down ~99% from ATH), price action is reflexive and prone to sharp, sentiment-driven spikes on thin volume rather than smooth trends. Behaves as an infra/L1 altcoin: correlated to broad crypto beta but amplified, with occasional dislocations from its own low liquidity and DWF-Labs-associated flow.

### Risk flags

- **Liquidity & venue concentration** — very thin volume and reliance on Binance as the sole major leveraged venue; delisting or liquidity withdrawal would be severe, and slippage/gap risk is high.
- **Supply overhang** — max supply 210M vs ~127M circulating (MC/FDV ~0.61) leaves meaningful emission/unlock dilution ahead.
- **Microcap fragility** — sub-$5M cap makes VIC easy to move, manipulate, or squeeze; leveraged positions face outsized liquidation risk.
- **Narrative dependence** — a legacy rebrand (TomoChain to Viction) with limited current mindshare; price hinges on renewed narrative or market-maker interest rather than durable demand.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=VICUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=VICUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=VIC` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=VIC` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=VICUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=VICUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=VIC"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

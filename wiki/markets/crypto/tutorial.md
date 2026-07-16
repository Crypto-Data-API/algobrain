---
title: "Tutorial"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, memecoins, altcoins]
aliases: ["TUT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://tutorialtoken.com"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]", "[[meme-coin-cycle]]"]
---

# Tutorial

**Tutorial** (TUT) is a token from a dev who made a tutorial on how to launch token on BNB chain 10 month ago, the OG Tutorial token was on testnet, so he decided to launch it on mainnet as a meme. 

The purpose of the project is to promote building on bsc and making useful education content. It ranks **#1139** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TUT |
| **Market Cap Rank** | #1139 |
| **Market Cap** | $10.46M |
| **Current Price** | $0.0125 |
| **Categories** | Meme, AI Meme, AI Agents |
| **Website** | [https://tutorialtoken.com](https://tutorialtoken.com) |

---

## Overview

Tutorial is a token from a dev who made a tutorial on how to launch token on BNB chain 10 month ago, the OG Tutorial token was on testnet, so he decided to launch it on mainnet as a meme. 

The purpose of the project is to promote building on bsc and making useful education content. 
The project was originally created on four.meme and liquidity was transferred to pancakeswap as bonding curve criteria was met.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 834.04M TUT |
| **Total Supply** | 834.04M TUT |
| **Max Supply** | 1.00B TUT |
| **Fully Diluted Valuation** | $10.46M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1697 (2025-09-20) |
| **Current vs ATH** | -92.61% |
| **All-Time Low** | $0.00028993 (2025-02-13) |
| **Current vs ATL** | +4228.34% |
| **24h Change** | +0.73% |
| **7d Change** | +27.32% |
| **30d Change** | +17.21% |
| **1y Change** | -79.96% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | TUT/USDT | N/A |
| Bitget | TUT/USDT | N/A |
| KuCoin | TUT/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://tutorialtoken.com](https://tutorialtoken.com) |
| **Twitter** | [@tutorialtoken](https://twitter.com/tutorialtoken) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.37M |
| **Market Cap Rank** | #1139 |
| **24h Range** | $0.0124 — $0.0133 |
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

TUT is tradable on **Binance** — both **spot** (TUT/USDT) and a **USD-margined perpetual** with the associated derivatives plumbing (funding, open interest, liquidations). It is **NOT** listed on Hyperliquid, so Binance is the **primary leveraged venue** and the reference market for price discovery on the perp. Secondary spot liquidity exists on Bitget and KuCoin, plus on-chain via PancakeSwap on BNB Chain. With a ~#1137 market-cap rank and only a few million dollars in daily volume, order books are thin: leverage is available but effective size is small, funding can swing hard, and liquidation clusters on the single dominant perp venue can move price disproportionately. Because Binance is the sole deep leveraged venue, execution and position sizing should assume elevated slippage on market orders, wider stops, and that most cross-venue basis/arbitrage must be spot-vs-Binance-perp rather than perp-vs-perp.

### Applicable strategies

- [[funding-rate-harvest]] — with a single dominant Binance perp and a reflexive memecoin, funding often runs persistently one-sided, letting a spot-vs-perp hedge harvest the carry.
- [[crowded-long-funding-fade]] — retail-driven meme rallies in TUT tend to crowd longs and push funding to extremes, setting up a fade of overheated positioning.
- [[liquidation-cascade-fade]] — thin books on the lone Binance perp make forced-liquidation wicks sharp and mean-reverting, favoring fading the flush.
- [[cash-and-carry]] — when the perp trades at a rich premium, long Binance spot / short the perp captures basis without directional exposure.
- [[meme-coin-cycle]] — TUT is an AI-meme launched from a tutorial gag, so its price action follows narrative-driven meme rotation more than fundamentals.
- [[volatility-breakout]] — low-float memecoins like TUT spend long stretches ranging then break violently on attention spikes, rewarding volatility-triggered entries.

### Volatility & regime character

TUT is a **small-cap memecoin** (AI-meme / AI-agent category) with high reflexivity: price is driven by attention, social momentum, and narrative rotation rather than cash flows. Realized volatility is high, with a low free float relative to a 1B max supply. As a low-cap alt it carries **high beta to BTC/ETH** in risk-off moves (it sells off hard when majors drop) but decouples to the upside during meme/narrative pumps. Expect regime alternation between quiet, illiquid ranges and violent expansion moves around catalysts.

### Risk flags

- **Liquidity & venue concentration** — leveraged trading concentrated on a single Binance perp; thin spot books mean slippage and gap risk, and a Binance delisting or halt would remove the primary venue.
- **Supply / emissions** — circulating supply (~834M) is below the 1B max supply, so future minting/unlocks toward max could add sell pressure; MC/FDV is currently ~1.0.
- **Narrative dependence** — value rests on meme/AI-agent narrative and BNB-chain building sentiment; attention fade can drain liquidity quickly.
- **Reflexivity & drawdown** — trades ~90%+ below its ATH with a history of extreme swings; leveraged positions face rapid liquidation risk in cascades.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=TUTUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=TUTUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=TUT` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=TUT` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=TUTUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=TUTUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=TUT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

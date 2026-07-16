---
title: "Sapien"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["SAPIEN"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.sapien.io/"
related: ["[[crypto-markets]]", "[[base]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[oi-confirmed-trend]]", "[[liquidation-cascade-fade]]"]
---

# Sapien

**Sapien** (SAPIEN) is an open protocol for sourcing verified human knowledge at scale. Its network of millions of contributors spans more than 100 countries, ranging from doctors and engineers to artists and students. It ranks **#814** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SAPIEN |
| **Market Cap Rank** | #814 |
| **Market Cap** | $20.24M |
| **Current Price** | $0.082729 |
| **Categories** | Artificial Intelligence (AI), Infrastructure, Base Ecosystem, Governance, Base Native |
| **Website** | [https://www.sapien.io/](https://www.sapien.io/) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Overview

Sapien is an open protocol for sourcing verified human knowledge at scale. Its network of millions of contributors spans more than 100 countries, ranging from doctors and engineers to artists and students. Together they produce high-quality AI training data, validated through Sapien’s onchain Proof of Quality system. This ensures enterprises and AI developers can access trusted, human-in-the-loop data while transforming fragmented online work into a sustainable, reputation-based profession. Incentives across the network are powered by the $SAPIEN token, an ERC-20 asset on Base.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 250.00M SAPIEN |
| **Total Supply** | 1.00B SAPIEN |
| **Max Supply** | 1.00B SAPIEN |
| **Fully Diluted Valuation** | $69.58M |
| **Market Cap / FDV Ratio** | 0.25 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.5364 (2025-11-06) |
| **Current vs ATH** | -87.02% |
| **All-Time Low** | $0.0627 (2026-03-29) |
| **Current vs ATL** | +11.00% |
| **24h Change** | -0.14% |
| **7d Change** | +3.97% |
| **30d Change** | -5.87% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Base

### Contract Addresses

| Chain | Address |
|---|---|
| Base | `0xc729777d0470f30612b1564fd96e8dd26f5814e3` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SAPIEN/USDT | N/A |
| Kraken | SAPIEN/USD | N/A |
| Bitget | SAPIEN/USDT | N/A |
| KuCoin | SAPIEN/USDT | N/A |
| Crypto.com Exchange | SAPIEN/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.sapien.io/](https://www.sapien.io/) |
| **Twitter** | [@joinsapien](https://twitter.com/joinsapien) |
| **Telegram** | [SapienCommunity](https://t.me/SapienCommunity) (123,869 members) |
| **Discord** | [https://discord.com/invite/sapien](https://discord.com/invite/sapien) |
| **Whitepaper** | [https://docs.sapien.io/](https://docs.sapien.io/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.23M |
| **Market Cap Rank** | #814 |
| **24h Range** | $0.0680 — $0.0703 |
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

SAPIEN is tradable on **Binance** — both spot (SAPIEN/USDT) and a USD-margined perpetual, which exposes funding rates, open interest, and liquidation data. It is **not listed on Hyperliquid**, so Binance is the primary leveraged venue. With a small ~$20M market cap and modest 24h volume, order books are thin: perp leverage concentrates flow on a single exchange, so funding and liquidation signals are meaningful but liquidity is easily exhausted. Size positions conservatively, favor limit/maker execution to reduce slippage, and expect wider spreads and greater impact than large-caps. Venue concentration means Binance perp availability effectively defines where directional and carry trades can be structured.

### Applicable strategies

- [[oi-confirmed-trend]] — pair Binance perp open-interest changes with price to confirm genuine trend continuation versus low-conviction chop in a thin book.
- [[funding-rate-harvest]] — collect funding on the SAPIEN perp when the rate skews persistently positive or negative, sized for the low-cap liquidity.
- [[liquidation-cascade-fade]] — fade forced-liquidation flushes on the leveraged perp, where a small cap amplifies cascade magnitude and mean-reversion snapbacks.
- [[breakout-and-retest]] — trade breakouts from consolidation with a retest filter, appropriate for a low-liquidity AI/data token prone to false starts.
- [[narrative-trading]] — position around the AI-training-data / verified-human-knowledge narrative that drives SAPIEN's episodic attention and volume.
- [[volatility-breakout]] — capture expansion moves after quiet ranges, common in small-cap tokens that whipsaw on catalysts.

### Volatility & regime character

Small-cap (rank ~835), high-beta altcoin with pronounced reflexivity typical of low-float, low-liquidity assets. As an AI/infrastructure token on Base (0.25 MC/FDV ratio), SAPIEN tends to amplify BTC/ETH directional moves during risk-on phases and sell off sharply in risk-off regimes, while adding idiosyncratic swings driven by AI-data narrative flows and thin order books. Expect elevated realized volatility and sensitivity to broad altcoin sentiment.

### Risk flags

- **Liquidity / venue concentration** — thin books and a single dominant leveraged venue (Binance) mean slippage, gap risk, and cascade risk on de-risking events.
- **Unlocks / emissions** — circulating supply (250M) is a fraction of the 1B total/max supply (0.25 MC/FDV), so scheduled emissions and future unlocks are a persistent supply overhang.
- **Narrative dependence** — valuation leans on the AI-training-data thesis; attention rotation away from the AI narrative can drain volume and liquidity quickly.
- **Small-cap fragility** — low market cap makes the token vulnerable to outsized swings from relatively small order flow and to broad altcoin regime shifts.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=SAPIENUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=SAPIENUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=SAPIEN` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=SAPIEN` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=SAPIENUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=SAPIENUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=SAPIEN"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[base]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

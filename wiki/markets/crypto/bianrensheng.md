---
title: "币安人生 (BinanceLife)"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, memecoins, altcoins]
aliases: ["币安人生"]
entity_type: protocol
headquarters: "Decentralized"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[meme-coin-cycle]]"]
---

# 币安人生 (BinanceLife)

**币安人生 (BinanceLife)** (币安人生) is a BNB Chain Ecosystem, Meme, Binance Alpha Spotlight, Chinese Meme, Four.meme Ecosystem (BNB Memes) project. It ranks **#86** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | 币安人生 |
| **Market Cap Rank** | #86 |
| **Market Cap** | $668.60M |
| **Current Price** | $0.668857 |
| **Categories** | BNB Chain Ecosystem, Meme, Binance Alpha Spotlight, Chinese Meme, Four.meme Ecosystem (BNB Memes) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.00B 币安人生 |
| **Total Supply** | 1.00B 币安人生 |
| **Max Supply** | 1.00B 币安人生 |
| **Fully Diluted Valuation** | $79.69M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.5108 (2025-10-08) |
| **Current vs ATH** | -84.41% |
| **All-Time Low** | $0.0384 (2026-03-29) |
| **Current vs ATL** | +107.18% |
| **24h Change** | +13.01% |
| **7d Change** | +65.33% |
| **30d Change** | +24.70% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0x924fa68a0fc644485b8df8abfa0a41c2e7744444` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | 币安人生/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Twitter** | [@BinanceLife_](https://twitter.com/BinanceLife_) |
| **Telegram** | [BinanceLife_token](https://t.me/BinanceLife_token) (10,761 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $72.34M |
| **Market Cap Rank** | #86 |
| **24h Range** | $0.0674 — $0.1048 |
| **CoinGecko Sentiment** | 83% positive |
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

币安人生 is tradable on **Binance** — both spot (币安人生/USDT) and USD-margined perpetual futures, which surface funding, open interest, and liquidation data. It is **NOT listed on Hyperliquid**, so Binance is the primary and effectively sole leveraged venue. This concentration means all discoverable derivatives signal (funding rate, OI, liq clusters) comes from one exchange, so there is no cross-venue funding dislocation to arbitrage against a decentralized perp market. Leverage is available but liquidity depth is thinner than for majors; execution should assume wider slippage on size, and position sizing should account for single-venue liquidity risk and the outsized impact of Binance-side funding resets on a small-cap memecoin book.

### Applicable strategies

- [[funding-rate-harvest]] — single-venue Binance perp funding on a hot Chinese memecoin can run persistently rich during rallies, letting a delta-neutral spot-long / perp-short harvest the premium.
- [[crowded-long-funding-fade]] — sharp +65% weekly moves attract crowded longs; fading extreme positive funding on 币安人生 captures the mean-reversion when leverage over-extends.
- [[long-liquidation-cascade]] — thin single-venue liquidity plus high memecoin leverage makes 币安人生 prone to downside liquidation cascades that can be traded on the break.
- [[post-liquidation-rebound]] — after a forced-liquidation flush, the low float and reflexive meme demand often snap price back, offering a rebound entry.
- [[meme-coin-cycle]] — as a Four.meme / Binance Alpha Spotlight Chinese meme, 币安人生 trades on the classic meme hype-to-decay cycle rather than fundamentals.
- [[breakout-and-retest]] — momentum-driven meme moves produce clean range breaks; entering on the retest of a broken level manages the elevated whipsaw risk.

### Volatility & regime character

Small/mid-cap memecoin (rank ~85) with high reflexivity typical of the Four.meme / BNB Chain meme cohort. Price action is narrative- and sentiment-driven rather than fundamental, with violent multi-day swings (24h +13%, 7d +65%) and deep drawdowns from ATH. Beta to BTC/ETH is loose in calm regimes but correlation spikes to the downside during broad crypto risk-off. As a BNB-ecosystem token it also carries idiosyncratic sensitivity to BNB Chain and Binance-specific flow and sentiment.

### Risk flags

- **Venue concentration** — liquidity and all leveraged/derivatives exposure sit on Binance alone; a single-venue liquidity shock or listing change is a concentrated risk.
- **Narrative dependence** — value is driven almost entirely by meme/hype cycles and Binance Alpha Spotlight attention; demand can evaporate quickly.
- **Memecoin reflexivity** — thin float and leverage make it prone to violent squeezes and liquidation cascades in both directions.
- **Liquidity/slippage** — depth is far below majors; large orders move price and funding, complicating delta-neutral rebalancing.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=币安人生USDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=币安人生USDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=币安人生` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=币安人生` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=币安人生USDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=币安人生USDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=币安人生"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

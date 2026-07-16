---
title: "Vulcan Forged"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, nft, altcoins, defi]
aliases: ["PYR"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://vulcanforged.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[momentum-investing]]", "[[dca-strategy]]"]
---

# Vulcan Forged

**Vulcan Forged** (PYR) is a non-fungible token (NFT) game studio, marketplace and dApp incubator with multiple games and an active community of users. It ranks **#1513** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PYR |
| **Market Cap Rank** | #1513 |
| **Market Cap** | $5.43M |
| **Current Price** | $0.1251 |
| **Categories** | Gaming (GameFi), NFT, Metaverse, Gaming Blockchains, Gaming Platform, Action Games, MMO |
| **Website** | [https://vulcanforged.com/](https://vulcanforged.com/) |

---

## Overview

Vulcan Forged is a non-fungible token (NFT) game studio, marketplace and dApp incubator with multiple games and an active community of users.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 43.42M PYR |
| **Total Supply** | 50.00M PYR |
| **Max Supply** | 50.00M PYR |
| **Fully Diluted Valuation** | $6.25M |
| **Market Cap / FDV Ratio** | 0.87 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $49.24 (2021-12-01) |
| **Current vs ATH** | -99.75% |
| **All-Time Low** | $0.1216 (2026-07-09) |
| **Current vs ATL** | +1.98% |
| **24h Change** | -2.96% |
| **7d Change** | -1.38% |
| **30d Change** | -33.66% |
| **1y Change** | -87.78% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x430ef9263e76dae63c84292c3409d61c598e9682` |
| Polygon Pos | `0x430ef9263e76dae63c84292c3409d61c598e9682` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | PYR/USDT | N/A |
| KuCoin | PYR/USDT | N/A |
| Crypto.com Exchange | PYR/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X430EF9263E76DAE63C84292C3409D61C598E9682/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://vulcanforged.com/](https://vulcanforged.com/) |
| **Twitter** | [@VulcanForged](https://twitter.com/VulcanForged) |
| **Telegram** | [VeriArti](https://t.me/VeriArti) (3,510 members) |
| **Discord** | [https://discord.com/invite/ZyjTvFM](https://discord.com/invite/ZyjTvFM) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $6.48M |
| **Market Cap Rank** | #1513 |
| **24h Range** | $0.1233 — $0.1409 |
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

PYR is tradable on **Binance SPOT only** — there is no liquid perpetual venue, so leverage and short access are limited and this is a **spot-primary** asset. Perp funding, basis, and liquidation-driven strategies do **not** apply. With a sub-$10M market cap and volume concentrated on a single major venue, execution should assume thin depth: size positions small relative to visible order-book liquidity, prefer limit orders over market orders, and account for slippage and wider spreads. Venue concentration means Binance availability effectively defines tradability — a delisting or maintenance halt removes the primary exit, so position sizing and stop placement should be conservative.

### Applicable strategies

- [[momentum-investing]] — PYR is a low-cap GameFi token that trends hard in both directions; riding established momentum captures the reflexive moves without needing leverage.
- [[breakout-and-retest]] — with a tight 24h range and low float, clean breaks above range highs followed by a retest offer defined-risk spot entries.
- [[dca-strategy]] — for conviction accumulation deep in a multi-year drawdown, averaging in spreads single-venue execution risk and smooths thin-liquidity fills.
- [[atr-trailing-stop]] — high realized volatility in a spot-only asset makes a volatility-scaled trailing stop essential for locking gains and capping downside without a perp hedge.
- [[narrative-trading]] — PYR price is heavily driven by GameFi/metaverse narrative cycles; positioning around sector sentiment shifts is a primary edge for this token.
- [[volatility-targeting]] — sizing to a volatility budget keeps risk constant across PYR's erratic swings, which is critical when hedging via perps is unavailable.

### Volatility & regime character

PYR is a **small-cap GameFi/metaverse infrastructure token** with high realized volatility and strong reflexivity typical of low-float gaming coins. It carries elevated high-beta exposure to broad crypto risk sentiment and is highly correlated to BTC/ETH direction during risk-on and risk-off swings, while idiosyncratic moves are dominated by GameFi/metaverse narrative rotation. In risk-off regimes, thin single-venue liquidity amplifies drawdowns; in narrative-driven rallies, the low float can produce outsized upside spikes.

### Risk flags

- **Liquidity/venue concentration** — spot-only on Binance with a small market cap; a single-venue delisting or halt would sharply impair exits.
- **Narrative dependence** — price is tightly tied to GameFi/metaverse sentiment cycles, which can fade quickly and leave the token illiquid.
- **Supply/emissions** — circulating supply is close to max supply, but any treasury or ecosystem distribution can still pressure a thin market.
- **Deep drawdown** — trades far below all-time high with weak longer-term trend; not a mean-reversion-to-ATH thesis, and low caps carry elevated failure/regulatory-scrutiny risk.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=PYRUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=PYRUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=PYRUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=PYRUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

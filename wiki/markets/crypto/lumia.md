---
title: "Lumia"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["LUMIA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://lumia.org/"
related: ["[[crypto-markets]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[momentum-investing]]", "[[liquidation-cascade-fade]]"]
---

# Lumia

**Lumia** (LUMIA) is a Smart Contract Platform, BNB Chain Ecosystem, Ethereum Ecosystem, Layer 2 (L2), Real World Assets (RWA), Governance project. It ranks **#1136** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LUMIA |
| **Market Cap Rank** | #1136 |
| **Market Cap** | $10.49M |
| **Current Price** | $0.0757 |
| **Categories** | Smart Contract Platform, Layer 2 (L2), Real World Assets (RWA), Governance |
| **Website** | [https://lumia.org/](https://lumia.org/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 138.50M LUMIA |
| **Total Supply** | 238.89M LUMIA |
| **Max Supply** | 238.89M LUMIA |
| **Fully Diluted Valuation** | $18.09M |
| **Market Cap / FDV Ratio** | 0.58 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2.49 (2024-12-04) |
| **Current vs ATH** | -96.98% |
| **All-Time Low** | $0.0550 (2026-02-28) |
| **Current vs ATL** | +37.02% |
| **24h Change** | +4.57% |
| **7d Change** | -40.41% |
| **30d Change** | -16.72% |
| **1y Change** | -76.21% |

---

## Platform & Chain Information

**Native Chain:** Multiple chains (see contract addresses below)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xd9343a049d5dbd89cd19dc6bca8c48fb3a0a42a7` |
| Binance Smart Chain | `0x7f39bcdca8e0e581c1d43aaa1cb862aa1c8c2047` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | LUMIA/TRY | N/A |
| KuCoin | LUMIA/USDT | N/A |
| Crypto.com Exchange | LUMIA/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://lumia.org/](https://lumia.org/) |
| **Twitter** | [@buildonlumia](https://twitter.com/buildonlumia) |
| **Telegram** | [lumia_community](https://t.me/lumia_community) (21,101 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $5.07M |
| **Market Cap Rank** | #1136 |
| **24h Range** | $0.0724 — $0.0763 |
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

LUMIA is tradable on [[binance]] — spot plus a USD-margined [[perpetual-futures|perpetual]] contract that carries [[funding-rate|funding]], [[open-interest]], and [[liquidations]] telemetry. It is NOT listed on Hyperliquid, so Binance is effectively the primary leveraged venue. With a market cap near rank #1136 and thin 24h volume, order books are shallow: the perp is the deepest place to express leveraged directional views, but position sizing must respect that a single venue concentrates both liquidity and liquidation risk. Slippage on spot is meaningful, so large entries/exits should be split, and stops should account for the fact that a cascade on the sole perp venue can move price faster than spot can absorb.

### Applicable strategies

- [[liquidation-cascade-fade]] — thin single-venue perp liquidity means forced-liquidation wicks on LUMIA overshoot fair value and mean-revert, offering fade entries.
- [[oi-confirmed-trend]] — rising Binance open interest alongside price confirms genuine leveraged participation versus a hollow move in an illiquid small-cap.
- [[momentum-investing]] — as a low-rank RWA/L2 token, LUMIA trends hard on narrative flows, rewarding momentum entries once direction is established.
- [[crowded-long-funding-fade]] — persistently positive perp funding flags crowded longs in a small float, setting up contrarian fade opportunities.
- [[breakout-and-retest]] — low float and tight ranges make clean breakouts from consolidation, then retests, tradable structures on LUMIA.
- [[range-mean-reversion]] — during quiet, news-free stretches the tight 24h range mean-reverts, favoring fading band extremes.

### Volatility & regime character

Small-cap (rank ~1136) infra/DeFi token spanning L2 and Real World Assets (RWA) narratives, with a low circulating-to-max-supply structure. Expect high, reflexive volatility: sharp narrative-driven pumps and equally sharp drawdowns (7d/30d/1y history shows deep negative moves off the ATH). High beta to BTC/ETH risk-on/risk-off swings, amplified by the small float; illiquidity makes realized volatility spiky rather than smooth.

### Risk flags

- Liquidity/venue concentration — Binance is the sole meaningful leveraged venue; a listing change or outage removes the primary hedging/exit path.
- Unlocks/emissions — Market Cap/FDV ratio near 0.58 implies a large uncirculated supply; scheduled token unlocks can pressure price.
- Narrative dependence — valuation leans on RWA and L2 storylines; sentiment reversals hit hard given the small cap.
- Thin order books — low 24h volume magnifies slippage and makes stops prone to wick-outs during volatility spikes.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=LUMIAUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=LUMIAUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=LUMIA` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=LUMIA` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=LUMIAUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=LUMIAUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=LUMIA"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

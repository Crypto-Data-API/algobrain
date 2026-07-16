---
title: "Heima"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["HEI"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.heima.network/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]", "[[token-unlock-supply-event]]"]
---

# Heima

**Heima** (HEI) is a BNB Chain Ecosystem, Binance Launchpool, Ethereum Ecosystem, YZi Labs (Prev. Binance Labs) Portfolio project. It ranks **#1148** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | HEI |
| **Market Cap Rank** | #1148 |
| **Market Cap** | $10.34M |
| **Current Price** | $0.1057 |
| **Categories** | Binance Launchpool |
| **Website** | [https://www.heima.network/](https://www.heima.network/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 97.76M HEI |
| **Total Supply** | 100.00M HEI |
| **Max Supply** | 100.00M HEI |
| **Fully Diluted Valuation** | $10.57M |
| **Market Cap / FDV Ratio** | 0.98 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.25 (2025-02-13) |
| **Current vs ATH** | -91.56% |
| **All-Time Low** | $0.0476 (2025-10-10) |
| **Current vs ATL** | +121.38% |
| **24h Change** | +2.45% |
| **7d Change** | -2.87% |
| **30d Change** | +47.25% |
| **1y Change** | -66.78% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xf8f173e20e15f3b6cb686fb64724d370689de083` |
| Binance Smart Chain | `0xf8f173e20e15f3b6cb686fb64724d370689de083` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | HEI/TRY | N/A |
| Bitget | HEI/USDT | N/A |
| KuCoin | HEI/USDT | N/A |
| Crypto.com Exchange | HEI/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.heima.network/](https://www.heima.network/) |
| **Twitter** | [@heimaNetwork](https://twitter.com/heimaNetwork) |
| **Telegram** | [heima_network](https://t.me/heima_network) (5,082 members) |
| **Discord** | [https://discord.gg/heima-network](https://discord.gg/heima-network) |
| **GitHub** | [https://github.com/litentry](https://github.com/litentry) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $14.92M |
| **Market Cap Rank** | #1148 |
| **24h Range** | $0.1006 — $0.1155 |
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

HEI is tradable on **Binance** — both **spot** and a **USD-margined perpetual** contract, which exposes funding, open interest, and liquidation data. It is **NOT listed on Hyperliquid**, so Binance is the primary leveraged venue. With a sub-$15M market cap and thin order books, leverage on the Binance perp can amplify both slippage and liquidation cascades; funding and OI on that single venue effectively define the derivatives picture. Because leveraged liquidity is concentrated on one exchange, execution should favor limit orders, staggered entries, and conservative position sizing — large market orders will move price disproportionately, and there is no secondary perp venue to hedge or arbitrage against directly.

### Applicable strategies

- [[funding-rate-harvest]] — collect funding on the Binance HEI perp when the low-float token trades at a persistent premium/discount, sizing small given thin liquidity.
- [[liquidation-cascade-fade]] — a low-cap, leverage-heavy perp is prone to sharp forced-liquidation wicks; fading the overshoot back toward spot can be productive.
- [[post-liquidation-rebound]] — after a cascade flushes leveraged longs on the single Binance venue, HEI often snaps back, offering a mean-reverting entry.
- [[volatility-breakout]] — HEI's high realized volatility and +47% 30d range make ATR-scaled breakouts from consolidation viable on the spot pair.
- [[token-unlock-supply-event]] — with circulating supply already ~98% of max, residual emissions/unlock schedules can trigger tradeable supply shocks.
- [[narrative-trading]] — as a BNB Chain / Binance Launchpool / YZi Labs (ex-Binance Labs) name, HEI reacts sharply to ecosystem and identity-DID narrative flow.

### Volatility & regime character

Small-cap (rank ~1147) altcoin with high reflexivity: sub-$15M market cap means low float and outsized percentage swings on modest flow. As a BNB Chain ecosystem / DID-infrastructure token, it carries beta to BTC/ETH broad-market risk but is dominated by idiosyncratic Binance-ecosystem and narrative catalysts. Expect wide intraday ranges, gap-prone behavior, and correlation that tightens in market-wide risk-off episodes while decoupling on token-specific news.

### Risk flags

- **Venue/liquidity concentration** — leveraged trading lives almost entirely on Binance; a single-venue outage, listing change, or funding spike has no offsetting perp market.
- **Low float / thin books** — small market cap and sub-$15M size make the book easy to move and vulnerable to liquidation cascades and manipulation.
- **Supply/unlock dynamics** — circulating supply near max supply limits future dilution but any residual emissions or team unlocks can pressure price.
- **Narrative dependence** — value is heavily tied to the Binance/BNB Chain ecosystem and DID narrative; sentiment reversals can be abrupt.
- **Regulatory** — as a DID/identity-adjacent token, evolving data/identity regulation could affect the underlying protocol thesis.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=HEIUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=HEIUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=HEI` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=HEI` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=HEIUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=HEIUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=HEI"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

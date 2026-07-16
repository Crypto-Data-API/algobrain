---
title: "Chainbase"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["C"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://chainbase.com/"
related: ["[[crypto-markets]]", "[[base]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[narrative-trading]]"]
---

# Chainbase

**Chainbase** (C) is a Artificial Intelligence (AI), Analytics, BNB Chain Ecosystem, Binance HODLer Airdrops, AI Applications, Binance Alpha Spotlight, Base Native project. It ranks **#1145** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | C |
| **Market Cap Rank** | #1145 |
| **Market Cap** | $10.32M |
| **Current Price** | $0.0645 |
| **Categories** | Artificial Intelligence (AI), Analytics, Binance HODLer Airdrops, AI Applications, Binance Alpha Spotlight, Base Native |
| **Website** | [https://chainbase.com/](https://chainbase.com/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 160.00M C |
| **Total Supply** | 1.00B C |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $64.48M |
| **Market Cap / FDV Ratio** | 0.16 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.5205 (2025-07-18) |
| **Current vs ATH** | -87.61% |
| **All-Time Low** | $0.0461 (2026-03-08) |
| **Current vs ATL** | +40.09% |
| **24h Change** | -2.93% |
| **7d Change** | -1.39% |
| **30d Change** | -32.68% |
| **1y Change** | -67.53% |

---

## Platform & Chain Information

**Native Chain:** Base

### Contract Addresses

| Chain | Address |
|---|---|
| Base | `0xba12bc7b210e61e5d3110b997a63ea216e0e18f7` |
| Binance Smart Chain | `0xc32cc70741c3a8433dcbcb5ade071c299b55ffc8` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | C/USDT | N/A |
| Bitget | C/USDT | N/A |
| KuCoin | C/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://chainbase.com/](https://chainbase.com/) |
| **Twitter** | [@ChainbaseHQ](https://twitter.com/ChainbaseHQ) |
| **Telegram** | [ChainbaseNetwork](https://t.me/ChainbaseNetwork) (68,810 members) |
| **GitHub** | [https://github.com/chainbase-labs](https://github.com/chainbase-labs) |
| **Whitepaper** | [https://docs.chainbase.com/introduction/litepaper](https://docs.chainbase.com/introduction/litepaper) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.58M |
| **Market Cap Rank** | #1145 |
| **24h Range** | $0.0640 — $0.0672 |
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

Chainbase (C) is tradable on **Binance** across both **spot** (C/USDT) and a **USD-margined perpetual**, which exposes funding, open interest, and liquidation dynamics for leveraged traders. It is **NOT** listed on Hyperliquid, so Binance is the primary — effectively sole — deep leveraged venue, with secondary spot listings on Bitget and KuCoin. Given the very thin liquidity (roughly single-digit-million-dollar daily turnover on a sub-$15M-market-cap asset), leverage sizing must stay small: order books are shallow, slippage on market orders is high, and perp funding/basis can dislocate sharply. Venue concentration on Binance means execution, price discovery, and any funding/liquidation strategy hinge on that single order book — a delisting or liquidity withdrawal would leave few fallbacks.

### Applicable strategies

- [[funding-rate-harvest]] — the single Binance USD-M perp lets traders collect funding when the perp trades persistently rich or cheap versus spot on this low-cap name.
- [[crowded-long-funding-fade]] — HODLer-airdrop origin and AI-narrative pumps invite crowded longs; fading extreme positive funding can capture the mean-reversion after such moves.
- [[liquidation-cascade-fade]] — thin books plus perp leverage make C prone to sharp liquidation wicks, giving fade entries against overshoots.
- [[breakout-and-retest]] — a heavily beaten-down small-cap (>85% off ATH) can offer clean breakout-and-retest setups when volume returns on narrative flow.
- [[token-unlock-supply-event]] — with only ~16% of supply circulating and unlimited max supply, scheduled unlocks and emissions are tradeable supply catalysts.
- [[narrative-trading]] — an AI/data-infra token on Base with Binance Alpha spotlight exposure trades heavily on AI and BNB/Base ecosystem narrative cycles.

### Volatility & regime character

Small-cap (rank ~#1145, ~$10M market cap) infrastructure/data token with high beta to Binance-ecosystem and AI-narrative flows. Reflexive, low-float behavior: with ~16% circulating and unlimited max supply, price is sensitive to thin liquidity and emissions. Strongly correlated to BTC/ETH risk-on/risk-off regimes, but amplified — it tends to sell off harder in drawdowns (down ~68% year-over-year, ~33% over 30 days) and spike violently on narrative catalysts. Expect high realized volatility and gappy, event-driven price action rather than smooth trends.

### Risk flags

- **Liquidity / venue concentration** — very low daily volume and Binance-dominant leveraged access; slippage and single-venue dependence are material.
- **Unlocks / emissions** — MCap/FDV ratio ~0.16 with unlimited max supply signals heavy future dilution; unlock schedules can pressure price.
- **Narrative dependence** — valuation leans on AI/data-infra and Binance Alpha/BNB-Base ecosystem narratives that can fade quickly.
- **Drawdown / trend** — deep, sustained decline from ATH; catching a falling small-cap carries reflexive downside risk.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=CUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=CUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=C` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=C` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=CUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=CUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=C"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[base]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

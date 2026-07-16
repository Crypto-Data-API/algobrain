---
title: "Dymension"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["DYM"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://portal.dymension.xyz/"
related: ["[[crypto-markets]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-arbitrage]]"]
---

# Dymension

**Dymension** (DYM) is a Smart Contract Platform, Cosmos Ecosystem, Modular Blockchain, Osmosis Ecosystem, Rollups-as-a-Service (RaaS) project. It ranks **#1237** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | DYM |
| **Market Cap Rank** | #1237 |
| **Market Cap** | $8.61M |
| **Current Price** | $0.0153 |
| **Categories** | Smart Contract Platform, Modular Blockchain, Rollups-as-a-Service (RaaS) |
| **Website** | [https://portal.dymension.xyz/](https://portal.dymension.xyz/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 564.60M DYM |
| **Total Supply** | 1.07B DYM |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $16.31M |
| **Market Cap / FDV Ratio** | 0.53 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $8.50 (2024-02-14) |
| **Current vs ATH** | -99.82% |
| **All-Time Low** | $0.0143 (2026-06-06) |
| **Current vs ATL** | +6.39% |
| **24h Change** | -1.38% |
| **7d Change** | -1.58% |
| **30d Change** | -12.97% |
| **1y Change** | -94.68% |

---

## Platform & Chain Information

**Native Chain:** Osmosis

### Contract Addresses

| Chain | Address |
|---|---|
| Osmosis | `ibc/9A76CDF0CBCEF37923F32518FA15E5DC92B9F56128292BC4D63C4AEA76CBB110` |
| Cosmos | `ibc/9A76CDF0CBCEF37923F32518FA15E5DC92B9F56128292BC4D63C4AEA76CBB110` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | DYM/USDT | N/A |
| Kraken | DYM/USD | N/A |
| Bitget | DYM/USDT | N/A |
| KuCoin | DYM/USDT | N/A |
| Crypto.com Exchange | DYM/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://portal.dymension.xyz/](https://portal.dymension.xyz/) |
| **Twitter** | [@dymension](https://twitter.com/dymension) |
| **Discord** | [https://discord.gg/dymension](https://discord.gg/dymension) |
| **Whitepaper** | [https://docs.dymension.xyz/](https://docs.dymension.xyz/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.57M |
| **Market Cap Rank** | #1237 |
| **24h Range** | $0.0152 — $0.0157 |
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

**Venues & liquidity** — DYM trades on BOTH Binance (spot DYM/USDT plus a USD-margined perpetual) and Hyperliquid (DYM-PERP, offering roughly 40-50x leverage). This is a genuine two-venue derivatives market rather than a single-listing microcap, so on-chain HL flow can be triangulated against Binance's centralized order book. Depth is reasonable for an alt of this size but not deep enough to ignore slippage: large market orders will walk the book on either venue, so size should be scaled to visible L2 depth and split across both venues where possible. The dual listing keeps mark prices tightly arbitraged and makes CEX-vs-DEX funding and basis comparisons tradeable.

**Applicable strategies**
- [[funding-rate-arbitrage]] — With a Binance USD-margined perp and a Hyperliquid DYM-PERP side by side, funding differentials between the two venues can be captured delta-neutral.
- [[hl-vs-cex-funding-divergence]] — Hyperliquid HLP-driven funding on DYM-PERP frequently diverges from Binance's funding, giving a clean two-venue divergence trade.
- [[cash-and-carry]] — Binance spot DYM plus a short perp lets you lock the perp premium as carry on a low-cap, high-funding alt.
- [[liquidation-cascade-fade]] — DYM's thin depth and high leverage make sharp liquidation wicks common; fading the flush after cascades exhausts is a repeatable setup.
- [[oi-confirmed-trend]] — Cross-referencing Hyperliquid open interest with price helps confirm whether a DYM move is real positioning or a low-liquidity squeeze.
- [[range-mean-reversion]] — Deeply depressed near its ATL, DYM often chops in tight ranges, favouring reversion inside established bounds until a narrative catalyst breaks it.

**Volatility & regime character** — DYM is a low-cap, high-beta infrastructure/modular-blockchain (Cosmos RaaS) altcoin sitting more than 99% below its ATH. It carries strong high-beta behaviour: it tends to amplify BTC/ETH directional moves on the downside and reacts violently to modular-blockchain and Cosmos-ecosystem narrative shifts. Realized volatility is elevated relative to majors, and reflexive squeezes are common given the small float and leveraged perp interest. Correlation to BTC/ETH is meaningful in risk-off moves but idiosyncratic during narrative-driven pumps.

**Risk flags**
- Venue concentration and liquidity: two-venue but still a low-cap; depth thins fast and slippage/gap risk is real on size.
- Emissions/supply: unlimited max supply with FDV well above market cap means ongoing dilution pressure from unlocks and emissions.
- Narrative dependence: price is highly sensitive to the modular-blockchain / RaaS / Cosmos narrative cycle rather than fundamentals.
- Perp funding dislocations: high leverage on a thin book can drive extreme funding and liquidation cascades in either direction.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=DYM` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=DYM` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=DYM&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=DYM&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=DYM"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

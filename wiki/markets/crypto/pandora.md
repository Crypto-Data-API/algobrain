---
title: "Pandora"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["PANDORA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.pandora.build/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]"]
---

# Pandora

**Pandora** (PANDORA) is the first ERC404, an experimental mixed ERC20 / ERC721 implementation with native liquidity and fractionalization for non-fungible tokens.

For each token held, addresses receive one replicant from the corresponding NFT collection. It ranks **#2490** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PANDORA |
| **Market Cap Rank** | #2490 |
| **Market Cap** | $1.45M |
| **Current Price** | $145.50 |
| **Categories** | ERC 404, Hybrid Token Standards |
| **Website** | [https://www.pandora.build/](https://www.pandora.build/) |

---

## Overview

Pandora is the first ERC404, an experimental mixed ERC20 / ERC721 implementation with native liquidity and fractionalization for non-fungible tokens.

For each token held, addresses receive one replicant from the corresponding NFT collection. This innovation enables persistent liquidity and semi-fungibility for all assets within the collection.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 10,000 PANDORA |
| **Total Supply** | 10,000 PANDORA |
| **Max Supply** | 10,000 PANDORA |
| **Fully Diluted Valuation** | $1.45M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $32,494.00 (2024-02-09) |
| **Current vs ATH** | -99.55% |
| **All-Time Low** | $40.40 (2026-02-26) |
| **Current vs ATL** | +261.90% |
| **24h Change** | +102.03% |
| **7d Change** | +2.35% |
| **30d Change** | +73.34% |
| **1y Change** | -84.34% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x9e9fbde7c7a83c43913bddc8779158f1368f0413` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X9E9FBDE7C7A83C43913BDDC8779158F1368F0413/0XDAC17F958D2EE523A2206206994597C13D831EC7 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.pandora.build/](https://www.pandora.build/) |
| **Twitter** | [@Pandora_ERC404](https://twitter.com/Pandora_ERC404) |
| **Telegram** | [pandora_404](https://t.me/pandora_404) (5,751 members) |
| **Discord** | [https://discord.gg/kzWgN4gjhg](https://discord.gg/kzWgN4gjhg) |
| **GitHub** | [https://github.com/0xacme/ERC404](https://github.com/0xacme/ERC404) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 579 |
| **GitHub Forks** | 204 |
| **Pull Requests Merged** | 1 |
| **Contributors** | 1 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $54,464.00 |
| **Market Cap Rank** | #2490 |
| **24h Range** | $70.40 — $150.76 |
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

PANDORA is a **perp-first** asset: it trades as **PANDORA-PERP on Hyperliquid** (leverage up to roughly **40-50x**), but it is **not listed on Binance**. Spot access is limited and offshore — the on-chain float lives in a single Uniswap V3 pool on Ethereum, and the entire fixed supply is only 10,000 tokens. As a result, price discovery and directional flow concentrate on the Hyperliquid perp rather than any deep spot venue. Practical implications: order-book depth is thin, so effective size per clip is small, spreads widen quickly during volatility, and slippage plus funding cost dominate execution. Sizing should be scaled to HL book depth (check the L2 book before entry), and stops should account for the gap risk typical of a low-liquidity, high-leverage perp. Because there is no Binance leg, standard CEX-vs-DEX hedging is impractical and the HL perp is effectively the only liquid instrument.

### Applicable strategies

- [[liquidation-cascade-fade]] — thin HL book plus 40-50x leverage means clustered liquidations overshoot fair value; fading the wick after a cascade is a repeatable PANDORA setup.
- [[crowded-long-funding-fade]] — after a reflexive pump (the page shows +102% in 24h), longs crowd the perp and funding spikes; fading the crowded, expensive-to-hold long side is high-probability.
- [[short-liquidation-squeeze]] — a tiny 10,000-token float and low OI make PANDORA prone to sharp upside squeezes that liquidate leveraged shorts on the HL perp.
- [[oi-price-exhaustion]] — with only one liquid venue, HL open interest is a clean gauge; rising OI into a stalling price flags exhaustion and reversal risk.
- [[volatility-breakout]] — PANDORA alternates between quiet drift and violent expansion; ATR-scaled breakout entries capture the reflexive moves while sizing to thin depth.
- [[scalping]] — the perp's wide, fast-moving intraday range suits short-hold, tightly-managed scalps for traders who respect the limited depth.

### Volatility & regime character

PANDORA behaves as a **high-beta, low-float experimental-token / narrative asset** — the first ERC404, so its regime is driven by the ERC404 hybrid-token narrative and speculative reflexivity rather than fundamentals or cash flows. With a 10,000-token fixed supply and micro-cap valuation, moves are exaggerated: the page records swings like +102% in 24h against a -99.55% drawdown from ATH. Correlation to BTC/ETH beta is loose and unreliable — it tends to trade on its own narrative cycles and liquidity conditions, amplifying broad-market risk-on moves but frequently decoupling entirely from majors.

### Risk flags

- **Venue concentration** — liquidity is effectively single-venue (Hyperliquid perp); no Binance listing and only a shallow Uniswap spot pool, so a venue outage or delisting is an outsized risk.
- **Liquidity / depth** — thin order book and tiny float make slippage, gaps, and squeeze/cascade dynamics severe; large orders move price.
- **Perp funding dislocations** — with a small speculative base, funding can spike hard after directional runs, making leveraged carry expensive and unstable.
- **Narrative dependence** — value is tied to the ERC404 experiment and speculative interest; if the narrative fades, liquidity and price can collapse with little support.
- **High-leverage reflexivity** — 40-50x leverage on a micro-cap perp invites rapid liquidation cascades in both directions; position sizing must be conservative.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=PANDORA` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=PANDORA` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=PANDORA&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=PANDORA&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=PANDORA"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

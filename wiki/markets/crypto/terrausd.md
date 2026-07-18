---
title: "TerraClassicUSD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: good
tags: [algorithmic-stablecoin, collapse, crypto, defi, stablecoins, terra, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, altcoins]
aliases: ["TerraUSD", "UST", "USTC"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.terra-classic.io"
related: ["[[2022-05-terra-luna-depeg-arb]]", "[[algorithmic-stablecoin]]", "[[crypto-markets]]", "[[stablecoin-depegs]]", "[[stablecoins]]", "[[terra-luna-2]]", "[[terra-luna-collapse]]", "[[terra-luna]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[narrative-trading]]"]
---

# TerraClassicUSD

**TerraClassicUSD** (USTC, originally UST / TerraUSD) was the largest [[algorithmic-stablecoin|algorithmic stablecoin]] in crypto history before its catastrophic depeg in May 2022. At its peak, UST had an $18.7 billion market cap and was backed entirely by a mint/burn arbitrage mechanism with [[terra-luna|LUNA]] — no fiat reserves, no over-collateralisation. When the mechanism failed, UST depegged from $1 to under $0.10 in less than a week, triggering the [[terra-luna-collapse]] and destroying ~$40 billion in combined value.

Since the collapse, USTC has been a freely traded token with no active peg mechanism. It trades at fractions of a cent, driven by speculation rather than any fundamental value.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USTC (originally UST) |
| **Market Cap Rank** | #714 |
| **Market Cap** | ~$25.5M |
| **Current Price** | ~$0.0046 |
| **ATH** | $1.09 (January 2021) |
| **Current vs ATH** | -99.58% |
| **Circulating Supply** | 5.58B USTC |
| **Category** | Former algorithmic stablecoin (no longer pegged) |

---

## How UST Worked (Before Collapse)

UST maintained its $1 peg through a **mint/burn arbitrage** with LUNA:

- **UST < $1**: Buy cheap UST → burn it → mint $1 of LUNA → sell LUNA for profit. UST supply contracts, price rises
- **UST > $1**: Burn LUNA → mint UST at $1 → sell UST above par. UST supply expands, price falls

This mechanism worked under normal conditions but was fatally vulnerable to reflexive feedback loops. When LUNA's price collapsed, burning UST yielded worthless LUNA, and the arbitrage that was supposed to stabilize the peg instead hyperinflated LUNA's supply. See [[2022-05-terra-luna-depeg-arb]] for the detailed mechanics.

**Anchor Protocol** subsidized ~19.5% APY on UST deposits, attracting $14B and creating massive concentrated demand. When large withdrawals began, the death spiral was unstoppable.

---

## The Depeg

| Date | UST Price | What Happened |
|------|-----------|---------------|
| May 7, 2022 | $0.985 | Large sells on Curve; first depeg |
| May 9 | $0.90 | LFG deploys BTC reserves to defend |
| May 10 | $0.68 | Reserves exhausted; arb hyperinflating LUNA |
| May 11 | $0.35 | Full bank run underway |
| May 12-13 | $0.10 | Peg irrecoverable; chain halted |

For the full timeline and contagion cascade, see [[terra-luna-collapse]].

---

## Post-Collapse Status

After the Terra 2.0 fork (May 28, 2022):
- UST was renamed **USTC** (TerraClassicUSD)
- The mint/burn stabilization mechanism was **permanently disabled**
- USTC trades purely on speculation — there is no peg maintenance and no collateral
- Community proposals to "re-peg" USTC have been discussed but none have produced a viable mechanism
- The SEC classified UST as a security in its case against Terraform Labs

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | ~$2.1M |
| **Typical behavior** | Speculative micro-cap trading; occasional spikes on community re-peg proposals |
| **Exchange listings** | Binance (USTC/USDT), Bitget, KuCoin |
| **Perpetual futures** | Available on [[hyperliquid|Hyperliquid]] (USTC-PERP) |

USTC has no fundamental value driver. Any trading thesis is purely speculative or community-narrative driven.

---

## Major News & Events

| Date | Event |
|------|-------|
| Dec 2017 | Terra whitepaper published by Do Kwon and Daniel Shin |
| Mar 2021 | Anchor Protocol launches; UST growth accelerates |
| Apr 2022 | UST reaches $18.7B market cap; becomes 3rd largest stablecoin |
| May 7-13, 2022 | [[terra-luna-collapse]]: UST depegs and collapses to ~$0.10 |
| May 28, 2022 | Terra 2.0 fork; UST renamed USTC, stabilization mechanism disabled |
| Apr 2024 | SEC civil trial: jury finds UST was a security |
| Jun 2024 | Terraform Labs settles with SEC for $4.47 billion |

---

## Trading Profile

### Venues & liquidity

USTC trades on **both** major venue types, which is unusual for a sub-$50M former stablecoin:

- **Binance** — spot (USTC/USDT) plus a **USD-margined perpetual**, giving USTC deep CEX order-book depth and a reference funding market.
- **Hyperliquid** — **USTC-PERP** with leverage up to ~40-50x, providing an on-chain perp with transparent funding, mark price, and L2 depth.

The result is a **deep, liquid two-venue market** relative to USTC's tiny market cap. Two independent perp venues (CEX + on-chain) plus Binance spot mean traders can route across books, but the underlying float is thin — large size still moves price, and depth on either side of the book can evaporate during re-peg-narrative spikes. Size positions to the shallower of the two books, and prefer resting/limit execution over market sweeps. The dual-venue structure is the enabling condition for cross-venue funding and basis plays below.

### Applicable strategies

- [[hl-vs-cex-funding-divergence]] — Binance USD-M perp and Hyperliquid USTC-PERP quote independent funding; a low-float, narrative-driven token like USTC frequently prices funding differently across the two venues.
- [[funding-rate-arbitrage]] — collect the funding spread between the Binance perp and Hyperliquid USTC-PERP while holding offsetting perp legs, hedging directional risk on a token with no fundamental anchor.
- [[crowded-long-funding-fade]] — re-peg-hope spikes crowd longs and push funding sharply positive; fade the crowded, over-levered side once funding runs rich.
- [[narrative-trading]] — USTC has zero fundamental value driver; price is almost entirely a function of community "re-peg" proposals and speculative narrative flows.
- [[liquidation-cascade-fade]] — up to ~50x leverage on a micro-float perp makes both long and short liquidation cascades sharp; fade the overshoot after forced deleveraging exhausts.
- [[mean-reversion]] — with no organic demand, speculative pumps on thin liquidity tend to round-trip, favoring reversion back toward the pre-spike range.

### Volatility & regime character

USTC is a **defunct algorithmic-stablecoin token now trading as a speculative micro-cap** — effectively a memecoin-style reflexive asset with no peg, no collateral, and no cash-flow driver. Realized volatility is very high and episodic: long dormant drift interrupted by violent, community-narrative-driven spikes ("re-peg" proposals) that fade quickly. Its correlation to BTC/ETH beta is weak and unstable; USTC moves far more on Terra-Classic-specific narrative and leverage flows than on broad market direction, so its beta to majors is low and inconsistent rather than a reliable high-beta alt.

### Risk flags

- **Liquidity / venue concentration** — despite two perp venues, the underlying float is thin; depth can vanish and slippage spikes during narrative-driven moves.
- **No peg / no fundamental value** — the stabilization mechanism is permanently disabled; there is no collateral or anchor, so nothing structurally caps downside.
- **Narrative dependence** — price action is dominated by community "re-peg" speculation, which is unpredictable and reflexive.
- **Perp funding dislocations** — independent funding on Binance vs Hyperliquid can swing hard and diverge during spikes; funding is both an opportunity and a carrying-cost risk.
- **Leverage-driven cascades** — up to ~50x on a micro-float perp makes liquidation cascades and squeezes frequent and severe.
- **Regulatory overhang** — UST was ruled a security in SEC v. Terraform Labs, an idiosyncratic legal/headline risk for the token.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=USTC` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=USTC` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=USTC&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=USTC&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=USTC"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[terra-luna-collapse]] — Full crash timeline and analysis
- [[2022-05-terra-luna-depeg-arb]] — The arbitrage death spiral mechanics
- [[terra-luna]] — Terra Luna Classic (LUNC), the companion token
- [[stablecoins]] — Stablecoin types and risk comparison
- [[stablecoin-depegs]] — History of de-peg events
- [[dai]] — Contrast: over-collateralised stablecoin that survived the crypto winter
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- SEC v. Terraform Labs (civil case), S.D.N.Y.

## Overview

TerraClassicUSD (USTC) was originally launched as an algorithmic stablecoin within the Terra ecosystem, designed to maintain a peg to the US dollar through an automated market-Module mechanism with LUNA (now LUNC). However, following the collapse of the Terra ecosystem in May 2022, the core stabilizing mechanism was disabled, and USTC lost its peg to the US dollar.

Since then, USTC has been a freely traded digital asset, with its price determined purely by market supply and demand. It no longer functions as a stablecoin, nor does it have an active peg-maintenance mechanism.

USTC remains an integral part of the Terra Classic ecosystem, where it continues to be used for various purposes, including DeFi applications , gas fees and trading. Unlike traditional fiat-backed assets, USTC’s value fluctuates based on market conditions and community participation.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 5.58B USTC |
| **Total Supply** | 6.08B USTC |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $33.50M |
| **Market Cap / FDV Ratio** | 0.92 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.09 (2021-01-11) |
| **Current vs ATH** | -99.50% |
| **All-Time Low** | $0.00406362 (2026-02-06) |
| **Current vs ATL** | +35.58% |
| **24h Change** | -0.67% |
| **7d Change** | -4.11% |
| **30d Change** | -8.82% |
| **1y Change** | -60.78% |

---

## Platform & Chain Information

**Native Chain:** Terra

### Contract Addresses

| Chain | Address |
|---|---|
| Terra | `uusd` |
| Osmosis | `ibc/BE1BB42D4BE3C30D50B68D7C41DB4DFCE9678E8EF8C539F6E6A9345048894FCC` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | USTC/USDT | N/A |
| Bitget | USTC/USDT | N/A |
| KuCoin | USTC/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48/0XA47C8BF37F92ABED4A126BDA807A7B7498661ACD | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.terra-classic.io](https://www.terra-classic.io) |
| **Twitter** | [@terra_money](https://twitter.com/terra_money) |
| **Discord** | [https://terra.sc/classicdiscord](https://terra.sc/classicdiscord) |
| **GitHub** | [https://github.com/classic-terra/core](https://github.com/classic-terra/core) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 78 |
| **GitHub Forks** | 60 |
| **Pull Requests Merged** | 65 |
| **Contributors** | 8 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

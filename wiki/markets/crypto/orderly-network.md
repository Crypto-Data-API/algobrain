---
title: "Orderly Network"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi, market-microstructure, exchange]
aliases: ["ORDER", "Orderly", "Orderly Network"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://orderly.network/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[hypercore]]", "[[clob]]", "[[perp-dex-aggregation]]", "[[hyperliquid-vs-dydx-vs-gmx]]", "[[market-microstructure]]", "[[hyperliquid-order-book-microstructure]]"]
---

# Orderly Network

**Orderly Network** (ORDER) is a shared, permissionless **order-book liquidity layer** for Web3 trading — a single [[clob|central limit order book]] shared across many blockchains, powered by Orderly Chain (an OP-stack L2) and LayerZero. Rather than running a consumer-facing exchange, Orderly acts as **underlying CLOB infrastructure** that multiple perp-DEX front-ends and protocols plug into, so independent UIs can share one pool of order-book liquidity instead of each bootstrapping its own. This makes it a direct point of comparison with [[hyperliquid|Hyperliquid]]'s vertically integrated, app-specific design. It ranks **#960** by market capitalization as of 2026-06-20.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ORDER |
| **Current Price** | $0.037681 |
| **Market Cap** | $14.76M |
| **Market Cap Rank** | #960 |
| **Fully Diluted Valuation** | $37.68M |
| **24h Volume** | $4.22M |
| **24h Range** | $0.037154 — $0.038005 |
| **24h Change** | +0.11% |
| **7d Change** | -6.27% |
| **Website** | [https://orderly.network/](https://orderly.network/) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Trading backdrop: the broad crypto market sits in **extreme fear** (Crypto Fear & Greed Index = 23) within an **established bear market** as of 2026-06-20. ORDER is roughly flat on the day but down ~6% on the week; with a ~$14.8M cap against ~$4.2M of daily turnover (~29% of cap), it is a thinly capitalized micro-cap where a single large order can move price materially — execution risk that matters more than for the larger venues it competes with.

### Categories

Smart Contract Platform, Decentralized Finance (DeFi), BNB Chain Ecosystem, Perpetuals, Solana Ecosystem, Avalanche Ecosystem, Polygon Ecosystem, Arbitrum Ecosystem, Ethereum Ecosystem, Optimism Ecosystem, Layer 2 (L2), Base Ecosystem, DragonFly Capital Portfolio, Pantera Capital Portfolio, Sequoia Capital Portfolio, OKX Ventures Portfolio, Optimism Superchain Ecosystem, Binance Alpha Spotlight, Abstract Ecosystem, Base Native.

---

## Overview

Orderly Network is an OP-stack L2 delivering a permissionless liquidity layer for Web3 trading, with **one shared order book across multiple blockchains** — powered by Orderly Chain and LayerZero. Its stated mission is to enable trading on any chain, any asset, any interface. Orderly offers spot and perpetual-futures order-book trading across chains including Arbitrum, Optimism, Polygon, Base, Mantle, and NEAR, while expanding to others.

The defining idea is **separation of liquidity from interface**: the order book and matching live in Orderly's infrastructure, while many independent front-ends ("builders") connect to it. 2026 surveys of the perp-DEX landscape refer to this family as **"Orderly-based markets"** and list it alongside [[hyperliquid|Hyperliquid]], dYdX, GMX, Drift, Vertex, and Aevo as one of the core families of perp venues (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

## Shared CLOB liquidity model

Orderly's role is best understood as the **"underlying order book" provider** for a network of front-ends, rather than a single consumer exchange (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]). Many trading UIs and protocols can route into the same Orderly order book, so liquidity is pooled across them instead of being fragmented per front-end.

| Layer | In the Orderly model | Analogy |
|---|---|---|
| **Interface / front-end** | Many independent builders' UIs and protocols | The "brand" the user sees |
| **Liquidity / matching** | One shared Orderly [[clob\|CLOB]] (Orderly Chain + LayerZero) | The shared order book everyone draws on |
| **Cross-chain delivery** | LayerZero messaging connects multiple chains to one book | Omnichain settlement plumbing |

This is the opposite end of a design continuum from a self-contained venue: where a vertically integrated venue owns the whole stack, Orderly deliberately *unbundles* the order book so it can be reused.

## Contrast with Hyperliquid's vertically integrated approach

[[hyperliquid|Hyperliquid]] is the canonical **vertically integrated** on-chain CLOB: its order books, matching, margining, and liquidations live in [[hypercore|HyperCore]] at the protocol level of a purpose-built L1, with [[hyperevm|HyperEVM]] layered on top — 2026 commentary frames it as "an exchange with an L1 wrapped around it" (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]). Orderly takes the inverse approach: it is a **shared liquidity layer** designed to be consumed by *other* people's front-ends across many chains.

| Dimension | Orderly Network | [[hyperliquid\|Hyperliquid]] |
|---|---|---|
| **Architecture** | Shared CLOB liquidity layer for many front-ends | Vertically integrated app-specific L1 ([[hypercore\|HyperCore]] + [[hyperevm\|HyperEVM]]) |
| **Who runs the UI** | Many independent "builder" front-ends | Primarily Hyperliquid's own app + builder integrations |
| **Liquidity model** | One book shared across front-ends and chains | One deep app-specific book, on-chain |
| **Cross-chain** | Omnichain via LayerZero / Orderly Chain | App-specific L1 (bridge in/out) |
| **Price-discovery role** | Aggregated across connected front-ends | Often a primary price-discovery venue for major perps (Source: research) |
| **Native token** | ORDER (see below) | HYPE |

Neither approach is strictly superior. Vertical integration concentrates liquidity and price discovery in one venue; the shared-layer model spreads one liquidity pool across many interfaces and chains. For a trader doing venue selection, the practical question is **where the depth actually is** for a given pair and size.

## Relevance to perp-DEX aggregation

Because there is **no single best perp DEX for all conditions** — execution quality depends on order size, funding, and available depth across venues — sophisticated traders increasingly use [[perp-dex-aggregation|perp-DEX aggregators]] that route across Hyperliquid, Orderly-based markets, dYdX, GMX, and others (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]). Orderly matters in this context as one of the **liquidity sources an aggregator routes into**:

| Aggregation use | How Orderly fits |
|---|---|
| **Best-execution routing** | An aggregator compares Orderly-based depth against [[hyperliquid\|Hyperliquid]] and others for a given order |
| **Order splitting** | Large orders can be split across Orderly and other books to minimize slippage |
| **Funding-rate differentials** | Funding can be compared across Orderly-based markets and other venues |
| **Liquidity-fragmentation awareness** | Knowing Orderly is a *shared* book (not per-front-end) changes the true-depth picture |

For the broader strategy framing — when to favor a vertically integrated venue vs. route elsewhere — see [[perp-dex-aggregation]] and the venue comparison in [[hyperliquid-vs-dydx-vs-gmx]].

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 391.84M ORDER |
| **Total Supply** | 1.00B ORDER |
| **Max Supply** | 1.00B ORDER |
| **Fully Diluted Valuation** | $37.68M |
| **Market Cap / FDV Ratio** | ~0.39 |

Only ~39% of the fixed 1B max supply is in circulation, so a meaningful future-emission overhang remains (MC/FDV ~0.39) — typical of an infrastructure token still inside its vesting/unlock schedule. ORDER's design intent is value accrual from network usage: it is the token used for staking, fee/rebate alignment, and governance across the shared liquidity layer, so its long-run thesis hinges on **how much builder-routed volume flows through Orderly's book** rather than on any single front-end's success.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.4915 (2025-10-06) |
| **Current vs ATH** | -92.33% |
| **All-Time Low** | $0.035503 (2026-06-06) |
| **Current vs ATL** | +6.16% |
| **24h Change** | +0.11% |
| **7d Change** | -6.27% |

ORDER printed a fresh all-time low (~$0.0355) on 2026-06-06 during the established bear market and trades just above it — a sign the token has been a high-beta loser in the risk-off tape despite the protocol's continued operation.

---

## Valuation Framing (qualitative)

ORDER is not valued like a consumer-exchange token; it is an **infrastructure/middleware bet** on the unbundling of order-book liquidity. The bull case is that, as perp trading fragments across dozens of front-ends, a shared neutral CLOB captures economics that no single UI can — a "liquidity-as-a-service" toll. The bear case is twofold: (1) vertically integrated venues like [[hyperliquid|Hyperliquid]] keep concentrating depth and price discovery, leaving little oxygen for a shared layer; and (2) even if Orderly-based volume grows, the value may accrue to the front-ends and traders rather than to the ORDER token. At a ~$15M cap and ~0.39 MC/FDV, the market is currently pricing the bear case. There is no published authoritative fair-value anchor in this wiki; treat any target as scenario-dependent on builder adoption and fee capture, not a derived number.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xabd4c63d2616a5201454168269031355f4764337` |
| Binance Smart Chain | `0x4e200fe2f3efb977d5fd9c430a41531fb04d97b8` |
| Avalanche | `0x4e200fe2f3efb977d5fd9c430a41531fb04d97b8` |
| Abstract | `0x9a4c8cd493cf0bf8e14bda5890e3f03a1cded719` |
| Base | `0x4e200fe2f3efb977d5fd9c430a41531fb04d97b8` |
| Solana | `ABt79MkRXUsoHuV2CVQT32YMXQhTparKFjmidQxgiQ6E` |
| Polygon Pos | `0x4e200fe2f3efb977d5fd9c430a41531fb04d97b8` |
| Arbitrum One | `0x4e200fe2f3efb977d5fd9c430a41531fb04d97b8` |
| Optimistic Ethereum | `0x4e200fe2f3efb977d5fd9c430a41531fb04d97b8` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | ORDER/USD | N/A |
| Upbit | ORDER/KRW | N/A |
| Bitget | ORDER/USDT | N/A |
| KuCoin | ORDER/USDT | N/A |
| Crypto.com Exchange | ORDER/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://orderly.network/](https://orderly.network/) |
| **Telegram** | [OrderlyNetworkAnnouncements](https://t.me/OrderlyNetworkAnnouncements) (2,388 members) |
| **Discord** | [https://discord.com/invite/orderlynetwork](https://discord.com/invite/orderlynetwork) |
| **GitHub** | [https://github.com/OrderlyNetwork](https://github.com/OrderlyNetwork) |

---

## Market Structure & Derivatives

| Characteristic | Detail |
|---|---|
| **24h Volume (token)** | $4.22M |
| **Market Cap Rank** | #960 |
| **24h Range** | $0.037154 — $0.038005 |
| **Token turnover** | ~29% of market cap/day — high relative to cap; price is sensitive to single large orders |
| **Spot venues** | Kraken, Upbit, Bitget, KuCoin, Crypto.com (see Exchange Listings) |

Two distinct liquidity layers should not be conflated: the **ORDER token's** spot/derivative liquidity (thin micro-cap, above) versus the **protocol's order-book volume** — the trading throughput routed through the shared Orderly CLOB by builder front-ends, which is the metric that actually validates the business. A trader sizing a position in the ORDER *token* is exposed to micro-cap liquidity risk; a trader executing perps *on* an Orderly-based front-end is drawing on the pooled book. ORDER perpetuals are also listed on some derivatives venues, but open interest is modest for a token of this size — funding and OI are worth checking before any leveraged expression.

### Peer comparison

| Project | Token | Approx. rank | Architecture | Liquidity model |
|---|---|---|---|---|
| **Orderly Network** | ORDER | ~#960 | Shared CLOB liquidity layer for many front-ends | One book pooled across builders & chains |
| [[hyperliquid\|Hyperliquid]] | HYPE | ~#10 | Vertically integrated app-specific L1 | One deep on-chain book ([[hypercore\|HyperCore]]) |
| dYdX | DYDX | mid-cap | App-specific chain (Cosmos), own order book | Self-contained book |
| GMX | GMX | mid-cap | Oracle-priced AMM/pool (Arbitrum) | LP-pool counterparty, not a CLOB |
| Drift | DRIFT | small-cap | Hybrid order book + AMM (Solana) | Self-contained, Solana-native |

Orderly is the smallest by token cap in this set and the only one whose explicit model is to be **consumed by other people's front-ends** rather than to run its own dominant venue (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

---

## Risks

- **Micro-cap liquidity / volatility:** at ~$15M market cap the ORDER token is thinly traded; price gaps and slippage on size are material, and it has been a high-beta loser (fresh ATL on 2026-06-06).
- **Emission overhang:** ~61% of max supply is not yet circulating (MC/FDV ~0.39); future unlocks are a structural headwind.
- **Competitive concentration:** vertically integrated venues (Hyperliquid) continue to pull depth and price discovery toward themselves, squeezing the shared-layer thesis.
- **Value-capture risk:** even if Orderly-routed volume grows, economics may accrue to builders/traders rather than the ORDER token.
- **Smart-contract & cross-chain risk:** Orderly Chain (OP-stack L2) plus LayerZero omnichain messaging add bridge and contract attack surface beyond a single-chain venue.
- **Macro regime:** with Fear & Greed at 23 (extreme fear) in an established bear market, micro-cap infrastructure tokens are acutely exposed to sentiment-driven drawdowns.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[hyperliquid]] — vertically integrated contrast case
- [[hypercore]] — Hyperliquid's protocol-level order-book engine
- [[hyperevm]] — Hyperliquid's smart-contract layer
- [[perp-dex-aggregation]] — cross-venue routing that treats Orderly as a liquidity source
- [[hyperliquid-vs-dydx-vs-gmx]] — perp-venue comparison
- [[clob]] · [[market-microstructure]] — conceptual grounding
- [[hyperliquid-order-book-microstructure]] — order-book behavior reference
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original market-data snapshot (tokenomics, listings, contract addresses)
- Market snapshot 2026-06-20: cryptodataapi.com / CoinGecko top-1000 markets data (price, market cap, rank, volume, supply, ATH/ATL refresh)
- (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]) — shared-CLOB-layer role, "Orderly-based markets" framing, contrast with Hyperliquid, perp-DEX aggregation context

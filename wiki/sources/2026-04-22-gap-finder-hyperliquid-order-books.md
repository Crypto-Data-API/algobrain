---
title: "Gap-Finder Research: Hyperliquid Order Books & On-Chain CLOB Trading"
type: source
created: 2026-06-20
updated: 2026-06-20
status: good
tags: [crypto, market-microstructure, hyperliquid, methodology, data-provider]
source_type: article
source_url: "https://hyperliquid.gitbook.io/hyperliquid-docs"
source_author: "Perplexity sonar-deep-research (synthesis) + Hyperliquid official docs"
source_date: 2026-04-22
source_file: "raw/articles/2026-04-22-gap-finder-hyperliquid-order-books.md"
confidence: medium
claims_count: 12
related: ["[[hyperliquid]]", "[[clob]]", "[[hypercore]]", "[[hyperbft]]", "[[hip-3-builder-deployed-perps]]", "[[hlp]]"]
---

Deep-research gap analysis (Perplexity `sonar-deep-research`, 2026-04-22) on Hyperliquid order books and on-chain central-limit-order-book (CLOB) trading, via a Perplexity deep-research run. It compared the wiki's existing Hyperliquid coverage against the current (2024–2026) state of the venue and recommended ~24 entity/concept/data-source additions. The synthesis itself is **MEDIUM** confidence; its underlying primary sources (Hyperliquid's own GitBook docs) are **HIGH** confidence.

## Key claims (with confidence)

- **[HIGH]** Hyperliquid splits execution into **HyperCore** (on-chain perp + spot order books, margining, liquidations) and **HyperEVM** (Ethereum-like smart-contract layer that composes with HyperCore liquidity). (Source: hyperliquid-docs)
- **[HIGH]** Order books use **price-time priority** with protocol-enforced tick size and lot size; every order, cancel, trade, and liquidation executes fully on-chain. (Source: hyperliquid-docs/trading/order-book)
- **[HIGH]** Consensus is **HyperBFT**, a HotStuff-inspired BFT protocol optimized for low-latency, order-book-centric workloads with single-block finality. (Source: hyperliquid-docs)
- **[MEDIUM]** HyperCore is engineered for very high throughput, cited "on the order of 200,000 orders/second." (Source: GoodCryptoX / docs)
- **[HIGH]** **Funding** is charged hourly; the rate combines a small fixed interest component with a **premium index** derived from **impact bid/ask prices** (order book consumed to a set depth vs the oracle price), with a clamp/cap. (Source: hyperliquid-docs/trading/funding)
- **[HIGH]** A **liquidation** triggers when account equity falls below maintenance margin, defined as **half the initial margin at max leverage**; max leverage ranges ~3–40× → maintenance-margin ratios ~16.7% down to ~1.25%. The protocol closes positions via market orders into existing book depth. (Source: hyperliquid-docs/trading/liquidations)
- **[HIGH]** Fees are based on **rolling 14-day volume** (spot volume counts double); a single tier spans perps/HIP-3/spot; **maker rebates** are paid continuously; fees are directed to the community (HLP, assistance fund, deployers). (Source: hyperliquid-docs/fees)
- **[HIGH]** **HIP-3** enables permissionless, builder-deployed perp markets that share HyperCore's matching engine but set their own oracle, contract specs, leverage limits, settlement, and fee shares; each HIP-3 DEX has its own on-chain backstop liquidation strategy contract and supports a "no-cross" (isolated) margin mode. (Source: hyperliquid-docs HIP-3 / margining)
- **[MEDIUM]** HIP-3 builder-deployed markets cleared **$62B in a single month**, lifting Hyperliquid's share of global perps volume to a record **6.63%**. (Source: The Defiant)
- **[MEDIUM]** **HYPE** token genesis launch was late November 2024 at an initial ~$3; roadmap targets full decentralization and HyperEVM expansion. (Source: hyperliquid-co wiki roadmap)
- **[MEDIUM]** Talos integrated Hyperliquid market data (spot, perps incl. HIP-3: trades, order books, OI, funding, derived metrics) into its **Coin Metrics** Market Data product. (Source: Talos)
- **[MEDIUM]** A research-grade **"Level 4" Hyperliquid order book dataset** (SSRN) was captured via a non-validating node, recording full order additions/executions/cancellations for microstructure research. (Source: SSRN)
- **[MEDIUM]** Comparable on-chain CLOBs include **Injective** (Cosmos-SDK exchange module), **Sei** (DeFi L1 with native CLOB), **Econia** (on-chain order book on Aptos), and **Orderly** (shared CLOB liquidity layer for multiple front-ends); 2026 commentary frames Hyperliquid as "an exchange with an L1 wrapped around it." (Source: Pontem, Phemex Academy, VOOI)

## Primary sources cited

- Hyperliquid Docs — Order Book: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/order-book
- Hyperliquid Docs — Funding: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding
- Hyperliquid Docs — Liquidations: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations
- Hyperliquid Docs — WebSocket API: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/websocket
- Hyperliquid Python SDK: https://github.com/hyperliquid-dex/hyperliquid-python-sdk
- Hyperliquid roadmap (community wiki): https://hyperliquid-co.gitbook.io/wiki/introduction/roadmap
- Pontem — On-chain order books 101 (Econia & more): https://pontem.network/posts/on-chain-order-books-101-econia-more
- Phemex Academy — Injective vs Hyperliquid (2026): https://phemex.com/academy/injective-vs-hyperliquid-defi-trading-network-2026
- HypurrScan: https://hypurrscan.io

## Pages this source contributed to

See `wiki/log.md` entry dated 2026-06-20 (gap analysis: hyperliquid order books).

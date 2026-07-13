---
title: "DeFiLlama"
type: entity
created: 2026-04-10
updated: 2026-06-10
status: good
tags: [crypto, defi, data-provider]
entity_type: company
founded: 2020
headquarters: "Decentralized"
website: "https://defillama.com"
aliases: ["DeFiLlama", "DefiLlama", "Defi Llama", "Llama"]
related: ["[[defi]]", "[[dune-analytics]]", "[[liquidity-provision]]", "[[liquid-staking]]", "[[restaking]]"]
---

DeFiLlama is the leading data aggregator and analytics platform for the [[defi|DeFi]] ecosystem, founded in 2020 by the pseudonymous developer 0xngmi. It tracks total value locked (TVL), yields, fees, revenues, stablecoin supply, bridge flows, and exploit data across 6,000+ DeFi protocols on 400+ blockchains as of 2026 (some 2026 reviews cite 7,000+ protocols on 500+ chains; up from roughly 3,000 protocols / 200 chains in 2024), and has become the de facto reference for DeFi metrics used by researchers, journalists, funds, and traders.

## Overview

DeFiLlama's core value proposition is normalization: it applies consistent methodology across heterogeneous protocols, chains, and asset types so that TVL and yield figures are actually comparable. The project is open-source, operates under a decentralized "Llama" collective, and exposes virtually all of its data through a free public API — a sharp contrast to closed analytics vendors.

## Key Dashboards

- **TVL** — rankings by protocol, chain, and category (lending, DEX, [[liquid-staking]], [[restaking]], CDP, yield aggregator, etc.), with historical charts and inflow/outflow breakdowns.
- **Yields** — the canonical cross-protocol APY comparison tool, covering lending markets, [[liquidity-provision|LP pools]], staking, restaking, and farming. Filters for stablecoin-only, audited-only, and impermanent-loss risk are widely used for yield stack construction.
- **Fees & Revenue** — shows gross fees paid by users and the share captured by the protocol, enabling fundamental-style valuation of tokens.
- **Stablecoins** — tracks supply, chain distribution, and peg history across USDT, USDC, DAI, and long-tail issuers.
- **Bridges and CEX transparency** — flow tracking across cross-chain bridges and on-chain CEX wallet balances.
- **Hacks tracker** — catalog of $3B+ in cumulative DeFi exploits, widely cited in security post-mortems.

## Pricing and API (as of June 2026)

The base website and core API remain free, but DeFiLlama now runs a tiered subscription model:

| Tier | Price | What you get |
|------|-------|--------------|
| **Open (free)** | $0 | Core TVL/revenue metrics, LlamaFeed real-time news/updates feed, community support |
| **Pro** | $49/mo ($490/yr) | LlamaAI analysis (5 questions/day), custom dashboards, CSV downloads, spreadsheet integrations (no API access) |
| **API** | $300/mo ($3,000/yr) | All Pro features plus API access at 1,000 requests/min and 1,000,000 calls/month |
| **Enterprise** | Custom | Direct raw database access, hourly feeds, bespoke TVL breakdowns by token address |

**LlamaFeed** is the real-time market-update feed (news, listings, hacks, unlocks, raises) and **LlamaAI** is the natural-language query layer added to the Pro tier. (Source: defillama.com/subscription and docs.llama.fi, June 2026)

## Governance: the 2023 token dispute

In March 2023, an internal dispute became public when a team member attempted to launch a LLAMA token against the wishes of lead developer 0xngmi, who announced a fork of the project. The dispute was resolved within days — the team retained control of defillama.com, the token launch was abandoned, and the project publicly recommitted to remaining token-free. **DeFiLlama has no token as of June 2026**; anything trading under a "LLAMA"-style ticker is unaffiliated. The episode is a useful case study in key-person and governance risk for data infrastructure that traders depend on.

## Ecosystem

The Llama collective runs several sister products: **DL News** (independent DeFi journalism), **LlamaFolio** (portfolio tracker), and **LlamaSwap** (DEX aggregator that routes through other aggregators for best execution). Competitors include [[dune-analytics|Dune Analytics]] (query-driven, user-authored dashboards), Token Terminal (fundamentals-focused, partially paywalled), and Nansen (wallet-labeling and on-chain intelligence). DeFiLlama tends to be the first stop for top-of-funnel DeFi research precisely because it is free, comprehensive, and methodologically transparent.

## Related

- [[defi]]
- [[dune-analytics]]
- [[liquidity-provision]]
- [[liquid-staking]]
- [[restaking]]

## Sources

- DeFiLlama platform — https://defillama.com
- DeFiLlama methodology docs — https://docs.llama.fi/
- DeFiLlama Pro/API pricing — https://docs.llama.fi/pro-api and https://defillama.com/subscription
- DeFiLlama API docs — https://api-docs.defillama.com/
- Datawallet, "DefiLlama Explained: Features, LlamaSwap & More (2026)" — https://www.datawallet.com/crypto/defillama-explained
- Contemporary coverage of the March 2023 fork/token dispute (CoinDesk, The Block, March 2023)
- Verified via Perplexity (sonar) and web search, 2026-06-10

---
title: "Zapper"
type: source
created: 2026-04-22
updated: 2026-06-12
status: good
tags: [data-provider, defi, yield-farming]
source_type: data
source_url: "https://zapper.xyz"
source_author: "Zapper"
confidence: high
aliases: ["Zapper.fi", "Zapper.xyz", "Zapper API"]
related: ["[[defi]]", "[[yield-farming]]", "[[defi-yield-farming]]", "[[token-terminal]]", "[[dune-analytics]]", "[[crypto-data-sources]]"]
---

Zapper (now at zapper.xyz, formerly zapper.fi) is a DeFi portfolio tracker, transaction aggregator, and on-chain data provider that gives a unified view of positions across dozens of EVM and non-EVM chains. Beyond the consumer dashboard, Zapper has increasingly positioned itself as an **on-chain data API**: the same wallet-resolution and position-decoding engine that powers the app is sold as a developer API (the Zapper API / GraphQL endpoint) that wallets, exchanges, and analytics products embed to render human-readable portfolios. For traders it is both a one-stop dashboard for managing [[yield-farming]] positions and a data source for building portfolio-tracking tooling across the fragmented DeFi landscape.

## Key Features

### Portfolio Dashboard
- **Unified view:** See all DeFi positions (LP tokens, lending deposits, staking, vaults, NFTs) across 30+ chains in a single dashboard
- **Wallet tracking:** Connect any wallet address to view its complete DeFi portfolio without connecting a wallet (read-only)
- **Historical performance:** Track portfolio value over time, including realized and unrealized P&L across all positions
- **Token balances:** Complete view of token holdings, claimable rewards, and airdrop eligibility

### Yield Discovery
- **Yield comparison:** Browse and filter yield opportunities across protocols and chains by APY, TVL, risk level, and asset type
- **Pool details:** View detailed metrics for individual pools including historical APY, TVL trends, and fee generation
- **One-click deposits:** "Zap in" to vault or LP positions directly through Zapper's interface, which handles multi-step transactions (swaps, approvals, deposits) in a single transaction

### Transaction Aggregation
- **Zap transactions:** Bundle multiple DeFi operations (swap + approve + deposit + stake) into single transactions, saving gas and reducing friction
- **Cross-protocol routing:** Automatically routes through optimal paths for entering or exiting complex DeFi positions
- **Transaction history:** Complete, decoded history of all DeFi interactions with human-readable descriptions

## Trading Relevance

- **Yield opportunity scanning:** Quickly identify the highest risk-adjusted yields across protocols and chains without manually checking each platform
- **Position management:** Monitor all [[defi-yield-farming|yield farming]] positions from one dashboard instead of logging into 10+ protocol UIs
- **Risk monitoring:** Track portfolio concentration, exposure by chain, and exposure by protocol to manage [[smart-contract-risk]]
- **Gas optimization:** "Zap" transactions reduce the number of on-chain interactions needed to enter or exit positions, saving significant gas costs on [[ethereum]] mainnet
- **Whale watching:** View any public wallet address to track what protocols and positions large/sophisticated DeFi users are farming

## Access and Pricing

- **App (free):** Full portfolio tracking, read-only wallet viewing across all supported chains, and zap transactions are free to use in the consumer app.
- **Zapper API (paid, usage-based):** The developer API is the commercial product. It is metered (credit/query-based pricing with a limited free allowance, then paid tiers scaling with query volume). It exposes portfolio balances, decoded positions, token metadata, transaction history, and price data via a GraphQL endpoint. Exact credit pricing drifts; verify at zapper.xyz before building against a specific tier.
- **Pro / subscription:** Enhanced app features and higher limits for power users have been offered at various points; the emphasis since the zapper.xyz rebrand has shifted toward the API as the monetisation surface.

Note: Zapper deprecated several legacy free public REST endpoints in favour of the metered GraphQL API, so older integrations that assumed a fully free API no longer hold — budget for API costs in any automation.

## Limitations

- **Not a data analysis tool:** Zapper shows current positions and basic history but lacks the deep analytical capabilities of [[dune-analytics]] or [[token-terminal]]
- **Protocol coverage gaps:** Newer or smaller protocols may not be supported immediately
- **Zap routing risk:** Automated transaction routing may execute at suboptimal prices during high volatility
- **No backtesting:** Cannot analyze historical strategy performance -- it is a portfolio tracker, not a research tool
- **Smart contract interaction risk:** Using Zapper's zap feature requires approving Zapper's contracts, adding another layer of smart contract exposure

## Related

- [[defi-yield-farming]] -- the strategy Zapper helps manage and monitor
- [[yield-farming]] -- the broader concept of earning yield in DeFi
- [[defi]] -- the ecosystem Zapper aggregates
- [[dune-analytics]] -- deeper on-chain analytics (complementary to Zapper's portfolio view)
- [[token-terminal]] -- protocol-level financial metrics (complementary to Zapper's position-level tracking)
- [[crypto-data-sources]] -- broader catalog of crypto data providers
- [[ethereum]] -- the primary chain for Zapper's DeFi aggregation

## Sources

- Zapper documentation and product pages (zapper.xyz) -- platform features, supported chains, and the Zapper API (GraphQL) developer offering
- General knowledge of DeFi portfolio-aggregation tooling (current as of June 2026); specific pricing tiers should be verified at the source as they drift

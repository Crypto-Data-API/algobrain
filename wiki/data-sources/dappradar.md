---
title: "DappRadar"
type: source
source_type: data
source_url: "https://dappradar.com"
created: 2026-04-22
updated: 2026-06-12
status: good
tags: [nft, crypto, defi, data-provider, analytics]
aliases: ["Dapp Radar", "DappRadar"]
related: ["[[nft-price-floor]]", "[[opensea]]", "[[blur]]", "[[magic-eden]]", "[[nft]]", "[[nft-trading]]", "[[coingecko]]", "[[dune-analytics]]"]
---

DappRadar is a multi-chain decentralized application (dapp) analytics platform that tracks usage, trading volume, and financial metrics across [[defi]] protocols, [[nft]] marketplaces, games, and other on-chain applications. Founded in 2018 and headquartered in Lithuania, it has become one of the most widely cited public sources for cross-chain dapp and NFT market data, referenced in industry reports, exchange research, and mainstream crypto journalism.

## What it tracks

DappRadar aggregates on-chain activity into a browsable, ranked format across several data categories:

- **DeFi TVL** — total value locked by protocol, chain, and category (lending, DEX, yield, liquid staking)
- **NFT sales and volume** — per-collection floor prices, sales counts, USD volume, unique buyers/sellers, and average sale price
- **NFT marketplace rankings** — aggregate volume and user counts across [[opensea]], [[blur]], [[magic-eden]], and chain-specific venues
- **Dapp rankings** — dapps ordered by active wallets (UAW), transaction count, volume, or balance, filterable by chain and category
- **Token analytics** — price, market cap, holders, and transfer activity for tokens tied to covered dapps
- **User wallet activity** — aggregate unique active wallet counts used as a proxy for user growth and engagement
- **Industry reports** — quarterly and annual "Dapp Industry Report" and "NFT Report" publications widely quoted in the press

## Chain coverage

DappRadar is explicitly multi-chain, which is part of why it is cited in cross-ecosystem research. Supported networks include, among others:

- [[ethereum]]
- BNB Chain
- Polygon
- [[solana]]
- Bitcoin / Bitcoin [[ordinals-protocol]]
- Arbitrum, Optimism, Base, and other EVM L2s
- Avalanche, Fantom, Cronos, Ronin, Immutable, and other L1/L2 gaming and NFT chains

Coverage depth varies by chain — Ethereum and BNB Chain have the longest histories and richest metadata, while newer chains and rollups may have partial category coverage.

## Trading use cases

For [[nft-trading]] and broader crypto traders, DappRadar functions as a top-down market scanner and sentiment dashboard:

- **NFT market sentiment** — rising aggregate NFT volume across chains is one input to gauging whether the segment is in an expansion or contraction phase
- **Cross-chain NFT volume comparison** — compare Ethereum vs Solana vs Bitcoin Ordinals NFT volume to identify which ecosystem is attracting flow, then rotate toward marketplaces on the leading chain
- **Marketplace share tracking** — observe share shifts between [[opensea]], [[blur]], [[magic-eden]], and others as a signal of which venue has the most active trader base for a given period
- **Dapp discovery and rotation** — use active-wallet and volume rankings to spot rising protocols before they appear on other aggregators, feeding [[narrative-trading]] and thematic baskets
- **Category rotation** — track whether flow is moving into lending, DEX, gaming, or NFT categories, and position accordingly
- **DeFi TVL confirmation** — cross-reference DappRadar TVL with [[defilama]] as a sanity check when values disagree
- **Report-driven positioning** — the quarterly DappRadar reports frequently move attention to specific chains or categories; traders can use them as context rather than as trade signals directly

## Access and pricing

- **Free web interface** — the browsable rankings, dapp/NFT/DeFi dashboards, and basic metrics are free and the main entry point for casual use
- **PRO / paid tiers** — historical time-series depth, custom data views, ad-free browsing, and portfolio tools sit behind a subscription (DappRadar has historically offered both fiat and RADAR-token-based access; verify current structure on [dappradar.com](https://dappradar.com))
- **API** — a developer API exposes dapp, DeFi, NFT, and token data programmatically; metered by request volume with free and paid tiers
- **Industry reports** — the quarterly "Dapp Industry Report" / "NFT Report" PDFs are published free and widely quoted

Pricing and the RADAR-token utility model drift; confirm current tiers before building tooling against the API.

## Limitations

- **Wash trading contamination** — reported NFT and DEX volumes can include wash-traded activity, particularly on chains or marketplaces that subsidize trading with token rewards. DappRadar publishes some cleaned volume metrics, but methodology is not uniform across all views
- **Methodology differences** — DappRadar's NFT volume figures often diverge from [[cryptoslam]], marketplace-native APIs, or [[dune-analytics]] custom queries because of differences in which transactions are counted (primary vs secondary, bundled sales, cross-chain bridging) and in USD-conversion timing
- **Delayed and partial coverage** — newer dapps and chains can take time to be indexed, and not every dapp submits metadata, so smaller-but-growing projects may be underrepresented
- **Aggregation over resolution** — DappRadar is strong for top-down views but weaker for trade-level analysis; for per-wallet or per-transaction work, [[dune-analytics]] or marketplace-native data is more appropriate
- **Paid tier for deeper data** — historical time-series, API access for programmatic use, and custom data exports are gated behind paid plans; the free web interface is the main entry point for casual use
- **Token incentive bias** — categories and chains running active incentive programs (points, airdrops, fee rebates) can show inflated activity that does not persist once incentives end
- **Not a pricing oracle** — floor prices shown are indicative, typically sourced from marketplace APIs, and should not be treated as real-time executable prices

## Related

- [[nft-price-floor]] — NFT-specific floor-price tracker
- [[opensea]], [[blur]], [[magic-eden]] — marketplaces whose volume feeds DappRadar's NFT rankings
- [[nft]], [[nft-trading]] — broader context for NFT data usage
- [[coingecko]] — complementary token and market-cap aggregator
- [[dune-analytics]] — customizable on-chain analytics alternative for deeper queries
- [[defilama]] — TVL-focused DeFi aggregator commonly used alongside DappRadar

## Sources

- DappRadar website, product documentation, and published industry reports (https://dappradar.com)
- Reference to DappRadar as a cross-chain NFT and dapp tracking tool in wiki gap-finder research (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]])

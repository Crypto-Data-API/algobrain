---
title: "Sniping (Crypto)"
type: concept
created: 2026-04-15
updated: 2026-05-04
status: good
tags: [crypto, defi, sniping, memecoins, mev, solana, ethereum, base, pump-fun, market-microstructure]
aliases: ["Sniping", "Token Sniping", "Launch Sniping", "DEX Sniping"]
related: ["[[memecoin-sniping]]", "[[liquidity-sniping]]", "[[pump-fun-bonding-curve-sniping]]", "[[token-migration-sniping]]", "[[jito-bundle-sniping]]", "[[axiom-pro]]", "[[bonkbot]]", "[[trojan-bot]]", "[[banana-gun]]", "[[maestro-bot]]", "[[photon-sol]]", "[[gmgn]]", "[[bullx]]", "[[holder-concentration-analysis]]", "[[rug-detection-checklist]]", "[[telegram-bot-trading]]", "[[mev-strategies]]"]
---

Sniping in crypto refers to the practice of executing buy transactions in the first few blocks (or first few seconds) after a tradable event - a new token launch, a liquidity addition, a contract migration, or a NFT mint - in order to capture price movement before the broader market can react. It is a latency-driven, infrastructure-heavy edge that sits at the intersection of [[market-microstructure]], [[mev-strategies]], and on-chain analytics. The category spans everything from automated [[liquidity-sniping]] of brand-new pools, to [[pump-fun-bonding-curve-sniping]] of Solana launchpads, to [[token-migration-sniping]] when a token graduates from one venue to another, to NFT mint sniping on Ethereum.

## Overview

Sniping is fundamentally a latency arbitrage. The "edge" is the time gap between when an opportunity becomes visible on-chain and when it is fully priced in by the market. Early in a launch this gap is large (seconds to minutes); a few blocks later it has collapsed. Snipers compete to compress their reaction time using a stack of:

- **Mempool subscriptions** (or geyser/yellowstone streams on Solana) to see pending transactions before they are confirmed
- **Co-located RPC nodes** to minimise network round-trip
- **Bundle submission** (e.g. [[jito-bundle-sniping]] on Solana, Flashbots on Ethereum) to bypass the public mempool and avoid being sandwiched
- **Pre-signed transactions** held in memory and broadcast on a trigger
- **Filtering layers** (rug checks, holder distribution, dev wallet history) that let the bot decide in single-digit milliseconds whether to fire

Almost all serious sniping today is bot-driven. Manual snipers using [[telegram-bot-trading]] interfaces participate in a slower second tier, paying premium fees for the bot operator's superior infrastructure.

## Categories of Sniping

### 1. Launch Sniping

Buying a token in the same block (or within the first few blocks) of its initial liquidity pool being created. On Ethereum this typically means watching for `addLiquidity` calls on Uniswap V2/V3 routers; on Solana it means watching for new Raydium / [[pump-fun-bonding-curve-sniping|Pump.fun]] / Meteora pools. The edge is largest here because price discovery has not yet started.

### 2. Liquidity Sniping

A superset of launch sniping that also includes detecting *re-additions* of liquidity, unlocks of previously locked LP tokens, or large incremental adds that signal an upcoming marketing push. See [[liquidity-sniping]] for the full taxonomy.

### 3. Pump.fun Sniping

Solana's Pump.fun launchpad uses a deterministic [[bonding-curve-analysis|bonding curve]] - buys progressively raise price until the token's market cap reaches roughly $69k, at which point it migrates to Raydium (or, since December 2025, to PumpSwap). Snipers target two distinct moments:

- **Pre-bond sniping**: buying very early on the curve, often within seconds of token creation, betting on the token reaching the migration threshold. Win rates are brutal - historically 1% or worse - but winners can return 100x+. Tools like XXYY's filter stack reportedly raised win rates to 20%+ by April 2025 by screening out bundled-holder rugs pre-bond.
- **Migration sniping**: see [[token-migration-sniping]] below.

See [[pump-fun-bonding-curve-sniping]] for the full mechanics.

### 4. Token Migration Sniping

When a token graduates from one venue to another (Pump.fun -> Raydium, Pump.fun -> PumpSwap, V2 -> V3 pool, CEX listing announcements), the change in liquidity profile typically produces a 5-50x volatility spike in the first minutes. Snipers monitor migration events via APIs like [[bitquery]] and queue buys against the new pool address before retail can find it. See [[token-migration-sniping]].

### 5. Jito Bundle Sniping

On Solana, [[jito-bundle-sniping]] involves packaging a buy transaction together with a tip into a Jito bundle, which is processed atomically and out-of-order relative to the public mempool. This both protects the snipe from being sandwiched and gives validators an incentive to land it in the next slot. Bundling has become table stakes for any serious Solana sniper since 2024.

### 6. NFT Mint Sniping

The original sniping meta. Bots monitor for new ERC-721 contracts being deployed (often by tracking known artist wallets or Manifold/Foundation factory contracts), then fire mint transactions in the same block. Profits come from listing on OpenSea/Blur immediately at a markup once the collection sells out. Largely commoditised since 2023.

## Tooling Landscape

Sniping infrastructure has bifurcated into two tiers:

### Tier 1 - Web/desktop platforms (lower fees, more screen real estate, slightly slower than Telegram bots for raw speed)

| Tool | Chain(s) | Niche |
|------|----------|-------|
| [[axiom-pro]] (axiom.trade) | Solana | Pump.fun and Solana memecoin meta. Promoted heavily by top traders such as Sajad. |
| [[photon-sol]] (photon-sol.tinyastro.io) | Solana | Fast trade execution with built-in filters and copy trading. |
| [[gmgn]] (gmgn.ai) | Solana, Base, BSC | Multi-chain analytics + execution; popular for early discovery. |
| [[bullx]] (bullx.io) | Solana, Base, ETH | Pro-focused multi-chain terminal. |
| XXYY (xxyy.io) | Solana | Pump.fun-specific sniper with advanced holder filters and bonding-curve prediction. |

### Tier 2 - Telegram bots (one-tap mobile UX, slightly higher fees)

| Bot | Chain(s) | Niche |
|------|----------|-------|
| [[bonkbot]] | Solana | The original Solana TG sniper; tight Pump.fun integration. |
| [[trojan-bot]] | Solana | Copy-trade and sniping with portfolio tools. |
| [[banana-gun]] | Solana, ETH, Base | MEV-protected one-click sniping; integrates Jito bundles. |
| [[maestro-bot]] | Multi-chain | Limit orders, copy-trading, whale tracking, real-time notifications. |

See [[telegram-bot-trading]] for the strategy-level write-up of the bot category.

### Supporting infrastructure

- **Discovery**: Dexscreener, Birdeye, Pump.fun leaderboards, GMGN trending pages
- **On-chain data**: [[bitquery]] (GraphQL feed of Pump.fun trades, OHLCV and bonding progress), Helius geyser, Triton, SolanaFM
- **Analytics dashboards**: Dune, Flipside, Birdeye whale wallets
- **Filtering**: [[holder-concentration-analysis]], [[rug-detection-checklist]], dev-wallet history scans, bundled-holder detection

## Edge Sources

Sniping edge comes from several stackable sources (see [[edge-taxonomy]]):

1. **Latency edge** - being earlier in the block ordering than competitors. Eroded fastest as more capital piles in.
2. **Informational edge** - knowing which wallets to copy, which devs are credible, which call-channels move markets. Persistent if relationships are private.
3. **Filtering edge** - having a better rug/bundle detector than the median sniper. Bots like XXYY explicitly compete on this.
4. **Risk-bearing edge** - many snipes lose 100% of stake; willingness to absorb a 90%+ loss rate in exchange for fat-tailed winners is itself an edge.
5. **Capital-flexibility edge** - small bankrolls can size into illiquid pools that whales cannot enter without crashing them.

## How Latency Wars Work

The competitive dynamic resembles a continuous high-frequency auction where the prize is the next slot's first buy of a tradeable token. The mechanics on Solana (the dominant venue in 2025-2026):

1. A new mint event hits the [[pump-fun]] program (`6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P`).
2. Bots ingesting the geyser stream see this within ~10-50ms and run their filter stack.
3. Filters that pass trigger a buy transaction packaged into a Jito bundle with a tip.
4. Validators select bundles by tip size; tips inflate during competitive launches.
5. Sandwich bots watch the same mempool and try to front-run unprotected buys, making bundling effectively mandatory.

The end state of any latency war is fee compression: tips and gas eat the edge until only the lowest-latency operators remain profitable. This is why edge decays.

## Decay Timeline

| Era | Dominant venue | Median sniper edge | What killed it |
|-----|----------------|---------------------|----------------|
| 2017-2020 | Uniswap V2 launches | Huge (10-100x on most early picks) | Bot proliferation, rug epidemic |
| 2021-2022 | NFT mints, BSC PancakeSwap | Large but rug-saturated | Mempool sniping became commoditised |
| 2023-early 2024 | Solana memecoin meta begins | Very large for early Pump.fun | Pump.fun launches Jan 2024 |
| Mid 2024-2025 | Pump.fun bonding-curve sniping | Compressed; win rates 1-5% | Bots like Axiom, XXYY professionalise |
| Late 2025 | PumpSwap migrations, ecosystem plays | Edge moves to filtering and informational layers | Filter quality became the bottleneck |
| 2026 | Multi-chain (Solana + Base + new launchpads) | Edge fragmenting; alpha leaks via call-channels | Continuous |

The general pattern: every launchpad goes through a 6-18 month edge cycle from "trivially profitable for early bots" to "only the top 1% of operators are net positive."

## Risk Profile

Sniping has the highest individual-trade variance of any commonly-practiced crypto strategy. Realistic expectations:

- 70-99% of snipes lose money (often 100% of stake to rugs/honeypots)
- Winners are fat-tailed; a 50-1000x winner can pay for hundreds of losses
- Position sizes must be small per snipe; bankroll management matters more than alpha
- Without a tested rug/bundle filter, expected value is sharply negative

See [[rug-detection-checklist]] and [[holder-concentration-analysis]] for the survival prerequisites. See [[memecoin-sniping]] for the strategy-level treatment with sizing and kill criteria.

## Related

- [[memecoin-sniping]] - the full strategy page
- [[liquidity-sniping]] - broader liquidity-event sniping
- [[pump-fun-bonding-curve-sniping]] - Pump.fun-specific mechanics
- [[token-migration-sniping]] - migration-event sniping
- [[jito-bundle-sniping]] - Solana bundle-based execution
- [[telegram-bot-trading]] - retail bot interface
- [[mev-strategies]] - related EVM block-level competition
- [[holder-concentration-analysis]], [[rug-detection-checklist]] - survival filters
- [[axiom-pro]], [[bonkbot]], [[trojan-bot]], [[banana-gun]], [[maestro-bot]], [[photon-sol]], [[gmgn]], [[bullx]] - tooling pages

## Sources

- [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]

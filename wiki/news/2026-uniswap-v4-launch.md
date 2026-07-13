---
title: "Uniswap v4 Launch — Hooks System, Lowest-Cost AMM"
type: news
created: 2026-05-14
updated: 2026-06-12
status: good
tags: [news, crypto, defi, market-microstructure]
aliases: ["Uniswap v4", "Uniswap v4 hooks", "v4 AMM launch"]
related: ["[[uniswap]]", "[[uniswap-v4-hooks-arbitrage]]", "[[aave]]", "[[dydx]]", "[[gmx]]", "[[automated-market-maker]]", "[[mev-burn-economics]]", "[[2025-defi-renaissance]]"]
event_date: 2025-01-30
markets_affected: [crypto, defi]
impact: high
verified: true
sources_count: 2
---

On **30 January 2025**, [[uniswap|Uniswap]] launched **v4** across ten chains, billing it as the most customizable and lowest-cost version of the protocol to date. The release introduces a **hooks system** that allows custom logic to be attached to individual pools, opening up programmable AMM behavior previously impossible on Uniswap. The launch followed **nine independent audits** and the largest security competition in protocol history, backed by a **$15.5M bug bounty** — building on a track record of **$2.75 trillion** in combined v2 + v3 trading volume with zero hacks. (The wiki originally logged this as a 2026 event from a secondary source; the canonical launch date per Uniswap Labs is 30 January 2025 — corrected on verification.)

## What happened

- **Multi-chain release.** Uniswap v4 deployed simultaneously on **10 chains**, extending the protocol's reach across the major EVM ecosystem.
- **Hooks system.** v4 introduces hooks — modular contracts that pool creators can attach to inject custom logic at key points in the swap lifecycle (before/after swap, liquidity adds, etc.). This enables pool-specific behavior: dynamic fees, on-chain limit orders, custom oracles, MEV protection, and more — without forking the core protocol.
- **Lowest-cost AMM to date.** v4 is positioned as the cheapest version of Uniswap by gas cost, achieved through a singleton contract architecture that consolidates all pools into a single contract and uses flash accounting to net swap deltas.
- **Security pedigree.** **Nine independent audits**, the **largest security competition in protocol history**, and a **$15.5M bug bounty** preceded the launch. Combined v2 + v3 processed **$2.75 trillion** in trading volume with **zero hacks** — a credibility anchor for the v4 release.

## Why it matters for traders

The hooks system and cost structure together change the economics of on-chain execution:

- **Arbitrage strategies become more viable.** Lower per-swap gas costs reduce the breakeven move size for cross-DEX and cross-chain arbitrage. Statistical arb strategies on stablecoin pools and correlated pairs see their fixed-cost overhead compressed. See [[uniswap-v4-hooks-arbitrage]] for the specific patterns enabled.
- **Pool-level customization invites specialist liquidity.** Hooks let pool deployers encode behavior tailored to a specific trading style — e.g. TWAMM-style time-weighted execution, dynamic fee curves keyed to volatility, or on-chain limit orders. The implication: liquidity fragments along strategy lines, and routing becomes more complex.
- **MEV searchers and stat arb favored.** The lowest-cost structure disproportionately benefits high-frequency on-chain actors. Searchers running [[mev-burn-economics|MEV]] strategies (sandwich, JIT liquidity, cross-DEX arb) capture more of the surplus from reduced gas drag. Retail directional swappers see modest fee improvements; specialist arbitrageurs see step-change improvements in unit economics.
- **Competitive pressure on peer DEXs.** v4's cost + customization combination pressures competing AMMs and order-book DEXs ([[dydx]], [[gmx]]) to differentiate on UX, derivatives, or sovereign-chain advantages rather than spot execution cost.
- **Composability with lending.** Tighter integration is plausible between v4 pools with custom hooks and lending protocols like [[aave]] — e.g. pools that auto-rebalance collateral, or that route fees into lending markets.

## Related events

- [[2025-defi-renaissance]] — the broader DeFi maturation cycle and DEX share growth that set the context for v4
- [[uniswap]] — protocol entity page
- [[uniswap-v4-hooks-arbitrage]] — strategy implications of the hooks system
- [[aave]], [[dydx]], [[gmx]] — peer DeFi protocols affected by v4's launch
- [[automated-market-maker]] — AMM concept page
- [[mev-burn-economics]] — MEV dynamics under v4

## Sources

- [[2026-04-22-gap-finder-ai-2026-major-news-stories]] — wiki ingestion source (logged the launch but mis-dated it to 2026)
- Uniswap Labs, "Uniswap v4 is here" (blog.uniswap.org/uniswap-v4-is-here) — confirms 10-chain deployment, hooks, nine audits, $15.5M bug bounty, $2.75T combined v2+v3 volume, and the **30 January 2025** launch date
- Perplexity verification (2026-06-12) — corrected the event date from 2026 to 30 Jan 2025; all magnitude facts confirmed

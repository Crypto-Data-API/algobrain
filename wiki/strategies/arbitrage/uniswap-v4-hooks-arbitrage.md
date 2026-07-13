---
title: "Uniswap V4 Hooks Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-06-21
status: excellent
tags: [arbitrage, defi, crypto, ethereum]
aliases: ["V4 Hooks Arb", "Uniswap V4 Custom Logic Arb", "Hook-Native Arbitrage"]
related: ["[[dex-pool-triangular-arbitrage]]", "[[mev-strategies]]", "[[multi-leg-arbitrage]]", "[[private-mempool-arbitrage]]"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto, defi]
complexity: advanced
backtest_status: live
edge_source: [analytical, structural, latency]
edge_mechanism: "Uniswap V4 (mainnet launch 30 January 2025) introduces 'hooks' — arbitrary smart contracts that execute before/after pool swaps. This enables custom AMM logic (dynamic fees, MEV-internalization, on-chain limit orders, custom curves, gated pools). Hook-specific behaviors create new arb surfaces invisible to V2/V3-aware bots. Edge concentrated in the first 6-18 months of any hook's deployment."
data_required: [v4-pool-state, hook-contract-bytecode, hook-specific-event-feeds, gas-oracle]
min_capital_usd: 100000
capacity_usd: 500000000
crowding_risk: medium
expected_sharpe: 2
expected_max_drawdown: 0.2
breakeven_cost_bps: 15
decay_evidence: "V4 deployed on mainnet 30 January 2025; hook-ecosystem TVL surpassed ~$1B by mid-2025. Strategy alive but each hook becomes commoditized once well-understood."
---

# Uniswap V4 Hooks Arbitrage

Trading the **[[arbitrage]] and [[mev|MEV]] opportunities created by [[uniswap|Uniswap]] V4 hooks** — arbitrary smart contracts that execute before/after pool swaps and can modify pool behavior in unprecedented ways. V4 launched on Ethereum mainnet on **30 January 2025** (whitepaper draft published June 2023) with a singleton-architecture redesign: instead of a separate pool contract per pair, all pools live in a single PoolManager contract, and per-pool customization happens via hooks. Hooks unlock custom AMM logic — **dynamic fees, MEV-internalization, on-chain limit orders, gated pools, custom curves, time-weighted average prices** — each of which creates a new arbitrage surface.

The strategy is hyper-novel: each major hook deployment opens a 6-18 month window of profitable arb until the mechanics become commoditized. It is fundamentally an [[mev|MEV]]-flavoured form of [[dex-pool-triangular-arbitrage]] — the new ingredient is that the *pool's own logic* (the hook) is part of the price-formation process, so the arbitrageur must reverse-engineer and out-model the hook itself.

> **Smart-contract & execution risk warning.** Hooks are arbitrary, often-unaudited code that runs inside the swap path. The same complexity that creates arb surfaces creates **catastrophic smart-contract risk** — Bunni V2, a V4 LP-automation hook, was hacked via a hook-logic exploit in September 2025. Hook arb requires the operator to read and simulate the hook bytecode before deploying capital; a malicious or buggy hook can trap funds, mis-settle, or be exploited mid-trade. On-chain execution additionally exposes the operator to failed-bundle gas burn, builder/priority-fee competition, and adverse selection on stale quotes (see [[mev]]).

## Edge Source

**Analytical** + **structural** + **latency**.

- **Analytical:** Each hook has unique math; understanding the hook's behavior (and edge cases) is the moat.
- **Structural:** Hooks can implement non-standard AMM behavior that V2/V3-trained arb bots miss.
- **Latency:** First-mover hooks have least competition; edge erodes as more searchers develop hook-specific bots.

## Why This Edge Exists

V4 hooks enable behaviors V3 couldn't:

| Hook Type | Function | Arb Opportunity |
|-----------|----------|------------------|
| **Dynamic fees** | Fees adjust based on volatility, time of day, oracle distance | Predict fee state and route trades when fee is low |
| **MEV-internalization** | Pool captures MEV via custom auction logic | Compete with hook for MEV; or partner via hook-aware bidding |
| **On-chain limit orders** | Pool natively supports resting orders | Liquidity sniping on limit-order fills |
| **Gated pools** | KYC-required, whitelist-only pools | Cross-pool arb between gated and ungated versions |
| **Custom bonding curves** | Non-constant-product (e.g. logistic for tokenized shares, sigmoid for memecoins) | New mathematical edges |
| **Time-weighted oracles** | Pool emits TWAP via hook; downstream protocols use it | Manipulate TWAP via gradual buying |
| **Auto-compounding LP** | Hook auto-reinvests fees into LP position | Front-run the compound |
| **Just-in-time liquidity** | Hook provides JIT liquidity for own LP | Compete with hook on JIT |

Counterparty: V2/V3-trained arb bots without hook awareness; LPs in hook pools who didn't model the hook's behavior; users of mispriced or stale-oracle hooks.

## Null Hypothesis

Under no-edge conditions, every hook pool is priced consistently with its V2/V3 siblings and with CEX reference prices, and any residual deviation sits inside the gas + swap-fee + slippage band — i.e. unexploitable. The null for a "hook-specific" edge is that apparent profits are (a) generic cross-DEX arb that any V3-aware bot would also capture, (b) selection bias from cherry-picking the handful of hooks that happened to be exploitable, or (c) gross-of-cost mirages that vanish once failed-bundle costs, priority fees, and adverse selection on stale quotes are charged. A sound test: simulate the hook's exact contract logic against historical blocks and compare hook-aware routing P&L vs a baseline V3-only arb bot over the same period — if the difference net of gas is not significantly positive, the hook adds no incremental edge.

## Variants

| Variant | Description | Holding Period |
|---------|-------------|----------------|
| **Dynamic-fee timing arb** | Route trades when fees temporarily low | Seconds-minutes |
| **MEV-internalization competition** | Build searcher bots that win the hook's auction | Per-block |
| **Custom-curve arb** | Exploit pricing inefficiency vs other AMMs | Seconds-minutes |
| **TWAP manipulation** | Slowly move TWAP via gradual orders for downstream protocols | Hours-days |
| **Limit-order sniping** | Take resting limit orders at favorable prices | Seconds |
| **Auto-compound front-run** | Front-run the hook's compounding action | Per-block |
| **Cross-hook triangulation** | Same pair, multiple hook variants — different prices | Seconds-minutes |

## Rules

1. **Hook universe scanning:** identify all V4 pools with non-trivial TVL and unique hook behaviors.
2. **Hook-behavior modeling:** for each hook, simulate the smart contract logic to predict swap outcomes.
3. **Arb surface mapping:** identify which hook behaviors create exploitable inefficiencies.
4. **Per-hook bot deployment:** each hook variant gets its own searcher bot.
5. **Continuous adaptation:** as hooks become competitive, rotate to newer or less-explored hooks.

## Implementation Pseudocode

```python
hook_pools = scan_v4_pools_with_hooks()
for pool in hook_pools:
    hook_behavior = analyze_hook_bytecode(pool.hook)
    if hook_behavior.has_dynamic_fees:
        deploy_dynamic_fee_arb_bot(pool)
    if hook_behavior.has_mev_internalization:
        deploy_mev_competition_bot(pool)
    if hook_behavior.has_custom_curve:
        deploy_curve_arb_bot(pool)

on every_block:
    for pool in hook_pools:
        opportunities = find_arb(pool, current_state)
        for opp in opportunities:
            if opp.expected_profit > gas + threshold:
                execute_via_flashbots_bundle(opp)
```

## Indicators / Data Used

- Uniswap V4 PoolManager events.
- Hook bytecode and source code (if verified).
- Hook-specific dashboards (typically deployed by the hook author).
- DefiLlama V4 category (TVL, volume).
- Eigenphi MEV tracking (post-hoc analysis).

## Example Trades

**Bunni V2 (V4 hook for LP automation)** — Bunni deployed V4 hooks for auto-rebalancing concentrated-liquidity positions (2025). Arbs identified that the rebalancing logic was front-runnable; estimated extraction ~$50-200K monthly during early deployment. Bunni was subsequently hacked via a hook-logic exploit in September 2025 — a reminder that the same complexity creating arb surfaces also creates smart-contract risk.

**Dynamic-fee hooks** — Hooks that adjust fees based on realized volatility or oracle distance. Arbs detected predictable low-fee windows and routed flow accordingly.

**MEV-Share-aware V4 hooks** — Several hooks integrated with MEV-Share to refund users; arbs that participated in the bidding captured 30-60% of refunded value.

**Limit-order V4 hooks** — Hooks supporting on-chain limit orders enabled liquidity sniping when limit orders crossed. Arbs took limit orders at premium prices when underlying moved against the limit poster.

(Full historical examples are limited as V4 launched only in January 2025; trading data fragmented across many hook variants.)

## Performance Characteristics

Early V4 hook arb desks reported 50-200% annualized returns in 2025 (concentrated in the first 6-9 months of each new hook deployment). These are **operator-reported figures, not an audited backtest**, and are survivorship-biased toward the hooks that happened to be exploitable. Sharpe high (1.5-3.0) but lumpy as hooks become commoditized.

Net-of-cost reality check: per-opportunity profits must clear several on-chain frictions before any of the headline return is real.

| Cost / friction | Magnitude | Notes |
|-----------------|-----------|-------|
| Base gas (mainnet bundle) | Variable with gas market | Each attempt costs gas whether it lands or not |
| Failed-bundle / reverted-tx burn | Recurring | Lost auctions still cost gas if not fully conditional |
| Builder / priority fees | Bid up under competition | You pay the searcher auction to get included |
| Adverse selection on stale quotes | Frequent | The "arb" was already taken; you fill against a sharper bot |
| Engineering cost (per-hook bot) | Fixed per hook | Each hook variant needs its own modelled bot |
| Smart-contract / exploit risk | Tail | A buggy or malicious hook can take the whole position |

The strategy's breakeven is roughly **15 bp round-trip** (per frontmatter), so it is only viable on pools with meaningful TVL and volatility. Below that, gas and priority fees consume the edge.

## Capacity Limits

Per-pool capacity bound by hook-pool TVL ($1-100M typical). Strategy-level capacity ~$500M.

## What Kills This Strategy

- Hook ecosystem matures and bots commoditize — the latency edge erodes as more searchers build hook-specific bots.
- V4 hooks become [[mev|MEV]]-internalized by default — the hook captures its own arb, leaving nothing for external searchers.
- Cross-DEX aggregator routing makes hook-specific edges invisible to most users (flow is internalised before it reaches the inefficient pool).
- Uniswap V5 redesign would reset the entire surface.
- Smart-contract exploit — a single bad hook can wipe a position (Bunni V2, Sept 2025); this is a per-trade existential risk, not just a return drag.
- Crowding / priority-fee inflation — when many searchers bid the same opportunity, builder fees consume the spread (see [[mev]]).

## Kill Criteria

- New-hook deployment frequency drops below 1/quarter.
- Average hook-specific arb spread compresses below 5 bp.

## Advantages

- New mathematical territory; less competition.
- Stack of sub-strategies (one per hook).
- High Sharpe in early-hook period.

## Disadvantages

- Smart contract risk per hook (audits often incomplete).
- Strategy obsolescence as hooks commoditize.
- Engineering cost (per-hook bot deployment).

## Sources

- Uniswap V4 whitepaper and Periphery documentation.
- Foundry V4 hook templates (open source).
- Atrium Academy V4 hook tutorials.
- **YouTube: "Uniswap V4 Hooks Explained" series by Smart Contract Programmer (2024).**
- **YouTube: "Bankless" interview with Hayden Adams on V4 (2024).**
- **YouTube: "Patrick Collins" Cyfrin V4 Hook coding tutorials (2024).**
- Eigenphi V4 MEV reports.
- Verified via Perplexity (sonar), 2026-06-10: V4 mainnet launch 30 Jan 2025 (blog.uniswap.org/uniswap-v4-is-here); V4 TVL >$1B by mid-2025 (oakresearch.io, acherontrading.com); Bunni V2 as V4 hook + 2025 hook exploit (mixbytes.io, acherontrading.com).

## Related

[[arbitrage]] · [[uniswap]] · [[mev]] · [[dex-pool-triangular-arbitrage]] · [[mev-strategies]] · [[multi-leg-arbitrage]] · [[private-mempool-arbitrage]] · [[intent-based-arbitrage]] · [[mev-burn-economics]] · [[limits-to-arbitrage]]

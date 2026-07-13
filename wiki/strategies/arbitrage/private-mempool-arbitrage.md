---
title: "Private Mempool Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-06-10
status: good
tags: [arbitrage, defi, crypto, market-microstructure, algorithmic]
aliases: ["Dark Mempool Arb", "Flashbots Protect Arb", "MEV-Share Arbitrage", "Bundle Arbitrage"]
related: ["[[mev-strategies]]", "[[mev-execution-guide]]", "[[dex-pool-triangular-arbitrage]]", "[[intent-based-arbitrage]]", "[[mev-burn-economics]]"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto, defi]
complexity: advanced
backtest_status: live
edge_source: [structural, latency, informational]
edge_mechanism: "Private order-flow auction venues (Flashbots Protect RPC, MEV-Share, BloXroute Private Tx, Eden Network) sell hashed/partial transaction information to whitelisted searchers. Subscribers see incoming user trades before public mempool, can construct backruns/bundles, share kickback with the user."
data_required: [protect-rpc-feed, mev-share-feed, builder-relay-bids]
min_capital_usd: 50000
capacity_usd: 100000000
crowding_risk: medium
expected_sharpe: 2.2
expected_max_drawdown: 0.1
breakeven_cost_bps: 5
decay_evidence: "Order flow migration from public mempool to private routes accelerated 2024 — ~70% of swap volume on Ethereum now flows through Flashbots Protect or similar by 2025."
---

# Private Mempool Arbitrage

Arbitrage executed against the **private order-flow auctions** (OFAs) that have replaced the public mempool as the primary venue for retail and institutional swap flow on Ethereum (and increasingly on L2s). Subscribers — Flashbots searchers, MEV-Share bidders, BloXroute private-tx clients, Eden Network bundlers — receive partial or full transaction information seconds before it would appear publicly, and bid for the right to *backrun* the trade with their own arb cycle. Profit is shared with the originating user as a "MEV refund" (kickback), creating a flywheel that pulls more order flow off the public mempool.

## Edge Source

**Structural** + **latency** + **informational**.

- **Structural:** Whitelisted access to OFA feeds is gated; only registered searchers can bid.
- **Latency:** Sub-100ms response budget; faster simulation infrastructure wins more bundles.
- **Informational:** Hashed order info (MEV-Share) reveals pool, direction, size class — enough to construct a profitable backrun.

## Why This Edge Exists

Until 2022, all swap transactions hit the public mempool, where any bot could see them and front-run, back-run, or sandwich. This destroyed retail user trust and created a tragedy-of-the-commons MEV race.

Flashbots launched **Flashbots Protect RPC** (private mempool, MEV-protected) and **MEV-Share** (programmable order flow with selective info disclosure + kickbacks). MetaMask, Uniswap front-end, and OKX Wallet now route through Protect by default. Estimated 60-75% of Ethereum swap volume runs through some form of OFA by mid-2025.

For arbs: the public mempool is a thin slice of the flow. The juicy profit lies in OFA subscription. Counterparty: smaller competitors who only watch the public mempool.

## Null Hypothesis

If the OFA auctions were perfectly competitive, searcher economic profit would be competed to zero: the winning bid would transfer essentially 100% of gross backrun value to the user (kickback) and the validator (priority fee), leaving the searcher with revenue equal to infrastructure cost — the standard all-pay-auction outcome. Under that null, hint subscriptions are worthless: win rate is proportional to bid aggressiveness, margins are zero, and P&L equals minus colocation/simulation costs. A second null: hashed/partial hints carry no information beyond what the public mempool reveals, so OFA subscribers have no construction advantage over public-mempool bots. Both nulls are currently rejected by observable data — Eigenphi and mevboost.pics attribution shows the top searcher cohort retaining a persistent 20-50% share of gross backrun value after kickbacks and fees, because simulation speed and inventory positioning differentiate bidders. The Kill Criteria below (kickback share climbing above 80%, win-rate below 1%) are precisely the conditions under which the null becomes true.

## Rules

1. Subscribe to MEV-Share, Flashbots Protect builder hints, BloXroute Private Tx, Eden, etc.
2. For each hint received: simulate the user's pending trade impact on cycle pools.
3. Compose backrun bundle: [user_tx, your_arb_tx] — atomically rebalance pools post-user.
4. Bid kickback to user (e.g. 50% of expected profit).
5. Submit bundle to MEV-Boost relay; winner is highest *user-share-adjusted* bid.
6. If win: bundle lands in the same block as user trade, atomic.

## Implementation Pseudocode

```python
on mev_share_hint(hint):
    # hint contains: pool, swap_direction, size_class, optional logs
    expected_state = simulate_user_swap(hint, pool_state)
    cycles = find_cycles_from(expected_state)
    best_cycle, gross = pick_best(cycles)
    if gross < min_threshold: return
    kickback_to_user = gross * 0.5
    bundle = [hint.tx_hash, build_arb_tx(best_cycle, kickback_to_user)]
    submit_to_relay(bundle, kickback=kickback_to_user)
```

## Indicators / Data Used

- Flashbots Protect RPC docs + MEV-Share API.
- MEV-Boost relay bid-history (Titan, Flashbots, Aestus, Agnostic, Bloxroute relays).
- Builder dominance reports (top 4: beaverbuild, Titan, rsync, Flashbots).
- mevboost.pics dashboard.
- Eigenphi MEV bundle attribution.

## Example Trade

**MEV-Share hint (illustrative, representative of 2025 flow), 2025-08-19, block ~22,968,500.**

Hint received at t=block-3s: WETH/USDC Uniswap v3 0.05% pool, sell direction, size class >$500K.

Simulation: user trade pushes WETH price down 0.18%. Backrun cycle: WETH → DAI (Curve) → USDC (Uniswap v3 0.05%) → WETH (Uniswap v3 0.30%). Gross profit estimate $620.

Bundle: kickback $310 to user, $310 to searcher gross. Gas $80, validator priority $150 (auto-set by relay rules). Net $80 to searcher. Win confirmed at block landing.

Aggregated across thousands of hints daily, top searchers extract $1-10M/year from MEV-Share alone.

## Performance Characteristics

mevboost.pics aggregated 2024-2025:
- ~85% of slots filled via MEV-Boost.
- Top 5 builders: 95% market share.
- Top 10 searchers extract estimated $50-150M/yr combined from private-route arb.
- Median bundle profit: $40-200; long tail to $50K+ for liquidations.

User kickback typical 30-70% of MEV refunded; UniswapX redistributes ~80%.

## Capacity Limits

Per-trade limited by user transaction size and pool depth. Strategy capacity ~$50-150M revenue per year for top-tier searchers; subject to flow availability.

## What Kills This Strategy

- Full-encryption mempools (Shutter Network, SUAVE) — eliminate hint info before searchers see it.
- [[mev-burn-economics|MEV-Burn]] — compresses extractable margin.
- Direct CEX/wallet routing bypasses all mempools (Coinbase wallet, OKX in some routes).
- Builder consolidation reduces auction quality.

## Kill Criteria

- Hint-feed sub revenue drops below subscription cost.
- Win-rate < 1% for 60 days.
- Average kickback to user climbs above 80% (race-to-zero on margin).

## Advantages

- Less competition than public mempool race.
- User kickback flywheel grows OFA flow over time.
- MEV-Protected means no failed sandwich risk.

## Disadvantages

- Subscription / whitelist gates entry.
- Inventory required to fill last-leg of cycles.
- Vulnerable to encrypted-mempool transitions.

## Sources

- Flashbots docs: Protect RPC, MEV-Share, MEV-Boost.
- mevboost.pics dashboards.
- Eigenphi MEV reports 2024-2025.
- Toni Wahrstätter, *MEV in Numbers* annual reports.

## Related

[[mev-strategies]] · [[mev-execution-guide]] · [[dex-pool-triangular-arbitrage]] · [[intent-based-arbitrage]] · [[mev-burn-economics]] · [[liquidation-cascade-arbitrage]] · [[multi-leg-arbitrage]]

---
title: "Slippage-Optimal Path-Finding"
type: strategy
created: 2026-04-26
updated: 2026-06-20
status: excellent
tags: [arbitrage, methodology, defi, crypto, algorithmic]
aliases: ["NPV Path-Finding", "Optimal Routing", "Convex Slippage Optimization"]
related: ["[[multi-leg-arbitrage]]", "[[dex-pool-triangular-arbitrage]]", "[[triangular-arbitrage]]", "[[mev-strategies]]", "[[automated-market-maker]]"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto, defi]
complexity: advanced
backtest_status: untested
edge_source: [analytical, latency]
edge_mechanism: "Competing arb bots size and route trades suboptimally against convex AMM slippage curves; solving the exact sizing/routing optimization captures the share of net profit naive bots leave on the table or burn by over-trading."
data_required: [amm-pool-reserves, v3-tick-maps, gas-prices, mempool-data]
min_capital_usd: 10000
capacity_usd: 5000000
crowding_risk: high
expected_sharpe: 1.0
expected_max_drawdown: 0.10
breakeven_cost_bps: 20
---

# Slippage-Optimal Path-Finding

The methodology for sizing and routing arbitrage trades to maximize net profit *after* AMM slippage, gas, and validator capture — not just maximize gross spread. Naive arb bots execute at fixed sizes or use linear approximations; sophisticated bots solve the convex optimization problem closed-form (for constant-product AMMs) or iteratively (for stableswap, weighted, concentrated-liquidity). The difference between naive and optimal sizing on a typical 4-leg cycle is 30-60% of net profit.

## Edge source

Per the [[edge-taxonomy]], this is an **analytical** edge layered on a **latency** game:

- **Analytical**: the profit function of an AMM cycle is convex (within tick ranges) and exactly computable from on-chain state. Most competing bots approximate it — fixed sizes, linear price-impact models, ignored tick crossings. Solving it exactly is pure math edge: same opportunity set, more profit extracted per opportunity, and crucially no losses from over-trading past the profit peak.
- **Latency**: the optimization only pays if the bundle lands. Block-builder auctions ([[mev-strategies]]) mean the analytical edge is monetized through bid efficiency — a bot that knows its true `profit(x*)` can bid closer to its ceiling than one that only knows a noisy estimate, winning auctions a naive bot must either lose or win unprofitably.

## Why this edge exists

The counterparties, and why they keep paying:

- **LPs in mid-liquidity pools** are passive by construction; the AMM invariant mechanically quotes stale prices after every external price move, and arbitrageurs are the designed-in mechanism that realigns them (this loss is LVR — loss-versus-rebalancing). The LPs "lose" knowingly in exchange for fees.
- **Naive arb competitors** under-extract (sub-optimal size leaves spread on the table for a follow-up trade) or over-trade (pushing past the optimum and gifting the reversal to whoever trades next block). Their mistakes are structural: closed-form sizing for mixed AMM cycles is genuinely hard (no closed form exists across Curve/Balancer/v3 ticks), so shortcuts persist.
- **Retail swappers using bad routes** create the mispricings in the first place; aggregators (1inch, Paraswap) fixed much of this for large trades, but long-tail pools and L2s still see chronically unrouted flow.

The edge decays per-venue as competitors adopt exact solvers, but regenerates with every new AMM design (v3 ticks, v4 hooks, new L2s) that breaks the previous generation's math.

## Null hypothesis

Under no-edge conditions, the priority-fee auction transfers essentially all gross profit to validators/builders: a bot with the same opportunity detection as everyone else but no sizing/bidding advantage wins only the auctions it overbids, earning ≈ 0 on wins and losing gas on failed or reverted attempts — net expectation ≤ 0. A useful falsification test: a fixed-size bot run on the same detection feed should show positive *gross* simulated P&L but flat-to-negative *net* live P&L. If the optimal-sizing variant cannot beat that baseline by a margin exceeding its extra compute/infrastructure cost, the analytical layer is adding nothing and observed profits are auction luck.

## Rules

**Universe and state**: maintain a pool graph (reserves, fee tiers, v3 tick maps) for all monitored AMMs, refreshed every block; optionally simulate pending mempool transactions to anticipate post-trade state.

**Detection (entry signal)**: search the pool graph for cycles whose product of effective rates exceeds 1 (negative-log-weight cycle detection, Bellman-Ford or specialized DFS over a pruned graph). A cycle is a candidate only if gross profit at *optimal* size exceeds the cost gate.

**Sizing**: 
- All-constant-product cycle → closed-form optimum (see below), microseconds.
- Mixed cycle (v3 / Curve / Balancer legs) → golden-section or Newton-Raphson on `profit(x)`, warm-started from the constant-product approximation.
- Large opportunity → split across parallel paths until marginal output rates equalize (water-filling).

**Cost gate and bidding**: execute only if `profit(x*) > gas + priority_bid + ε`. Bid at most `capture_ceiling × profit(x*)` (e.g., 85%); never bid into negative EV to "win."

**Execution**: submit as a single atomic transaction or builder bundle with revert protection; the trade either completes the full cycle or costs only the failed-inclusion gas (zero on private relays that drop reverting bundles).

**Position sizing / inventory**: per-trade size is set by the optimizer, not by conviction — cap it additionally at the inventory held per chain (or use flash loans to remove the cap at ~5-9 bps fee). Rebalance inventory across chains when skew exceeds ~30% of target.

**Exit**: none in the conventional sense — every trade is atomic and flat at the end of the transaction. The only persistent exposure is inventory (base assets held for gas and principal), which should be hedged or kept in the unit of account.

## Implementation pseudocode

```python
def on_new_block(state):
    for cycle in find_profitable_cycles(state.pool_graph):    # neg-log cycle search
        if all_constant_product(cycle):
            x_star = closed_form_optimum(cycle)               # Angeris-Chitra
        else:
            x_star, _ = optimal_input(cycle)                  # golden-section, below
        x_star = min(x_star, inventory_cap_or_flashloan_max)

        gross = profit_before_costs(x_star, cycle)
        gas   = base_gas + per_leg_gas * len(cycle)
        bid   = capture_ceiling * (gross - gas)               # e.g. 0.85
        if gross - gas - bid > min_profit_threshold:
            submit_bundle(build_atomic_tx(cycle, x_star), tip=bid)

def optimal_input(cycle, x_min=100, x_max=10_000_000):
    f = lambda x: -profit_after_costs(x, cycle)
    # golden-section search
    while x_max - x_min > epsilon:
        x1, x2 = golden_partition(x_min, x_max)
        if f(x1) < f(x2):
            x_max = x2
        else:
            x_min = x1
    return (x_min + x_max) / 2, profit_after_costs((x_min + x_max) / 2, cycle)
```

## The problem, formally

Given a cycle of N pools with reserves (xᵢ, yᵢ) and fees fᵢ, find input size **x** that maximizes:

```
profit(x) = output(x) - x - gas - priority_fee(x)
```

where each leg's output follows the constant-product invariant:

```
output_leg = (y_i × x_in × (1 - f_i)) / (x_i + x_in × (1 - f_i))
```

Naive approach: pick x = $10K and execute. Often loses 50%+ of available profit to suboptimal sizing — or turns a profitable cycle into a loss by over-trading (see Example trade).

## Closed-form solution: constant-product cycle

For a pure constant-product cycle (Uniswap v2, Sushiswap), the optimal input has a closed form — the Angeris-Chitra (2020) result, solvable in microseconds. The cleanest derivation composes the legs into one *virtual* constant-product pool. For two legs — leg 1 with reserves (a₁, b₁), fee multiplier γ₁ = 1 − f₁; leg 2 with reserves (a₂, b₂), fee multiplier γ₂ — the composed pool has virtual reserves:

```
E_in  = a₁ × a₂ / (a₂ + γ₁ × b₁)
E_out = γ₁ × b₁ × b₂ / (a₂ + γ₁ × b₁)
```

and the optimal input is:

```
x* = (sqrt(γ × E_in × E_out) − E_in) / γ      where γ = fee multiplier on the input leg
```

x* > 0 exactly when the cycle is profitable (γ·E_out > E_in). For N legs, apply the composition recursively. This is the formula implemented in Flashbots' open-source `simple-arbitrage` reference bot.

## Iterative solution: mixed AMM cycle

Real cycles span Uniswap v2, Uniswap v3 (concentrated), Curve stableswap, Balancer weighted. Each has a different invariant — no closed form exists for the mixed case.

Standard approach: golden-section search or Newton-Raphson on the gradient of `profit(x)`. Convex (provably) for v2 and v3 within a single tick range; quasi-convex across ticks. Convergence in 5-15 iterations from a heuristic warm-start (the all-v2 closed form using each pool's local linearization).

### Solver by AMM type

| AMM type | Invariant | Slippage curve | Optimal-sizing method | Gotcha |
|---|---|---|---|---|
| Uniswap v2 / Sushi (constant product) | `x·y = k` | Smooth, convex | Closed form (Angeris-Chitra) | None — microseconds |
| Uniswap v3 (concentrated) | `x·y = k` per tick range | Piecewise convex, discontinuous at ticks | Per-tick sub-problems, stitch at boundaries | Tick crossings (non-convex globally) |
| Curve stableswap | StableSwap invariant | Near-flat then steep | Newton-Raphson on `profit(x)` | Amplification `A` shifts the knee |
| Balancer weighted | `Π xᵢ^wᵢ = k` | Weight-dependent | Golden-section / Newton | Non-equal weights skew the optimum |
| Mixed cycle (any combination) | No closed form | Composite | Golden-section warm-started from all-v2 form | This is where the naive cohort over/under-trades |

The whole analytical edge lives in the bottom rows: the closed form handles the easy case, and the naive competitor cohort approximates the hard cases (v3 ticks, Curve, mixed) with fixed sizes or linear price-impact — leaving the 30-60% net-profit gap this strategy harvests.

## Concentrated liquidity (Uniswap v3) caveat

Uniswap v3 ticks are non-convex globally — crossing a tick boundary changes the effective slippage curve discontinuously. Slippage-optimal pathfinding must:

1. Identify which ticks the trade will cross.
2. Solve sub-problems within each tick range.
3. Stitch solutions at boundaries.

This is what 1inch Pathfinder, Paraswap, and Uniswap's auto-router do internally. Naive bots ignore tick crossings and over-trade.

## Multi-path routing (splitting)

For larger trades, splitting across multiple pools (e.g. 60% via Uniswap v3 0.05%, 40% via Sushiswap) often beats single-path. The optimal split solves:

```
maximize: sum(output_i(α_i × x))
subject to: sum(α_i) = 1, α_i ≥ 0
```

For convex pools, optimum is where **marginal output rates equalize across all routed paths** — the classical water-filling argument.

## Gas and priority-fee inclusion

Gas is non-trivial for short cycles ($30-200 typical on Ethereum L1) and the priority-fee bid is itself a function of expected profit. Joint optimization:

```
total_cost(x) = base_gas + per_leg_gas × N + priority_bid(profit(x))
priority_bid(p) = p × validator_capture_ratio  # ~0.6-0.8 on competitive opportunities, 2025
```

This recursion converges quickly (3-5 iterations) under realistic capture ratios.

## Cross-chain / cross-L2

When the cycle spans chains, the bridge step adds:
- Bridge fee (LayerZero, CCTP, etc.).
- Latency (instant bridges have premium fees; cheap bridges have 1-15 min delay).
- Inventory rebalancing cost (rather than literal bridge, often cheaper to rebalance via inventory).

Optimal pathfinding here adds a **time-discount term** to handle inventory borrowing cost over the bridge delay. See [[cross-chain-arbitrage]] and [[cross-l2-arbitrage]].

## When naive equals optimal

For high-liquidity, low-fee cycles where slippage is negligible (deep Uni v3 0.05% pools), naive fixed-size = optimal to within 1%. Most of the inefficiency lies in:
- Mid-liquidity pools ($100K-$10M TVL).
- Multi-tick v3 trades.
- Cross-AMM mixed cycles.
- Cross-chain rebalancing.

## Indicators / data used

- Pool reserves and fee tiers for every monitored AMM, per block (archive/full node or indexer).
- Uniswap v3 tick-level liquidity maps (the `tickBitmap` / liquidity-net data) — required for correct multi-tick sizing.
- Gas: base fee, per-opcode costs of the route contract, historical inclusion-tip distributions per builder.
- Mempool / private-orderflow feeds for anticipating state changes (optional but material on L1).
- Bridge fee and latency schedules for cross-chain variants.
- No conventional "indicators" — the strategy consumes raw microstructure state, not derived signals.

## Example trade

Two-pool WETH/USDC cycle, both 30 bps constant-product pools:

- Pool B (cheap): 800 WETH / 2,400,000 USDC → price 3,000
- Pool A (rich): 1,000 WETH / 3,050,000 USDC → price 3,050 (a 1.65% gap; ~1.05% net of the 60 bps round-trip fees)

Route: USDC → WETH in B, WETH → USDC in A. Composing the legs (formula above): E_in ≈ 1,335,100 USDC, E_out ≈ 1,353,300 USDC, giving **x\* ≈ 7,060 USDC**, output ≈ 7,097 USDC → **gross profit ≈ $37**, net ≈ $22 after $15 gas.

Compare naive sizing on the same opportunity:
- Naive $10,000 input → output ≈ $10,031 → $31 gross, $16 net. Optimal sizing nets ~38% more.
- Naive $50,000 input → output ≈ $48,710 → **loses $1,290 before gas**: past the profit peak, your own slippage exceeds the price gap. Over-trading converts a winning cycle into a guaranteed loss.

The asymmetry is the whole point: under-sizing costs you part of the edge; over-sizing costs you multiples of it.

### Sizing outcomes side-by-side

| Input size | Output | Gross | Net (after ~$15 gas) | vs. optimal |
|---|---|---|---|---|
| Optimal `x*` ≈ $7,060 | ≈ $7,097 | ≈ $37 | ≈ $22 | baseline |
| Naive $10,000 | ≈ $10,031 | ≈ $31 | ≈ $16 | −38% net (under-extracts past peak) |
| Naive $50,000 | ≈ $48,710 | **−$1,290** | deeply negative | over-trades into a guaranteed loss |

The optimum is a single point on a concave-down profit curve; both directions away from it cost money, but the right tail (over-trading) is unbounded while the left tail (under-trading) is bounded by the spread. This is the core reason exact sizing — not just spread detection — is the edge. See [[slippage]] for the underlying price-impact mechanics and [[automated-market-maker]] for the invariant math.

## Validation and backtesting

This strategy is uniquely hard to backtest honestly because it is on-chain and atomic. Apply the on-chain sins from [[arbitrage-backtesting-guide]]: model **one-block latency** (~12s on ETH L1, not zero), pay **gas on reverted attempts** (the failed-inclusion drag), and never assume bundles land for free. Simulate against historical per-block pool state (archive node / indexer), price the priority-fee auction at realistic 60-90% validator-capture ratios, and plot the cost-sensitivity curve: at what gas + bid level does net go to zero? Gross-only backtests of MEV arb are the single most over-stated number in crypto — the gross spread exists, but the auction takes most of it.

## Performance characteristics

With a realistic cost overlay (not simulated-gross):

- **Per-opportunity economics**: typical atomic-arb profits run $5-500 gross; on competitive opportunities the builder/validator auction captures 60-90% of gross, so net per win is often $1-50 on L1. Long-tail pools and young L2s (gas in cents, thinner competition) retain materially higher net margins.
- **Failed-inclusion drag**: bots paying public-mempool gas on reverted attempts can lose 20-50% of gross wins to failures; private bundles (drop-if-revert) reduce this to ~0 at the cost of lower inclusion priority.
- **Aggregate shape**: high win-rate, small-win, near-zero-overnight-exposure P&L — Sharpe on *deployed* capital can be high, but the honest denominator includes idle inventory across chains, which drags the strategy-level Sharpe toward the ~1.0 in frontmatter for a competent non-elite operator. Elite searchers with superior infra do far better; that is their latency edge, not this page's analytical one.
- **Decay**: per-venue net margins decay as competitors adopt exact solvers; the 30-60% naive-vs-optimal gap in the lead applies against the *naive* cohort, which shrinks every year on mature venues.

## Capacity limits

Hard-capped by the opportunity flow, not by AUM in the usual sense. Per-trade size is bounded by the optimizer itself (x* scales with pool depth — mid-liquidity pools cap trades at $5K-50K), and flash loans make principal nearly free, so extra capital buys almost nothing beyond multi-chain inventory. Aggregate atomic-arb MEV across major chains has been estimated in the low hundreds of millions of dollars per year (Flashbots / EigenPhi data, 2021-2024), split among hundreds of searchers via auctions. A single operator's realistic capacity is low single-digit $M/yr of net extraction; frontmatter `capacity_usd: 5000000` reflects working capital beyond which returns do not scale.

## What kills this strategy

- **Auction compression**: as the searcher set matures, validator capture ratios grind toward 95-100% on contested opportunities, leaving net ≈ 0 for everyone without a latency or orderflow advantage.
- **Math commoditization**: exact solvers (open-source CFMM routers, aggregator routers) close the naive-vs-optimal gap that this strategy specifically monetizes.
- **Protocol changes**: Uniswap v4 hooks, dynamic fees, MEV-internalizing AMM designs (e.g., MEV taxes, batch auctions like CoW) redirect the arb profit to LPs or users — the designed-away scenario.
- **Private orderflow**: as retail flow moves to private channels (RFQ, orderflow auctions), fewer mispricings ever reach public pools.
- **Infrastructure failure**: a bug in route construction or revert protection turns atomic "risk-free" trades into one-sided fills; a single unprotected failure on a large flash-loan trade can erase months of profit.
- **Cross-chain leg risk**: the non-atomic bridge variant carries genuine inventory/price risk during the 1-15 min delay — it is the one part of the strategy that can gap.

## Kill criteria

- Rolling 30-day net P&L (including failed-transaction gas and infra costs) < 0 → pause and re-baseline.
- Bundle win rate < 5% over the last 1,000 submitted bundles → infrastructure is uncompetitive; stand down on that chain.
- Required priority bid > 90% of gross on > 80% of won opportunities for a month → auction fully competitive; retire the venue.
- Any single execution loss > 2% of allocated capital (revert-protection or routing bug) → halt all chains until root-caused.
- Strategy drawdown > 10% of allocated capital → kill.

## Advantages

- Atomic execution: within-transaction cycles carry no overnight or directional exposure — the trade either completes profitably or reverts.
- Mathematically grounded edge: exact convex optimization against competitors using approximations; verifiable in simulation before risking capital.
- Capital-light: flash loans substitute for principal; the binding inputs are engineering and gas float.
- Regenerating opportunity set: every new AMM design, fee tier, and L2 launch resets the competitive math for a window.
- Improves any parent arb strategy: this is a methodology layer that upgrades [[triangular-arbitrage]] / [[multi-leg-arbitrage]] implementations rather than competing with them.

## Disadvantages

- Winner-take-most auctions: the analytical edge is monetized only if bundles land; without competitive infrastructure the math is worthless.
- High and continuous engineering cost (per-block state sync, tick-map handling, route contracts, revert protection) against small per-trade profits.
- Crowded and decaying on mature venues; sustainable margins migrate to long-tail pools and new chains, which demand constant re-deployment.
- Validator/builder capture (60-90% on contested flow) means most of the gross never reaches the searcher.
- Cross-chain variants reintroduce inventory and bridge risk that the atomic version is prized for avoiding.
- Smart-contract and protocol-upgrade risk on every venue touched.

## Tools and libraries

- **1inch Pathfinder** (proprietary, used in 1inch Aggregator).
- **Uniswap auto-router** (open source).
- **Paraswap router** (open source).
- **Balancer SOR (Smart Order Router)** (open source).
- **CFMM Router (Angeris-Chitra)** for academic baseline.
- **Flashbots `simple-arbitrage`** reference implementation of the two-pool closed form.

## Sources

- Angeris & Chitra, *Improved Price Oracles: Constant Function Market Makers* (2020) — derives the closed-form optimal arbitrage trade for constant-product AMMs. (Confirmed via Perplexity (sonar), 2026-06-10.)
- Adams, Salem, Robinson, et al., *Uniswap v3 Core* whitepaper (2021).
- 1inch Pathfinder blog series 2021-2024.
- Cousaert et al., *SoK: Yield Aggregators in DeFi* (IEEE ICBC 2022) — methodology overview.
- Paraswap routing blog.
- Flashbots, `simple-arbitrage` reference bot (GitHub) — open-source implementation of the composed-pool closed form.

## Related

[[arbitrage]] · [[arbitrage-overview]] · [[multi-leg-arbitrage]] · [[dex-pool-triangular-arbitrage]] · [[triangular-arbitrage]] · [[automated-market-maker]] · [[slippage]] · [[market-impact]] · [[mev-strategies]] · [[flash-loan-arbitrage]] · [[cross-chain-arbitrage]] · [[cross-l2-arbitrage]] · [[limits-to-arbitrage]] · [[arbitrage-backtesting-guide]] · [[arbitrage-parameter-cheatsheet]] · [[edge-taxonomy]]

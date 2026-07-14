---
title: "Flash Loan Arbitrage"
type: strategy
created: 2026-04-07
updated: 2026-07-14
status: good
tags: [arbitrage, crypto, defi, flash-loan, aave, dex, mev, atomic, ethereum]
aliases: ["Flash Loan Arb", "Atomic Arbitrage", "DeFi Flash Arb"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: cost-corrected

# Edge characterization (see [[edge-taxonomy]])
edge_source: [structural, latency]
edge_mechanism: "AMM pools re-price only when someone trades against them, so a swap on one pool leaves correlated pools stale for the rest of the block. A searcher borrows uncollateralised capital via a flash loan, closes the gap across pools atomically, and repays in the same transaction. The counterparty is the liquidity provider / trader whose swap moved one pool but not the others — and, increasingly, the block builder who captures most of the value via priority fees."

# Data and infrastructure requirements
data_required: [dex-pool-reserves, mempool-pending-txs, gas-and-priority-fee, flash-loan-fee-schedule, token-security-flags]
min_capital_usd: 2000
capacity_usd: 5000000
crowding_risk: high

# Performance expectations (net of gas, priority fees, and builder payment)
expected_sharpe: 1.0
expected_max_drawdown: 0.20
breakeven_cost_bps: 40

# Decay history
decay_evidence: "Atomic DEX-arb gross MEV persists (millions/week across Ethereum + L2s per EigenPhi/Flashbots data), but the share retained by the searcher has collapsed. Since Flashbots MEV-Boost (2022) and the shift to sealed-bid block-building auctions, 80-95%+ of a naive atomic arb's gross profit is bid away to the block builder/validator via priority fees. CEX-DEX arbitrage (which pros dominate with off-chain price signals) captures the majority of DEX MEV; pure public-mempool atomic arb available to a new searcher is heavily competed and frequently unprofitable after builder payment."

# Lifecycle
kill_criteria: |
  - 30-day realised net profit per included bundle < gas cost of failed attempts (negative expectancy)
  - inclusion rate < 5% of submitted profitable bundles for 14 days (losing the builder auction)
  - a single smart-contract loss event from a bug or unguarded callback
  - flash-loan provider pause/exploit on the primary venue

related: ["[[mev-execution-guide]]", "[[private-mempool-arbitrage]]", "[[jito-solana-mev-arbitrage]]", "[[dex-pool-triangular-arbitrage]]", "[[slippage-optimal-pathfinding]]", "[[cross-exchange-arbitrage]]", "[[triangular-arbitrage]]", "[[aave]]", "[[decentralized-exchanges]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Flash Loan Arbitrage

Flash loan arbitrage is a DeFi-native, fully atomic strategy: a searcher borrows uncollateralised capital from a flash-loan provider ([[aave|Aave]] at 0.09%, Balancer/Morpho at ~0%, Uniswap flash swaps), uses it to close a price gap across [[decentralized-exchanges]] within a single blockchain transaction, repays the loan plus fee, and keeps the remainder — all in one block. If the route is unprofitable, the transaction *reverts* and nothing happens except the gas spent on the failed attempt, so the searcher risks **no principal**, only gas. The naive framing ("borrow big, buy cheap on DEX A, sell dear on DEX B, keep the spread") is real but badly out of date on the economics: since the rise of sealed-bid block-building auctions ([[mev-execution-guide|MEV-Boost]] on Ethereum, Jito on Solana), the *builder/validator captures most of the gross profit* through the priority fee the searcher must bid to get included. The edge is genuine; who keeps it is the whole game.

## Edge source

Mapping to [[edge-taxonomy]], flash-loan arbitrage is **structural + latency**:

- **Structural.** An AMM pool's price is a deterministic function of its reserves and only changes when someone swaps against it. So any swap that moves Pool A necessarily leaves correlated Pools B, C… stale until arbitrage rebalances them. This stale-until-traded property is a hard-coded feature of constant-function market makers — the gap is *created mechanically* by every non-arb swap and *must* be closed by someone. Flash loans remove the capital constraint entirely, so the only gate is being the transaction that closes it.
- **Latency.** The gap exists for the remainder of the block (Ethereum ~12s; L2s/Solana sub-second). Whoever's bundle lands first in the ordering wins the whole thing; everyone else's transaction reverts. On-chain this is not a wall-clock race but an *auction* race — the winner is whoever bids the builder the highest priority fee for the top-of-block slot, which is why the value leaks to builders.

It is **not** informational (pool reserves are public) and **not** analytical (the math is a closed-form AMM invariant). The edge is the operational + auction capability to (a) spot the gap, (b) construct a profitable multi-hop route, and (c) win the block-space auction for it.

## Why this edge exists

- **AMMs are passive.** Uniswap-style pools never quote proactively; they wait to be traded against. A large swap, a mispriced oracle update, a liquidation, or a new-pool launch all leave exploitable gaps that *something* must arb. That flow never stops.
- **Flash loans democratise capital but not inclusion.** Anyone can borrow $10M with no collateral, so capital is not the moat — inclusion is. The scarce resource became top-of-block ordering, which is auctioned.
- **Composability creates long routes.** Because every DeFi protocol is a callable contract, a single transaction can chain 5-7 pools across Uniswap, Curve, Balancer, and aggregators, finding profit paths invisible to two-pool scanners. Complexity itself is a (shrinking) moat.
- **Why the searcher's slice shrank.** Pre-2022, a fast searcher in the public mempool kept most of the spread. [[mev-execution-guide|MEV-Boost]] and sealed-bid builder auctions turned inclusion into a competitive bid: to guarantee your bundle lands atop the block, you pay the builder a priority fee approaching your entire expected profit. Empirically 80-95%+ of a public-mempool atomic arb's gross now goes to the builder/validator. The residual edge concentrates in operators with **exclusive order flow** (private RFQ/CEX-DEX signals) that competitors cannot see and therefore cannot bid against.

## Null hypothesis

Under efficient, instantly-arbitraged pools with a competitive builder auction, the searcher's *net* profit is bid down to their marginal cost of doing business (gas + a thin margin for the winning bid), i.e. approximately zero economic profit. Concretely, under the null:

- Every profitable atomic route is discovered by many searchers simultaneously; the builder auction competes the priority fee up to ~100% of gross profit.
- A new entrant with only public-mempool information wins inclusion rarely, and when it wins, net profit after the required bid is ~0.
- Gas on reverted (lost-auction) attempts makes the *expected* net negative for a marginal searcher.
- Only operators with private/exclusive flow earn a persistent positive residual.

The empirical record broadly **confirms** the null for public-mempool atomic arb and **fails** it for exclusive-flow operators. Gross DEX MEV is large and persistent; searcher-retained net for a generic new entrant is thin-to-negative. **If a new deployment's realised net-per-included-bundle does not exceed the gas burned on failed attempts over 30 days, it is operating in the null regime and should stop** — the edge is real but is accruing to builders and to searchers with flow you do not have.

## Rules

### Entry conditions (per candidate route)

1. **Simulated net profit gate.** Simulate the full transaction against current pending state (Tenderly, a local EVM/`revm` fork, or an eth_call bundle sim). Require `sim_profit − flash_fee − gas − expected_builder_bid ≥ profit_floor`, with `profit_floor ≥ 0.05% of loan notional AND ≥ 2× worst-case reverted-gas cost`.
2. **Slippage-robust route.** Re-price the route against reserves *minus* any higher-priority pending swaps you can see; require it to still clear after the most adverse plausible reordering.
3. **Token safety.** Every token on the path passes a security check — no transfer tax, no honeypot, no pausable/blacklist function that could brick a leg mid-route.
4. **Provider health.** Flash-loan provider not paused; fee schedule unchanged; sufficient pool liquidity for the borrow size.
5. **Private submission.** Submit as a bundle to a builder / private relay ([[mev-execution-guide|Flashbots]], MEV-Share, or Jito on Solana) — never the public mempool, or you will be back-run/sandwiched by the very searchers you compete with.

### Exit conditions

Atomic — there is **no exit management**. The transaction either lands profitably (loan borrowed, route executed, loan repaid, profit kept, all in one block) or reverts (nothing changes, only the failed-attempt gas is lost). No position is ever held, so there is no leg risk, no inventory, no directional exposure.

### Sizing

- **Borrow size = the route's optimal size**, the amount that maximises `net_profit(size)` where marginal AMM slippage erodes the gap — a solvable one-dimensional optimisation per route, not "borrow as much as possible."
- **Bid discipline.** Bid the builder up to the point where marginal expected value of a higher inclusion probability equals the marginal fee. Do not bid into negative net.

## Implementation pseudocode

```solidity
// ArbExecutor.sol — atomic flash-loan arb (Aave v3 callback pattern, sketch)
// The whole trade lives inside the flash-loan callback; any failing require() reverts everything.
function executeArb(address asset, uint256 amount, bytes calldata route) external onlyOwner {
    POOL.flashLoanSimple(address(this), asset, amount, route, 0);
}

function executeOperation(
    address asset, uint256 amount, uint256 premium, address, bytes calldata route
) external override returns (bool) {
    require(msg.sender == address(POOL), "only aave pool");
    uint256 startBal = IERC20(asset).balanceOf(address(this));

    _runRoute(route);   // e.g. swap asset->WETH on UniV3, WETH->asset on Curve, ...

    uint256 owed = amount + premium;             // premium = 0.09% for Aave v3
    uint256 endBal = IERC20(asset).balanceOf(address(this));
    require(endBal >= startBal + owed, "unprofitable: revert whole tx");  // atomic guard
    IERC20(asset).approve(address(POOL), owed);
    return true;                                 // Aave pulls `owed`; remainder = profit
}
```

```python
# searcher.py — off-chain discovery + bundle submission (the part that actually matters)
FLASH_FEE_BPS   = 9.0            # Aave v3; use 0 for Balancer/Uniswap flash swaps
PROFIT_FLOOR_BPS = 5.0          # min net edge on loan notional after ALL costs
MIN_NET_OVER_REVERT = 2.0       # net must exceed 2x the wasted-gas cost of a lost auction

def evaluate(route, reserves, pending, gas_gwei, builder):
    size = optimal_size(route, reserves)                 # argmax net_profit(size)
    gross = simulate(route, size, reserves, adverse=pending)  # sim vs adverse reordering
    flash = size * FLASH_FEE_BPS / 1e4
    gas   = est_gas(route) * gas_gwei * 1e-9 * eth_usd()
    est_bid = builder.expected_winning_bid(route)        # what inclusion will cost
    net = gross - flash - gas - est_bid
    if net < PROFIT_FLOOR_BPS/1e4 * size:  return None
    if net < MIN_NET_OVER_REVERT * gas:    return None   # negative expectancy vs reverts
    if not tokens_safe(route):             return None   # honeypot/tax/blacklist guard
    return build_bundle(route, size, priority_fee=price_bid(net, builder))

def price_bid(net, builder):
    # bid up to where marginal P(inclusion) * net == marginal fee; never bid into negative net
    return min(0.9 * net, builder.competitive_tip())
```

The production searcher wraps this with: a mempool/websocket watcher (pending swaps, new pools, oracle updates, liquidations), a routing engine over the pool graph ([[slippage-optimal-pathfinding]]), continuous simulation, a token-safety oracle, and private bundle submission to one or more builders. The Solidity contract must be audited — an unguarded callback or missing `onlyOwner` is a total-loss bug.

## Indicators / data used

- **DEX pool reserves** — the raw price surface; the gap lives in reserve ratios across pools.
- **Pending-transaction / mempool state** — to anticipate the reordering that will happen before your bundle lands.
- **Gas + priority-fee market** — the dominant *variable* cost and the auction you must win.
- **Flash-loan provider fee + liquidity** — Aave 0.09%, Balancer/Morpho/Uniswap flash swaps ~0%.
- **Token security flags** — honeypot / transfer-tax / blacklist detection is non-negotiable before routing through a token.
- **Builder/relay inclusion stats** — your realised inclusion rate is the single best live measure of whether you are winning the auction.
- **Sources** — EigenPhi / Flashbots dashboards (MEV volumes), native RPC + `revm`/Tenderly simulation, cryptodataapi.com DEX and security endpoints for pool discovery and token screening.

## Example trade

**Opportunity (illustrative):** a $2M USDC→WETH swap hits a Uniswap v3 WETH/USDC pool, pushing its WETH price ~0.30% above a correlated Curve/Balancer pool that has not moved this block.

**Naive (2020-era) framing:**
1. Flash-borrow 600 WETH-equivalent USDC from Aave.
2. Buy WETH cheap on Curve, sell dear on Uniswap.
3. Gross ≈ 0.30% × ~$2M sizing ≈ **$6,000**.
4. Flash fee (Aave 0.09%): ~$1,800. Gas: ~$120.
5. "Net ≈ $4,080." — **This is the number that no longer survives contact with the auction.**

**Realistic cost overlay (2024-2026):**

| Cost / claim leg | Amount | Note |
|---|---|---|
| Gross spread captured | ~$6,000 | Before anyone else bids |
| Flash-loan fee (Aave 0.09%) | −$1,800 | Zero if routed via Balancer/Uniswap flash swap |
| Gas (multi-hop, ~500k gas @ 20 gwei) | −$120 | Paid even on reverts |
| **Builder priority fee (auction)** | **−$3,700 to −$3,900** | The competitive bid to land top-of-block; ~80-95% of *residual* gross |
| **Searcher net (if bundle wins)** | **~$200-500** | And only on the fraction of attempts that win inclusion |
| Expected value across attempts | near zero for a new public-flow searcher | Losses = wasted gas on the many bundles that lose the auction |

**Result:** the *same* raw opportunity that looked like a $4k win is, after the block-building auction, a ~$200-500 win *conditional on winning inclusion* — and a small gas loss when you do not. A generic new searcher competing only on public-mempool signals wins inclusion rarely and often runs at negative expectancy. The operators who keep meaningful money route **exclusive flow** (private RFQ, CEX-DEX signals) that competitors cannot see and therefore cannot bid against. The honest cost-corrected conclusion: the edge is real and large in gross, but for anyone without exclusive flow it is mostly transferred to builders.

## Performance characteristics

Cost-corrected picture (2024-2026):

| Metric | Value | Note |
|---|---|---|
| Gross DEX-arb MEV (ecosystem) | $millions/week | Large and persistent (EigenPhi/Flashbots). |
| Searcher-retained net, public flow, new entrant | ~0 to slightly negative | Builder auction extracts the rest; reverted-gas drag. |
| Searcher-retained net, exclusive flow | positive but narrow | The only durable positive-expectancy variant. |
| Sharpe (achievable, public flow) | ~1.0 or lower | Dominated by inclusion variance, not price risk. |
| Max drawdown | up to 20% | Gas bleed on lost auctions + a possible contract-bug tail. |
| Win/inclusion rate | often < 5-10% of submitted profitable bundles | You lose most auctions. |
| Breakeven cost budget | ~40 bps round-trip | Flash fee + gas + builder bid combined. |
| Principal at risk | ~0 | Atomicity is the one genuine free lunch — but only on principal, not on gas. |

**Costs the naive version ignores:** (1) the **builder priority fee**, which is the whole game and typically dwarfs the flash-loan fee; (2) **reverted-attempt gas**, paid on every lost auction, which turns expected value negative for marginal searchers; (3) **smart-contract audit/maintenance cost** and the fat-tail risk of a bug; (4) the **exclusive-flow disadvantage** — you are structurally behind operators who see order flow you cannot.

## Capacity limits

Different from most strategies: **capital is not the constraint** (flash loans are effectively unbounded up to provider liquidity). The binding constraints are:

- **Per-opportunity gap size × pool depth** — optimal borrow is capped by AMM slippage; oversizing erodes the gap you are closing. Individual routes are typically low-thousands to low-millions of gross.
- **Inclusion / auction share** — the builder captures most of the surplus regardless of your size, so scaling notional does not scale *net* proportionally.
- **Aggregate** — ecosystem gross is millions/week, but the searcher-retained slice available to a new public-flow entrant is a small fraction of that.

Realistic working capacity for a competent-but-non-exclusive-flow operator: **effectively small** — this is an infrastructure/flow game, not a capital game. Deploying more USD does not help; deploying exclusive order flow or superior builder relationships does.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Value capture by builders (Failure Mode #4, crowding — the dominant one).** Sealed-bid block auctions transfer 80-95%+ of gross to the builder/validator. The gap is closed; you just are not the one paid for closing it.
2. **Losing the inclusion auction.** Every profitable bundle is seen by many searchers; the highest bidder wins and the rest revert, paying gas for nothing. Persistent auction losses = negative expectancy.
3. **Smart-contract bug (Failure Mode #6, tail realised).** An unguarded flash callback, a missing access-control modifier, or a reentrancy hole is a total-loss event — the one place this "zero-principal-risk" strategy can actually lose principal.
4. **Adverse reordering / stale simulation.** A higher-priority pending swap changes pool reserves between your simulation and inclusion, turning a modelled profit into a revert (best case) or a partial-fill loss if the guard is weak.
5. **Token traps (Failure Mode #6).** Routing through a honeypot, transfer-tax, or pausable token can trap the borrowed funds and fail the atomic repay — or, worse, drain the contract.
6. **Provider/protocol risk.** A flash-loan provider pause or exploit, or a chain reorg, removes the venue mid-strategy.
7. **Gas-spike expectancy flip.** During congestion, reverted-attempt gas rises faster than opportunity value; the strategy's expectancy goes negative until fees normalise.

## Kill criteria

Stop (pause) the searcher on any of:

1. **30-day realised net per included bundle < gas burned on failed attempts** — negative expectancy; you are subsidising builders.
2. **Inclusion rate < 5% of submitted profitable bundles for 14 days** — you are losing the auction; more capital will not fix it.
3. **Any single smart-contract loss event** — halt, audit, and re-deploy only after fixing the root cause.
4. **Flash-loan provider pause/exploit** on the primary venue — switch providers or stop until resolved.
5. **Sustained gas regime** where modelled net is below the revert-gas floor for the target routes.

Re-deploy: contract re-audited, a fresh flow source or builder relationship secured, and a 14-day paper/canary run showing positive net-per-included-bundle above the revert-gas floor. See [[when-to-retire-a-strategy]] — the *mechanism* (stale AMM pools) never disappears, so this is pause-able, but re-entry without exclusive flow usually just re-confirms the null.

## Advantages

- **Zero principal risk.** Atomicity means an unprofitable route reverts; you lose only gas, never the borrowed capital.
- **No capital requirement.** Borrow from 1 to millions of tokens uncollateralised; capital is never the moat.
- **No leg risk, no inventory, no holding period.** Everything settles in one block.
- **Permissionless and composable.** Anyone can deploy a contract and chain arbitrary DeFi protocols into complex routes.
- **Gross opportunity is persistent.** AMMs keep generating gaps every block; the raw edge does not vanish.

## Disadvantages

- **The builder eats the edge.** Sealed-bid auctions transfer most gross profit to block builders/validators — the defining economic reality of the strategy today.
- **Requires Solidity + infra expertise.** Custom, audited contracts; a simulation pipeline; builder/relay integration.
- **Reverted-gas bleed.** Every lost auction costs gas; high failure rates flip expectancy negative.
- **Contract-bug tail risk.** The single way to lose principal is a code flaw — and it is catastrophic when it happens.
- **Exclusive-flow players dominate.** Without private order flow you are structurally behind CEX-DEX and RFQ-flow operators.
- **Chain-specific.** Each chain (Ethereum, Arbitrum, Base, Solana) needs separate contracts, builders, and infra.
- **Shrinking, competed margins.** As more searchers enter, the searcher-retained slice trends to the null.

## Sources

- Flashbots / MEV-Boost documentation and dashboards — the sealed-bid block-building auction mechanism that transfers most atomic-arb value to builders; the reason public-mempool searcher net collapsed post-2022. See [[mev-execution-guide]].
- EigenPhi and public MEV analytics — ongoing measurement of DEX-arb gross MEV (millions/week) and the split between atomic DEX arb and CEX-DEX arbitrage (the latter dominated by pros with off-chain flow).
- [[aave]] flash-loan documentation — 0.09% v3 premium, `flashLoanSimple` callback pattern; Balancer/Morpho/Uniswap flash-swap alternatives at ~0% fee.
- bZx incident (2020) — early demonstration of flash-loan atomic composability (used to manipulate an oracle and extract ~$350k); illustrates both the power and the token/oracle-trap risk of the pattern.
- [[cross-exchange-arbitrage]] — the centralised, inventory-based analogue where principal *is* at risk and there is no atomicity.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI is **not** a mempool/simulation feed — for execution you need a native RPC + `revm`/Tenderly and a builder relay. Use CryptoDataAPI for **pool discovery, token screening, and depth research** that feeds the routing engine.

**Live data:**
- `GET /api/v1/dex/trending` — trending DEX pools across Solana/Ethereum/Base/BSC/Arbitrum (candidate venues)
- `GET /api/v1/dex/new-pools` — newest launches, multi-chain (fresh pools = fresh gaps)
- `GET /api/v1/dex/token/{chain}/{address}` — token info + top pools (build the pool graph for a token)
- `GET /api/v1/dex/security/{chain}/{address}` — token security report (honeypot / rug / transfer-tax gate)
- `GET /api/v1/liquidity/depth` — per-coin depth/spread at 10/25/50/100 bps (size the route)

**Historical / research:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for correlated-pool spread research
- `GET /api/v1/backtesting/symbols` — backtest-available symbols

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/new-pools"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/security/ethereum/0xTOKEN"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-dex]], [[cryptodataapi-backtesting]].

## Related

- [[mev-execution-guide]] — how block-building auctions, bundles, and private relays actually work (essential context).
- [[private-mempool-arbitrage]] — submitting through private order flow to avoid being back-run.
- [[jito-solana-mev-arbitrage]] — the Solana equivalent (Jito bundles/tips instead of MEV-Boost).
- [[dex-pool-triangular-arbitrage]] — a common route shape flash loans finance.
- [[slippage-optimal-pathfinding]] — the routing engine that finds and sizes multi-hop paths.
- [[cross-exchange-arbitrage]] — the CEX, inventory-based analogue with principal at risk.
- [[triangular-arbitrage]] — single-venue multi-pair variant.
- [[aave]] — the canonical flash-loan provider.
- [[decentralized-exchanges]] — the venues where the gaps form.
- [[edge-taxonomy]] — structural + latency edge categories.
- [[failure-modes]] — the kill-criteria source taxonomy.
- [[when-to-retire-a-strategy]] — pause-vs-retire framework.

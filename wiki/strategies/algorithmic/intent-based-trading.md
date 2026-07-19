---
title: "Intent-Based Trading"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [crypto, defi, intents, solvers, uniswapx, cow-protocol, mev, batch-auction, account-abstraction, algorithmic]
aliases: ["Intent-Based Execution", "Solver-Based Trading", "Solving", "UniswapX Filling", "CoW Solver", "1inch Fusion Resolver"]
strategy_type: algorithmic
timeframe: intraday
markets: [crypto]
complexity: advanced
backtest_status: naive-backtested

# Edge characterization (see [[edge-taxonomy]])
edge_source: [structural, latency, informational]
edge_mechanism: "As a solver/filler you win a batch auction by returning more output than the user's limit and more than rival solvers, then capture the residual — CoW ring-matching surplus, cross-venue routing improvement, and your own inventory spread — minus gas and settlement risk; the user on the other side is paying for guaranteed MEV-protected execution and is happy to leave that residual on the table."

# Data and infrastructure requirements
data_required: [dex-pool-state, cex-quotes, dex-liquidity-depth, mempool-stream, gas-oracle, intent-orderflow]
min_capital_usd: 50000       # solver inventory + on-chain bonding/collateral
capacity_usd: 50000000       # intent orderflow settles hundreds of millions/day
crowding_risk: high

# Performance expectations (net of gas, settlement failures, inventory risk)
expected_sharpe: 1.3
expected_max_drawdown: 0.15
breakeven_cost_bps: 5        # solving is a thin-margin, high-turnover business

# Decay history
decay_evidence: "Early UniswapX/CoW solving (2023-2024) had wide margins with few competitors; win-rate and per-fill margin compressed as professional market-maker solvers (Wintermute, SCP, Barter, Propeller) industrialised the auctions. Solver concentration rose — a handful of solvers win the majority of CoW batches — and priority-ordering / private-orderflow deals raised the barrier. The user-side benefit (price improvement, MEV protection) persisted and grew; the solver-side *margin* decayed toward market-maker economics."

# Lifecycle
kill_criteria: |
  - solver batch win-rate falls below the level where fixed infra cost is covered
  - net margin per settled batch < gas + settlement-failure cost over trailing 30 days
  - repeated settlement reverts / slashing from misquoted batches
  - orderflow migrates to a venue/mechanism where you have no edge or access

related: ["[[cow-protocol]]", "[[uniswap]]", "[[1inch]]", "[[mev-strategies]]", "[[implementation-shortfall]]", "[[jit-liquidity]]", "[[concentrated-liquidity]]", "[[cross-exchange-arbitrage]]", "[[ai-solvers]]", "[[ai-mev]]", "[[slippage]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Intent-Based Trading

Intent-based trading, as a *buildable* strategy, means operating on the **solver / filler** side of an intent protocol — [[cow-protocol|CoW Protocol]] (batch auctions), UniswapX (Dutch-auction fills), or [[1inch|1inch Fusion]] (resolvers). Users sign an off-chain *intent* ("swap 10 ETH for the most USDC, at least X, by deadline") instead of a transaction; a network of competing solvers computes execution paths — routing across DEXs, matching opposing intents peer-to-peer (Coincidence of Wants), or filling from their own inventory — and the solver that returns the most output *and* beats its rivals wins the right to settle and keeps the residual surplus. It is an execution-and-market-making strategy that overlaps [[mev-strategies]], [[jit-liquidity]], and [[cross-exchange-arbitrage]], and it is the mechanism that [[implementation-shortfall]]-minimising traders exploit from the *user* side.

> Two roles, one page. The **user side** (routing your own flow through intents for better fills and MEV protection) is an *execution improvement*, not a standalone return stream — it is covered under Rules → "User-side". The **solver side** (running a bot that competes to fill others' intents) is the genuine buildable, capital-at-risk strategy, and is the focus of the frontmatter metrics.

## Edge source

Mapping to [[edge-taxonomy]] (solver side):

- **Structural (primary).** The batch-auction / Dutch-auction design *creates* a capturable surplus. CoW's ring matching lets a solver pair a seller of ETH with a buyer of ETH directly, skipping AMM fees and price impact entirely — the saved fee/impact is surplus. UniswapX's Dutch auction decays a price until a filler finds it profitable — the filler captures the gap between the decayed clearing price and true executable price. This surplus is a designed feature of the mechanism, not an opinion.
- **Latency (secondary).** Winning is a race: the solver that computes the best route and submits fastest within the auction window wins. Lower latency to DEX/CEX quotes, faster optimisation, and priority submission paths decide contested batches — the same latency logic as [[mev-strategies]].
- **Informational (tertiary).** A solver that sees the batch of intents knows the *net* order imbalance before the public market does, and a solver with private CEX inventory or off-chain market-maker quotes can price the fill better than a purely on-chain competitor. That informational/inventory advantage is what lets professional market-maker solvers dominate.

There is a **risk-bearing** component too: filling from inventory means warehousing the position and its price risk until it can be unwound, exactly like [[jit-liquidity]] and CEX market-making.

## Why this edge exists

1. **Users pay for certainty and protection.** The counterparty is a user who wants a *guaranteed* MEV-protected fill with no gas-estimation or route-building. They rationally accept a price that is better than a naive DEX swap but still leaves a residual for the solver — they are buying insurance against sandwiching and execution failure. The solver is paid to bear that execution risk (the intent has a fixed minimum-out; the solver eats any adverse move between winning and settling).
2. **Coincidence-of-wants surplus is real and free.** When two intents offset, the AMM fee and price impact that both would otherwise pay simply do not exist. A solver that finds the match captures (or shares) that saved cost. This surplus grows with orderflow density and cannot be arbitraged away — it is created by the batching.
3. **Fragmented liquidity rewards the best router.** The best execution path across dozens of DEXs, private market makers, and CoW matches is genuinely hard to compute in the auction window. Solvers with better routing, more venue access, and private inventory consistently beat naive competitors — a durable, if competitive, informational/latency edge.

## Null hypothesis

Under a no-edge world, the batch auction is perfectly competitive: solvers bid the surplus down to their marginal cost (gas + inventory risk), so the *user* captures all price improvement and the solver's net margin is zero. In that world:

- Winning-solver net margin per batch equals gas plus a fair risk charge — no economic profit.
- No solver can systematically win contested batches (routing/inventory advantages are equalised).
- CoW ring-matching surplus is fully rebated to users, not retained by solvers.

The null is **the intended end-state and largely true for the majors.** CoW explicitly rebates surplus to users, and on liquid ETH/USDC batches solver margins are thin — the mechanism is working as designed and the *user* wins. The null is *rejected* where a solver has a genuine edge: superior routing, private CEX inventory to internalise fills, exclusive orderflow, or lower latency — those solvers retain economic margin. If a solver's net margin per settled batch is indistinguishable from gas cost for 30+ days, it has no edge over the field and should stop paying to compete.

## Rules

### Solver-side (the tradeable strategy)

Compete to fill a batch/intent when **all** hold:

1. **Solvable surplus exists:** your best computed route (DEX legs + CoW matches + inventory fill) returns output ≥ the user's minimum-out **plus** a margin ≥ your gas + risk charge + target profit.
2. **Beat the field:** your solution's total surplus exceeds your estimate of rival solvers' best (or you have exclusive/priority access to this batch).
3. **Inventory/quote freshness:** any inventory leg is priced off a CEX/[[cross-exchange-arbitrage|cross-venue]] quote no older than the auction window; stale quotes are rejected.
4. **Settlement safety:** simulate the settlement transaction; it must succeed and net-out positive after worst-case gas at current [[mev-strategies|priority-fee]] levels.
5. **Slashing/bond headroom:** posting the solution does not risk the solver's bond beyond a set fraction on a single batch.

**Unwind:** any inventory taken on to fill (not offset by a CoW match) is hedged/unwound on a CEX or DEX immediately, targeting a hold of seconds, not minutes.

**Sizing:** cap inventory-at-risk per batch ≤ a fixed fraction of solver capital; never let a single misquoted batch exceed the bond/slashing tolerance.

### User-side (execution improvement, not a return stream)

- Route trades ≥ ~$10k notional (where MEV/impact savings exceed the intent latency cost) through CoW/UniswapX/Fusion rather than a naive DEX swap.
- Set the minimum-out from a live [[slippage|depth-aware]] quote, not a naive spot price.
- Prefer intents for tokens/pairs with deep solver competition (majors); fall back to direct routing for long-tail tokens no solver will fill well.
- Measure realised price vs an [[implementation-shortfall]] benchmark to confirm the intent path is actually improving fills.

## Implementation pseudocode

```python
# solver.py — decision core for a CoW / UniswapX / Fusion solver
MIN_MARGIN_BPS   = 3        # required surplus over user min-out, in bps of notional
MAX_INV_FRAC     = 0.10     # <=10% of solver capital warehoused per batch
GAS_SAFETY_MULT  = 1.5      # buffer over current priority-fee estimate

def solve_batch(batch, venues, inventory, gas_oracle, rival_est):
    best = optimize_execution(          # the hard, competitive part
        intents=batch.intents,
        cow_matches=find_ring_matches(batch.intents),   # peer-to-peer offsets
        dex_routes=route_across(venues),                # Uniswap/Curve/Balancer/...
        inventory=inventory,                            # internalise from own book
    )
    if best is None:
        return no_bid("no feasible solution")

    surplus_bps = (best.total_out - batch.total_min_out) / batch.total_notional * 1e4
    gas_cost    = gas_oracle.settlement_cost(best.txn) * GAS_SAFETY_MULT
    gas_bps     = gas_cost / batch.total_notional * 1e4
    risk_bps    = inventory_risk_charge(best.inventory_legs)   # warehouse price risk

    net_bps = surplus_bps - gas_bps - risk_bps
    if net_bps < MIN_MARGIN_BPS:
        return no_bid(f"margin {net_bps:.1f}bps below floor")
    if best.inventory_notional > MAX_INV_FRAC * inventory.capital:
        return no_bid("inventory cap exceeded")
    if surplus_bps <= rival_est.best_surplus_bps:
        return no_bid("rival solver beats us")
    if not simulate(best.txn).success:
        return no_bid("settlement would revert")

    return submit_solution(
        solution=best,
        hedge_plan=hedge_uncovered_legs(best.inventory_legs),  # unwind on CEX/DEX
        priority_fee=gas_oracle.competitive_tip(),
    )
```

Production adds: streaming DEX pool-state and CEX quotes; a fast route optimiser (mixed-integer / heuristic solver); a private submission path; a settlement simulator; a bond/slashing monitor; and an inventory hedger that unwinds internalised fills within seconds.

## Indicators / data used

- **Intent / batch orderflow** — the auction feed from CoW (order book / auction API), UniswapX (Dutch-order feed), or 1inch Fusion (resolver feed). The raw signal; access is the barrier.
- **DEX pool state & liquidity depth** — live reserves/tick liquidity across Uniswap, Curve, Balancer, etc., for routing and price-impact estimation. See [[slippage]], [[concentrated-liquidity]].
- **CEX / off-chain quotes** — for pricing internalised (inventory) fills and hedging; [[cryptodataapi]] `market-data/ticker/price` and `hyperliquid/l2-book` give the reference and depth for the unwind leg.
- **Gas / priority-fee oracle** — settlement cost dominates thin margins; the single most important cost input alongside inventory risk.
- **Mempool** — to gauge competitive priority-fee levels and settlement inclusion.
- **Liquidity/depth analytics** — `liquidity/depth` for spread/impact context at 10/25/50/100 bps when sizing an inventory fill.

## Example trade

**Setup (CoW Protocol batch):**

- Batch contains, among others: Intent A — sell 40 ETH for ≥ 125,600 USDC; Intent B — buy 25 ETH with ≤ 78,900 USDC. ETH mid ≈ $3,150.
- **Ring match:** 25 ETH of A offsets B directly (Coincidence of Wants) — no AMM fee, no price impact on that slice.
- **Remainder:** 15 ETH of A routed across Uniswap V3 + Curve; solver internalises 5 ETH from its own inventory at the CEX mid.

**Solve:**

- CoW-matched 25 ETH: both users get mid-price fills; the saved ~30 bps AMM fee + impact ≈ surplus of ~$236, shared per protocol rules — solver retains a slice.
- Routed 15 ETH: solver returns ~$47,300 vs the user minimum of ~$47,100 → ~$200 improvement, of which the solver's margin after routing cost is ~$40.
- Internalised 5 ETH: filled from inventory at CEX mid, hedged instantly on [[hyperliquid]]/Binance — captures ~1-2 bps inventory spread ≈ ~$3.
- **Gas to settle the batch:** ~$18 at current priority-fee (buffered ×1.5 = $27 reserved).

**Outcome:**

- Solver wins the batch (its total surplus beats rivals'), settles on-chain, and nets ~$45-60 after gas and the inventory hedge — on a batch moving ~$220k of notional. That is **~2-3 bps net margin**, which is why solving is a *thin-margin, high-turnover* business: profit comes from winning many batches per day, not from any single fat fill.

**User-side view of the same trade:** Intent A's seller received ~$47,300 for the routed 15 ETH vs ~$47,050 from a naive Uniswap swap, and paid no gas and took no sandwich risk — a clean [[implementation-shortfall]] improvement, but not a "return" they earned, just a cost they avoided.

## Performance characteristics

**Solver side** is a competitive market-making business with a thin per-fill margin and high turnover:

| Metric | Realistic value | Note |
|---|---|---|
| Net margin per settled batch | ~1-5 bps | After gas + inventory risk; compresses with competition. |
| Batch win-rate | venue/edge-dependent | A few solvers win most CoW batches; the long tail wins little. |
| Sharpe (net) | ~1.3 | Steady in normal flow; drawdowns from misquoted/adversely-selected fills. |
| Max drawdown | ~15% | Inventory left un-hedged into a fast move, or settlement reverts. |
| Capital use | inventory + bond | Mostly turnover, not held capital; capital funds internalisation + slashing bond. |
| Breakeven cost budget | ~5 bps round trip | Gas + hedge + settlement-failure reserve; below this there is no business. |

**Cost overlay (never naive):**

- **Settlement gas / priority fee:** the dominant cost. Ethereum-mainnet batch settlement can be $10-100+; on L2s far cheaper. A solver that wins on gross surplus but misjudges gas settles at a loss.
- **Settlement-failure / revert cost:** a reverted settlement wastes gas and can risk the bond — reserve for it.
- **Inventory hedging cost:** CEX taker/maker fees + slippage on the unwind leg for internalised fills.
- **Adverse selection:** you disproportionately win the batches you *mis*-price too aggressively; a disciplined margin floor and rival-estimate are essential.
- **Infra / access cost:** low-latency quotes, private orderflow deals, and optimiser compute are real fixed costs that the per-batch margin must amortise.

A naive "solver P&L = gross surplus" backtest is meaningless — the entire economics live in gas, inventory risk, and win-rate against a professional field.

## Capacity limits

- **Solver side:** capacity scales with *orderflow*, which is large — CoW/UniswapX/Fusion collectively settle hundreds of millions of dollars per day. A capable solver can fill tens of millions per day, bounded by (a) available intent flow it can win, (b) inventory it can warehouse and hedge, and (c) bond/slashing limits. Working capacity for a serious operator: **tens of millions of dollars of daily settled notional**; the constraint is *winning* flow, not deploying capital.
- **User side:** effectively uncapped as an execution method for the majors; for long-tail tokens, capacity is limited by whether any solver will competitively fill the intent at all.
- **Concentration caveat:** because a handful of professional solvers win most batches, realistic capacity for a *new* entrant is far smaller until it builds routing/inventory/access parity.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Solver concentration / crowding (#4).** The dominant risk. Professional market-maker solvers (with private inventory, exclusive orderflow, and superior routing) win the majority of batches; a marginal solver's win-rate and margin collapse to below its fixed cost.
2. **Margin compression (#4/#5).** As the mechanism matures, surplus is increasingly rebated to users by design (CoW's explicit goal), squeezing solver economics toward zero.
3. **Gas / settlement-cost spikes (#6).** A priority-fee spike between winning and settling can turn a profitable batch into a loss; misjudged gas is a recurring bleed.
4. **Adverse selection.** You win exactly the batches you underpriced; without a rival-estimate and margin floor, the win-set is negatively selected.
5. **Inventory risk (tail — #6).** An internalised fill left un-hedged into a fast move is a directional loss; the hedge leg can slip or fail.
6. **Orderflow migration / access loss (#5).** Flow moves to a new venue/mechanism, or an exclusive-orderflow deal cuts you out of the batches worth winning.
7. **Slashing / settlement reverts (#7).** A buggy solution that reverts or violates constraints can be slashed, an operational-collapse risk unique to bonded solving.

## Kill criteria

Pause (the mechanism persists; your *access/edge* is what lapses) on any of:

1. **Batch win-rate below the level that covers fixed infra cost** over a trailing 30-day window.
2. **Net margin per settled batch < gas + settlement-failure reserve** over trailing 30 days.
3. **Repeated settlement reverts or a slashing event** from misquoted batches.
4. **Orderflow migrates** to a venue/mechanism where you have no routing edge or no access.
5. **Inventory-leg hedge slippage** consistently exceeds the captured spread (internalisation no longer pays).

Re-deploy when a routing/inventory/access improvement restores positive net margin in a paper run across ≥ 100 batches. See [[when-to-retire-a-strategy]].

## Advantages

- **Structural, designed surplus** — CoW ring-matching and Dutch-auction gaps create capturable value that is not an opinion or a forecast.
- **Capital-light, high-turnover** — most P&L is turnover on thin margins; large held capital is not required beyond inventory + bond.
- **Diversifying** — solver P&L is driven by flow and execution skill, largely uncorrelated with directional crypto beta.
- **Composable with adjacent edges** — routing, [[jit-liquidity]], and [[cross-exchange-arbitrage]] inventory all feed the same optimiser.
- **User-side is pure improvement** — for a trader with flow, routing through intents strictly reduces [[implementation-shortfall]] and MEV leakage with no downside beyond mild latency.

## Disadvantages

- **Professionalised, concentrated field** — a few solvers win most batches; new entrants face steep routing/inventory/access barriers.
- **Thin margins, gas-dominated** — a small priority-fee misjudgment erases the profit on a batch.
- **Adverse selection** — the batches you win are biased toward the ones you mispriced.
- **Bond/slashing risk** — a buggy solution is an operational total-loss vector absent from simple arb.
- **Inventory / hedge risk** — internalised fills warehouse price risk that must be unwound flawlessly.
- **Access-dependent** — exclusive orderflow and private RPC deals increasingly gate the profitable batches.
- **Opaque to the user** — on the user side, the execution path is hard to verify; users must benchmark to confirm they are actually getting best execution.

## Sources

- [[cow-protocol|CoW Protocol]] documentation — batch auctions, solver competition, Coincidence-of-Wants ring matching, surplus rebate to users (docs.cow.fi).
- UniswapX whitepaper and docs — Dutch-auction intent fills and filler economics ([[uniswap]] labs).
- [[1inch|1inch Fusion / Fusion+]] documentation — resolver model and gasless intent settlement.
- ERC-4337 account-abstraction spec — the gasless-intent enabling layer (eips.ethereum.org).
- Flashbots / MEV research on orderflow auctions and solver concentration (2023-2025) — evidence for the margin/concentration decay in frontmatter; see [[mev-strategies]], [[ai-solvers]], [[ai-mev]].
- Related wiki strategies: [[jit-liquidity]], [[cross-exchange-arbitrage]], [[implementation-shortfall]].

## Getting the Data (CryptoDataAPI)

CryptoDataAPI does not serve the intent/auction orderflow itself (that comes from the CoW/UniswapX/Fusion APIs) — it supplies the **reference prices, DEX pool discovery, and hedge-leg depth** a solver needs for routing and inventory pricing.

**Live data:**
- `GET /api/v1/dex/trending` — active DEX pools across chains (routing universe)
- `GET /api/v1/dex/token/{chain}/{address}` — token info + top pools (venue-level liquidity for routing)
- `GET /api/v1/market-data/ticker/price?symbol=ETHUSDT` — CEX reference price for pricing internalised fills
- `GET /api/v1/hyperliquid/l2-book?coin=ETH` — L2 order-book depth for the hedge/unwind leg
- `GET /api/v1/liquidity/depth` — per-coin depth/spread at 10/25/50/100 bps (price-impact context)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1m&limit=1000` — for backtesting route/margin models
- `GET /api/v1/backtesting/klines` — deep OHLCV archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/liquidity/depth"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/l2-book?coin=ETH"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-dex]] (also [[cryptodataapi-market-data]], [[cryptodataapi-hyperliquid]]).

**Live dashboards:** [order-book depth](https://cryptodataapi.com/quant-order-books) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Routing universe** — refresh `GET /api/v1/dex/trending` and per-token `GET /api/v1/dex/token/{chain}/{address}` to keep the solver's venue map current
- **Inventory pricing** — `GET /api/v1/market-data/ticker/price` (CEX reference) plus `GET /api/v1/hyperliquid/l2-book?coin=ETH` (hedge-leg depth) price internalised fills before bidding an auction
- **Regime gate** — `GET /api/v1/liquidity/regime` fragility score — widen solver margins when books are fragile; `GET /api/v1/quant/market` for vol-state awareness on the unwind leg
- **Backtest** — route/margin models against `GET /api/v1/backtesting/klines` — honest window: 1m bars only since 2026-03-30 (the resolution auction-latency studies need); 1h/4h/1d reach 2017-08 for coarser work
- **Tips** — the intent/auction orderflow itself stays on the CoW/UniswapX/Fusion APIs; check `GET /api/v1/liquidity/depth` before quoting size on thin pairs

## Related

- [[cow-protocol]] — batch-auction intent protocol; the canonical solver venue
- [[uniswap]] — UniswapX Dutch-auction intents
- [[1inch]] — 1inch Fusion resolver model
- [[mev-strategies]] — the extraction family solving overlaps and protects users from
- [[implementation-shortfall]] — the execution benchmark intents optimise toward (user side)
- [[jit-liquidity]] — inventory-provision cousin that feeds the same optimiser
- [[concentrated-liquidity]] — the DEX liquidity structure solvers route across
- [[cross-exchange-arbitrage]] — the hedge/unwind and inventory-pricing counterpart
- [[ai-solvers]], [[ai-mev]] — machine-learning approaches to route/margin optimisation
- [[slippage]] — the price-impact cost routing minimises
- [[edge-taxonomy]] — where this sits among the six edge categories
- [[failure-modes]], [[when-to-retire-a-strategy]] — the kill-criteria framework
- [[cryptodataapi]] — the reference-data layer; see [[cryptodataapi-dex]]

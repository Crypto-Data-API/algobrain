---
title: "JIT Liquidity"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: draft
tags: [crypto, defi, liquidity, uniswap, mev, concentrated-liquidity, amm, just-in-time, ethereum, algorithmic]
aliases: ["Just-In-Time Liquidity", "JIT LP", "JIT Liquidity Provision", "Sandwich-Free LP"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: untested

# Edge characterization
edge_source: [latency, informational, structural]
edge_mechanism: "Mempool visibility of a large pending swap lets a searcher mint ultra-concentrated liquidity around the execution price in the same block, capture the bulk of that single swap's fee, and burn immediately — collecting fee income with only single-block inventory risk, financed by a flash loan."
data_required: [mempool-pending-txs, dex-pool-state, tick-liquidity, gas-price, builder-relay]
min_capital_usd: 5000
capacity_usd: 5000000
crowding_risk: high

# Performance expectations (net of gas, builder tip, single-swap LVR)
expected_sharpe: 2.0
expected_max_drawdown: 0.15
breakeven_cost_bps: 0

# Decay history
decay_evidence: "JIT margins compressed sharply as searcher competition and the PBS/builder-auction market matured post-2022; a small number of sophisticated teams win most opportunities, and Uniswap v4 hooks plus JIT-resistant pool designs can now penalize or block same-block mint-and-burn. Profitability is increasingly concentrated in the largest, most clearly-uninformed swaps."

related: ["[[concentrated-liquidity]]", "[[loss-versus-rebalancing]]", "[[mev-strategies]]", "[[flashbots]]", "[[mempool]]", "[[uniswap]]", "[[impermanent-loss]]", "[[automated-market-maker]]", "[[adverse-selection]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# JIT Liquidity

Just-in-time (JIT) liquidity is an [[mev-strategies|MEV]] strategy in which a searcher, seeing a large swap sitting in the [[mempool|mempool]], mints an ultra-concentrated [[concentrated-liquidity|liquidity]] position (often just one or two ticks wide) around that swap's execution price *in the same block, immediately before the swap*, captures the bulk of the swap's fee, and burns the position immediately after — all atomically. By concentrating capital into the exact tick the swap will trade through, the JIT provider grabs the disproportionate share of that one trade's fee (typically 80–95%) that would otherwise be spread across passive [[concentrated-liquidity|range LPs]]. Because the position exists for a single block, the liquidity can be **flash-loaned**, making JIT a near-zero-capital, single-block bet whose only real costs are gas, the builder tip, and the [[loss-versus-rebalancing|LVR]] of that one swap. Its profitability hinges entirely on the pending swap being *uninformed*.

## Edge source

Per [[edge-taxonomy]], JIT is a **latency + informational + structural** edge:

- **Latency / informational.** The edge originates in *seeing the pending swap before it executes* — public-mempool visibility on Ethereum L1, or an order-flow relationship on private-flow venues. Whoever detects the large swap and constructs a valid bundle fastest wins the right to provide the liquidity. This is a pure information/speed edge over passive LPs who cannot react within the block.
- **Structural.** The AMM pays swap fees pro-rata to in-range liquidity. By momentarily owning almost all the in-range liquidity, the JIT provider structurally captures almost all the fee — a mechanical consequence of how [[automated-market-maker|AMM]] fee distribution works, not a forecast.

Crucially, JIT is *also* an [[adverse-selection]] trade: the provider ends the block holding the other side of the swap (short the asset a big buyer just bought). Against uninformed flow that residual is harmless; against informed flow it is the whole risk.

## Why this edge exists

- **Large swaps are lumpy and visible.** A $500k router order sits in the public mempool for a block or two before inclusion. That visibility is the exploitable asymmetry — passive LPs committed their liquidity hours ago and cannot re-concentrate in time.
- **Fee distribution rewards concentration absolutely.** In a concentrated-liquidity AMM, the fee on a swap is split by *share of active liquidity at the traded ticks*. Minting a huge, one-tick position just before the swap makes the JIT provider ~all of that share for that trade, then it exits before bearing any ongoing risk.
- **Flash loans remove the capital constraint.** Because mint → swap-executes → burn is atomic within one bundle, the liquidity can be borrowed and repaid in the same transaction, so the strategy needs almost no standing capital — only gas and tip. That collapses the barrier to a pure execution/latency game.
- **The counterparty is usually uninformed.** The archetypal JIT target is a large aggregator/router market order executing for reasons unrelated to short-horizon fair value. The single-swap LVR against such flow is small relative to the fee captured.

## Null hypothesis

Under a no-edge world, JIT nets zero after costs:

- The fee captured on the target swap exactly equals gas + builder tip + the single-swap LVR (the adverse inventory left after the swap). No searcher would systematically profit.
- Builder-auction competition bids away any surplus: the priority fee/tip required to win inclusion rises until expected profit is zero.
- Against a representative mix of pending swaps, the informed fraction inflicts LVR that offsets the fee earned on the uninformed fraction.

The null is rejected only when a searcher can **select** swaps whose captured fee reliably exceeds gas + tip + LVR — i.e., large, clearly-uninformed swaps in high-fee-tier pools — and win the bundle auction at a tip below that surplus. As competition (crowding) and builder-auction efficiency rise, the surplus compresses toward the null, which is exactly the documented decay.

## Rules

### Detection and trigger (entry)

1. **Monitor the mempool** for pending swaps on target pools (Uniswap v3/v4 and forks) above a size threshold — e.g. notional ≥ $200k, where the fee can clear gas + tip.
2. **Filter for uninformedness.** Prefer aggregator/router flow and large single orders; deprioritize swaps that look like informed directional flow (e.g. following a price catalyst, or from addresses with a toxic markout history). This filter *is* the edge; misjudging it is the loss.
3. **Compute the tightest capturing range.** Determine the minimal tick range around the swap's execution path that will absorb the trade. Narrower = higher fee share but higher risk of the swap walking out of your range (capturing less). Size liquidity `L` so your share of active liquidity at the traded ticks is maximized without over-providing.
4. **Check the economics gate:** proceed only if `expected_fee_capture > gas(mint) + gas(burn) + builder_tip + expected_single_swap_LVR`.

### Bundle construction and exit

Construct an atomic bundle (order matters):
- **(a)** Flash-loan the two tokens (or one, minting single-sided at the edge) and **mint** the concentrated position at the target ticks.
- **(b)** The victim swap **executes** against your liquidity (you now hold the post-swap inventory).
- **(c)** **Burn** the position, collect fees, unwind/return inventory, and **repay the flash loan**.
- Submit via [[flashbots|Flashbots]] / a block builder with a priority tip. If any leg fails or the swap is not included as expected, the whole bundle **reverts** — no partial exposure.

Exit is automatic: the position never survives the block. Any residual inventory delta from the swap is unwound within the same bundle (or immediately after via a follow-on swap), so the strategy targets flat at block end.

### Sizing

- **Liquidity** is bounded by the swap size — providing more than the swap consumes just dilutes your own fee share and increases the inventory you must unwind.
- **Tip** is set by the bundle auction: bid up to the point where expected profit net of tip stays positive; over-bidding hands the surplus to the builder.
- **Per-opportunity risk cap** on the single-swap LVR you are willing to eat if the swap turns out informed.

## Implementation pseudocode

```python
# jit_liquidity.py — mempool-triggered single-block LP bundle
MIN_SWAP_USD   = 200_000     # only chase swaps large enough to clear gas+tip
FEE_TIER       = 0.0030      # 30 bps pool
def on_pending_swap(tx, pool, gas_price, builder):
    if tx.notional_usd < MIN_SWAP_USD:
        return
    if looks_informed(tx):                       # THE edge: skip toxic/directional flow
        return

    # tightest range that captures the swap path
    lo, hi   = capturing_ticks(pool, tx)         # 1-2 ticks around execution
    L        = liquidity_for_swap(pool, tx, lo, hi)
    fee_cap  = tx.notional_usd * FEE_TIER * expected_share(pool, L, lo, hi)  # ~80-95%

    gas_cost = (GAS_MINT + GAS_BURN) * gas_price
    lvr_swap = single_swap_lvr(tx, lo, hi)       # inventory left after the swap
    tip      = builder.min_tip_to_win(pool)

    if fee_cap <= gas_cost + tip + lvr_swap:     # economics gate
        return

    bundle = [
        flash_loan_and_mint(pool, lo, hi, L),    # (a) borrow + mint concentrated position
        tx,                                      # (b) victim swap executes against our LP
        burn_collect_unwind_repay(pool, lo, hi), # (c) burn, collect fees, unwind, repay loan
    ]
    builder.submit_bundle(bundle, tip=tip)       # atomic; reverts entirely on any failure
```

The real searcher adds: simulation of the bundle against the current state before submitting; multi-builder submission for inclusion probability; an `looks_informed` model trained on address markout history; and back-run unwind routing for any residual inventory.

## Indicators / data used

- **Pending mempool transactions** — the trigger; large swaps on target pools before inclusion.
- **DEX pool state and tick liquidity** — current price, active-liquidity distribution, and competing liquidity at the traded ticks (sets your fee share).
- **Gas price / base fee** — the dominant cost and the economics gate.
- **Builder / relay tip market** — the minimum tip to win inclusion.
- **Address markout / flow-toxicity history** — to score whether the pending swap is informed (the loss-avoidance model). Related: [[adverse-selection]], [[loss-versus-rebalancing]].

## Example trade

**$200,000 USDC→ETH swap, Uniswap v3 ETH/USDC 30 bps pool, Ethereum L1.**

- **Detect:** the pending swap appears in the mempool; size ($200k) clears the threshold and the source is an aggregator router (uninformed filter passes).
- **Range:** mint a ~1-tick position around the execution price using flash-loaned funds, sized to absorb ~all of the swap.
- **Fee capture:** swap fee = $200,000 × 0.30% = $600. JIT share ≈ 90% → **~$540**.
- **Costs:** mint + burn gas at a moderate base fee ≈ $40; builder tip ≈ $30; single-swap LVR (residual ETH short unwound in-bundle) ≈ $20 against uninformed flow.
- **Net:** ~$540 − $40 − $30 − $20 ≈ **+$450 in a single block**, near-zero standing capital (liquidity flash-loaned).

**Informed-swap failure variant.** The same setup, but the $200k buy is the first leg of an informed accumulation and ETH keeps ripping after the swap. The JIT provider is left short ETH at the post-swap price; unwinding costs more than the $540 fee — the single-swap LVR balloons to, say, $900, turning the trade into a **−$430** loss. This is the entire risk of JIT: the fee is fixed and small; the adverse-selection tail on informed flow is the variable that decides the P&L. The `looks_informed` filter is the strategy.

## Performance characteristics

Realistic, cost-corrected picture:

| Metric | Value | Note |
|---|---|---|
| Per-win capture | 80–95% of swap fee | Minus gas + tip + single-swap LVR |
| Win rate | high on filtered flow | Most large router swaps are uninformed |
| Loss distribution | fat right tail on informed swaps | The adverse-selection tail dominates losses |
| Standing capital | ~0 (flash-loaned) | Only gas + tip + operational buffer |
| Gas + tip per attempt | $30–$150 (L1, base-fee dependent) | The recurring friction |
| Sharpe | ~2.0 in benign flow | Collapses when informed flow rises or competition wins the auctions |
| Max drawdown | 10–15% | A cluster of misjudged-informed swaps |

The economics are a filter problem, not a forecasting problem: capture is nearly deterministic; profitability is set by (a) winning the bundle auction cheaply and (b) not providing into informed flow.

## Capacity limits

Capacity is bounded **per opportunity by the size of the swaps you can profitably front**, and in aggregate by **how many large uninformed swaps flow through the target pools and how much of that flow you win against competitors.** There is no benefit to deploying more capital than a given swap consumes (flash loans make capital a non-constraint), so scaling means *winning more opportunities*, which runs directly into crowding: a small number of sophisticated searcher teams win most large JIT opportunities. Realistic addressable notional per opportunity is up to a few million (bounded by the largest swaps and available flash-loan depth); aggregate strategy capacity is set by opportunity frequency, not capital — hence `capacity_usd` ≈ $5M as a per-opportunity working figure rather than a book size.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Adverse selection on informed swaps (primary).** Providing into a swap that keeps moving leaves the JIT LP with a losing inventory whose unwind cost exceeds the fee. This is the LVR-of-a-single-swap tail. See [[loss-versus-rebalancing]], [[adverse-selection]].
2. **Crowding / auction competition.** Other searchers bid up the tip and split the flow, compressing surplus toward zero — the documented decay.
3. **JIT-resistant design.** Uniswap v4 hooks (and other AMM designs) can penalize or block same-block mint-and-burn, or route large-swap fees to committed LPs, removing the opportunity structurally.
4. **Private order flow.** As large swaps increasingly route through private mempools/RFQ and away from the public mempool, the detection edge disappears — you cannot front what you cannot see.
5. **Gas/tip spikes.** A base-fee surge raises the economics gate above the fee capture, killing marginal opportunities.
6. **Bundle/inclusion risk.** Reverts are free (atomic), but repeated failed inclusion wastes simulation resources and cedes flow to faster builders.

## Kill criteria

Pause the strategy when **any**:

- **Rolling 100-attempt net P&L < 0** — the informed-flow filter or the auction economics have turned negative.
- **Realized JIT-fee capture < gas + tip + LVR** on the median opportunity for a sustained window (surplus arb'd out).
- **Informed-swap loss rate rises above a set threshold** (e.g. >15% of provisions end with unwind cost > fee) — the `looks_informed` model has decayed.
- **Target pools migrate to JIT-resistant hooks** or large flow moves to private mempools → the structural opportunity is gone.

Like other MEV strategies, JIT is opportunity-driven and pause-able: when a pool goes JIT-resistant, rotate to pools/chains where the opportunity persists rather than retiring the technique. See [[when-to-retire-a-strategy]].

## Advantages

- **Near-zero standing capital** — liquidity is flash-loaned within the atomic bundle.
- **Single-block risk** — inventory exposure lasts one block; no ongoing IL like passive [[concentrated-liquidity|range LPing]].
- **Atomic execution** — bundles revert entirely on failure, eliminating partial-fill risk.
- **High, near-deterministic fee capture** on the targeted swap — the mechanics are mechanical, not predictive.
- **Direction-neutral in intent** — the strategy profits from fees, not from a price view (the only directional risk is the residual single-swap inventory).

## Disadvantages

- **Existential adverse-selection tail** — informed swaps flip a win into a loss; the whole edge is the informed/uninformed filter.
- **Highly competitive and crowded** — a few teams dominate; surplus is bid away in builder auctions.
- **Harms passive LPs** — JIT siphons the most profitable swaps from committed [[concentrated-liquidity|range LPs]], which is why AMMs are designing it out.
- **Fragile to design and routing changes** — v4 hooks, JIT-resistant pools, and private order flow each remove the opportunity.
- **Specialized infrastructure** — mempool monitoring, bundle construction, simulation, and builder relationships are non-trivial.
- **Ethereum-L1-centric** — most viable where a public mempool + builder auction exist; different or absent on sequencer-based L2s.
- **Regulatory ambiguity** — as an MEV-adjacent strategy, legal classification remains unsettled.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI does not stream the raw mempool (use a node / Flashbots mempool stream for the trigger), but it supplies the pool-state, volatility, and gas context for opportunity screening and back-testing.

**Live data:**
- `GET /api/v1/dex/trending?chain=ethereum` — trending DEX pools (which pools see large swap flow)
- `GET /api/v1/dex/new-pools` — newest pools/launches where JIT competition may be thinner
- `GET /api/v1/dex/token/{chain}/{address}` — token info + top pools for a target pair
- `GET /api/v1/volatility/regime` — volatility regime (informs single-swap LVR risk)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1m&limit=1000` — OHLCV to model single-swap LVR
- `GET /api/v1/backtesting/klines` — deep archive for backtesting JIT economics across regimes

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/trending?chain=ethereum"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Pool selection** — `GET /api/v1/dex/trending?chain=ethereum` ranks pools by the large-swap flow JIT targets; `GET /api/v1/dex/token/{chain}/{address}` adds per-pair depth context
- **Risk pricing** — `GET /api/v1/volatility/regime` sets the single-swap LVR risk on the residual inventory; stand down in `vol_shock` states
- **Regime gate** — `GET /api/v1/liquidity/regime` fragility score — fragile books raise the odds a large pending swap is informed, the adverse-selection tail that decides JIT P&L
- **Backtest** — model single-swap LVR from 1m `GET /api/v1/backtesting/klines` (only since 2026-03-30, so minute-level history is shallow); the mempool trigger itself is not replayable from any REST archive
- **Tips** — the trigger is a node/Flashbots mempool stream; keep CryptoDataAPI in the screening and risk-state loop, cached and outside the block-race latency path

## Related

- [[concentrated-liquidity]] — the LP mechanism JIT weaponizes into a single block; JIT skims the swaps passive CL positions compete for
- [[loss-versus-rebalancing]] — the single-swap version of which is JIT's core risk against informed flow
- [[mev-strategies]] — the broader category of block-level value extraction
- [[flashbots]] — the relay/builder infrastructure used to submit atomic JIT bundles
- [[mempool]] — the source of the pending-swap trigger
- [[adverse-selection]] — the informed/uninformed distinction that decides JIT P&L
- [[uniswap]] — the primary venue; v4 hooks can make pools JIT-resistant
- [[edge-taxonomy]] / [[failure-modes]] / [[when-to-retire-a-strategy]] — framing and kill-criteria methodology

## Sources

- Uniswap v3 Core whitepaper (Adams et al., 2021) — concentrated-liquidity mechanics that make single-tick JIT possible.
- Flashbots documentation — bundle construction, atomic execution, and the builder/relay auction JIT bundles are submitted through.
- Milionis, Moallemi, Roughgarden, Zhang, *Automated Market Making and Loss-Versus-Rebalancing* (2022), arXiv:2208.06046 — the LVR/adverse-selection framing of the residual single-swap inventory; see [[loss-versus-rebalancing]].
- General MEV / JIT-liquidity research (Flashbots, EigenPhi, and academic MEV literature) on JIT prevalence, profitability, and its effect on passive LPs.

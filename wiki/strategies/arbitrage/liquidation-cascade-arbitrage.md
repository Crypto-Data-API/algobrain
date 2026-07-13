---
title: "Liquidation Cascade Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, crypto, defi, algorithmic]
aliases: ["Liquidation Bot", "Cascade Front-Run", "Keeper Arbitrage", "MEV Liquidations", "Liquidator Strategy"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto, defi]
complexity: advanced
backtest_status: paper-traded
edge_source: [latency, structural, informational]
edge_mechanism: "On-chain lending protocols pay a 5-13% bonus to anyone who liquidates an undercollateralized position. Cascade dynamics during sharp price moves create stacked, temporally-clustered opportunities that overshoot fair price."
data_required: [oracle-prices, lending-position-graph, gas-price, mempool, dex-liquidity]
min_capital_usd: 0
capacity_usd: 100000000
crowding_risk: high
expected_sharpe: 2.0
expected_max_drawdown: 0.10
breakeven_cost_bps: 50
decay_evidence: "Liquidation bonuses unchanged since 2018-2020; competition extreme; ~$1B+ extracted across DeFi history."
related: ["[[mev-strategies]]", "[[flash-loan-arbitrage]]", "[[funding-rate-arbitrage]]", "[[aave]]", "[[compound]]", "[[makerdao]]", "[[liquity]]", "[[gmx]]", "[[hyperliquid]]", "[[2022-05-terra-luna-depeg-arb]]", "[[counterparty-stress-arbitrage]]", "[[2006-09-amaranth-natural-gas-blowup]]", "[[fastest-profitable-trades]]"]
---

# Liquidation Cascade Arbitrage

Liquidation cascade arbitrage front-runs or follows on-chain liquidations on lending protocols ([[aave]], [[compound]], [[makerdao]], [[liquity]], dYdX) and on-chain perpetual venues ([[gmx]], [[hyperliquid]], dYdX v4). Liquidators receive a **5–13% bonus** on the seized collateral, and during cascading sell-offs (BTC -15% in an hour), stacked liquidations push prices below fair value momentarily — creating a layered MEV opportunity that has historically extracted **>$1B cumulatively across DeFi**.

This is a [[mev-strategies|MEV]] strategy: it relies on the same execution stack as [[mev-execution-guide]] (bundle construction, private mempool, gas bidding) and on the cascade dynamics formalized in [[liquidation-cascade-modeling]]. It pairs with [[flash-loan-arbitrage]] (capital-free atomic execution) and frequently co-occurs with [[stablecoin-pair-arbitrage]] during the same market-wide stress events.

## Edge Source

**Latency** + **structural** + **informational** (see [[edge-taxonomy]]).

- **Latency:** First-to-confirm wins the entire bonus. Sub-block, sub-millisecond infrastructure required.
- **Structural:** Protocols literally code in a bonus to incentivize external keepers; this is a paid public good, not a hidden edge.
- **Informational:** Mempool monitoring + lending-position graph queries reveal at-risk positions before the oracle ticks.

## Why This Edge Exists

Lending protocols cannot self-liquidate; they need external actors to maintain solvency. The bonus (5% on Aave V3 for stables, up to 13% on volatile collateral, 13% on MakerDAO via auctions, 15% on Liquity) compensates the liquidator for gas, capital, and execution risk. During cascades, multiple positions become liquidatable in the same block — the resulting forced selling overshoots fair value because the AMM curve is convex and there's no absorbing patient bid in the same block.

## Null Hypothesis

If markets were continuous and liquidations were spread evenly over time, prices would absorb each liquidation with minimal slippage and the bonus would equal the liquidator's marginal cost. Empirically, cascades are clustered (liquidations within seconds of each other) and prices overshoot — confirming a real edge for fast operators.

## Rules

### Entry — Pure Liquidator (Keeper)

1. **Index all open positions** on target protocols (Aave V2/V3, Compound V2/V3, Maker, Liquity, GMX, Hyperliquid)
2. **Subscribe to oracle price updates** — Chainlink, Pyth, internal oracles
3. **Compute health factor** for every position on every oracle tick
4. **When health factor < 1:** construct liquidation transaction
5. **Atomic flash-loan stack** (see [[flash-loan-arbitrage]]):
   - Borrow debt asset from [[aave]]
   - Call `liquidate()` on target position
   - Receive collateral + bonus
   - Swap collateral on DEX → debt asset
   - Repay flash loan
   - Pocket the bonus
6. **Submit via Flashbots / private mempool** to avoid sandwich/front-run

### Entry — Cascade Follower (Liquidity Replenisher)

1. **Wait for cascade signal:** >10 liquidations in 1 minute on a single protocol, OR >5% price overshoot vs. CEX index
2. **Buy the underwater asset** on the DEX where cascade is dumping (Uniswap, Curve, GMX vAMM)
3. **Hedge** on a CEX perp ([[binance]], [[bybit]], [[hyperliquid]]) at the better price
4. **Hold** until DEX price reverts to CEX (minutes-to-hours)

### Exit
- Pure liquidator: exit is atomic in the same transaction
- Cascade follower: exit when DEX/CEX spread closes to within 30 bps

## Implementation Pseudocode

```python
# Pure liquidator
def liquidator_loop():
    while True:
        new_oracle_price = wait_for_oracle_tick()
        for position in lending_positions(at_risk=True):
            hf = compute_health_factor(position, new_oracle_price)
            if hf < 1.0:
                expected_bonus = position.collateral_value * bonus_rate(protocol)
                gas_cost      = estimate_gas() * gas_price()
                if expected_bonus > gas_cost * safety_margin:
                    tx = build_atomic_liquidation(
                        flash_loan_amount = position.debt,
                        liquidate_call    = (position, max_repay),
                        collateral_swap   = best_dex_route(),
                    )
                    submit_flashbots_bundle(tx, priority_fee=high)

# Cascade follower
def cascade_follower():
    if liquidation_count(window="1min") > 10:
        dex_price = uniswap_price()
        cex_price = binance_index()
        if dex_price < cex_price * 0.95:
            long  = buy_dex(amount, venue="uniswap")
            short = open_perp_short(amount, venue="binance")
            wait_until_spread_closes(threshold=0.003)
            unwind_both()
```

## Indicators / Data Used

- **Oracle price feeds:** Chainlink, Pyth, Uniswap TWAP (varies by protocol)
- **Health factor / collateralization ratio:** position-level, computed every block
- **Mempool monitoring:** pending oracle updates, pending liquidations
- **Liquidation bonus rates:** Aave (5–13%), Maker (13% via auction), Liquity (10% Stability Pool), GMX (varies)
- **DEX liquidity depth:** for the collateral-to-debt swap leg
- **Gas price:** must price into expected profit
- **CEX index price:** anchor for cascade-follower trade

## Example Trade — Black Thursday, March 12, 2020

The canonical liquidation cascade. ETH dropped from ~$194 to ~$110 (-43%) on March 12, 2020, sliding below $100 the next day. [[makerdao]] CDPs (now Vaults) became massively undercollateralized.

- **Bug:** Ethereum gas prices spiked to 200+ gwei, but Maker's auction keepers had hard-coded gas limits and failed to bid on collateral auctions.
- **Result:** Keeper bots — dominated by a single operator — submitted **$0 bids** on collateral auctions and won them uncontested, taking roughly **$8.32M worth of ETH for free**.
- **Aftermath:** The system was left with ~$4.5–5.7M of unbacked DAI; Maker recapitalized by minting MKR via an emergency debt auction (March 19, 2020), diluting holders. A governance proposal to compensate the zero-bid liquidation victims was voted down; a class-action suit followed.

**Lessons baked into modern bot design:**
- Dynamic gas pricing
- Bid against expected fair value, not historical
- Gas-priority bidding for flash crashes

## Example Trade — Terra/Luna May 2022 Cascade

May 7-12, 2022: UST depeg triggered Anchor exits, then LUNA hyperinflation. Cross-protocol contagion liquidated an estimated $10B+ of leveraged positions on [[aave]], [[compound]], and others. Top liquidators reportedly cleared tens of millions of dollars in bonuses across the week, per Flashbots and on-chain analytics reporting.

## Example Trade — March 12, 2025 Hyperliquid ETH Whale Liquidation (counterexample)

On March 12, 2025, a whale unwound a ~$200M ETH long on [[hyperliquid]] by withdrawing margin until the position force-liquidated into the HLP (Hyperliquidity Provider) vault — Hyperliquid's protocol-owned liquidity pool that acts as liquidator-of-last-resort. HLP **lost ~$4M over 24 hours** absorbing the exit. The episode cuts both ways for this strategy: being the liquidator counterparty pool earns steady cascade income in normal regimes (HLP was cumulatively profitable into 2025), but a sophisticated player can weaponize the liquidation engine to dump size onto the pool at a stale mark. Hyperliquid tightened margin requirements within days. The lesson: liquidation flow is *usually* paid flow, but the payer can occasionally be you.

## Performance Characteristics

- **Pure liquidator profitability:** Concentrated to ~10–20 dominant searchers; individual liquidations net $100–$10,000; cascade days net $100K–$1M
- **Total annual extraction:** ~$200–500M/year aggregate across DeFi (Flashbots/Eigenphi)
- **Sharpe (top operators):** 3.0+, but with extreme infrastructure costs
- **Cascade-follower returns:** 1–5% per cascade event when executed cleanly; 5–10 events/year of size

## Bonus Schedule by Protocol

| Protocol | Bonus | Mechanism |
|----------|-------|-----------|
| [[aave]] V3 | 5% (stables), 7-10% (BTC/ETH), up to 13% (long-tail) | Direct call to `liquidationCall()` |
| [[compound]] V2 | 8% | Direct `liquidateBorrow()` |
| Compound V3 | Variable (per market config) | Cometd liquidation engine |
| [[makerdao]] | 13% (penalty fee) | Liquidations 2.0 Dutch auction |
| [[liquity]] | 0.5% gas comp + 10% (via Stability Pool deposits) | Stability Pool absorbs first |
| [[gmx]] V2 | 0.5% liquidation fee + price-impact rebate | Protocol-driven |
| [[hyperliquid]] | Auction to HLP vault | Vault depositors receive yield |
| dYdX v4 | Insurance fund + liquidator rebate | Validator network executes |

## Infrastructure Requirements

This is a latency-bound strategy; the infrastructure *is* the edge. A pure liquidator that is even one block slow loses every contested race.

| Component | Purpose | Why it matters |
|---|---|---|
| **Low-latency RPC / own node (Geth/Reth)** | Mempool + state access | Detect at-risk positions and pending oracle ticks first |
| **Position indexer** | Track every open position's health factor | Recompute on every oracle tick across all target protocols |
| **Oracle subscription (Chainlink/Pyth)** | Trigger detection | Liquidatability flips the instant the oracle ticks |
| **Flashbots / private bundle submission** | Atomic, sandwich-safe execution | See [[mev-execution-guide]] for bundle construction and gas bidding |
| **Flash-loan integration** | Capital-free execution | Borrow debt asset, liquidate, swap, repay atomically ([[flash-loan-arbitrage]]) |
| **DEX routing** | Collateral → debt swap leg | Best-execution across pools to preserve the bonus |

The bundle construction, gas-bidding, and mempool-monitoring mechanics are shared with all MEV strategies and are documented once in [[mev-execution-guide]]. This page covers the liquidation-specific logic that sits on top of that execution stack. For modeling *which* positions cascade and how far prices overshoot, see [[liquidation-cascade-modeling]].

## Cost-Aware Breakeven

`breakeven_cost_bps` is ~50 (frontmatter). The bonus must clear all of the following before a liquidation is worth submitting — and during gas spikes (exactly when cascades happen) the gas term can dominate.

| Cost | Magnitude | Notes |
|---|---|---|
| Gas | Spikes hardest during cascades | The Black Thursday failure was a gas-pricing bug |
| Builder bid (priority fee) | Competitive — high in contested liquidations | Often the largest cost in a race |
| DEX swap fee + slippage | Scales with collateral size | Erodes the bonus on the swap leg |
| Flash-loan fee | Small per-protocol fee | Aave/dYdX flash-loan cost |
| Failed-tx gas | Wasted when outbid (public) or reverted | Mitigated by private bundles |

No fabricated returns are quoted: realized P&L is the bonus minus these costs minus the probability of losing the race, all of which vary by event and competition. The historical figures in the example trades are dated and cited (see Sources), not projections.

## Capacity Limits

- Atomic flash-loan liquidations are **capital-free** — capacity is bounded by available debt-token liquidity for the flash loan and DEX depth for the swap leg
- Cascade-follower trades cap at ~$10M per event before move-the-market becomes self-defeating
- Total addressable opportunity grows with DeFi TVL

## What Kills This Strategy

- **Bonus reduction:** Protocols can vote down bonuses
- **Protocol-internal liquidator vaults** (Hyperliquid HLP, Liquity Stability Pool) capture the flow before external bots can act
- **Better oracles:** Faster, more frequent updates reduce the window between insolvency and liquidation
- **Centralized liquidator privileges:** Some protocols (GMX V2) reserve liquidations for whitelisted keepers
- **Regulatory:** US classification of liquidator activity as broker-dealer activity (theoretical)
- **Mempool privacy:** Encrypted mempools (SUAVE, Shutter) reduce the informational edge

## Kill Criteria

- Net P&L per liquidation falls below 2x gas cost for 30 consecutive days
- A target protocol introduces internal liquidator vault that captures >80% of flow
- Infrastructure cost (RPC, co-location, indexers) exceeds 50% of gross
- Failed-tx rate exceeds 30% (gas wasted on lost races)

## Advantages

- **Zero capital requirement** when combined with [[flash-loan-arbitrage]]
- **Atomic execution** — no leg risk, no holding period
- **Cleanly defined edge** — protocols literally pay you
- **Asymmetric in cascades** — most profit concentrated in rare events
- **Permissionless** — no relationship with a venue required (most protocols)

## Disadvantages

- **Extreme competition** — top 5 searchers capture most flow
- **Latency arms race** — co-location, custom relays, validator-builder integrations needed
- **Smart-contract risk** — bug in your liquidator contract can drain it
- **Black-swan failure** — see Maker March 12, 2020 ($0 bid bug went the *other* way and cost the protocol)
- **MEV-sandwich vulnerability** if not using private mempools (Flashbots)
- **Capital-cost trap** in chains without flash loans (BSC liquidations historically required real capital)
- **Validator collusion** can re-order or steal bundles

## Sources

- Flashbots transparency dashboard
- Eigenphi MEV analytics
- MakerDAO Black Thursday post-mortem (March 2020); Glassnode, "What Really Happened to MakerDAO" (2020)
- Hyperliquid HLP vault disclosures
- Aave / Compound / Liquity protocol documentation
- Data inputs (oracles, position graphs, mempool, DEX depth): [[crypto-data-sources]]
- Verified via Perplexity (sonar), 2026-06-10 — confirmed Black Thursday zero-bid total (~$8.32M ETH for 0 DAI), the ~$4-4.5M+ unbacked-DAI shortfall, the rejected compensation vote, the March 12, 2020 ETH drop ($194 → ~$111, -43%), and that HLP *lost* ~$4M in 24h on the March 12, 2025 whale liquidation. Citations: https://insights.glassnode.com/what-really-happened-to-makerdao/, https://thedefiant.io/news/defi/maker-votes-to-not-compensate-black-thursday-victims, https://www.tradingview.com/news/coinpedia:abc3617e7094b:0-makerdao-s-black-thursday-how-one-bot-got-8-32m-in-eth-for-free/

## Related

- [[mev-strategies]] — parent category
- [[mev-execution-guide]] — the shared execution stack (bundles, gas bidding, mempool)
- [[liquidation-cascade-modeling]] — modeling which positions cascade and how far prices overshoot
- [[flash-loan-arbitrage]] — funding mechanism for atomic liquidations
- [[funding-rate-arbitrage]] — sister cash-and-carry on perp venues
- [[stablecoin-pair-arbitrage]] — frequently co-occurs in the same crisis
- [[aave]], [[compound]], [[makerdao]], [[liquity]], [[gmx]], [[hyperliquid]]
- [[2022-05-terra-luna-depeg-arb]] — cascade event
- [[curve-finance]] — frequent venue for the swap leg
- [[crypto-data-sources]] — oracle feeds, position graphs, mempool, DEX depth
- [[edge-taxonomy]], [[failure-modes]]

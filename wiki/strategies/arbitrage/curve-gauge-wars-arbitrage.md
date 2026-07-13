---
title: "Curve Gauge Wars Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, defi, crypto, ethereum]
aliases: ["Curve Wars", "veCRV Bribe Arb", "vlCVX Bribe Trade", "Bribe Yield Arb"]
strategy_type: quantitative
timeframe: position
markets: [crypto, defi]
complexity: advanced
backtest_status: paper-traded
edge_source: [structural, behavioral]
edge_mechanism: "veCRV/vlCVX holders direct CRV emissions to Curve pools; protocols needing liquidity pay bribes that exceed organic governance value, creating a yield arb between bribe income and lock cost."
data_required: [vecrv-supply, cvx-locked, gauge-weights, votium-bribes, hidden-hand-bribes, pool-tvl]
min_capital_usd: 10000
capacity_usd: 250000000
crowding_risk: high
expected_sharpe: 1.0
expected_max_drawdown: 0.40
breakeven_cost_bps: 100
decay_evidence: "Bribe APRs collapsed post-Terra (May 2022), recovered modestly 2023-2024."
related: ["[[funding-rate-arbitrage]]", "[[lst-depeg-arbitrage]]", "[[stablecoin-pair-arbitrage]]", "[[curve-finance]]", "[[convex]]", "[[yearn]]", "[[frax]]", "[[defi-yield-farming]]", "[[2022-05-terra-luna-depeg-arb]]"]
---

# Curve Gauge Wars Arbitrage

The "Curve Wars" trade is a structural [[arbitrage]] on the bribe (vote-incentive) market built on top of [[curve-finance|Curve Finance]]'s vote-escrow governance system. Holders of veCRV (vote-escrowed CRV, locked up to 4 years) direct CRV emissions to specific Curve pools via gauge weight votes. Protocols that need on-chain stablecoin liquidity pay **bribes** (typically in their own token or stables) to veCRV / vlCVX voters via marketplaces like **Votium** and **Hidden Hand** (built by Redacted Cartel) to direct emissions to their pool. Arbitrageurs accumulate the governance tokens to harvest these bribes at **15–40%+ APR** (peak 2021–2022) on stablecoin-equivalent capital. The trade is a clean illustration of [[limits-to-arbitrage]]: the edge persists precisely *because* the cheapest way to capture it requires locking capital for 16 weeks to 4 years, an illiquidity constraint that deters most marginal arbitrageurs.

The strategy sits at the intersection of governance arbitrage and DeFi [[yield-farming]]: it is a yield trade whose underlying cash flow is a bribe rather than a fee, and whose principal is exposed to the price of an illiquid, smart-contract-locked governance token.

## Edge Source

**Structural** + **behavioral** (see [[edge-taxonomy]]).

- **Structural:** [[curve-finance]] hard-coded a 4-year max lock for max boost. Capital that locks longest receives the most voting power. Protocols cannot lock-up faster than the governance schedule allows.
- **Behavioral:** Protocols treating bribes as a *marketing budget* (cheaper than building their own LM program) rather than an efficient vote price means voters can over-extract.

## Why This Edge Exists

Stablecoin protocols ([[frax]], MIM (Abracadabra's Magic Internet Money), Alchemix, Curve's own crvUSD, [[lido|Lido]]'s stETH/ETH) need deep on-chain liquidity to keep their tokens at peg. Curve emits CRV to pools weekly based on gauge votes. So the cost stack:

1. Protocol mints/buys its native token
2. Pays it to Votium / Hidden Hand to bribe vlCVX or veCRV voters
3. Voters direct CRV emissions to that protocol's Curve pool
4. LPs in that pool earn extra CRV emissions, attracting capital
5. Pool gets deeper → token holds peg better → protocol's TVL grows

The arbitrageur's job is to be at step 3, holding voting power. The bribes paid often exceed what governance "should" cost, particularly when multiple protocols compete in the same epoch.

## Null Hypothesis

If governance markets were perfectly efficient, bribes paid per unit of vote would equal the marginal LP yield captured by the bribed pool, and the bribe-harvest yield would equal the risk-free stable yield plus a premium that exactly compensates for (a) lock-up illiquidity and (b) CVX/CRV price drawdown risk. In practice, principal-agent dynamics (protocol treasuries, bull-market budgeting, brand wars) overpay — demonstrably visible in bribe-yield premiums of 15–40% APR over staking-equivalent yield from 2021 to mid-2022.

A clean test of the null: compute realized total return of a vlCVX bribe-harvest position *including* the mark-to-market on the CVX principal over a full cycle. Under the null, that total return should equal the stable-yield benchmark. Empirically, the *yield leg* beat the benchmark by a wide margin while the *principal leg* destroyed most of it during the 2022 bear — so the bribe premium was real but was substantially an illiquidity/price-risk premium rather than pure mispricing.

## Why the Mispricing Persists

Three structural reasons the bribe premium does not arbitrage away (the [[limits-to-arbitrage]] lens):

1. **Lock-up illiquidity.** Capturing the bribe yield natively requires locking CRV for up to 4 years (non-redeemable) or CVX for rolling 16-week windows. Most capital cannot bear that horizon, so the marginal voter is structurally scarce.
2. **Stacked smart-contract risk.** The position depends on Curve + Convex + Votium/Hidden Hand + the bribed pool simultaneously. Each layer is a [[smart-contract-vulnerability-taxonomy|smart-contract vulnerability]] surface; the compounded risk discourages large risk-managed pools from sizing up.
3. **Operational drag.** Bi-weekly voting across multiple platforms, multi-token bribe claims, and tax accounting impose a real operating cost that scales poorly, leaving small-to-mid voters under-competed.

## Rules

### Entry — Direct veCRV Path

1. **Acquire CRV** on the open market (Curve pool, Uniswap)
2. **Lock CRV → veCRV** via Curve UI for maximum 4 years (gives 1:1 voting power)
3. **Vote weekly** in gauge weight elections (10-day cycle in practice)
4. **Claim bribes** from Votium, Hidden Hand
5. **Compound:** sell bribes for stables (or more CRV) and reinvest

### Entry — vlCVX (Convex) Path (Most Common)

1. **Acquire CVX**
2. **Stake → vote-locked CVX (vlCVX)** for 16-week locks (rolling)
3. **Vote on Convex's pooled veCRV via Snapshot** every 2 weeks
4. **Claim bribes** auto-distributed via Votium / Hidden Hand
5. **Re-lock** as needed

### Exit
- Locks are non-transferable; veCRV cannot be unlocked early at all
- vlCVX unlocks every 16 weeks; can stop re-locking
- Sell unlocked CVX/CRV to exit position
- Active funds rotate through CRV/CVX dependencies based on bribe yields

### Position Sizing
- Critical to track *real* bribe yield (USD bribes / USD locked, annualized)
- Cap allocation at 25% of stable yield book given lock-up illiquidity
- Diversify across vlCVX, veCRV, and Frax-equivalent (vefxs)
- Size the hedged sleeve (short CVX perp against locked stack) separately — the hedge isolates bribe yield but introduces funding-cost and basis risk

### Venue Comparison

| Venue | Token | Lock | Liquidity of position | Voting cadence | Notes |
|-------|-------|------|----------------------|----------------|-------|
| Direct veCRV | CRV → veCRV | Up to 4yr, **non-redeemable** | None until expiry | ~10-day gauge cycle | Max boost; capital fully trapped |
| Convex vlCVX | CVX → vlCVX | 16-week rolling | Stop re-locking to exit | Bi-weekly Snapshot | Most common; aggregates >50% of veCRV |
| Frax vefxs | FXS → vefxs | Up to 4yr | None until expiry | Frax gauge votes | Parallel ve-economy; correlated cycle |
| Liquid wrappers (cvxCRV, sdCRV) | — | Tradeable | High | Delegated | Lower yield; no lock but counterparty/peg risk |

## Implementation Pseudocode

```python
def gauge_war_arb():
    # Daily routine
    bribe_apr = (last_round_bribes_usd * 26) / vlcvx_supply_usd
    cvx_price = market_cvx_price()

    if bribe_apr > stable_yield_floor() + risk_premium():
        cvx_to_buy = sizing()
        cvx        = buy_cvx(cvx_to_buy)
        vlcvx      = lock_cvx(cvx, weeks=16)

    # Bi-weekly: vote
    on_round_open():
        votes = optimize_votes_for_bribe_yield()      # max bribes per vote
        submit_snapshot_vote(votes)

    # Bi-weekly: claim
    on_round_close():
        bribes = claim_votium() + claim_hidden_hand()
        usd_value = swap_to_stables(bribes)
        if compound:
            buy_cvx(usd_value)
            relock(weeks=16)
```

## Indicators / Data Used

- **veCRV supply** and lock distribution (Convex holds >50%)
- **vlCVX supply** and lock duration histogram
- **Gauge weights** (Curve `GaugeController`)
- **Votium bribe rounds** (votium.app, snapshot.org)
- **Hidden Hand bribe rounds** (hiddenhand.finance)
- **Round-by-round $ per vlCVX** historical APR
- **CRV emissions schedule** (yearly reduction; tail emissions)
- **Pool TVL** of bribed pools

## Example Trade — Frax Bribe Cycle Q1 2022

- **Setup:** [[frax]] aggressively bribed for FRAX/USDC pool gauge weight to grow FRAX TVL
- **Round 14 (Jan 2022):** vlCVX bribe round paid ~$0.45 per vlCVX (Frax + MIM + Terra contributing)
- **CVX price:** $35
- **Round-over-round:** Bribes paid bi-weekly = 26 rounds/year
- **Annualized bribe yield:** $0.45 × 26 / $35 = **~33% APR** in stables/governance tokens
- **Plus:** native CVX staking rewards (~5% APR in cvxCRV)
- **Total:** ~38% APR on capital exposed

**Trade size example:**
- $1M into 28,500 CVX at $35
- Lock as vlCVX
- Annual income: ~$380K in bribes + native rewards
- Risk: CVX itself dropped 95%+ peak-to-trough (Nov 2021 to Dec 2022)

## Example Trade — Frax / Anchor Pre-Terra Peak

In April 2022, the **4pool** initiative (FRAX + USDC + USDT + UST) was Terra's last attempt to bootstrap UST liquidity outside of Anchor. [[terraform-labs]] was rumored to be accumulating CVX directly + paying massive bribes to direct CRV emissions to 4pool. This pushed bribe yields above 40% APR briefly. May 2022 Terra collapse vaporized UST bribes overnight; the Convex flywheel broke; CVX dropped from $25 to $3 in 6 weeks. **Voters who held vlCVX through this lost 70%+ on the principal even while harvesting 30%+ APR on bribes — a textbook example of "yield does not protect from token-price drawdown."**

## Performance Characteristics

| Period | Bribe APR (vlCVX) | CVX price | Net experience |
|--------|--------------------|-----------|----------------|
| Q4 2021 | 20-30% | $35-45 | Excellent yield, modest CVX drawdown |
| Q1 2022 | 30-45% | $25-35 | Peak yields, CVX rolling over |
| May 2022 | Crashed to <10% | $5-8 | Terra collapse breaks flywheel |
| Q3-Q4 2022 | 5-12% | $4-8 | Bribes dry up during bear |
| 2023 | 8-18% | $3-6 | LSDfi (frxETH) + new entrants revive |
| 2024 | 10-25% | $2-5 | crvUSD bootstrap drives bribes |
| 2025 | Variable | <$5 | Mature; concentrated to fewer protocols |

- **Best market conditions:** Bull markets with multiple stablecoin/LSD launches competing for liquidity
- **Worst conditions:** Bear markets, depeg events that kill bribers (UST), Curve TVL declines
- **Sharpe (yield-only):** 2.0+; with unhedged token price exposure: <0.5. A partially hedged implementation (shorting CVX perps against a portion of the locked stack to isolate bribe yield) lands in between, ~1.0 — the figure used in this page's frontmatter.

## The Curve Wars Power Hierarchy

| Layer | Token | Function |
|-------|-------|----------|
| **Base** | CRV | Native, locked → veCRV (4yr max) |
| **L1 meta-governance** | CVX (Convex) | Holds majority of veCRV, 16wk locks |
| **L2 meta-governance** | YFI (Yearn) | Owns large CVX position |
| **L3 meta-governance** | BTRFLY (Redacted) | Owns YFI/CVX/CRV; bribes everyone |
| **Bribe markets** | Votium, Hidden Hand, Warden Quest (Paladin) | Vote-payment auctions |
| **Bribers** | FRAX, MIM, Lido (LDO), Origin (OUSD) | Pay to direct emissions |

**Convex peak share:** ~53% of veCRV at peak in 2022, making CVX the de-facto Curve governance token.

## Capacity Limits

- veCRV market cap: peaked ~$3-5B; meaningfully large positions need >$10M
- vlCVX market cap: peaked ~$2B; capacity for arb capital ~$250M without moving CVX price
- Bribe market liquidity: $10-50M per round; single-voter cap ~5% to avoid signaling

## What Kills This Strategy

See [[failure-modes]] for the general taxonomy. The dominant risks for this trade:

- **Curve TVL decline:** CRV emissions become less valuable; the underlying asset the whole flywheel monetizes shrinks
- **Briber consolidation:** if only 1-2 protocols bribe, the auction mechanism degenerates and bribe APRs collapse
- **Curve fork capturing share:** Velodrome, Aerodrome on Optimism/Base now run vote-escrow models, fragmenting the bribe pool
- **Token-price drawdown** on CVX/CRV wipes out yield gains — the principal risk dwarfs the carry (see the 2022 example)
- **Smart-contract / governance attacks:** flash-loaned governance attacks on Curve / Convex, or an exploit in Votium / Hidden Hand / the bribed pool. This is the catastrophic tail — a single bug in any layer of the Curve + Convex + bribe-market + pool stack can zero the position. See [[defi-hacks-and-exploits]] and [[smart-contract-vulnerability-taxonomy]]. Curve itself suffered a $73M Vyper-reentrancy exploit in July 2023 that put CRV (used as Aave collateral) into a near-liquidation spiral
- **Bridge / cross-chain risk:** if the position is mirrored on an L2 ve-fork (Aerodrome/Velodrome), the canonical bridge introduces additional [[bridge]] / [[cross-chain]] exposure
- **Ethereum gas wars** raising claim costs above bribe value for small voters

## Kill Criteria

- Bribe APR falls below stable yield + 5% premium for 3 consecutive months
- CVX/CRV down >50% since lock initiation AND no recovery catalyst
- Convex governance compromise or multi-sig incident
- Curve emissions schedule cut materially
- Total bribe market < $5M/round for 6 weeks

## Advantages

- **Stablecoin-denominated yield** (most bribes paid in stables or governance tokens that can be sold)
- **Multiple revenue streams:** bribes + cvxCRV rewards + admin fees
- **Composability:** stake LP positions in Convex for boosted yields too
- **Protocol-aligned:** legitimate governance participation
- **Scalable:** can deploy hundreds of millions

## Disadvantages

- **Lock-up illiquidity:** veCRV is *non-redeemable* (4yr); vlCVX is 16wk
- **Token-price risk:** CVX dropped >95% from peak; bribe APR doesn't compensate
- **Governance complexity:** must vote bi-weekly across multiple platforms
- **Bribe-market dependency:** Votium / Hidden Hand are single points of failure
- **Smart-contract stack risk:** Curve + Convex + Votium + the bribed pool itself
- **Tax complexity:** bi-weekly income claims, multiple token types, lock conversions
- **Bear market collapse:** post-Terra, the entire flywheel partially broke

## Historical Highlights

- **August 2020:** Curve launches with CRV emissions. Yearn dominates early.
- **May 2021:** Convex launches; aggregates veCRV faster than competitors.
- **Q4 2021:** "Curve Wars" name coined; CVX peaks at ~$60.
- **Jan 2022:** Frax launches frxETH precursor strategy; bribe APRs hit 40%.
- **April 2022:** 4pool Terra initiative; peak bribe yields.
- **May 2022:** [[2022-05-terra-luna-depeg-arb|Terra collapse]] breaks Convex flywheel.
- **2023-2024:** crvUSD launch + LSDfi (frxETH, sfrxETH) revive bribe demand.
- **2024-2025:** Aerodrome/Velodrome ve(3,3) forks compete; mature equilibrium.

## Sources

- Curve Finance protocol documentation
- Convex Finance documentation
- Votium / Hidden Hand bribe round history
- DefiLlama Convex/Curve dashboards
- llama.airforce analytics
- General market knowledge; no specific wiki source ingested yet.

## Related

- [[curve-finance]], [[convex]], [[frax]], [[yearn]], [[lido]]
- [[arbitrage]] — parent category; [[limits-to-arbitrage]] — why the bribe premium persists
- [[yield-farming]] / [[defi-yield-farming]] — broader category
- [[funding-rate-arbitrage]], [[lst-depeg-arbitrage]], [[stablecoin-pair-arbitrage]]
- [[smart-contract-vulnerability-taxonomy]], [[defi-hacks-and-exploits]] — the stacked-contract tail risk
- [[bridge]], [[cross-chain]] — L2 ve-fork mirror exposure
- [[edge-taxonomy]], [[failure-modes]] — strategy-development framing
- [[2022-05-terra-luna-depeg-arb]] — event that broke the flywheel
- [[mev-strategies]] — adjacent on-chain extraction

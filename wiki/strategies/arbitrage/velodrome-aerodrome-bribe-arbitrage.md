---
title: "Velodrome / Aerodrome Bribe Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-06-10
status: good
tags: [arbitrage, defi, crypto]
aliases: ["ve(3,3) Bribe Arb", "veVELO Bribe", "veAERO Bribe", "Solidly-Style Bribe Trading"]
related: ["[[curve-gauge-wars-arbitrage]]", "[[velodrome-finance]]", "[[aerodrome-finance]]", "[[airdrop-farming]]"]
strategy_type: hybrid
timeframe: position
markets: [crypto, defi]
complexity: advanced
backtest_status: live
edge_source: [structural, analytical, informational]
edge_mechanism: "Velodrome (Optimism, 2022+) and Aerodrome (Base, 2023+) implement Andre Cronje's ve(3,3) tokenomics: lock VELO/AERO for veVELO/veAERO; vote weekly to direct emissions to specific liquidity pools; receive bribes from protocols competing for that emission. Bribe yield often exceeds 30-100% APR for veToken holders; arbs construct optimal vote allocations."
data_required: [bribe-marketplace-prices, gauge-vote-history, pool-tvl-flow, velo-aero-emissions-schedule]
min_capital_usd: 50000
capacity_usd: 200000000
crowding_risk: medium
expected_sharpe: 1.8
expected_max_drawdown: 0.25
breakeven_cost_bps: 100
decay_evidence: "Velodrome 2024 TVL ~$200M; Aerodrome ~$1B. Bribe-yield compression as more capital deploys; recent yields 25-50% APR vs 50-100% in 2023."
---

# Velodrome / Aerodrome Bribe Arbitrage

Trading the **bribe markets** for [[velodrome-finance|Velodrome]] (Optimism's dominant DEX) and [[aerodrome-finance|Aerodrome]] (Base's dominant DEX) — both implementations of **Andre Cronje's ve(3,3) tokenomics**. Lock VELO/AERO tokens for veVELO/veAERO (held as transferable ERC-721 veNFTs); weekly vote to direct emissions to specific liquidity pools; collect bribes from protocols competing for those emissions. The strategy stack:

1. **Optimal vote allocation** — distribute votes to maximize bribe yield.
2. **Bribe pre-positioning** — buy veToken when bribe-implied yield exceeds VELO/AERO carry cost.
3. **Cross-protocol bribe arb** — route protocols' bribe budgets to most cost-effective pools.
4. **veToken price arb vs locked yield** — sell illiquid veToken position via NFT marketplaces or bond protocols.

## Edge Source

**Structural** + **analytical** + **informational**.

- **Structural:** Locked veToken position is illiquid; locked-position holders extract liquidity premium via bribes.
- **Analytical:** Multi-week optimization across many pools, bribe sources, vote-decay mechanics.
- **Informational:** Bribe-protocol announcements often telegraph future bribe budgets days ahead.

## Why This Edge Exists

ve(3,3) mechanics:
1. Lock VELO (Velodrome) or AERO (Aerodrome) for 1-4 years.
2. Receive veVELO/veAERO as a **veNFT** (ERC-721). Unlike Curve's non-transferable veCRV, Solidly-style ve positions are NFTs — the lock itself can be transferred or sold on secondary markets.
3. Each weekly epoch, vote to direct emissions to specific liquidity pools.
4. Pools your votes direct emissions to → emissions become your reward.
5. Protocols competing for that emission "bribe" you with their tokens (USDC, OP, AERO, VELO, governance tokens).
6. Bribes accumulate in your address weekly.

Bribes ("voting incentives") are paid primarily via Velodrome's and Aerodrome's native incentive contracts; aggregator marketplaces such as Hidden Hand (and the Curve-ecosystem equivalents Votium / yBribe) serve the broader vote-incentive market and provide cross-protocol yield benchmarks. Typical bribe yields:

| Period | Velodrome veVELO yield | Aerodrome veAERO yield |
|--------|------------------------|------------------------|
| Q4 2022 | 80-120% APR | n/a (Aerodrome launched Aug 2023) |
| Q4 2023 | 50-80% APR | 100-150% APR |
| Q4 2024 | 25-45% APR | 35-60% APR |
| Q1 2025 | 20-35% APR | 30-50% APR |

Counterparty: protocols spending bribe budget to attract liquidity (Frax, Rocket Pool, Aave, Pendle, Beefy, Convex, Yearn, etc.); newcomer LPs not running optimal vote allocation.

## Null Hypothesis

Under no-edge conditions, bribe yield is exactly fair compensation for what the locker gives up: 1-4 years of illiquidity plus full VELO/AERO token-price risk. In an efficient vote market, dollars-of-bribe-per-vote equalize across pools every epoch (any pool paying above-market gets flooded with votes within hours), so "optimal vote allocation" adds nothing over naive pro-rata voting — and the all-in return of lock + vote + collect equals holding the unlocked token, minus the illiquidity discount. Two falsifiable tests: (1) compare an optimizer's realized $/vote against the epoch-average $/vote across all pools — if the gap is consistently <5%, allocation skill is illusory; (2) compare total locker return (bribes + fees + token P&L) against simply holding spot VELO/AERO over the same window — if locked positions underperform after the 2022-style token drawdowns are included, the "30-100% APR" headline is just risk premium being paid for bearing lockup and token beta.

## Variants

| Variant | Description | Period |
|---------|-------------|--------|
| **Vote-and-collect** | Lock veToken, vote to highest-bribe pool, collect weekly | 1-4 years |
| **Bribe-spread arb** | Buy veToken when bribe-yield > token carry cost | Weeks-months |
| **Cross-protocol bribe routing** | For protocols, deploy bribe budget across Velo/Aero/Curve/Convex optimally | Continuous |
| **veNFT secondary trading** | Trade locked veNFT positions on NFT marketplaces / dedicated veNFT markets | Variable |
| **Vote-buying market making** | Run a service that aggregates voters and resells to protocols at premium | Continuous |
| **Cross-chain bribe arb** | Route emission across Velodrome (OP) and Aerodrome (Base) for same protocol | Weeks |

## Rules

1. **Bribe-marketplace monitoring:** track Velodrome native incentives, Aerodrome native incentives, Hidden Hand, and Curve-side markets (Votium/yBribe) for cross-market yield comparison.
2. **Vote-yield optimization:** for each epoch, allocate veToken votes to maximize $ bribes per veToken-vote.
3. **Pre-epoch positioning:** if expected next-epoch bribes >> current veToken price, buy veToken via secondary or lock new VELO/AERO.
4. **Bribe collection:** harvest weekly; convert to stables or compound back.
5. **Token-price hedging:** locked VELO/AERO carries token-price risk; hedge via perp short if bribe-yield doesn't compensate.

## Implementation Pseudocode

```python
on epoch_start:
    veVELO_balance = get_balance()
    pools = list_eligible_pools()
    bribes = {pool: get_bribes(pool) for pool in pools}
    optimal_allocation = solve_optimal_votes(veVELO_balance, bribes)
    cast_votes(optimal_allocation)

on epoch_end:
    rewards = collect_bribes()
    convert_to_stables(rewards)
    if mode == "compound":
        buy_velo(amount=rewards)
        lock_velo(duration=4_years)
```

## Indicators / Data Used

- Velodrome / Aerodrome subgraph (vote weights, bribe history).
- Hidden Hand bribe marketplace API.
- Votium / yBribe (Curve-ecosystem vote markets, for cross-market yield benchmarks).
- DefiLlama Velodrome / Aerodrome category.
- Protocol bribe-budget announcements (governance forums).

## Example Trades

**Aerodrome AERO surge, Q4 2023.** Aerodrome launched on Base Aug 2023; AERO airdropped to OP / Base users. Early lockers received 100-150% APR bribes from Frax, Rocket Pool, Pendle. AERO price rallied 5x from $0.20 to $1.20 over 4 months. Lockers earned both bribe yield + token appreciation = 200-400% on capital.

**Velodrome OP-pair bribes, 2023-2024.** Optimism DAO directed massive bribe budget to OP-paired pools on Velodrome to bootstrap OP liquidity. veVELO holders voting OP pools captured 60-100% APR.

**Pendle bribe campaigns on Aerodrome 2024.** Pendle bribed veAERO holders to direct AERO emissions to Pendle-LRT pools. Triangle: lock AERO → vote Pendle pool → collect Pendle bribes (PENDLE token + USDC) → sell PENDLE for stables.

**veNFT secondary-market discounts (recurring).** Because veVELO/veAERO locks are ERC-721 veNFTs, locked positions trade on NFT marketplaces and dedicated veNFT venues. They typically change hands at 5-15% discounts to intrinsic (underlying token × lock multiplier) value; arbs buy discounted veNFTs, collect bribes through the remaining lock, or merge/re-list at tighter discounts.

## Performance Characteristics

Top dedicated veToken / bribe-arb desks (Convex-style operations on Velo/Aero) report 25-50% annualized returns 2024 (compressed from 50-100% in 2023). Sharpe 1.5-2.5.

## Capacity Limits

Per-protocol capacity bound by veToken supply and bribe-market depth. Velodrome ~$50M; Aerodrome ~$100M.

## What Kills This Strategy

- VELO/AERO token-price collapse (locked positions cannot be exited).
- Migration of bribe activity to other ve(3,3) protocols (Camelot, Thena, Pearl, Velocore).
- Curve ecosystem displacement.
- ve(3,3) tokenomics losing favor.

## Kill Criteria

- Bribe-yield below 15% APR sustained.
- TVL on Velodrome/Aerodrome falling below $50M / $200M respectively.

## Advantages

- Recurring weekly opportunity.
- Decoupled from broad crypto beta (mostly).
- High yield without leverage.

## Disadvantages

- Locked-position illiquidity.
- Token-price risk on VELO/AERO.
- Operational complexity (weekly vote/harvest cycles).

## Sources

- Velodrome / Aerodrome documentation.
- Andre Cronje, *Solidly Whitepaper* (Feb 2022) — original ve(3,3) design.
- Hidden Hand (https://hiddenhand.finance) bribe market analytics.
- DefiLlama Velo/Aero TVL tracking.
- **YouTube: "Velodrome Explained" by various Optimism creators (2023-2024).**
- **YouTube: "Aerodrome Bribe Strategy" tutorials (2024).**
- **YouTube: "Bankless" Andre Cronje ve(3,3) interview (2022).**

## Related

[[curve-gauge-wars-arbitrage]] · [[velodrome-finance]] · [[aerodrome-finance]] · [[airdrop-farming]] · [[restaking-token-arbitrage]] · [[defi-yield-farming]] · [[points-farming]]

---
title: "MEV Strategies"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [crypto, mev, defi, algorithmic, arbitrage, flashbots, mempool, ethereum, market-microstructure, hyperliquid]
aliases: ["Maximal Extractable Value", "Miner Extractable Value", "MEV Extraction", "Searcher Strategies"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: untested

# Edge characterization (see [[edge-taxonomy]])
edge_source: [latency, structural, informational]
edge_mechanism: "Block-ordering rights are auctioned to whoever pays the builder most; a searcher with faster detection, atomic execution, and private orderflow captures price discrepancies and ordering value that appear and vanish inside a single block, at the expense of slower searchers and the users whose transactions move the state."

# Data and infrastructure requirements
data_required: [mempool-pending-tx, dex-pool-reserves, v3-tick-maps, gas-basefee, liquidation-events, builder-relay-api]
min_capital_usd: 5000        # gas float + failed-tx buffer + modest inventory; flash loans remove principal for atomic legs
capacity_usd: 5000000        # per-operator working-capital ceiling; extra capital does not buy more wins
crowding_risk: high

# Performance expectations (net of gas, builder bid, and failed-race drag)
expected_sharpe: 1.0         # competent non-elite operator; elite searchers with superior infra do far better (latency edge, not this page's)
expected_max_drawdown: 0.15
breakeven_cost_bps: 50       # opportunity-level, not portfolio bps: net must clear gas + builder bid + flash-loan fee per attempt

# Decay history
decay_evidence: "Builder bid capture on contested Ethereum opportunities has ground toward 90-100% of gross; private orderflow (MEV-Share, MEV-Blocker, Flashbots Protect), encrypted mempools (SUAVE/Shutter), and batch-auction DEXs (CoW Protocol) progressively remove the informational edge. Flashbots/EigenPhi data document a small set of dominant searchers capturing most flow."

# Lifecycle
kill_criteria: |
  - bundle inclusion rate below the level where infra cost > net MEV for 30 consecutive days
  - median net profit per landed bundle < gas-plus-overhead breakeven for the target chain
  - required builder bid > 90% of gross on > 80% of won opportunities for a month (auction fully competitive)
  - any single execution loss > 2% of allocated capital from a routing/revert-protection bug
  - a target venue introduces protocol-internal ordering / liquidator capture that removes the addressable flow

related: ["[[mev-execution-guide]]", "[[mev]]", "[[flashbots]]", "[[flash-loan-arbitrage]]", "[[slippage-optimal-pathfinding]]", "[[liquidation-cascade-arbitrage]]", "[[cross-exchange-arbitrage]]", "[[defi-yield-farming]]", "[[triangular-arbitrage]]", "[[gas-fees]]", "[[ethereum]]", "[[uniswap]]", "[[jito]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[ai-mev]]"]
---

# MEV Strategies

Maximal Extractable Value (MEV) is the profit extractable by controlling the **ordering, insertion, or censoring** of transactions within a block. Originally "Miner Extractable Value" on proof-of-work [[ethereum]], it was renamed after [[the-merge|The Merge]] once validators inherited block-production rights. This page specifies the four buildable MEV strategies a **searcher** actually runs — **DEX arbitrage, back-running, sandwiching, and JIT liquidity** — each as an implementable spec with its edge source, sizing, infrastructure, and a realistic gas-and-competition cost overlay. For the shared execution plumbing (Flashbots bundle construction, gas bidding, mempool monitoring) see the companion [[mev-execution-guide]]; for exact trade sizing against AMM curves see [[slippage-optimal-pathfinding]].

## Edge source

Per [[edge-taxonomy]], MEV is a **latency + structural + informational** hybrid:

- **Latency.** Post-Merge, block-ordering is auctioned via [[flashbots]]-style relays (Jito on Solana). The searcher who detects an opportunity and lands a bundle first wins it outright; everyone else reverts or arrives too late. Edge is measured in milliseconds and block positions.
- **Structural.** The MEV supply chain (searcher → builder → proposer) is a *designed* market. Paying the highest priority fee/tip is a repeatable, sanctioned way to buy ordering — not a hidden exploit.
- **Informational.** The public mempool broadcasts pending intent. A searcher who decodes pending swaps, liquidations, and pool creations faster than rivals sees the opportunity before it settles.

## Why this edge exists

Blockchains order transactions discretely, one block at a time, and the right to order them is economically valuable. Three frictions sustain the edge: (1) most users broadcast to the **public mempool**, leaking their intent; (2) AMM price impact is **deterministic and computable**, so the profit of a back-run, sandwich, or JIT is known in advance; and (3) inclusion is a **pay-to-play auction**, so capital-and-infrastructure-rich searchers reliably outbid casual participants. The other side is the ordinary user whose swap moves a pool, the lending protocol that must pay a liquidation bonus, and slower searchers who lose the race — they keep losing because they cannot see the opportunity in time or cannot pay enough to be ordered first.

## Null hypothesis

If block-ordering were random and the mempool fully private, expected MEV per searcher would equal the builder bid plus gas — zero net edge, competed away. The observed reality — a small set of dominant searchers earning persistent positive net MEV (documented by [[flashbots]] and EigenPhi) — rejects that null: latency and infrastructure create a durable, concentrated edge for the fastest operators. A useful falsification test for *your* operation: run the detector in shadow mode and compare simulated-gross to actually-landed-net; if net is indistinguishable from zero after gas and bid, you have detection but no latency/orderflow edge, and observed wins are auction luck.

## Rules — the four buildable strategies

Every MEV strategy shares one exit rule: **atomic**. The whole cycle executes in a single transaction/bundle or reverts — there is no discretionary exit, no partial-fill leg risk (when submitted privately). What differs is detection, sizing, and infrastructure.

### 1. DEX arbitrage (the "clean" MEV)

- **Edge source:** analytical + latency. Correcting price divergence across AMMs ([[uniswap]] v2/v3, Sushi, Curve, Balancer) keeps on-chain prices aligned — a legitimate market function.
- **Detection:** monitor pool reserves each block; find cycles whose product of effective rates > 1 (see [[slippage-optimal-pathfinding]]).
- **Sizing:** solve the exact optimum against convex slippage — *not* a fixed size. Over-trading past the profit peak converts a winning cycle into a loss (see [[slippage-optimal-pathfinding]] for the closed form and the over-trading trap).
- **Infra:** flash-loan the principal ([[flash-loan-arbitrage]]) → atomic swap cycle → repay; submit as a private bundle so no rival can back-run or reorder you.
- **Capital:** ~$0 (flash-loan funded); binding input is infra and gas float.

### 2. Back-running

- **Edge source:** informational + latency. Execute *immediately after* a state-changing transaction (a large swap, an oracle update, an LP add) to capture the arb it creates — without touching the victim's price.
- **Detection:** decode a large pending swap in the mempool; compute the post-trade pool state; if the resulting cross-pool arb clears costs, queue a bundle ordered *right behind* it.
- **Sizing:** optimal against the *post-victim* reserves, not the current ones.
- **Infra:** submit `[victim_tx, your_backrun]` as an ordered bundle, or use **MEV-Share / MEV-Blocker** orderflow (the victim opts in and you bid for the backrun right). Non-extractive: the user is not made worse off.
- **Capital:** ~$0 (flash-loan funded).

### 3. Sandwiching (extractive — controversial)

- **Edge source:** informational + latency, but **value is taken from the user**, not from a mispricing. Front-run a victim's swap (buy first, pushing price up), let the victim fill worse, back-run (sell into the price they moved).
- **Detection:** a large pending swap with **loose slippage tolerance** in the public mempool; the profit is bounded by how much of the victim's tolerance you can consume.
- **Sizing:** the front-run size that maximizes extraction within the victim's slippage band — too large self-limits (you move price past their revert threshold).
- **Infra:** requires **upfront capital** for the front-run leg (you hold the token between front and back). Must land both legs in the exact positions around the victim — a builder-level ordering guarantee, else you carry inventory risk.
- **Ethics/risk:** directly taxes DeFi users; increasingly designed-away by private mempools that hide the victim from you. Included here for completeness; the durable, defensible strategies are DEX-arb, backrun, and JIT.

### 4. JIT (Just-In-Time) liquidity

- **Edge source:** structural + informational. On concentrated-liquidity AMMs ([[uniswap]] v3), add a large, tightly-ranged LP position **in the same block, just before** a large swap; capture the bulk of that swap's fee; withdraw the liquidity immediately after.
- **Detection:** a large pending v3 swap whose fee (on a tight range around current tick) exceeds the gas + capital cost of the JIT mint/burn.
- **Sizing:** liquidity concentrated in the exact tick range the swap will traverse, sized so your share of the fee dominates the passive LPs' — bounded by the swap notional.
- **Infra:** an atomic `mint → (victim swap) → burn` bundle; needs **substantial working capital** (the LP principal, briefly) but no directional exposure if the range is symmetric and the burn is same-block.
- **Trade-off:** competes with and dilutes passive LPs; a structural, non-user-extractive form of MEV (the swapper gets the same price; passive LPs get less fee).

### Strategy comparison

| Strategy | Edge | Capital | User harmed? | Key infra | Where it lives |
|---|---|---|---|---|---|
| DEX arbitrage | analytical+latency | ~$0 (flash loan) | No | Private bundle, optimal sizing | ETH L1/L2, Solana |
| Back-running | informational+latency | ~$0 (flash loan) | No | Ordered bundle / MEV-Share | ETH L1/L2, Solana |
| Sandwiching | informational+latency | Upfront (inventory) | **Yes** | Front/back ordering guarantee | Public-mempool chains |
| JIT liquidity | structural+informational | Large (brief LP) | Passive LPs diluted | Atomic mint/swap/burn | Uniswap v3 (ETH, L2s) |

## Implementation pseudocode

```python
# mev_searcher.py — detection -> economics gate -> private bundle
# shared plumbing (bundle build, priority-fee bid) lives in [[mev-execution-guide]]

def on_pending_or_block(state):
    for opp in detect(state):               # dex-arb cycle | backrun | sandwich | jit
        x = optimal_size(opp)               # see [[slippage-optimal-pathfinding]]; NOT fixed size
        gross = gross_profit(x, opp)
        gas   = est_gas(opp) * state.base_fee
        fee   = flash_loan_fee(x, opp)      # ~0-9 bps depending on provider; 0 if capital held
        # builder takes most of the residual on contested flow:
        bid   = bid_pct(opp.competition) * max(gross - gas - fee, 0)   # 90%+ when contested
        net   = gross - gas - fee - bid
        if net > min_net_threshold(opp.chain):   # ETH L1: ~$5; L2/Solana: cents
            submit_private_bundle(build_atomic_tx(opp, x),
                                  tip=bid,
                                  target_block=state.block + 1,
                                  drop_if_revert=True)   # reverts cost nothing
        # else: skip — the auction would take all the edge
```

The decisive line is `bid = bid_pct(...) * residual`: on contested Ethereum opportunities the builder captures the large majority of gross, so **the strategy is dominated by costs, not by gross spread** — exactly why fixed-size, gross-only thinking bankrupts naive entrants.

## Indicators / data used

- **Mempool pending transactions** — decoded for pending swaps, liquidations, LP adds, pool creations (WebSocket to a low-latency node; see [[mev-execution-guide#Mempool-Monitoring]]).
- **DEX pool reserves + v3 tick maps** — per-block state for exact sizing.
- **Gas base fee + builder-bid distributions** — to price the inclusion auction.
- **Liquidation triggers** — health factors on Aave/Compound/perp venues (feeds [[liquidation-cascade-arbitrage]]).
- **Builder/relay APIs** — Flashbots, Titan, bloXroute, Ultra Sound (Ethereum); **Jito block engine** (Solana).
- **Bundle simulation** — pre-execution `eth_callBundle` to verify profitability before paying gas.

## Example trade (DEX arbitrage — the clean case)

1. **Detection:** WETH/USDC on [[uniswap]] v3 marks $3,200; on Sushi $3,188 — a $12 (0.38%) gap.
2. **Optimal size:** solving against both pools' depth (not a fixed guess) says buy ~15 ETH on Sushi, sell on Uni maximizes net.
3. **Bundle:** flash-loan USDC from Aave → buy 15 ETH on Sushi @ $3,188 → sell 15 ETH on Uni @ $3,200 → repay flash loan + fee, all atomic.
4. **Gross:** 15 × $12 = **$180**. Flash-loan fee ~$2. Gas + priority ~$30.
5. **Builder bid:** on a contested pair the builder takes ~90% of the post-gas residual. Post-gas/fee ≈ $148; bid ≈ $133; **net ≈ $15** in a single block (~12s). Capital used: **$0**.

The $148 "profit" a naive gross-only calc reports is mostly the builder's; the searcher keeps the ~$15 residual — and only if the bundle lands. This is the entire economic character of MEV.

## Performance characteristics (realistic cost overlay)

MEV economics are dominated by costs, not gross spread. No fabricated portfolio return is given — realized P&L depends on competition, chain, and latency, all varying continuously.

| Cost component | Where it lands | Notes |
|---|---|---|
| **Gas** | Paid on inclusion (0 on reverted private bundles) | Use Flashbots/Jito so reverts cost nothing |
| **Builder bid (priority fee/tip)** | The dominant cost — often 90%+ of gross on contested flow | Higher bid = higher inclusion, lower retention |
| **Flash-loan fee** | ~0–9 bps of notional | 0 on some providers; Aave-class ~5–9 bps |
| **Failed-race gas** | Lost when outbid *after* public submission | Eliminated by private bundles |
| **Infrastructure** | $200–500/mo+ fixed (RPC/dedicated node, indexers, relay access) | The real barrier to entry |

Per-chain minimum net thresholds reflect the residual: **Ethereum L1 only large arbs clear (>~$50 gross, >~$5 net); Arbitrum/Base micro-arbs viable (cents); Solana near-zero gas makes sub-dollar arbs viable via Jito.** Aggregate shape: high win-rate, small-win, near-zero-overnight-exposure P&L. The `expected_sharpe: 1.0` in frontmatter is for a **competent non-elite** operator once idle inventory across chains is in the denominator; elite searchers do far better — that gap is their *latency* edge, not a strategy any page can hand you.

## Capacity limits

- **Per-opportunity capacity** is bounded by the size of the underlying inefficiency (the swap being back-run, the position being liquidated) and DEX depth — not by searcher capital, since atomic flash-loan execution needs none.
- **Strategy-wide capacity** is bounded by the *number* of opportunities and your **win rate** against rivals. More capital does not buy more wins; faster detection and higher bids do.
- **Crowding is high.** A small set of dominant searchers captures most Ethereum-mainnet flow. Realistic capacity for a *new* entrant is the long tail incumbents miss, plus less-contested chains (newer L2s, app-chains, Solana). Aggregate atomic-arb MEV across major chains has run in the low hundreds of millions/year (Flashbots/EigenPhi), split among hundreds of searchers; a single operator's realistic net extraction is low single-digit $M/yr — hence `capacity_usd: 5000000`.

## What kills this strategy

Mapped to [[failure-modes]]:

- **Losing the latency race (Failure Mode: infra disadvantage).** Incumbents with co-located nodes, lower-latency RPC, and direct builder integrations win consistently; a slower entrant's bundles never land.
- **Bid compression to zero edge (crowding).** As competition intensifies, builders extract nearly all gross via the bid, leaving no residual.
- **Encrypted / private mempools.** SUAVE, Shutter, threshold encryption, and opt-in private orderflow (MEV-Share, MEV-Blocker, Flashbots Protect) erode the *informational* edge by hiding pending intent — and specifically starve **sandwiching**.
- **Protocol-internal capture.** Liquidator vaults, protocol-owned ordering, and MEV-internalizing AMM designs (**CoW Protocol** batch auctions, MEV taxes, Uniswap v4 hooks) remove flow before external searchers can act.
- **Builder/relay trust failure.** A builder front-running or unbundling your transactions destroys the assumption that private submission is safe.
- **Smart-contract / routing bug.** A flaw in the searcher's execution contract can drain it or turn an "atomic, risk-free" trade into a one-sided fill on a large flash-loan leg.

## Kill criteria

The searcher operation is halted (paused, per-chain) on any of:

1. **Bundle inclusion rate** below the level where infrastructure cost exceeds net MEV for **30 consecutive days**.
2. **Median net profit per landed bundle** below the gas-plus-overhead breakeven for the target chain.
3. **Required builder bid > 90% of gross on > 80%** of won opportunities for a month — the auction is fully competitive; retire that venue.
4. **Any single execution loss > 2% of allocated capital** from a routing or revert-protection bug — halt all chains until root-caused.
5. A target venue introduces **protocol-internal ordering / liquidator capture** that removes the addressable flow (the designed-away scenario).

See [[when-to-retire-a-strategy]]. MEV is *venue-migratable*: as one chain's auction saturates, the addressable edge moves to newer/cheaper chains — so per-chain kill-and-migrate is usually right, whole-strategy retirement rarely.

## Advantages

- **Atomic execution** — bundles land profitably or revert at no cost (Flashbots/Jito), eliminating leg risk and, when private, sandwich exposure to *you*.
- **No directional market risk** — DEX-arb/backrun/JIT profit is independent of market direction.
- **Capital-light** — flash loans remove standing inventory for the atomic strategies.
- **Computable economics** — gross profit and builder bid are known before submission; skip anything that does not clear.
- **Regenerating opportunity set** — every new AMM design, fee tier, and L2/app-chain resets the competitive math for a window.

## Disadvantages

- **Extreme competition and crowding** — a few dominant searchers capture most flow; the builder takes most of the residual.
- **Latency arms race** — competitive operation needs custom nodes, co-location, and direct builder relationships.
- **Smart-contract and builder/relay counterparty risk** — a contract bug or a dishonest builder can be catastrophic.
- **Eroding edge** — private/encrypted mempools and protocol-internal capture shrink the addressable opportunity over time.
- **Ethical and regulatory overhang** — sandwiching extracts directly from users; front-running is illegal in traditional markets and MEV's legal status is unresolved.
- **Un-backtestable honestly** — gross-only backtests of MEV are the most over-stated number in crypto; the auction takes most of the gross (see [[slippage-optimal-pathfinding#Validation-and-backtesting]]).

## Sources

- [[flashbots]] documentation (docs.flashbots.net) — bundles, relays, MEV-Share.
- Jito (Solana) block-engine and tip documentation — the Solana MEV supply chain.
- EigenPhi (eigenphi.io) — MEV transaction analysis and searcher concentration data.
- Vitalik Buterin et al., MEV literature; Flashbots research on the searcher→builder→proposer supply chain.
- Uniswap v3 core whitepaper — concentrated-liquidity mechanics underlying JIT.
- CoW Protocol / batch-auction and MEV-internalization designs — the designed-away context.
- General market knowledge; companion pages [[mev-execution-guide]] and [[slippage-optimal-pathfinding]] carry the execution and sizing detail. No single external source ingested yet.

## Getting the Data (CryptoDataAPI)

The core MEV feed is a low-latency mempool/node connection (not a REST API). CryptoDataAPI supplements it with DEX pool discovery, token-security screening (rug/honeypot avoidance before touching a new pool), and cross-exchange liquidation context for liquidation MEV:

- `GET /api/v1/dex/new-pools` — newest launches, multi-chain (new-pool / JIT / sniping candidates)
- `GET /api/v1/dex/trending` — trending DEX pools (Solana/Ethereum/Base/BSC/Arbitrum)
- `GET /api/v1/dex/token/{chain}/{address}` — token info + top pools for routing
- `GET /api/v1/dex/security/{chain}/{address}` — token security report (rug/honeypot detection) before executing against a pool
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations context for [[liquidation-cascade-arbitrage]]

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/dex/security/ethereum/0xTOKEN"
```

Auth: `X-API-Key` header. Catalogs: [[cryptodataapi-dex]], [[cryptodataapi-market-intelligence]].

## Related

- [[mev-execution-guide]] — how to actually submit: bundle construction, gas bidding, mempool monitoring, MEV protection
- [[slippage-optimal-pathfinding]] — exact trade sizing against AMM slippage curves (the analytical layer)
- [[mev]] — what MEV is, conceptually
- [[flashbots]] — the dominant Ethereum MEV relay/infrastructure; [[jito]] — the Solana equivalent
- [[flash-loan-arbitrage]] — capital-free funding for atomic MEV legs
- [[liquidation-cascade-arbitrage]] — liquidation MEV submitted via bundles
- [[cross-exchange-arbitrage]] — the off-chain equivalent of DEX arbitrage
- [[triangular-arbitrage]] — multi-pair price inconsistency exploitation
- [[defi-yield-farming]] — a DeFi-native strategy that interacts with MEV (JIT dilutes passive LPs)
- [[gas-fees]] — the cost that dominates on-chain MEV economics
- [[ethereum]] / [[uniswap]] — the primary venues
- [[ai-mev]] — the ML angle (mempool classification, bid shading, RL strategy selection)
- [[edge-taxonomy]] / [[failure-modes]] / [[when-to-retire-a-strategy]]

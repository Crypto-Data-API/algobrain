---
title: "MEV-Burn Economics"
type: concept
created: 2026-04-26
updated: 2026-06-11
status: good
tags: [mev, ethereum, eip, economics, defi]
aliases: ["MEV Burn", "Execution Tickets", "EIP-7732 MEV-Burn"]
related: ["[[mev-strategies]]", "[[mev-execution-guide]]", "[[dex-pool-triangular-arbitrage]]", "[[intent-based-arbitrage]]"]
domain: [market-microstructure]
prerequisites: ["[[mev-strategies]]", "[[ethereum-pos]]"]
difficulty: advanced
---

# MEV-Burn Economics

**MEV-Burn** refers to a family of Ethereum protocol proposals that redirect part of the value extracted by validators (currently captured via priority fees and MEV-Boost block bids) toward burning ETH — analogous to how EIP-1559 burns the base fee. The leading variants under discussion 2024-2026 are **MEV-Burn proper** (Justin Drake's PBS-aware burn) and **Execution Tickets** (proposer-builder market with auction-burn). The economic effect is to compress validator income from MEV while making ETH more deflationary, fundamentally re-pricing arbitrage strategies that depend on bidding up gas to capture MEV.

## What MEV-Burn Does

Currently on Ethereum (post-Merge, pre-MEV-Burn):

1. Searcher finds an [[dex-pool-triangular-arbitrage|arbitrage]] worth $100.
2. Searcher bids $90 priority fee + $10 keep (90% to validator, 10% to searcher).
3. MEV-Boost auctions the slot to highest-paying builder; winning builder pays validator $90.
4. Validator income = $90 / slot (on top of base ETH issuance ~$5).

Under MEV-Burn:

1. Same arbitrage worth $100.
2. Builder bid auctioned via PBS, but with a **floor bid** set by the *attesters* (committee separate from proposer).
3. The floor bid amount is **burned** (sent to 0x0).
4. Validator only receives the *delta* above the floor.

So if attester floor is $80 of the $100 bid: $80 burned, $20 to validator, $0 to searcher. Searcher participation requires bidding above the floor.

## Why It Matters for Arbitrage

| Variable | Pre-Burn | Post-Burn |
|----------|----------|-----------|
| Searcher capture | 10-20% | 0-5% (floor compresses margin) |
| Validator capture | 80-90% | 5-15% (delta-above-floor) |
| Burned to protocol | 0% | 70-90% (floor) |
| Strategy viability | High-margin profits viable | Only ultra-high-margin survive |

The economic effect collapses the searcher business at the margin. Arbs that net <$50 today become unprofitable post-burn because the attester floor will exceed the gross profit.

Strategies most affected:
- **High-frequency [[dex-pool-triangular-arbitrage|cyclic arb]]:** small per-trade profits ($30-150) — likely killed.
- **[[liquidation-cascade-arbitrage|Liquidations]]:** large bonuses survive but margin compresses.
- **Sandwich attacks:** become marginal — most are <$200 gross.
- **[[intent-based-arbitrage|Intent-based / off-chain]] arb:** unaffected (settles outside the public block-space auction).

## Implementation Status (as of 2026-04)

| Proposal | Status | Earliest Live |
|----------|--------|---------------|
| MEV-Burn (Drake) | Research / EIP draft | Pectra+1 fork (2027+) |
| Execution Tickets | Earlier-stage research | Post-2027 |
| Slot Auctions (Buterin) | Discussion | Post-2027 |

No MEV-Burn variant is live on mainnet as of the current date. ETH supply has been net-deflationary since the Merge purely from EIP-1559; MEV-Burn would deepen that.

## Second-Order Effects

1. **Builder centralization risk reduces.** Currently 4 builders (beaverbuild, Titan, rsync, Flashbots) win >90% of slots. Burning the floor removes the marginal-bid moat.
2. **Solo-staker incentive improves *relative* to MEV-Boost-using validators.** Today solo-stakers earn 30-50% less than MEV-Boost users. Post-burn, both earn the delta-above-floor — gap closes.
3. **Searcher migration to L2s and off-chain venues.** Searchers will follow MEV. Expect Solana, Hyperliquid, intent systems to absorb the displaced flow.
4. **Cross-chain arb premium widens.** Cross-chain MEV (Hyperlane, LayerZero) is harder to burn — searcher activity there grows.

## Detection / Modeling

To anticipate strategy survival post-burn, model:

```python
expected_floor_bp = historical_winning_bid * 0.85  # attester sets ~85% of bid
margin_post_burn = gross_profit - expected_floor - gas
if margin_post_burn < min_threshold:
    strategy_at_risk = True
```

Top searchers (jaredfromsubway.eth, etc.) are publicly modeling this and have begun migrating to L2 + off-chain in 2025.

## Sources

- Justin Drake, *MEV-Burn — a Simple Design* (Ethereum Research, 2023).
- Vitalik Buterin, *Endgame* (2021); follow-ups 2024-2025.
- Toni Wahrstätter, *Time is Money: Strategic Timing Games in PoS* (2023).
- Flashbots research blog: PBS+, SUAVE, MEV-Burn analyses.
- ethresear.ch threads on Execution Tickets.

## Related

[[mev-strategies]] · [[mev-execution-guide]] · [[dex-pool-triangular-arbitrage]] · [[liquidation-cascade-arbitrage]] · [[intent-based-arbitrage]] · [[private-mempool-arbitrage]] · [[ethereum-pos]]

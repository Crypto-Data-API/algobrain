---
title: "Slashing"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [crypto, ethereum, risk-management]
aliases: ["slashing", "Slashing", "slashing penalty", "validator slashing"]
domain: [market-microstructure]
prerequisites: ["[[proof-of-stake]]", "[[staking]]"]
difficulty: intermediate
related: ["[[staking]]", "[[proof-of-stake]]", "[[restaking]]", "[[ethereum]]", "[[liquid-staking]]"]
---

Slashing is the penalty mechanism in [[proof-of-stake]] networks where a portion of a validator's staked capital is destroyed (or redistributed) as punishment for misbehavior. It is the cryptoeconomic backbone of PoS security: validators must have meaningful skin in the game, so that attacking the network is more expensive than the gain from attacking it. Without slashing, a malicious actor could validate conflicting histories at no cost.

## Slashable Offenses on Ethereum

[[ethereum|Ethereum]] defines two slashable offenses:

- **Equivocation / double-signing** — a validator proposes two different blocks for the same slot, or signs two conflicting attestations. This is typically caused by a validator accidentally running the same keys on two machines (a failover mistake) or by a malicious operator trying to support two forks.
- **Surround voting** — a validator signs attestations that contradict each other by "surrounding" an earlier vote, undermining finality.

## The Slashing Process

When a slashable offense is detected and reported on-chain, the protocol applies a multi-stage penalty:

1. **Initial penalty** — at least 1 ETH burned immediately
2. **Correlation penalty** — scales with the number of validators slashed in a nearby window, on the theory that mass slashing implies a coordinated attack and deserves harsher punishment; can reach up to the full stake (~32 ETH) in the worst case
3. **Forced exit** — the validator is ejected from the active set and its remaining balance is withdrawn after a delay
4. **Gradual leak** — small penalties accrue during the exit period

## Historical Slashing

Slashing on Ethereum has been rare. Since the Beacon Chain launched in December 2020, fewer than 500 validators out of ~1M have been slashed, and most were operator mistakes (misconfigured infrastructure) rather than attacks. The median penalty has been around 1 ETH — a minor fraction of the 32 ETH stake.

## Slashing in Restaking

[[restaking]] introduces additional slashing conditions. Each Actively Validated Service (AVS) defines its own slashable offenses. A single pool of ETH may therefore be subject to Ethereum consensus slashing **plus** a slashing condition per AVS it helps secure — compounding risk in exchange for compounding yield.

## Liquid Staking and Slashing Dispersion

[[liquid-staking]] pools distribute slashing risk across many validators. If Lido operates 100,000 validators and one is slashed for 1 ETH, stETH holders collectively absorb a loss of ~0.00001% — effectively imperceptible. This dispersion is one of the key reasons LSTs have achieved dominant market share.

## Trading Relevance

Slashing is a direct, asymmetric tail risk on any staking or [[restaking]] yield. A trader or allocator chasing staking APR must price it as the cost side of the trade: the headline yield (e.g. ~3-4% on ETH) is only attractive net of expected slashing loss and operational risk. Because slashing is rare but severe, it behaves like a short-volatility / insurance-selling payoff — steady carry punctuated by occasional sharp drawdowns, often correlated across validators run on the same client or infrastructure. This makes **client and operator diversity** a real risk-management lever: the correlation penalty means concentrating stake on one dominant client or one node operator turns an individual mistake into a systemic, max-severity event. For [[liquid-staking]] tokens (stETH, etc.), slashing risk is socialized and diluted across the validator set, which is why LSTs trade at only a small discount to spot and why their slashing-adjusted yield is the relevant comparison for any staking-yield-arbitrage trade. In [[restaking]], stacking multiple AVS slashing conditions on the same collateral compounds this tail — the extra yield is explicit compensation for taking on additional, sometimes opaque, slashing exposure.

## Related

- [[staking]]
- [[proof-of-stake]]
- [[restaking]]
- [[liquid-staking]]

## Sources

- Ethereum.org, "Proof-of-stake (PoS)" and "Attestations / Slashing" documentation — official description of slashable offenses (double-signing, surround voting) and the multi-stage penalty
- Buterin, V. et al., "Combining GHOST and Casper" (Casper FFG paper) — the cryptoeconomic finality and slashing framework underpinning Ethereum consensus
- EigenLayer whitepaper, "The Restaking Collective" — AVS-defined slashing conditions and pooled-security risk in restaking

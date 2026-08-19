---
title: "ZK-Rollup"
type: concept
created: 2026-07-17
updated: 2026-08-19
status: draft
tags: [crypto, on-chain, market-microstructure, ethereum]
aliases: ["ZK-Rollups", "Zero-Knowledge Rollup", "Validity Rollup", "zkEVM"]
domain: [crypto, market-microstructure]
prerequisites: ["[[zero-knowledge-proofs]]", "[[layer-1]]", "[[layer-2]]"]
difficulty: advanced
---

# ZK-Rollup

A **ZK-rollup** is a [[layer-2]] scaling design that executes transactions off Ethereum L1, then proves their correctness with a cryptographic **validity proof** (a zk-SNARK or zk-STARK) rather than assuming correctness and relying on a dispute window. This page covers the rollup architecture and its trading implications; the underlying cryptography — how a validity proof actually works, SNARK vs STARK trade-offs — lives on [[zero-knowledge-proofs]]. The competing L2 correctness model, which assumes validity and challenges it after the fact, is covered on [[optimistic-rollup]].

## How It Works

A ZK-rollup's block lifecycle has four steps: a **sequencer** orders and batches transactions off-chain; a **prover** executes the batch and generates a validity proof that the resulting state transition is correct; the batch's compressed data (calldata, or blob space since the March 2024 Dencun upgrade) and the proof are posted to Ethereum L1; an on-chain **verifier contract** checks the proof — a computation that is cheap and fast regardless of how large the underlying batch was — and, if valid, immediately finalizes the new state root. Because correctness is proven rather than assumed, there is no fraud-proof challenge window: withdrawals are gated only by proof-generation time (minutes to roughly an hour today), not the 7-day wait optimistic rollups require.

**zkEVM equivalence taxonomy.** Not all ZK-rollups run the EVM the same way. Vitalik Buterin's informal Type 1-4 spectrum ranks them by compatibility versus proving speed:

| Type | Compatibility | Proving cost | Examples |
|------|---------------|---------------|----------|
| Type 1 | Fully Ethereum-equivalent, no code changes needed | Slowest to prove | Full Ethereum-equivalent provers (research-stage, e.g. some Taiko configurations) |
| Type 2 | EVM-equivalent bytecode, minor state-tree differences | Slow | zkSync Era's ambition, Polygon zkEVM's later stages |
| Type 3 | Mostly EVM-equivalent, a few opcodes unsupported/altered | Faster | Earlier Polygon zkEVM, Scroll pre-full-equivalence |
| Type 4 | High-level language compiled to a custom VM, not bytecode-equivalent | Fastest | StarkNet (Cairo VM) |

The trade-off is structural: the closer a rollup gets to perfect Ethereum equivalence, the harder (and slower) it is to generate a validity proof for arbitrary EVM execution, which is why fully Type-1 ZK-rollups remained rare even years after the concept was proposed.

**The prover market.** Generating a SNARK/STARK for a full batch of EVM execution is computationally heavy — historically requiring specialized GPU or FPGA clusters running for minutes per batch. Whoever controls proving controls a rollup's liveness, so "decentralizing the prover" (letting many independent parties compete to generate proofs, as opposed to one operator-run cluster) is an active engineering race across the sector, alongside sequencer decentralization.

## Concrete Examples

- **StarkEx / StarkNet (StarkWare, since 2020):** uses STARK proofs (no trusted setup) and the custom Cairo VM. StarkEx powered dYdX v3's order book, ImmutableX's NFT minting, and Sorare — at peak, StarkEx alone processed more transactions than Ethereum L1. The STRK token airdropped to early users in February 2024.
- **zkSync Era (Matter Labs, mainnet March 2023):** the first EVM-compatible ZK-rollup at production scale, built around native account abstraction and the "ZK Stack." The ZK token airdropped in June 2024.
- **Polygon zkEVM (mainnet March 2023):** pursued Type 2/3 EVM equivalence and is a core piece of Polygon's cross-chain "AggLayer" vision.
- **Scroll:** built in close collaboration with the Ethereum Foundation, pursuing bytecode-level zkEVM equivalence rather than a custom VM.
- **Linea:** ConsenSys's zkEVM, integrated tightly with MetaMask's user base.
- **Airdrop farming wave (2023-2024):** because none of the major ZK-rollups had launched a token at the time, on-chain activity across zkSync, StarkNet, and later LayerZero-adjacent points programs became a large, explicit farming target — one of the clearest recent examples of [[airdrop-farming]] driving real transaction volume ahead of any underlying product-market fit signal.

## Trading Relevance

- **[[cross-l2-arbitrage]]:** ZK-rollups' faster native finality (minutes, once a proof posts) versus optimistic rollups' 7-day withdrawal window changes the bridge-choice calculus for the strategy — a ZK-rollup can, in principle, support tighter inventory cycles without relying on third-party fast bridges.
- **[[airdrop-farming]]:** STRK (Feb 2024) and ZK (Jun 2024) are the canonical large-cap ZK-rollup airdrops; both shaped how subsequent points-farming campaigns across the sector were designed and gamed.
- **[[zkml-predictive-mev]]:** the same proving infrastructure that makes ZK-rollups work is reused to let a searcher prove that an MEV bundle was generated by a specific model without revealing the model's weights — a direct spillover of ZK-rollup proving tech into strategy design.
- **[[mev-strategies]]:** MEV extraction differs from L1 PBS/Flashbots on every ZK-rollup, since a single (usually centralized today) sequencer controls transaction ordering pre-proof; sequencer-decentralization roadmaps are a monitorable catalyst for MEV strategy design on each rollup.
- **Proving-cost economics as an investment lens:** a ZK-rollup's real unit economics depend on prover cost per batch versus fees collected — a fundamental signal distinct from, and harder to observe than, simple TVL or transaction-count metrics used for optimistic rollups.

## Related

- [[zero-knowledge-proofs]] — the underlying cryptography (SNARK vs STARK, completeness/soundness/zero-knowledge properties)
- [[optimistic-rollup]] — the competing fraud-proof-based L2 correctness model
- [[layer-2]] — the broader rollup/sidechain/state-channel scaling category
- [[layer-1]] — the Ethereum base layer ZK-rollups settle to and inherit security from
- [[cross-l2-arbitrage]] — arbitrage strategy directly affected by ZK-rollup finality speed
- [[airdrop-farming]] — the dominant early-adoption incentive for ZK-rollup users
- [[zkml-predictive-mev]] — ZK proving reused for verifiable, private MEV model logic
- [[mev-strategies]] — sequencer-specific MEV architecture on ZK-rollups

## Sources

- General cryptography/L2 infrastructure knowledge; no specific wiki source ingested yet.

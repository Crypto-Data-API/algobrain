---
title: "Modular Blockchains"
type: concept
created: 2026-07-19
updated: 2026-08-20
status: draft
tags: [crypto, on-chain, market-microstructure]
aliases: ["Modular Blockchain", "Modular Stack", "Modular Thesis"]
domain: [crypto, market-microstructure]
prerequisites: ["[[layer-1]]", "[[layer-2]]", "[[data-availability]]"]
difficulty: intermediate
---

# Modular Blockchains

**Modular blockchains** split the four core functions of a blockchain — execution, settlement, consensus, and [[data-availability|data availability]] — across specialized, independently scalable layers, instead of one validator set handling all four itself. A [[layer-2|rollup]] that executes transactions, posts its data to Celestia, and settles disputes on Ethereum is a modular stack assembled from three separate chains. The opposing design, a **monolithic** chain like [[solana|Solana]], bundles all four functions into a single validator set and a single block — simpler to reason about and, at the base layer, typically cheaper, but unable to scale any one function independently of the others.

## How It Works

The four functions, and what each does:

1. **Execution** — running the transactions and computing the resulting state (what a rollup's sequencer and virtual machine do).
2. **Settlement** — the layer that verifies proofs (fraud proofs or validity proofs) and finalizes disputes, providing the ultimate security backstop and the place bridges anchor to. Ethereum is the dominant settlement layer today.
3. **Consensus** — ordering transactions into blocks and agreeing on that ordering across a validator set.
4. **Data availability** — publishing the raw transaction data so anyone can independently reconstruct and verify state, covered in depth on [[data-availability]].

A monolithic chain does all four with one validator set and one block cadence: throughput is capped by whatever the slowest function can sustain on commodity hardware, and there's no way to add capacity to, say, DA without also touching execution. A modular stack decouples them: an execution layer ([[optimistic-rollup|optimistic]] or [[zk-rollup|zk-rollup]]) can be swapped, upgraded, or run in parallel with others, while settlement and DA stay fixed — and DA capacity itself can be sourced from whichever provider (Ethereum blobs, Celestia, EigenDA) offers the best cost/security tradeoff at a given time, independent of how execution is done.

**The core bet behind modularity** is that specialization beats generalization at scale — the same reasoning that led general-purpose computers toward separate CPUs, GPUs, and storage tiers rather than one chip doing everything. The core bet behind the monolithic counter-argument is that keeping execution and consensus in the same trust domain avoids the added latency, bridging risk, and composability breaks that come from splitting a transaction's lifecycle across multiple chains — an app-to-app call within a monolithic chain is atomic and same-block; the equivalent call across a rollup and its settlement layer is not.

**Shared sequencing and "based" rollups** are attempts to recover some of monolithic composability within a modular stack — coordinating transaction ordering across multiple rollups (or, in a "based" rollup, delegating ordering directly to the settlement layer's own block proposers) so that cross-rollup transactions can be sequenced atomically despite execution being split across chains.

## Concrete Examples

- **Celestia (mainnet October 2023):** the reference implementation of a minimal, DA-only chain — it deliberately does not execute transactions, only orders and guarantees availability of data, letting rollups (including "sovereign rollups" that settle nowhere but Celestia itself) plug in.
- **Ethereum's own modular pivot:** since [[ethereum|Ethereum]]'s roadmap shifted toward a rollup-centric future (formalized well before EIP-4844), L1 has increasingly positioned itself as primarily a settlement and DA layer (via blobs), with execution pushed to [[layer-2|L2s]] — Ethereum did not stay monolithic even though it started that way.
- **EigenLayer / EigenDA (2024):** rather than bootstrapping a new token and validator set from zero, EigenDA reuses Ethereum's existing economic security via restaking, letting operators who've already staked ETH opt in to also secure a DA layer — an example of modularity extending into shared security, not just shared function.
- **Rollup frameworks as modular tooling:** the OP Stack (Optimism's Superchain) and Arbitrum Orbit both let a team assemble a new chain by choosing its execution client, DA layer, and settlement target independently — the productization of the modular thesis into a deployable stack.
- **Solana as the monolithic counter-case:** by keeping execution, consensus, and DA in one validator set with a fast native block time, Solana avoids cross-layer bridging risk and latency, at the cost of requiring high-spec validator hardware and having no independent DA market to price separately from execution.

## Trading Relevance

- **Narrative-basket positioning:** "modular vs. monolithic" is one of the more persistent multi-quarter narratives in crypto; taking a position in modular-stack tokens (Celestia, EigenLayer-linked assets, rollup-framework tokens) versus high-throughput monolithic L1s (Solana and peers) is effectively a bet on which architecture captures the next leg of on-chain activity.
- **[[l1-l2-rotation]]:** relative activity and fee capture between Ethereum-plus-L2s (the modular cohort) and monolithic alt-L1s is a rotation signal this narrative-catalog entry tracks directly.
- **[[cross-chain-arbitrage]] and [[cross-l2-arbitrage]]:** modularity multiplies the number of distinct execution environments an asset can exist across, which is the structural precondition for both strategies — more fragmentation, more arbitrage surface.
- **[[airdrop-farming]]:** new modular-stack chains (rollups launched via OP Stack, Orbit, or on Celestia DA) have been a recurring source of points and airdrop campaigns, following the same pattern documented on [[optimistic-rollup]].
- **Infrastructure risk sizing:** a modular stack's overall security is only as strong as its weakest layer — a chain with strong execution but a validium-style off-chain DA committee inherits that committee's trust assumptions regardless of how secure its settlement layer is, a distinction worth pricing into any smart-contract risk assessment.

## Related

- [[data-availability]] — the specific layer this page's taxonomy separates out
- [[layer-2]] — rollups, the execution layer in most modular stacks
- [[layer-1]] — Ethereum, the dominant settlement layer
- [[celestia]] — the reference minimal DA-only modular chain
- [[eigenlayer]] — restaking-secured shared infrastructure, including EigenDA
- [[solana]] — the reference monolithic-chain counter-design
- [[optimistic-rollup]] / [[zk-rollup]] — the two dominant execution-layer designs in a modular stack
- [[l1-l2-rotation]] — narrative-catalog entry tracking modular-vs-monolithic activity rotation
- [[cross-chain-arbitrage]] / [[cross-l2-arbitrage]] — strategies whose opportunity set grows with modular fragmentation

## Sources

- General crypto/rollup-infrastructure knowledge; no specific wiki source ingested yet.

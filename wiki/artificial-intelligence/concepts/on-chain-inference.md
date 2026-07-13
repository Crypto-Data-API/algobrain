---
title: "On-Chain Inference"
type: concept
created: 2026-04-11
updated: 2026-06-12
status: good
tags: [crypto, defi, machine-learning]
aliases: ["On-Chain AI", "On-Chain ML", "Smart Contract Inference"]
domain: [market-microstructure]
difficulty: intermediate
related: ["[[ritual-network]]", "[[allora]]", "[[bittensor-subnets]]", "[[zkml]]", "[[ai-oracles]]", "[[defai]]", "[[decentralized-ai]]", "[[restaking-and-ai]]", "[[statistical-proof-of-execution]]"]
---

# On-Chain Inference

**On-chain inference** is the practice of calling a machine-learning model from inside a smart contract as a native step of on-chain computation. Rather than a human (or an off-chain bot) querying a model and then submitting the result as a transaction, the smart contract itself requests an inference during its own execution and uses the result to make decisions — dynamic collateral ratios, adaptive fee curves, risk-scored lending, prediction-market resolution, and more.

## Why It's Hard

Smart contract execution environments (EVM and its cousins) are built for small, deterministic computations — arithmetic, hashing, state lookups — metered in gas. Running a modern neural network directly inside that environment is, in most cases, millions of times more expensive than the model cost would be off-chain. This is why "on-chain inference" rarely means literally executing the model on the blockchain's native VM. It almost always means **calling an external inference network with some form of verification guarantee**.

The three competing architectures reflect different trade-offs on cost, trust, and latency:

## The Three Architectures

### 1. Oracle / Co-Processor Pattern

A smart contract emits a request; an off-chain node (or network of nodes) runs the inference and returns the result along with a proof or attestation; the contract consumes the result in the next block. This is the architecture used by [[ritual-network|Ritual]], Chainlink Functions, ORA, and most production systems today.

- **Pros**: works with any model size; minimal on-chain overhead
- **Cons**: adds at least one block of latency; trust assumption depends on the verification method

### 2. Rollup / Co-Hosted Pattern

The inference runs inside a specialized rollup or app-chain where the sequencer also handles ML execution, and the rollup posts results (or compressed proofs) back to the settlement layer. [[allora]] and 0g are closer to this end of the spectrum.

- **Pros**: inference is "native" to the execution environment; tighter integration with DeFi primitives
- **Cons**: limited to models the rollup infrastructure supports; harder to scale to large foundation models

### 3. ZK-Verified Pattern

A zero-knowledge proof is generated alongside the inference, cryptographically guaranteeing that the claimed output came from the claimed model on the claimed input without revealing any of them. See [[zkml]] for details.

- **Pros**: strongest trust model; no re-execution or committee required
- **Cons**: prover cost is currently 10³–10⁶× the raw inference cost; practical only for small models or selective inputs

## Gas and Latency Constraints

The hard numerical reality: as of 2026, running even a small (1M parameter) model directly inside the EVM is impractical — you hit block gas limits before completing a forward pass. This means every production "on-chain inference" system is really an **off-chain-compute + on-chain-verification** hybrid. The interesting design space is in how verification is amortized, who pays for it, and what fraction of calls can tolerate a one-block lag.

Expect latency of at least 1 block (roughly 2–12 seconds depending on chain) and per-call cost in the $0.10–$10 range depending on the verification path and model size. High-frequency applications are excluded by construction.

## Projects: Inference Networks Compared

| Project | Architecture | Verification | Typical Model Size |
|---------|--------------|--------------|--------------------|
| [[ritual-network|Ritual]] | Co-processor | Committee + slashing | Large (LLMs) |
| [[allora]] | Co-hosted rollup | Topic-level consensus | Small–medium |
| [[bittensor-subnets|Bittensor]] | Off-chain network | Validator consensus | Variable by subnet |
| [[zero-gravity|0G]] | Modular DA + compute | Data availability proofs | Medium |
| ORA | Co-processor | Optimistic + zk fallback | Small–medium |
| Modulus Labs | ZK prover for ML | Zero-knowledge | Small only |

## DeFi Applications

On-chain inference is interesting to DeFi primarily because it enables **dynamic, model-driven parameters** that previously had to be hard-coded or manually governed:

- **Risk-based lending** — lending protocols adjust collateral factors based on an ML-estimated default probability per borrower
- **Adaptive AMM fees** — liquidity pools increase fees when a model predicts elevated toxicity or volatility
- **Dynamic margin** — perp DEXes scale initial margin against an ML volatility forecast
- **Prediction-market resolution** — markets close based on ML-classified event outcomes rather than human arbiters
- **Agent-driven treasury management** — DAOs route treasury allocations based on agent recommendations (see [[ai-agent-daos]])

In practice, most of these remain demos or pilots as of early 2026. The gap between "technically possible" and "economically superior to a simpler hard-coded rule" is wide, and on-chain inference currently wins only when verifiability or permissionless composability is the key property — not when cost or speed is.

## See Also

- [[zkml]] — Zero-knowledge verification of ML outputs
- [[ai-oracles]] — Prediction-as-a-service oracle networks (closely related pattern)
- [[decentralized-ai]] — Parent movement
- [[defai]] — The DeFi-specific consumption layer for inference
- [[ritual-network]] — Leading co-processor implementation
- [[allora]] — Leading rollup-style inference network
- [[statistical-proof-of-execution]] — Probabilistic verification path for inference
- [[restaking-and-ai]] — Cryptoeconomic security substrate for inference networks
- [[artificial-intelligence]] — AI section hub

## Sources

- [[2026-04-11-perplexity-ai-crypto-gaps]] — Perplexity research on decentralized AI verification approaches
- Ritual, Allora, ORA, and 0G public documentation on inference-network architectures (as of 2026)
- Modulus Labs and EZKL ZKML benchmarking writeups for prover-cost figures

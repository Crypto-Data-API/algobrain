---
title: "ZKML (Zero-Knowledge Machine Learning)"
type: concept
created: 2026-04-11
updated: 2026-06-12
status: good
tags: [crypto, machine-learning, defi]
aliases: ["ZKML", "Zero-Knowledge ML", "Verifiable Inference"]
domain: [market-microstructure]
difficulty: advanced
related: ["[[on-chain-inference]]", "[[ritual-network]]", "[[decentralized-ai]]", "[[ai-oracles]]", "[[defai]]", "[[model-inference-vs-training]]", "[[statistical-proof-of-execution]]"]
---

# ZKML (Zero-Knowledge Machine Learning)

**ZKML** is the application of zero-knowledge cryptography to machine-learning inference: generating a cryptographic proof that a specific model produced a specific output from a specific input, without revealing any of them beyond what the verifier chooses to disclose. It is the most rigorous answer to the [[on-chain-inference|on-chain inference]] verification problem and the primary technical foundation for trust-minimized [[decentralized-ai|decentralized AI]].

## What Gets Proven

Three variants cover most ZKML use cases, each hiding a different component:

- **Proof of valid inference** — reveal the model and the output, hide (some of) the input. Useful for privacy-preserving credit scoring.
- **Proof of model integrity** — reveal the input and the output, hide the model weights. Useful when the model is proprietary but the user wants to verify they got the real thing.
- **Proof of honest evaluation** — reveal everything, but prove via succinct proof that the computation was correct so verifiers don't need to re-run it. Useful for trustless inference marketplaces.

## Three Technical Approaches

### 1. zkSNARK Circuits

Translate the model into an arithmetic circuit and generate a SNARK (Groth16, PLONK, Halo2). Leading libraries: EZKL, Giza (Orion), Modulus Labs' Remainder. This is the most common academic approach and the one most closely associated with the "ZKML" label.

- **Strengths**: succinct proofs (a few kB), constant-time verification
- **Weaknesses**: prover time can be 10³–10⁶× the raw inference time; quantization and fixed-point arithmetic introduce accuracy loss; circuit size grows with model size

### 2. Optimistic ZK / Interactive Proofs

Run the inference and post the result; require a challenge period in which anyone can re-execute and dispute with a fraud proof. Cheaper than full SNARKs because proofs are only generated on challenge. Closer in spirit to optimistic rollups than to classical ZK.

- **Strengths**: near-native inference cost in the happy path
- **Weaknesses**: challenge windows add latency; relies on at least one honest watcher

### 3. TEE-Based Verification

Use trusted execution environments (Intel SGX, AMD SEV, Nvidia Confidential Compute) to attest that the computation ran inside a sealed enclave. Not strictly "zero-knowledge" but often grouped with ZKML in practice because it solves the same trust problem.

- **Strengths**: near-native cost; works for arbitrary model size
- **Weaknesses**: hardware trust assumption; side-channel attack history

## The Cost Reality

As of early 2026, ZKML is **not yet economically practical for large models**, though the performance trajectory through 2024–2025 has been dramatic enough to change the medium-term outlook. Concrete orders of magnitude:

- Tiny models (MNIST-scale, ~tens of thousands of parameters): seconds of prover time per inference
- Small models (ResNet, ~tens of millions of parameters): minutes to hours per inference
- Large models (Llama-3-8B and up): not feasible with current general-purpose provers

This is why production DeAI systems lean heavily on the optimistic, committee-based, or probabilistic verification models (see [[on-chain-inference]] and [[statistical-proof-of-execution]]), and why ZKML demos tend to use small specialized models rather than general-purpose LLMs.

## The 2024–2026 Performance Inflection

Three technical developments between 2024 and 2026 have pushed ZKML from "research-only" toward "practical for specific applications," even if not yet for full-scale LLMs (Source: [[2026-04-11-perplexity-ai-crypto-gaps]]):

### 1. Overhead Trajectory: 1,000,000× → 10,000×

The ratio of prover time to raw inference time dropped roughly 100× between 2024 and 2025, and is expected to drop another 5–10× through 2026 as GPU-optimized provers ship. This is not enough to make ZKML on Llama-3-70B practical, but it is enough to make ZKML on a 100M-parameter classifier run in seconds rather than hours.

### 2. Proof Compression via Folding

Folding schemes (Nova, HyperNova, SuperNova, and their descendants) compress proof size in a way that does not scale with the complexity of the computation being proven. Concrete reported numbers: ResNet-50 proof size dropped from **1.27 GB to under 100 KB** with folding-based systems. GPT-style transformer models become more feasible because proof size no longer grows with sequence length. By 2026 every major ZKML framework is expected to integrate folding as a standard component (Source: [[2026-04-11-perplexity-ai-crypto-gaps]]).

### 3. Operator Compilers Replacing Per-Operator Implementations

Early ZKML frameworks supported a hand-curated subset of ONNX operators (typically ~50 out of 120+). By late 2025 multiple frameworks had shipped **operator compilers** — generalized circuit templates that can compile any computational graph directly, removing the "does the framework support my model's layers" bottleneck. The shift is analogous to moving from hand-written assembly to an optimizing compiler: it makes the tooling usable for models the framework authors never anticipated.

### Concrete Benchmarks

Specific results from the 2025 cohort worth knowing:

- **zkPyTorch** (March 2025) — proved VGG-16 image classifier inference in ~2.2 seconds
- **Lagrange DeepProve** (August 2025) — first serious attempt at large LLM inference proving; performance numbers still preliminary but orders of magnitude ahead of prior baselines
- **EZKL** — continues to be the reference open-source ZKML toolkit, with active development on folding support

These are not general-purpose LLM-scale proofs. They are targeted wins on specific model shapes, and they map to the realistic near-term deployment path for ZKML: **verify specific small models for high-value decisions**, not "verify every inference in production."

## Use Cases Where ZKML Already Makes Sense

- **Verifiable oracle predictions** — prove a price or volatility forecast came from the claimed model
- **Private credit scoring** in DeFi — prove your score without revealing the inputs
- **MEV-resistant agents** — prove an agent's trading decision was not front-runnable information
- **Model-integrity attestation** — prove an AI service is serving the model it claims to serve
- **Compliance proofs** — prove a bank's risk model was applied correctly without disclosing the model

## Leading Projects

| Project | Focus |
|---------|-------|
| EZKL | Open-source ZKML toolkit for SNARK-ifying ONNX models |
| Giza | ZKML infra on Starknet, Orion library |
| Modulus Labs | ZK prover specialized for ML, targets L2 integrations |
| Worldcoin (orb attestation) | TEE-based attestation pipeline for iris models |
| Ora | Co-processor with optimistic and ZK verification paths |

## Why Traders Should Care

ZKML is a long-dated bet, not a near-term narrative. The relevant trading question is not "which ZKML token moons" but "at what point does verifiable inference become economically necessary for a high-value DeFi use case." Candidates: compliance-sensitive lending, on-chain insurance pricing, regulated prediction markets. If any of these take off, ZKML-adjacent projects benefit structurally. Until then, the ecosystem runs on hype, grant funding, and research credibility, not revenue.

## See Also

- [[on-chain-inference]] — The parent design pattern ZKML serves
- [[ai-oracles]] — Adjacent verification pattern for oracle feeds
- [[decentralized-ai]] — Parent movement
- [[ritual-network]] — Production inference network experimenting with ZK paths
- [[defai]] — DeFi consumption layer for verifiable inference
- [[artificial-intelligence]] — AI section hub

## Sources

- [[2026-04-11-perplexity-ai-crypto-gaps]] — overhead trajectory, folding compression figures, operator-compiler shift, and 2025 benchmark cohort
- EZKL documentation and benchmarks (ezkl.xyz) — reference open-source ZKML toolkit
- Modulus Labs, "The Cost of Intelligence" — early ZKML cost analysis and prover-overhead framing
- Kothapalli, Setty, Tzialla, "Nova: Recursive Zero-Knowledge Arguments from Folding Schemes" (CRYPTO 2022) — folding-scheme foundation
- Worldcoin and Intel SGX / Nvidia Confidential Compute documentation — TEE attestation approaches

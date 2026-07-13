---
title: "Ritual Network"
type: entity
created: 2026-04-09
updated: 2026-06-10
status: good
tags: [crypto, ai-trading, machine-learning, defi]
aliases: ["Ritual", "Ritual Network", "Infernet", "Ritual Chain"]
entity_type: protocol
founded: 2023
headquarters: "Decentralized"
website: "https://ritual.net"
related: ["[[foundation-models]]", "[[model-inference-vs-training]]", "[[bittensor-subnets]]", "[[defai]]", "[[ai-agent-tokens]]", "[[artificial-intelligence]]", "[[decentralized-ai]]", "[[on-chain-inference]]", "[[restaking-and-ai]]", "[[zkml]]"]
---

# Ritual Network

**Ritual** is a decentralized AI infrastructure project that enables smart contracts to call AI models as part of on-chain computation. Founded in 2023 by Niraj Pant and Akilesh Potti (both ex-Polychain Capital), it bridges [[foundation-models|foundation models]] and [[defi|DeFi]] by letting protocols integrate AI directly into smart-contract logic — for example, a lending protocol using a model to assess collateral risk in real time. For traders it is a pre-token venture-stage bet on the [[on-chain-inference|on-chain inference]] thesis.

## Key Facts (as of June 2026)

| Field | Detail |
|---|---|
| **Founded** | 2023, by Niraj Pant and Akilesh Potti (ex-Polychain); team from DeepMind, Paradigm, Coinbase, Citadel, Palantir |
| **Funding** | **$25M Series A (announced November 2023)** led by Archetype, with Accel, Robot Ventures, Polychain and angels; total raised ~$26M |
| **Products** | **Infernet** (decentralized AI oracle/co-processor, live since launch Nov 2023-2024; 8,000+ nodes claimed) and **Ritual Chain** (AI-native L1) |
| **Chain status** | Ritual Foundation launched and announced the **Ritual Chain public testnet**; full production mainnet **not confirmed live** as of June 10, 2026 |
| **Token** | No liquid $RITUAL token trading as of June 10, 2026; airdrop/TGE anticipated by community guides (snapshot speculation from Q3 2025 onward) |

## How It Works

1. **Infernet (live)**: a lightweight oracle library connecting off-chain AI computation to on-chain smart contracts on any EVM chain — contracts request inference, nodes execute it off-chain and deliver results with proofs
2. **Ritual Chain (in development/testnet)**: a sovereign L1 with AI-native precompiles ("Stateful Precompiles", scheduled transactions) so inference is first-class in the execution environment
3. **Cryptographic verification** ensures the inference was computed correctly (not fabricated) — spanning optimistic, [[zkml|zk]], and TEE-based approaches
4. **Results** are delivered on-chain for use in DeFi protocols, DAOs, or agent systems

## Why It Matters

Most [[ai-trading-agents|AI agents]] today interact with blockchains from the outside — calling APIs, then submitting transactions. Ritual enables AI *inside* the blockchain's execution environment, opening possibilities for:

- On-chain risk assessment for lending protocols
- AI-powered pricing for options and derivatives
- Dynamic fee adjustment based on market conditions
- Automated portfolio rebalancing triggered by model outputs

## Comparison to Bittensor

| Dimension | Ritual | [[bittensor-subnets|Bittensor]] |
|-----------|--------|-----------|
| **Focus** | On-chain AI inference | Decentralized AI training + inference |
| **Integration** | Smart contract native | Off-chain with API access |
| **Verification** | Cryptographic proof | Validator consensus |
| **Use case** | DeFi-native AI | Broad AI marketplace |
| **Token** | None live (as of June 2026) | TAO (liquid since 2021) |

## Trading Relevance

- **No direct token exposure yet**: Ritual is venture-stage; the tradeable angle is the eventual TGE/airdrop (testnet participation and Infernet node operation are the typical farming routes) — treat all airdrop-date claims as speculation
- A Ritual token launch would be a sector event for [[defai|DeFAI]] and [[ai-agent-tokens|AI-token]] baskets, comparable to prior infra TGEs
- Adoption of on-chain inference by lending/derivatives protocols would create new model-driven on-chain signals traders can read directly
- Key risk: the on-chain inference thesis remains unproven; Infernet node counts are project-reported, not independently audited

## Related

- [[foundation-models]] — Models served through Ritual
- [[model-inference-vs-training]] — Inference economics
- [[bittensor-subnets]] — Related decentralized AI network
- [[defai]] — DeFi + AI convergence
- [[on-chain-inference]] — The core thesis
- [[zkml]] — Verification technology
- [[decentralized-ai]] — Sector overview
- [[artificial-intelligence]] — AI section hub

## Sources

- Ritual Foundation, "Unveiling Ritual": https://ritualfoundation.com/blog/unveiling-ritual
- Ritual docs, Infernet ↔ Chain architecture: https://www.ritualfoundation.org/docs/architecture/infernet-to-chain
- Messari, Ritual fundraising profile: https://messari.io/project/ritual/fundraising
- Crypto-Reporter, "Ritual Foundation Launches… Announces Ritual Chain Testnet": https://www.crypto-reporter.com/press-releases/ritual-foundation-launches-to-advance-decentralized-ai-announces-ritual-chain-testnet-82570/
- Gate Learn, "What Is Ritual?": https://www.gate.com/learn/articles/a-simple-guide-to-ritual-the-open-ai-infrastructure-network/4594
- Verified via web search, 2026-06-10

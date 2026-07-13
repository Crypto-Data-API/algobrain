---
title: "RPC Poisoning"
type: concept
created: 2026-04-28
updated: 2026-06-11
status: good
tags: [crypto, defi, risk-management, security, smart-contracts, exploits]
aliases: ["RPC node poisoning", "RPC compromise", "RPC redirection attack", "node-spoofing attack"]
domain: [risk-management, crypto, market-microstructure]
difficulty: advanced
prerequisites: ["[[smart-contracts]]", "[[cross-chain-bridges]]"]
related: ["[[2026-04-18-kelp-layerzero-exploit]]", "[[dvn-compromise-patterns]]", "[[cross-chain-bridges]]", "[[smart-contract-vulnerability-taxonomy]]", "[[multi-dvn-bridge-config-arbitrage]]", "[[ai-amplified-exploit-arbitrage]]", "[[2026-exploit-target-watchlist]]", "[[2020-2024-bridge-exploits]]"]
---

**RPC poisoning** is an attack in which a malicious actor causes a dapp, bridge verifier, or oracle to read state from a compromised or attacker-controlled RPC node, then act on that false state as if it were genuine on-chain reality. The attacker doesn't break any cryptographic primitive — they break the *view* the consumer has of the chain. The [[2026-04-18-kelp-layerzero-exploit|KelpDAO / LayerZero exploit]] (April 2026, ~$290M direct loss; ~$15B TVL drain across DeFi within 48h) is the canonical case, where DDoS forced LayerZero's 1-of-1 DVN to fail over to poisoned RPC nodes and accept a forged cross-chain message.

## What an RPC node does

A blockchain RPC (Remote Procedure Call) endpoint serves queries about chain state — block contents, transaction status, contract storage reads, log queries. Most dapps, indexers, and verifiers don't run their own full nodes; they call out to RPC providers (Alchemy, Infura, QuickNode, or self-hosted nodes).

A bridge verifier, oracle, or off-chain agent making a decision based on chain state has to *trust the RPC node it's reading from*. The chain itself is honest, but the RPC node sits between the chain and the consumer — and if that node is dishonest, the consumer's view is corrupted.

## How RPC poisoning works

The attacker's goal is to make a consumer (typically a bridge verifier or oracle) read attacker-chosen state — usually a fake transaction log or contract storage value that justifies releasing funds.

### Vector 1: Compromise the RPC node directly

- Compromise a node operator's infrastructure (server, key material, DNS).
- Modify the node's response to specific queries (e.g., return a forged log claiming a deposit happened on the source chain).
- Genuine on-chain state is untouched, but the consumer reading via this node sees a corrupted view.

### Vector 2: Force failover to attacker-controlled nodes

This is the [[2026-04-18-kelp-layerzero-exploit|KelpDAO]] vector:

1. The verifier configures multiple RPC endpoints with automatic failover.
2. Attacker DDoS's the legitimate primary endpoints, making them unresponsive.
3. The verifier fails over to a backup endpoint — which the attacker has either compromised or directly operates.
4. The poisoned endpoint returns the attacker's forged response.

The verifier sees a "responsive node" and cannot easily distinguish "this is the real node, just slower" from "this is a poisoned failover."

### Vector 3: BGP / DNS hijack

- Attacker hijacks BGP routes or DNS records to redirect traffic destined for a legitimate RPC provider to attacker-controlled servers.
- Even hardware-secured verifier infrastructure can be tricked because the redirection happens at the network layer below the application.
- Limited applicability — BGP/DNS hijacks are visible to network operators and usually detected within hours — but the window can be enough.

### Vector 4: Stale-state / archive-node poisoning

- For consumers that read historical state (e.g., oracle aggregators reading prices at block N), an archive-node provider can be subtly compromised to return incorrect historical state.
- Rarely used as a primary vector but can compound other attacks.

## KelpDAO case (April 18, 2026)

Per [[2026-04-18-kelp-layerzero-exploit]] and the LayerZero post-mortem:

- The KelpDAO `rsETH` OFT (Omnichain Fungible Token) bridge ran a **1-of-1 DVN configuration** — a single Decentralized Verifier Network (LayerZero Labs) was responsible for verifying cross-chain messages.
- The attacker DDoS'd the legitimate RPC infrastructure that the DVN relied on for reading source-chain state, then surfaced poisoned RPC responses claiming that a deposit had occurred on Unichain.
- The DVN, unable to read genuine state and configured to failover, accepted the poisoned response and signed off on a cross-chain message releasing 116,500 rsETH (~$290M) from Ethereum L1 escrow.
- Stolen rsETH was immediately deposited as collateral on Aave, Compound, and Euler, with ~$236M borrowed against it before guardians could pause.
- LayerZero's post-mortem identified the mechanism precisely: **RPC poisoning + DDoS forcing failover to corrupted nodes**.
- LayerZero subsequently announced it will no longer sign messages from applications running 1-of-1 DVN configurations.

## Why this works against well-audited code

Smart-contract audits verify what happens *given correct inputs*. They cannot verify:

- Whether the verifier's RPC endpoint is genuine
- Whether failover paths preserve the verifier's security assumptions
- Whether DDoS against a single dependency can collapse the security model to single-point-of-trust

Bridge verifiers are sophisticated systems but inherit any RPC trust assumption their designers made. A "decentralized" verifier that depends on a single RPC provider is centralized in that one dependency.

## Defenses

### Multiple, diverse RPC sources with quorum

- Read source-chain state from N independent RPC providers (Alchemy + Infura + QuickNode + self-hosted + Pocket Network).
- Require K-of-N agreement before treating the response as canonical.
- The cost of an RPC-poisoning attack rises with K; compromising 5 of 7 independent providers is an order of magnitude harder than compromising 1.

### Self-hosted full nodes for critical infrastructure

- High-value bridges, oracles, and signers should run their own full nodes alongside third-party providers.
- Self-hosted node disagrees with third-party providers → halt the action and alert.

### Cryptographic state attestation

- Light-client proofs (Ethereum's light client protocol, Cosmos IBC's tendermint headers) let the consumer verify state cryptographically rather than trust the RPC's claim.
- Where light clients don't exist, MPT (Merkle Patricia Trie) proofs can be required for any consumed state.

### Failover discipline

- Halt-on-failure rather than failover-on-failure for high-value operations. If the primary RPC stops responding, *pause the protocol* rather than silently failing over.
- Per the post-KelpDAO LayerZero policy: **never accept failover during DDoS conditions** without human review.

### Multi-DVN configurations

For LayerZero specifically, the immediate mitigation is moving from 1-of-1 DVN to multi-DVN configurations (typically 2-of-3 or 3-of-5 with diverse operators). See [[dvn-compromise-patterns]] and the [[multi-dvn-bridge-config-arbitrage]] strategy.

## Trader-side implications

- **1-of-1 DVN apps are the immediate exposed surface.** Per [[multi-dvn-bridge-config-arbitrage]], short the basket of LayerZero apps still running 1-of-1 configurations 60+ days post-KelpDAO.
- **Cross-chain bridges with thin RPC diversity are the next class.** Look for bridges that publish their RPC infrastructure; ones that don't are higher-risk.
- **Oracle infrastructure.** Pyth's first-party publishers, Chainlink's multi-source aggregation, and RedStone's pull-based model all reduce RPC-poisoning surface relative to push-based oracles reading from a single RPC. Sector rotation: long Chainlink/Pyth, short newer oracles with thinner RPC architecture.
- **Watch for DDoS as a leading indicator.** RPC-poisoning attacks typically pair with DDoS against the legitimate path. Sustained DDoS on a bridge's RPC dependencies during a low-liquidity hour is a high-precision signal — short the bridge token and any apps consuming its messages.

## Related

- [[2026-04-18-kelp-layerzero-exploit]] — canonical case
- [[dvn-compromise-patterns]] — the LayerZero verifier-set companion concept
- [[cross-chain-bridges]] — broader bridge-architecture context
- [[multi-dvn-bridge-config-arbitrage]] — trader strategy
- [[smart-contract-vulnerability-taxonomy]] — vuln-class index
- [[ai-amplified-exploit-arbitrage]] — hub strategy
- [[2026-exploit-target-watchlist]] — quarterly tracker
- [[2020-2024-bridge-exploits]] — historical bridge incidents

## Sources

- LayerZero post-mortem on KelpDAO incident (April 2026)
- Galaxy Research: "KelpDAO LayerZero Exploit DeFi" (April 2026)
- [[multi-dvn-bridge-config-arbitrage]] — DVN-configuration framing
- LayerZero protocol announcements, post-incident

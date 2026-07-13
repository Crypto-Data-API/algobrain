---
title: "Blockchain"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [crypto, defi]
aliases: ["distributed-ledger", "distributed-ledger-technology", "dlt"]
domain: [market-microstructure]
prerequisites: ["[[bitcoin]]"]
difficulty: beginner
related: ["[[bitcoin]]", "[[ethereum]]", "[[proof-of-work]]", "[[proof-of-stake]]", "[[smart-contracts]]", "[[on-chain-analysis]]", "[[defi]]", "[[decentralized-exchanges]]"]
---

# Blockchain

A **blockchain** is a distributed, append-only ledger that records transactions in cryptographically linked blocks, providing immutability and transparency without requiring a central authority. It is the foundational technology underlying [[bitcoin]], [[ethereum]], and the entire [[crypto-markets|cryptocurrency]] ecosystem.

---

## How It Works

1. **Transactions** are broadcast to a peer-to-peer network of nodes
2. **Nodes** validate transactions against protocol rules (e.g., sufficient balance, valid signatures)
3. **Blocks** bundle validated transactions together at regular intervals (e.g., ~10 min for [[bitcoin]], ~12 sec for [[ethereum]])
4. **Consensus mechanisms** -- either [[proof-of-work]] or [[proof-of-stake]] -- determine which node gets to propose the next block
5. **Chaining** links each new block to the previous one via a cryptographic hash, making retroactive tampering computationally infeasible

The result is a tamper-resistant, publicly auditable history of every transaction ever processed on the network.

---

## Key Properties

| Property | Description |
|---|---|
| **Immutability** | Once confirmed, transactions cannot be reversed or altered |
| **Decentralization** | No single entity controls the ledger; consensus is distributed |
| **Transparency** | All transactions are publicly visible (on public chains) |
| **Permissionless** | Anyone can participate as a user or validator |

---

## Trading Relevance

- Blockchain data is the basis of [[on-chain-analysis]], enabling traders to track [[whale-trade|whale movements]], exchange flows, and supply dynamics in real time
- Block confirmation times affect trade settlement speed -- critical for [[arbitrage]] across [[decentralized-exchanges|DEXs]] and centralized exchanges
- Network congestion (high gas fees) can signal periods of extreme market activity or [[defi]] demand
- Understanding blockchain architecture helps traders evaluate L1 vs L2 tradeoffs when choosing trading venues like [[hyperliquid]], [[arbitrum]], or [[solana]]

---

## Sources

- Satoshi Nakamoto, *Bitcoin: A Peer-to-Peer Electronic Cash System* (2008) — the original whitepaper defining the chained-block, proof-of-work ledger
- Vitalik Buterin, *Ethereum Whitepaper* (2013) — generalising the blockchain to a programmable, smart-contract platform
- Antonopoulos & Wood, *Mastering Ethereum* / Antonopoulos, *Mastering Bitcoin* (O'Reilly) — technical references on blockchain architecture and consensus

## See Also

- [[proof-of-work]] -- Bitcoin's original consensus mechanism
- [[proof-of-stake]] -- Ethereum's consensus mechanism since The Merge
- [[smart-contracts]] -- Programmable logic executed on blockchains
- [[on-chain-analysis]] -- Using blockchain data for trading signals
- [[defi]] -- Decentralized finance built on blockchain infrastructure

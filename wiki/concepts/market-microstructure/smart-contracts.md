---
title: "Smart Contracts"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [crypto, defi, ethereum]
aliases: ["smart-contract", "Smart Contract"]
related: ["[[blockchain]]", "[[ethereum]]", "[[defi]]", "[[decentralized-exchanges]]", "[[uniswap]]", "[[aave]]"]
domain: [market-microstructure]
prerequisites: ["[[blockchain]]", "[[ethereum]]"]
difficulty: intermediate
---

# Smart Contracts

A **smart contract** is self-executing code deployed on a [[blockchain]] that automatically enforces the terms of an agreement when predefined conditions are met. Pioneered by [[ethereum]] in 2015, smart contracts are the foundational building block of [[defi|decentralized finance]], enabling trustless lending, trading, and asset management without intermediaries.

---

## How They Work

Smart contracts are written in languages like **Solidity** (Ethereum) or **Rust** (Solana) and deployed to a blockchain's virtual machine (e.g., the EVM). Once deployed, the code is immutable and publicly verifiable. Anyone can interact with the contract by sending a transaction that triggers its functions.

Key characteristics:
- **Deterministic** -- given the same inputs, they always produce the same outputs
- **Trustless** -- execution is guaranteed by the network, not by any counterparty
- **Composable** -- contracts can call other contracts, enabling complex DeFi "money legos"
- **Transparent** -- source code is typically verified and readable on block explorers

---

## Applications in Trading

| Use Case | Examples |
|---|---|
| **Decentralized Exchanges** | [[uniswap]] AMM pools, [[dydx]] order books |
| **Lending/Borrowing** | [[aave]] flash loans, Compound supply/borrow |
| **Derivatives** | [[gmx]] perpetuals, Synthetix synthetic assets |
| **Stablecoins** | MakerDAO's DAI minting via collateralized vaults |
| **Bridges** | Cross-chain asset transfers between L1s and L2s |

---

## Trading Relevance

- Smart contract risk (bugs, exploits, rug pulls) is a major consideration when trading or providing liquidity in [[defi]]
- [[on-chain-analysis|On-chain analysis]] of contract interactions reveals institutional activity and protocol health
- Gas costs for contract execution directly impact trading profitability on [[ethereum]] mainnet vs cheaper L2s like [[arbitrum]]

---

## See Also

- [[ethereum]] -- The primary smart contract platform
- [[defi]] -- The ecosystem built on smart contracts
- [[blockchain]] -- The underlying infrastructure
- [[decentralized-exchanges]] -- DEXs powered by smart contracts

## Sources

- Szabo, N. (1997). "Formalizing and Securing Relationships on Public Networks." *First Monday* — the original conceptualization of smart contracts, predating blockchain.
- Buterin, V. (2014). *Ethereum Whitepaper* — defines the EVM and the Turing-complete smart-contract platform.
- Ethereum Foundation. *Solidity Documentation* (docs.soliditylang.org) — the canonical smart-contract language reference.
- Atzei, N., Bartoletti, M. & Cimoli, T. (2017). "A Survey of Attacks on Ethereum Smart Contracts." *POST 2017* — catalog of smart-contract vulnerability classes relevant to DeFi risk.

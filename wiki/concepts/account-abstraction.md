---
title: "Account Abstraction"
type: concept
created: 2026-07-19
updated: 2026-10-17
status: draft
tags: [crypto]
aliases: ["ERC-4337", "Smart Accounts", "Smart Contract Wallets", "EIP-7702"]
domain: [crypto, smart-contracts]
prerequisites: ["[[ethereum]]", "[[smart-contracts]]"]
difficulty: intermediate
related: ["[[ethereum]]", "[[layer-2]]", "[[safe]]", "[[self-custody]]", "[[ai-agents]]", "[[2025-02-bybit]]"]
---

# Account Abstraction

**Account abstraction** replaces Ethereum's fixed "one private key controls one account" model with **smart accounts**: wallets whose rules for signing, paying gas and recovering access are set by code. The main standard, **ERC-4337**, went live on Ethereum mainnet in March 2023 without a protocol change; **EIP-7702**, shipped in the Pectra upgrade in May 2025, lets ordinary key-based accounts take on smart-account behaviour. For traders, it matters as wallet infrastructure (session keys, gas sponsorship, batched transactions), as a security surface, and as a recurring infrastructure narrative.

## Overview

Ethereum has two account types. **Externally owned accounts (EOAs)** are controlled by a single private key; lose the key and the funds are gone, and every action needs ETH for gas. **Contract accounts** run code but historically could not start transactions themselves. Account abstraction lets a user's account be a contract that *can* start transactions, so the account defines its own validity rules.

That enables features EOAs cannot offer:

- **Gas sponsorship and gas in other tokens** — a third party (a "paymaster") pays gas, or the user pays in a stablecoin.
- **Batched transactions** — approve and swap, or close several positions, in one atomic operation.
- **Session keys** — a limited key that can, for example, trade a set of pairs for 24 hours but cannot withdraw.
- **Social recovery and multisig** — recovery through guardians, or several signers needed to move funds (the [[safe|Safe]] model).
- **Spending limits and allow-lists** — rules useful for teams, treasuries and automated agents.

## How It Works

### ERC-4337

ERC-4337 adds account abstraction at the application layer rather than through a consensus change:

1. The wallet signs a **UserOperation** (a transaction-like object) and sends it to a separate mempool.
2. **Bundlers** collect UserOperations and submit them on-chain in one transaction.
3. A singleton **EntryPoint** contract verifies each operation against the account's own validation logic, then executes it.
4. An optional **paymaster** contract agrees to cover the gas, under whatever conditions it sets.

Because it needs no hard fork, ERC-4337 runs on Ethereum and most EVM [[layer-2]] networks. Some chains, such as zkSync Era and Starknet, build account abstraction into the protocol so that every account is a smart account.

### EIP-7702

EIP-7702 (activated with Pectra on 7 May 2025) lets an existing EOA sign an authorization that points its code at a smart-contract implementation. The user keeps the same address and balances but gains batching, sponsorship and delegated permissions. The catch is that a signed authorization to a malicious contract hands control of the whole account to that contract, which created a new phishing pattern.

## Security Considerations

- **Code risk replaces key risk.** A smart account is only as safe as its contract and its signing interface (see [[smart-contract-risk]]).
- **Signing-interface attacks.** The [[2025-02-bybit|February 2025 Bybit hack]] (about $1.46 billion) compromised the Safe multisig front end so that signers approved a transaction different from the one shown. Multisig smart accounts do not protect against what-you-see-is-not-what-you-sign failures.
- **Delegation phishing.** Under EIP-7702, signing an unknown delegation is as dangerous as giving away a seed phrase.

## Trading Relevance

- **Execution and bots.** Session keys and delegated "agent" keys let a bot or trading front end sign orders without holding the withdrawal key. [[hyperliquid|Hyperliquid]]'s API wallets follow the same principle: they can trade but not withdraw. This is the safer pattern for any automated strategy (see [[exchange-api-key-security]]).
- **On-chain strategies.** Batched, atomic operations reduce the number of separate transactions in DeFi loops such as [[delta-neutral-yield-farming]] and [[airdrop-farming]], cutting gas and reducing the window in which a half-finished position is exposed.
- **AI agents.** Smart accounts with spending limits and allow-lists are the natural wallet for autonomous [[ai-agents]] that need to transact without full custody.
- **Narrative trades.** Wallet and smart-account tokens such as [[safe|SAFE]], [[trust-wallet-token|TWT]] and [[instadapp|FLUID]] trade on the account-abstraction and [[self-custody]] narrative rather than on cash flows; they fit the [[narrative-trading]] playbook and tend to move on upgrade milestones (ERC-4337 launch, Pectra) and wallet-security news.

## Related

- [[ethereum]] — the chain where account abstraction was standardised
- [[layer-2]] — where most ERC-4337 activity happens
- [[safe]] — the dominant multisig smart-account stack
- [[self-custody]] — the custody model smart accounts extend
- [[2025-02-bybit]] — signing-interface risk in practice
- [[saakuru-labs]] — a gasless consumer chain competing with paymaster-based gas sponsorship
- [[ai-agents]], [[exchange-api-key-security]], [[narrative-trading]]

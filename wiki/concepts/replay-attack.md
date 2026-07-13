---
title: "Replay Attack"
type: concept
created: 2026-04-27
updated: 2026-06-11
status: good
tags: [crypto, fork, security, market-microstructure]
aliases: ["Cross-Chain Replay", "Transaction Replay"]
related: ["[[hard-fork]]", "[[fork-airdrop-triangulation]]", "[[2017-08-bitcoin-cash-fork-arbitrage]]", "[[2016-07-ethereum-dao-fork-arbitrage]]"]
domain: [market-microstructure, security]
prerequisites: ["[[hard-fork]]"]
difficulty: intermediate
---

# Replay Attack

In the post-[[hard-fork|hard-fork]] context, a **replay attack** is the act of taking a transaction broadcast on one chain and rebroadcasting it on the sibling chain. Because both chains share the pre-fork history (and therefore the same keys, addresses, and UTXO/nonce structures), an unprotected transaction signed for chain A can also be valid on chain B. The unintended consequence: a holder who only meant to spend on one chain ends up moving coins on both.

## Why It Exists

A hard fork creates two chains with identical state at the snapshot block. Without a chain identifier in the signed transaction, there is no way for chain B to tell that a transaction was meant for chain A:

- **Bitcoin (UTXO model):** A transaction consumes specific outputs by reference. Both chains have those outputs. The signature is over the transaction body, which is identical.
- **Ethereum (account model):** A transaction includes a nonce. Both chains' accounts have the same nonce post-snapshot. The signature is over the unsigned transaction including nonce.

## Replay Protection Mechanisms

| Chain | Mechanism | Activated |
|-------|-----------|-----------|
| Bitcoin Cash | `SIGHASH_FORK_ID` (0x40 flag) — adds a fork-specific value to the signature digest | At UAHF, 2017-08-01 |
| Ethereum (post-DAO fork) | EIP-155 — chain ID bound into the signature | EIP-155 added October 2016 (2 months after fork) |
| Ethereum Classic | Adopted EIP-155 with a different chain ID | Late 2016 |
| Bitcoin SV | Inherited BCH's `SIGHASH_FORK_ID`, then changed flag at split | 2018-11-15 |
| ETHW (Ethereum PoW) | Distinct chain ID (10001) | At Merge, 2022-09-15 |

## The 2016 ETH/ETC Replay Window

The original DAO fork is the classic case study. Between **July 20, 2016** (the fork) and the activation of EIP-155 a few months later, ETH and ETC transactions were freely replayable. Several exchanges and users lost funds when:

1. They sent ETH to a deposit address that had also been credited ETC.
2. The exchange (or attacker) replayed the transaction on ETC.
3. The user's ETC balance was drained without their authorization.

Coinbase and Poloniex both reported customer losses during this window. The lesson institutionalized chain-ID-bound signing in nearly every subsequent fork.

## Replay-Attack Trading Implications

Replay risk is a *structural* signal that fork-arb desks watch:

1. **Splitting coins safely.** Before replay protection is in place, traders use "splitter contracts" or "taint splitting" — sending the parent coin into a transaction that is valid only on one chain (e.g., spending from a UTXO that exists only on the new chain), so subsequent transactions cannot be replayed.
2. **Front-running exchange withdrawals.** When users withdraw the parent asset from exchanges that have not deployed replay protection, sophisticated parties can replay the transaction on the sibling chain to redirect the forked coin to themselves.
3. **Pre-emptive splitting fees.** During the BCH fork, services like Coin.dance offered splitting-as-a-service for 0.5-1% — an explicit price on replay risk.
4. **Exchange operational risk.** Exchanges that delay deposits during the replay window (e.g., Coinbase post-BCH) protect customers but cost themselves volume; exchanges that don't may lose customer funds.

## Why It Matters for [[fork-airdrop-triangulation]]

The replay window adds a **friction tax** on the fork-arb playbook:

- A trader holding BTC pre-fork wants to hold both BTC and BCH post-fork.
- Without replay protection, naively spending BCH may also spend the corresponding BTC.
- The trader must either wait for replay protection (delay = BCH price decay) or use a splitter (cost = 0.5-1% + technical risk).

This is why **the most profitable fork arbs went to desks with custom splitter infrastructure** (Cumberland, Jump, Alameda) rather than to retail. The operational moat persisted until exchanges and chains standardized replay protection.

## Modern Status

Post-2018, every major contentious hard fork has launched with replay protection enabled by default — the playbook is well-understood and chain developers consider it a basic engineering requirement. The replay-attack edge has therefore decayed into a historical artifact, but the operational sophistication it required built the desks that still dominate event-driven crypto trading today.

## Related

[[hard-fork]] · [[fork-airdrop-triangulation]] · [[2017-08-bitcoin-cash-fork-arbitrage]] · [[2016-07-ethereum-dao-fork-arbitrage]] · [[ethereum-classic]] · [[bitcoin-cash]]

## Sources

- Vitalik Buterin et al., **EIP-155** specification, October 2016.
- Bitcoin Cash UAHF specification (Bitcoin ABC, 2017) — `SIGHASH_FORK_ID`.
- Coinbase blog: "Customer ETC distribution" (August 2016).
- Andreas Antonopoulos, *Mastering Bitcoin* (2nd ed., 2017), Ch. 10.

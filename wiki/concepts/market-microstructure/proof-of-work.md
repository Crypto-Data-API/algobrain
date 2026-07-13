---
title: "Proof of Work"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [crypto, bitcoin]
aliases: ["PoW", "proof-of-work-consensus", "mining consensus"]
related: ["[[blockchain]]", "[[bitcoin]]", "[[proof-of-stake]]", "[[halving]]"]
domain: [market-microstructure]
prerequisites: ["[[blockchain]]", "[[bitcoin]]"]
difficulty: intermediate
---

# Proof of Work

**Proof of Work (PoW)** is a consensus mechanism in which network participants (miners) compete to solve computationally intensive cryptographic puzzles to validate transactions and produce new blocks on a [[blockchain]]. It is the original consensus model introduced by [[bitcoin]] in 2009 and remains the security backbone of the BTC network.

---

## How It Works

1. **Miners** collect pending transactions and assemble them into a candidate block
2. They repeatedly hash the block header with different nonce values, searching for a hash below the network's **difficulty target**
3. The first miner to find a valid hash broadcasts the block to the network
4. Other nodes verify the solution (trivially fast) and accept the block
5. The winning miner receives the **block reward** (currently 3.125 BTC after the 2024 [[halving]]) plus transaction fees

The difficulty adjusts dynamically to maintain consistent block times (~10 minutes for Bitcoin) regardless of total network hashrate.

---

## Key Characteristics

| Aspect | Detail |
|---|---|
| **Security** | Attacking the network requires >50% of total hashrate (prohibitively expensive for Bitcoin) |
| **Energy** | Significant electricity consumption -- a frequent criticism |
| **Hardware** | Bitcoin mining uses specialized ASIC chips; general-purpose GPUs are no longer competitive |
| **Decentralization** | Mining has consolidated into large pools (Foundry, AntPool), raising centralization concerns |

---

## Trading Relevance

- **Hashrate trends** serve as a proxy for miner confidence and network security; declining hashrate can signal miner capitulation during bear markets
- **Miner revenue** and break-even costs influence BTC sell pressure -- miners must sell BTC to cover electricity costs
- The [[halving]] reduces PoW block rewards, creating supply shocks that have historically preceded bull cycles
- [[ethereum]] abandoned PoW for [[proof-of-stake]] in September 2022 ("The Merge"), fundamentally changing ETH's issuance economics

---

## See Also

- [[bitcoin]] -- The largest PoW blockchain
- [[proof-of-stake]] -- The alternative consensus mechanism used by Ethereum
- [[halving]] -- Bitcoin's block reward reduction schedule
- [[blockchain]] -- The distributed ledger secured by PoW

## Sources

- Nakamoto, S. (2008), "Bitcoin: A Peer-to-Peer Electronic Cash System" — the original PoW whitepaper
- Bitcoin Core developer documentation (bitcoin.org) — mining, difficulty adjustment, and block validation
- Back, A. (2002), "Hashcash — A Denial of Service Counter-Measure" — the proof-of-work primitive Bitcoin built on

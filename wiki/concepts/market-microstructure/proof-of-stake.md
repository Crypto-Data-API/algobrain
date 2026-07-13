---
title: "Proof of Stake"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [crypto, ethereum, defi]
aliases: ["PoS", "proof-of-stake-consensus", "staking consensus"]
related: ["[[blockchain]]", "[[ethereum]]", "[[proof-of-work]]", "[[solana]]", "[[defi]]"]
domain: [market-microstructure]
prerequisites: ["[[blockchain]]", "[[proof-of-work]]"]
difficulty: intermediate
---

# Proof of Stake

**Proof of Stake (PoS)** is a consensus mechanism in which validators are selected to propose and attest to new blocks based on the amount of cryptocurrency they have "staked" (locked) as collateral. It replaced [[proof-of-work]] as [[ethereum|Ethereum's]] consensus model in September 2022 and is used by most modern blockchains including [[solana]], [[polygon]], and [[arbitrum|Arbitrum's]] underlying L1.

---

## How It Works

1. **Validators** deposit tokens as stake (e.g., 32 ETH for Ethereum) to participate in block production
2. The protocol **randomly selects** a validator to propose each new block, weighted by stake size
3. Other validators **attest** to the block's validity
4. Valid blocks are finalized and the proposer earns rewards (block rewards + transaction fees)
5. **Slashing** penalizes validators who act maliciously (e.g., double-signing) by destroying a portion of their staked tokens

---

## PoS vs PoW

| Dimension | Proof of Stake | [[proof-of-work|Proof of Work]] |
|---|---|---|
| **Energy** | ~99.95% less than PoW | Extremely high electricity usage |
| **Hardware** | Standard servers | Specialized ASICs / GPUs |
| **Security Cost** | Economic (staked capital at risk) | Physical (electricity + hardware) |
| **Yield** | Stakers earn ~3-5% APR | Miners earn block rewards minus costs |
| **Entry Barrier** | Capital requirement (32 ETH) | Hardware + electricity costs |

---

## Trading Relevance

- **Staking yield** creates a benchmark "risk-free rate" for crypto, influencing [[defi]] lending rates across the ecosystem
- Liquid staking derivatives (Lido's stETH, Rocket Pool's rETH) are major DeFi primitives and tradeable assets in their own right
- Validator economics and staking ratios affect token supply dynamics -- higher staking rates reduce circulating supply
- Slashing events can trigger short-term price volatility and signal network instability
- The Merge transformed ETH from an inflationary to a potentially deflationary asset under EIP-1559

---

## See Also

- [[ethereum]] -- The largest PoS blockchain by market cap
- [[proof-of-work]] -- The predecessor consensus mechanism
- [[blockchain]] -- The distributed ledger infrastructure
- [[defi]] -- DeFi protocols built on PoS chains
- [[solana]] -- High-throughput PoS chain

## Sources

- Ethereum Foundation, "Proof-of-stake (PoS)" — official documentation (ethereum.org/developers/docs/consensus-mechanisms/pos)
- Buterin, V. et al., "Combining GHOST and Casper" (2020) — Ethereum's PoS finality design
- Saleh, F. (2021), "Blockchain Without Waste: Proof-of-Stake," *Review of Financial Studies* — economic analysis of PoS security

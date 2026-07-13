---
title: "Dencun Upgrade"
type: concept
created: 2026-04-22
updated: 2026-06-11
status: good
tags: [crypto, ethereum, defi]
aliases: ["EIP-4844", "proto-danksharding", "Deneb-Cancun"]
domain: [market-microstructure]
difficulty: intermediate
related: ["[[ethereum]]", "[[layer-2]]", "[[nft]]", "[[nft-trading]]", "[[erc-721]]", "[[arbitrum]]", "[[polygon]]", "[[gas-fees]]", "[[fees]]"]
---

The Dencun upgrade was a hard fork of [[ethereum|Ethereum]] activated on March 13, 2024, that combined changes on both the execution layer (Cancun) and the consensus layer (Deneb). Its centerpiece was EIP-4844, often called "proto-danksharding," which introduced a dedicated data-availability layer for [[layer-2|Layer 2]] rollups via a new transaction type called blob-carrying transactions. The practical effect was an order-of-magnitude reduction in L2 data-posting costs, which propagated through to dramatically lower user-facing fees on rollups such as Base, [[arbitrum|Arbitrum]], and Optimism, and eventually contributed to L1 average gas prices falling to levels not seen since May 2017 (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]]).

## Timeline

- **March 13, 2024** — Dencun activated on [[ethereum|Ethereum]] mainnet at epoch 269568, following successful deployments on Goerli, Sepolia, and Holesky testnets earlier in the year.
- **Early 2025** — Ethereum L1 average gas prices fell below 10 Gwei, described as the lowest levels since May 2017 (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]]).
- **Post-Dencun** — Base, Arbitrum, and Optimism converged as the dominant rollup trio, collectively handling roughly 90% of L2 transaction share, with Base capturing a plurality of DeFi total value locked among L2s (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]]).

## EIPs Included

Dencun bundled nine EIPs across the execution and consensus layers:

| EIP | Name | Purpose |
|---|---|---|
| EIP-4844 | Shard Blob Transactions (proto-danksharding) | Introduces a new transaction type carrying "blobs" of data for L2 data availability at a separate, cheaper fee market |
| EIP-1153 | Transient Storage Opcodes | Adds `TSTORE` / `TLOAD` opcodes for storage that only persists within a single transaction, enabling cheaper reentrancy guards and intermediate state |
| EIP-4788 | Beacon Block Root in the EVM | Exposes beacon chain block roots to smart contracts, enabling trust-minimized staking and restaking protocols |
| EIP-5656 | MCOPY Instruction | Adds a native memory-copy opcode, replacing expensive loop-based copies |
| EIP-6780 | SELFDESTRUCT Semantic Change | Restricts `SELFDESTRUCT` to only clear state when used in the same transaction as contract creation, a precursor to eventual removal |
| EIP-7044 | Perpetually Valid Signed Voluntary Exits | Allows validator exit messages to remain valid across forks, simplifying staking provider key handling |
| EIP-7045 | Increased Max Attestation Inclusion Slot | Extends the window during which attestations can be included, improving consensus participation |
| EIP-7514 | Add Max Epoch Churn Limit | Caps the per-epoch validator activation rate to slow staking growth |
| EIP-7516 | BLOBBASEFEE Opcode | Exposes the current blob base fee to the EVM, letting contracts read L2 data-posting cost conditions |

## How Blob Transactions Work

EIP-4844 introduces a third transaction type that carries one or more "blobs" — fixed-size binary objects (~128 KiB each) that exist in a separate data-availability layer rather than in regular execution calldata.

Key properties:

- **Separate fee market** — blobs have their own base fee (queryable via the `BLOBBASEFEE` opcode from EIP-7516) that is independent of the regular EIP-1559 gas market. This prevents L2 data posts from competing with L1 smart contract calls for the same fee auction.
- **Block capacity** — each block targets 3 blobs and caps at 6 blobs (the longer-term "danksharding" roadmap envisions ~4096 blobs per block, which is where the "proto-" in proto-danksharding comes from).
- **Execution layer cannot read blobs directly** — contracts can only access a KZG commitment (a hash-like cryptographic accumulator) of the blob, not the bytes themselves. This is sufficient for rollup fraud/validity proofs.
- **Pruning** — blobs are retained by consensus-layer nodes for roughly 18 days (4096 epochs) and then pruned. This is acceptable because rollups only need the data available long enough for anyone to reconstruct state and submit fraud proofs; once the challenge window closes, the blob can be discarded. Long-term archival is an out-of-protocol concern.

The net effect: rollups get a bulk-discount "data lane" that is one to two orders of magnitude cheaper than posting the same data as calldata.

## Impact on L2 Fees

The immediate post-Dencun period saw roughly 10x fee reductions on the major optimistic rollups (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]]). Order-of-magnitude illustrative figures from contemporary reporting:

| Network | Typical swap fee (pre-Dencun) | Typical swap fee (post-Dencun) |
|---|---|---|
| Base | ~$0.05-0.25 | ~$0.001-0.02 |
| Arbitrum | ~$0.20-1.00 | ~$0.02-0.10 |
| Optimism | ~$0.15-0.80 | ~$0.01-0.10 |

These are approximate ranges — actual fees fluctuate with L1 base fee, blob base fee, and the specific operation — but the step change in April 2024 was clearly visible across every major rollup's median user fee.

Second-order effects on L2 market structure:

- **TVL consolidation** — the combination of lower fees and strong ecosystem incentives pulled activity toward Base, Arbitrum, and Optimism, with smaller rollups struggling to maintain relevance.
- **L2 economics diverged** — Base, with heavy Coinbase-driven activity, remained solidly profitable on blob and execution-layer margins, while Arbitrum and Optimism reportedly operated closer to breakeven (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]]).

## Impact on NFT Trading

Dencun has direct consequences for [[nft|NFT]] market structure on L2s:

- **L2 mint viability** — pre-Dencun, minting a low-priced NFT on an L2 could still cost a meaningful fraction of the NFT's face value. Post-Dencun, L2 mint fees frequently fell below $0.05, making sub-$5 collections economically viable for the first time.
- **Floor-price trading friction** — for collections with floor prices in the single-digit dollars (a growing segment after the 2024-2025 NFT contraction), [[nft-trading|NFT trading]] round-trip costs on L2 became negligible, enabling flipping strategies that were previously unprofitable.
- **Cross-chain implications** — Base in particular became a meaningful destination for new [[erc-721|ERC-721]] launches, with creators choosing the L2 over L1 mainnet to pass the fee savings to buyers.
- **Gas-sensitive strategies** — automated [[nft-arbitrage|NFT arbitrage]], sweep bots, and trait-sniping strategies that were marginal on L1 became viable on post-Dencun L2s because the fixed cost per attempted transaction collapsed.

The flip side: lower fees also lower the cost of wash trading and spam, which means L2 NFT volume data from post-Dencun markets requires more careful filtering than equivalent L1 data.

## Trading-Relevant Metrics

Rough before/after reference points (approximate, drawn from contemporary observations in the cited gap-finder source):

- **Ethereum L1 average gas** — from frequent spikes to 30-100+ Gwei during 2021-2023 periods of high activity, down to sub-10 Gwei averages by early 2025 (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]]).
- **L2 median swap cost** — approximately 10x reduction across Base, Arbitrum, and Optimism immediately following March 13, 2024.
- **Blob base fee** — a new market data feed worth monitoring; sustained blob-fee spikes (when many rollups post simultaneously) propagate to higher L2 user fees even when L1 gas is quiet.
- **L2 TVL share** — the Base/Arbitrum/Optimism trio moved to ~90% of L2 transaction share post-Dencun, with Base carrying the plurality of L2 DeFi TVL (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]]).

Implication for traders: post-Dencun, the dominant variable in L2 execution cost is no longer L1 calldata gas but the blob base fee. Strategies that model L2 costs should read `BLOBBASEFEE` (on-chain) or equivalent blob fee oracles (off-chain) rather than extrapolating from L1 gas.

## Related

- [[ethereum]] — the L1 where Dencun was deployed
- [[layer-2]] — primary beneficiary of EIP-4844's blob data availability
- [[nft]] — lower L2 fees materially changed NFT market structure
- [[nft-trading]] — post-Dencun L2 fee floor enables previously unprofitable trading strategies
- [[erc-721]] — the standard most affected by L2 minting economics
- [[arbitrum]], [[polygon]] — specific L2 networks impacted
- [[gas-fees]], [[fees]] — broader fee-market context

## Sources

- Gap-finder research on NFT trading infrastructure and L2 economics (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]])
- Ethereum Improvement Proposals (EIP-4844, EIP-1153, EIP-4788, EIP-5656, EIP-6780, EIP-7044, EIP-7045, EIP-7514, EIP-7516) — public specifications at eips.ethereum.org

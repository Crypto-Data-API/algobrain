---
title: "Zero-Knowledge Proofs"
type: concept
created: 2026-07-17
updated: 2026-10-17
status: review
tags: [crypto, privacy, layer-2, algorithmic, machine-learning]
aliases: ["ZKP", "ZK Proofs", "zk-SNARKs", "zk-STARKs", "Zero Knowledge"]
domain: [crypto, market-microstructure]
difficulty: advanced
prerequisites: ["[[blockchain]]", "[[layer-1]]"]
---

# Zero-Knowledge Proofs

A **zero-knowledge proof (ZKP)** is a cryptographic protocol in which a *prover* convinces a *verifier* that a statement is true without revealing any information beyond the fact that the statement is true. The canonical example: you can prove you know a password without revealing the password itself. In blockchain contexts, ZKPs are the technical foundation of ZK-rollups (a dominant Layer 2 scaling solution), privacy protocols, and an emerging category of on-chain ML inference ([[zkml-predictive-mev]]).

## How It Works

A ZKP must satisfy three properties:

1. **Completeness:** If the statement is true, an honest prover can always convince the verifier.
2. **Soundness:** If the statement is false, no cheating prover can convince an honest verifier (except with negligible probability).
3. **Zero-knowledge:** The verifier learns nothing from the proof beyond the truth of the statement.

**In practical blockchain terms:** A ZKP allows a prover to submit a cryptographic proof to an Ethereum smart contract (the verifier) that a batch of thousands of transactions were all executed correctly — without the smart contract needing to re-execute them individually. This is what makes ZK-rollups highly scalable.

### ZK-SNARK vs ZK-STARK

Two families dominate:

| Type | Full name | Proof size | Verification speed | Trusted setup required |
|------|-----------|------------|-------------------|----------------------|
| **zk-SNARK** | Succinct Non-Interactive ARgument of Knowledge | Very small (~200 bytes) | Very fast | Yes (security risk if setup compromised) |
| **zk-STARK** | Scalable Transparent ARgument of Knowledge | Larger (~50KB) | Somewhat slower | No (post-quantum resistant) |

zk-SNARKs are used in Zcash (Groth16), Polygon zkEVM, and early ZK-rollups. zk-STARKs are used in StarkWare's StarkEx and StarkNet, and by StarkWare because they avoid the trusted setup assumption.

### ZK-rollups

ZK-rollups (zkSync, StarkNet, Polygon zkEVM, Scroll) execute transactions off-chain and submit two things to Ethereum L1: (1) the compressed state difference (calldata), and (2) a validity proof (the ZKP) that proves all transactions were executed correctly. The L1 verifies the proof — which is fast and cheap — and accepts the state update. This allows thousands of transactions to settle on Ethereum L1 with the security of L1 but a fraction of the gas cost.

Key distinction vs. Optimistic rollups (Arbitrum, Optimism): ZK-rollups provide **cryptographic finality** immediately (the proof is valid); Optimistic rollups assume validity and rely on a fraud-proof window (typically 7 days) for dispute. ZK-rollups have faster finality but are harder to build. *(Precision 2026-10-17: "immediately" means once the validity proof has been generated **and verified on L1**. Rollups batch proofs, so hard L1 finality typically lags by minutes to hours. Withdrawals still wait for the proof and the L1 finality window, but they skip the ~7-day optimistic challenge period. For cross-L2 arbitrage the relevant latency is often the sequencer's soft confirmation (sub-second), which is a trust assumption on a usually centralised sequencer.)*

## Concrete Examples

- **Zcash (2016, shielded transactions):** The first major blockchain deployment of zk-SNARKs. Zcash's "Sapling" upgrade (2018) made shielded proofs fast enough for practical use (~3 seconds on a laptop). See [[privacy-coins]] for trading context.
- **StarkEx (2020–):** StarkWare's ZK-rollup for trading. Powers dYdX v3 (perpetuals), ImmutableX (NFTs), and Sorare (fantasy sports). At peak, StarkEx processed more transactions than Ethereum mainnet combined. *(Update: dYdX moved to its own Cosmos-based chain (dYdX v4) in late 2023 and wound down v3 afterwards, so "powers dYdX v3" is historical. See [[dydx]].)*
- **zkSync Era (launched Mar 2023):** First EVM-compatible ZK-rollup at mainnet scale. Allows Ethereum smart contracts to deploy with minimal changes onto a ZK-rollup environment.
- **Polygon zkEVM (launched Mar 2023):** Polygon's ZK-rollup. Type 2 EVM-equivalence — designed to be near-identical to Ethereum execution.
- **ZKML (2024–):** Combining zero-knowledge proofs with machine learning inference. A model's prediction can be proven correct on-chain without revealing the model weights. This enables [[zkml-predictive-mev]] — submitting ML-derived MEV strategies whose logic is verified by the blockchain but remains proprietary.

## Trading Relevance

ZKPs affect the trading landscape in several ways:

- **[[cross-l2-arbitrage]] on ZK-rollups:** ZK-rollups with fast finality create faster settlement for cross-L2 arbs. Arbitrage between ZK-rollup liquidity and Ethereum L1 (or between two ZK-rollups) is a growing opportunity as ZK-rollup TVL increases.
- **[[privacy-coins]] and ZK-based privacy:** ZK-based privacy protocols (Tornado Cash successors, Aztec Network's AZTEC) use ZKPs to provide Ethereum-native shielded transactions. If these protocols achieve adoption, they reduce privacy coins' unique value proposition — a structural headwind for XMR and ZEC.
- **[[zkml-predictive-mev]]:** The intersection of ZKPs and ML. A searcher can prove on-chain that their MEV bundle was generated by a specific model, enabling decentralised MEV strategies where the model logic is kept private but the proof is public.
- **ZK-rollup token airdrops and incentives:** ZK-rollup protocols (zkSync, StarkNet, Scroll) have conducted or are expected to conduct large governance token airdrops to early users. This creates [[airdrop-farming]] opportunities where the activity on ZK-rollups earns future token distributions. *(Update 2026-10-17: all three distributions have happened: Starknet's STRK in February 2024, zkSync's ZK in June 2024 and Scroll's SCR in October 2024. The trading question is now the vesting overhang on insider and investor allocations, not the airdrop itself. See [[unlock-aware-momentum]], [[token-unlocks]] and [[l2-rollups-basket]].)*
- **[[mev-strategies]] on ZK-rollups:** ZK-rollup MEV is structurally different from Ethereum L1 MEV — sequencers (centralised or decentralised) control ordering, and the PBS/Flashbots model does not directly apply. Each ZK-rollup has its own MEV architecture; understanding the sequencer model is prerequisite to operating MEV strategies on them. See [[mev]].

### Protocol-risk note for traders

ZK systems move trust from re-execution to the correctness of circuits and verifiers, so a soundness bug can create assets out of nothing. The **2026-06-05 Zcash Orchard counterfeiting disclosure** cut ZEC ~38% in a day ([[2026-06-05-zcash-orchard-counterfeiting-bug]]). Treat newly audited or upgraded proof systems as event risk in position sizing. Rollups' upgradeable verifier contracts and security councils are a related, governance-side trust assumption. [[mythos-release-window-exploit-short]] trades this vulnerability-discovery risk directly.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI does not serve proof or rollup-level metrics (proving cost, batch latency, TVL per rollup). It does serve the *token* side of the ZK sector:

- `GET /api/v1/coins/category-groups` — curated **Layer-2 & scaling** and **privacy** groups (ZK, STRK, SCR-type tokens; ZEC) with price, market cap, rank and 24h/7d change
- `GET /api/v1/supply/unlocks?symbol=STRK` — forward vesting cliffs sized against float, the main supply catalyst after the 2024 airdrops
- `GET /api/v1/security/events?symbol=ZEC` — recent security events (protocol-bug risk)
- `GET /api/v1/backtesting/klines?symbol=STRKUSDT&interval=1d&start=2024-02-20` — token OHLCV for post-airdrop and unlock event studies

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/supply/unlocks?symbol=STRK"
```

Auth: `X-API-Key` header. Full endpoint catalogs: [[cryptodataapi-supply]], [[cryptodataapi-coins]].

## Related

- [[zk-rollup]] — the scaling application of ZKPs
- [[privacy-coins]] — Zcash uses ZKPs for shielded transactions
- [[zkml-predictive-mev]] — ML inference proven on-chain via ZKPs
- [[layer-2]] — ZK-rollups are the dominant ZKP-based L2 design
- [[layer-1]] — ZK-rollups settle proofs on L1
- [[cross-l2-arbitrage]] — arbitrage enabled by L2 ecosystems
- [[mev-strategies]] — MEV architecture differs on ZK-rollups vs L1
- [[airdrop-farming]] — early ZK-rollup usage earns protocol airdrops

## Sources

- General cryptography/ZKP knowledge; no specific wiki source ingested yet.

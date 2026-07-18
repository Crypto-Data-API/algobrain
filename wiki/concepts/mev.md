---
title: "MEV"
type: concept
created: 2026-07-17
updated: 2026-07-19
status: draft
tags: [crypto, defi, arbitrage, market-microstructure, execution, algorithmic]
aliases: ["Maximal Extractable Value", "Miner Extractable Value", "Block Value Extraction"]
domain: [market-microstructure, crypto]
difficulty: advanced
prerequisites: ["[[blockchain]]", "[[ethereum]]", "[[perpetual-futures]]"]
---

# MEV

**Maximal Extractable Value (MEV)** is the total value that can be extracted from a block by choosing which transactions to include, exclude, or reorder — beyond the standard block reward and transaction fees. The term was originally "Miner Extractable Value" (pre-Ethereum Merge), renamed to "Maximal" after proof-of-stake replaced miners with validators. MEV accrues to block producers (validators/miners) and to **searchers** — bots that detect profitable opportunities in the mempool and pay high priority fees to have their transactions included in favourable positions within a block.

## How It Works

MEV exists because:

1. **Transactions are public before inclusion.** On most blockchains, pending transactions broadcast to the public mempool, revealing user intent before the trade executes.
2. **Block ordering is discretionary.** The block producer chooses the order of transactions within their block. This ordering right has economic value.
3. **DeFi is deterministic.** AMM (automated market maker) price impact is mathematically computable from the pool state. A searcher can calculate the exact profit of a front-run, back-run, or sandwich *before* submitting.

**The MEV supply chain:**

```
Opportunity detected → Searcher constructs bundle → Builder assembles block → Validator proposes block
```

- **Searcher:** Detects the opportunity (pending swap, liquidatable loan, new pool) and constructs a transaction bundle designed to capture value.
- **Builder:** Aggregates searcher bundles and regular transactions into the most profitable block. Builders are specialised in post-PBS (Proposer-Builder Separation) Ethereum.
- **Validator:** Proposes the block built by the winning builder. The validator earns the MEV tip (priority fee) from the searcher's bundle.
- **Relay (e.g. Flashbots):** Mediates trust between builder and validator — allows validators to accept blocks without seeing the contents (preventing front-running by validators).

## MEV Types

| Type | Mechanism | Who bears the cost |
|------|-----------|-------------------|
| **Arbitrage (back-run)** | Buy after a large swap moves a pool's price; sell into the new equilibrium | No one harmed; price re-equilibrates |
| **Sandwich attack** | Front-run a user's swap to buy first, then back-run to sell after their fill worsens the price | The victim user — pays worse execution |
| **Liquidation capture** | Trigger a DeFi loan liquidation and capture the protocol's liquidation bonus | Borrower loses collateral at discount |
| **JIT liquidity** | Provide concentrated liquidity in an AMM just before a large swap, capture most of the fee, withdraw immediately | Passive LPs — captured a fee they didn't get |
| **NFT sniping** | Front-run a reveal or floor-price listing event | The would-be buyer who missed the transaction |

## Concrete Examples

- **Flashbots, launched Jan 2021:** Flashbots introduced "dark pool" bundle submission, allowing searchers to submit bundles to miners/builders without broadcasting to the public mempool. This eliminated most "gas wars" (where searchers bid ever-higher fees in a race to be included) and made MEV more efficient — but also more concentrated. By mid-2021, Flashbots was processing over 80% of Ethereum's MEV.
- **The "sandwich tax":** Uniswap's own analytics have shown that popular tokens on V2/V3 can have effective sandwich-attack rates of 5-15% of volume during high-volatility periods. On-chain analysis by EigenPhi estimated total sandwich revenue to searchers at hundreds of millions of dollars annually across 2022-2023.
- **March 2020 MakerDAO liquidations:** During Black Thursday, Ethereum gas prices spiked so high that normal liquidation bots failed to submit. A single sophisticated searcher submitted zero-bid liquidation transactions (bidding $0 for collateral) during the chaos and received $8.3M in ETH collateral near-free — the most extreme MEV event in DeFi history.
- **Jito on Solana (2022–):** Solana has no PBS system natively; Jito Labs built an off-protocol MEV infrastructure (Jito Block Engine) that handles ~50%+ of Solana validator stake. Jito tips (the Solana equivalent of Flashbots priority fees) generate tens of millions in revenue monthly.

## Trading Relevance

MEV is central to multiple AlgoBrain strategies:

- **[[mev-execution-guide]]:** The full operational guide for participating as a searcher — Flashbots bundle construction, gas bidding, mempool monitoring, and the profitability decision framework. The guide's cost analysis (builder bids typically consume 90%+ of gross profit) quantifies why MEV is viable only for fast, capital-efficient operators.
- **[[mev-strategies]]:** The strategy catalog — arbitrage back-runs, liquidation capture, JIT liquidity, and sandwich attacks (the last of which is excluded from AlgoBrain's ethical scope as it directly harms users).
- **[[liquidation-cascade-arbitrage]]:** On-chain liquidations are one of the largest and most consistent MEV sources. The strategy submits liquidation transactions via bundles to capture the protocol's liquidation bonus.
- **[[flash-loan-arbitrage]]:** Flash loans eliminate the capital requirement for MEV arb — the searcher borrows, executes the arb, and repays in a single atomic transaction, with no net capital at risk.
- **[[jito-solana-mev-arbitrage]]:** Solana-specific MEV via Jito Block Engine. Solana's sub-second blocks and low fees make micro-arbs viable that would be uneconomic on Ethereum mainnet.
- **[[on-chain-flow-trading]]:** MEV activity data (from EigenPhi, Dune Analytics) is a real-time signal for on-chain activity levels, which correlates with network usage, gas prices, and token volatility.

## Related

- [[mev-strategies]] — the catalog of specific MEV strategies
- [[mev-execution-guide]] — operational guide for executing MEV
- [[flash-loan-arbitrage]] — capital-free MEV execution
- [[flashbots]] — the dominant MEV relay/builder infrastructure on Ethereum
- [[liquidation-cascade-arbitrage]] — liquidation MEV strategy
- [[jito-solana-mev-arbitrage]] — Solana MEV via Jito
- [[ethereum]] — the dominant MEV chain
- [[layer-1]] — MEV architecture differs by L1
- [[market-microstructure]] — MEV is a microstructure phenomenon
- [[arbitrage]] — most non-sandwich MEV is a form of arbitrage

## Sources

- General crypto/MEV knowledge; no specific wiki source ingested yet.

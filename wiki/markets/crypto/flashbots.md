---
title: "Flashbots"
type: entity
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [crypto, mev, defi, market-microstructure]
aliases: ["Flashbots"]
entity_type: protocol
website: "https://www.flashbots.net"
related: ["[[mev]]", "[[mev-strategies]]", "[[jito-solana-mev-arbitrage]]", "[[ethereum]]", "[[defi]]", "[[mempool]]", "[[arbitrage]]"]
---

Flashbots is a research and development organization focused on mitigating the negative externalities of Maximal Extractable Value ([[mev|MEV]]) on [[ethereum|Ethereum]] and other blockchains. Founded in 2020, Flashbots has built critical infrastructure that reshaped how transactions are ordered, submitted, and processed on Ethereum — most importantly **Proposer-Builder Separation (PBS)**, implemented at the application layer through MEV-Boost. Its stated mission is to "democratize MEV extraction" and reduce its harms: minimise the centralising pressure MEV exerts on validators, reduce harmful forms like sandwiching, and make value extraction transparent and competitive rather than hidden.

## What is MEV?

Maximal Extractable Value (formerly "Miner Extractable Value") refers to the profit that block producers (validators, miners) and specialized actors ("searchers") can extract by reordering, inserting, or censoring transactions within a block. See the dedicated [[mev|MEV]] page for the full taxonomy; common forms include:

- **[[arbitrage|Arbitrage]]**: Exploiting price discrepancies between [[defi|DeFi]] protocols (e.g., buying a token on [[uniswap|Uniswap]] and selling on [[sushiswap|SushiSwap]])
- **Liquidations**: Front-running liquidation transactions on lending protocols like [[aave|Aave]] and [[compound|Compound]]
- **Sandwich attacks**: Placing transactions before and after a victim's trade to profit from the price impact. A trader sees a large buy order in the [[mempool]], buys before it (front-run), lets the victim's trade push the price up, then sells (back-run)
- **JIT (Just-In-Time) liquidity**: Providing concentrated liquidity right before a large swap and withdrawing immediately after

## The MEV Supply Chain

Flashbots' architecture re-organised Ethereum's transaction-ordering market into a layered supply chain. Understanding the roles is the key to understanding all Flashbots products:

| Role | What it does | Incentive |
|------|--------------|-----------|
| **User / wallet** | Originates a transaction | Wants good execution, no sandwiching |
| **Searcher** | Scans for MEV (arb, liquidations, sandwiches), bundles ordered transactions | Profits from the extracted value |
| **Builder** | Assembles bundles + public txs into the most valuable full block | Wins the proposer auction, keeps a margin |
| **Relay** | Trusted intermediary that validates blocks and forwards the highest bid to the proposer; hides block contents until the proposer commits | Enables trustless builder↔proposer exchange |
| **Proposer (validator)** | Signs the most profitable header it is offered | Maximises reward without running a builder |

This separation is what **Proposer-Builder Separation (PBS)** means in practice: validators no longer need sophisticated MEV-extraction software to capture MEV rewards, which reduces the centralising advantage that large, well-resourced validators would otherwise enjoy.

## Flashbots Products

### MEV-Boost
The most significant Flashbots product, and the de-facto implementation of off-chain PBS for Ethereum proof-of-stake. MEV-Boost is middleware run alongside a validator's consensus client that outsources block building to a competitive market:

- **Block builders**: Specialized actors that construct optimal blocks by ordering transactions to maximize MEV
- **Block proposers** (validators): Choose the most profitable block header from builders via a competitive sealed-bid auction, without seeing the block body until they commit
- **Relays**: Intermediaries that connect builders and proposers, validate block validity, and ensure builders cannot steal MEV nor proposers unbundle blocks

As of 2024, over 90% of Ethereum blocks are built through MEV-Boost, demonstrating its dominance in the block production pipeline. A live debate is **enshrined PBS (ePBS)** — moving this auction into the Ethereum protocol itself to remove reliance on trusted relays.

### Flashbots Protect
A private transaction submission service (RPC endpoint) that prevents front-running and sandwich attacks. Users send transactions to Flashbots Protect instead of the public [[mempool]], ensuring their transactions are not visible to MEV searchers until included in a block. It can also return a share of any backrun MEV the transaction creates and offers transaction "fast mode" vs. "max privacy" trade-offs.

### Flashbots Auction (MEV-Share)
An **order-flow auction (OFA)** that lets users selectively reveal parts of their transaction (a "hint") so searchers can bid to backrun it, and **returns a share of the resulting MEV to the user** rather than letting it be fully extracted. MEV-Share is built on the **SUAVE / MEV-Share matchmaker** design and is a leading example of "MEV redistribution" rather than mere mitigation.

### SUAVE (Single Unified Auction for Value Expression)
A planned decentralized block-building network and "encrypted mempool" designed to act as a shared sequencing layer across many chains. SUAVE aims to create a permissionless, cross-domain marketplace for transaction-ordering preferences, decentralising the builder/relay roles that today are relatively concentrated.

## Flashbots on Other Chains

While Flashbots itself is Ethereum-focused, the PBS / private-orderflow model it pioneered has been ported across ecosystems:

- **L2 rollups** (Arbitrum, Optimism, Base) — mostly run a single centralized sequencer today, which captures or suppresses MEV directly; decentralized-sequencer and shared-sequencer designs borrow PBS ideas.
- **Solana** — uses [[jito-solana-mev-arbitrage|Jito]], a parallel MEV stack (Jito-Solana validator client + block-engine + tip auction) that performs an analogous role to MEV-Boost in Solana's high-throughput, no-public-mempool environment.
- **Cross-chain** — SUAVE is explicitly designed as a chain-agnostic sequencing layer.

## MEV by the Numbers

- **Cumulative MEV extracted on Ethereum**: Over $600M since January 2020
- **Daily MEV**: Varies from $1M to $10M+ depending on market volatility
- **Sandwich attack volume**: Billions of dollars in monthly volume during peak DeFi activity
- **MEV-Boost adoption**: >90% of Ethereum validators use MEV-Boost

## Trading Implications

- **Strategy design**: DeFi traders must account for MEV as a cost. Large swaps on DEXes are vulnerable to sandwich attacks unless using private submission channels like Flashbots Protect or MEV-Share.
- **[[mev-strategies|MEV strategies]]**: A category of crypto-native [[algorithmic-trading|algorithmic trading]] focused on extracting MEV via specialized bots — see also [[jito-solana-mev-arbitrage|Jito MEV on Solana]] for the Solana equivalent.
- **Searcher competition**: MEV extraction is intensely competitive, with searchers engaging in priority gas auctions (PGAs) and latency optimization; sealed-bid relay auctions replaced the public PGA spam that previously congested the [[mempool]].
- **Execution cost**: For a normal trader, the practical lesson is that *which RPC endpoint you submit through* is itself an execution-quality decision — public mempool exposes you to sandwiching, private RPCs reduce that at the cost of trust assumptions.
- **Infrastructure dependency**: Understanding Flashbots infrastructure is essential for anyone building DeFi applications or trading strategies on Ethereum.

## Risks and Criticisms

- **Relay / builder centralization**: A small number of relays and builders process the majority of blocks, reintroducing centralization and a censorship vector (e.g. OFAC-compliant relays filtering sanctioned addresses). ePBS and SUAVE are responses to this.
- **Trusted relay assumption**: MEV-Boost relays are trusted not to steal MEV or leak block contents; a malicious relay is a single point of failure until enshrined PBS exists.
- **MEV is mitigated, not eliminated**: Private channels protect individual users but the underlying extractable value still exists; backrunning and arbitrage continue, just more transparently.
- **Liveness / dependency risk**: Validators leaning on MEV-Boost have historically missed slots during relay outages, a systemic reliability concern.

## Related

- [[mev]] -- The core concept of extractable value Flashbots was built to address
- [[mev-strategies]] -- Trading strategies focused on MEV extraction
- [[jito-solana-mev-arbitrage]] -- Solana's parallel MEV stack and tip auction
- [[ethereum]] -- The blockchain where Flashbots primarily operates
- [[mempool]] -- The pending transaction pool that MEV searchers monitor
- [[defi]] -- The ecosystem most affected by MEV

## Sources

- Flashbots research papers and documentation provide the foundation for MEV analysis in crypto markets
- General market knowledge; no specific wiki source ingested yet.

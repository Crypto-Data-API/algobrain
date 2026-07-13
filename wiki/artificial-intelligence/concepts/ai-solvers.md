---
title: "AI Solvers (Intent-Based Routing)"
type: concept
created: 2026-04-11
updated: 2026-06-12
status: good
tags: [crypto, defi, machine-learning, algorithmic, ai-trading]
aliases: ["Intent-Based Routing", "DeFi Solvers", "Solver Networks", "Intent Solvers"]
domain: [market-microstructure]
difficulty: advanced
related: ["[[cow-protocol]]", "[[1inch]]", "[[intent-based-trading]]", "[[ai-mev]]", "[[mev-strategies]]", "[[defai]]", "[[ai-trading-agents]]", "[[decentralized-ai]]", "[[statistical-proof-of-execution]]", "[[model-context-protocol]]", "[[llm-defi-interfaces]]"]
---

# AI Solvers (Intent-Based Routing)

**AI solvers** are the off-chain participants in intent-based DeFi protocols — CoW Protocol, UniswapX, 1inch Fusion, Bungee, Across — who compete in auctions to execute user trade intents. The user signs a declarative intent ("swap 10 ETH for at least 32,000 USDC before 3pm"); a network of solvers races to find the most efficient execution path across CEXs, DEXs, liquidity pools, bridges, and private market makers; the winning solver executes and takes the spread. It is, by volume, **the largest production deployment of machine learning in DeFi today**, and an underappreciated bridge between [[defai|DeFAI]] and professional quantitative trading.

## Why Solvers Are an ML Problem

A solver's job is the classic combinatorial-optimization-under-uncertainty problem, and it has the three properties that make ML useful:

1. **Huge search space** — routing across dozens of liquidity venues with different fee tiers, depth, and latency
2. **Noisy reward signal** — the same route may be optimal now and suboptimal in 200ms depending on competing order flow
3. **Fast feedback loop** — the solver wins or loses the auction within seconds, producing a measurable outcome for every decision

Hand-written routing heuristics worked for early DEX aggregators. They stopped being competitive once the search space included cross-chain bridges, intent-matching between users (CoW's "coincidence of wants"), and MEV-internalization strategies. Production solvers today lean heavily on supervised learning (predicting fillable prices), reinforcement learning (learning when to take a fast vs slow path), and combinatorial search augmented with learned heuristics.

## The Leading Intent Protocols

| Protocol | Intent Type | Solver Population | Launch Chain |
|----------|-------------|--------------------|--------------|
| [[cow-protocol|CoW Protocol]] | Swap with CoW matching | Semi-permissioned solver list | Ethereum + L2s |
| UniswapX | Swap with limit + expiry | Permissioned auction (UniswapX V2+) | Ethereum + L2s |
| 1inch Fusion | Swap with Dutch auction | Permissioned resolver network | Ethereum + L2s |
| Bungee | Cross-chain swap | Bridge + swap solver network | Multi-chain |
| Across | Cross-chain intent | Relayer network with capital backing | Multi-chain |

See also [[intent-based-trading]] for the strategy angle on this from a trader's perspective.

## How ML Helps

Three specific sub-problems where ML dominates the hand-written baseline:

### 1. Route Discovery

Given a source token, a destination token, and a size, find a path through liquidity venues that minimizes slippage net of gas. A graph-search baseline enumerates possibilities; a learned heuristic prunes the search tree based on patterns from historical fills — which pools are currently deep, which bridges are congested, which private market makers quoted tightly on the last similar size.

### 2. Bid Selection in Dutch Auctions

UniswapX and 1inch Fusion use Dutch auctions: the price starts generous and decays over a time window, and any solver can fill at any point. Bidding too early gives away margin; bidding too late loses the order to a competitor. This is structurally identical to the bid-shading problem in [[ai-mev|AI MEV]] bidding, and the same RL techniques apply.

### 3. Counterparty Matching (CoW-Specific)

CoW Protocol adds a unique twist: if user A wants to swap X→Y and user B wants Y→X simultaneously, the solver can match them directly at a midpoint price, splitting the saved slippage. Finding profitable coincidences of wants across dozens of orders per batch is a combinatorial problem where learned heuristics dramatically outperform exhaustive search at typical batch sizes.

## Relationship to MEV

AI solvers and [[ai-mev|AI MEV]] are two sides of the same coin. MEV searchers extract value from transaction ordering in the public mempool; intent solvers *internalize* MEV by routing through private channels before the order ever hits the public mempool. For users, intent protocols are a protection mechanism against MEV. For professional execution firms, solving and MEV searching are often the same business run through different software stacks — the optimization skills, data infrastructure, and latency engineering are nearly identical.

## The Five-Layer DeFi Stack Framing

By 2025–2026, the intent-based architecture had become the dominant design pattern for L2 DeFi. A useful framing of the resulting stack has emerged in industry research (Source: [[2026-04-11-perplexity-ai-crypto-gaps]]):

| Layer | Function | Examples |
|-------|----------|----------|
| **1. Settlement** | Canonical asset state | Ethereum L1, Bitcoin |
| **2. Execution** | ZK/optimistic rollups | Arbitrum, Base, Optimism, zkSync |
| **3. Interoperability** | Cross-chain messaging | LayerZero, CCIP, Hyperlane, Wormhole |
| **4. Account / Intent** | Smart accounts, paymaster gas sponsorship, intent solvers | [[cow-protocol|CoW]], UniswapX, [[1inch|1inch Fusion]], Safe, Biconomy |
| **5. Automation** | On-chain AI execution agents | [[ai-trading-agents|AI agents]], [[llm-defi-interfaces|LLM wallets]], MCP-based automation |

The critical shift this framing captures is that **DeFi UX has moved up the stack**: users increasingly interact at Layer 5 (declare a goal in natural language to an AI agent) rather than at Layer 2 (sign a swap transaction on a specific rollup). Layer 4 — where intent solvers live — is the *plumbing* that makes this work: the translation from "what the user wants" to "what transactions will execute on which venues."

For AI solvers specifically, this framing matters because it positions them not as an optimization layer on top of DeFi but as the **essential connective tissue** between agent-level intent and on-chain execution. The 2026 integration point to watch is how solver networks begin incorporating verifiable AI output validation (see [[statistical-proof-of-execution]] and Warden Protocol's SPEx deployment) — which will be the first time an intent solver can cryptographically prove that its routing decisions followed a specific agreed-upon model rather than an opaque optimization.

## Who Runs Solvers Today

The solver population is surprisingly concentrated and surprisingly professional. Most of the top solvers on CoW Protocol and UniswapX are:

- Incumbent market makers (Wintermute, GSR, Flow Traders, Jump, SEBI-style prop shops)
- MEV searcher firms that expanded into intent solving (bloXroute, rsync, propellerheads)
- A smaller tail of open-source / community-run solvers

This concentration is itself interesting: permissionless intent protocols have ended up creating a de-facto professional solver class, mirroring the professionalization of MEV searchers after Flashbots. It is an honest counterweight to the "retail-driven DeFAI" narrative — the production ML in DeFi is mostly being done by the same firms who dominate quant trading everywhere else.

## Trading / Research Angle

For researchers, intent-solver data is one of the richest public ML datasets in DeFi. Every CoW batch, every UniswapX fill, every 1inch Fusion auction is on-chain, with full context (what was offered, who won, at what price). This is a fertile ground for retrospective ML research on execution quality, MEV-internalization efficiency, and solver performance.

For traders, the clearest angle is **solver performance as a proxy for execution alpha**. If a solver consistently wins auctions at tighter spreads than peers, that solver is capturing real execution alpha — and some intent protocols now publish per-solver performance scorecards that quantify this directly.

## See Also

- [[cow-protocol]] — Reference intent protocol with CoW-matching
- [[1inch]] — 1inch Fusion intent protocol
- [[intent-based-trading]] — Strategy-side perspective
- [[ai-mev]] — Adjacent ML-in-DeFi problem
- [[mev-strategies]] — Parent MEV taxonomy
- [[ai-trading-agents]] — Broader autonomous-agent context
- [[defai]] — Parent DeFAI narrative
- [[decentralized-ai]] — Broader AI×crypto context
- [[artificial-intelligence]] — AI section hub

## Sources

- (Source: [[2026-04-11-perplexity-ai-crypto-gaps]]) — Perplexity research on AI×crypto gaps, including the five-layer DeFi stack framing
- CoW Protocol documentation and solver competition rules (docs.cow.fi)
- Uniswap Labs, UniswapX whitepaper; 1inch Fusion documentation
- Flashbots research on MEV and intent-based execution

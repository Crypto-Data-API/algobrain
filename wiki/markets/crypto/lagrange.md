---
title: "Lagrange"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, ai-trading, machine-learning]
aliases: ["LA", "Lagrange Labs"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.lagrangefoundation.org"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[zero-knowledge-proof]]", "[[zk-rollup]]", "[[restaking-and-ai]]", "[[eigenlayer]]", "[[zkml]]", "[[on-chain-inference]]", "[[decentralized-ai]]"]
---

# Lagrange

**Lagrange** (LA) is a [[zero-knowledge-proof|zero-knowledge]] coprocessor and verifiable-compute network — an "infinite proving layer" that generates ZK proofs for rollups, apps, coprocessors, and cross-chain interoperability. Its core products are the **ZK Coprocessor** (proving correct computation over arbitrary on-chain storage and block ranges), a **ZK Prover Network** that produces proofs for [[zk-rollup|ZK rollups]], a **State Committee** for cross-chain state, and **DeepProve**, a [[zkml|zkML]] system for proving AI/ML inference. The native token **LA** is used to pay for and stake against proof generation.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21 LA trades at **$0.073007**, ranked **#991** by market capitalization (~**$14.09M**), up **+0.32%** on the day and down **-3.27%** over the trailing week — flat-to-soft in a risk-off market (BTC ~$64,180; Fear & Greed 22 / Extreme Fear). Note the wide gap between market cap and fully diluted valuation: only a small fraction of the 1B total supply circulates, leaving significant emission overhang.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LA |
| **Market Cap Rank** | #991 |
| **Market Cap** | $14,085,885 |
| **Current Price** | $0.073007 |
| **24h / 7d Change** | +0.32% / -3.27% |
| **Categories** | Artificial Intelligence (AI), BNB Chain Ecosystem, Ethereum Ecosystem, Zero Knowledge (ZK), Binance HODLer Airdrops, Binance Alpha Spotlight |
| **Website** | [https://www.lagrangefoundation.org](https://www.lagrangefoundation.org) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). Earlier top-1000 snapshot fields below are retained for history.*

---

## Overview

Today, Lagrange has expanded its ZK Prover Network to power proof generation for ZK rollups, adding onto Lagrange’s existing ZK Coprocessor and State Committee offerings. With this new addition, Lagrange now unlocks proofs for anything – for rollups, apps, coprocessors and interoperability – as an infinite proving layer that enables anyone to prove everything at internet scale. Previously, Lagrange launched the first production-ready ZK prover network in the industry, operated by top operators including Coinbase, Kraken, OKX and more. Now, Lagrange’s ZK Prover Network is expanding to address key challenges faced by rollups and advance ZK adoption and utility.

The ZK Coprocessor can generate a proof of correct computation over arbitrary storage slots for arbitrary block ranges. For example, consider an application that wishes to compute the average on Ethereum for ETH / USDC pricing. A developer must first specify the memory slots and block range (~50,400) that they are interested in including in the data set. Next the developer writes the computations that is to be executed across the storage slots over the different blocks in parallel. Once the proof is generated, it will prove both the storage inclusion and the aggregated computation as valid with respect to a block header derived from smart contract information.

## Architecture & Products

Lagrange is a verifiable-compute infrastructure project rather than an app. Its product lines all share one primitive: producing a succinct [[zero-knowledge-proof|ZK proof]] that some computation was performed correctly, so a smart contract can trust the result without re-executing it.

- **ZK Coprocessor** — proves correct computation over arbitrary historical on-chain state (storage slots across block ranges), giving smart contracts trustless access to large-scale data analytics they could never compute on-chain directly.
- **ZK Prover Network** — a decentralized network of operators that generate proofs for [[zk-rollup|ZK rollups]] and applications; Lagrange has highlighted participation from major operators (e.g. exchanges and infrastructure providers) running prover capacity.
- **State Committee** — a proof-based mechanism for verifying cross-chain state, supporting [[on-chain-inference|interoperability]] and bridging use cases.
- **DeepProve ([[zkml|zkML]])** — a system for generating proofs of AI/ML model inference, so an on-chain consumer can verify that a specific model produced a specific output. This is Lagrange's bridge into the [[decentralized-ai|verifiable-AI]] / [[ai-trading|AI x crypto]] narrative and the reason for its AI category tags.

Lagrange has roots in the [[eigenlayer|EigenLayer]] [[restaking-and-ai|restaking]] ecosystem, where economic security for the prover/committee networks can be bootstrapped via restaked collateral.

### The proving model, precisely

Each Lagrange product reduces to the same cryptographic guarantee: a **succinct [[zero-knowledge-proof|ZK proof]]** that a stated computation was executed correctly over a stated input set, which an on-chain verifier contract can check cheaply without re-running the work. Two ingredients make the coprocessor in particular work:

1. **Verifiable data inclusion.** Ethereum state is committed inside Merkle-Patricia tries whose roots are bound to each block header. To prove a computation over historical state, the prover must first prove that the storage slots it read *genuinely belong* to those blocks — i.e. produce Merkle inclusion proofs against the relevant block-header commitments — before proving the computation that ran on top of them. The final proof attests to both: *these were the real values* and *this was the correct aggregate over them*.
2. **Parallel proof aggregation.** Computing over a wide block range (the worked example spans ~50,400 blocks) is parallelized — sub-proofs are generated independently and then **recursively aggregated** into a single succinct proof. Recursion (a proof that verifies other proofs) is what lets the system scale to "internet-scale" ranges while keeping the on-chain verification cost flat.

The **ZK Prover Network** decentralizes who generates these proofs: a set of operators (Lagrange has highlighted participation from large infrastructure operators such as major exchanges) contribute proving capacity, coordinated and economically secured via [[eigenlayer|EigenLayer]] restaking, with slashing for incorrect or unavailable proofs. **DeepProve** applies the same prove-correct-execution machinery to a neural-network forward pass — proving that a *specific model* produced a *specific output* on a given input — which is the [[zkml|zkML]] primitive underlying verifiable on-chain inference.

## Token Role (LA)

- **Payment for proofs** — applications pay LA to request proof generation from the prover network.
- **[[staking]] / security** — operators stake (or are secured by restaked) collateral to provide proving capacity and earn fees; misbehavior is slashable.
- **Coordination** — LA aligns demand (apps needing proofs) with supply (provers offering compute).

Tokenomics are the key caution: ~193M LA circulate against a 1.00B total supply (MC/FDV ≈ 0.19), so the market cap reflects only ~19% of fully diluted value and substantial future emissions/unlocks loom.

## Competitive Position

Lagrange operates in the fast-moving verifiable-compute / ZK-infrastructure category alongside coprocessor and proving projects (e.g. Axiom, [[brevis|Brevis]], [[risc-zero|RISC Zero]], [[boundless|Boundless]], Succinct, [[zerobase|ZeroBase]], =nil;). Its differentiation is a broad bundle — coprocessor + decentralized prover network + cross-chain state + zkML — and its restaking-based security model. The zkML / DeepProve angle positions it to capture demand if verifiable AI inference becomes a real on-chain primitive. As infrastructure, however, Lagrange's value depends on developers actually routing proof demand through it, and proving is a cost center that competitors are racing to make cheaper.

| Project | Primary primitive | Security model | Differentiator vs. Lagrange |
|---|---|---|---|
| **Lagrange (LA)** | Coprocessor + prover net + State Committee + zkML | EigenLayer restaking | Broadest product bundle; operator-grade prover network; DeepProve zkML |
| **[[brevis\|Brevis]] (BREV)** | Coprocessor over historical/cross-chain data | Pure ZK + optimistic | Narrower data-query focus; Celer lineage |
| **[[boundless\|Boundless]] (ZKC)** | Universal proving marketplace (RISC Zero zkVM) | PoVW staking | Open chain-agnostic marketplace, not a bundled stack |
| **[[zerobase\|ZeroBase]] (ZBT)** | Real-time proving network | ZK + TEE hybrid | Latency focus; TEE trust assumption |
| **Axiom** | ZK coprocessor (Ethereum history) | Pure ZK | Ethereum-native data queries; no native token of comparable profile |

## Narrative & Catalysts

Lagrange sits at the intersection of the two most reflexive infrastructure narratives — **ZK** and **AI** (via DeepProve / zkML) — plus the **restaking** thesis and a **Binance-ecosystem** distribution angle (Binance HODLer Airdrops, Binance Alpha Spotlight category tags). Key catalysts: real, paid proof demand routed through the prover network (the only durable value driver), DeepProve adoption if verifiable on-chain AI inference becomes a live primitive, and expansion of the operator set. The dominant counterweight is dilution — at MC/FDV ≈ 0.19, ~81% of fully diluted value is unrealized supply, so emissions/unlocks can overwhelm demand-side catalysts.

## History & Timeline

- **2025-06-06** — LA all-time high of **$1.72** (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-02-06** — All-time low of **$0.1593** during the bear market (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-22** — Trades ~$0.073, ~90% below ATH; rank #991, market cap ~$14M (cryptodataapi.com / CoinGecko).

> The project has stated its ZK Prover Network was "the first production-ready ZK prover network in the industry," operated by major operators. Founding/TGE dates are not asserted here because no specific dated source for them has been ingested — only the dated price events above.

## Risks

- **Tokenomics / dilution** — very low float (MC/FDV ≈ 0.19); emissions and unlocks are a persistent overhang on price.
- **Narrative dependence** — sits at the intersection of two hype-prone narratives (ZK and AI); valuation can run ahead of usage and de-rate sharply in risk-off tape.
- **Demand / adoption risk** — proving infrastructure only accrues value with real, paid proof demand; that demand is early and competitive.
- **Technical & competitive** — ZK proving is hard, fast-evolving, and heavily contested; cheaper or faster rivals can displace incumbents quickly.
- **Restaking dependency** — security bootstrapped via [[eigenlayer|EigenLayer]] inherits that system's risks (correlated slashing, operator concentration).
- **Low liquidity** — ~$14M market cap; thin liquidity magnifies volatility.

## Trading Playbook (bear / Extreme-Fear regime)

> *Not investment advice. Context only, for the 2026-06-22 Established-Bear-Market regime (Fear & Greed 21).*

- **Regime read.** LA is a low-float, dual-narrative (ZK + AI) microcap — among the highest-beta profiles in the cohort. In an Established Bear Market it tends to overshoot on both sides; the +0.00% 1y figure reflects a name that round-tripped its entire post-listing range.
- **Dilution-aware.** With MC/FDV ≈ 0.19, the structural pressure is the supply schedule; treat rallies into unlock windows with caution and avoid anchoring to FDV-implied "fair value."
- **Catalyst > chart.** Without demonstrable paid proof demand or a DeepProve/zkML adoption catalyst, bounces are narrative-driven. Manage risk tightly and respect the thin order book.
- **Liquidity.** ~$14M cap with thin depth — size down, use limits, expect slippage on size.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 193.00M LA |
| **Total Supply** | 1.00B LA |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $163.96M |
| **Market Cap / FDV Ratio** | 0.19 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.72 (2025-06-06) |
| **Current vs ATH** | -90.45% |
| **All-Time Low** | $0.1593 (2026-02-06) |
| **Current vs ATL** | +3.22% |
| **24h Change** | -7.12% |
| **7d Change** | -16.59% |
| **30d Change** | -24.20% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x0fc2a55d5bd13033f1ee0cdd11f60f7efe66f467` |
| Binance Smart Chain | `0x389ad4bb96d0d6ee5b6ef0efaf4b7db0ba2e02a0` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | LA/USDT | N/A |
| Upbit | LA/KRW | N/A |
| Bitget | LA/USDT | N/A |
| KuCoin | LA/USDT | N/A |
| Crypto.com Exchange | LA/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.lagrangefoundation.org](https://www.lagrangefoundation.org) |
| **Twitter** | [@lagrangefndn](https://twitter.com/lagrangefndn) |
| **Discord** | [https://discord.com/invite/Hnr52BvWUk](https://discord.com/invite/Hnr52BvWUk) |
| **GitHub** | [https://github.com/Lagrange-Labs](https://github.com/Lagrange-Labs) |
| **Whitepaper** | [https://www.lagrange.dev/blog](https://www.lagrange.dev/blog) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $8.25M |
| **Market Cap Rank** | #985 |
| **24h Range** | $0.1638 — $0.1801 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[zero-knowledge-proof]]
- [[zk-rollup]]
- [[zkml]]
- [[eigenlayer]]
- [[restaking-and-ai]]
- [[decentralized-ai]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 via cryptodataapi.com / CoinGecko.
- Project documentation and architecture descriptions: general market knowledge; no additional specific wiki source ingested yet.

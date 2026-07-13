---
title: "Boundless"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins]
aliases: ["ZKC", "Boundless Network"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://beboundless.xyz/"
related: ["[[crypto-markets]]", "[[bnb]]", "[[zero-knowledge-proof]]", "[[verifiable-compute]]", "[[risc-zero]]"]
---

# Boundless

**Boundless** (ZKC) is a universal [[zero-knowledge-proof|zero-knowledge]] proving network — a decentralized marketplace for [[verifiable-compute|verifiable compute]] that lets any blockchain or application offload expensive proof generation to a competitive network of independent provers. Built within the [[risc-zero|RISC Zero]] ecosystem, Boundless aims to make ZK proving a shared, chain-agnostic utility so developers can build high-throughput applications that bypass traditional block-size and gas limits.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).* ZKC trades at **$0.04762542**, ranked **#998** with a market cap of **~$13.84M**. It is down **-1.40%** over 24h and **-7.21%** over the week — softness consistent with the broad ZK/infra cohort during the current Extreme Fear regime (BTC ~$64,180; Fear & Greed 22).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ZKC |
| **Market Cap Rank** | #998 |
| **Market Cap** | ~$13.84M |
| **Current Price** | $0.04762542 |
| **24h / 7d Change** | -1.40% / -7.21% |
| **Categories** | Zero Knowledge (ZK), Verifiable Compute, BNB Chain Ecosystem, Ethereum Ecosystem, Binance HODLer Airdrops, Governance |
| **Website** | [https://beboundless.xyz/](https://beboundless.xyz/) |

---

## Overview

Boundless is a universal protocol that brings [[zero-knowledge-proof|ZK]] proving to every chain. Generating zero-knowledge proofs is computationally expensive and specialized; rather than each chain or app building and operating its own proving infrastructure, Boundless turns proving into an open, competitive marketplace. Developers submit **proof requests**, and a decentralized network of **provers** competes to fulfill them, earning direct fees plus protocol-level incentives.

By abstracting away the complexity of proof generation, aggregation, and on-chain settlement, Boundless lets developers build without managing the underlying infrastructure, while provers supply strong liveness guarantees, censorship resistance, and a steadily improving cost curve driven by open-market competition. This architecture **decouples execution from consensus**, a defining feature of [[verifiable-compute|verifiable computing]]: heavy computation happens off-chain, and only a succinct proof is verified on-chain. As the number of prover nodes grows, total protocol capacity scales, distributing compute across every connected chain.

---

## Mechanism: Proof of Verifiable Work

- **Proof request marketplace.** Applications post proof requests (a computation to be proven). Provers bid to fulfill them, and the winning prover generates the proof and returns it for on-chain verification.
- **Proof of Verifiable Work (PoVW).** Boundless's incentive design rewards provers for useful proving work rather than for arbitrary hashing. Unlike proof-of-work mining, the "work" here is the productive generation of valid ZK proofs, aligning network rewards with actual demand for verifiable compute.
- **RISC Zero foundation.** Boundless leverages the [[risc-zero|RISC Zero]] zkVM, which proves the correct execution of general-purpose programs (compiled to RISC-V), making it possible to prove arbitrary computation rather than only narrow, hand-built circuits.
- **Chain-agnostic.** Because verification is just a smart-contract check, any chain that can verify the proofs can consume Boundless capacity — making proving a shared resource rather than a per-chain silo.

### The proving / verification model, precisely

Boundless's technical core is the [[risc-zero|RISC Zero]] **zkVM**: a virtual machine that executes a general-purpose program (compiled to the RISC-V instruction set) and emits a **ZK proof of correct execution** — a *receipt* attesting that "this exact program, run on these inputs, produced this output," without re-running the program. This generality is the key advantage over hand-written circuits: a developer writes ordinary code (e.g. Rust) rather than designing a bespoke arithmetic circuit per computation, dramatically lowering the engineering cost of adding a new provable workload.

The end-to-end loop:

1. **Request.** An application posts a proof request to the marketplace — a program plus inputs and a price it will pay.
2. **Auction.** Independent provers bid to fulfill it; a winning prover is assigned the job and must post ZKC collateral.
3. **Prove.** The prover runs the program in the RISC Zero zkVM and generates the execution receipt (the succinct proof).
4. **Verify & settle.** The receipt is verified on the destination chain by a small verifier contract; on success the prover is paid (fee + PoVW reward), on failure-to-deliver the prover's stake is **slashed**. Because verification cost is roughly constant regardless of how heavy the proven computation was, even very large off-chain workloads settle cheaply on-chain.

This is the concrete meaning of "decoupling execution from consensus": the chain never re-executes the work, it only checks a proof, so throughput is bounded by proving capacity (which scales with the number of provers) rather than by block gas limits.

---

## Token Role

ZKC is the protocol's native token. Its roles:

- **Staking / collateral** — provers [[staking|stake]] ZKC as collateral to participate, with slashing for failure to deliver valid proofs on time, ensuring liveness and honesty.
- **Incentives / rewards** — provers earn ZKC (via PoVW) on top of request fees, bootstrapping the supply side until organic proving demand matures.
- **Governance** — holders steer protocol parameters.
- **Settlement** — proof requests are paid for within the marketplace, tying fee flow to ZKC demand.

---

## Competitive Position

Boundless sits in the fast-growing "ZK proving / verifiable compute" infrastructure category alongside other decentralized prover networks and proof aggregation layers. Its association with [[risc-zero|RISC Zero]] gives it a credible technical lineage and a general-purpose zkVM. The bull case is that as rollups, bridges, and AI/data-integrity use cases proliferate, demand for outsourced proving compounds and a neutral, chain-agnostic marketplace captures it. The bear case is that proving is increasingly commoditized, many teams build proving in-house, and a decentralized marketplace must win on cost and latency against vertically integrated alternatives.

| Project | Model | Foundation | Differentiator vs. Boundless |
|---|---|---|---|
| **Boundless (ZKC)** | Open proving marketplace + PoVW | RISC Zero zkVM (RISC-V) | Neutral, chain-agnostic auction marketplace; general zkVM |
| **[[lagrange\|Lagrange]] (LA)** | Bundled coprocessor + prover net + zkML | Custom ZK + EigenLayer | Broader integrated stack, restaking-secured |
| **[[brevis\|Brevis]] (BREV)** | Coprocessor over historical data | Custom ZK + optimistic | Data-query specialization, not a general marketplace |
| **[[zerobase\|ZeroBase]] (ZBT)** | Real-time proving network | ZK + TEE hybrid | Latency focus; TEE trust assumption |
| **Succinct (SP1)** | zkVM + prover network | SP1 zkVM (RISC-V) | Closest analogue — competes directly on zkVM + proving |

The sharpest direct comparison is to other **general-purpose zkVM + prover-network** plays (Succinct's SP1); Boundless's wedge is the explicit *open auction marketplace* with Proof of Verifiable Work rather than a single integrated prover.

---

## Narrative & Catalysts

Boundless trades on the **ZK / verifiable-compute** narrative and the **RISC Zero ecosystem** halo, with a **Binance-distribution** angle (Binance HODLer Airdrops category tag). Catalysts: real proof demand from rollups/bridges/AI-integrity use cases flowing through the marketplace, growth in the active prover set (capacity scales with provers), and any flagship integrations that prove the chain-agnostic thesis. The bear weight is the same as the cohort: proving costs are falling industry-wide and emissions create supply overhang, so a marketplace must grow volume faster than margins compress.

---

## History & Timeline

- **2025-09-15** — ZKC all-time high of **$1.78** (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-03-29** — All-time low of **$0.0656** (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-22** — Trades ~$0.0476, deep below ATH; rank #998, market cap ~$13.8M; -1.40% 24h / -7.21% 7d, tracking the broad ZK/infra drawdown (cryptodataapi.com / CoinGecko).

> Only dated price events from the ingested snapshot are listed. No specific dated TGE/launch source has been ingested, so a launch date is not asserted.

---

## Risks

- **Narrative dependence.** Pricing is tightly coupled to the ZK / verifiable-compute / restaking-infra narrative; rotations out of "infra" hit it hard (note **-7.21% 7d**).
- **Emissions / dilution.** Circulating supply is a fraction of total supply, so prover rewards and future unlocks create meaningful supply overhang.
- **Demand risk.** The marketplace only accrues value if real proof demand materializes; early-stage proving networks can be dominated by incentive-farming rather than organic usage.
- **Competition / commoditization.** Proving costs are falling industry-wide; a marketplace can be squeezed if margins compress faster than volume grows.
- **Low liquidity.** A sub-$15M cap makes ZKC volatile and exposed to slippage and sentiment swings.

---

## Trading Playbook (bear / Extreme-Fear regime)

> *Not investment advice. Context only, for the 2026-06-22 Established-Bear-Market regime (Fear & Greed 21).*

- **Regime read.** ZKC is a sub-$15M ZK-infra microcap trading ~97% below its 2025 ATH. In an Established Bear Market the cohort bleeds on infra rotations (-7.21% on the week); there is no evidence of a floor in the price action.
- **Emissions.** Max supply is uncapped and prover rewards (PoVW) plus unlocks are a continuous source of new supply — a structural headwind that demand must outrun.
- **Demand proof, not promise.** The marketplace thesis only pays off with organic, paid proof volume; until that is visible, treat moves as narrative/liquidity-driven. Catalyst-gate any long thesis.
- **Sizing.** Thin depth — use limits, size down, expect slippage.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 290.26M ZKC |
| **Total Supply** | 1.04B ZKC |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $73.37M |
| **Market Cap / FDV Ratio** | 0.28 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.78 (2025-09-15) |
| **All-Time Low** | $0.0656 (2026-03-29) |
| **24h Change** | -1.40% |
| **7d Change** | -7.21% |

> *Current price $0.04762542 is deep below the 2025 ATH, with continued weakness (-7.21% 7d) tracking the broad ZK/infra drawdown during Extreme Fear.*

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0x15247e6e23d3923a853ccf15940a20ccdf16e94a` |
| Ethereum | `0x000006c2a22ff4a44ff1f5d0f2ed65f781f55555` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ZKC/USDT | N/A |
| Upbit | ZKC/KRW | N/A |
| Bitget | ZKC/USDT | N/A |
| KuCoin | ZKC/USDT | N/A |
| Crypto.com Exchange | ZKC/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://beboundless.xyz/](https://beboundless.xyz/) |
| **Twitter** | [@boundless_xyz](https://twitter.com/boundless_xyz) |
| **Telegram** | [boundlessannouncements](https://t.me/boundlessannouncements) (2,636 members) |
| **Whitepaper** | [https://docs.beboundless.xyz/developers/what](https://docs.beboundless.xyz/developers/what) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $0.04762542 |
| **Market Cap Rank** | #998 |
| **24h Change** | -1.40% |
| **7d Change** | -7.21% |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Related

- [[zero-knowledge-proof]]
- [[verifiable-compute]]
- [[risc-zero]]
- [[staking]]
- [[crypto-markets]]
- [[bnb]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original snapshot data
- Market data 2026-06-21 via cryptodataapi.com / CoinGecko
- General market knowledge; no additional specific wiki source ingested yet.

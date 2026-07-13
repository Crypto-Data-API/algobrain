---
title: "Brevis"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, ethereum]
aliases: ["BREV"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://brevis.network/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[zero-knowledge-proof]]", "[[verifiable-compute]]"]
---

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

# Brevis

**Brevis** (BREV) is a **[[zero-knowledge-proof|ZK]] coprocessor** — verifiable off-chain compute infrastructure that lets smart contracts access and compute over large volumes of historical and cross-chain data without trusting an intermediary. Instead of running expensive logic on-chain, a contract requests a result from Brevis; the network computes it off-chain over real blockchain data and returns the answer together with a [[zero-knowledge-proof]] that the computation was performed correctly. As of 2026-06-22 BREV trades at **$0.081184**, ranked **#822** by market capitalization with a market cap of roughly **$20.29M** (24h **-1.11%**, 7d **-5.80%**) against a risk-off market backdrop (Fear & Greed 21 / Extreme Fear; BTC ~$64,508).

---

## What Brevis Does

A "coprocessor" in the [[verifiable-compute]] sense is an off-chain engine that performs heavy computation and proves the result, so the on-chain contract only has to verify a succinct proof rather than re-execute the work. Brevis applies this to **historical and cross-chain blockchain data**: a dApp can ask questions like "what was this wallet's average trading volume over the last 90 days across these chains?" and receive a ZK-verified answer it can act on trustlessly.

Typical use cases include:

- **Data-driven DeFi** — loyalty/volume-based fee tiers, trading-history-based incentives, and on-chain reputation, computed over real history rather than self-reported state.
- **Cross-chain state proofs** — proving facts about one chain's state to a contract on another.
- **Scaling compute** — moving expensive aggregation/analytics off-chain while preserving trustlessness via proofs.

---

## Mechanism & Architecture

- **ZK coprocessor model** — contracts emit a request; Brevis provers fetch the relevant on-chain data, run the requested computation off-chain, and generate a [[zero-knowledge-proof]] attesting correctness. The contract verifies the proof on-chain and consumes the result.
- **Proof systems** — Brevis combines ZK circuits with optimistic and aggregation techniques (its "coChain" / pipelined-proving design) to amortize proving cost across many queries.
- **Data access** — supports historical block data and cross-chain reads, which is the hard part that pure on-chain contracts cannot do efficiently.
- **Origins** — Brevis was incubated by the team behind Celer Network; its whitepaper is hosted on Celer infrastructure.

Brevis is deployed across [[ethereum|Ethereum]], BNB Chain, and Base ecosystems (token contract address `0x086f405146ce90135750bbec9a063a8b20a8bffb` on each).

### The proving / verification model, precisely

The hard problem a coprocessor solves is **trustlessly reading the past**. A smart contract can cheaply read *current* state, but it cannot natively look back over thousands of historical blocks or across other chains — that data is not in its execution context, and naively importing it would mean trusting whoever supplied it. Brevis closes this gap with two linked proofs:

1. **Data-authenticity proof.** Historical blockchain state lives in Merkle-Patricia tries committed to each block header, and the chain of block headers is itself hash-linked. Brevis's provers generate ZK proofs that the values they read (a wallet's balances, swap events, positions across a 90-day window, etc.) genuinely appear in those committed blocks — so the contract knows the *inputs* are real, not asserted.
2. **Computation proof.** A second proof attests that the requested computation (e.g. an average, a sum, a threshold test) was executed correctly over exactly those authenticated inputs.

The final receipt the on-chain verifier checks binds both together: *these are the real historical values* AND *this is the correct result over them*. To keep this affordable at scale, Brevis's **coChain** / pipelined design combines pure-ZK circuits with optimistic and **aggregation** techniques — batching and recursively combining many sub-proofs so the marginal cost of each additional query falls and on-chain verification stays cheap regardless of how much history was processed. The optimistic layer trades a challenge-window delay for lower proving cost on workloads that can tolerate it, while a ZK fallback preserves trustlessness.

---

## The BREV Token

BREV is the network's native token (circulating ≈ 250M of a 1B max supply, market-cap-to-FDV ratio ≈ 0.25, meaning roughly three-quarters of the supply is not yet circulating — a meaningful future-emission overhang). It was distributed in part via a **Binance HODLer Airdrop**. The token's intended roles in a ZK coprocessor network typically include:

- **Paying for proving / compute** — fees for off-chain computation and proof generation.
- **Staking / security** — collateral aligning provers and operators with honest behavior.
- **Governance** — protocol parameters and incentives.

The low circulating-to-total ratio is a key risk factor: unlocks can pressure price as more supply enters the market.

---

## Competitive Position

Brevis sits in the fast-growing **ZK coprocessor / verifiable-compute** category alongside projects like Axiom, [[lagrange|Lagrange]], and Herodotus, and overlaps conceptually with general-purpose [[zero-knowledge-proof|ZK]] infrastructure (e.g. [[boundless|Boundless]], [[zerobase|ZeroBase]]). The category's thesis is that as DeFi and on-chain apps demand richer, history-aware logic, trustless off-chain compute becomes essential. Competition centers on proving cost, latency, developer ergonomics, and breadth of supported data sources/chains. The space is early and unproven at scale, so category winners are not yet settled.

| Project | Focus | Proof approach | Differentiator vs. Brevis |
|---|---|---|---|
| **Brevis (BREV)** | Coprocessor over historical & cross-chain data | ZK + optimistic + aggregation (coChain) | Data-driven DeFi (volume tiers, reputation); Celer lineage |
| **Axiom** | Ethereum historical-data coprocessor | Pure ZK | Ethereum-native focus; deep historical queries |
| **[[lagrange\|Lagrange]] (LA)** | Coprocessor + prover net + zkML | ZK, restaking-secured | Broader bundle incl. zkML (DeepProve) |
| **Herodotus** | Storage proofs / cross-chain state access | ZK storage proofs | Storage-proof specialization |
| **[[boundless\|Boundless]] (ZKC)** | General proving marketplace | RISC Zero zkVM | Chain-agnostic open marketplace, not data-specific |

Brevis's wedge is **data-driven DeFi** — volume-based fee tiers, history-based incentives, and on-chain reputation computed over authenticated history — plus its hybrid ZK/optimistic cost optimization.

---

## Narrative & Catalysts

Brevis trades on the **ZK coprocessor / verifiable-compute** narrative, with a **Binance-distribution** angle (Binance HODLer Airdrops, Base Native category tags) and a **Celer** pedigree. Catalysts: real integrations where dApps use Brevis-computed history (fee tiers, loyalty, reputation) in production, breadth of supported chains/data sources, and proving-cost improvements that make richer queries economic. Counterweight: the category is early and unproven at scale, and the heavy emission overhang (~25% of supply circulating) means unlocks can swamp token-side catalysts.

---

## History & Timeline

- **2026-01-07** — BREV all-time high of **$0.5601** (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-04-05** — All-time low of **$0.1042** (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-22** — Trades ~$0.0812, ~79% below ATH; rank #822, market cap ~$20.3M; -1.11% 24h / -5.80% 7d against the Extreme-Fear backdrop (cryptodataapi.com / CoinGecko).

> Brevis was incubated by the Celer Network team (whitepaper hosted on Celer infrastructure). Beyond the dated price events above, no specific dated TGE/launch source has been ingested, so a launch date is not asserted.

---

## Risks

- **Supply overhang** — only ~25% of tokens circulate; future unlocks can dilute holders.
- **Early/unproven category** — verifiable off-chain compute is technically demanding and adoption is nascent; product-market fit is not guaranteed.
- **Smart-contract & cryptographic risk** — bugs in circuits, provers, or verifier contracts could produce invalid-but-accepted results.
- **Liquidity / volatility** — microcap (#822, ~$20M); 7d down 5.80%.
- **Competitive risk** — a crowded coprocessor field with well-funded rivals.

*Not investment advice. ZK-infrastructure microcaps are highly speculative.*

---

## Trading Playbook (bear / Extreme-Fear regime)

> *Not investment advice. Context only, for the 2026-06-22 Established-Bear-Market regime (Fear & Greed 21).*

- **Regime read.** BREV is a ~$20M ZK-coprocessor microcap ~79% below its January-2026 ATH, drifting down with the infra cohort (-5.80% on the week). No floor is evident; the ATL ($0.1042) printed in April 2026 has already been broken below the current quote, underscoring how weak the tape is.
- **Emissions.** ~25% float means unlocks/emissions are the dominant medium-term overhang; rallies into unlock windows have historically faded across this cohort.
- **Adoption proof.** The data-driven-DeFi thesis only pays off with live integrations consuming Brevis-computed history; absent that, moves are narrative/liquidity-driven. Catalyst-gate any long.
- **Sizing.** Microcap depth — use limits, size down, expect slippage on size.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BREV |
| **Market Cap Rank** | #822 |
| **Market Cap** | $20,293,208 |
| **Current Price** | $0.081184 |
| **24h Change** | -1.11% |
| **7d Change** | -5.80% |
| **Categories** | Infrastructure, Smart Contract Platform, BNB Chain Ecosystem, Zero Knowledge (ZK), Base Ecosystem, Binance HODLer Airdrops, Base Native |
| **Website** | [https://brevis.network/](https://brevis.network/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 250.00M BREV |
| **Total Supply** | 1.00B BREV |
| **Max Supply** | 1.00B BREV |
| **Fully Diluted Valuation** | $116.34M |
| **Market Cap / FDV Ratio** | 0.25 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.5601 (2026-01-07) |
| **Current vs ATH** | -79.21% |
| **All-Time Low** | $0.1042 (2026-04-05) |
| **24h Change** (2026-06-22) | -1.11% |
| **7d Change** (2026-06-22) | -5.80% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x086f405146ce90135750bbec9a063a8b20a8bffb` |
| Binance Smart Chain | `0x086f405146ce90135750bbec9a063a8b20a8bffb` |
| Base | `0x086f405146ce90135750bbec9a063a8b20a8bffb` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | BREV/USDT | N/A |
| Kraken | BREV/USD | N/A |
| Upbit | BREV/KRW | N/A |
| Bitget | BREV/USDT | N/A |
| KuCoin | BREV/USDT | N/A |
| Crypto.com Exchange | BREV/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://brevis.network/](https://brevis.network/) |
| **Twitter** | [@brevis_zk](https://twitter.com/brevis_zk) |
| **Telegram** | [brevisnetwork](https://t.me/brevisnetwork) (5,655 members) |
| **GitHub** | [https://github.com/brevis-network/](https://github.com/brevis-network/) |
| **Whitepaper** | [https://get.celer.app/brevis/BrevisWhitePaper_09271015.pdf](https://get.celer.app/brevis/BrevisWhitePaper_09271015.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Market Cap Rank** | #822 |
| **Market Cap** | $20,293,208 |
| **Price** | $0.081184 |
| **24h Change** | -1.11% |
| **7d Change** | -5.80% |
| **Last Updated** | 2026-06-22 |

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
- [[verifiable-compute]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 via cryptodataapi.com / CoinGecko.
- General market knowledge; no specific protocol source ingested yet.

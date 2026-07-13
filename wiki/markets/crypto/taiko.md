---
title: "Taiko"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, ethereum, altcoins]
aliases: ["TAIKO"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://taiko.xyz/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-2]]", "[[zk-rollup]]", "[[zkevm]]", "[[sequencer]]", "[[data-availability]]", "[[airdrop]]"]
---

# Taiko

**Taiko** (TAIKO) is an [[ethereum|Ethereum]] [[layer-2|Layer 2]] built as an **Ethereum-equivalent (Type-1) [[zkevm|zkEVM]] [[zk-rollup|ZK-rollup]]** and operated as a **based rollup** — meaning transaction sequencing is delegated to Ethereum L1 validators/proposers rather than a dedicated, project-controlled [[sequencer]]. The goal is for using Taiko to feel identical to using Ethereum, with the same opcodes and EVM semantics. As of 2026-06-22 TAIKO trades at **$0.088418**, ranked **#890** with a market capitalization of **~$17.1M**, up **5.27%** on the day and **1.17%** over the week — a relative outperformer within a broad bear regime.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Crypto Fear & Greed Index: 21 (Extreme Fear).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TAIKO |
| **Market Cap Rank** | #890 |
| **Market Cap** | ~$17.10M |
| **Current Price** | $0.088418 |
| **24h Change** | +5.27% |
| **7d Change** | +1.17% |
| **Architecture** | Ethereum L2 — Type-1 zkEVM ZK-rollup, based rollup |
| **Categories** | Smart Contract Platform, Ethereum Ecosystem, Layer 2 (L2), Zero Knowledge (ZK), Rollup, OKX Ventures Portfolio, Binance Alpha Spotlight |
| **Website** | [https://taiko.xyz/](https://taiko.xyz/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Crypto Fear & Greed Index: 21 (Extreme Fear).*

---

## Overview

Taiko is a fully open-source, permissionless [[ethereum|Ethereum]] [[layer-2|Layer 2]]. Architecturally it is a [[zk-rollup|ZK-rollup]]: it batches L2 transactions, generates a **zero-knowledge validity proof** that the new state was computed correctly, and posts that proof plus the data to Ethereum [[layer-1|L1]] for [[data-availability|data availability]] and settlement. Unlike [[optimistic-rollup|optimistic rollups]], validity proofs give near-instant cryptographic finality without a multi-day fraud-proof challenge window.

Taiko aims to be a **Type-1 / Ethereum-equivalent [[zkevm|zkEVM]]** — the most faithful (and most technically demanding) zkEVM class — reusing Ethereum's execution environment with no modifications, so existing contracts and tooling work unchanged. Taiko's other defining design is the **based rollup** model: instead of running its own [[sequencer|sequencer]], Taiko outsources transaction ordering to Ethereum L1 proposers/validators ("based sequencing"). This inherits L1's liveness and censorship-resistance and avoids a single project-controlled sequencer, at the cost of more complex economics and dependence on L1 block builders.

### zkEVM "Type" classification

The Ethereum research community (notably Vitalik Buterin's taxonomy) classifies [[zkevm|zkEVMs]] by how faithfully they reproduce Ethereum:

| Type | Equivalence | Trade-off | Examples |
|---|---|---|---|
| **Type 1** | Fully **Ethereum-equivalent** (no changes to Ethereum) | Hardest to prove; slowest, most expensive proofs | **Taiko** |
| Type 2 | EVM-equivalent (minor internal changes) | Faster proving, near-perfect compatibility | [[scroll]], Polygon zkEVM (target) |
| Type 2.5 / 3 | Almost-EVM-equivalent | Faster proving, some opcodes/precompiles differ | early zkEVMs |
| Type 4 | High-level-language equivalent (compiles Solidity to custom bytecode) | Fastest proving, lowest compatibility | [[zksync\|zkSync Era]] (originally), StarkNet |

Taiko's Type-1 choice is the purist's path: maximum compatibility and the strongest "feels exactly like Ethereum" guarantee, at the price of the heaviest proving workload — which is why prover performance and cost are central to its economics.

### Based rollup: how sequencing works

In a conventional rollup, a project-run [[sequencer]] orders transactions, captures MEV, and is a censorship/liveness single point of failure. A **based rollup** ("L1-sequenced rollup") instead lets **Ethereum L1 block proposers/builders** include and order the rollup's blocks as part of L1 block production. Consequences:

- **Inherited liveness & censorship-resistance** — Taiko is as live and censorship-resistant as Ethereum L1 itself; there is no separate sequencer that can go down or censor.
- **Decentralization by default** — no need to "decentralize the sequencer" later (the problem [[metis-token|Metis]], [[blast]], [[optimism]] and others must solve), because sequencing *is* Ethereum's proposer set.
- **MEV / economics flow to L1** — MEV is captured by L1 proposers/builders rather than the rollup, complicating fee/token economics and removing sequencer revenue as a value-accrual source.

### Rollup stack: settlement, data availability, proving

| Layer | Taiko approach |
|---|---|
| **Settlement** | [[ethereum]] L1 — validity ([[zk-rollup\|ZK]]) proofs verified on Ethereum give cryptographic finality, no multi-day fraud-proof window |
| **Data availability** | Transaction data posted to Ethereum (blobs, post-[[eip-4844\|EIP-4844]]) for [[data-availability]] |
| **Execution** | Type-1 [[zkevm]] — unmodified Ethereum execution environment |
| **Sequencing** | **Based** — Ethereum L1 proposers/builders order Taiko blocks |
| **Proving** | Open, permissionless **provers** generate validity proofs and are rewarded in protocol incentives; multi-prover designs for robustness |
| **Gas token** | **ETH** (TAIKO is governance/incentive only) |

---

## Comparison vs peer Layer-2 networks

| Network | Proof system | zkEVM type | Sequencing | Finality |
|---|---|---|---|---|
| **Taiko** | [[zk-rollup\|ZK]] (validity) | **Type-1 (Ethereum-equivalent)** | **Based (L1)** | Fast (proof verification) |
| [[zksync\|zkSync Era]] | ZK | Type-4 (LLVM/zkEVM) | Centralized | Fast |
| [[scroll\|Scroll]] | ZK | Type-2 | Centralized | Fast |
| [[optimism\|Optimism]] | [[optimistic-rollup\|Optimistic]] | n/a (EVM-equiv.) | Centralized | ~7-day window |
| [[arbitrum\|Arbitrum]] | Optimistic | n/a | Centralized | ~7-day window |
| [[metis-token\|Metis]] | Optimistic | n/a | Decentralized (DSEQ) | ~7-day window |

Taiko is differentiated on two axes simultaneously — it is both the most Ethereum-faithful zkEVM class (Type-1) *and* a based rollup — making it one of the more ideologically "Ethereum-aligned" L2 designs, though the based model is newer and less battle-tested at scale.

---

## Governance

TAIKO is the protocol's governance and incentive token. Holders govern protocol parameters, and the token is used to coordinate and reward the open prover and proposer markets that secure and operate the based rollup. Because gas is paid in ETH and MEV accrues to L1, TAIKO's value accrual depends primarily on governance demand and any protocol-level incentive/fee capture rather than on a transaction-fee burn — a structurally thinner value-accrual story than fee-burning L2s.

---

## Token & What It Does

The **TAIKO** token is the network's governance and protocol-incentive asset. It is used to coordinate the protocol's actors — block **proposers** and **provers** (who are rewarded for generating validity proofs) — and for governance over protocol parameters. Gas on Taiko is paid in ETH, in keeping with its Ethereum-equivalence goal; TAIKO itself is not the gas token. Total / max supply is 1.0B TAIKO with roughly 192M circulating, leaving a low market-cap-to-FDV ratio (~0.14–0.19) and a substantial future-unlock overhang.

---

## History

Taiko ran a series of public testnets ("Alpha"/Katla, etc.) before launching its mainnet and the TAIKO token in mid-2024, distributed in part via an [[airdrop]] to early testnet participants and community members. As with most L2 governance tokens minted near the 2024 peak, TAIKO has fallen sharply since — it sits roughly 97% below its 2024 all-time high amid the broader bear regime.

### Timeline

- **2022-2024** — Multiple public testnets (Alpha series, Katla, Hekla) validating the Type-1 [[zkevm]] and based-sequencing design; backed by investors including OKX Ventures.
- **2024-05/06** — Mainnet launch and **TAIKO token generation / [[airdrop]]** to testnet participants and community; all-time high ~$3.80 (2024-06-05), followed by the typical post-airdrop decline.
- **2024-2025** — Continued work on prover decentralization (multi-prover, permissionless proving) and based-rollup preconfirmation research to improve UX latency.
- **2026** — All-time low $0.1063 (2026-02-06); trading $0.088418 as of 2026-06-22 (the current price is below the listed ATL because the prior ATL field predates more recent lows — figures as reported by CoinGecko).

> *Additional events will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Risks

- **Prover complexity & cost** — Type-1 zkEVM proving is computationally heavy; proving latency/cost and prover centralization are practical risks for a small-cap network.
- **Based-rollup dependencies** — outsourcing sequencing to L1 ties Taiko's UX and economics to Ethereum block production and the proposer-builder pipeline; this is a newer, less battle-tested model than centralized sequencing.
- **Rollup security assumptions** — ZK-rollup safety depends on the soundness of the proving system and on L1 data availability; a bug in the prover/verifier circuits is catastrophic.
- **Token overhang & decay** — large unvested supply and the post-airdrop sell-down weigh on price; the token is down ~97% from its ATH.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 191.52M TAIKO |
| **Total Supply** | 1.00B TAIKO |
| **Max Supply** | 1.00B TAIKO |
| **Fully Diluted Valuation** | $114.91M |
| **Market Cap / FDV Ratio** | 0.19 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.80 (2024-06-05) |
| **Current vs ATH** | -96.97% |
| **All-Time Low** | $0.1063 (2026-02-06) |
| **Current vs ATL** | +8.38% |
| **24h Change** | -2.56% |
| **7d Change** | -12.41% |
| **30d Change** | +0.86% |
| **1y Change** | -77.41% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x10dea67478c5f8c5e2d90e5e9b26dbe60c54d800` |
| Binance Smart Chain | `0x30c60b20c25b2810ca524810467a0c342294fc61` |
| Taiko | `0xa9d23408b9ba935c230493c40c73824df71a0975` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Upbit | TAIKO/KRW | N/A |
| Bitget | TAIKO/USDT | N/A |
| KuCoin | TAIKO/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://taiko.xyz/](https://taiko.xyz/) |
| **Twitter** | [@taikoxyz](https://twitter.com/taikoxyz) |
| **Discord** | [https://discord.com/invite/taikoxyz](https://discord.com/invite/taikoxyz) |
| **GitHub** | [https://github.com/taikoxyz](https://github.com/taikoxyz) |
| **Whitepaper** | [https://docs.taiko.xyz/start-here/getting-started](https://docs.taiko.xyz/start-here/getting-started) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.96M (2026-04-09 snapshot) |
| **Market Cap Rank** | #890 |
| **Price (2026-06-22)** | $0.088418 |
| **24h Change (2026-06-22)** | +5.27% |
| **7d Change (2026-06-22)** | +1.17% |
| **24h Range (2026-04-09 snapshot)** | $0.1150 — $0.1185 |
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
- [[layer-2]]
- [[zk-rollup]]
- [[zkevm]]
- [[sequencer]]
- [[data-availability]]
- [[airdrop]]
- [[optimism]]
- [[arbitrum]]
- [[metis-token]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 via cryptodataapi.com / CoinGecko (Crypto Fear & Greed Index: 21, Extreme Fear).
- General market knowledge; no additional specific wiki source ingested yet for architecture/history claims.

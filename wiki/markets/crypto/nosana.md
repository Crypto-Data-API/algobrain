---
title: "Nosana"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [ai-trading, altcoins, crypto, machine-learning]
aliases: ["NOS", "Nosana"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://nosana.io/"
related: ["[[artificial-intelligence]]", "[[crypto-markets]]", "[[decentralized-compute]]", "[[depin]]", "[[solana]]"]
---

# Nosana

**Nosana** (NOS) is a [[solana|Solana]]-based **decentralized GPU compute network** ([[depin|DePIN]]) for [[artificial-intelligence|AI]] workloads — primarily AI inference. It coordinates a permissionless marketplace where GPU owners contribute hardware and AI developers rent that compute on demand, with [[solana|Solana]] handling fast, low-cost coordination and settlement. (Nosana originally launched as a CPU-based CI/CD crowd-computing platform and has since pivoted to GPU-powered [[decentralized-compute|decentralized compute]] for the AI inference market.) It ranks **#670** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).* NOS trades around **$0.2813**, market cap **~$28.1M** (rank #670), **-3.49% over 24h** and a sharp **-19.27% over 7d** — significant relative weakness, amplified by an Extreme-Fear market (Fear & Greed 22, BTC ~$64,180).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NOS |
| **Market Cap Rank** | #670 |
| **Market Cap** | $28,125,886 |
| **Current Price** | $0.281259 |
| **Categories** | Artificial Intelligence (AI), Solana Ecosystem, DePIN |
| **Website** | [https://nosana.io/](https://nosana.io/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Nosana operates a [[decentralized-compute|decentralized compute]] network on [[solana|Solana]]. GPU operators ("hosts") register their hardware and earn rewards for completing compute jobs, while AI developers and applications submit inference workloads (and, increasingly, other GPU-bound tasks) to the network and pay for the compute they consume. By aggregating idle and independently-owned GPUs into a single marketplace, Nosana aims to undercut centralized cloud GPU pricing — the core value proposition of the GPU [[depin|DePIN]] sector.

Solana is used as the coordination and settlement layer: its high throughput and low fees make it suitable for the frequent micro-settlements and job-scheduling messages a compute marketplace generates. Nosana's earlier identity was a CPU-based, crowd-sourced CI/CD (continuous-integration) platform; with the AI compute boom it repositioned toward GPU inference, which is now its primary focus and the basis for its "AI + DePIN" categorization.

---

## Architecture — How It Works

Nosana is structured as a three-sided marketplace coordinated on-chain by Solana programs (smart contracts):

1. **Hosts (supply side).** GPU owners install the Nosana node software and register their hardware. The network's design favors **AI inference** — running an already-trained model to produce outputs — rather than large distributed training, because inference is latency-tolerant, parallelizable across many independent single-GPU machines, and does not require the high-bandwidth interconnect (NVLink/InfiniBand) that distributed training needs. This is what makes a permissionless pool of heterogeneous, geographically-scattered GPUs viable.
2. **Job posters (demand side).** Developers package a workload as a container image (a job definition), specify the GPU class and resources required, and submit it with a NOS payment. The job is matched to an eligible host, executed, and the result returned.
3. **Coordination / settlement layer (Solana).** On-chain programs handle job posting, host selection, escrow of payment, and release of rewards on verified completion. Solana's sub-second finality and sub-cent fees let the network settle many small jobs without the settlement cost swamping the compute cost — a structural reason Nosana chose Solana over an EVM L1.

**Verification and trust.** The defining hard problem of any compute DePIN is proving that an untrusted, anonymous host *actually ran the job correctly* rather than returning garbage to farm rewards. Nosana relies on a combination of host **staking** (economic skin-in-the-game that can be slashed for misbehavior), reputation tiers, and redundancy/challenge checks rather than full cryptographic proof-of-computation. This is weaker than the zero-knowledge verifiability offered by a data network like [[space-and-time|Space and Time]], and is an open area for all GPU DePINs.

**Inference focus.** Nosana has leaned into being an *inference endpoint* network — letting developers deploy open models (LLMs, image/diffusion models) and call them via API, competing with hosted-inference offerings rather than only renting raw GPU time. This moves it up the value chain from "spot GPU rental" (where it competes head-on with [[akash-network|Akash]]) toward "serverless AI inference" (where the comparison is to centralized inference APIs).

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 100.00M NOS |
| **Total Supply** | 100.00M NOS |
| **Max Supply** | 100.00M NOS |
| **Fully Diluted Valuation** | $23.84M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $7.83 (2024-03-06) |
| **Current vs ATH** | -96.98% |
| **All-Time Low** | $0.0105 (2023-10-23) |
| **Current vs ATL** | +2163.50% |
| **24h Change** | -3.49% |
| **7d Change** | -19.27% |
| **1y Change** | -55.48% |

> NOS's **-19.3% weekly drop** was among the steepest 7-day declines among AI/DePIN small-caps in this snapshot, a reminder of how reflexive these narrative-driven tokens are in risk-off conditions. NOS is ~97% below its March 2024 ATH of $7.83. Unusually for the sector, NOS has a **fully circulating fixed supply** (100M, MCap/FDV ≈ 1.00), so there is no future-unlock dilution overhang.

---

## Architecture & Token Role

The **NOS token** (SPL token on [[solana|Solana]]) is the network's unit of work and coordination:

- **Payment / work token** — buyers pay NOS to rent GPU compute; hosts earn NOS for completing verified jobs. This is the central [[depin|DePIN]] demand loop — real inference usage should drive NOS throughput.
- **Staking** — hosts and participants stake NOS (Nosana has used staking tiers/"NOS staking" to rank node access and reputation), aligning operators with network quality and providing slashing-style accountability.
- **Governance** — NOS is intended to govern protocol parameters over time.

Because total supply is fixed and already fully circulating, the demand-vs-emissions dynamic is unusually clean: there is no inflationary host-reward emission diluting the token, so value accrual depends almost entirely on **paid compute demand** and on rewards being funded by buyer payments rather than new issuance.

### Value Accrual & Governance

NOS captures value through three channels, all gated by *real usage* rather than emissions:

- **Fee throughput.** Every paid job routes NOS from buyer to host. Higher GPU utilization means more NOS velocity and, in principle, more demand to acquire and hold NOS to transact.
- **Staking sink.** Hosts must stake NOS to access better job tiers and build reputation; this locks supply out of the float and ties host revenue to network quality.
- **Governance.** NOS is intended to govern protocol parameters (fee splits, staking tiers, treasury) over time, giving holders a claim on how the marketplace evolves.

The fixed 100M supply is the cleanest part of the Nosana thesis: unlike most [[depin|DePIN]] peers, there is **no future-unlock or emission overhang** diluting holders. The flip side is that there is no inflationary subsidy to bootstrap host supply — the network must fund rewards from genuine buyer payments, raising the bar for cold-start demand.

## Competitive Position

Nosana competes directly in the GPU [[depin|DePIN]] sector and indirectly against centralized GPU clouds (AWS, CoreWeave, Lambda). Its angle is Solana-native speed/cost plus a focus on AI **inference** and serverless model endpoints rather than raw GPU spot rental.

| Project | Token | Chain | Primary focus | Supply / dilution | Distinct angle |
|---|---|---|---|---|---|
| **Nosana** | NOS | [[solana]] | GPU inference / serverless model endpoints | 100M fully circulating, **no overhang** | Solana-native speed + inference focus |
| **[[render-token\|Render]]** | RNDR/RENDER | Solana (migrated) | GPU rendering + expanding to AI compute | Emission-based (BME model) | Largest GPU DePIN brand; rendering heritage |
| **[[akash-network\|Akash]]** | AKT | Cosmos | General GPU/CPU cloud (Kubernetes-style) | Inflationary staking emissions | Spot-market reverse auction for raw compute |
| **[[io\|io.net]]** | IO | Solana | GPU clustering for ML training + inference | Large FDV / unlock overhang | Aggregates idle GPUs into clusters |

Nosana is among the **smallest** of the credible GPU DePINs by market cap, which cuts both ways: more room to re-rate if inference demand inflects, but less capital, brand, and supply depth than [[render-token|Render]] or [[akash-network|Akash]]. Its no-dilution supply is a genuine structural differentiator versus IO and AKT, whose unlock/emission schedules add persistent sell pressure.

## How & Where It Trades

- **Spot venues.** NOS is an SPL token traded on a handful of centralized exchanges (Kraken, Crypto.com) and Solana DEXs (Orca) — see the Exchange Listings section. Concentration on a few venues means liquidity is shallow and depends heavily on Solana-ecosystem flow.
- **Derivatives.** No deep, liquid NOS perpetual-futures market exists at this size; price discovery is spot-driven, so the token cannot be easily hedged and is prone to gap moves.
- **Float / liquidity.** With supply fully circulating there is **no unlock overhang**, but the ~$28M cap and modest 24h volume (sub-$0.4M in the snapshot) mean large orders move price materially. Treat NOS as a thin small-cap.

## Narrative, Category & Catalysts

NOS sits at the intersection of two of the strongest crypto narratives of the 2024–2026 cycle — **AI** and **DePIN** — plus the **Solana ecosystem** beta. That makes it a high-beta expression: in risk-on AI rallies these tokens can move several-fold, and in risk-off tape they bleed faster than majors (the -19% week in the 2026-06-21 snapshot is a clean example, occurring against an Extreme-Fear backdrop). Plausible catalysts: demonstrable growth in paid inference volume / GPU utilization, new model-endpoint integrations, a broad Solana or AI-DePIN narrative rotation, or exchange listings deepening liquidity. The dominant de-rating risk is the AI-DePIN narrative cooling while real paying demand stays thin.

## History & Timeline

- **2021–2023** — Nosana launches as a CPU-based, crowd-sourced **CI/CD** (continuous-integration) platform on [[solana|Solana]].
- **2023-10-23** — NOS all-time low of **$0.0105** recorded.
- **2024-03-06** — NOS all-time high of **$7.83**, during the AI/DePIN narrative peak of that cycle.
- **2024–2025** — Nosana pivots from CI/CD to **GPU-powered AI inference**, the basis for its current "AI + DePIN" positioning.
- **2026-06-21** — Trades ~$0.281 (~97% below ATH) with a sharp -19% week amid market-wide Extreme Fear (per snapshot below).

## Risks

- **Demand realization** — the defining risk for all GPU DePIN: whether real, recurring, paying AI inference demand materializes versus speculative token flow; the -19% week underscores how fragile the narrative bid is.
- **Reliability / quality** — decentralized consumer/independent GPUs can lag centralized clouds on uptime, networking, and large-model serving, limiting enterprise adoption.
- **Verification gap** — host honesty rests on staking/reputation, not full cryptographic proof; a determined adversary could attempt to farm rewards without genuine computation.
- **Intense competition** — better-capitalized rivals ([[render-token|Render]], [[akash-network|Akash]], [[io|io.net]]) compete for the same supply and demand.
- **Solana dependence** — inherits Solana's reliability, congestion, and ecosystem risk.
- **Liquidity / size** — ~$28M cap small-cap with high volatility and slippage risk; no liquid derivatives to hedge.

## Trading Playbook

> *Educational context, not financial advice. NOS is a thin, high-beta small-cap.*

- **Regime awareness.** In the current **Established Bear Market / Extreme Fear** tape (Fear & Greed 21, BTC ~16% below its 200-day MA as of 2026-06-22), high-beta AI/DePIN small-caps like NOS tend to underperform majors and trend hard in both directions. The -19% snapshot week is characteristic — these names amplify risk-off moves.
- **Beta, not hedge.** NOS is effectively a leveraged bet on the AI-DePIN narrative *and* Solana beta. It rallies hardest when both are risk-on and bleeds fastest when they are not.
- **Liquidity discipline.** Size positions for thin books and wide spreads; assume meaningful slippage on entry/exit and that no perp market exists to hedge.
- **What to watch.** Genuine signals are utilization/usage growth and inference-demand traction, not price alone — the bull case requires fee revenue, not just narrative.

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `nosXBVoaCTtYdLvKY6Csb4AC8JCdQKKAaWYtx2ZMoo7` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | NOS/USD | N/A |
| Crypto.com Exchange | NOS/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | NOSXBVOACTTYDLVKY6CSB4AC8JCDQKKAAWYTX2ZMOO7/SO11111111111111111111111111111111111111112 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://nosana.io/](https://nosana.io/) |
| **Twitter** | [@nosana_ai](https://twitter.com/nosana_ai) |
| **Telegram** | [NosanaCI](https://t.me/NosanaCI) (12 members) |
| **Discord** | [https://discord.com/invite/nosana-ai](https://discord.com/invite/nosana-ai) |
| **GitHub** | [https://github.com/nosana-ci](https://github.com/nosana-ci) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $383,642.00 (Apr-2026 snapshot) |
| **Market Cap Rank** | #670 |
| **Current Price** | $0.281259 |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[solana]]
- [[depin]]
- [[decentralized-compute]]
- [[artificial-intelligence]]
- [[render-token]]
- [[akash-network]]
- [[io]]
- [[iexec-rlc]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no other specific wiki source ingested yet.

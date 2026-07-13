---
title: "SEDA"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, oracle, data-provider, defi]
aliases: ["SEDA", "Flux Protocol", "SEDA Protocol"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.seda.xyz/"
related: ["[[crypto-markets]]", "[[oracle]]", "[[cross-chain]]", "[[smart-contracts]]"]
---

# SEDA

**SEDA** (SEDA) is a modular, multi-chain [[oracle]] and data-transport network — a permissionless protocol for fetching, aggregating, and delivering any data type to [[smart-contracts]] across many blockchains. SEDA grew out of the earlier **Flux protocol** oracle project and rebranded to SEDA; it is unrelated to the FLUX/Flux decentralized-compute network (see [[zelcash|Flux (FLUX, compute/DePIN)]]), despite the shared legacy name. Its tagline is "any data type, for all networks."

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, SEDA trades at **$0.03083077** with a market capitalization of about **$22.94M**, ranking **#756**. It was **down 7.04%** over 24 hours and **down 8.94%** over 7 days — a notably weak week, underperforming as the broader market sat in Extreme Fear (Crypto Fear & Greed Index 22; BTC near $64,180).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SEDA |
| **Market Cap Rank** | #756 |
| **Market Cap** | ~$22.94M |
| **Current Price** | $0.03083077 |
| **24h Change** | -7.04% |
| **7d Change** | -8.94% |
| **Former Name** | Flux protocol (oracle; rebranded to SEDA) |
| **Categories** | Oracle, Modular Blockchain, Smart Contract Platform, Cross-Chain Data, Ethereum / Base / Osmosis / HyperEVM ecosystems |
| **Website** | [https://www.seda.xyz/](https://www.seda.xyz/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## History & Rebrand

SEDA originated as the **Flux protocol**, an oracle/data project, before rebranding to **SEDA** (its CoinGecko id is `seda-2`). This naming is a common source of confusion: SEDA's "Flux" heritage is entirely separate from the [[zelcash|FLUX/Flux decentralized-compute network]] covered elsewhere in this wiki. The rebrand accompanied a repositioning toward a modular, [[cross-chain]] data layer rather than a single-chain price feed.

---

## Architecture

SEDA is designed as a **modular oracle network** that separates data sourcing, aggregation, and on-chain settlement:

- **Data Request Network** — A decentralized network of operators (overlay nodes / executors) that pick up data requests, fetch the requested data from off-chain or on-chain sources, and reach consensus on a result.
- **Modular & multi-chain** — Rather than living on one chain, SEDA pushes verified results to many destination chains. Its contracts/deployments span the Ethereum, Base, Osmosis (Cosmos/IBC), and HyperEVM ecosystems, making it a [[cross-chain]] data layer.
- **Programmable data feeds** — Builders can define custom data requests ("any data type") via WASM-style logic, not just standard price feeds, so the network can serve prices, custom APIs, and arbitrary computations.
- **Crypto-economic security** — Operators are incentivized and slashable, aligning the [[oracle]] result with economic stake to deter manipulation.

### The data-request lifecycle

A typical SEDA flow runs: (1) a smart contract on a destination chain (Ethereum, Base, HyperEVM, or an Osmosis/IBC app) posts a **data request** specifying what to fetch and how to aggregate it; (2) overlay/executor nodes pick it up, each independently fetching from the specified sources; (3) the network **aggregates** the individual results (e.g., median/tally with outlier rejection) and reaches consensus on a single value; (4) the agreed result is **settled back** to the requesting chain with a proof, and honest operators are rewarded while provably-wrong ones can be slashed. Because the request logic is **programmable** (WASM-style "Oracle Programs"), SEDA can serve far more than price feeds — custom APIs, computations, and arbitrary data types — which is the core of its "any data type" pitch and its main differentiation from feed-templated oracles.

### Pull vs push design

Modern oracles split between **push** (the oracle proactively writes updates on-chain, like classic Chainlink price feeds) and **pull** (consumers request/pull a fresh value on demand, like Pyth). SEDA's data-request model is fundamentally **pull/request-driven and modular**, which suits app-chains and modular rollups that want to provision their own data on demand rather than rely on a fixed set of pre-deployed feeds. This is the same structural bet Pyth and RedStone made, and it is increasingly the dominant pattern for new chains.

---

## What the SEDA Token Does

- **Staking / security** — SEDA is staked by network operators to participate in resolving data requests; misbehavior is penalized.
- **Fees** — Data requests are paid for in SEDA (or routed through it), creating demand tied to oracle usage.
- **Governance** — Token holders participate in protocol governance and parameterization.

Note the token's supply profile: a large total/uncapped supply relative to circulating supply means future emissions/unlocks are a consideration for valuation.

---

## Distinguishing Features

- **Generality** — Positions itself as oracle infrastructure for *any* data type across *all* networks, contrasting with feed-specialized oracles.
- **Modularity** — Decouples the data-resolution layer from settlement, so it can serve modular and app-chain ecosystems.
- **Multi-ecosystem reach** — Native presence across EVM (Ethereum/Base/HyperEVM) and Cosmos/IBC (Osmosis).

---

## Comparison vs Oracle Peers

The oracle market is dominated by a few entrenched names. SEDA competes as a smaller, modular/pull-based "any data type" challenger.

| Project | Token | Model | Strength | SEDA's contrast |
|---|---|---|---|---|
| **SEDA** | SEDA | Modular, pull/request-driven, programmable data requests | Generality (any data type), multi-chain incl. Cosmos/IBC | The challenger being described here |
| **Chainlink** | LINK | Push price feeds + CCIP, services, off-chain compute | Dominant integrations, brand, enterprise reach | SEDA is far smaller; competes on flexibility, not footprint |
| **Pyth Network** | PYTH | Low-latency **pull** feeds sourced from first-party publishers | Fast price data, broad multichain, exchange-grade sources | Closest design cousin; Pyth is much larger and price-focused |
| **RedStone** | (token) | Modular oracle, on-demand "pull" data delivery | Modular DA-native delivery, LST/LRT price niche | Similar modular ethos; RedStone has strong LRT-collateral traction |
| **API3** | API3 | First-party dAPIs run by data providers (Airnode) | First-party data, OEV capture | Different security model (provider-run feeds) |

Takeaway: SEDA's design (modular, pull-based, programmable, multi-VM) is squarely in the modern oracle paradigm and most resembles Pyth/RedStone. Its problem is scale: Chainlink owns integrations and Pyth owns low-latency price data, so SEDA must win on *generality* and on serving modular/app-chain ecosystems the incumbents under-serve.

---

## How & Where SEDA Trades

- **Thin and lightly listed.** Per the CoinGecko data snapshot, SEDA shows **no major centralized-exchange listings**, so liquidity is concentrated on-chain and on smaller venues. This is the dominant trading-structure fact about the token: it is a low-liquidity micro-cap.
- **Multi-chain token, fragmented liquidity.** SEDA is deployed across **Osmosis (native, via IBC), Base, HyperEVM, and Ethereum**. Liquidity is split across these surfaces, which deepens slippage on any single venue. Osmosis (Cosmos DEX) is a natural on-chain trading home given the IBC-native deployment.
- **No meaningful derivatives.** There is no significant perp/futures market, so there is no funding-rate signal; risk can only be managed by size.
- **Trading implications** — At ~$23M cap with sub-$0.5M daily volume and few CEX rails, SEDA behaves like a thin infrastructure micro-cap: prone to gap moves, hard to exit in size, and highly sensitive to a single large holder. The **-9% week** into 2026-06-21 underperforming an already-weak market is characteristic.

---

## Narrative, Category & Catalysts

- **Category** — **Oracle / decentralized data infrastructure** with a **modular-blockchain** and **cross-chain** angle. Adjacent to the "modular DA + app-chain" thesis.
- **Catalysts** — New integrations (especially with modular rollups and Cosmos/IBC and HyperEVM apps that need custom data); a Tier-1 exchange listing that would materially deepen liquidity; expansion of the data-request menu beyond price feeds; and any broad rotation back into "real-yield infrastructure" narratives.
- **Headwind — incumbent moat.** Chainlink and Pyth set the default for new deployments; SEDA must convert its generality pitch into sticky integrations.
- **Headwind — regime & supply.** In an Established Bear with Fear & Greed at **21**, micro-cap infra de-rates, and SEDA's large/uncapped total supply versus circulating creates an emission/unlock overhang as tokens vest.

---

## History & Timeline

Only dated, verifiable milestones are listed.

| Date | Event |
|---|---|
| — | Project originates as the **Flux protocol** oracle/data project (predecessor) |
| (rebrand) | Repositions and rebrands to **SEDA** (CoinGecko id `seda-2`); pivots toward a modular, cross-chain data layer |
| 2025-11-02 | SEDA all-time high of **$0.2636** |
| 2026-03-27 | SEDA all-time low of **$0.0190** |
| 2026-06-21 | Trades ~$0.0308, ~91% below ATH, down ~9% on the week in Extreme Fear |

---

## Risks

- **Crowded oracle market** — Competes against entrenched incumbents (Chainlink, Pyth, RedStone, API3); winning oracle market share and integrations is difficult.
- **Weak recent price action** — Down ~9% on the week and far below its November 2025 all-time high (~$0.26), signaling fading momentum and thin liquidity.
- **Low liquidity / limited listings** — Modest 24h volume and few major centralized listings increase slippage and volatility.
- **Emission/unlock overhang** — Uncapped or large total supply versus circulating supply can pressure price as tokens vest.
- All figures other than the dated market snapshot are qualitative; node counts and throughput are not independently verified here.

---

## Overview

SEDA is a modular standard for data transport and querying — any data type, for all networks — delivering decentralized [[oracle]] results to [[smart-contracts]] across multiple chains.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 655.23M SEDA |
| **Total Supply** | 1.02B SEDA |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $22.93M |
| **Market Cap / FDV Ratio** | 0.64 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2636 (2025-11-02) |
| **Current vs ATH** | -91.47% |
| **All-Time Low** | $0.0190 (2026-03-27) |
| **Current vs ATL** | +18.05% |
| **24h Change** | +0.99% |
| **7d Change** | +13.26% |
| **30d Change** | +2.02% |
| **1y Change** | +3.87% |

---

## Platform & Chain Information

**Native Chain:** Osmosis

### Contract Addresses

| Chain | Address |
|---|---|
| Osmosis | `ibc/956AEF1DA92F70584266E87978C3F30A43B91EE6ABC62F03D097E79F6B99C4D8` |
| Base | `0x306acd0c07c430abbbb2e74ef7bde94f32a898c0` |
| Hyperevm | `0x4f96b683714377c38123631f2d17cdf18b3f46a7` |
| Ethereum | `0x14862c03a0caccc1ab328b062e64e31b2a1afcd7` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.seda.xyz/](https://www.seda.xyz/) |
| **Twitter** | [@sedaprotocol](https://twitter.com/sedaprotocol) |
| **Telegram** | [+AEmfJttwGHE4ODhi](https://t.me/+AEmfJttwGHE4ODhi) (3,745 members) |
| **Discord** | [https://discord.com/invite/seda](https://discord.com/invite/seda) |
| **GitHub** | [https://github.com/sedaprotocol](https://github.com/sedaprotocol) |
| **Whitepaper** | [https://docs.seda.xyz/seda-network](https://docs.seda.xyz/seda-network) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $420,053.00 |
| **Market Cap Rank** | #703 |
| **24h Range** | $0.0222 — $0.0234 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Playbook (Bear / Extreme-Fear Regime)

> Educational framing only — not investment advice. SEDA is a thinly-listed oracle micro-cap.

- **Regime first.** In an Established Bear with Fear & Greed at 21, illiquid infra micro-caps de-rate and bounces fail; the -9% week into 2026-06-21 (worse than the market) is the base-rate behavior.
- **Liquidity is the dominant risk.** With no major CEX rails and liquidity split across Osmosis/Base/HyperEVM/Ethereum, getting in or out in size is the hard part. Trade small, use limit orders, and pre-check the deepest pool (often Osmosis given IBC-native deployment).
- **It's a catalyst/integration story, not a momentum story.** The realistic long thesis is a re-rating on a concrete integration win or a Tier-1 listing that adds liquidity — discrete events, not trend. Absent those, treat rallies as mean-reversion to sell into.
- **Invalidation / risk control.** No derivatives to hedge; manage by size. Structural reference: the 2026-03 ATL ($0.0190) is the floor that matters — a break on volume signals continuation lower.
- **What would change the thesis** — major exchange listing(s), marquee oracle integrations on modular/app-chains, and a market-wide return of risk appetite for infrastructure tokens. None present as of 2026-06-22.

---

## See Also

- [[crypto-markets]]
- [[oracle]]
- [[cross-chain]]
- [[smart-contracts]]
- [[zelcash|Flux (FLUX) — unrelated decentralized-compute network]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge and the project's public documentation (seda.xyz / docs.seda.xyz); market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). No additional specific wiki source ingested yet.

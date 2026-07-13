---
title: "HyperEVM"
type: market
created: 2026-04-28
updated: 2026-06-20
status: excellent
tags: [crypto, defi, smart-contracts, ai-trading]
aliases: ["HyperEVM", "Hyperliquid EVM", "HL EVM"]
related: ["[[hyperliquid]]", "[[hypercore]]", "[[hyperbft]]", "[[hype]]", "[[hlp]]", "[[hyperliquid-hlp-basis-arbitrage]]", "[[hyperliquid-vault-architecture]]", "[[hip-3-builder-deployed-perps]]", "[[hyperliquid-api-and-sdk]]", "[[hyperliquid-order-book-microstructure]]", "[[crypto-markets]]", "[[2026-exploit-target-watchlist]]", "[[smart-contract-vulnerability-taxonomy]]", "[[ai-amplified-exploit-arbitrage]]", "[[hyperliquid-vs-dydx-vs-gmx]]", "[[clob]]"]
---

**HyperEVM** is the general-purpose EVM execution layer launched on top of [[hyperliquid|Hyperliquid's]] custom L1. Distinct from Hyperliquid's order-book matching engine and the HLP vault, HyperEVM is the **smart-contract environment** where third-party DeFi protocols can deploy. The [[2026-exploit-target-watchlist|exploit watchlist]] places HyperEVM in **Tier 1: Imminent Risk** because it is a recently-launched smart-contract environment running on centralized-operator infrastructure, with a single-team operator (Hyperliquid) and limited outside auditor diversity.

## Key facts

| Field | Detail |
|-------|--------|
| **Layer** | EVM execution environment on Hyperliquid L1 |
| **Operator** | Hyperliquid (single team) |
| **Status** | Recently launched (post-2025); details in flux |
| **Watchlist tier** | Tier 1: Imminent Risk |
| **Audit coverage** | L1 + HLP vault audited; HyperEVM is the newer surface |

## What HyperEVM is

Hyperliquid runs a custom L1 optimized for high-throughput perpetual order-book matching. The L1 originally exposed only the order-book primitives (place/cancel orders, settle, manage the [[hlp|HLP]] vault). HyperEVM extends the L1 with a **general-purpose EVM** — third-party protocols can deploy Solidity contracts that execute on Hyperliquid's chain, with potential composability into the order-book primitives.

Both [[hypercore|HyperCore]] and HyperEVM are **states of the same L1**, secured by the same consensus — Hyperliquid's [[hyperbft|HyperBFT]] (a HotStuff-derived BFT protocol) orders transactions for both layers. This is the architectural key: HyperEVM is not a separate sidechain bolted onto an exchange; it is a second execution environment sharing one validator set, one consensus, and one notion of finality with the order-book engine. That shared-consensus design is what makes the [[hypercore|HyperCore]] ↔ HyperEVM composability described below trustless within the chain (rather than a bridge between two systems), but it is also why the [[2026-exploit-target-watchlist|watchlist]] treats validator-set centralization as a risk that spans *both* layers at once.

This is a meaningful architectural step:

- **For Hyperliquid**: HyperEVM lets the ecosystem grow beyond the perp-DEX use case toward a full DeFi stack, capturing additional fee revenue and TVL.
- **For users**: HyperEVM offers near-CEX execution speed combined with EVM composability — potentially attractive for high-frequency strategies.
- **For risk**: HyperEVM is a brand-new smart-contract environment running on a chain whose validator/operator set is dominated by the Hyperliquid team. The combination of new code + centralized operator + emerging composability with the order book creates a distinct attack surface from HLP vault risk.

## Market structure: how contracts read HyperCore

The architectural fact that makes HyperEVM more than "just another EVM chain" is its tight integration with [[hypercore|HyperCore]] — the protocol-level engine that holds Hyperliquid's perp and spot order books, margining, and liquidations. The official architecture splits state execution into two components: **HyperCore** (fully on-chain order books) and **HyperEVM** (an Ethereum-like smart-contract environment that can access HyperCore's liquidity) (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]). The composability runs in this direction: smart contracts on HyperEVM can compose with the order-book liquidity living in HyperCore, using it as a building block rather than re-implementing matching.

| Layer | What it holds | What it exposes to the other layer |
|---|---|---|
| [[hypercore|HyperCore]] | Perp + spot [[clob\|order books]], margin, liquidations, funding | Liquidity, prices, margin/funding state that EVM contracts can read and trade against |
| **HyperEVM** | General-purpose Solidity contracts, DeFi protocols, vaults | Programmable logic that places/hedges positions against HyperCore's books |

For a contract developer, this means a DeFi protocol on HyperEVM can build on HyperCore's order books directly: a vault contract can read order-book depth, mark/oracle prices, and funding, then place or hedge positions on the perp markets as part of its own logic (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]). This is qualitatively different from a vanilla EVM where a "DEX" is itself a smart contract — here the deepest liquidity is a protocol primitive the EVM *reaches into*, not something it must bootstrap.

### What this enables

| Composable pattern | How it uses HyperCore |
|---|---|
| **Vaults** | Pool user capital in an EVM contract, deploy it as positions/quotes on HyperCore order books |
| **Structured products** | Encode a payoff (e.g., covered-call-like, principal-protected) that hedges via perp positions on the books |
| **Automated strategies** | On-chain bots that trade or hedge against the books from contract logic, not just from off-chain wallets |
| **Collateral / money markets** | Use HyperCore positions and balances as inputs to lending/borrowing logic |

The contrast with [[hip-3-builder-deployed-perps|HIP-3]] is worth noting: HIP-3 extends HyperCore's *order books themselves* to permissionless deployers (new markets, same matching engine), whereas HyperEVM extends Hyperliquid with a *smart-contract layer* that composes with those books. Both inherit HyperCore's performance, from different directions.

> Specific precompiles, bridge primitives, and read/write interfaces between HyperEVM and HyperCore state are documented in the Hyperliquid developer docs and change between releases — verify against the primary docs (see **Sources**) and the [[hyperliquid-api-and-sdk]] page before building.

## Gas, fees, and the HYPE relationship

HyperEVM does **not** have its own token — the ecosystem token is **[[hype|HYPE]]**, and HyperEVM is one of the things that gives HYPE utility beyond the order book. The relationship runs along several channels:

| Channel | How HYPE relates to HyperEVM |
|---|---|
| **Gas / execution** | Transactions and contract execution on HyperEVM consume gas denominated in HYPE — the same asset that secures the chain — so EVM activity is a direct demand source for HYPE |
| **Shared security** | HyperEVM is secured by the same [[hyperbft|HyperBFT]] validator set and HYPE-aligned economics as [[hypercore|HyperCore]]; there is no separate "HyperEVM token" to bootstrap |
| **Fee/value flows** | Hyperliquid fees are directed to the community ([[hlp|HLP]], an assistance fund, deployers) rather than middlemen — as HyperEVM activity grows it adds to the fee base that accrues to the ecosystem (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]) |
| **Roadmap weighting** | The roadmap's stated focus includes **expanding the HyperEVM ecosystem** and establishing Hyperliquid as default liquidity infrastructure as finance moves on-chain (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]) |

The practical consequence for a HYPE holder: HyperEVM is a **second demand vector** layered on top of perp-trading fees. If the EVM ecosystem attracts TVL and transaction volume, that activity is denominated in and settled with HYPE, broadening HYPE's role from "exchange token" toward "gas + settlement asset of an L1." Conversely, HyperEVM adoption that fails to materialize leaves HYPE valued primarily on the perp-DEX business. HYPE itself launched at genesis in late November 2024 (~$3 initial); the roadmap targets full decentralization alongside HyperEVM expansion (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]). For HYPE's own market data and tokenomics, see [[hype]].

## Ecosystem traction (qualitative)

The investment case for HyperEVM rests on whether real DeFi protocols deploy and attract liquidity, not on the architecture alone. As a recently launched environment (post-2025), traction should be read **qualitatively** and verified against live data before relying on it:

| Signal | What to watch | Where to verify |
|---|---|---|
| **TVL growth** | Total value locked in HyperEVM protocols vs. the rest of the Hyperliquid ecosystem | DeFiLlama Hyperliquid page |
| **Protocol diversity** | Lending/money markets, DEXs/AMMs, vaults, structured products, stablecoins deploying on HyperEVM | DeFiLlama, project announcements |
| **Composability usage** | Vaults/contracts that actually read [[hypercore\|HyperCore]] state and trade the books (the differentiated use case), not just generic EVM apps | On-chain activity, project docs |
| **Builder activity** | Deployments via the EVM vs. order-book extensions via [[hip-3-builder-deployed-perps\|HIP-3]] | Hyperliquid docs, ecosystem trackers |

The strategic framing: HyperEVM lets the Hyperliquid ecosystem grow beyond the perp-DEX into a **full DeFi stack** that composes with [[hypercore|HyperCore]] liquidity — the application layer to HyperCore's liquidity layer. The two extension paths are complementary: [[hip-3-builder-deployed-perps|HIP-3]] widens the *order books* themselves (permissionless new markets on the same matching engine), while HyperEVM widens the *programmable surface* around those books. Both inherit HyperCore performance and [[hyperbft|HyperBFT]] security; the open question is whether enough builders choose HyperEVM over established EVM L2s given Hyperliquid's single-operator trust model.

## Trading relevance

| Why a trader cares | Detail |
|---|---|
| **On-chain vaults that trade the books** | Strategy capital can be deployed via HyperEVM contracts that quote/hedge on HyperCore — the smart-contract analog of running a bot via the [[hyperliquid-api-and-sdk\|native API/SDK]] |
| **Structured-product exposure** | Payoffs hedged against perp books become available as composable on-chain primitives |
| **New surface, new risk** | A new smart-contract layer composing with order-book state is a distinct attack surface (see watchlist below) |
| **Where to read state** | Live order-book/margin/funding state is read via [[hyperliquid-api-and-sdk]]; deep microstructure questions are in [[hyperliquid-order-book-microstructure]] |

## Distinction from HLP vault and order book

- **Hyperliquid order book ([[hypercore|HyperCore]])** — the matching-engine layer. Audited; battle-tested by perpetual-DEX volume since 2023.
- **[[hlp|HLP]] vault** — the protocol-owned liquidity vault that market-makes the order book. Audited; concentrates LP risk but conceptually well-understood. See [[hyperliquid-hlp-basis-arbitrage]] for the basis-trade strategy.
- **HyperEVM** — the new general-purpose smart-contract layer. Distinct attack surface; less battle-testing.

All three share one consensus ([[hyperbft|HyperBFT]]) and one token ([[hype|HYPE]]). A protocol exploit on HyperEVM (e.g., a third-party DeFi protocol deployed there) would not necessarily affect [[hlp|HLP]] or the order book — but **a bug in HyperEVM itself** (the runtime, the precompiles, the bridging primitives between EVM state and order-book state) could cascade into HLP and order-book trust assumptions because they are not isolated systems but co-resident states of the same chain.

## Watchlist concerns

Per [[2026-exploit-target-watchlist]]:

| Concern | Detail |
|---------|--------|
| **Newly launched smart-contract environment** | HyperEVM is recent; ecosystem deployments are early-stage with thin audit coverage |
| **Centralized operator infrastructure** | Hyperliquid validators are dominated by the project team; this is a different trust model from Ethereum L1 or major L2s |
| **Single-team, no major outside auditor diversity** | The audit firms covering HyperEVM are a smaller set than the firms covering Aave, Compound, or other deeply-audited protocols |
| **Composability with order-book primitives** | If HyperEVM contracts can interact with HLP vault state or order-book state, the attack surface is larger than a vanilla EVM |

Concrete risk vectors to watch:

- **EVM-to-order-book bridge bugs.** Any primitive that lets HyperEVM contracts read or write order-book state is a security boundary; bugs in that boundary could let a HyperEVM contract drain order-book liquidity.
- **HLP vault depeg from HyperEVM contagion.** If a third-party HyperEVM protocol fails dramatically, sympathy depeg pressure on HLP.
- **Validator-set centralization risk.** A compromise of Hyperliquid's validator infrastructure (operationally, not cryptographically) would affect both order-book and HyperEVM trust.

## Trader-side implications

For pre-positioning hedges (per [[ai-amplified-exploit-arbitrage]]):

- **HYPE token cheap-to-carry short.** Modest size; covers any HyperEVM-class incident that hits HYPE pricing.
- **HLP vault depeg watch.** Most likely channel for a HyperEVM-class incident to affect tradable pricing is HLP depeg from underlying. Monitor HLP NAV vs underlying assets; depeg above 0.5% on liquidity-rich windows is a buy signal in the [[hyperliquid-hlp-basis-arbitrage|basis-arb]] framework but a sell signal if accompanied by exploit reports.
- **Sector rotation on hits.** A HyperEVM-class exploit would drive flow to dYdX (Cosmos), GMX (Arbitrum), Drift (Solana — though see [[2026-04-01-drift-protocol-exploit|Drift's own exploit]]), and other perp DEXs. Pre-position by maintaining the long-perp-DEX-basket / short-Hyperliquid pair.
- **Wait on first incident.** HyperEVM has not yet had a public Tier-1 exploit event as of late April 2026. The first such event will be informationally important — both for the trade and for setting the post-incident norms (does Hyperliquid validator-freeze stolen funds Cetus-style? Does it socialize losses across HLP holders?).

## Open items to expand

This page covers HyperEVM's architecture (composability with [[hypercore|HyperCore]]), trading relevance, and the [[2026-exploit-target-watchlist|watchlist's]] Tier 1 risk framing. Still worth ingesting as primary docs and reports become available:

- Concrete launch date and version history.
- Specific HyperEVM precompiles and bridging primitives between EVM state and order-book state.
- Audit-firm coverage detail (which firms, what scope, when).
- Validator-set composition.
- Ecosystem deployments (which third-party DeFi protocols are live on HyperEVM).
- Public bug-bounty details if any.

## Related

- [[hyperliquid]] — parent entity
- [[hypercore]] — the order-book engine HyperEVM composes with
- [[hyperbft]] — the shared BFT consensus securing both HyperCore and HyperEVM
- [[hype]] — ecosystem token; gas/settlement asset for HyperEVM (no separate HyperEVM token)
- [[hlp]] — protocol-owned liquidity vault sharing the chain with HyperEVM
- [[hip-3-builder-deployed-perps]] — the other extension of HyperCore (permissionless markets)
- [[hyperliquid-api-and-sdk]] — how to read live HyperCore state
- [[hyperliquid-order-book-microstructure]] — book behavior contracts trade against
- [[hyperliquid-hlp-basis-arbitrage]] — HLP-vault trader strategy
- [[hyperliquid-vault-architecture]] — vault structure on Hyperliquid
- [[hyperliquid-vs-dydx-vs-gmx]] — comparative analysis
- [[2026-exploit-target-watchlist]] — Tier 1 ranking source
- [[smart-contract-vulnerability-taxonomy]] — vuln-class index
- [[ai-amplified-exploit-arbitrage]] — hub strategy
- [[clob]] — central-limit-order-book concept

## Sources

- (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]) — HyperCore/HyperEVM split, composability, roadmap, fee flows
- [[2026-exploit-target-watchlist]] — Tier 1 ranking and risk framing
- Hyperliquid public documentation — https://hyperliquid.gitbook.io/hyperliquid-docs
- DeFiLlama TVL data on Hyperliquid ecosystem

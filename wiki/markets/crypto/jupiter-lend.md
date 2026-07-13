---
title: "Jupiter Lend"
type: market
created: 2026-04-28
updated: 2026-04-28
status: draft
tags: [crypto, defi, solana, lending]
aliases: ["Jupiter Lend", "JupLend", "jupUSD"]
related: ["[[jupiter-exchange-solana]]", "[[solana]]", "[[crypto-markets]]", "[[2026-exploit-target-watchlist]]", "[[smart-contract-vulnerability-taxonomy]]", "[[ai-amplified-exploit-arbitrage]]", "[[oracle-manipulation]]", "[[donation-attacks]]", "[[2026-04-01-drift-protocol-exploit]]"]
---

**Jupiter Lend** is the lending and money-market product of the [[jupiter-exchange-solana|Jupiter]] DeFi stack on [[solana|Solana]]. Distinct from the Jupiter Exchange (the dominant Solana DEX aggregator), Jupiter Lend launched in **August 2025** and reached **$1.65B TVL** by Q1 2026 — described in the [[2026-exploit-target-watchlist|exploit watchlist]] as the "fastest-growing money market in DeFi history". The fast TVL ramp combined with relatively thin audit coverage relative to that growth places Jupiter Lend in **Tier 1: Imminent Risk** on the watchlist; the page exists primarily to document that risk surface for traders pre-positioning hedges per [[ai-amplified-exploit-arbitrage]].

## Key facts

| Field | Detail |
|-------|--------|
| **Product** | Lending / money market |
| **Parent ecosystem** | Jupiter (Solana DEX aggregator stack) |
| **Native chain** | [[solana\|Solana]] |
| **Launched** | August 2025 |
| **TVL (Q1 2026)** | ~$1.65B |
| **Watchlist tier** | Tier 1: Imminent Risk |
| **Stable product** | jupUSD (Ethena white-label, multi-chain) |

## Why the watchlist flags it

The [[2026-exploit-target-watchlist|watchlist]] places Jupiter Lend in Tier 1 on three axes:

1. **TVL × loss-elasticity.** $1.65B TVL is large, and concentration in a single lending protocol's contracts means an exploit could affect the full TVL rather than a fraction.
2. **Code novelty.** Solana-native lending architecture, integrated with Jupiter's existing aggregation infrastructure. New architecture that hasn't accumulated multi-year battle-testing.
3. **Audit gap.** Audit coverage is thin relative to the speed of TVL growth — the protocol's TVL ramp outpaced the depth of public audit-firm coverage.

The watchlist also notes Jupiter Lend's **jupUSD stable** as part of the Ethena white-label cluster (alongside USDm, suiUSDe), with combined supply >$100M in Q1 2026. Multi-chain rapid deployment with thin per-deployment audit coverage is itself a watchlist concern.

## Distinction from Jupiter Exchange

- **[[jupiter-exchange-solana|Jupiter Exchange]]** is the dominant Solana DEX aggregator — routing trades across SPL token pairs and major Solana DEXs (Orca, Raydium, Phoenix, Meteora). Mature product; trade-routing logic.
- **Jupiter Lend** is a separate, newer product: a money market for borrowing and lending Solana-native assets. Different code surface, different risk profile.

The two share branding and likely share some governance / treasury infrastructure, but they are distinct products with distinct exploit risks. Conflating them in a wiki entry was a documentation gap that this page resolves.

## jupUSD (Ethena white-label)

Jupiter Lend's jupUSD is part of the Ethena white-label synthetic stablecoin family — protocols that use Ethena's delta-neutral basis-trade mechanism (long spot ETH/SOL/etc + short perp) to back a stablecoin issued under their own brand. Other examples: USDm, suiUSDe.

The shared mechanism means:

- **Same mechanism risk.** If Ethena's delta-neutral basis trade breaks (sustained negative perp funding, exchange counterparty failure, liquidity dislocation in the underlying perp markets), jupUSD has the same exposure as sUSDe.
- **Multi-chain coordination risk.** Each white-label deployment is its own contract surface; per-deployment audit coverage varies.
- **Sympathy-depeg correlation.** A depeg event on any Ethena white-label tends to drag the others. See [[2026-04-kelp-stable-sympathy-depeg]] for the canonical sympathy-depeg trade structure.

## Trader-side implications

For pre-positioning hedges (per [[ai-amplified-exploit-arbitrage]] and [[2026-exploit-target-watchlist]]):

- **Cheap-to-carry shorts** on JUP token (Jupiter governance token) at low size as a tail-hedge. JUP is liquid on multiple CEXs and Hyperliquid; carry cost is bearable.
- **jupUSD depeg watch.** Sympathy-depeg trades on jupUSD if a related Ethena white-label depegs first; pair with USDe/sUSDe.
- **Solana DeFi sector rotation.** A Jupiter Lend exploit would cascade through Solana DeFi (similar to the [[2026-04-01-drift-protocol-exploit|Drift]] response). Pre-position by maintaining short Solana DeFi basket / long EVM perp DEXs as a relative-value hedge.
- **Donation-attack scan.** While Solana lending architecture differs from Compound v2, related accounting-attack patterns ([[donation-attacks|donation attacks]]) can apply to any vault-share-based lending model. AI scanners likely cover Jupiter Lend's surface; cheap-to-carry shorts size for tail.
- **Oracle-source dependency.** A Solana-based lending protocol pricing collateral against on-chain Solana DEX prices is exposed to [[oracle-manipulation|oracle manipulation]] in the Mango-class pattern. Audit coverage of oracle-source aggregation should be specifically interrogated.

## Status

Jupiter Lend is currently a **stub-grade page** — created to disambiguate from Jupiter Exchange and to document the watchlist's Tier 1 ranking. Expand with:

- Concrete contract addresses for jupUSD, jupSOL, jupBTC borrow markets.
- Audit coverage detail (firms, dates, scope).
- Oracle-source detail (Pyth? Chainlink? Self-source?).
- Multi-sig / governance signer composition.
- Recent TVL composition (which assets, what concentration).

These should be ingested as Solana DeFi data sources are added.

## Related

- [[jupiter-exchange-solana]] — sibling product (DEX aggregator)
- [[solana]] — host chain
- [[2026-exploit-target-watchlist]] — Tier 1 ranking source
- [[smart-contract-vulnerability-taxonomy]] — relevant vuln classes
- [[oracle-manipulation]] — adjacent risk vector
- [[donation-attacks]] — adjacent risk vector
- [[ai-amplified-exploit-arbitrage]] — hub strategy
- [[2026-04-01-drift-protocol-exploit]] — Solana DeFi sympathy-rotation precedent

## Sources

- [[2026-exploit-target-watchlist]] — Tier 1 ranking and TVL figure (Q1 2026)
- Solana DeFi public dashboards (DeFiLlama TVL data)

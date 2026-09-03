---
title: "AsterDEX"
type: entity
created: 2026-09-03
updated: 2026-09-03
status: good
tags: [exchange, crypto, derivatives, defi, hyperliquid, perpetual-futures, bnb]
entity_type: exchange
aliases: ["Aster", "ASTER", "Aster DEX", "Astherus"]
founded: 2025
website: "https://www.asterdex.com"
related: ["[[hyperliquid]]", "[[asterdex-perp-trading-map]]", "[[hyperliquid-vs-asterdex-vs-tiger-brokers]]", "[[cryptodataapi-exchanges]]", "[[perpetual-futures]]", "[[aster-2]]", "[[bnb-chain]]", "[[funding-rate]]", "[[liquidation]]"]
---

# AsterDEX

**AsterDEX** (brand: **Aster**, ticker **ASTER**) is a decentralized, multi-chain perpetual-futures exchange that runs both a transparent order-book mode and a "Simple Mode" offering extreme leverage. It differentiates on **hidden orders** (dark-pool-style execution invisible until fill) and **yield-bearing collateral** (USDF, asBNB), positioning it as the privacy- and capital-efficiency-focused counterpart to [[hyperliquid|Hyperliquid]]'s fully transparent book. This page is the entity/venue reference; for the full strategy treatment see [[asterdex-perp-trading-map]], and for a head-to-head comparison see [[hyperliquid-vs-asterdex-vs-tiger-brokers]].

## Key Facts

| Metric | Value |
|---|---|
| Formed | December 2024 merger of APX Finance and Astherus |
| Rebranded / launched as "Aster" | March 2025 |
| Headquarters | Decentralized (no fixed HQ; entity backed by YZi Labs) |
| Backing | YZi Labs (formerly Binance Labs); CZ (Changpeng Zhao) an advisor and personal investor |
| Products | Perpetual futures (crypto + promotional zero-fee US stock perps), spot, yield-bearing collateral |
| Chains | BNB Chain (majority of volume), Ethereum, Arbitrum, Solana, plus its own Aster Chain L1 |
| Max leverage | Up to 1001x (Simple Mode); lower on Pro/order-book mode |
| KYC | Not required |
| Custody | Self-custody |

CryptoDataAPI's own venue directory (see below) independently profiles AsterDEX as `kind: DEX`, `founded: "2024"`, `based: "On-chain (multi-chain)"` — the "2024" reflects the APX Finance/Astherus merger date rather than the March 2025 "Aster" brand launch; this page treats the merger and rebrand as two distinct, both-documented milestones rather than picking one as "the" founding date.

## Formation & Backing

AsterDEX did not launch from scratch — it is the product of a **December 2024 merger** between two pre-existing projects: **APX Finance**, an on-chain perpetuals platform live since 2021 with a reported cumulative volume in the hundreds of billions of dollars, and **Astherus**, a multi-asset liquidity/yield hub. In **March 2025**, the combined entity rebranded from "Astherus" to **Aster**, launching the unified AsterDEX product. The project is backed by **YZi Labs** (the rebranded former Binance Labs), and **CZ has publicly acted as an advisor and a personal investor**, which the wiki's existing [[asterdex-perp-trading-map|strategy map]] notes at "$2.5M+ in ASTER." AsterDEX's own Aster Chain L1 mainnet followed in March 2026.

## Fee Schedule

AsterDEX's headline differentiator versus Hyperliquid is aggressively low — in places zero — maker fees, though the exact schedule has moved over time and across modes; treat specific basis-point figures as a snapshot rather than a permanent quote:

| Mode / Tier | Maker | Taker | Notes |
|---|---|---|---|
| Pro Mode (order book) | As low as 0% (maker fees zeroed on USDT-margined perps as of early 2026 per third-party trackers) | ~0.035–0.04% | Among the lowest in the perp-DEX space; [[asterdex-perp-trading-map]] cites 0.005–0.01% maker in an earlier snapshot |
| USD1-margined perps | 0% | ~0.005% | A separate, even-cheaper collateral track per third-party fee trackers |
| Simple Mode (up to 1001x) | ~0.08% | ~0.08% | Flat, higher fee reflecting the extreme-leverage retail product |
| VIP tiers | Scales down with 14-day rolling volume | Down to ~0.025% at the top tier | Additional 5% discount for paying fees in ASTER |

**Do not treat any single number above as current** — AsterDEX has changed its fee schedule multiple times since 2025 (e.g., a maker-fee cut reported for early February 2026); verify against AsterDEX's own fee page before sizing a strategy around a specific basis-point assumption.

## Execution Mechanics Relevant to Arbitrage and Liquidations

### Hidden Orders (Dark-Pool Execution)

AsterDEX's Pro Mode supports **fully hidden limit orders** — size and price are invisible on the public book until the order fills. This is the single largest structural difference from Hyperliquid's fully transparent book: it removes visible-order MEV front-running for large positions, at the cost of degrading order-flow signals (tape reading, footprint charts, absorption analysis) that depend on seeing the whole book. See [[asterdex-perp-trading-map]] Strategy 4 and Strategy 7 for the arbitrage and mean-reversion implications.

### Leverage and Liquidation Density

Simple Mode's up to 1001x leverage means a ~0.1% adverse price move can trigger liquidation on the most extreme positions. Combined with hidden orders (which obscure the resting liquidity that would otherwise be visible during a cascade), this produces liquidation clusters that are denser and faster-unwinding than on 40-50x-capped venues like Hyperliquid — see [[asterdex-perp-trading-map]] Strategy 8 for the mechanics and [[liquidation]] for the general framework.

### Multi-Chain Architecture

AsterDEX deploys across BNB Chain (majority of volume), Ethereum, Arbitrum, and Solana, plus its own Aster Chain L1 — versus Hyperliquid's single custom L1. This broadens access without bridging but multiplies smart-contract attack surface (each chain deployment is a separate contract) and opens AsterDEX-internal cross-chain funding-rate dispersion as a structural, if unproven, opportunity (see [[asterdex-perp-trading-map]] Strategy 2).

### Yield-Bearing Collateral

Traders can post **USDF** (a yield-bearing stablecoin backed by delta-neutral DeFi strategies) or **asBNB** (a liquid-staking token) as margin, earning yield on collateral that sits idle on most other venues. This improves the economics of delta-neutral funding-rate carry but introduces a **collateral-value risk layer** distinct from standard USDC/USDT margin — see [[asterdex-perp-trading-map]] Strategy 1 and Strategy 9 for the mechanism and the correlated-failure risk during a systemic DeFi stress event.

### Notable for Arbitrage

- **Hidden-order accumulation** — institutional-size positions (>$100K notional) can be built without visible-order front-running, an execution edge distinct from any predictive edge
- **Cross-chain funding dispersion** — the same instrument trading across four chains may carry different funding prints per chain if liquidity is not fully pooled; unverified but structurally plausible given differing user bases per chain
- **Liquidation cascade trading** — the combination of extreme leverage tiers and hidden resting liquidity makes cascades sharper but harder to read in real time than on a fully transparent book
- **Zero/near-zero fee windows** — promotional zero-fee stock perps and near-zero crypto maker fees at various points have made grid and high-turnover strategies materially cheaper to run than on fee-charging competitors, though these promotions are not permanent

## What Could Not Be Verified

- **Exact current fee schedule** — third-party trackers disagree on specific basis-point figures and AsterDEX has changed fees multiple times since 2025; the table above is a directional snapshot, not a quote to trade on
- **Current TVL, open interest, and volume figures** — these move materially month to month for a young, incentive-sensitive perp DEX; see [[asterdex-perp-trading-map]] for a dated Q1 2026 snapshot and CryptoDataAPI's live endpoints below for current figures
- **A single "founded" date** — sources reasonably describe AsterDEX as either a December 2024 merger, a March 2025 rebrand/launch, or (per CryptoDataAPI's exchange directory) simply "2024"; this page reports all three rather than asserting one

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/exchanges/asterdex` — venue profile: `kind`, `focus[]`, `specs` (instruments, max_leverage, KYC, custody), no API key required (see [[cryptodataapi-exchanges]])
- `GET /api/v1/exchanges?referral_only=true` — filters the venue directory to partner-link venues only

```bash
curl "https://cryptodataapi.com/api/v1/exchanges/asterdex"
```

Auth: none required for the Exchanges category. Endpoint catalog: [[cryptodataapi-exchanges]]. See also [[cryptodataapi]].

AsterDEX itself is not yet a first-class venue in CryptoDataAPI's derivatives/funding/OI feeds the way Hyperliquid is (see [[cryptodataapi-hyperliquid]] for that venue's full live+historical coverage); CryptoDataAPI's liquidation feed does ingest AsterDEX force-orders where available per the exchange directory's own description.

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] researching or routing to AsterDEX can:

- **Venue discovery** — `GET /api/v1/exchanges/asterdex` to pull current `specs` (leverage cap, custody, KYC) before recommending the venue for a given strategy or trader profile, rather than relying on a static write-up
- **Cross-venue comparison** — `GET /api/v1/exchanges` (all venues) to compare AsterDEX's `specs.max_leverage` and `kind` against [[hyperliquid]] and other listed DEXes programmatically
- **Regime gate** — since AsterDEX's own market data is not yet in CryptoDataAPI's Hyperliquid-parity feeds, cross-reference [[hyperliquid]]'s BNB/ETH/BTC perp data (`GET /api/v1/hyperliquid/summary`) as the nearest liquid proxy when AsterDEX-specific data is unavailable
- **Strategy map** — apply the [[asterdex-perp-trading-map]] decision framework (structural edge → regime → size → counterparty check) before selecting one of its 11 documented strategies

## Related

- [[hyperliquid]] — the transparent-book perp-DEX benchmark AsterDEX is most often compared against
- [[asterdex-perp-trading-map]] — full strategy treatment: funding arb, hidden-order accumulation, liquidation cascade trading, kill criteria
- [[hyperliquid-vs-asterdex-vs-tiger-brokers]] — three-way platform comparison including a regulated broker
- [[cryptodataapi-exchanges]] — the venue-directory API this page's data section cites
- [[aster-2]] — redirect stub for the CoinGecko `aster-2` token slug, now resolving here
- [[bnb-chain]] — the chain carrying the majority of AsterDEX's trading volume
- [[perpetual-futures]] — the underlying instrument
- [[funding-rate]], [[liquidation]] — mechanics referenced above

## Sources

- https://cryptodataapi.com/api/docs and live `GET /api/v1/exchanges/asterdex` response (fetched 2026-09-03)
- [[asterdex-perp-trading-map]] — existing wiki treatment (formation, backing, key metrics, fee snapshots)
- [[hyperliquid-vs-asterdex-vs-tiger-brokers]] — existing wiki comparison page
- APX Finance x Astherus merger announcement, December 2024 (Medium, apx-finance)
- "Aster Emerges: Astherus Rebrands to Lead Decentralized Perpetual Trading," The Block / CryptoSlate / FinSMEs, March 2025
- Third-party fee trackers (Bitsgap, exchange-compare.com, dexcexhub.com), 2026 — AsterDEX fee schedule snapshots; treated as directional, not authoritative, per the hedges above

---
title: "Moonwell"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, lending]
aliases: ["WELL", "Moonwell Artemis", "Moonwell Apollo"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://moonwell.fi"
related: ["[[crypto-markets]]", "[[lending]]", "[[base]]", "[[defi]]", "[[governance-token]]", "[[compound]]", "[[aave]]", "[[liquidity]]"]
---

# Moonwell

**Moonwell** (WELL) is an open, non-custodial [[lending|lending and borrowing]] protocol — a Compound-style money market — deployed on **[[base|Base]]** and **Moonbeam**. Users supply crypto assets to earn yield and can borrow against their collateral, all governed by transparent on-chain interest-rate and risk parameters. **WELL** is the protocol's [[governance-token|governance token]]. (The protocol's flagship Moonbeam deployment was historically known as **Moonwell Artemis**, built on code derived from the earlier Moonwell Apollo deployment.)

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* WELL: $0.00369769, rank #896, market cap $16,687,251, 24h -2.46%, 7d +1.26%. Market backdrop: Fear & Greed Index at 21 (Extreme Fear).

As of 2026-06-22, WELL traded at **$0.00369769**, ranked **#896** by market capitalization with a market cap of approximately **$16.69M**. The token was one of the steadier names in the set — **-2.46% over 24 hours** but still **+1.26% over the trailing 7 days**, modestly outperforming on the week during an "Extreme Fear" tape (Fear & Greed 21). It remains well below its 2022 all-time high, in line with the broader compression of DeFi-token valuations.

---

## What Moonwell Does

Moonwell is a decentralized money market in the mold of [[compound|Compound]] and Aave. Its two core functions are:

- **Supplying / lending** — users deposit assets into pooled markets and earn variable interest paid by borrowers; deposits are represented by interest-bearing receipt tokens.
- **Borrowing** — users borrow assets against supplied collateral, subject to per-asset collateral factors. Positions that fall below required collateralization are liquidated to keep the protocol solvent.

Interest rates adjust algorithmically based on each market's utilization (the ratio of borrowed to supplied funds), so rising demand to borrow pushes both borrow and supply rates higher. Moonwell emphasizes a user-friendly experience and fast, low-cost transactions, which fits well with its strong presence on the low-fee [[base|Base]] L2.

---

## Mechanism and Architecture

- **Compound-style markets** — each supported asset has its own pool with a collateral factor, reserve factor, and a utilization-based interest-rate model. This is the canonical over-collateralized [[lending]] design.
- **Over-collateralization and liquidations** — borrowers must keep collateral value above a threshold; liquidators repay unhealthy positions in exchange for a discount on the seized collateral, protecting lenders.
- **Multi-chain deployment** — Moonwell runs on Base (its primary growth chain) and Moonbeam. The historical Artemis (Moonbeam) deployment reused audited code from the earlier Apollo deployment.
- **Security posture** — the protocol has emphasized multi-signature controls on contracts, third-party audits (e.g., Halborn), and a bug-bounty program (Immunefi). As always, audits reduce but do not eliminate smart-contract risk.

### Interest-rate model in depth

Like [[compound|Compound]], each Moonwell market sets rates from a **utilization curve**. Utilization `U = borrows / (cash + borrows)`. The borrow rate follows a **kinked (two-slope) model**: below an "optimal" utilization (the kink) rates rise gently; above it they rise steeply to incentivize repayment and new deposits and to protect lender liquidity. The supply rate is the borrow rate × utilization × (1 − reserve factor) — i.e., suppliers earn the interest borrowers pay, minus the slice routed to protocol reserves. This means **supply APY scales with how heavily a market is borrowed**, and a market near 100% utilization both pays high yield and risks withdrawal illiquidity.

### Worked example (illustrative)

A supplier deposits **$10,000 of USDC** into a Moonwell market with a 75% collateral factor:

1. They receive interest-bearing receipt tokens and begin earning the market's supply APY plus any WELL incentive rewards.
2. They can borrow up to **$7,500** of another asset (75% collateral factor) against the deposit — but borrowing to the limit leaves no buffer.
3. A safer borrow of **$4,000** keeps the position well-collateralized. If the borrowed asset's price rises or the collateral falls enough that the borrow exceeds the liquidation threshold, a **liquidator** repays part of the debt and seizes collateral at a discount (the liquidation incentive).
4. Net economic position: the supplier earns yield on $10,000 while accessing $4,000 of liquidity without selling the collateral. *(Illustrative; live collateral factors and rates per protocol.)*

---

## Token Role: WELL

WELL is Moonwell's [[governance-token|governance token]] and incentive asset:

- **Governance** — WELL holders vote on protocol parameters, new markets, collateral factors, and treasury decisions, typically through on-chain governance.
- **Incentives / liquidity mining** — WELL is distributed to suppliers and borrowers to bootstrap and retain liquidity across markets.
- **Staking / safety alignment** — staking mechanisms can align long-term holders with protocol health.

WELL has a high circulating-to-max-supply ratio (most of its 5B max supply already in circulation), so future emission-driven dilution is comparatively limited versus newer DeFi tokens.

### Governance & value accrual in depth

- **stkWELL safety module** — Moonwell adopted an Aave-style **safety-module staking** design: holders stake WELL into stkWELL to earn rewards and, critically, to act as a **backstop** that can be slashed to cover protocol shortfalls (bad debt). This aligns long-term holders with protocol solvency and gives WELL a direct, if contingent, role in risk-bearing.
- **Reserve factor → treasury** — a portion of borrower interest is diverted to protocol reserves, building a treasury that WELL governance controls.
- **Cross-chain governance** — WELL governs deployments on both [[base|Base]] and Moonbeam; proposals cover new markets, collateral factors, reserve factors, interest-rate parameters, and incentive emissions. Because parameters like collateral factors directly determine bad-debt risk, governance quality is a core safety variable.
- **Incentive emissions** — WELL is emitted to suppliers/borrowers to bootstrap liquidity. This is a double-edged value lever: it attracts TVL but can sustain "mercenary" liquidity that leaves when rewards taper.

---

## History & Notable Events

- **2021–2022** — Moonwell launches as a Compound-style money market; its **Moonbeam** deployment ("**Moonwell Artemis**") and earlier **Moonwell Apollo** (Moonriver) bring on-chain lending to the Polkadot-adjacent ecosystems. Shared, audited codebase across deployments.
- **2023 — Base expansion** — Moonwell deploys on **[[base|Base]]** shortly after Coinbase's L2 launch, becoming one of the larger early lending markets on the chain and shifting its growth center there.
- **2023 onward** — iterates on the stkWELL safety module, multichain WELL governance, and asset onboarding (including liquid-staking and stablecoin collateral), competing for Base lending TVL against newer entrants and the incumbents [[aave|Aave]]/[[compound|Compound]].

---

## Competitive Position

Moonwell competes with the dominant lending protocols — [[aave|Aave]] and [[compound|Compound]] — as well as Base-native and multi-chain money markets. Its differentiation is a polished, retail-friendly UX and an early, sizable footprint on Base, which has become one of the most active L2 ecosystems. The challenge is that lending TVL and brand strength are heavily concentrated in Aave; smaller money markets must compete on chain selection, incentives, asset coverage, and reliability.

### Comparison vs lending peers

| Protocol | Model | Primary chains | Token & backstop | Edge | Position |
|---|---|---|---|---|---|
| **Moonwell** | Compound-style pooled markets | [[base\|Base]], Moonbeam | WELL + stkWELL safety module | Retail UX, early Base footprint | Leading Base-native money market |
| [[aave\|Aave]] | Pooled markets + isolation/e-mode | Many (Ethereum, L2s) | AAVE + Safety Module | Deepest liquidity, most assets, brand | Category leader by TVL |
| [[compound\|Compound]] | Pooled markets (originator) / Comet | Ethereum, some L2s | COMP | Battle-tested, simple primitive | Pioneer; smaller than Aave now |
| Morpho | Peer-to-peer matching over pools / isolated vaults | Ethereum, Base | MORPHO | Rate optimization, curated vaults | Fast-growing efficiency layer |

Moonwell's strategy is to win share on a specific high-growth chain (Base) with superior UX rather than to out-scale Aave globally.

---

## Risks

- **Smart-contract and liquidation risk** — lending protocols are prime exploit targets; bad-debt events, oracle failures, or cascading liquidations during volatility can impair suppliers.
- **Collateral / depeg risk** — supporting volatile or lightly-liquid collateral increases the chance of under-collateralized positions in fast markets.
- **Micro-cap token** — at ~$17.2M (rank #892), WELL is a small-cap asset; the token's value is distinct from protocol TVL and can be volatile.
- **Incentive dependence** — usage partly driven by WELL emissions can recede if incentives taper ("mercenary" liquidity).
- **Chain concentration** — heavy reliance on Base ties Moonwell's fortunes to that ecosystem's continued growth and security.

> **Data disclaimer:** Figures above are point-in-time market snapshots (2026-06-22) and qualitative descriptions of mechanism. TVL, APY, and current audit status are not independently verified here and should be confirmed against official documentation and on-chain analytics before any decision.

---

## Platform & Chain Information

**Native Chains:** [[base|Base]], Moonbeam

### Contract Addresses

| Chain | Address |
|---|---|
| Moonbeam | `0x511ab53f793683763e5a8829738301368a2411e3` |
| Base | `0xa88594d404727625a9437c3f886c7643872296ae` |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Max Supply** | 5.00B WELL |
| **Total Supply** | 5.00B WELL |
| **Market Cap / FDV** | High (most supply circulating) |

*Note: exact circulating supply and FDV change with each snapshot; re-verify at source.*

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Kraken | WELL/USD |
| KuCoin | WELL/USDT |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://moonwell.fi](https://moonwell.fi) |
| **Twitter** | [@MoonwellDeFi](https://twitter.com/MoonwellDeFi) |
| **Telegram** | [moonwellfichat](https://t.me/moonwellfichat) |
| **Discord** | [https://discord.com/invite/moonwellfi](https://discord.com/invite/moonwellfi) |
| **GitHub** | [moonwell-fi/contracts-open-source](https://github.com/moonwell-fi/contracts-open-source) |
| **Docs** | [https://docs.moonwell.fi](https://docs.moonwell.fi/moonwell-finance/overview/what-is-moonwell) |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[lending]]
- [[base]]
- [[compound]]
- [[aave]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko snapshot).
- General market knowledge; no additional specific wiki source ingested yet.

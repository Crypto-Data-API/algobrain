---
title: "Liquity USD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoin]
aliases: ["LUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.liquity.org/"
related: ["[[cdp]]", "[[collateralization]]", "[[crypto-markets]]", "[[defi]]", "[[depeg]]", "[[ethereum]]", "[[liquity-bold-2]]", "[[liquity]]", "[[maker]]", "[[stablecoin]]"]
---

# Liquity USD

**Liquity USD** (ticker **LUSD**) is an interest-free, [[ethereum]]-collateralized, decentralized [[stablecoin]] soft-pegged to the US dollar and minted by the **Liquity** protocol (see [[liquity]]). It is distinct from **LQTY**, Liquity's secondary/governance-adjacent incentive token — LUSD is the dollar unit, LQTY is the protocol token. Liquity is a non-custodial, immutable, and governance-free borrowing protocol that lets users draw **0%-interest** loans in LUSD against [[ethereum]] (ETH) as collateral. It ranks **#668** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

At the latest snapshot LUSD traded at **$1.01** (market cap **$28,248,066**, rank **#668**), up **0.33% over 24h** and **0.19% over 7d**. A price of **~$1.01 is on-peg** for LUSD: the protocol's redemption mechanism enforces a hard floor near $1 while the supply cap and collateral backing keep it from straying far above, so it routinely trades in a tight $1.00–$1.02 band rather than at exactly $1.00. The peg held its tight band even through the current Extreme-Fear, Established-Bear tape (BTC ~$64,211; Fear & Greed 21).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LUSD |
| **Market Cap Rank** | #668 |
| **Market Cap** | $28,248,066 |
| **Current Price** | $1.01 (on-peg) |
| **24h Change** | +0.33% |
| **7d Change** | +0.19% |
| **Categories** | Stablecoins, Decentralized Finance (DeFi), USD Stablecoin, Crypto-backed Stablecoin, Ethereum Ecosystem, Arbitrum Ecosystem, Optimism Ecosystem, Polygon Ecosystem, Base Ecosystem |
| **Website** | [https://www.liquity.org/](https://www.liquity.org/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

LUSD is a fully redeemable USD-pegged [[stablecoin]] issued by the [[liquity]] protocol. Liquity is a decentralized borrowing protocol that lets users draw **0%-interest** loans against [[ethereum]] (ETH) used as collateral. Loans are paid out in LUSD and must maintain a minimum collateral ratio of only **110%** — one of the most capital-efficient ratios among decentralized, crypto-backed stablecoins. Borrowers pay a one-time borrowing fee at issuance rather than recurring interest.

Liquity is **non-custodial, immutable, and governance-free** — the core contracts cannot be upgraded or paused, which removes admin-key risk but also means no parameter can be changed after deployment. (Liquity's second generation, [[liquity-bold-2|BOLD]] / Liquity V2, replaces the fixed fee with user-set interest rates; LUSD remains the immutable V1 stablecoin.)

## Architecture — Backing & Collateral Model

Each LUSD enters circulation as debt against ETH locked in an individual position (called a **Trove**). The system is therefore **over-collateralized**: although an individual Trove can go as low as 110% collateralization, the protocol enforces a higher total-collateral floor in stressed conditions. Because backing is ETH (a volatile asset), LUSD relies on liquidations and a buffer pool — not a fiat reserve — to stay solvent. See [[collateralization]] and [[cdp]].

## Peg-Maintenance Mechanism

LUSD's soft peg is enforced from both sides:

- **Redemptions (hard floor near $1).** Anyone can redeem LUSD directly with the protocol for **$1 of underlying ETH** (minus a redemption fee), drawn from the riskiest Troves first. If LUSD trades **below $1**, arbitrageurs buy it cheap and redeem it for $1 of ETH, pushing the price back up. This is the mechanism that keeps LUSD from straying meaningfully below peg.
- **Borrowing supply response (soft ceiling).** If LUSD trades **above ~$1.10**, borrowing becomes attractive (you can mint LUSD against ETH and sell it), expanding supply and pushing the price down. Between these bounds LUSD floats, which is why ~$1.01 is normal and on-peg.

## Liquidations & the Stability Pool

When a Trove falls below the minimum collateral ratio it is **liquidated**: its debt is cancelled against LUSD deposited in the **Stability Pool**, and the liquidated ETH collateral is distributed to Stability Pool depositors (typically at a discount, giving them a net gain). If the Stability Pool is empty, debt and collateral are **redistributed** across remaining Troves, with fellow borrowers acting as guarantors of last resort. In extreme system-wide stress, **Recovery Mode** raises the effective collateral requirement (toward 150%) to protect solvency.

---

## How LUSD Differs from BOLD (Liquity V2)

LUSD is Liquity V1; [[liquity-bold-2|BOLD]] is the V2 stablecoin. The two coexist:

| Dimension | LUSD (Liquity V1) | [[liquity-bold-2|BOLD]] (Liquity V2) |
|---|---|---|
| Borrowing cost | One-time fee, 0% recurring interest | User-set annual interest rate |
| Collateral | ETH only | ETH + wstETH + rETH (ring-fenced branches) |
| Redemption ordering | By collateral ratio (riskiest first) | By interest rate (lowest first) |
| Yield to holders | None native | Yield routed to Stability Pool depositors |
| Contracts | Immutable, governance-free | V2 contracts; minimal governance |

---

## Competitive Position

LUSD competes among decentralized, crypto-backed stablecoins on the axes of decentralization, capital efficiency, and censorship resistance:

| Stablecoin | Backing | Key trait | vs LUSD |
|---|---|---|---|
| **LUSD** | ETH only, immutable | 0% interest, 110% min CR, governance-free | Most "credibly neutral"; ETH-only collateral |
| **DAI / USDS** ([[maker|Maker/Sky]]) | Multi-collateral incl. RWAs/USDC | Largest decentralized stable | More centralized collateral; far larger |
| **[[liquity-bold-2|BOLD]]** (Liquity V2) | ETH + LSTs | User-set rates, LST collateral | Same lineage, more flexible, newer |
| **crvUSD / GHO** | Multi-collateral lending | DEX/lending-native stables | Different issuance mechanics |

LUSD's differentiator is radical immutability and decentralization; its constraint is ETH-only collateral and a relatively small ~$28M cap.

---

## How & Where It Trades

LUSD trades on Ethereum DEXs (Uniswap, Sushiswap, Balancer) and is bridged to several L2s (Arbitrum, Optimism, Base, Polygon, zkSync). As a stablecoin, the relevant "price" is peg adherence; secondary-market liquidity is thinner than fiat-backed majors like USDC/USDT.

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | LUSD/USDC | Spot |
| Uniswap V2 (Ethereum) | LUSD/WETH | Spot |
| Sushiswap | LUSD/LQTY | Spot |
| Balancer V2 | LUSD/bb-pool | Spot |

---

## Narrative, Category & Catalysts

- **Category:** Decentralized, crypto-backed [[stablecoin]] — the "credibly neutral" / censorship-resistant stable narrative.
- **Bull catalysts:** Demand for non-fiat, immutable stables during regulatory or counterparty stress; ETH strength expanding collateral capacity; Stability-Pool yield attracting deposits.
- **Bear catalysts:** Migration of borrowing demand to V2 [[liquity-bold-2|BOLD]] (which offers LST collateral and yield); shrinking supply if redemptions outpace minting; small size limiting integrations.
- In a risk-off ETH tape, redemptions can compress supply as borrowers close Troves, but the peg mechanism keeps price stable — LUSD is a defensive, on-peg holding, not a directional bet.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 29.30M LUSD |
| **Total Supply** | 29.30M LUSD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $29.38M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## History / Timeline

| Date | Event |
|---|---|
| 2021-04-05 | LUSD all-time high of **$1.16** (brief above-peg episode during high redemption-optionality demand). |
| 2022-01-27 | LUSD all-time low of **$0.8967** (brief depeg). |
| (Liquity V2 era) | Liquity launches V2 with the [[liquity-bold-2|BOLD]] stablecoin; LUSD remains the immutable V1 unit. |
| 2026-06-21 | Trades ~$1.01 (on-peg), rank #668, ~$28.2M cap. |

*Only dated events with on-page provenance are listed; as a stablecoin, LUSD's history is a tight band around $1.*

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.16 (2021-04-05) |
| **All-Time Low** | $0.8967 (2022-01-27) |
| **Current Price** | $1.01 (on-peg) |
| **24h Change** | +0.33% |
| **7d Change** | +0.19% |

*As a [[stablecoin]], LUSD's price history is a tight band around $1; the ATH/ATL above represent brief depeg episodes, not directional appreciation.*

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x5f98805a4e8be255a32880fdec7f6728c6568ba0` |
| Zksync | `0x503234f203fc7eb888eec8513210612a43cf6115` |
| Base | `0x368181499736d0c0cc614dbb145e2ec1ac86b8c6` |
| Polygon Pos | `0x23001f892c0c82b79303edc9b9033cd190bb21c7` |
| Arbitrum One | `0x93b346b6bc2548da6a1e7d98e9a421b42541425b` |
| Optimistic Ethereum | `0xc40f949f8a4e094d1b49a23ea9241d289b7b2819` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | LUSD/USDC | Spot |
| Uniswap V2 (Ethereum) | LUSD/WETH | Spot |
| Sushiswap | LUSD/LQTY | Spot |
| Balancer V2 | LUSD/bb-pool | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.liquity.org/](https://www.liquity.org/) |
| **Twitter** | [@LiquityProtocol](https://twitter.com/LiquityProtocol) |
| **Reddit** | [https://www.reddit.com/r/Liquity/](https://www.reddit.com/r/Liquity/) |
| **Discord** | [https://discord.gg/2up5U32](https://discord.gg/2up5U32) |
| **GitHub** | [https://github.com/liquity/dev](https://github.com/liquity/dev) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 352 |
| **GitHub Forks** | 339 |
| **Pull Requests Merged** | 47 |
| **Contributors** | 5 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $1.01 (on-peg) |
| **Market Cap** | $28,248,066 |
| **Market Cap Rank** | #668 |
| **24h Change** | +0.33% |
| **7d Change** | +0.19% |
| **Last Updated** | 2026-06-21 |

---

## Risks

- **Depeg risk.** Although redemptions provide a hard floor near $1, LUSD can briefly trade away from peg during liquidity crunches or extreme ETH volatility (see [[depeg]]). It has historically traded slightly above $1 due to its supply cap and the value of redemption optionality.
- **Collateral (ETH) volatility.** Backing is volatile [[ethereum]]; a fast ETH crash can push Troves into liquidation en masse, stressing the Stability Pool.
- **Stability Pool exhaustion / redistribution.** If the Stability Pool is depleted during a crash, liquidated debt is redistributed to remaining borrowers, raising their effective leverage and risk.
- **Immutability cuts both ways.** Governance-free, non-upgradeable contracts eliminate admin-key risk but mean bugs or suboptimal parameters cannot be patched in the original protocol.
- **Oracle risk.** Liquidations depend on a price oracle for ETH; oracle failure or manipulation could trigger improper liquidations or under-collateralization.
- **Liquidity / size.** At roughly $28M market cap, LUSD is a relatively small stablecoin; secondary-market liquidity is thinner than for fiat-backed majors.

> *Informational only, not investment advice. Stablecoins are not risk-free; even overcollateralized designs can deviate from peg under extreme stress.*

---

## Trading Playbook

- **Regime behavior:** LUSD is a defensive, on-peg instrument. In risk-off tape it functions as a decentralized dollar; the interesting variable is *supply*, which contracts as borrowers close Troves when ETH falls and expands when borrowing demand returns. It does not appreciate directionally.
- **What to watch:** peg deviation (sustained moves outside $1.00–$1.02 are the signal); ETH price and aggregate Trove collateralization (liquidation pressure); Stability Pool depth; LUSD supply trend vs V2 [[liquity-bold-2|BOLD]] migration.
- **In this tape:** with ETH ~27% below its 200-day MA and Extreme Fear, ETH-collateral stress is the key thing to monitor — watch for Stability Pool adequacy and any redistribution events. As a holding, LUSD is a way to sit in a credibly-neutral dollar; the trade is in the Stability-Pool yield and redemption arbitrage, not in price.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[liquity]]
- [[liquity-bold-2]]
- [[stablecoin]]
- [[collateralization]]
- [[cdp]]
- [[depeg]]
- [[maker]]
- [[ethereum]]
- [[defi]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.

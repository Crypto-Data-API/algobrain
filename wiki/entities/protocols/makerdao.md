---
title: "MakerDAO"
type: entity
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [crypto, defi, stablecoin, ethereum, governance, lending, decentralized, makerdao]
aliases: ["Maker", "MakerDAO", "Sky Protocol", "Sky", "MKR"]
entity_type: protocol
founded: 2014
headquarters: "Decentralized"
website: "https://makerdao.com"
related: ["[[dai]]", "[[defi]]", "[[ethereum]]", "[[stablecoins]]", "[[defi-lending]]", "[[aave]]", "[[usdc]]", "[[stablecoin-depegs]]", "[[stablecoin-yields]]", "[[smart-contracts]]"]
---

# MakerDAO

**MakerDAO** is the decentralized autonomous organization behind the Maker Protocol, which issues [[dai|DAI]] — the largest decentralized [[stablecoins|stablecoin]] with approximately $5 billion in circulation. Founded in 2014 by Rune Christensen, MakerDAO pioneered the concept of over-collateralized lending on [[ethereum|Ethereum]]: users deposit crypto assets into smart contract "Vaults" and mint DAI against their collateral. MakerDAO is governed by MKR token holders who vote on risk parameters, collateral types, and protocol upgrades.

In September 2024, MakerDAO announced a rebrand to **[[sky|Sky Protocol]]**, with [[dai|DAI]] migrating to [[usds|USDS]] and MKR migrating to SKY. The rebrand remains controversial, and both names coexist during the transition.

## Naming Glossary (Maker → Sky)

Because the rebrand introduced parallel naming, both vocabularies appear across the wiki and the wider market. This table maps the legacy Maker terms to their Sky-era equivalents:

| Maker (legacy) | Sky (current) | What it is |
|---|---|---|
| MakerDAO | [[sky\|Sky]] (Sky Protocol) | The protocol / DAO brand |
| [[dai\|DAI]] | [[usds\|USDS]] (Sky Dollar) | The primary stablecoin (1:1 convertible; DAI persists) |
| MKR | SKY (~1 MKR ≈ 24,000 SKY) | The governance / backstop token |
| DAI Savings Rate (DSR) | Sky Savings Rate (SSR) | Variable yield paid to stablecoin savers |
| sDAI | sUSDS | Yield-bearing wrapped savings token |
| SubDAOs | Stars | Specialized governance units / sub-ecosystems |
| — | SkyLink | Cross-chain distribution layer for USDS/SKY |

DAI is not being forcibly retired — USDS is an opt-in upgrade with a 1:1 converter, and DAI continues to circulate. Both can coexist indefinitely.

## Overview

MakerDAO occupies a unique position in [[defi|DeFi]] — it is simultaneously a **stablecoin issuer**, a **decentralized lending protocol**, and a **central bank analogue** for crypto. Its governance decisions on stability fees (interest rates), collateral ratios, and the DAI Savings Rate function like monetary policy decisions, making MakerDAO one of the most consequential DAOs in existence.

| Metric | Value |
|---|---|
| **Founded** | 2014 (concept); December 2017 (DAI launch on mainnet) |
| **Total Value Locked** | ~$8-10B |
| **DAI in circulation** | ~$5B |
| **Governance token** | MKR (transitioning to SKY) |
| **Revenue** | ~$200-300M annually (stability fees + RWA yields) |
| **Blockchain** | [[ethereum|Ethereum]] (primary), multi-chain via bridges |

## Protocol Architecture

The Maker Protocol is a set of [[smart-contracts|smart contracts]] (the "Multi-Collateral Dai" or MCD system) on [[ethereum|Ethereum]]. The internal accounting is unusual and worth understanding because it explains many of the protocol's behaviors:

| Component | Internal name | Role |
|---|---|---|
| **Core vault engine** | `Vat` | The central ledger; tracks every vault's collateral and debt |
| **Collateral adapters** | `GemJoin` / `DaiJoin` | Move tokens in/out of the `Vat` accounting system |
| **Liquidation system** | `Dog` + `Clipper` | Trigger and run collateral auctions (Liquidations 2.0) |
| **Stability fee accrual** | `Jug` | Accrues the per-collateral interest rate over time |
| **Savings rate** | `Pot` | Holds DSR/SSR deposits; mints sDAI/sUSDS receipts |
| **Peg Stability Module** | `PSM` | 1:1 swaps between fiat-backed stablecoins (e.g. [[usdc\|USDC]]) and DAI |
| **Price feeds** | `Spot` + Oracles | Median-based [[oracle-manipulation\|price oracles]] with a security delay (OSM) |
| **Surplus / deficit** | `Vow` | Routes protocol surplus to buybacks and deficits to MKR auctions |
| **Emergency shutdown** | `End` (Global Settlement) | Freezes the system and lets holders redeem collateral pro-rata |

The **Oracle Security Module (OSM)** delays new prices by one hour, giving the system and keepers time to react and reducing [[oracle-manipulation|oracle-manipulation]] risk. **Direct Deposit Modules (D3Ms)** let Maker deploy DAI directly into money markets like [[aave|Aave]] to set a target borrow rate, effectively exporting monetary policy to other protocols.

## How the Maker Protocol Works

### Vault Mechanism

The core product: users lock collateral and mint DAI.

1. User deposits collateral (ETH, WBTC, USDC, stETH, real-world assets, etc.) into a Maker Vault smart contract
2. User mints DAI against the collateral, up to the maximum allowed by the collateral ratio
3. Most vault types require **150%+ collateralization** — $1,500 in collateral to mint $1,000 of DAI
4. User pays a **stability fee** (variable interest rate) on the outstanding DAI debt
5. If collateral value drops below the **liquidation ratio**, the vault is automatically liquidated — collateral sold at auction to repay DAI + a liquidation penalty (typically 13%)
6. To recover collateral, user repays DAI debt + accrued stability fees

### Peg Stability

DAI maintains its $1 peg through economic incentives:

- **DAI > $1**: Users open vaults and mint new DAI to sell above par → supply increases → price falls
- **DAI < $1**: Users buy cheap DAI to repay vault debts at par → supply decreases → price rises
- **Peg Stability Module (PSM)**: Allows direct 1:1 swaps between USDC and DAI, providing a hard floor/ceiling near $1
- **DAI Savings Rate (DSR)**: Variable yield paid to DAI holders who deposit into the DSR contract. Used as a monetary policy lever — higher DSR = more DAI demand

### DAI Savings Rate (DSR) and sDAI

The DSR is MakerDAO's most important monetary policy tool. When DAI holders deposit into the DSR contract, they receive **sDAI** — a yield-bearing wrapper that automatically appreciates against DAI. During 2023-2024, the DSR ranged from **5-8%**, funded primarily by RWA yields (US Treasuries).

sDAI has become one of the most widely integrated yield-bearing stablecoins in DeFi, used as collateral on [[aave|Aave]], Compound, and other lending protocols.

## MKR Governance

MKR token holders govern all protocol parameters:

| Parameter | What MKR Holders Decide |
|---|---|
| **Stability fees** | Interest rates charged to vault creators (protocol revenue) |
| **Collateral types** | Which assets can back DAI (onboarding/offboarding) |
| **Debt ceilings** | Maximum DAI mintable against each collateral type |
| **Liquidation ratios** | Minimum collateralization before liquidation triggers |
| **DAI Savings Rate** | Yield paid to DAI depositors |
| **Oracle configuration** | Price feed sources and parameters |
| **Emergency shutdown** | Nuclear option: wind down the entire protocol |

**MKR as backstop**: If the system becomes undercollateralized (e.g., liquidations fail to recover enough DAI), new MKR tokens are minted and auctioned to cover the deficit. This dilutes existing MKR holders — making them the lender of last resort and aligning their incentives with sound risk management.

## Collateral Composition

MakerDAO's collateral has evolved dramatically from ETH-only to a diversified portfolio:

| Collateral Category | Approximate Share | Examples |
|---|---|---|
| **Real-World Assets (RWA)** | ~40% | US Treasuries (via BlockTower, Monetalis), institutional loans |
| **USDC (PSM)** | ~25% | Direct 1:1 swap module |
| **ETH and staked ETH** | ~20% | ETH, wstETH, rETH |
| **WBTC and other crypto** | ~10% | WBTC, various ERC-20 tokens |
| **Other** | ~5% | Smaller vault types |

### The Centralization Paradox

A significant portion of DAI's backing comes from centralized assets — USDC (via the PSM) and US Treasuries (via RWA vaults). This creates a tension:

- DAI is the premier "decentralized" stablecoin, but its backing is substantially centralized
- If Circle froze USDC in the PSM, ~25% of DAI's backing would be at risk
- If US Treasury markets experienced severe disruption, RWA-backed DAI could be affected
- Community debate between purists (reduce centralized collateral) and pragmatists (RWAs provide stable, profitable backing) is ongoing

### Real-World Assets (RWA) in Depth

[[real-world-assets|Real-world assets]] transformed MakerDAO from a crypto-collateral lender into a hybrid that earns TradFi yield. The mechanism: governance approves an RWA vault operator (a legal SPV) that takes DAI, converts it to USD, and buys short-duration [[treasuries|US Treasuries]] or makes institutional loans. The yield flows back to the protocol.

| RWA program (representative) | Asset type | Why it matters |
|---|---|---|
| Monetalis Clydesdale | Short-term US Treasuries via SPV | Among the largest single RWA allocations |
| BlockTower Andromeda | Treasury ladder | Scaled RWA Treasury exposure |
| Coinbase custody allocation | USDC earning Coinbase-paid yield | Yield on otherwise-idle PSM USDC |
| Spark Tokenization Grand Prix | Tokenized Treasury funds (e.g. BlackRock BUIDL, others) | On-chain-native RWA, part of the Endgame plan |

The strategic logic: when the [[federal-reserve|Fed]] funds rate is high, holding DAI's USDC/cash reserves in Treasuries earns ~4-5% risk-free, which can fund a competitive savings rate while still accruing surplus. The risk: RWAs introduce legal/custodial counterparty risk, regulatory exposure, and the [[vasp-regulation|compliance]] surface of TradFi — the opposite of DeFi's permissionless ideal. RWA yield is also rate-sensitive: a sharp Fed cut compresses both protocol revenue and the sustainable savings rate.

## Products and Sub-Protocols

The Sky ecosystem is organized as a set of "Stars" (formerly SubDAOs), each running specialized functions on top of the core protocol:

| Product | What it is | Trader relevance |
|---|---|---|
| **Core protocol** | USDS/DAI issuance, vaults, savings rate | The monetary base of the system |
| **[[spark-protocol\|Spark (SparkLend)]]** | A lending market (Aave-v3 fork) seeded with Maker liquidity via D3M | Borrow/lend USDS at protocol-influenced rates; sUSDS collateral |
| **Spark Liquidity Layer** | Deploys stablecoin liquidity across chains and money markets | Routes idle reserves to yield, including tokenized RWAs |
| **sUSDS / sDAI** | Yield-bearing savings wrappers | Composable yield-bearing collateral across DeFi |
| **SkyLink** | Cross-chain distribution of USDS/SKY to L2s and other chains | Multi-chain access; relevant to [[cross-chain-arbitrage\|cross-chain]] flow |
| **Grand Prix / Star launches** | Periodic onboarding of new collateral, tokens, and sub-DAOs | New listings can move SKY and reprice ecosystem tokens |

## The Endgame Plan

"Endgame" is Rune Christensen's multi-year restructuring proposal (introduced 2022, executed from 2024) that produced the Sky rebrand. Its stated goals:

- **Decentralize via Stars (SubDAOs)** — break the monolithic DAO into specialized, semi-autonomous units, each with its own token and farming program, to reduce governance bottlenecks.
- **Reduce regulatory attack surface** — a fully fungible, brand-clean USDS is intended to be more resilient than a single monolithic entity. A controversial element of early Endgame drafts discussed the ability to **freeze** USDS at the smart-contract level for compliance, which alarmed decentralization purists.
- **Tokenomics reset** — the 1 MKR ≈ 24,000 SKY redenomination, plus farming incentives to bootstrap the new tokens and savings products.
- **Path to a "NewGov" / AI-assisted governance** — long-term ambitions to encode governance rules into "Atlas," a living constitution, with tooling to reduce reliance on continuous human voting.

Endgame is the most consequential thing to understand about the protocol post-2024: it is why two token systems coexist, why new savings products appeared, and why the brand is now "Sky."

## Risk Profile

| Risk | Description | Mitigation |
|---|---|---|
| **Centralization paradox** | ~Half of backing is USDC + RWAs (centralized) | Diversification debate; surplus buffer |
| **Oracle failure / manipulation** | Bad price feed could trigger wrongful liquidations | OSM 1-hour delay; multi-source medians ([[oracle-manipulation]]) |
| **Liquidation cascade** | Auctions fail under congestion/volatility (Black Thursday) | Liquidations 2.0 (instant-settlement clips), circuit breakers |
| **RWA counterparty / legal** | SPV default, custodian failure, regulatory action | Diversified operators; legal structuring |
| **[[smart-contracts\|Smart-contract]] risk** | Bug in MCD or a Star protocol | Heavy auditing; long track record; bug bounties |
| **Governance attack** | Hostile MKR/SKY accumulation or low-turnout vote | GSM pause delay on executive spells; voter delegation |
| **Stablecoin-collateral contagion** | A backing stablecoin depegs (see [[stablecoin-depeg-history]]) | PSM caps; surplus buffer; collateral diversification |
| **Peg break** | USDS/DAI trades meaningfully off $1 | PSM 1:1 swaps; savings rate as demand lever ([[depeg-risk]]) |

## Revenue Model

MakerDAO is one of the most profitable DeFi protocols:

| Revenue Source | Mechanism | Approximate Contribution |
|---|---|---|
| **Stability fees** | Interest on vault debt (5-8% on ETH vaults during high-rate periods) | ~30% |
| **RWA yields** | US Treasury and institutional loan yields (~4-5%) | ~55% |
| **Liquidation penalties** | 13% fee on liquidated vaults | ~10% |
| **PSM fees** | Small fees on USDC↔DAI swaps | ~5% |

A portion of revenue funds the DAI Savings Rate; the remainder accrues to MKR holders through token buybacks (the "Smart Burn Engine").

## Key Historical Events

### Black Thursday — March 12, 2020

The defining stress test for MakerDAO:

- ETH crashed **43% in a single day** during the COVID market panic
- Ethereum network congestion caused gas prices to spike, making liquidation auctions dysfunctional
- Some liquidators bid **$0** on collateral auctions and won — exploiting the gas congestion to be the only bidder
- The protocol became **$5.4 million undercollateralized**
- Emergency MKR auction minted and sold new MKR to cover the deficit
- DAI traded above $1.05 for weeks as vault holders scrambled to buy DAI to repay debts (reducing supply)
- Post-mortem: MakerDAO added circuit breakers, improved auction mechanics, and diversified collateral to include USDC

**Lesson**: Over-collateralization works, but auction mechanics must be robust under extreme conditions. Unlike [[terra-luna-collapse|Terra/LUNA]], MakerDAO survived its stress test — bruised but functional.

### USDC/SVB Depeg — March 2023

When Silicon Valley Bank collapsed, [[usdc|USDC]] briefly traded at $0.87 because Circle held $3.3B in reserves at SVB. DAI depegged to ~$0.89 in sympathy because a significant portion of DAI collateral was USDC (via the PSM). When USDC recovered after the FDIC intervened, DAI recovered.

**Lesson**: The centralization paradox made real — DAI's decentralized design was undermined by its dependence on a centralized stablecoin.

### Sky Protocol Rebrand — September 2024

MakerDAO announced a comprehensive rebrand:

- DAI → **USDS** (Sky Dollar)
- MKR → **SKY** governance token
- SubDAOs → **Stars** (specialized DAOs managing different protocol functions)

The rebrand has been **controversial**. Critics argue it abandons one of DeFi's strongest brands. Supporters argue it enables a new governance structure better suited for scaling. As of early 2026, both DAI/USDS and MKR/SKY coexist during the migration period.

## MakerDAO vs Other Stablecoin Issuers

| Dimension | MakerDAO (DAI) | [[circle|Circle]] (USDC) | Tether (USDT) | Terra (UST) |
|---|---|---|---|---|
| **Model** | Over-collateralized DeFi | Fiat-backed centralized | Fiat-backed centralized | Algorithmic (failed) |
| **Can freeze tokens** | No | Yes | Yes | N/A |
| **Collateral transparency** | Fully on-chain | Monthly attestation | Quarterly attestation | None (self-referential) |
| **Yield for holders** | Yes (DSR/sDAI) | No | No | Yes (Anchor — unsustainable) |
| **Survived stress tests** | Yes (Black Thursday, SVB) | Yes (SVB) | Yes (multiple) | **No** — collapsed |
| **Capital efficiency** | Low (150%+ collateral) | High (1:1) | High (1:1) | High (but fragile) |

The key lesson from comparing MakerDAO to [[terra-luna-collapse|Terra]]: over-collateralization is expensive in capital terms but provides genuine stability. Algorithmic efficiency without collateral is cheap until it breaks — then it breaks completely.

## How Traders Use MakerDAO

| Use case | Mechanism | Notes |
|---|---|---|
| **Leverage long ETH/crypto** | Deposit ETH, mint DAI/USDS, buy more ETH (recursive) | Cheaper, non-liquidatable-by-margin-call vs CEX margin, but exposed to the liquidation ratio |
| **Stablecoin "carry"** | Hold sDAI/sUSDS for the savings rate | Yield is funded largely by RWA Treasury yield; rate-sensitive |
| **Borrow against collateral** | Mint a stablecoin without selling the underlying | Tax-deferral and continued upside exposure |
| **Peg arbitrage** | Trade DAI/USDS deviations vs $1 via PSM and vaults | The PSM provides a near-hard band; see [[stablecoin-pair-arbitrage]] |
| **Liquidation keeping** | Bid in `Clipper` auctions on undercollateralized vaults | A profession in itself; profits from liquidation penalty discount |
| **SKY/MKR directional** | Trade the governance token on revenue/sentiment | Buyback ("Smart Burn Engine") links revenue to token value |

## Trading Relevance

- **MKR/SKY price** correlates with DeFi sentiment and protocol revenue. Higher stability fees = more revenue = more buyback pressure
- **Savings-rate changes** impact DeFi-wide stablecoin yields — when Maker/Sky raises the DSR/SSR, competing lending rates adjust ([[stablecoin-yields]])
- **DAI/USDS peg deviations** provide [[arbitrage|arbitrage]] opportunities for vault operators and PSM users
- **Governance votes** on collateral onboarding can signal which assets the protocol considers institutionally credible
- **RWA yield** makes the protocol a bridge between TradFi yields and DeFi — changes in [[treasuries|US Treasury]] rates directly affect profitability and the savings rate
- **Spark (SparkLend) rates** are partly steered by Maker via D3M, so Maker governance indirectly sets borrow costs across part of the lending market

## See Also

- [[dai]] — The stablecoin issued by MakerDAO
- [[defi]] — Decentralized finance ecosystem
- [[defi-lending]] — Lending protocols including Maker
- [[ethereum]] — MakerDAO's primary blockchain
- [[stablecoins]] — Stablecoin market overview
- [[stablecoin-depegs]] — DAI depeg history (Black Thursday, SVB)
- [[stablecoin-yields]] — sDAI and DSR yield
- [[aave]] — Competing lending protocol; also integrates sDAI
- [[usdc]] — Major DAI collateral source (PSM) and competitor
- [[terra-luna-collapse]] / [[terra-luna]] — Contrast: algorithmic stablecoin that failed where MakerDAO succeeded
- [[smart-contracts]] — Foundation of Maker's vault system
- [[stablecoin-competition]] — Competitive landscape
- [[sky]] — The current brand of the protocol
- [[usds]] — Sky Dollar, the USDS upgrade of DAI
- [[spark-protocol]] — Maker/Sky's lending market (SparkLend)
- [[real-world-assets]] — Treasury-backed collateral powering the savings rate
- [[stablecoin]] — General stablecoin concept
- [[stablecoin-depeg-history]] — Master depeg timeline (DAI appears via Black Thursday and SVB)
- [[depeg-risk]] — Framework for peg-break risk
- [[oracle-manipulation]] — Oracle risk relevant to the OSM/`Spot` system
- [[stablecoin-pair-arbitrage]] — Trading DAI/USDS peg deviations
- [[treasuries]] — Underlying RWA yield source
- [[federal-reserve]] — Rate setter whose decisions move RWA yield and the savings rate

## Sources

- MakerDAO / Sky governance forum and on-chain voting records
- Maker Protocol / Sky technical documentation (MCD contract reference: `Vat`, `Pot`, `PSM`, `End`)
- Black Thursday post-mortem (MakerDAO blog, March 2020)
- Sky Endgame / "The Endgame Plan" governance proposals (Rune Christensen, 2022-2024)
- General DeFi market analysis
- General market knowledge; specific TVL/circulation figures above are approximate and not point-in-time verified.

---
title: "Midas mHYPER"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, tokenization, yield]
aliases: ["MHYPER", "mHYPER"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://midas.app/mhyper"
related: ["[[real-world-assets]]", "[[tokenization]]", "[[stablecoin]]", "[[crypto-markets]]", "[[ethereum]]"]
---

# Midas mHYPER

**Midas mHYPER** (MHYPER) is a **tokenized yield-bearing structured product** issued by Midas. It is a tokenized certificate that references the performance of selected market-neutral, stablecoin-focused strategies deployed across on-chain markets and ecosystems, with the strategy monitored by **Hyperithm** — a digital-asset manager based in Tokyo and Seoul — acting as the appointed **Risk Manager**. Unlike a 1:1 stablecoin, mHYPER is designed to accrue value over time, so its price trades **above $1** as net yield compounds into the token's reference NAV.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, MHYPER trades at **$1.11** with a market capitalization of **$33,892,261**, ranking **#595** by market cap. It was unchanged over 24 hours (**0.00%**) and up **+0.19%** over the trailing week. The slow, monotonic upward drift in price is the signature of a yield-accruing instrument rather than a pegged or directional asset — the **>$1 price reflects accrued yield/NAV growth, not a premium or de-peg.** The wider crypto market sat in Extreme Fear (Fear & Greed 22, Bitcoin ~$64,180).

---

## What mHYPER Is

mHYPER is part of Midas's family of **Liquid Yield Tokens**, which wrap professionally managed off-chain/on-chain strategies into a single transferable ERC-20-style token:

- **Issuer:** Midas, an RWA / tokenization platform that issues yield-bearing certificates against managed strategies.
- **Risk Manager:** Hyperithm (Tokyo / Seoul), responsible for monitoring and managing the underlying strategy's risk profile.
- **Strategy:** Diversified, **market-neutral**, stablecoin-focused strategies deployed across DeFi venues. The market-neutral design aims to harvest yield (funding, basis, lending spreads, liquidity provision) while minimizing directional exposure to crypto prices.
- **Yield treatment:** Yield is **accrual-based** — it compounds into the token's reference value rather than being distributed. This is why the unit price rises over time and sits above $1.

---

## Fund structure, custody & NAV

mHYPER is best understood as a **tokenized fund / structured certificate**, not a stablecoin or a trustless on-chain vault. Its value rests on an off-chain / issuer layer:

- **Fund structure:** A permissioned RWA certificate wrapping a managed, market-neutral strategy basket. Midas is the issuer/wrapper; Hyperithm is the appointed risk manager who monitors and constrains the strategy. The token is a **claim on the managed strategy's net asset value**, not a direct on-chain claim on specific reserves.
- **Custody:** Strategy assets and positions sit with the manager/issuer's custody and venue arrangements off the holder's chain. Holders do not custody the underlying positions; they hold a transferable certificate referencing them.
- **NAV:** The reference value is **NAV-based** — net yield (after strategy costs and fees) compounds into the per-token reference value, which is why MHYPER drifts above $1. Holders rely on the **issuer's NAV reporting and attestations** rather than fully transparent on-chain reserves.
- **Eligibility / gating:** Minting and redemption are **KYC-gated and subject to eligibility/jurisdiction restrictions** (a permissioned RWA product). Many holders acquire it on the secondary market, but primary mint/redeem at NAV is the realistic exit and is permissioned.

### Mint, Redeem, and Backing

mHYPER is a permissioned RWA certificate. Minting and redemption flow through Midas's issuance infrastructure (typically KYC-gated and subject to eligibility/jurisdiction restrictions). The token is a **claim on a managed strategy**, so its value rests on the off-chain/issuer layer: the strategies actually performing, the manager managing risk competently, and Midas honoring redemptions at NAV.

---

## Comparison vs peers

| Token | Issuer | Underlying | Yield source | Access |
|---|---|---|---|---|
| **mHYPER** | Midas | Market-neutral DeFi strategy basket | Funding/basis/lending spreads | Permissioned (KYC mint/redeem) |
| mTBILL | Midas | US Treasury bills | T-bill yield | Permissioned RWA |
| mBASIS | Midas | Delta-neutral basis trade | Funding/basis | Permissioned RWA |
| [[ethena-usde\|sUSDe]] | Ethena | Delta-neutral hedge | Funding/basis | Permissionless |

Within the Midas family, mHYPER is the **active, market-neutral strategy** sibling of the more vanilla mTBILL (Treasuries) and mBASIS (pure basis) — higher potential yield, but more strategy/manager risk. Versus a permissionless yield dollar like sUSDe, mHYPER trades trustless on-chain composability for a professionally managed, but gated and NAV-opaque, off-chain strategy.

---

## Settlement and Chains

mHYPER is issued natively on **[[ethereum|Ethereum]]** and bridged to Monad and Plasma.

| Chain | Address |
|---|---|
| Ethereum | `0x9b5528528656dbc094765e2abb79f293c21191b9` |
| Monad | `0xd90f6bfed23ffde40106fc4498dd2e9edb95e4e7` |
| Plasma | `0xb31bea5c2a43f942a3800558b1aa25978da75f8a` |

---

## How & where it trades & is used

mHYPER is a **permissioned, NAV-accruing certificate** with **extremely thin secondary on-chain liquidity** (24h change 0.00% and negligible volume at the snapshot). The realistic round-trip is **primary mint/redeem at NAV through Midas** (KYC-gated), not order-book trading. Where secondary liquidity exists it is on Ethereum (and bridged Monad/Plasma) DEXs, but it is too shallow to absorb size. As composable collateral it is constrained by its permissioned nature — integrations must accommodate eligibility gating. Treat it as a **hold-to-NAV yield certificate**, not a tradable token.

---

## Narrative, category & catalysts

mHYPER sits in the **tokenized-fund / RWA yield** category — bringing a professionally managed, market-neutral crypto strategy on-chain as a single transferable token, alongside Midas's mTBILL/mBASIS and broader [[tokenization|tokenized-fund]] peers. Catalysts: (1) sustained, positive market-neutral yield from funding/basis/lending; (2) AUM growth and new chain deployments (Monad, Plasma) widening distribution; (3) integrations accepting mHYPER as collateral. The dominant risk to the thesis is that "market-neutral" yield is regime-dependent — funding and basis can compress or invert, and the current Extreme-Fear backdrop pressures those sources.

---

## History / timeline

- **2026** — Issued as part of Midas's Liquid Yield Token family; deployed on Ethereum and bridged to Monad and Plasma.
- **2026-06-21** — Snapshot: **$1.11** NAV-accrued price, $33,892,261 market cap, rank #595, 24h change 0.00%, +0.19% over 7 days. No de-peg events flagged — the >$1 price is accrued NAV, consistent with a monotonic yield-accruing instrument.

(No dated depeg or NAV-gap events appear in available data; the price history is a smooth upward NAV drift.)

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MHYPER |
| **Product type** | Tokenized yield-bearing structured product (certificate) |
| **Issuer** | Midas |
| **Risk Manager** | Hyperithm (Tokyo / Seoul) |
| **Strategy** | Market-neutral, stablecoin-focused DeFi strategies |
| **Yield treatment** | Accrual into NAV (price drifts above $1) |
| **Market Cap Rank** | #595 |
| **Market Cap** | $33,892,261 |
| **Current Price** | $1.11 |
| **24h Change** | 0.00% |
| **7d Change** | +0.19% |
| **Native Chain** | Ethereum |
| **Categories** | Ethereum Ecosystem, Yield-Bearing Tokens, Midas Liquid Yield Tokens, Plasma Ecosystem, Monad Ecosystem |
| **Website** | [https://midas.app/mhyper](https://midas.app/mhyper) |

---

## Risks

- **Off-chain / issuer dependency:** mHYPER is a claim on a managed strategy. Value depends on Midas (issuer) and Hyperithm (risk manager) — counterparty, operational, and manager risk, not trustless on-chain backing.
- **NAV-gap risk:** Secondary price can diverge from reported NAV, and reported NAV itself depends on issuer attestation; a gap between believed and realisable NAV is a core risk for any tokenized fund.
- **Strategy / yield-source risk:** "Market-neutral" is a design goal, not a guarantee. Basis blowouts, liquidation cascades, smart-contract exploits in the venues used, negative-funding regimes, or correlation breakdowns can produce losses despite the neutral framing.
- **Redemption / liquidity risk:** Secondary on-chain liquidity is extremely thin (24h volume is negligible). Redemption at NAV through the issuer is the realistic exit, and it is **permissioned and may be gated** (KYC, eligibility, jurisdiction).
- **Collateral / custody risk:** Strategy assets sit in off-chain/issuer custody; holders rely on that custody and on the manager's execution rather than on-chain reserves.
- **NAV opacity:** As a structured certificate, holders rely on the issuer's NAV reporting and attestations rather than fully transparent on-chain reserves.
- **Regulatory risk:** Tokenized structured products occupy an evolving regulatory category; eligibility and transfer restrictions apply.

---

## Trading / usage playbook

- **Hold-to-NAV, not trade.** With negligible secondary volume, the realistic round-trip is permissioned mint/redeem at NAV through Midas; do not expect to exit size on a DEX.
- **Confirm eligibility first.** Mint/redeem is KYC-gated and jurisdiction-restricted — verify access before sizing in.
- **Yield is regime-dependent.** Market-neutral returns rely on positive funding/basis/lending spreads; in negative-funding or stressed regimes the NAV drift can stall or reverse.
- **Mark to NAV, watch the gap.** Track the issuer's NAV reporting and any secondary-price gap to NAV; a persistent discount signals redemption/liquidity stress.
- **Compare within the family.** For lower risk, mTBILL (Treasuries) or mBASIS (pure basis) are the more vanilla Midas siblings.

---

## See Also

- [[real-world-assets]]
- [[tokenization]]
- [[stablecoin]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). General market knowledge on Midas Liquid Yield Tokens and Hyperithm; no additional specific wiki source ingested yet.

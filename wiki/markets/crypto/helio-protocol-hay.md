---
title: "Lista USD"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stablecoins, defi]
aliases: ["LISUSD", "lisUSD", "Lista USD", "HAY", "Helio Protocol"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://helio.money/"
related: ["[[crypto-markets]]", "[[lista]]", "[[bnb]]", "[[stablecoin]]", "[[stablecoins]]", "[[dai]]", "[[usdc]]"]
---

# Lista USD

**Lista USD** (ticker **LISUSD / lisUSD**, formerly **HAY** from **Helio Protocol**) is a **crypto-overcollateralized USD-pegged [[stablecoin]]** on **[[bnb|BNB Chain]]**, targeting a soft 1 USD peg. Its issuer describes it as a **"destablecoin"**: an over-collateralized asset where 1 lisUSD is redeemable for $1 *of cryptocurrency collateral* (primarily BNB and liquid-staked BNB), not fiat. Users mint and borrow lisUSD by depositing collateral, then use it to stake for yield, provide liquidity, or transfer value.

> **Scope note:** This page covers the **lisUSD stablecoin asset** (ticker LISUSD). The issuing protocol, its **LISTA governance token**, the slisBNB liquid-staking product, and the Helio→Lista rebrand are covered in depth on **[[lista|Lista DAO]]**. lisUSD is a distinct tradeable asset (rank ~#333, ~$1) from the LISTA token (rank ~#761, ~$0.055); this page is the stablecoin reference and defers to [[lista]] for governance/tokenomics of the DAO.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | LISUSD |
| **Price** | $0.997089 |
| **Market cap** | $75.2M |
| **Market-cap rank** | #333 |
| **24h volume** | $41,524 |
| **24h change** | -0.02% |
| **Circulating supply** | 75.38M LISUSD |
| **Total supply** | 75.38M LISUSD |
| **All-time high** | $2.00 |
| **All-time low** | $0.208609 |

Circulating supply equals total supply (market-cap / FDV ≈ 1.00). Price is near peg (~$0.997). The broader tape on 2026-06-21 was Extreme Fear (Fear & Greed 21; [[bitcoin|BTC]] ~$64,568) — a backdrop in which BNB-collateralized stablecoins warrant close attention to collateral ratios.

> *Informational only, not investment advice. A "destablecoin" is a soft peg and has deviated far from $1 in the past.*

---

## Architecture — How It Works

Lista USD is a **crypto-overcollateralized CDP stablecoin** ("destablecoin"), in the over-collateralized tradition of [[dai|DAI]] but native to BNB Chain and issued by [[lista|Lista DAO]] (formerly Helio Protocol):

- **Minting / borrowing** — users deposit collateral (primarily BNB and liquid-staked BNB / LSD assets such as Lista's **slisBNB**) into vaults and mint-borrow lisUSD against it above a required collateralization ratio. Using yield-bearing slisBNB as collateral lets users layer staking yield under their borrowed dollar (the Lista "loop" — see [[lista]]).
- **Soft peg** — the target is 1 USD, defended by **overcollateralization**, **liquidation of unhealthy positions**, and **arbitrage**. Helio/Lista calls lisUSD a "destablecoin" precisely because it floats around $1 rather than guaranteeing hard fiat redemption — it is redeemable for $1 *of crypto collateral*, not fiat.
- **Liquidation engine** — when a vault falls below its required collateral ratio, it is liquidated to retire the lisUSD debt and protect the peg. Because collateral is BNB-heavy, a sharp BNB drawdown can cascade into mass liquidations — the central tail risk.
- **Utility** — minted lisUSD can be staked for yield, used in liquidity mining, and used as a medium of transfer within the BNB Chain DeFi ecosystem.
- **Governance** — operated as a DAO ([[lista|Lista DAO]]); the community governs treasury, revenue pool, collateral types, and risk parameters. Backing is verifiable **on-chain via the collateral vaults** rather than via off-chain reserve attestation.

The wide historical range (ATH $2.00 in 2022, ATL $0.208609 in 2022) reflects significant early peg deviation during the project's launch period as Helio Protocol's HAY; it has since traded much closer to $1.

---

## Tokenomics & Supply

lisUSD supply is **demand-driven**: it expands as users mint against BNB/slisBNB collateral and contracts on repayment/liquidation, with circulating lisUSD over-collateralized by the vaults. Circulating equals total supply (75.38M; MC/FDV ≈ 1.00) — consistent with a debt-issued, fully-circulating stable rather than a pre-mined token. lisUSD itself carries no governance rights; the **LISTA** token holds the DAO's governance and value-accrual economics (vote-escrow, stability-fee/revenue routing) — detailed on **[[lista]]**.

---

## Comparison vs Peer Stablecoins

| Stablecoin | Collateral | Peg model | Chain / issuer | Distinguishing trait |
|---|---|---|---|---|
| **lisUSD** (this page) | BNB + slisBNB (LSD), over-collateralized | Soft "destablecoin" peg | BNB Chain / [[lista\|Lista DAO]] | LSD collateral enables stake-then-borrow loop |
| **[[dai]] (DAI/USDS)** | Multi-collateral CDP (crypto + RWA) | Over-collateralized soft peg | Ethereum / Sky (Maker) | Canonical CDP stable; deepest liquidity |
| **[[usdc]]** | Cash + Treasuries (Circle) | Hard mint/redeem peg | Multi-chain / Circle | Fiat-backed; peg-stability contrast |
| **[[usdx]]** | Crypto-collateralized | Soft peg | BNB-ecosystem peer | Other BNB-orbit crypto-collateralized dollar |

lisUSD's closest design analog is **[[dai|DAI]]** (over-collateralized CDP soft-peg). Its differentiator is **BNB-Chain nativity plus liquid-staked collateral**: posting yield-bearing slisBNB as collateral stacks staking yield under the minted dollar, at the cost of heavy BNB concentration that DAI's diversified collateral avoids.

---

## How & Where It Trades / Is Used

lisUSD lives on **[[bnb|BNB Chain]]** (contract `0x0782b6d8c4551b9760e74c0545a9bcd90bdc41e5`) and is used mostly within BNB Chain DeFi (Lista money markets, liquidity pools, yield strategies). The source data shows **no major centralized-exchange listings** and modest 24h volume (~$41.5K) against a ~$75.2M cap — so most lisUSD is **held and deployed inside the protocol** rather than actively spot-traded. Liquidity is concentrated in on-chain BNB Chain venues, and composability is largely within the Lista/BNB DeFi ecosystem.

---

## Narrative, Category & Catalysts

- **Category:** BNB-Chain crypto-overcollateralized CDP stablecoin / "destablecoin"; the stable side of the Lista DAO liquid-staking + CDP stack.
- **Bull catalysts:** growth in BNB staking and slisBNB collateral (more mint demand); rising lisUSD circulation and stability-fee revenue (benefiting [[lista|LISTA]] holders); BNB-Chain DeFi activity; deeper lisUSD liquidity tightening the peg.
- **Bear catalysts:** sharp BNB drawdowns triggering liquidation cascades and peg stress; thin liquidity amplifying any de-peg; competition from centralized stables (USDT/USDC) and other BNB CDP stables; governance/parameter missteps.

---

## History / Timeline

| Date | Event |
|---|---|
| 2022 | Launches as **HAY** under **Helio Protocol**; early peg deviation — ATH **$2.00** and ATL **$0.208609** both recorded in 2022. |
| (rebrand) | Helio Protocol rebrands to **[[lista\|Lista DAO]]**; HAY becomes **lisUSD**, slisBNB liquid staking and the LISTA token added. |
| 2026-06-21 | lisUSD trades ~$0.997089, rank #333, ~$75.2M cap; near peg, thin volume. |

*The 2022 ATL of $0.208609 and ATH of $2.00 are real recorded extremes from the early HAY period — the standout cautionary data points; the rebrand timing is described qualitatively (precise date not in the wiki record).*

---

## Risks

- **De-peg / soft-peg risk** — as a "destablecoin" it is explicitly a soft peg; it has historically deviated far from $1 (ATL $0.208609), though it currently sits near peg.
- **Collateral-concentration risk** — heavy reliance on BNB and BNB-based liquid-staked assets means a sharp BNB drawdown can trigger liquidations and peg stress.
- **Liquidation / smart-contract risk** — peg defense depends on the liquidation engine, oracle prices, and the protocol's contracts functioning under stress.
- **Redemption-gating risk** — no fiat redemption at par; exit is via repaying/liquidating CDPs or thin secondary DEX liquidity, which can be costly in stress.
- **Liquidity risk** — limited listings and modest volume make large exits costly.
- **Governance / issuer risk** — parameters and treasury are DAO-controlled ([[lista|Lista DAO]]); governance decisions and continued development affect stability.
- **Regulatory risk** — evolving stablecoin rules may affect issuance and DeFi integrations.

In the current Extreme-Fear environment (Fear & Greed 21), BNB-collateralized stablecoins are particularly exposed to collateral drawdowns and liquidation cascades.

---

## Trading / Usage Playbook

- **Use case:** lisUSD is the borrow-side dollar of the Lista stack — mint it against BNB/slisBNB to unlock liquidity while keeping staking yield, or hold/farm it within BNB-Chain DeFi. As a standalone parked dollar it is thinner than USDT/USDC.
- **What to watch:** **BNB price** (the dominant collateral — the single biggest driver of liquidation and peg risk); collateral ratios / vault health; the lisUSD secondary price vs $1; Lista DAO risk-parameter changes.
- **Risk-off framing:** in Extreme Fear with BNB under pressure, watch collateral ratios closely — a fast BNB leg down is the main threat to the peg. Treat lisUSD borrowing as a *leveraged BNB position* and size for liquidation-cascade scenarios; prefer repaying debt over selling lisUSD into thin liquidity.

---

## Related

- [[lista]] — the issuing DAO, LISTA governance token, and slisBNB liquid staking (governance/tokenomics reference)
- [[dai]] — the canonical crypto-overcollateralized stablecoin (closest design analog)
- [[stablecoin]] / [[stablecoins]] — category overview
- [[bnb]] — the primary collateral asset and host chain
- [[usdc]] — fiat-backed peer (for peg-stability contrast)
- [[satoshi-stablecoin|Satoshi Stablecoin]], [[usdx|USDX]] — other crypto-collateralized peers
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; protocol mechanics (lisUSD CDP, slisBNB collateral, Helio→Lista rebrand) from public Lista DAO documentation. No specific wiki source ingested yet.

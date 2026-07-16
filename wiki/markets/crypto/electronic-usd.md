---
title: "Electronic USD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, real-world-assets, stablecoin, tokenization]
aliases: ["EUSD", "Electronic Dollar", "eUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://register.app/"
related: ["[[crypto-markets]]", "[[dai]]", "[[depeg]]", "[[ethereum]]", "[[real-world-assets]]", "[[stablecoin]]", "[[tokenization]]", "[[treasuries]]", "[[usdc]]"]
---

# Electronic USD

**Electronic USD** (ticker **eUSD / EUSD**) is a **U.S. dollar–pegged [[stablecoin]]** in the **Reserve Protocol** ecosystem, designed to hold a value of $1.00 and trade as an on-chain digital dollar. Reserve "RTokens" like eUSD are backed by a **transparent, on-chain basket of collateral** rather than by a single off-chain reserve account, which is why aggregators classify eUSD as both **fiat-backed and crypto-backed (overcollateralized)**. It is **Base-native** and also live on [[ethereum|Ethereum]] and Arbitrum.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, eUSD trades at **$0.996636** with a market capitalization of **$23,273,339**, ranking **#752** by market cap. At roughly **$1.00 it is on-peg**, with a minor ~0.3% discount well within normal stablecoin trading bands. It was down **-0.22%** over 24 hours and **-0.49%** over the trailing week — typical micro-fluctuation around the dollar peg, not a [[depeg]]. The broader crypto market was in Extreme Fear (Fear & Greed 21; [[bitcoin|BTC]] ~$64,568), conditions under which small stablecoin discounts are common.

> *Informational only, not investment advice. Stablecoins can break their peg under collateral stress.*

---

## What eUSD Is

eUSD is an asset issued through **Reserve Protocol** infrastructure (the "Register" app at register.app). Reserve's model lets stablecoins ("RTokens") be backed by a transparent on-chain basket of collateral:

- **Peg:** intended to function as a stable on-chain dollar at $1.00.
- **Backing:** a **diversified collateral basket**. eUSD is described across aggregators as both **fiat-backed** and **crypto-backed**, reflecting a basket that can include tokenized cash-equivalents (e.g., yield-bearing dollar instruments such as tokenized [[treasuries|Treasuries]] / T-bill exposure) and is typically **overcollateralized** for safety, with the Reserve mechanism providing a backstop layer.
- **Yield treatment:** in the Reserve model, collateral yield is generally directed to the protocol/backstop rather than rebasing the token's unit value, so eUSD remains a ~$1.00 unit rather than a price-appreciating token.

---

## Architecture — How It Works

Reserve's RToken design is the key to understanding eUSD. Three roles interact around the collateral basket:

- **Collateral basket.** eUSD is fully backed by a basket of dollar-equivalent assets defined on-chain. Each basket unit must always be redeemable, so the protocol enforces 1:1 backing of the issued supply by the basket's reference value.
- **Overcollateralization buffer (RSR stakers).** On top of the basket, Reserve uses a **staked-backstop layer**: holders of the Reserve governance/insurance asset stake to provide first-loss capital. If a collateral asset defaults or de-pegs, the basket switches to a backup configuration and the staked buffer absorbs the shortfall — protecting eUSD holders. This is what makes eUSD *overcollateralized in stress*, distinct from a flat 1:1 fiat reserve.
- **Yield routing.** Where basket assets earn yield (e.g. tokenized T-bills), that yield accrues to the protocol/backstop rather than to the eUSD unit, keeping eUSD a stable $1.00 unit instead of a rebasing or appreciating token.

### Mint, Redeem, and Peg Mechanism

eUSD can be **minted by depositing the required collateral basket** and **redeemed for that underlying collateral** — the core arbitrage that holds the $1.00 peg: if eUSD trades below $1, redeemers buy cheap eUSD and redeem for $1 of collateral; if above $1, minters deposit collateral to mint and sell. Because backing is on-chain and (where applicable) overcollateralized, **reserve transparency is higher** than for purely off-chain fiat stablecoins — though any tokenized real-world collateral in the basket still carries off-chain/issuer dependency. There is no centralized issuer redemption queue; redemption is a permissionless on-chain action against the basket.

---

## Settlement and Chains

eUSD is multi-chain, **Base-native**, and also deployed on Ethereum and Arbitrum.

| Chain | Address |
|---|---|
| Ethereum | `0xa0d69e286b938e21cbf7e51d71f6a4c8918f482f` |
| Base | `0xcfa3ef56d303ae4faaba0592388f19d7c3399fb4` |
| Arbitrum One | `0x12275dcb9048680c4be40942ea4d92c74c63b844` |

---

## Tokenomics & Supply

eUSD has **no fixed supply** — it expands and contracts with mint/redeem demand, and circulating supply is always backed by the collateral basket (plus the staked overcollateralization buffer). eUSD itself is *not* a value-accrual token; the Reserve ecosystem's governance/insurance asset (RSR) carries the staking-and-backstop economics. At a ~$23M cap, eUSD is a small-cap RToken whose supply is a function of demand for a transparent, on-chain-collateralized dollar.

---

## Comparison vs Peer Stablecoins

| Stablecoin | Backing model | Transparency | Yield handling | Distinguishing trait |
|---|---|---|---|---|
| **eUSD** (this page) | On-chain basket (fiat- + crypto-backed) + staked backstop | On-chain basket; high | Yield → protocol/backstop; unit stays $1 | Overcollateralized via RSR staker first-loss |
| **[[usdc]]** | Cash + short-dated Treasuries (Circle) | Off-chain attestations | Issuer keeps reserve yield | Largest regulated fiat dollar; deep liquidity |
| **[[dai]] (DAI/USDS)** | Multi-collateral CDP (crypto + RWA) | On-chain vaults | Surplus to protocol | Largest decentralized CDP soft-peg |
| **Tokenized T-bill dollars** ([[real-world-assets|RWA]]) | Tokenized [[treasuries\|Treasuries]] | Issuer + on-chain | Yield rebases to holder | Yield-bearing; eUSD can *hold* these in its basket |

eUSD's signature is its **configurable, on-chain basket plus first-loss backstop** — more transparent than [[usdc]]'s off-chain reserves and more flexible than [[dai|DAI]]'s vault collateral, at the cost of greater mechanism complexity and a smaller, less liquid market.

---

## How & Where It Trades / Is Used

Secondary liquidity is **moderate** and concentrated on-chain across Base, Ethereum, and Arbitrum (DEX pools pairing eUSD with other dollars). Large redemptions rely on the protocol's permissionless **mint/redeem path against collateral** rather than on deep CEX order books. As an RToken it is composable across Reserve-ecosystem and general DeFi venues; in practice it is held by DeFi users seeking a transparent on-chain dollar rather than traded as a liquid spot pair.

---

## Narrative, Category & Catalysts

- **Category:** transparent, basket-backed RToken dollar; sits at the intersection of DeFi stablecoins and [[real-world-assets|RWA]] / [[tokenization|tokenization]] (its basket can hold tokenized [[treasuries|Treasuries]]).
- **Bull catalysts:** growth of tokenized T-bill collateral improving the basket's quality and (protocol-side) yield; Base-ecosystem adoption; demand for on-chain-transparent dollars vs off-chain fiat stables; deeper eUSD liquidity tightening the peg.
- **Bear catalysts:** impairment/de-peg of a basket collateral asset; thin secondary liquidity widening discounts; regulatory pressure on tokenized-RWA collateral; competition from larger, deeper dollars.

---

## History / Timeline

| Date | Event |
|---|---|
| 2024-03 | All-time low **$0.867** — a documented historical depeg / volatility around the peg. |
| 2024-04 | All-time high **$1.13** — overshoot in thin/volatile conditions. |
| 2026-06-21 | Trades $0.996636, rank #752, ~$23.3M cap; ~0.3% discount, on-peg. |

*The 2024 ATL of $0.867 and ATH of $1.13 are real recorded extremes showing eUSD has experienced meaningful volatility around the peg in the past; the current ~$0.9966 is well within normal bands.*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | EUSD |
| **Peg** | 1:1 U.S. dollar |
| **Ecosystem** | Reserve Protocol (register.app) |
| **Backing** | Diversified collateral basket (fiat-backed + crypto-backed, typically overcollateralized) |
| **Market Cap Rank** | #752 |
| **Market Cap** | $23,273,339 |
| **Current Price** | $0.996636 (on-peg) |
| **24h Change** | -0.22% |
| **7d Change** | -0.49% |
| **Native Chain** | Base (also Ethereum, Arbitrum) |
| **Categories** | Stablecoins, USD Stablecoin, Fiat-backed + Crypto-backed Stablecoin, Base Native |
| **Website** | [https://register.app/](https://register.app/) |

---

## Risks

- **Collateral / backing risk:** Peg integrity depends on the value and liquidity of the underlying collateral basket. Any tokenized real-world collateral carries off-chain/issuer dependency; volatile crypto collateral carries market risk (mitigated by overcollateralization and the backstop layer).
- **Depeg risk:** Stablecoins can trade below $1 in stress, redemption queues, or collateral impairment. eUSD's historical extremes ($0.867 ATL in March 2024; $1.13 ATH in April 2024) show it has experienced volatility around the peg in the past; the current ~$0.9966 is well within normal bands.
- **Backstop-adequacy risk:** the staked first-loss buffer protects holders only up to its size; a large, simultaneous collateral impairment could exceed it.
- **Smart-contract / protocol risk:** Reserve Protocol mechanics, the RToken contracts, and bridges across Base/Ethereum/Arbitrum each introduce technical risk.
- **Liquidity risk:** Secondary liquidity is moderate; large redemptions rely on the protocol's mint/redeem path against collateral.
- **Regulatory risk:** USD stablecoin regulation continues to evolve and could affect issuance, collateral, or redemption.

---

## Trading / Usage Playbook

- **Use case:** a transparent, basket-backed on-chain dollar for DeFi users who want verifiable collateral over off-chain attestations; not a high-liquidity trading pair.
- **What to watch:** the composition and health of the collateral basket; the size of the staked backstop relative to supply; the eUSD secondary price vs $1 (depeg signal given moderate liquidity); any basket collateral that is a tokenized RWA (off-chain dependency).
- **Risk-off framing:** in Extreme Fear, prefer redeeming/arbitraging against the basket over selling into thin DEX pools; basket transparency is eUSD's main advantage precisely when off-chain reserve confidence is shaky.

---

## See Also

- [[stablecoin]]
- [[real-world-assets]]
- [[tokenization]]
- [[treasuries]]
- [[dai]]
- [[usdc]]
- [[depeg]]
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). General market knowledge on Reserve Protocol and eUSD; no additional specific wiki source ingested yet.


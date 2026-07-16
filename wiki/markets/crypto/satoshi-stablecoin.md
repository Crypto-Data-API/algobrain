---
title: "Satoshi Stablecoin"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [bitcoin, crypto, stablecoins]
aliases: ["River satUSD", "SATUSD", "Satoshi Stablecoin", "satUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://river.inc"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[dai]]", "[[stablecoin]]", "[[stablecoins]]", "[[usdc]]"]
---

# Satoshi Stablecoin

**Satoshi Stablecoin** (SATUSD / satUSD) is a crypto-collateralized, chain-abstracted US-dollar [[stablecoin]] issued by **River** (formerly Satoshi Protocol), targeting a 1 USD peg. It is built around an "omni-CDP" (collateralized-debt-position) model: users can deposit collateral on one chain and mint satUSD on another **without bridging the underlying assets**, enabling cross-chain collateral, yield, and liquidity. Given River's roots and deployments, the design is oriented toward **[[bitcoin]]-backed collateral**. It is deployed natively across BOB Network, [[ethereum|Ethereum]], Base, Arbitrum, BNB Chain, Sonic, Bitlayer, BEVM, BSquared, and Hemi — several of which are Bitcoin-aligned L2s.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | SATUSD |
| **Price** | $0.994731 |
| **Market cap** | $158.4M |
| **Market-cap rank** | #202 |
| **24h volume** | $1,371 |
| **24h change** | +0.06% |
| **Circulating supply** | 159.20M SATUSD |
| **Total supply** | 159.20M SATUSD |
| **All-time high** | $1.68 |
| **All-time low** | $0.635574 |

Circulating supply equals total supply (market-cap / FDV ≈ 1.00). Price sits just under peg (~$0.995), but 24h volume is extremely thin (~$1.4K).

---

## Architecture: omni-CDP peg & backing mechanism

satUSD is a **crypto-overcollateralized stablecoin** in the [[dai]] lineage, with a distinctive **cross-chain ("omni-CDP")** twist:

- **Omni-CDP minting.** A user locks collateral in a CDP on **Chain A** and mints satUSD on **Chain B** *without moving the collateral across a bridge*. River's chain-abstraction layer coordinates the position — tracking the collateral, the debt, and the health factor across ecosystems — so the user gets dollar liquidity where they want it while the collateral stays put on its home chain. This avoids the classic bridge-custody risk of locking-and-wrapping collateral, at the cost of a more complex coordination/oracle layer.
- **Collateral.** Given River's positioning and its Bitcoin-L2 deployments (Bitlayer, BEVM, BSquared, Hemi, BOB), the design centers on using crypto — including **BTC-aligned assets** — as collateral, in the overcollateralized spirit of [[dai]]. Each satUSD is intended to be backed by more than $1 of crypto collateral.
- **Peg defense.** The 1 USD target is defended by (1) overcollateralization, (2) liquidation of unhealthy positions when their collateral ratio breaches the threshold, and (3) mint/redeem arbitrage. 1 satUSD is intended to be redeemable for ~$1 of crypto collateral via the protocol's redemption mechanism, which is the hard floor that anchors the market price.
- **Use cases.** Beyond holding a synthetic dollar, satUSD is designed for **earning, leverage, and scaling liquidity natively across multiple chains** — e.g. a Bitcoin holder can borrow dollars against BTC-aligned collateral and deploy them on a different chain without selling the BTC.

The wide historical range (ATH $1.68, ATL $0.635574) indicates the token has experienced significant peg deviation in both directions during its history. No third-party reserve attestation is referenced in the source data — as expected for a crypto-collateralized CDP design, where collateral is **verifiable on-chain** rather than via off-chain audit.

### Why the BTC-collateral angle matters

Most large stablecoins are backed by fiat reserves ([[usdc]], [[usdt]]) or ETH-centric crypto collateral ([[dai]]). satUSD's differentiator is letting the enormous, mostly idle **Bitcoin** collateral base be used productively to mint dollars, via Bitcoin L2s, without giving up BTC exposure or trusting a centralized custodian. This is the same thesis behind other Bitcoin-backed dollar projects, and it ties satUSD's collateral health directly to BTC's price (≈ $64,568 as of 2026-06-22) and to the maturity of the young Bitcoin-L2 stack it relies on.

---

## Comparison vs peer crypto-collateralized & BTC-backed dollars

| Token | Collateral base | Cross-chain model | Peg at snapshot | Issuer |
|---|---|---|---|---|
| **satUSD** | Crypto, incl. BTC-aligned (overcollateralized) | **Omni-CDP** (collateral chain A, mint chain B, no bridge) | ~$0.995 | River (ex-Satoshi Protocol) |
| [[dai]] | ETH-centric crypto + RWA + PSM | Single-chain mint, bridged token | ~$1.00 | MakerDAO / Sky |
| [[helio-protocol-hay\|Lista USD]] | Crypto-collateralized CDP | Single-chain (BNB ecosystem) | ~$1.00 | Lista DAO |
| [[usdc]] | Fiat reserves (cash + T-bills) | Native multi-chain issuance | ~$1.00 | Circle |

Versus [[dai]] and Lista USD, satUSD's claimed edge is the **omni-CDP** chain-abstraction — collateral and mint can live on different chains without bridging — and its **Bitcoin-collateral orientation**. Versus fiat-backed [[usdc]], the trade-off is the usual one: decentralization and on-chain verifiability in exchange for collateral-volatility and liquidation risk, plus, here, the added novelty risk of the cross-chain coordination layer.

---

## How & where it trades

satUSD is multi-chain, with its native chain listed as **BOB Network** and an Ethereum deployment at `0x1958853a8be062dc4f401750eb233f5850f0d0d2`. The only listing in the source data is a **DEX** pool — Uniswap V3 on Ethereum (satUSD vs [[usdt]]). Reported 24h volume is very low (~$1,371), so secondary-market liquidity is thin; most satUSD is likely held within the River protocol as CDP-minted dollars and deployed for yield/leverage rather than spot-traded. As with other thin CDP dollars, the on-chain redemption path — not secondary DEX depth — is what holders should rely on to realize ~$1.

---

## Narrative & catalysts

satUSD sits at the intersection of two narratives: the **crypto-collateralized stablecoin** revival and the **"BitcoinFi" / Bitcoin-L2 DeFi** buildout (Bitlayer, BEVM, BSquared, Hemi, BOB). Its thesis is that Bitcoin's vast collateral base should be able to mint dollars productively across chains. Catalysts that would matter: growth and security maturation of the Bitcoin-L2 ecosystems it depends on; adoption of the omni-CDP as a borrowing primitive by BTC holders; and deeper secondary liquidity to make satUSD usable as a settlement/collateral asset. In the current bottoming/accumulation macro regime (Fear & Greed 21, "Extreme Fear", as of 2026-06-22) and with BTC near $64.5K, collateral-value pressure is the key thing to watch for any BTC-backed CDP dollar.

---

## History / timeline

- **Earlier history** — launched as **Satoshi Protocol**, a Bitcoin-collateralized stablecoin project, later rebranded to **River**.
- **All-time high $1.68 / all-time low $0.635574** — the historical band shows large peg deviations in both directions, characteristic of a young, thinly-traded CDP dollar (exact dates not in the snapshot, so not asserted here).
- **2026-06-21** — snapshot: ~$0.995, ~$1.4K daily volume, ~$158M market cap, rank #202; native chain BOB, multi-chain deployment across 10+ networks including several Bitcoin L2s.

---

## Risks

- **De-peg risk.** Currently a touch under peg (~$0.995); the historical ATL of $0.635574 shows it can deviate sharply, and overcollateralized stablecoins depend on healthy collateral and functioning liquidations.
- **Cross-chain / omni-CDP risk.** The chain-abstraction design (collateral on one chain, mint on another) introduces coordination and oracle complexity; a fault in that machinery — stale prices, desynchronized state, or a coordination-layer exploit — is a **novel failure mode** versus single-chain CDPs.
- **Collateral / Bitcoin-L2 risk.** Exposure to younger Bitcoin L2s (Bitlayer, BEVM, BSquared, Hemi, BOB) adds smart-contract, bridge, and ecosystem-maturity risk; a fault on a collateral chain can impair backing on a mint chain.
- **Liquidation-cascade risk.** Because collateral is volatile crypto (BTC-aligned), a sharp BTC drawdown can push many positions below threshold at once; if liquidations cannot clear (thin liquidity, scarce arbitrage capital), the peg can break downward.
- **Liquidity risk.** Near-zero reported volume means exiting a position at quoted prices is difficult; price discovery is fragile.
- **Issuer / governance risk.** Depends on River's continued development, parameterization, and the integrity of the redemption mechanism.
- **Regulatory risk.** Evolving stablecoin rules may affect issuance and listings.

---

## Trading / usage playbook

- **Use the redemption path, not the DEX, for size.** With ~$1.4K daily secondary volume, rely on the protocol's CDP redemption (~$1 of collateral per satUSD) to realize value; the Uniswap pool is for small clips only.
- **Watch BTC and collateral health.** As a BTC-oriented CDP dollar, satUSD's solvency tracks Bitcoin's price; in a falling-BTC regime, monitor system collateralization and liquidation activity before treating satUSD as a safe dollar.
- **Borrowers: keep a wide health-factor buffer.** If using the omni-CDP to borrow against BTC-aligned collateral, the cross-chain coordination and volatile collateral argue for a conservative loan-to-value to avoid being liquidated in a cascade.
- **Prefer it where its edge applies.** satUSD is most useful to a Bitcoin holder who wants dollar liquidity on another chain without selling BTC; for a plain liquid dollar, [[usdc]]/[[usdt]]/[[dai]] are deeper and simpler.

---

## Related

- [[dai]] — the canonical crypto-overcollateralized stablecoin (closest design analog)
- [[stablecoin]] / [[stablecoins]] — category overview
- [[bitcoin]] — relevant given River's Bitcoin-L2 deployments and BTC collateral orientation
- [[usdc]] — fiat-backed peer (for peg-stability contrast)
- [[helio-protocol-hay|Lista USD]] — another crypto-collateralized peer
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SATUSD |
| **Market Cap Rank** | #192 |
| **Market Cap** | $158.64M |
| **Current Price** | $0.9940 |
| **Categories** | Stablecoins, USD Stablecoin, Crypto-backed Stablecoin, Base Native |
| **Website** | [https://river.inc](https://river.inc) |

---

## Overview

River is building a chain-abstraction stablecoin system that enables cross-chain collateral, yield, and liquidity—all without bridging. 

Powered by the omni-CDP stablecoin satUSD, users can earn, leverage, and scale across different ecosystems natively. 

River features the first omni-CDP module that allows users to collateralize assets on Chain A and mint stablecoin satUSD on Chain B—without bridging the assets.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 159.20M SATUSD |
| **Total Supply** | 159.20M SATUSD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $158.64M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.68 (2025-02-22) |
| **Current vs ATH** | -40.63% |
| **All-Time Low** | $0.6356 (2024-07-21) |
| **Current vs ATL** | +56.77% |
| **24h Change** | -0.01% |
| **7d Change** | +0.00% |
| **30d Change** | +0.07% |
| **1y Change** | -0.43% |

---

## Platform & Chain Information

**Native Chain:** Bob Network

### Contract Addresses

| Chain | Address |
|---|---|
| Bob Network | `0xecf21b335b41f9d5a89f6186a99c19a3c467871f` |
| Sonic | `0xb4818bb69478730ef4e33cc068dd94278e2766cb` |
| Bsquared Network | `0x8dd8b12d55c73c08294664a5915475ed1c8b1f6f` |
| Bitlayer | `0xba50ddac6b2f5482ca064efac621e0c7c0f6a783` |
| Bevm | `0x2031c8848775a5efb7cff2a4edbe3f04c50a1478` |
| Base | `0x70654aad8b7734dc319d0c3608ec7b32e03fa162` |
| Binance Smart Chain | `0xb4818bb69478730ef4e33cc068dd94278e2766cb` |
| Ethereum | `0x1958853a8be062dc4f401750eb233f5850f0d0d2` |
| Arbitrum One | `0xb4818bb69478730ef4e33cc068dd94278e2766cb` |
| Hemi | `0xb4818bb69478730ef4e33cc068dd94278e2766cb` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X1958853A8BE062DC4F401750EB233F5850F0D0D2/0XDAC17F958D2EE523A2206206994597C13D831EC7 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://river.inc](https://river.inc) |
| **Twitter** | [@RiverdotInc](https://twitter.com/RiverdotInc) |
| **Telegram** | [river_inc](https://t.me/river_inc) (40,568 members) |
| **Discord** | [https://discord.com/invite/river-inc](https://discord.com/invite/river-inc) |
| **GitHub** | [https://github.com/Satoshi-Protocol](https://github.com/Satoshi-Protocol) |
| **Whitepaper** | [https://docs.river.inc/](https://docs.river.inc/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1,844.35 |
| **Market Cap Rank** | #192 |
| **24h Range** | $0.9924 — $0.9964 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]

---

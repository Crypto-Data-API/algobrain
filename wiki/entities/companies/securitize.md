---
title: "Securitize"
type: entity
created: 2026-07-19
updated: 2026-09-06
status: good
tags: [company, real-world-assets, institutional, compliance]
aliases: ["Securitize Inc.", "Securitize Markets"]
entity_type: company
founded: 2017
website: "https://securitize.io"
related: ["[[blackrock-usd-institutional-digital-liquidity-fund]]", "[[securitize-tokenized-aaa-clo-fund]]", "[[apollo-diversified-credit-securitize-fund]]", "[[vaneck-treasury-fund]]", "[[tokenization]]", "[[real-world-assets]]", "[[tokenized-treasuries]]", "[[blackrock]]"]
---

# Securitize

**Securitize** is a tokenization platform for real-world assets (RWAs) founded in 2017, best known as the tokenization agent and transfer agent for **BlackRock's BUIDL** — the fund that helped legitimize the entire tokenized-Treasury sector. Unlike an unregistered crypto token issuer, Securitize positions itself as **regulated market infrastructure**: it operates as an SEC-registered transfer agent and runs a broker-dealer/alternative-trading-system (ATS) affiliate (Securitize Markets), putting it inside the same securities-law perimeter that governs traditional transfer agents and private-securities marketplaces rather than outside it. This regulatory posture — infrastructure provider operating under securities law, not an issuer selling unregistered tokens to retail — is what has let major traditional asset managers work with Securitize to bring funds on-chain.

## Business Model: Tokenization and Transfer-Agent Infrastructure

Securitize does not typically manage the underlying assets in the products it tokenizes; it provides the layer that turns a traditional fund interest into an on-chain token and keeps the on-chain record synchronized with the legal ownership register:

- **Tokenization** — minting a blockchain-native token that represents a fractional claim on a fund or asset, using permissioned token standards rather than freely-transferable ERC-20s.
- **Transfer agency** — Securitize's SEC-registered transfer-agent role means it maintains the official register of who owns what, mint/redemption at the fund's published NAV, and enforces a whitelist so tokens only move between KYC/AML-screened, eligible holders.
- **Primary-market distribution** — Securitize Markets, the broker-dealer/ATS affiliate, handles subscription and (where permitted) secondary transfers among eligible investors under securities-law exemptions (Reg D for U.S. accredited/qualified investors, Reg S for non-U.S. investors).

This is the **off-chain custody / SPV** custody model described in the wiki's [[tokenization]] concept page: the underlying asset (Treasuries, private credit, a CLO tranche) is held by a regulated custodian or fund structure, and the token is a claim on that structure enforced by a combination of smart-contract allowlisting and traditional securities law — not a fully trustless, code-only claim the way a liquid-staking token is.

## Flagship Products

Securitize's track record spans several of the largest tokenized real-world-asset products on the wiki:

- **[[blackrock-usd-institutional-digital-liquidity-fund|BlackRock BUIDL]]** — launched March 2024, a tokenized money-market fund holding cash, U.S. Treasury bills, and repo, with Securitize as tokenization and transfer agent and BNY Mellon providing custody/administration. BUIDL was the largest tokenized Treasury fund through most of 2024-2025 (peaking near $2.9B) before being overtaken by a competitor in early 2026; see the BUIDL page for the full detail.
- **[[securitize-tokenized-aaa-clo-fund|Securitize Tokenized AAA CLO Fund (STAC)]]** — a tokenized fund giving exposure to AAA-rated U.S.-dollar CLO tranches, with servicing and custody by BNY.
- **[[apollo-diversified-credit-securitize-fund|Apollo Diversified Credit Securitize Fund (ACRED)]]** — a tokenized feeder fund into Apollo Global Management's diversified private-and-public-credit strategy, notable as an early example of a tokenized private-credit product used as on-chain collateral in permissioned DeFi.
- Securitize has also tokenized products for other traditional managers, including a VanEck tokenized Treasury fund (see [[vaneck-treasury-fund]]).

Across these products, Securitize's role is consistent: it is the tokenization/transfer-agent layer, while the underlying asset management is done by the traditional manager (BlackRock, Apollo, VanEck) and custody/servicing is often provided by a separate institutional custodian (BNY Mellon in BUIDL's and STAC's case). Per a mid-2026 RWA.xyz snapshot cited on the BUIDL page, the Securitize platform carried roughly $2.5B in assets across four RWA products.

## How the Products Actually Trade

A defining feature of Securitize-tokenized products is that they are **not freely tradable retail tokens**. Transfers are restricted to Securitize-whitelisted, KYC'd wallets at the smart-contract level, minimums are institutional (BUIDL launched with a $5M minimum), and secondary-market volume on BUIDL, STAC, and ACRED is effectively zero — liquidity runs through Securitize's own subscription/redemption pipe (plus, for BUIDL specifically, a Circle-operated USDC instant-redemption facility) rather than an open order book. This is the direct consequence of operating under securities-law exemptions instead of issuing a freely transferable token: compliance is enforced by the allowlist, not by market access restrictions alone.

## Regulatory Significance

Securitize is the wiki's clearest example of the **securities-law-compliant tokenization model** described in [[real-world-assets]] and [[tokenization]]: transfers restricted to whitelisted wallets, security-token standards rather than plain ERC-20s, and a compliance layer (KYC/AML, Reg D/Reg S) built into the token itself rather than left to individual venues. As of the Q1-Q2 2026 estimates cited on [[real-world-assets]], tokenized RWAs excluding stablecoins totaled roughly $26-31B, with tokenized Treasuries/money-market funds — the category Securitize's BUIDL, STAC, and VanEck products sit in — the single largest bucket. Securitize's ability to bring BlackRock, Apollo, and BNY Mellon into the same on-chain structure is repeatedly cited across this wiki as the moment that gave the RWA tokenization thesis institutional credibility, distinct from earlier, less regulated attempts at asset tokenization.

## Trading and Investing Relevance

Securitize itself does not have a publicly traded token; exposure to its business is indirect, through the products it tokenizes (BUIDL, STAC, ACRED, and others) or through the broader RWA-tokenization narrative that these products anchor. Because its flagship products carry effectively zero secondary-market volume and a flat or slowly NAV-accruing price by design, they function as **sector barometers and narrative drivers** rather than directional trading instruments — AUM growth or contraction across Securitize's platform is the more meaningful signal than any on-chain price action. See [[blackrock-usd-institutional-digital-liquidity-fund]] for how this plays out concretely, including the competitive dynamic against rival tokenized-Treasury issuers.

## Related

- [[blackrock-usd-institutional-digital-liquidity-fund]] — Securitize's flagship tokenization client (BUIDL)
- [[securitize-tokenized-aaa-clo-fund]] — Securitize-tokenized AAA CLO fund, serviced by BNY
- [[apollo-diversified-credit-securitize-fund]] — Securitize-tokenized Apollo private-credit feeder fund
- [[vaneck-treasury-fund]] — another Securitize-tokenized Treasury product
- [[tokenization]] — the general mechanism, including the off-chain custody/SPV model Securitize's products use
- [[real-world-assets]] — the broader RWA category and market-size context
- [[tokenized-treasuries]] — the specific product category most of Securitize's flagship funds sit in
- [[blackrock]] — asset manager behind BUIDL

## Sources

- [[blackrock-usd-institutional-digital-liquidity-fund]], [[securitize-tokenized-aaa-clo-fund]], [[apollo-diversified-credit-securitize-fund]] — wiki entity pages for Securitize's role, product structure, custody arrangements, and permissioning/whitelist mechanics
- [[tokenization]], [[real-world-assets]] — wiki concept pages cross-checked for the off-chain custody/SPV model and RWA market-size figures
- General knowledge of Securitize's 2017 founding and its SEC-registered transfer-agent / broker-dealer (Securitize Markets) structure, cross-checked against the cited wiki pages; exact registration dates and entity-level regulatory detail are not independently verified here — confirm against Securitize's own regulatory disclosures before relying on them

---
title: "Paxos"
type: entity
created: 2026-07-19
updated: 2026-09-06
status: good
tags: [company, stablecoins, regulation, compliance, institutional]
aliases: ["Paxos Trust Company", "Paxos Trust"]
entity_type: company
founded: 2012
headquarters: "New York, USA"
website: "https://www.paxos.com"
related: ["[[paxos-standard]]", "[[pyusd]]", "[[binance-usd]]", "[[global-dollar]]", "[[stablecoins]]", "[[mica]]", "[[stablecoin-regulation]]", "[[real-world-assets]]", "[[2023-02-busd-wind-down]]"]
---

# Paxos

**Paxos** (formally **Paxos Trust Company, LLC**) is a regulated blockchain infrastructure firm chartered as a **limited-purpose trust company** by the New York State Department of Financial Services (NYDFS), operating in stablecoin issuance, tokenized-asset settlement, and white-label crypto brokerage infrastructure. Paxos was founded in 2012 (originally as itBit) and has since built its business model around operating strictly inside a state-regulated trust-company perimeter rather than offshore — issuing **USDP** (Pax Dollar), **PYUSD** (for PayPal), and formerly **BUSD** (for Binance, wound down by regulatory order in 2023). For traders and researchers, Paxos is the wiki's clearest example of the "regulated-issuer" model that frameworks like the EU's [[mica|MiCA]] are explicitly designed around.

## Regulatory Foundation: the NYDFS Trust Charter

Paxos's entire business rests on its **NYDFS limited-purpose trust charter**, a New York state banking-law license that is distinct from a federal bank charter. The charter subjects Paxos to:

- **Reserve and custody rules** — assets held on behalf of token holders or clients must be segregated under New York trust law, not commingled with Paxos's own operating funds.
- **Capital and examination requirements** — NYDFS sets minimum capital standards and can examine Paxos's books, controls, and reserve composition at will.
- **AML/KYC obligations** — standard anti-money-laundering and know-your-customer compliance for a regulated financial institution.
- **Direct regulatory authority to compel action** — as the BUSD case below demonstrates, NYDFS can order Paxos to alter or halt a specific product line without a court process.

This is the same regulatory wrapper documented in more depth on [[paxos-standard]] and [[pyusd]], and it is the reason Paxos is repeatedly cited across this wiki as one of the more heavily regulated stablecoin issuers, alongside Circle. See [[stablecoin-regulation]] for how the NYDFS model compares to other jurisdictions' stablecoin regimes.

## Stablecoin Issuance History

Paxos has issued or currently issues several major dollar stablecoins, each under the same trust-charter wrapper:

- **[[paxos-standard|USDP (Pax Dollar)]]** — launched September 2018 as **Paxos Standard (PAX)**, one of the first NYDFS-approved dollar stablecoins (alongside Gemini's GUSD in the same 2018 cohort). Rebranded from PAX to USDP in 2021. Backed by cash and short-dated U.S. Treasuries with monthly third-party attestations.
- **[[binance-usd|BUSD]]** — a white-label stablecoin Paxos issued for [[binance|Binance]] starting in 2019, which scaled to roughly $23B in circulation at its 2022 peak before being wound down (see below).
- **[[pyusd|PYUSD (PayPal USD)]]** — launched August 2023, issued by Paxos on behalf of PayPal. The first stablecoin issued by a major U.S. financial-services company, trading on Ethereum and Solana with reserves in cash and short-dated Treasuries.
- **Global Dollar (USDG)** — Paxos is a participant in the Global Dollar Network, a more recent multi-issuer stablecoin initiative; see [[global-dollar]] for the token-level detail.

Across all of these, the mechanism is identical: fiat-collateralized, 1:1 reserve-backed, custodial stablecoins with a direct mint/redeem path at par for onboarded institutions, monthly independent attestations, and full issuer discretion to freeze or blacklist tokens for compliance reasons.

## The BUSD Wind-Down: a Regulatory Case Study

Paxos's most consequential regulatory episode is the **BUSD wind-down**, which the wiki treats as a canonical case study in [[2023-02-busd-wind-down]]. On **February 13, 2023**, two separate regulatory actions landed on the same day:

1. The **SEC issued a Wells Notice** to Paxos signaling intent to pursue enforcement, alleging BUSD was an unregistered security.
2. **NYDFS ordered Paxos to halt minting new BUSD**, citing unspecified concerns about Paxos's oversight of the Binance relationship.

Unlike a reserve-solvency crisis, BUSD's backing was never in question — the action was about licensing and classification, not whether the dollars existed. Paxos kept redemptions open throughout, and BUSD circulation declined gradually over 2023-2024 (from roughly $16B to under $1B) as users migrated to USDC, USDT, and FDUSD, rather than suffering a panic depeg. The SEC's case was later dropped. This episode is the wiki's clearest illustration that NYDFS can compel a regulated issuer to materially change a specific product line by administrative order — a regulatory-authority fact directly relevant to how [[stablecoin-regulation]] and [[mica]] frame the trade-off a regulated issuer accepts in exchange for legitimacy and market access.

## Tokenization and Settlement Business

Beyond stablecoin issuance, Paxos operates infrastructure for **tokenized-asset settlement and white-label crypto brokerage** — providing the custody, trading, and settlement rails that let non-crypto-native companies offer crypto buying, selling, and holding to their own users without building the infrastructure themselves. PayPal and Venmo's in-app crypto features are the most visible example of this brokerage-infrastructure business, running alongside (but distinct from) Paxos's role as PYUSD's issuer. This positions Paxos similarly to [[securitize|Securitize]] in spirit — a regulated intermediary that lets other companies bring assets on-chain inside a compliant wrapper — though Paxos's core focus is payment stablecoins and brokerage rails rather than Securitize's tokenized-fund/RWA securities model.

## Regulatory Significance

Paxos is a useful reference point for the two major stablecoin-regulation frameworks this wiki covers in depth:

- **US state-level regulation** — Paxos operates entirely inside the NYDFS trust-charter perimeter, the strictest state-level regime in the US as documented in [[stablecoin-regulation]]. The BUSD episode is direct evidence of that regime's teeth.
- **MiCA-style EU frameworks** — [[mica|MiCA]]'s E-Money Token (EMT) rules require a licensed credit institution or Electronic Money Institution, 1:1 reserves with a minimum share in bank deposits, independent audits, and a redemption right at par. Paxos's USDP/PYUSD model already satisfies the substance of those requirements under a different (US state trust) regulatory label — making Paxos a useful real-world example of what a MiCA-compliant EMT issuer's reserve and governance practices look like in practice, even though Paxos's US products are not themselves MiCA-licensed.

## Related

- [[paxos-standard]] — USDP (Pax Dollar), the original Paxos-issued stablecoin
- [[pyusd]] — PayPal's stablecoin, issued by Paxos
- [[binance-usd]] — BUSD, the wound-down Paxos-for-Binance stablecoin
- [[global-dollar]] — Global Dollar Network (USDG), a newer multi-issuer initiative Paxos participates in
- [[2023-02-busd-wind-down]] — detailed case study of the February 2023 SEC/NYDFS action
- [[stablecoin-regulation]] — US state-level and global stablecoin regulatory comparison
- [[mica]] — EU framework Paxos's reserve/audit practices parallel
- [[securitize]] — comparable regulated-intermediary model for tokenized RWAs rather than stablecoins
- [[stablecoins]] — the broader asset class

## Sources

- [[paxos-standard]], [[pyusd]], [[binance-usd]] — wiki entity pages for issuer history, reserve model, and regulatory wrapper detail
- [[2023-02-busd-wind-down]] — wiki news page verifying the February 13, 2023 SEC Wells Notice and NYDFS minting-halt date, the "no panic depeg" outcome, and the circulation decline timeline
- [[mica]], [[stablecoin-regulation]] — wiki concept pages cross-checked for the EMT/regulated-issuer framing
- General knowledge of Paxos's 2012 founding (as itBit) and NYDFS trust-chartered structure, cross-checked against the cited wiki pages; the precise founding/rebrand timeline and the brokerage-infrastructure client list (PayPal, Venmo) reflect well-documented public history but no single external source document has been ingested for this page — confirm current details against Paxos's own disclosures before relying on them

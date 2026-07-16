---
title: "BRLA Digital BRLA"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, forex, stablecoin]
aliases: ["BRLA"]
entity_type: protocol
headquarters: "Brazil (BRLA Digital)"
website: "https://brla.digital/"
related: ["[[brazilian-real]]", "[[brz]]", "[[crown-brlv]]", "[[crypto-markets]]", "[[depeg]]", "[[forex]]", "[[polygon]]", "[[stablecoin]]"]
---

# BRLA Digital BRLA

**BRLA Digital BRLA** (BRLA) is a fiat-backed [[stablecoin]] that tracks the **[[brazilian-real|Brazilian real]] (BRL)**, not the US dollar. Issued by **BRLA Digital**, it is designed primarily for **B2B cross-border payments and on/off-ramps**, and is marketed as the only **audited** BRL stablecoin — a compliance-first competitor to [[brz|BRZ]] and [[crown-brlv|Crown BRLV]] inside Brazil's on-chain economy.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

## Why the ~$0.19 USD price is the peg, not a depeg

BRLA is pegged to **one Brazilian real**, and one real is currently worth roughly **0.19 US dollars** on the [[forex]] market (about 5.2 reais per dollar). A USD-denominated quote of **$0.192626** for BRLA therefore reflects the BRL/USD exchange rate and indicates the peg is **holding correctly** — it is **not** a depegged dollar stablecoin. On-peg means ~1.00 **real** per BRLA, so judge it against BRL, not USD. This is the same FX framing as its peers [[brz]] and [[crown-brlv]], and as [[frankencoin]] (Swiss franc). A true depeg would show as a gap between BRLA's price and the live BRL/USD rate.

## Market Snapshot (2026-06-21)

| Field | Value |
|---|---|
| **Ticker** | BRLA |
| **Price (USD)** | $0.192626 (≈ 1.00 BRL — on peg) |
| **Market Cap Rank** | #516 |
| **Market Cap** | $40,845,434 |
| **24h Change** | -0.06% |
| **7d Change** | -1.91% |
| **Currency tracked** | Brazilian real (BRL) |

The 24h/7d changes in USD terms (-0.06% / -1.91%) primarily reflect the BRL/USD exchange rate, not a move off the real peg.

## Issuer & Jurisdiction

BRLA is issued by **BRLA Digital**, a Brazil-based fintech focused on regulated stablecoin infrastructure and cross-border payments. The project emphasizes compliance and auditing, marketing BRLA as **the only audited BRL stablecoin** for businesses needing reliable on/off-ramps. It is deeply integrated with Brazil's **[[pix|Pix]]** instant-payment system, allowing fiat reais to flow directly to and from the token. The token is deployed primarily on [[polygon]], with additional deployments on Gnosis Chain (xDai), Celo, Moonbeam, Base, and [[ethereum|Ethereum]] — a broad EVM footprint aimed at meeting clients on whichever chain they already use.

## Architecture — How It Works

### Reserve & collateral model
BRLA is a **fiat-collateralised** stablecoin: each token is intended to be backed **1:1 by Brazilian reais held in reserve**, with reserve management handled by **Avenia**. The compliance and audit framing is the differentiator — where [[brz|BRZ]] leans on longevity/distribution and [[crown-brlv|BRLV]] on sovereign-bond backing in a bankruptcy-remote structure, BRLA's pitch is **auditability and KYC/KYB-grade onboarding** for corporate treasuries.

### Peg & redemption mechanism
The peg is held by **primary mint/redeem at par against BRL reserves** plus secondary arbitrage. Because BRLA is built around round-trip B2B settlement, the redemption path (reais out via Pix/banking) is a first-class feature rather than an afterthought, which strengthens the practical arbitrage that keeps the on-chain price near one real.

### Mint / redeem, KYC/KYB gating, on/off-ramp rails
- **Mint:** Businesses and verified users mint BRLA by depositing reais (often via Pix) through BRLA Digital's ramp after **KYC/KYB** onboarding.
- **Redeem:** BRLA is redeemed back to reais via the issuer's off-ramp, enabling round-trip BRL settlement for cross-border flows.
- **Rails:** Pix-connected fiat ramps are the core utility — convert BRL to on-chain BRLA, move/settle globally, and convert back.

## Tokenomics & Supply

BRLA is supply-elastic: circulating supply expands and contracts with mint/redeem demand from its payment and treasury users rather than following a fixed emission schedule. There is no fixed max supply and no native yield — a holder is simply long the real on-chain. Snapshot market cap was ~$40.8M (the USD value of the reais represented on-chain at the prevailing FX rate).

## Comparison vs Other BRL Stablecoins

| | **BRLA** | **[[brz\|BRZ]]** | **[[crown-brlv\|Crown BRLV]]** | **BRL1 / BBRL (peers)** |
|---|---|---|---|---|
| **Peg** | Brazilian real (BRL) | Brazilian real (BRL) | Brazilian real (BRL) | Brazilian real (BRL) |
| **Issuer** | BRLA Digital (Brazil) | Transfero Group (Brazil/Switzerland) | Crown (São Paulo) | Various (e.g. Banco Braza for BBRL) |
| **Reserve model** | BRL reserves (managed by Avenia) | BRL cash reserves | Brazilian government bonds (BRLY layer) | BRL reserves / bank-issued |
| **Differentiator** | Only **audited** BRL coin; B2B, Pix-native, KYC/KYB | Longevity, multi-chain breadth, exchange distribution | Institutional, bankruptcy-remote, sovereign-bond yield | Bank/network-specific distribution |
| **Primary chain(s)** | Polygon (+ Celo, Gnosis, Moonbeam, Base, ETH) | Multi-chain (ETH, BNB, SOL, Polygon, +) | Base (+ Ethereum) | Polygon |
| **Mkt cap (snapshot)** | ~$40.8M | ~$51.6M | ~$71.7M | smaller |

BRL stablecoins collectively (BRZ, BRLA, BRL1, etc.) have accounted for billions in historical on-chain volume, much of it routed through Polygon in Latin America.

## How & Where It Trades / Is Used

- **Primary use:** **Treasury and payment rails for companies** moving value in and out of Brazil — invoicing, supplier settlement, and FX-light cross-border transfers using on-chain BRL.
- **Payment corridors:** Brazil-inbound/outbound B2B flows, leaning on Pix for the fiat leg and EVM chains (Polygon especially) for the on-chain leg.
- **DeFi composability:** A standard fungible token across its EVM deployments, BRLA can be used in DEX pools and lending, though depth is thin relative to dollar majors.
- **Trading:** Limited centralised-exchange presence relative to BRZ; most liquidity and utility live on-chain and through the issuer's ramp.

## Narrative, Category & Catalysts

BRLA is a **regional / FX-denominated stablecoin** positioned at the **regulated B2B** end of the BRL market. Catalysts: growth in Brazil-linked cross-border commerce; maturation of **Pix** as a fiat on/off-ramp; the central bank's **Drex** (digital real) programme and evolving stablecoin licensing, where an "audited, compliant" coin is comparatively well-placed; and broader Latin-American stablecoin adoption on Polygon. The 2026 macro backdrop (Extreme Fear, bottoming/accumulation regime) compresses speculative liquidity but matters less for a payments-utility coin than for trading-driven tokens.

## History / Timeline

- BRLA Digital launched and grew the BRLA token as Brazil's on-chain BRL ecosystem expanded, deploying across Polygon, Celo, Gnosis, Moonbeam, Base, and Ethereum.

*(Specific dated launch events are not verified in available wiki sources and are deliberately omitted to avoid fabrication.)*

## Risks

- **FX risk for USD holders:** A USD-based holder is implicitly **long the Brazilian real** and exposed to BRL/USD [[forex]] volatility.
- **Issuer / reserve-counterparty risk:** Holders depend on BRLA Digital (and reserve manager Avenia) maintaining full reserves and honoring redemptions; audit/attestation quality is central to trust.
- **Regulatory risk:** Brazilian stablecoin and payments regulation (Drex, licensing) is evolving and could affect operations.
- **Redemption-gating risk:** B2B-grade KYC/KYB gating means par redemption is permissioned; access frictions can impair the arbitrage that holds the peg for non-onboarded holders.
- **Liquidity / depeg risk:** With ~$41M market cap and limited CEX presence, on-chain liquidity can be thin and prone to short-term [[depeg]] on large trades.
- **Smart-contract / multi-chain risk:** Contract or bridge issues across deployment chains could affect supply integrity.

## Trading / Usage Playbook

- **As FX exposure:** BRLA expresses a **long-BRL** view on-chain; USD P&L is dominated by BRL/USD, not by the (tight) peg.
- **On/off-ramp / treasury use:** Best suited to businesses with Brazil exposure — use Pix-connected mint/redeem for round-trip BRL settlement; expect KYC/KYB onboarding.
- **Peg monitoring:** "On-peg" = ~1.00 **real**, not $1.00. Watch for a gap vs the live BRL/USD rate as the depeg signal.
- **Sizing:** Thin secondary market — size to on-chain/ramp depth, not headline cap.

## See Also

- [[stablecoin]]
- [[brazilian-real]]
- [[forex]]
- [[brz]]
- [[crown-brlv]]
- [[pix]]
- [[crypto-markets]]
- [[polygon]]

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.


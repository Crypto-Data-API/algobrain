---
title: "Royal Dollar"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stablecoins]
aliases: ["RUSD"]
entity_type: protocol
headquarters: "Hong Kong (RIB Digital Holdings)"
website: "https://www.rcoins.digital/"
related: ["[[stablecoins]]", "[[crypto-markets]]", "[[ethereum]]", "[[usdt]]", "[[usdc]]", "[[royal-euro]]", "[[depeg]]"]
---

# Royal Dollar

**Royal Dollar** (ticker **RUSD**) is a fiat-backed, USD-referenced [[stablecoins|stablecoin]] issued by **RIB Digital Holdings Limited (Hong Kong)** under the **RCOINS** digital-asset brand. It targets a **1:1 peg to the US dollar** and is deployed across multiple chains — [[ethereum|Ethereum]], BNB Chain, and Tron — for payments, treasury operations, OTC trading, and exchange liquidity. As of the snapshot below it trades essentially on peg at ~$1.00. It is the dollar sibling of [[royal-euro|Royal Euro (REUR)]] within the same issuer family.

## Market data

| Field | Value |
|---|---|
| **Ticker** | RUSD |
| **Price** | $1.00 |
| **Market cap** | $250.06M |
| **Market-cap rank** | #142 |
| **24h volume** | $132.12M |
| **24h change** | +0.03% |
| **Circulating supply** | 250.00M RUSD |
| **Total supply** | 5.00B RUSD |
| **All-time high** | $1.002 (2026-03-20) |
| **All-time low** | $0.9979 (2026-04-24) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

## Issuer & ecosystem

RUSD is issued by **RIB Digital Holdings Limited**, the licensed/regulated digital division of the **Royal Investment Bank Group (RIB GROUP)** within the broader **RCCG Group**, headquartered in **Hong Kong**. It is one of three **RCOINS** Royal Stablecoins — **RUSD (USD), [[royal-euro|REUR]] (EUR), and RXAU (gold)** — sharing common issuance, reserve, and settlement infrastructure (the hybrid **RxBridge** instant-settlement ecosystem). The issuer markets **bank-grade, on-chain-verifiable proof-of-reserve** across the family.

## Architecture — Peg, backing & yield mechanism

Royal Dollar is presented as a **fiat-backed (off-chain reserve) stablecoin**, structurally similar to [[usdt]] and [[usdc]] rather than to crypto-collateralised designs like [[dai]] or yield synthetics like [[ethena-usde]]. The issuer states each RUSD is a "USD-referenced stable-value digital asset" backed by reserves held by RIB Digital Holdings, with proof-of-reserve published as part of the RCOINS model.

- **Reserve & collateral model:** off-chain USD reserves intended to cover circulating supply 1:1. Peg confidence depends on reserve quality, custody, and attestation cadence (see [[stablecoin-attestations]]).
- **Regulatory wrapper:** a single **Hong Kong** issuer under Hong Kong's evolving stablecoin/digital-asset regime; multi-chain issuance (incl. Tron) can attract additional scrutiny.
- **Peg & redemption mechanism:** maintained by primary mint (on receipt of USD) and 1:1 redemption, plus secondary arbitrage. RUSD itself is **not** marketed as a yield-bearing token — holders earn no native rebase or appreciation; any yield accrues to the issuer deploying reserves rather than to token holders.
- **Mint / redeem & KYC gating:** primary issuance/redemption runs through the issuer's permissioned, KYC-gated channel; secondary holders transact on-chain. Redemption mechanics, reserve composition, and attestation cadence are **not fully documented** in data available to this wiki, so — as with all opaque fiat-backed issuers — the peg ultimately depends on the issuer's ability and willingness to honour 1:1 redemptions.

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 250.00M RUSD |
| **Total Supply** | 5.00B RUSD |
| **Max Supply** | Unlimited |
| **Mkt cap / FDV** | circulating $250M vs 5.00B authorised |

Only **250M of an authorised 5.00B** supply circulates. For a deposit-backed coin this gap is an **authorisation ceiling, not latent dilution** — each circulating RUSD should map to one USD of reserve, and new tokens only enter on deposit. Supply is mint-on-deposit and elastic to redemption.

## Comparison vs Other USD Stablecoins

| | **RUSD** | **[[usdt\|USDT]]** | **[[usdc\|USDC]]** | **[[royal-euro\|REUR]] (sibling)** |
|---|---|---|---|---|
| **Peg** | US dollar | US dollar | US dollar | Euro |
| **Issuer** | RIB Digital Holdings (Hong Kong) | Tether | Circle | RIB Digital Holdings (Hong Kong) |
| **Reserve model** | Off-chain USD reserves, proof-of-reserve | USD cash + T-bills + other | USD cash + short T-bills | EUR reserves |
| **Transparency** | Issuer proof-of-reserve; limited public attestation in wiki data | Quarterly attestations | Monthly attestations, regulated | Issuer proof-of-reserve |
| **Chains** | Ethereum, BNB Chain, Tron | Multi-chain | Multi-chain | Ethereum, BNB Chain, Tron |
| **Mkt cap (snapshot)** | ~$250M | ~$100B+ | tens of billions | ~$17M |

RUSD is a **mid-small USD stablecoin** (rank ~#142) whose differentiator is the **RCOINS/RxBridge bank-issuer ecosystem**; the dollar majors dwarf it in liquidity and have far more mature attestation regimes.

## How & Where It Trades / Is Used

RUSD is a multi-chain token (Ethereum, BNB Chain, Tron). Reported 24h volume is **~$132M**, which is large relative to its $250M market cap — unusually high turnover for a stablecoin this size, consistent with use in **OTC/exchange liquidity routing** rather than purely passive holding. The CoinGecko snapshot does not surface a deep set of named centralised-exchange order books, so a meaningful share of that volume may be **off-book / OTC** within the RxBridge ecosystem. Traders should confirm live venue depth before sizing positions, as headline volume for newer stablecoins can be concentrated on a small number of pairs.

## Narrative, Category & Catalysts

RUSD sits in the **bank-issuer / proof-of-reserve USD stablecoin** category. Catalysts: demand for on-chain dollar settlement outside the USDT/USDC duopoly; build-out of the RxBridge fiat↔crypto settlement rails; and Hong Kong's maturing stablecoin licensing regime, which could either legitimise or constrain non-major issuers. Because RUSD is dollar-pegged, it does **not** carry the FX exposure that its euro sibling REUR does — its USD value should stay ~$1.00 regardless of the macro regime. The 2026 backdrop (Extreme Fear, bottoming/accumulation) primarily affects RUSD via overall stablecoin demand and liquidity, not its peg.

## History / Timeline

- **2026-03-20** — recorded all-time high of **$1.002**.
- **2026-04-24** — recorded all-time low of **$0.9979**.

The tight $0.998–$1.002 band indicates peg stability to date. *(Exact launch date is not verified in available wiki sources and is deliberately not stated. ATH/ATL dates are from the CoinGecko snapshot.)*

## Risks

- **De-peg risk:** Tight historical range ($0.998–$1.002) suggests stability to date, but a fiat-backed peg can break instantly if reserves are insufficient or redemptions are frozen ([[depeg]]).
- **Collateral / reserve-counterparty risk:** Reserve composition and custody are not transparently attested in available data; quality and liquidity of reserves are unverified here.
- **Issuer / custodial risk:** Single-issuer (RIB Digital Holdings, Hong Kong) centralised model — counterparty, governance, and solvency risk concentrate on one entity.
- **Redemption-gating risk:** Par redemption is KYC-gated and issuer-controlled; a freeze would break the arbitrage that holds the peg.
- **Regulatory risk:** Hong Kong stablecoin licensing regime is evolving; cross-chain (incl. Tron) issuance can attract additional scrutiny.
- **Liquidity / concentration risk:** High headline volume may mask thin or concentrated on-chain liquidity; large redemptions could move the peg.

## Trading / Usage Playbook

- **As a dollar instrument:** RUSD is a USD-peg token (no FX exposure, unlike sibling REUR) — useful for on-chain dollar settlement, but with **higher issuer/transparency risk** than USDT/USDC.
- **On/off-ramp use:** primary mint/redeem is KYC-gated through the issuer; for size, prefer the majors unless RxBridge access is the specific need.
- **Peg monitoring:** watch for any sustained deviation from $1.00 and for redemption-channel status; confirm venue depth before treating headline volume as liquidity.

## Platform & chain

Native chain: [[ethereum|Ethereum]]. Also issued on BNB Chain and Tron.

| Chain | Contract |
|---|---|
| Ethereum | `0x44bb433d29fe966992a9c812da7f252c9c53f285` |
| BNB Chain | `0x44bb433d29fe966992a9c812da7f252c9c53f285` |
| Tron | `TUvns399UpycBBpVsCVJLCjXFBjzHrNUR1` |

## See also

- [[stablecoins]] — category overview
- [[usdt]], [[usdc]] — peer fiat-backed stablecoins
- [[royal-euro]] — euro sibling (same issuer)
- [[dai]], [[ethena-usde]] — alternative peg designs
- [[stablecoin-attestations]]
- [[crypto-markets]]

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- General market knowledge; no specific wiki source ingested yet.

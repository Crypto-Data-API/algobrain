---
title: "Securitize Tokenized AAA CLO Fund"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, real-world-assets, stocks, tokenized-treasuries]
aliases: ["STAC", "Securitize Tokenized AAA CLO Fund"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.bny.com/corporate/global/en/about-us/newsroom/company-news/securitize-launches-tokenized-aaa-clo-fund-with-services-provided-by-bny-bringing-institutional-structured-credit-on-chain.html"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[real-world-assets]]", "[[securitize]]"]
---

# Securitize Tokenized AAA CLO Fund

**Securitize Tokenized AAA CLO Fund** (ticker **STAC**) is a tokenized [[real-world-assets|real-world-asset]] fund issued by **[[securitize|Securitize]]** that gives on-chain exposure to a diversified portfolio of **U.S.-dollar AAA-rated Collateralized Loan Obligation (CLO) tranches** — the highest-quality, most senior slice of the CLO capital structure. Servicing and custody are provided by **BNY (The Bank of New York Mellon)**, one of the world's largest custodian banks, bringing institutional structured credit on-chain. Token value **accrues with the fund's NAV** (price-accretion, non-rebasing) as CLO income compounds. It is issued on [[ethereum|Ethereum]].

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | STAC |
| **Issuer / wrapper** | Securitize (fund); servicing & custody by BNY |
| **Underlying** | Diversified portfolio of AAA-rated USD CLO tranches |
| **Current price** | $1,020.95 |
| **Market cap** | $102.30M |
| **Market cap rank** | #266 |
| **24h volume** | $0 (no secondary on-chain volume at snapshot) |
| **24h change** | -0.02% |
| **Circulating supply** | ~100,198 STAC |
| **Total supply** | ~100,198 STAC |
| **All-time high** | $1,023.81 (2026-06-10) |
| **All-time low** | $997.66 (2026-02-06) |
| **Chain** | Ethereum |

> The narrow, gently rising price range (~$998 to ~$1,024) is typical of a high-grade, yield-accruing credit fund where NAV creeps up with income rather than swinging with crypto prices. **The price reflects administratively-set fund NAV, not a market order book** — the relevant disclaimer is NAV/valuation integrity and redemption access, not crypto-cycle volatility.

---

## How It Works (Architecture Deep Dive)

STAC is a **tokenized fund share** representing exposure to a managed pool of senior, AAA-rated CLO tranches — securitized pools of senior secured corporate loans.

- **Fund structure & manager:** **Securitize** issues and tokenizes the fund interest and acts as the transfer-agent / primary-market layer. **BNY** provides institutional **servicing and custody** for the underlying assets — a notable feature, as a top-tier custodian bank servicing an on-chain fund lends institutional credibility.
- **Underlying assets:** **AAA-rated USD CLO tranches** — the highest-quality, most senior slice of the CLO capital structure, sitting above mezzanine and equity tranches. AAA CLO tranches are historically associated with very low default rates (no AAA CLO tranche has ever defaulted in the modern era, per industry data) and yields competitive with similarly rated corporate bonds.
- **Custody / servicing:** BNY custodies and services the underlying CLO portfolio; Securitize maintains the on-chain register and tokenization layer.
- **Eligible-investor gating:** A **permissioned, institutional / qualified-investor product** offered under securities-law exemptions (Reg D / Reg S). Transfers are restricted to Securitize-whitelisted, KYC/AML-screened holders. Not a freely circulating retail token.
- **Mint / redeem flow & settlement:** Subscriptions/redemptions occur through Securitize against fund NAV, with BNY handling servicing; restricted to eligible investors and governed by the offering's liquidity terms.
- **Yield source & distribution:** Income reflects prevailing **AAA CLO spreads and short-term rates** (CLO tranches pay a floating spread over a reference rate). Yield is delivered via **NAV price-accretion** — the token price rises as income accrues, rather than minting new tokens. Exact APY is governed by the offering and not asserted here.
- **Oracle / NAV feed:** Price tracks fund NAV set from the underlying CLO valuations, not open-market order flow.
- **Transfer restrictions / whitelist:** Transfers are limited to the permissioned holder set at the contract / transfer-agent level.

See [[securitize]] for the issuer, [[real-world-assets]] for the asset class, and the sister product [[apollo-diversified-credit-securitize-fund]].

---

## Comparison vs Peer Tokenized Credit / RWA Products

| Product | Issuer / Servicer | Underlying | Credit quality | NAV model |
|---|---|---|---|---|
| **STAC** | Securitize + BNY | AAA-rated USD CLO tranches | Senior, AAA (highest grade) | Price-accruing (~$1,021) |
| **JAAA (tokenized)** | Tokenized Janus Henderson AAA CLO ETF | AAA CLO tranches | Senior, AAA | Price/NAV |
| **[[apollo-diversified-credit-securitize-fund\|ACRED]]** | Securitize + Apollo | Diversified private + public credit | Mixed/mid-grade | Price-accruing (~$1,099) |
| **[[midas-mf-one\|mF-ONE]]** | Midas + Fasanara | Private credit + delta-neutral crypto | Private credit | Price-accruing (~$1.10) |
| **[[buidl]]** (BUIDL) | BlackRock + Securitize | U.S. Treasuries | Near risk-free | $1.00 NAV (rebasing) |

STAC's distinguishing trait is its **AAA-only, senior-tranche mandate** with a top-tier bank (BNY) as custodian/servicer — positioning it as the highest-grade structured-credit option among tokenized credit funds, with lower expected yield but materially lower credit risk than diversified-credit peers like ACRED.

---

## How & Where It Trades / Is Used

- **Primary issuance:** Subscriptions/redemptions occur through Securitize against fund NAV, with BNY handling servicing; restricted to eligible investors.
- **Eligibility:** KYC/AML-cleared institutional / qualified investors only (Reg D / Reg S); not open retail.
- **Secondary trading:** Negligible on public venues — CoinGecko reported $0 24h volume. Transfers are limited to the permissioned holder set; this is a **hold-to-NAV** instrument.
- **DeFi composability:** As a high-grade tokenized credit asset, STAC is a candidate for use as **collateral in permissioned/institutional DeFi**, where venues whitelist it; broad composability is constrained by the whitelist.
- **Tracking:** Price tracks fund NAV set from the underlying CLO valuations, not open-market order flow.
- **Hours:** On-chain transfer among permitted holders is 24/7; pricing and redemptions follow the fund's operating schedule.

---

## Narrative, Category & Catalysts

STAC brings **institutional structured credit (AAA CLOs)** on-chain, extending the tokenized-credit narrative beyond Treasuries into high-grade securitized products. Catalysts:

- **Custodian-bank validation:** BNY's involvement as servicer/custodian is a notable institutional-adoption signal for on-chain structured credit.
- **CLO demand:** AAA CLO tranches offer floating-rate, high-grade yield that has been in strong institutional demand; tokenizing access broadens distribution.
- **RWA diversification:** STAC lets on-chain investors diversify beyond Treasury tokens into senior structured credit while staying at the top of the credit-quality spectrum.
- **Rates / credit cycle:** Floating-rate CLO income benefits from elevated short-term rates; the key risk is the corporate-credit cycle, not the crypto cycle.

### History / Timeline

- **2026-02-06:** All-time low NAV recorded near $997.66 (per snapshot data).
- **2026-06-10:** All-time high NAV recorded near $1,023.81 (per snapshot data).
- **2026-06-21:** Market snapshot — ~$102.30M market cap, ~$1,021 NAV, rank #266.
- Launch announced via BNY newsroom: "Securitize Launches Tokenized AAA CLO Fund with Services Provided by BNY." (Exact launch date not independently verified here — do not infer one.)

---

## Risks

- **Credit risk:** Although AAA tranches are senior and historically low-default, they are not risk-free — a severe corporate-credit downturn could pressure even high-grade CLO marks.
- **Issuer / custodial / servicing risk:** Holders rely on Securitize (tokenization/transfer agency) and BNY (servicing/custody) for accurate accounting and redemption.
- **Redemption-gating / liquidity risk:** With effectively no secondary market and gated redemptions, exit depends on the fund's redemption process and underlying CLO liquidity.
- **NAV-gap / valuation risk:** NAV depends on CLO marks, which can lag in stressed markets, so the on-chain price may overstate realizable value during stress.
- **Regulatory / securities-law risk:** Tokenized structured-credit funds operate under evolving securities rules; eligibility and terms can change.
- **Smart-contract risk:** As an on-chain token, it carries contract/operational risk despite institutional backing.

---

## Trading / Usage Playbook

- **Who can hold it:** KYC/AML-cleared institutional / qualified investors whitelisted through Securitize (Reg D / Reg S). Not for open retail.
- **Primary use case:** On-chain access to **high-grade (AAA) structured-credit yield** for institutions seeking floating-rate income above Treasuries with strong credit quality and BNY custody.
- **Collateral use:** Suitable as high-grade collateral on venues that whitelist it; treat liquidity as gated and NAV-based.
- **Exit discipline:** Plan for NAV-based primary redemption windows; do not rely on secondary liquidity.

---

## See Also

- [[real-world-assets]]
- [[securitize]]
- [[apollo-diversified-credit-securitize-fund]]
- [[midas-mf-one]] — peer tokenized private-credit product
- [[tokenized-treasuries]]
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- cryptodataapi.com / CoinGecko market snapshot, 2026-06-21
- BNY newsroom: "Securitize Launches Tokenized AAA CLO Fund with Services Provided by BNY"
- General market knowledge; no specific wiki source ingested yet.


---
title: "Midas mF-ONE"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, real-world-assets]
aliases: ["MF-ONE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://midas.app/mfone"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[morpho]]", "[[real-world-assets]]", "[[tokenized-treasuries]]"]
---

# Midas mF-ONE

**Midas mF-ONE** (ticker **mF-ONE**) is a tokenized certificate issued by **Midas** that provides on-chain exposure to **Fasanara Capital's F-ONE strategy**, a diversified private-credit and digital-asset fund. Unlike a tokenized Treasury, the underlying here is a **private-credit portfolio** — fintech-originated receivables, SME lending, real-estate-backed credit, and delta-neutral crypto strategies — wrapped as an ERC-20 on [[ethereum|Ethereum]]. mF-ONE is a **value-accruing (non-rebasing) NAV** design: the certificate's price drifts upward as private-credit yield accrues. It lets qualified investors access real-world private-credit returns through a blockchain-native [[real-world-assets|RWA]] instrument that is composable in DeFi lending markets such as [[morpho|Morpho]].

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | mF-ONE |
| **Market Cap Rank** | #354 |
| **Current Price** | $1.098 |
| **Market Cap** | $70.3M |
| **24h Volume** | $0 (negligible secondary) |
| **24h Change** | -0.03% |
| **Circulating Supply** | 64.04M MF-ONE |
| **Total Supply** | 64.04M MF-ONE |
| **All-Time High** | $1.098 |
| **All-Time Low** | $1.008 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The token's price has drifted up from ~$1.008 to its all-time high of $1.098 as private-credit yield accrues into the certificate's value — a value-accruing (non-rebasing) design where NAV grows over time. Effectively zero secondary volume is typical of a permissioned, qualified-investor private-credit token where flow runs through primary mint/redeem with Midas rather than open trading. **The price reflects the fund's periodic NAV mark, not a market order book** — the relevant disclaimer is NAV/valuation integrity and redemption gating, not crypto-cycle volatility.

---

## How It Works (Architecture Deep Dive)

mF-ONE is a tokenized certificate built on Midas's **Liquid Yield Token** framework, representing a claim on an off-chain private-credit fund.

- **Fund structure & manager:** The underlying **F-ONE strategy** is managed by **Fasanara Capital**, a London-based alternative asset manager specializing in fintech/private credit. **Midas** issues the on-chain certificate, handling tokenization, compliance, and on-chain liquidity mechanics; the certificate represents an economic claim on the F-ONE fund.
- **Underlying assets:** A diversified portfolio of **private credit** (fintech receivables, SME lending, real-estate-backed credit) plus **delta-neutral crypto strategies**. This is a credit/strategy fund, **not** a cash-equivalent Treasury product, so it carries credit and strategy risk and is marked periodically rather than daily.
- **Custody / structuring:** The underlying fund is managed by Fasanara off-chain under traditional-finance risk frameworks; Midas handles the tokenization, compliance, and redemption mechanics on-chain. Market cap equals FDV (MC/FDV = 1.00), reflecting full backing by the underlying NAV.
- **Eligible-investor gating:** Access is restricted to **qualified / institutional investors** with KYC/AML screening, under applicable securities-law exemptions. mF-ONE is not an open-retail instrument and transfers are limited to whitelisted addresses.
- **Mint / redeem flow & settlement:** Holders mint and redeem the certificate against the underlying fund through Midas's primary issuance flow, subject to the fund's liquidity terms (private credit is inherently less liquid than Treasuries, so redemptions may carry notice periods or windows).
- **Yield source & distribution:** Yield comes from private-credit interest income and the delta-neutral crypto sleeve, delivered via **NAV price-accretion** (the certificate value rises; no rebasing).
- **Oracle / NAV feed:** The on-chain value tracks the F-ONE strategy's NAV as marked by the manager; because the underlying is illiquid and marked periodically, the on-chain value reflects fund accounting rather than continuous market price discovery.
- **Transfer restrictions / whitelist:** Transfers are confined to the permissioned, KYC'd holder set.
- **DeFi composability:** The token can be supplied as collateral / used in DeFi lending markets such as [[morpho|Morpho]], a distinguishing feature versus purely hold-to-NAV private-credit funds.

---

## Comparison vs Peer Tokenized Credit / RWA Products

| Product | Issuer / Manager | Underlying | Risk profile | DeFi composability |
|---|---|---|---|---|
| **mF-ONE** | Midas + Fasanara | Private credit + delta-neutral crypto | Private-credit + strategy risk | Yes (e.g., [[morpho\|Morpho]]) |
| **[[apollo-diversified-credit-securitize-fund\|ACRED]]** | Securitize + Apollo | Diversified private + public credit | Mid-grade credit-cycle | Permissioned collateral |
| **[[securitize-tokenized-aaa-clo-fund\|STAC]]** | Securitize + BNY | AAA-rated USD CLO tranches | Senior, high-grade | Permissioned |
| **[[ousg]]** (OUSG) | Ondo Finance | U.S. Treasuries | Near risk-free cash | Yes |
| **[[buidl]]** (BUIDL) | BlackRock + Securitize | U.S. Treasuries | Near risk-free cash | Permissioned |

mF-ONE is differentiated by its **DeFi-native composability** (usable on Morpho) combined with a higher-yield, higher-risk private-credit + delta-neutral-crypto mandate — versus the safer Treasury and AAA-CLO tokens.

---

## How & Where It Trades / Is Used

- **Primary market:** Mint/redeem with Midas for qualified investors — the dominant venue (secondary volume ~$0).
- **Eligibility:** KYC/AML-cleared qualified / institutional investors only; not open retail.
- **Secondary market:** On-chain transfers on [[ethereum|Ethereum]]; negligible DEX liquidity. The token is composable in DeFi lending (e.g. [[morpho|Morpho]]) but not actively traded on open order books.
- **DeFi composability / collateral use:** Can be supplied as collateral in DeFi lending markets such as Morpho — enabling holders to borrow against the certificate while it accrues yield, though this layers smart-contract and liquidation risk on top of fund risk.
- **Hours:** Token transfers run 24/7 on-chain, but primary subscription/redemption and the underlying private-credit fund follow the fund's dealing calendar, which may be periodic rather than continuous.
- **Tracking:** Tracks the NAV of the F-ONE strategy as yield accrues. Because the underlying is private credit (illiquid, marked periodically), the on-chain value reflects fund accounting rather than continuous market price discovery.

---

## Narrative, Category & Catalysts

mF-ONE sits in the **tokenized private credit** segment of the RWA narrative, with a distinctive DeFi-composability angle. Catalysts:

- **Private-credit boom:** Strong institutional appetite for private-credit yield drives demand for tokenized access.
- **DeFi composability for RWAs:** Usability as collateral on Morpho is a key differentiator and a proof-point for plugging tokenized credit into DeFi lending.
- **Midas / Liquid Yield Token framework:** Midas's tokenization model aims to make a range of yield strategies composable on-chain, of which mF-ONE is one.
- **Credit cycle:** Returns depend on the private-credit cycle and the performance of the delta-neutral crypto sleeve, not directly on the crypto price cycle.

### History / Timeline

- **2025–2026:** Midas issued mF-ONE as a tokenized certificate over Fasanara Capital's F-ONE strategy on Ethereum, with DeFi composability via Morpho. (Exact launch date not independently verified here — do not infer one.)
- **2026-06-21:** Market snapshot — ~$70.3M market cap, ~$1.098 NAV (at ATH), rank #354.

---

## Risks

- **Credit / strategy risk (dominant):** Unlike a Treasury token, mF-ONE is exposed to defaults in the underlying private-credit book and to losses in the delta-neutral crypto sleeve. NAV can fall.
- **Issuer / counterparty risk:** Dependence on Midas (issuer/tokenizer) and Fasanara Capital (fund manager). Manager or issuer failure is a primary tail risk.
- **Redemption-gating / liquidity risk:** Private credit is illiquid; redemptions may be gated, delayed, or subject to notice periods, and there is essentially no secondary market to exit quickly.
- **NAV-gap / valuation risk:** Private-credit NAV relies on periodic marks and manager judgment, which can lag reality and create gaps between reported and realizable value.
- **Regulatory / securities-law risk:** As a tokenized security/certificate for qualified investors, it sits within evolving securities regulation and transfer restrictions.
- **Smart-contract / DeFi risk:** Use as DeFi collateral (e.g. on Morpho) adds smart-contract and liquidation/de-peg risk on top of the underlying fund risk.
- **Macro backdrop:** As of 2026-06-23 the crypto [[fear-and-greed-index|Fear & Greed Index]] reads **21 ("Extreme Fear")**, with the long-horizon regime model in bottoming/accumulation. Private-credit exposure is less correlated to crypto beta day-to-day, but credit stress tends to cluster with broad risk-off conditions, which can pressure the underlying portfolio precisely when redemptions are sought. **The certificate tracks fund NAV/yield, not the crypto cycle.**

---

## Trading / Usage Playbook

- **Who can hold it:** KYC/AML-cleared qualified / institutional investors whitelisted by Midas. Not for open retail.
- **Primary use case:** On-chain access to **diversified private-credit + delta-neutral-crypto yield**, with the option to use the certificate as DeFi collateral.
- **Collateral use:** Can be supplied on Morpho and similar venues; sizing should account for the illiquid underlying and potential liquidation risk if used as leveraged collateral.
- **Exit discipline:** Plan for periodic, NAV-based redemption through Midas; do not rely on secondary liquidity, and expect notice periods typical of private credit.

---

## Platform & Chain Information

**Deployment:** [[ethereum|Ethereum]] (ERC-20)

| Chain | Address |
|---|---|
| Ethereum | `0x238a700ed6165261cf8b2e544ba797bc11e466ba` |

---

## See Also

- [[real-world-assets]] / [[rwa]]
- [[morpho]] — DeFi lending market where mF-ONE is composable
- [[apollo-diversified-credit-securitize-fund]], [[securitize-tokenized-aaa-clo-fund]] — peer tokenized-credit products
- [[tokenized-treasuries]] — contrast: cash-equivalent vs. private-credit RWA
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.


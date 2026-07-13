---
title: "Theo Short Duration US Treasury Fund"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, tokenized-treasuries]
aliases: ["THBILL"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://theo.xyz"
related: ["[[crypto-markets]]", "[[real-world-assets]]", "[[tokenized-treasuries]]", "[[ethereum]]", "[[ousg]]", "[[hashnote-usyc]]"]
---

# Theo Short Duration US Treasury Fund

**Theo Short Duration US Treasury Fund** (ticker **THBILL**) is a [[tokenized-treasuries|tokenized Treasury]] fund: an on-chain share whose underlying assets are short-duration U.S. Treasury bills, cash, and Treasury-collateralized repo. It is issued by **Theo**, an institutional-grade tokenization platform, and deployed multi-chain across [[ethereum|Ethereum]], Base, Arbitrum One, and HyperEVM. THBILL is an **accruing-NAV** (price-accretion) design: rather than rebasing the supply, yield accrues into the token's value, so the unit price drifts upward over time. It is a yield-bearing [[real-world-assets|real-world asset]] (RWA) aimed at giving on-chain capital exposure to the front end of the U.S. Treasury curve with DeFi composability from launch.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | THBILL |
| **Market Cap Rank** | #232 |
| **Current Price** | $1.024 |
| **Market Cap** | $122.5M |
| **24h Volume** | $111,278 |
| **24h Change** | +0.85% |
| **Circulating Supply** | 119.68M THBILL |
| **Total Supply** | 119.68M THBILL |
| **All-Time High** | $1.11 |
| **All-Time Low** | $0.9067 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The price hovering near $1.00 with a slow upward drift is characteristic of a [[tokenized-treasuries|tokenized T-bill]] product where yield accrues into the token's net asset value rather than being paid as a separate distribution. Thin secondary volume ($0.1M/24h relative to a ~$122M market cap) is typical of permissioned RWA instruments, where most flow happens via primary mint/redeem rather than open secondary trading. **The quoted price reflects accrued NAV, not crypto-cycle beta** — the ATL near $0.91 and ATH near $1.11 reflect thin-book secondary dislocations and accrual rather than fundamental moves in the Treasury portfolio.

---

## How It Works (Architecture Deep Dive)

THBILL is a tokenized fund interest issued through Theo's institutional tokenization stack, with the economic claim moving across multiple chains.

- **Fund structure & issuer:** **Theo** operates the tokenization platform and issues the fund interest as an on-chain token representing an economic claim on the underlying short-duration Treasury fund (not a bearer asset).
- **Underlying assets:** Short-duration **U.S. Treasury bills**, cash, and repurchase agreements collateralized by Treasuries — the standard portfolio for a short-duration Treasury / money-market-style fund, holding front-end paper to minimize duration and credit risk.
- **Custody:** Underlying Treasuries are held with regulated off-chain custodians; the on-chain token mirrors that custodied position 1:1 (market cap equals fully diluted valuation, MC/FDV = 1.00).
- **Eligible-investor gating:** Like peer tokenized Treasury products ([[ousg|OUSG]], [[hashnote-usyc|USYC]], [[buidl|BUIDL]]), primary subscription and redemption are gated to KYC/AML-screened, whitelisted — typically non-U.S. or qualified — investors under securities-law exemptions (Reg S / Reg D). Retail open-market access is generally restricted.
- **Mint / redeem flow & settlement:** Whitelisted participants mint and redeem against the underlying fund through Theo's primary issuance flow. The multi-chain deployment lets the same economic interest move across [[ethereum|Ethereum]], Base, Arbitrum One, and HyperEVM, settling on-chain.
- **Yield source & distribution:** Yield comes from the T-bill / repo portfolio and is delivered via **price accretion** — the token's NAV rises as income accrues, rather than minting new tokens (non-rebasing). This is the opposite design choice from rebasing $1.00-NAV peers like [[buidl|BUIDL]] and [[vaneck-treasury-fund|VBILL]].
- **Oracle / NAV feed:** The token is designed to track the value of the short-duration Treasury portfolio plus accrued yield; on secondary venues, price can deviate from accrued NAV due to on-chain supply/demand and arbitrage friction.
- **Transfer restrictions / whitelist:** Transfers are restricted to the permissioned holder set maintained by the issuer; non-whitelisted addresses cannot hold the token.

---

## Comparison vs Peer Tokenized Treasury Products

| Product | Issuer / Manager | NAV model | Chains | Notable trait |
|---|---|---|---|---|
| **THBILL** | Theo | Price-accruing (~$1.02+) | Ethereum, Base, Arbitrum, HyperEVM | DeFi-composable from launch; multi-L2 |
| **[[ousg]]** (OUSG) | Ondo Finance | Price-accruing | Multi-chain | Instant USDC mint/redeem; BUIDL-backed |
| **[[hashnote-usyc]]** (USYC) | Hashnote / Circle | Price-accruing | Multi-chain | Repo-focused; Circle collateral integration |
| **[[buidl]]** (BUIDL) | BlackRock + Securitize | $1.00 NAV (rebasing) | Multi-chain | Largest tokenized-Treasury fund |
| **[[vaneck-treasury-fund\|VBILL]]** | VanEck + Securitize | $1.00 NAV (rebasing) | Multi-chain | Stablecoin in-kind subscriptions |

THBILL's positioning emphasizes Layer-2 / multi-chain reach (Base, Arbitrum, HyperEVM) and DeFi composability, in contrast to the rebasing $1.00-NAV brand-name funds.

---

## How & Where It Trades / Is Used

- **Primary market:** Mint/redeem with the issuer for whitelisted participants — the dominant venue for net flows.
- **Eligibility:** KYC/AML-cleared, whitelisted (typically non-U.S. or qualified) investors only; not open retail.
- **Secondary market:** Limited on-chain liquidity, e.g. a Uniswap V3 THBILL/USDC pool on [[ethereum|Ethereum]]. Secondary volume is thin compared with market cap, and thin books can produce price dislocations (reflected in the wide historical ATH/ATL).
- **DeFi composability:** Designed to be composable across its supported chains, allowing use in lending/collateral contexts where the venue permits the permissioned token.
- **Hours:** The token itself transfers 24/7 on-chain, but the underlying Treasury market and primary creation/redemption follow traditional banking/market hours.
- **Tracking:** Designed to track the value of its short-duration Treasury portfolio plus accrued yield. Deviations on secondary venues reflect on-chain supply/demand and arbitrage friction rather than a change in underlying value.

---

## Narrative, Category & Catalysts

THBILL sits in the **tokenized Treasuries** segment of the RWA narrative, with a tilt toward Layer-2 and DeFi-native distribution. Catalysts include:

- **Rates regime:** Front-end U.S. yields drive the product's appeal; richer T-bill yields make on-chain Treasury tokens more attractive than idle stablecoins.
- **Multi-chain / L2 growth:** Deployment on Base, Arbitrum, and HyperEVM positions THBILL to capture DeFi-native demand for yield-bearing cash collateral.
- **Institutional RWA adoption:** Part of the broader wave bringing regulated fixed-income on-chain alongside [[ousg]], [[hashnote-usyc]], and [[buidl]].
- **DeFi composability:** Native usability as collateral/cash in DeFi differentiates it from purely hold-to-NAV permissioned funds.

### History / Timeline

- **2025–2026:** Theo launched THBILL as a tokenized short-duration U.S. Treasury fund, with multi-chain deployment across Ethereum, Base, Arbitrum One, and HyperEVM. (Exact launch date not independently verified here — do not infer one.)
- **2026-06-21:** Market snapshot — ~$122.5M market cap, ~$1.024 NAV, rank #232.

---

## Risks

- **Issuer / counterparty risk:** Reliance on Theo and its fund administrators, custodians, and legal structuring. A failure or fraud at the issuer or custodian level is the primary tail risk for any tokenized fund.
- **Custodial risk:** The on-chain token is only as good as the off-chain custody and the enforceability of the legal claim on the underlying Treasuries.
- **NAV-gap / tracking / liquidity risk:** Thin secondary liquidity can cause price dislocations (note the historical ATL near $0.91 / ATH near $1.11) and make exits slow for holders who cannot use primary redemption.
- **Redemption-gating risk:** In stress, primary redemption may be gated or delayed, leaving only thin secondary venues for exit.
- **Regulatory / securities-law risk:** Tokenized fund interests sit in an evolving regulatory perimeter (securities laws, transfer restrictions, jurisdictional eligibility). Rule changes could restrict who may hold or trade the token.
- **Smart-contract risk:** Multi-chain deployment broadens the smart-contract and bridge attack surface.
- **Macro backdrop:** As of 2026-06-23 the crypto [[fear-and-greed-index|Fear & Greed Index]] reads **21 ("Extreme Fear")**, with the long-horizon regime model in bottoming/accumulation. Cash-equivalent RWA products like THBILL are relatively insulated from crypto beta — part of their appeal in risk-off regimes — but secondary liquidity can still thin out in stressed conditions. **The token tracks Treasury NAV/yield, not the crypto cycle.**

---

## Trading / Usage Playbook

- **Who can hold it:** KYC/AML-cleared, whitelisted (typically non-U.S. or qualified) investors only.
- **Primary use case:** On-chain **cash management / collateral** — front-end Treasury yield with DeFi composability across Ethereum and L2s.
- **Collateral use:** Suitable as high-quality collateral on venues that accept the permissioned token; check each venue's whitelist.
- **Exit discipline:** Prefer primary redemption at NAV; treat the thin THBILL/USDC secondary pool as a convenience, not a deep exit — large orders can move the thin book.

---

## Platform & Chain Information

**Deployment:** Multi-chain ([[ethereum|Ethereum]], Base, Arbitrum One, HyperEVM)

| Chain | Address |
|---|---|
| Ethereum | `0x5fa487bca6158c64046b2813623e20755091da0b` |
| HyperEVM | `0xfdd22ce6d1f66bc0ec89b20bf16ccb6670f55a5a` |
| Base | `0xfdd22ce6d1f66bc0ec89b20bf16ccb6670f55a5a` |
| Arbitrum One | `0xfdd22ce6d1f66bc0ec89b20bf16ccb6670f55a5a` |

---

## See Also

- [[real-world-assets]] / [[rwa]]
- [[tokenized-treasuries]]
- [[ousg]], [[hashnote-usyc]], [[buidl]], [[vaneck-treasury-fund]] — peer tokenized Treasury / MMF products
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

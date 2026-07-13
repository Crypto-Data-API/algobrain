---
title: "iShares Core US Aggregate Bond ETF (Ondo Tokenized ETF)"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, bonds, tokenization]
aliases: ["AGGON", "AGGon"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://app.ondo.finance/assets/aggon"
related: ["[[real-world-assets]]", "[[tokenization]]", "[[ondo-finance]]", "[[bonds]]", "[[treasuries]]", "[[etf]]", "[[duration]]", "[[crypto-markets]]", "[[ethereum]]"]
---

# iShares Core US Aggregate Bond ETF (Ondo Tokenized ETF)

**iShares Core US Aggregate Bond ETF (Ondo Tokenized ETF)** (ticker **AGGON**) is a [[tokenization|tokenized]] [[real-world-assets|real-world asset (RWA)]] issued by [[ondo-finance|Ondo Global Markets]] on [[ethereum|Ethereum]] (bridged to BNB Smart Chain and Solana) that gives non-US holders on-chain economic exposure to BlackRock's **iShares Core US Aggregate Bond ETF (AGG)** — the flagship broad U.S. investment-grade [[bonds|bond]] fund. Each token references one share of the underlying ETF, custodied off-chain, so AGGON is an on-chain proxy for the total U.S. investment-grade bond market. Within the Ondo Global Markets line it is the **core bond / moderate-duration ballast building block**.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, AGGON trades at **$101.33** with a market capitalization of **$14,356,287**, ranking **#982** by market cap. It was down **-0.22%** over 24 hours and up **+0.55%** over the trailing week — the muted moves typical of a broad investment-grade bond index. As of 2026-06-23 the broader crypto market remained in Extreme Fear (Fear & Greed 21, bottoming/accumulation regime; Bitcoin ~$64,568, ETH ~$1,737), but AGGON's drivers are US bond yields and the AGG US session, not the crypto cycle.

---

## What AGGON Is

AGGON belongs to the **Ondo Global Markets** line of tokenized U.S.-listed instruments. The structure is a permissioned RWA wrapper:

- **Underlying:** iShares Core US Aggregate Bond ETF (AGG), which tracks the Bloomberg US Aggregate Bond Index — a broad basket of U.S. investment-grade debt spanning [[treasuries|Treasuries]], agency mortgage-backed securities, and investment-grade corporate bonds. It is the benchmark "total bond market" ETF, carrying moderate [[duration]] (~6 years) and high-quality credit.
- **Backing:** Real AGG shares purchased and custodied off-chain. The token is a digital claim on that share, not a synthetic.
- **Economics:** Holders receive economic exposure "similar to holding AGG and reinvesting any dividends" — coupon/distribution income is reflected in the token's reference value rather than paid out separately.
- **No shareholder rights:** No voting rights or governance claim on BlackRock's fund.

---

## Architecture: How the Wrapper Works

- **Issuer / wrapper:** [[ondo-finance|Ondo Finance]] via Ondo Global Markets structures and issues the token as a digital claim on a real AGG share.
- **1:1 backing & proof-of-reserves:** Each AGGON is backed 1:1 by a custodied AGG share held off-chain with regulated custodians/brokers; attestation of those holdings is the integrity anchor.
- **Mint / redeem & KYC gating:** Authorized participants create and redeem tokens against real ETF shares. Mint/redeem is KYC-gated and transfer-restricted, **not available to U.S. persons**, aimed at non-US retail and institutional users. 24/5 access is advertised, gated by the underlying market calendar; additional jurisdictional restrictions apply.
- **Oracle / price feed:** The reference value derives from AGG's NAV / share price; on-chain price tracks that feed, anchored by mint/redeem arbitrage. Tracking is mechanical but depends on the issuer's operational integrity.
- **24/7 token vs. market-hours underlying:** AGGON transfers 24/7 on-chain; AGG trades only during US market sessions, so tight tracking and primary creation/redemption are constrained to US hours.
- **Coupon / expense-ratio handling:** AGG pays monthly distributions from its underlying bond coupons; these accrue into AGGON's reference value. The token inherits AGG's expense ratio (~0.03%) plus any Ondo wrapper fees.

---

## Settlement, Chains, and Peg Mechanism

AGGON is issued natively on **[[ethereum|Ethereum]]** and bridged to BNB Smart Chain and Solana.

| Chain | Address |
|---|---|
| Ethereum | `0xff7cf16aa2ffc463b996db2f7b7cf0130336899d` |
| BNB Smart Chain | `0x08ce97f3d5cf11e577d091ab048bc5e2eae3fabb` |
| Solana | `13qTjKx53y6LKGGStiKeieGbnVx3fx1bbwopKFb3ondo` |

The token tracks the NAV of the underlying ETF share through Ondo's mint/redeem mechanism: authorized participants create and redeem tokens against real ETF shares, anchoring the on-chain price to AGG.

---

## Tracking & Peg

- **Premium / discount:** On-chain price can trade above or below NAV when arbitrage is constrained; mint/redeem restores fair value once US markets reopen.
- **Weekend-gap risk:** AGG does not trade on weekends or US holidays, so AGGON's on-chain price is stale relative to rate news during those windows.
- **Duration / rate sensitivity:** AGG carries **moderate** duration (~6 years) — far less rate-sensitive than long-duration [[ishares-20-year-treasury-bond-etf-ondo-tokenized-etf|TLTON]], but more than a money-market instrument. A 1% rise in yields implies roughly a mid-single-digit-percentage price decline. Credit risk is low (investment grade) but not zero, since the index includes IG corporates and agency MBS alongside Treasuries.
- **Tracking error:** Inherits AGG's small tracking error to the Bloomberg US Aggregate index, plus any incremental dislocation from thin on-chain liquidity.

---

## Comparison vs. Alternatives

| Dimension | **AGGON (Ondo)** | Holding real AGG | TLTON (Ondo) | IVVON (Ondo) |
|---|---|---|---|---|
| Underlying | Broad IG US bonds | Broad IG US bonds | 20yr+ US Treasuries | S&P 500 equity |
| Composition | Treasuries + MBS + IG corp | Treasuries + MBS + IG corp | Long Treasuries only | Equities |
| Duration | Moderate (~6y) | Moderate (~6y) | Very high (~16–17y) | None (equity) |
| Credit risk | Low (IG) | Low (IG) | ~None (sovereign) | Equity risk |
| Access | Non-US KYC, on-chain 24/7 | Global brokerage | Non-US KYC | Non-US KYC |
| Backing | Real AGG shares, off-chain | Direct fund ownership | Real TLT shares | Real IVV shares |
| Role in book | Core bond ballast | Core bond ballast | Long-duration / rates bet | Equity beta core |

AGGON is the **"total bond market" default** of the Ondo set: broader and lower-duration than TLTON, it suits an investor wanting diversified investment-grade bond ballast rather than a concentrated long-end rates bet. Versus holding AGG directly, the trade-off is on-chain composability and non-US access against custodial and peg risk.

---

## How & Where It Trades

- **Primary market:** Mint/redeem through Ondo Global Markets for eligible users, gated to US market hours.
- **Secondary market:** On-chain transfers and limited DEX liquidity across [[ethereum|Ethereum]], BNB Smart Chain, and Solana; secondary depth is thin relative to the ~$14M market cap.
- **Liquidity:** Mint/redeem is the primary fair-value channel; large orders depend on it rather than DEX depth.

---

## Narrative & Catalysts

AGGON's thesis is **on-chain access to TradFi investment-grade fixed income**: a single composable token for diversified US bond beta, usable as collateral or stable-value ballast in an on-chain portfolio. Catalysts include the broader RWA tokenization wave led by Ondo, growing demand for on-chain dollar-bond exposure as a lower-volatility complement to crypto, and macro regimes that favor high-quality fixed income.

### History / Timeline

- **2026-04-09** — AGGON captured in the CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-21** — Market snapshot: $101.33, ~$14.4M market cap, rank #982; +0.55% on the week.

---

## Risks

- **Issuer / custodian counterparty risk:** Value depends on Ondo and its custodians holding the underlying AGG shares and honoring redemptions — counterparty and operational risk, not trustless backing.
- **Interest-rate / duration risk:** AGG carries moderate duration; rising yields push its price down, and that risk passes through to AGGON.
- **Credit risk:** Low but non-zero — the index includes investment-grade corporates and agency MBS; spread widening in stress can hurt the price.
- **Redemption-gating risk:** Mint/redeem is KYC-gated, non-US-only, and market-hours-bound; halted creations can break the peg arbitrage.
- **Liquidity risk:** Thin on-chain secondary liquidity; mint/redeem is the primary fair-value channel and is gated by market hours and KYC.
- **Regulatory / eligibility risk:** Transfer restrictions and U.S.-person exclusion; evolving regulatory treatment of tokenized securities.
- **Peg / tracking risk:** A breakdown in mint/redeem arbitrage (or weekend gaps) could let the on-chain price drift from NAV.

---

## Trading Playbook

- **Core bond ballast:** Use AGGON as the diversified bond sleeve of an on-chain stock/bond portfolio — lower volatility than equities, lower duration than TLTON.
- **Default over TLTON:** Prefer AGGON when you want broad IG bond exposure rather than a concentrated long-end rates view; reserve [[ishares-20-year-treasury-bond-etf-ondo-tokenized-etf|TLTON]] for explicit duration bets.
- **Pair with equity:** Combine with [[ishares-core-s-p-500-etf-ondo-tokenized-etf|IVVON]] and [[ishares-core-msci-eafe-etf-ondo-tokenized-etf|IEFAON]] to build a classic global stock/bond mix on-chain.
- **Execute in US hours:** Transact size while mint/redeem arbitrage is live.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | AGGON |
| **Underlying ETF** | iShares Core US Aggregate Bond ETF (AGG) |
| **Issuer** | Ondo Global Markets ([[ondo-finance|Ondo Finance]]) |
| **Asset class** | Broad U.S. investment-grade bonds (via tokenized ETF) |
| **Market Cap Rank** | #982 |
| **Market Cap** | $14,356,287 |
| **Current Price** | $101.33 |
| **24h Change** | -0.22% |
| **7d Change** | +0.55% |
| **Native Chain** | Ethereum |
| **Categories** | Tokenized Assets, Real World Assets (RWA), Tokenized ETFs, Ondo Tokenized Assets |
| **Website** | [https://app.ondo.finance/assets/aggon](https://app.ondo.finance/assets/aggon) |

---

## See Also

- [[ondo-finance]]
- [[real-world-assets]]
- [[bonds]]
- [[treasuries]]
- [[etf]]
- [[duration]]
- [[ishares-20-year-treasury-bond-etf-ondo-tokenized-etf]] — long-duration bond sibling
- [[ishares-core-s-p-500-etf-ondo-tokenized-etf]] — equity-beta sibling
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). General market knowledge on Ondo Global Markets and the iShares AGG ETF; no additional specific wiki source ingested yet.

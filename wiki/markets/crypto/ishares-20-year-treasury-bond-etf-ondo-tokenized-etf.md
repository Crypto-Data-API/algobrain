---
title: "iShares 20+ Year Treasury Bond ETF (Ondo Tokenized ETF)"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, treasuries, bonds, tokenization]
aliases: ["TLTON", "TLTon"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://app.ondo.finance/assets/tlton"
related: ["[[real-world-assets]]", "[[tokenization]]", "[[ondo-finance]]", "[[treasuries]]", "[[bonds]]", "[[etf]]", "[[duration]]", "[[crypto-markets]]", "[[ethereum]]"]
---

# iShares 20+ Year Treasury Bond ETF (Ondo Tokenized ETF)

**iShares 20+ Year Treasury Bond ETF (Ondo Tokenized ETF)** (ticker **TLTON**) is a [[tokenization|tokenized]] [[real-world-assets|real-world asset (RWA)]] issued by [[ondo-finance|Ondo Global Markets]] on [[ethereum|Ethereum]] (bridged to BNB Smart Chain and Solana) that gives non-US holders on-chain economic exposure to BlackRock's **iShares 20+ Year Treasury Bond ETF (TLT)** — the flagship long-duration U.S. Treasury fund. Each token references one share of the underlying ETF, custodied off-chain by Ondo's broker-dealer infrastructure, so TLTON is effectively an on-chain, unlevered bet on long-dated [[treasuries|U.S. Treasury]] prices and the [[duration|interest-rate duration]] they carry. Within the Ondo Global Markets line it is the **long-duration ballast / rates building block**.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, TLTON trades at **$89.32** with a market capitalization of **$20,109,792**, ranking **#827** by market cap. It was roughly flat over 24 hours (**-0.05%**) and up **+1.12%** over the trailing week — consistent with a modest rally in long Treasury prices. As of 2026-06-23 the broader crypto market remained risk-off, with Bitcoin near $64,568, ETH near $1,737, and the Crypto [[fear-and-greed-index|Fear & Greed Index]] at 21 (Extreme Fear; bottoming/accumulation regime). TLTON's price path, however, is driven by long-term US Treasury yields and the TLT US session, not by the crypto cycle.

---

## What TLTON Is

TLTON belongs to the **Ondo Global Markets** line of tokenized U.S. equities and ETFs. The structure is a permissioned RWA wrapper:

- **Underlying:** iShares 20+ Year Treasury Bond ETF (TLT), which holds U.S. Treasury bonds with remaining maturities greater than 20 years. TLT is a pure [[duration]] instrument — its price rises when long-term yields fall and falls when they rise, with no meaningful credit risk.
- **Backing:** Real TLT shares purchased and custodied off-chain. The token is a digital claim on that share, not a synthetic or basket exposure.
- **Economics:** Tokenholders receive economic exposure "similar to holding TLT and reinvesting any dividends" — the ETF's monthly coupon distributions are reflected in the token's reference value rather than paid out separately.
- **No shareholder rights:** Holders do not get voting rights or any governance claim on BlackRock's fund.

---

## Architecture: How the Wrapper Works

- **Issuer / wrapper:** [[ondo-finance|Ondo Finance]] via Ondo Global Markets structures and issues the token; it is a digital claim on a real TLT share.
- **1:1 backing & proof-of-reserves:** Each TLTON is backed 1:1 by a custodied TLT share held off-chain with regulated custodians/brokers; attestation of those holdings is the integrity anchor.
- **Mint / redeem & KYC gating:** Authorized participants can create and redeem tokens against real ETF shares. Mint/redeem is KYC-gated and transfer-restricted, explicitly **not available to U.S. persons**, and aimed at non-US retail and institutional users. 24/5 access is advertised, gated by the underlying market's trading calendar; additional jurisdictional restrictions apply.
- **Oracle / price feed:** The token's reference value derives from TLT's NAV / share price; on-chain price tracks that feed, with the mint/redeem arbitrage keeping the two anchored. Tracking is mechanical rather than sentiment-driven, but depends entirely on the issuer's operational integrity.
- **24/7 token vs. market-hours underlying:** TLTON transfers 24/7 on-chain; TLT trades only during US market sessions, so tight tracking and primary creation/redemption are constrained to US hours.
- **Coupon / expense-ratio handling:** TLT pays monthly distributions from its Treasury coupons; these accrue into TLTON's reference value. The token inherits TLT's expense ratio (~0.15%) plus any Ondo wrapper fees.

---

## Settlement, Chains, and Peg Mechanism

TLTON is issued natively on **[[ethereum|Ethereum]]** and bridged to BNB Smart Chain and Solana.

| Chain | Address |
|---|---|
| Ethereum | `0x992651bfeb9a0dcc4457610e284ba66d86489d4d` |
| BNB Smart Chain | `0xf69e40069ac227c11459e3f4e8a446b3401616b6` |
| Solana | `KaSLSWByKy6b9FrCYXPEJoHmLpuFZtTCJk1F1Z9ondo` |

The token tracks the NAV of the underlying ETF share through Ondo's mint/redeem mechanism: authorized participants create and redeem tokens against real ETF shares, which keeps the on-chain price anchored to TLT.

---

## Tracking & Peg

- **Premium / discount:** On-chain price can trade above or below NAV when arbitrage is constrained; mint/redeem restores fair value once US markets reopen.
- **Weekend-gap risk:** TLT does not trade on weekends or US holidays, so TLTON's on-chain price is stale relative to rate news during those windows. A sharp move in long yields at Monday's open will gap TLTON.
- **Duration / rate sensitivity:** This is the dominant tracking-relevant feature. TLT has very high effective duration (~16–17 years), so a 1% rise in long-term yields can drive a roughly double-digit-percentage price decline. That sensitivity passes straight through to TLTON — it is the most rate-sensitive token in the Ondo set (vs. moderate-duration [[ishares-core-us-aggregate-bond-etf-ondo-tokenized-etf|AGGON]] and zero-duration equity tokens like [[ishares-core-s-p-500-etf-ondo-tokenized-etf|IVVON]]).
- **Tracking error:** Inherits TLT's small tracking error to its Treasury index, plus any incremental dislocation from thin on-chain liquidity.

---

## Comparison vs. Alternatives

| Dimension | **TLTON (Ondo)** | Holding real TLT | AGGON (Ondo) | IVVON (Ondo) |
|---|---|---|---|---|
| Underlying | 20yr+ US Treasuries | 20yr+ US Treasuries | Broad IG US bonds | S&P 500 equity |
| Duration | Very high (~16–17y) | Very high (~16–17y) | Moderate (~6y) | None (equity) |
| Credit risk | ~None (sovereign) | ~None (sovereign) | Low (IG) | Equity risk |
| Rate sensitivity | Highest in set | Highest | Moderate | N/A |
| Access | Non-US KYC, on-chain 24/7 | Global brokerage | Non-US KYC | Non-US KYC |
| Backing | Real TLT shares, off-chain | Direct fund ownership | Real AGG shares | Real IVV shares |
| Role in book | Duration / rates ballast | Duration / rates ballast | Core bond ballast | Equity beta core |

TLTON is the **purest rates expression** in the Ondo set: a long-duration, credit-clean Treasury bet, useful for expressing a falling-yield view or as a deflation/recession hedge. Versus simply holding TLT in a brokerage, the trade-off is on-chain composability and non-US access against custodial counterparty and peg risk.

---

## How & Where It Trades

- **Primary market:** Mint/redeem through Ondo Global Markets for eligible users, gated to US market hours.
- **Secondary market:** On-chain transfers and limited DEX liquidity across [[ethereum|Ethereum]], BNB Smart Chain, and Solana; secondary depth is thin relative to the ~$20M market cap.
- **Liquidity:** Mint/redeem is the primary fair-value channel; large orders depend on it rather than DEX depth.

---

## Narrative & Catalysts

TLTON's thesis is **on-chain access to TradFi duration**: it lets non-US holders express a long-Treasury / falling-yield view as a composable on-chain token, usable as collateral or ballast in an on-chain portfolio. Catalysts include the broader RWA tokenization wave led by Ondo, growing demand for on-chain dollar-bond exposure as a stable-value and hedging instrument, and macro regimes (disinflation, rate cuts, flight-to-quality) that favor long-duration Treasuries.

### History / Timeline

- **2026-04-09** — TLTON captured in the CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-21** — Market snapshot: $89.32, ~$20.1M market cap, rank #827; +1.12% on the week amid a modest long-Treasury rally.

---

## Risks

- **Issuer / custodian counterparty risk:** Value rests on Ondo and its custodians actually holding the underlying TLT shares and honoring redemptions. This is counterparty and operational risk, not trustless on-chain backing.
- **Interest-rate / duration risk:** TLT is one of the most rate-sensitive ETFs in existence. A rise in long-term yields can produce double-digit price declines; this risk passes straight through to TLTON.
- **Redemption-gating risk:** Mint/redeem is KYC-gated, non-US-only, and market-hours-bound; halted creations can break the peg arbitrage.
- **Liquidity risk:** On-chain secondary liquidity is thin relative to the underlying ETF.
- **Regulatory / eligibility risk:** Transfer restrictions and the U.S.-person exclusion mean the token can be frozen or restricted; the regulatory treatment of tokenized securities continues to evolve.
- **Peg / tracking risk:** Any breakdown in the mint/redeem arbitrage (e.g., halted creations, weekend gaps) could let the on-chain price drift from NAV.

---

## Trading Playbook

- **Duration ballast:** Use TLTON as the long-duration sleeve of an on-chain stock/bond portfolio, paired with [[ishares-core-s-p-500-etf-ondo-tokenized-etf|IVVON]] (equity) and [[ishares-core-msci-eafe-etf-ondo-tokenized-etf|IEFAON]] (intl equity).
- **Rates view:** Hold TLTON to express a falling-long-yield / recession-hedge thesis; size it knowing it is the highest-beta-to-rates instrument in the set.
- **Pair vs. AGGON:** For a lower-duration, broader bond exposure, prefer [[ishares-core-us-aggregate-bond-etf-ondo-tokenized-etf|AGGON]]; use TLTON only when you specifically want the long end.
- **Execute in US hours:** Transact size while mint/redeem arbitrage is live; avoid large weekend trades into a stale price.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TLTON |
| **Underlying ETF** | iShares 20+ Year Treasury Bond ETF (TLT) |
| **Issuer** | Ondo Global Markets ([[ondo-finance|Ondo Finance]]) |
| **Asset class** | Long-duration U.S. Treasuries (via tokenized ETF) |
| **Market Cap Rank** | #827 |
| **Market Cap** | $20,109,792 |
| **Current Price** | $89.32 |
| **24h Change** | -0.05% |
| **7d Change** | +1.12% |
| **Native Chain** | Ethereum |
| **Categories** | Tokenized Assets, Real World Assets (RWA), Tokenized ETFs, Ondo Tokenized Assets |
| **Website** | [https://app.ondo.finance/assets/tlton](https://app.ondo.finance/assets/tlton) |

---

## See Also

- [[ondo-finance]]
- [[real-world-assets]]
- [[treasuries]]
- [[duration]]
- [[etf]]
- [[ishares-core-us-aggregate-bond-etf-ondo-tokenized-etf]] — moderate-duration bond sibling
- [[ishares-core-s-p-500-etf-ondo-tokenized-etf]] — equity-beta sibling
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). General market knowledge on Ondo Global Markets and the iShares TLT ETF; no additional specific wiki source ingested yet.

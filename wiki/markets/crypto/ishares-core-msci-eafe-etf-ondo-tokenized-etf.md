---
title: "iShares Core MSCI EAFE ETF (Ondo Tokenized ETF)"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, tokenization, stocks]
aliases: ["IEFAON", "IEFAon"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://app.ondo.finance/assets/iefaon"
related: ["[[real-world-assets]]", "[[tokenization]]", "[[ondo-finance]]", "[[etf]]", "[[crypto-markets]]", "[[ethereum]]"]
---

# iShares Core MSCI EAFE ETF (Ondo Tokenized ETF)

**iShares Core MSCI EAFE ETF (Ondo Tokenized ETF)** (ticker **IEFAON**) is a [[tokenization|tokenized]] [[real-world-assets|real-world asset (RWA)]] issued by [[ondo-finance|Ondo Global Markets]] on [[ethereum|Ethereum]] (bridged to BNB Smart Chain and Solana) that gives non-US holders on-chain economic exposure to BlackRock's **iShares Core MSCI EAFE ETF (IEFA)** — a broad developed-markets ex-US/ex-Canada equity fund. Each token references one share of the underlying ETF, custodied off-chain, so IEFAON is an on-chain proxy for a diversified basket of large-, mid-, and small-cap equities across Europe, Australasia, and the Far East. Within the Ondo Global Markets line it is the **international-equity diversification building block**, the non-US complement to [[ishares-core-s-p-500-etf-ondo-tokenized-etf|IVVON]].

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, IEFAON trades at **$97.25** with a market capitalization of **$16,586,719**, ranking **#905** by market cap. It was essentially flat over 24 hours (**+0.04%**) and down **-1.49%** over the trailing week, reflecting softness in developed ex-US equities. As of 2026-06-23 the wider crypto market remained in Extreme Fear (Fear & Greed 21, bottoming/accumulation regime; Bitcoin ~$64,568, ETH ~$1,737), but IEFAON's drivers are international developed-market equities and currencies, not the crypto cycle.

---

## What IEFAON Is

IEFAON belongs to the **Ondo Global Markets** line of tokenized U.S.-listed equities and ETFs. The structure is a permissioned RWA wrapper:

- **Underlying:** iShares Core MSCI EAFE ETF (IEFA), which tracks the MSCI EAFE IMI index — developed-market equities outside the U.S. and Canada (Japan, the UK, Eurozone, Switzerland, Australia, and others). It is one of the most widely held international-equity ETFs and a core building block for global diversification.
- **Backing:** Real IEFA shares purchased and custodied off-chain. The token is a digital claim on that share, not a synthetic.
- **Economics:** Holders receive economic exposure "similar to holding IEFA and reinvesting any dividends" — fund distributions are reflected in the token's reference value rather than paid out separately.
- **No shareholder rights:** No voting rights or governance claim on BlackRock's fund.

---

## Architecture: How the Wrapper Works

- **Issuer / wrapper:** [[ondo-finance|Ondo Finance]] via Ondo Global Markets structures and issues the token as a digital claim on a real IEFA share.
- **1:1 backing & proof-of-reserves:** Each IEFAON is backed 1:1 by a custodied IEFA share held off-chain with regulated custodians/brokers; attestation of those holdings is the integrity anchor.
- **Mint / redeem & KYC gating:** Authorized participants create and redeem tokens against real ETF shares. Mint/redeem is KYC-gated and transfer-restricted, **not available to U.S. persons**, aimed at non-US retail and institutional users. 24/5 access is advertised, gated by the underlying market calendar; additional jurisdictional restrictions apply.
- **Oracle / price feed:** The reference value derives from IEFA's NAV / share price; on-chain price tracks that feed, anchored by mint/redeem arbitrage. Tracking is mechanical but depends on the issuer's operational integrity.
- **24/7 token vs. market-hours underlying:** IEFAON transfers 24/7 on-chain; IEFA (a US-listed fund) prices during US market sessions while its underlying constituents trade on overseas exchanges in other time zones — so tight tracking and primary creation/redemption are constrained to US hours, and there is an additional layer of stale-pricing between the US fund and its non-US holdings.
- **Distributions & expense-ratio handling:** IEFA pays distributions from its constituents' dividends; these accrue into IEFAON's reference value. The token inherits IEFA's expense ratio (~0.07%) plus any Ondo wrapper fees.

---

## Settlement, Chains, and Peg Mechanism

IEFAON is issued natively on **[[ethereum|Ethereum]]** and bridged to BNB Smart Chain and Solana.

| Chain | Address |
|---|---|
| Ethereum | `0xfeff7a377a86462f5a2a872009722c154707f09e` |
| BNB Smart Chain | `0x918008c3d29496c37b478b611967beaca365af36` |
| Solana | `C9J9vZ8N79GzzxFoRkPWCkGtMKU8akg4FhUk4r9ondo` |

The token tracks the NAV of the underlying ETF share through Ondo's mint/redeem mechanism: authorized participants create and redeem tokens against real ETF shares, anchoring the on-chain price to IEFA.

---

## Tracking & Peg

- **Premium / discount:** On-chain price can trade above or below NAV when arbitrage is constrained; mint/redeem restores fair value once US markets reopen.
- **Weekend / time-zone gap risk:** IEFA does not price on weekends or US holidays, and its overseas constituents trade in non-US hours, so IEFAON's on-chain price can be doubly stale relative to live international markets.
- **Currency exposure:** As an unhedged international-equity basket, IEFAON carries currency risk across the EAFE region (yen, euro, sterling, Swiss franc, Aussie dollar, etc.) on top of equity beta — moves in the US dollar affect the token's value even if local equities are flat.
- **Tracking error:** Inherits IEFA's tracking error to the MSCI EAFE IMI index, plus any incremental dislocation from thin on-chain liquidity.

---

## Comparison vs. Alternatives

| Dimension | **IEFAON (Ondo)** | Holding real IEFA | IVVON (Ondo) | AGGON (Ondo) |
|---|---|---|---|---|
| Underlying | Developed ex-US/Canada equity | Developed ex-US/Canada equity | S&P 500 (US large-cap) | Broad IG US bonds |
| Geography | Japan, UK, Eurozone, etc. | Same | United States | United States |
| Currency risk | High (unhedged EAFE FX) | High (unhedged EAFE FX) | None (USD) | None (USD) |
| Asset class | International equity | International equity | US equity | US bonds |
| Access | Non-US KYC, on-chain 24/7 | Global brokerage | Non-US KYC | Non-US KYC |
| Backing | Real IEFA shares, off-chain | Direct fund ownership | Real IVV shares | Real AGG shares |
| Role in book | Intl-equity diversifier | Intl-equity diversifier | US-equity core | Bond ballast |

IEFAON is the **international diversification leg** of the Ondo set: pairing it with [[ishares-core-s-p-500-etf-ondo-tokenized-etf|IVVON]] gives global equity beta on-chain, reducing single-country concentration. Versus holding IEFA directly, the trade-off is on-chain composability and non-US access against custodial counterparty and peg risk.

---

## How & Where It Trades

- **Primary market:** Mint/redeem through Ondo Global Markets for eligible users, gated to US market hours.
- **Secondary market:** On-chain transfers and limited DEX liquidity across [[ethereum|Ethereum]], BNB Smart Chain, and Solana; secondary depth is thin relative to the ~$16.6M market cap.
- **Liquidity:** Mint/redeem is the primary fair-value channel; large orders depend on it rather than DEX depth.

---

## Narrative & Catalysts

IEFAON's thesis is **on-chain access to international TradFi equity beta**: a single composable token for developed-market ex-US diversification, letting non-US holders round out an otherwise US-heavy on-chain portfolio. Catalysts include the broader RWA tokenization wave led by Ondo, rotation toward international equities during periods of US-market underperformance or dollar weakness, and growing demand for diversified on-chain beta beyond the S&P 500.

### History / Timeline

- **2026-04-09** — IEFAON captured in the CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-21** — Market snapshot: $97.25, ~$16.6M market cap, rank #905; -1.49% on the week amid developed ex-US softness.

---

## Risks

- **Issuer / custodian counterparty risk:** Value depends on Ondo and its custodians holding the underlying IEFA shares and honoring redemptions — counterparty and operational risk, not trustless backing.
- **Equity-market risk:** As a broad international-equity basket, IEFAON carries full developed-market equity drawdown risk.
- **Currency risk:** Unhedged exposure to EAFE-region currencies adds an FX layer on top of equity beta.
- **Redemption-gating risk:** Mint/redeem is KYC-gated, non-US-only, and market-hours-bound; halted creations can break the peg arbitrage.
- **Liquidity risk:** Thin on-chain secondary liquidity; mint/redeem is the primary fair-value channel and is gated by market hours and KYC.
- **Regulatory / eligibility risk:** Transfer restrictions and U.S.-person exclusion; evolving regulatory treatment of tokenized securities.
- **Peg / tracking risk:** A breakdown in mint/redeem arbitrage, weekend gaps, or time-zone mismatch could let the on-chain price drift from NAV.

---

## Trading Playbook

- **International diversifier:** Use IEFAON to add developed ex-US equity exposure to an on-chain portfolio that would otherwise be US-concentrated via [[ishares-core-s-p-500-etf-ondo-tokenized-etf|IVVON]].
- **Global equity sleeve:** Combine IEFAON + IVVON for broad global equity beta, then add [[ishares-core-us-aggregate-bond-etf-ondo-tokenized-etf|AGGON]] / [[ishares-20-year-treasury-bond-etf-ondo-tokenized-etf|TLTON]] for bond ballast.
- **Dollar / rotation view:** Hold IEFAON to express a weaker-dollar or international-outperformance thesis; remember the unhedged FX exposure cuts both ways.
- **Execute in US hours:** Transact size while mint/redeem arbitrage is live; be aware of the extra time-zone stale-pricing layer.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | IEFAON |
| **Underlying ETF** | iShares Core MSCI EAFE ETF (IEFA) |
| **Issuer** | Ondo Global Markets ([[ondo-finance|Ondo Finance]]) |
| **Asset class** | Developed ex-US equities (via tokenized ETF) |
| **Market Cap Rank** | #905 |
| **Market Cap** | $16,586,719 |
| **Current Price** | $97.25 |
| **24h Change** | +0.04% |
| **7d Change** | -1.49% |
| **Native Chain** | Ethereum |
| **Categories** | Tokenized Assets, Real World Assets (RWA), Tokenized ETFs, Ondo Tokenized Assets |
| **Website** | [https://app.ondo.finance/assets/iefaon](https://app.ondo.finance/assets/iefaon) |

---

## See Also

- [[ondo-finance]]
- [[real-world-assets]]
- [[etf]]
- [[tokenization]]
- [[ishares-core-s-p-500-etf-ondo-tokenized-etf]] — US-equity sibling
- [[ishares-core-us-aggregate-bond-etf-ondo-tokenized-etf]] — bond-ballast sibling
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). General market knowledge on Ondo Global Markets and the iShares IEFA ETF; no additional specific wiki source ingested yet.

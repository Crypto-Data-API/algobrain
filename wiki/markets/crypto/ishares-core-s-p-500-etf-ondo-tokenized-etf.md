---
title: "iShares Core S&P 500 ETF (Ondo Tokenized ETF)"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, sp500]
aliases: ["IVVON"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://app.ondo.finance/assets/ivvon"
related: ["[[crypto-markets]]", "[[real-world-assets]]", "[[ondo-finance]]", "[[ethereum]]", "[[tokenization]]", "[[etf]]"]
---

# iShares Core S&P 500 ETF (Ondo Tokenized ETF)

**iShares Core S&P 500 ETF (Ondo Tokenized ETF)** (ticker **IVVON**) is a [[tokenization|tokenized]] [[real-world-assets|real-world asset (RWA)]] issued by **[[ondo-finance|Ondo Global Markets]]** on [[ethereum|Ethereum]] (and bridged to Solana and BNB Chain) that gives non-US holders on-chain economic exposure to BlackRock's **iShares Core S&P 500 ETF (NYSE Arca: IVV)** — itself the lowest-cost flagship wrapper on the S&P 500 index, with dividends reinvested into the token's reference value. IVVON is the broad-beta US-equity building block of the Ondo Global Markets line: a single on-chain token that delivers the same 500-stock large-cap exposure a US investor would get from IVV (or SPY/VOO), without the holder ever leaving the chain.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | IVVON |
| **Market Cap Rank** | #361 |
| **Current Price** | $755.31 |
| **Market Cap** | $67.9M |
| **24h Volume** | $389,204 |
| **24h Change** | +0.32% |
| **Circulating Supply** | 89,901 IVVON |
| **Total Supply** | 89,901 IVVON |
| **All-Time High** | $768.16 |
| **All-Time Low** | $638.02 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The ~$755 token price reflects the per-share value of the underlying IVV ETF (which trades near the S&P 500 level scaled by IVV's NAV), not a crypto-native valuation. Each IVVON is intended to be worth one share of IVV, so the token price moves with U.S. equities, and the all-time high near $768 marks a corresponding high in the underlying. Because IVVON's value is anchored to the US session, it is essentially uncorrelated with the crypto cycle: as of 2026-06-23 the crypto [[fear-and-greed-index|Fear & Greed Index]] sits at 21 (Extreme Fear) in a bottoming/accumulation regime, but IVVON's day-to-day path is set by the S&P 500's US trading day, not by Bitcoin (≈$64,568) or ETH (≈$1,737).

---

## Architecture: How the Wrapper Works

IVVON belongs to the **Ondo Global Markets** line of tokenized US equities and ETFs. The structure is a permissioned RWA wrapper rather than a synthetic or basket replica:

- **Issuer / wrapper:** [[ondo-finance|Ondo Finance]], via Ondo Global Markets, structures and issues the token; the on-chain token is a digital claim on a real IVV share.
- **1:1 backing & custody:** Each IVVON is backed 1:1 by a corresponding underlying IVV share, purchased and held off-chain with regulated custodians/brokers (market cap equals FDV, MC/FDV = 1.00). The on-chain token mirrors that custodied position; proof-of-reserves / attestation of the underlying holdings is the integrity anchor.
- **Mint / redeem & KYC gating:** Mint and redeem are restricted to eligible (typically non-US) KYC'd users; "additional restrictions apply," and U.S. persons are generally excluded under the global-markets structure. Eligible users can mint and redeem tokenized US ETFs roughly 24h/day, five days a week, with the issuer accessing traditional exchange liquidity to source or unwind the underlying shares.
- **Oracle / price feed:** The token's reference value is derived from the underlying IVV NAV / share price; on-chain price tracks that feed, with arbitrage via the mint/redeem channel keeping the two anchored.
- **24/7 token vs. market-hours underlying:** IVVON transfers 24/7 on-chain, but IVV trades only during NYSE/Nasdaq sessions. Tight tracking and primary creation/redemption are therefore constrained to US market hours; the token can drift on weekends and overnight.
- **Distributions & expense ratio:** Holders receive exposure "similar to holding IVV and reinvesting dividends" — S&P 500 dividend distributions are reflected in the token's reference value rather than paid out as a separate coupon. The token inherits IVV's underlying expense ratio (~0.03%, among the cheapest equity ETFs), plus any Ondo wrapper fees.
- **Settlement chains:** Native on [[ethereum|Ethereum]], bridged to Solana and BNB Chain.

---

## Tracking & Peg

The token is designed to track IVV (and thus the S&P 500). Key tracking considerations:

- **Premium / discount:** On-chain price can trade above or below the underlying NAV when arbitrage is constrained; the mint/redeem channel is the mechanism that pulls it back to fair value once US markets reopen.
- **Weekend-gap risk:** Because IVV does not trade on weekends or US holidays, IVVON's on-chain price is effectively "stale" relative to news during those windows. A Monday open that gaps the S&P 500 will gap IVVON, and weekend on-chain trades may transact away from the eventual fair value.
- **Tracking error:** IVVON inherits IVV's own (very small) tracking error to the S&P 500 index, plus any incremental dislocation from thin on-chain liquidity.
- **No leverage / no rate duration:** Unlike the bond ETFs in this set (TLTON, AGGON), IVVON carries pure equity beta — no interest-rate duration risk, but full exposure to equity drawdowns.

---

## Comparison vs. Alternatives

| Dimension | **IVVON (Ondo)** | Holding real IVV / SPY | xStock S&P 500 (e.g. SPYx) | IEFAON (intl) / TLTON (bonds) |
|---|---|---|---|---|
| Form | On-chain token, 1:1 IVV-backed | Brokerage ETF share | On-chain tokenized S&P exposure | Ondo tokens, different asset class |
| Access | Non-US KYC'd, on-chain 24/7 | US + global brokerage | Varies by issuer / venue | Same Ondo gating |
| Underlying | S&P 500 (US large-cap) | S&P 500 | S&P 500 | EAFE intl equity / 20yr Treasuries |
| Backing | Real IVV shares, off-chain custody | Direct fund ownership | Issuer-dependent | Real IEFA / TLT shares |
| Hours | Token 24/7; mint/redeem US hours | US market hours | Token 24/7 | Token 24/7; underlying market hours |
| Role in book | Broad US-equity beta core | Broad US-equity beta core | Broad US-equity beta core | Intl diversification / duration |

IVVON's distinguishing feature within the Ondo set is that it is the **broadest, lowest-volatility equity building block** — where [[micron-technology-ondo-tokenized-stock|MUON]] (single semis name) and [[circle-internet-group-ondo-tokenized-stock|CRCLON]] (single fintech name) are concentrated single-stock bets, IVVON is the diversified market-beta anchor. Versus xStock-style S&P tokens, the practical difference is issuer, custody model, and eligibility rules rather than the underlying index.

---

## How & Where It Trades

- **Primary market:** Mint/redeem through Ondo Global Markets for eligible users; primary creation/redemption is gated to US equity trading hours since it requires transacting in the underlying IVV.
- **Secondary market:** On-chain transfers and limited DEX liquidity across [[ethereum|Ethereum]], Solana, and BNB Chain. Secondary volume (~$0.4M/24h) is modest relative to the ~$68M market cap.
- **Liquidity:** Large orders rely on the primary mint/redeem channel rather than DEX depth; on-chain secondary depth is thin and can widen spreads outside US hours.

---

## Narrative & Catalysts

IVVON's thesis is **on-chain access to TradFi beta**: it lets non-US users hold the single most benchmarked equity exposure on earth (the S&P 500) as a composable on-chain token — usable as collateral, in DeFi, or simply as a 24/7-transferable savings/beta vehicle — without a US brokerage account. Catalysts that grow this category include the broader RWA tokenization wave led by Ondo and BlackRock's own on-chain ambitions, rising non-US demand for dollar-denominated equity beta, and DeFi venues accepting tokenized ETFs as collateral.

### History / Timeline

- **2026-04-09** — IVVON captured in the CoinGecko top-1000 snapshot at rank #361 (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-21** — Market snapshot: $755.31, ~$68M market cap, all-time high $768.16 / all-time low $638.02.

---

## Risks

- **Issuer / custodian counterparty risk:** Dependence on [[ondo-finance|Ondo]], its brokers, and custodians holding the underlying IVV shares. Issuer or custodian failure is the primary tail risk; backing is custodial, not trustless.
- **Redemption-gating risk:** Mint/redeem is KYC-gated, non-US-only, and limited to US market hours. If creations/redemptions are paused, the arbitrage that holds the peg can break.
- **Tracking / peg risk:** Price can diverge from IVV/the S&P 500 during off-hours, weekends, or when arbitrage capacity is limited; the token also inherits IVV's (small) tracking error to the index.
- **Liquidity risk:** Thin on-chain secondary liquidity can make exits costly outside the primary mint/redeem window.
- **Market risk:** Full exposure to US equity drawdowns — IVVON falls one-for-one with the S&P 500. (No interest-rate duration risk, unlike the bond ETFs in this set.)
- **Regulatory risk:** Tokenized securities face an evolving, jurisdiction-specific regime; eligibility rules can change and restrict holders.
- **Smart-contract / bridge risk:** Multi-chain deployment widens the attack surface.
- **Macro backdrop:** As of 2026-06-23 the crypto Fear & Greed Index reads 21 (Extreme Fear) with market-health 29/100 (bearish, bottoming/accumulation). IVVON's risk is driven by US equities rather than crypto beta, but on-chain liquidity for the wrapper can still thin in risk-off crypto regimes.

---

## Trading Playbook

- **Broad-beta core:** Use IVVON as the on-chain equivalent of a US large-cap index allocation — the diversified beta anchor of an on-chain portfolio.
- **Pair with diversifiers:** Combine with [[ishares-core-msci-eafe-etf-ondo-tokenized-etf|IEFAON]] for international equity diversification and [[ishares-20-year-treasury-bond-etf-ondo-tokenized-etf|TLTON]] / [[ishares-core-us-aggregate-bond-etf-ondo-tokenized-etf|AGGON]] for duration/bond ballast to build a classic stock/bond mix entirely on-chain.
- **Mind the calendar:** Execute size during US market hours when mint/redeem arbitrage is live; avoid transacting large weekend orders into a stale on-chain price.
- **Not a crypto-cycle play:** Treat IVVON's drivers as the US equity session, not the crypto Fear & Greed regime.

---

## Platform & Chain Information

**Deployment:** Multi-chain ([[ethereum|Ethereum]], Solana, BNB Chain)

| Chain | Address |
|---|---|
| Ethereum | `0x62ca254a363dc3c748e7e955c20447ab5bf06ff7` |
| BNB Chain | `0x1104eb7e85e25eb45f88e638b0c27a06c1a91cb2` |
| Solana | `CqW2pd6dCPG9xKZfAsTovzDsMmAGKJSDBNcwM96ondo` |

---

## See Also

- [[ondo-finance]] — issuer (Ondo Global Markets)
- [[ishares-core-msci-eafe-etf-ondo-tokenized-etf]] — intl-equity sibling
- [[ishares-20-year-treasury-bond-etf-ondo-tokenized-etf]] — long-duration bond sibling
- [[ishares-core-us-aggregate-bond-etf-ondo-tokenized-etf]] — aggregate-bond sibling
- [[real-world-assets]] / [[tokenization]]
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). General market knowledge on Ondo Global Markets and the iShares IVV ETF; no additional specific wiki source ingested yet.

---
title: "FTX Collapse Arbitrage (November 2022)"
type: news
created: 2026-04-26
updated: 2026-06-12
status: good
tags: [crypto, history, ftx, exchange-collapse, sbf, arbitrage]
aliases: ["FTX Implosion", "SBF Collapse", "Alameda Wind-Down", "FTT Death Spiral"]
event_date: 2022-11-08
markets_affected: [crypto, defi]
impact: high
verified: true
sources_count: 5
related: ["[[bankruptcy-claim-arbitrage]]", "[[2022-06-three-arrows-blowup]]", "[[block-trade-flipping-arbitrage]]", "[[liquidation-cascade-arbitrage]]"]
---

# FTX Collapse Arbitrage (November 2022)

Between **November 2-11, 2022**, FTX — then the world's second-largest crypto exchange — collapsed in 10 days following a CoinDesk report on Alameda Research's balance sheet, triggering the second-largest crypto-industry collapse in history (after Mt. Gox 2014). FTT (FTX exchange token) fell from $25 to ~$2; Solana ecosystem tokens dropped 40-70% in a week; total bankruptcy claims totaled **$8.7B**. Sophisticated arbitrageurs profited via three vectors: pre-positioning on the CoinDesk report, FTT-vs-spot triangulation during the death spiral, and post-bankruptcy claim trading that ultimately delivered **>100¢ recovery to creditors** (FTX customers were eventually paid in full + interest).

## The Trigger

**November 2, 2022 — CoinDesk report:**
- Ian Allison published *"Divisions in Sam Bankman-Fried's Crypto Empire Blur on His Trading Titan Alameda's Balance Sheet"*.
- Revealed Alameda's June 30, 2022 balance sheet showed $14.6B assets — but $5.8B was FTT (Alameda owned more FTT than circulating supply traded daily).
- Implication: Alameda was using FTX-issued tokens as collateral for borrowings; if FTT price fell, Alameda was insolvent.

**November 6, 2022 — CZ tweets:**
- Binance CEO Changpeng Zhao announced Binance would liquidate its remaining $529M FTT position.
- "Recent revelations" cited.
- FTT immediately began dropping.

**November 8, 2022 — Bank run:**
- FTX customers attempt withdrawals; queue grows from $250M/day to $5B+ Tuesday.
- FTX halts withdrawals.
- Binance announces non-binding LOI to acquire FTX.

**November 9, 2022:** Binance withdraws acquisition LOI after due diligence.

**November 11, 2022:** FTX, FTT, Alameda Research, and ~130 affiliates file for Chapter 11 bankruptcy in Delaware.

## The Cascade

| Date | FTT | SOL | BTC | Comment |
|------|-----|-----|-----|---------|
| Nov 1 | $25 | $32 | $20,500 | Pre-CoinDesk |
| Nov 2 | $24 | $32 | $20,400 | CoinDesk report |
| Nov 6 | $22 | $30 | $20,800 | CZ tweet |
| Nov 7 | $16 | $25 | $20,500 | Death spiral begins |
| Nov 8 | $7 | $14 | $17,500 | Withdrawal halt |
| Nov 9 | $4 | $13 | $16,000 | Binance LOI fails |
| Nov 11 | $1.50 | $11 | $16,800 | Bankruptcy filing |
| Dec 31 | $1.20 | $10 | $16,500 | Year-end |

Solana's collapse was particularly violent because:
- SBF was Solana's largest external supporter.
- FTX held large SOL positions that needed to be liquidated.
- Solana ecosystem tokens (SRM, RAY, FIDA, MAPS, OXY, MEDIA) were structurally tied to FTX.

## Triangular Arbitrage Opportunities

**Trade 1: Pre-CoinDesk-report short.** Sophisticated readers of public on-chain data (CoinDesk Marc Hochstein and team had been investigating for months) had advance signals. Some hedge funds reportedly built FTT shorts in October 2022 at $25-30; covered at $1.50 = 95% return.

**Trade 2: FTT death-spiral short.** Once CZ tweeted Nov 6, the death spiral was structurally certain. Shorts entered at $20-22 covered at $2-4 = 80-90% return in 4-5 days.

**Trade 3: Solana/SOL ecosystem short.** SOL fell from $32 to $11 in 10 days. Pair trade: short SOL, long ETH (less FTX-exposed). ETH/SOL ratio nearly doubled in 2 weeks.

**Trade 4: BTC funding-rate trade.** BTC perp funding spiked positive (long-side panic) then deeply negative (forced selling) within 72 hours. Funding-rate arb across Binance/Bybit/OKX was 50-150% APR for several days.

**Trade 5: FTX claim trading.** Customer claims initially traded at 8-15¢ in late November 2022. Recovery exceeded expectations:
- Specialist firms (Olympus Peak, FactsETF) bought claims at 10-15¢ in 2022.
- Mid-2023: claims at 30-40¢.
- Late 2023: claims at 60-80¢ as recovery thesis improved.
- 2024: claims at 100¢+ as recovery exceeded liabilities.
- October 2024 reorg plan: 100% recovery + interest for non-government claims (the "petition date" valuation made customers whole on the dollar value of crypto in November 2022, even though crypto then 4x'd).

Specialist claim traders extracted **5-10x returns** over 18-24 months. Among the largest single-event arbitrage profits in crypto history.

**Trade 6: Solana ecosystem token block sales.** FTX bankruptcy estate sold $1.4B+ in SOL, SRM, MAPS, OXY tokens via OTC blocks 2023-2024. Buyers (Pantera, Galaxy Digital, Multicoin) absorbed at deep discounts and held; SOL recovered from $10 to $200+ by early 2024 = 20x return.

## Winners

**Specialist claim traders** — Olympus Peak, FactsETF, Cherokee Acquisition, Castlelake, Diameter Capital. Estimated $1-3B+ in extracted value across the multi-year claim recovery.

**Solana ecosystem accumulators** — Multicoin Capital, Pantera, Galaxy Digital — bought SOL at $10-20 from FTX estate liquidation; held through $200+ recovery. Multi-billion dollar trade.

**Pre-positioned shorts** — Smaller specialist funds that read the CoinDesk report and shorted FTT immediately; estimated 50-200% returns.

**Distressed CEO Stephen Ehrlich (Voyager)** — Voyager's bankruptcy estate received better-than-expected recovery via Galaxy / FTX bid wars.

**John J. Ray III (FTX trustee)** — Earned ~$30M in fees managing the recovery; resurrected reputation from Enron.

## Losers

**FTX retail customers (initially)** — Withdrew unable November 8, 2022; lost access to $8.7B+ in assets. Eventually made whole via 2024 plan but lost 18-24 months of opportunity cost (and crypto 4x'd in that window).

**Sequoia Capital** — $214M FTX investment marked to zero. Embarrassing public retraction of the Sam Bankman-Fried profile.

**Tom Brady, Gisele Bündchen, Steph Curry, Larry David** — High-profile FTX endorsers; faced class-action lawsuits.

**SBF / Caroline Ellison / Sam Trabucco / Gary Wang / Nishad Singh** — Indicted; SBF convicted October 2023 on 7 counts; 25-year sentence March 2024.

**Crypto industry sentiment** — 2022-2023 "crypto winter" extended; institutional adoption pause; regulatory scrutiny intensified globally.

## Aftermath

- **November 22, 2022:** John J. Ray III appointed CEO/Chief Restructuring Officer.
- **December 12, 2022:** SBF arrested in Bahamas; extradited to US.
- **March 2023:** Caroline Ellison, Sam Trabucco, Gary Wang plead guilty.
- **October 2023:** SBF guilty on 7 counts.
- **March 2024:** SBF sentenced to 25 years.
- **October 2024:** FTX reorganization plan confirmed; 100% recovery + interest for most claims.
- **2024-2025:** Customer payouts begin; FTT ironically rallied post-confirmation.
- **2025:** SBF appeals; Caroline Ellison sentenced to 2 years.

## Lessons for Crypto Traders

1. **Read the public balance sheets.** CoinDesk's FTT-collateral analysis was based on publicly available June 30, 2022 financials. The thesis was discoverable for any analyst willing to do the work.
2. **CEX tokens used as collateral = systemic risk.** FTT, BNB, OKB, KCS — the pattern repeats. Self-issued tokens cannot truly collateralize self-issued exchanges.
3. **Distressed claim trading is the highest-Sharpe crypto strategy.** FTX claim traders earned 5-10x in 18-24 months on what was essentially "buy the recovery delta."
4. **Forced-seller cascades during exchange collapses generate generational entry prices.** SOL at $10 → $200 = 20x within 18 months for those who absorbed estate liquidations.
5. **Personal-brand-as-trust-signal is fragile.** SBF's "Effective Altruism" persona collapsed in days; lesson for both investors and operators.
6. **Recovery > liabilities is rare but possible.** Crypto bull market 2023-2024 turned FTX bankruptcy from -50¢ recoveries to 100%+ recoveries.

## Sources

- *FTX Trading Ltd. Chapter 11 Plan*, In re FTX Trading Ltd. (D. Del. October 2024).
- Ian Allison / CoinDesk, *Divisions in SBF's Crypto Empire Blur on Alameda Balance Sheet* (November 2, 2022).
- John J. Ray III testimony before US House Financial Services Committee (December 2022).
- Michael Lewis, *Going Infinite* (2023) — biographical context.
- *FTX Bankruptcy Examiner Reports* (2023).

## Related

[[bankruptcy-claim-arbitrage]] · [[2022-06-three-arrows-blowup]] · [[block-trade-flipping-arbitrage]] · [[liquidation-cascade-arbitrage]] · [[2022-05-terra-luna-depeg-arb]] · [[2022-06-steth-depeg]] · [[gbtc-discount-arbitrage]] · [[archegos-blowup-2021]]

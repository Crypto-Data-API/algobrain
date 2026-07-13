---
title: "COVID Crash (February-March 2020)"
type: news
created: 2026-05-07
updated: 2026-06-12
status: good
tags: [history, crash, volatility, covid, vix, options, circuit-breakers, fed]
aliases: ["COVID Crash", "COVID-19 Crash", "March 2020 Crash", "Pandemic Crash", "Coronavirus Crash", "Pandemic", "pandemic"]
event_date: 2020-03-16
markets_affected: [stocks, options, credit, treasuries, oil, crypto]
impact: high
verified: true
sources_count: 7
related: ["[[long-vol-vs-short-vol]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[gfc]]", "[[black-monday]]", "[[universa-investments]]", "[[mark-spitznagel]]", "[[nassim-taleb]]", "[[tail-risk-hedging]]", "[[bill-ackman]]", "[[2020-03-ackman-pandemic-cds-trade]]", "[[circuit-breakers]]", "[[federal-reserve]]", "[[treasury-basis-trade]]", "[[crisis-alpha]]", "[[long-vol-overlay]]", "[[variance-risk-premium]]", "[[volatility-regime-classification]]"]
---

The COVID crash of **February-March 2020** was the fastest 30%+ S&P 500 drawdown in history: SPX fell 33.9% from its **February 19, 2020** intraday high of 3393.52 to its **March 23, 2020** intraday low of 2191.86 in just 23 trading sessions. The CBOE [[vix-futures|VIX]] index closed at **82.69 on March 16, 2020**, the highest closing print on record (eclipsing the 80.86 close on November 20, 2008 during the [[gfc]]). Four [[circuit-breakers|Level 1 market-wide circuit breakers]] tripped in eight sessions. [[universa-investments|Universa Investments]] reportedly returned **+4,144%** for the month on its tail-risk strategy, the canonical empirical demonstration of the long-vol case. The episode is the single largest vol monetization of the modern era and the reference event for [[long-vol-vs-short-vol|long-vol versus short-vol]] book performance.

## Overview

Through the second half of 2019 and into early 2020, US equity markets had run a multi-quarter low-vol grind: SPX rose ~30% from October 2018 to February 2020, realized vol was sub-12, and short-vol strategies were once again earning a quiet, large chunk of the [[variance-risk-premium]]. The early COVID-19 outbreak in Wuhan in late January received only modest market attention. SPX closed at an all-time high on February 19 2020. Within four weeks, the slowest-acting health crisis in modern memory had become the fastest-acting financial crisis, repricing essentially every asset class simultaneously and forcing the largest, fastest, broadest central-bank response in history.

## What Happened

**Wednesday, February 19 2020.** SPX closes at all-time high 3386.15 (intraday 3393.52). VIX 14.4. Vol-selling and risk-parity books at full risk.

**Monday, February 24 -- Friday, February 28 2020.** Italy's outbreak becomes the first major non-China cluster. SPX falls 11.5% over the week. VIX rises from 17 to 40.

**Monday, March 9 2020.**
- Saudi Arabia announces a price war with Russia after the OPEC+ deal collapses; WTI crude falls ~25% overnight.
- SPX opens down ~7%; the **first Level 1 circuit breaker** in 23 years trips at 9:34am ET, halting trading for 15 minutes.
- SPX closes -7.6%, VIX 54.5.

**Wednesday, March 11 2020.** WHO declares COVID-19 a pandemic. SPX -4.9%, VIX 53.9.

**Thursday, March 12 2020.**
- Fed's first emergency action: $1.5T in repo and broader Treasury purchases announced mid-session.
- **Second Level 1 circuit breaker** trips at the open.
- SPX closes -9.5%, the largest single-day percentage drop since [[black-monday|Black Monday 1987]] until that date. VIX 75.5.

**Sunday, March 15 2020.** Fed cuts the federal funds rate to 0-0.25% in an emergency Sunday move and announces $700B of QE.

**Monday, March 16 2020.**
- Despite the Sunday Fed action, SPX futures lock limit-down overnight.
- **Third Level 1 circuit breaker** trips at the open.
- SPX closes **-12.0%, the largest one-day drop since 1987**. VIX closes at **82.69**, the highest closing VIX in history.
- 10y Treasury yields whipsaw despite Fed buying; the [[treasury-basis-trade]] is unwinding violently as relative-value funds sell on-the-run Treasuries to meet margin calls.

**Wednesday, March 18 2020.** **Fourth Level 1 circuit breaker** trips. Treasury futures liquidity is the worst on record per several dealer microstructure reports. Investment-grade credit spreads gap wider; corporate bond ETFs (LQD, HYG) trade at material discounts to NAV.

**Monday, March 23 2020.**
- Fed announces **unlimited QE and direct purchase of investment-grade and (later) high-yield corporate bonds** via emergency 13(3) facilities (the SMCCF and PMCCF).
- SPX makes its closing low at **2237.40**; intraday low **2191.86**, marking a **-33.9% peak-to-trough**.
- The drawdown is over. From this date, SPX reverses and rallies almost without interruption back to new all-time highs by August 2020.

**Friday, March 27 2020.** US Congress passes the $2.2T CARES Act fiscal package.

The full peak-to-trough was 23 trading sessions. The full round-trip back to the prior high took roughly 5 months -- the fastest bear-market recovery in modern history.

## Mechanism / Why It Happened

Three layered shocks compounded:

1. **Fundamental: pandemic-driven economic shutdown.** Forced economic contraction was the proximate trigger. The collapse in Q2 GDP (-31% annualized in the US) was the largest since the Great Depression.
2. **Structural: forced-deleveraging and basis-trade unwind.** Risk-parity funds, vol-target ETFs, and CTA portfolios mechanically cut equity exposure as realized vol exploded. The [[treasury-basis-trade]] -- relative-value hedge funds long cash Treasuries / short Treasury futures financed in repo -- broke down as funding costs blew out, forcing cash-Treasury sales into a market that was supposed to be the safe haven. This drove the unprecedented mid-March behaviour where Treasuries and equities sold off together.
3. **Liquidity: dealer balance-sheet constraints.** Post-2008 regulation (SLR, Volcker) constrained dealer ability to absorb the wave of forced selling. The Fed had to step in not just as lender of last resort but as **buyer of last resort** across a broader range of assets than at any point in its history.

Vol on the way down was extreme but rational given the realized variance: SPX had multiple 7-12% daily moves; trailing 21-day realized vol exceeded 90% by mid-March. Implied vol was high but, in retrospect, nearly fairly priced relative to the path that was actually realized.

## Casualties / Survivors

**Casualties.**
- **Risk-parity and vol-target funds.** Bridgewater's All Weather and Pure Alpha reported drawdowns of ~12-21% for the quarter. Vol-target ETFs (e.g., risk-control indices embedded in structured notes) mechanically delevered into the lows.
- **Naked short-vol books and short-strangle accounts.** A repeat of the [[volmageddon|2018]] population pattern: many retail accounts lost 50-100% of equity. Several short-vol mutual funds wound down or marked down sharply (e.e.g., LJM had already wound down in 2018).
- **Treasury basis-trade hedge funds.** Several relative-value funds reported 20-40% drawdowns. Some closed; others returned investor capital. The Fed's repo facilities and Treasury purchases ultimately staunched the bleeding.
- **Oil-related credit and producers.** WTI fell to below zero on April 20 2020 (the WTI May contract printed -$37); leveraged ETPs tracking oil futures (USO) restructured; several oil-linked structured products were terminated.
- **Investment-grade and high-yield corporate credit.** Spreads gapped wider; the LQD ETF traded at a 5-7% discount to NAV in mid-March. The Fed's SMCCF/PMCCF facilities reversed this within weeks.

**Survivors and beneficiaries.**
- **[[universa-investments]]** -- reportedly returned **+4,144% for March 2020** on the tail-risk overlay capital. For a client with a 3.3% allocation to Universa and 96.7% in equities, the portfolio-level math was approximately +4,144% × 3.3% ≈ +137% contribution from the overlay versus -34% × 96.7% ≈ -33% from the equity book, for a roughly **+104% net portfolio month** -- the textbook empirical case for [[tail-risk-hedging]].
- **[[bill-ackman]] / Pershing Square.** Hedged the firm's portfolio in late February with **$27M of CDS protection on $71B notional of investment-grade and high-yield indices**, monetized for **$2.6B in late March** -- a roughly 100x return on the hedge. See [[2020-03-ackman-pandemic-cds-trade]].
- **CTAs and managed-futures.** Trend models had been long stocks, long bonds, short oil; the rapid reversal hurt early but the late-March short-equity / long-bond positioning monetized through April-May. Full-year 2020 was strong for trend-following.
- **Long-vol overlay sleeves.** The [[long-vol-overlay]] configuration described in [[long-vol-vs-short-vol]] absorbed the equity drawdown and freed allocators to **buy the lows** rather than be forced sellers.
- **[[mark-spitznagel]]** publicly used the March 2020 result to argue that the prior decade of premium bleed was inexpensive insurance properly priced.

## Impact on Vol Books

The COVID crash is the single most important empirical event in modern vol-book history because it provided a **clean, large monetization** that decisively settled the long-running argument about whether tail-risk hedging is worth its annual cost.

- **Pure long vol** had its banner event. Universa's 4,144% figure is widely cited and -- whatever the precise calculation methodology -- is consistent with the path-dependent payoff of deep-OTM SPX puts when SPX falls 30% in 23 sessions.
- **Pure short vol** absorbed catastrophic drawdowns. Naked short-strangle accounts that survived [[volmageddon|February 2018]] were liquidated. Short-vol funds that had quietly grown AUM through 2019 disappeared.
- **Short vol with long-vol overlay.** The synthesis worked at the largest test of the decade. Books with overlays sized at 5-10% of vega budget cut net drawdowns from a hypothetical -50%/-100% to -10%/-15%. The overlay's [[vega]] gain dominated everything else on the book.
- **Variance-swap and dispersion books.** Index variance swaps marked at par-vol levels of 60-80; dispersion baskets monetized strongly as single-stock vol exploded relative to index vol.

The episode also reinforced -- in a way Volmageddon had only sketched -- that vol shocks come in **multiple flavours**: 2018 was an ETP microstructural unwind, 2020 was a fundamental forced-deleveraging, [[vix-august-2024-spike|2024]] was a positioning unwind. A robust long-vol overlay must be cheap enough to fund through multi-year calm but rich enough in convexity to monetize all three regimes. See [[long-vol-overlay]].

## Lessons / Takeaways

1. **Tail-risk hedging works at scale.** Universa, Pershing's CDS hedge, and the long-vol overlay community all delivered the convex payoff their mandates promised, in size, on the same trade. The decade's debate about whether the cost is "worth it" was empirically resolved.
2. **Speed matters more than depth.** The [[gfc|GFC]] was a deeper drawdown but ran 17 months; COVID was 23 sessions. Strategies whose [[kill-criteria]] reference monthly performance never engaged. Anything depending on backstop hedges had to have the hedges already on the book.
3. **Treasuries are not always the hedge.** During the worst week of mid-March, the 10y Treasury sold off as funds liquidated to meet margin calls. The reflexive "60/40 rebalance" failed for several days. Long-vol overlays do not have this failure mode because their P&L is mechanically convex in the equity move.
4. **The Fed will intervene faster than expected.** The Mar 23 unlimited-QE-plus-corporate-credit announcement was the fastest, broadest central-bank action in history. Strategies betting on a multi-month bear market underperformed the V-shaped recovery.
5. **The synthesis is not optional.** Naked short vol is a guaranteed-ruin strategy on a long enough horizon. The COVID crash is the third in a four-decade series of empirical demonstrations ([[black-monday|1987]], [[gfc|2008]], [[volmageddon|2018]], COVID, [[vix-august-2024-spike|2024]]).

## Related

- [[long-vol-vs-short-vol]] -- the framework into which the event slots
- [[universa-investments]], [[mark-spitznagel]], [[nassim-taleb]] -- the canonical long-vol survivors
- [[tail-risk-hedging]] -- the strategy validated by the event
- [[bill-ackman]], [[2020-03-ackman-pandemic-cds-trade]] -- the CDS hedge case study
- [[volmageddon]], [[vix-august-2024-spike]] -- adjacent vol shocks
- [[gfc]], [[black-monday]] -- prior reference events
- [[circuit-breakers]] -- the market-wide halt mechanism that triggered four times
- [[federal-reserve]] -- the institution whose response defined the recovery
- [[treasury-basis-trade]] -- the relative-value trade that broke
- [[crisis-alpha]] -- the category of returns delivered by long-vol books
- [[long-vol-overlay]] -- the synthesis that worked
- [[variance-risk-premium]] -- the premium short-vol books had been harvesting
- [[volatility-regime-classification]] -- "Crisis" regime in extremis

## Sources

- CBOE historical VIX data, March 16 2020 close 82.69 (highest in CBOE VIX history).
- S&P 500 historical price data, Feb 19 2020 high 3393.52 to Mar 23 2020 low 2191.86 (-33.9% peak-trough).
- *Wall Street Journal*, March 2020 daily coverage of circuit-breaker halts and Fed actions, including the March 12 and March 16 sessions.
- *Bloomberg*, "Universa's Tail Risk Fund Returns 4,144% in March," April 2020 -- the headline reporting on Spitznagel's March return.
- Pershing Square Capital Management investor letter, Q1 2020 -- documenting the $27M-to-$2.6B CDS hedge.
- Federal Reserve press releases, March 12 / March 15 / March 23 2020 -- the emergency rate cut, QE expansion, and unlimited-QE-plus-13(3) facility announcements.
- Spitznagel, Mark. *Safe Haven: Investing for Financial Storms* (2021) -- post-event reflection and portfolio-level math.
- Taleb, Nassim Nicholas, post-event interviews and Twitter posts, March-April 2020.
- BIS and Fed staff papers on the March 2020 Treasury market dysfunction and the [[treasury-basis-trade]] unwind.

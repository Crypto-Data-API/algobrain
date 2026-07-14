---
title: "VIX August 2024 Spike (Yen-Carry Unwind)"
type: news
created: 2026-05-07
updated: 2026-06-12
status: good
tags: [volatility, history, vix, options, short-vol-blowup, yen-carry, japan, macro]
aliases: ["August 2024 VIX spike", "August 5 2024 vol shock", "Yen-carry unwind 2024", "Aug 5 2024", "VIX 65 Spike", "Aug 2024 Vol Shock", "Aug 5 Yen Crash", "Nikkei Crash 2024", "Carry Unwind 2024", "BoJ Hike Aftermath"]
event_date: 2024-08-05
markets_affected: [stocks, options, forex, japan]
impact: high
verified: true
sources_count: 6
related: ["[[long-vol-vs-short-vol]]", "[[volmageddon]]", "[[covid-crash]]", "[[short-strangle]]", "[[variance-risk-premium]]", "[[vix-futures]]", "[[vix-term-structure]]", "[[carry-trade]]", "[[yen-carry-trade]]", "[[bank-of-japan]]", "[[universa-investments]]", "[[long-vol-overlay]]", "[[volatility-regime-classification]]", "[[gamma]]", "[[vega]]", "[[zero-dte-options]]", "[[liquidity-cascade]]"]
---

The VIX spike of **August 5, 2024** was the largest single-day percentage move in spot VIX history, with intraday prints near 65 from a Friday close near 23 -- a rise of roughly 180% before substantial mean-reversion later in the session. The trigger was a violent unwind of the [[yen-carry-trade|JPY-funded carry trade]] following a hawkish Bank of Japan policy shift and a softer-than-expected US July payrolls print, which compressed three weeks of macro-positioning losses into a 12-hour window across Asia, Europe, and US futures. The shock liquidated a meaningful tail of short-strangle accounts and short-vol overlays and is the most recent canonical example of the asymmetry described in [[long-vol-vs-short-vol]].

## Overview

For most of 2024, the macro environment had been close to the textbook short-vol regime: low realized SPX vol, persistent rate-differential carry into USD assets funded in JPY, and a trending equity tape. The CBOE [[vix-futures|VIX]] index spent the first seven months of 2024 mostly between 12 and 16. As of late July, JPY had weakened to roughly USDJPY 162, the cleanest carry-funded leg of the global risk trade in over a decade. Short-vol strategies -- both retail short-strangle accounts and institutional [[variance-risk-premium]] sleeves -- had earned a strong year of theta.

Two events compounded over the final week of July and the first week of August. The Bank of Japan, on July 31 2024, raised its policy rate by 15bp (to ~0.25%) and signalled balance-sheet normalization. On August 2, the US July nonfarm-payrolls print came in at 114K versus consensus ~175K, with the unemployment rate jumping to 4.3% and triggering the Sahm-rule recession indicator. The dollar fell sharply against the yen; carry positions began to unwind. The unwind ran into the weekend with little liquidity to absorb it, and Monday Aug 5 opened with a global liquidity cascade.

## What Happened

**Wednesday, July 31 2024.** BoJ raises rate to 0.25%, governor Ueda's press conference is read as hawkish. USDJPY falls from ~152 to ~150. SPX closes ~+1.6% (pre-shock).

**Friday, Aug 2 2024.** US July payrolls miss (114K vs 175K consensus), unemployment 4.3%. SPX falls 1.8%, VIX closes near 23.4 (up from ~16 a week prior). USDJPY breaks 147. Asian and European weekend liquidity is thin.

**Sunday-Monday, Aug 4-5 2024 (Asia open).** The Topix opens sharply lower; Japanese banks fall ~20%+ over the session. Nikkei 225 closes Aug 5 down 12.4%, its worst single-day percentage drop since [[black-monday|Black Monday 1987]]. USDJPY trades down to ~141.7 intraday.

**Monday, Aug 5 2024 (US open).**
- SPX futures gap down ~3-4% pre-market.
- Spot VIX prints an intraday high near 65.7 in the first hour of US cash trading -- the highest reading since the [[covid-crash|March 2020 crash]] and the largest one-day percentage move in spot VIX since the index's 1990 inception.
- VIX futures front-month spikes from ~17 Friday close to ~38 intraday, an unusually large but smaller-magnitude move than spot VIX -- a sign that the spike was concentrated in [[zero-dte-options|short-dated]] index options where dealers were short [[gamma]].
- The VIX prints between ~50 and 65 are widely read as **stale-quote artefacts**: bid-ask spreads in deep-OTM SPX puts widened so much that the implied-vol calculation feeding the VIX produced unreliable values for roughly 90 minutes.
- SPX itself fell only ~3% on the day before recovering. VIX closed at 38.6, well off the intraday high but still up ~65% on the day.

**Tuesday, Aug 6 -- Friday, Aug 9 2024.** SPX recovers most of the move within four sessions; VIX falls back to the mid-20s by Aug 9. The Bank of Japan's deputy governor Uchida walks back the hawkish guidance on Aug 7, calming JPY and risk assets.

The full peak-to-trough on SPX was roughly **-8.5%** from the July 16 high to the Aug 5 low. The vol move was vastly larger than the underlying equity move suggested -- the same decoupling signature observed in [[volmageddon|February 2018]].

## Mechanism / Why It Happened

Three layered drivers:

1. **JPY-funded carry unwind.** Estimates from BIS, JPMorgan, and Goldman put the gross size of JPY-funded carry positions at $500B-$1T+ across FX, equities, and credit by mid-2024. A coordinated unwind requires buyers of JPY against a thinly-positioned market, and the speed of that unwind drove the FX and equity legs together in a feedback loop.

2. **Dealer short-gamma in short-dated options.** Through 2023-2024, retail and institutional flows had pushed open interest in [[zero-dte-options|0-DTE]] and short-dated SPX options to record levels, and the dealer community ran consistently short [[gamma]] in those tenors. When SPX gapped down, dealers needed to **sell** index futures to re-hedge -- which mechanically extended the move and was the same reflexivity Charlie McElligott (Nomura) and Brent Kochuba (SpotGamma) had warned about for months.

3. **VIX-microstructure stale-quoting.** The CBOE's spot VIX index is computed from a strip of SPX option bid-ask midpoints. When SPX option spreads widen 10-20x in a vol shock and the strip includes deep wings that are essentially un-quotable, the VIX print becomes mechanically unstable. Several CBOE members and analysts (notably Christopher Cole and various sell-side desks) noted that the 60-65 intraday VIX prints overstated the true tradable vol level by 10-20 points. The futures market priced it more honestly at ~38.

The triggering macro event -- a soft payrolls print and a 15bp BoJ hike -- was small compared to historical vol-shock catalysts. The shock is best understood as a positioning unwind compounded by short-gamma dealer hedging and VIX-index microstructure quirks, not as a fundamental repricing of US recession risk.

## Casualties / Survivors

**Casualties.**
- **Retail short-strangle accounts.** Brokerage forums, Tastytrade community threads, and several public client letters documented retail accounts that lost 40-90% of equity. Many had layered in additional short premium during the late-July rise in IV, increasing the gap-risk loss.
- **JPY-funded discretionary global-macro books.** Multiple multi-strategy funds reported drawdowns of 3-8% on the day from the FX leg alone. Several Japanese real-money accounts cut equity exposure into the cascade.
- **0-DTE retail call/put-selling strategies.** "Daily income" strategies built around overnight 0-DTE put-spread sales encountered a Monday gap that put many positions through the short strike at the open, with limited ability to manage out.
- **Short-vol structured products** with embedded short-strangle exposure repriced sharply; redemption queues opened at several issuers.
- **A small number of named funds** (e.g. "Conifer", "Optio Lux"-style short-premium vehicles) reported drawdowns of 20-50% on the week. The damage was less terminal than [[volmageddon|February 2018]] because most institutional vehicles by 2024 had wing-bought defined-risk structures rather than naked strangles.

**Survivors and beneficiaries.**
- **[[universa-investments]]** -- structurally long deep-OTM SPX puts, monetized a portion of the spike in line with its barbell mandate.
- **Long-vol overlay sleeves.** Books with explicit overlays (the synthesis described in [[long-vol-vs-short-vol]]) absorbed the day with single-digit drawdowns.
- **VIX call-spread holders.** Buyers of front-month VIX 25/40 call spreads put on in mid-July paid roughly $0.80 and saw the structure mark to nearly $14 intraday on Aug 5 -- a ~17x payoff before mean-reversion.
- **CTAs and managed-futures.** Trend models had been short JPY/long USD into the shock; many cut and reversed, capturing a portion of the move.

## Impact on Vol Books

August 5 2024 reinforced the post-2018 evolution of the vol-book structure:

- **Naked short-vol books** -- particularly retail strangle accounts -- took the maximum-asymmetry loss again, six and a half years after [[volmageddon]] supposedly taught the lesson. The lesson is recurring because the population of short-vol participants turns over every cycle.
- **Defined-risk short-vol structures** ([[iron-condor|iron condors]], put-spread sales) bounded losses to the wing distance. They still lost, but losses were arithmetic, not geometric.
- **Pure long-vol books.** Aug 5 2024 was a real but not banner monetization. Universa and similar mandates likely added several years of expected return in a session, but the move did not match the magnitude or duration of [[covid-crash|March 2020]] or [[gfc|2008]].

The episode also accelerated regulatory and structural attention to **VIX-index quoting in stress**. Several proposals to amend the VIX calculation to exclude clearly stale wings, or to publish a parallel "tradable VIX" reference, gained traction at CBOE in late 2024 and 2025.

## Lessons / Takeaways

1. **Macro positioning unwinds are vol-shock catalysts.** Fundamental newsflow on Aug 5 was modest. The shock came from the speed at which a multi-trillion-dollar carry position needed to find a new equilibrium, mediated through short-gamma dealer hedges. The same template -- crowded carry, weekend trigger, Monday unwind -- is repeatable.
2. **VIX is a microstructural index.** A 65 print does not mean realized vol of 65; it means the SPX option strip was unhealthy. Traders who acted on the headline VIX print (e.g. selling premium "into the spike") often got better fills in the futures than in the cash options. Always consult the VIX-futures curve in a shock.
3. **The synthesis still works.** The [[long-vol-overlay]] thesis was empirically reconfirmed. Books with overlays were positioned to act as buyers of risk on Aug 6-7; books without overlays were forced sellers.
4. **0-DTE concentration is a new fragility.** The growth of zero-dated options between 2022 and 2024 made dealer short-gamma hedging more concentrated and more reflexive. This is a structural amplifier that did not exist in [[volmageddon|2018]].
5. **Speed compresses the trade.** The full peak-trough cycle in SPX was three weeks; the violent leg was 12 hours. Any strategy whose [[kill-criteria]] depend on a multi-day drawdown signal will not engage in time. Risk processes need intra-session triggers.

## Related

- [[long-vol-vs-short-vol]] -- the framework page that anchors this event
- [[volmageddon]] -- the 2018 ETP-driven precedent
- [[covid-crash]] -- the larger, slower 2020 shock
- [[gfc]] -- the deep-cycle 2008 reference
- [[yen-carry-trade]] -- the macro positioning unwound here
- [[bank-of-japan]] -- the policy authority whose hike triggered the unwind
- [[carry-trade]] -- the broader concept
- [[zero-dte-options]] -- the dealer-gamma amplifier
- [[vix-futures]], [[vix-term-structure]] -- the curve dynamics
- [[short-strangle]] -- the structure most damaged among retail
- [[iron-condor]] -- the defined-risk alternative that fared better
- [[long-vol-overlay]] -- the structural lesson
- [[universa-investments]] -- the canonical long-vol survivor
- [[volatility-regime-classification]] -- "Crisis" regime print

## Sources

- *Bloomberg*, "VIX Soars to Pandemic-Era Levels in 'Volmageddon 2.0'," Aug 5-7 2024 coverage of the spike, the JPY unwind, and the BoJ aftermath.
- *Wall Street Journal*, "Why the Stock-Market Selloff Was So Sudden and So Violent," Aug 6 2024 explanatory piece on the carry unwind and dealer short-gamma feedback.
- *Financial Times*, "Yen Carry Trade Unravels," Aug 5-9 2024 -- BIS data on JPY-funded carry exposure and the cross-asset feedback.
- CBOE post-event commentary on VIX index calculation in the Aug 5 session and subsequent proposals to amend the inclusion criteria for the SPX option strip.
- BoJ press conferences, July 31 2024 (Ueda) and Aug 7 2024 (Uchida walk-back) -- primary record of the policy signals.
- Sell-side derivatives research from Nomura (Charlie McElligott), Goldman Sachs, and JPMorgan dated Aug 5-9 2024 on dealer gamma positioning and 0-DTE concentration.
- US Bureau of Labor Statistics, July 2024 Employment Situation (released Aug 2 2024) -- the payrolls trigger.

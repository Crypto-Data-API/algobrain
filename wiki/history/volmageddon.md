---
title: "Volmageddon (February 2018)"
type: news
created: 2026-05-07
updated: 2026-06-12
status: good
tags: [volatility, history, options, vix, short-vol-blowup, etp]
aliases: ["Volmageddon", "Vol-mageddon", "XIV blow-up", "Feb 5 2018 vol shock", "volmageddon-2018", "Volpocalypse", "VIX Flash Crash 2018", "XIV Termination"]
event_date: 2018-02-05
markets_affected: [stocks, options, etp]
impact: high
verified: true
sources_count: 6
related: ["[[long-vol-vs-short-vol]]", "[[xiv-velocity-shares]]", "[[ljm-preservation-and-growth]]", "[[variance-risk-premium]]", "[[short-strangle]]", "[[vix-futures]]", "[[vix-term-structure]]", "[[contango]]", "[[vix-august-2024-spike]]", "[[covid-crash]]", "[[universa-investments]]", "[[mark-spitznagel]]", "[[tail-risk-hedging]]", "[[volatility-regime-classification]]", "[[gamma]]", "[[vega]]"]
---

Volmageddon refers to the short-volatility blow-up of **February 5-6, 2018**, when the [[vix-futures|VIX futures]] complex repriced violently, the inverse-VIX ETP [[xiv-velocity-shares|XIV (VelocityShares Daily Inverse VIX Short-Term ETN)]] lost roughly 96% of its value in a single after-hours session, and a generation of short-vol funds and retail premium-sellers were liquidated. It is the canonical case study in how a structurally short-[[vega]], structurally short-[[gamma]] product behaves when implied volatility doubles intraday, and the proximate reason most surviving short-vol playbooks now insist on an explicit [[long-vol-overlay|long-vol overlay]]. See [[long-vol-vs-short-vol]] for how the event fits into the broader vol-book taxonomy.

## Overview

Through 2017, the [[xiv-velocity-shares|XIV]] ETN, ProShares' SVXY ETF, and a long tail of short-VIX-futures hedge fund mandates had become one of the most crowded trades in markets. AUM in inverse and short-VIX-linked products had grown to roughly $3-4 billion by January 2018. The strategy worked beautifully because the [[vix-futures|VIX futures curve]] was in persistent [[contango]] -- front-month futures were systematically priced higher than spot VIX -- so short-VIX-futures positions earned a daily roll yield as those futures decayed toward a stable low spot. From its 2010 inception through January 2018, XIV had returned roughly 1,800%. CBOE's spot VIX index spent most of 2017 below 12, registering its lowest annual mean in the index's history.

The trade was structurally short [[vega]]: a doubling of implied vol implied an enormous loss. That risk was widely acknowledged but discounted on the assumption that vol would not double overnight. On Feb 5, 2018 it did.

## What Happened

**Friday, Feb 2, 2018.** A stronger-than-expected US wage-growth print in the January employment report sparked a bond-yield spike. SPX fell ~2.1%, VIX closed at ~17.3. Mechanical rebalancing logic in the inverse and leveraged VIX-futures ETPs implied that the products would need to **buy** large quantities of front-month VIX futures into the close to hold their inverse exposure as vol rose -- a known but underappreciated reflexivity.

**Monday, Feb 5, 2018.**
- SPX fell ~4.1% on the day, including a ~700-point Dow drop in the final hour.
- Spot VIX printed an intraday high near 50 from a Friday close of 17.3 -- a rise of nearly 200% in a session and the largest single-day percentage move in VIX up to that date.
- Front-month VIX futures, the actual instrument the ETPs tracked, gapped sharply higher into the 4:00pm cash close and continued to climb in the post-close VIX-futures session.
- ETP rebalancing into the close (the ~4:15pm "VWAP window" for the daily reset) added forced-buying pressure on already-spiking VIX futures.

**After the close, Feb 5.** Indicative net asset values for inverse-VIX ETPs collapsed. XIV's indicative value fell from ~$108 at the prior close to roughly $4-5, a ~96% loss. SVXY, structured as a 1x inverse ETF, fell roughly 90% on an indicative basis.

**Tuesday, Feb 6, 2018.** Credit Suisse, the issuer of the XIV ETN, announced that an "Acceleration Event" had been triggered (the prospectus permitted termination if the indicative value fell more than 80% in a day). Credit Suisse exercised its early-redemption right; XIV ceased trading on Feb 15 and was redeemed at its Feb 15 indicative value (~$5.99). ProShares modified SVXY's leverage from -1.0x to -0.5x in late February to reduce gap risk. Several short-vol mutual funds and hedge funds with similar exposure announced large losses.

**Friday, Feb 9, 2018.** SPX bottomed for the move ~10.2% below the Jan 26 high. VIX closed at ~29 on Feb 9 after touching 50 on Feb 6 intraday. The shock was over in roughly four sessions but wiped out years of short-vol P&L.

## Mechanism / Why It Happened

Three forces compounded:

1. **Crowded short-vol positioning.** Inverse and short-VIX ETPs collectively held a structurally large short position in front-month VIX futures. Multiple research notes (Macro Risk Advisors, Pravit Chintawongvanich; Goldman Sachs derivatives strategy) had warned through 2017 that the rebalancing demand from these products on a vol shock was geometrically larger than the dollar AUM suggested.

2. **Reflexive ETP rebalancing.** Inverse ETPs maintain constant daily inverse exposure. When VIX futures rise, the products' short exposure mechanically grows in absolute terms, requiring them to **buy** more VIX futures to restore the target leverage. This buying happens in a narrow window before the cash close. On Feb 5, the size of that buying was estimated by sell-side desks at $200-300M of VIX-futures vega -- an amount the front-month book could not absorb without a large repricing.

3. **Path-dependent, non-linear payoffs.** The inverse-VIX product is short [[gamma]] in vol: the loss accelerates as vol rises. A move from VIX 12 to 17 was painful but survivable for the ETPs; a move from 17 to 38 (the Feb 5 close in spot VIX) was catastrophic because the loss curvature compounds.

The triggering macro event -- a payrolls-driven rates shock -- was modest by historical standards. The event was a microstructural unwind, not a fundamental crash. SPX fell roughly 10% peak-to-trough; VIX behaved as if SPX had fallen 25%+. That decoupling is the signature of an ETP-driven vol shock and is a key reason it recurred in [[vix-august-2024-spike|August 2024]] in different clothes.

## Casualties / Survivors

**Casualties.**
- **[[xiv-velocity-shares|XIV (VelocityShares Daily Inverse VIX Short-Term ETN)]]** -- terminated by Credit Suisse on Feb 15, 2018. Roughly $1.6B of investor capital was effectively wiped out.
- **[[ljm-preservation-and-growth]]** -- a short-strangle mutual fund managed by LJM Funds Management that lost approximately 80% in two trading days (Feb 5-6) and was wound down. Investors filed claims that risk disclosures had understated the strategy's tail exposure.
- **VelocityShares Daily 2x VIX Short-Term ETN (TVIX)** survived but its mirror -- the daily 2x inverse, ZIV/SVXY-class products -- was either terminated or had its leverage reduced.
- A long tail of retail short-strangle accounts: Forums and broker filings recorded numerous accounts that lost 50-100% of equity. Several lawsuits against options-selling educational programs followed.
- Discretionary short-vol hedge funds with smaller AUM: Catalyst-style and "income enhancement" sleeves at multi-strategy funds reported P&L drops of 20-40% for the week.

**Survivors and beneficiaries.**
- **[[universa-investments]]** -- [[mark-spitznagel]]'s long-vol fund, which is structurally long deep-OTM SPX puts, monetized a portion of the move although Feb 2018 was small in magnitude versus their banner 2008 and March 2020 events.
- **Long-vol overlay sleeves** at multi-strategy funds with explicit tail hedges turned what would have been a 25-40% short-vol drawdown into a 5-15% net drawdown.
- **VIX market-makers** with positive-gamma books and access to inventory benefitted from the explosion in bid-ask spreads in VIX options and futures.

## Impact on Vol Books

Volmageddon is the cleanest empirical illustration of the asymmetry described in [[long-vol-vs-short-vol]]:

- **Naked short vol** -- represented by XIV, LJM, and unhedged short-strangle accounts -- suffered the maximum bound of the negative-skew distribution. Five years of theta capture were erased in two sessions. For XIV holders, the loss was **terminal**: there was no path back even if vol normalized, because the product itself was redeemed at the trough.
- **Short vol with long-vol overlay** -- the institutional configuration -- absorbed the shock. The overlay's [[vega]] gain (front-month VIX calls trebled in price; 25-delta SPX puts went up 5-10x) covered the bulk of the strangle loss. Books survived to continue compounding.
- **Pure long vol** -- Universa-style portfolios -- monetized but the move was small enough that the multi-year IRR contribution was modest. The textbook lesson is that long-vol books make most of their decade in a few sessions; Feb 2018 was a session, not the session.

The post-event regulatory and product response materially reshaped the short-vol landscape. CBOE adjusted VIX-derivative settlement procedures; ProShares cut SVXY leverage; the inverse-VIX ETP cohort never fully recovered AUM. The short-vol trade migrated from levered ETPs into option strategies with bounded losses ([[iron-condor|iron condors]], defined-risk credit spreads, [[put-write-index|put-write indices]]) -- a structural improvement, but one that preserved the underlying [[variance-risk-premium]] harvest while removing the catastrophic gap-risk leg. See [[options-portfolio-construction]].

## Lessons / Takeaways

1. **Short [[vega]] is path-dependent.** A short-vol position's loss is not linear in vol; it is convex in the wrong direction. Backtests that compute end-of-day P&L on a straight-line-vol move underestimate intraday gap risk by an order of magnitude.
2. **Crowded products distort their own underlyings.** When ETP rebalancing demand is large versus the underlying contract's open interest, the ETP becomes the marginal price-setter in a stress event. This is the same mechanism at work in the [[lme-nickel-squeeze-2022|2022 LME nickel squeeze]] and the Aug 2024 VIX spike.
3. **Termination clauses convert paper losses into permanent losses.** XIV was structurally unable to recover because the product itself was redeemed at the trough. Short-vol exposures should be held in instruments without forced-redemption triggers if the strategy depends on mean reversion.
4. **The [[variance-risk-premium]] is real but lumpy.** Five clean years of theta were earned in 2013-2017 and then halved in two sessions. An honest Sharpe must be calculated over a full cycle, not a calm sub-sample. See [[deflated-sharpe-ratio]] and [[ergodicity]].
5. **The synthesis works.** Books with explicit long-vol overlays survived. Books without them did not. There is no defensible reason to run scale short vol without an overlay, and Volmageddon is the first piece of evidence on that point.

## Related

- [[long-vol-vs-short-vol]] -- the comparison framework into which this event slots
- [[xiv-velocity-shares]] -- the ETN at the center of the blow-up
- [[ljm-preservation-and-growth]] -- the canonical short-vol fund casualty
- [[vix-august-2024-spike]] -- the next ETP/positioning-driven vol shock
- [[covid-crash]] -- a much larger but slower-developing vol shock
- [[universa-investments]] -- the canonical long-vol survivor
- [[variance-risk-premium]] -- the structural premium short-vol books harvest
- [[vix-futures]] -- the underlying instruments
- [[contango]] -- the curve shape that funded the pre-2018 short-vol trade
- [[vix-term-structure]] -- the curve dynamics that broke
- [[short-strangle]], [[iron-condor]] -- the option structures that replaced ETP-based short vol
- [[long-vol-overlay]] -- the structural lesson institutionalised after 2018
- [[volatility-regime-classification]] -- the regime taxonomy in which Feb 2018 was a "Crisis" regime print

## Sources

- Credit Suisse press release, Feb 6 2018: announcement of XIV "Acceleration Event" and early-redemption notice.
- *Wall Street Journal*, "How a Hot Trade Turned to Disaster," Feb 6-9 2018 coverage of the XIV termination and ETP unwind.
- *Bloomberg*, "Inverse VIX ETN Wipeout Stuns Investors," Feb 6 2018 and follow-on reporting.
- ProShares press release, Feb 27 2018: announcement of SVXY leverage change from -1x to -0.5x.
- LJM Funds Management investor letters, Feb-Mar 2018, documenting the LJM Preservation & Growth Fund losses.
- Macro Risk Advisors and Goldman Sachs derivatives research notes, 2017-2018, on inverse-VIX ETP rebalancing demand.
- Spitznagel, Mark. *Safe Haven: Investing for Financial Storms* (2021) -- discussion of short-vol fragility and the survivor-bias problem.

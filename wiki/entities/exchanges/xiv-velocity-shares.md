---
title: "XIV — VelocityShares Daily Inverse VIX Short-Term ETN"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [volatility, history, derivatives, futures]
aliases: ["XIV", "VelocityShares Daily Inverse VIX Short-Term ETN", "VelocityShares XIV", "Inverse VIX ETN"]
entity_type: company
founded: 2010
headquarters: "Zurich, Switzerland (issuer: Credit Suisse AG)"
website: ""
related: ["[[volmageddon]]", "[[vix]]", "[[vix-futures]]", "[[short-volatility-strategies]]", "[[long-vol-vs-short-vol]]", "[[ljm-preservation-and-growth]]", "[[malachite-capital]]", "[[catalyst-hedged-futures]]", "[[svxy]]", "[[svxy-proshares]]", "[[exchange-traded-note]]", "[[acceleration-event]]", "[[contango]]", "[[backwardation]]", "[[vix-term-structure]]", "[[universa-investments]]", "[[failure-modes]]", "[[gap-risk]]"]
---

XIV was the ticker for the **VelocityShares Daily Inverse VIX Short-Term ETN**, an exchange-traded note issued by **Credit Suisse AG** in November 2010 that provided **-1x daily exposure** to the **S&P 500 VIX Short-Term Futures Index** (SPVXSP). For most of 2012-2017 the product compounded one of the highest realized [[sharpe-ratio|Sharpe ratios]] of any retail-accessible vehicle in the world, becoming a beloved short-vol trade for retail and institutional investors alike. On **February 5, 2018** ([[volmageddon|Volmageddon]]) XIV's [[indicative-value]] fell roughly **-96% in after-hours trading** as VIX futures repriced violently into a backwardated curve. Credit Suisse exercised the **acceleration event** clause in the prospectus and **terminated the note on February 21, 2018**, redeeming holders at the diminished cash value. XIV is the most widely cited single instrument in the history of short-volatility blow-ups.

## Overview

XIV was structured as an [[exchange-traded-note|exchange-traded note]] (a senior, unsubordinated, unsecured debt obligation of Credit Suisse), tracking the inverse daily performance of the S&P 500 VIX Short-Term Futures Index. The index itself rolls a long position in front- and second-month [[vix-futures|VIX futures]] to maintain a constant 30-day weighted maturity. Because the VIX futures curve is **in [[contango]]** the majority of the time, a short position in the index produces structural roll yield -- which translated into a steady upward drift in XIV during normal markets. Combined with the equity bull market and very low realized vol of 2012-2017, XIV's price compounded from $10 at inception to over **$140** by January 2018.

The ETN was distributed by Janus Capital's VelocityShares unit and listed on Nasdaq.

## Mechanics

- **Issuer**: Credit Suisse AG (Nassau Branch).
- **Structure**: Senior unsecured ETN -- holders had credit exposure to Credit Suisse and tracking exposure to the underlying index, but no claim on the underlying VIX futures themselves.
- **Underlying index**: S&P 500 VIX Short-Term Futures Index (SPVXSP), which tracks a constant-30-day-maturity long position in front-month and second-month VIX futures.
- **Daily exposure**: -1x the daily percentage change in the index (so a +10% day in the index = approximately -10% in XIV's indicative value).
- **Daily rebalance**: Like all daily-leveraged ETPs, XIV rebalanced its notional exposure each day to maintain -1x. This rebalance is the source of the **path-dependence problem** -- compounding -1x daily over volatile periods drifts away from -1x of the cumulative index move.
- **Acceleration event**: The prospectus included an issuer call ("acceleration event") that would trigger if the indicative value fell **80% or more from the previous day's close** (or equivalently if the daily move in the underlying index exceeded ~80% in the wrong direction for XIV). The acceleration provision effectively put a hard floor of zero on Credit Suisse's tail liability.

## Track Record

- **November 2010 inception**: Initial value $10.
- **2012-2017**: Compounded steadily as VIX stayed low, the VIX futures curve stayed in contango, and the equity bull market continued. Multi-year drawdowns were modest.
- **2017**: Among the best-performing tradable instruments in the world; final 2017 close near $140, an **annualized return well above 50%** since inception, with reported [[sharpe-ratio]] above 2 in-sample.
- **January 2018**: Continued upward drift, peaking around $145.
- **February 5, 2018**: Catastrophic loss (see below).
- **February 21, 2018**: Redeemed at the cash value following the acceleration event.

The ETN's final-five-years return profile was the textbook example of [[sharpe-ratio-pitfalls|Sharpe ratio pitfalls]] for [[negative-skew]] strategies: a beautiful in-sample track record that contained no information about the strategy's behavior in a tail event.

## Blow-Up: February 5, 2018 (Volmageddon)

The mechanics of the failure on Feb 5, 2018:

1. **Late-day equity selloff**: The S&P 500 fell ~4.1% during the U.S. session, accelerating into the close. VIX rose from ~17 to the high 20s during regular trading hours.
2. **VIX futures rebalance pressure**: The S&P 500 VIX Short-Term Futures Index closed up sharply on the day. XIV's published indicative value fell substantially in regular hours but had not yet hit the acceleration threshold.
3. **After-hours surge**: VIX futures traded in extended hours, and the index closing-mechanism math, combined with end-of-day rebalance flows from XIV and similar products, produced a violent move in front-month VIX futures. The S&P 500 VIX Short-Term Futures Index gained approximately **+96% on the day**, meaning -1x daily exposure produced an indicative value loss of **roughly -96%**.
4. **Acceleration event triggered**: The indicative value fell more than 80% from the prior day's close. Credit Suisse announced the acceleration event the following morning (February 6, 2018).
5. **Termination on Feb 21, 2018**: Credit Suisse paid holders the cash equivalent of the acceleration-date indicative value -- approximately **$5.99** per ETN (verified via Perplexity, 2026-06-10; some early reports cited ~$5.30 from the interim indicative value), versus a February 5 regular-session close of **$99.00** and a mid-January 2018 all-time high near **$146**. Total holder losses across the cohort were estimated at **$1.5-2 billion**.

The reflexive flows from XIV and SVXY rebalance hedging on the day are widely cited as having amplified the VIX-futures move itself -- a textbook **reflexivity / liquidity-cascade** dynamic. Industry analyses and subsequent SEC and academic studies argued the products' aggregate end-of-day rebalance flows had grown large relative to the liquidity of front-month VIX futures, making a self-reinforcing feedback loop possible once a sufficient initial move occurred.

## Why It Matters / Lessons

1. **Short-VIX-futures ETNs were always going to fail in a sufficiently large vol shock.** Daily -1x compounding plus contango drift produces a slow-grinding-up price path with mathematically unbounded one-day downside risk. Holding XIV was a position whose maximum loss was 100% on any single day and whose distribution of one-day moves had a fat left tail. A 96% loss is catastrophic but not theoretically surprising.
2. **The acceleration event clause was a feature, not a bug.** From Credit Suisse's perspective, the clause prevented a negative indicative value (and corresponding issuer liability beyond zero). From the holder's perspective, the clause guaranteed a permanent loss-of-capital outcome rather than an opportunity to recover when vol normalized.
3. **Reflexivity in inverse-vol products.** The aggregate AUM of XIV and similar products had become large enough that their end-of-day rebalance flows contributed to the magnitude of the move that destroyed them. This is the **"the trade got too big"** problem.
4. **Sharpe is meaningless for [[negative-skew]] daily-leveraged products.** XIV's seven-year in-sample Sharpe was over 2. Its terminal payoff was -96% in a single session. Sharpe assumes [[gaussian-assumption|Gaussian]] returns; daily-leveraged inverse-vol ETNs do not have Gaussian returns. See [[sharpe-ratio-pitfalls]].
5. **The product is a lesson, not a one-off.** SVXY (the ProShares short-VIX ETF) survived Volmageddon only by switching to **-0.5x daily exposure** afterward -- an explicit acknowledgment that the original -1x design was structurally incompatible with surviving large vol shocks. That structural rewrite is the practical regulatory consensus.
6. **Same family as [[ljm-preservation-and-growth|LJM]], [[malachite-capital|Malachite]], [[catalyst-hedged-futures|Catalyst]].** Different wrapper, same core risk: net short premium, net short vega, net short gamma, with insufficient long-vol overlay. The wrapper just controls how the loss is distributed (retail vs. institutional, ETN vs. mutual fund vs. hedge fund).

## Key People (Issuer / Sponsor)

- **Credit Suisse AG** -- Note issuer. The bank exercised the acceleration event and terminated the note. Credit Suisse exited the U.S. ETN business shortly after the event.
- **VelocityShares (Janus Capital)** -- Sponsor / branding entity. The VelocityShares brand was acquired and rebranded over subsequent years; the short-vol family of products did not return in -1x form.
- **S&P Dow Jones Indices** -- Calculation agent for the S&P 500 VIX Short-Term Futures Index.

## Related

- [[volmageddon]] -- the event
- [[vix]] -- the underlying index family
- [[vix-futures]] -- the actual instruments referenced
- [[vix-term-structure]] -- the mechanism behind contango drift
- [[contango]] -- the structural roll yield XIV harvested in calm regimes
- [[backwardation]] -- the regime that destroyed it
- [[short-volatility-strategies]] -- the strategy archetype
- [[long-vol-vs-short-vol]] -- comparison and synthesis page
- [[ljm-preservation-and-growth]] -- the matching mutual-fund failure
- [[malachite-capital]] -- the matching hedge-fund failure two years later
- [[catalyst-hedged-futures]] -- the matching short-call mutual-fund failure
- [[svxy-proshares]] -- the surviving (and rewritten) short-VIX ETF
- [[exchange-traded-note]] -- the wrapper type
- [[acceleration-event]] -- the prospectus clause that ended the product
- [[universa-investments]] -- the structural opposite
- [[failure-modes]] -- failure-mode taxonomy
- [[gap-risk]] -- the core risk
- [[sharpe-ratio-pitfalls]] -- why the in-sample Sharpe was misleading
- [[negative-skew]] -- the return profile

## Sources

- VelocityShares Daily Inverse VIX Short-Term ETN prospectus, Credit Suisse AG (2010 and amendments through 2018).
- Credit Suisse press release, "Credit Suisse Announces Event Acceleration of XIV ETNs" (February 6, 2018).
- *Wall Street Journal*, "How a Once-Hot Investment Was Wiped Out in Hours" (February 6, 2018).
- *Bloomberg*, "VelocityShares XIV Will Be Liquidated After Volatility Surge" (February 6, 2018) and follow-on coverage.
- *Financial Times*, post-Volmageddon analyses (February-March 2018).
- Augustin, P., Cheng, I.-H., and Van den Bergen, L., academic working papers and journal articles on the February 2018 VIX-futures cascade and inverse-VIX-ETP liquidity dynamics.
- S&P Dow Jones Indices methodology document, S&P 500 VIX Short-Term Futures Index.
- ProShares SVXY prospectus amendments (March 2018) documenting the change from -1x to -0.5x daily exposure.
- [[long-vol-vs-short-vol]] -- internal synthesis on the broader cohort of short-vol failures.
- Redemption value ($5.99/note) and deal facts verified via Perplexity (sonar), 2026-06-10.

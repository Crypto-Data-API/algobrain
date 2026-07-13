---
title: "Long-Term Capital Management (1994-1998 Collapse)"
type: news
created: 2026-05-07
updated: 2026-06-12
status: good
tags: [history, hedge-fund, ltcm, relative-value, fixed-income-arbitrage, leverage, vol, russia-crisis, 1998]
aliases: ["LTCM", "Long-Term Capital Management", "LTCM Collapse", "1998 LTCM Crisis", "LTCM Collapse 1998", "Ltcm Collapse 1998"]
event_date: 1998-09-23
markets_affected: [stocks, options, credit, fixed-income, treasuries, swaps, mortgage]
impact: high
verified: true
sources_count: 7
related: ["[[long-vol-vs-short-vol]]", "[[gfc]]", "[[volmageddon]]", "[[covid-crash]]", "[[black-monday]]", "[[vix-august-2024-spike]]", "[[universa-investments]]", "[[mark-spitznagel]]", "[[nassim-taleb]]", "[[tail-risk-hedging]]", "[[john-meriwether]]", "[[myron-scholes]]", "[[robert-merton]]", "[[salomon-brothers]]", "[[federal-reserve]]", "[[relative-value-arbitrage]]", "[[fixed-income-arbitrage]]", "[[swap-spread-trade]]", "[[on-the-run-vs-off-the-run]]", "[[variance-risk-premium]]", "[[long-vol-overlay]]", "[[volatility-regime-classification]]", "[[ergodicity]]"]
---

Long-Term Capital Management (LTCM) was the most prestigious relative-value hedge fund of its era, founded in 1994 by John Meriwether (former head of bond arbitrage at Salomon Brothers) with Nobel laureates Myron Scholes and Robert Merton on its strategy committee. From inception to early 1998, the fund returned 20-40% net per year on equity capital, growing from $1.25B AUM at launch to roughly $4.7B at peak. In **August-September 1998**, following Russia's default on August 17 and the resulting global flight-to-quality, LTCM's relative-value spreads widened against it across multiple markets simultaneously; the fund lost approximately **$4.6B in the four weeks from late August to mid-September**, leaving roughly $400M of equity supporting $125B of balance-sheet positions and ~$1.25 trillion of off-balance-sheet derivatives notional. On **September 23 1998**, the Federal Reserve Bank of New York coordinated a $3.625B private-sector recapitalisation by 14 major banks. LTCM was wound down by 2000. The episode is the canonical pre-GFC example of a relative-value short-vol blow-up at scale and a recurring reference event in the [[long-vol-vs-short-vol]] literature.

## Overview

LTCM's strategy was textbook **relative-value arbitrage**: identify pairs of securities whose prices should converge by some economic logic (e.g., on-the-run vs. off-the-run Treasuries, swap-rate vs. Treasury-yield spreads, dual-listed equity discounts), put on the converging trade with substantial leverage to amplify the small per-unit spread, and let convergence deliver the return. The fund's edge was a combination of: (i) rigorous quantitative pricing from Scholes/Merton-trained academic talent; (ii) extraordinary balance-sheet leverage made available by Wall Street counterparties on the basis of the fund's reputation; and (iii) a pioneering willingness to put on positions across asset classes -- swaps, mortgage securities, sovereign debt, equity volatility, and merger-arbitrage spreads -- in a single integrated book.

The strategy was, in vol-book language, **structurally short relative-value volatility**: each individual trade was small and convergent in normal markets but profoundly negative-skew in stress, when correlations rose to 1.0 and "diverging spreads" became "all spreads diverging together." LTCM ran roughly 25-30:1 balance-sheet leverage at end-1997, rising to 50:1+ on a notional basis in mid-1998 as equity declined.

## What Happened

**1994-1997.** Net returns of 20% (1994), 43% (1995), 41% (1996), 17% (1997) on equity. Capital grew to ~$7B; the fund returned $2.7B to investors at end-1997 to keep the ratio of opportunities-to-capital tight. Year-end 1997 equity ~$4.7B.

**Q1-Q2 1998.** Modest early-year losses on swap-spread and bond-spread positions (-1% to -3% per month). Spreads were tight; the marginal trade profitability had compressed. Several risk-arbitrage and equity-vol positions were added.

**Monday, August 17 1998.** **Russia defaults on its rouble-denominated debt** and devalues the rouble. Global flight-to-quality begins immediately. Investors dump emerging-market debt, peripheral sovereigns, swap-rate-paying positions, and corporate credit, and rush into US Treasuries and German Bunds. **Every leg of LTCM's relative-value book is on the wrong side** of this flow:

- Long off-the-run Treasuries / short on-the-run Treasuries: the spread widens (on-the-runs become hyper-bid).
- Long swap rates / short Treasury rates (i.e., paid-fixed in swaps vs. long Treasuries): swap-Treasury spreads blow out as funding stress widens.
- Long emerging-market sovereign debt / short G7 hedges: the long leg craters.
- Short equity vol via index variance: realized vol explodes; variance-swap mark-to-market collapses.
- Long takeover-target equities / short acquirer in merger-arb: merger spreads widen on funding stress.

**August 21 1998.** LTCM loses $553M on a single day -- the worst session in the fund's history. Equity falls below $4B.

**Late August 1998.** Equity at $2.9B by August 31. Leverage is rising toward 50:1 as balance-sheet positions cannot be reduced without cratering prices further. Counterparties begin asking for additional margin.

**September 1-21 1998.**
- LTCM's losses continue at ~$200-500M per day.
- The fund tries to raise emergency capital from Warren Buffett (Berkshire), Goldman Sachs, and others. Buffett offers $250M for the entire book in late September; the offer is conditional and lapses.
- Equity falls to roughly $400M by September 22. Total balance-sheet positions still ~$125B; off-balance-sheet derivatives notional still in the $1T+ range. Leverage ratio is mathematically meaningless -- the fund is effectively insolvent if marked at fire-sale prices.

**Wednesday, September 23 1998.** Federal Reserve Bank of New York president William J. McDonough convenes 14 major banks at the FRBNY building in Manhattan. The banks collectively contribute **$3.625B** in fresh capital in exchange for 90% of LTCM's equity. The original partners are diluted; Meriwether and the other partners retain a small stake and continue to manage the wind-down. **The Fed itself does not provide capital** -- this is a private-sector rescue with public-sector convening.

**Late 1998.** Markets stabilise after the Fed cuts rates 25bp on September 29 and 50bp inter-meeting on October 15. LTCM's positions slowly unwind through 1999-2000. Returns of capital to the new owners are modest; the original LTCM partnership returns roughly **-92%** from peak equity to wind-down.

**2000.** The fund is fully liquidated. Meriwether founds JWM Associates the same year (which would itself eventually wind down in 2009 after GFC-era losses).

## Mechanism / Why It Happened

Three layered drivers, each of which has recurred in subsequent vol shocks:

1. **Correlation went to 1.0 in stress.** LTCM's risk model treated the fund's many positions as roughly independent -- the diversification benefit produced low aggregate volatility on the book. In the post-Russia flight-to-quality, every relative-value spread moved adversely *together*. The diversification benefit collapsed precisely when needed. This is the canonical demonstration of the **"correlation in the tail"** failure of pre-1998 risk models. Post-LTCM, "stress correlations" rather than "normal correlations" became standard input to bank and hedge-fund VaR.
2. **Leverage at scale invited reflexive selling.** LTCM's positions were large enough relative to the markets they traded that the *anticipation* of LTCM unwinding became a trade in itself. Several Wall Street trading desks began putting on the opposite side of LTCM's known positions in late August, accelerating the move against the fund. The same reflexive amplification has recurred in [[volmageddon|2018]] (inverse-VIX rebalancing visible to the Street) and [[archegos-blowup-2021|Archegos 2021]] (concentrated single-stock positions visible to prime brokers).
3. **Negative-skew strategies have non-Gaussian tails.** LTCM's monthly P&L through 1994-1997 looked like a 4+ Sharpe strategy: positive 95% of months, modest drawdowns. The 1998 path was a single-tail event on a strategy whose "Sharpe" was structurally meaningless because the underlying P&L distribution had a fat negative tail. **The Sharpe ratio was lying because the strategy was [[long-vol-vs-short-vol|short vol in disguise]].** This is the foundational point [[nassim-taleb]] made in *Dynamic Hedging* (1997) and elaborated in *Fooled by Randomness* (2001) using LTCM as a recurring example.

The Russia default itself was the **trigger**, not the underlying cause. The underlying cause was a portfolio whose true risk was orders of magnitude larger than its historical volatility implied, leveraged at scale into instruments that became illiquid in stress.

## Casualties / Survivors

**Casualties.**
- **LTCM partners.** Meriwether, Scholes, Merton, Larry Hilibrand, Eric Rosenfeld and other principals lost the bulk of their personal capital invested in the fund. Several had taken out personal loans collateralised by their LTCM stakes; those loans were called.
- **LTCM external limited partners.** The pre-rescue equity (~$400M) was diluted to roughly 10% of post-rescue equity; original investors received only modest distributions in the eventual wind-down.
- **Bear Stearns** -- although not a member of the rescue consortium, suffered from being LTCM's prime broker and from having seen the gross positions. Bear Stearns' refusal to participate in the rescue was a recurring source of friction with peer firms; some commentators link Bear's eventual 2008 isolation to its 1998 behaviour.
- **Several other relative-value hedge funds** (e.g., Convergence Asset Management, MKP Capital's predecessor strategies) suffered correlated losses in August-September 1998 and were wound down or restructured.
- **Russian sovereign creditors** more broadly: the default itself wiped out a generation of Russian bank exposure and led to sustained capital flight.

**Survivors and beneficiaries.**
- **The 14 rescuing banks** -- ultimately broke even or made small profits on the rescue capital, since the underlying LTCM positions slowly converged in 1999-2000 once panic faded.
- **[[universa-investments|Universa]] did not yet exist** (founded 2007). However, **[[nassim-taleb]]** -- then a partner at Empirica Capital, an early long-vol hedge fund -- has cited the 1998 event as a foundational data-point for his thesis on the inadequacy of Gaussian risk models. *Fooled by Randomness* (2001) and the subsequent Black Swan literature traces from 1998 (and 1987).
- **Long-vol option-buyers** generally: SPX VIX rose from ~17 in early August 1998 to ~46 in early October. OTM SPX puts and VIX calls (when they existed) appreciated substantially.
- **Warren Buffett / Berkshire Hathaway** -- although his bid for the LTCM book was not accepted, his 1998 letter and subsequent commentary used the LTCM episode as the canonical illustration of why Berkshire avoids derivatives leverage. He has revisited the example repeatedly over decades.

## Impact on Vol Books

LTCM is a slightly different shape of vol shock than the others on this comparison list, but the structural lesson is identical to [[long-vol-vs-short-vol]]:

- **LTCM was a short-vol book in disguise.** It did not look like the [[short-strangle]] writing of [[volmageddon|2018]] or [[vix-august-2024-spike|2024]]; it looked like elegant, low-vol, multi-asset relative-value arbitrage. But the underlying P&L distribution was negative-skew with a fat left tail -- the canonical short-vol shape. The Sharpe ratio was high in calm regimes and the maximum drawdown was -92% in the one stress regime that mattered. This is exactly the [[ergodicity]] divergence between time-average and ensemble-average that recurs in every short-vol blow-up.
- **The hidden short-vol position is the universal pattern.** Many strategies that do not appear to be "short vol" are actually short vol when their P&L distribution is examined: relative-value arb, merger-arb, structured-credit warehousing, short-credit-protection, currency-carry, and various basis trades. The 1998 event surfaced this pattern in the relative-value space; subsequent events surfaced it in inverse-VIX ETPs, structured products, and 0-DTE selling.
- **Long-vol overlays were not yet institutional practice.** LTCM had no explicit overlay; the few discretionary "tail hedges" the fund used were small relative to the gross book. The post-1998 wave of long-vol-overlay adoption among multi-strategy funds began precisely from the LTCM lesson, was reinforced by [[gfc|2008]], and is now best practice (see [[long-vol-overlay]]).
- **The skew responded.** Equity options skew steepened in late 1998 and again after [[gfc|2008]], reinforcing the persistent crash-protection premium installed in [[black-monday|1987]]. LTCM is part of the cumulative empirical case that drives the structural [[variance-risk-premium]].

## Lessons / Takeaways

1. **Sharpe ratios mislead for negative-skew strategies.** LTCM's pre-1998 Sharpe was ~4. Its true risk-adjusted return, including the 1998 path, was sharply negative. This is the foundational empirical case for [[deflated-sharpe-ratio]] and the Taleb critique of mean-variance evaluation.
2. **Leverage and crowding kill convergence trades.** A trade that is right but takes 18 months to converge against you is a wrong trade if you are forced to liquidate at month 12. Position sizing must respect liquidation horizon, not just analytical horizon.
3. **The Fed will convene but not always capitalise.** The 1998 LTCM rescue was *coordinated* but not *funded* by the Fed -- the capital came from private banks. Subsequent events ([[gfc|2008]], [[covid-crash|2020]]) saw Fed funding directly, but the LTCM model -- private-sector recap orchestrated by the FRBNY -- remains a template for non-systemic but large-balance-sheet-distress events.
4. **Hidden short-vol is everywhere.** The single most important post-LTCM insight is that any strategy with a high Sharpe and a low historical drawdown should be examined for *latent* short-vol exposure. If the strategy collects a small premium for taking a small risk that occasionally compounds into a large risk, it is short vol regardless of what its branding says.
5. **The synthesis still applies.** A relative-value book with an explicit long-vol overlay sized at 5-10% of the vega budget would have lost 20-30% in 1998 instead of 92%. The institutional adoption of overlays in the years following 1998 is a direct response to this reasoning.

## Related

- [[long-vol-vs-short-vol]] -- the framework page
- [[gfc]] -- the next, larger relative-value-and-credit blow-up
- [[volmageddon]], [[vix-august-2024-spike]], [[covid-crash]] -- subsequent vol shocks
- [[black-monday]] -- the prior reference event in the modern vol-shock series
- [[archegos-blowup-2021]] -- another single-fund leverage cascade
- [[universa-investments]], [[mark-spitznagel]], [[nassim-taleb]] -- long-vol thinkers
- [[tail-risk-hedging]], [[long-vol-overlay]] -- the strategies whose institutional adoption traces from 1998
- [[john-meriwether]], [[myron-scholes]], [[robert-merton]] -- LTCM principals
- [[salomon-brothers]] -- Meriwether's prior firm
- [[federal-reserve]] -- the convening authority of the rescue
- [[relative-value-arbitrage]], [[fixed-income-arbitrage]], [[swap-spread-trade]], [[on-the-run-vs-off-the-run]], merger-arbitrage -- the strategy categories LTCM ran
- [[ergodicity]] -- why time-average and ensemble-average diverge
- [[variance-risk-premium]] -- the structural premium relevant to all negative-skew strategies
- [[volatility-regime-classification]] -- 1998 as a "Crisis" regime print

## Sources

- Lowenstein, Roger. *When Genius Failed: The Rise and Fall of Long-Term Capital Management* (2000) -- the canonical narrative history.
- Federal Reserve Bank of New York, public statements on the September 23 1998 coordinated recapitalisation.
- Edwards, Franklin R. "Hedge Funds and the Collapse of Long-Term Capital Management" (1999, *Journal of Economic Perspectives*) -- early academic post-mortem.
- Jorion, Philippe. "Risk Management Lessons from Long-Term Capital Management" (2000, *European Financial Management*) -- VaR and risk-model critique.
- Taleb, Nassim Nicholas. *Dynamic Hedging* (1997) and *Fooled by Randomness* (2001) -- pre- and post-event critique of LTCM-style negative-skew strategies.
- *Wall Street Journal* and *Bloomberg* coverage, August-September 1998.
- President's Working Group on Financial Markets, "Hedge Funds, Leverage, and the Lessons of Long-Term Capital Management" (April 1999) -- official US-government post-event report.

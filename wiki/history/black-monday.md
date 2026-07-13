---
title: "Black Monday (October 19, 1987)"
type: news
created: 2026-05-07
updated: 2026-06-12
status: good
tags: [history, crash, volatility, options, portfolio-insurance, dynamic-hedging, sp500]
aliases: ["Black Monday", "1987 Crash", "October 19 1987", "1987 Stock Market Crash", "1987-black-monday", "1987-stock-market-crash", "1987-crash", "Crash of 1987", "crash-of-1987"]
event_date: 1987-10-19
markets_affected: [stocks, options, futures, sp500, dow-jones]
impact: high
verified: true
sources_count: 6
related: ["[[long-vol-vs-short-vol]]", "[[volmageddon]]", "[[covid-crash]]", "[[gfc]]", "[[vix-august-2024-spike]]", "[[long-term-capital-management]]", "[[portfolio-insurance]]", "[[universa-investments]]", "[[mark-spitznagel]]", "[[nassim-taleb]]", "[[tail-risk-hedging]]", "[[brady-commission]]", "[[circuit-breakers]]", "[[volatility-skew]]", "[[options-pricing]]", "[[black-scholes]]", "[[long-vol-overlay]]", "[[variance-risk-premium]]"]
---

Black Monday refers to **Monday, October 19, 1987**, when the Dow Jones Industrial Average fell **-22.6% in a single session** (508 points, to 1738.74), the largest one-day percentage decline in DJIA history. The S&P 500 fell -20.5%. The crash was driven by a feedback loop between equity selling and **[[portfolio-insurance]]** -- a then-popular dynamic-hedging strategy that mechanically sold S&P 500 futures as prices fell -- and was the formative event behind modern [[tail-risk-hedging|tail-risk thinking]], the persistent post-1987 [[volatility-skew|volatility skew]] in equity options, and the establishment of **[[circuit-breakers|market-wide circuit breakers]]**. It is a recurring reference event in the [[long-vol-vs-short-vol]] literature because the 1987 episode produced asymmetric P&L outcomes that mirror those of every subsequent vol shock.

## Overview

The mid-1980s bull market had run almost without interruption from August 1982 to August 1987, with the DJIA rising from 776 to 2722, a 250%+ gain in five years. Multiple structural fragilities had built up by autumn 1987: persistent US trade and budget deficits, a weakening dollar despite the post-Plaza Accord effort, rising US Treasury yields (the 10y reached ~10.2% in early October from ~7% in January), and the rapid adoption of computer-driven **[[portfolio-insurance]]** strategies among large institutional money managers. By some estimates, $60-90B of equity assets in the US were "insured" via dynamic-hedging programs by mid-1987 -- a population large enough that its synchronous selling would dominate normal liquidity provision.

## What Happened

**Wednesday-Friday, October 14-16 1987.** A confluence of negative news -- a wider-than-expected US trade deficit, a House Ways and Means Committee proposal targeting takeover-related interest deductions, and continuing rate pressure -- drove the DJIA down 9.5% over three sessions. The Friday Oct 16 close at 2246.74 was -10.4% from the August high. Portfolio-insurance programs entered the weekend with significant accumulated, but not yet executed, sell-orders.

**Monday, October 19 1987.**
- US futures markets opened with heavy sell-side imbalance; the S&P 500 futures gapped down at the 9:30am ET cash open.
- The opening of the cash market was disorderly -- a substantial number of NYSE specialist books could not match orders for the first 30-90 minutes; many large-cap stocks did not print until 10am or later.
- **Portfolio-insurance algorithms**, mechanically calibrated to sell S&P 500 futures as prices fell to maintain a target portfolio delta, contributed an estimated $4-6B of futures sales through the day -- a scale that overwhelmed market-maker capacity.
- Index-arbitrage flow, normally a source of stabilising bid by buying futures and selling cash, was disabled mid-session by the futures-cash basis blowing out to 20-30 SPX points (vs. typical ~1 point). Arbitrageurs could not meaningfully take the other side because they could not source borrow or had hit balance-sheet limits.
- **DJIA closed at 1738.74, down 508 points, -22.6%.** S&P 500 closed at 224.84, **-20.5%**. NYSE volume was 604M shares, more than double the prior record.

**Tuesday, October 20 1987.**
- Pre-open: rumors that the NYSE would close mid-day; multiple major specialist firms appeared near insolvency.
- Federal Reserve, under chairman **Alan Greenspan** (sworn in just two months earlier), issued a one-sentence statement before the open: *"The Federal Reserve, consistent with its responsibilities as the Nation's central bank, affirmed today its readiness to serve as a source of liquidity to support the economic and financial system."* The Fed coordinated with major commercial banks to extend credit to securities firms.
- DJIA closed +5.9% (102 points) but only after a violent intraday round-trip in which it fell another ~10% from the open before recovering. Several index futures were halted intraday; the open-outcry pits in Chicago saw extreme dislocations between SPX cash, SPX futures, and the MMI (Major Market Index) future.

**Week of October 19-23 1987.** DJIA round-tripped in a wide range. By Friday Oct 23 the index had recovered to ~1950, still down ~28% from its August high.

**1987-1988 aftermath.** The DJIA bottomed in October 1987 (no major secondary low) and resumed its uptrend; the index made a new all-time high by August 1989. Despite the magnitude of the one-day move, **the 1987 crash did not become a recession-tied bear market** -- US GDP growth in 1987 was +3.5%, in 1988 +4.2%. This decoupling from the real economy is one of the defining features of the event.

## Mechanism / Why It Happened

Three structural factors compounded:

1. **[[portfolio-insurance]] reflexivity.** The strategy, developed by Hayne Leland, Mark Rubinstein, and John O'Brien at LOR (Leland O'Brien Rubinstein Associates), used dynamic delta-hedging to **synthetically replicate a long put** without paying explicit option premium. As the market fell, the model required selling an increasing number of S&P 500 futures. This was mathematically elegant in theory but assumed continuously liquid markets. When all such programs sold simultaneously into a falling tape, the assumption broke down -- the synthetic put could not be replicated faster than the cash market could repulse the order flow. The portfolio-insurance community had become large enough that its hedging demand **was** the marginal flow.

2. **Specialist and dealer balance-sheet exhaustion.** NYSE specialists were the designated liquidity providers; their inventory limits were reached early on Oct 19. With dealers stepping back, the bid-ask of large-cap stocks gapped wider; the futures-cash basis blew out 30+ SPX points; index arbitrage stopped functioning. The market became, for several hours, a one-way auction.

3. **Linked-but-disconnected markets.** The cash-equity market (NYSE), the index-futures market (CME's S&P 500 futures), and the options market (CBOE) were institutionally and operationally separate, with different opening procedures, trading halts, and clearing systems. The lack of synchronization amplified the dislocation; a halt in one venue did not halt the others.

The **[[brady-commission]]** report (January 1988), commissioned by President Reagan, formally identified portfolio-insurance-driven futures selling and the "linkage" failures across cash, futures, and options as the proximate causes. The report's recommendations led directly to the modern **[[circuit-breakers]]** (Levels 1, 2, 3) and to coordinated trading-halt procedures across NYSE, CME, and CBOE.

## Casualties / Survivors

**Casualties.**
- **Portfolio-insurance providers.** LOR and several copycat programs experienced large client losses; the strategy as marketed (synthetic put protection without premium cost) was discredited. AUM in portfolio-insurance products fell from peak ~$80-90B in mid-1987 to ~$10B within 18 months.
- **NYSE specialist firms.** Several major specialist units required emergency credit lines on October 20; at least one firm (the Spear, Leeds & Kellogg unit, among others) was reportedly within hours of insolvency before Fed-coordinated bank credit was extended.
- **Equity mutual funds.** Several large funds posted -25%+ monthly returns. Retail redemptions accelerated for months.
- **Naked short-options writers.** Short-put and short-strangle accounts in late-1987 SPX and equity options were liquidated. Options market-makers without convex inventory took severe losses.

**Survivors and beneficiaries.**
- **[[nassim-taleb]]**, then a young options trader at First Boston, has described in *Dynamic Hedging* (1997) and later interviews how a long-OTM-puts position monetized strongly on Oct 19. His subsequent body of work on fat tails and convex hedging traces directly from the crash.
- **[[mark-spitznagel]]**, who would later found [[universa-investments]] in 2007, has cited 1987 as the formative observation behind his thesis that markets systematically underprice deep tail risk.
- **Long-vol option-buyers** generally. Out-of-the-money SPX puts bought in early October 1987 -- typically priced at <$1.00 -- traded at $20-50+ on October 19. Convex payoffs of 20-50x were widely reported, although such positions were rare among institutional investors prior to 1987.
- **Paul Tudor Jones** -- famously identified an elevated crash risk in his 1986-1987 research and produced strong 1987 returns, in part by being short SPX futures into October. The *Trader* documentary (1987) records the period.

## Impact on Vol Books

Black Monday is the single most important *historical* event in the [[long-vol-vs-short-vol]] taxonomy because it is the moment **the equity-options [[volatility-skew|skew]] is born**. Pre-1987, equity options were priced approximately at-the-money via the symmetric **[[black-scholes]]** assumption, with little distinction between OTM-put and OTM-call implied vols. Post-1987, OTM SPX puts have permanently traded at materially higher implied vols than OTM SPX calls -- a structural premium for crash protection that has persisted for nearly four decades. This skew is the single largest source of the [[variance-risk-premium]] that short-vol books harvest and the single largest cost long-vol books pay for tail protection.

- **Naked short-vol books** in 1987 were largely uncategorised; the discipline of "short vol" did not yet have its modern vocabulary. But short option-writing accounts and naked-put-writing programs (common in the early 1980s) were mauled. The episode predisposed the next generation of options writers to demand explicit OTM-put protection.
- **Long-vol books** as we now understand them (Universa-style, deep-OTM-put-buying with a continuous roll) post-date 1987. The strategy's intellectual origin, however, is October 19 1987 itself.
- **Portfolio insurance** was a *false* long-vol strategy: it claimed to deliver put-like payoffs without paying premium, but the dynamic hedge broke down precisely when the put was needed. The post-1987 lesson -- explicit options are not equivalent to synthetic delta-hedged options in a discontinuous market -- is foundational to [[tail-risk-hedging]].
- **The skew tax.** Long-vol overlays since 1987 must pay the persistent skew premium in OTM SPX puts. This is why the long-vol overlay, in calm regimes, runs at -1% to -3% per year of NAV: that is the price the market sets for crash protection, set by the lasting memory of 1987.

The episode is also where *[[circuit-breakers]]* and the institutional infrastructure of cross-venue trading halts originated. Modern Level 1/2/3 SPX circuit breakers, triggered four times in the [[covid-crash|March 2020 crash]], are the direct legacy of the [[brady-commission]] response to 1987.

## Lessons / Takeaways

1. **Synthetic options are not real options.** Dynamic-hedging-replicated puts assume continuous liquidity; explicit puts pay premium upfront and bear no liquidity risk. The 1987 crash settled that argument permanently in favour of explicit instruments. See [[tail-risk-hedging]].
2. **Strategy crowding becomes the strategy's trigger.** When portfolio-insurance assets exceeded the marginal liquidity of the futures market, the strategy itself created the move it was supposed to hedge. The same template recurred in [[volmageddon|February 2018]] (inverse-VIX ETPs) and [[vix-august-2024-spike|August 2024]] (yen-carry + 0-DTE dealer gamma). Crowded reflexive hedging is a recurring vol-shock catalyst.
3. **The skew is forever.** The structural OTM-put premium installed after 1987 is the single most persistent edge in equity options. Both short-vol books (collecting it) and long-vol books (paying it) build their entire architecture around this fact.
4. **Macroeconomic decoupling.** The 1987 crash was almost entirely a financial event; GDP and earnings barely flinched. Vol shocks need not coincide with recessions. Portfolio risk processes that key off recessionary indicators will miss this kind of event.
5. **Central-bank intervention works.** Greenspan's October 20 statement, plus Fed-coordinated bank credit, stopped the cascade in 24 hours. The template -- fast, broad, public liquidity backstop -- is now the standard playbook (deployed in [[gfc|2008]], [[covid-crash|2020]], and the Mar 2023 banking stress).

## Related

- [[long-vol-vs-short-vol]] -- the framework page
- [[portfolio-insurance]] -- the strategy whose feedback loop drove the cascade
- [[brady-commission]] -- the official post-event analysis
- [[circuit-breakers]] -- the institutional response
- [[volatility-skew]] -- the persistent post-1987 options-pricing feature
- [[black-scholes]] -- the pricing model insufficient for a 1987-style move
- [[universa-investments]], [[mark-spitznagel]], [[nassim-taleb]] -- the long-vol thinkers whose intellectual origin was 1987
- [[tail-risk-hedging]] -- the strategy whose existence post-dates 1987
- [[volmageddon]], [[covid-crash]], [[vix-august-2024-spike]] -- the next-generation vol shocks following the same crowding template
- [[gfc]], [[long-term-capital-management]] -- subsequent reference events
- [[variance-risk-premium]] -- the structural premium installed post-1987

## Sources

- *Report of the Presidential Task Force on Market Mechanisms* (the **Brady Report**), January 1988 -- the official US-government post-event analysis.
- *Wall Street Journal*, October 19-23 1987 daily coverage; subsequent reconstruction series.
- Federal Reserve press release, October 20 1987 -- Greenspan's "source of liquidity" statement.
- Taleb, Nassim Nicholas. *Dynamic Hedging* (1997) -- practitioner account of the 1987 trading session and the breakdown of Black-Scholes assumptions.
- Spitznagel, Mark. *The Dao of Capital* (2013) and *Safe Haven* (2021) -- discussions of 1987 as the formative tail-risk event.
- Carlson, Mark. "A Brief History of the 1987 Stock Market Crash with a Discussion of the Federal Reserve Response" (Federal Reserve Board working paper, 2007) -- consolidated empirical narrative.
- Schwert, G. William. "Stock Volatility and the Crash of '87" (1990, *Review of Financial Studies*) -- academic measurement of the volatility regime around the event.

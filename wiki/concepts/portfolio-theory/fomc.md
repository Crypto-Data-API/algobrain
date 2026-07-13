---
title: "Federal Open Market Committee"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [macro, regulation]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[federal-reserve]]", "[[interest-rates]]"]
difficulty: intermediate
aliases: ["FOMC", "Federal Open Market Committee", "Fed Meeting", "fomc"]
related: ["[[federal-reserve]]", "[[fomc-meetings]]", "[[forward-guidance]]", "[[interest-rates]]", "[[interest-rate-risk]]", "[[fed-funds-futures]]", "[[us-dollar]]", "[[us-treasury-bonds]]", "[[macroeconomics]]", "[[inflation]]", "[[quantitative-easing]]", "[[monetary-policy]]", "[[dot-plot]]"]
---

The Federal Open Market Committee (FOMC) is the [[monetary-policy|monetary policy]]-making body of the [[federal-reserve|Federal Reserve System]] and the single most influential institution in global financial markets. The FOMC sets the target range for the federal funds rate -- the overnight interbank lending rate that serves as the benchmark for all USD-denominated interest rates -- and directs open market operations including the purchase and sale of [[us-treasury-bonds|US Treasury]] securities and mortgage-backed securities.

## Structure and Schedule

The FOMC consists of twelve members: the seven members of the Federal Reserve Board of Governors, the president of the Federal Reserve Bank of New York (a permanent voting member), and four of the remaining eleven regional Fed bank presidents who serve one-year voting terms on a rotating basis. (All twelve regional presidents attend and participate in discussion; only five vote at any time.) The committee meets eight times per year on a pre-announced schedule (roughly every six weeks), with the ability to hold emergency meetings during crises. Each meeting produces a policy statement, and four of the eight meetings include the Summary of Economic Projections (SEP) -- whose interest-rate panel is the [[dot-plot|"dot plot"]] -- charting each member's individual projection for the future path of interest rates. Detailed minutes of each meeting are released three weeks later, and the Fed Chair holds a press conference after every scheduled meeting.

| What is released | When (ET) | What it tells the market |
|------------------|-----------|--------------------------|
| Policy statement | 2:00 PM | The rate decision and the change in language (the "lean") |
| [[dot-plot\|Dot plot]] / SEP | 2:00 PM (4 of 8 meetings) | The committee's projected rate path, GDP, unemployment, inflation |
| Chair press conference | 2:30 PM | Tone, nuance, Q&A — often the bigger mover than the statement |
| Minutes | 3 weeks later | Detail and dissent behind the decision; can re-price expectations |

## Market Impact

FOMC announcements are among the highest-volatility scheduled events in global markets. The policy statement, released at 2:00 PM Eastern Time, is parsed word-by-word by algorithms and traders for any change in language that signals a shift in the committee's stance. The dot plot, when released, can move markets significantly if the median projected rate path diverges from market pricing (as reflected in [[fed-funds-futures]] and CME FedWatch probabilities). The press conference, beginning at 2:30 PM, often triggers a second wave of volatility as the Chair answers questions and provides nuance that the written statement cannot convey. Rate decisions ripple through every asset class: equities, bonds, currencies, commodities, and crypto all respond to changes in the expected path of US monetary policy.

> **Worked example — why the surprise, not the level, moves price.** Suppose the market has fully priced a 25 bp cut: [[fed-funds-futures]] imply a ~95% probability and equities have already drifted up into the meeting. If the FOMC delivers exactly that cut *and* the statement and [[dot-plot|dot plot]] match expectations, the reaction can be muted or even a "sell the news" pullback — the decision was already in the price. Now suppose the cut is delivered but the dot plot signals *fewer* cuts next year than the market expected (a "hawkish cut"): short-term yields and the [[us-dollar]] jump, and rate-sensitive growth equities sell off — despite a rate *cut* — because the *expected path* shifted up. The tradable variable is the gap between the outcome and what was already discounted.

### Cross-asset transmission (typical reaction)

| Asset | Hawkish surprise (higher-for-longer) | Dovish surprise (lower/sooner) |
|-------|--------------------------------------|--------------------------------|
| Short-term yields (2Y) | Up | Down |
| Long bonds / duration | Down (price) | Up (price) |
| [[us-dollar]] | Stronger | Weaker |
| Growth / long-duration equities | Pressured | Lifted |
| Gold | Pressured (higher real yields) | Lifted |
| Crypto / risk assets | Pressured (tighter liquidity) | Lifted |

These are tendencies, not laws — the reaction depends entirely on what was *already priced* going in.

## Forward Guidance and Quantitative Policy

Beyond the federal funds rate, the FOMC uses forward guidance -- explicit communication about the likely future path of policy -- as a tool to shape market expectations without actually moving rates. During the 2008-2015 and 2020-2022 periods, the FOMC also employed quantitative easing (QE), purchasing large quantities of Treasuries and mortgage-backed securities to push down long-term yields and stimulate the economy. The reverse process, quantitative tightening (QT), involves allowing securities to mature without reinvestment, shrinking the Fed's balance sheet and tightening financial conditions. Traders monitor the pace of QT as closely as rate decisions, since balance sheet policy directly affects liquidity conditions in the [[us-treasury-bonds|Treasury]] market and, by extension, risk appetite across all asset classes. The detailed communication mechanics of guidance are covered in [[forward-guidance]].

## The Dual Mandate

The FOMC operates under a congressionally defined **dual mandate**: maximum employment and price stability. Since 2012 the Fed has formally defined price stability as **2% inflation** over the longer run (measured by the PCE price index), and in 2020 it shifted to a "flexible average inflation targeting" framework that tolerates inflation running moderately above 2% for a time to make up for past undershoots. There is no fixed numerical target for employment because the "maximum" sustainable level shifts with demographics and productivity; the committee instead assesses a range of labour-market indicators. When the two objectives conflict — for example, high inflation alongside rising unemployment (stagflation) — the committee must weigh them, and how it signals that trade-off is itself market-moving.

## Trading and Portfolio Relevance

- **Highest-impact scheduled event.** FOMC days reset the entire USD interest-rate complex; for the options-surface, vol, and intraday-pattern implications (pre-announcement drift, even-week FOMC cycle, term-structure inversion and crush), see the companion page [[fomc-meetings]].
- **Path over level.** Markets price the rate *decision* in advance most of the time; the move is to the *unexpected* component — the tone, the [[forward-guidance|dot plot]], and the revision to the projected path priced in [[fed-funds-futures|fed funds futures]] and CME FedWatch.
- **Cross-asset transmission.** Hawkish surprises lift the dollar and short-duration value while pressuring long-duration growth and gold; dovish surprises reverse it. Balance-sheet (QT pace) changes can matter more than the rate decision for liquidity-sensitive assets including crypto.

## Common Pitfalls and Risks

- **Trading the headline, not the surprise.** Reacting to "the Fed cut/hiked" without checking what was already priced is the classic retail error — the move is in the *unexpected* component (see worked example above).
- **The 2:00–2:30 whipsaw.** Markets often spike one way on the statement, then fully reverse on the press conference once the Chair adds nuance. Position entered on the first move can be stopped out by the second.
- **Vol crush.** Implied [[volatility|volatility]] is elevated into the meeting and collapses afterward regardless of direction; buying naked options right before the print can lose money even on a correct directional call.
- **Over-reading a single dot.** The [[dot-plot|dot plot]] is a snapshot of individual projections, not a commitment; it is frequently wrong about its own future path, and the median can swing meeting to meeting.
- **Forgetting the balance sheet.** Focusing only on the rate ignores [[quantitative-easing|QT/QE]] pace, which drives liquidity and can dominate the reaction for risk assets.
- **Liquidity gaps and slippage.** Spreads widen and depth thins around 2:00 PM; stop orders can fill far from the trigger.

## Related

- [[federal-reserve]] — the central-bank system the FOMC sits within
- [[monetary-policy]] — the broader policy toolkit the FOMC executes
- [[fomc-meetings]] — the options/volatility and market-microstructure companion page
- [[dot-plot]] — the Summary of Economic Projections rate panel
- [[forward-guidance]] — the communication tool the committee uses to shape expectations
- [[fed-funds-futures]] — where the market-implied policy path is priced
- [[interest-rates]] / [[interest-rate-risk]] — the variable set and the duration exposure it creates
- [[us-treasury-bonds]] — directly affected by rate and balance-sheet decisions
- [[quantitative-easing]] — the balance-sheet tool (QE/QT)
- [[inflation]] — one half of the dual mandate
- [[macroeconomics]] — the broader macro framework

## Sources

- Federal Reserve Board — *About the FOMC*, *FOMC Calendars, Statements, and Minutes*, and the *Summary of Economic Projections* (federalreserve.gov/monetarypolicy).
- Federal Reserve — *Statement on Longer-Run Goals and Monetary Policy Strategy* (2012, revised 2020) — the dual-mandate and 2% / flexible-average-inflation-targeting framework.
- Federal Reserve Act, Section 2A — the statutory dual mandate (maximum employment, stable prices).
- CME Group — *FedWatch Tool* and the [[fed-funds-futures|fed funds futures]] complex, the standard market gauge of policy-path probabilities.

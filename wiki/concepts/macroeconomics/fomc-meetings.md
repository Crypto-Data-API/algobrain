---
title: "FOMC Meetings"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [macro, federal-reserve, monetary-policy, volatility, options, calendar-effects]
aliases: ["FOMC", "Federal Open Market Committee", "FOMC Date"]
domain: [macroeconomics, market-microstructure]
prerequisites: ["[[federal-reserve]]", "[[interest-rates]]"]
difficulty: intermediate
related: ["[[federal-reserve]]", "[[fomc]]", "[[fomc-drift]]", "[[interest-rates]]", "[[interest-rate-risk]]", "[[fed-funds-futures]]", "[[us-treasury-bonds]]", "[[implied-volatility]]", "[[volatility-term-structure]]", "[[volatility-regime]]", "[[theta-targeting]]", "[[vega-budgeting]]", "[[expiration-laddering]]", "[[macro-events]]", "[[options-portfolio-construction]]"]
---

The Federal Open Market Committee (FOMC) holds **eight scheduled meetings per year** plus occasional unscheduled meetings during crises. The scheduled meetings are the single highest-impact recurring events on the US economic calendar — they reset the path of the federal-funds rate, drive the short end of the [[us-treasury-bonds|Treasury]] curve, and produce some of the most reliable short-window patterns in equity returns and the [[implied-volatility|IV]] surface. For a [[theta-targeting|theta-targeted]] options book, FOMC dates are not just macro noise to weather — they are surface-distorting events that should be explicitly *shaped around* in the [[expiration-laddering|DTE ladder]]. This page focuses on the **market-microstructure and options-vol implications** of FOMC dates; for the institutional structure and policy mechanics of the committee, see [[fomc]].

## Overview

The FOMC is the monetary-policy arm of the [[federal-reserve|Federal Reserve System]]. Each meeting produces:

- **Policy statement** — released at 2:00 PM Eastern, parsed word-by-word.
- **Summary of Economic Projections (SEP)** with the "dot plot" — at four of the eight annual meetings (March, June, September, December).
- **Press conference** — Fed Chair, beginning at 2:30 PM, runs ~45–60 minutes.
- **Minutes** — released three weeks later.

Each of these has measurable, distinct market impact. The intraday "FOMC drift" / "FOMC pump" pattern — abnormal equity returns running into and around the announcement window — is one of the most robust calendar effects in the US data, documented by Cieslak, Morse, & Vissing-Jorgensen (2019) in *American Economic Review*. The vol-surface effects — front-end IV ramp, term-structure inversion, and post-meeting crush — mirror the earnings-vol cycle in form, though at index level and with different magnitudes.

## How It Works

### Schedule and unscheduled meetings

Eight scheduled meetings per year, typically every six weeks, on a published calendar. Unscheduled meetings occur during crises:

- **2008-10-08** — emergency 50-bp cut in concert with global central banks during the GFC.
- **2020-03-03** — emergency 50-bp cut, and **2020-03-15** emergency 100-bp cut to zero, during the Covid liquidity event.
- **2023-03 weekend actions** — facility announcements (BTFP) following SVB collapse, communicated via the FOMC channel even where not formally a meeting.

Unscheduled meetings are **vol-shock events** — IV spikes across the curve, the term structure can invert sharply within hours, and the [[options-premium-selling|short-vol]] cohort takes large mark-to-market hits.

### Effect on the vol surface

Front-end (1–14 DTE) IV rises into a scheduled FOMC meeting. The ramp is smaller than a single-name earnings ramp but distributed across the *entire index complex* (SPX, NDX, RUT, individual mega-caps via [[implied-correlation|implied correlation]]). Typical magnitudes on SPX:

- Front-week IV ramp: +1 to +3 absolute vol points in the 5 trading days before the meeting.
- Term-structure inversion: front cycle 1–2 vol points above the next monthly cycle as the meeting approaches.
- Post-meeting crush: 1–4 absolute vol points within the first hour after the statement, with a second leg during/after the press conference depending on tone.

When the meeting is *expected to be policy-changing* (cut/hike vs hold), magnitudes roughly double. When the dot plot is included, the meeting is significantly higher impact than statement-only meetings.

### The intraday FOMC pattern

Cieslak, Morse, & Vissing-Jorgensen (2019) document the **"FOMC cycle"** — average US equity returns are systematically higher in *even weeks* relative to the FOMC announcement (week 0 is the announcement week, with even weeks 0, 2, 4, 6 outperforming odd weeks 1, 3, 5). The effect is large enough that **the entire equity risk premium since 1994 was earned in the even-week subset of the calendar.** The leading explanation is that FOMC communication and informal Fed-speak unevenly resolves uncertainty across the cycle; markets reward holding through resolution.

Adjacent and complementary effects:

- **Pre-FOMC announcement drift** (Lucca & Moench, 2015, *Journal of Finance*): in the 24 hours before the 2pm announcement, S&P 500 cumulative returns averaged ~50 bps in the 1994–2011 window, accounting for ~80% of the equity risk premium over the sample. See [[fomc-drift]].
- **Post-statement intraday volatility** spikes during the 2:00–3:00 PM window, often reverses partially after the press conference, then mean-reverts overnight.
- **2:00 PM "head-fake"** — frequent immediate move on the statement is reversed during or after the press conference as nuance emerges. Discretionary traders generally avoid taking new positions in the 2:00–2:30 PM window for this reason.

### SOMA, balance sheet, and liquidity

The System Open Market Account (SOMA) is the Fed's portfolio of Treasuries and MBS. Quantitative tightening (QT) — letting securities mature without reinvestment — is set by the FOMC and has measurable effects on liquidity in repo markets, Treasury bill issuance, and the supply of dollar liquidity to risk assets. Communicated changes to the QT pace are vol-surface events even when the rate decision is unchanged. Balance-sheet policy also drives [[reverse-repo-rate|RRP balance]] dynamics that affect short-term funding markets and, by extension, equity factor returns.

### FedWatch and the path

The CME [[fed-funds-futures]] curve and the CME FedWatch tool quote market-implied probabilities of policy actions at each upcoming meeting. The market typically prices the *next* meeting's outcome with high confidence (>80% on a single action by 1 week before). The longer-dated path — six months, twelve months out — is far more diffuse, and re-pricing of that path is the dominant channel through which FOMC days move risk assets. A meeting can be a "dovish hold" (no rate change but lower-than-expected dot plot) or a "hawkish hold" (no change but higher dot plot) and produce a 1–3% S&P move on either tone shift, even with no actual policy change.

## Examples / Empirical Evidence

### Cieslak, Morse & Vissing-Jorgensen (2019)

*"Stock Returns over the FOMC Cycle"*, *Journal of Finance*, vol. 74. The seminal paper documenting that **equity excess returns over Treasury bills from 1994–2016 are concentrated in even weeks** of the FOMC calendar (week 0, 2, 4, 6 around each meeting). The pattern persists post-publication and across subsamples. The proposed mechanism — informal Fed communication dripping out unevenly across the cycle — does not fully explain the effect, but the empirical regularity is robust.

### Lucca & Moench (2015) — pre-FOMC announcement drift

*"The Pre-FOMC Announcement Drift"*, *Journal of Finance*. Cumulative S&P 500 returns from 2pm the day *before* an FOMC announcement to 2pm of the announcement day average ~50 bps over the 1994–2011 sample, vs ~1–2 bps on a typical 24-hour window. Eight FOMC meetings per year times 50 bps ≈ 4% per year, accounting for ~80% of the equity risk premium in that sample. See [[fomc-drift]].

### 2022-12-14 hawkish-hold reaction

Fed held rates as expected but raised the dot plot's terminal-rate projection by 50 bps. SPX dropped −2.5% from the announcement to close. Front-week SPX IV had *crushed* immediately on the no-change statement, then **re-ramped during the press conference** as the dot-plot tone became apparent — an unusual round-trip on the surface that caught short-strangle sellers on both sides.

### 2024-09-18 dovish 50-bp cut

First cut of the cycle, larger than the consensus 25 bps. SPX +1% on the day; front-week IV crushed sharply; the [[volatility-term-structure|term structure]] normalised quickly as the policy uncertainty resolved into a clear easing path. A textbook "in-line crush" where the implied move was largely realised but the post-event surface clean-up favoured short-vol entrants closing into the next session.

### 2020-03-15 emergency cut

Sunday-evening 100-bp cut to zero plus QE restart. Monday: SPX -12% (limit-down at open), VIX +25 points to >80. **Unscheduled FOMC actions are vol-shock events**; any short-vol book holding through these prints catastrophic mark-to-market losses. The standard practitioner rule is to size as if every FOMC week could become unscheduled.

## Implications for Strategy / Common Mistakes

### Implications for theta-targeted books

- **DTE laddering should explicitly span or avoid FOMC dates**. A 45 DTE [[iron-condor]] that crosses an FOMC meeting is a different product from one that does not. Many practitioners run a second ladder rule: "no new front-cycle positions opened in the 5 trading days before an FOMC meeting except as paired front/back-month structures." See [[expiration-laddering]].
- **Pre-FOMC theta is partially unrealised** — analogous to pre-earnings theta in single names. The position is bleeding to vega expansion at the same time it accrues theta. Realised P&L only arrives in the post-meeting crush.
- **The FOMC pump is a tailwind for short-premium books** *on average* — the post-2pm crush is the high-decay window that completes the cycle. But unscheduled meetings or surprise tone shifts (hawkish hold) reverse this and produce the worst single-day P&L outcomes.
- **Vega budgeting** should include an FOMC-stress scenario: a +5 vol-point shock to the front cycle, holding back month flat (the canonical surface signature of a surprise meeting). Books that pass a uniform IV-shock test can fail this scenario. See [[vega-budgeting]] and [[options-stress-testing]].

### Implications for systematic strategies

- **Do not pretend FOMC days are normal days** in a backtest. Returns, vol, and skew are non-stationary across the FOMC cycle. Strategies that require IID returns produce inflated Sharpes if they implicitly load on the FOMC pattern (the Lucca-Moench drift alone can rescue an otherwise bad strategy).
- **Calendar-aware backtesting** should bucket performance into pre-FOMC, FOMC-day, and post-FOMC windows and report each separately. A strategy that earns its entire return in the announcement window is making one bet per quarter, not many.
- **Even-week vs odd-week loading** — the Cieslak et al. finding is large enough that any factor strategy with a bias toward even weeks of the FOMC cycle is unconsciously loading on the FOMC factor. Worth checking explicitly.

### Common mistakes

- **Treating the 2:00 PM print as the end of the event** — the press conference at 2:30 frequently produces a second leg of move and re-pricing. Many "won at 2:00" trades turn into losses by 4:00.
- **Selling premium right before an FOMC meeting because the IV ramp makes it look rich** — without sizing for the unscheduled-meeting tail, this is buying a small cushion against a large left tail.
- **Carrying single-name short-vol books through unscheduled meetings** — the index-level vol shock spreads to single names via implied correlation, and short-strangle sellers on individual names are blown up alongside index sellers.
- **Confusing the policy decision with the surprise** — what moves markets is the *tone*, *dots*, and *path-revision*, not the rate change itself. The market prices the rate decision in advance most of the time; the surface reaction is to the *unexpected* component.
- **Ignoring the SOMA / balance-sheet announcement** — QE and QT pace changes are sometimes the most consequential element of the meeting, even when the rate decision is uneventful.

## Related

- [[fomc]] — the institutional / structural reference page on the committee
- [[federal-reserve]] — the Fed system as a whole
- [[fomc-drift]] — the pre-announcement drift anomaly
- [[fed-funds-futures]] — market-implied probabilities of policy actions
- [[interest-rates]] — the macro variable being set
- [[interest-rate-risk]] — duration exposure across the book
- [[us-treasury-bonds]] — directly affected by FOMC actions
- [[implied-volatility]] — the input the meeting reshapes
- [[volatility-term-structure]] — pre- and post-meeting term-structure inversion
- [[volatility-regime]] — regime-conditional sizing of short-vol books
- [[theta-targeting]] — why FOMC weeks distort the realisation of theta income
- [[vega-budgeting]] — FOMC stress scenarios in the budget
- [[expiration-laddering]] — laddering DTE explicitly around FOMC dates
- [[options-portfolio-construction]] — where macro-event sizing fits in the broader book
- [[macro-events]] — broader macro-event taxonomy
- [[options-stress-testing]] — formal stress scenarios including FOMC

## Sources

- Cieslak, A., Morse, A., & Vissing-Jorgensen, A. (2019). *"Stock Returns over the FOMC Cycle."* *Journal of Finance*, 74(5), 2201–2248. (The paper establishing the even-week FOMC cycle pattern.)
- Lucca, D. O., & Moench, E. (2015). *"The Pre-FOMC Announcement Drift."* *Journal of Finance*, 70(1), 329–371.
- Federal Reserve Board — *FOMC Calendars and Statements*. https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- CME Group — *FedWatch Tool* and the [[fed-funds-futures|fed funds futures]] complex.
- [[itpm-trading-philosophy]] — practitioner framework for laddering DTE around macro events.

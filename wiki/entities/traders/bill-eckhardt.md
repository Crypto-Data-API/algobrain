---
title: "Bill Eckhardt"
type: entity
created: 2026-04-20
updated: 2026-06-22
status: excellent
tags: [person, futures, trend-following, quantitative, history]
entity_type: person
headquarters: "Chicago, USA"
website: "https://www.eckhardttrading.com"
aliases: ["Eckhardt", "William Eckhardt"]
related: ["[[turtle-trading]]", "[[richard-dennis]]", "[[turtle-traders]]", "[[trend-following]]", "[[donchian-channels]]", "[[atr]]", "[[position-sizing]]", "[[cta]]"]
---

Bill Eckhardt was the partner of [[richard-dennis|Richard Dennis]] in the famous [[turtle-trading|Turtle Trading]] experiment of the early 1980s. While Dennis argued that successful trading could be taught, Eckhardt maintained it required innate talent. Together they trained 23 novice [[turtle-traders|"Turtles"]], funding each with $200K–$2M to trade a [[donchian-channels|Donchian Channel]]-based [[breakout]] system with [[atr|ATR]]-normalised [[position-sizing]] (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]). Eckhardt lost the bet — the Turtles reportedly earned over $100 million — and went on to found **Eckhardt Trading Company (ETC)**, one of the longest-running systematic futures managers ([[cta|CTAs]]) in the industry.

## Key Facts

| Field | Detail |
|-------|--------|
| Born | Chicago (1940s); trained mathematician |
| Education | B.A. mathematics, DePaul (1969); M.S. mathematics, University of Chicago (1970); ~4 yrs doctoral research in mathematical logic |
| Known for | Co-creator of the [[turtle-traders\|Turtle Traders]] experiment (1983–84) with [[richard-dennis]]; founder of Eckhardt Trading Company |
| The wager | Dennis: trading can be taught (nature vs. nurture). Eckhardt: it requires innate skill — Eckhardt lost the headline bet |
| Firm | Eckhardt Trading Company (ETC), Chicago — founded 1991; peak >$1B managed; registered [[cta\|CTA]] |
| Method | Systematic [[trend-following]] + counter-trend + trend-neutral; avg trade ~9 days; rigorous [[backtesting]] / anti-[[overfitting]] |
| Signature views | Optimize *expectancy*, not win rate; "if it feels good, don't do it"; survival comes from [[position-sizing]], not entries; critic of [[optimal-f]] / maximal Kelly sizing |
| Profile | "The Mathematician" in Schwager's *The New Market Wizards* (1992) |
| Honor | 2016 CME Group Managed Futures Pinnacle Achievement Award (with Dennis) |

## Overview

- Born in Chicago; earned a mathematics degree (B.A. DePaul, 1969) and an M.S. in mathematics from the University of Chicago (1970), then spent four years in doctoral research in **mathematical logic** at the University of Chicago before leaving academia in 1974 to trade futures at the Mid-America Commodity Exchange alongside boyhood friend Richard Dennis.
- Profiled as **"The Mathematician"** in Jack Schwager's *The New Market Wizards* (1992) — the source of widely quoted Eckhardt maxims such as "the amateurs go broke taking large losses, the professionals go broke taking small profits" and his warnings against optimizing for comfort in trading.
- Founded **Eckhardt Trading Company in 1991** (incorporated May 1992; registered CTA since 1991), Chicago. ETC has managed **over $1 billion** at peak and reports a team of 17 including 6 full-time research scientists.
- Reported track record: roughly **14.5% annualized from July 1991 to May 2013** versus 9.2% for the S&P 500 over the same span; approximately **12% annualized over 1991-2022** (third-party compilations; programs are short-to-medium-term systematic, average trade duration ~9 days, spanning trend-following, counter-trend, and trend-neutral systems).
- Launched the **Evolution Strategies UCITS fund in 2020**.
- Jointly received (with Richard Dennis) the **2016 Managed Futures Pinnacle Achievement Award** from CME Group.
- **Status June 2026:** ETC's website remains active and the firm continues to operate as a systematic long-short global futures manager; Eckhardt keeps a low public profile, with no notable 2025-2026 news (Perplexity check, 2026-06-10).

## The Turtle Experiment (1983-1984)

Dennis and Eckhardt recruited two cohorts of trainees via newspaper ads, taught them a complete mechanical [[trend-following]] system in two weeks (Donchian-style 20/55-day breakouts, ATR ("N")-based position sizing, strict heat limits, pyramiding rules), and funded them with Dennis's capital. The experiment settled their nature-vs-nurture wager decisively in Dennis's favor on the headline result — but Eckhardt's caveat survived: dispersion among Turtles trading the *same rules* was large, which he attributed to differences in discipline and risk tolerance. Several Turtles (Jerry Parker of Chesapeake Capital, Paul Rabar, Liz Cheval) went on to run major CTAs.

## Trading Philosophy

Eckhardt's distinct contributions to systematic trading doctrine:

- **The "win-rate illusion":** systems should optimize expectancy, not the percentage of winners; high win-rate systems typically embed negative skew.
- **Anti-intuition:** "If it feels good, don't do it" — comfortable trades (taking quick profits, holding losers, averaging down) are systematically mispriced because the crowd shares the same impulses.
- **Risk control over prediction:** he attributes long-run CTA survival almost entirely to [[position-sizing]] and loss-cutting rather than entry signals.
- **Science of trading:** ETC's research culture treats system development as applied statistics, with heavy emphasis on avoiding [[overfitting|over-fitting]] — Eckhardt was an early public voice on data-mining bias in backtests.

### Position sizing and the optimal-f critique

Eckhardt is one of the most cited skeptics of **bet-maximizing** position sizing. Frameworks like Ralph Vince's [[optimal-f]] (and the related [[kelly-criterion|Kelly criterion]]) compute the fixed fraction of capital that maximizes the *long-run geometric growth rate* of an account. Eckhardt's objection is practical, not arithmetic: the optimal fraction is razor-edged. Trading even slightly *above* optimal-f produces violently worse compound returns than the optimum, and the inputs (win rate, payoff ratio, the largest expected loss) are estimated from a finite, non-stationary sample — so a trader who sizes at the historically "optimal" fraction is almost certainly sizing too large for the live distribution, and the drawdowns at full Kelly/optimal-f (routinely 50%+) are psychologically and operationally unsurvivable. His prescription is to trade at a *fraction* of the theoretical optimum, accept a lower geometric growth rate in exchange for a far smaller chance of ruin, and treat the **largest plausible loss** — not the average — as the binding constraint on size. This is the same instinct behind the Turtle "N"/[[atr|ATR]] sizing rule, which caps each position's dollar volatility and ties total portfolio "heat" to a fixed risk budget rather than to a return-maximizing bet size.

The companion idea — **optimize expectancy, not win rate** — follows directly: a system can win 70% of the time and still have negative expectancy if the occasional losses are large (negative skew), so sizing and system selection should target the *distribution* of outcomes (mean × frequency, net of the tail), not the comfort of a high hit-rate.

## Trading Relevance

Eckhardt is one of the primary sources of modern [[trend-following]] practice: the Turtle rules he co-taught are the most widely replicated mechanical system in retail and institutional folklore, and his *New Market Wizards* interview is standard reading on expectancy, skew, and position sizing. ETC's 30+ year audited CTA record is also a frequently cited datapoint that medium-term systematic futures trading can survive cost and regime change.

## Related

- [[turtle-trading]]
- [[turtle-traders]]
- [[richard-dennis]]
- [[trend-following]]
- [[breakout]]
- [[donchian-channels]]
- [[richard-donchian]]
- [[atr]]
- [[position-sizing]]
- [[optimal-f]]
- [[kelly-criterion]]
- [[expectancy]]
- [[cta]]
- [[backtesting]]
- [[overfitting]]

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)
- Eckhardt Trading Company official site: https://www.eckhardttrading.com/about-us/ (founding 1991, $1B+ peak managed accounts, Evolution Strategies UCITS 2020, team details; accessed 2026-06-10)
- Jack Schwager, *The New Market Wizards* (HarperBusiness, 1992) — "William Eckhardt: The Mathematician."
- The Hedge Fund Journal profile: https://thehedgefundjournal.com/eckhardt-trading-company/
- Michael Covel, *The Complete TurtleTrader* (HarperCollins, 2007) — Turtle experiment detail.
- CME Group, Managed Futures Pinnacle Achievement Award 2016 (Dennis & Eckhardt).
- Perplexity verification of current status, 2026-06-10.

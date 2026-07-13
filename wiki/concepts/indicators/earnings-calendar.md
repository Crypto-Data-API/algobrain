---
title: "Earnings Calendar"
type: concept
created: 2026-04-13
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, data-provider, event-driven]
domain: [fundamental-analysis]
prerequisites: ["[[earnings-per-share]]"]
difficulty: beginner
aliases: ["Earnings Calendar", "Earnings Season", "Earnings Schedule"]
related: ["[[earnings-per-share]]", "[[catalyst]]", "[[earnings-momentum]]", "[[data-sources-overview]]", "[[implied-volatility]]", "[[iv-crush]]", "[[economic-indicators]]", "[[earnings-season]]", "[[volatility]]", "[[event-driven-trading]]"]
---

An earnings calendar tracks the dates when publicly listed companies report quarterly or annual financial results. Earnings announcements are among the most significant [[catalyst|catalysts]] for stock price movement, and the calendar is the primary tool for timing entries and exits around reporting periods and for avoiding unhedged exposure during high-[[volatility]] earnings events. It is the corporate analog of the macro [[economic-indicators|economic calendar]].

## Earnings Season Structure

US [[earnings-season]] occurs four times per year, roughly in January (Q4 reports), April (Q1), July (Q2), and October (Q3). The bulk of S&P 500 companies report within a 4-6 week window each quarter. Companies report either before market open (pre-market) or after market close (after-hours), and the timing matters because it determines whether the initial price reaction occurs in the pre-market session or in after-hours trading. Banks traditionally kick off each earnings season, followed by large-cap tech, industrials, and smaller companies.

| Quarter | Fiscal period covered | Typical reporting months | Kicks off with |
|---------|----------------------|--------------------------|----------------|
| Q4 / full year | Oct-Dec | mid-January to mid-February | Big banks |
| Q1 | Jan-Mar | mid-April to mid-May | Big banks |
| Q2 | Apr-Jun | mid-July to mid-August | Big banks |
| Q3 | Jul-Sep | mid-October to mid-November | Big banks |

### Reporting time conventions

| Tag | Meaning | Typical clock (ET) | Where the move first prints |
|-----|---------|--------------------|------------------------------|
| **BMO** | Before market open | ~6:00-9:00 AM | Pre-market session |
| **AMC** | After market close | ~4:00-5:00 PM | After-hours session |
| **TBD / unconfirmed** | Date estimated, not yet confirmed | n/a | Verify before trading |

Popular tools for tracking earnings dates include Earnings Whispers, the Yahoo Finance earnings calendar, Nasdaq's earnings calendar, and brokerage-provided calendars from platforms like [[thinkorswim]] and [[interactive-brokers|Interactive Brokers]]. Note that reported dates are often unconfirmed estimates until the company officially announces, so traders verify before placing event-dependent trades.

## Why It Matters for Options Traders

For options traders, the earnings calendar is essential because of the [[implied-volatility]] dynamics surrounding reporting dates. [[implied-volatility|IV]] typically ramps up in the days and weeks before an earnings announcement as the market prices in uncertainty about the outcome, then collapses sharply after the announcement -- a phenomenon known as [[iv-crush]]. This creates opportunities for strategies that sell premium before earnings (straddles, strangles, iron condors) to capture the IV contraction, as well as strategies that buy premium early and sell before the report to ride the IV expansion.

### Worked example: the expected move

The market-implied expected move can be estimated from the price of the at-the-money (ATM) straddle expiring just after the report. A common rule-of-thumb: **expected move ≈ ATM straddle price ÷ stock price** (illustrative numbers):

- Stock trades at **$200**.
- The weekly ATM call costs **$7** and the ATM put costs **$6** -> straddle = **$13**.
- Implied expected move ≈ 13 / 200 = **±6.5%**, i.e. roughly **$187 to $213** by expiration.
- A premium seller profits if the actual post-report move is smaller than ±6.5% and IV crushes; a premium buyer needs a move *larger* than that to overcome the IV-crush headwind.

This is why simply being "right on direction" can still lose money through earnings: the post-report [[iv-crush]] can deflate an option even when the stock moves your way but by less than the priced-in expected move.

## Why It Matters for Directional Traders

Understanding the earnings calendar also helps directional traders avoid being unexpectedly caught in a binary event: holding an unhedged position through an earnings report is effectively a bet on the outcome, and the average post-earnings move for S&P 500 stocks is roughly 4-6% in either direction. Traders who want to exploit the post-event trend rather than the binary gamble watch for [[earnings-momentum|post-earnings announcement drift]] (PEAD), where prices continue in the direction of an earnings surprise for weeks afterward.

### Trader playbook around the calendar

| Goal | Typical approach | Key risk |
|------|------------------|----------|
| Avoid binary risk | Flatten or hedge directional positions before the date | Missing a favorable gap |
| Sell IV | Iron condor / short strangle placed pre-report, closed post-report | Outsized move beyond the wings |
| Buy IV (vol expansion) | Long calendar/straddle bought early, sold *before* the report | IV doesn't ramp; theta decay |
| Exploit the drift | Enter *after* the report in the surprise direction (PEAD) | Reversal / fading the gap |
| Breakout into earnings | Note when a [[base-pattern\|base]] resolves near a report date | Gap reverses the breakout |

## Common Pitfalls and Risks

- **Stale or unconfirmed dates**: many calendar sites show estimated dates. A position sized for a Thursday report can be blindsided if the company actually reports Tuesday. Always verify against the company's investor-relations page or a confirmed feed.
- **Underestimating gap risk**: stops do not protect against overnight earnings gaps; the open can be far through your stop level.
- **Ignoring IV crush as an options buyer**: buying cheap-looking options into earnings often loses to the post-report volatility collapse even on a correct directional call.
- **PEAD fade**: drift is a statistical tendency, not a guarantee; small-cap surprises can fully reverse within days.
- **Calendar clustering**: on the heaviest weeks of [[earnings-season]], dozens of correlated names report together, concentrating portfolio risk on a single day.
- **Guidance over the print**: forward guidance and conference-call commentary frequently move the stock more than the headline EPS/revenue beat or miss.

## Related

- [[earnings-per-share]] — the headline metric reported on the calendar date
- [[earnings-season]] — the clustered reporting windows the calendar organizes
- [[catalyst]] — earnings are the most common scheduled catalyst
- [[earnings-momentum]] — post-earnings announcement drift exploits the reaction
- [[implied-volatility]] — pre-earnings IV ramp and post-earnings crush
- [[iv-crush]] — the volatility collapse that follows the report
- [[event-driven-trading]] — the strategy family that trades scheduled catalysts
- [[economic-indicators]] — the macro analog of the corporate earnings calendar
- [[volatility]] — the underlying driver of pre- and post-report option pricing

## Sources

- Nasdaq, Yahoo Finance, and Earnings Whispers earnings calendars — primary public schedules of reporting dates.
- FactSet *Earnings Insight* — quarterly aggregate S&P 500 earnings season statistics (beat rates, average surprise, reporting timeline).
- General options-market knowledge for the expected-move and IV-crush mechanics; no additional specific wiki source ingested yet.

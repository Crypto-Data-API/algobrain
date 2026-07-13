---
title: "Earnings Season"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [fundamental-analysis, event-driven, stocks, volatility]
aliases: ["Earnings Season", "Reporting Season", "Earnings Wave"]
domain: [fundamental-analysis, market-microstructure]
prerequisites: ["[[earnings-per-share]]", "[[earnings-calendar]]"]
difficulty: beginner
related: ["[[earnings-calendar]]", "[[earnings-per-share]]", "[[earnings]]", "[[earnings-momentum]]", "[[catalyst]]", "[[implied-volatility]]", "[[iv-crush]]", "[[gap-risk]]", "[[event-driven-trading]]", "[[market-hours]]", "[[economic-indicators]]"]
---

**Earnings season** is the recurring stretch of weeks each quarter during which the bulk of publicly listed companies report their financial results. In the United States it happens four times a year, and because most large companies cluster their releases into the same few-week window, the period concentrates [[catalyst|catalysts]], [[volatility]], and trading volume. For a dashboard user, earnings season is simply the time of year when "your" stocks are most likely to gap, re-rate, or surprise. This page covers the *rhythm and behaviour* of the season; for the tool that lists exact dates, see [[earnings-calendar]].

## When earnings season happens

US companies report quarterly results roughly one to two months after each fiscal quarter ends. The four seasons are:

| Season | Quarter reported | Typical window | Opens with |
|--------|------------------|----------------|------------|
| **Q4 / full-year** | Oct–Dec | mid-January to mid-February | Big banks |
| **Q1** | Jan–Mar | mid-April to mid-May | Big banks |
| **Q2** | Apr–Jun | mid-July to mid-August | Big banks |
| **Q3** | Jul–Sep | mid-October to mid-November | Big banks |

The "official" start each quarter is informally marked by the large US banks (JPMorgan, Wells Fargo, Citigroup and peers), which report first. From there the wave broadens out over roughly four to six weeks: large-cap technology and consumer names follow, then industrials and healthcare, and finally the long tail of smaller companies. The single heaviest stretch is usually the two middle weeks, when hundreds of companies — including most of the megacaps that dominate the [[market-capitalization|cap-weighted]] indices — report within days of each other.

Other markets run on their own cadence. Australian companies on the [[asx-200|ASX]] report on a **half-yearly** rhythm (February and August "reporting season") because most use a June fiscal year-end and are only required to report twice a year, not quarterly. Many European companies similarly report half-yearly. So "earnings season" is a US-centric quarterly concept that has looser analogues elsewhere.

## The shape of a single report

Each company's report is a scheduled, binary-ish event. The headline numbers the market reacts to are:

- **Revenue** (the "top line") versus consensus expectations.
- **Earnings per share** ([[earnings-per-share|EPS]]) versus consensus — the "beat or miss."
- **Guidance** — management's forward outlook for next quarter / full year.

A company can "beat" on EPS and still fall, because the market trades the *surprise relative to expectations* and the *forward guidance*, not the raw number. Forward guidance and the earnings-call commentary frequently move the stock more than the headline beat or miss itself. A "beat-and-raise" (beat this quarter, raise guidance) is the bullish ideal; a "beat-and-lower" often sells off hard.

Historically, a clear majority of S&P 500 companies *beat* consensus EPS in any given quarter — typically around 70–80%. This is partly genuine and partly an artifact of expectation management: analysts and companies tend to guide estimates low enough that they can be cleared, so a "beat" is often already priced in. What moves a stock is the *magnitude and direction of the surprise* against what was expected, not the beat itself.

## Why the season matters for traders and dashboard users

- **Concentrated event risk.** Holding an unhedged position through a report is effectively a bet on a binary outcome. The average post-earnings single-stock move for an S&P 500 name is roughly 4–6% in either direction, and stops do **not** protect against an overnight [[gap-risk|gap]] — the open can be far through your stop level.
- **Reporting-time conventions.** Companies report either **before market open (BMO)** or **after market close (AMC)**, so the first big price reaction prints in the pre-market or after-hours session rather than the regular session. See [[market-hours]] for how those extended sessions behave.
- **Volatility cycle.** [[implied-volatility|Implied volatility]] in a stock's options typically ramps *up* into its report as uncertainty is priced in, then collapses immediately after — the [[iv-crush]]. This means an options buyer can be right on direction and still lose money if the move is smaller than the priced-in expected move.
- **Calendar clustering.** On the heaviest weeks, dozens of correlated names report together, concentrating portfolio risk onto single days. A diversified-looking book can behave like one big bet during peak season.
- **Index-level impact.** Because a handful of megacaps carry the [[s-and-p-500|S&P 500]], the days those specific giants report can move the whole index. Aggregate season statistics (overall beat rate, blended earnings growth, net profit margins) are watched as a read on corporate health and the broader market.

### The blackout period

In the weeks leading up to a report, companies typically enter a **buyback blackout** — a self-imposed window during which they stop repurchasing their own shares to avoid trading on material non-public information. Because corporate buybacks are a large, persistent source of demand for US equities, the clustering of blackouts around earnings season can quietly remove a buyer from the market, and the resumption of buybacks afterward can add support. This is a structural, calendar-driven flow effect rather than anything about the fundamentals.

## Post-earnings drift

The reaction does not always end on report day. **Post-earnings announcement drift** ([[earnings-momentum|PEAD]]) is the well-documented tendency for a stock to keep moving in the direction of an earnings surprise for days to weeks after the report — positive surprises drift up, negative surprises drift down. It is one of the most persistent anomalies in equity markets, usually attributed to investors underreacting to new information. Traders who want to exploit the *trend* rather than gamble on the *binary* often enter *after* the print, in the surprise direction, rather than holding through the event. The drift is a statistical tendency, not a guarantee — small-cap surprises in particular can fully reverse within days.

## How an ALFRED-style fundamental review uses the season

Earnings season is when the inputs to a fundamental analysis get refreshed. The metrics ALFRED tracks — revenue and EPS growth, margins, [[return-on-equity|ROE]], cash flow, debt — are restated each reporting period, so a report can change the investment case. Consistent with [[alfred-investment-philosophy|Fred McNaught's]] approach, a single quarter is noise; the value is in the *trend* across reporting periods and whether management's guidance proves reliable over time. A reporting date is also a scheduled point on a company's calendar (see the Company Calendar section of the [[alfred-report-methodology|report template]]) at which forecasts can be checked against actuals.

## Common pitfalls

- **Mistaking a beat for a buy.** If the beat was already expected, the stock can fall on a beat. Trade the surprise and the guidance, not the headline.
- **Underestimating gap risk.** Overnight earnings gaps jump straight through stop-loss levels; position sizing, not stops, is the real control.
- **Buying cheap-looking options into the print.** [[iv-crush]] routinely deflates an option even on a correct directional call.
- **Treating a clustered book as diversified.** Many holdings reporting the same week is concentration, not diversification.
- **Relying on unconfirmed dates.** Many calendar sites show *estimated* report dates until the company confirms — verify before placing event-dependent trades (see [[earnings-calendar]]).

## Related

- [[earnings-calendar]] — the tool that lists exact reporting dates and BMO/AMC tags
- [[earnings-per-share]] — the headline metric reported each season
- [[earnings]] — the broader earnings concept and its drivers
- [[earnings-momentum]] — post-earnings announcement drift (PEAD)
- [[catalyst]] — earnings are the most common scheduled catalyst
- [[implied-volatility]] — the pre-report IV ramp
- [[iv-crush]] — the post-report volatility collapse
- [[gap-risk]] — why stops fail across earnings reports
- [[market-hours]] — pre-market and after-hours, where earnings reactions first print
- [[event-driven-trading]] — the strategy family that trades scheduled catalysts

## Sources

- FactSet *Earnings Insight* — quarterly aggregate S&P 500 earnings-season statistics (beat rates, blended growth, reporting timeline).
- Nasdaq, Yahoo Finance, and Earnings Whispers earnings calendars — public schedules of reporting dates.
- ASX, "Reporting season" guidance — Australian half-yearly reporting cadence.
- General equity-market knowledge for post-earnings drift and buyback-blackout mechanics; no additional specific wiki source ingested yet.

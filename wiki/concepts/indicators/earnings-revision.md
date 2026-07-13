---
title: "Earnings Revisions"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [fundamental-analysis, momentum, indicators]
aliases: ["earnings revision", "earnings revisions", "estimate revision", "analyst revision momentum"]
domain: [fundamental-analysis]
prerequisites: ["[[earnings-per-share]]"]
difficulty: intermediate
related: ["[[momentum-screening]]", "[[canslim]]", "[[relative-strength]]", "[[economic-indicators]]", "[[ibd]]"]
---

Earnings revisions measure changes in analyst consensus estimates for a company's future earnings per share (EPS). When analysts raise their estimates, it signals improving business fundamentals that the market has not yet fully priced in; when they lower estimates, it signals deterioration. Revisions are widely regarded as one of the most powerful alpha signals in equity investing because they capture fundamental momentum — real changes in a company's earnings trajectory — rather than just price momentum.

## Types of Revisions

Analysts publish estimates for multiple time horizons, and each carries different informational value:

- **FY1 EPS (current fiscal year)** — The most closely tracked estimate. Changes here reflect near-term business conditions and are highly actionable for swing and position traders.
- **FY2 EPS (next fiscal year)** — Revisions to forward-year estimates often carry more weight because they reflect structural changes in the business, not just one quarter's noise.
- **Revenue revisions** — Less commonly tracked but equally important. Revenue revisions capture top-line growth changes, which can precede earnings revisions when margins are stable.
- **Quarterly EPS (Q1-Q4)** — Granular revisions around specific quarters, often driven by guidance updates or channel checks.

## Measuring Revision Breadth

The most common metric is **revision breadth**, calculated as the percentage of analysts revising estimates upward minus the percentage revising downward over a given period (typically 1 month or 3 months). A stock covered by 20 analysts where 15 have raised estimates and 2 have lowered them has revision breadth of (15/20) - (2/20) = 65% — a strong positive signal.

Other measures include the **magnitude** of revisions (a 20% increase in consensus EPS is more meaningful than a 2% increase) and the **acceleration** of revisions (revisions becoming larger and more frequent).

## Post-Revision Drift

Research by Gleason and Lee (2003) demonstrated that stocks experiencing positive earnings revisions continue to outperform for 6-12 months following the revision — a phenomenon called **post-revision drift**. This is the earnings revision analog of [[momentum-trading|post-earnings announcement drift]] (PEAD). The market systematically underreacts to the information contained in analyst revisions, creating a tradeable window.

The drift is strongest when:
- Revisions are large in magnitude
- Multiple analysts revise in the same direction (high breadth)
- The revision follows an [[earnings|earnings beat]] (the surprise-revision cycle)

## The Earnings Surprise Cycle

Earnings revisions do not occur in a vacuum. The typical cycle works as follows:

1. A company reports an earnings beat (actual EPS exceeds consensus)
2. Analysts raise their forward estimates in response
3. The raised estimates create a higher bar for the next quarter
4. If the company beats again, the cycle repeats — creating sustained revision momentum

This virtuous cycle explains why stocks with consecutive earnings beats and rising revisions often produce the strongest momentum returns. It is a core principle behind [[canslim|CANSLIM's]] emphasis on accelerating quarterly earnings.

## Revisions as a Leading Indicator

Unlike backward-looking metrics such as trailing EPS growth or P/E ratios, earnings revisions are forward-looking. They incorporate new information — management guidance, industry data, macro changes — before it shows up in reported financials. This is why revision momentum is considered a leading indicator and is heavily weighted in [[momentum-screening]] models alongside price momentum.

## Practical Use in Screening

In a multi-factor [[momentum-screening|momentum screen]], earnings revision momentum typically receives 20-30% weight. Common thresholds include:
- Positive net revisions (more ups than downs) over the past 3 months
- FY1 consensus EPS estimate increase of at least 5% over the past 90 days
- At least 3 analysts covering the stock (to avoid thin-coverage noise)

## Related

- [[momentum-screening]] — Earnings revisions are a key input in systematic momentum screens
- [[canslim]] — The "E" in CANSLIM emphasizes current earnings acceleration, which drives revisions
- [[fundamental-analysis]] — Revisions bridge the gap between fundamental and technical analysis

## Sources

- Gleason, C. A. & Lee, C. M. C. (2003). "Analyst Forecast Revisions and Market Price Discovery." *The Accounting Review*, 78(1), 193-225 — documents post-revision drift and market underreaction to analyst revisions.
- Givoly, D. & Lakonishok, J. (1979). "The Information Content of Financial Analysts' Forecasts of Earnings." *Journal of Accounting and Economics* — early evidence that revisions carry tradeable information.
- Zacks Investment Research — popularized revision-breadth ranking systems (the Zacks Rank) built on analyst estimate revisions.

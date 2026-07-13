---
title: "Cash Runway"
type: concept
created: 2026-07-03
updated: 2026-07-03
status: good
tags: [fundamental-analysis, valuation, risk-management, liquidity]
aliases: ["Cash Runway", "cash-runway", "Runway", "Cash Burn Runway"]
domain: [fundamental-analysis, risk-management]
difficulty: beginner
related: ["[[burn-rate]]", "[[free-cash-flow]]", "[[dilution]]", "[[cash-flow-statement]]", "[[rule-of-40]]", "[[liquidity]]", "[[working-capital]]", "[[bankruptcy]]"]
---

Cash runway is an estimate of how long a company can keep operating before it runs out of cash, assuming it keeps spending at its current rate. It is calculated as the company's cash and equivalents divided by its monthly net [[burn-rate]], and is usually expressed in months. Runway is one of the most important figures for judging an unprofitable, cash-consuming business — early-stage start-ups and pre-profit growth companies — because for such firms the balance-sheet cash pile, not reported earnings, is the binding constraint on survival.

## What it measures

For a profitable company, next year's cash comes largely from this year's operations, so survival is rarely in question. For a company that spends more cash than it brings in, every month erodes a finite cash reserve. Runway answers the blunt question: *at the current pace, how many months of cash are left?*

**Runway (months) = cash and equivalents ÷ monthly net burn**

- "Cash and equivalents" is the liquid balance available to fund operations — typically cash, bank deposits, and short-term marketable securities, and sometimes an undrawn credit line if it is genuinely accessible.
- "Monthly net burn" is the net amount of cash consumed per month. It can be measured backward-looking (from recent actuals) or forward-looking (from the company's own budget or an analyst's forecast). A forward estimate is often more useful because burn frequently changes as a company scales, cuts costs, or approaches breakeven.

A company with £24m of cash burning £2m per month has roughly 12 months of runway. When runway shrinks toward zero, the company must either raise more capital, cut spending, or reach cash-flow breakeven — or it faces insolvency.

## Gross versus net burn

Two different "burn" figures are commonly quoted, and confusing them produces very different runways:

- **Gross burn** is total operating cash outflow per month — everything the company spends to keep the lights on (salaries, rent, marketing, cloud, etc.), ignoring any revenue.
- **Net burn** is gross burn minus cash *received* (mainly from customers). Net burn is the figure that actually depletes the cash balance, so runway should almost always be computed on **net** burn.

A company can have high gross burn but modest net burn if it already earns meaningful revenue; conversely a pre-revenue firm's gross and net burn are nearly identical. See [[burn-rate]] for the full treatment.

## Estimating burn from the financials

Burn is not a line item on the [[cash-flow-statement]]; it is derived from it:

- The simplest proxy is the **change in cash** over a period: if cash fell from £30m to £18m over six months, net burn averaged about £2m per month. This captures everything — operations, investing, and financing — but can be distorted by one-off financing events (a capital raise inflates cash) or large investments.
- A cleaner operating measure combines **operating cash flow** with the necessary portion of **investing cash flow** (chiefly maintenance [[capex]]). Cash from *financing* (new equity or debt) is normally excluded, because the point of runway is to measure how long the business survives *without* fresh capital.
- For a maturing company that is close to or past breakeven, [[free-cash-flow]] (operating cash flow minus capex) is often the natural burn measure — negative FCF is the cash the business consumes each period, and dividing cash by that rate gives a runway. Positive FCF means there is, in effect, no runway problem at all.

Because reported cash flows are lumpy quarter to quarter, analysts typically average several periods or use a forward budget rather than annualising a single noisy quarter.

## Why it matters to investors

Runway is fundamentally a measure of **financing risk**, and it drives several investment considerations:

- **Dilution and financing risk.** A short runway is a near-certain signal that a capital event is coming. If the company cannot reach breakeven in time, it must raise equity — diluting existing shareholders (see [[dilution]]) — or take on debt, which adds interest cost and covenants. Equity raised from a position of weakness (a nearly empty treasury) is usually done at a depressed price, so a short runway is often bad for the *existing* share price even when the raise itself keeps the company alive.
- **The 2022-2024 "profitability pivot."** After more than a decade of ultra-low interest rates, monetary tightening from 2022 sharply raised the cost of capital and made investors far less willing to fund cash-burning businesses. Growth and technology companies that had run on cheap external capital pivoted hard toward extending runway — mass layoffs, cost cuts, and a rhetorical shift from "growth at all costs" to "efficient growth" and a "path to profitability." Runway became a headline metric in that period precisely because raising the next round was no longer a formality.
- **Screening speculative names.** Runway is a core screen for speculative growth and [[penny-stock]] investing and for pre-profit technology companies, where the difference between a firm with three years of cash and one with three months is enormous. Combined with a growth-versus-profitability heuristic like the [[rule-of-40]], runway helps separate businesses that can afford to keep spending from those that cannot.
- **[[liquidity]] and solvency context.** Runway sits alongside conventional liquidity measures (current ratio, quick ratio, [[working-capital]]) but is more forward-looking: it explicitly projects the cash balance against the spend rate rather than taking a static snapshot.

## Caveats

- **Burn is lumpy.** Cash outflows are rarely smooth. One-off items (litigation settlements, restructuring, milestone payments), seasonal patterns, and [[working-capital]] swings (a build-up of inventory or receivables) can make any single period's burn unrepresentative. A runway computed from one noisy quarter can be badly wrong; use a multi-period average or a forward budget.
- **Access to capital markets matters more than the number.** Runway assumes no new financing, but a company with a credible path to profitability can often raise on good terms even with a low cash balance, while a business the market has soured on may be unable to raise at *any* price. The strength of the equity story and the state of the financing window frequently matter more than the raw months of cash.
- **Runway is not the same as solvency.** A company approaching the end of its runway is not automatically bound for [[bankruptcy]]. Management can pull levers — cut discretionary spending, slow hiring, and steer the business toward cash-flow breakeven — that extend or eliminate the runway problem. Runway measures the *current* trajectory, not an inevitable outcome.
- **Buffer conventions are rules of thumb, not laws.** In start-up practice, a common comfort threshold is to hold roughly **12 to 18 months** of runway, so that there is time to hit milestones and raise the next round before cash gets dangerously low. This is a widely-cited convention, not a fixed rule — appropriate runway depends on the business model, the fund-raising environment, and how predictable the burn is.

## Worked example

A pre-profit software company holds **£30m** in cash and equivalents. Over the last two quarters its cash balance fell by **£12m**, so its average net burn is:

- £12m ÷ 6 months = **£2m per month** of net burn.

Runway at the current pace:

- £30m ÷ £2m per month = **15 months** of runway.

Fifteen months sits comfortably inside a typical 12-18 month buffer, but suppose the company then doubles its sales-and-marketing spend and net burn rises to **£3m per month**:

- £30m ÷ £3m per month = **10 months** of runway.

Now the company is inside the danger zone: with only ten months of cash it will likely need to raise (accepting [[dilution]]) or cut costs within the next couple of quarters. If instead it had trimmed burn to **£1.5m per month**, runway would extend to £30m ÷ £1.5m = **20 months**, buying time to reach breakeven or negotiate a raise from strength. These figures are illustrative round numbers and are not tied to any specific company.

## Related

[[burn-rate]] · [[free-cash-flow]] · [[dilution]] · [[cash-flow-statement]] · [[rule-of-40]] · [[liquidity]] · [[working-capital]] · [[bankruptcy]] · [[penny-stock]] · [[capex]]

## Sources

- General, widely-taught corporate-finance and start-up-financing knowledge. Cash runway, burn rate, and the gross-versus-net-burn distinction are standard concepts in venture-capital and early-stage-investing practice; the 12-18-month buffer is a commonly-cited rule of thumb rather than a fixed rule. The observation that cash-burning companies pivoted toward extending runway as interest rates rose from 2022 reflects widely-reported market conditions of that period. No specific company figures are cited — the numeric examples above are illustrative round numbers.

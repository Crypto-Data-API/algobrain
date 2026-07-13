---
title: "Net Income"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [fundamental-analysis, valuation, indicators]
aliases: ["net income", "net profit", "bottom line", "net earnings", "profit after tax", "PAT", "NPAT"]
domain: [fundamental-analysis]
prerequisites: ["[[operating-income]]", "[[gross-profit]]"]
difficulty: beginner
related: ["[[earnings-per-share]]", "[[operating-income]]", "[[gross-profit]]", "[[return-on-equity]]", "[[return-on-assets]]", "[[free-cash-flow]]", "[[financial-statement-analysis]]"]
---

**Net income** (also called Net Profit, Net Earnings, or "the bottom line") is the final profit a company reports after deducting all expenses from revenue: cost of goods sold, operating expenses, interest, and taxes. It is the most-watched single number in corporate accounting and the basis for [[earnings-per-share|EPS]], dividend decisions, and most valuation multiples.

## Formula

```
Net Income = Revenue
           − COGS
           − Operating Expenses
           − Interest Expense
           + Other Income / − Other Expenses
           − Income Tax
```

Or, working from operating income:

```
Net Income = Operating Income (EBIT) − Interest − Taxes
```

## Why It's the "Bottom Line"

Net income is the final number on the income statement (literally the bottom line). It represents what is legally available to shareholders — either to be reinvested (retained earnings) or distributed as dividends. Public companies report net income quarterly, and analysts compare it against consensus expectations to drive short-term stock movements.

## Profit Hierarchy

Net income is the endpoint of the income statement waterfall:

```
Revenue
  − COGS              → Gross Profit
  − Operating Expenses → Operating Income (EBIT)
  − Interest, Taxes   → Net Income  ← you are here
```

## Used In Many Other Metrics

Net income is the numerator in many of the most important financial ratios:

- **[[earnings-per-share|EPS]]** = (Net Income − Preferred Dividends) / Shares Outstanding
- **[[return-on-equity|ROE]]** = Net Income / Shareholders' Equity
- **[[return-on-assets|ROA]]** = Net Income / Total Assets
- **[[price-to-earnings-ratio|P/E Ratio]]** = Stock Price / EPS = Market Cap / Net Income
- **Net Margin** = Net Income / Revenue

## Limitations

Net income is heavily influenced by accounting choices and one-off items:

- **Non-cash charges**: depreciation, amortisation, impairments, stock-based compensation can dramatically reduce reported net income without affecting actual cash generated
- **One-off items**: gains/losses on asset sales, restructuring charges, legal settlements distort comparisons across periods
- **Tax engineering**: a low effective tax rate one quarter (e.g., from utilising NOLs) can boost net income temporarily
- **GAAP vs adjusted**: companies often report "adjusted" or "non-GAAP" net income that excludes items management deems non-recurring — sometimes legitimate, sometimes a way to hide recurring problems

For these reasons, sophisticated investors complement net income analysis with [[free-cash-flow|Free Cash Flow]] (which is harder to manipulate) and [[operating-income|Operating Income]] (which strips out financing and tax distortions).

## Trading Relevance

Net income drives the single most important event in the equity calendar: the quarterly earnings report. Stocks gap on the **surprise** — reported EPS (net income per share) versus consensus — and then frequently continue drifting in the surprise's direction for weeks, the well-documented **post-earnings-announcement drift (PEAD)** anomaly (Bernard & Thomas, 1989). Key trading angles:

- **Earnings momentum / PEAD**: long positive surprises, short negative ones; the drift is strongest in the days-to-weeks after the print.
- **Quality of earnings (accruals)**: net income built on rising accruals rather than cash tends to mean-revert and underperform (Sloan's accruals anomaly, 1996) — a short signal. Reconcile net income to [[free-cash-flow]] before trusting it.
- **GAAP vs adjusted divergence**: a widening gap between adjusted and GAAP net income is a red flag that management is excluding recurring costs.

Because net income is the most manipulable headline number, professional traders treat a beat that comes from a low tax rate, a one-off gain, or aggressive capitalisation very differently from a beat driven by [[gross-margin]] expansion.

## Related

- [[earnings-per-share]]
- [[operating-income]]
- [[free-cash-flow]]
- [[return-on-equity]]

## Sources

- [[fred-gross-profit-article]]
- [[fred-share-investing-guide]]
- Sloan, Richard G. (1996). "Do Stock Prices Fully Reflect Information in Accruals and Cash Flows about Future Earnings?" *The Accounting Review* 71(3).
- Bernard, V. & Thomas, J. (1989). "Post-Earnings-Announcement Drift." *Journal of Accounting Research* 27.
- FASB / IFRS income-statement presentation standards.

---
title: "Income Statement"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, education, stocks]
domain: [fundamental-analysis, valuation]
difficulty: beginner
aliases: ["Income Statement", "Profit and Loss Statement", "P&L", "Statement of Operations", "Statement of Profit or Loss", "Income Statements"]
prerequisites: ["[[accrual-accounting]]"]
related: ["[[balance-sheet]]", "[[cash-flow-statement]]", "[[financial-statement-analysis]]", "[[revenue]]", "[[gross-profit]]", "[[operating-income]]", "[[net-income]]", "[[earnings-per-share]]", "[[ebitda]]", "[[net-margin]]", "[[accrual-accounting]]", "[[depreciation]]"]
---

The **income statement** (also called the *profit and loss statement*, *P&L*, or *statement of operations*) is one of the three core financial statements. It reports how much a company earned and spent over a **period of time** — a quarter or a fiscal year — and walks from the top line ([[revenue]]) down to the bottom line ([[net-income]]). Where the [[balance-sheet]] is a point-in-time snapshot, the income statement is a *flow* covering an interval.

## What it captures

The income statement answers a single question: **"How profitable was the business over this period?"** It is built on [[accrual-accounting]], so revenue is recorded when it is *earned* and expenses when they are *incurred* — not when cash changes hands. This is why a profitable income statement does not guarantee positive cash flow, and why it must be read alongside the [[cash-flow-statement]].

## The profit waterfall

A multi-step income statement subtracts costs in tiers, exposing a different margin at each level:

```
Revenue (Net Sales)              ← the "top line"
  − Cost of Goods Sold (COGS)
  ───────────────────────────
  = Gross Profit                 → Gross Margin = Gross Profit / Revenue
  − Operating Expenses (SG&A, R&D, D&A)
  ───────────────────────────
  = Operating Income (EBIT)      → Operating Margin = EBIT / Revenue
  − Interest Expense
  ± Other Income / Expense
  ───────────────────────────
  = Pre-Tax Income (EBT)
  − Income Tax
  ───────────────────────────
  = Net Income                   ← the "bottom line"
  ÷ Shares Outstanding
  ───────────────────────────
  = Earnings Per Share (EPS)
```

Each subtotal supports its own analysis:

| Line | Reads as |
|------|----------|
| [[revenue]] | Demand, pricing power, unit growth |
| [[gross-profit]] | Production / delivery efficiency, pricing power |
| [[operating-income]] (EBIT) | Profitability of the core business, before financing and tax |
| [[ebitda]] | EBIT with [[depreciation]] & amortization added back (a cash-earnings proxy) |
| Pre-tax income | Profit after financing costs |
| [[net-income]] | What is legally attributable to shareholders |
| [[earnings-per-share]] | Net income per share — the headline number markets react to |

## How it connects to the other statements

- **To the [[balance-sheet]]:** Net income that is not paid out as [[dividends]] flows into **retained earnings**, raising shareholders' equity. The income statement therefore *feeds* the equity section of the balance sheet each period.
- **To the [[cash-flow-statement]]:** Net income is the *starting line* of the cash flow statement's operating section (under the indirect method). Non-cash income-statement items — [[depreciation]], amortization, [[share-based-compensation]] — are then added back to reconcile accrual profit to actual cash generated.

This linkage is the heart of the three-statement model: the income statement explains performance, the balance sheet records the resulting position, and the cash flow statement reconciles the two in cash terms (see [[financial-statement-analysis]]).

## GAAP vs. adjusted ("non-GAAP")

Companies frequently present a second, *adjusted* income statement that strips out items management deems non-recurring (restructuring charges, acquisition costs, sometimes [[share-based-compensation]]). Adjusted figures can aid comparability — or can flatter results by excluding genuinely recurring costs. A widening gap between GAAP and adjusted net income is a recognised red flag in [[financial-statement-analysis]].

## Limitations

- **Accrual, not cash.** Revenue can be booked before cash arrives (rising accounts receivable) and expenses recognised before they are paid. Persistent divergence between net income and operating cash flow is the basis of the **accruals anomaly**.
- **Management discretion.** Choices on [[depreciation]] schedules, revenue recognition timing, and reserve estimates shift reported profit between periods.
- **One-off items.** Asset sales, impairments, legal settlements, and tax effects can distort a single period; trend several years rather than reacting to one print.
- **No balance-sheet context.** A strong P&L says nothing about leverage or liquidity — pair it with the [[balance-sheet]].

## Worked example (hypothetical)

Consider **Acme Co.**, an entirely hypothetical company, for one fiscal year. All figures are illustrative round numbers:

| Line | Amount |
|------|--------|
| Revenue | $1,000 |
| − COGS | $600 |
| **= Gross Profit** | **$400** (40% gross margin) |
| − Operating expenses (SG&A + R&D + D&A) | $250 |
| **= Operating Income (EBIT)** | **$150** (15% operating margin) |
| − Interest expense | $20 |
| **= Pre-tax income** | **$130** |
| − Income tax (at 25%) | $32.50 |
| **= Net Income** | **$97.50** (9.75% net margin) |
| Shares outstanding | 100 |
| **= EPS** | **$0.975** |

If Acme pays $40 of [[dividends]], the remaining $57.50 is retained, lifting shareholders' equity on next period's [[balance-sheet]] by that amount. The $97.50 net income would also become the first line of Acme's [[cash-flow-statement]], where non-cash charges inside that $250 of operating expense (e.g. depreciation) get added back.

## Related

- [[balance-sheet]] — the point-in-time companion statement
- [[cash-flow-statement]] — reconciles net income to cash
- [[financial-statement-analysis]] — reading the three statements together
- [[revenue]] · [[gross-profit]] · [[operating-income]] · [[net-income]] — the waterfall subtotals
- [[earnings-per-share]] — net income on a per-share basis
- [[ebitda]] — earnings measure that adds back D&A
- [[accrual-accounting]] — the recognition basis behind the statement

## Sources

- IFRS IAS 1, *Presentation of Financial Statements*
- US GAAP ASC 220, *Income Statement — Reporting Comprehensive Income*
- IFRS 15 / US GAAP ASC 606, *Revenue from Contracts with Customers* (revenue recognition)
- Stephen Penman, *Financial Statement Analysis and Security Valuation*

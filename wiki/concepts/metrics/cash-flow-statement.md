---
title: "Cash Flow Statement"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, education, stocks]
domain: [fundamental-analysis, valuation]
difficulty: beginner
aliases: ["Cash Flow Statement", "Statement of Cash Flows", "Cash Flow", "CFS", "Statement of Cash Flow"]
prerequisites: ["[[accrual-accounting]]", "[[income-statement]]"]
related: ["[[income-statement]]", "[[balance-sheet]]", "[[financial-statement-analysis]]", "[[free-cash-flow]]", "[[net-income]]", "[[depreciation]]", "[[working-capital]]", "[[capex]]", "[[accrual-accounting]]", "[[share-based-compensation]]", "[[deferred-revenue]]", "[[dividends]]", "[[share-buybacks]]"]
---

The **cash flow statement** (formally the *statement of cash flows*) is one of the three core financial statements. It tracks the **actual cash** that moved into and out of a company over a period and reconciles the accrual-based [[net-income]] from the [[income-statement]] to the real change in the cash balance on the [[balance-sheet]]. Because cash is far harder to manipulate than accrual earnings, many investors treat it as the most trustworthy of the three statements.

## What it captures

The income statement is built on [[accrual-accounting]] — it records revenue when *earned* and expenses when *incurred*, regardless of cash timing. The cash flow statement strips that timing away and answers: **"Where did the cash actually come from, and where did it go?"** It is the bridge between accrual profit and the cash a business genuinely generates.

## The three sections

Cash flows are sorted into three buckets:

| Section | Captures | Examples |
|---------|----------|----------|
| **Operating activities (CFO)** | Cash from running the core business | Cash from customers, payments to suppliers and staff, taxes, interest |
| **Investing activities (CFI)** | Cash for long-term assets | [[capex]] (buying PP&E), acquisitions, purchases/sales of securities |
| **Financing activities (CFF)** | Cash from/to capital providers | Issuing or repaying debt, issuing stock, [[dividends]], [[share-buybacks]] |

The three sections sum to the **net change in cash** for the period, which ties exactly to the movement in the cash line of the [[balance-sheet]].

## Direct vs. indirect method

The **operating** section can be presented two ways:

- **Indirect method** (used by the vast majority of public companies): start with [[net-income]], then add back non-cash expenses (e.g. [[depreciation]], amortization, [[share-based-compensation]]) and adjust for changes in [[working-capital]] (receivables, inventory, payables, [[deferred-revenue]]).
- **Direct method:** list actual cash receipts and payments. More intuitive but rarely used because it is costlier to compile.

A simplified indirect-method operating section:

```
Net Income
  + Depreciation & Amortization      (non-cash expense, added back)
  + Share-Based Compensation         (non-cash expense, added back)
  − Increase in Accounts Receivable  (sales not yet collected in cash)
  + Increase in Accounts Payable     (expenses not yet paid in cash)
  + Increase in Deferred Revenue     (cash collected before earned)
  ───────────────────────────────────
  = Cash Flow from Operations (CFO)
```

## Free cash flow

The most important figure derived from the statement is **[[free-cash-flow]]**:

```
Free Cash Flow = Cash Flow from Operations − Capital Expenditures
```

FCF is the cash left after maintaining and growing the asset base — the cash genuinely available for [[dividends]], [[share-buybacks]], debt repayment, or reinvestment. It re-imposes the real cost of [[capex]] that [[ebitda]] hides.

## How it connects to the other statements

- **From the [[income-statement]]:** [[net-income]] is the first line of the indirect-method operating section.
- **To the [[balance-sheet]]:** the net change in cash updates the cash balance; [[capex]] increases PP&E; financing flows change debt and equity. Changes in balance-sheet [[working-capital]] accounts *drive* the operating-section adjustments.

This is why the three statements form a single articulated model: a change in any balance-sheet account between two periods shows up as a cash flow (see [[financial-statement-analysis]]).

## Why analysts prize it ("quality of earnings")

A recurring red flag is **net income rising while operating cash flow stagnates or falls** — often a sign that profit is being inflated by aggressive accruals (e.g. booking revenue faster than cash collection). Healthy companies generally show CFO consistently *exceeding* net income, because non-cash [[depreciation]] is added back. Comparing CFO to net income is a core earnings-quality check in [[financial-statement-analysis]].

## Limitations

- **Capex is lumpy.** A single year's [[free-cash-flow]] can be depressed by a large growth project that will pay off later; trend several years.
- **Classification choices.** Where interest, taxes, and certain items sit (operating vs. financing) varies under [[ifrs-vs-gaap|IFRS vs. US GAAP]], affecting reported CFO.
- **One-offs.** Working-capital swings, asset sales, and timing of payments can flatter or depress a single period's cash flow.
- **Stock-based comp add-back.** Adding back [[share-based-compensation]] inflates CFO even though it is a real cost to shareholders via dilution — a frequent point of debate.

## Worked example (hypothetical)

Continuing with **Acme Co.** (a hypothetical company) for one year, all figures illustrative:

| Line | Amount |
|------|--------|
| Net Income | $97.50 |
| + Depreciation & amortization | $40 |
| + Share-based compensation | $15 |
| − Increase in accounts receivable | −$10 |
| + Increase in accounts payable | $5 |
| **= Cash Flow from Operations (CFO)** | **$147.50** |
| − Capital expenditures | $50 |
| **= Free Cash Flow** | **$97.50** |
| Investing: capex | −$50 |
| Financing: dividends + buybacks | −$60 |
| **= Net change in cash** | **+$37.50** |

Note that Acme's CFO ($147.50) comfortably exceeds its net income ($97.50) — a healthy quality-of-earnings signal — and that the $37.50 net change in cash would raise the cash line on next period's [[balance-sheet]] by exactly that amount.

## Related

- [[income-statement]] — supplies the net income that starts the operating section
- [[balance-sheet]] — its cash line is reconciled by this statement
- [[free-cash-flow]] — the headline cash metric derived here
- [[financial-statement-analysis]] — reading the three statements together
- [[working-capital]] — its changes drive operating-section adjustments
- [[capex]] — subtracted to reach free cash flow
- [[depreciation]] · [[share-based-compensation]] — non-cash items added back

## Sources

- IFRS IAS 7, *Statement of Cash Flows*
- US GAAP ASC 230, *Statement of Cash Flows*
- Stephen Penman, *Financial Statement Analysis and Security Valuation*

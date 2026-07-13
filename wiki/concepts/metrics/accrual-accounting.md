---
title: "Accrual Accounting"
type: concept
created: 2026-04-13
updated: 2026-06-22
status: excellent
tags: [fundamental-analysis, valuation, education]
domain: [fundamental-analysis]
difficulty: intermediate
aliases: ["Accrual Basis", "Accrual-Basis Accounting", "Accruals"]
prerequisites: ["[[balance-sheet]]"]
related: ["[[balance-sheet]]", "[[income-statement]]", "[[cash-flow-statement]]", "[[gross-profit]]", "[[earnings-per-share]]", "[[earnings-quality]]", "[[free-cash-flow]]", "[[accruals-anomaly]]", "[[cash-conversion-cycle]]", "[[alfred-fundamental-analysis]]"]
---

**Accrual accounting** records revenue when it is *earned* and expenses when they are *incurred*, regardless of when cash actually changes hands. It is the standard, regulator-mandated accounting method for publicly listed companies (required under IFRS and US GAAP) and is the basis for the income statement and [[balance-sheet]] that fundamental analysts work from. Its mirror image is **cash-basis accounting**, which records transactions only when cash moves.

## Overview

The accrual principle rests on two conventions:

- **Revenue recognition** — revenue is booked when the performance obligation is satisfied (goods delivered, service rendered), even if the customer has not yet paid. The unpaid amount becomes an **account receivable** on the balance sheet.
- **Matching principle** — expenses are recognised in the same period as the revenue they helped generate, even if the cash outflow happens earlier or later. Unpaid costs become **accruals/payables**; cash paid in advance becomes a **prepayment** or deferred asset.

Accrual accounting therefore deliberately *decouples* reported profit from cash movement. The reconciling items — receivables, payables, inventory, depreciation, deferred revenue, provisions — are collectively called **accruals**, and they are exactly the difference between accrual-basis net income and cash-basis profit:

$$\text{Net Income} = \text{Operating Cash Flow} + \text{Total Accruals}$$

This identity is the analytical key: the more of reported profit that comes from accruals rather than cash, the more the earnings depend on management estimates and timing — and the lower their quality (see [[earnings-quality]]).

### Worked Example — Where Profit and Cash Diverge

A software company signs a \$1.2m three-year support contract and invoices the full amount on day one, but the customer pays nothing yet, and the company prepays \$300k of cloud costs that benefit all three years.

| Item | Accrual treatment (Year 1) | Cash treatment (Year 1) |
|---|---|---|
| Revenue | \$400k recognised (1 of 3 years earned); \$800k sits as **deferred revenue** | \$0 (no cash received) |
| Invoiced-but-unpaid | \$400k becomes an **account receivable** | n/a |
| Cloud cost | \$100k expensed (matched); \$200k a **prepaid asset** | \$300k cash out |
| Year-1 result | +\$300k accrual profit | −\$300k cash |

Same economic activity, opposite signs. The \$600k gap (\$300k profit vs −\$300k cash) is **accruals**. Over the full life of the contract the two converge — accruals always reverse — but in any single period the divergence is where both legitimate timing and outright manipulation live.

### Accrual vs Cash Accounting

| Aspect | Accrual | Cash |
|--------|---------|------|
| Revenue recognised | When earned (goods delivered / service performed) | When cash received |
| Expenses recognised | When incurred (matched to revenue) | When cash paid |
| Used by | Public companies, large businesses | Small businesses, personal finance |
| Regulatory status | Required by IFRS, US GAAP, ASX/SEC filers | Not accepted for listed companies |
| Strength | Matches economic activity to period | Cannot be gamed by timing recognition |
| Weakness | Recognition timing is a discretion that can be manipulated | Ignores obligations and earned-but-unpaid amounts |

## Trading Relevance

Accrual accounting creates a structural gap between **reported earnings** and **actual cash flow** — and that gap is one of the most reliable forensic signals in equity analysis.

- **Earnings quality.** A company can report rising [[earnings-per-share|EPS]] while operating cash flow stagnates or falls. When earnings are driven by accruals (growing receivables, capitalised costs, channel-stuffing) rather than cash, the earnings are *low quality* and tend to reverse — cash earnings persist into future periods far better than accrual earnings. This is why a [[cash-flow-statement|cash flow statement]] check is non-negotiable: "companies survive on cash flow" (Source: [[fred-sam-session-2024-01-02]]). See [[earnings-quality]].
- **The accrual ratio.** A standard quality screen is

$$\text{Accrual Ratio} = \frac{\text{Net Income} - \text{Operating Cash Flow}}{\text{Total Assets}}$$

  High positive accruals (net income far exceeding cash flow) flag aggressive recognition or working-capital build that often precedes earnings disappointments. *Worked example:* a firm reports \$500m net income but only \$200m operating cash flow on \$5,000m total assets → accrual ratio = (500 − 200) / 5,000 = **+6%**. A second firm reports \$300m net income on \$350m operating cash flow → ratio = (300 − 350) / 5,000 = **−1%**. The first firm's profit is mostly non-cash and statistically more likely to disappoint; the second's earnings are *backed by cash* and higher quality, even though its headline EPS is lower.
- **The accruals anomaly.** Sloan (1996) documented that firms with **high accruals systematically underperform** low-accrual firms over the following year — a tradeable market inefficiency where investors fail to discount the lower persistence of accrual-based earnings. A long-low-accrual / short-high-accrual portfolio historically earned an abnormal return, though the effect has decayed since publication and crowding. See [[accruals-anomaly]] for the full effect and its decay.
- **Manipulation red flag.** Most accounting frauds (Enron, WorldCom) operate by inflating accruals — recognising revenue early, capitalising operating costs, or deferring expenses. Persistent divergence between net income and cash flow is the single most cited warning sign, and underlies forensic scores such as the Beneish M-score and the Sloan accrual measure.

### Where Accruals Hide — A Checklist

| Signal | What to watch | Why it matters |
|---|---|---|
| Receivables growing faster than revenue | Days sales outstanding (DSO) rising | Revenue booked but not collected → channel stuffing risk |
| Inventory building faster than sales | Days inventory rising | Demand may be weaker than reported margins suggest |
| Capitalising vs expensing | Rising "capitalised software / development" | Costs moved off the income statement to flatter profit |
| Net income ≫ operating cash flow | Widening NI − OCF gap | The core accrual-ratio warning |
| One-off "non-recurring" gains | Frequency of "adjustments" | Recurring non-recurring items inflate adjusted earnings |

## Related

- [[balance-sheet]] — accruals create receivables, payables, prepayments, and deferred revenue
- [[income-statement]] / [[cash-flow-statement]] — the accrual report vs the cash reconciliation
- [[free-cash-flow]] — the cash-based counterpart used to validate accrual earnings
- [[earnings-quality]] — the broader assessment of how cash-backed reported earnings are
- [[accruals-anomaly]] — the tradeable market inefficiency arising from accrual mispricing
- [[cash-conversion-cycle]] — measures the cash-timing impact of operating accruals
- [[earnings-per-share]] — accrual-based; quality depends on cash backing
- [[alfred-fundamental-analysis]] — operating cash flow as validation of accrual-based earnings

## Sources

- Richard G. Sloan, "Do Stock Prices Fully Reflect Information in Accruals and Cash Flows About Future Earnings?", *The Accounting Review*, 71(3), 1996 — foundational accruals-anomaly paper
- IFRS Conceptual Framework for Financial Reporting (accrual basis) — IFRS Foundation
- FASB Statement of Financial Accounting Concepts No. 8 (recognition and measurement) — US GAAP basis
- [[fred-sam-session-2024-01-02]] — "Companies survive on cash flow"

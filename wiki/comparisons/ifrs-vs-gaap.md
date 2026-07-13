---
title: "IFRS vs. US GAAP"
type: comparison
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, education, stocks]
subjects: ["[[ifrs]]", "[[us-gaap]]"]
comparison_dimensions: [philosophy, inventory, asset-revaluation, development-costs, cash-flow-classification, comparability]
aliases: ["IFRS vs GAAP", "IFRS versus US GAAP", "GAAP vs IFRS", "IFRS vs. US GAAP"]
related: ["[[income-statement]]", "[[balance-sheet]]", "[[cash-flow-statement]]", "[[goodwill]]", "[[depreciation]]", "[[capex]]", "[[financial-statement-analysis]]", "[[accrual-accounting]]", "[[working-capital]]"]
---

**IFRS vs. US GAAP** compares the two dominant accounting frameworks used to prepare company financial statements. **IFRS** (International Financial Reporting Standards, set by the IASB) is used in over 140 countries — the EU, UK, Australia, Canada, and much of Asia. **US GAAP** (Generally Accepted Accounting Principles, set by the FASB) is required for US-listed domestic companies. Because the two standards report the *same* economic events differently, a stock investor comparing a US company with a foreign peer must understand where the numbers are not apples-to-apples.

## The core philosophical difference

The single most important distinction is one of approach:

- **US GAAP is rules-based.** It provides detailed, prescriptive rules and bright-line thresholds for specific situations. This improves consistency but can be gamed by structuring transactions to just clear a numerical line.
- **IFRS is principles-based.** It states broad principles and relies more on professional judgment to apply the underlying intent. This is more flexible and harder to game by technicality, but allows more variation between companies.

Most of the concrete differences below flow from this philosophical split.

## Key differences that affect reported numbers

| Dimension | US GAAP | IFRS | Why it matters |
|-----------|---------|------|----------------|
| **Inventory (LIFO)** | LIFO (last-in, first-out) **permitted** | LIFO **prohibited** | In inflation, LIFO lowers reported profit and taxes; a US firm using LIFO is not comparable to an IFRS peer on [[net-income]] or inventory value |
| **Inventory write-down reversals** | Once written down, **cannot** be reversed | Reversal **allowed** if value recovers | IFRS earnings can rebound from a prior write-down; GAAP cannot |
| **Asset revaluation (PP&E)** | Carried at historical cost less [[depreciation]] | May **revalue** PP&E and intangibles to fair value | IFRS [[balance-sheet]] asset values and equity can be higher |
| **Development costs (R&D)** | Generally **expensed** as incurred | Development costs **capitalised** if criteria met | IFRS can show higher near-term profit and an intangible asset where GAAP shows an expense |
| **Goodwill impairment** | One-step quantitative test (post-2017) | Test at cash-generating-unit level | Timing and size of [[goodwill]] write-downs can differ |
| **Cash-flow classification** | Interest paid/received and dividends = operating | More **flexibility** (interest/dividends may sit in operating, investing, or financing) | Reported operating cash flow on the [[cash-flow-statement]] is not directly comparable |
| **Component depreciation** | Permitted, less commonly required | **Required** — depreciate significant components separately | Affects the [[depreciation]] schedule and asset carrying values |

## Why it matters to a stock investor

- **Cross-border comparison is not apples-to-apples.** Two competitors — one reporting under US GAAP, one under IFRS — can show different margins, asset values, and cash flows for *identical* economics. Valuation multiples (P/E, EV/EBITDA, P/B) must be interpreted with the standard in mind.
- **LIFO is the classic gotcha.** A US industrial using LIFO understates inventory on the [[balance-sheet]] and (in inflation) understates profit versus an IFRS peer. Filings disclose a "LIFO reserve" to convert back to a comparable (FIFO) basis.
- **R&D-heavy companies look different.** Under IFRS, capitalised development costs boost near-term profit and create an asset; under GAAP the same spend is expensed, depressing current earnings. This skews tech, pharma, and engineering comparisons.
- **Cash-flow quality.** Because interest and dividend classification is flexible under IFRS, headline operating cash flow needs to be checked against the components before trusting a [[free-cash-flow]] comparison.

## How analysts handle it

- **Normalise before comparing.** Strip LIFO (add back the LIFO reserve), recharacterise capitalised development costs, and re-classify cash flows to a common basis when comparing a GAAP and an IFRS company.
- **Read the reconciliation.** Foreign private issuers historically reconciled to US GAAP; even without a formal reconciliation, the notes disclose the major policy differences.
- **Prefer cash and enterprise metrics.** Cash-based and enterprise-value measures are somewhat less sensitive to accounting-policy choices than accrual earnings, though not immune (see [[financial-statement-analysis]]).
- **Watch convergence — but don't assume it.** The FASB and IASB have converged several standards (notably revenue recognition under ASC 606 / IFRS 15, and leases), but core differences like LIFO and asset revaluation persist.

## Worked example (hypothetical)

Suppose **Acme Co.** (US GAAP) and **Beta Ltd.** (IFRS) are identical hypothetical manufacturers with the same sales, costs, and physical inventory in an inflationary year:

| Item | Acme (US GAAP, LIFO) | Beta (IFRS, FIFO) |
|------|----------------------|-------------------|
| Reported cost of goods sold | Higher (newest, costlier units) | Lower (oldest, cheaper units) |
| Reported [[net-income]] | **Lower** | **Higher** |
| Inventory on [[balance-sheet]] | **Lower** (old costs) | **Higher** (recent costs) |
| Development spend on a new product | Expensed → lower profit | Capitalised → higher profit + an asset |

Despite running economically identical businesses, Beta reports higher earnings and a larger asset base purely because of accounting policy. An investor who ranked the two on raw [[income-statement]] profit — without normalising for LIFO and capitalised development — would wrongly conclude Beta is the stronger operator.

## Related

- [[income-statement]] · [[balance-sheet]] · [[cash-flow-statement]] — the statements the two regimes shape
- [[goodwill]] — impairment testing differs between the standards
- [[depreciation]] — component depreciation and asset revaluation differ
- [[capex]] — capitalisation of development costs and PP&E differs by regime
- [[accrual-accounting]] — the shared foundation both regimes build on
- [[financial-statement-analysis]] — normalising across standards before comparing

## Sources

- IFRS Foundation, *International Financial Reporting Standards* (IASB)
- FASB *Accounting Standards Codification* (US GAAP)
- IFRS 15 / ASC 606, *Revenue from Contracts with Customers* (a converged standard)
- Stephen Penman, *Financial Statement Analysis and Security Valuation*

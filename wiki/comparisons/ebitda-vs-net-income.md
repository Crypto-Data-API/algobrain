---
title: "EBITDA vs Net Income"
type: comparison
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, stocks, education]
aliases: ["EBITDA vs net income", "EBITDA vs earnings", "operating earnings vs bottom line"]
subjects: ["[[ebitda]]", "[[net-income]]"]
comparison_dimensions: [definition, what-it-captures, what-it-ignores, manipulability, use-cases]
related: ["[[ebitda]]", "[[net-income]]", "[[operating-income]]", "[[free-cash-flow]]", "[[earnings-per-share]]", "[[ev-ebitda]]", "[[price-to-earnings-ratio]]", "[[financial-statement-analysis]]"]
---

**EBITDA** and **net income** are two of the most quoted profitability figures, and one of the most common questions ALFRED users ask is which to trust. The short answer: [[net-income|net income]] is the official GAAP bottom line that belongs to shareholders, while [[ebitda|EBITDA]] is a non-GAAP measure that strips out financing, taxes, and non-cash charges to approximate core operating performance. They answer different questions, and using the wrong one — or trusting EBITDA blindly — is a frequent valuation mistake.

## The Core Difference

Both start from the same revenue but stop at different points on the income statement. The bridge between them is exactly the set of items EBITDA adds back:

$$\text{EBITDA} = \text{Net Income} + \text{Interest} + \text{Taxes} + \text{Depreciation} + \text{Amortization}$$

Reading the income statement from the bottom up, EBITDA removes four layers that net income keeps in:

| Item added back to reach EBITDA | What it reflects | Why EBITDA strips it |
|---|---|---|
| **Taxes** | Jurisdiction / tax regime | Make cross-border firms comparable |
| **Interest** | Capital structure (debt load) | Compare leveraged vs. debt-free firms |
| **Depreciation** | Non-cash wear on tangible assets | Remove non-cash accounting allocation |
| **Amortization** | Non-cash write-down of intangibles | Remove non-cash accounting allocation |

So **EBITDA sits near the top** (operating output, capital-structure-neutral) and **net income sits at the very bottom** (what is actually left for shareholders after everything).

## Side-by-Side

| Dimension | EBITDA | Net Income |
|-----------|--------|------------|
| **Status** | Non-GAAP, company-defined | GAAP / IFRS, audited |
| **Captures** | Core operating performance, neutral to financing & tax | The true residual profit to shareholders |
| **Ignores** | Interest, taxes, depreciation, amortization, capex, working capital | Nothing GAAP recognises (but includes non-cash distortions) |
| **Affected by debt load?** | No (by design) | Yes — interest reduces it |
| **Affected by one-offs?** | Often adjusted away ("adjusted EBITDA") | Yes — impairments, gains, settlements all flow through |
| **Drives which metric?** | [[ev-ebitda|EV/EBITDA]] | [[earnings-per-share|EPS]], [[price-to-earnings-ratio|P/E]] |
| **Manipulability** | High — add-backs are discretionary | Lower — but still subject to accruals and estimates |
| **Best for** | Comparing operating businesses across capital structures / jurisdictions | Measuring actual returns to equity holders |

## Worked Example (illustrative round numbers)

A capital-intensive firm and an asset-light firm with identical EBITDA:

| | Capital-intensive (Telecom-like) | Asset-light (Software-like) |
|---|---|---|
| EBITDA | $300M | $300M |
| Depreciation & amortization | (180M) | (20M) |
| Interest (heavy debt) | (60M) | (5M) |
| Taxes | (15M) | (65M) |
| **Net income** | **$45M** | **$210M** |

Both look identical on EBITDA, but net income tells the real story: the capital-intensive firm's heavy [[debt-to-equity|debt]] and depreciation consume most of its operating output, leaving little for shareholders. **This is precisely why EBITDA flatters capital-heavy businesses** — it ignores the depreciation that represents real, recurring capex, and the interest that represents real cash leaving the building.

## When to Use Which

**Use EBITDA when:**
- Comparing operating performance across firms with different debt loads or tax jurisdictions
- Building [[ev-ebitda|EV/EBITDA]] multiples for M&A, LBO, or relative valuation
- Sizing debt capacity ("turns of EBITDA") in leveraged finance and credit covenants

**Use net income when:**
- Measuring what actually accrues to shareholders ([[earnings-per-share|EPS]], [[price-to-earnings-ratio|P/E]], dividends)
- Comparing the bottom-line profitability of similar firms within one country/sector
- Assessing whether a company is genuinely profitable, not just operationally cash-generative

**Trust neither alone — cross-check with [[free-cash-flow|free cash flow]].** The relationship *EBITDA − capex − Δworking capital − cash taxes − cash interest ≈ free cash flow* exposes the gap EBITDA hides. For an airline or telecom that gap is enormous; for asset-light software it is small.

## Common Pitfalls

1. **"Adjusted EBITDA" inflation.** Companies add back stock-based compensation, recurring "one-time" charges, and other costs to flatter the headline number. A widening gap between adjusted EBITDA and GAAP net income is a governance red flag (the WeWork "Community Adjusted EBITDA" case is the textbook example — see [[ebitda]]).
2. **Treating EBITDA as cash.** Warren Buffett's critique — *"Does management think the tooth fairy pays for capex?"* — captures the central flaw: EBITDA ignores the real cash cost of maintaining the asset base.
3. **Ignoring leverage.** Two firms with equal EBITDA can have wildly different net income and risk depending on debt; the [[interest-coverage-ratio]] and [[debt-to-equity]] reveal what EBITDA conceals.
4. **One-time items in net income.** A single asset sale or impairment can make net income jump or collapse for reasons unrelated to operations — which is partly why EBITDA exists.

## Related

- [[ebitda]] — full treatment of the operating measure
- [[net-income]] — the GAAP bottom line
- [[operating-income]] — EBIT, the rung between the two
- [[free-cash-flow]] — the "truth serum" that reconciles them
- [[ev-ebitda]] — valuation multiple built on EBITDA
- [[price-to-earnings-ratio]] — valuation multiple built on net income
- [[earnings-per-share]] — net income per share
- [[interest-coverage-ratio]], [[debt-to-equity]] — what EBITDA hides about leverage
- [[financial-statement-analysis]]

## Sources

- Berkshire Hathaway shareholder letters (Warren Buffett & Charlie Munger) — critique of EBITDA vs. real earnings
- SEC Regulation G — non-GAAP measure reconciliation rules (EBITDA vs. GAAP net income)
- Aswath Damodaran, *Investment Valuation* — earnings measures and their use in valuation
- General market knowledge; no additional specific wiki source ingested yet.

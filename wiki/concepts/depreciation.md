---
title: "Depreciation"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, valuation, accounting]
aliases: ["Depreciation", "Amortization", "Depreciation and Amortization", "D&A"]
related: ["[[ebitda]]", "[[free-cash-flow]]", "[[financial-statement-analysis]]", "[[earnings]]", "[[capex]]", "[[enterprise-value]]", "[[discounted-cash-flow]]", "[[accruals-anomaly]]"]
domain: [valuation, fundamental-analysis]
prerequisites: ["[[financial-statement-analysis]]"]
difficulty: intermediate
---

Depreciation is the accounting process of allocating the cost of a tangible long-lived asset (property, plant, equipment) over its useful life, recognising a portion of the cost as an expense each period rather than all at once when the asset is purchased. Its intangible-asset equivalent is **amortization**. Depreciation is a **non-cash expense**: it reduces reported [[earnings]] but involves no cash outflow in the period it is recorded, which is why it is added back when reconciling net income to operating cash flow and is the "D&A" in [[ebitda]].

## Overview

When a company buys a machine for \$1,000,000 with a 10-year useful life, accounting matching principles require the cost to be spread across the years the machine generates revenue, not expensed entirely in year one. Common methods:

- **Straight-line:** equal expense each year = (Cost − Salvage value) / Useful life. The \$1M machine with \$0 salvage and 10-year life depreciates \$100,000 per year.
- **Declining balance / double-declining:** accelerated — larger expense in early years, applying a fixed rate to the asset's remaining book value.
- **Units-of-production:** expense tied to actual usage (e.g. machine hours, miles).
- **Sum-of-the-years'-digits (SYD):** another accelerated method that weights early years more heavily via a declining fraction.

### Methods compared

| Method | Pattern of expense | Annual amount (formula) | Best fit |
|---|---|---|---|
| Straight-line | Even | (Cost − Salvage) / Life | Buildings, furniture, predictable wear |
| Double-declining balance | Front-loaded | 2 × (1/Life) × Beginning book value | Tech, vehicles — fast obsolescence |
| Units-of-production | Usage-driven | (Cost − Salvage) × (units used / total units) | Machinery, aircraft, mines |
| Sum-of-the-years'-digits | Front-loaded | (Cost − Salvage) × (remaining life / SYD) | Assets most productive when new |

### Worked example: straight-line vs. double-declining

Take the \$1,000,000 machine, \$0 salvage, 10-year life. Straight-line books \$100,000 every year. Double-declining applies a 20% rate (2 × 1/10) to the *remaining book value*:

| Year | Straight-line expense | DDB expense | DDB book value (end) |
|---|---|---|---|
| 1 | \$100,000 | \$200,000 | \$800,000 |
| 2 | \$100,000 | \$160,000 | \$640,000 |
| 3 | \$100,000 | \$128,000 | \$512,000 |
| 4 | \$100,000 | \$102,400 | \$409,600 |

Both methods expense the *same total* (\$1M) over the asset's life — only the *timing* differs. Accelerated methods report lower early-year earnings (and lower early taxes) but higher later-year earnings, which is why method choice matters for cross-company comparability.

Each period the accumulated depreciation reduces the asset's **carrying (book) value** on the balance sheet; the income statement shows the period's depreciation expense; and the cash-flow statement adds it back in the operating section because no cash left the business.

### Where it shows up on the three statements

| Statement | How depreciation appears | Effect |
|---|---|---|
| [[income-statement\|Income statement]] | Depreciation expense (in COGS or SG&A/operating) | Lowers operating income and net income |
| [[balance-sheet\|Balance sheet]] | Accumulated depreciation (contra-asset) | Reduces net PP&E / book value |
| [[cash-flow-statement\|Cash flow statement]] | Added back in operating activities | No effect on cash; reconciles NI to CFO |

A subtle but important point: a higher depreciation charge *reduces* reported earnings but *increases* operating cash flow via the tax shield (lower taxable income → lower cash taxes). This is why depreciation is central to both earnings-quality and cash-flow analysis.

A key distinction: depreciation is the periodic **expensing** of past capital outlays, whereas **[[capex]]** is the actual **cash spent** on new assets. Over a long horizon for a stable business the two converge, but in a given year they can differ sharply — a growing company's capex exceeds depreciation (it is building capacity), while a harvesting/declining business may have depreciation above capex (it is running down its asset base).

## Trading relevance

- **EBITDA and "earnings quality."** Because [[ebitda]] adds D&A back, it flatters capital-intensive businesses (telecoms, utilities, miners) that must continually reinvest. Analysts compare EBITDA to capex to see whether reported cash generation is real or merely deferred reinvestment. Treating depreciation as "not a real cost" is a classic valuation trap — those assets genuinely wear out.
- **Free cash flow.** [[free-cash-flow]] = operating cash flow − capex. Depreciation is added back in operating cash flow, then real capex is subtracted, so FCF captures the economic cost that EBITDA hides.
- **Earnings manipulation flag.** Management can inflate reported earnings by lengthening assumed useful lives or raising salvage values, lowering annual depreciation. Sudden changes in depreciation assumptions are a red flag in [[financial-statement-analysis]] and feed the [[accruals-anomaly]] — firms with high non-cash accruals tend to underperform.
- **Tax shield.** Depreciation reduces taxable income, creating a "depreciation tax shield" (depreciation × tax rate) that is a real cash benefit and a standard input in [[discounted-cash-flow]] valuation. Accelerated-depreciation and bonus-depreciation tax rules shift this benefit forward.

## How traders use depreciation

Depreciation is not traded directly, but it is a workhorse input in fundamental screens and a recurring source of edge:

- **Normalizing earnings across methods/regimes.** Two otherwise identical firms can report different earnings purely because one uses accelerated depreciation or assumes shorter useful lives. Analysts standardize (or switch to cash-based metrics) before comparing, especially across jurisdictions ([[ifrs-vs-gaap|IFRS vs. US GAAP]]).
- **Capex-vs-D&A as a growth tell.** Tracking the **capex ÷ depreciation ratio** over time: a ratio persistently above 1 signals genuine expansion; a drift below 1 can flag under-investment that will hurt future competitiveness — useful in [[financial-statement-analysis]] and in spotting "harvest mode" businesses.
- **Earnings-quality / accruals screening.** A sudden drop in the depreciation rate (longer assumed lives, higher salvage) that boosts EPS is a textbook red flag and a building block of the [[accruals-anomaly]] short leg. Conservative depreciation paired with strong cash flow is a positive-quality signal.
- **Adjusting EBITDA back to reality.** When a screen surfaces a "cheap on EV/[[ebitda|EBITDA]]" capital-intensive name, replacing the added-back D&A with maintenance capex (sometimes called "owner earnings") often reveals it is not cheap at all.
- **Sector lens.** Asset-heavy sectors (utilities, telecom, railroads, semiconductors, miners) carry large D&A relative to earnings, so EBITDA-based comparisons systematically flatter them versus asset-light software/services firms — a known cross-sector valuation trap.

## Common pitfalls

- **Treating D&A as "free."** EBITDA's add-back tempts traders to ignore reinvestment, but the assets genuinely wear out; over a cycle, depreciation approximates true maintenance cost.
- **Confusing depreciation with capex.** They diverge in any single year; only over a long horizon for a steady-state business do they converge.
- **Ignoring impairments.** A one-off [[asset-impairment|impairment]] is distinct from routine depreciation but lands in the same lines — analysts must separate recurring D&A from lumpy write-downs.
- **Cross-border comparability.** Differing useful-life conventions and revaluation rules under [[ifrs-vs-gaap|IFRS vs. GAAP]] make raw earnings comparisons misleading without normalization.

## Related

- [[ebitda]] — earnings measure that explicitly adds back depreciation
- [[free-cash-flow]] — the cash metric that re-imposes the real cost of reinvestment
- [[capex]] — the cash counterpart to the accounting depreciation expense
- [[financial-statement-analysis]] — where depreciation assumptions are scrutinised
- [[accruals-anomaly]] — the market mispricing linked to non-cash accruals
- [[income-statement]] — carries the period depreciation expense
- [[balance-sheet]] — carries accumulated depreciation as a contra-asset
- [[cash-flow-statement]] — where D&A is added back to net income
- [[discounted-cash-flow]] — uses the depreciation tax shield as an input
- [[ifrs-vs-gaap]] — accounting regimes that govern useful-life rules

## Sources

- Penman, S. *Financial Statement Analysis and Security Valuation.* McGraw-Hill.
- IFRS IAS 16 (Property, Plant and Equipment) and US GAAP ASC 360.
- Sloan, R. (1996). "Do Stock Prices Fully Reflect Information in Accruals and Cash Flows About Future Earnings?" *The Accounting Review.*

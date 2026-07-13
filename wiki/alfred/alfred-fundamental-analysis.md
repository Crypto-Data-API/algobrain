---
title: "Alfred Fundamental Analysis"
type: concept
created: 2026-04-09
updated: 2026-04-13
status: good
tags: [alfred, fundamental-analysis, valuation, education]
aliases: ["Alfred FA", "Alfred Fundamentals"]
domain: [fundamental-analysis, valuation]
difficulty: intermediate
related: ["[[alfred]]", "[[fundamental-analysis]]", "[[exchange-data-sources]]", "[[asx-limited]]", "[[sec]]"]
---

Alfred's fundamental analysis framework — the core financial metrics used to evaluate a company from its fiscal reports, with formulas, sourcing notes, and a worked example using Propel Funeral Partners (ASX: PFP) FY2023 annual report.

## Metric Reference

Every metric falls into one of three categories:

- **Provided** — read directly from the financial report
- **Calculated** — derived from provided numbers using a formula
- **External** — requires data outside the single report (e.g. share price, prior period data)

---

## Share Price & Valuation

### Share Price

- **Source**: External (market data on reporting date)
- **Notes**: Use the closing price on the fiscal year end date

### PE Ratio (Price-to-Earnings)

- **Formula**: `PE RATIO = SHARE PRICE / EPS`
- **Example**: 4.19 / 0.1612 = 25.99
- **Notes**: Can also calculate using EPS (Adjusted) for a cleaner comparison — e.g. 4.19 / 0.1770 = 23.67. Always note which EPS variant you used.

### DCF (Discounted Cash Flow)

- **Source**: Calculated externally (requires projecting future cash flows and choosing a discount rate)
- **Notes**: Not derivable from a single report. Requires assumptions about growth rate, discount rate, and terminal value. The gold standard of intrinsic valuation but highly sensitive to inputs. See [[fundamental-analysis]] for methodology.

---

## Dividends

### Dividend per Share

- **Source**: Provided in report
- **Notes**: Often reported in cents (e.g. "14 cents") — convert to dollars (0.14) for calculations

### Dividend Yield %

- **Formula**: `DIVIDEND YIELD % = (ANNUAL DIVIDEND PER SHARE / SHARE PRICE) * 100`
- **Example**: 0.14 / 4.19 * 100 = 3.34%

### Dividend Payout %

- **Source**: Provided (approximate) or calculated
- **Formula** (if calculating): `PAYOUT % = (DIVIDENDS PER SHARE / EPS) * 100`
- **Notes**: High payout ratios (>80%) mean less earnings retained for growth. Low payout ratios suggest room for dividend increases or reinvestment.

---

## Profitability & Returns

### Net Income

- **Source**: Provided in report
- **Notes**: Reported as "Net profit after tax" (NPAT) in Australian company reports. This is the bottom-line profit after all expenses, interest, and tax.

### ROE % (Return on Equity)

- **Formula**: `ROE % = (NET INCOME / SHAREHOLDERS EQUITY) * 100`
- **Example**: 19,010,000 / 253,333,000 * 100 = 7.5%
- **Notes**: Measures how efficiently the company generates profit from shareholders' investment. Higher is better. Compare within the same industry.

### ROA % (Return on Assets)

- **Formula**: `ROA % = (NET INCOME / TOTAL ASSETS) * 100`
- **Example**: 19,010,000 / 539,860,000 * 100 = 3.52%
- **Notes**: Measures how efficiently the company uses all assets (debt + equity funded) to generate profit.

### Shareholders Equity

- **Source**: Provided in report
- **Notes**: Reported as "Total equity" in company reports. Equals Total Assets minus Total Liabilities.

---

## Debt & Solvency

### Debt to Equity Ratio

- **Formula**: `DEBT TO EQUITY = TOTAL DEBT / SHAREHOLDERS EQUITY`
- **Example**: 173,475,000 / 253,333,000 = 0.68
- **Notes**: Below 1.0 means the company has more equity than debt. Above 2.0 is generally considered highly leveraged. Industry-dependent.

### Current Ratio

- **Formula**: `CURRENT RATIO = CURRENT ASSETS / CURRENT LIABILITIES`
- **Example**: 129,266,000 / 286,527,000 = 0.45
- **Notes**: Measures short-term liquidity. Below 1.0 means current liabilities exceed current assets — potential liquidity concern, but common in some industries.

### Quick Ratio

- **Formula**: `QUICK RATIO = (CURRENT ASSETS - INVENTORY) / CURRENT LIABILITIES`
- **Example**: (129,266,000 - 4,825,000) / 286,527,000 = 0.43
- **Notes**: Stricter liquidity test — excludes inventory which may not be quickly convertible to cash.

### Inventory

- **Source**: Provided in report (under "Inventories")

### Interest Expense

- **Source**: Provided in report
- **Notes**: May be reported as "Net interest expense" in company reports.

### Net Interest Cover Ratio

- **Formula**: `INTEREST COVER = EBIT / INTEREST EXPENSE`
- **Example**: 34,570,000 / 4,988,000 = 6.93
- **Notes**: How many times the company can cover its interest payments from operating earnings. Below 1.5 is dangerous. Above 3.0 is generally comfortable.

### Total Debt

- **Source**: Calculated from report
- **Notes**: This can be tricky. Sum all interest-bearing obligations: bank loans + lease liabilities + bonds + other borrowings. In the PFP example: bank loans 139,496,000 + lease liabilities 33,979,000 = 173,475,000. Not the same as Total Liabilities (which includes trade payables, provisions, etc.).

---

## Cash Flow

### Net Operating Cash Flow

- **Source**: Provided in report (cash flow statement)
- **Notes**: The actual cash generated from operations after working capital changes. More reliable than accounting profit because it's harder to manipulate.

### Gross Operating Cash Flow

- **Notes**: Not always explicitly stated in reports. The distinction between gross and net operating cash flow depends on what deductions the company includes. Check the cash flow statement structure.

### Cash + Equivalents

- **Source**: Provided in report (balance sheet)
- **Notes**: Liquid assets immediately available.

---

## Revenue & Margins

### Revenue

- **Source**: Provided in report (income statement, top line)

### COGS (Cost of Goods Sold)

- **Source**: Provided in report
- **Notes**: Direct costs attributable to producing goods/services sold.

### Gross Profit

- **Formula**: `GROSS PROFIT = REVENUE - COGS`
- **Source**: Usually provided directly

### Gross Profit % (Gross Margin)

- **Formula**: `GROSS MARGIN % = (GROSS PROFIT / REVENUE) * 100`
- **Example**: 118,084,000 / 168,512,000 * 100 = 70.10%
- **Notes**: High gross margins indicate pricing power or low direct costs.

### Operating Expense (inc COGS)

- **Source**: Provided or calculated — total expenses including COGS

### Operating Expense (exc COGS)

- **Formula**: `OPEX (exc COGS) = OPERATING EXPENSE (inc COGS) - COGS`
- **Notes**: Administrative, selling, and general expenses.

### Operating Margin %

- **Formula**: `OPERATING MARGIN % = (OPERATING INCOME / REVENUE) * 100`
- **Example**: 32,257,000 / 168,512,000 * 100 = 19.14%
- **Notes**: Shows what percentage of revenue remains after all operating costs.

---

## EBIT & EBITDA

### EBIT (Earnings Before Interest and Tax)

- **Source**: Provided in report or calculated
- **Formula** (if calculating): `EBIT = NET INCOME + INTEREST EXPENSE + TAX EXPENSE`

### EBITDA (Earnings Before Interest, Tax, Depreciation and Amortisation)

- **Source**: Provided in report or calculated
- **Formula** (if calculating): `EBITDA = EBIT + DEPRECIATION + AMORTISATION`

### EBIT Growth %

- **Formula**: `EBIT GROWTH % = ((EBIT CURRENT - EBIT PRIOR) / EBIT PRIOR) * 100`
- **Example**: (34,570,000 - 28,626,000) / 28,626,000 * 100 = 20.76%
- **Notes**: Requires prior period data. Measures operating earnings momentum.

### EBITDA Growth %

- **Formula**: Same structure as EBIT Growth, using EBITDA figures

---

## Earnings Per Share

### EPS (Basic)

- **Source**: Provided in report
- **Notes**: Often reported in cents — convert to dollars for PE calculations. PFP example: 16.12 cents = $0.1612.

### EPS (Adjusted)

- **Source**: Provided in report
- **Notes**: Excludes one-off items (restructuring, impairments, etc.) for a cleaner picture of ongoing earnings. PFP example: 17.70 cents.

### EPS TTM (Trailing Twelve Months)

- **Notes**: NOT possible from a single annual report alone. Requires summing the most recent four quarters. Must pull data from prior interim reports.

### EPS Forecast

- **Source**: External (analyst consensus estimates)
- **Notes**: Not in the company report. Available from broker research, Bloomberg, Refinitiv, or free sources like Yahoo Finance.

---

## Balance Sheet

### Total Assets

- **Source**: Provided in report
- **Formula**: `TOTAL ASSETS = CURRENT ASSETS + NON-CURRENT ASSETS`

### Current Assets

- **Source**: Provided in report
- **Notes**: Assets expected to be converted to cash within 12 months (cash, receivables, inventory, prepayments).

### Non-Current Assets

- **Source**: Provided in report
- **Notes**: Long-term assets (property, plant, equipment, intangibles, goodwill).

### Total Liabilities

- **Source**: Provided in report
- **Formula**: `TOTAL LIABILITIES = CURRENT LIABILITIES + NON-CURRENT LIABILITIES`
- **Notes**: Includes ALL obligations — not just debt. Trade payables, provisions, tax liabilities, lease liabilities, and borrowings.

### Current Liabilities

- **Source**: Provided in report
- **Notes**: Obligations due within 12 months.

### Non-Current Liabilities

- **Source**: Provided in report
- **Notes**: Long-term obligations (loans, bonds, long-term leases, provisions).

---

## Worked Example: Propel Funeral Partners (ASX: PFP) — FY2023

Source: [PFP 2023 Annual Report](https://investors.propelfuneralpartners.com.au/FormBuilder/_Resource/_module/ddcuvcykS0CWUrGSOhB0gw/file/PFP_2023_Annual_Report.pdf) (fiscal year ending June 2023).

| Metric | Value | Source | Notes |
|--------|-------|--------|-------|
| **Share Price** (30/06/2023) | $4.19 | Provided | Closing price on FY end date |
| **PE Ratio** | 25.99 | Calculated | 4.19 / 0.1612 = 25.99. Using Adjusted EPS: 4.19 / 0.1770 = 23.67 |
| **Dividend per Share** | $0.14 | Provided | Reported as 14 cents |
| **Dividend Yield %** | 3.34% | Calculated | 0.14 / 4.19 * 100 |
| **Dividend Payout %** | ~79% | Provided | Approximate |
| **Net Income** | $19,010,000 | Provided | "Net profit after tax" |
| **Shareholders Equity** | $253,333,000 | Provided | "Total equity" |
| **ROE %** | 7.50% | Calculated | 19,010,000 / 253,333,000 |
| **ROA %** | 3.52% | Calculated | 19,010,000 / 539,860,000 |
| **Debt to Equity** | 0.68 | Calculated | 173,475,000 / 253,333,000 |
| **Current Ratio** | 0.45 | Calculated | 129,266,000 / 286,527,000 |
| **Inventory** | $4,825,000 | Provided | "Inventories" |
| **Quick Ratio** | 0.43 | Calculated | (129,266,000 - 4,825,000) / 286,527,000 |
| **Interest Expense** | $4,988,000 | Provided | "Net interest expense" |
| **Interest Cover** | 6.93x | Calculated | 34,570,000 / 4,988,000 |
| **Net Op Cash Flow** | $32,257,000 | Provided | Cash flow statement |
| **Operating Margin %** | 19.14% | Calculated | 32,257,000 / 168,512,000 |
| **Revenue** | $168,512,000 | Provided | |
| **Gross Profit** | $118,084,000 | Provided | |
| **Gross Margin %** | 70.10% | Provided | |
| **EBIT** | $34,570,000 | Provided | |
| **EBITDA** | $45,958,000 | Provided | |
| **EBIT Growth %** | 20.76% | Calculated | (34,570 - 28,626) / 28,626 * 100 |
| **EPS** | 16.12c | Provided | |
| **EPS (Adjusted)** | 17.70c | Provided | |
| **EPS TTM** | N/A | — | Requires prior interim reports |
| **Total Assets** | $539,860,000 | Provided | |
| **Current Assets** | $129,266,000 | Provided | |
| **Non-Current Assets** | $410,594,000 | Provided | |
| **Total Liabilities** | $286,527,000 | Provided | Current + non-current |
| **Current Liabilities** | $117,114,000 | Provided | |
| **Non-Current Liabilities** | $169,413,000 | Provided | |
| **Total Debt** | $173,475,000 | Calculated | Bank loans 139,496 + lease liabilities 33,979 |

## Fred's Verbal Benchmarks

Specific numerical thresholds [[fred-mcnaught|Fred McNaught]] applies when evaluating stocks, extracted from his recorded analysis sessions. These supplement the quantitative formulas above with Fred's qualitative judgement on what "good" and "bad" look like in practice.

### From NST (Northern Star) Analysis — April 2024

| Metric | Value | Fred's Assessment |
|--------|-------|------------------|
| PE ratio | 24.2 | **Red flag** — too high for a commodity stock. Stock is "fully priced" |
| ROE | 7% | **Red flag** — below acceptable threshold |
| D/E ratio | 15.6 | "Low as it should be for a commodity stock" — acceptable |
| Current ratio | 2.8 | "Fine" — adequate liquidity |
| Quick ratio | 1.8 | Acceptable |
| EBITDA margin (5yr avg) | 27.6% | "Excellent" — strong operational performance |
| Dividend yield (5yr avg) | 1.8% | Noted but not decisive on its own |

(Source: [[fred-sam-session-2024-04-25]])

### General Benchmarks

- **EPS growth + dividend growth** → share price will "soon follow" (Source: [[fred-sam-session-2024-01-10]])
- **ROE** should be evaluated against the cash rate — if ROE doesn't significantly exceed what you could earn in a bank deposit, the management isn't earning a sufficient return on your equity (Source: [[fred-sam-session-2024-01-02]])
- **PE above sector average** implies greater risk but also higher potential reward — becomes a risk-reward analysis (Source: [[fred-sam-session-2024-01-10]])
- **Low PE is not always attractive** — may signal a value trap or structural decline (Source: [[fred-sam-session-2024-01-02]])
- **[[gmroi|GMROI]]**: Stock Turn x Gross Profit % > 100 indicates adequate inventory return for retail businesses (Source: [[fred-sam-session-2024-02-09]], [[fred-sam-session-2024-10-18]])
- **Gross profit** is "the oxygen of any business" — always assess this metric (Source: [[fred-sam-session-2024-01-19]], [[fred-gross-profit-article]])
- **"Fully priced"** = upside depends on external factors (commodity price, macro) you can't control, not the company's own fundamentals improving (Source: [[fred-sam-session-2024-04-25]])

See [[alfred-investment-philosophy]] for Fred's complete decision framework and [[alfred-case-studies]] for worked examples.

## Key Gotchas

1. **EPS in cents vs dollars** — Australian reports typically state EPS in cents. Always convert to dollars before calculating PE ratio.
2. **Total Debt vs Total Liabilities** — Total Debt is interest-bearing obligations only (loans, bonds, leases). Total Liabilities includes everything (payables, provisions, tax). Don't confuse them.
3. **"Net profit after tax" = Net Income** — Australian terminology differs from US GAAP.
4. **"Total equity" = Shareholders Equity** — Same concept, different label.
5. **EPS TTM requires multiple reports** — A single annual report only gives you annual EPS, not trailing twelve months from the current date.
6. **EPS Forecast is external** — Never in the company report. Analyst consensus only.
7. **Gross vs Net Operating Cash Flow** — Not all reports separate these clearly. Check the cash flow statement structure.
8. **Total Debt calculation** — May require summing multiple line items (bank loans + lease liabilities + bonds). Read the notes to financial statements carefully.
9. **Current Ratio below 1.0** — Not automatically bad. Some industries (funeral services, retail) consistently operate below 1.0 due to business model characteristics.

## Data Sources

For official reporting data access:
- **ASX-listed companies**: See [[exchange-data-sources#Australia — ASX]]
- **US-listed companies**: See [[exchange-data-sources#USA — SEC / EDGAR]]

## Related

- [[alfred]] — Alfred AI assistant overview
- [[fundamental-analysis]] — Broader fundamental analysis concepts
- [[exchange-data-sources]] — Official exchange data endpoints
- [[asx-limited]] — ASX reporting obligations and listing requirements
- [[sec]] — SEC/EDGAR filing system for US companies

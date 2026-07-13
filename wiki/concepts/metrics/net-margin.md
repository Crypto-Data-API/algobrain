---
title: "Net Profit Margin"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, indicators]
aliases: ["Net Margin", "net margin", "net profit margin", "net-profit-margin", "Net Profit Margin", "bottom-line margin", "profit margin"]
domain: [fundamental-analysis]
prerequisites: ["[[net-income]]", "[[revenue]]", "[[operating-margin]]"]
difficulty: beginner
related: ["[[gross-margin]]", "[[operating-margin]]", "[[net-income]]", "[[earnings-per-share]]", "[[return-on-equity]]", "[[fundamental-analysis]]"]
---

**Net profit margin** (often just "net margin" or "profit margin") is the percentage of revenue that survives all the way down the income statement to become bottom-line profit, after every cost has been subtracted: cost of goods sold, operating expenses, interest, taxes, and one-off items. It is the most complete single-number measure of how profitable a company ultimately is, and it sits at the bottom of the margin "waterfall" below [[gross-margin]] and [[operating-margin]].

## Formula

$$\text{Net Profit Margin} = \frac{\text{Net Income}}{\text{Revenue}} \times 100\%$$

[[net-income|Net income]] is the final "bottom line" of the income statement — what remains after COGS, SG&A, R&D, depreciation, interest expense, and taxes. [[revenue|Revenue]] ("the top line") is total sales before any deductions. Both figures come directly from the income statement, so net margin is one of the easiest ratios to compute.

## The Margin Waterfall

Net margin is the last stop in a sequence of progressively stricter profitability measures:

| Margin | Numerator | What it subtracts from revenue |
|---|---|---|
| [[gross-margin\|Gross margin]] | Gross profit | Direct cost of goods sold only |
| [[operating-margin\|Operating margin]] | Operating income (EBIT) | + operating expenses (SG&A, R&D, D&A) |
| **Net margin** | Net income | + interest, taxes, and non-operating items |

The gap between operating margin and net margin reveals the drag from **financing and taxes**. A heavily indebted company can post a healthy operating margin but a thin net margin because interest expense eats the difference. A one-time tax benefit, asset sale, or litigation charge can also push net margin temporarily away from the operating trend — which is why analysts often prefer operating margin for judging the *core* business and reserve net margin for the all-in result.

## Worked Example

A company reports, for the year:

- Revenue: $500 million
- Net income: $40 million

$$\text{Net Profit Margin} = \frac{40}{500} \times 100\% = 8\%$$

So 8 cents of every sales dollar ends up as profit for shareholders. If a competitor with the same $500m in revenue earns $60m of net income, its 12% net margin signals either better cost control, lower leverage, pricing power, or a more favourable tax position.

## Typical Ranges by Industry

Net margins vary enormously across sectors, so comparisons are only meaningful within an industry:

- **Software / SaaS, high-end pharma**: 20–35%+ (scalable, asset-light, pricing power)
- **Branded consumer / luxury**: 10–20%
- **Industrials, mature tech hardware**: 5–12%
- **Retail and distribution**: 2–6% (high volume, thin margins)
- **Grocery and supermarkets**: 1–3%
- **Airlines and commodity producers**: highly cyclical, frequently negative in downturns

A broad-market average net margin sits in the high single digits to low double digits, but the dispersion is wide.

## Interpretation

- **Expanding net margin** signals operating leverage, deleveraging, falling tax rates, or a more profitable sales mix — often a precursor to upward [[earnings-per-share|EPS]] revisions.
- **Contracting net margin** while revenue grows can mean discounting, cost inflation, or rising interest expense — a classic warning that growth is being "bought."
- **Watch the trend over many quarters.** A single quarter can be distorted by a tax settlement, impairment, or gain on sale; the multi-year trajectory is the signal.

## Role in DuPont Analysis

Net margin is the profitability leg of the DuPont decomposition of [[return-on-equity]]:

$$\text{ROE} = \text{Net Margin} \times \text{Asset Turnover} \times \text{Equity Multiplier}$$

This breaks ROE into *how much profit per sale*, *how efficiently assets generate sales*, and *how much leverage is applied*. Two firms with identical ROE can have very different risk profiles depending on whether fat margins or heavy leverage is doing the work.

## Limitations

1. **Distorted by one-off items.** Asset sales, impairments, restructuring charges, and tax events can swing net income without reflecting the ongoing business. Many analysts look at *adjusted* or *normalized* net margin alongside the GAAP figure.
2. **Sensitive to capital structure and tax.** Two operationally identical firms can show different net margins purely because one carries more debt or operates in a higher-tax jurisdiction — which is why [[operating-margin]] and [[ebitda|EBITDA]] margins are preferred for cross-company comparison.
3. **Meaningless for banks and insurers.** For financials, interest is a revenue/cost-of-business line rather than financing, so headline net margin figures are accounting artifacts; use [[return-on-equity|ROE]], [[return-on-assets|ROA]], and price-to-[[tangible-book-value]] instead.
4. **Says nothing about capital intensity.** A 10% net margin business that needs enormous assets to operate may create less value than a 6% margin, capital-light one — cross-check with [[return-on-invested-capital|ROIC]].

## Trading Relevance

Net margin is a core input to quality and profitability screens in [[fundamental-analysis]]: persistently high and stable net margins are a fingerprint of pricing power and a durable competitive moat. Because it is the most "all-in" margin, it ties most directly to the [[earnings-per-share|EPS]] that drives the headline [[price-to-earnings-ratio|P/E]] multiple. Margin-expansion stories — a company crossing into sustained profitability or deleveraging — are among the more reliable multi-quarter long setups, while margin compression amid still-growing revenue is a textbook caution flag. Sharp jumps in net margin should always be checked against [[operating-margin]] and [[free-cash-flow]] to confirm the improvement is operational and cash-backed rather than a one-time accounting gain.

## Related

- [[gross-margin]]
- [[operating-margin]]
- [[net-income]]
- [[earnings-per-share]]
- [[return-on-equity]]
- [[fundamental-analysis]]

## Sources

- Penman, Stephen H. *Financial Statement Analysis and Security Valuation* (McGraw-Hill) — profitability ratios and the DuPont decomposition.
- CFA Institute, *Financial Reporting and Analysis* curriculum — margin analysis.
- Damodaran, Aswath. Net-margin datasets by industry, NYU Stern (pages.stern.nyu.edu/~adamodar).

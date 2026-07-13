---
title: "Current Ratio"
type: concept
created: 2026-04-10
updated: 2026-06-22
status: excellent
tags: [fundamental-analysis, liquidity, valuation]
aliases: ["current ratio", "working capital ratio", "Working Capital Ratio"]
domain: [fundamental-analysis]
difficulty: beginner
prerequisites: ["[[balance-sheet]]"]
related: ["[[quick-ratio]]", "[[debt-to-equity]]", "[[balance-sheet]]", "[[working-capital]]", "[[cash-conversion-cycle]]", "[[free-cash-flow]]", "[[altman-z-score]]", "[[financial-statement-analysis]]"]
---

The **current ratio** is the most basic measure of short-term [[liquidity]] — a company's ability to meet obligations coming due within the next 12 months using the assets it expects to convert to cash within the same window. It is sometimes called the **working capital ratio**.

## Formula

$$\text{Current Ratio} = \frac{\text{Current Assets}}{\text{Current Liabilities}}$$

**Current assets** include cash, marketable securities, accounts receivable, inventory, and prepaid expenses. **Current liabilities** include accounts payable, short-term debt, the current portion of long-term debt, accrued expenses, and deferred revenue. Both figures come directly from the [[balance-sheet]]. (Current assets − current liabilities is [[working-capital]], the dollar version of the same idea.)

## Worked Example (illustrative round numbers)

A retailer's [[balance-sheet]]:

| Current assets | $ | Current liabilities | $ |
|----------------|---|---------------------|---|
| Cash | 40M | Accounts payable | 120M |
| Accounts receivable | 60M | Short-term debt | 40M |
| Inventory | 150M | Accrued expenses | 40M |
| Prepaid expenses | 10M | | |
| **Total** | **260M** | **Total** | **200M** |

| Ratio | Calculation | Result |
|-------|-------------|--------|
| Current ratio | 260 / 200 | **1.30×** |
| [[working-capital]] | 260 − 200 | **$60M** |
| [[quick-ratio]] (strip inventory & prepaids) | (260 − 150 − 10) / 200 | **0.50×** |

The current ratio of 1.30× looks "adequate," but the [[quick-ratio]] of 0.50× reveals the firm relies heavily on selling inventory to cover near-term bills — a crucial nuance the headline ratio hides. This is exactly why the two should always be read together.

## Interpretation

The current ratio answers the question: *if every short-term bill came due tomorrow, could the company pay it from assets on hand?*

- **> 2.0** — conservative, often held by cash-rich software and pharma firms
- **1.5 – 2.0** — healthy cushion for most industries
- **1.0 – 1.5** — adequate but worth monitoring
- **< 1.0** — a potential red flag; the firm may need to refinance, draw down credit lines, or raise capital to meet obligations

A rising current ratio generally signals improving liquidity, but an unusually high value can also indicate inefficient use of capital — cash sitting idle or inventory piling up unsold.

## Trading Relevance

The current ratio is a first-pass solvency screen used in distress detection and credit analysis. A ratio sliding below 1.0 and falling is a leading indicator of refinancing risk — the firm may be forced to raise equity (dilution), draw credit lines, or sell assets, all of which pressure the share price. Distress models such as the [[altman-z-score|Altman Z-score]] lean on working-capital-to-assets, a close cousin of the current ratio. Conversely, screening for *deteriorating* current ratios alongside rising [[debt-to-equity]] is a classic short-candidate filter. Because it is a single-day [[balance-sheet]] snapshot, it is most useful as a *trend* across several quarters and is best read together with the [[cash-conversion-cycle]] (which adds timing) and [[free-cash-flow]] (which shows whether the business actually generates the cash the ratio implies).

### How Investors and Traders Use It

- **Distress / bankruptcy screens** — a sub-1.0 and falling ratio flags firms that may breach covenants or need emergency financing; it is an input to the [[altman-z-score]].
- **Credit and lending decisions** — lenders set minimum current-ratio covenants; a breach can trigger default even if the company is still operating.
- **Quality filters for long investors** — a comfortable but not bloated ratio (≈1.5–2.5 in most sectors) signals a firm that can self-fund through a downturn.
- **Trend over level** — analysts watch the multi-quarter trajectory and the gap to the [[quick-ratio]] far more than any single absolute reading.

## Typical Ranges by Industry

- **Software**: often 2.0 – 4.0 (large deferred-revenue balances and cash hoards)
- **Pharma / biotech**: 3.0+ (R&D runways)
- **Manufacturers**: 1.5 – 2.5
- **Retail**: 1.0 – 1.5 (fast inventory turnover compensates)
- **Grocery / restaurants**: often < 1.0 — they sell inventory for cash before paying suppliers, so a low ratio is structural, not distressed

## Limitations

1. **Inventory quality** — the current ratio treats a pallet of slow-moving unsold goods the same as cash. The [[quick-ratio]] refines this by stripping inventory out.
2. **Receivables quality** — aging, uncollectible, or concentrated receivables may never convert to cash on schedule.
3. **Snapshot in time** — the ratio can be window-dressed at quarter-end by paying down short-term debt or delaying payables.
4. **Ignores timing** — "within 12 months" lumps together obligations due next week and next November. The [[cash-conversion-cycle]] provides a more dynamic view.
5. **Ignores access to credit** — a firm with a $1B undrawn revolver has liquidity the ratio cannot see.

Always interpret alongside the [[quick-ratio]], [[free-cash-flow]], and working-capital trends.

## Related

- [[quick-ratio]] — the same idea with inventory stripped out
- [[debt-to-equity]] — longer-term solvency complement
- [[balance-sheet]] — source of all inputs
- [[working-capital]] — the dollar version (current assets − current liabilities)
- [[cash-conversion-cycle]] — dynamic working-capital timing view
- [[free-cash-flow]] — cash actually generated
- [[altman-z-score]] — distress model built on working-capital ratios
- [[financial-statement-analysis]]

## Sources

- CFA Institute, *Financial Statement Analysis* curriculum — liquidity ratio definitions and limitations
- Edward I. Altman, "Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy", *Journal of Finance*, 1968 — working-capital ratios in distress prediction
- Aswath Damodaran, *Investment Valuation* — liquidity and solvency analysis
- General market knowledge; no additional specific wiki source ingested yet.

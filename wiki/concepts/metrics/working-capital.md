---
title: "Working Capital"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [fundamental-analysis, liquidity, valuation]
aliases: ["working capital", "net working capital", "NWC", "change in working capital"]
domain: [fundamental-analysis]
difficulty: beginner
prerequisites: ["[[balance-sheet]]"]
related: ["[[current-ratio]]", "[[quick-ratio]]", "[[cash-conversion-cycle]]", "[[free-cash-flow]]", "[[balance-sheet]]", "[[cash-flow-statement]]", "[[ebitda]]", "[[financial-statement-analysis]]"]
---

**Working capital** is the cash a company has tied up in running its day-to-day operations — the difference between the short-term assets it owns and the short-term bills it owes. It is the dollar-amount cousin of the [[current-ratio]] and a direct measure of operational liquidity: positive working capital means a firm can fund its near-term obligations from assets already on hand, while negative working capital means it relies on suppliers, customers, or financing to bridge the gap.

## Formula

$$\text{Working Capital} = \text{Current Assets} - \text{Current Liabilities}$$

**Current assets** include cash, marketable securities, accounts receivable, inventory, and prepaid expenses. **Current liabilities** include accounts payable, short-term debt, the current portion of long-term debt, accrued expenses, and deferred revenue. All inputs come from the [[balance-sheet]].

A narrower, more operationally focused version strips out cash and short-term debt to isolate the capital absorbed by the operating cycle:

$$\text{Operating Working Capital} = \text{(Receivables} + \text{Inventory)} - \text{Payables}$$

The period-over-period **change in working capital (ΔWC)** is what flows through the cash-flow statement and reduces or boosts [[free-cash-flow]]: growing working capital consumes cash; shrinking it releases cash.

## Worked Example (illustrative round numbers)

A manufacturer's [[balance-sheet]]:

| Current assets | $ | Current liabilities | $ |
|----------------|---|---------------------|---|
| Cash | 50M | Accounts payable | 110M |
| Accounts receivable | 90M | Short-term debt | 40M |
| Inventory | 130M | Accrued expenses | 50M |
| **Total** | **270M** | **Total** | **200M** |

| Metric | Calculation | Result |
|--------|-------------|--------|
| Working capital | 270 − 200 | **$70M** |
| [[current-ratio]] | 270 / 200 | **1.35×** |
| Operating working capital | (90 + 130) − 110 | **$110M** |

If, a year later, the firm grows and inventory plus receivables climb by $30M while payables rise only $10M, working capital expands by $20M — meaning $20M of cash was *consumed* by growth and subtracted from that year's [[free-cash-flow]], even if reported profit rose.

## Interpretation

Working capital is best read as *how much cash the operating cycle locks up* and *which way it is trending*:

- **Positive and stable** — the firm self-funds its operating cycle; typical of most manufacturers and retailers.
- **Negative by design** — some businesses collect from customers before paying suppliers (grocery chains, subscription software with deferred revenue, large platform retailers). Here negative working capital is a *strength* — suppliers and customers finance the business for free.
- **Rising faster than revenue** — a warning sign: cash is being trapped in unsold inventory or uncollected receivables, a common precursor to a cash crunch even amid growing sales.
- **Falling sharply** — can signal improving efficiency, or distress (stretching payables, liquidating inventory to raise cash).

Because growth *consumes* working capital, fast-growing firms often look profitable on the income statement while generating little or negative cash — one of the most common reasons a growing company runs out of money.

## Typical Patterns by Business Model

- **Heavy-inventory manufacturers / industrials**: large positive working capital; cash tied up in raw materials and finished goods.
- **Grocery / discount retail**: near-zero or negative — fast [[stock-turn|inventory turnover]] and slow supplier payment.
- **Subscription software**: often negative — customers prepay (deferred revenue) before costs are incurred.
- **Construction / long-cycle projects**: large and volatile, driven by milestone billing and work-in-progress.

## Limitations

1. **Snapshot in time.** Like all [[balance-sheet]] figures it is a single-day reading and can be window-dressed at quarter-end.
2. **More is not better.** A bloated working-capital balance often signals *inefficiency* — idle cash, slow-moving inventory, or lax collections — not strength. The goal is usually to minimise working capital while staying solvent.
3. **Ignores timing within the cycle.** Two firms with identical working capital can have very different cash dynamics; the [[cash-conversion-cycle]] adds the missing time dimension.
4. **Quality of components matters.** Aging receivables and obsolete inventory inflate working capital without representing recoverable cash.

Read working capital alongside the [[current-ratio]] and [[quick-ratio]] (the ratio versions), the [[cash-conversion-cycle]] (timing), and [[free-cash-flow]] (whether the business actually converts profit to cash).

## Trading Relevance

Working-capital dynamics are a key bridge between reported earnings and actual cash, and the **change in working capital** is a line item that quant value and quality screens watch closely. A widening gap between rising profits and stagnant or negative operating cash flow — driven by ballooning receivables or inventory — is a well-known earnings-quality red flag and short-candidate signal, because it often precedes write-downs or a liquidity squeeze. Conversely, a management team that structurally reduces working capital (negotiating better supplier terms, tightening collections) permanently boosts [[free-cash-flow]] and per-share value. In merger and LBO analysis, the **normalized working-capital level** is a heavily negotiated deal term, since the buyer must fund the operating cycle from day one.

## Related

- [[current-ratio]] — the ratio form of the same idea (current assets ÷ current liabilities)
- [[quick-ratio]] — stricter liquidity measure stripping inventory
- [[cash-conversion-cycle]] — adds timing: days to convert working capital into cash
- [[free-cash-flow]] — change in working capital directly affects FCF
- [[balance-sheet]] — source of all inputs
- [[cash-flow-statement]] — where the change in working capital flows through
- [[ebitda]] — ignores working-capital swings, a key gap vs. cash flow
- [[financial-statement-analysis]]

## Sources

- CFA Institute, *Financial Statement Analysis* curriculum — working capital and liquidity management
- Aswath Damodaran, *Investment Valuation* — change in working capital in free-cash-flow estimation
- General market knowledge; no additional specific wiki source ingested yet.

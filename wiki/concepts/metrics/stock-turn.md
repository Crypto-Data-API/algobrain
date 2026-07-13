---
title: "Stock Turn"
type: concept
created: 2026-04-13
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, indicators]
aliases: ["Inventory Turnover", "Inventory Turns", "Stock Turnover"]
domain: [fundamental-analysis]
difficulty: intermediate
related: ["[[gmroi]]", "[[gross-profit]]", "[[retail-metrics]]", "[[fundamental-analysis]]", "[[valuation]]", "[[gross-margin]]", "[[inventory-turnover]]", "[[revenue-growth]]"]
---

Stock turn ([[inventory-turnover]]) measures the number of times a company's inventory is sold and replaced over a 12-month period. It is calculated as cost of goods sold divided by average inventory. Fred McNaught uses a benchmark rule for retail businesses: **Stock Turn x Gross Profit must exceed 100** for the business to be considered efficient. This metric is one of Fred's key [[retail-metrics]] and works in conjunction with [[gmroi]] to assess whether a retailer is managing its inventory effectively relative to the margin it earns.

## Calculation

The standard formula is:

**Stock Turn = Cost of Goods Sold (COGS) / Average Inventory**

Average inventory is typically (Beginning Inventory + Ending Inventory) / 2, though some analysts use a 12-month average for more precision. An alternative formulation uses Revenue instead of COGS in the numerator, which produces a slightly higher number since revenue includes the gross margin. The COGS-based version is more theoretically correct because both numerator and denominator are at cost, but the revenue-based version is sometimes used when COGS is not separately reported.

A closely related, more intuitive expression is **Days Sales of Inventory (DSI)**, the average number of days a unit sits on the shelf before it sells:

```
DSI = 365 / Stock Turn        (equivalently, Avg Inventory / COGS × 365)
```

### Worked example

Suppose a retailer reports COGS of **$120M** for the year, with beginning inventory of **$18M** and ending inventory of **$22M**:

- Average inventory = ($18M + $22M) / 2 = **$20M**
- Stock turn = $120M / $20M = **6.0x** — the firm cycles its entire inventory six times a year.
- DSI = 365 / 6.0 ≈ **61 days** — on average a product sits 61 days before sale.

If the same firm earns a 40% [[gross-margin|gross profit margin]], Fred's screen gives **6.0 × 40 = 240**, comfortably above 100 — an efficient operation. A luxury retailer turning 1.5x at a 60% margin scores 1.5 × 60 = 90, *failing* the screen despite the fatter margin.

## Interpretation by Industry

Stock turn varies enormously by industry, making cross-sector comparisons meaningless. The metric is only useful when compared against direct competitors or historical trends within the same business:

| Industry | Typical Stock Turn | Why |
|---|---|---|
| Grocery / Supermarkets | 12-15x | Perishable goods force rapid turnover |
| Fast Fashion | 8-12x | Quick product cycles, low cost inventory |
| General Retail | 4-8x | Seasonal inventory, moderate shelf life |
| Luxury Goods | 1-3x | High-value, slow-moving inventory by design |
| Heavy Equipment | 1-3x | Expensive, long sales cycles |
| Pharmaceuticals | 3-6x | Regulated inventory, expiration dates |

A rising stock turn over time generally signals improving operational efficiency -- the company is selling through inventory faster with less capital tied up. A declining stock turn may indicate overstocking, obsolescence risk, or weakening demand. However, an extremely high stock turn can also indicate the company is under-stocked and potentially losing sales.

## Fred's "Stock Turn x Gross Profit > 100" Rule

Fred McNaught teaches that neither stock turn nor [[gross-profit|gross profit margin]] should be evaluated in isolation for retail businesses. A retailer with a 50% gross margin but a stock turn of only 1.5x (product = 75) is not generating enough return on its inventory investment. Conversely, a grocery retailer with a 20% margin but 8x stock turn (product = 160) is very efficient despite the low margin. The "greater than 100" threshold is a quick screen that identifies businesses where the combination of margin and inventory velocity is sufficient to generate attractive returns on capital. This product is closely related to [[gmroi]] (Gross Margin Return on Inventory Investment), which formalizes the same insight.

## Use in Fundamental Analysis

For [[fundamental-analysis]] and [[valuation]] purposes, stock turn helps assess management quality and working capital efficiency. Analysts look for: consistent or improving stock turn relative to peers, alignment between stock turn trends and [[revenue-growth|revenue growth]] (growing revenue with stable or improving turn is positive; growing revenue with deteriorating turn suggests the growth may be driven by inventory stuffing), and the relationship between stock turn and days sales of inventory (DSI = 365 / Stock Turn), which expresses the same concept in a more intuitive time-based format.

### Stock turn in the cash conversion cycle

Stock turn is one leg of working-capital efficiency. Faster turns mean less cash is locked in unsold goods, shortening the **cash conversion cycle** (CCC = DSI + days sales outstanding − days payable outstanding). A retailer that turns inventory quickly and pays suppliers slowly can run on negative working capital — effectively financing growth with suppliers' money. This is why high stock turn is prized by traders assessing self-funding compounders versus capital-hungry retailers.

## Pitfalls

- **Cross-industry comparison is meaningless.** A 2x turn is disastrous for a grocer and excellent for a heavy-equipment dealer. Only compare against direct peers and the company's own history.
- **Revenue-based vs. COGS-based.** Using revenue in the numerator inflates the ratio by the gross margin; never mix the two methods when comparing firms.
- **Seasonality.** A single year-end inventory snapshot can badly misstate turns for seasonal retailers; use a multi-quarter average where possible.
- **Too high can be bad.** An unusually high turn may signal under-stocking, stock-outs, and lost sales rather than efficiency.
- **Obsolescence hidden in averages.** Slow-moving or obsolete SKUs can be masked by fast-moving ones; aggregate turn hides the tail of dead stock that may need write-downs.
- **Margin blindness.** Turn alone ignores profitability — which is exactly why Fred pairs it with [[gross-margin|gross profit]] and why [[gmroi]] exists.

## Related

- [[gmroi]] — Gross Margin Return on Inventory Investment, the related profitability metric
- [[gross-profit]] — the margin component of Fred's efficiency formula
- [[gross-margin]] — the margin percentage used in the "x Gross Profit > 100" screen
- [[inventory-turnover]] — the standard finance term for stock turn
- [[retail-metrics]] — the broader set of retail analysis metrics
- [[revenue-growth]] — turn trends should be read alongside top-line growth
- [[fundamental-analysis]] — the discipline that uses stock turn for company evaluation
- [[valuation]] — how inventory efficiency feeds into company worth

## Sources

- [[fred-share-investing-guide]] — Fred McNaught's "Stock Turn x Gross Profit > 100" retail efficiency rule.
- CFA Institute, *Financial Statement Analysis* curriculum — activity ratios and inventory turnover.
- Investopedia, "Inventory Turnover Ratio" — COGS- vs. revenue-based formulas and days-sales-of-inventory.

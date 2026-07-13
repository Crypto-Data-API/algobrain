---
title: "Retail Metrics"
type: concept
created: 2026-04-13
updated: 2026-06-22
status: excellent
tags: [fundamental-analysis, valuation, indicators]
aliases: ["Retail KPIs", "Retail Operating Metrics"]
domain: [fundamental-analysis]
prerequisites: ["[[fundamental-analysis]]", "[[gross-profit]]"]
difficulty: intermediate
related: ["[[gmroi]]", "[[stock-turn]]", "[[gross-margin]]", "[[gross-profit]]", "[[fundamental-analysis]]", "[[valuation]]"]
---

Retail metrics are operating indicators tailored to evaluating retail businesses, where inventory management and margin efficiency — not headline earnings — are the decisive drivers of value creation. Because retailers convert capital into inventory and back into cash on a fast cycle, the key questions are how *quickly* stock sells and how *much margin* each turn earns, which is why retail analysis leans on velocity-and-margin ratios rather than earnings multiples alone.

## Core Efficiency Metrics

The three metrics at the centre of retail analysis combine margin and inventory velocity:

- **[[gmroi|GMROI]] (Gross Margin Return on Investment)** = Gross Margin $ / Average Inventory Cost. Answers "for every dollar of inventory, how many dollars of gross margin?" A GMROI above 1 means the inventory is generating more gross margin than it costs to hold.
- **[[stock-turn]] (inventory turnover)** = COGS / Average Inventory. The number of times inventory is sold and replaced per year. High turn means less capital tied up and lower obsolescence risk.
- **[[gross-margin]]** = Gross Profit / Revenue. The slice of each sales dollar left after the cost of the goods themselves.

### Fred's "Stock Turn × Gross Profit > 100" rule

Fred McNaught teaches that neither metric should be read in isolation for a retailer: **Stock Turn × Gross Profit % must exceed 100** for the business to be considered operationally efficient (Source: [[fred-share-investing-guide]]). A boutique with a 50% margin but only 1.5× turn scores 75 (inefficient); a grocer with a 20% margin but 8× turn scores 160 (very efficient despite the thin margin). The threshold is a quick screen that fuses margin and velocity into the same insight that [[gmroi|GMROI]] formalizes.

#### Worked example — applying the rule across business models

| Retailer type | Gross margin | [[stock-turn\|Stock turn]] | Turn × Margin | Verdict |
|---|---|---|---|---|
| Luxury boutique | 60% | 1.2× | 72 | Below 100 — slow velocity drags it down despite fat margins |
| Specialty apparel | 45% | 2.5× | 112.5 | Just over the line — healthy |
| Discount variety | 30% | 4× | 120 | Efficient |
| Supermarket / grocer | 22% | 8× | 176 | Very efficient — thin margin redeemed by high velocity |
| Warehouse club | 13% | 12× | 156 | Razor-thin margin, but turn is so high the model works |

The lesson the rule encodes: **margin and velocity are substitutes.** A grocer earning 22 cents on the dollar but selling its shelves eight times a year out-earns the capital tied in a boutique making 60 cents but turning stock barely once. This is exactly why a retailer cannot be judged on [[gross-margin]] alone, and why cross-format comparison (boutique vs. grocer) is meaningless — they sit at opposite ends of the same trade-off curve. The rule is the back-of-envelope version of [[gmroi|GMROI]], which expresses the same idea as dollars of margin per dollar of inventory.

## Additional Retail KPIs

| Metric | What it measures |
|---|---|
| [[same-store-sales\|Same-store sales]] (comp sales) | Sales growth from stores open ≥12 months, stripping out new-store expansion |
| Sales per square metre / foot | Productivity of the physical footprint |
| Basket size (average transaction value) | Spend per transaction |
| Foot traffic / conversion rate | Visitors and the share who buy |
| Sell-through rate | Units sold ÷ units received over a period (markdown risk indicator) |
| Shrinkage | Inventory lost to theft, damage, or error |
| Days sales of inventory (DSI) | 365 / stock turn — the same velocity in days (the DIO leg of the [[cash-conversion-cycle\|CCC]]) |

Comparable-store sales is the metric the market watches most closely, because total-sales growth can be manufactured simply by opening stores; comps isolate whether the existing fleet is healthy.

### Decomposing comparable-store sales

Comp sales themselves break into two drivers, and *which* one is growing matters enormously:

$$\text{Comp sales growth} \approx \text{traffic (transactions)} \times \text{average ticket}$$

- **Traffic-driven comps** (more transactions) are higher quality — genuine demand pulling more customers through the door or to the site.
- **Ticket-driven comps** (higher average spend) can be healthy (premium mix-shift) *or* a warning sign when the rise is just **price inflation** masking *falling unit volumes*. In an inflationary period a retailer can post "+5% comps" while actually selling *fewer* items.

**Worked example.** A chain reports +6% comparable-store sales. Decomposed: transactions −2%, average ticket +8%. Stripping out ~7% selling-price inflation, *real* unit demand is *negative* — the headline comp is flattered by price, not strength. A competitor posting +3% comps split as +4% traffic / −1% ticket is the healthier business despite the lower headline. This is why analysts always ask for the **traffic vs. ticket** split (and units vs. price) behind a comp number.

When a retailer **strips out new-store expansion**, the comp base also excludes a noisy contributor: a fleet growing total revenue +15% while comps are *flat* is buying growth by opening stores, not improving the existing ones — a classic late-cycle tell that the core fleet has stalled.

## Trading Relevance

For an investor screening ASX retailers such as Woolworths, Wesfarmers, or JB Hi-Fi, operating KPIs reveal competitive positioning that earnings multiples miss. Decelerating comp sales, falling GMROI, or a deteriorating stock turn alongside "growing" revenue often signals inventory stuffing or markdown pressure before it shows up in reported earnings. Conversely, a retailer steadily lifting GMROI and comps while holding margin is compounding value efficiently. These metrics only carry meaning *relative to direct peers or the company's own history* — cross-sector comparison (a supermarket vs. a luxury house) is meaningless because their business models target opposite ends of the margin/velocity spectrum.

### What traders watch around earnings

- **The comp number vs. consensus** — comparable-store sales is the single most-watched line; a small miss or beat versus guidance can move the stock more than the EPS headline.
- **The traffic/ticket and units/price split** — the *quality* of a comp beat (real volume vs. price inflation) often determines whether the market believes it.
- **Inventory vs. sales growth** — inventory growing *faster* than sales is a leading red flag: markdowns and gross-margin compression are coming. Read this through [[stock-turn]] and the DIO leg of the [[cash-conversion-cycle|CCC]].
- **Gross margin + comps together** — comps up but gross margin down means the growth was *bought* with discounts; both up together is genuine pricing power.
- **Guidance and forward commentary** — retail is highly seasonal and weather/holiday-sensitive; management's forward comp guidance and inventory-position commentary often drive the move more than the reported quarter.
- **The Stock Turn × Gross Profit screen** — a fast first filter to rank peers by operational efficiency before deeper [[fundamental-analysis]].

## Common pitfalls

- **Reading metrics in isolation** — margin without velocity (or vice versa) misleads; that is the whole point of GMROI and Fred's Turn × Margin rule.
- **Cross-sector comparison** — comparing a grocer's stock turn to a luxury boutique's is meaningless; only direct peers and own-history comparisons inform.
- **Total sales vs. comps confusion** — revenue growth from opening stores can mask a stalling core fleet; always isolate [[same-store-sales|comps]].
- **Inflation-flattered comps** — a positive comp can hide *falling* unit volumes when prices are rising; demand for the unit/volume split.
- **Definition inconsistency** — companies vary in how they define a "comparable" store (≥12 vs. ≥13 months, treatment of remodels, e-commerce inclusion); compare like-for-like definitions across periods and peers.
- **Ignoring channel mix** — blending online and physical comps can obscure a declining store base propped up by e-commerce, or vice versa.

## Related

- [[gmroi]]
- [[stock-turn]]
- [[inventory-turnover]]
- [[same-store-sales]]
- [[cash-conversion-cycle]]
- [[gross-margin]]
- [[gross-profit]]
- [[fundamental-analysis]]
- [[valuation]]

## Sources

- [[fred-share-investing-guide]] — Fred McNaught's retail metrics and the "Stock Turn × Gross Profit > 100" rule.
- Levy, M. & Weitz, B., *Retailing Management* — GMROI, sell-through, and retail KPI definitions.
- Investopedia, "Same-Store Sales," "GMROI," and "Inventory Turnover" — standard definitions.

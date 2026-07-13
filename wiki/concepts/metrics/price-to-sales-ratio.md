---
title: "Price-to-Sales Ratio"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [fundamental-analysis, valuation]
aliases: ["P/S", "P/S ratio", "PSR", "price-to-sales", "price to sales"]
domain: [fundamental-analysis, valuation]
prerequisites: ["[[revenue]]"]
difficulty: beginner
related: ["[[price-to-earnings-ratio]]", "[[price-to-book-ratio]]", "[[peg-ratio]]", "[[financial-statement-analysis]]", "[[fundamental-analysis]]"]
---

The **Price-to-Sales ratio** (P/S, or PSR) compares a company's market capitalization to its annual revenue. Because revenue is harder to manipulate than earnings and exists even for unprofitable firms, P/S is the valuation metric of choice for early-stage, turnaround, and high-growth companies where [[price-to-earnings-ratio|P/E]] is meaningless or negative.

## Formula

```
P/S = Market Capitalization / Trailing 12-Month Revenue

Equivalently:
P/S = Stock Price / Sales Per Share
```

For a cleaner apples-to-apples version that accounts for debt, analysts sometimes use **EV/Sales** = Enterprise Value / Revenue instead.

## Origin and Popularization

**Kenneth Fisher** popularized P/S in *Super Stocks* (1984), arguing that earnings were too volatile to rely on for cyclical or growth companies, while revenue remained a stable measure of business size. Fisher's original rules targeted PSRs below 0.75 for industrial stocks and below 1.5 for mature companies, though these thresholds have not held up as markets have re-rated higher over decades.

## Typical Ranges

| Business Type | Typical P/S |
|---|---|
| Grocery, distribution, low-margin retail | 0.1 – 0.5 |
| Mature industrials, autos | 0.5 – 1.5 |
| S&P 500 average | 2 – 3 |
| Consumer brands | 2 – 5 |
| Software / SaaS | 5 – 15 |
| Hyper-growth tech | 20 – 40+ |

A reading below 1.0 is classically cheap but only meaningful once margin structure is considered — a 2% net margin business at 1x sales is 50x earnings, while a 20% margin business at 1x sales is 5x earnings.

## Why P/S Works for Unprofitable Companies

A pre-profit biotech or early-stage SaaS company has negative earnings, so P/E is undefined. Revenue, however, still exists and still grows. P/S lets you track valuation through the "J-curve" of a company investing heavily to scale. It is central to how venture and growth investors value private rounds, often paired with revenue growth rate.

## The Critical Limitation: Margins Are Invisible

P/S treats a dollar of revenue from a 50%-margin software company identically to a dollar from a money-losing razor-thin delivery service. **Two companies with the same P/S can have wildly different intrinsic values.** A company growing revenue 40% while losing more money each quarter looks no different on P/S from a profitable 40% grower — but one is a rocket ship and the other is a cash incinerator.

## The Rule of 40

For SaaS specifically, analysts pair P/S with the **Rule of 40**: a healthy software company should have Revenue Growth Rate + Operating Margin ≥ 40%. This partially compensates for P/S's margin-blindness by forcing growth-profitability tradeoffs into the analysis.

## Trading Relevance

P/S is the dominant valuation lens for the part of the market where [[price-to-earnings-ratio|P/E]] is undefined — pre-profit tech, biotech, and turnarounds — which makes it the key gauge for **growth-stock excess and mean reversion**. Historically extreme P/S readings have flagged tops: in 2000–2001 and again in 2021–2022, baskets of software names at 20–40x sales subsequently de-rated by 60–80% as the multiple, not the business, collapsed. Trading uses:

- **Relative-value within a sector**: rank peers on EV/Sales (debt-adjusted) and trade the spread between the cheapest and richest, controlling for growth and margin so you are not just shorting the fastest grower.
- **Mean-reversion / froth signals**: a sector's median P/S far above its own history is a regime warning for [[market-regime]] positioning, not a precise timing tool.
- **Pairing**: always overlay margin (Rule of 40 for SaaS) or [[peg-ratio|PEG]] context, because P/S is blind to whether each revenue dollar is profitable.

## Related

- [[price-to-earnings-ratio]], [[price-to-book-ratio]]
- [[fundamental-analysis]], [[financial-statement-analysis]]

## Sources

- Fisher, Kenneth L. *Super Stocks* (Dow Jones-Irwin, 1984) — origin and popularisation of the price-to-sales ratio.
- O'Shaughnessy, James P. *What Works on Wall Street* (McGraw-Hill) — backtests showing low P/S as a value factor.
- Damodaran, Aswath. *Investment Valuation* (Wiley) — revenue multiples and EV/Sales.

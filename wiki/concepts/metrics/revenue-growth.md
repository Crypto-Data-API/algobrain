---
title: "Revenue Growth"
type: concept
created: 2026-04-13
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, valuation, indicators]
aliases: ["Sales Growth", "Top-Line Growth", "Revenue Growth Rate"]
domain: [fundamental-analysis]
prerequisites: ["[[revenue]]"]
difficulty: beginner
related: ["[[revenue]]", "[[earnings-per-share]]", "[[gross-profit]]", "[[fundamental-analysis]]", "[[valuation]]", "[[price-to-earnings]]", "[[cagr]]", "[[gross-margin]]", "[[free-cash-flow]]"]
---

Revenue growth is the rate at which a company's top-line sales are increasing (or decreasing) over a given period, typically expressed as a year-over-year (YoY) or quarter-over-quarter (QoQ) percentage. Because [[revenue]] sits above every cost line on the income statement and is harder to manipulate than earnings, its trajectory is one of the earliest and most reliable signals of a business's underlying health.

## Formula

$$\text{Revenue Growth} = \frac{\text{Revenue}_{\text{current}} - \text{Revenue}_{\text{prior}}}{\text{Revenue}_{\text{prior}}} \times 100\%$$

For multi-year trends, the compound annual growth rate ([[cagr|CAGR]]) smooths quarterly noise:

$$\text{Revenue CAGR} = \left( \frac{\text{Revenue}_{\text{end}}}{\text{Revenue}_{\text{begin}}} \right)^{1/n} - 1$$

where *n* is the number of years. A 3–5 year CAGR gives a clearer picture of the durable growth trajectory than any single period.

### The growth measures compared

| Measure | Formula sketch | Best for | Watch out for |
|---|---|---|---|
| YoY (year-over-year) | (this quarter vs same quarter last year) | Removing seasonality | One-off comps, calendar shifts |
| QoQ (quarter-over-quarter) | (this quarter vs prior quarter) | Spotting turns early | Heavily distorted by seasonality |
| Sequential annualised | QoQ × 4 (roughly) | Fast-moving SaaS | Overreacts to a single strong quarter |
| [[cagr|CAGR]] (multi-year) | (End/Begin)^(1/n) − 1 | Durable trajectory | Hides the *shape* of the path (lumpy vs smooth) |
| TTM (trailing twelve months) | sum of last 4 quarters | Smoothing reported noise | Lags genuine inflection points |

### Worked example

Suppose a company grows revenue from **$100M** to **$260M** over four years:

- Year-by-year: $100M → $150M → $195M → $230M → $260M.
- Latest YoY = ($260M − $230M) / $230M = **13.0%** — and decelerating from the ~50% it printed in year one.
- Four-year [[cagr|CAGR]] = (260 / 100)^(1/4) − 1 = (2.60)^0.25 − 1 ≈ **27.0%**.

The single-period YoY (13%) and the multi-year CAGR (27%) tell very different stories — which is precisely why analysts look at both. The smooth 27% CAGR hides a sharp deceleration that the latest YoY exposes (see *Growth Deceleration as a Signal* below).

## Types of Growth

Analysts distinguish carefully between the sources of top-line growth:

- **Organic growth** — increases from existing operations: new customers, higher prices, or greater volume. This is the purest measure of business health.
- **Acquired (inorganic) growth** — top-line added through M&A. It can flatter headline numbers without reflecting operational improvement, and often comes with integration risk and dilution.
- **Constant-currency growth** — strips out FX translation effects, which can materially distort reported revenue for multinationals.

## Growth Deceleration as a Signal

A subtle but powerful signal in [[fundamental-analysis]] is *deceleration* — revenue still growing, but at a slowing rate. A company decelerating from 40% to 30% to 20% YoY may look healthy on the surface, yet the declining second derivative frequently triggers **multiple compression** as the market reprices forward expectations downward. This matters most for high-growth technology and SaaS names where [[price-to-earnings|P/E]] and price-to-sales multiples are dominated by forward growth assumptions.

The **"Rule of 40"** in SaaS investing captures the growth/profitability tradeoff: revenue growth % + profit (or [[free-cash-flow|FCF]]) margin % should exceed 40%. It encodes that the market will tolerate low margins from a fast grower, or modest growth from a profitable one, but not weakness on both.

| Profile | Rev growth | Margin | Rule-of-40 score | Read |
|---|---|---|---|---|
| Hyper-growth, burning cash | 60% | −15% | 45 | Passes — growth justifies the burn |
| Balanced compounder | 25% | 20% | 45 | Passes — the ideal mix |
| Mature, profitable | 8% | 35% | 43 | Passes — quality over speed |
| Stalling, still burning | 12% | −10% | 2 | **Fails** — weak on both, prime de-rating candidate |

## The Growth-vs-Margin Tradeoff

Top-line growth is only valuable if it does not destroy unit economics. The crucial pairing is revenue growth against [[gross-margin|gross margin]] and operating margin:

- **Profitable growth** — revenue rising while margins hold or expand. This is operating leverage and the most rewarded combination.
- **"Growth at any cost"** — revenue rising only because the firm is discounting, over-spending on customer acquisition, or buying revenue via M&A. Margins compress, and the market eventually punishes it.
- **Quality of revenue** — recurring/subscription revenue with high retention is worth a far higher multiple than one-off, project, or low-margin pass-through revenue, even at the same growth rate.

A trader's quick test: is incremental revenue dropping through to incremental [[gross-profit]] and [[free-cash-flow]], or is it being competed away? Decomposing growth into **price × volume × mix** answers whether growth is durable (pricing power, volume gains) or fragile (one-off mix or FX effects).

## Trading Relevance

Revenue reversal is a classic sell signal. When a company's revenue flips from growth to decline, it often marks the start of fundamental deterioration well before earnings collapse — Fred McNaught cites the IRI case study, where the stock fell from roughly $6 to 38 cents after revenue growth reversed (Source: [[fred-share-investing-guide]]). Because revenue is harder to manipulate than earnings (which can be flattered by reserve releases, capitalized costs, or one-offs), a reversing top line is treated as an early-warning indicator. For growth investors, revenue *acceleration* — paired with stable or expanding [[gross-profit|margins]] — is the bullish counterpart; growth at the cost of collapsing margins is "growth at any cost" and rarely rewarded.

## Pitfalls

- **Easy comps / hard comps.** A big YoY number may just reflect a weak prior-year base (e.g. a COVID trough); the next year's "hard comp" can make a healthy business look stalled.
- **Inorganic flattery.** Acquisitions inflate headline growth without operational improvement. Always isolate organic growth.
- **FX masking.** Constant-currency growth can differ sharply from reported growth for multinationals; a strong dollar can hide real underlying expansion (or vice versa).
- **Channel stuffing / pull-forward.** Booking shipments ahead of demand or discounting to pull sales into the quarter borrows from the future; watch for matching rises in receivables or inventory (see [[stock-turn]]).
- **Mix shift.** Growth driven by a low-margin product line can lift revenue while lowering [[gross-margin]] — top-line up, profit quality down.
- **Vanity for unprofitable firms.** Revenue growth with no path to [[free-cash-flow]] is not value creation; the Rule of 40 exists precisely to discipline this.

## Related

- [[revenue]]
- [[cagr]] — the smoothed multi-year growth measure
- [[gross-margin]] — the margin half of the growth/margin tradeoff
- [[gross-profit]]
- [[free-cash-flow]] — where durable growth ultimately shows up
- [[earnings-per-share]]
- [[fundamental-analysis]]
- [[valuation]]
- [[price-to-earnings]]

## Sources

- [[fred-share-investing-guide]] — revenue reversal as a sell signal; IRI case study.
- CFA Institute, *Equity Valuation* curriculum — growth analysis and multiple compression.
- Investopedia, "Revenue Growth Rate" and "Rule of 40" — definitions and SaaS application.

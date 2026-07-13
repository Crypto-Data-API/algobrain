---
title: "Owner Earnings"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, stocks]
aliases: ["Owner Earnings", "Owner's Earnings", "Buffett Owner Earnings"]
domain: [fundamental-analysis, valuation]
prerequisites: ["[[free-cash-flow]]", "[[intrinsic-value]]"]
difficulty: intermediate
related: ["[[free-cash-flow]]", "[[intrinsic-value]]", "[[discounted-cash-flow]]", "[[warren-buffett]]", "[[cash-flow-statement]]", "[[net-income]]", "[[valuation]]", "[[margin-of-safety]]"]
---

**Owner earnings** is a measure of the true cash a business generates for its owners, defined by [[warren-buffett|Warren Buffett]] in his 1986 Berkshire Hathaway shareholder letter as a more honest alternative to reported accounting earnings. The idea is to start from net income, add back non-cash charges, and then subtract the capital spending the business genuinely *needs* to maintain its competitive position and unit volume. Buffett argued this figure — not GAAP net income, and not crude cash flow — is "the relevant item for valuation purposes" and the number that should be discounted to estimate [[intrinsic-value|intrinsic value]].

## The formula

Buffett's definition, paraphrased from the 1986 letter:

```
Owner Earnings = Net Income
               + Depreciation, amortisation & other non-cash charges
               - Maintenance capital expenditure ("required capex")
               - Increase in net working capital
```

The crucial and difficult term is **maintenance capex** — the portion of total capital expenditure required just to sustain current operations and competitive position, as opposed to **growth capex** that expands the business. Buffett's insight is that ordinary cash-flow measures either ignore capex entirely (overstating cash) or subtract *all* capex including growth investment (understating the cash a steady-state business throws off). Owner earnings deliberately deducts only the maintenance portion.

### Relationship to other measures

| Measure | Capex treatment | Tends to... |
|---|---|---|
| [[net-income\|Net income]] (GAAP) | None deducted; subtracts non-cash D&A | Misstate cash (accruals, non-cash charges) |
| [[free-cash-flow\|Free cash flow]] (FCF) | Subtracts **total** capex | Understate a growing firm's steady-state cash |
| **Owner earnings** | Subtracts **maintenance** capex only | Approximate the sustainable cash to owners |

Owner earnings sits between net income and FCF, and equals FCF when a firm does no growth capex.

## Key assumptions and their sensitivity

- **Maintenance vs growth capex is a judgment call.** Companies do not report the split, so the analyst must estimate it — from depreciation as a proxy, management commentary, segment unit economics, or the relationship between historical capex and capacity. This estimate is the chief source of error and the chief source of analytical edge.
- **Working-capital swings.** Growing firms tie up cash in receivables and inventory; the change in net working capital can be volatile year to year, so owner earnings is best assessed on a normalised, multi-year basis rather than a single period.
- **Non-cash add-backs need scrutiny.** Adding back depreciation is standard, but adding back recurring "one-off" charges or treating [[share-based-compensation|stock-based compensation]] as a costless non-cash item can inflate the figure — a common abuse Buffett explicitly warned against.

## How ALFRED-style fundamental analysis uses it

- **A cash-quality cross-check on earnings.** ALFRED-style [[fundamental-analysis]] reads the [[net-income|net profit]], the [[cash-flow-statement|cash flow statement]] and capex lines from a company's report; owner earnings combines them into a single estimate of *sustainable* cash, flagging firms whose accounting earnings are not backed by cash.
- **The cash flow to discount.** In an intrinsic-value [[discounted-cash-flow|DCF]], owner earnings (or a closely related normalised FCF) is the cleanest cash-flow line to project and discount, because it strips out non-cash distortions and growth-capex noise.
- **Moat and reinvestment read.** A high and stable owner-earnings-to-net-income ratio indicates earnings backed by real cash and modest maintenance needs — characteristics of a capital-light business with a durable [[economic-moat|moat]]. Low or erratic owner earnings relative to reported profit is a red flag for capital intensity or aggressive accounting.

## Limitations

- **Not a reported number.** Owner earnings appears in no financial statement and cannot be pulled directly from a single report; it must be reconstructed, so two analysts can derive different figures.
- **Maintenance-capex estimation error.** The whole measure hinges on a split the company never discloses; in capital-intensive or fast-changing businesses this estimate can be very wrong.
- **Backward-looking inputs.** It is built from historical statements and so inherits all their lags; pairing it with a forward view (and a [[margin-of-safety|margin of safety]]) is essential.
- **Manipulable add-backs.** Like any cash metric, it can be flattered by reclassifying recurring costs as non-cash or "non-recurring."

## Worked example (hypothetical)

> The figures below are illustrative and do not refer to any real company.

A hypothetical manufacturer reports, for one year:

```
Net income .................................. $500M
+ Depreciation & amortisation ............... $120M
+ Other non-cash charges .................... $ 30M
- Maintenance capex (estimated) ............. $ 90M   (of $150M total capex; $60M is growth)
- Increase in net working capital ........... $ 20M
-----------------------------------------------------
= Owner earnings ............................ $540M
```

Compare the three measures for the same year:

```
Net income            = $500M
Free cash flow        = 500 + 120 + 30 - 150 (total capex) - 20  = $480M
Owner earnings        = 500 + 120 + 30 -  90 (maint. capex) - 20  = $540M
```

Owner earnings ($540M) exceeds simple free cash flow ($480M) by exactly the $60M of growth capex — capturing the idea that the firm *chose* to spend on expansion and that its steady-state cash generation is higher than a total-capex FCF figure suggests. If the analyst's maintenance-capex estimate is too low, owner earnings is overstated — which is why this single judgment deserves the most scrutiny.

## Related

- [[free-cash-flow]] — the closest standard measure; owner earnings refines its capex treatment
- [[intrinsic-value]] — owner earnings is Buffett's preferred input to estimate it
- [[discounted-cash-flow]] — discounts owner earnings to a present value
- [[warren-buffett]] — defined the concept in the 1986 Berkshire letter
- [[cash-flow-statement]] — the source of the non-cash add-backs and capex figures
- [[net-income]] — the starting point of the calculation
- [[economic-moat]] — high, stable owner earnings is a moat signal
- [[margin-of-safety]] — the buffer applied to any owner-earnings-based value
- [[valuation]] — broader context

## Sources

- Buffett, W.E. *Berkshire Hathaway Shareholder Letter, 1986* — the original definition of owner earnings (the "Appendix" discussion of accounting and the Scott Fetzer purchase-price accounting example).
- Graham, B. & Dodd, D. *Security Analysis* — the earnings-power and earnings-quality lineage owner earnings builds on.
- Damodaran, A. *Investment Valuation* (3rd ed., Wiley, 2012) — normalising cash flows and reinvestment for valuation.

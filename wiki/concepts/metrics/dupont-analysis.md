---
title: "DuPont Analysis"
type: concept
created: 2026-07-01
updated: 2026-07-02
status: good
tags: [fundamental-analysis, valuation, education]
aliases: ["DuPont Analysis", "DuPont Model", "DuPont Identity", "DuPont Framework", "3-Step DuPont", "5-Step DuPont"]
domain: [fundamental-analysis]
prerequisites: ["[[return-on-equity]]", "[[net-margin]]", "[[debt-to-equity]]"]
difficulty: intermediate
related: ["[[return-on-equity]]", "[[return-on-assets]]", "[[net-margin]]", "[[debt-to-equity]]", "[[financial-statement-analysis]]", "[[balance-sheet]]", "[[income-statement]]", "[[leverage]]", "[[return-on-invested-capital]]"]
---

DuPont analysis is a technique that decomposes [[return-on-equity]] (ROE) into its underlying drivers so an analyst can see *why* a company earns the return it does, rather than just *how much*. Developed by an engineer at the DuPont Corporation in the 1910s, it breaks ROE into the product of profitability, asset efficiency, and financial leverage — turning a single headline ratio into a diagnostic of where a business's returns come from and where they are vulnerable.

## The three-step identity

The classic decomposition expresses ROE as the product of three ratios:

**ROE = Net Profit Margin × Asset Turnover × Equity Multiplier**

| Component | Formula | What it measures |
|-----------|---------|------------------|
| Net profit margin | Net Income / Revenue | Profitability — how much of each sales dollar becomes profit ([[net-margin]]) |
| Asset turnover | Revenue / Total Assets | Efficiency — how much revenue each dollar of assets generates |
| Equity multiplier | Total Assets / Shareholders' Equity | Leverage — how much of the asset base is funded by debt vs equity |

The first two terms multiply to [[return-on-assets]] (Net Margin × Asset Turnover = ROA). The third term, the equity multiplier, is the [[leverage]] amplifier that converts ROA into ROE. This makes the relationship explicit: **ROE = ROA × Equity Multiplier**.

## Why the decomposition matters

Two companies can report an identical 20% ROE for entirely different reasons:

- A luxury brand might earn it through a fat 25% net margin on slow-turning inventory and little debt.
- A discount retailer might earn the same 20% on a razor-thin 2% margin, but spin its assets over many times a year.
- A leveraged firm might earn it on mediocre margins and turnover, propped up by a high equity multiplier — i.e. by carrying a lot of debt.

The third case is the warning DuPont was designed to surface: an ROE that looks healthy only because the company is heavily levered. A rising equity multiplier flatters ROE while quietly increasing [[interest-rate-risk]] and the risk of financial distress, so analysts treat leverage-driven ROE growth with suspicion relative to margin- or efficiency-driven growth.

## The five-step (extended) DuPont

The extended version splits the net margin term further to isolate the effects of interest and tax, separating *operating* performance from *financing* and *tax* effects:

**ROE = (Operating Margin) × (Asset Turnover) × (Interest Burden) × (Tax Burden) × (Equity Multiplier)**

where the interest burden (Pre-tax Income / EBIT) and tax burden (Net Income / Pre-tax Income) each sit between 0 and 1 and quantify how much of operating profit survives interest expense and taxes. This finer cut helps distinguish a company whose ROE is falling because its core operations are weakening from one whose ROE is falling only because rising rates have increased its interest burden.

## Example

A company reports: Net Income $50m, Revenue $1,000m, Total Assets $500m, Shareholders' Equity $250m.

- Net margin = 50 / 1,000 = 5%
- Asset turnover = 1,000 / 500 = 2.0×
- Equity multiplier = 500 / 250 = 2.0×
- **ROE = 5% × 2.0 × 2.0 = 20%**, of which ROA = 5% × 2.0 = 10%, doubled to 20% by the 2.0× equity multiplier.

If next year ROE rises to 24% purely because the equity multiplier climbs to 2.4× (more debt) while margin and turnover are unchanged, DuPont analysis flags that the improvement is leverage, not operating progress.

## Uses and limitations

- **Trend analysis** — tracking each component over several years reveals whether an ROE trend is being driven by genuine operating improvement or by balance-sheet engineering.
- **Peer comparison** — comparing the three drivers across competitors shows whether a firm competes on margin, on turnover, or on leverage.
- **Limitations** — DuPont inherits all the weaknesses of its inputs: it relies on accounting figures that can be distorted by one-off items, [[goodwill]], off-balance-sheet financing, and differing [[ifrs]]/[[us-gaap]] treatments. It also says nothing about cash generation, so it pairs best with a [[cash-flow-statement]] review.

## Practical notes

- **Use average balance-sheet figures.** Because ROE, ROA, asset turnover, and the equity multiplier mix a flow (income statement) with a stock (balance sheet), best practice is to use the *average* of beginning- and end-of-period assets and equity rather than a single point-in-time snapshot — this avoids distortions when the balance sheet changes sharply during the year (e.g., a large acquisition or buyback).
- **Watch shrinking or negative equity.** Aggressive [[share-buybacks]] can shrink shareholders' equity to a sliver — or push it below zero — mechanically inflating the equity multiplier and ROE without any real improvement in the business. DuPont makes this visible: a soaring equity multiplier alongside flat margins and turnover is the tell. Firms with negative book equity (e.g., after years of buybacks) produce a meaningless ROE, and DuPont's decomposition is where that shows up.
- **Cross-check with [[return-on-invested-capital]].** Because the equity multiplier rewards leverage, many analysts pair DuPont with ROIC, which measures return on *all* invested capital (debt + equity) and is not flattered by financial gearing. DuPont explains *why* ROE moves; ROIC checks whether the underlying business actually earns above its [[wacc|cost of capital]].

## Related

[[return-on-equity]] · [[return-on-assets]] · [[net-margin]] · [[debt-to-equity]] · [[leverage]] · [[financial-statement-analysis]] · [[return-on-invested-capital]] · [[share-buybacks]] · [[income-statement]] · [[balance-sheet]]

## Sources

- Standard corporate-finance and financial-statement-analysis texts (e.g., Bodie, Kane & Marcus, *Investments*; Penman, *Financial Statement Analysis and Security Valuation*) present the three- and five-step DuPont decompositions as described here. The framework originates with the DuPont Corporation's early-20th-century internal management-accounting practice; the relationships above are general, widely-taught market knowledge.

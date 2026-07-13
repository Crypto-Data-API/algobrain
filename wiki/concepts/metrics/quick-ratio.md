---
title: "Quick Ratio"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [fundamental-analysis, liquidity, valuation]
aliases: ["quick ratio", "acid-test ratio", "acid test"]
domain: [fundamental-analysis]
prerequisites: ["[[current-ratio]]"]
difficulty: beginner
related: ["[[current-ratio]]", "[[debt-to-equity]]", "[[free-cash-flow]]", "[[financial-statement-analysis]]"]
---

The **quick ratio**, also known as the **acid-test ratio**, is a stricter measure of short-term [[liquidity]] than the [[current-ratio]]. It asks whether a company can meet its near-term obligations using only its most liquid assets — excluding inventory and other items that may not convert to cash quickly or at full value.

## Formula

$$\text{Quick Ratio} = \frac{\text{Cash} + \text{Marketable Securities} + \text{Accounts Receivable}}{\text{Current Liabilities}}$$

An equivalent and often more convenient formulation:

$$\text{Quick Ratio} = \frac{\text{Current Assets} - \text{Inventory} - \text{Prepaid Expenses}}{\text{Current Liabilities}}$$

## Why "Acid Test"?

The name comes from the 19th-century practice of testing gold purity with nitric acid — if the metal survived the acid, it was real. The quick ratio is the financial equivalent: it strips out the soft assets (inventory that might not sell, prepayments that can't be recovered) and tests whether the *hard* liquid assets alone can cover what the company owes in the next 12 months. It is the default liquidity measure used by credit analysts and lenders.

## Interpretation

- **> 1.0** — healthy; liquid assets alone cover short-term liabilities
- **0.7 – 1.0** — acceptable for many industries, tight for others
- **< 0.7** — potentially concerning, depending on the business model

A quick ratio that is dramatically lower than the [[current-ratio]] tells you the balance sheet leans heavily on inventory — which is fine for a grocer but alarming for an engineering firm with finished goods that are hard to resell.

## Typical Ranges and Industry Caveats

- **Software, SaaS**: 1.5 – 4.0 (no inventory, large cash piles)
- **Professional services**: 1.0 – 2.0
- **Manufacturers**: 0.8 – 1.2
- **Retail, grocery, restaurants**: often 0.2 – 0.6 — and perfectly healthy. These businesses sell inventory for cash in days, then pay suppliers on 30–60 day terms, so a low quick ratio is structural rather than distressed.

Always compare to industry peers and the firm's own historical baseline.

## Limitations

1. **Receivables quality** — treats all accounts receivable as near-cash, ignoring aging and collectibility risk.
2. **Timing blindness** — same snapshot problem as the [[current-ratio]]; doesn't distinguish a bill due tomorrow from one due in 11 months.
3. **Undrawn credit lines** — a firm with committed revolving credit has liquidity the ratio does not capture.
4. **Complement, not replacement** — the quick ratio *refines* the current ratio; most analysts use both together rather than choosing between them.

For a complete liquidity picture, pair the quick ratio with [[free-cash-flow]], [[debt-to-equity]], and the cash conversion cycle.

## Trading Relevance

The quick ratio is a solvency / survival screen — most useful in the part of the market where bankruptcy risk is the dominant driver of returns. It is an input to distress models (it sits alongside working-capital and leverage terms in Altman's Z-score logic) and a practical filter for **short candidates and value traps**: a deteriorating quick ratio combined with negative [[free-cash-flow]] and rising [[debt-to-equity]] is a classic balance-sheet-stress short setup, since such firms are forced into dilutive raises or fire-sale asset disposals. On the long side, screening *out* low-quick-ratio names helps avoid leveraged businesses that look statistically cheap but cannot survive a liquidity squeeze or refinancing-rate shock. The metric matters most in capital-intensive, cyclical, and credit-sensitive sectors, and during regimes of tightening funding conditions; for asset-light software names with large cash balances it rarely binds. As always, judge the trend and the peer/industry baseline rather than the absolute level — a 0.4 quick ratio is structural and healthy for a grocer but alarming for a manufacturer.

## Related

- [[current-ratio]]
- [[debt-to-equity]]
- [[free-cash-flow]]
- [[financial-statement-analysis]]

## Sources

- Altman, Edward I. (1968). "Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy." *Journal of Finance* 23(4).
- Penman, Stephen H. *Financial Statement Analysis and Security Valuation* (McGraw-Hill) — liquidity ratios.
- CFA Institute, *Financial Reporting and Analysis* curriculum — liquidity and solvency ratios.

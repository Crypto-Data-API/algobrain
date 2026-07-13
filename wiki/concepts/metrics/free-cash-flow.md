---
title: "Free Cash Flow (FCF)"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [fundamental-analysis, cash-flow, metrics, financial-statements, valuation]
aliases: ["FCF", "fcf", "free cash flow", "free-cash-flow", "owner earnings"]
domain: [fundamental-analysis]
prerequisites: ["[[financial-statement-analysis]]"]
difficulty: intermediate
related: ["[[ebitda]]", "[[return-on-invested-capital]]", "[[intrinsic-value]]", "[[dcf-analysis]]", "[[price-to-earnings-ratio]]", "[[financial-statement-analysis]]"]
---

**Free cash flow (FCF)** is the cash a business generates from its operations after funding the capital expenditures required to maintain and grow the asset base. It is widely regarded as the single most important fundamental metric because it measures the actual cash available to be returned to investors — as dividends, buybacks, debt repayment, or reinvestment.

## Formula

$$\text{FCF} = \text{Cash Flow from Operations} - \text{Capital Expenditures}$$

Both inputs come directly from the **cash flow statement**. CapEx is typically the "purchase of property, plant, and equipment" line under investing activities. Two refinements of the basic formula are commonly used in valuation:

- **Free Cash Flow to the Firm (FCFF)** = EBIT × (1 − tax rate) + D&A − ΔWorking Capital − CapEx. Represents cash available to *all* capital providers (debt and equity holders) and is the input to enterprise-value DCFs.
- **Free Cash Flow to Equity (FCFE)** = FCF − Net Debt Repayment. Represents cash available to equity holders only and is discounted at the cost of equity.

## Owner Earnings

Warren Buffett's "owner earnings" concept in his 1986 Berkshire shareholder letter is functionally the same idea: reported earnings + D&A − the average annual CapEx needed to maintain competitive position. The spirit is identical: *what cash could the owner actually extract from the business without damaging it?*

## Interpretation

- **Positive and growing FCF** — the gold standard; the business self-funds and generates surplus cash.
- **Positive FCF, negative earnings** — often a tax-optimized mature business (heavy D&A shields earnings) — usually healthy.
- **Negative FCF, positive earnings** — a red flag. Earnings are accruals; if cash isn't following them, question working capital, aggressive revenue recognition, or growth CapEx that may never pay off.
- **Negative FCF by design** — acceptable in early-stage growth companies reinvesting heavily, but the market eventually demands a credible path to positive FCF.

## Why Cash Is Harder to Fake

Earnings involve dozens of accrual judgments — revenue recognition, bad-debt provisions, inventory reserves, depreciation schedules, goodwill impairments. Cash is cash: it either left the bank account or it didn't. While FCF can still be *managed* (stretching payables, squeezing receivables, cutting maintenance CapEx), systematic manipulation is far harder to sustain than earnings management.

## FCF Yield and Valuation

$$\text{FCF Yield} = \frac{\text{FCF}}{\text{Market Cap}}$$

FCF yield is the cash-flow analog of the inverse [[price-to-earnings-ratio]] and is a cleaner valuation signal because it bypasses accounting noise. A 6–8% FCF yield is generally considered attractive for a mature business; < 3% implies high growth expectations baked in.

The discounted cash flow ([[intrinsic-value|DCF]]) model — the theoretical anchor of all fundamental valuation — projects future FCFs explicitly and discounts them back to present value.

## Limitations

1. **Lumpy CapEx** — large projects distort a single year. Average FCF across a cycle.
2. **Maintenance vs growth CapEx** — GAAP doesn't split them, so aggressive growth investment can mask weak core economics.
3. **Working capital swings** — a one-time inventory drawdown can flatter FCF temporarily.
4. **Stock-based compensation** — added back in operating cash flow but is a real cost. Many analysts subtract SBC to get a truer picture.

## Trading Relevance

FCF yield is one of the most robust value factors in systematic equity investing — ranking a universe by FCF/Market Cap and going long the cheap quintile has historically delivered a value premium that is cleaner than book-to-market or earnings-based screens because cash is harder to manipulate than accruals. FCF also anchors **quality** factors: "free-cash-flow conversion" (FCF ÷ net income) screens for companies whose accounting earnings are genuinely backed by cash, and a persistent gap between rising earnings and stagnant or negative FCF is a classic short/avoid signal flagging accrual-driven, low-quality earnings. The [[dcf-analysis|DCF]] — the theoretical anchor of all intrinsic valuation — projects future FCFs explicitly and discounts them at the WACC (using FCFF) or cost of equity (using FCFE). Capital-allocation traders also watch FCF directly because it funds the dividends, buybacks, and debt paydown that drive total shareholder yield.

## Related

- [[ebitda]]
- [[return-on-invested-capital]]
- [[intrinsic-value]], [[dcf-analysis]]
- [[price-to-earnings-ratio]]
- [[financial-statement-analysis]]

## Sources

- Buffett, W. (1986), Berkshire Hathaway shareholder letter — definition of "owner earnings"
- Damodaran, A., *Investment Valuation* — FCFF, FCFE, and discounted-cash-flow valuation
- CFA Institute curriculum, *Free Cash Flow Valuation* — FCFF/FCFE computation and discounting
- US GAAP ASC 230 / IFRS IAS 7 — *Statement of Cash Flows*, the source of operating cash flow and capex

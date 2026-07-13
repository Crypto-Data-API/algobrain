---
title: "Free Cash Flow Yield"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, metrics, liquidity]
aliases: ["FCF Yield", "fcf yield", "free cash flow yield", "free-cash-flow-yield", "FCF/EV yield", "cash flow yield"]
domain: [fundamental-analysis]
prerequisites: ["[[free-cash-flow]]", "[[market-capitalization]]", "[[enterprise-value]]"]
difficulty: intermediate
related: ["[[free-cash-flow]]", "[[price-to-cash-flow]]", "[[earnings-yield]]", "[[price-to-earnings-ratio]]", "[[enterprise-value]]", "[[dividend-yield]]", "[[cash-flow-statement]]", "[[fundamental-analysis]]"]
---

**Free cash flow yield** expresses a company's [[free-cash-flow|free cash flow]] as a percentage of its market value. It is the cash-flow analog of the [[earnings-yield|earnings yield]] (the inverse of the [[price-to-earnings-ratio|P/E]] ratio) and answers the investor's most direct question: *for every dollar I pay for this business today, how much actual cash does it throw off each year?* Because cash is far harder to manipulate than accounting earnings, FCF yield is often considered one of the cleaner valuation signals.

## Formula

There are two standard versions, differing in the denominator:

$$\text{FCF Yield (equity)} = \frac{\text{Free Cash Flow}}{\text{Market Capitalization}} \times 100\%$$

$$\text{FCF Yield (firm)} = \frac{\text{Free Cash Flow}}{\text{Enterprise Value}} \times 100\%$$

- The **equity version** (FCF ÷ [[market-capitalization|market cap]]) measures the yield to equity holders and is the simplest to compute.
- The **enterprise version** (FCF ÷ [[enterprise-value|enterprise value]]) is more rigorous for cross-company comparison because it accounts for differences in debt and cash, the same way [[ev-ebitda|EV/EBITDA]] improves on P/E. Pairing FCFF with EV keeps numerator and denominator consistent (both pre-financing).

[[free-cash-flow|Free cash flow]] is cash flow from operations minus capital expenditures.

## Worked Example

A company has:

- Free cash flow: $800 million
- Market capitalization: $16 billion
- Net debt: $4 billion → enterprise value = $20 billion

$$\text{FCF Yield (equity)} = \frac{800}{16{,}000} = 5.0\%$$
$$\text{FCF Yield (firm)} = \frac{800}{20{,}000} = 4.0\%$$

An equity FCF yield of 5% means the business generates 5 cents of free cash per year for every dollar of market value — comparable to a bond yielding 5%, except the cash flow can grow.

## Interpretation

- **High FCF yield (roughly 6–8%+)** on a stable, mature business is generally considered attractive — the market is paying a low price for each dollar of cash generation.
- **Low FCF yield (under ~3%)** implies high growth expectations are baked into the price; investors are paying up today for cash flows they expect to be much larger later.
- **Negative FCF yield** is normal for early-stage growth companies reinvesting heavily, but the market eventually demands a credible path to positive free cash flow.

Like earnings yield, FCF yield is naturally compared against the **risk-free rate** (e.g. the 10-year Treasury). When a quality company's FCF yield sits well above the risk-free rate, the equity looks attractive on a relative-value basis; when it compresses toward or below it, the cushion for disappointment is thin.

## Why It Beats Earnings-Based Yields

The [[earnings-yield|earnings yield]] uses net income, which is shaped by dozens of accrual judgments — depreciation schedules, revenue recognition, provisions, and non-cash charges. FCF yield uses cash that has actually moved, so it sidesteps much of that accounting noise. A company can report rising earnings while free cash flow stagnates or turns negative (a classic accrual red flag); FCF yield catches what earnings-based multiples miss.

## FCF Yield vs. Dividend Yield

[[dividend-yield|Dividend yield]] measures only the cash actually *paid out*; FCF yield measures the cash *available* to pay out. The difference matters:

- If **FCF yield > dividend yield**, the dividend is comfortably covered and there is room to grow it, buy back stock, or pay down debt.
- If **dividend yield > FCF yield**, the company is paying out more than it generates — funding the dividend from the balance sheet or borrowing, which is rarely sustainable.

## Limitations

1. **Lumpy capital expenditure** — a single heavy-capex year can depress FCF and overstate the yield's cheapness or richness. Average across a cycle.
2. **Maintenance vs. growth capex** — GAAP does not separate them, so a company investing heavily for growth can look artificially cash-poor.
3. **Working-capital swings** — a one-off inventory or receivables movement can flatter or depress a single year's FCF.
4. **Stock-based compensation** — added back in operating cash flow but a real economic cost; many analysts subtract it for a truer FCF figure.
5. **Not meaningful for banks/insurers** — the FCF concept does not apply cleanly to financials.

## Trading Relevance

FCF yield is one of the most robust **value factors** in systematic equity investing: ranking a universe by FCF/market cap (or FCF/EV) and going long the cheapest quintile has historically delivered a cleaner value premium than book-to-market or earnings-based screens, precisely because cash resists manipulation. It also doubles as a **quality** check — "free-cash-flow conversion" (FCF ÷ net income) flags whether reported earnings are genuinely cash-backed, and a widening gap between rising earnings and flat-or-negative FCF is a recognised avoid/short signal. Capital-allocation and income-oriented traders watch FCF yield directly because it bounds the dividends, buybacks, and debt paydown that drive total shareholder yield.

## Related

- [[free-cash-flow]]
- [[price-to-cash-flow]] — the reciprocal multiple (P/FCF = 1 / FCF yield)
- [[earnings-yield]]
- [[price-to-earnings-ratio]]
- [[enterprise-value]]
- [[dividend-yield]]
- [[cash-flow-statement]] — where free cash flow is derived
- [[fundamental-analysis]]

## Sources

- Damodaran, Aswath. *Investment Valuation* (Wiley) — free cash flow to firm/equity and yield-based valuation.
- CFA Institute, *Free Cash Flow Valuation* curriculum — FCFF/FCFE and relative-value yields.
- Greenblatt, Joel. *The Little Book That Beats the Market* — cash-flow/earnings yield as a value screen.

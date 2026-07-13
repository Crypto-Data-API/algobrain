---
title: "DCF Analysis"
type: concept
created: 2026-04-13
updated: 2026-06-22
status: excellent
tags: [fundamental-analysis, valuation]
aliases: ["Discounted Cash Flow", "DCF"]
domain: [fundamental-analysis]
difficulty: advanced
related: ["[[intrinsic-value]]", "[[alfred-fundamental-analysis]]", "[[free-cash-flow]]", "[[margin-of-safety]]", "[[discounted-cash-flow]]", "[[wacc]]", "[[terminal-value]]", "[[valuation]]", "[[weighted-average-cost-of-capital]]"]
---

Discounted Cash Flow (DCF) analysis is an intrinsic valuation method that projects a company's future [[free-cash-flow|free cash flows]] and discounts them back to present value using an appropriate discount rate (typically the [[weighted-average-cost-of-capital]]). The sum of these discounted cash flows, plus a terminal value, provides an estimate of the company's intrinsic worth. Fred McNaught uses DCF as a "rough guide only," cautioning that the output is highly sensitive to assumptions about growth rates, margins, and the discount rate -- small changes in inputs can produce dramatically different valuations. He prefers to use DCF alongside [[peer-comparison]] and relative valuation metrics like [[price-to-earnings-ratio|PE ratios]] rather than relying on it in isolation. For the theoretical foundations of the time-value-of-money mathematics, see [[discounted-cash-flow]]; this page is the *applied valuation workflow*.

## Core Formula

The value of a business is the present value of its future cash flows plus a [[terminal-value]]:

$$\text{Value} = \sum_{t=1}^{n} \frac{\text{FCF}_t}{(1 + r)^t} + \frac{\text{TV}_n}{(1 + r)^n}$$

where $\text{FCF}_t$ is the free cash flow in year $t$, $r$ is the discount rate, $n$ is the length of the explicit forecast, and $\text{TV}_n$ is the terminal value at the end of year $n$.

## FCFF vs FCFE — Two Flavours of DCF

The choice of cash flow dictates the discount rate and what you get out:

| | FCFF (free cash flow to firm) | FCFE (free cash flow to equity) |
|---|---|---|
| Cash flow to | All capital providers (debt + equity) | Equity holders only |
| Formula | EBIT × (1 − tax) + D&A − capex − ΔNWC | Net income + D&A − capex − ΔNWC + net borrowing |
| Discount rate | [[wacc|WACC]] | Cost of equity ($k_e$, e.g. from CAPM) |
| Output | Enterprise value → subtract net debt → equity value | Equity value directly |

The firm-level (FCFF + WACC) approach is the industry standard because it is insensitive to changes in capital structure during the forecast. The two methods should reconcile to the same equity value when assumptions are consistent.

## Step-by-Step DCF Walkthrough

### Step 1: Project Revenue and Margins

Start with the company's historical financials (3-5 years minimum). Identify the revenue growth rate trajectory and operating margins. Project revenue forward 5-10 years using a combination of top-down (market size, share) and bottom-up (unit economics, pricing) analysis. Model operating margins converging toward a sustainable long-term level. Be explicit about assumptions: "Revenue grows 15% in year 1, decelerating 2% annually to a terminal rate of 4%."

### Step 2: Calculate Free Cash Flow

For each projected year, derive [[free-cash-flow]] (FCF): Operating Income * (1 - Tax Rate) + Depreciation & Amortization - Capital Expenditures - Change in Working Capital. FCF represents the cash truly available to all capital providers after the business has reinvested what it needs to sustain the projected growth. A common error is projecting high revenue growth without correspondingly higher capex and working capital needs.

### Step 3: Choose the Discount Rate (WACC)

The [[weighted-average-cost-of-capital]] blends the cost of equity (often estimated via CAPM: risk-free rate + beta * equity risk premium) and the after-tax cost of debt, weighted by the company's target capital structure. Typical WACC for large US companies ranges from 7-12%. For riskier companies or emerging markets, it can be significantly higher. The choice of WACC is one of the most consequential assumptions in the entire model.

### Step 4: Calculate Terminal Value

Since projecting cash flows indefinitely is impractical, a terminal value captures all value beyond the explicit forecast period. Two approaches:

- **Perpetuity Growth Method**: TV = Final Year FCF * (1 + g) / (WACC - g), where g is the long-term growth rate (typically 2-3%, approximating nominal GDP growth). The growth rate must be below WACC or the formula produces nonsensical results.
- **Exit Multiple Method**: TV = Final Year EBITDA * chosen EV/EBITDA multiple. The multiple should reflect what a buyer would reasonably pay for the business at that future date.

Terminal value often represents 60-80% of total DCF value, which highlights why terminal assumptions matter so much.

### Step 5: Discount and Sum

Discount each year's FCF and the terminal value back to the present: PV = FCF_t / (1 + WACC)^t. Sum all present values to get Enterprise Value. Subtract net debt (total debt minus cash) to get equity value. Divide by shares outstanding to get implied share price. Compare this to the current market price to assess whether the stock offers a [[margin-of-safety]].

## Worked Example (illustrative round numbers)

A company with current FCF of $100M, growing 8% for 5 years, [[wacc|WACC]] of 10%, terminal growth $g$ = 3%, net debt $200M, and 100M shares outstanding.

**Explicit forecast (FCF grows 8%/yr, discounted at 10%):**

| Year | FCF | Discount factor 1/(1.10)^t | PV |
|------|-----|-----------------------------|-----|
| 1 | 108.0 | 0.909 | 98.2 |
| 2 | 116.6 | 0.826 | 96.4 |
| 3 | 126.0 | 0.751 | 94.6 |
| 4 | 136.0 | 0.683 | 92.9 |
| 5 | 146.9 | 0.621 | 91.2 |
| **Sum of PV(FCF)** | | | **≈ 473** |

**Terminal value** (perpetuity growth, using year-5 FCF of 146.9):

$$\text{TV}_5 = \frac{146.9 \times (1.03)}{0.10 - 0.03} = \frac{151.3}{0.07} \approx 2{,}162 \quad\Rightarrow\quad \text{PV} = 2{,}162 \times 0.621 \approx 1{,}343$$

**Pull it together:**

| Component | Value |
|-----------|-------|
| PV of explicit FCF | ≈ 473 |
| PV of terminal value | ≈ 1,343 |
| **Enterprise value** | **≈ 1,816** |
| − Net debt | −200 |
| **Equity value** | **≈ 1,616** |
| ÷ Shares (100M) | |
| **Implied value per share** | **≈ $16.16** |

Note that the terminal value (≈1,343) is roughly **74%** of enterprise value — the textbook warning that DCF is dominated by terminal assumptions is borne out even in this modest example. If the stock trades at $11, the model implies a ~30% [[margin-of-safety]]; if it trades at $20, the model says it is overvalued *given these inputs*.

## Common Pitfalls

- **Over-optimistic growth projections**: The base rate for US companies sustaining >15% revenue growth for a decade is very low. Anchoring to recent high growth without mean-reversion is the most common DCF error.
- **WACC errors**: Using the wrong beta, ignoring the debt/equity mix, or applying a developed-market WACC to an emerging-market company.
- **Terminal value dominance**: If terminal value is >80% of total value, the DCF is essentially a terminal value model dressed up as a multi-year forecast. Stress-test terminal assumptions aggressively.
- **Ignoring dilution**: Stock-based compensation and convertible securities dilute existing shareholders but are often excluded from FCF.
- **Circular references**: WACC depends on equity value (for weights), which depends on the DCF output, which depends on WACC. Use iterative solving or target capital structure weights.

## Sensitivity Analysis

Always present DCF results as a range, not a point estimate. A sensitivity table varying the discount rate (rows) and terminal growth rate (columns) by +/- 1-2% shows how dramatically the output changes. Continuing the worked example above (implied ≈ $16/share at WACC 10%, g 3%), a stylized sensitivity grid of implied value per share might look like:

| WACC ↓ / g → | g = 2% | g = 3% | g = 4% |
|--------------|--------|--------|--------|
| **9%** | ~$17 | ~$20 | ~$24 |
| **10%** | ~$14 | ~$16 | ~$19 |
| **11%** | ~$12 | ~$13 | ~$15 |

A ±1% move in either input swings the answer by 20–40% — the entire investment case can flip on assumptions that are themselves only estimates. If the current stock price falls within the range under reasonable assumptions, the stock may be fairly valued. If it sits well below the low end of the range, there may be a [[margin-of-safety]]. This sensitivity is exactly why Fred treats DCF as a "rough guide only" and cross-checks against [[peer-comparison]].

## Sources

- Damodaran, A. *Investment Valuation: Tools and Techniques for Determining the Value of Any Asset* (3rd ed., Wiley, 2012) — the standard reference for DCF mechanics, WACC estimation, and terminal value.
- Koller, T., Goedhart, M. & Wessels, D. *Valuation: Measuring and Managing the Value of Companies* (McKinsey, 7th ed., 2020) — practitioner framework for FCF projection and sensitivity analysis.
- McNaught, F. ITPM (Institute of Trading and Portfolio Management) curriculum — treats DCF as a "rough guide" cross-checked against [[peer-comparison]] relative valuation.
- General market knowledge; no additional specific wiki source ingested yet.

## Related

- [[discounted-cash-flow]] — theoretical foundations of the DCF methodology (time value of money)
- [[valuation]] — overview of all valuation approaches
- [[weighted-average-cost-of-capital]] · [[wacc]] — the discount rate
- [[terminal-value]] — the post-forecast value, usually 60–80% of the total
- [[free-cash-flow]] — the cash flows being projected and discounted
- [[intrinsic-value]] — what DCF attempts to estimate
- [[margin-of-safety]] — the gap between intrinsic value and market price
- [[peer-comparison]] — the relative valuation complement to DCF

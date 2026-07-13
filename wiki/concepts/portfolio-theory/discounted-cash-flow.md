---
title: "Discounted Cash Flow"
type: concept
created: 2026-04-13
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, valuation]
aliases: ["DCF", "Discounted Cash Flow Valuation", "Present Value of Cash Flows"]
domain: [fundamental-analysis]
prerequisites: ["[[free-cash-flow]]", "[[weighted-average-cost-of-capital]]"]
difficulty: advanced
related: ["[[dcf-analysis]]", "[[valuation]]", "[[weighted-average-cost-of-capital]]", "[[free-cash-flow]]", "[[intrinsic-value]]", "[[margin-of-safety]]"]
---

Discounted Cash Flow (DCF) is a [[valuation]] methodology that estimates the intrinsic worth of an asset by projecting its future free cash flows and discounting them back to their present value. The core principle is the time value of money: a dollar received today is worth more than a dollar received in the future, because today's dollar can be invested to earn a return. DCF is widely considered the most theoretically rigorous approach to valuation in finance. For a step-by-step practical walkthrough, see [[dcf-analysis]].

## The DCF Framework

A standard DCF valuation has three components. First, the analyst projects [[free-cash-flow|free cash flows]] (FCF) for a discrete forecast period, typically 5 to 10 years. FCF represents the cash a business generates after accounting for capital expenditures -- it is the cash available to all capital providers (debt and equity holders). Second, a terminal value captures the value of all cash flows beyond the forecast period, since most businesses are assumed to operate indefinitely. Terminal value is calculated either using a perpetuity growth model (Gordon Growth: FCF * (1+g) / (WACC - g)) or an exit multiple approach (applying an EV/EBITDA or EV/FCF multiple to the final year's figures). Third, all projected cash flows and the terminal value are discounted to the present using the [[weighted-average-cost-of-capital]] (WACC) as the discount rate.

### The core formula

The present value of a stream of future cash flows is the sum of each year's cash flow discounted by the appropriate factor:

```
                 n
Enterprise     ____    FCF_t            Terminal Value_n
Value      =   \      ---------    +    -----------------
               /___   (1 + r)^t            (1 + r)^n
                t=1

where  r = WACC,  Terminal Value = FCF_(n+1) / (r − g)  [Gordon Growth]
```

To go from enterprise value to **equity value (and per-share intrinsic value)**:

```
Equity Value  = Enterprise Value − Net Debt − Minority Interest − Preferred
Intrinsic Value per Share = Equity Value / Diluted Shares Outstanding
```

### Inputs at a glance

| Input | What it is | Typical source / range | Sensitivity |
|---|---|---|---|
| FCF | Cash to all capital providers (FCFF) | Forecast from revenue → margins → reinvestment | High |
| [[weighted-average-cost-of-capital\|WACC]] (r) | Blended cost of debt + equity | Often 7–11% for mature firms | Very high |
| Terminal growth (g) | Perpetual growth after forecast | Capped at long-run GDP/inflation, ~2–3% | Very high |
| Forecast horizon (n) | Explicit projection years | 5–10 years | Medium |
| Net debt | Debt − cash, to bridge EV→equity | [[balance-sheet]] | Medium |
| Share count | Diluted shares for per-share value | Filings, incl. [[stock-based-compensation\|SBC]] dilution | Medium |

### Worked example

Suppose a mature firm generates **$100M of FCF this year**, growing **8% per year for 5 years**, then **2.5% in perpetuity**, discounted at a **WACC of 9%**.

- Year 1–5 FCF: $108.0M, $116.6M, $126.0M, $136.0M, $146.9M.
- Discounted (at 9%): ≈ $99.1M + $98.2M + $97.3M + $96.3M + $95.5M ≈ **$486.4M** for the explicit period.
- Terminal value at end of year 5 = $146.9M × 1.025 / (0.09 − 0.025) = $150.6M / 0.065 ≈ **$2,317M**.
- Discount the terminal value back 5 years: $2,317M / (1.09)^5 ≈ **$1,506M**.
- **Enterprise value ≈ $486M + $1,506M ≈ $1,992M.** If net debt is $200M, equity value ≈ $1,792M; across 100M shares, intrinsic value ≈ **$17.9 per share**.

Note that the terminal value ($1,506M) is roughly **76% of the total** — the textbook illustration of terminal-value dominance flagged below.

## Sensitivity to Assumptions

DCF is powerful in theory but fragile in practice. Small changes in key inputs produce dramatically different outputs. The discount rate (WACC), long-term growth rate, and operating margin assumptions are particularly sensitive levers. A 1% change in the terminal growth rate or WACC can swing the valuation by 20-30%. This is why experienced analysts -- including Fred McNaught in the ITPM curriculum -- treat DCF as a "rough guide" rather than a precision instrument, and always run sensitivity tables that show the valuation across a range of assumptions. DCF works best for mature businesses with relatively predictable cash flows (utilities, consumer staples) and is least reliable for early-stage companies, cyclical businesses, or firms undergoing rapid change.

A typical **sensitivity (football-field) table** grids per-share intrinsic value against the two most powerful levers — WACC and terminal growth. Continuing the worked example above (centered on ~$17.9/share), the pattern looks like this (illustrative):

| WACC \ g | 1.5% | 2.5% | 3.5% |
|---|---|---|---|
| **8.0%** | $19.8 | $22.5 | $26.4 |
| **9.0%** | $16.2 | $17.9 | $20.2 |
| **10.0%** | $13.6 | $14.7 | $16.2 |

A spread from ~$13.6 to ~$26.4 — nearly 2× — from moving each lever a single percentage point is exactly why a DCF output should be read as a *range*, never a single number. Disciplined analysts quote the central estimate together with this grid and a [[margin-of-safety]] haircut.

## FCFF vs. FCFE: which cash flow, which discount rate

There are two consistent ways to build a DCF, and mixing them is a frequent error:

| Approach | Cash flow discounted | Discount rate | Output |
|---|---|---|---|
| **FCFF (firm)** | Free cash flow to the *firm* (pre-financing) | [[weighted-average-cost-of-capital\|WACC]] | Enterprise value → subtract net debt → equity |
| **FCFE (equity)** | Free cash flow to *equity* (after interest & debt) | Cost of equity (e.g. [[capm\|CAPM]]) | Equity value directly |

The FCFF/WACC route is the industry standard because WACC and capital structure are easier to keep consistent; the FCFE/cost-of-equity route is common for banks and financials where "debt" is part of operations. Discounting FCFF at the cost of equity, or FCFE at WACC, double-counts or omits the financing effect and is one of the "wrong discount rate" pitfalls below.

## DCF vs. Relative Valuation

DCF provides an absolute valuation grounded in fundamentals, whereas relative valuation methods (like [[price-to-earnings-ratio|PE ratios]], EV/EBITDA, or [[peer-comparison]]) value a company by reference to how the market prices comparable firms. In practice, analysts use both approaches as cross-checks. If a DCF says a stock is worth $80 but every comparable company trades at multiples implying $120, the analyst must investigate which approach is capturing reality more accurately. A significant gap between DCF and market price may indicate either a genuine [[margin-of-safety]] opportunity or a flawed DCF model.

## Common Pitfalls

- **Over-optimistic revenue growth**: projecting 15-20% growth for a decade when base rates for the industry are 5-8%
- **Ignoring reinvestment needs**: FCF projections that assume high growth without corresponding capital expenditure
- **Terminal value dominance**: in many DCFs, 60-80% of total value comes from the terminal value, making the terminal assumptions disproportionately important
- **Wrong discount rate**: using an equity cost of capital when the firm is levered, or vice versa (see the FCFF/FCFE table above)
- **Anchoring to a desired outcome**: reverse-engineering inputs to justify a target price
- **Ignoring [[stock-based-compensation|stock-based compensation]]**: treating SBC as a non-cash add-back without modeling the share-count dilution it causes — inflates per-share value
- **g ≥ r**: setting terminal growth at or above the discount rate, which makes the Gordon Growth denominator collapse and the valuation explode to nonsense

## How traders and analysts use DCF

DCF is rarely the *trade trigger* on its own — it is too slow and assumption-heavy for fast markets — but it anchors several practical workflows:

- **Reverse DCF**: instead of forecasting cash flows, hold the current market price fixed and solve for the growth rate the market is *implying*. If a stock's price requires 25% FCF growth forever and the industry grows 6%, the market is pricing in heroics — a short candidate or, if you disagree the other way, a clear [[margin-of-safety]] long.
- **Scenario / probability-weighted DCF**: build bull, base, and bear cases, assign probabilities, and take the expected value. This makes the range explicit rather than pretending to a point estimate.
- **Cross-check against multiples**: pair DCF with EV/[[ebitda|EBITDA]] and [[price-to-earnings-ratio|P/E]] so an aggressive model can't quietly diverge from how the market prices peers (see next section).
- **Position-sizing input**: the gap between intrinsic value and price, after a [[margin-of-safety]] haircut, informs conviction and therefore size for discretionary [[value-investing|value]] books.

## Sources

- Williams, J.B. *The Theory of Investment Value* (Harvard University Press, 1938) — the origin of the dividend/cash-flow discount model and intrinsic-value-as-discounted-cash-flow.
- Damodaran, A. *Investment Valuation* (3rd ed., Wiley, 2012) — comprehensive treatment of DCF assumptions, discount rates, and terminal value.
- Gordon, M.J. (1959). "Dividends, Earnings, and Stock Prices." *Review of Economics and Statistics*, 41(2) — the Gordon Growth (perpetuity) terminal-value model.

## Related

- [[dcf-analysis]] — step-by-step practical DCF walkthrough
- [[valuation]] — overview of valuation approaches
- [[terminal-value]] — the post-forecast lump sum, usually most of DCF value
- [[discount-rate]] — the rate that converts future cash flows to present value
- [[dividend-discount-model]] — the dividend-only special case of DCF
- [[owner-earnings]] — Buffett's preferred cash-flow input to discount
- [[weighted-average-cost-of-capital]] — the discount rate used in DCF
- [[free-cash-flow]] — the cash flows being discounted
- [[intrinsic-value]] — the concept DCF attempts to estimate
- [[margin-of-safety]] — the discount applied to a DCF estimate before acting
- [[capm]] — derives the cost of equity used in WACC / FCFE
- [[ebitda]] — feeds exit-multiple terminal values and cross-checks
- [[balance-sheet]] — net debt bridge from enterprise to equity value
- [[value-investing]] — the discipline DCF most directly serves

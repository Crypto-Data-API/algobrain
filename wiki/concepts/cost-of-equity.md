---
title: "Cost of Equity"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, portfolio-theory]
domain: [valuation, portfolio-theory]
prerequisites: ["[[capm]]", "[[risk-free-rate]]"]
difficulty: intermediate
aliases: ["Cost of Equity", "Required Return on Equity", "Re", "Ke", "Required Rate of Return"]
related: ["[[weighted-average-cost-of-capital]]", "[[capm]]", "[[discount-rate]]", "[[dividend-discount-model]]", "[[risk-free-rate]]", "[[equity-risk-premium]]", "[[beta]]", "[[cost-of-debt]]", "[[discounted-cash-flow]]", "[[valuation]]"]
---

The **cost of equity** is the rate of return that equity investors require to compensate them for the risk of owning a company's stock. It is the equity-holder's side of a firm's [[weighted-average-cost-of-capital|cost of capital]] -- the opportunity cost of putting money into one company's shares rather than into an alternative investment of comparable risk. Because shareholders have a residual, non-contractual claim on cash flows, the cost of equity is almost always higher than a firm's [[cost-of-debt|cost of debt]].

## Overview

Unlike interest on debt, the cost of equity is not an observable, contractual number -- a company never writes shareholders a cheque labelled "required return." It is an **estimated** discount rate, inferred from market data and risk models. It serves two central purposes:

1. **As a discount rate** -- in a [[dividend-discount-model|dividend discount model (DDM)]] or an equity-level [[discounted-cash-flow|discounted cash flow]], future cash flows to shareholders are discounted at the cost of equity to produce an intrinsic value. It is also the equity input (Re) inside [[weighted-average-cost-of-capital|WACC]].
2. **As a hurdle rate** -- a company creates value for shareholders only when the return it earns on equity-funded projects exceeds its cost of equity.

## Formula: The CAPM Approach

The dominant method for estimating the cost of equity is the [[capm|Capital Asset Pricing Model (CAPM)]]:

```
Re = Rf + Beta * (Rm - Rf)
```

Where:

- **Re** = cost of equity (the required return)
- **Rf** = the [[risk-free-rate|risk-free rate]], typically the yield on a long-dated government bond (e.g., the 10-year US Treasury)
- **Beta** = the stock's [[beta|systematic risk]] -- its sensitivity to overall market movements; beta of 1.0 moves with the market, >1.0 is more volatile, <1.0 is less
- **(Rm - Rf)** = the [[equity-risk-premium|equity risk premium]] -- the extra return investors demand for holding stocks over the risk-free asset (historically estimated in the ~4%-6% range for the US market, though estimates vary widely by method and period)

The logic: investors are paid the risk-free rate for the time value of money, plus an additional premium scaled by how much undiversifiable risk the stock adds to a diversified portfolio.

## Alternative Approach: The Dividend Discount / Gordon Growth Method

For stable, dividend-paying firms, the cost of equity can be backed out of the [[dividend-discount-model|Gordon Growth Model]]:

```
Re = (D1 / P0) + g
```

Where **D1** is next year's expected dividend per share, **P0** is the current share price, and **g** is the long-run dividend growth rate. This method ties the cost of equity directly to the price the market is paying, but it only works for firms with predictable, growing dividends and is highly sensitive to the assumed growth rate.

## Why It Matters to a Stock Investor

- **It sets the bar for value creation.** A company that earns a [[return-on-equity|return on equity]] below its cost of equity is destroying shareholder value even if accounting profits are positive. The spread between ROE and cost of equity is a cleaner signal of a durable franchise than headline earnings.
- **It drives intrinsic value.** In any DCF or DDM, the cost of equity (or WACC) is the discount rate, and small changes produce large swings in fair value -- especially for long-duration growth stocks whose value sits far in the future.
- **It explains rate sensitivity.** Because Rf is embedded in the cost of equity, rising interest rates raise the required return and compress valuations across the market. Long-duration growth equities behave like long-duration bonds, which is why richly-valued tech sold off sharply during the 2022 rate-hike cycle.
- **It frames the equity-vs-bond decision.** Comparing a stock's earnings yield to its cost of equity, or to bond yields, is a first-order check on whether equities are cheap or expensive relative to fixed income.

## Hypothetical Worked Example

*The following figures are illustrative, not investment advice or a forecast.*

Suppose an analyst is valuing a hypothetical large-cap industrial company:

- Risk-free rate (10-year Treasury): **Rf = 4.0%**
- The stock's beta: **Beta = 1.20**
- Assumed equity risk premium: **(Rm - Rf) = 5.0%**

Applying CAPM:

```
Re = 4.0% + 1.20 * 5.0% = 4.0% + 6.0% = 10.0%
```

The analyst would discount the company's projected equity cash flows at **10%**. If a competitor in the same industry had a beta of 0.80 (less volatile), its cost of equity would be 4.0% + 0.80 * 5.0% = **8.0%** -- a lower hurdle, reflecting that investors demand less compensation for its lower systematic risk. Holding cash flows equal, the lower-beta firm would be worth more simply because its cash flows are discounted at a gentler rate.

## Limitations and Caveats

- **Beta is unstable and backward-looking.** It is estimated from historical price data and can shift materially across measurement windows, making the output sensitive to the estimation period.
- **The equity risk premium is contested.** There is no consensus value; estimates range from ~3% to ~7% depending on whether one uses historical averages, implied (forward-looking) premia, or survey data. This single assumption can swing the cost of equity by several percentage points.
- **CAPM is a single-factor model.** It captures only market risk via beta. Multi-factor models (e.g., Fama-French) add size, value, profitability, and other factors that empirically explain returns CAPM misses.
- **It is an estimate, not a fact.** Two competent analysts can derive materially different costs of equity for the same firm. Best practice is to compute a *range* and stress-test the valuation across it rather than relying on a single point estimate.
- **Not appropriate as the firm-wide discount rate when debt is material.** For valuing the whole enterprise (debt + equity), use [[weighted-average-cost-of-capital|WACC]], of which the cost of equity is only one component.

## Related

- [[weighted-average-cost-of-capital]] -- blends cost of equity and cost of debt
- [[capm]] -- the standard model for estimating cost of equity
- [[discount-rate]] -- the broader concept of which cost of equity is one form
- [[dividend-discount-model]] -- alternative estimation via dividends and growth
- [[risk-free-rate]] -- the Rf input
- [[equity-risk-premium]] -- the market premium input
- [[beta]] -- the systematic-risk input
- [[cost-of-debt]] -- the other half of the capital-cost picture
- [[discounted-cash-flow]] -- where cost of equity is applied as a discount rate
- [[valuation]] -- the broader discipline

## Sources

- Sharpe, W. F. (1964) "Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk" -- *Journal of Finance* -- foundational CAPM paper underlying the cost-of-equity formula.
- Damodaran, A. -- *Investment Valuation* and his NYU Stern cost-of-capital and equity-risk-premium datasets -- widely used practitioner references for cost-of-equity estimation.
- Koller, Goedhart, Wessels -- *Valuation: Measuring and Managing the Value of Companies* (McKinsey) -- standard treatment of discount-rate estimation.

---
title: "Weighted Average Cost of Capital"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [fundamental-analysis, valuation, portfolio-theory]
domain: [valuation, portfolio-theory]
prerequisites: ["[[capm]]", "[[cost-of-equity]]"]
difficulty: intermediate
aliases: ["WACC", "Weighted Average Cost of Capital", "Cost of Capital"]
related: ["[[discounted-cash-flow]]", "[[capm]]", "[[cost-of-equity]]", "[[cost-of-debt]]", "[[enterprise-value]]", "[[valuation]]"]
---

The weighted average cost of capital (WACC) is the blended rate of return that a company must earn on its existing assets to satisfy all of its capital providers -- both equity shareholders and debt holders. It represents the opportunity cost of deploying capital within the firm and is the standard discount rate used in [[discounted-cash-flow|discounted cash flow (DCF)]] analysis to convert projected future free cash flows into a present value estimate of [[enterprise-value]].

## Formula

WACC is calculated as the weighted average of the cost of equity and the after-tax cost of debt, where the weights reflect the firm's target or actual capital structure:

```
WACC = (E / V) * Re + (D / V) * Rd * (1 - Tc)
```

Where:
- **E** = market value of equity
- **D** = market value of debt
- **V** = E + D (total firm value)
- **Re** = cost of equity, typically estimated using the [[capm|Capital Asset Pricing Model]] (CAPM): Re = Rf + Beta * (Rm - Rf)
- **Rd** = cost of debt (yield on the company's outstanding bonds or borrowing rate)
- **Tc** = corporate tax rate (the tax shield on interest payments reduces the effective cost of debt)

The cost of equity is almost always higher than the after-tax cost of debt because equity holders bear more risk and have no contractual claim to cash flows. This means that increasing leverage (more debt, less equity) can lower WACC up to a point, beyond which financial distress costs and rising debt yields offset the benefit.

## Typical Ranges and Practical Use

WACC varies significantly by industry, capital structure, and prevailing interest rates. As a rough guide: stable utilities might have a WACC of 5-7%, large-cap industrials 7-10%, and high-growth technology firms 10-15% or higher. In a DCF model, small changes in WACC produce large changes in the resulting valuation, making it one of the most sensitive inputs. Analysts should stress-test DCF outputs across a range of WACC assumptions rather than relying on a single point estimate. Common pitfalls include using book values of debt and equity instead of market values, applying a single beta estimate without considering its instability over time, and failing to adjust for country risk when valuing firms in emerging markets.

## ROIC vs WACC: The Value-Creation Test

The single most important use of WACC outside of DCF is the **ROIC > WACC** test. A firm creates economic value only when its return on invested capital exceeds its cost of capital; if ROIC < WACC, the firm destroys value with every dollar it reinvests, no matter how fast revenue grows. The spread (ROIC − WACC) is the cleanest quantitative summary of whether a business has a durable competitive advantage. This frames "economic profit" (a.k.a. EVA):

```
Economic Profit = (ROIC − WACC) * Invested Capital
```

A company growing rapidly while earning ROIC below its WACC (common among cash-burning growth firms) is mathematically diminishing shareholder value even as the top line expands — a distinction headline earnings growth hides.

## Trading and Investing Relevance

- **Mispriced discount rates create the value opportunity.** Markets routinely over-extrapolate near-term growth and under-price the discount rate, especially for long-duration growth equities. Because terminal value dominates DCF and is discounted at WACC, a 1pp error in WACC can swing fair value by 20-40% for a high-growth name. Long-duration assets behave like long-duration bonds: their valuations are acutely sensitive to the risk-free rate embedded in the [[cost-of-equity]], which is why richly-valued tech sold off sharply in the 2022 rate-hike cycle.
- **Capital-allocation screens.** Quality and quant strategies screen for persistent ROIC − WACC spreads as a proxy for moat (see [[quality-anomaly]]). Firms that aggressively reinvest below their cost of capital are flagged by the [[anomalies/asset-growth-anomaly|asset-growth anomaly]] and [[anomalies/investment-anomaly|investment anomaly]] as future underperformers.
- **Capital-structure events.** Buybacks, debt issuance, and recapitalizations change the E/V and D/V weights and therefore WACC; merger-arb and event-driven desks model the post-deal WACC to value synergies.
- **Macro sensitivity.** Rising rates lift both Rf (cost of equity) and Rd (cost of debt), raising WACC across the board and compressing valuations market-wide — a key transmission channel from central-bank policy to equity prices.

## Sources

- Modigliani, F. & Miller, M. (1958) "The Cost of Capital, Corporation Finance and the Theory of Investment" — *American Economic Review* — foundational capital-structure theory.
- Koller, Goedhart, Wessels — *Valuation: Measuring and Managing the Value of Companies* (McKinsey) — practitioner standard on WACC estimation and the ROIC-WACC framework.
- Damodaran, A. — *Investment Valuation* and his online cost-of-capital datasets (NYU Stern) — widely used industry WACC and beta references.

## Related

- [[discounted-cash-flow]]
- [[discount-rate]]
- [[terminal-value]]
- [[capm]]
- [[cost-of-equity]]
- [[cost-of-debt]]
- [[enterprise-value]]
- [[valuation]]
- [[quality-anomaly]]

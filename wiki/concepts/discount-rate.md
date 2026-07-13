---
title: "Discount Rate"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, portfolio-theory]
aliases: ["Discount Rate", "Required Rate of Return", "Hurdle Rate", "Required Return"]
domain: [fundamental-analysis, valuation, portfolio-theory]
prerequisites: ["[[discounted-cash-flow]]", "[[capm]]"]
difficulty: intermediate
related: ["[[discounted-cash-flow]]", "[[weighted-average-cost-of-capital]]", "[[cost-of-equity]]", "[[capm]]", "[[terminal-value]]", "[[dividend-discount-model]]", "[[risk-free-rate]]", "[[intrinsic-value]]", "[[valuation]]", "[[treasury-bonds]]"]
---

The **discount rate** is the rate of return used to convert future cash flows into their present value. It answers the question "what is a dollar received in the future worth today?" and is the single most powerful lever in any [[discounted-cash-flow|discounted cash flow]] or [[dividend-discount-model|dividend discount]] valuation. Conceptually it bundles two things: the **time value of money** (a dollar today can be invested to earn a return, so a future dollar is worth less) and **risk** (the less certain a future cash flow, the more it should be discounted). It is also called the *required rate of return* or *hurdle rate* — the minimum return an investor demands to bear the risk of the cash flow.

## The math

The present value of a single future cash flow is:

```
PV = CF_t / (1 + r)^t

where  CF_t = cash flow in year t,
       r    = discount rate,
       t    = number of years until the cash flow arrives
```

The discount *factor* `1 / (1 + r)^t` shrinks toward zero as either the rate `r` or the horizon `t` grows — which is why far-future cash flows (and the [[terminal-value|terminal value]]) are so sensitive to the chosen rate. The full value of an asset sums this expression across every future cash flow.

## Choosing the right rate

The correct discount rate depends on *whose* cash flow is being discounted — mixing them is a classic valuation error:

| Cash flow being discounted | Correct discount rate | Why |
|---|---|---|
| Free cash flow to the **firm** (pre-financing) | [[weighted-average-cost-of-capital\|WACC]] | Blends the return required by *all* capital providers |
| Free cash flow to **equity** / dividends | [[cost-of-equity\|Cost of equity]] | Only equity holders' required return |
| A risk-free cash flow (e.g. a Treasury) | Risk-free rate | No default/risk premium needed |

The cost of equity itself is usually built up from a **[[risk-free-rate|risk-free rate]] plus a risk premium**, most commonly via [[capm|CAPM]]:

```
Cost of equity = R_f + Beta * (R_m - R_f)

R_f = risk-free rate (often the 10-year [[treasury-bonds|Treasury]] yield)
Beta = sensitivity of the stock to the market
(R_m - R_f) = equity risk premium
```

So the discount rate ties valuation directly to macro conditions: when the risk-free rate rises, every discount rate rises, and the present value of all future cash flows falls.

## Key assumptions and their sensitivity

The discount rate is the most sensitive input in intrinsic valuation, for the same reason that long-duration bonds are the most rate-sensitive bonds — value lives far out in the future and is heavily compounded.

- **Duration effect.** The further out a cash flow, the more a change in `r` moves its present value. High-growth firms (whose value is concentrated in distant cash flows and the terminal value) are "long-duration equities" and re-rate violently when rates move — the mechanism behind the 2022 sell-off in richly-valued tech.
- **Magnitude.** A 1-percentage-point change in the discount rate can swing an intrinsic-value estimate by 15–30%, and more for long-duration names. Because of this, analysts present valuations as a *range* across discount-rate scenarios, never a single point estimate (see the sensitivity grids in [[discounted-cash-flow]] and [[weighted-average-cost-of-capital]]).
- **Consistency with growth.** The relationship between the discount rate `r` and the perpetual growth rate `g` governs the terminal value; `g` must stay safely below `r` or the valuation diverges.

## How ALFRED-style fundamental analysis uses it

- **Set it deliberately, stress-test it always.** ALFRED-style [[fundamental-analysis]] treats the discount rate as a primary assumption to be justified (risk-free rate + a sensible risk premium for the business) and then varied across a range, rather than a number to be reverse-engineered to hit a target price.
- **Reverse approach.** Holding price fixed and solving for the *implied* discount rate (or implied growth) reveals what the market is assuming — a useful cross-check against the analyst's own required return.
- **Hurdle-rate discipline.** Used as a hurdle rate, the discount rate is the bar a prospective investment's expected return must clear; pairing it with a [[margin-of-safety|margin of safety]] keeps position decisions honest about uncertainty.

## Limitations

- **Unobservable.** The "true" discount rate for a given company is not observable; the risk premium and beta are estimated with wide error bars.
- **Single-rate simplification.** Applying one constant rate to every future year assumes a stable risk and rate environment that rarely holds; more refined models vary the rate by period.
- **Garbage-in dominance.** Because the output is so sensitive, the discount rate can quietly become the assumption that decides the answer — making transparent, stress-tested rates essential to avoid false precision.

## Worked example (hypothetical)

> The figures below are illustrative and do not refer to any real company.

Consider a single cash flow of **$1,000 to be received in 5 years**. Its present value under three different discount rates:

```
At  5%:  PV = 1,000 / (1.05)^5 = 1,000 / 1.2763 = $783.53
At  8%:  PV = 1,000 / (1.08)^5 = 1,000 / 1.4693 = $680.58
At 12%:  PV = 1,000 / (1.12)^5 = 1,000 / 1.7623 = $567.43
```

The same future $1,000 is worth **$784, $681, or $567 today** depending only on the rate chosen — a 28% range from moving the discount rate across a plausible band. Push the horizon to 20 years and the spread widens dramatically, which is exactly why long-duration cash flows and terminal values demand the most careful rate selection.

## Related

- [[discounted-cash-flow]] — the method that applies the discount rate
- [[weighted-average-cost-of-capital]] — the discount rate for whole-firm cash flows
- [[cost-of-equity]] — the discount rate for equity / dividend cash flows
- [[capm]] — the standard way to estimate the cost of equity
- [[terminal-value]] — the component most sensitive to the discount rate
- [[dividend-discount-model]] — discounts dividends at the cost of equity
- [[risk-free-rate]] — the floor the discount rate is built on
- [[intrinsic-value]] — the output the discount rate helps produce
- [[treasury-bonds]] — the usual source of the risk-free rate input
- [[valuation]] — broader context

## Sources

- Fisher, I. *The Theory of Interest* (Macmillan, 1930) — foundational treatment of the time value of money and discounting.
- Sharpe, W.F. (1964). "Capital Asset Prices." *Journal of Finance* — the CAPM derivation of a risk-adjusted required return.
- Damodaran, A. *Investment Valuation* (3rd ed., Wiley, 2012) and his cost-of-capital datasets (NYU Stern) — discount-rate estimation and equity-risk-premium references.

---
title: "Terminal Value"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, stocks]
aliases: ["Terminal Value", "TV", "Continuing Value", "Horizon Value"]
domain: [fundamental-analysis, valuation]
prerequisites: ["[[discounted-cash-flow]]", "[[discount-rate]]"]
difficulty: advanced
related: ["[[discounted-cash-flow]]", "[[dcf-analysis]]", "[[weighted-average-cost-of-capital]]", "[[discount-rate]]", "[[dividend-discount-model]]", "[[ev-ebitda]]", "[[free-cash-flow]]", "[[valuation]]", "[[intrinsic-value]]"]
---

**Terminal value (TV)** is the estimated value of all the cash flows a business will generate *after* the explicit forecast period of a [[discounted-cash-flow|discounted cash flow]] model. Because a company is assumed to operate indefinitely but no one can forecast year-by-year cash flows forever, a DCF projects perhaps 5–10 years in detail and then collapses everything beyond that horizon into a single lump-sum terminal value, which is itself discounted back to the present. In most DCF models the terminal value accounts for the **majority of total value** — commonly 60–80% — which makes its assumptions the single most consequential part of the valuation.

## The two methods

There are two standard ways to compute terminal value, and a disciplined analyst usually runs both as cross-checks.

### 1. Perpetuity growth (Gordon Growth) method

Assumes free cash flow grows at a constant rate `g` forever after the final explicit year `n`:

```
TV_n = FCF_n * (1 + g) / (r - g)

where  FCF_n = free cash flow in the final forecast year,
       g     = perpetual growth rate (long-run, capped near GDP),
       r     = discount rate ([[weighted-average-cost-of-capital|WACC]] for firm cash flows)
```

`TV_n` is the value *as of year n* and must then be discounted back to today by dividing by `(1 + r)^n`. This is the same formula that powers the [[dividend-discount-model|Gordon Growth Model]] — applied to the DCF tail rather than the whole stock.

### 2. Exit multiple method

Applies a valuation multiple — typically [[ev-ebitda|EV/EBITDA]], or sometimes EV/FCF — to the final forecast year's metric, as if the business were sold at the horizon at prevailing market multiples:

```
TV_n = Exit Multiple * Metric_n     (e.g. 8x * final-year EBITDA)
```

This grounds the terminal value in observable market pricing rather than a perpetual-growth assumption, but it imports relative-valuation risk: the chosen multiple reflects *today's* market sentiment, which may not hold at the horizon.

## Key assumptions and their sensitivity

Terminal value is where small input errors do the most damage, for two reasons: it is the largest component of value, and the perpetuity formula divides by the small number `(r - g)`.

- **The `g ≥ r` trap.** If the perpetual growth rate is set at or above the discount rate, the denominator `(r - g)` goes to zero or negative and the valuation explodes to nonsense. `g` must always be well below `r` and capped at a defensible long-run rate (roughly long-run nominal GDP / inflation, ~2–3%). A firm cannot grow faster than the economy forever, or it would eventually *become* the economy.
- **Lever sensitivity.** A 1-percentage-point change in either `g` or `r` can swing the terminal value — and therefore the whole DCF — by 20–30%. Analysts present a **sensitivity (football-field) table** gridding value against `r` and `g` rather than quoting a single number.
- **Reasonableness checks.** The implied exit multiple from a perpetuity-growth TV should be sanity-checked against current market multiples, and vice versa. If the perpetuity method implies a 40x EV/EBITDA exit for a mature firm, the growth assumption is too aggressive.

## How ALFRED-style fundamental analysis uses it

- **It is the dominant input, so it gets the most scrutiny.** Because the terminal value typically drives most of an intrinsic-value estimate, ALFRED-style [[fundamental-analysis]] treats the `g` and exit-multiple assumptions as the critical levers and stress-tests them explicitly rather than burying them.
- **Cross-method triangulation.** Computing TV both ways — perpetuity growth and exit multiple — and reconciling the two is a built-in error check; a large gap signals an unrealistic growth rate or an out-of-line multiple.
- **Feeds the margin of safety.** Since the terminal value is the least certain part of the model, the [[margin-of-safety|margin of safety]] demanded against a DCF is, in effect, mostly a haircut on terminal-value risk.

## Limitations

- **False precision.** A terminal value carried to the dollar implies a confidence in perpetual cash flows that no one possesses; it is best read as a wide range.
- **Mature-state assumption.** The perpetuity method assumes the firm has reached a stable, steady state by year `n`; if the explicit horizon ends before maturity, the terminal value is misanchored.
- **Multiple-cycle risk.** The exit-multiple method assumes today's market multiples persist to the horizon, which fails across valuation regimes (e.g. a de-rating in interest-rate cycles).
- **Reinvestment consistency.** Perpetual growth requires perpetual reinvestment; a TV that assumes growth without the capital expenditure to fund it overstates value.

## Worked example (hypothetical)

> The figures below are illustrative and do not refer to any real company.

A hypothetical firm's DCF forecasts **$120M of free cash flow in the final explicit year (year 5)**, with a **WACC of 9%**.

**Perpetuity-growth method** (perpetual growth `g` = 2.5%):

```
TV_5 = 120 * (1 + 0.025) / (0.09 - 0.025) = 123 / 0.065 = $1,892M  (value at year 5)
Discount to today: 1,892 / (1.09)^5 = 1,892 / 1.5386 = $1,230M
```

**Exit-multiple method** (8x EV/EBITDA on year-5 EBITDA of $200M):

```
TV_5 = 8 * 200 = $1,600M  (value at year 5)
Discount to today: 1,600 / 1.5386 = $1,040M
```

The two methods give present-day terminal values of roughly **$1,230M vs $1,040M** — an ~18% spread from two reasonable approaches. An analyst would investigate the gap (here the perpetuity method implies a richer exit multiple of ~9.5x), perhaps settle on a blended figure, and run the `g`/`r` grid to bound the range before trusting any single number.

## Related

- [[discounted-cash-flow]] — terminal value is one of its three components
- [[dcf-analysis]] — step-by-step DCF that builds a terminal value
- [[weighted-average-cost-of-capital]] — the `r` used to grow and discount the TV
- [[discount-rate]] — the rate that discounts the terminal value back to today
- [[dividend-discount-model]] — uses the identical Gordon-Growth perpetuity formula
- [[ev-ebitda]] — the multiple most often used in the exit-multiple method
- [[free-cash-flow]] — the cash flow extrapolated into perpetuity
- [[valuation]] — broader context for intrinsic methods
- [[margin-of-safety]] — the buffer that absorbs terminal-value uncertainty

## Sources

- Gordon, M.J. (1959). "Dividends, Earnings, and Stock Prices." *Review of Economics and Statistics*, 41(2) — the perpetuity-growth model.
- Damodaran, A. *Investment Valuation* (3rd ed., Wiley, 2012) — terminal-value estimation, the `g`-cap rule, and consistency checks.
- Koller, T., Goedhart, M. & Wessels, D. *Valuation: Measuring and Managing the Value of Companies* (McKinsey & Company, Wiley) — continuing-value formula and the reinvestment-consistency constraint.

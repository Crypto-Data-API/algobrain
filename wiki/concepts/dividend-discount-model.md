---
title: "Dividend Discount Model"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, stocks]
aliases: ["DDM", "Dividend Discount Model", "Gordon Growth Model", "Dividend Growth Model", "Gordon-Shapiro Model"]
domain: [fundamental-analysis, valuation]
prerequisites: ["[[discount-rate]]", "[[dividends]]"]
difficulty: intermediate
related: ["[[discounted-cash-flow]]", "[[discount-rate]]", "[[terminal-value]]", "[[cost-of-equity]]", "[[capm]]", "[[dividend-yield]]", "[[intrinsic-value]]", "[[valuation]]", "[[earnings-yield]]"]
---

The **dividend discount model (DDM)** estimates the [[intrinsic-value|intrinsic value]] of a share as the present value of all the dividends it is expected to pay over its life, discounted back at the investor's required rate of return. It is the oldest formal equity-[[valuation]] method and a direct application of the principle that the value of any asset is the present value of the cash it returns to its owner. The DDM is the cash-flow-to-equity special case of [[discounted-cash-flow|discounted cash flow]] where the "cash flow" is the dividend actually paid out.

## The math

In its most general form, value equals the discounted stream of future dividends:

```
            ____  D_t
P_0   =     \    -------
            /___  (1 + r)^t
             t=1
```

Where `P_0` is the fair value today, `D_t` is the dividend in year `t`, and `r` is the [[cost-of-equity|cost of equity]] (the discount rate appropriate to equity cash flows, often estimated with [[capm|CAPM]]).

### Single-stage: the Gordon Growth Model

If dividends are assumed to grow at a constant rate `g` forever, the infinite series collapses to the **Gordon Growth Model** (Gordon & Shapiro, 1956; Gordon, 1959):

```
P_0 = D_1 / (r - g)

where  D_1 = next year's expected dividend,
       r   = required return (cost of equity),
       g   = perpetual dividend growth rate  (must be < r)
```

This is the same perpetuity-growth formula used to compute [[terminal-value|terminal value]] inside a DCF — DDM simply applies it to the *whole* life of the stock rather than the tail.

### Multi-stage DDM

Because few firms grow at one constant rate forever, practitioners use **two-stage** or **three-stage** models: an explicit high-growth phase (each dividend discounted individually), followed by a Gordon-Growth terminal value that captures the mature, steady-state phase. This mirrors the structure of a full DCF.

## Key assumptions and their sensitivity

The DDM has only three real inputs, and two of them are extremely sensitive:

| Input | What it is | Sensitivity |
|---|---|---|
| `D_1` | Next period's dividend | Low–medium (usually observable) |
| `r` | [[cost-of-equity\|Cost of equity]] / required return | **Very high** |
| `g` | Perpetual growth rate | **Very high** |

Because value is `D_1 / (r - g)`, the answer depends on the *difference* between two large, uncertain numbers. As `g` approaches `r`, the denominator collapses toward zero and the valuation explodes toward infinity — the same `g ≥ r` failure mode that breaks terminal-value calculations. A move in `g` from 3% to 4% when `r` is 8% raises value from `D_1/0.05` to `D_1/0.04`, a 25% jump from a single percentage point. For this reason `g` must be capped at a defensible long-run rate (roughly nominal GDP growth, ~2–4%), never above the discount rate.

## How ALFRED-style fundamental analysis uses it

In a fundamental workflow the DDM is most useful as a **sanity check and a reverse-engineering tool**, not a primary price target:

- **Dividend-paying, stable names.** For mature, cash-returning businesses — utilities, consumer staples, REITs, banks, mature infrastructure — where payout is high and predictable, the DDM is often *more* reliable than a full DCF because the dividend is an actual observed cash flow rather than a modeled one. ALFRED's [[fundamental-analysis]] already captures [[dividend-yield|dividend yield]] and [[dividend-payout-ratio|payout ratio]]; the DDM strings those into an intrinsic-value estimate.
- **Reverse DDM.** Hold today's price fixed and solve for the `g` the market is implying: `g = r − D_1/P_0`. If the market is pricing a 6% perpetual dividend-growth rate for a firm that has grown payouts 2% a year, the stock looks demanding; the reverse is a [[margin-of-safety]] candidate.
- **Cross-check against multiples.** The DDM output is triangulated against [[price-to-earnings-ratio|P/E]], [[earnings-yield|earnings yield]] and a DCF, exactly as described in [[valuation]] — convergence raises confidence, divergence flags a modeling problem.

## Limitations

- **Useless for non-dividend payers.** Many growth companies pay no dividend, reinvesting everything; the basic DDM returns zero or undefined value for them. Analysts then fall back to a free-cash-flow DCF or use total payout (dividends **+** buybacks).
- **Ignores buybacks.** Share repurchases are an economically equivalent return of capital but are invisible to a pure dividend model, understating value for buyback-heavy firms.
- **Payout policy ≠ value creation.** A firm can raise its dividend by under-investing; the DDM rewards the higher payout even when it destroys long-term value. Earnings power, not the distribution decision, ultimately drives worth.
- **Single-rate fragility.** The constant-growth form assumes a stable, perpetual relationship between payout, growth and return that real firms rarely sustain.

## Worked example (hypothetical)

> The figures below are illustrative and do not refer to any real company.

A hypothetical mature utility is expected to pay a **$2.00 dividend next year (`D_1`)**, grow that dividend **4% per year in perpetuity (`g`)**, and an investor requires a **9% return (`r`)**.

```
P_0 = D_1 / (r - g) = 2.00 / (0.09 - 0.04) = 2.00 / 0.05 = $40.00
```

So the model implies a fair value of **$40 per share**. If the stock trades at $32, the reverse DDM solves `g = 0.09 − 2.00/32 = 0.09 − 0.0625 = 2.75%` — i.e. the market is pricing slower dividend growth (2.75%) than the analyst's 4% assumption, suggesting potential undervaluation *if* the 4% estimate holds.

A **two-stage** variant might assume the same $2.00 dividend grows 10% for three years (discounted individually) before settling to 4% forever (a Gordon-Growth [[terminal-value|terminal value]] from year three), producing a higher figure (~$49) that reflects the near-term growth burst.

## Related

- [[discounted-cash-flow]] — the general method; DDM is its dividend-only special case
- [[terminal-value]] — uses the identical Gordon-Growth perpetuity formula
- [[discount-rate]] — the `r` in the model; for equity this is the cost of equity
- [[cost-of-equity]] — typically estimated with [[capm|CAPM]] for DDM inputs
- [[dividend-yield]] — the current-yield building block of the model
- [[intrinsic-value]] — the quantity the DDM estimates
- [[valuation]] — overview of where DDM sits among methods
- [[margin-of-safety]] — the discount demanded against the DDM estimate

## Sources

- Williams, J.B. *The Theory of Investment Value* (Harvard University Press, 1938) — the original statement that a stock is worth the present value of its future dividends.
- Gordon, M.J. & Shapiro, E. (1956). "Capital Equipment Analysis: The Required Rate of Profit." *Management Science* — the constant-growth dividend formula.
- Gordon, M.J. (1959). "Dividends, Earnings, and Stock Prices." *Review of Economics and Statistics*, 41(2).
- Damodaran, A. *Investment Valuation* (3rd ed., Wiley, 2012) — multi-stage DDM construction and discount-rate estimation.

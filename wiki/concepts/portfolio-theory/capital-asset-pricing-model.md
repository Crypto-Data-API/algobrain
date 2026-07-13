---
title: "Capital Asset Pricing Model (CAPM)"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [portfolio-theory, valuation, risk-management]
aliases: ["CAPM", "Capm", "Capital Asset Pricing Model", "Security Market Line"]
related: ["[[modern-portfolio-theory]]", "[[efficient-frontier]]", "[[beta]]", "[[alpha]]", "[[sharpe-ratio]]", "[[diversification]]", "[[discounted-cash-flow]]", "[[multi-factor-portfolio]]", "[[value-factor]]", "[[equity-risk-premium]]", "[[risk-free-rate]]", "[[capital-market-line]]", "[[weighted-average-cost-of-capital]]"]
domain: [portfolio-theory]
prerequisites: ["[[modern-portfolio-theory]]", "[[beta]]", "[[diversification]]"]
difficulty: intermediate
---

The **Capital Asset Pricing Model (CAPM)** is an equilibrium model that prices a risky asset's expected return as a linear function of its sensitivity to overall market risk ([[beta]]). It formalizes the intuition that investors are compensated only for *systematic* (non-diversifiable) risk, not for idiosyncratic risk that can be eliminated through [[diversification]], and it provides the discount rate (cost of equity) used in most [[discounted-cash-flow|DCF]] valuation.

## The Formula

$$ E(R_i) = R_f + \beta_i \,\big(E(R_m) - R_f\big) $$

where:

- $E(R_i)$ = expected return of asset $i$
- $R_f$ = risk-free rate (typically the yield on short- or long-dated government bonds — e.g. the 10-year US Treasury)
- $\beta_i$ = beta of asset $i$ = $\dfrac{\mathrm{Cov}(R_i, R_m)}{\mathrm{Var}(R_m)}$, its return sensitivity to the market
- $E(R_m)$ = expected return of the market portfolio
- $E(R_m) - R_f$ = the **equity risk premium** (historically ~4-6% per year for US equities)

A stock with $\beta = 1$ moves one-for-one with the market and earns the full market return. A stock with $\beta = 1.5$ is expected to return $R_f + 1.5 \times$ the risk premium — more return for more systematic risk. A stock with $\beta = 0.5$ (a defensive utility, say) earns less. The line that plots $E(R_i)$ against $\beta$ is the **Security Market Line (SML)**.

## Worked Example

Take a risk-free rate of $R_f = 4\%$ (≈ the 10-year US Treasury yield) and an expected market return of $E(R_m) = 10\%$, so the [[equity-risk-premium|equity risk premium]] is $E(R_m) - R_f = 6\%$. CAPM then gives the required return for any beta:

| Asset | Beta ($\beta$) | CAPM calculation | Expected return |
|-------|:-------------:|------------------|:---------------:|
| Cash / T-bill | 0.0 | $4\% + 0.0 \times 6\%$ | **4.0%** |
| Defensive utility | 0.5 | $4\% + 0.5 \times 6\%$ | **7.0%** |
| Market / index fund | 1.0 | $4\% + 1.0 \times 6\%$ | **10.0%** |
| High-beta growth stock | 1.5 | $4\% + 1.5 \times 6\%$ | **13.0%** |
| Leveraged cyclical | 2.0 | $4\% + 2.0 \times 6\%$ | **16.0%** |

So a stock with $\beta = 1.5$ must be **expected** to return 13% just to compensate for its systematic risk. If your fundamental analysis says it will return only 11%, CAPM judges it overpriced (it plots *below* the SML); if you expect 15%, it is underpriced (it plots *above* the SML) and offers positive [[alpha]].

## The Security Market Line (SML)

The SML is CAPM plotted in $(\beta, \text{expected return})$ space: a straight line that starts at $R_f$ when $\beta = 0$ and rises with slope equal to the equity risk premium. In the example above, the SML runs from $(0, 4\%)$ through $(1.0, 10\%)$ with a slope of 6% per unit of beta.

- **On the line** — the asset is fairly priced; its expected return exactly matches its systematic risk.
- **Above the line** — undervalued; expected return exceeds the CAPM-required return → buy.
- **Below the line** — overvalued; expected return falls short of what its risk demands → avoid or short.

The SML differs from the [[capital-market-line|Capital Market Line (CML)]]: the CML prices *efficient portfolios* against total risk (standard deviation), whereas the SML prices *any individual asset* against systematic risk ([[beta]]).

## Why It Works: The Logic of Systematic Risk

CAPM rests on the [[modern-portfolio-theory|Markowitz]] insight that rational investors hold the [[efficient-frontier|efficient]] market portfolio and lend/borrow at $R_f$. Because idiosyncratic risk washes out in a diversified book, the market will not pay a premium for it — only for the risk that *cannot* be diversified away, i.e. covariance with the market. Beta is the precise measure of that covariance. Developed independently by William Sharpe (1964, Nobel 1990), John Lintner (1965), and Jan Mossin (1966), CAPM was the first formal theory linking risk to required return.

## Trading and Portfolio Relevance

- **Cost of equity for valuation.** CAPM supplies the discount rate in a [[discounted-cash-flow]] model. A higher beta raises the discount rate and lowers fair value, all else equal.
- **Performance attribution.** Realized return minus CAPM-predicted return is **[[alpha]]** (Jensen's alpha) — the part of a manager's return not explained by market exposure. This is the foundational definition of skill versus beta.
- **Hedging and exposure budgeting.** Beta tells you how much index exposure a position carries, enabling beta-neutral or beta-targeted construction.
- **Benchmark for factor models.** CAPM is the single-factor base case that [[multi-factor-portfolio|multi-factor models]] (Fama-French, Carhart) extend by adding size, [[value-factor|value]], momentum, and quality factors to explain returns CAPM leaves unexplained.
- **Cost of capital.** CAPM's cost of equity is one input to the [[weighted-average-cost-of-capital|WACC]], the blended hurdle rate firms use for capital budgeting.

## CAPM Assumptions

CAPM is an equilibrium model that holds only under a tight set of idealized assumptions:

| Assumption | Reality check |
|------------|---------------|
| Investors are rational, risk-averse mean-variance optimizers | Behavioral biases pervade real markets |
| A single holding period | Investors have many horizons |
| Frictionless markets — no taxes, no transaction costs | Costs and taxes are material |
| Unlimited borrowing/lending at the [[risk-free-rate]] | Borrowing rates exceed lending rates |
| Homogeneous expectations (everyone agrees on inputs) | Forecasts diverge widely |
| A single, observable "market portfolio" of *all* assets | Only proxied by an index (Roll's critique) |
| All assets are perfectly divisible and liquid | Many are not |

Each violated assumption is a wedge between the clean theory and messy empirical returns — and the source of CAPM's documented limitations below.

## Limitations

Empirically, the SML is too flat: low-beta stocks earn *more* than CAPM predicts and high-beta stocks earn *less* (the "low-volatility anomaly"). The model assumes a single period, frictionless markets, homogeneous expectations, and that the unobservable "market portfolio" can be proxied by an index (Roll's critique). These failures motivated the Arbitrage Pricing Theory and the Fama-French factor models, which remain CAPM's direct descendants. Despite this, CAPM endures as the standard teaching framework and the default cost-of-equity estimator in corporate finance.

## Related

- [[modern-portfolio-theory]] — the framework CAPM builds on
- [[efficient-frontier]] — the set of optimal risk-return portfolios
- [[beta]] — the single risk input CAPM prices
- [[alpha]] — return in excess of the CAPM prediction
- [[multi-factor-portfolio]] — models that extend CAPM with additional factors
- [[discounted-cash-flow]] — uses CAPM's cost of equity as a discount rate

## Sources

- Sharpe, William F. "Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk." *Journal of Finance* (1964).
- Lintner, John. "The Valuation of Risk Assets and the Selection of Risky Investments in Stock Portfolios and Capital Budgets." *Review of Economics and Statistics* (1965).
- Fama, Eugene F., and Kenneth R. French. "The Capital Asset Pricing Model: Theory and Evidence." *Journal of Economic Perspectives* (2004).
- Bodie, Kane, Marcus. *Investments* — standard textbook treatment of CAPM and the SML.

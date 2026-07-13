---
title: "Covariance"
type: concept
created: 2026-06-30
updated: 2026-07-02
status: good
tags: [portfolio-theory, quantitative, correlation, risk-management]
aliases: ["Covariance Matrix", "Cov", "Variance-Covariance Matrix"]
domain: [portfolio-theory, quantitative]
prerequisites: ["[[volatility]]", "[[correlation]]"]
difficulty: intermediate
related:
  - "[[correlation]]"
  - "[[volatility]]"
  - "[[diversification]]"
  - "[[modern-portfolio-theory]]"
  - "[[efficient-frontier]]"
  - "[[mean-variance-optimization]]"
  - "[[beta]]"
  - "[[value-at-risk]]"
  - "[[risk-parity]]"
---

# Covariance

**Covariance** measures how two assets' returns move *together*: positive covariance means they tend to rise and fall in tandem, negative covariance means one tends to rise when the other falls, and zero covariance means there is no linear relationship. It is the raw statistical ingredient behind [[diversification]], [[correlation]], [[beta]], and the entire machinery of [[modern-portfolio-theory|Modern Portfolio Theory]]. Where correlation answers *"in which direction and how reliably?"*, covariance also carries the *magnitude* of the assets' movements — which is exactly what a portfolio's risk math needs.

## Formula

For two assets with returns X and Y over n periods, with means X̄ and Ȳ:

```
Cov(X, Y) = (1/n) · Σ (Xᵢ − X̄)(Yᵢ − Ȳ)
```

Each term multiplies the two assets' deviations from their own averages. When both assets are above (or both below) their means at the same time, the product is positive; when they are on opposite sides, it is negative. Summing tells you whether co-movement is, on balance, positive or negative.

A few identities make covariance easy to reason about:

- **An asset with itself is its variance:** `Cov(X, X) = Var(X) = σ²`.
- **Covariance, volatility, and correlation are linked:** `Cov(X, Y) = ρ · σ_X · σ_Y`, where ρ is the [[correlation]] coefficient. This is the bridge between the two measures.
- **[[beta|Beta]] is a scaled covariance:** `β = Cov(asset, market) / Var(market)`.

## Covariance vs Correlation

These are constantly confused. They describe the same relationship but answer different questions:

| Property | Covariance | [[correlation\|Correlation]] |
|---|---|---|
| Range | −∞ to +∞ | −1 to +1 |
| Units | Return × return (scale-dependent) | Dimensionless |
| Tells you | Direction **and** magnitude of co-movement | Direction and *strength*, stripped of scale |
| Best use | The math input to portfolio variance and optimizers | Intuitive, comparable measure across any pair |

Correlation is simply the *standardised* covariance — divide covariance by the product of the two volatilities and you get a number between −1 and +1 you can compare across asset pairs. Covariance keeps the units, which is precisely why it is the quantity that plugs into the portfolio-variance formula.

## Why It Is the Engine of Portfolio Risk

Portfolio risk is *not* the average of the individual asset risks — it depends on how the assets co-move. For a two-asset portfolio with weights w₁, w₂:

```
σ_portfolio² = w₁²σ₁² + w₂²σ₂² + 2·w₁·w₂·Cov(1, 2)
```

The entire benefit of [[diversification]] lives in that final covariance term. Low or negative covariance shrinks portfolio variance below the weighted average of the parts — the "free lunch" of diversification. For a portfolio of many assets, this generalises to the **covariance matrix** Σ, and total variance is `wᵀ Σ w`, where w is the vector of weights. That matrix — variances on the diagonal, covariances off it — is the single object that [[mean-variance-optimization|mean-variance optimization]], the [[efficient-frontier|efficient frontier]], [[risk-parity]], and parametric [[value-at-risk]] all consume.

## Worked Example (hypothetical)

Two assets over five periods (returns in %):

- Asset A: +2, −1, +3, −2, +1 → mean = +0.6%
- Asset B: +1, −1, +2, −1, +1 → mean = +0.4%

Take the deviations from each mean and multiply the paired deviations:

| Period | A − Ā | B − B̄ | Product |
|---|---|---|---|
| 1 | +1.4 | +0.6 | +0.84 |
| 2 | −1.6 | −1.4 | +2.24 |
| 3 | +2.4 | +1.6 | +3.84 |
| 4 | −2.6 | −1.4 | +3.64 |
| 5 | +0.4 | +0.6 | +0.24 |
| | | **Σ** | **10.80** |

`Cov(A, B) = 10.80 / 5 = +2.16` (in %²) — a **positive** covariance, so A and B mostly move the same direction. To standardise it, compute each standard deviation: `σ_A = √(17.2/5) ≈ 1.86%` and `σ_B = √(7.2/5) = 1.20%`. Then the [[correlation]] is `ρ = 2.16 / (1.86 × 1.20) ≈ 0.97` — not just positive but very tight, so holding both delivers almost no diversification. The covariance gave the magnitude (2.16 %²); the correlation (0.97) made it comparable across any pair. (Figures are illustrative.)

## Practical Notes and Rules of Thumb

- **You almost always look at correlation, but optimize on covariance.** Humans reason in correlation (−1 to +1); the optimizer needs the covariance matrix because it carries the volatility scaling.
- **The covariance matrix is hard to estimate well.** With many assets there are far more pairwise covariances than data points, so raw estimates are noisy. Practitioners apply *shrinkage* (e.g., Ledoit-Wolf) or factor models to stabilise it — otherwise [[mean-variance-optimization|optimizers]] produce extreme, unstable weights ("error maximisation").
- **It is non-stationary.** Covariances drift with regime and spike in crises as [[correlation-breakdown|correlations converge toward +1]] — the diversification the matrix promised weakens exactly when it is needed. Stress-test with crisis-period covariances, not calm-market averages.
- **Use returns, not prices.** Covariance of raw price *levels* is spurious; always compute it on returns. The estimate also depends on the return frequency and lookback window.

## Limitations

- **Linear only.** Covariance captures linear co-movement; assets can have near-zero covariance yet be strongly dependent in the tails (see [[tail-risk]]). This is why covariance-based [[value-at-risk]] understates crisis risk.
- **Scale makes it hard to read directly.** Because it is not bounded, a covariance number alone says little until standardised into [[correlation]].
- **Estimation error dominates in high dimensions.** The number of parameters grows with the square of the asset count, so large covariance matrices are mostly noise without shrinkage or a factor structure.

## Related

- [[correlation]] — the standardised, dimensionless version of covariance
- [[volatility]] — the diagonal of the covariance matrix is variance (volatility squared)
- [[diversification]] — its benefit lives entirely in the covariance term
- [[modern-portfolio-theory]] — built directly on the covariance matrix
- [[efficient-frontier]] — traced out by optimizing against covariances
- [[mean-variance-optimization]] — consumes the covariance matrix as its core input
- [[beta]] — a covariance with the market, scaled by market variance
- [[value-at-risk]] — parametric VaR is computed from the covariance matrix
- [[risk-parity]] — allocates by risk contribution derived from covariances

## Sources

- Markowitz, H. (1952). "Portfolio Selection." *Journal of Finance* — establishes covariance as the central input to portfolio construction.

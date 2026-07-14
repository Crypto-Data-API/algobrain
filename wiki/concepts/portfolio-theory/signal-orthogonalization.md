---
title: "Signal Orthogonalization"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [portfolio-theory, quantitative, machine-learning, crypto]
aliases: ["Orthogonalization", "Signal Orthogonalization", "Residualization", "Beta Neutralization"]
domain: [portfolio-theory, quantitative]
prerequisites: ["[[correlation]]", "[[capm]]", "[[information-coefficient]]"]
difficulty: advanced
related: ["[[information-coefficient]]", "[[alpha-model]]", "[[multi-factor-portfolio]]", "[[feature-selection-trading]]", "[[feature-engineering-crypto]]", "[[capm]]", "[[correlation]]", "[[btc-dominance]]", "[[crypto-signal-library]]"]
---

**Signal orthogonalization** is the process of stripping out the components of a candidate signal that are already explained by known factors — most importantly **BTC/ETH beta** and **existing signals in the book** — so that what remains is the signal's *unique, independent* contribution. In crypto this is not a nicety but a necessity: almost every raw signal is contaminated with market direction, and a signal that merely re-expresses "BTC went up" adds no diversification, no true [[information-coefficient|breadth]], and no alpha.

## Why this is crypto-acute

In equities you orthogonalize against market, size, value, momentum, etc. In crypto the dominant factor swamps everything else: **BTC-beta explains the majority of the cross-sectional variance of most tokens' returns.** During risk-on and risk-off, correlations across the top ~200 assets converge toward 1 (a [[correlation-breakdown|correlation regime shift]] in reverse). Consequences:

- A "new" on-chain or funding signal often has a high [[information-coefficient|IC]] simply because it co-moves with BTC — which co-moves with everything. Remove BTC-beta and the IC frequently collapses to ~0. If it does, the signal was never alpha; it was leverage on market direction.
- Nominal [[information-coefficient|breadth]] (150 perps) badly overstates *effective* breadth, because the bets are one BTC trade in disguise. The Fundamental Law's `IR ≈ IC × √Breadth` uses **independent** breadth, so beta-contaminated books have far lower IR than their position count suggests.
- Stacking several signals that are each 70%+ BTC-beta gives an [[alpha-model]] the illusion of diversification while concentrating a single directional bet.

## Orthogonalization against BTC/ETH beta (residualization)

The core tool is **regression residualization**. To neutralize a candidate signal (or an asset's returns) against BTC and ETH:

1. Regress the candidate `y` on the factor returns:
   `y_t = α + β_BTC · r_BTC,t + β_ETH · r_ETH,t + ε_t`
2. The **residual `ε_t`** is the orthogonalized signal — the part of `y` uncorrelated with BTC and ETH by construction.
3. Use `ε_t` (or the intercept `α` for return series) as the clean signal for [[information-coefficient|IC]] evaluation and [[alpha-model|alpha modeling]].

For a *portfolio* rather than a signal, the analogue is **beta-neutralization**: size a BTC (and ETH) short against the book so net `β ≈ 0`, isolating the residual return. This is the same math a [[capm|CAPM]]-style regression yields, applied to hedge rather than to residualize.

**Rolling betas.** Crypto betas are unstable — an alt's BTC-beta swings with regime and its own liquidity. Estimate `β` on a rolling / EWMA window (e.g. trailing 30-90d) and re-hedge, rather than assuming a static beta. A stale beta leaves residual market exposure that masquerades as alpha.

## Orthogonalization against existing signals (Gram-Schmidt)

Removing BTC-beta is only step one; a candidate may also duplicate signals already in the book (funding, basis, and OI all read leverage). To isolate what's *incrementally* new, orthogonalize against the existing signal set:

- **Sequential residualization (Gram-Schmidt).** Order signals by priority/robustness. Residualize signal 2 against signal 1, signal 3 against the residuals of 1 and 2, and so on. Each surviving component is orthogonal to all prior ones, so no return-driver is double-counted. Order matters — the first signal keeps its full variance; later ones keep only their unique part.
- **Multivariate residualization.** Regress the candidate on *all* existing signals at once and keep the residual — order-independent, and the standard way to ask "does this add anything the book doesn't already have?"
- **PCA / eigenportfolios.** Replace a correlated block of signals with its principal components; the components are mutually orthogonal by construction, though less interpretable. The first PC of the crypto cross-section is essentially the BTC-beta / market factor — projecting it out is another route to market-neutralization.
- **Symmetric orthogonalization.** When you don't want to privilege any signal's ordering, symmetric (Löwdin) orthogonalization decorrelates the set while keeping each output as close as possible to its original — useful for a stack of co-equal factors.

## Worked example (illustrative)

A desk builds a cross-sectional **exchange-netflow** signal on the top 100 perps and measures rank-IC = **0.05** at a 3-day horizon — looks strong. Diagnostics:
1. **Regress netflow-signal returns on BTC + ETH.** BTC-beta is high; the intercept (alpha) is small.
2. **Recompute IC on the residual.** Rank-IC drops from 0.05 to **~0.02**. Two-fifths of the apparent skill was market direction.
3. **Residualize against the existing funding-carry signal.** IC falls again slightly (netflow and funding both partly encode leverage/positioning).
4. **Conclusion.** The signal keeps a small but *genuinely independent* ~0.015-0.02 IC — worth a modest, beta-neutral allocation, but nowhere near the 0.05 headline. Sizing it off the raw IC would have over-bet a mostly-directional trade (numbers illustrative).

The general lesson: **the orthogonalized IC, not the raw IC, is what determines a signal's true contribution and size.**

## Implementation sketch

```python
# Residualize a candidate signal against BTC/ETH beta, then re-score it.
# All inputs are aligned, point-in-time, and use only past data for the fit.
import numpy as np, statsmodels.api as sm

def orthogonalize(y, factor_returns, window=60):
    # y: candidate signal-return series; factor_returns: DataFrame [r_btc, r_eth]
    resid = np.full_like(y, np.nan, dtype=float)
    for t in range(window, len(y)):
        X = sm.add_constant(factor_returns.iloc[t-window:t])   # rolling window
        beta = sm.OLS(y[t-window:t], X).fit().params           # fit on PAST only
        x_t = np.r_[1.0, factor_returns.iloc[t].values]
        resid[t] = y[t] - x_t @ beta                           # residual = clean signal
    return resid                                               # feed to rank-IC / alpha model
```

The same loop generalizes to Gram-Schmidt: replace `factor_returns` with the matrix of already-accepted signals and residualize each new candidate against them in priority order.

## Beta-neutral vs. dollar-neutral vs. orthogonalized

These are often conflated but differ:
- **Dollar-neutral** — equal long and short notional. Says nothing about market exposure; a dollar-neutral alt book can still be net-long BTC-beta.
- **Beta-neutral** — net factor beta ≈ 0 after hedging BTC/ETH. Removes market *return* exposure.
- **Orthogonalized signal** — the *forecast* is statistically independent of the factors. You can hold an orthogonalized signal and still choose to run it beta-neutral or not at the portfolio stage. Orthogonalization is about *measuring and isolating* independent skill; neutralization is about *hedging* the resulting positions.

## Pitfalls

- **Over-orthogonalizing.** Residualize against too many correlated "factors" and you can regress away real alpha, leaving only noise. Keep the factor set economically motivated (BTC, ETH, maybe a size/liquidity and a momentum factor).
- **Unstable betas → residual leakage.** A stale or mis-estimated beta leaves market exposure in the "residual." Use rolling betas and re-check the residual's beta is ~0.
- **Look-ahead in the regression.** Betas must be estimated only on data available at decision time; fitting beta on the full sample leaks the future.
- **Order dependence in Gram-Schmidt.** The sequence changes which signal "owns" shared variance; document and justify the ordering, or use the order-independent multivariate residual.
- **Neutralizing the very thing you want.** If your edge *is* a smarter market-timing signal, fully beta-neutralizing it removes the bet. Orthogonalize to *measure* independence; choose deliberately whether to hedge the beta or keep it.

## Getting the Data (CryptoDataAPI)

Orthogonalization needs the candidate signal plus BTC/ETH return series (the factors) over the same window:

**Factor returns (BTC/ETH beta):**
- `GET /api/v1/market-data/btc-price-history?days=365` — BTC daily history for beta estimation
- `GET /api/v1/backtesting/klines?symbol=BTCUSDT&interval=1d&limit=1000` and `?symbol=ETHUSDT` — BTC/ETH return factors, historical
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1h` — intraday factor returns for shorter-horizon residualization

**Candidate signal series (examples):**
- `GET /api/v1/on-chain/exchange-flows/{symbol}` — netflow candidate
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding candidate
- `GET /api/v1/backtesting/funding` — funding history to align with factor returns

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/btc-price-history?days=365"
```

Auth: `X-API-Key` header. Category pages: [[cryptodataapi-market-data]], [[cryptodataapi-on-chain]], [[cryptodataapi-backtesting]].

## Related

- [[information-coefficient]] — recompute IC on the residual to find true skill
- [[alpha-model]] — orthogonal signals restore genuine breadth in the combiner
- [[multi-factor-portfolio]] — the factor framework residualization lives inside
- [[feature-selection-trading]] — orthogonalization as an alternative to dropping correlated features
- [[capm]] — the beta regression underlying market-neutralization
- [[btc-dominance]] — the market factor most crypto signals are contaminated by

## Sources

- Grinold, Richard, and Ronald Kahn. *Active Portfolio Management* (2000) — factor residualization and independent breadth
- [[book-machine-learning-for-asset-managers]] — de Prado on denoising, feature clustering, and orthogonal features
- [[book-advances-in-financial-ml]] — orthogonal features and avoiding substitution effects

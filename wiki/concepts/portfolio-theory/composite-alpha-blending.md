---
title: "Composite Alpha Blending"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [portfolio-theory, quantitative, algorithmic, machine-learning]
aliases: ["Composite Alpha Blending", "Signal Blending", "Alpha Combination", "Signal Ensemble", "Composite Score"]
domain: [portfolio-theory, quantitative]
prerequisites: ["[[alpha-model]]", "[[information-coefficient]]"]
difficulty: advanced
related: ["[[alpha-model]]", "[[information-coefficient]]", "[[signal-orthogonalization]]", "[[information-ratio]]", "[[multi-factor-portfolio]]", "[[hyperliquid-baskets-overview]]", "[[funding-rate]]", "[[open-interest]]", "[[ml-crypto-price-prediction]]"]
---

# Composite Alpha Blending

**Composite alpha blending** is the process of combining many individually-weak trading signals into a single, stronger **composite score** (or ensemble prediction). No single crypto signal — funding extremes, OI divergence, exchange netflows, regime state, market breadth — is reliable on its own; each has a low [[information-coefficient|Information Coefficient]] and fires wrongly often. Blended intelligently, their independent errors partly cancel and their common signal reinforces, producing a composite whose IC and stability exceed any component. This is the [[alpha-model|alpha model]]'s combination step, and it is distinct from — and upstream of — capital allocation.

## Why Blending Raises Performance

The **Fundamental Law of Active Management** (Grinold) frames the payoff:

```
IR ≈ IC × √Breadth
```

The [[information-ratio|Information Ratio]] scales with the *quality* of each forecast (IC) and the number of *independent* bets (breadth). Blending helps on both axes: averaging diversifies away idiosyncratic signal noise (raising effective IC), and stacking several genuinely different signals adds breadth. The crucial word is **independent** — the breadth term collapses if the signals are really the same bet in disguise. Correlated signals inflate *apparent* breadth while adding little real information, which is why [[signal-orthogonalization]] (de-correlating signals before blending) is a prerequisite for the law to pay off. (See [[alpha-model]] for the IC/breadth decomposition in full.)

## Preparing Signals Before Blending

Raw signals are not comparable — funding is a percentage, OI divergence a ratio, netflow a dollar amount. Normalize before combining:

1. **Sign-align.** Orient every signal so "+" means the same directional view (e.g. bullish). A contrarian funding signal must be flipped.
2. **Cross-sectional or time-series z-score.** Convert each signal to a z-score (subtract mean, divide by standard deviation) so all live on a common scale.
3. **Winsorize / clip.** Cap z-scores at ±3 so a single blown-out reading (a memecoin funding spike) does not dominate the composite.
4. **De-correlate.** Apply [[signal-orthogonalization]] (Gram–Schmidt or PCA) so overlapping signals are not double-counted.

## Three Ways to Blend

### 1. Equal-Weight (z-score averaging)

Average the standardized signals: `composite = mean(z_1, …, z_n)`. Robust, transparent, and hard to overfit — the sensible default for a diversified signal stack, and often competitive with fancier schemes out-of-sample. Its weakness: it ignores that some signals are genuinely better than others.

### 2. IC-Weight

Weight each signal by its historical [[information-coefficient|Information Coefficient]] — the correlation between the signal and subsequent returns: `composite = Σ IC_i × z_i / Σ|IC_i|`. Signals that have actually predicted returns get more say. This is the factor-model workhorse. Caveat: ICs must be estimated out-of-sample or on a rolling window; fitting weights on the same data used to test them is [[overfitting-detection|overfitting]], and ICs decay ([[alpha-decay]]), so weights need refreshing.

### 3. ML-Stacked (ensemble)

A meta-learner ([[xgboost-trading|gradient-boosted trees]], logistic regression, or a neural net) takes the individual signals as features and learns a non-linear combination — including interactions like "netflow matters only when the regime is risk-on." Highest ceiling, highest overfitting risk; demands [[purged-kfold-cv|purged cross-validation]] and generous regularization. Often paired with [[meta-labeling]], where the stack sizes/vetoes a primary directional bet.

| Method | Overfitting risk | Interpretability | Handles interactions | Typical use |
|---|---|---|---|---|
| Equal-weight | Low | High | No | Default / small samples |
| IC-weight | Medium | High | No | Factor models, medium history |
| ML-stacked | High | Low | Yes | Large, diverse signal sets |

**Practical guidance:** start equal-weight, graduate to IC-weight once you trust your IC estimates, and only reach for ML stacking with many signals, long history, and rigorous validation. In crypto's short samples (see [[ml-crypto-price-prediction]]), simpler blends frequently win out-of-sample.

## A Crypto Signal Stack

Five weak, economically-distinct crypto signals blended into one directional composite:

| Signal | Bullish reading | CryptoDataAPI source |
|---|---|---|
| **Funding** | funding not over-heated / mildly negative | `derivatives/funding-rates` |
| **OI divergence** | OI rising with price (confirmed trend) | `liquidity/oi-divergence` |
| **Exchange netflow** | net outflows (coins leaving CEXs) | `on-chain/exchange-flows/{symbol}` |
| **Regime** | HMM regime = `strong_trend_bull` / risk-on | `quant/market`, `regimes/current` |
| **Breadth** | high % of alts above their 200D MA | `market-health/altcoin-breadth` |

Each becomes a z-score, gets sign-aligned so "+" is bullish, is de-correlated, and is averaged (or IC-weighted) into a single composite that drives the trade. Because the drivers are structurally different — positioning, on-chain flow, statistical regime, breadth — their errors are only weakly correlated, so the blend is steadier than any one.

### Worked composite

Suppose the standardized, sign-aligned readings are:

```
funding z    = +0.8   (funding cool — bullish)
OI-div z      = +1.2   (OI confirming up-move)
netflow z     = -0.4   (mild inflows — slightly bearish)
regime z      = +1.5   (strong_trend_bull)
breadth z     = +0.6   (broad participation)

equal-weight composite = (0.8 + 1.2 - 0.4 + 1.5 + 0.6) / 5 = +0.74   → net bullish
```

An IC-weighted version, with regime and OI historically the strongest predictors, would tilt further toward those and might read closer to +0.9.

## Fusing the 27 Hyperliquid Baskets Into One Alpha

The [[hyperliquid-baskets-overview|27 Hyperliquid strategy baskets]] are usually treated as *separate* strategies to allocate capital across. Composite blending offers a more powerful use: **fuse their outputs into a single unified alpha score**, going beyond capital allocation to signal integration.

- **Each basket emits a score, not just a position.** A basket like [[oi-confirmed-trend]] or [[breadth-and-momentum-divergence]] produces a continuous conviction reading per asset, not merely on/off.
- **Standardize and de-correlate across baskets.** Many baskets overlap (several are momentum/trend variants); [[signal-orthogonalization]] collapses that redundancy so correlated baskets do not triple-count the same bet — the difference between 27 *nominal* and perhaps 6–8 *effective* independent signals.
- **Blend into one cross-sectional alpha.** Equal-weight, IC-weight, or ML-stack the 27 orthogonalized basket scores into a single per-asset alpha vector, which [[portfolio-construction]] then sizes against risk and cost.

The distinction matters: **capital allocation** asks "how much money to each basket?"; **composite blending** asks "what is the one best combined view per asset?" The latter extracts breadth the former leaves on the table, but only after honest de-correlation — otherwise the Fundamental Law's breadth term is an illusion (see [[alpha-model]]).

## Pitfalls

- **Correlated "independent" signals.** The dominant failure. Five momentum variants are one signal; effective breadth (and IR) is a fraction of the nominal count. Orthogonalize first.
- **Overfit blend weights.** Grid-searching weights on the backtest manufactures phantom IC. Prefer equal-weight or out-of-sample IC estimates.
- **Look-ahead in IC estimation.** ICs must use only past data at each point; computing them on the full sample leaks the future into the weights.
- **Non-stationary signal distributions.** Crypto signal scales drift across regimes; z-score on rolling windows and re-standardize, don't assume a fixed distribution.
- **Regime dependence.** A blend tuned in a bull market can invert in a bear. Consider regime-conditional weights, and monitor realized vs. expected composite IC as an early-warning gauge ([[alpha-decay]]).

## Getting the Data (CryptoDataAPI)

The component signals are pulled from derivatives, liquidity, on-chain, regime, and breadth endpoints; the baskets themselves have a dedicated endpoint.

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding signal
- `GET /api/v1/liquidity/oi-divergence` — OI-vs-price divergence signal
- `GET /api/v1/on-chain/exchange-flows/BTC` — CEX netflow signal
- `GET /api/v1/quant/market` — HMM regime probabilities
- `GET /api/v1/regimes/current` — long-horizon regime label
- `GET /api/v1/market-health/altcoin-breadth` — breadth signal
- `GET /api/v1/trading-strategy-baskets` — the meta-basket scores to fuse

**Historical data (for IC estimation and blend backtests):**
- `GET /api/v1/backtesting/funding` — funding archive
- `GET /api/v1/quant/history` — point-in-time regime probability records
- `GET /api/v1/on-chain/whale-score/BTC` — historical on-chain conviction series

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/trading-strategy-baskets"
```

Auth: `X-API-Key` header. Endpoint catalogs: [[cryptodataapi-strategy-baskets]], [[cryptodataapi-derivatives]], [[cryptodataapi-regimes]], [[cryptodataapi-on-chain]].

## Related

- [[alpha-model]] — blending is its signal-combination step
- [[information-coefficient]] — the weight and the quality metric for blending
- [[signal-orthogonalization]] — de-correlate signals before blending (prerequisite for real breadth)
- [[information-ratio]] — what a good blend maximizes
- [[multi-factor-portfolio]] — the factor framework blends live inside
- [[hyperliquid-baskets-overview]] — the 27 baskets fused into one alpha
- [[ml-crypto-price-prediction]] — an ML-stacked blend end-to-end

## Sources

- Grinold, R. & Kahn, R. (2000). *Active Portfolio Management* — the Fundamental Law and the IC/breadth decomposition.
- Narang, R. (2013). *Inside the Black Box* — alpha models and signal combination in quant systems.
- [[book-advances-in-financial-ml]] — López de Prado, M. (2018) — ensemble/stacking and feature importance for combining signals.

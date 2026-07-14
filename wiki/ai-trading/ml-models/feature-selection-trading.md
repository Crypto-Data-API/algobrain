---
title: "Feature Selection for Trading Models"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [ai-trading, machine-learning, quantitative, crypto]
aliases: ["Feature Selection", "Feature Importance", "Feature Pruning"]
domain: [machine-learning, portfolio-theory]
prerequisites: ["[[feature-engineering-finance]]", "[[overfitting-in-trading]]"]
difficulty: advanced
related: ["[[feature-engineering-crypto]]", "[[feature-engineering-finance]]", "[[information-coefficient]]", "[[signal-orthogonalization]]", "[[overfitting-in-trading]]", "[[random-forest-trading]]", "[[xgboost-trading]]", "[[ml-trading-pipeline]]", "[[crypto-signal-library]]"]
---

Feature selection is the process of reducing a large candidate feature set to a small, non-redundant set that actually improves out-of-sample forecasting. In trading — and acutely in crypto, where every venue multiplies the feature count — the binding constraint is not "which model" but "which features survive honest importance testing without overfitting." This page covers the two dominant importance methods (**MDA** and **MDI**), **mutual information** for nonlinear screening, **redundancy pruning**, and the **curse of dimensionality** as it bites per-venue crypto feature sets.

## Why selection matters more in trading

Financial signals have tiny signal-to-noise ratios: a good feature might carry an [[information-coefficient|IC]] of 0.03-0.06. With low SNR, every irrelevant feature you add is almost pure noise that the model can (and will) fit to the training set. The result is a beautiful backtest and no live edge (see [[overfitting-in-trading]]). Feature selection is therefore a form of [[overfitting-detection|overfitting control]], not just efficiency.

Crypto compounds this: the same conceptual signal (funding, OI, netflow, basis) exists **per venue and per asset**, so a raw panel can carry hundreds of near-duplicate columns — Binance funding, Hyperliquid funding, Bybit funding, OKX funding — that are 0.9+ correlated. Naive models split importance across these clones and understate each.

## Feature importance methods

### MDI — Mean Decrease Impurity (in-sample, tree-based)
MDI is the default importance from a [[random-forest-trading|random forest]] or [[xgboost-trading|gradient-boosted]] tree: for each feature, sum the impurity reduction (Gini / variance) it produces across all splits, averaged over trees. Fast and free (computed at fit time), but flawed for trading:
- **Biased toward high-cardinality / continuous features** — a noisy continuous feature gets more split opportunities than a binary one.
- **In-sample only** — measures fit, not generalization.
- **Masking / substitution effects** — when two features are correlated (endemic in crypto), MDI arbitrarily splits importance between them, so a genuinely important signal can look weak because its clone stole half the credit (Source: [[book-advances-in-financial-ml]]).

Use MDI as a fast first pass, never as the final word.

### MDA — Mean Decrease Accuracy (out-of-sample, permutation)
MDA measures importance by *breaking* a feature: fit the model, score it out-of-sample, then randomly **permute** one feature's column and re-score. The drop in performance (accuracy, or better, IC / negative log-loss) is that feature's importance. Advantages:
- **Out-of-sample and model-agnostic** — works on any fitted model.
- **Directly answers "does live performance depend on this feature?"**

Crypto/finance caveats:
- Use **purged, embargoed cross-validation** so permutation doesn't leak across the autocorrelated, overlapping-label structure of price series (Source: [[book-advances-in-financial-ml]]).
- **Substitution still bites**: permuting one of two correlated clones barely hurts because the model reads the signal off the twin. Fix by clustering correlated features and permuting the *whole cluster* together (**MDA on feature clusters** / clustered feature importance).

### MDI vs. MDA
| | MDI | MDA |
|---|---|---|
| Sample | In-sample (fit) | Out-of-sample (permutation) |
| Cost | Free at fit time | N re-scorings per feature |
| Model | Trees only | Any model |
| Main flaw | Cardinality bias, in-sample | Correlated-feature masking |
| Best use | Fast first cut | Final keep/drop decision |

## Mutual information (nonlinear screening)

Linear correlation / [[information-coefficient|IC]] misses nonlinear and non-monotonic relationships — common in crypto, where, e.g., *both* extreme positive and extreme negative funding predict mean-reversion (a U-shape a linear IC scores as ~0). **Mutual information (MI)** measures the general statistical dependence between a feature and forward return, capturing nonlinearity:
- MI ≥ 0; zero iff independent. Estimate via binning or k-nearest-neighbor estimators (e.g. `sklearn.feature_selection.mutual_info_regression`).
- Use as a **univariate filter** to rank candidates before the expensive MDA step.
- Caveat: MI is a *marginal* measure — it ignores redundancy between features, so high-MI features can still be duplicates of each other.

A practical pipeline: MI/IC filter (drop features with ~0 dependence) → redundancy pruning → MDA on clusters for the final set.

## Redundancy pruning

Because crypto features cluster hard (per-venue clones, funding vs. basis vs. OI all reading leverage), pruning correlated features is essential:
- **Correlation clustering** — compute the feature-feature correlation (or a distance = 1 - |ρ|), hierarchically cluster, and keep one representative per cluster (highest MI/IC, or a cluster composite).
- **Orthogonalization** — instead of dropping, residualize each feature against the others so you keep unique information; see [[signal-orthogonalization]] (regression residualization / Gram-Schmidt). Prefer this to hard dropping when clones each carry a little independent signal.
- **VIF / PCA** — variance-inflation-factor screening or replacing a correlated block with its top principal components (a form of [[signal-orthogonalization|orthogonalization]]). PCA components are uncorrelated but less interpretable.

## The curse of dimensionality with per-venue crypto sets

As feature count `p` grows relative to *effective* sample size `n`, data becomes sparse, distances become meaningless, and the model can memorize noise. Crypto makes `p` explode and `n` shrink simultaneously:
- **`p` explodes**: (signal families) × (venues) × (assets) × (lookback windows). Funding × 5 venues × 200 perps × 4 windows is already 4,000 columns.
- **`n` is smaller than it looks**: crypto's "10 years" is mostly one or two structurally distinct regimes; overlapping labels and high autocorrelation mean the *effective* independent-sample count is a fraction of the row count.
- **Consequence**: the honest `n/p` ratio can be far below the ~10:1 rule-of-thumb, so importance estimates are unstable and backtests overfit.

Mitigations: aggressive redundancy pruning (collapse per-venue clones to one composite), cross-sectional ranking to pool information across assets (raising effective `n`), regularization (L1/elastic-net drives coefficients to zero), limiting tree depth / feature-subsampling, and — most importantly — a *prior economic rationale* for every feature (see [[edge-taxonomy]]) rather than a blind sweep.

## Practical selection workflow

1. **Screen** — drop features with near-zero univariate MI *and* near-zero [[information-coefficient|rank-IC]] on out-of-sample folds.
2. **Cluster** — hierarchically cluster surviving features by correlation; identify per-venue clone groups.
3. **Prune / orthogonalize** — keep one representative per cluster, or residualize (see [[signal-orthogonalization]]).
4. **Rank** — clustered **MDA** on purged, embargoed CV for the final keep/drop.
5. **Stability-check** — re-run selection across time folds; a feature that's important in only one regime is fragile.
6. **Cap the count** — target a feature set where effective `n/p` stays comfortably above 10:1.

```python
# Cluster per-venue clones, then rank surviving clusters by out-of-sample MDA.
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.feature_selection import mutual_info_regression
import numpy as np

# 1. Univariate screen: drop near-zero mutual information
mi = mutual_info_regression(X, y)
keep = X.columns[mi > mi_threshold]

# 2. Correlation clustering (distance = 1 - |rho|)
dist = 1 - np.abs(np.corrcoef(X[keep].T))
clusters = fcluster(linkage(dist[np.triu_indices_from(dist, 1)], "average"),
                    t=0.3, criterion="distance")     # ~|rho|>0.7 grouped

# 3. Clustered MDA on purged/embargoed CV: permute a whole cluster at once
#    importance[c] = baseline_IC - IC_after_permuting_cluster_c
```

## Getting the Data (CryptoDataAPI)

Feature selection runs on the assembled feature panel plus forward returns. Build both from the historical archive so selection is done point-in-time:

**Panel construction (historical):**
- `GET /api/v1/backtesting/klines` — OHLCV for forward-return labels and price features
- `GET /api/v1/backtesting/funding` — funding archive (per-venue funding clones live here)
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time snapshot (avoids survivorship in the selection universe)
- `GET /api/v1/backtesting/symbols` — the backtest-available universe as of each date

**Live cross-check of shortlisted features:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC`, `GET /api/v1/liquidity/oi-divergence`, `GET /api/v1/on-chain/exchange-flows/{symbol}` — pull the live values of features that survive selection

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/funding"
```

Auth: `X-API-Key` header. Category pages: [[cryptodataapi-backtesting]], [[cryptodataapi-derivatives]], [[cryptodataapi-on-chain]].

## Related

- [[feature-engineering-crypto]] — where the candidate crypto features come from
- [[information-coefficient]] — the univariate screen that precedes selection
- [[signal-orthogonalization]] — the alternative to hard-dropping correlated features
- [[overfitting-in-trading]] / [[overfitting-detection]] — why selection is overfitting control
- [[random-forest-trading]] / [[xgboost-trading]] — the models whose importances feed MDI/MDA
- [[ml-trading-pipeline]] — selection sits between feature engineering and model fit

## Sources

- [[book-advances-in-financial-ml]] — de Prado on MDA/MDI, substitution effects, purged/embargoed CV, and clustered feature importance
- [[book-machine-learning-for-asset-managers]] — multicollinearity, distance metrics for feature clustering, and denoising
- CryptoDataAPI endpoint catalog (verified 2026-07-13) for panel-construction endpoints

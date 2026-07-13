---
title: "scikit-learn"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["scikit-learn", "sklearn"]
domain: [ai-trading]
difficulty: beginner
related: ["[[tools-frameworks-overview]]", "[[pytorch]]", "[[supervised-learning]]", "[[unsupervised-learning]]", "[[xgboost-trading]]", "[[random-forest-trading]]", "[[cross-validation-trading]]", "[[feature-engineering-finance]]", "[[ml-trading-pipeline]]", "[[artificial-intelligence]]"]
---

# scikit-learn

**scikit-learn** (sklearn) is the standard open-source Python library for traditional [[machine-learning-overview|machine learning]] (current stable line 1.7.x as of mid-2026). It provides consistent APIs for [[supervised-learning|classification/regression]], [[unsupervised-learning|clustering/dimensionality reduction]], model selection, and preprocessing. For trading, scikit-learn is where most practical ML work happens — [[xgboost-trading|XGBoost]] and [[random-forest-trading|Random Forest]] models that consistently outperform deep learning on structured financial data all use scikit-learn's API conventions.

> **Why "boring" beats "deep" in trading.** Financial data is mostly tabular, low signal-to-noise, and non-stationary. Deep nets shine when data is abundant and structure is rich (images, language); on small, noisy, tabular financial datasets, gradient-boosted trees and well-regularised linear models (all sklearn-shaped) typically win and are far easier to validate against [[overfitting-in-trading|overfitting]]. Most successful systematic strategies use scikit-learn-style models, not deep learning.

## Why scikit-learn for Trading

| Strength | Detail |
|----------|--------|
| **Simplest API** | `model.fit(X, y)` → `model.predict(X_test)` — 3 lines from data to prediction |
| **Tabular data champion** | Designed for structured data (price, volume, fundamentals) — exactly what trading uses |
| **Complete pipeline** | Preprocessing, feature selection, model training, [[cross-validation-trading|cross-validation]] in one library |
| **No GPU required** | Runs on any machine — no [[nvidia-ai|NVIDIA]] dependency |
| **XGBoost/LightGBM compatible** | Gradient boosting libraries follow sklearn API — drop-in replacement |
| **Production-ready** | Stable, well-tested, backward-compatible |

## Key Modules for Trading

| Module | What It Does | Trading Use |
|--------|-------------|-------------|
| **`sklearn.ensemble`** | [[random-forest-trading|Random Forest]], Gradient Boosting, AdaBoost | Signal generation, [[ensemble-methods|ensemble]] strategies |
| **`sklearn.linear_model`** | Linear/Logistic Regression, Lasso, Ridge | Baseline models, [[feature-engineering-finance|feature importance]] |
| **`sklearn.model_selection`** | [[cross-validation-trading|Cross-validation]], [[hyperparameter-tuning|grid search]], train/test split | Validation and tuning |
| **`sklearn.preprocessing`** | Scaling, encoding, normalisation | Feature preprocessing |
| **`sklearn.metrics`** | [[ai-evaluation-metrics|Accuracy, F1, AUC, MSE]] | Model evaluation |
| **`sklearn.decomposition`** | PCA, factor analysis | Dimensionality reduction, factor discovery |
| **`sklearn.cluster`** | K-Means, DBSCAN | [[unsupervised-learning|Regime detection]], asset clustering |
| **`sklearn.pipeline`** | Chain preprocessing + model into one object | Reproducible, deployable pipelines |

## scikit-learn vs PyTorch vs XGBoost

| | scikit-learn | [[pytorch|PyTorch]] | XGBoost |
|---|------------|---------|---------|
| **Best for** | Traditional ML, prototyping | Deep learning, NLP, vision | Tabular prediction (winning Kaggle) |
| **Data type** | Tabular (structured) | Any (text, images, sequences) | Tabular (structured) |
| **GPU** | Not needed | Required for large models | Optional (faster with GPU) |
| **Learning curve** | Lowest | Moderate | Low (sklearn-compatible API) |
| **Trading use** | Baseline models, preprocessing, validation | [[lstm-trading|LSTM]], [[transformer-trading|transformers]], [[foundation-models|LLMs]] | Primary signal model |

## Typical Trading Pipeline with scikit-learn

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from xgboost import XGBClassifier

# Build pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', XGBClassifier(n_estimators=200, max_depth=5))
])

# Walk-forward cross-validation (NOT the default KFold — that leaks the future)
tscv = TimeSeriesSplit(n_splits=5)
scores = cross_val_score(pipe, X, y, cv=tscv, scoring='f1')
```

> **Critical trading caveat.** Never use sklearn's default `KFold` or `cross_val_score` shuffling on time-series financial data — random splits train on future data and test on the past, producing inflated, fictional scores. Always use `TimeSeriesSplit` (or a purged/embargoed walk-forward scheme to handle overlapping labels; see [[cross-validation-trading]]). Most "amazing" backtests die here.

## See Also

- [[tools-frameworks-overview]] — Tools hub
- [[pytorch]] — For deep learning (complement to sklearn)
- [[xgboost-trading]] — The model that uses sklearn's API
- [[random-forest-trading]] — sklearn native
- [[supervised-learning]] — The paradigm sklearn implements
- [[cross-validation-trading]] — sklearn's `TimeSeriesSplit`
- [[ml-trading-pipeline]] — End-to-end pipeline using sklearn
- [[feature-engineering-finance]] — Preprocessing with sklearn
- [[artificial-intelligence]] — AI section hub

## Sources

- scikit-learn official documentation and user guide (scikit-learn.org), version 1.7.x current to mid-2026.
- Pedregosa et al., "Scikit-learn: Machine Learning in Python" (JMLR, 2011).
- Lopez de Prado, *Advances in Financial Machine Learning* (2018) — purged/embargoed cross-validation and why standard KFold fails on financial data.

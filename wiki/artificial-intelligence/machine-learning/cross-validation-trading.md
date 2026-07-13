---
title: "Cross-Validation for Trading"
type: concept
created: 2026-04-09
updated: 2026-06-11
status: good
tags: [ai-trading, machine-learning, backtesting]
aliases: ["Cross-Validation", "Cross Validation", "Walk-Forward Validation", "Time Series CV"]
domain: [ai-trading]
prerequisites: ["[[supervised-learning]]", "[[backtesting-pitfalls]]"]
difficulty: intermediate
related: ["[[supervised-learning]]", "[[overfitting-in-trading]]", "[[backtesting-pitfalls]]", "[[walk-forward-optimization]]", "[[bias-variance-tradeoff]]", "[[ml-trading-pipeline]]", "[[machine-learning-overview]]", "[[artificial-intelligence]]", "[[pybroker]]", "[[optuna]]", "[[purged-kfold-cv]]", "[[walk-forward-analysis]]", "[[optimization-objectives]]"]
---

# Cross-Validation for Trading

**Cross-validation** is the technique for estimating how well a model will perform on unseen data. Standard cross-validation (random k-fold) **does not work for financial data** because it breaks temporal ordering — training on future data to predict the past. Trading requires time-series-aware validation methods.

## Why Standard Cross-Validation Fails

In standard k-fold CV, data is randomly split into train/test folds. For trading:

- **Problem**: A model trained on 2024 data could be tested on 2023 data
- **Result**: Artificially inflated performance — the model has "seen the future"
- **Consequence**: Strategies that look great in validation fail completely in live trading

## Time-Series Validation Methods

### Walk-Forward Validation (Best Practice)

Train on a rolling window of past data, test on the next period, slide forward:

```
|--Train (2020-2022)--|--Test (2023)--|
      |--Train (2021-2023)--|--Test (2024)--|
            |--Train (2022-2024)--|--Test (2025)--|
```

This exactly simulates how a model would be deployed: always trained on past data, always tested on unseen future data. See [[walk-forward-optimization]] for implementation details.

### Expanding Window

Like walk-forward but the training window grows instead of sliding:

```
|--Train (2020-2022)--|--Test (2023)--|
|--Train (2020-2023)--------|--Test (2024)--|
|--Train (2020-2024)----------------|--Test (2025)--|
```

Uses all available history. Better when more data consistently improves the model.

### Purged K-Fold

Modified k-fold that removes data near the train/test boundary to prevent leakage:

```
|--Train--|--Gap--|--Test--|--Gap--|--Train--|
```

The "purge gap" ensures that no overlapping information bleeds between train and test sets. Useful when features use lagged values or rolling windows. Purged k-fold CV — together with "embargoing" (dropping observations immediately after the test set) and Combinatorial Purged Cross-Validation (CPCV) — was formalized by Marcos López de Prado in *Advances in Financial Machine Learning* (2018), the standard reference for leakage-resistant validation of trading models. See [[purged-kfold-cv]].

## Common Mistakes

| Mistake | Consequence |
|---------|-----------|
| **Random k-fold on time series** | Look-ahead bias, grossly overfitted results |
| **No gap between train and test** | Feature leakage from overlapping windows |
| **Optimizing hyperparameters on test set** | Test set is no longer "unseen" — need a third validation set |
| **Single train/test split** | Results depend on which period was chosen — not robust |
| **Forgetting transaction costs** | Model looks profitable before costs, unprofitable after |

## PyBroker's Native Cross-Validation

[[pybroker|PyBroker]] provides built-in time-series cross-validation that integrates with its backtesting engine. Models are trained and validated within walk-forward windows, with proper temporal splits. This avoids the common mistake of training on the full dataset and then backtesting on the same data. PyBroker handles the train/test window management, feature computation, and model retraining automatically at each fold boundary (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]]).

## Combining CV with Optuna

Use [[optuna|Optuna]] inside each cross-validation fold to optimize hyperparameters. The inner loop (Optuna) optimizes parameters, the outer loop (walk-forward CV) validates generalization. This nested approach is the most rigorous but computationally expensive (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]]).

```
For each walk-forward fold:
    1. Inner loop: Optuna optimizes hyperparameters on in-sample data
       (e.g., 100 trials of Bayesian optimization)
    2. Outer loop: Best parameters from inner loop are tested on
       the out-of-sample window
    3. Record OOS performance with the optimized parameters
    4. Slide window forward and repeat

Result: honest OOS performance where hyperparameters were tuned
        without ever seeing the test data
```

This nested CV + optimization approach is expensive (100 Optuna trials x N walk-forward folds = hundreds to thousands of backtests) but produces the most trustworthy performance estimates. See [[walk-forward-analysis]] for window sizing guidance and [[optimization-objectives]] for choosing what to optimize inside each fold.

## See Also

- [[walk-forward-optimization]] — Detailed implementation guide
- [[walk-forward-analysis]] — Window sizing and efficiency metrics
- [[overfitting-in-trading]] — What poor validation leads to
- [[backtesting-pitfalls]] — Broader backtesting mistakes
- [[bias-variance-tradeoff]] — Why validation matters
- [[supervised-learning]] — Models that need validation
- [[ml-trading-pipeline]] — Where validation fits in the pipeline
- [[pybroker]] — ML-first backtesting framework with native time-series CV
- [[optuna]] — Bayesian optimization framework for the inner tuning loop
- [[purged-kfold-cv]] — Time-series-aware k-fold with purging
- [[optimization-objectives]] — Choosing what to optimize during CV
- [[machine-learning-overview]] — ML section hub
- [[artificial-intelligence]] — AI section hub

## Sources

- López de Prado, M. (2018). *Advances in Financial Machine Learning*. Wiley. (Ch. 7: cross-validation in finance — purging, embargoing, CPCV.)
- (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]]) — PyBroker native time-series CV and nested Optuna + walk-forward workflow.
- scikit-learn documentation — `TimeSeriesSplit`: [https://scikit-learn.org/stable/modules/cross_validation.html#time-series-split](https://scikit-learn.org/stable/modules/cross_validation.html#time-series-split)

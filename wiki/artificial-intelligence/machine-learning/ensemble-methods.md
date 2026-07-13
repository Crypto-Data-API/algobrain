---
title: "Ensemble Methods"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Ensemble Methods", "Bagging", "Boosting", "Stacking"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[supervised-learning]]", "[[xgboost-trading]]", "[[random-forest-trading]]", "[[bias-variance-tradeoff]]", "[[machine-learning-overview]]", "[[artificial-intelligence]]"]
---

# Ensemble Methods

**Ensemble methods** combine multiple models to produce better predictions than any single model alone. They are the most successful approach in practical ML trading — [[xgboost-trading|XGBoost]] and [[random-forest-trading|Random Forest]], the two most widely used trading models, are both ensembles.

## Three Ensemble Strategies

### Bagging (Bootstrap Aggregating)

Train many models on random subsets of data, average their predictions.

- **How**: Sample data with replacement → train model → repeat → average
- **Effect**: Reduces [[bias-variance-tradeoff|variance]] (overfitting)
- **Key model**: [[random-forest-trading|Random Forest]] (bagging of decision trees)
- **Trading use**: Stable signal generation, robust feature importance

### Boosting

Train models sequentially, each correcting the errors of the previous one.

- **How**: Train model 1 → find its errors → train model 2 to fix those errors → repeat
- **Effect**: Reduces both bias and variance
- **Key models**: [[xgboost-trading|XGBoost]], LightGBM, CatBoost
- **Trading use**: Maximum predictive power on tabular financial data

### Stacking

Train different model types, then train a meta-model on their outputs.

- **How**: Train XGBoost, Random Forest, and LSTM separately → use their predictions as features for a final model
- **Effect**: Captures different aspects of the data from different architectures
- **Trading use**: Combining fundamental, technical, and sentiment models

## Why Ensembles Dominate Trading ML

| Reason | Explanation |
|--------|------------|
| **Reduces overfitting** | Averaging multiple models smooths out individual noise |
| **Handles noisy data** | Financial data is very noisy; single models easily fit noise |
| **Feature robustness** | Different trees/models may use different features, reducing dependence on any single one |
| **Proven track record** | XGBoost and Random Forest consistently win ML competitions on tabular data |

## Practical Example: Signal Stacking

A common trading ensemble:

1. **Model A** (XGBoost): Predicts next-day direction from technical indicators
2. **Model B** (Random Forest): Predicts regime from macro features
3. **Model C** ([[finbert]]): Sentiment score from recent news
4. **Meta-model** (Logistic Regression): Combines A, B, C into final signal with confidence

This is more robust than any individual model because each captures different information.

## See Also

- [[xgboost-trading]] — Gradient boosting for trading
- [[random-forest-trading]] — Bagging for trading
- [[bias-variance-tradeoff]] — Why ensembles work
- [[supervised-learning]] — The learning paradigm ensembles operate in
- [[ml-trading-pipeline]] — Where ensembles fit in the pipeline
- [[machine-learning-overview]] — ML section hub
- [[artificial-intelligence]] — AI section hub

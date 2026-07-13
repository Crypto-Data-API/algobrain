---
title: "AI Evaluation Metrics"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Evaluation Metrics", "AI Metrics", "F1 Score", "Precision", "Recall"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[ai-research-overview]]", "[[ai-benchmarks]]", "[[supervised-learning]]", "[[nlp-sentiment-analysis]]", "[[cross-validation-trading]]", "[[overfitting-in-trading]]", "[[artificial-intelligence]]"]
---

# AI Evaluation Metrics

**Evaluation metrics** quantify how well an AI model performs its task. Choosing the right metric is critical — a model optimised for the wrong metric can be useless or dangerous for trading. A sentiment classifier with 95% accuracy sounds great, but if it misclassifies the 5% that are market-moving events, it's worse than useless.

## Classification Metrics (Sentiment, Direction Prediction)

| Metric | Formula | What It Measures | Trading Use |
|--------|---------|-----------------|-------------|
| **Accuracy** | (TP+TN)/(TP+TN+FP+FN) | Overall correctness | Baseline, but misleading for imbalanced data |
| **Precision** | TP/(TP+FP) | Of predicted positives, how many are correct? | "When I predict bullish, how often am I right?" |
| **Recall** | TP/(TP+FN) | Of actual positives, how many did I find? | "Of all bullish moves, how many did I catch?" |
| **F1 Score** | 2 × (Precision × Recall)/(Precision + Recall) | Balance of precision and recall | Standard for [[nlp-sentiment-analysis|sentiment classification]] |
| **AUC-ROC** | Area under receiver operating curve | Discrimination ability across thresholds | Model ranking, threshold-independent evaluation |
| **MCC** (Matthews Correlation Coefficient) | Correlation between predicted and actual | Best single metric for imbalanced binary classification | Highly imbalanced signals (rare events) |

### The Accuracy Trap

If the market goes up 55% of days, a model that always predicts "up" has 55% accuracy — but zero trading value. **Accuracy is almost never the right metric for trading models.** Use precision/recall for signal quality, or trading-specific metrics (below).

### Precision vs Recall for Trading

| Preference | Strategy Type | Why |
|-----------|--------------|-----|
| **High precision** (few false positives) | Low-frequency, high-conviction strategies | Only trade when very confident — fewer but better signals |
| **High recall** (catch all true signals) | Event-driven, momentum strategies | Don't miss any real signal — accept some false alarms |
| **Balanced F1** | General-purpose signal generation | Standard starting point |

## Regression Metrics (Price Prediction, Volatility)

| Metric | What It Measures | Trading Use |
|--------|-----------------|-------------|
| **MSE** (Mean Squared Error) | Average squared error — penalises large errors heavily | Volatility prediction (large errors are costly) |
| **MAE** (Mean Absolute Error) | Average absolute error — robust to outliers | Price level prediction |
| **RMSE** | Square root of MSE — in same units as target | Standard reporting metric |
| **R²** | Proportion of variance explained | Model explanatory power (often very low for financial data — R² > 0.05 is notable) |
| **MAPE** | Mean absolute percentage error | Percentage-based error for comparison across assets |

## NLP-Specific Metrics

| Metric | What It Measures | Used For |
|--------|-----------------|---------|
| **Perplexity** | How "surprised" the model is by text | Language model quality (lower = better) |
| **BLEU** | N-gram overlap between generated and reference text | Translation, summarisation quality |
| **ROUGE** | Recall-oriented overlap | Summarisation quality |
| **BERTScore** | Semantic similarity using embeddings | Generation quality beyond exact word match |
| **Human evaluation** | Humans rate quality directly | Gold standard but expensive and slow |

## Trading-Specific Metrics

These metrics evaluate the **trading system**, not just the model:

| Metric | What It Measures | Why It Matters |
|--------|-----------------|---------------|
| **Sharpe Ratio** | Risk-adjusted return | Standard measure of strategy quality |
| **Hit Rate** | Percentage of profitable trades | Intuitive signal quality measure |
| **Profit Factor** | Gross profit / gross loss | Must be > 1 for profitability |
| **Max Drawdown** | Largest peak-to-trough decline | Tail risk measure |
| **Calmar Ratio** | Annual return / max drawdown | Risk-adjusted with focus on worst case |
| **Information Coefficient** | Correlation between predictions and outcomes | Signal quality at the individual prediction level |

The gap between **model metrics** (F1, AUC) and **trading metrics** (Sharpe, drawdown) is where most ML trading projects fail. A high-F1 model can still produce a negative-Sharpe strategy due to transaction costs, slippage, and position sizing.

## See Also

- [[ai-research-overview]] — Research hub
- [[ai-benchmarks]] — Standardised benchmark tests
- [[supervised-learning]] — The paradigm most metrics evaluate
- [[cross-validation-trading]] — How metrics are computed properly
- [[overfitting-in-trading]] — When metrics mislead
- [[nlp-sentiment-analysis]] — Applied classification metrics
- [[artificial-intelligence]] — AI section hub

## Sources

- Classification/regression metric definitions — standard ML references (scikit-learn metrics documentation; Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*)
- Matthews Correlation Coefficient for imbalanced classification — Chicco & Jurman, BMC Genomics (2020)
- NLP metrics — BLEU (Papineni et al., 2002), ROUGE (Lin, 2004), BERTScore (Zhang et al., 2020)
- Trading-specific metrics (Sharpe, Calmar, Information Coefficient) — see [[sharpe-ratio]], [[maximum-drawdown]] and standard quant references

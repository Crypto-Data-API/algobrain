---
title: "Supervised Learning"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Supervised Learning", "Supervised ML"]
domain: [ai-trading]
difficulty: beginner
related: ["[[unsupervised-learning]]", "[[reinforcement-learning]]", "[[machine-learning-vs-deep-learning]]", "[[types-of-ai]]", "[[xgboost-trading]]", "[[random-forest-trading]]", "[[lstm-trading]]", "[[finbert]]", "[[feature-engineering-finance]]", "[[overfitting-in-trading]]", "[[artificial-intelligence]]"]
---

# Supervised Learning

**Supervised learning** trains a model on labeled data — input/output pairs where the correct answer is known. The model learns to map inputs to outputs, then predicts outputs for new, unseen inputs. It is the most widely used machine learning paradigm in trading and the foundation of most predictive models.

## How It Works

1. **Collect labeled data**: Historical examples where you know the outcome
   - Input: price, volume, sentiment features on day T
   - Label: whether price went up or down on day T+1
2. **Train the model**: Algorithm adjusts its internal parameters to minimize prediction errors
3. **Validate**: Test on held-out data the model hasn't seen ([[backtesting-pitfalls|walk-forward validation]])
4. **Predict**: Apply to new live data to generate trading signals

## Two Types of Supervised Learning

### Classification (Predict a Category)

The model outputs a discrete label.

| Task | Input Features | Output | Model |
|------|---------------|--------|-------|
| Sentiment classification | Earnings call text | Bullish / Bearish / Neutral | [[finbert]] |
| Direction prediction | Technical indicators | Up / Down | [[xgboost-trading|XGBoost]], [[random-forest-trading|Random Forest]] |
| Regime detection | Volatility, correlation features | Bull / Bear / Sideways | Logistic regression, SVM |
| Default prediction | Financial ratios | Default / No default | Gradient boosted trees |

### Regression (Predict a Number)

The model outputs a continuous value.

| Task | Input Features | Output | Model |
|------|---------------|--------|-------|
| Price forecasting | Historical prices, macro data | Next-day price | [[lstm-trading|LSTM]], linear regression |
| Volatility estimation | Returns, VIX, option data | Implied volatility | Neural networks |
| Fair value estimation | Fundamentals, comps | Target price | Ensemble models |

## The Most Important Trading Models

| Model | Type | Strengths | Trading Use |
|-------|------|-----------|------------|
| **[[xgboost-trading|XGBoost]]** | Gradient boosted trees | Best for tabular data, handles missing values, fast | The workhorse — price prediction, feature screening |
| **[[random-forest-trading|Random Forest]]** | Ensemble of decision trees | Resistant to overfitting, feature importance | Signal generation, regime classification |
| **[[lstm-trading|LSTM]]** | Recurrent neural network | Captures temporal dependencies | Time-series forecasting |
| **[[finbert|FinBERT]]** | Transformer (BERT) | Financial language understanding | [[nlp-sentiment-analysis|Sentiment analysis]] |
| **Logistic Regression** | Linear classifier | Interpretable, fast, baseline | Quick signal screening |
| **SVM** | Support vector machine | Works well in high-dimensional spaces | Classification with many features |

## The Feature Engineering Problem

Supervised learning is only as good as its features. The model can't discover signal that isn't represented in the input data. This makes [[feature-engineering-finance|feature engineering]] — the art of creating informative input features from raw market data — the most critical skill in supervised ML for trading.

Common feature categories:
- **Price-based**: Returns, moving averages, RSI, Bollinger Bands
- **Volume-based**: Volume ratios, OBV, VWAP deviation
- **Fundamental**: P/E, EV/EBITDA, earnings surprise
- **Sentiment**: News sentiment scores, social media metrics
- **Macro**: Interest rates, VIX, DXY, yield curve slope
- **Alternative**: Satellite data, web traffic, job postings

## Key Risks

| Risk | Description | Mitigation |
|------|------------|-----------|
| **[[overfitting-in-trading|Overfitting]]** | Model memorizes training data noise | Walk-forward validation, regularization, simple models |
| **Look-ahead bias** | Using future data to predict the past | Strict temporal splits in training/test data |
| **Survivorship bias** | Only training on stocks that still exist | Include delisted securities in training data |
| **Regime change** | Historical patterns break in new market conditions | Regime-aware models, frequent retraining |
| **Feature leakage** | Target variable information leaks into features | Careful [[feature-engineering-finance|feature engineering]] pipeline |

## See Also

- [[unsupervised-learning]] — Learning without labels
- [[reinforcement-learning]] — Learning through trial and error
- [[xgboost-trading]] — The most practical supervised model for trading
- [[random-forest-trading]] — Ensemble tree-based approach
- [[lstm-trading]] — Supervised deep learning for time series
- [[finbert]] — Supervised NLP for financial sentiment
- [[feature-engineering-finance]] — Creating features for supervised models
- [[overfitting-in-trading]] — The primary risk in supervised trading models
- [[ml-trading-pipeline]] — End-to-end pipeline
- [[machine-learning-vs-deep-learning]] — Where supervised learning fits
- [[artificial-intelligence]] — AI section hub

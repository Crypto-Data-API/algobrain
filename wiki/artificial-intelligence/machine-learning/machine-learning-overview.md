---
title: "Machine Learning"
type: overview
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Machine Learning", "ML"]
related: ["[[supervised-learning]]", "[[unsupervised-learning]]", "[[reinforcement-learning]]", "[[machine-learning-vs-deep-learning]]", "[[types-of-ai]]", "[[ml-trading-pipeline]]", "[[feature-engineering-finance]]", "[[overfitting-in-trading]]", "[[artificial-intelligence]]"]
---

# Machine Learning

**Machine learning** (ML) is the subset of AI where systems learn from data rather than being explicitly programmed. Instead of writing rules like "if RSI < 30 then buy," an ML model discovers patterns in historical data and uses them to make predictions or decisions. ML is the backbone of quantitative trading, powering everything from signal generation to execution optimization.

## The Three Paradigms

| Paradigm | How It Learns | Trading Use | Key Pages |
|----------|--------------|-------------|-----------|
| **[[supervised-learning]]** | Labeled examples (input → correct answer) | Price prediction, sentiment classification | [[xgboost-trading]], [[random-forest-trading]], [[finbert]] |
| **[[unsupervised-learning]]** | Discovers patterns in unlabeled data | Regime detection, anomaly detection, clustering | K-Means, PCA, autoencoders |
| **[[reinforcement-learning]]** | Trial and error with rewards | Execution, [[ai-market-making|market making]], position sizing | [[reinforcement-learning-trading|DQN, PPO, SAC]] |

Most trading ML uses **supervised learning**. Unsupervised learning is used for feature discovery and regime classification. Reinforcement learning is the most natural fit for trading but the hardest to make work in practice.

## The ML Trading Pipeline

The [[ml-trading-pipeline|end-to-end pipeline]] for ML trading:

1. **Data collection** → Price, volume, fundamentals, alternative data ([[data-sources-overview]])
2. **[[feature-engineering-finance|Feature engineering]]** → Transform raw data into model inputs
3. **Model selection** → Choose algorithm (XGBoost, LSTM, ensemble)
4. **Training** → Fit model on historical data
5. **Validation** → Walk-forward testing to prevent [[overfitting-in-trading|overfitting]]
6. **[[backtesting-overview|Backtesting]]** → Simulate strategy performance
7. **Deployment** → Paper trading → live capital

## Key Models for Trading

### Traditional ML (Tabular Data)

| Model | Strengths | Best For |
|-------|-----------|---------|
| **[[xgboost-trading|XGBoost]]** | Handles tabular data, missing values, fast | Price prediction, feature screening |
| **[[random-forest-trading|Random Forest]]** | Resistant to overfitting, interpretable | Signal generation, regime classification |
| **LightGBM** | Faster than XGBoost for large datasets | High-frequency feature evaluation |
| **Logistic Regression** | Interpretable, fast baseline | Quick screening, feature importance |

### Deep Learning (Sequential / Unstructured Data)

| Model | Strengths | Best For |
|-------|-----------|---------|
| **[[lstm-trading|LSTM]]** | Temporal dependencies | Time-series forecasting |
| **[[transformer-architecture|Transformers]]** | Long-range attention | [[nlp-sentiment-analysis|Sentiment]], [[llm-market-analysis|market analysis]] |
| **[[cnn-chart-recognition|CNN]]** | Spatial pattern recognition | Chart pattern detection |
| **[[gan-synthetic-data|GANs]]** | Generative capability | Synthetic training data |

### Foundation Models

| Model | Provider | Best For |
|-------|---------|---------|
| **Claude** | [[anthropic]] | Research, code generation, long-document analysis |
| **GPT-4** | [[openai]] | Broadest ecosystem, function calling |
| **[[finbert|FinBERT]]** | [[hugging-face]] | Financial sentiment classification |

## The Five Pitfalls

Every ML trading project faces these risks:

1. **[[overfitting-in-trading|Overfitting]]** — Model learns noise instead of signal. Mitigation: walk-forward validation, regularization
2. **Look-ahead bias** — Accidentally using future information. Mitigation: strict temporal data splits
3. **Survivorship bias** — Only training on stocks that still exist. Mitigation: include delisted securities
4. **Regime change** — Historical patterns break. Mitigation: regime-aware models, frequent retraining
5. **Transaction costs** — Ignoring slippage, fees, and market impact. Mitigation: realistic [[backtesting-pitfalls|backtesting]] with costs

## See Also

- [[supervised-learning]] — Learning with labels (most trading ML)
- [[unsupervised-learning]] — Pattern discovery without labels
- [[reinforcement-learning]] — Learning through trial and error
- [[machine-learning-vs-deep-learning]] — ML vs DL vs foundation models
- [[ml-trading-pipeline]] — End-to-end implementation guide
- [[feature-engineering-finance]] — The most critical skill in trading ML
- [[overfitting-in-trading]] — The #1 risk
- [[backtesting-overview]] — Testing ML strategies
- [[artificial-intelligence]] — AI section hub

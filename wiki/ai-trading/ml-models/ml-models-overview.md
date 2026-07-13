---
title: "ML Models for Trading"
type: index
created: 2026-04-06
updated: 2026-06-12
status: good
tags: [machine-learning, ai-trading, index]
aliases: ["ML Models", "ml-models", "Ml Models"]
---

# ML Models for Trading

Machine learning and deep learning models applied to price prediction, signal generation, execution, and risk/compliance in financial markets.

Financial markets are among the hardest prediction problems in ML because the signal-to-noise ratio is extremely low, the data distribution is non-stationary, and the act of trading on a signal can destroy it. No architecture overcomes these facts; the right model is the one whose inductive bias matches the structure of the problem and whose complexity is justified by out-of-sample, cost-corrected performance. This section surveys the model families that have proven most useful, organized by the data structure they exploit.

The [[ml-trading-pipeline]] page provides an end-to-end blueprint. Equally important is understanding [[overfitting-in-trading]] -- in finance, a model that looks great on historical data usually fails live because it has memorized noise. See also the [[edge-taxonomy]] and [[deflated-sharpe-ratio]] for separating real edge from data-mined artifacts.

## Start Here

- [[ml-trading-pipeline]] -- From raw data to live predictions, step by step
- [[xgboost-trading]] -- The default model for tabular financial features
- [[overfitting-in-trading]] -- Why most ML trading models fail and how to prevent it
- [[feature-engineering-finance]] -- Features usually matter more than architecture

## Model Families

### Tabular / tree-based (cross-sectional features)
For engineered features (factors, fundamentals, microstructure stats), gradient-boosted trees dominate. They are robust to mixed feature scales, handle missing data, and resist overfitting better than deep nets on small, noisy tabular datasets.
- [[xgboost-trading]] -- gradient-boosted trees; the workhorse for tabular alpha
- [[random-forest-trading]] -- bagged trees; strong baseline, lower variance

### Sequence models (time series)
For modelling a single instrument's history through time.
- [[lstm-trading]] -- gated recurrent network; long the default sequence model
- [[xlstm-ts]] -- modernised LSTM; state-of-the-art on some daily-direction benchmarks
- [[transformer-trading]] -- attention-based; powerful but data-hungry and overfit-prone on noisy series

### Relational / graph models (cross-asset structure)
For modelling relationships *between* instruments and entities.
- [[graph-neural-networks-finance]] -- learns over correlation, sector, supply-chain, and ownership graphs

### Generative models
- [[gan-synthetic-data]] -- synthetic market data for augmentation, stress-testing, and privacy

### NLP / language models (unstructured text)
For extracting signal from filings, news, earnings calls, and social media.
- [[nlp-sentiment-analysis]] -- sentiment extraction pipelines
- [[finbert]] -- finance-domain BERT for sentiment/classification
- [[earnings-call-analysis]] -- tone and content analysis of transcripts
- [[llm-market-analysis]] -- large language models for research synthesis and signal generation

### Computer vision
- [[cnn-chart-recognition]] -- convolutional nets applied to chart-image pattern recognition

### Reinforcement learning
- [[reinforcement-learning-trading]] -- sequential decision making for execution and position management

### Derivatives / pricing
- [[deep-learning-option-pricing]] -- neural surrogates for option pricing and calibration

### Risk, fraud & compliance (second-order, trading-adjacent)
- [[federated-learning-aml]] -- privacy-preserving cross-institution AML/fraud models

## Cross-cutting concerns

- [[feature-engineering-finance]] -- input design; usually higher-leverage than architecture choice
- [[overfitting-in-trading]] -- the dominant failure mode
- [[market-regime-detection-ml]] -- conditioning models on the prevailing regime
- [[ai-trading-risks]] -- model risk, data leakage, and deployment hazards

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/ai-trading/ml-models"
WHERE type != "index"
SORT updated DESC
```

## Comparisons

- [[python-vs-r-for-trading]] -- choosing between Python and R for ML and quantitative trading

## Related

- [[ai-trading-agents]] -- autonomous LLM-driven trading agents
- [[backtesting-pitfalls]] -- validating ML models without fooling yourself
- [[deflated-sharpe-ratio]] -- correcting performance for the number of trials

## Sources

- Section overview; see individual pages for their cited sources. Benchmark and architecture claims for newer models (e.g. [[xlstm-ts]], [[graph-neural-networks-finance]], [[federated-learning-aml]]) trace to [[2026-04-22-gap-finder-ai-2026-major-news-stories]].

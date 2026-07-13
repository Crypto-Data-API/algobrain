---
title: "Advances in Financial Machine Learning — Marcos Lopez de Prado (2018)"
type: source
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [book, machine-learning, quantitative, backtesting]
aliases: ["Advances in Financial Machine Learning", "AFML", "Lopez de Prado ML"]
related: ["[[feature-engineering-finance]]", "[[overfitting-in-trading]]", "[[walk-forward-optimization]]", "[[ml-trading-pipeline]]", "[[advances-in-financial-ml]]"]
source_type: book
source_author: "Marcos Lopez de Prado"
source_date: 2018
confidence: high
claims_count: 12
---

The first rigorous textbook on applying [[machine-learning]] to financial markets, written by Marcos Lopez de Prado — a principal at AQR Capital Management and former head of machine learning at Guggenheim Partners. The book argues that most published ML trading research is fundamentally flawed due to misapplication of standard ML techniques to financial data, which violates core assumptions (i.i.d. samples, stationarity, large sample sizes). Lopez de Prado provides a complete pipeline of purpose-built techniques — from data structuring through feature engineering, labeling, cross-validation, and bet sizing — that address finance-specific challenges. The book is widely considered the definitive reference for practitioners building ML-based trading systems.

## Key Claims

1. [HIGH] **Standard ML techniques fail in finance without modification**: Financial data violates the independent and identically distributed (i.i.d.) assumption that underpins most ML algorithms. Time series data exhibits serial correlation, regime changes, and non-stationarity. Applying sklearn defaults to financial data produces models that backtest well but fail catastrophically in live trading. (Source: Marcos Lopez de Prado)

2. [HIGH] **Triple barrier labeling produces better training targets than fixed-horizon returns**: Instead of labeling observations by fixed-horizon forward returns (e.g., "return over next 5 days"), the triple barrier method defines three exit conditions: a profit-taking barrier, a stop-loss barrier, and a maximum holding period. This produces labels that reflect how a trader would actually manage a position, resulting in more realistic and useful training targets. (Source: Marcos Lopez de Prado)

3. [HIGH] **Fractionally differentiated features preserve memory while achieving stationarity**: Standard differencing (returns) achieves stationarity but destroys long-term memory in the series. Fractional differentiation applies a non-integer order of differencing (e.g., d=0.4) that makes the series stationary enough for ML while preserving the memory structure that contains predictive signal. (Source: Marcos Lopez de Prado)

4. [HIGH] **Combinatorial purged cross-validation (CPCV) prevents information leakage**: Standard k-fold cross-validation is invalid for financial time series because training and test sets share temporally adjacent observations whose labels overlap. CPCV creates combinatorial train/test splits with purging (removing samples near the train/test boundary) and embargo (adding a buffer period), preventing any leakage of future information into training data. (Source: Marcos Lopez de Prado)

5. [HIGH] **Meta-labeling separates "what to trade" from "how much to bet"**: A two-model architecture where the primary model generates trade signals (direction) and a secondary meta-labeling model predicts whether the primary signal will be profitable. This allows the bet-sizing model to filter out low-conviction signals, dramatically improving the strategy's risk-adjusted returns without changing the underlying alpha source. (Source: Marcos Lopez de Prado)

6. [HIGH] **Feature importance methods identify signal vs. noise**: Mean Decrease Accuracy (MDA), Mean Decrease Impurity (MDI), and Single Feature Importance (SFI) are three complementary methods for measuring whether a feature genuinely contributes predictive power or is fitting to noise. Using all three provides robust feature selection that reduces overfitting. (Source: Marcos Lopez de Prado)

7. [HIGH] **Most published alpha is overfitting — the deflated Sharpe ratio detects this**: When researchers test hundreds of strategy variants and report only the best-performing one, the reported Sharpe ratio is inflated by selection bias. The deflated Sharpe ratio adjusts for the number of trials conducted, providing a more honest estimate of whether a strategy has genuine out-of-sample edge. (Source: Marcos Lopez de Prado)

8. [HIGH] **Financial ML is a pipeline, not a model**: The choice of ML algorithm (random forest, gradient boosting, neural network) matters far less than the data preparation, feature engineering, labeling, cross-validation, and bet-sizing stages. Practitioners who focus on algorithm selection while neglecting the pipeline will consistently produce overfitted, non-reproducible results. (Source: Marcos Lopez de Prado)

9. [HIGH] **Volume and dollar bars are superior to time bars**: Sampling price data at fixed time intervals (1-minute, daily) produces bars with highly variable information content — quiet periods generate noise-filled bars while volatile periods compress critical information. Volume bars (sampled every N contracts) and dollar bars (sampled every $N traded) produce more uniform information content per observation, improving ML model performance. (Source: Marcos Lopez de Prado)

10. [HIGH] **Sample weighting by uniqueness prevents overweighting overlapping observations**: When labels span multiple bars (as with triple barrier labeling), observations overlap temporally and are not independent. Weighting each sample by its uniqueness — the fraction of the label period not shared with other samples — prevents the ML model from overweighting redundant information. (Source: Marcos Lopez de Prado)

11. [HIGH] **Bet sizing should be proportional to model confidence, not binary**: Rather than taking full-size positions on every signal, position size should scale with the model's predicted probability of success. This is implemented through the meta-labeling model's output and can be calibrated using the average active bets at any given time. Binary (all-in or nothing) bet sizing leaves significant risk-adjusted return on the table. (Source: Marcos Lopez de Prado)

12. [HIGH] **The book is the definitive reference for ML-based trading system construction**: Lopez de Prado's framework — from data bars through feature engineering, labeling, sample weighting, cross-validation, feature importance, bet sizing, and portfolio construction — represents the most complete publicly available methodology for building ML trading systems that are robust to the specific challenges of financial data. (Source: Marcos Lopez de Prado, widely corroborated by practitioner community)

## Concepts Referenced

- [[machine-learning]], [[feature-engineering-finance]]
- [[overfitting-in-trading]], [[walk-forward-optimization]]
- [[ml-trading-pipeline]], [[backtesting-pitfalls]]
- [[position-sizing]], [[risk-management]]
- [[sharpe-ratio]], [[cross-validation]]

## Pages Backed

- [[ml-trading-pipeline]] — complete pipeline architecture for ML-based trading systems
- [[feature-engineering-finance]] — fractionally differentiated features and volume/dollar bars
- [[overfitting-in-trading]] — deflated Sharpe ratio and multiple-testing correction
- [[walk-forward-optimization]] — CPCV as the gold standard for financial cross-validation
- [[backtesting-pitfalls]] — information leakage, i.i.d. violations, and label overlap
- [[position-sizing]] — bet sizing proportional to model confidence via meta-labeling

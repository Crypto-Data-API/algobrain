---
title: ML Trading Pipeline
type: concept
created: 2026-04-06
updated: 2026-04-14
status: good
tags: [ai-trading, machine-learning, data-engineering]
difficulty: intermediate
related:
  - "[[feature-engineering-finance]]"
  - "[[overfitting-in-trading]]"
  - "[[xgboost-trading]]"
  - "[[ai-trading-risks]]"
  - "[[book-advances-in-financial-ml]]"
  - "[[book-inside-the-black-box]]"
  - "[[book-hands-on-ml-algorithmic-trading]]"
  - "[[book-quantitative-trading-ernest-chan]]"
  - "[[book-machine-learning-for-asset-managers]]"
  - "[[book-artificial-intelligence-in-finance]]"
  - "[[optuna]]"
  - "[[pybroker]]"
---

## Overview

An ML trading pipeline is the end-to-end workflow for building, validating, deploying, and monitoring a machine learning trading system. Each step has domain-specific pitfalls — most critically, respecting temporal ordering and preventing information leakage. Getting the pipeline wrong invalidates everything downstream, no matter how sophisticated your model is.

## Pipeline Steps

### Step 1: Data Collection
Gather OHLCV prices, fundamental data, alternative data, and any other inputs. Use adjusted prices (split/dividend adjusted). Source from reliable providers and cross-validate between vendors. Store raw data immutably — never modify historical records.

### Step 2: Feature Engineering
Transform raw data into informative, stationary features. See [[feature-engineering-finance]] for comprehensive feature categories. Ensure no look-ahead bias — every feature computation must use only data available at that timestamp.

### Step 3: Label Creation
Define what you are predicting. Common targets: forward 1-day/5-day return (regression), directional move (binary classification), or triple-barrier method (Lopez de Prado — labels based on which of profit target, stop loss, or time limit is hit first) (Source: [[book-advances-in-financial-ml]]). Label choice profoundly affects model behavior.

### Step 4: Train / Validation / Test Split
**Critical rule: never shuffle financial data.** Use temporal splits only (Source: [[book-advances-in-financial-ml]]):
- **Train**: oldest data (e.g., 2010-2019)
- **Validation**: next period (e.g., 2020-2021) for hyperparameter tuning
- **Test**: most recent data (e.g., 2022-2025) — touch only once for final evaluation
- **Purge gap**: leave a gap between train and validation/test to prevent label leakage (if labels use 5-day forward returns, gap must be >= 5 days)

### Step 5: Model Training
Start simple: [[random-forest-trading|Random Forest]] or [[xgboost-trading|XGBoost]] as baseline (Source: [[book-machine-learning-for-asset-managers]]). Only move to [[lstm-trading|LSTMs]] or [[transformer-trading|transformers]] if the baseline is inadequate and you have sufficient data (Source: [[book-artificial-intelligence-in-finance]]). Train on the training set only.

### Step 6: Hyperparameter Tuning
Use Bayesian optimization ([[optuna|Optuna]]) on the validation set. Avoid exhaustive grid search — it increases [[overfitting-in-trading|overfitting]] risk through multiple testing. Limit the number of hyperparameter combinations tested.

### Step 7: Backtesting
Simulate execution with realistic transaction costs, slippage, market impact, and fill probabilities. Use walk-forward backtesting (retrain on expanding or rolling windows). Never optimize strategy rules on backtest results — that is curve fitting.

### Step 8: Paper Trading
Deploy on live data without real capital. Compare results to backtest expectations. Run for minimum 3-6 months for daily strategies — this is the true out-of-sample test.

### Step 9: Live Deployment
Deploy with strict risk controls: position limits, daily loss limits, kill switches. Start with minimal capital (Source: [[book-quantitative-trading-ernest-chan]]). Infrastructure: Docker, cloud (AWS/GCP), reliable data feeds, redundant execution.

### Step 10: Monitoring & Retraining
Monitor prediction accuracy, signal strength, PnL attribution, and feature drift. Retrain on schedule or when triggered by decay. See [[ai-trading-risks]].
## Common Mistakes

| Step | Mistake | Consequence |
|------|---------|-------------|
| Data | Survivorship bias in stock universe | Inflated backtest returns |
| Features | Using raw prices instead of returns | Non-stationarity breaks models |
| Labels | Predicting next-day close with today's close as feature | Trivial leakage |
| Split | Random shuffled cross-validation | Massive data leakage |
| Training | Using test set for any model selection | Overfitting to test set |
| Backtest | Ignoring transaction costs | Strategy is unprofitable after costs |
| Deploy | No kill switch or loss limits | Catastrophic drawdown |

## Implementation

```
Key tools at each stage:
- Data: pandas, yfinance, polygon.io, arctic (data storage)
- Features: pandas-ta, ta-lib, scikit-learn preprocessing
- Modeling: scikit-learn, xgboost, lightgbm, pytorch
- Validation: scikit-learn TimeSeriesSplit, mlfinance (purged CV)
- Tuning: optuna (Bayesian optimization)
- Backtesting: backtrader, vectorbt, zipline-reloaded
- Deployment: Docker, FastAPI, Redis (signal queue), cron (scheduling)
- Monitoring: Grafana, Prometheus, custom dashboards, PnL trackers
```

## Example Use Case

A daily equity long-short strategy: (1) collect OHLCV + fundamentals for Russell 1000, (2) engineer 25 [[feature-engineering-finance|features]], (3) label with triple-barrier method, (4) split with 5-day purge gap, (5) train [[xgboost-trading|XGBoost]], (6) tune with Optuna, (7) walk-forward backtest with quarterly retraining, (8) paper trade 4 months, (9) deploy with 2% daily loss limit, (10) monitor with automated drift detection and monthly retraining.

## Crypto Instantiation

For a crypto-specific build of this pipeline, the generic steps map onto dedicated pages. Start from [[ml-crypto-price-prediction]] — an end-to-end, buildable crypto pipeline — which wires together a crypto feature stage, [[triple-barrier-labeling|triple-barrier labels]] whose barrier widths scale to crypto's high, liquidation-prone volatility (Step 3), a [[meta-labeling|meta-labeling]] primary/secondary architecture that pairs an economic side signal with an ML confidence gate (Steps 3 and 5), and [[purged-kfold-cv|purged/combinatorial cross-validation]] for leakage-free validation (Step 4). To satisfy Step 2's stationarity requirement without discarding memory, apply [[fractional-differentiation]] to persistent price and on-chain series, and where the side model draws on many weak signals, fuse them first with [[composite-alpha-blending]]. Because crypto history is short and statistically thin, weight these validation and overfitting defenses more heavily than you would in equities.

## Sources

- [[book-advances-in-financial-ml]] — triple-barrier labeling, purged cross-validation, temporal train/test splits, and the overall ML pipeline framework for finance
- [[book-inside-the-black-box]] — quant fund architecture: alpha models, risk models, execution models, and how they connect in institutional pipelines
- [[book-hands-on-ml-algorithmic-trading]] — practical ML pipeline implementation with Python, feature engineering, and model evaluation for trading
- [[book-quantitative-trading-ernest-chan]] — independent quant setup, capital deployment, and practical backtesting considerations
- [[book-machine-learning-for-asset-managers]] — de Prado (2020) covers portfolio construction pipelines, hierarchical risk parity (HRP), and the importance of starting with simple models before adding complexity
- [[book-artificial-intelligence-in-finance]] — Hilpisch (2020) provides end-to-end deep learning pipeline implementations with Python for financial prediction and trading agent deployment

## Related

- [[feature-engineering-finance]] — step 2 of the pipeline, often the most impactful
- [[overfitting-in-trading]] — pipeline design is the primary defense
- [[xgboost-trading]] — recommended starting model for most pipelines
- [[ai-trading-risks]] — risk management at every pipeline step
- [[optuna]] — Bayesian optimization framework for step 6 (hyperparameter tuning)
- [[pybroker]] — ML-first backtesting framework that integrates training and backtesting

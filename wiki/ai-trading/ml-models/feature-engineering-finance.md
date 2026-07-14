---
title: Feature Engineering for Financial ML
type: concept
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [ai-trading, machine-learning, data-engineering]
difficulty: intermediate
related:
  - "[[feature-engineering-crypto]]"
  - "[[feature-selection-trading]]"
  - "[[xgboost-trading]]"
  - "[[random-forest-trading]]"
  - "[[overfitting-in-trading]]"
  - "[[ml-trading-pipeline]]"
  - "[[book-advances-in-financial-ml]]"
  - "[[book-hands-on-ml-algorithmic-trading]]"
  - "[[book-machine-learning-for-asset-managers]]"
---

## Overview

Feature engineering is the process of transforming raw market data into informative inputs for ML models. In financial ML, **feature quality matters more than model choice** (Source: [[book-advances-in-financial-ml]]) — an [[xgboost-trading|XGBoost model]] with excellent features will outperform an [[lstm-trading|LSTM]] with raw prices. The challenge is creating features that are stationary, informative, and not overfit to historical patterns. This page catalogs the main feature categories and best practices for financial feature engineering.

## How It Works

Raw market data (prices, volumes, fundamentals) is not directly suitable for most ML models. Prices are non-stationary, features have different scales, and predictive information is hidden in derived relationships. Feature engineering extracts and normalizes this into a tabular format where each row is a timestep and each column is a meaningful, stationary signal. The critical principle: **use returns and ratios, not raw levels** — a 5-day return of -3% is universally comparable across assets and time periods.

## Feature Categories

**1. Price-based features:**
- Simple and log returns (1d, 5d, 20d, 60d)
- Realized volatility (rolling standard deviation of returns)
- High-low range ratio, close-to-open gap
- Moving average ratios (price / MA20, MA5 / MA50)

**2. Technical indicators as features:**
- RSI(14), stochastic oscillator — momentum/overbought signals
- MACD histogram, signal line crossover distance
- Bollinger Band %B (position within bands), bandwidth
- ADX — trend strength; ATR — volatility

**3. Volume features:**
- On-Balance Volume (OBV) and OBV slope
- Volume ratio (current / 20-day average volume)
- VWAP distance (price deviation from VWAP)
- Volume-price trend (accumulation/distribution)

**4. Order book features (HFT):**
- Bid-ask spread, mid-price change, depth imbalance (bid vs. ask size)
- Order flow delta (aggressive buy volume - aggressive sell volume)

**5. Sentiment & alternative data:**
- [[nlp-sentiment-analysis|News sentiment]] scores, social media volume, put/call ratio, VIX
- Satellite imagery, credit card transaction volumes, web traffic, job postings

**6. Cross-asset features:**
- Sector relative strength, rolling beta to SPY, yield curve slope, credit spreads

## Crypto Features

Crypto markets add a distinct feature layer that has no clean equity analogue — perpetual [[funding-rates|funding]] (both a positioning signal and a real carry cash-flow), [[open-interest]] and liquidation dynamics, L2 [[order-book]] imbalance, cross-venue [[basis|basis]] and [[coinbase-premium|premium]], and [[on-chain-analysis|on-chain]] flows ([[exchange-netflow|netflow]], [[mvrv|MVRV]]/dormancy, whale-score). They also bring crypto-specific pitfalls: 24/7 markets with no session boundaries, funding-as-carry, thin low-float alts, dead-token survivorship, token-age effects, and the need for regime-conditional z-scoring. See **[[feature-engineering-crypto]]** for the full treatment, and **[[crypto-signal-library]]** for a browsable menu of crypto signal primitives mapped to data endpoints.

## Strengths & Weaknesses

**Strengths:**
- Good features make simple models perform like complex ones
- Domain knowledge translates directly into predictive power
- Feature importance analysis reveals what drives predictions (Source: [[book-machine-learning-for-asset-managers]])

**Weaknesses:**
- Time-consuming and requires deep market knowledge
- Easy to introduce look-ahead bias accidentally
- Too many features leads to [[overfitting-in-trading|overfitting]] (curse of dimensionality); alpha decay erodes features over time

## Implementation

```
- pandas / numpy — core computation
- ta-lib / pandas-ta — 100+ technical indicators
- scikit-learn — StandardScaler, feature selection (mutual_info, RFE)
- shap — feature importance and interaction effects
- statsmodels — stationarity tests (ADF), autocorrelation
```

## Best Practices

- **Stationarity**: test with ADF; use returns, differences, or z-scores — never raw levels (Source: [[book-advances-in-financial-ml]]) (Source: [[book-machine-learning-for-asset-managers]])
- **Normalization**: z-score using rolling windows (not global stats) to avoid look-ahead
- **Lag features**: include t-1, t-5, t-20 to give tabular models temporal context
- **No look-ahead**: every feature must use only data available at prediction time

## Sources

- [[book-advances-in-financial-ml]] — fractional differentiation for stationarity, feature importance via MDA/MDI, and the principle that feature quality dominates model choice
- [[book-hands-on-ml-algorithmic-trading]] — practical feature engineering recipes for financial ML, including alternative data features and NLP-derived signals
- [[book-machine-learning-for-asset-managers]] — de Prado (2020) covers feature importance via MDA/MDI, the dangers of multicollinearity in feature sets, and proper feature selection techniques for portfolio construction

## Related

- [[feature-engineering-crypto]] — the crypto-native specialization of this page
- [[feature-selection-trading]] — pruning the feature set with MDA/MDI and mutual information
- [[xgboost-trading]] — benefits most from good feature engineering
- [[random-forest-trading]] — feature importance helps guide engineering
- [[overfitting-in-trading]] — too many features is a primary overfitting cause
- [[ml-trading-pipeline]] — feature engineering is step 2 of the pipeline
- [[nlp-sentiment-analysis]] — sentiment as a feature category

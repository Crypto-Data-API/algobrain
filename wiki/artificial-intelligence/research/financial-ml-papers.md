---
title: "Financial ML Papers"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Financial ML Papers", "Trading ML Research"]
domain: [ai-trading]
difficulty: advanced
related: ["[[ai-research-overview]]", "[[landmark-ai-papers]]", "[[supervised-learning]]", "[[reinforcement-learning-trading]]", "[[xgboost-trading]]", "[[lstm-trading]]", "[[nlp-sentiment-analysis]]", "[[overfitting-in-trading]]", "[[artificial-intelligence]]"]
---

# Financial ML Papers

Key academic papers on machine learning for trading and finance. These papers introduced methodologies, identified pitfalls, and established frameworks that inform how ML is applied to markets today. Unlike general AI papers (which announce new architectures), financial ML papers often focus on **what doesn't work** and why — which is arguably more valuable for traders.

## Essential Reading

### Methodology & Frameworks

| Paper | Author(s) | Year | Key Contribution |
|-------|----------|------|-----------------|
| *Advances in Financial Machine Learning* | Marcos López de Prado | 2018 | **The reference book.** Triple barrier labelling, meta-labelling, purged k-fold CV, fractional differentiation. Codified best practices for ML in trading |
| *Machine Learning for Asset Managers* | López de Prado | 2020 | Portfolio construction with ML, hierarchical risk parity, feature importance |
| *The Cross-Section of Expected Returns* | Harvey, Liu, Zhu | 2016 | **Multiple testing correction** — most published "factors" are false discoveries. Of 400+ published factors, most don't survive correction |
| *Empirical Asset Pricing via Machine Learning* | Gu, Kelly, Xiu | 2020 | Comprehensive comparison of ML methods for stock return prediction. Neural nets and tree models outperform linear for cross-sectional returns |
| *Deep Learning for Finance* | Dixon, Halperin, Bilokon | 2020 | Book covering deep learning applications across finance — derivatives pricing, risk, trading |

### What Works (and What Doesn't)

| Paper | Key Finding | Trading Implication |
|-------|-----------|-------------------|
| *Can Machine Learning Predict Stock Returns?* (various) | ML models achieve statistically significant but economically small prediction of returns | Don't expect large R² — even R² = 0.01-0.05 can be economically significant after transaction costs |
| *Stock Market Prediction Using LSTM* (various) | LSTMs can predict price direction slightly above random | [[lstm-trading|LSTM]] works but barely — success depends on features, not architecture |
| *FinBERT: Financial Sentiment Analysis with BERT* (Araci, 2019) | Finance-specific BERT outperforms general BERT on financial text | [[finbert|Domain-specific models]] beat general models for financial NLP |
| *Gradient Boosting for Stock Return Prediction* (various) | [[xgboost-trading|XGBoost/LightGBM]] consistently competitive with deep learning on tabular financial data | Don't over-engineer — tree models are hard to beat on structured data |

### Critical Warnings

| Paper | Warning | Why You Must Read This |
|-------|---------|----------------------|
| *Pseudo-Mathematics and Financial Charlatanism* (López de Prado, 2019) | Most backtested trading strategies are false discoveries due to multiple testing | Your amazing backtest is probably overfit |
| *Backtesting* (Harvey & Liu, 2015) | Sharpe ratios from backtests are inflated by selection bias | Adjust for how many strategies you tested to find this one |
| *The Deflated Sharpe Ratio* (Bailey & López de Prado, 2014) | Correct Sharpe ratio for number of trials, data length, skewness | The real Sharpe of your strategy is lower than the backtest shows |
| *Benchmarks of Machine Learning for Financial Markets* (various) | Many published financial ML results don't replicate | Be sceptical of claimed performance — reproduce before deploying |

### Reinforcement Learning for Trading

| Paper | Key Contribution |
|-------|-----------------|
| *Deep Reinforcement Learning for Optimal Execution* (Ning et al., 2021) | RL agents learn to split large orders optimally — outperform TWAP/VWAP |
| *A Deep RL Framework for Optimal Trading* (Deng et al., 2017) | Early framework for RL portfolio management — showed potential but fragility |
| *Practical Deep RL for Order Execution* (Karpe et al., 2020) | Production-focused: addresses sim-to-real gap, realistic market impact |

### NLP for Finance

| Paper | Key Contribution |
|-------|-----------------|
| *FinBERT* (Araci, 2019) | [[finbert|Financial BERT]] for sentiment — the standard financial NLP model |
| *When Words Sway Markets* (Tetlock, 2007) | Foundational paper showing media pessimism predicts market declines |
| *Lazy Prices* (Cohen et al., 2020) | Changes in 10-K language predict future returns — textual analysis has alpha |
| *Earnings Call NLP* (various) | Management tone in earnings calls predicts post-earnings drift |

## The López de Prado Canon

Marcos López de Prado's work deserves special attention — he's the most influential voice on ML trading methodology:

1. **Triple Barrier Method**: Label trades based on hitting profit target, stop loss, or time expiry (not just future return)
2. **Meta-Labelling**: Train a second model to predict whether the first model's signal will be profitable (precision over recall)
3. **Purged K-Fold CV**: [[cross-validation-trading|Time-series cross-validation]] that removes data leakage from overlapping labels
4. **Fractional Differentiation**: Make time series stationary while preserving memory — better features
5. **Deflated Sharpe Ratio**: Correct for how many strategies you tested

## See Also

- [[ai-research-overview]] — Research hub
- [[academic-papers-quant-finance]] — Classic factor / asset-pricing papers (complementary, non-ML)
- [[landmark-ai-papers]] — General AI papers
- [[supervised-learning]] — The paradigm most financial ML uses
- [[xgboost-trading]] — The model most financial ML papers use
- [[overfitting-in-trading]] — The core warning from financial ML research
- [[cross-validation-trading]] — Proper validation methodology
- [[nlp-sentiment-analysis]] — Applied financial NLP
- [[artificial-intelligence]] — AI section hub

## Sources

- López de Prado, M. (2018) — *Advances in Financial Machine Learning* (Wiley)
- López de Prado, M. (2020) — *Machine Learning for Asset Managers* (Cambridge)
- Harvey, Liu & Zhu (2016) — "...and the Cross-Section of Expected Returns" (*Review of Financial Studies*)
- Gu, Kelly & Xiu (2020) — "Empirical Asset Pricing via Machine Learning" (*Review of Financial Studies*)
- Bailey & López de Prado (2014) — "The Deflated Sharpe Ratio" (*Journal of Portfolio Management*)
- Araci, D. (2019) — "FinBERT: Financial Sentiment Analysis with Pre-trained Language Models"
- Tetlock, P. (2007) — "Giving Content to Investor Sentiment" (*Journal of Finance*); Cohen, Malloy & Nguyen (2020) — "Lazy Prices" (*Journal of Finance*)

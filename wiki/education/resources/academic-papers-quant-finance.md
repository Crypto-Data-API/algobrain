---
title: Landmark Academic Papers in Quant Finance
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [education, academic, research, machine-learning]
related:
  - "[[factor-investing]]"
  - "[[ml-for-trading-specialization]]"
  - "[[financial-engineering-coursera]]"
---

# Landmark Academic Papers Every Quant Should Read

These papers form the intellectual foundation of modern quantitative and AI-driven trading. Each one introduced concepts that changed how markets are understood and traded. Reading the originals — not just summaries — builds the deep understanding that separates rigorous quants from recipe followers.

## Factor Models and Asset Pricing

**Fama & French (1993) — "Common Risk Factors in the Returns on Stocks and Bonds"**
Introduced the three-factor model: market, size (SMB), and value (HML). Showed that CAPM alone is insufficient to explain stock returns. Foundation of [[factor-investing]]. Every multi-factor model you build descends from this paper.

**Carhart (1997) — "On Persistence in Mutual Fund Performance"**
Added momentum as the fourth factor. Demonstrated that most mutual fund "alpha" is explained by exposure to known factors. Key implication: your ML model needs to beat the four-factor benchmark, not just the market.

**Jegadeesh & Titman (1993) — "Returns to Buying Winners and Selling Losers"**
Documented the momentum effect — stocks that went up continue to go up (3-12 month horizon). One of the most robust anomalies in finance. Still profitable when implemented carefully with proper risk management.

## Machine Learning in Finance

**Gu, Kelly & Xiu (2020) — "Empirical Asset Pricing via Machine Learning"**
The definitive study comparing ML methods for stock return prediction. Tested linear models, trees, neural networks, and ensemble methods on decades of data. Key finding: neural networks and tree ensembles significantly outperform linear models. Gradient boosted trees provide the best risk-adjusted performance.

**Marcos Lopez de Prado (2018) — "Advances in Financial Machine Learning"**
Not a single paper but a book that introduced numerous techniques now standard in the field: triple barrier labeling, fractional differentiation, meta-labeling, combinatorial purged cross-validation. Changed how financial data is prepared for ML. Implementations available in the mlfinlab library (see [[github-repos-for-trading]]).

## Deep Learning for Trading

**Bao, Yue & Rao (2017) — "A Deep Learning Framework for Financial Time Series"**
Combined wavelet transforms with stacked autoencoders and LSTM networks for stock prediction. Demonstrated that deep learning can capture non-linear patterns in financial time series that traditional methods miss.

**Fischer & Krauss (2018) — "Deep Learning with Long Short-Term Memory Networks for Financial Market Predictions"**
Applied LSTM networks to predict S&P 500 constituent returns. Showed significant out-of-sample profitability after transaction costs. Important for establishing that deep learning can work in finance, not just in computer vision and NLP.

## How to Read These Papers

1. Read the abstract and conclusion first to understand the claim
2. Study the methodology section to understand how they tested it
3. Look at the data section critically — period, universe, frequency
4. Check for out-of-sample testing and robustness checks
5. Search for replication studies and critiques
6. Implement the core idea yourself using [[python-quant-stack]]

## Where to Find Papers

Most are available free on SSRN (ssrn.com), arXiv (arxiv.org), or Google Scholar. University library access (even alumni access) unlocks paywalled journals.

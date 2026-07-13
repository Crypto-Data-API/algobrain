---
title: "Machine Learning in Finance: From Theory to Practice — Dixon, Halperin, Bilokon (2020)"
type: source
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [book, machine-learning, derivatives, reinforcement-learning, quantitative]
aliases: ["Machine Learning in Finance", "Dixon Halperin Bilokon", "ML in Finance"]
related: ["[[reinforcement-learning-trading]]", "[[ml-trading-pipeline]]", "[[feature-engineering-finance]]", "[[xgboost-trading]]", "[[random-forest-trading]]", "[[options-greeks]]", "[[machine-learning-in-finance]]"]
source_type: book
source_author: "Matthew Dixon, Igor Halperin, Paul Bilokon"
source_date: 2020
confidence: high
claims_count: 10
---

The most mathematically rigorous textbook on machine learning for finance, authored by Matthew Dixon (Illinois Institute of Technology), Igor Halperin (NYU), and Paul Bilokon (Imperial College London). Published by Springer in their quantitative finance series, the book provides full mathematical derivations connecting ML methods to financial theory. Coverage spans supervised learning, [[reinforcement-learning-trading|reinforcement learning]], inverse reinforcement learning, Gaussian processes, Bayesian neural networks, GANs for synthetic data, and model interpretability — with particular depth on derivatives applications including ML-based options pricing, hedging, and [[options-greeks|Greeks]] estimation. The book uniquely bridges academic ML research with quantitative finance practice at a graduate level.

## Key Claims

1. [HIGH] **Supervised learning for finance requires careful treatment of non-stationarity, autocorrelation, and regime changes**: Financial time series violate the i.i.d. assumption underpinning standard ML methods. The authors provide rigorous frameworks for detecting non-stationarity (unit root tests, structural break tests), handling autocorrelation in features and targets, and adapting models to regime changes through windowed training and regime-conditional models. (Source: Dixon, Halperin, Bilokon)

2. [HIGH] **Gaussian processes provide uncertainty quantification that point-estimate models lack**: GPs produce a full posterior predictive distribution rather than a single point estimate, enabling principled uncertainty quantification for risk management and position sizing. The posterior uncertainty naturally widens in regions of sparse training data and narrows where data is dense, providing a built-in measure of model confidence. (Source: Dixon, Halperin, Bilokon)

3. [HIGH] **Inverse reinforcement learning can recover the implicit reward functions of expert traders**: Given a dataset of an expert trader's historical decisions (entries, exits, position sizes), inverse RL algorithms (MaxEnt IRL, Bayesian IRL) infer the reward function the trader was implicitly optimizing. This enables learning from expert behavior without requiring explicit labeling of "good" vs. "bad" trades. (Source: Dixon, Halperin, Bilokon)

4. [HIGH] **Q-learning and policy gradient methods learn optimal hedging strategies for derivatives portfolios**: RL agents trained to dynamically hedge options portfolios discover hedging policies that outperform Black-Scholes delta hedging under realistic conditions: discrete rebalancing intervals, transaction costs, stochastic volatility, and jumps. The learned policies naturally adapt hedge ratios to the current market regime. (Source: Dixon, Halperin, Bilokon)

5. [HIGH] **Kernel methods and SVMs remain competitive with deep learning for small financial datasets**: When training data is limited (hundreds to low thousands of observations — common for many financial prediction tasks), support vector machines and kernel methods with appropriate regularization often match or outperform deep neural networks. The authors provide guidance on when deep learning's capacity is warranted versus when simpler models suffice. (Source: Dixon, Halperin, Bilokon)

6. [HIGH] **GANs can create synthetic financial data for augmenting limited training sets**: Generative adversarial networks — particularly conditional GANs and Wasserstein GANs — can generate realistic synthetic price paths, volatility surfaces, and order book states. These augment limited real data for training and provide diverse scenarios for stress testing. The authors address the challenge of ensuring generated data preserves stylized facts of financial returns. (Source: Dixon, Halperin, Bilokon)

7. [HIGH] **The no-arbitrage principle constrains ML models**: Financial predictions must be consistent with the absence of arbitrage — this is a hard economic constraint, not a soft regularization term. The book demonstrates how to encode no-arbitrage conditions (put-call parity, monotonicity of call prices in strike, convexity) as architectural constraints in neural networks for options pricing. (Source: Dixon, Halperin, Bilokon)

8. [HIGH] **Feature engineering for derivatives requires encoding Greeks, moneyness, time-to-expiry, and term structure**: Derivatives ML models require a richer feature space than equity models: delta, gamma, vega, theta, moneyness (ITM/ATM/OTM), time-to-expiry, implied volatility surface coordinates, and the term structure of interest rates. The choice of feature representation (raw Greeks vs. normalized) significantly impacts model performance. (Source: Dixon, Halperin, Bilokon)

9. [HIGH] **Bayesian neural networks provide posterior distributions over predictions rather than point estimates**: By placing prior distributions over network weights and performing approximate Bayesian inference (variational inference, MC dropout), Bayesian neural networks output predictive distributions that quantify model uncertainty. This is critical in finance where overconfident point predictions can lead to catastrophic position sizing errors. (Source: Dixon, Halperin, Bilokon)

10. [HIGH] **Model interpretability (SHAP, LIME) is essential for regulatory compliance and risk management**: Black-box ML models face adoption barriers in regulated financial institutions. SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations) provide post-hoc explanations of individual predictions, enabling compliance with regulatory requirements for model explainability and building trust with risk managers and portfolio managers. (Source: Dixon, Halperin, Bilokon)

## Concepts Referenced

- [[machine-learning]], [[deep-learning]]
- [[reinforcement-learning-trading]], [[options-greeks]]
- [[feature-engineering-finance]], [[ml-trading-pipeline]]
- [[xgboost-trading]], [[random-forest-trading]]
- [[risk-management]], [[derivatives]]

## Pages Backed

- [[reinforcement-learning-trading]] — Q-learning, policy gradients, and inverse RL for trading and hedging
- [[ml-trading-pipeline]] — supervised learning pipeline adapted for financial data challenges
- [[feature-engineering-finance]] — derivatives feature engineering (Greeks, moneyness, term structure)
- [[xgboost-trading]] — ensemble methods with mathematical foundations
- [[random-forest-trading]] — random forest models with rigorous feature importance analysis
- [[options-greeks]] — ML-based Greeks estimation and no-arbitrage constrained pricing

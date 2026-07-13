---
title: "Hands-On Machine Learning for Algorithmic Trading — Stefan Jansen (2018)"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [education, book, machine-learning, python]
related:
  - "[[nlp-sentiment-analysis]]"
  - "[[reinforcement-learning-trading]]"
  - "[[feature-engineering-finance]]"
  - "[[ml-trading-pipeline]]"
---

## Overview

**Hands-On Machine Learning for Algorithmic Trading** by Stefan Jansen (2018) is the most practical, code-first book for building ML trading systems in Python. Spanning nearly 800 pages, it covers the full spectrum of modern ML applied to finance: from classical techniques (linear models, decision trees, random forests) to deep learning (CNNs, RNNs, autoencoders) to reinforcement learning for trading. The book is built around Jupyter notebooks with working code throughout. It also covers alternative data sources (satellite imagery, social media, SEC filings) and NLP techniques for extracting alpha from text. Jansen treats ML for trading as an engineering discipline, not just a research exercise.

## Key Takeaways

- **The ML for trading pipeline is end-to-end.** Data sourcing, feature engineering, model training, backtesting, and deployment are all covered with working code.
- **NLP is a powerful source of alpha.** Sentiment analysis of news, earnings calls, SEC filings, and social media can generate signals that complement price-based features.
- **Alternative data creates new edges.** Satellite imagery, credit card data, web scraping, and app usage data provide information advantages unavailable from price alone.
- **Deep learning has specific financial applications.** CNNs for pattern recognition in price charts, RNNs/LSTMs for sequential data, autoencoders for feature extraction and anomaly detection.
- **Reinforcement learning reframes trading as a sequential decision problem.** RL agents learn optimal policies for entry, exit, and position sizing through interaction with market environments.
- **Feature engineering matters more than model selection.** The same model with better features dramatically outperforms a fancier model with naive features.
- **Backtesting ML strategies requires special care.** Walk-forward validation, purging, and embargoing are essential to prevent overfitting.

## Who Should Read This

Python developers and data scientists who want to apply their ML skills to trading. Quants transitioning from traditional statistics to machine learning. Anyone who learns best by running code and seeing results. Prerequisite: comfort with Python, pandas, and basic ML concepts.

## How It Applies to AI Trading

This is the most directly applicable book for building AI trading systems. Every chapter produces working code that can be adapted to real trading. The [[nlp-sentiment-analysis]] chapters show how to build sentiment signals from scratch. The [[reinforcement-learning-trading]] chapters implement RL agents that learn to trade. The feature engineering sections directly inform [[feature-engineering-finance]] practices. The backtesting framework addresses [[ml-trading-pipeline]] requirements. Unlike more theoretical texts, Jansen gives you a codebase you can modify and deploy — making this the bridge between learning and doing.

## Rating

**8/10** — The most practical ML trading book with real code. Some sections could use deeper theoretical grounding, and the pace of ML evolution means some libraries are dated. But the concepts, architecture, and approach remain highly relevant. Pairs excellently with [[advances-in-financial-ml]] for theory.

## Related

- [[nlp-sentiment-analysis]] — NLP techniques for extracting trading signals from text
- [[reinforcement-learning-trading]] — RL-based trading agents covered in depth
- [[feature-engineering-finance]] — Practical feature construction for financial ML
- [[ml-trading-pipeline]] — The end-to-end system this book helps you build
- [[advances-in-financial-ml]] — The theoretical companion to this practical book

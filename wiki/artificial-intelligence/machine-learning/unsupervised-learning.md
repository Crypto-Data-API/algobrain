---
title: "Unsupervised Learning"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Unsupervised Learning", "Unsupervised ML", "Clustering"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[supervised-learning]]", "[[reinforcement-learning]]", "[[machine-learning-vs-deep-learning]]", "[[types-of-ai]]", "[[embeddings-vector-databases]]", "[[feature-engineering-finance]]", "[[foundation-models]]", "[[artificial-intelligence]]"]
---

# Unsupervised Learning

**Unsupervised learning** finds hidden patterns and structures in data without labeled examples. Unlike [[supervised-learning|supervised learning]] where the model knows "this is bullish, this is bearish," unsupervised models discover groupings, anomalies, and relationships on their own. It's the primary tool for market regime detection, anomaly identification, and dimensionality reduction in trading.

## How It Works

1. **Feed unlabeled data**: Raw features with no outcome labels
2. **Algorithm finds structure**: Clusters similar data points, identifies outliers, or compresses dimensions
3. **Human interprets**: The model discovers groups — you determine what they mean for trading

## Core Techniques

### Clustering

Group similar data points together. Models don't know what the clusters *mean* — that's your job.

| Algorithm | How It Works | Trading Use |
|-----------|-------------|-------------|
| **K-Means** | Assigns points to k nearest centroids | Market regime detection (cluster days by vol, correlation, trend) |
| **DBSCAN** | Density-based clustering, finds irregular shapes | Anomaly detection in order flow |
| **Gaussian Mixture Models** | Probabilistic cluster assignment | Regime classification with uncertainty estimates |
| **Hierarchical Clustering** | Tree of nested clusters | Sector/asset group discovery |

**Trading example — Regime Detection**:
Feed daily features (returns, volatility, correlation, VIX level) into K-Means with k=3. The algorithm might discover:
- **Cluster A**: Low vol, positive returns, low correlation → "Risk-on bull"
- **Cluster B**: High vol, negative returns, high correlation → "Crisis/sell-off"
- **Cluster C**: Low vol, flat returns, moderate correlation → "Range-bound"

Different trading strategies work in different regimes. Unsupervised learning identifies which regime you're in.

### Dimensionality Reduction

Compress many features into fewer dimensions while preserving information.

| Algorithm | Trading Use |
|-----------|-------------|
| **PCA** (Principal Component Analysis) | Reduce 50+ features to 3-5 principal components. Identify which factors drive returns |
| **t-SNE / UMAP** | Visualize high-dimensional data in 2D. Spot hidden clusters in stock behavior |
| **Autoencoders** | Neural network compression. Detect anomalies when reconstruction error is high |

**Trading example — Factor Discovery**:
Run PCA on 100 stock return series. The first principal component typically captures the "market factor" (beta to SPY). The second might capture a growth/value rotation. These are data-driven factors discovered without labels.

### Anomaly Detection

Identify data points that don't fit the normal pattern.

| Method | Trading Use |
|--------|-------------|
| **Isolation Forest** | Detect unusual trading volumes, price moves, or order patterns |
| **Autoencoders** | Flag transactions that reconstruct poorly (potential manipulation) |
| **Local Outlier Factor** | Identify stocks behaving differently from their usual cluster |

## Self-Supervised Learning (The Bridge to LLMs)

[[foundation-models|Foundation models]] (GPT-4, Claude, LLaMA) are trained using **self-supervised learning** — a form of unsupervised learning where the model predicts parts of its input from other parts:

- **Next token prediction**: Given "The Federal Reserve raised", predict "interest"
- **Masked token prediction**: Given "Apple reported [MASK] billion in revenue", predict "$94.8"

This enables training on massive unlabeled text corpora, which is why LLMs can be trained on the entire internet without anyone labeling each sentence.

## When to Use Unsupervised vs Supervised

| Use Case | Approach |
|----------|---------|
| "Will this stock go up?" | [[supervised-learning|Supervised]] (classification) |
| "What market regime are we in?" | **Unsupervised** (clustering) |
| "Is this order flow unusual?" | **Unsupervised** (anomaly detection) |
| "What factors drive returns?" | **Unsupervised** (PCA) |
| "What sentiment is this headline?" | [[supervised-learning|Supervised]] (classification) |
| "Which stocks behave similarly?" | **Unsupervised** (clustering) |
| "How should I compress these features?" | **Unsupervised** (dimensionality reduction) |
| "Find similar documents to this research note" | **Unsupervised** ([[embeddings-vector-databases|embeddings]]) |

## See Also

- [[supervised-learning]] — Learning with labels
- [[reinforcement-learning]] — Learning through trial and error
- [[embeddings-vector-databases]] — Unsupervised representations for semantic search
- [[feature-engineering-finance]] — Creating features that unsupervised models analyze
- [[foundation-models]] — Self-supervised learning at scale
- [[machine-learning-vs-deep-learning]] — The broader hierarchy
- [[ml-trading-pipeline]] — End-to-end pipeline
- [[artificial-intelligence]] — AI section hub

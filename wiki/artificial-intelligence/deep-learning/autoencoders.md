---
title: "Autoencoders"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Autoencoder", "VAE", "Variational Autoencoder"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[deep-learning-overview]]", "[[neural-networks]]", "[[unsupervised-learning]]", "[[generative-adversarial-networks]]", "[[diffusion-models]]", "[[embeddings-vector-databases]]", "[[feature-engineering-finance]]", "[[artificial-intelligence]]"]
---

# Autoencoders

An **autoencoder** is a neural network that learns to compress data into a lower-dimensional representation (encoding) and then reconstruct it (decoding). The compressed representation captures the most important features of the data. In trading, autoencoders are used for anomaly detection, dimensionality reduction, denoising, and as building blocks for other generative models.

## Architecture

```
Input (100 features) → Encoder → Bottleneck (10 features) → Decoder → Reconstructed Input
```

The network is forced to learn an efficient compression because the bottleneck is smaller than the input. Whatever information survives the compression is what the model considers most important.

## Variants

| Variant | Innovation | Trading Use |
|---------|-----------|-------------|
| **Vanilla autoencoder** | Simple compression/reconstruction | Dimensionality reduction for feature engineering |
| **Denoising autoencoder** | Trained to reconstruct from corrupted input | Denoise financial data, remove market microstructure noise |
| **Variational autoencoder (VAE)** | Learns a probability distribution in latent space | Generate synthetic data, scenario modeling |
| **Sparse autoencoder** | Forces most latent units to be inactive | Discover the few most important factors driving returns |
| **Temporal autoencoder** | Sequence-aware encoding | Time-series compression, regime fingerprinting |

## Trading Applications

### 1. Anomaly Detection
Train autoencoder on "normal" market data. When new data reconstructs poorly (high reconstruction error), it signals something unusual:
- Unusual trading patterns (potential manipulation)
- Market regime changes
- Earnings surprise detection (filing language deviates from historical norm)
- Flash crash early warning

### 2. Feature Engineering
Use the bottleneck layer as compressed features for downstream models:
- Compress 100+ raw features into 10 latent factors
- These learned factors often capture meaningful market structure (similar to PCA but non-linear)
- Feed compressed features into [[xgboost-trading|XGBoost]] or other [[supervised-learning|supervised models]]

### 3. Denoising
Financial data is noisy. Denoising autoencoders can:
- Smooth price series while preserving important structure
- Clean order book data from microstructure noise
- Extract signal from noisy alternative data sources

### 4. Synthetic Data (VAE)
Variational autoencoders generate new data by sampling from the learned latent distribution:
- Generate synthetic return paths for [[backtesting-pitfalls|backtesting augmentation]]
- Create realistic market scenarios for stress testing
- Less powerful than [[generative-adversarial-networks|GANs]] or [[diffusion-models]] but easier to train

## Autoencoders vs Other Approaches

| Task | Autoencoder | Alternative | When to Use Autoencoder |
|------|------------|-------------|------------------------|
| **Anomaly detection** | Reconstruction error | Isolation Forest | When you have lots of "normal" data |
| **Dimensionality reduction** | Non-linear compression | PCA (linear) | When relationships are non-linear |
| **Data generation** | VAE | [[generative-adversarial-networks|GAN]], [[diffusion-models|Diffusion]] | When training stability matters more than quality |
| **Denoising** | Denoising autoencoder | Kalman filter | When noise patterns are complex/non-linear |

## See Also

- [[deep-learning-overview]] — Deep learning hub
- [[unsupervised-learning]] — The paradigm autoencoders operate in
- [[generative-adversarial-networks]] — Alternative generative model
- [[diffusion-models]] — Newer generative approach
- [[embeddings-vector-databases]] — Related compression concept
- [[feature-engineering-finance]] — Where autoencoder features are used
- [[neural-networks]] — The building block
- [[artificial-intelligence]] — AI section hub

## Sources

- Kingma & Welling, "Auto-Encoding Variational Bayes" (2013), arXiv:1312.6114 — the VAE
- Vincent et al., "Extracting and Composing Robust Features with Denoising Autoencoders" (ICML 2008)
- Gu, Kelly, Xiu, "Autoencoder Asset Pricing Models" (Journal of Econometrics, 2021) — non-linear latent factors for cross-sectional returns
- Goodfellow, Bengio, Courville, "Deep Learning" (MIT Press, 2016), ch. 14 — autoencoders

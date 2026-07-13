---
title: "Synthetic Data Generation"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Synthetic Data", "Data Augmentation", "Synthetic Market Data"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[generative-ai-overview]]", "[[generative-adversarial-networks]]", "[[diffusion-models]]", "[[autoencoders]]", "[[gan-synthetic-data]]", "[[backtesting-pitfalls]]", "[[monte-carlo-backtesting]]", "[[artificial-intelligence]]"]
---

# Synthetic Data Generation

**Synthetic data generation** creates artificial datasets that mimic the statistical properties of real data. For trading, synthetic market data addresses a fundamental limitation: you only have one historical record per asset. Generative models ([[generative-adversarial-networks|GANs]], [[diffusion-models|diffusion models]], [[autoencoders|VAEs]]) produce alternative market histories for more robust backtesting, stress testing, and model training.

## Why Synthetic Data for Trading

| Problem | How Synthetic Data Helps |
|---------|------------------------|
| **Limited history** | One Bitcoin price history since 2009 → generate 10,000 plausible alternatives |
| **Rare events** | Only a few crashes in history → generate thousands of crash scenarios |
| **[[overfitting-in-trading|Overfitting]]** | Model memorises the single historical path → test on diverse synthetic paths |
| **Strategy robustness** | Strategy works on history → does it work on statistically similar but different paths? |
| **Data privacy** | Can't share real client data → generate synthetic equivalent for research |

## Generation Methods

| Method | How | Quality | Trading Application |
|--------|-----|---------|-------------------|
| **[[generative-adversarial-networks|GAN]]** (TimeGAN, FinGAN) | Generator vs discriminator adversarial training | Good | Time-series paths preserving stylised facts |
| **[[diffusion-models|Diffusion]]** (FinDiff, TimeGrad) | Iterative denoising from noise | Better | Higher quality paths, better distribution coverage |
| **[[autoencoders|VAE]]** | Encode to latent space, sample, decode | Moderate | Simpler, more stable training |
| **Copula models** | Statistical dependency modelling | Good for distributions | Cross-asset correlation-preserving scenarios |
| **Bootstrap** | Resample with replacement from real data | Fast, simple | Quick robustness checks |
| **[[monte-carlo-backtesting|Monte Carlo]]** | Parametric simulation from fitted distribution | Established | Traditional scenario generation |

## What "Good" Synthetic Data Preserves

Financial data has unique statistical properties (**stylised facts**) that synthetic data must reproduce:

| Stylised Fact | What It Means | Test |
|-------------|--------------|------|
| **Fat tails** | Extreme moves more frequent than normal distribution | Kurtosis, QQ-plot |
| **Volatility clustering** | High-vol periods follow high-vol periods | ARCH effects test |
| **Leverage effect** | Negative returns increase volatility more than positive | Asymmetric correlation |
| **Mean reversion** | Returns tend to mean-revert at long horizons | Autocorrelation at multiple lags |
| **Cross-asset correlation** | Assets move together, especially in crises | Correlation matrix comparison |
| **Volume patterns** | U-shaped intraday volume, event-driven spikes | Volume distribution tests |

Synthetic data that violates these properties will produce misleading backtest results.

## Practical Workflow

```
1. Collect real market data (OHLCV, fundamentals, etc.)
2. Train generative model on real data
3. Validate: compare statistical properties of synthetic vs real
4. Generate N synthetic datasets (1000+ for robustness)
5. Backtest strategy on all synthetic datasets
6. Evaluate: strategy works on >80% of synthetic paths → robust
7. Strategy only works on specific paths → likely overfitting
```

## Limitations

- **Out-of-distribution events**: Generative models learn from history — they won't generate truly unprecedented events (COVID crash, 9/11)
- **Correlation structure**: Preserving realistic cross-asset correlations, especially during stress, is the hardest part
- **Validation**: How do you prove synthetic data is "realistic enough"? Statistical tests help but aren't definitive
- **False confidence**: Passing synthetic tests doesn't guarantee live performance — it's necessary but not sufficient

## See Also

- [[generative-ai-overview]] — GenAI hub
- [[gan-synthetic-data]] — Applied GAN implementations
- [[generative-adversarial-networks]] — GAN architecture
- [[diffusion-models]] — Diffusion architecture
- [[autoencoders]] — VAE architecture
- [[monte-carlo-backtesting]] — Traditional Monte Carlo approach
- [[backtesting-pitfalls]] — Why synthetic augmentation matters
- [[overfitting-in-trading]] — What synthetic testing helps detect
- [[artificial-intelligence]] — AI section hub

## Sources

- Yoon, Jarrett & van der Schaar, "Time-series Generative Adversarial Networks (TimeGAN)," NeurIPS 2019 — the canonical reference for GAN-based time-series synthesis that preserves stylised facts.
- Cont, R., "Empirical properties of asset returns: stylized facts and statistical issues," Quantitative Finance (2001) — the standard catalogue of the stylised facts (fat tails, volatility clustering, leverage effect) synthetic data must reproduce.
- General literature on diffusion models for time series (FinDiff, TimeGrad) and variational autoencoders for financial scenario generation.

---
title: "Deep Learning"
type: overview
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Deep Learning", "DL", "deep-learning"]
related: ["[[neural-networks]]", "[[machine-learning-vs-deep-learning]]", "[[supervised-learning]]", "[[convolutional-neural-networks]]", "[[recurrent-neural-networks]]", "[[transformer-architecture]]", "[[generative-adversarial-networks]]", "[[diffusion-models]]", "[[autoencoders]]", "[[foundation-models]]", "[[artificial-intelligence]]"]
---

# Deep Learning

**Deep learning** is the subset of [[machine-learning-overview|machine learning]] that uses [[neural-networks|neural networks]] with many layers (hence "deep") to automatically learn hierarchical representations from data. Unlike traditional ML where you hand-craft features, deep learning models learn their own features — making them dominant for unstructured data (text, images, audio) and increasingly powerful for structured financial data.

## Architecture Map

```
Deep Learning
├── Feedforward Networks (basic)
├── [[convolutional-neural-networks|CNNs]] — spatial patterns (charts, images)
├── [[recurrent-neural-networks|RNNs / LSTMs]] — sequential data (time series)
├── [[transformer-architecture|Transformers]] — attention-based (LLMs, NLP)
├── [[generative-adversarial-networks|GANs]] — generate synthetic data
├── [[diffusion-models|Diffusion Models]] — high-quality generation
└── [[autoencoders|Autoencoders]] — compression & anomaly detection
```

## Architectures by Trading Application

| Architecture | Input Type | Trading Application | Key Page |
|-------------|-----------|-------------------|----------|
| **[[convolutional-neural-networks|CNN]]** | Images, 2D patterns | Chart pattern recognition, satellite imagery | [[cnn-chart-recognition]] |
| **[[recurrent-neural-networks|RNN/LSTM]]** | Sequential time series | Price forecasting, volatility prediction | [[lstm-trading]] |
| **[[transformer-architecture|Transformer]]** | Text, sequences | [[nlp-sentiment-analysis|Sentiment]], [[llm-market-analysis|market analysis]], [[foundation-models|LLMs]] | [[transformer-trading]] |
| **[[generative-adversarial-networks|GAN]]** | Any (generates new data) | Synthetic training data, scenario generation | [[gan-synthetic-data]] |
| **[[diffusion-models|Diffusion Model]]** | Any (generates new data) | Synthetic data, time-series augmentation | [[diffusion-models]] |
| **[[autoencoders|Autoencoder]]** | Tabular, time series | Anomaly detection, dimensionality reduction, denoising | [[autoencoders]] |

## Why Deep Learning for Trading?

### Where It Excels
- **Unstructured data**: Text (earnings calls, news), images (charts, satellite), audio (Fed speeches)
- **Complex non-linear patterns**: Relationships too complex for hand-crafted features
- **Transfer learning**: [[foundation-models|Pre-trained models]] adapted to finance with minimal data

### Where Traditional ML Wins
- **Tabular data**: [[xgboost-trading|XGBoost]] still beats deep learning on structured price/volume/fundamental data
- **Small datasets**: Deep learning needs more data than traditional ML
- **Interpretability**: Decision trees are explainable; deep networks are black boxes
- **Training cost**: Deep learning requires GPUs; XGBoost runs on a laptop

See [[machine-learning-vs-deep-learning]] for the full comparison.

## Training Deep Learning Models

| Component | What It Does | Trading Consideration |
|-----------|-------------|---------------------|
| **Loss function** | Measures prediction error | MSE for regression, cross-entropy for classification |
| **Optimizer** | Updates weights (Adam, SGD) | Adam is default; learning rate is critical |
| **Regularization** | Prevents [[overfitting-in-trading|overfitting]] (dropout, weight decay) | Essential — financial data is noisy |
| **Batch size** | Training samples per step | Larger = faster but may miss fine patterns |
| **Epochs** | Full passes through data | Too many = overfitting; use early stopping |
| **GPU** | Hardware acceleration | [[nvidia-ai|NVIDIA]] GPUs required for training |

## See Also

- [[neural-networks]] — The fundamental building block
- [[machine-learning-vs-deep-learning]] — Where deep learning fits
- [[convolutional-neural-networks]] — CNNs for spatial patterns
- [[recurrent-neural-networks]] — RNNs/LSTMs for sequences
- [[transformer-architecture]] — Attention-based models (LLMs)
- [[generative-adversarial-networks]] — GANs for synthetic data
- [[diffusion-models]] — Diffusion for generation
- [[autoencoders]] — Compression and anomaly detection
- [[foundation-models]] — Very large deep learning models
- [[nvidia-ai]] — GPU hardware for training
- [[attention-mechanism]] — Core mechanism behind transformers
- [[artificial-intelligence]] — AI section hub

## Sources

- LeCun, Bengio, Hinton, "Deep Learning" (Nature, 2015) — survey by the field's founders
- Goodfellow, Bengio, Courville, "Deep Learning" (MIT Press, 2016) — standard textbook
- Grinsztajn, Oyallon, Varoquaux, "Why do tree-based models still outperform deep learning on tabular data?" (NeurIPS 2022) — basis for the XGBoost-vs-DL note
- López de Prado, "Advances in Financial Machine Learning" (Wiley, 2018) — ML pitfalls in finance

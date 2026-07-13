---
title: "Transformer Architecture"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning]
aliases: ["Transformer", "Transformers", "Attention Is All You Need"]
domain: [ai-trading]
difficulty: advanced
related: ["[[attention-mechanism]]", "[[foundation-models]]", "[[transformer-trading]]", "[[finbert]]", "[[lstm-trading]]", "[[recurrent-neural-networks]]", "[[artificial-intelligence]]"]
---

# Transformer Architecture

The **transformer** is the neural network architecture that powers all modern [[foundation-models|foundation models]] (GPT-4, Claude, Gemini, LLaMA). Introduced in the 2017 paper "Attention Is All You Need" by Vaswani et al., the transformer replaced recurrent networks ([[lstm-trading|LSTMs]]) as the dominant architecture for sequence processing, enabling the scale-up to billion-parameter models.

## Core Mechanism: Self-Attention

The key innovation is **self-attention** — a mechanism that allows every token in a sequence to attend to every other token, weighted by relevance. For a financial example:

> "Apple reported **revenue** of **$94.8 billion**, **beating** analyst expectations of $92.5 billion"

Self-attention allows the model to directly connect "revenue" with "$94.8 billion" and "beating" with "expectations" regardless of their distance in the text — something [[lstm-trading|LSTMs]] struggle with for long sequences. The mechanism computes three projections per token — query, key, and value — and weights each token's contribution by the dot-product similarity between queries and keys. See [[attention-mechanism]] for the detailed mechanics, including multi-head and causal attention.

Two structural choices distinguish transformer families:

- **Encoder-only** (BERT, [[finbert|FinBERT]]) — bidirectional attention; best for classification and embedding tasks like sentiment scoring
- **Decoder-only** (GPT, Claude, LLaMA) — causal (left-to-right) attention; best for generation and the dominant design for modern LLMs
- **Encoder-decoder** (T5, original 2017 transformer) — used for translation and sequence-to-sequence tasks

## Architecture Components

| Component | Function | Trading Analogy |
|-----------|----------|----------------|
| **Embedding layer** | Converts tokens to vectors | Converting raw market data to features |
| **Multi-head attention** | Multiple parallel attention patterns | Looking at price, volume, and sentiment simultaneously |
| **Feed-forward network** | Non-linear transformation | Combining features into signals |
| **Layer normalization** | Stabilizes training | Risk normalization across positions |
| **Positional encoding** | Encodes sequence order | Timestamps on market data |

## Why Traders Should Care

You don't need to understand the math to use transformers, but understanding the architecture explains:

1. **Context window limits**: Why models can only process a certain number of tokens (relates to attention's O(n²) scaling)
2. **Hallucinations**: Attention can create spurious correlations, especially on out-of-distribution data
3. **[[transformer-trading|Time-series transformers]]**: Adapted architectures (TFT, Informer) that use attention for price prediction
4. **[[finbert|FinBERT]]**: A transformer fine-tuned on financial text for [[nlp-sentiment-analysis|sentiment analysis]]

## See Also

- [[attention-mechanism]] — The core mechanism inside every transformer
- [[foundation-models]] — Models built on transformers
- [[transformer-trading]] — Transformers applied to trading time-series
- [[finbert]] — Financial sentiment transformer
- [[lstm-trading]] — The architecture transformers replaced
- [[artificial-intelligence]] — AI section hub

## Sources

- Vaswani et al., "Attention Is All You Need" (2017), arXiv:1706.03762 — original transformer paper
- Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers" (2018) — encoder-only design
- Lim et al., "Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting" (2019/2021) — TFT for financial time-series
- Zhou et al., "Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting" (AAAI 2021)

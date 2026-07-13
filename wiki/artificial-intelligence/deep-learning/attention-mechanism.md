---
title: "Attention Mechanism"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Attention", "Self-Attention", "Multi-Head Attention"]
domain: [ai-trading]
difficulty: advanced
related: ["[[transformer-architecture]]", "[[foundation-models]]", "[[recurrent-neural-networks]]", "[[deep-learning-overview]]", "[[transformer-trading]]", "[[artificial-intelligence]]"]
---

# Attention Mechanism

The **attention mechanism** is the core innovation that powers [[transformer-architecture|transformers]] and all modern [[foundation-models|large language models]]. It allows a model to focus on the most relevant parts of its input when producing each output — like a trader scanning a dense earnings report and focusing on the revenue and guidance numbers while ignoring boilerplate.

## The Core Idea

Given a sequence of inputs, attention computes a weighted average where the weights represent **relevance**:

For the sentence: *"Fed raises rates by 25 basis points, citing persistent inflation"*

When processing "inflation," attention assigns high weights to "raises," "rates," and "25 basis points" — the contextually relevant words — and low weights to "citing" and "by."

## Types of Attention

| Type | How It Works | Used In |
|------|-------------|---------|
| **Self-attention** | Each position attends to all other positions in the same sequence | [[transformer-architecture|Transformers]], [[foundation-models|LLMs]] |
| **Cross-attention** | One sequence attends to a different sequence | Translation, encoder-decoder models |
| **Multi-head attention** | Multiple parallel attention patterns, each capturing different relationships | All modern transformers |
| **Causal attention** | Each position can only attend to earlier positions (not future) | GPT-style autoregressive LLMs |

## Multi-Head Attention

Instead of one attention pattern, transformers run multiple attention "heads" in parallel. Each head can learn to focus on different aspects:

- **Head 1** might focus on syntactic relationships ("subject-verb")
- **Head 2** might focus on numerical associations ("revenue" → "$94.8 billion")
- **Head 3** might focus on sentiment cues ("beating" → positive)

The outputs of all heads are concatenated and combined.

## Why Attention Replaced RNNs

[[recurrent-neural-networks|RNNs/LSTMs]] process sequences one step at a time, making it hard to connect distant elements. Attention connects every position to every other position directly:

| Dimension | RNN/LSTM | Attention |
|-----------|---------|-----------|
| **Long-range dependencies** | Degrades over distance | Direct connection regardless of distance |
| **Parallelization** | Sequential (slow) | Fully parallel (fast on GPU) |
| **Computational cost** | O(n) per step | O(n²) total (quadratic in sequence length) |
| **Scalability** | Limited by vanishing gradients | Scales to millions of tokens |

The O(n²) cost is why [[foundation-models|LLMs]] have context window limits — processing 1M tokens requires attending to 1M × 1M position pairs. Much of the engineering progress since 2020 has been about defeating this scaling: **FlashAttention** (an IO-aware exact-attention kernel) cut memory use and made long contexts practical without approximation, while **sparse**, **linear**, and **sliding-window** attention variants trade some exactness for sub-quadratic cost. These advances are why modern models now ship with context windows of hundreds of thousands to a million tokens — enough to feed an entire 10-K filing or a year of intraday data into a single prompt.

## Trading-Specific Attention

In [[transformer-trading|financial transformers]], attention patterns reveal which time steps the model considers most important for prediction:

- **Temporal attention**: Model may focus on specific past dates (earnings days, Fed meetings)
- **Feature attention**: Model may focus on volume spikes rather than price when predicting volatility
- **Cross-asset attention**: In multi-asset models, attention shows which assets the model considers correlated

Visualizing attention weights can provide some interpretability for otherwise black-box deep learning models.

## See Also

- [[transformer-architecture]] — The architecture built on attention
- [[foundation-models]] — Models powered by attention
- [[recurrent-neural-networks]] — The architecture attention replaced
- [[transformer-trading]] — Attention applied to financial data
- [[deep-learning-overview]] — Deep learning hub
- [[artificial-intelligence]] — AI section hub

## Sources

- Vaswani et al., "Attention Is All You Need" (2017), arXiv:1706.03762 — scaled dot-product and multi-head attention
- Bahdanau, Cho, Bengio, "Neural Machine Translation by Jointly Learning to Align and Translate" (2014) — the original attention mechanism
- Dao et al., "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness" (NeurIPS 2022)
- Beltagy, Peters, Cohan, "Longformer: The Long-Document Transformer" (2020) — sparse/sliding-window attention

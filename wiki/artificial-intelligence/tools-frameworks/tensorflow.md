---
title: "TensorFlow"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["TensorFlow", "TF", "Keras"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[tools-frameworks-overview]]", "[[pytorch]]", "[[deep-learning-overview]]", "[[google-deepmind]]", "[[nvidia-ai]]", "[[model-deployment]]", "[[artificial-intelligence]]"]
---

# TensorFlow

**TensorFlow** is Google's open-source deep learning framework, originally released in 2015. It was the dominant ML framework until [[pytorch|PyTorch]] overtook it in research adoption around 2019-2020. TensorFlow retains strong positions in production deployment (TF Serving), mobile/edge AI (TFLite, now LiteRT), and Google Cloud's TPU ecosystem. A major shift since 2023: **Keras 3 is multi-backend** — the same Keras code can run on TensorFlow, [[pytorch|PyTorch]], or JAX backends — so Keras is no longer synonymous with TensorFlow and is increasingly used as a portable high-level API regardless of the underlying engine.

## Key Components

| Component | Purpose | Trading Use |
|-----------|---------|-------------|
| **TensorFlow Core** | Low-level tensor operations | Custom model architectures |
| **Keras** | High-level API (Keras 3 is **multi-backend**: TF/PyTorch/JAX) | Rapid prototyping, portable model building |
| **TF Serving** | Production model serving | Low-latency inference API |
| **TFLite** | Mobile/edge deployment | On-device inference (trading apps) |
| **TFX** | End-to-end [[mlops|ML pipeline]] | Production ML systems |
| **TensorBoard** | Visualisation and [[experiment-tracking|experiment tracking]] | Monitor training, compare runs |

## When to Choose TensorFlow

| Scenario | Choose TF | Why |
|----------|----------|-----|
| Existing TF codebase | Yes | Migration cost outweighs PyTorch benefits |
| Google Cloud / TPU deployment | Yes | Native TPU support |
| Mobile/edge inference | Consider | TFLite more mature than PyTorch Mobile |
| Production ML pipeline | Consider | TFX provides end-to-end orchestration |
| New research project | No — use [[pytorch|PyTorch]] | Industry standard for research |
| Using [[hugging-face|Hugging Face]] models | Either — but PyTorch is default | HF supports TF but community defaults to PyTorch |

## TensorFlow for Trading

The same trading tasks as [[pytorch|PyTorch]] but with Keras API:
- `tf.keras.layers.LSTM` for time series
- `tf.keras.applications` for pre-trained vision models
- TF Serving for low-latency production inference
- TensorBoard for tracking training metrics

## Related

- [[tools-frameworks-overview]] — Tools hub
- [[pytorch]] — Dominant alternative
- [[google-deepmind]] — TensorFlow's creator (Google)
- [[model-deployment]] — TF Serving for production
- [[mlops]] — TFX pipeline
- [[deep-learning-overview]] — What you build with TF
- [[artificial-intelligence]] — AI section hub

## Sources

- TensorFlow official documentation (tensorflow.org).
- Keras 3 multi-backend documentation (keras.io), 2023–2026.
- Abadi et al., "TensorFlow: A System for Large-Scale Machine Learning" (Google, OSDI 2016).
- Framework-adoption trends: Papers With Code (paperswithcode.com).

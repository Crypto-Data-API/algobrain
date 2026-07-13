---
title: "PyTorch"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["PyTorch", "torch"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[tools-frameworks-overview]]", "[[tensorflow]]", "[[deep-learning-overview]]", "[[neural-networks]]", "[[nvidia-ai]]", "[[meta-ai]]", "[[lstm-trading]]", "[[transformer-architecture]]", "[[artificial-intelligence]]"]
---

# PyTorch

**PyTorch** is the dominant deep learning framework, originally developed by [[meta-ai|Meta AI]] and released in 2016. It provides the tensor computation and automatic differentiation engine used to build, train, and deploy [[neural-networks|neural networks]]. Since 2022 it has been governed by the **PyTorch Foundation** under the **Linux Foundation** (vendor-neutral, with Meta as a primary contributor); the current stable line is **2.9.x** (mid-2026). PyTorch is the default framework in the large majority of AI research papers and at most AI labs — [[anthropic|Anthropic]] and [[google-deepmind|DeepMind]] also make heavy use of JAX, but PyTorch remains the lingua franca of applied deep learning.

## Why PyTorch Dominates

| Strength | Detail |
|----------|--------|
| **Pythonic** | Feels like regular Python — debug with print statements, use standard loops |
| **Dynamic computation graph** | Build graph on-the-fly (eager execution) — easier debugging than static graphs |
| **Research standard** | The large majority (~75%+) of NeurIPS/ICML papers with code use PyTorch |
| **`torch.compile`** | Since PyTorch 2.0, a single decorator JIT-compiles models for large speedups while keeping eager-mode debuggability |
| **Ecosystem** | [[hugging-face|Hugging Face]] Transformers, torchvision, torchaudio, torchtext all built on PyTorch |
| **Production** | TorchScript, ONNX export, TorchServe for deployment |
| **GPU acceleration** | Native [[nvidia-ai|CUDA]] support, distributed training across multi-GPU clusters |

## PyTorch for Trading

| Trading Task | PyTorch Component | Example |
|-------------|------------------|---------|
| **[[lstm-trading|LSTM]] price prediction** | `torch.nn.LSTM` | Build sequence model on OHLCV data |
| **[[transformer-trading|Transformer]] time series** | `torch.nn.Transformer` or HF Transformers | Temporal Fusion Transformer for forecasting |
| **[[cnn-chart-recognition|Chart pattern recognition]]** | `torchvision` + `torch.nn.Conv2d` | CNN classifier on candlestick chart images |
| **[[reinforcement-learning-trading|RL trading agent]]** | `torch` + Stable-Baselines3 | PPO/SAC agent for execution optimisation |
| **Custom loss functions** | `torch.nn.Module` | Sharpe-ratio-aware loss, asymmetric loss for directional prediction |
| **[[fine-tuning-llms|LLM fine-tuning]]** | HF Transformers + PEFT | LoRA fine-tune on financial text |

## PyTorch vs TensorFlow

| Dimension | PyTorch | [[tensorflow|TensorFlow]] |
|-----------|---------|------------|
| **Research adoption** | ~75% | ~20% |
| **Industry production** | Growing rapidly | Legacy presence (TF Serving, TFLite) |
| **Debugging** | Easy (eager by default) | Harder (graph mode historically) |
| **Mobile/edge** | ExecuTorch (newer) | TFLite (mature) |
| **TPU support** | Via JAX bridge | Native |
| **Learning curve** | Lower | Higher |
| **Community** | Larger, growing | Mature, stable |

**Verdict**: PyTorch for new projects. TensorFlow only if you have existing TF infrastructure or need TPU-native support.

## Key Libraries in the PyTorch Ecosystem

| Library | Purpose | Trading Use |
|---------|---------|-------------|
| **[[hugging-face|Transformers]]** | Pre-trained model access | [[finbert|FinBERT]], LLM inference, [[fine-tuning-llms|fine-tuning]] |
| **Lightning** (PyTorch Lightning) | Training boilerplate reduction | Faster experiment iteration |
| **Stable-Baselines3** | [[reinforcement-learning|RL]] algorithms (PPO, SAC, DQN) | Trading agent training |
| **torchvision** | Computer vision utilities | [[cnn-chart-recognition|Chart image]] preprocessing |
| **ONNX** | Model export to portable format | Deploy PyTorch models in production |
| **TorchServe** | Model serving (**deprecated 2025**) | Legacy; prefer NVIDIA Triton or a FastAPI wrapper for new deployments |

## Related

- [[tools-frameworks-overview]] — Tools hub
- [[tensorflow]] — Alternative framework
- [[scikit-learn]] — For traditional ML (complement to PyTorch)
- [[deep-learning-overview]] — What you build with PyTorch
- [[nvidia-ai]] — GPU hardware PyTorch runs on
- [[meta-ai]] — PyTorch's originator
- [[hugging-face]] — PyTorch-based model ecosystem
- [[model-deployment]] — Getting PyTorch models to production
- [[artificial-intelligence]] — AI section hub

## Sources

- PyTorch official documentation and release notes (pytorch.org), version 2.9.x current to mid-2026.
- PyTorch Foundation / Linux Foundation governance announcements (pytorch.org/foundation), 2022–2025.
- Paszke et al., "PyTorch: An Imperative Style, High-Performance Deep Learning Library" (NeurIPS 2019).
- Framework-adoption figures: Papers With Code framework trends (paperswithcode.com).

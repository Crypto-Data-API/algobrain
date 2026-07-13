---
title: "Model Deployment & Serving"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Model Deployment", "Model Serving", "ML Inference"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[tools-frameworks-overview]]", "[[mlops]]", "[[model-inference-vs-training]]", "[[cloud-trading-infrastructure]]", "[[artificial-intelligence]]"]
---

# Model Deployment & Serving

**Model deployment** is getting a trained ML model out of a notebook and into a system that makes predictions on live data. **Serving** is how the model receives requests and returns predictions in production. This is where most ML trading projects stall — the model works in backtesting but never gets deployed.

## Deployment Patterns

| Pattern | How | Best For |
|---------|-----|---------|
| **Batch inference** | Run model on all data periodically (hourly, daily) | End-of-day signal generation, portfolio rebalancing |
| **Online (real-time) inference** | Model serves predictions via API on demand | Live trading signals, real-time risk scoring |
| **Streaming inference** | Model processes continuous data stream | Order flow analysis, real-time sentiment |
| **Edge/embedded** | Model runs on local device | Low-latency trading, no network dependency |

## Deployment Stack

| Component | Options | Trading Consideration |
|-----------|---------|---------------------|
| **Model format** | ONNX, TorchScript, pickle, SavedModel | ONNX for framework-agnostic portability |
| **API framework** | FastAPI, Flask, gRPC | FastAPI for Python ML serving (async, fast) |
| **Containerisation** | Docker, Podman | Reproducible environment, easy scaling |
| **Orchestration** | Kubernetes, Docker Compose | Multi-model serving, auto-scaling |
| **Serving platform** | NVIDIA Triton, TF Serving, vLLM/TGI (LLMs) | Triton for GPU-accelerated multi-model; TorchServe is **deprecated** (as of 2025) — prefer Triton or a plain FastAPI wrapper |
| **Cloud ML** | AWS SageMaker, GCP Vertex AI, Azure ML | Managed deployment, pay-per-inference |
| **Monitoring** | Evidently, WhyLabs, Prometheus + Grafana | Drift detection, latency tracking |

## Trading Deployment Architecture

```
Market Data Feed
     ↓
Feature Pipeline (compute indicators, preprocess)
     ↓
Model Server (FastAPI + Docker)
     ↓
Signal → Risk Check → Order Management → Exchange API
     ↓
Monitoring Dashboard (latency, predictions, drift)
```

## Latency Considerations

| Timeframe | Latency Budget | Deployment Choice |
|-----------|---------------|-------------------|
| **Daily/swing trading** | Seconds-minutes OK | Batch inference, cloud API |
| **Intraday** | < 1 second | Local real-time, optimised inference |
| **High-frequency** | < 1 millisecond | Custom C++/FPGA, no ML inference in hot path |
| **LLM analysis** | Seconds | API call to [[anthropic|Claude]]/[[openai|GPT-4]], async |

For most retail and mid-frequency traders, a FastAPI server running on a cloud VPS is sufficient. Only institutional HFT requires sub-millisecond latency where ML inference becomes a bottleneck — and at that tier, ML is typically used *offline* to calibrate parameters of a deterministic, hand-optimised hot path (often C++ or FPGA), not invoked per-tick. The further down the latency budget you go, the simpler and more deterministic the in-loop logic must be.

## Common Failures

| Failure | Cause | Prevention |
|---------|-------|-----------|
| **Train/serve skew** | Features computed differently in training vs production | Use feature store; test feature parity |
| **Silent model failure** | Model crashes but system keeps running on stale predictions | Health checks, staleness alerts |
| **Dependency drift** | Python library update changes model behaviour | Pin all versions, containerise |
| **Data format change** | Upstream data schema changes | Data validation (Great Expectations) |
| **Memory/GPU exhaustion** | Model too large for deployed hardware | Profile before deployment, set resource limits |

## Related

- [[tools-frameworks-overview]] — Tools hub
- [[mlops]] — The broader operational lifecycle
- [[model-inference-vs-training]] — Inference economics
- [[cloud-trading-infrastructure]] — Infrastructure for deployed models
- [[experiment-tracking]] — Selecting the model to deploy
- [[artificial-intelligence]] — AI section hub

## Sources

- NVIDIA Triton Inference Server documentation (docs.nvidia.com).
- ONNX and ONNX Runtime project documentation (onnx.ai).
- FastAPI documentation (fastapi.tiangolo.com).
- PyTorch serving guidance noting TorchServe deprecation (pytorch.org), 2025.
- Evidently AI / WhyLabs documentation on production drift monitoring.

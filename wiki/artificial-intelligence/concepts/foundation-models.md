---
title: "Foundation Models"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning]
aliases: ["Foundation Model", "Large Language Model", "LLM"]
domain: [ai-trading]
difficulty: beginner
related: ["[[anthropic]]", "[[openai]]", "[[google-deepmind]]", "[[meta-ai]]", "[[mistral-ai]]", "[[transformer-architecture]]", "[[fine-tuning-llms]]", "[[rlhf-constitutional-ai]]", "[[artificial-intelligence]]"]
---

# Foundation Models

**Foundation models** are large AI models pre-trained on massive datasets that serve as the base for a wide range of applications. In trading, the most relevant foundation models are large language models (LLMs) like [[anthropic|Claude]], [[openai|GPT-4]], [[google-deepmind|Gemini]], [[meta-ai|LLaMA]], and [[mistral-ai|Mistral]] — all built on the [[transformer-architecture|transformer architecture]].

## Key Foundation Model Families

As of mid-2026 the frontier families are:

| Family | Provider | Open/Closed | Context Window | Trading Strength |
|--------|----------|-------------|---------------|-----------------|
| **Claude** (Opus / Sonnet / Haiku) | [[anthropic]] | Closed | up to 1M tokens | Long-document analysis, agentic tool use, code generation |
| **GPT** (GPT-4-class and successors) | [[openai]] | Closed | 128K–1M tokens | Broadest ecosystem, function calling, wide tooling |
| **Gemini** | [[google-deepmind]] | Closed | up to 1M+ tokens | Native multimodal (charts + tables + text) |
| **LLaMA** | [[meta-ai]] | Open-weight | 128K+ tokens | Local deployment, [[fine-tuning-llms|fine-tuning]], privacy |
| **Mistral** | [[mistral-ai]] | Open-weight | 128K+ tokens | Efficient inference, cost-effective |
| **DeepSeek / Qwen** | DeepSeek / Alibaba | Open-weight | 128K+ tokens | Strong open reasoning models, low cost |

> Model versions and exact context limits move every few months — always confirm the current model id, context window, and pricing against the provider's own documentation before building on a specific number. The relative *shape* of the landscape (a few closed frontier labs plus a competitive open-weight tier) has been stable since 2024.

### Two model "modes" relevant to trading

- **Standard chat/completion models** — fast, cheap, good for summarisation, extraction, classification of news and filings
- **Reasoning models** (extended/"thinking" variants across all major families) — spend more compute per query to work through multi-step problems; better for complex analysis (e.g. reconciling a cash-flow statement) but slower and costlier. Match the mode to the task.

## Why Foundation Models Changed Trading

Before foundation models, building AI trading tools required:
- Custom dataset collection and labeling
- Training models from scratch (months of work)
- Specialized ML engineering expertise

Foundation models provide:
- **Zero-shot capability**: Ask a model to analyze a financial document with no training data
- **[[prompt-engineering-trading|Prompt engineering]]**: Customize behavior through natural language instructions
- **Tool use / function calling**: Models can interact with APIs, databases, and trading systems
- **[[fine-tuning-llms|Fine-tuning]]**: Adapt to financial domains with relatively small datasets

This is why [[ai-trading-agents|AI trading agents]] became possible in 2024-2025 — the foundation models reached sufficient quality for financial reasoning.

## Evaluation for Trading

Not all models are equal for trading applications. Key criteria:

| Criterion | Why It Matters |
|-----------|---------------|
| **Reasoning quality** | Can it correctly analyze a complex earnings report? |
| **Factual accuracy** | Does it [[hallucinations-ai|hallucinate]] financial data? |
| **Context window** | Can it process entire 10-K filings (100K+ tokens)? |
| **Latency** | Fast enough for real-time market analysis? |
| **Cost** | Can you afford to run it continuously? |
| **Tool use** | Can it call APIs, execute code, interact with exchanges? |

## See Also

- [[transformer-architecture]] — The architecture underneath
- [[anthropic]], [[openai]], [[google-deepmind]], [[meta-ai]], [[mistral-ai]] — Model providers
- [[fine-tuning-llms]] — Adapting models to finance
- [[rlhf-constitutional-ai]] — How models are aligned
- [[prompt-engineering-trading]] — Getting the best outputs
- [[llm-market-analysis]] — Applied financial analysis with LLMs
- [[artificial-intelligence]] — AI section hub

## Sources

- Bommasani et al., "On the Opportunities and Risks of Foundation Models" (Stanford CRFM, 2021) — coined the term
- Vaswani et al., "Attention Is All You Need" (2017) — the transformer architecture
- Provider model documentation: Anthropic (Claude), OpenAI (GPT), Google DeepMind (Gemini), Meta (Llama), Mistral AI, DeepSeek, Alibaba (Qwen) — for current model ids, context windows, and pricing

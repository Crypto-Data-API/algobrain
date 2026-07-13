---
title: "Generative AI"
type: overview
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Generative AI", "GenAI"]
related: ["[[generative-ai-landscape]]", "[[agentic-ai]]", "[[multimodal-models]]", "[[text-code-generation]]", "[[synthetic-data-generation]]", "[[generative-ai-economics]]", "[[foundation-models]]", "[[prompt-engineering-trading]]", "[[retrieval-augmented-generation]]", "[[image-generation-ai]]", "[[diffusion-models]]", "[[generative-adversarial-networks]]", "[[artificial-intelligence]]"]
---

# Generative AI

**Generative AI** is the category of AI that creates new content — text, code, images, audio, video, and data — rather than classifying or predicting from existing inputs. It is the most transformative AI development since deep learning itself, driven by [[foundation-models|foundation models]] (OpenAI GPT-5 series, Anthropic Claude Opus 4.8/Fable 5, Google Gemini, Meta LLaMA) that can generate human-quality output across modalities.

For trading, generative AI powers research automation, code generation, strategy ideation, [[agentic-ai|autonomous agents]], [[synthetic-data-generation|synthetic data]] for backtesting, and natural-language interfaces to market analysis.

## The Generative AI Stack

```
Applications (what users see)
  ├── [[text-code-generation|Text & Code Generation]] — research, strategy code, reports
  ├── [[image-generation-ai|Image Generation]] — charts, visualisation, synthetic data
  ├── [[speech-and-audio-ai|Audio/Speech]] — voice interfaces, earnings call synthesis
  ├── Video Generation — Sora, Runway (emerging)
  └── [[synthetic-data-generation|Synthetic Data]] — augmented training data, scenarios

Orchestration (how it's coordinated)
  ├── [[agentic-ai|Agentic AI]] — autonomous multi-step reasoning and action
  ├── [[retrieval-augmented-generation|RAG]] — grounding in real data
  ├── [[prompt-engineering-trading|Prompt Engineering]] — steering model behaviour
  └── Tool Use / Function Calling — connecting to APIs and systems

Models (the engines)
  ├── [[foundation-models|Foundation Models]] — GPT-5, Claude (Opus 4.8 / Fable 5), Gemini, LLaMA
  ├── [[multimodal-models|Multimodal Models]] — text + image + audio + video
  └── Specialised — [[finbert|FinBERT]], Code Llama, Whisper

Infrastructure (what runs it)
  ├── [[nvidia-ai|GPU Compute]] — training and inference hardware
  ├── [[model-inference-vs-training|Inference Economics]] — cost per token
  └── [[open-source-ai-movement|Open-Source Models]] — self-hosted alternatives
```

## Topics in This Section

| Page | Focus |
|------|-------|
| [[generative-ai-landscape]] | Market map: who builds what, market size, competitive dynamics |
| [[agentic-ai]] | Autonomous AI agents: reasoning loops, tool use, multi-agent systems |
| [[multimodal-models]] | Models that see, read, hear, and speak simultaneously |
| [[text-code-generation]] | LLMs for writing and coding — the primary trading use case |
| [[synthetic-data-generation]] | Generating training data, market scenarios, stress tests |
| [[generative-ai-economics]] | Unit economics: token costs, ROI, build vs buy |

## Generative vs Discriminative AI

| | Discriminative (Traditional ML) | Generative AI |
|---|---|---|
| **Task** | Classify, predict, score | Create, write, design, synthesise |
| **Output** | Label, number, probability | Text, image, code, audio |
| **Example** | "Is this headline bullish?" → 0.87 | "Write a research note on AAPL earnings" → 500-word analysis |
| **Training** | [[supervised-learning|Supervised]] on labeled data | Self-supervised on massive unlabeled corpora |
| **Trading use** | Signal generation | Research, code, strategy, agent reasoning |

Most trading AI systems combine both: generative AI for research and ideation, discriminative AI for signal generation and execution.

## See Also

- [[generative-ai-landscape]] — Market map and competitive dynamics
- [[agentic-ai]] — Autonomous agents
- [[multimodal-models]] — Multi-sense AI
- [[text-code-generation]] — Writing and coding with AI
- [[synthetic-data-generation]] — Creating training data
- [[generative-ai-economics]] — Costs and ROI
- [[foundation-models]] — The models powering GenAI
- [[artificial-intelligence]] — AI section hub

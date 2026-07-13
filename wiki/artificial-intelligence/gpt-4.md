---
title: "GPT-4"
type: concept
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, company]
aliases: ["GPT 4", "GPT-4", "GPT-4o", "GPT-4 Turbo"]
related: ["[[openai]]", "[[foundation-models]]", "[[llm-market-analysis]]", "[[bert]]", "[[finbert]]", "[[nlp]]", "[[earnings-call-analysis]]", "[[retrieval-augmented-generation]]"]
difficulty: intermediate
domain: [machine-learning]
---

**GPT-4** is a large multimodal language model released by [[openai|OpenAI]] in March 2023, the fourth generation of its Generative Pre-trained Transformer family. It accepts text (and, in later variants, image and audio) input and produces text output, and was the first widely deployed model to reach roughly graduate-level performance on a broad range of professional and academic benchmarks. Successive variants — GPT-4 Turbo (late 2023, longer context, cheaper) and GPT-4o ("omni", 2024, natively multimodal and faster) — extended the line. It is the most common reference point for "frontier LLM" in finance discussions and competes directly with Anthropic's Claude family and Google's Gemini.

## How it works

GPT-4 is a [[transformer-trading|transformer]]-based, decoder-only model trained in two broad phases: large-scale self-supervised pretraining on text (predict the next token) followed by alignment via supervised fine-tuning and reinforcement learning from human feedback (RLHF). OpenAI has not disclosed parameter counts or architecture details; it is widely believed to use a mixture-of-experts design. Key practical properties for users:

- **Context window** — GPT-4 Turbo / GPT-4o offer up to ~128K tokens of context, enough to load long documents (10-Ks, transcripts) in a single prompt.
- **Tool use / function calling** — the model can emit structured calls to external tools and APIs, the basis for agentic workflows.
- **Multimodality** — GPT-4o reads charts, screenshots, and tables as images.

## Trading and finance relevance

GPT-4 and its successors are used across the research and signal-generation stack, almost always as one component of a larger pipeline rather than a standalone trader:

- **Document analysis** — summarizing and extracting structured facts from [[earnings-call-analysis|earnings calls]], SEC filings, and analyst reports, typically wired up with [[retrieval-augmented-generation|RAG]] over a document store.
- **News and sentiment** — classifying headlines and central-bank communications as hawkish/dovish or bullish/bearish; see [[llm-market-analysis]] and [[nlp]]. For high-volume, latency-sensitive sentiment, smaller fine-tuned models like [[finbert]] are often cheaper and faster than calling GPT-4.
- **Idea generation and code** — drafting backtests, feature ideas, and data-cleaning code for quant workflows.
- **Agents** — function calling lets GPT-4 drive [[ai-trading-agents|trading agents]] that query data, reason, and place orders, though autonomy in live trading remains experimental and risky (see [[ai-trading-risks]]).

**Caveats for traders:** LLMs hallucinate, have a training cutoff (so they lack live market data unless fed it), are non-deterministic, and can be slow/expensive per call — all disqualifying for low-latency execution. They are most valuable for *research and unstructured-text processing*, not tick-level decisions. There is also a meta-trade: GPT-4's launch was a major catalyst for the 2023-2025 AI capex cycle and the [[nvidia-ai|NVIDIA]]/AI-infrastructure equity theme.

## Related

- [[openai]] — the developer
- [[foundation-models]] — the broader model category
- [[llm-market-analysis]] — applied use in trading research
- [[finbert]] — lighter finance-specific NLP alternative
- [[bert]] — earlier transformer; encoder-only

## Sources

- OpenAI, "GPT-4 Technical Report," 2023 (arXiv:2303.08774).
- OpenAI product announcements: GPT-4 Turbo (Nov 2023), GPT-4o (May 2024).
- [[book-hands-on-ml-algorithmic-trading]] — LLM/NLP use in trading pipelines.

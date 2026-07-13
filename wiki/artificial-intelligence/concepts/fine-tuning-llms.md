---
title: "Fine-Tuning LLMs for Finance"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning]
aliases: ["Fine-Tuning", "FineTuning", "Domain Adaptation"]
domain: [ai-trading]
difficulty: advanced
related: ["[[foundation-models]]", "[[finbert]]", "[[meta-ai]]", "[[hugging-face]]", "[[model-inference-vs-training]]", "[[nvidia-ai]]", "[[artificial-intelligence]]"]
---

# Fine-Tuning LLMs for Finance

**Fine-tuning** adapts a pre-trained [[foundation-models|foundation model]] to a specific domain by training it further on domain-specific data. For trading, this means taking a general-purpose model and training it on financial text (earnings calls, SEC filings, analyst reports, market commentary) to improve its accuracy and relevance for financial tasks.

## Why Fine-Tune?

| Approach | Pros | Cons | Best For |
|----------|------|------|----------|
| **General LLM** (no fine-tuning) | No setup cost, broadest knowledge | May misunderstand financial jargon | Quick research queries |
| **[[prompt-engineering-trading|Prompt engineering]]** | Easy to iterate, no training needed | Limited by model's base knowledge | Most trading use cases |
| **[[retrieval-augmented-generation|RAG]]** | Grounded in real data, no training | Requires document pipeline | Document-heavy research |
| **Fine-tuning** | Best domain accuracy, fastest inference | Requires data + compute + expertise | High-volume production use |

Fine-tuning is the highest-effort, highest-reward approach. It's worth it when you need to process thousands of financial documents daily at production quality.

## Notable Financial Fine-Tunes

| Model | Base | Training Data | Use Case |
|-------|------|---------------|----------|
| **[[finbert|FinBERT]]** | BERT | Financial news, earnings calls | Sentiment classification |
| **BloombergGPT** | Custom 50B | Bloomberg's proprietary data | Financial NLP (not public) |
| **FinGPT** | LLaMA | Public financial data | Open-source financial LLM |

## Techniques

- **Full fine-tuning**: Update all model weights (expensive, requires many GPUs)
- **LoRA/QLoRA**: Low-rank adaptation — update only a small fraction of weights (practical on consumer hardware)
- **PEFT**: Parameter-efficient fine-tuning methods via [[hugging-face|Hugging Face]] libraries
- **Instruction tuning / RLHF**: Aligning a fine-tuned model to follow finance-specific instructions (see [[rlhf-constitutional-ai]])

## When NOT to Fine-Tune

Fine-tuning is frequently the wrong first move. It bakes knowledge into weights, so it goes stale the moment markets move, and it cannot cite a source. For most trading workflows the better-default ordering is:

1. **Prompt engineering** first — cheapest, fastest to iterate
2. **[[retrieval-augmented-generation|RAG]]** next — when answers must be grounded in current, verifiable documents (filings, news). This is the right tool for factual freshness and is far safer against [[hallucinations-ai|hallucination]].
3. **Fine-tuning** only when you need a consistent *style/format/task behaviour* at high volume (e.g. classifying thousands of headlines into a fixed sentiment schema), or to compress a long prompt into the weights to cut latency and cost.

A common production pattern is RAG *plus* a small LoRA fine-tune for output formatting — combining fresh facts with a reliable house style.

## See Also

- [[foundation-models]] — The base models being fine-tuned
- [[finbert]] — The canonical financial fine-tune
- [[meta-ai]] — LLaMA, the most common base model for fine-tuning
- [[hugging-face]] — Tools and platform for fine-tuning
- [[model-inference-vs-training]] — Compute economics
- [[retrieval-augmented-generation]] — Usually the better default than fine-tuning
- [[artificial-intelligence]] — AI section hub

## Sources

- Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models" (2021); Dettmers et al., "QLoRA" (2023)
- Hugging Face PEFT library documentation
- Wu et al., "BloombergGPT: A Large Language Model for Finance" (2023)
- Yang et al., "FinGPT" project documentation; Araci, "FinBERT" (2019)

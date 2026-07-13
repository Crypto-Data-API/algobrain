---
title: "Zero-Shot & Few-Shot Learning"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning]
aliases: ["Zero-Shot Learning", "Few-Shot Learning", "In-Context Learning"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[foundation-models]]", "[[prompt-engineering-trading]]", "[[fine-tuning-llms]]", "[[llm-market-analysis]]", "[[artificial-intelligence]]"]
---

# Zero-Shot & Few-Shot Learning

**Zero-shot** and **few-shot** learning are paradigms where [[foundation-models|LLMs]] perform tasks they weren't explicitly trained for — either with no examples (zero-shot) or a handful of examples (few-shot) provided in the prompt. These capabilities are why traders can use LLMs for financial analysis without building custom models.

## Zero-Shot

The model performs a task from instructions alone:

> **Prompt**: "Classify this headline as bullish, bearish, or neutral: 'Tesla misses delivery estimates by 8%'"
> **Output**: "Bearish"

No training data, no examples needed. The model generalizes from its pre-training knowledge. This is the foundation of [[llm-market-analysis|LLM market analysis]].

## Few-Shot (In-Context Learning)

Provide a few examples to establish the pattern:

> **Prompt**: "Classify earnings sentiment:
> 'Revenue grew 15% YoY' → Bullish
> 'Guidance lowered for Q3' → Bearish
> 'Margins stable at 22%' → Neutral
>
> Now classify: 'Free cash flow doubled to $4.2B'"
> **Output**: "Bullish"

Few-shot dramatically improves consistency and enables custom classification schemes without [[fine-tuning-llms|fine-tuning]].

## Trading Applications

| Paradigm | Best For | Accuracy | Cost |
|----------|---------|----------|------|
| **Zero-shot** | Quick screening, ad-hoc analysis | Good | Lowest |
| **Few-shot** | Consistent classification at scale | Better | Low |
| **[[fine-tuning-llms|Fine-tuning]]** | Production pipelines, edge cases | Best | Highest |

Most traders start with zero-shot, graduate to few-shot for production, and only fine-tune when processing thousands of documents daily.

## Caveats for Financial Use

- **Knowledge cutoff** — zero-shot answers reflect the model's training cutoff, not live markets. Always ground time-sensitive analysis with [[retrieval-augmented-generation|retrieval]] or current data in the prompt.
- **Example ordering and selection bias** — few-shot performance is sensitive to which examples you pick and their order; a skewed example set biases the classifier toward the majority label.
- **Hallucination risk** — zero-shot extraction of specific figures (revenue, dates) is error-prone; verify any number the model produces against the source document. See [[hallucinations-ai]].
- **Calibration** — LLM confidence is poorly calibrated; treat sentiment labels as features, not ground truth, and backtest before trusting them in a live pipeline.

## See Also

- [[prompt-engineering-trading]] — Practical techniques for both paradigms
- [[foundation-models]] — Models that enable zero/few-shot capabilities
- [[fine-tuning-llms]] — The next step when few-shot isn't enough
- [[llm-market-analysis]] — Applied financial analysis
- [[hallucinations-ai]] — Why to verify model outputs
- [[artificial-intelligence]] — AI section hub

## Sources

- Brown et al., "Language Models are Few-Shot Learners" (GPT-3, NeurIPS 2020), arXiv:2005.14165 — defined in-context few-shot learning
- Wei et al., "Finetuned Language Models Are Zero-Shot Learners" (FLAN, ICLR 2022)
- Lu et al., "Fantastically Ordered Prompts and Where to Find Them" (ACL 2022) — example-ordering sensitivity
- Anthropic and OpenAI prompting documentation — practical zero/few-shot guidance

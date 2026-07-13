---
title: "Meta AI (Llama)"
type: entity
created: 2026-04-09
updated: 2026-06-10
status: good
tags: [company, ai-trading, machine-learning]
aliases: ["Meta AI", "LLaMA", "Llama", "Meta Superintelligence Labs", "MSL", "FAIR"]
entity_type: company
founded: 2013
headquarters: "Menlo Park, USA"
website: "https://ai.meta.com"
related: ["[[openai]]", "[[anthropic]]", "[[foundation-models]]", "[[open-source-ai-movement]]", "[[hugging-face]]", "[[fine-tuning-llms]]", "[[artificial-intelligence]]"]
---

# Meta AI (Llama)

**Meta AI** is the AI division of Meta Platforms (NASDAQ: META), originating in the FAIR lab founded in 2013 under Yann LeCun, and most notable for the **Llama** family of open-weight models. Llama's 2023 release catalyzed the [[open-source-ai-movement|open-source AI movement]], enabling anyone to run powerful language models locally — including for trading applications — without API costs or data-privacy concerns. In mid-2025 Meta reorganized its AI effort into **Meta Superintelligence Labs (MSL)**, marking a strategic pivot that traders track closely as a driver of META's stock and the open-vs-closed AI narrative.

## Key Models

| Model | Parameters | Significance |
|-------|-----------|-------------|
| **LLaMA 1** (Feb 2023) | 7B-65B | First high-quality open model; leaked, then officially released |
| **Llama 2** (Jul 2023) | 7B-70B | Commercially licensed, fine-tuned for chat |
| **Llama 3 / 3.1 / 3.3** (2024) | 8B-405B | 405B was the first open frontier-class model |
| **Llama 4 Scout & Maverick** (Apr 5, 2025) | MoE (17B active; Scout 109B / Maverick 400B total) | First natively multimodal, mixture-of-experts Llama; Scout shipped a 10M-token context window; mixed community reception and LMArena benchmark controversy |
| **Llama 4 Behemoth** (~2T) | Never released | Training difficulties at 2T scale; effectively shelved as of 2026 |
| **Code Llama** | 7B-34B | Code-specialized variant for trading bot development |

## 2025-2026: The Superintelligence Pivot

- **June 2025** — Meta invested **$14.3B for a ~49% stake in Scale AI** and hired its CEO **Alexandr Wang** to lead the newly formed **Meta Superintelligence Labs**, alongside a high-profile talent raid on OpenAI/DeepMind with reported nine-figure pay packages.
- **2025** — Restructurings and layoffs inside MSL (~600 AI roles cut in October 2025); chief scientist **Yann LeCun announced his departure** in late 2025 to found his own startup.
- **2025-2026** — Meta signaled a partial retreat from fully open weights for its frontier work; in April 2026, reports described MSL shipping its first **closed-weight, API-only reasoning model**. Open Llama models remain available on [[hugging-face|Hugging Face]].
- Meta's 2026 AI capex guidance (~$100B+) makes META one of the largest single buyers of [[nvidia-ai|NVIDIA]] GPUs — its earnings calls are a key read on AI infrastructure demand.

## Trading Relevance

Llama models are critical for traders who want to:

- **Run models locally**: No API costs, no data leaving your machine — essential for proprietary strategy research
- **[[fine-tuning-llms|Fine-tune]]** on financial data: Create domain-specific models trained on earnings calls, SEC filings, or market data
- **Deploy at scale**: Lower inference costs than API-based models for high-volume [[nlp-sentiment-analysis|sentiment analysis]]
- **Build private agents**: [[ai-trading-agents|Trading agents]] that don't send strategy details to third-party APIs

The open-weight approach means quantized Llama models run on consumer GPUs, making AI-powered trading research accessible without [[anthropic|Anthropic]] or [[openai|OpenAI]] API subscriptions. Note the license is not OSI-approved open source: companies >700M MAU need a special license, and EU-domiciled use of Llama 4 multimodal models is restricted.

**As a stock driver**: META's AI strategy (capex, MSL talent spend, open-vs-closed pivot) is a primary input to its valuation; the June 2025 Scale AI deal and subsequent capex raises each moved the stock and the broader AI-infrastructure complex.

## Related

- [[foundation-models]] — What Llama is
- [[open-source-ai-movement]] — The movement Llama catalyzed (and partially retreated from)
- [[fine-tuning-llms]] — Adapting Llama for financial tasks
- [[hugging-face]] — Where Llama models are distributed
- [[nvidia-ai]] — Hardware supplier for Meta's training clusters
- [[artificial-intelligence]] — AI section hub

## Sources

- Meta AI blog, "The Llama 4 herd" (Apr 5, 2025): https://ai.meta.com/blog/llama-4-multimodal-intelligence/
- TechTarget, "Meta Llama 4 explained": https://www.techtarget.com/whatis/feature/Meta-Llama-4-explained-Everything-you-need-to-know
- Reuters/CNBC coverage of Meta's $14.3B Scale AI investment and Superintelligence Labs formation (June 2025)
- Skywork, "Llama 4's 2T Behemoth: The Reality for Open-Source AI in 2025": https://skywork.ai/blog/llama-4-behemoth-open-source-2025/
- Verified via web search, 2026-06-10

---
title: "Mistral AI"
type: entity
created: 2026-04-09
updated: 2026-06-10
status: good
tags: [company, ai-trading, machine-learning]
aliases: ["Mistral", "Mistral AI"]
entity_type: company
founded: 2023
headquarters: "Paris, France"
website: "https://mistral.ai"
related: ["[[openai]]", "[[meta-ai]]", "[[google-deepmind]]", "[[nvidia-ai]]", "[[foundation-models]]", "[[open-source-ai-movement]]", "[[hugging-face]]", "[[artificial-intelligence]]"]
---

# Mistral AI

**Mistral AI** is a French AI company producing high-performance open-weight and commercial language models. Founded in 2023 by Arthur Mensch (ex-[[google-deepmind|DeepMind]]) with Guillaume Lample and Timothée Lacroix (ex-Meta), it is Europe's flagship AI lab and a key player in the [[open-source-ai-movement|open-source AI movement]]. Its September 2025 Series C — led by chip-equipment monopolist **ASML** at an **€11.7B (~$14B) valuation** — made it one of the most closely watched private AI names for pre-IPO and AI-sector positioning.

## Key Models

| Model | Parameters | Significance |
|-------|-----------|-------------|
| **Mistral 7B** (2023) | 7B | Outperformed Llama 2 13B at half the size |
| **Mixtral 8x7B / 8x22B** (2023-24) | ~47B / ~141B (MoE) | Mixture-of-Experts architecture, efficient inference |
| **Mistral Large 2** (2024) | 123B | Frontier-class commercial model |
| **Mistral Medium 3** (May 2025) | Undisclosed | Frontier-adjacent performance at ~8x lower cost claim |
| **Magistral** (June 2025) | Small 24B (open) + Medium | Mistral's first reasoning model family — "great at mathematics and coding" (Mensch, London Tech Week 2025) |
| **Codestral / Devstral** | Code-focused | Programming and agentic coding models |

## Funding and Business (2025-2026)

- **Sept 2025** — **€1.7B Series C** at €11.7B post-money, led by **ASML** (taking an ~11% fully diluted stake); participation from DST Global, a16z, NVIDIA, General Catalyst, Index, Lightspeed, Bpifrance. The ASML tie-up includes joint AI R&D for semiconductor lithography.
- **Revenue ramp**: from roughly **$20M ARR at the start of 2025 to $400M+ by February 2026** (~20x in 14 months); publicly targeting **$1B ARR in 2026** (CNBC).
- **March 2026** — raised **$830M in debt to buy 13,800 NVIDIA chips** for a new data center near Paris ("Mistral Compute" sovereign-cloud push, in partnership with NVIDIA).
- **Le Chat** consumer assistant grew strongly in Europe on a data-sovereignty pitch.

## Trading Relevance

- **Efficient inference**: MoE architectures provide near-frontier quality at lower [[model-inference-vs-training|compute costs]] — important for continuous [[ai-trading-agents|agent operation]]
- **Open weights**: Apache-2.0 models (7B, Mixtral, Magistral Small) can be run locally for private trading research and [[fine-tuning-llms|fine-tuned]] on proprietary data
- **European regulatory advantage**: EU-based and GDPR/EU-AI-Act native — relevant for European trading firms that cannot ship data to US APIs; also unaffected by Meta's EU restrictions on Llama 4
- **API access**: La Plateforme offers API pricing competitive with [[openai|OpenAI]] and [[anthropic|Anthropic]]
- **AI-sector signal**: the ASML-Mistral deal is the canonical example of European "sovereign AI" capital flows; Mistral's mooted IPO is a future event for AI-equity desks, and its NVIDIA chip orders are a datapoint on GPU demand

## Related

- [[foundation-models]] — What Mistral builds
- [[open-source-ai-movement]] — The ecosystem Mistral contributes to
- [[meta-ai]] — Llama, the other major open-weight model family
- [[google-deepmind]] — Where co-founder Arthur Mensch trained
- [[nvidia-ai]] — Investor and chip supplier (13,800 GPUs, 2026)
- [[hugging-face]] — Where Mistral open models are distributed
- [[artificial-intelligence]] — AI section hub

## Sources

- Mistral AI, "Mistral AI raises 1.7B€ to accelerate technological progress with AI" (Sept 2025): https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai/
- CNBC, "AI firm Mistral valued at $14 billion as chip giant ASML takes major stake" (Sept 9, 2025): https://www.cnbc.com/2025/09/09/ai-firm-mistral-valued-at-14-billion-as-asml-takes-major-stake.html
- DataCenterDynamics, "Mistral AI raises €1.7bn in funding round led by ASML": https://www.datacenterdynamics.com/en/news/mistral-ai-raises-17bn-in-funding-round-led-by-asml/
- Klover.ai analysis of Mistral revenue trajectory (2026): https://www.klover.ai/is_ai_profitable_mistrals_path_toward_profit_analysis_2026/
- Verified via web search, 2026-06-10

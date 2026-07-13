---
title: "Perplexity Deep Research — Claude Fable 5 for Finance & Trading (June 2026)"
type: source
created: 2026-06-10
updated: 2026-06-12
status: good
tags: [meta, source, ai-trading, machine-learning]
aliases: ["Claude Fable 5 Research", "Fable 5 Finance Perplexity", "Fable 5 Deep Research"]
source_type: data
source_url: "n/a — Perplexity sonar-deep-research aggregating 59 named sources"
source_author: "Perplexity (sonar-deep-research model)"
source_date: 2026-06-10
source_file: "raw/articles/2026-06-10-claude-fable-5-finance.md"
confidence: high
claims_count: 30
related:
  - "[[claude]]"
  - "[[anthropic]]"
  - "[[2026-04-07-claude-mythos-project-glasswing]]"
  - "[[2026-06-01-perplexity-mythos-public-rollout]]"
  - "[[mythos-release-window-exploit-short]]"
  - "[[2026-anthropic-finance-agents-launch]]"
  - "[[2026-claude-opus-4-7-finance-benchmark]]"
---

#meta

Perplexity `sonar-deep-research` run dated 2026-06-10 (~20-30 web searches, 59 cited sources) on **Claude Fable 5** with a finance/trading focus. Commissioned during a [[gap-analysis|gap analysis]] for "claude fable" after the wiki's model pages were found to be a generation behind (topping out at Opus 4.7, no Fable 5 or Opus 4.8). Full output: `raw/articles/2026-06-10-claude-fable-5-finance.md`.

## The headline finding: Fable 5 IS the Mythos public rollout

**Claude Fable 5 (released 9 June 2026) is the safety-wrapped public release of the Mythos-class model the wiki has been tracking** via [[2026-04-07-claude-mythos-project-glasswing]] and [[2026-06-01-perplexity-mythos-public-rollout]]. Fable 5 and the concurrently-released, access-restricted **Claude Mythos 5** share the same underlying base model; Mythos 5 (Project Glasswing partners only) runs without the safety classifiers, while Fable 5 wraps the same system in a safety shell "safe for general use." This directly resolves the catalyst-window thesis behind [[mythos-release-window-exploit-short]] and mythos-capability-overhang-vol: the rollout those strategies were positioned around materialized on 9 June 2026. [HIGH] (Sources 1, 2, 3, 7, 9, 10)

## Key extracted claims with confidence flags

### Specifications & commercial terms
- **Released 9 June 2026**, API model ID `claude-fable-5`; available on the Claude API, Claude Platform on AWS, Amazon Bedrock, Google Vertex AI, Microsoft Foundry, and GitHub Copilot. [HIGH] (4, 6, 7, 41)
- **New top tier ("Fable") above Opus** — first time Anthropic has shipped a tier above Opus; described as its "most capable widely released model." [HIGH] (7, 10)
- **1M-token context, 128K max output, text+image input.** [HIGH] (4, 7)
- **Pricing $10 / $50 per million input/output tokens — exactly 2× Opus 4.8** ($5 / $25). US-only inference at a 1.1× multiplier; 90% cached-input discount applies (same as Opus). [HIGH] (7, 40, 50, 51)
- **Adaptive thinking only** — fixed `budget_tokens` budgets and `temperature`/`top_p`/`top_k` not supported; an explicit `thinking:{type:"disabled"}` errors. Depth is controlled only via the `effort` parameter. [HIGH] (7, 39, 42)
- **Safety fallback to Opus 4.8** on cybersecurity / biology / chemistry / model-distillation queries; fallback occurs in **<5% of sessions** (~2% on GDPval-AA). API users must configure a "Fallback API" or flagged requests are blocked; **fallback requests are not billed at Fable rates.** [HIGH] (2, 3, 7, 9, 45, 51)
- **Mandatory 30-day data retention ("covered model")** for safety monitoring on every platform; data is *not* used for training but is reviewed for abuse. Forces a trade-off for zero-data-retention finance customers. [HIGH] (7, 44)
- Free on Claude.ai Pro/Max/Team/Enterprise **only 9–22 June 2026**, then usage credits required. [MEDIUM-HIGH] (1, 24, 53)

### Benchmarks (finance / agentic / coding)
- **Vals AI CorpFin v2 (corporate finance): 71.83% — #1 of 111 models**, ahead of Opus 4.8, GPT-5.5, Gemini 3.x. [HIGH] (14, 48)
- **Vals Index 75.14% (#1/25); Vals Multimodal Index 74.15% (#1/20).** [HIGH] (14, 48)
- **Finance Agent v2 (agentic finance): 56.31% — 2nd, behind Gemini 3.5 Flash at 57.86%**; Opus 4.8 = 53.92%. No model clears 58%; hardest categories (Financial Modeling, Precedents) top out ~23%. *This is the one finance benchmark where Fable 5 does **not** lead.* [HIGH] (18, 48)
- **GDPval-AA: 1932 ELO — #1** (Opus 4.8 = 1890, GPT-5.5 = 1769, Gemini 3.1 Pro = 1314). [HIGH] (11, 25)
- **Hebbia Finance Benchmark: highest of any model tested** (qualitative; no published % yet). [MEDIUM-HIGH] (9, 45)
- **MMLU Pro 91.50% (#1/110); MMMU 89.31% (#1).** [HIGH] (14, 48)
- **SWE-Bench Pro 80.3%** (Opus 4.8 = 69.2%, GPT-5.5 = 58.6%, Gemini 3.1 Pro = 54.2%); SWE-bench Verified 95.0%; Terminal-Bench 2.1 80.5%; LiveCodeBench 89.8%; FrontierCode Diamond 29.3% (Opus 4.8 = 13.4%, GPT-5.5 = 5.7%). [HIGH] (9, 13, 14, 25, 48)
- **Document-vision GDP.pdf 29.8%** (Opus 4.8 = 22.5%, GPT-5.5 = 24.9%) — relevant to 10-K / filing extraction. [HIGH] (9, 25, 47)
- **No verified `tau-bench` data and no GPT-6 exists** — comparisons are vs GPT-5.5; any GPT-6 / tau-bench claim is speculative. [HIGH] (9, 25, 26)

### Adoption (finance / trading)
- **IMC (proprietary trading firm): Fable 5 "aced" trading-analysis evals** — factual lookup, conceptual reasoning, root-cause analysis, expected-value analysis. **The only explicitly named trading firm to validate Fable 5.** [HIGH] (9, 10, 46)
- **Stripe**: Fable 5 completed a 50M-line Ruby codebase migration (est. ~2 months of human work) in ~1 day. [HIGH] (9, 52)
- **Anthropic's pre-built finance agents** (Market Researcher, Credit Analyst, Portfolio Manager, Risk Manager) remain **documented on Opus 4.7**, not officially migrated to Fable 5 — Fable is a drop-in upgrade, not the marketed default. *(Corrects any assumption that the finance agents now run on Fable.)* [HIGH] (15, 56)
- Pre-Fable institutional Claude users: Bridgewater, BCI (Canada), Norges Bank Investment Management, Commonwealth Bank of Australia, AIG, FundamentalLabs. [HIGH] (15, 16, 30)
- **Morgan Stanley participating in Mythos testing**; Project Glasswing expanded to ~200 partners across 15 countries. [MEDIUM-HIGH] (28, 58)

### Corporate / market significance
- **Series H: $65B raised at ~$965B post-money** (late May 2026), framed as likely the last private round before IPO; confidential IPO filing reported; ~$47B revenue run-rate cited. [HIGH] (21, 35, 37)
- New premium tier = pricing power at the top of the market + intensified competitive pressure on OpenAI/Google in high-end enterprise. [MEDIUM] (25, 34, 35)
- **AI-adjacent equities**: frontier rollout sustains GPU demand (NVDA — the SpaceX deal alone cites 220,000+ NVIDIA GPUs); broad cloud hosting benefits AMZN/MSFT/GOOGL; Fable 5 benchmark leadership pressures GPT-5.x and Gemini 3.x. Sources give **no explicit equity forecasts** — directional/causal observations only. [MEDIUM] (25, 34, 54)

## Reliability notes

- Confidence is **high** overall: specs, pricing, and benchmark numbers trace to Anthropic's own docs (sources 4, 7, 41, 44), Vals AI leaderboards (14, 18, 48), and major outlets (TechCrunch, BusinessInsider, ITPro). Trading-relevance framing is analysis, not sourced fact.
- **Single-source / qualitative items** flagged MEDIUM: Hebbia exact scores (unpublished), Morgan Stanley Mythos participation, equity implications.
- **Explicit non-findings** (valuable): no `tau-bench` results for Fable 5; no GPT-6; finance agents *not* officially on Fable 5; no named Fable 5 *bank/hedge-fund* customers beyond IMC's trading-analysis validation.

## Pages updated from this research

- [[claude]] — Fable 5 section rewritten with verified benchmarks, the Mythos connection, IMC/Stripe, pricing/retention/fallback architecture.
- [[anthropic]] — Mythos-class tier, Series H ($65B / $965B), Fable-as-Mythos-public-release.

---
title: "Claude"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [llm, ai-trading, machine-learning, anthropic, nlp]
aliases: ["Claude AI", "Claude Opus", "Claude Sonnet", "Claude Haiku", "Claude Fable", "Anthropic Claude"]
related: ["[[anthropic]]", "[[llm-market-analysis]]", "[[ai-trading]]", "[[ai-trading-overview]]", "[[gpt]]", "[[gemini]]", "[[openai]]", "[[nlp-sentiment-analysis]]", "[[ai-trading-agents]]", "[[finbert]]"]
entity_type: ai-model
website: "https://claude.ai"
---

# Claude

**Claude** is a family of large language models built by [[anthropic|Anthropic]] and named after Claude Shannon, the founder of information theory. As of mid-2026 the line spans four tiers — Haiku, Sonnet, Opus, and the new top-end **Fable** — with **Claude Fable 5** the most capable model and **Claude Opus 4.8** the flagship Opus, both optimized for coding, long-horizon agentic work, multi-step reasoning, and long-context document analysis. Claude is widely used in trading research workflows for filing analysis, multi-document synthesis, sentiment classification, and as the reasoning core inside [[ai-trading-agents|agent-based research systems]].

## Overview

Claude is Anthropic's primary product line. The models are accessible through the Anthropic API directly and via the major cloud platforms — AWS Bedrock and Google Cloud Vertex AI — making Claude available within the same VPCs where regulated firms already host their data. The models emphasize:

- **Long context** — context windows of 200K tokens (Claude 3 family) up to 1M tokens (Claude Opus 4.x), enabling whole-10-K, whole-prospectus, or whole-codebase ingestion in a single call.
- **Constitutional AI training methodology** — Anthropic's alignment approach in which the model critiques and revises its own outputs against a written set of principles, in addition to standard RLHF.
- **Coding and structured reasoning** — repeatedly benchmark-leading on SWE-bench Verified and on multi-step financial reasoning tasks.

The models are deployed through the Claude API, the consumer-facing claude.ai chat interface, and Claude Code (Anthropic's agentic CLI used by developers, researchers, and increasingly by trading shops to build their own pipelines).

## Model Family

Claude is sold in four tiers, each refreshed roughly every 6-12 months:

### Haiku — fast and inexpensive

The smallest tier. Optimized for high-volume, low-latency tasks: classification, routing, retrieval-augmented generation over short contexts, real-time chat. Pricing is the cheapest per token, making it the right choice for screening millions of headlines or tweets.

### Sonnet — balanced

The mid tier and historically the workhorse model. Sonnet versions (3.5, 3.7, 4, 4.5, 4.6) have repeatedly led benchmarks at general-purpose reasoning at a fraction of Opus pricing. Most production trading-research workloads run on Sonnet because the cost-quality tradeoff is favorable.

### Opus — flagship reasoning

The high-end production tier. Opus is the right choice for the hardest reasoning tasks: multi-document synthesis across thousands of pages, complex agentic workflows with many tool calls, financial modeling that requires careful arithmetic, and code generation across large codebases. Opus models carry a 1M-token context window (from Opus 4.6 onward) at standard API pricing with no long-context premium. **Claude Opus 4.8** is the current flagship — highly autonomous, state-of-the-art on long-horizon agentic execution, knowledge work, and file-based memory, priced at roughly $5 / $25 per million input / output tokens.

### Fable — most capable

The newest and top-most tier, introduced in 2026 above Opus. **Claude Fable 5** (`claude-fable-5`) is Anthropic's most powerful, most intelligent model: a 1M-token context window, up to 128K output tokens, and adaptive-thinking-only reasoning. It is priced at roughly **$10 / $50 per million input / output tokens — about 2× Opus** — positioning it as the model reserved for the hardest research and agentic tasks where being right matters more than per-call cost. See [[#Claude Fable 5 (2026)]] below.

### Generation timeline (public models)

| Year | Notable releases |
|------|------------------|
| 2023 | Claude 1, Claude 2 (100K context) |
| 2024 | Claude 3 family (Haiku, Sonnet, Opus); 200K context; vision; Claude 3.5 Sonnet; Computer Use beta |
| 2025 | Claude 3.7 Sonnet (Extended Thinking); Claude Sonnet 4 / Opus 4; Sonnet 4.5; Opus 4.5 |
| 2026 | Claude Opus 4.6 / Sonnet 4.6 (1M context); Claude Haiku 4.5; Claude Mythos Preview (restricted); Claude Opus 4.7; **Claude Opus 4.8**; **Claude Fable 5 + Claude Mythos 5** (9 Jun 2026 — new top tier; Fable = public, Mythos 5 = Glasswing-restricted) |

## Key Capabilities Relevant to Trading

- **Long-context document ingestion.** A 1M-token window covers an annual 10-K, 10-Qs, latest two earnings call transcripts, and the proxy statement in a single prompt. This eliminates much of the chunk-and-rerank pipeline complexity.
- **Tool use / function calling.** The API natively supports structured tool calls, which lets a trading agent fetch market data, run code, query databases, and read files inside a single conversation loop.
- **Vision.** Claude 3 and later can read charts, screenshots of terminals, and PDFs with embedded images — useful for analyzing investor-day decks, sell-side report charts, and CRSP-style PDFs.
- **Extended Thinking (Claude 3.7+).** A reasoning mode where the model generates a private chain of thought before producing a final answer, improving multi-step financial calculation accuracy.
- **Code generation.** Claude is widely regarded as the strongest coding model as of 2025-2026 (consistently leading SWE-bench Verified), which matters for traders building [[backtesting|backtests]], data pipelines, and research notebooks.
- **Structured output.** JSON mode and function calling ensure outputs slot into existing data models — important for production [[ml-trading-pipeline|ML pipelines]] that demand schema-stable signals.

## How Traders Use It

Real-world use cases observed in 2025-2026:

- **Earnings call analysis.** Feed the full transcript and the prior-quarter transcript; ask for a structured diff of guidance, tone changes, and management hedging. See earnings-call-analysis.
- **SEC filing differencing.** Compare risk-factor sections across consecutive 10-Ks to surface new material risks. The 200K-1M context window enables side-by-side comparison without splitting the document.
- **News and headline classification.** Zero-shot classification at scale into bullish / bearish / neutral or into more nuanced taxonomies. Often paired with [[finbert]] as an ensemble.
- **Multi-document research synthesis.** Aggregate broker reports, conference call transcripts, and trade-press articles to produce a research memo on a single thesis.
- **Agent-based research workflows.** Claude as the reasoning core of an [[ai-trading-agents|agent]] that iterates: pull data → generate hypothesis → write backtest → review results → refine.
- **Filing-event signal generation.** Detect when a company's filings contain language that has historically preceded earnings beats / misses (e.g., changes in revenue-recognition footnotes, segment-disclosure shifts).
- **Code generation for quant infrastructure.** Many smaller systematic shops now use Claude Code to build and maintain their data ingestion, factor calculation, and risk reporting code.

## Claude Opus 4.7 (2026)

Anthropic released **Claude Opus 4.7** in 2026 as the new flagship Opus-tier model. Unlike previous Opus generations evaluated primarily on general-purpose benchmarks (SWE-bench Verified, MMLU, GPQA), Opus 4.7 was positioned explicitly around finance-specialized evaluation (Source: [[2026-04-22-gap-finder-ai-2026-major-news-stories]]).

### Benchmark performance

- **Vals AI Finance Agent benchmark — 64.4%.** Opus 4.7 leads the Vals AI Finance Agent leaderboard, the first model to clear the 60% threshold on this benchmark. The benchmark specifically measures the ability of an LLM to act as a financial agent across multi-step research, analysis, and decision-support tasks.
- **GDPval-AA — leader.** Opus 4.7 also tops the GDPval-AA evaluation, which measures performance on economically valuable knowledge work — the kind of cognitive labor that actually gets compensated in GDP terms. For finance applications this is closer to the relevant measure than abstract reasoning benchmarks.

### Anthropic's pre-built finance agents

Opus 4.7 is the **foundation model** for Anthropic's suite of pre-built finance agents launched in 2026:

- **Market Researcher**
- **Credit Analyst**
- **Portfolio Manager**
- **Risk Manager**

These agents ship with pre-wired connections to institutional data sources (FactSet, S&P Capital IQ, MSCI, PitchBook, Morningstar) and to firm-internal systems. See [[anthropic#2026 Financial Services Push]] and [[2026-anthropic-finance-agents-launch]] for the institutional-deployment context.

### Significance for LLM benchmarking

The Opus 4.7 release marks an industry-level shift from general-purpose LLM benchmarking to **finance-specialized benchmarking**. Until 2025, leaderboards traders watched were MMLU, GPQA, SWE-bench, and the LMSYS Arena — all general-purpose. With Vals AI Finance Agent and GDPval-AA emerging as the new battleground, traders evaluating which LLM to deploy in research workflows should be tracking these benchmarks rather than coding or math benchmarks alone.

This shift parallels the rise of domain-adapted models like [[llama-fin]] (an 8B model that outperforms GPT-4o on finance-specific tasks via domain-adaptive post-training) — together they signal that the LLM market for finance is bifurcating away from one-size-fits-all general models.

## Claude Opus 4.8 (2026)

Anthropic followed Opus 4.7 with **Claude Opus 4.8** (`claude-opus-4-8`), which became the current flagship Opus-tier model. It keeps the same API surface as Opus 4.7 — adaptive-thinking-only reasoning, with the fixed `budget_tokens` "thinking budget" and the `temperature` / `top_p` / `top_k` sampling parameters removed — and is positioned as Anthropic's most capable *generally available* model: highly autonomous, state-of-the-art on long-horizon agentic execution, knowledge work, and file-system-based memory, with clearer, warmer writing. It retains the 1M-token context window at standard pricing (~$5 / $25 per million input / output tokens) and up to 128K output tokens.

For trading research, the practical upshot of 4.8 over 4.7 is **longer, more reliable autonomous runs** — overnight document-review or backtest-construction tasks that complete a multi-step plan without human correction — plus stronger one-shot bug-finding in quant code. A new beta capability, **mid-session system prompts**, lets an agent harness inject trusted context partway through a session (e.g. "this book's positions changed", "remaining token budget is low") without invalidating the prompt cache — useful for long-running [[ai-trading-agents|research agents]] that accumulate state.

## Claude Fable 5 (2026)

**Claude Fable 5** (`claude-fable-5`) was released on **9 June 2026** as Anthropic's most powerful model and the first entry in a **new tier above Opus** — the first time Anthropic has shipped a tier above Opus rather than another Opus point release (Source: [[2026-06-10-perplexity-claude-fable-5-finance]]).

### Fable 5 *is* the public Mythos release

The single most important fact for traders is that **Fable 5 is the safety-wrapped, publicly accessible release of the Mythos-class model the wiki has been tracking** (see [[2026-04-07-claude-mythos-project-glasswing]] and [[2026-06-01-perplexity-mythos-public-rollout]]). Fable 5 and the concurrently-released, access-restricted **Claude Mythos 5** share the same underlying base model: Mythos 5 (Project Glasswing partners only) runs *without* the safety classifiers; Fable 5 wraps the identical system in a safety shell "safe for general use." On standard capability benchmarks the two score within 1-3 points of each other, so when Fable's classifiers don't trigger its output is effectively indistinguishable from Anthropic's internal frontier.

This resolves the catalyst-window thesis behind [[mythos-release-window-exploit-short]] and mythos-capability-overhang-vol — the "Mythos public rollout" those nodes were positioned around **materialized on 9 June 2026** as Fable 5.

### Specifications and commercial terms

- **New top tier**, above Haiku / Sonnet / Opus — Anthropic's "most capable widely released model."
- **1M-token context, up to 128K output tokens, text + image input.**
- **Pricing $10 / $50 per million input / output tokens — exactly 2× Opus 4.8** ($5 / $25). A US-only inference option carries a 1.1× multiplier; the standard 90% cached-input discount applies. The clean 2× multiplier makes the routing economics simple: any workload costs precisely double on Fable vs Opus 4.8.
- **Adaptive thinking only.** Fixed `budget_tokens` thinking budgets and the `temperature` / `top_p` / `top_k` sampling parameters are unsupported; depth is controlled only via the `effort` parameter (including `max`).
- **Safety fallback to Opus 4.8.** Queries touching cybersecurity, biology, chemistry, or model distillation are silently routed to Opus 4.8 (or blocked, on the API, unless a "Fallback API" is configured). Fallback fires in **<5% of sessions** (~2% on the GDPval-AA benchmark); fallback requests are **not** billed at Fable rates. For trading desks this means Fable deliberately underperforms on, e.g., probing exchange infrastructure for vulnerabilities or reverse-engineering rival models for alpha.
- **Mandatory 30-day data retention** ("covered model") for safety monitoring on every platform — *not* used for training, but a hard trade-off for zero-data-retention (ZDR) finance customers, who must enable retention at the workspace level to use Fable 5 at all.
- Distributed via the Claude API, Claude Platform on AWS, Amazon Bedrock, Google Vertex AI, Microsoft Foundry, and GitHub Copilot.

### Benchmark performance (finance, agentic, coding)

Fable 5 resets the top of most leaderboards — a genuine tier jump, widening as tasks get longer (Source: [[2026-06-10-perplexity-claude-fable-5-finance]]):

| Benchmark | Fable 5 | Opus 4.8 | GPT-5.5 | Gemini 3.x |
|-----------|---------|----------|---------|------------|
| **Vals AI CorpFin v2** (corporate finance) | **71.83% — #1 of 111** | below | below | below |
| **Finance Agent v2** (agentic finance) | 56.31% — **2nd** | 53.92% | — | **57.86% (Gemini 3.5 Flash, #1)** |
| **GDPval-AA** (knowledge work, ELO) | **1932 — #1** | 1890 | 1769 | 1314 (3.1 Pro) |
| **MMLU Pro** | **91.50% — #1/110** | below | below | below |
| **SWE-Bench Pro** (agentic coding) | **80.3%** | 69.2% | 58.6% | 54.2% (3.1 Pro) |
| **FrontierCode Diamond** (hard coding) | **29.3%** | 13.4% | 5.7% | below |
| **GDP.pdf** (document vision) | **29.8%** | 22.5% | 24.9% | — |

Other firsts include the **Vals Index (75.14%)**, **Vals Multimodal Index (74.15%)**, SWE-bench Verified (95.0%), Terminal-Bench 2.1 (80.5%), and LiveCodeBench (89.8%). On **Hebbia's Finance Benchmark** (senior-level document reasoning) Fable 5 posts the highest score of any model tested (exact % unpublished).

Two caveats matter: **Finance Agent v2 is the one finance benchmark where Fable 5 does not lead** — Gemini 3.5 Flash edges it 57.86% vs 56.31% — and **no model clears 58%** there, with the hardest categories (financial modeling, precedents) topping out near 23%. The takeaway: Fable 5 is an excellent research and drafting assistant but is **not reliable enough for unsupervised trade execution or portfolio rebalancing**. (There is **no verified `tau-bench` data** for Fable 5, and **no GPT-6** exists — comparisons run against GPT-5.5.)

### Trading & finance adoption

- **IMC** (the proprietary trading firm) ran Fable 5 through a battery of trading-analysis evaluations — factual lookup, conceptual reasoning, root-cause analysis, expected-value analysis — and reports the model "aced" them nearly across the board. **IMC is the only explicitly named trading firm to validate Fable 5 to date.**
- **Stripe** used Fable 5 to complete a migration of a **50-million-line Ruby codebase** — estimated at ~2 months of human work — in roughly **one day**, illustrating the model's value for the large, complex codebases banks and quant shops maintain.
- Anthropic's **pre-built finance agents** (Market Researcher, Credit Analyst, Portfolio Manager, Risk Manager) remain **documented on Opus 4.7**, *not* officially migrated to Fable 5 — Fable is a drop-in upgrade, not the marketed default engine. Existing Claude finance customers (Bridgewater, BCI, Norges Bank IM, Commonwealth Bank of Australia, AIG) are associated with Claude generally, not Fable specifically.
- **Morgan Stanley** is participating in Anthropic's restricted **Mythos** testing (the cyber-defense, Glasswing-gated sibling), now expanded to ~200 partners across 15 countries.

### Why it matters for traders

- **Capability ceiling for the hardest agentic finance work.** Fable 5 is the natural reasoning core for deep multi-document due diligence, complex DCF / credit modelling, and long-horizon research loops where an error is expensive — and where a 2× price premium is immaterial next to the cost of being wrong on a position.
- **A third tier in the routing stack.** Production stacks already route bulk work (headline screening, classification) to Haiku / Sonnet and reserve Opus for hard cases. Analysts recommend sending ~80% of traffic to Opus 4.8 (or cheaper) and reserving Fable 5 for the hardest ~10-20% where its uplift changes outcomes.
- **The Mythos overhang made tradeable.** Because Fable 5 is the public Mythos rollout, its release is the realization of the AI-vulnerability-discovery catalyst the wiki's [[mythos-release-window-exploit-short|exploit-window]] and capability-overhang vol strategies anticipate — with Mythos 5 (the un-nerfed Glasswing version, "strongest cybersecurity capabilities of any model in the world") sitting one access-tier above it.
- **AI-adjacent equities.** Each frontier release sustains GPU demand (Anthropic's SpaceX deal alone cites 220,000+ NVIDIA GPUs), benefits the cloud hosts (Amazon, Microsoft, Google), and pressures [[gpt|GPT]]-5.x and [[gemini|Gemini]] 3.x in high-end enterprise. Anthropic's **Series H ($65B at ~$965B post-money, late May 2026)** and reported confidential IPO filing make the model layer itself an emerging asset class — see [[anthropic]].

## Pricing and Access

Claude is sold through three primary channels:

- **Anthropic API direct** — pay-as-you-go pricing per million input/output tokens, tiered by model size. Haiku is the cheapest; Opus sits well above it; and **Fable 5 is the most expensive at ~$10 / $50 per million input / output tokens (roughly 2× Opus 4.8)**. The wide spread across four tiers is what makes tiered routing (cheap models for volume, premium models for hard cases) the dominant cost-control pattern.
- **AWS Bedrock** — Claude available within AWS regions including ones approved for regulated workloads. Same pricing tiers, integrated billing.
- **Google Cloud Vertex AI** — Claude integrated into Google's enterprise ML platform.

Anthropic also offers a **Pro** ($20/month) and **Max** ($100-$200/month) tier of consumer subscriptions for the claude.ai web interface, used by individual analysts and smaller shops that don't need API integration.

For trading firms, the choice typically rests on data-residency and security requirements: AWS Bedrock and Vertex are preferred when the firm's data is already inside those clouds; the direct Anthropic API is preferred for the latest model availability (new Claude models often appear on the direct API before the cloud partners).

## Limitations

- **Compute cost.** Opus inference is expensive at scale. Running Opus across millions of headlines daily becomes a six-figure annual line item; many production deployments use Sonnet or Haiku for the bulk and reserve Opus for hard cases.
- **No real-time market data.** Claude has a training cutoff; it does not natively know prices or news after that cutoff. Production systems must inject current data via tool use or retrieval.
- **Latency.** API round-trips of 200ms to several seconds disqualify Claude from [[low-latency-trading|low-latency]] or [[hft|HFT]] applications. It is a research and signal-generation tool, not an execution engine.
- **Hallucination risk.** Like all LLMs, Claude can fabricate financial numbers with high confidence. Production pipelines need ground-truth validation against a structured source for any number the model produces.
- **Reproducibility.** Outputs vary slightly across runs and across model updates; backtest reproducibility requires pinning a specific model version and a fixed temperature.
- **Rate limits.** Tier-based per-minute and per-day token limits can throttle large-scale batch workloads — usually addressable by negotiating an enterprise contract.

## Comparison to Competitors

| Dimension | Claude (Anthropic) | GPT (OpenAI) | Gemini (Google) |
|-----------|--------------------|--------------|-----------------|
| **Long context** | Up to 1M tokens | Up to 1M tokens (limited models) | Up to 1M-2M tokens |
| **Coding benchmarks** | Consistently leading | Strong | Strong |
| **Reasoning** | Strong, especially over long context | Strong, especially math | Strong, especially multimodal |
| **Trading adoption** | Rapidly growing, dominant in code | Largest installed base | Growing |
| **Safety positioning** | Constitutional AI, interpretability | RLHF, red-teaming | RLHF |
| **Cloud distribution** | AWS Bedrock, Vertex, direct API | Azure, direct API | Vertex, direct |
| **Vision** | Yes | Yes (GPT-4o) | Yes (native multimodal) |

Trading research workflows often use multiple models in ensemble: Claude for long-context document analysis and code, GPT for math-heavy reasoning, Gemini for cross-asset multimodal tasks. The cost of running all three on the same query is small relative to the cost of being wrong on a single trade.

## Related

- [[anthropic]] — the company that builds Claude
- [[llm-market-analysis]] — the broader concept of using LLMs for market analysis
- [[ai-trading]] — section overview
- [[gpt]] — primary commercial competitor
- [[gemini]] — Google's LLM family
- [[openai]] — primary competitive lab
- [[nlp-sentiment-analysis]] — broader context
- [[ai-trading-agents]] — agent architectures using Claude as reasoning core
- [[finbert]] — financial-domain specialist often used alongside Claude for ensemble sentiment scoring
- [[backtesting]] — Claude Code is widely used to build backtests
- [[low-latency-trading]] — the use case Claude is **not** suitable for
- [[2026-claude-opus-4-7-finance-benchmark]] — Opus 4.7 finance benchmark results
- [[2026-anthropic-finance-agents-launch]] — pre-built finance agents built on Opus 4.7
- [[llama-fin]] — domain-adapted 8B finance LLM, complementary trend
- [[ml-trading-pipeline]] — where tiered Claude routing slots into a production signal pipeline
- [[2026-04-07-claude-mythos-project-glasswing]] — the Mythos program; Fable 5 is its public release
- [[mythos-release-window-exploit-short]] — strategy positioned around the Mythos/Fable rollout window
- [[2026-06-10-perplexity-claude-fable-5-finance]] — sourced deep research underlying the Fable 5 section

## Sources

- (Source: [[2026-06-10-perplexity-claude-fable-5-finance]]) — Perplexity deep research (59 cited sources) on Fable 5 specs, benchmarks, and finance/trading adoption.
- Anthropic model documentation — *Introducing Claude Fable 5 and Claude Mythos 5*; model overview; Fable 5 pricing and data-retention pages (platform.claude.com, anthropic.com).
- Vals AI benchmark leaderboards (CorpFin v2, Finance Agent v2, SWE-bench, Vals Index).
- Claude release announcements (anthropic.com/news), 2023-2026.
- AWS Bedrock and Google Vertex AI Claude integration documentation.
- Public SWE-bench Verified leaderboard results.
- Industry reporting from Bloomberg, The Information, TechCrunch on Claude release cadence.
- (Source: [[2026-04-22-gap-finder-ai-2026-major-news-stories]])

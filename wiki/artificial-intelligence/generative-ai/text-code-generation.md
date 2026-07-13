---
title: "Text & Code Generation"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Text Generation", "Code Generation", "AI Coding", "LLM Writing"]
domain: [ai-trading]
difficulty: beginner
related: ["[[generative-ai-overview]]", "[[foundation-models]]", "[[prompt-engineering-trading]]", "[[anthropic]]", "[[openai]]", "[[ai-trading-agents]]", "[[backtesting-overview]]", "[[artificial-intelligence]]"]
---

# Text & Code Generation

**Text and code generation** is the primary use case of [[foundation-models|large language models]] and the most directly impactful generative AI capability for trading. LLMs write research notes, generate [[backtesting-overview|backtesting]] code, draft trade rationales, summarise filings, and produce structured analysis — tasks that previously required hours of human effort.

## Text Generation for Trading

| Use Case | Input | Output | Time Saved |
|----------|-------|--------|-----------|
| **Earnings summary** | 50-page 10-K filing | 1-page structured summary with key metrics | Hours → minutes |
| **Research note** | Market data + thesis | Multi-paragraph analysis with citations | 1 hour → 5 minutes |
| **Trade rationale** | Position + market context | Documented reasoning for compliance/review | 20 min → 2 min |
| **Macro commentary** | Economic data releases | Daily market wrap for clients/team | 30 min → 3 min |
| **Risk report** | Portfolio positions + VaR | Narrative risk summary for stakeholders | 45 min → 5 min |

## Code Generation for Trading

| Use Case | What's Generated | Framework |
|----------|-----------------|-----------|
| **[[backtesting-overview|Backtesting]] scripts** | Full backtest pipeline from strategy description | [[backtrader-framework|Backtrader]], [[vectorbt]], [[quantconnect|QuantConnect]] |
| **Data pipelines** | Fetch, clean, transform market data | pandas, APIs |
| **Technical indicators** | Custom indicator calculations | TA-Lib, pandas |
| **Visualisation** | Charts, dashboards, performance reports | matplotlib, plotly |
| **Execution scripts** | Order management, API integration | Exchange APIs, ccxt |
| **Analysis notebooks** | Exploratory data analysis | Jupyter, pandas |

### Claude Code for Trading

[[anthropic|Claude Code]] specifically changed the game for individual traders:
- Describe a strategy in English → receive a complete backtesting script
- "Build me a data pipeline that fetches BTC hourly candles from Binance and computes RSI, MACD, and Bollinger Bands" → working Python code
- Iterate: "The backtest shows too many trades. Add a 4-hour cooldown between signals" → code updated

This capability is what the [[ai-narrative-arc|2025 AI narrative]] identified as the most durable AI trading innovation — AI as **coding copilot** rather than autonomous trader. By 2026, frontier coding models (Claude Opus 4.8, Fable 5) extended this from single-shot scripts to **long-horizon agentic execution** — multi-step refactors, full backtest harnesses, and overnight runs that complete without human correction, given a clear up-front goal.

## Quality Tiers

| Tier | Model (as of mid-2026) | Code Quality | Cost |
|------|-------|-------------|------|
| **Frontier / agentic** | Claude Fable 5, Claude Opus 4.8, GPT-5 | Reliable for complex codebases, long-horizon refactors, architecture decisions | $$$ |
| **Production balanced** | Claude Sonnet 4.6, GPT-5 mid-tier | Good first pass, needs review for edge cases | $$ |
| **Quick prototype** | Claude Haiku 4.5, GPT-5 mini | Fast scaffolding, may need significant editing | $ |
| **Local/private** | Code Llama, StarCoder, open-weight successors | Competitive for common patterns, weaker on complex logic | Free (GPU) |

Pricing as of mid-2026: Claude Opus 4.8 is ~$5 / $25 per million input / output tokens; Sonnet 4.6 ~$3 / $15; Haiku 4.5 ~$1 / $5; Fable 5 (the top tier) ~$10 / $50. Vendor pricing drifts — confirm current rates before sizing a workflow's cost.

## The Verification Rule

> **Always verify AI-generated code before running it with real capital.** Code generation excels at common patterns but can introduce subtle bugs in edge cases — incorrect datetime handling, off-by-one errors in lookback windows, or wrong assumptions about API data formats.

The safe workflow:
1. AI generates code
2. Human reviews logic and tests with paper trading
3. Validate against known results (reproduce a published backtest)
4. Deploy with small capital, monitor closely
5. Scale up after verification period

## See Also

- [[generative-ai-overview]] — GenAI hub
- [[foundation-models]] — The models generating text and code
- [[prompt-engineering-trading]] — Getting better outputs
- [[anthropic]] — Claude Code
- [[openai]] — GPT-4, Copilot
- [[backtesting-overview]] — Where generated code is deployed
- [[hallucinations-ai]] — Risk of incorrect generated content
- [[artificial-intelligence]] — AI section hub

## Sources

- Anthropic and OpenAI model and pricing documentation for tier capabilities and per-token costs (mid-2026 snapshot — vendor pricing and model line-ups drift; reverify before relying on the numbers).
- Provider entity pages: [[anthropic]], [[openai]].

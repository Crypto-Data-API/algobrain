---
title: AI Trading Agents
type: concept
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [llm, ai-trading, agents]
related: ["[[llm-market-analysis]]", "[[backtesting]]", "[[risk-management]]", "[[order-management-systems]]", "[[eliza-framework]]", "[[crewai]]", "[[langchain]]", "[[anthropic]]", "[[openai]]", "[[ai-agent-tokens]]", "[[defai]]", "[[ai-agent-strategies]]", "[[artificial-intelligence]]", "[[ai-prediction-markets]]", "[[ai-solvers]]", "[[ai-mev]]", "[[decentralized-ai]]", "[[llm-defi-interfaces]]", "[[ai-governance-attacks]]", "[[model-context-protocol]]", "[[agentic-commerce]]", "[[statistical-proof-of-execution]]"]
---

# AI Trading Agents

Autonomous AI agents that can research, hypothesize, code, backtest, and execute trades represent the frontier of [[ai-trading]]. Unlike static models that produce a single output, agents operate in loops — observing, reasoning, acting, and learning.

## Multi-Agent Architectures

Modern agent systems decompose trading into specialized roles:

- **Research agent**: Ingests news, filings, market data; produces structured summaries
- **Signal generation agent**: Analyzes research output, identifies trade opportunities
- **Risk management agent**: Evaluates proposed trades against portfolio constraints, [[position-sizing]] rules, and drawdown limits
- **Execution agent**: Routes orders, manages fills, handles partial executions via [[fix-protocol]] or exchange APIs
- **Monitoring agent**: Watches live positions, triggers alerts, escalates anomalies

Each agent can be a separate LLM instance with its own system prompt, tools, and memory. They communicate through shared state or message passing.

## LLM-Based Agent Capabilities

What makes LLM agents different from traditional algorithmic systems:

1. **Read and interpret unstructured data** — earnings calls, Reddit threads, research papers
2. **Generate hypotheses** — "This sector rotation pattern resembles 2018; here's a trade idea"
3. **Write and debug code** — generate [[backtesting]] scripts, fix data pipeline errors
4. **Adapt strategies** — modify parameters based on regime changes without human intervention
5. **Explain decisions** — produce human-readable rationale for every trade

## Frameworks and Examples

| Framework | Description |
|-----------|-------------|
| AutoGPT | General-purpose agent; can be prompted for trading research |
| [[anthropic|Claude Code]] | Strategy development, code generation, data analysis |
| [[eliza-framework|Eliza framework]] | Open-source agent framework used in crypto trading bots |
| [[crewai|CrewAI]] | Multi-agent orchestration for complex workflows |
| [[langchain|LangGraph]] | Stateful agent graphs with tool use |

## Current State: Mostly Experimental

The honest assessment: **AI trading agents are not consistently profitable** in production. Challenges include:

- **Compounding errors**: Small reasoning mistakes cascade through multi-step processes
- **Latency**: LLM inference is too slow for anything requiring sub-second decisions
- **Cost**: Running multiple agents continuously burns through API credits
- **Overfitting to narratives**: LLMs can construct convincing but wrong market stories
- **Hallucinated actions**: Agents may "believe" they executed a trade when they didn't

## The Future

The trajectory points toward agents that continuously learn from their own trading history, adapt to regime changes, and collaborate with human traders as copilots rather than replacements. The gap between research demos and production profitability remains wide, but narrowing.

## See Also

- [[llm-market-analysis]] — foundational LLM capabilities for markets
- [[cloud-trading-infrastructure]] — where to run agent systems
- [[order-management-systems]] — what agents connect to for execution
- [[eliza-framework]] — dominant crypto agent framework
- [[crewai]] — multi-agent orchestration
- [[langchain]] — LLM application framework
- [[ai-agent-tokens]] — crypto tokens in the AI agent space
- [[ai-agent-strategies]] — trading strategies using AI agents
- [[defai]] — DeFi + AI convergence
- [[artificial-intelligence]] — broader AI landscape

---
title: "Agentic AI"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Agentic AI", "AI Agents", "Autonomous AI"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[generative-ai-overview]]", "[[ai-trading-agents]]", "[[eliza-framework]]", "[[crewai]]", "[[langchain]]", "[[foundation-models]]", "[[prompt-injection]]", "[[ai-planning]]", "[[reinforcement-learning]]", "[[ai-security-trading]]", "[[ai-agent-tokens]]", "[[artificial-intelligence]]"]
---

# Agentic AI

**Agentic AI** refers to AI systems that can autonomously plan, reason, use tools, and take multi-step actions to achieve goals — going beyond single-response generation into persistent, goal-directed behaviour. Agentic AI is the architecture behind [[ai-trading-agents|trading agents]], coding assistants, research bots, and the [[ai-agent-tokens|crypto agent token]] ecosystem.

## What Makes AI "Agentic"

| Capability | Chatbot (Non-Agentic) | Agent (Agentic) |
|-----------|----------------------|-----------------|
| **Reasoning** | Single response to single query | Multi-step reasoning across a workflow |
| **Memory** | Forgets after conversation ends | Persistent memory across sessions |
| **Tool use** | No external actions | Calls APIs, reads databases, executes code |
| **Planning** | Reactive (responds to prompts) | Proactive (decomposes goals into subtasks) |
| **Autonomy** | Human initiates every interaction | Acts independently toward defined objectives |
| **Self-correction** | No — gives one answer | Evaluates own output, retries if unsatisfactory |

## The Agent Loop

```
┌──→ Observe (read market data, news, portfolio state)
│         ↓
│    Think (LLM reasoning: what should I do?)
│         ↓
│    Plan (decompose into subtasks)
│         ↓
│    Act (call tools: execute trade, run analysis, fetch data)
│         ↓
│    Evaluate (did the action succeed? update strategy?)
│         ↓
└────────┘ (loop until goal achieved or human intervenes)
```

## Agent Architectures

| Pattern | How | Framework | Trading Use |
|---------|-----|-----------|-------------|
| **ReAct** (Reason + Act) | LLM alternates between reasoning traces and tool calls | [[langchain|LangChain/LangGraph]] | Research agent: reason about what data to fetch, fetch it, reason about findings |
| **Plan-then-Execute** | Generate full plan, then execute steps | [[crewai|CrewAI]] | Portfolio rebalancing: plan all trades, then execute in sequence |
| **Multi-agent** | Multiple specialised agents collaborate | CrewAI, AutoGen | Research agent → analyst agent → risk agent → execution agent |
| **Reflexion** | Agent reflects on failures and self-corrects | Custom | Backtesting agent: runs test, analyses failure, adjusts parameters, re-runs |
| **Tool-augmented** | LLM with access to calculators, APIs, databases | Function calling (any LLM) | Market analysis with live price feeds, technical indicators |

## Key Components

| Component | Purpose | Example |
|-----------|---------|---------|
| **System prompt** | Define agent's role, constraints, personality | "You are a quantitative analyst. Never trade more than 2% of portfolio on a single idea." |
| **Memory** | Persist context across interactions | Conversation history, trade log, research notes |
| **Tools** | External capabilities the agent can invoke | Price API, news API, code execution, trade execution |
| **[[retrieval-augmented-generation|RAG]]** | Ground reasoning in factual data | Search wiki, filing database, research notes |
| **Guardrails** | Prevent harmful or unintended actions | Position limits, [[prompt-injection]] defence, human approval gates |

Tool access is increasingly standardised via the [[model-context-protocol|Model Context Protocol (MCP)]], which lets agents connect to data sources and execution venues through a uniform interface rather than bespoke integrations — relevant for plugging an agent into market-data feeds, brokers, and the wiki itself.

## The Honest Assessment

From the [[ai-narrative-arc|2024-2026 experience]]:

- **What works**: AI agents for research, code generation, data analysis, and structured workflows
- **What doesn't (yet)**: Fully autonomous trading that consistently outperforms humans
- **The lesson**: Agents are most valuable as **copilots** — extending human capability rather than replacing human judgment
- **The risk**: [[prompt-injection]], [[hallucinations-ai|hallucinations]], and cascading errors make fully autonomous agents unreliable for capital-at-risk decisions
- **The trajectory**: Improving rapidly — by mid-2026, frontier models ([[anthropic|Claude Opus 4.8/Sonnet 4.6]], GPT-4o-class, Gemini) sustain longer multi-step tool-use chains with lower error rates than the 2024 generation, and longer effective context windows let agents hold more portfolio and research state. Reliability on long-horizon, capital-at-risk autonomy still lags the hype, so production deployments remain human-supervised.

## Trading-Specific Agent Patterns

See [[ai-trading-agents]] for applied architectures and [[ai-agent-strategies]] for strategy categories.

## See Also

- [[generative-ai-overview]] — GenAI hub
- [[ai-trading-agents]] — Applied trading agents
- [[eliza-framework]], [[crewai]], [[langchain]] — Agent frameworks
- [[ai-agent-strategies]] — Strategy categories
- [[ai-agent-tokens]] — Crypto agent tokens
- [[prompt-injection]] — Primary agent security risk
- [[ai-security-trading]] — Securing agent systems
- [[ai-planning]] — Planning algorithms agents use
- [[model-context-protocol]] — Standard for connecting agents to tools and data
- [[artificial-intelligence]] — AI section hub

## Sources

- ReAct (Yao et al., 2022), Reflexion (Shinn et al., 2023), and the agent-pattern literature
- Anthropic, OpenAI, and LangChain/LangGraph agent and tool-use documentation, reviewed June 2026
- Model Context Protocol specification (Anthropic, 2024-onward)

---
title: "Model Context Protocol (MCP)"
type: concept
created: 2026-04-11
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, defi]
aliases: ["MCP", "Model Context Protocol", "Anthropic MCP"]
domain: [market-microstructure]
difficulty: intermediate
related: ["[[anthropic]]", "[[eliza-framework]]", "[[langchain]]", "[[crewai]]", "[[ai-trading-agents]]", "[[llm-defi-interfaces]]", "[[defai]]", "[[decentralized-ai]]", "[[artificial-intelligence]]"]
---

# Model Context Protocol (MCP)

**Model Context Protocol** (MCP) is an open protocol, originally released by [[anthropic|Anthropic]] in November 2024, that standardizes how LLM applications connect to external data sources, tools, and services. By Q4 2025 it had become the de-facto interface layer between LLM agents and everything outside the model — databases, APIs, file systems, enterprise SaaS, and on-chain blockchain tooling. It sits *upstream* of agent frameworks like [[eliza-framework|Eliza]], [[langchain|LangChain]], and [[crewai|CrewAI]]: those frameworks build agent *behavior* on top of MCP, while MCP itself standardizes *how the agent sees the world*.

For an AI×crypto wiki, MCP matters because it is the protocol layer that allows a single LLM to interact with dozens of blockchains, DEXes, lending protocols, oracle feeds, and data providers through a uniform interface — without reimplementing tool bindings for each target. It is the plumbing that makes [[llm-defi-interfaces|LLM-fronted DeFi wallets]] and [[ai-trading-agents|autonomous trading agents]] practical at all (Source: [[2026-04-11-perplexity-ai-crypto-gaps]]).

## The Problem MCP Solves

Before MCP, every LLM agent framework had to define its own way of exposing tools to the model. Eliza had its plugin system; LangChain had its Tool abstraction; CrewAI had task delegation. The cost of this fragmentation was real:

- **Redundant integrations** — every framework had to separately integrate with each data source
- **Vendor lock-in** — switching frameworks meant rewriting tool bindings
- **Missing capabilities** — niche data sources rarely had integrations in any framework
- **Testing fragmentation** — no standard way to mock tool responses for evaluation

MCP standardizes the three things every LLM-plus-tools system needs: a **resources** abstraction (read-only context the model can consult), a **tools** abstraction (actions the model can invoke with side effects), and a **prompts** abstraction (reusable templates for specific workflows). Any MCP-compatible server exposes these three surfaces, and any MCP-compatible client can consume them — without either side knowing about the other.

## How MCP Works

MCP is structured as a client–server protocol over JSON-RPC. The canonical pattern:

- **MCP Server** — a program that exposes some capability (read files, query a database, call an API, execute an on-chain transaction). It declares its resources, tools, and prompts at startup.
- **MCP Client** — typically an LLM application (Claude Desktop, a custom agent, a DeFi wallet) that connects to one or more MCP servers and surfaces their capabilities to the underlying model.
- **Transport** — stdio or HTTP-based; streamed responses supported for long-running operations.

The LLM itself does not need to know anything MCP-specific. The client translates model tool calls into MCP tool invocations, and translates MCP resource reads into context the model consumes. This separation is why MCP composes cleanly with any LLM that supports function calling, including OpenAI, Anthropic, Google, and open-weight models.

## The November 2025 One-Year Milestone

By the one-year anniversary of MCP's release (November 2025), several maturity markers had landed:

- **Tool calling inside sampling requests** — servers can now request the LLM's help during tool execution, enabling recursive agent loops
- **Server-side agent loops** — MCP servers can orchestrate multi-step workflows rather than just exposing single-call tools
- **Parallel tool execution** — clients can dispatch multiple MCP tool calls simultaneously, enabling genuine agent concurrency
- **Decoupled request payloads** — more flexible message structures for complex tool interactions
- **Enterprise adoption at scale** — multiple enterprise governance, compliance, and data-access platforms shipped MCP servers as the canonical integration pattern

The trajectory matches earlier platform protocols (REST, GraphQL, gRPC) in moving from "novel idea" to "obvious default" in roughly one year. By mid-2026, MCP support is shipped first-party across the major model providers' agent SDKs and is the assumed integration layer for new agent frameworks rather than an optional add-on.

## Why MCP Matters for AI×Crypto Specifically

Three specific MCP properties make it load-bearing for decentralized finance and trading agents:

### 1. Uniform Blockchain Integration

An MCP server can wrap a blockchain RPC, a DEX aggregator, a lending protocol, or an oracle feed. A single LLM agent connecting to multiple such servers gains composable access to the whole DeFi stack without reimplementing each integration. Brian AI, Hey Anon, and other [[llm-defi-interfaces|LLM-fronted DeFi wallets]] increasingly use MCP or MCP-inspired patterns internally.

### 2. Separation of Planning from Execution

Because MCP tools can have explicit side-effect semantics, the protocol supports a clean "propose then sign" pattern: the LLM constructs a transaction plan using MCP tools that don't execute, and a separate signing step (with the user's approval) commits the plan to chain. This is essential for any agent that handles real money.

### 3. Permissionless Tool Composition

An agent using MCP can in principle connect to any MCP server any developer ships — including DeFi-specific servers that emerge post-launch. This permissionless composability aligns naturally with DeFi's own composability thesis and is probably why MCP-based patterns are propagating faster in crypto than in traditional SaaS.

## The Regulatory Dimension

MCP's rise has regulatory implications that are only starting to be named:

- **Audit trails** — MCP servers can log every tool invocation, creating a natural audit trail for compliance-sensitive AI applications
- **Access control** — server-level authorization makes it straightforward to restrict what an agent can do on behalf of a specific user
- **Liability clarity** — when a trading agent makes a bad decision, the MCP server logs separate the model's reasoning from the tool's execution, which matters for post-hoc attribution

These properties don't solve the hard questions of agent liability — see [[ai-agent-daos]] — but they make the technical substrate friendlier to regulators than the prior "opaque LLM calls opaque API" pattern.

## What MCP Is Not

For precision:

- **MCP is not an agent framework** — it does not define how an agent decides what to do; frameworks like Eliza and LangChain still handle that layer
- **MCP is not a blockchain protocol** — it has no on-chain component; it's a client–server protocol for LLM applications
- **MCP is not Anthropic-specific** — though Anthropic released it, the protocol is open and has implementations from OpenAI, Google, and many independent developers
- **MCP does not solve alignment or safety** — it is infrastructure, not a safety mechanism; see [[ai-safety-alignment]]

## See Also

- [[anthropic]] — Creator of MCP
- [[eliza-framework]] — Agent framework that builds on top of MCP and MCP-like patterns
- [[langchain]] — Agent framework, complementary to MCP
- [[crewai]] — Agent framework, complementary to MCP
- [[ai-trading-agents]] — Primary consumer of MCP in the trading context
- [[llm-defi-interfaces]] — DeFi wallets that rely on MCP-style tool integration
- [[defai]] — Parent DeFAI narrative
- [[decentralized-ai]] — Broader AI×crypto context
- [[artificial-intelligence]] — AI section hub

## Sources

- [[2026-04-11-perplexity-ai-crypto-gaps]] — Perplexity research identifying MCP as a structural gap in coverage
- Anthropic MCP announcement (November 2024) and one-year-anniversary post (November 2025), modelcontextprotocol.io
- Model Context Protocol specification and reference documentation, modelcontextprotocol.io

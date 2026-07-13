---
title: "Agentic Commerce"
type: concept
created: 2026-04-11
updated: 2026-06-12
status: good
tags: [ai-trading, agents, crypto, defi]
aliases: ["Agent Commerce", "Agentic Payments", "Agent-to-Agent Commerce"]
domain: [market-microstructure]
difficulty: intermediate
related: ["[[ai-trading-agents]]", "[[llm-defi-interfaces]]", "[[model-context-protocol]]", "[[ai-solvers]]", "[[defai]]", "[[decentralized-ai]]", "[[proof-of-humanity]]", "[[artificial-intelligence]]"]
---

# Agentic Commerce

**Agentic commerce** is the category of economic activity in which autonomous AI agents conduct purchases, negotiations, and payments on behalf of users or other agents — sometimes directly with merchant platforms, sometimes with other AI agents, sometimes through brokered intermediaries. It is a cross-domain category that spans traditional retail, enterprise SaaS, and crypto-native DeFi, and the crypto angle is specifically about **cryptographic settlement and programmable payment rails** that make agent-to-agent commerce economically coherent.

The category was formally named in a 2025 McKinsey research note and has since been adopted across both the AI and crypto ecosystems. It is structurally important because it is one of the few AI×crypto framings where the narrative is driven by traditional enterprise research rather than by crypto-native hype (Source: [[2026-04-11-perplexity-ai-crypto-gaps]]).

## The Three Interaction Models

McKinsey's 2025 framework identified three distinct interaction patterns that agentic commerce encompasses. The distinction matters because each model has different trust, payment, and infrastructure requirements.

### 1. Agent-to-Site

An AI agent directly accesses a merchant website or API on behalf of a human user. The merchant knows it is dealing with an agent; the agent completes the purchase using the user's payment method or a delegated allowance.

- **Example**: OpenAI's **Operator** (launched January 2025, now integrated into ChatGPT) can browse sites and complete purchases on behalf of a user
- **Payment rail**: traditional (credit card, stored payment method) or crypto (session-key-signed transactions)
- **Trust model**: the user trusts the agent; the merchant authenticates the payment, not the agent's identity

### 2. Agent-to-Agent

Two autonomous agents negotiate and settle a transaction directly, without a shared merchant frontend. This is the model with the deepest crypto connection because **crypto is uniquely suited to cryptographic settlement between unknown counterparties**.

- **Example**: two enterprise procurement agents negotiating a bulk purchase without involving human approvers
- **Payment rail**: natively crypto (stablecoins, programmable payments, escrow via smart contracts)
- **Trust model**: each agent verifies the other through cryptographic credentials, reputation systems, or [[proof-of-humanity|identity attestations]] for the humans they represent

### 3. Brokered Agent-to-Site

A third-party platform sits between agents and merchants, handling protocol translation, payment coordination, and dispute resolution. Analogous to how OpenTable sits between restaurant-goers and restaurants.

- **Example**: an "agent-accessible merchant directory" where an agent can discover and transact with many merchants through one broker
- **Payment rail**: broker handles conversion between user-side and merchant-side rails
- **Trust model**: both agent and merchant trust the broker; broker has reputational skin in the game

## The Stripe + OpenAI Agentic Commerce Protocol

In Q1 2025, Stripe and OpenAI co-developed the **Agentic Commerce Protocol** — a concrete specification that lets users complete purchases inside ChatGPT without leaving the chat. The key design elements:

- **Cryptographic signatures** on purchase intents (not unlike EIP-712 typed structured data signing in Ethereum)
- **Conditional execution logic** (purchase completes only if merchant matches stated conditions)
- **Session-scoped authorization** (the user pre-authorizes a spending envelope, and the agent executes within it)

This is structurally interesting for two reasons. First, it is a *cryptographic* payment protocol developed by a traditional fintech (Stripe) in response to agent-driven commerce needs — a rare case of traditional finance reaching into crypto primitives rather than the reverse. Second, it creates a design template that crypto-native projects can adopt and extend: every design decision (intent signing, conditional execution, session scoping) maps cleanly to existing crypto primitives like [[ai-solvers|intent-based routing]], account abstraction, and smart contract escrow.

## The Market Scale

McKinsey's 2025 framework projected that **the US B2C retail market alone could see ~$1 trillion in orchestrated revenue from agentic commerce by 2030**, with global projections of $3–5 trillion. These are forecasts, not observed revenue, and should be treated as directional rather than precise. But even the directional framing is large enough to change how enterprise and crypto infrastructure decisions are made.

Three specific downstream effects are already visible:

1. **L2 scaling is being optimized for agent transaction patterns** — small, frequent, low-value payments rather than the high-value DeFi trades that dominated early L2 usage
2. **Account abstraction and session keys are mainstream** — driven in large part by the need for agents to transact without per-transaction human signing
3. **Intent solver networks (see [[ai-solvers]]) are positioning to serve agent-to-agent flow** — since agents generate exactly the kind of declarative intent that solver networks are built to process

## The Crypto Advantage (If Any)

The honest question: does crypto actually win in agentic commerce, or does traditional fintech (Stripe, Visa, bank rails) capture the category by default? Three arguments for a real crypto advantage:

1. **Permissionless counterparty discovery** — agents can find and transact with new counterparties without each side pre-registering with a central authority
2. **Programmable payment logic** — conditional, multi-hop, escrow-based, or revenue-share payments are trivial in crypto and awkward in traditional rails
3. **Cross-border and cross-currency** — agent-to-agent commerce will inevitably cross currency and jurisdiction lines; stablecoins and programmable bridges handle this natively

Three arguments against:

1. **Traditional rails already work at scale** — Stripe, Visa, Plaid, and their peers handle multi-trillion-dollar flows with latency and reliability that crypto has not yet matched for consumer transactions
2. **Consumer trust and liability frameworks** — traditional payments have well-understood fraud protection, chargebacks, and regulatory backing; crypto rails do not
3. **User experience asymmetry** — agents transacting on behalf of users need to fit into existing consumer wallets and banking apps; those are far more mature in the traditional stack

The realistic prediction is that agentic commerce will run on **both** rails simultaneously, with crypto winning the specific slices where its advantages matter (cross-border, programmable logic, agent-to-agent) and traditional rails winning the rest.

## Connection to Autonomous Agent DAOs

Agentic commerce is the consumer-facing counterpart of [[ai-agent-daos|autonomous agent DAOs]]. The DAO side solves governance, accountability, and capital management for agent-operated organizations; the commerce side solves the mechanics of how those agents transact with the outside world. The two together constitute the full stack of "AI as economic actor" that the 2024–2026 AI×crypto narrative has been gesturing at.

## Honest Assessment

As of early 2026, agentic commerce is more narrative than revenue. OpenAI Operator, the Stripe Agentic Commerce Protocol, and early agent wallets are in production but serve a small user base relative to the $1–5T forecast. The category's structural importance is real — the shift from human-directed to agent-directed commerce is a once-per-decade pattern — but the timeline is slower than the narrative implies. Expect the category to matter over a 5–10 year horizon, not 12 months.

For traders, the cleanest angle is **payment rail infrastructure**: L2s, account abstraction, intent solvers, and stablecoin issuers all benefit from agentic commerce growth regardless of which specific agents succeed.

## See Also

- [[ai-trading-agents]] — Trading-specific subset of agentic commerce
- [[llm-defi-interfaces]] — Consumer wallet layer that agentic commerce sits on top of
- [[model-context-protocol]] — Tool-layer infrastructure for agents
- [[ai-solvers]] — Intent-based routing as the execution layer for agent payments
- [[proof-of-humanity]] — Identity layer for agent counterparty verification
- [[ai-agent-daos]] — DAO-governed counterpart
- [[defai]] — DeFi + AI parent narrative
- [[artificial-intelligence]] — AI section hub

## Sources

- (Source: [[2026-04-11-perplexity-ai-crypto-gaps]]) — Perplexity research on agentic commerce as a distinct category
- McKinsey 2025 research on agentic commerce (framework and market sizing)
- Stripe + OpenAI Agentic Commerce Protocol announcement (Q1 2025)

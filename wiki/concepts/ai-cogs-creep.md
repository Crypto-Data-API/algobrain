---
title: "AI COGS Creep"
type: concept
created: 2026-05-09
updated: 2026-06-11
status: good
tags: [ai-trading, machine-learning, behavioral-finance, risk-management, market-microstructure]
aliases: ["AI Gross Margin Compression", "Inference Cost Creep", "Hidden COGS of AI"]
related: ["[[solow-paradox-2026]]", "[[ai-layoff-trap]]", "[[margin-expansion-disparity]]", "[[white-collar-ai-displacement-short]]", "[[2026-05-08-cloudflare-ai-layoff-selloff]]", "[[2026-04-09-saas-agent-selloff]]", "[[klarna]]", "[[capital-vs-labor-asymmetry]]", "[[saas]]", "[[unit-economics]]"]
domain: [market-microstructure, behavioral-finance, risk-management]
prerequisites: ["[[unit-economics]]", "[[saas]]"]
difficulty: intermediate
---

**AI COGS creep** is the firm-level mechanism by which integrating AI features into a software product compresses gross margin from the traditional SaaS 70–80% range toward 50–65%. The compression comes from variable AI infrastructure costs — inference compute, model API charges, model routing, vector database storage, retrieval augmentation — that flow through cost of revenue rather than operating expense. Unlike the labor cost layoffs reduce, AI COGS sits inside gross profit, so headcount cuts cannot offset it. AI COGS creep is the firm-level signature of [[solow-paradox-2026]] and the proximate explanation for why the [[2026-05-08-cloudflare-ai-layoff-selloff|Cloudflare May 2026]] print missed gross margin (72.8% vs 75.1% consensus) on the same day it announced AI-driven layoffs.

## The arithmetic

A canonical illustration (per *The SaaS CFO*):

| Component | Traditional SaaS | SaaS + AI features |
|-----------|------------------|---------------------|
| Revenue | $100 | $100 |
| Direct COGS (hosting, support) | $20 | $20 |
| AI variable cost (inference, routing, vectors) | $0 | **$15** |
| Total COGS | $20 | $35 |
| **Gross margin** | **80%** | **65%** |

The ICONIQ 2026 *State of AI* survey reports that AI-product builders expect **average gross margins of ~52% in 2026** — well below the 70–80% benchmark for legacy SaaS. The trajectory points lower as adoption deepens before tooling efficiencies arrive.

(Sources: *The SaaS CFO*, ICONIQ Capital, BainCapitalVentures, SoftwareSeni.)

## The cost layers

AI COGS creep aggregates several variable costs that did not exist in the prior SaaS unit economics:

1. **Inference compute** — token-by-token charges for LLM API calls, or amortized GPU cost if self-hosted. Heavy users and verbose prompts blow up unit economics.
2. **Model routing** — multi-provider routing layers (OpenRouter-style, AI Gateway-style) carry their own margins on top of underlying inference.
3. **Vector database storage and queries** — RAG workflows store embeddings (cents per million tokens at storage; query costs at retrieval).
4. **Retrieval augmentation pipelines** — the orchestration layer (chunking, re-ranking, filtering) consumes additional inference.
5. **Evaluation and safety infrastructure** — content moderation, hallucination checks, guardrails — each its own inference call.
6. **Egress and bandwidth** — heavy multimodal payloads (image/audio/video) carry CDN and egress costs.

Several of these scale super-linearly with usage: a "power user" cohort can consume 10–50× the inference of an average user without paying 10–50× the subscription fee.

## Why layoffs cannot fix this

This is the pivot point for traders. **Headcount sits in operating expense; AI COGS sits in cost of revenue.** Cutting people improves operating margin but does not improve gross margin. Investors in 2026 have learned to read these separately:

- A clean AI-cuts story produces opex savings → improves operating margin
- An AI-features story produces COGS creep → compresses gross margin
- The two layer on top of each other; cuts cannot offset COGS

This is precisely what [[2026-05-08-cloudflare-ai-layoff-selloff|Cloudflare's May 2026 print]] revealed: 1,100 roles cut, but gross margin missed by 230 bps because Workers / R2 / D1 (lower-margin developer products) grew faster than legacy CDN/security. The market now reads "AI-first restructuring" as a flag for both risks at once.

## Connection to seat compression

AI COGS creep is the **cost-side** of the SaaS squeeze. The **revenue-side** is seat compression — see [[2026-04-09-saas-agent-selloff]]: as AI agents replace human seat-license users, seat counts and seat revenue erode. Together:

- Revenue: seat compression → top line under pressure
- Cost: AI COGS creep → gross margin under pressure
- Result: gross profit compression on both sides; only the firms with pricing power, proprietary data, or distribution moats can defend

This is why the [[margin-expansion-disparity]] gap is widening — frontier AI deployers (Mag 7) capture inference revenue *as suppliers*, while non-frontier SaaS *as buyers* of inference faces COGS creep without being able to pass it through.

## Pricing model responses

Firms have begun shifting pricing models to defend gross margin:

- **Outcomes-based pricing** — charge per outcome (lead generated, ticket resolved) rather than per seat, internalizing the agent productivity instead of letting customers capture it. Heavily marketed by AI-first vendors in 2025–2026.
- **Consumption-based pricing** — pass inference cost through transparently (Snowflake-style credits)
- **AI feature tiering** — restrict heavy AI features to higher SKUs, hoping mix shift offsets COGS
- **Bring-your-own-key (BYOK)** — push inference cost off-platform; preserves margin but removes a meaningful revenue line

Each response trades different risks. The market has not yet endorsed any of them as the durable answer.

## Trading implications

- **Short basket sharpener**: high-AI-feature, low-pricing-power SaaS names are exposed on both seat compression *and* AI COGS creep. The [[white-collar-ai-displacement-short]] strategy gains a screen: "gross margin trajectory" alongside "AI exposure."
- **Long basket filter**: AI-deployer firms whose AI revenue is *outbound* (selling inference, infrastructure, models) are insulated from AI COGS creep — Mag 7 hyperscalers, Nvidia. Verify that AI revenue is supplier-side, not buyer-side.
- **Earnings event risk**: any 2026 earnings print where AI features have been added carries discrete gross-margin downside risk on the same day — model the asymmetry.
- **Analyst-day signal**: management commentary on "AI COGS" or "AI gross margin trajectory" is a leading indicator. Commentary about "outcomes-based pricing pivot" is the polite acknowledgement that COGS is creeping.
- **Specific candidates exposed**: [[snowflake|SNOW]] (Cortex AI inference), [[mongodb|MDB]] (Atlas Vector Search), [[datadog|DDOG]] (LLM observability), [[salesforce|CRM]] (Agentforce), [[servicenow|NOW]] (Now Assist), [[atlassian|TEAM]] (Atlassian Intelligence)

## What unwinds the trade

- **Inference cost collapse** — if foundation-model inference costs drop another 10× in 12 months, the $15 layer in the canonical example may become $1.50 and gross margins recover. Watch token cost trajectories from Anthropic, OpenAI, Google, and open-weight competition.
- **Outcomes-based pricing legitimization** — if customers accept outcomes-based pricing at scale, AI vendors capture the productivity rather than passing it through.
- **Hardware efficiency** — TPU / custom-silicon adoption could reset unit economics for self-hosted deployments.
- **Demand for AI features cools** — the unlikely scenario where customers stop pushing AI features onto SaaS roadmaps; would relieve COGS pressure but kill the AI-narrative multiple.

If two or more of these resolve favorably within 12 months, AI COGS creep stops being load-bearing for the short thesis.

## Related

- [[solow-paradox-2026]] — productivity gap at the firm level
- [[ai-layoff-trap]] — labor-side mechanism; AI COGS creep is the cost-side mechanism
- [[margin-expansion-disparity]] — the disparity AI COGS creep deepens
- [[white-collar-ai-displacement-short]] — strategy that uses AI COGS creep as a stock screen
- [[2026-05-08-cloudflare-ai-layoff-selloff]] — first firm-level visible confirmation
- [[2026-04-09-saas-agent-selloff]] — sector-wide seat-compression repricing
- [[klarna]] — service-quality reversal that compounds COGS creep
- [[capital-vs-labor-asymmetry]] — capital-side capture of productivity gains
- [[unit-economics]] — base concept
- [[saas]] — base concept

## Sources

- [Your AI Feature Is Quietly Destroying Your Gross Margin — The SaaS CFO](https://www.thesaascfo.com/your-ai-feature-is-quietly-destroying-your-gross-margin/)
- [Why AI Gross Margins Are So Much Lower Than SaaS — SoftwareSeni](https://www.softwareseni.com/why-ai-gross-margins-are-so-much-lower-than-saas-and-what-that-means-for-your-business/)
- [Outcomes-Based Pricing and AI-First SaaS Gross Margin Economics — SoftwareSeni](https://www.softwareseni.com/outcomes-based-pricing-and-ai-first-saas-gross-margin-economics-explained/)
- [The Economics of AI-First B2B SaaS in 2026 — Monetizely](https://www.getmonetizely.com/blogs/the-economics-of-ai-first-b2b-saas-in-2026)
- [The Hidden COGS of AI: Why Your Pricing Model Might Be Doomed — Monetizely](https://www.getmonetizely.com/articles/the-hidden-cogs-of-ai-why-your-pricing-model-might-be-doomed)
- [Gross Margin Myth in AI Apps — Bain Capital Ventures](https://baincapitalventures.com/insight/gross-margin-is-a-bs-metric/)
- [Unit economics for AI SaaS companies — Drivetrain](https://www.drivetrain.ai/post/unit-economics-of-ai-saas-companies-cfo-guide-for-managing-token-based-costs-and-margins)
- ICONIQ Capital, *2026 State of AI* — survey-derived 52% AI gross margin benchmark

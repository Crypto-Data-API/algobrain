---
title: "Perplexity Deep Research: AI×Crypto Coverage Gaps Audit"
type: source
created: 2026-04-11
updated: 2026-06-12
status: good
tags: [ai-trading, crypto, machine-learning, defi, meta]
aliases: ["AI Crypto Gaps Audit", "AIxCrypto Gaps Audit", "Perplexity AI Crypto Gap Finder"]
source_type: article
source_url: "https://api.perplexity.ai/chat/completions"
source_author: "Perplexity sonar-deep-research"
source_date: 2026-04-11
source_file: "r2://trader-wiki/articles/2026-04-11-perplexity-ai-crypto-gaps.md"
confidence: medium
claims_count: 30
related: ["[[decentralized-ai]]", "[[defai]]", "[[artificial-intelligence]]", "[[ai-narrative-arc]]", "[[zkml]]", "[[restaking-and-ai]]", "[[ai-mev]]", "[[llm-defi-interfaces]]", "[[truth-terminal-goat]]", "[[ai-solvers]]"]
---

# Perplexity Deep Research: AI×Crypto Coverage Gaps Audit

On 2026-04-11 a one-shot call to Perplexity's `sonar-deep-research` model was executed with a single carefully-scoped prompt asking the model to identify gaps in this wiki's AI×crypto coverage, given an explicit list of what was already covered. The model performed 80 search queries and returned ~7,300 tokens of structured findings across 30 distinct items. Cost: $1.08. Prompt and full response are preserved in the raw file at the path above.

This page summarizes the claims, assigns confidence levels, and records which claims were extracted into wiki pages. It is the canonical citation target for any new page sourced primarily from this research.

## Methodology and Confidence Framing

Perplexity `sonar-deep-research` is itself an LLM-driven research tool. Its outputs are citation-rich but inherit the failure modes of its underlying search and summarization layers. Claims here are classified:

- **HIGH**: verifiable against a specific cited source with matching dates, numbers, and named actors
- **MEDIUM**: plausible, well-sourced but with single-source risk or imprecise dates
- **LOW**: speculative, rumor-level, or contradicted by other sources
- **UNVERIFIED**: flagged for later verification

**Overall confidence**: MEDIUM. The research surfaced genuinely useful structural gaps, but specific numerical claims (market caps, TVL, launch dates) should be re-verified before publication in any page where precision matters.

## Claims Extracted

### Verifiable AI Infrastructure (claims 1–3)

1. **[MEDIUM]** Warden Protocol's SPEX (Statistical Proof of Execution) is deployed in production by February 2026, providing sampling-based probabilistic verification for AI workloads. Reported 5–10 orders of magnitude speedup vs ZKML (milliseconds vs minutes). Source: SPEX whitepaper; arXiv 2603.19025 "Towards Verifiable AI with Lightweight Cryptographic Proofs"
2. **[MEDIUM]** EigenLayer crossed ~$18B restaked ETH by Feb 2026; introduced "Vertical AVS" category including **EigenAI** (mainnet late 2025) and **EigenCompute** (mainnet alpha Jan 2026); ELIP-12 (Q1 2026) mandates fee-generating AVS; ~280 crypto-AI projects now require trust-minimized model evaluation. Source: blockeden.xyz Feb 2026 report
3. **[MEDIUM]** Verifiable inference layer (OpenGradient, Giza Orion, Modal, Together.ai) occupies middle ground between GPU compute tokenization and ZKML — "verifiable cloud" pattern. Source: blog.icme.io guide to ZKML 2025

### MCP as Foundational Infrastructure (claim 4)

4. **[HIGH]** Model Context Protocol (MCP) was released by Anthropic in November 2024; by Q4 2025 had become the de-facto standard for connecting AI agents to external data, APIs, and on-chain systems. The Nov 2025 one-year update introduced tool calling in sampling requests, server-side agent loops, parallel tool execution, and decoupled request payloads. Source: blog.modelcontextprotocol.io first-anniversary post

### Agentic Commerce (claims 5–6)

5. **[MEDIUM]** McKinsey published 2025 research framing "agentic commerce" as a distinct $1–5T market category with three interaction models (agent-to-site, agent-to-agent, brokered agent-to-site). Stripe + OpenAI co-developed an Agentic Commerce Protocol in Q1 2025 for in-ChatGPT purchases using cryptographic signatures. OpenAI released Operator in January 2025
6. **[MEDIUM]** Base reached ~$12.64B TVL by Feb 2026 and became the primary venue for production AI agents; **Clanker** (tokenbot) alone generated $8.02M in fees in a single week in early Feb 2026, having facilitated 21,870 token launches in one day. Other Base-native projects: A0x (no-code agentic platform), Venice (privacy-first inference API on Base). Source: svb.com crypto outlook, binance square posts

### Content Authenticity (claims 7–8)

7. **[MEDIUM]** C2PA / Content Authenticity Initiative reached production inflection point in 2026; CAWG 1.2 spec released late 2025; adoption by Adobe Firefly, Worldcoin, Provenance Labs. Blockchain-backed content provenance becomes essential as AI-generated content proliferates. Source: contentauthenticity.org state-of-2026 post
8. **[MEDIUM]** SEC digital assets regulatory framework proposal (September 2025) explicitly addresses AI content attribution and liability. Source: sec.gov ctf-written-sec-proposal-digital-asset-09-08-2025.pdf

### Recent Agent Developments and AI Token Reset (claims 9–11)

9. **[MEDIUM]** Terminal of Truths wallet (Truth Terminal behind GOAT memecoin) accumulated ~$656K in wallet value by early 2025, holding 1.93M GOAT tokens plus other memecoins. Marc Andreessen's $50K BTC donation (July 2024) was the watershed "first AI millionaire" moment. Source: arkm.com Arkham research post
10. **[MEDIUM]** AI16Z token reached ~$2B market cap within 10 days of launch in early February 2025 on Solana. Source: openexo post
11. **[HIGH]** AI tokens collectively posted -50.2% YTD 2025; sector lost ~75% year-over-year; eight of top ten AI tokens had losses >70% by Q4 2025 (ASI Alliance -84%, Render -82%, The Graph -82%). Source: cryptoslate.com "10 biggest crypto losers of 2025"

### Decentralized Autonomous Agents (claims 12–14)

12. **[MEDIUM]** Peer-reviewed empirical study on DeAgents (decentralized autonomous agents) published 2025 examining the trustless-autonomy paradox. Source: arXiv 2505.09757
13. **[MEDIUM]** Unichain became first Ethereum L2 to mandate TEE-based block building by August 2025. Features: encrypted mempool (decrypted only inside TEE), deterministic priority ordering, 200–250ms flashblocks. Source: symbiosis.finance defi 2025–2026 overview
14. **[MEDIUM]** ESMA TRV Risk Analysis (July 2025) published first regulatory taxonomy of MEV under MiCA, distinguishing benign (arbitrage, liquidations) from toxic (front-running, sandwich attacks). Created regulatory incentives for L2s to adopt MEV-suppressing architectures

### Academic and Research (claims 15–17)

15. **[MEDIUM]** Peer-reviewed body of work on federated learning with blockchain-based incentive mechanisms. Source: arXiv 2602.08290
16. **[MEDIUM]** ZKML overhead dropped from ~1,000,000x to ~10,000x in 2024–2025; 2026 shift to GPU optimization expected to add 5–10x speedups. zkPyTorch (March 2025) proved VGG-16 in 2.2s; Lagrange DeepProve (August 2025) tackled large LLM inference. Proof compression via folding: ResNet-50 proof size from 1.27GB to <100KB. Source: blog.icme.io definitive guide to ZKML 2025
17. **[MEDIUM]** ZKML frameworks moved from implementing ONNX operators one-by-one toward operator compilers and generalized primitives

### Cross-Chain and Intent-Based Architecture (claims 18–19)

18. **[MEDIUM]** Peer-reviewed measurement study of cross-chain arbitrage MEV covering Sept 2023–Aug 2024. Source: ACM DL 3771566
19. **[MEDIUM]** By 2025–2026 intent-based architecture became dominant DeFi design pattern; five-layer stack emerged: settlement → execution → interoperability → account/intent → automation

### Protocol Launches and Pivots (claims 20–24)

20. **[MEDIUM]** Sonic Labs unveiled **Spawn** at ETHDenver 2026 — natural-language Web3 app builder with AI agent "Spawny" for iteration; closed beta March 2026. Source: blog.soniclabs.com
21. **[MEDIUM]** **Nexus** Layer 1 + Nexus zkVM announced record-breaking Testnet III achieving "quadrillion FLOPS of verifiable compute". Source: blog.nexus.xyz 2025 Nexus wrapped post
22. **[LOW]** Starknet 2025 year-in-review claims: sub-500ms transaction speed, fully decentralized sequencing, quantum-secure roadmap. Source: starknet.io 2025-year-in-review post
23. **[LOW]** zkVerify mainnet-launched 2025 as unified ZK proof verification aggregation layer. Source: zkverify.io 2025 year-in-review
24. **[LOW]** Lorenzo Protocol (Bitcoin DeFi / staking) crossed ~$600M TVL by March 2025. Source: lorenzo-protocol.webflow.io

### Developer Tools and SDKs (claims 25–28)

25. **[MEDIUM]** ElizaOS positioned as "Agentic Operating System"; deployed verifiable agents on EigenLayer infrastructure by Q1 2026; used for production trading agents on Base. Source: elizaos.ai
26. **[MEDIUM]** Brian expanded to include Synapse (Starknet DeFi assistant), BEAMX (non-custodial intent app), Ava (portfolio-management agents), copy-trading bots via XMTP. Source: docs.brianknows.org
27. **[LOW]** Giza Orion provides Cairo-native verifiable SVM model tutorials. Source: orion.gizatech.xyz
28. **[MEDIUM]** OpenGradient Python SDK for decentralized model management and inference. Source: github.com/OpenGradient/sdk

### Regulatory Developments (claims 29–30)

29. **[MEDIUM]** ESMA TRV Risk Analysis July 2025 — see claim 14
30. **[MEDIUM]** SEC digital assets framework proposal September 2025 — see claim 8

## Claims Used in Wiki Pages

The following pages were created or updated sourcing this research (tracked here so claims can be re-verified later):

- [[model-context-protocol]] — sources claim 4
- [[agentic-commerce]] — sources claims 5–6
- [[statistical-proof-of-execution]] — sources claim 1
- [[content-authenticity]] — sources claims 7–8
- [[zkml]] — extended with claims 16–17
- [[restaking-and-ai]] — extended with claim 2
- [[ai-narrative-arc]] — extended with claims 9, 10, 11
- [[ai-mev]] — extended with claims 13, 14, 18
- [[truth-terminal-goat]] — extended with claim 9
- [[llm-defi-interfaces]] — extended with claim 26
- [[ai-solvers]] — extended with claim 19
- [[bittensor-subnets]] — extended with claim 11 (post-reset context)

## Claims NOT Used (Reasoning)

- **Claim 22** (Starknet quantum-secure roadmap): not AI×crypto-specific; general L2 infrastructure
- **Claim 23** (zkVerify mainnet): useful tool but not a standalone structural bridge; may be mentioned inline in zkml.md as a verification aggregation example
- **Claim 24** (Lorenzo Protocol): not AI-specific enough for the scope of this audit
- **Claim 27** (Giza Orion Cairo tutorials): already implicitly covered in zkml.md; not worth a dedicated mention

## Contradictions and Caveats

- The Perplexity response gives a specific SPEX whitepaper arXiv ID (2603.19025) that should be re-verified — the numbering pattern is consistent with 2026 arXiv IDs but the actual paper title should be confirmed before being quoted directly in wiki content.
- Market-cap and fee claims for specific tokens (AI16Z $2B in 10 days, Clanker $8.02M/week) are taken from secondary sources rather than primary on-chain data. Before any wiki page presents these as precise figures, an on-chain verification step is recommended.
- The "8 of 10 top AI tokens down 70%+" claim is aligned with CoinGecko data trajectory but specific percentages should be re-verified against primary data.

## See Also

- [[decentralized-ai]] — The parent AI×crypto framework
- [[defai]] — DeFi + AI narrative
- [[ai-narrative-arc]] — 2024–2026 cycle history
- [[artificial-intelligence]] — AI section hub

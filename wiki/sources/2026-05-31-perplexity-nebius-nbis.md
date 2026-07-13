---
title: "Perplexity Research — Nebius Group (NBIS)"
type: source
created: 2026-05-31
updated: 2026-06-12
status: good
tags: [meta, ai-trading, fundamental-analysis]
aliases: ["Perplexity NBIS Research", "Nebius Group NBIS Source", "NBIS Fundamentals Research"]
source_type: data
source_url: "n/a — Perplexity API research aggregating 7 named sources"
source_author: "Perplexity (sonar model)"
source_date: 2026-05-31
source_file: "raw/articles/2026-04-22-gap-finder-nebius-group-nasdaq-nbis-ai-cloud-infras.md"
confidence: high
claims_count: 13
related:
  - "[[nebius-group]]"
  - "[[coreweave]]"
  - "[[ai-capex-vs-cash-flow-divergence]]"
---

#meta

Perplexity API research dated 2026-05-31 on Nebius Group N.V. (NASDAQ: NBIS), run via `tools/gap_finder.py` in standard mode after the user asked for fundamentals during portfolio research (immediately following SHAZ inquiry). Sources include the Nebius Q1 2026 Shareholder Letter (primary document), SEC 6-K filings, and several aggregator/industry sources. Raw output saved to `raw/articles/2026-04-22-gap-finder-nebius-group-nasdaq-nbis-ai-cloud-infras.md`.

## Why this was researched

User asked about NBIS during AI infrastructure portfolio research, following discussion of CRWV and SHAZ. Wiki had no existing NBIS page. Per the memory rule established earlier in the session (`feedback_always_update_wiki`), useful third-party data should be wired into the wiki by default rather than left as chat-only synthesis. Standard Perplexity mode (~$0.03) was used given that NBIS is a well-covered name and the question was fundamentals, not deep research.

## Underlying sources cited by Perplexity

| # | Source | Type | Relevance |
|---|---|---|---|
| 1 | Plisio — NBIS stocks page | Aggregator | Backlog disclosures, funding-gap commentary |
| 2 | Stocktitan SEC 6-K filing | Primary regulatory filing | Quarterly financial disclosure |
| 3 | Simply Wall St — NBIS valuation | Financial screen | Valuation framework, recent AI infra context |
| 4 | **Nebius Q1 2026 Shareholder Letter (PDF)** | **Primary corporate source** | Q1 2026 financials direct from issuer |
| 5 | MarketBeat — NBIS financials | Aggregator | Historical financials and ratios |
| 6 | Perplexity Finance — NBIS | Aggregator | Cross-reference data |
| 7 | Nebius investor relations | Primary corporate | IR materials |

The Nebius Q1 2026 SHL (source 4) is the highest-confidence document — direct issuer disclosure. The SEC 6-K (source 2) corroborates. Aggregator sources (1, 3, 5, 6) generally reproduce the issuer numbers.

## Key extracted claims with confidence flags

| Claim | Value | Confidence | Source |
|---|---|---|---|
| Rebranded from Yandex N.V. to Nebius Group | **August 2024** | HIGH | [6] Perplexity Finance |
| Q1 2026 AI cloud revenue | **$389.7M** | HIGH | [4] Nebius Q1 2026 SHL, [2] SEC 6-K |
| Q1 2026 group adjusted EBITDA | **Strongly positive** | HIGH | [4] Nebius Q1 2026 SHL |
| Q1 2026 cash balance | **~$9.3B** | HIGH | [4] Nebius Q1 2026 SHL |
| Q1 2026 capex | **~$2.5B (quarterly)** | HIGH | [4] Nebius Q1 2026 SHL |
| 2026 implied annual capex | **~$20–25B** | MEDIUM | [1] Plisio (industry/analyst framing) |
| MSFT + META disclosed backlog | **~$44B combined** | MEDIUM | [1] Plisio citing DCD reporting |
| Mäntsälä Finland data centre | Core European asset | HIGH | [1], [7] |
| Kansas City US data centre buildout | Active expansion | HIGH | [1], [4] |
| NVIDIA strategic partnership / equity stake | Yes | HIGH | Multiple |
| Customer prepayment financing model | Material to balance-sheet strategy | MEDIUM | [1] Plisio analysis |
| Funding gap for 2026 capex | $10-15B+ additional financing implied | MEDIUM | [1] Plisio analysis |
| Yandex restructuring legacy | Persistent governance/headline discount | MEDIUM | [1], [6] |

## Pages this research contributed to

- [[nebius-group]] — new entity page using extracted claims
- Cross-references added to [[coreweave]] as the closest publicly-listed peer

## Caveats

- Q1 2026 numbers from issuer SHL are HIGH confidence as of issue date (2026-05-13 per file metadata). NBIS is volatile — interim updates can change the picture.
- The $44B MSFT + META backlog figure is sourced through Plisio citing Data Center Dynamics reporting; direct issuer confirmation of the combined figure should be verified against the next 6-K.
- The $20-25B 2026 implied capex is analyst/industry framing — not direct issuer guidance. Treat as expectational, not contractual.
- Customer concentration disclosures may understate or overstate; segment-level breakouts in subsequent quarterly filings are the authoritative source.
- **Not investment advice.** The wiki analysis classifies NBIS as a legitimate AI infrastructure business (zero [[ai-microcap-pump-pattern]] signals) but flags standard AI capex divergence risks per [[ai-capex-vs-cash-flow-divergence]].

## Confidence assignment

**Overall: HIGH** for Q1 2026 financial snapshot from issuer SHL; MEDIUM for forward-looking capex/backlog/funding-gap framing which is analyst-derived not issuer-disclosed; MEDIUM for ongoing geopolitical-overhang assessment.

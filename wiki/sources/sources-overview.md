---
title: "Source Summaries"
type: index
created: 2026-04-06
updated: 2026-04-20
status: good
tags: [sources, index]
---

# Source Summaries

LLM-generated summaries of all ingested sources. Each summary extracts key claims, assigns confidence levels, and links to wiki pages that were created or updated.

## All Sources

```dataview
TABLE source_type, source_date, confidence, claims_count
FROM "wiki/sources"
WHERE type = "source"
SORT source_date DESC
```

## Book Sources

```dataview
TABLE source_type, source_author, source_date, confidence, claims_count
FROM "wiki/sources"
WHERE source_type = "book"
SORT source_date ASC
```


## Options Risk Management Sources

- [[recovering-losing-options-positions]] — Compiled research on professional options position recovery and risk management. Covers rolling mechanics (3 roll types, worked examples for short puts, long calls, iron condors), the 21-DTE gamma trap rule, spread conversion, scaling discipline, defined-risk replacements, the 2% sizing rule, portfolio-level Greeks monitoring, and the professional five-pillar playbook (prevention, early defense, active repair, hedging, process). 28 claims from 12 cited references.

## DeFi Sources

- [[2026-04-15-defi-wiki-content-guide]] — Comprehensive DeFi research guide covering fundamentals, glossary, trading strategies, market state (2025-2026), hacks/security, AI x DeFi, Solana DeFi, RWA tokenisation, derivatives/perpetuals, regulation, and risks. 48 claims from 43 cited references.

## Commodities Research Sources

- [[2026-04-14-commodities-research-framework]] — Comprehensive commodities investing and trading research framework covering energy, metals, agriculture, soft commodities, livestock, futures curve dynamics, quantitative strategies (momentum, carry, value), data sources, and macro linkages. 42 claims extracted.

## Prediction Market Sources

- [[polymarket-wiki-guide]] — Comprehensive Polymarket research guide covering founding, technology stack (Polygon, UMA oracle, CLOB), market categories, key milestones (2020-2026), trading strategies, notable traders (Theo $85M, Vitalik $70K), AI/LLM integration, controversies, Kalshi comparison, POLY token, developer ecosystem. 52 claims from 43 cited sources.

## By Confidence

### High Confidence
```dataview
LIST
FROM "wiki/sources"
WHERE confidence = "high"
SORT source_date DESC
```

### Medium Confidence
```dataview
LIST
FROM "wiki/sources"
WHERE confidence = "medium"
SORT source_date DESC
```

### Low Confidence
```dataview
LIST
FROM "wiki/sources"
WHERE confidence = "low"
SORT source_date DESC
```

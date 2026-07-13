---
title: "Perplexity Research — Sharon AI Holdings (SHAZ)"
type: source
created: 2026-05-31
updated: 2026-06-12
status: good
tags: [meta, ai-trading, risk-management]
aliases: ["Perplexity SHAZ Research", "Sharon AI Holdings SHAZ Source", "SHAZ Fundamentals Research"]
source_type: data
source_url: "n/a — Perplexity API research aggregating 7 named sources"
source_author: "Perplexity (sonar model)"
source_date: 2026-05-31
source_file: "raw/articles/2026-04-22-gap-finder-sharon-ai-holdings-nasdaq-ticker-shaz-co.md"
confidence: medium
claims_count: 12
related:
  - "[[sharon-ai-holdings]]"
  - "[[ai-microcap-pump-pattern]]"
---

#meta

Perplexity API research dated 2026-05-31 on Sharon AI Holdings (NASDAQ: SHAZ), run via `tools/gap_finder.py` in standard mode after the user requested a fundamentals lookup on the ticker during portfolio analysis. The query returned 7 named sources and the model's synthesis. Raw output saved to `raw/articles/2026-04-22-gap-finder-sharon-ai-holdings-nasdaq-ticker-shaz-co.md` (note: gap_finder filename pattern uses an earlier date stamp — content is dated to query date).

## Why this was researched

User asked about SHAZ during portfolio analysis on 2026-05-31. The name was unfamiliar to the model from training data alone, and the assistant declined to confabulate fundamentals on a real publicly-traded stock the user might buy with SMSF money. Perplexity standard scan was used to surface verifiable third-party data before any analysis was given.

## Underlying sources cited by Perplexity

| # | Source | Type | Relevance |
|---|---|---|---|
| 1 | Simply Wall St — SHAZ profile | Financial screen | Revenue, cash runway, debt/equity |
| 2 | Morningstar — SHAZ quote | Financial database | Price history, fair value estimate |
| 3 | MarketChameleon — SHAZ overview | Options/volatility data | IV, options activity |
| 4 | Robinhood — SHAZ page | Retail broker page | Founding date, basic description |
| 5 | AlphaSpread — SHAZ analyst estimates | Aggregator | Forward estimates |
| 6 | TradingView — SHAZ symbol page | Charting/data | Price history |
| 7 | **RedChip** — SHAZ stocks page | **Paid IR coverage** | Marketing/promotional narrative |

The presence of RedChip in the source set is itself a material data point — see [[ai-microcap-pump-pattern]] for why paid IR coverage is a pump-pattern signal.

## Key extracted claims with confidence flags

| Claim | Value | Confidence | Source |
|---|---|---|---|
| Company founded as public entity | **2024-12-30** | HIGH | [4] Robinhood |
| TTM revenue | **~$1.54M** | HIGH | [1] Simply Wall St |
| Market cap | **~$1.22B** | HIGH | [1] Simply Wall St |
| Implied revenue multiple | **~790x** | HIGH | Calculated |
| Cash runway | **< 1 year** | HIGH | [1] Simply Wall St |
| Debt/equity ratio | **224.9%** | HIGH | [1] Simply Wall St |
| 52-week low | **~$0.99** | HIGH | [2], [4] |
| Late May 2026 price | **High-$60s to mid-$70s** | HIGH | [2] Morningstar |
| Morningstar fair value gap | **Substantial premium to FV** | MEDIUM | [2] Morningstar — methodology not fully exposed |
| Business positioning | **Neocloud / GPU-as-a-Service / Sovereign AI Australia** | MEDIUM | [2], [3], [7] — marketing-claim category, not verified |
| Customer base | Unspecified ("AI labs," "enterprise customers") | LOW | [7] promotional source |
| Sell-side coverage | None from major banks | MEDIUM | absence of mention across sources |

## Pages this research contributed to

- [[sharon-ai-holdings]] — new entity page using extracted claims
- [[ai-microcap-pump-pattern]] — new concept page; SHAZ used as worked instance

## Caveats

- Perplexity standard mode was used (not deep mode — deep failed earlier in the session). Source recall is more limited than deep mode would provide.
- RedChip is a paid IR firm; their content is promotional, not independent research. Sources [1] [2] are higher-confidence financial data; source [7] is treated as marketing material.
- Numbers are point-in-time as of 2026-05-31; SHAZ is a volatile microcap and any specific number may be stale within weeks.
- **Not investment advice**. The wiki conclusion is that SHAZ fits the pump pattern at high confidence; that pattern conclusion is the wiki's analytical position, not a sourced claim per se.

## Confidence assignment

**Overall: MEDIUM**

- Financial data points (revenue, debt, runway, price history): HIGH — sourced from established financial databases
- Pattern classification (pump-pattern instance): MEDIUM — synthesis from the data points using the [[ai-microcap-pump-pattern]] framework, not a third-party claim
- Forward-looking outcome distribution: based on historical pattern base rates, not specific to SHAZ — treat as framework expectations, not company-specific forecasts

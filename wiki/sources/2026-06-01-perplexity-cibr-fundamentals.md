---
title: "Perplexity Research — CIBR (First Trust Nasdaq Cybersecurity ETF)"
type: source
created: 2026-06-01
updated: 2026-06-12
status: good
tags: [meta, source, ai-trading, stocks]
aliases: ["CIBR Perplexity Research", "CIBR Fundamentals Research"]
source_type: data
source_url: "n/a — Perplexity API research aggregating 8 named sources"
source_author: "Perplexity (sonar model)"
source_date: 2026-06-01
source_file: "raw/articles/2026-04-22-gap-finder-cibr-first-trust-nasdaq-cybersecurity-et.md"
confidence: medium
claims_count: 10
related:
  - "[[cibr-first-trust-nasdaq-cybersecurity-etf]]"
  - "[[mythos-capability-overhang-vol]]"
  - "[[2026-04-07-claude-mythos-project-glasswing]]"
---

#meta

Perplexity API research dated 2026-06-01 on CIBR (First Trust Nasdaq Cybersecurity ETF), run via `tools/gap_finder.py` during portfolio research after assistant identified CIBR as the wiki-recommended basket vehicle for Mythos public-rollout positive scenario but had no dedicated wiki page on the ETF. Per `feedback_always_update_wiki` memory rule.

## Why this was researched

User asked for "more info on CIBR" following the revised Mythos rollout analysis. The wiki had no CIBR page; the closest content was a passing mention in [[mythos-capability-overhang-vol]] and [[glasswing-partner-long-basket]]. Perplexity standard scan was used to surface current fundamentals before writing the new entity page.

## Underlying sources cited by Perplexity

| # | Source | Type | Relevance |
|---|---|---|---|
| 1 | TradingView — CIBR holdings page | Aggregator | Top-holding snapshot with weights |
| 2 | **First Trust — official CIBR holdings page** | **Issuer primary** | **Authoritative holdings + weights** |
| 3 | Zacks ETF — CIBR holding | Aggregator | Performance and ratio statistics |
| 4 | 247WallSt — Cybersecurity as 2026 resilience theme | Industry commentary | Macro narrative context |
| 5 | Cybersecurity Ventures — CIBR as 2026 investment | Industry advocacy | Bull-case narrative |
| 6 | First Trust — CIBR holdings (second URL) | Issuer primary | Cross-reference |
| 7 | Morningstar — CIBR portfolio | Financial database | Portfolio statistics |
| 8 | SumGrowth — CIBR profile | Aggregator | Cross-reference |

The First Trust sources (2, 6) are the authoritative holdings sources. Morningstar (7) provides standardised portfolio statistics. 247WallSt (4) and Cybersecurity Ventures (5) are commentary/narrative sources — useful for context but lower confidence than direct issuer data.

## Key extracted claims with confidence flags

| Claim | Confidence | Source |
|---|---|---|
| CIBR has materially larger AUM than HACK, BUG, WCBR competitors | HIGH | [4] [5] commentary |
| Top holdings include PANW, CRWD, FTNT, CSCO, ZS, NET, CYBR, OKTA, S, HCP, LDOS, AKAM, Thales | HIGH | [1] [2] [6] First Trust + TradingView |
| Construction is modified market-cap weighted (single-name caps applied) | HIGH | [2] First Trust methodology |
| Expense ratio ~0.59% | HIGH | Standard for thematic ETF; consistent with First Trust products |
| Inception July 2015 | HIGH | Public record |
| Holdings broadened beyond pure software (networking, IT services, defense-adjacent included) | HIGH | [1] [2] |
| Cybersecurity framed as 2026 resilience theme alongside defense / energy | MEDIUM | [4] commentary |
| Performance dispersion among cyber ETFs widened in 2026 | MEDIUM | [4] commentary |
| AI-security spend narrative supporting PANW, CRWD, NET specifically | MEDIUM-HIGH | [5] commentary + general 2026 enterprise software discussion |
| Holdings list changed meaningfully between Feb-May 2026 | MEDIUM | [2] [6] First Trust update logs |

## Pages this research contributed to

- [[cibr-first-trust-nasdaq-cybersecurity-etf]] — new entity page with full fundamentals, holdings table, Mythos relevance, SMSF fit analysis

## Caveats

- Specific dollar AUM not directly extracted from sources — characterised as "materially larger" qualitatively per industry commentary
- Holdings weights drift quarterly; specific weights shown should be considered representative not current as of any particular date
- Expense ratio confirmed at category level (thematic ETF range) but not pulled from current factsheet
- Performance numbers not extracted — should be verified against current First Trust factsheet before any sized position
- **Not investment advice.** The wiki documents CIBR as a basket vehicle; specific position-taking is downstream

## Confidence assignment

**Overall: MEDIUM-HIGH** — High confidence on structural facts (issuer, index, construction, typical holdings) from First Trust primary; medium confidence on narrative claims (resilience theme, AI-security spend) which are commentary not primary; specific weights and AUM should be verified against current First Trust factsheet before any sized position.

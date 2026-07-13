---
title: "Narratives Schema"
type: concept
created: 2026-05-08
updated: 2026-05-08
status: good
tags: [narratives, schema, conventions]
aliases: ["narratives-schema"]
---

# Narrative frontmatter schema

Every file under `wiki/narratives/` (except `_index.md`, `_schema.md`, and
`_log.md`) is a narrative. Filename is the slug; the bot's `NarrativeReader`
keys narratives by filename stem.

```yaml
---
title: "Salesforce Workforce Cut → AI-Margin Expansion"
type: narrative
created: 2026-05-08
updated: 2026-05-08
status: active                   # proposed | active | played-out | invalidated
side: long                       # long | short | pair | neutral
tickers_primary: [CRM]           # the names this thesis directly trades
tickers_secondary: [NOW, WDAY]   # adjacent / read-across
tickers_hedge: [SPY, XLK]        # used for sector / beta neutralization
time_horizon_days: 90            # expected catalyst window
catalysts:                       # explicit, dated where possible
  - "2026-05-21 — Q1 earnings"
  - "2026-07-15 — guidance update"
sources:                         # URLs, wiki pages, news refs
  - "https://www.example.com/crm-layoffs"
  - "[[ai-capex]]"
  - "[[saas-margin-pressure]]"
invalidation:                    # what kills this thesis
  - "Layoffs reversed within 60 days"
  - "Operating margin guide cut"
risk_reward_target: "3:1"        # high-level — actual signal R:R is per-trade
summary: "Salesforce just laid off 20% of staff. If revenue holds, margins jump and the stock re-rates. Long calls into next earnings."
created_by: "manual"             # manual | slash-command | auto-macro-tilt
---

# Salesforce Workforce Cut → AI-Margin Expansion

[Body — full thesis. What's happening, why it matters, what proves it,
what disproves it. Cite wiki pages and external sources liberally.
The bot will display the body verbatim on the /narratives detail page.]

## Why now

[The dated catalyst — what made this an opportunity *this week*.]

## Expression

[Which structures (long calls? credit spreads? pair?) and on which tickers.
Short-circuits Stage 5 of the playbook by suggesting structures up front;
the bot's pipeline will still confirm with its own R:R + sizing gates.]

## Risks

[Known unknowns. Macro overlays that could swamp the thesis. Crowded-trade
risk. Etc.]

## Signals generated

[Auto-populated by the bot. List of Signal IDs with status + P&L. Append-only
log; never edited by hand.]
```

## The `summary` field — write this for a non-trader

The dashboard renders `summary` verbatim on each narrative card. Treat it as
the elevator pitch for someone who doesn't know what a "channel" or
"compression" is. **Rules:**

1. **Plain English.** No "reinforcing channels", "asymmetric setup", "secular
   tailwinds", "mispriced vol". Use words a non-trader uses.
2. **2-3 short sentences.** What is happening. Why it matters for the price.
   What we're doing about it.
3. **Stand-alone.** Never end with a colon and a list. The card doesn't show
   the body.
4. **Concrete.** Name the company / event / number. "Salesforce laid off 20%"
   beats "headcount-driven margin expansion".

Good: `"European banks earn most of their profit from interest spreads. The
ECB is cutting rates faster than the Fed, which crushes those spreads. We're
buying puts on the biggest banks until earnings reflect it."`

Bad: `"Three reinforcing channels compress European bank earnings:"` —
jargon, lists nothing, mid-sentence.

If `summary` is missing, the dashboard falls back to extracting the first
paragraph under `## Thesis` → `## Headline` → first prose paragraph. That
fallback is for legacy narratives only; new narratives must set `summary`.

## Required fields

- `title`, `type: narrative`, `created`, `updated`, `status`, `side`,
  `tickers_primary`, `time_horizon_days`, `created_by`, `summary`.

## Optional fields

- `tickers_secondary`, `tickers_hedge` (default `[]`).
- `catalysts`, `sources`, `invalidation` (default `[]`).
- `risk_reward_target` (default empty).

## Status values

- `proposed` — draft only, no signals generated yet.
- `active` — bot is allowed to generate signals against this narrative.
- `played-out` — close-out narrative. Append realized P&L to `_log.md`.
- `invalidated` — thesis disproved. Append reason to `_log.md`.

The bot reads `status` at boot and on hot-reload. Only narratives with
`status: active` bias the candidate scan.

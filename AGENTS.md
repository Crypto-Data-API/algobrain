# AlgoBrain — LLM Schema

> This file governs how coding agents (Codex, etc.) maintain the AlgoBrain wiki.
> Read this file in full before any wiki operation.

## Scope

A crypto-trading-strategy knowledge base. In scope: **crypto, blockchain, DeFi, trading, algorithms, markets** — plus macro context (FX, rates, commodities, market history) and AI/ML knowledge that feed crypto strategy development. Out of scope: stock-picking, equity fundamentals, single-name equity coverage. Do not add equity-specific content.

## Architecture

Two layers:

1. **`wiki/`** — LLM-generated markdown. Summaries, entity pages, concept pages, strategy pages, comparisons, synthesis. The LLM owns this layer entirely.
2. **`AGENTS.md`** (this file) — The schema. Defines structure, conventions, and workflows. `CLAUDE.md` is the same schema addressed to Claude Code; keep the two in sync.

This is a standalone Obsidian vault (the vault root is this repository). Page templates live in `templates/`. Attachments go in `attachments/`.

## Data Layer: CryptoDataAPI

**[[cryptodataapi|CryptoDataAPI]]** (`https://cryptodataapi.com`, auth via `X-API-Key` header) is the canonical market-data source for this wiki — 190+ REST endpoints across coins, market data (Binance spot), derivatives (funding/OI/long-short), Hyperliquid (perps, candles, L2 book, trader intelligence), liquidity depth, volatility/market/meme/event/security/policy regimes, HMM quant probabilities, sentiment (fear & greed, stablecoins), market intelligence (ETF flows, liquidations, options, Coinbase premium), on-chain (exchange flows, miner metrics, MVRV, whale scores), DEX/memecoins, NFTs, and a backtesting archive (klines, funding, liquidations, Parquet since 2020).

- Hub page: `wiki/data-sources/cryptodataapi.md`; per-category pages: `wiki/data-sources/cryptodataapi-*.md`
- Pages describing data an endpoint serves carry a **`## Getting the Data (CryptoDataAPI)`** section (live endpoint + historical endpoint + curl example), inserted before `## Related`
- When creating or upgrading such a page, add that section and link the relevant `cryptodataapi-*` category page
- Strategy and indicator pages end that section with a **`### AI agent workflow`** sub-block: 3-6 *page-specific* bullets (signal endpoints, regime gate, matching backtesting-archive endpoint, execution tips) linking [[cryptodataapi-mcp]]. MCP setup boilerplate (connect commands, key creation, x402) lives ONLY on `wiki/data-sources/cryptodataapi-mcp.md` — never duplicate it onto content pages
- The local wiki MCP server (`tools/mcp_server.py`) attaches a `data_instruction` block to every `wiki_search` response pointing agents at CryptoDataAPI and [[cryptodataapi-mcp]] — keep this intact when modifying the server
- Never invent endpoint paths — verify against https://cryptodataapi.com/api/docs

## Top-Level Wiki Sections

- `wiki/markets/` — markets and instruments (`crypto/` is the core; `commodities/`, `forex/`, `bonds/` are macro context)
- `wiki/strategies/` — catalog of strategies (see also `regime-matrix.md` and `live-journal.md`)
- `wiki/concepts/` — foundational concepts including `risk-management/`, `portfolio-theory/`, `indicators/`, `market-microstructure/`, `behavioral-finance/`, `backtesting/`, `anomalies/`, `metrics/` (on-chain), `tax/` (AU trader tax)
- `wiki/strategy-development/` — methodology for *producing* strategies (edge taxonomy, hypothesis workflow, research checklist, overfitting detection, failure modes)
- `wiki/data-sources/` — catalog of data providers; CryptoDataAPI is the canonical layer
- `wiki/entities/` — exchanges, protocols, traders, funds, companies (crypto-centric only), regulators
- `wiki/history/` — crashes, notable events (crypto + macro/trading history)
- `wiki/crypto-narratives/` — backtester-ready narrative impact catalog (JSON in `catalog/`)
- `wiki/narratives/` — active trade theses (uses `_index.md`/`_log.md`/`_schema.md` control files)
- `wiki/news/`, `wiki/sources/`, `wiki/education/`, `wiki/comparisons/`, `wiki/ai-trading/`, `wiki/artificial-intelligence/`
- `wiki/index.md`, `wiki/log.md`, `wiki/overview.md`

## Page Naming Conventions

- **Filenames**: lowercase, hyphen-separated. Example: `moving-average-convergence-divergence.md`
- **No abbreviations in filenames** unless the abbreviation IS the canonical name (e.g., `rsi.md`, `macd.md`)
- **Category overview pages**: named `<category>-overview.md` (e.g., `markets-overview.md`, `strategies-overview.md`). NEVER use `_index.md` — it shows as "_index" in Obsidian's graph view instead of the topic name (exception: the self-contained `wiki/narratives/` subsystem keeps its `_index.md`/`_log.md`/`_schema.md` trio)
- **Source summaries**: `wiki/sources/<source-id>.md`
- **Disambiguation**: if two concepts share a name, add a parenthetical: `momentum-(physics).md` vs `momentum-(indicator).md`

## Frontmatter Schema

Every wiki page MUST have YAML frontmatter. The schema varies by page type:

### Common Fields (all pages)

```yaml
---
title: "Human-Readable Title"
type: concept | strategy | entity | market | comparison | news | source | index | overview
created: 2026-04-06
updated: 2026-04-06
status: stub | draft | review | good | excellent
tags: [tag1, tag2, tag3]
aliases: ["Alternative Name", "Abbreviation"]
related: ["[[page-one]]", "[[page-two]]"]
---
```

### Field Definitions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | yes | Display title |
| `type` | enum | yes | Page type — determines template and Dataview queries |
| `created` | date | yes | Date page was first created (YYYY-MM-DD) |
| `updated` | date | yes | Date page was last modified (YYYY-MM-DD) |
| `status` | enum | yes | Maturity level of the page |
| `tags` | list | yes | Flat tag list for filtering |
| `aliases` | list | no | Alternative names (enables Obsidian alias search) |
| `related` | list | no | Explicit wikilinks to related pages |

### Status Levels

| Status | Meaning |
|--------|---------|
| `stub` | Placeholder — title and maybe one sentence |
| `draft` | Has content but incomplete or unverified |
| `review` | Content is present, needs fact-checking or polish |
| `good` | Solid page, sourced, reviewed |
| `excellent` | Comprehensive, multi-sourced, cross-referenced |

### Extended Fields by Page Type

**Source summary** (`type: source`):
```yaml
source_type: article | pdf | video | tweet | screenshot | data | book
source_url: "https://..."
source_author: "Author Name"
source_date: 2026-04-01
confidence: high | medium | low
claims_count: 5
```

**Strategy page** (`type: strategy`):
```yaml
strategy_type: technical | fundamental | quantitative | algorithmic | hybrid
timeframe: scalp | intraday | swing | position | long-term
markets: [crypto]
complexity: beginner | intermediate | advanced
backtest_status: untested | naive-backtested | walk-forward-validated | cost-corrected | deflated-sharpe-significant | paper-traded | pilot | live | paused | retired

# Edge characterization (see [[edge-taxonomy]])
edge_source: [behavioral, structural, informational, analytical, latency, risk-bearing]  # one or more
edge_mechanism: "one-sentence explanation of who is on the other side and why"

# Data and infrastructure requirements
data_required: [ohlcv-daily, options-chain, funding-rates, on-chain-flows]
min_capital_usd: 5000        # smallest sensible deployment size
capacity_usd: 10000000       # estimated capacity before market impact dominates
crowding_risk: low | medium | high

# Performance expectations
expected_sharpe: 0.8           # net of costs
expected_max_drawdown: 0.15
breakeven_cost_bps: 30         # bps round-trip the strategy can absorb

# Decay history
decay_evidence: "link to paper or note showing edge decay since X year"

# Lifecycle (only if deployed — see [[live-journal]])
deploy_date: 2026-04-10
capital_allocation: "5% of book"
kill_criteria: |
  - drawdown > 20%
  - rolling 6-month Sharpe < 0
last_review: 2026-04-10
next_review: 2026-05-10
```

**Strategy page sections** — every strategy page should follow this structure (in addition to standard frontmatter and lead paragraph):

1. **Lead paragraph** — what the strategy is, in 2-3 sentences
2. **Edge source** — which of the five edge categories (see [[edge-taxonomy]]) and why
3. **Why this edge exists** — the mechanism; who is on the other side; why they keep losing
4. **Null hypothesis** — what would the strategy look like under random / no-edge conditions?
5. **Rules** — entry, exit, position sizing
6. **Implementation pseudocode** — a code-block sketch of the actual decision logic
7. **Indicators / data used** — include CryptoDataAPI endpoints where applicable
8. **Example trade**
9. **Performance characteristics** — with realistic cost overlay, not naive backtest
10. **Capacity limits** — at what AUM does market impact dominate?
11. **What kills this strategy** — the most likely failure modes from [[failure-modes]]
12. **Kill criteria** — numerical conditions for retiring it (see [[when-to-retire-a-strategy]])
13. **Advantages**
14. **Disadvantages**
15. **Sources**
16. **Related** — wikilinks

**Entity page** (`type: entity`):
```yaml
entity_type: person | company | exchange | fund | regulator | protocol
founded: 2009
headquarters: "New York, USA"
website: "https://..."
```

**News event** (`type: news`):
```yaml
event_date: 2026-04-01
markets_affected: [crypto]
impact: high | medium | low
verified: true | false
sources_count: 3
```

**Concept page** (`type: concept`):
```yaml
domain: [risk-management, technical-analysis, market-microstructure]
prerequisites: ["[[another-concept]]"]
difficulty: beginner | intermediate | advanced
```

**Comparison page** (`type: comparison`):
```yaml
subjects: ["[[subject-a]]", "[[subject-b]]"]
comparison_dimensions: [cost, speed, features]
```

## Wikilink Conventions

- **Always use wikilinks** for cross-references: `[[page-name]]` or `[[page-name|Display Text]]`
- **Link generously** — if a concept, entity, strategy, or market is mentioned and has (or should have) a page, link it
- **Create forward links** — it is OK to link to pages that do not yet exist. They appear as unresolved links in Obsidian's graph view, signaling gaps to fill
- **Wikilink format**: `[[filename-without-extension]]` — NEVER include `.md` extension or folder paths
- **Aliases in links**: use `[[rsi|RSI]]` if the display text differs from the filename
- **Section links**: use `[[page-name#Section Heading]]` for deep links
- **Do NOT link common English words** — only link trading/finance terms that warrant their own page

## Ingest Workflow

When a new source is provided for ingestion, follow these steps IN ORDER:

### Step 1: Create Source Summary
1. Create `wiki/sources/<source-id>.md` using the source-summary template (`templates/source-summary.md`)
2. Extract all factual claims, data points, and arguments
3. Assign a confidence level (high/medium/low) based on:
   - **High**: Peer-reviewed research, official data, well-sourced journalism
   - **Medium**: Expert opinion, reputable blog, unverified but plausible
   - **Low**: Social media, anonymous source, speculative
4. List all claims with inline confidence markers: `[HIGH]`, `[MEDIUM]`, `[LOW]`
5. Identify all entities, concepts, strategies, and markets mentioned

### Step 2: Update or Create Wiki Pages
For each entity, concept, strategy, or market identified:
1. If the page exists: ADD new information under the appropriate section, cite the source with `(Source: [[source-id]])`
2. If the page does NOT exist: CREATE it using the appropriate template, populate with what the source provides, set status to `stub` or `draft`
3. Add wikilinks between the source summary and all pages it contributed to
4. Check scope first — do not create equity-specific pages

### Step 3: Handle Contradictions
When new information contradicts existing wiki content:
1. Do NOT silently overwrite. Add a `## Contradictions` section (or append to it)
2. Present both claims with their sources and confidence levels:
   ```
   > **Claim A** (Source: [[source-1]], confidence: HIGH): "Statement A"
   > **Claim B** (Source: [[source-2]], confidence: MEDIUM): "Statement B"
   > **Resolution**: Pending further evidence. Claim A is currently favored due to higher source confidence.
   ```
3. If one claim clearly supersedes (newer data, higher confidence, more sources), note this but preserve the history

### Step 4: Update Indexes and Log
1. Add an entry to `wiki/log.md`:
   ```
   ## 2026-04-06 14:30 — Ingested: "Bitcoin ETF Approval Analysis"
   - Source: [[2026-04-06-bitcoin-etf-approval-analysis]]
   - Type: article
   - Pages created: [[bitcoin-etf]], [[sec]]
   - Pages updated: [[bitcoin]], [[etf]]
   - Claims: 5 (3 HIGH, 2 MEDIUM)
   ```
2. Update `wiki/index.md` if new pages were created
3. Update `wiki/sources/sources-overview.md` with the new source entry

### Step 5: Update Overview (periodically)
After every 5-10 ingestions, or when significant new themes emerge:
1. Rewrite `wiki/overview.md` to reflect the current state of knowledge
2. Identify emerging themes, knowledge gaps, and areas of contradiction

## Query Workflow

When asked to answer a question using the wiki:

1. **Search** wiki pages (filename and content search)
2. **Read** the most relevant pages (aim for 3-7 sources)
3. **Synthesize** an answer, citing wiki pages with wikilinks
4. **Identify gaps** — if the wiki lacks information to fully answer, say so explicitly
5. **Suggest ingestion** — recommend specific sources to fill identified gaps
6. Do NOT fabricate information that is not in the wiki. The wiki is the ground truth.

## Lint Workflow

Periodically check wiki health:

1. **Frontmatter completeness**: every page has all required fields
2. **Broken wikilinks**: links to pages that do not exist (flag pages with >5 broken links)
3. **Orphan pages**: pages with no inbound links
4. **Stale pages**: pages not updated in >90 days with status below `good`
5. **Missing source citations**: wiki pages with no `(Source: [[...]])` references
6. **Empty pages**: pages with no content beyond frontmatter
7. **Index sync**: verify `wiki/index.md` lists all major pages that exist
8. **Tag consistency**: flag non-standard tags
9. **Duplicate content**: flag pages with very similar titles or content
10. **Scope drift**: flag equity-specific pages that violate the crypto scope

### Approved Tags

```
# Markets
crypto, forex, commodities, options, futures, bonds, defi, nft

# Strategy types
technical-analysis, fundamental-analysis, quantitative, algorithmic,
day-trading, swing-trading, position-trading, scalping, arbitrage,
mean-reversion, trend-following, momentum, breakout, pairs-trading

# Concepts
risk-management, portfolio-theory, market-microstructure, order-types,
indicators, behavioral-finance, valuation, leverage, margin, derivatives,
volatility, correlation, liquidity, slippage, on-chain, funding-rate,
perpetual-futures, liquidations, open-interest

# Asset-specific
bitcoin, ethereum, altcoins, stablecoins, memecoins, gold, oil, treasuries

# Meta
history, news, education, book, person, company, exchange, regulation,
ai-trading, machine-learning, backtesting, data-provider, market-regime,
regime-detection, methodology, event-driven, hyperliquid

# Adopted 2026-07-19 (tag audit)
anomalies, australia, bittensor, combinations, crashes, execution, exploits, gamefi, hedge-funds, hedging, macro, market-making, meta-strategy, narrative-impact, options-structures, privacy, python, real-world-assets, security, sniping, solana, statistics, strategy-development, tax, trading-bots, volume
```

## Content Guidelines

### Tone and Style
- **Encyclopedic but accessible** — write like a well-sourced wiki, not a textbook
- **Concrete over abstract** — include examples, numbers, dates
- **Source everything** — every factual claim should trace back to a source page
- **No opinion without attribution** — "X is the best strategy" must be attributed to a source

### Page Structure Convention
Every non-index page should follow this general structure:
1. **Frontmatter** (YAML)
2. **Lead paragraph** — 2-3 sentence definition/summary (no heading needed)
3. **Overview / Description** — deeper explanation
4. **Sections** specific to the page type (see templates)
5. **Getting the Data (CryptoDataAPI)** — where the page maps to an API endpoint
6. **Related** — wikilinks to related pages
7. **Sources** — list of source summaries that contributed to this page

### Dataview Integration
Category overview pages should include Dataview queries for auto-listing:
```dataview
TABLE status, updated
FROM "wiki/markets/crypto"
WHERE type != "index"
SORT updated DESC
```

## Rules for the LLM

1. **ALWAYS update `wiki/log.md`** after any wiki operation
2. **ALWAYS add frontmatter** to every new page
3. **ALWAYS use wikilinks** for cross-references
4. **NEVER fabricate sources** — only reference sources that exist
5. **NEVER silently overwrite** — when updating, preserve existing content and add new information
6. **Cite sources inline** using `(Source: [[source-id]])` format
7. **Update `wiki/index.md`** when creating new pages
8. **Maintain tag consistency** — use only approved tags (or propose new ones in the log)
9. **Handle contradictions explicitly** — see the contradiction workflow above
10. **Prefer specificity** — "BTC dropped 15% on 2024-03-05" over "BTC dropped significantly"
11. **Date all claims** — include when the information was true/published
12. **Stay in scope** — crypto/trading/macro/AI only; no equity-specific content
13. **Never invent CryptoDataAPI endpoints** — verify against the live docs before documenting

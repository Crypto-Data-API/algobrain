# Trading Wiki — LLM Schema

> This file governs how the LLM (Claude Code) maintains the trading wiki.
> Read this file in full before any wiki operation.

## Architecture

Three layers:

1. **Cloudflare R2** (`r2://trader-wiki/`) — Immutable source documents stored in Cloudflare R2. The LLM reads but NEVER modifies these after upload. Use `python tools/raw_sync.py` to upload/download.
2. **`wiki/`** — LLM-generated markdown. Summaries, entity pages, concept pages, comparisons, synthesis. The LLM owns this layer entirely.
3. **`CLAUDE.md`** (this file) — The schema. Defines structure, conventions, and workflows.

> **Note:** `raw/` is a local cache directory (gitignored). Files are fetched from R2 on demand via `python tools/raw_sync.py download <key>`. The master index of all raw sources is at `wiki/sources/raw-source-index.md`.

## Top-Level Wiki Sections

- `wiki/markets/` — markets and instruments
- `wiki/strategies/` — catalog of strategies (see also `regime-matrix.md` and `live-journal.md`)
- `wiki/concepts/` — foundational concepts including `risk-management/`, `portfolio-theory/`, `indicators/`, `market-microstructure/`, `behavioral-finance/`, `backtesting/`, `anomalies/`
- `wiki/strategy-development/` — methodology for *producing* strategies (edge taxonomy, hypothesis workflow, research checklist, overfitting detection, failure modes, ITPM playbook)
- `wiki/data-sources/` — catalog of free, paid, alternative, crypto, options, macro, news data providers
- `wiki/entities/` — companies, exchanges, traders, regulators
- `wiki/history/` — crashes, notable events
- `wiki/news/`, `wiki/sources/`, `wiki/education/`, `wiki/comparisons/`, `wiki/ai-trading/`, `wiki/artificial-intelligence/`, `wiki/alfred/`
- `wiki/index.md`, `wiki/log.md`, `wiki/overview.md`

## Page Naming Conventions

- **Filenames**: lowercase, hyphen-separated. Example: `moving-average-convergence-divergence.md`
- **No abbreviations in filenames** unless the abbreviation IS the canonical name (e.g., `rsi.md`, `macd.md`)
- **Category overview pages**: named `<category>-overview.md` (e.g., `markets-overview.md`, `strategies-overview.md`). NEVER use `_index.md` — it shows as "_index" in Obsidian's graph view instead of the topic name
- **Source summaries**: `wiki/sources/<source-id>.md` where `<source-id>` matches the raw source slug
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
source_file: "r2://trader-wiki/articles/some-article.md"
confidence: high | medium | low
claims_count: 5
```

**Strategy page** (`type: strategy`):
```yaml
strategy_type: technical | fundamental | quantitative | algorithmic | hybrid
timeframe: scalp | intraday | swing | position | long-term
markets: [crypto, stocks]
complexity: beginner | intermediate | advanced
backtest_status: untested | naive-backtested | walk-forward-validated | cost-corrected | deflated-sharpe-significant | paper-traded | pilot | live | paused | retired

# Edge characterization (see [[edge-taxonomy]])
edge_source: [behavioral, structural, informational, analytical, latency, risk-bearing]  # one or more
edge_mechanism: "one-sentence explanation of who is on the other side and why"

# Data and infrastructure requirements
data_required: [ohlcv-daily, options-chain, funding-rates, fundamentals-pit]
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
7. **Indicators / data used**
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
markets_affected: [crypto, stocks]
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

### Step 1: Receive and Store Raw Source
1. Determine the source type (article, pdf, video, tweet, screenshot, data, book)
2. Save the raw source locally to `raw/<type>/` (this directory is gitignored — it's a local cache)
3. Name the file with a descriptive slug: `articles/2026-04-06-bitcoin-etf-approval-analysis.md`
4. For web articles: save as markdown with the original URL in a comment at the top
5. For screenshots: save the image file and create a companion `.md` file with OCR/description
6. Upload to Cloudflare R2: `python tools/raw_sync.py upload raw/<type>/<filename>`
7. NEVER modify raw sources after upload to R2

### Step 2: Create Source Summary
1. Create `wiki/sources/<source-id>.md` using the source-summary template
2. Extract all factual claims, data points, and arguments
3. Assign a confidence level (high/medium/low) based on:
   - **High**: Peer-reviewed research, official data, well-sourced journalism
   - **Medium**: Expert opinion, reputable blog, unverified but plausible
   - **Low**: Social media, anonymous source, speculative
4. List all claims with inline confidence markers: `[HIGH]`, `[MEDIUM]`, `[LOW]`
5. Identify all entities, concepts, strategies, and markets mentioned

### Step 3: Update or Create Wiki Pages
For each entity, concept, strategy, or market identified:
1. If the page exists: ADD new information under the appropriate section, cite the source with `(Source: [[source-id]])`
2. If the page does NOT exist: CREATE it using the appropriate template, populate with what the source provides, set status to `stub` or `draft`
3. Add wikilinks between the source summary and all pages it contributed to

### Step 4: Handle Contradictions
When new information contradicts existing wiki content:
1. Do NOT silently overwrite. Add a `## Contradictions` section (or append to it)
2. Present both claims with their sources and confidence levels:
   ```
   > **Claim A** (Source: [[source-1]], confidence: HIGH): "Statement A"
   > **Claim B** (Source: [[source-2]], confidence: MEDIUM): "Statement B"
   > **Resolution**: Pending further evidence. Claim A is currently favored due to higher source confidence.
   ```
3. If one claim clearly supersedes (newer data, higher confidence, more sources), note this but preserve the history

### Step 5: Update Indexes and Log
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
4. Update `wiki/sources/raw-source-index.md` with the R2 key for the raw file

### Step 6: Update Overview (periodically)
After every 5-10 ingestions, or when significant new themes emerge:
1. Rewrite `wiki/overview.md` to reflect the current state of knowledge
2. Identify emerging themes, knowledge gaps, and areas of contradiction

## Query Workflow

When asked to answer a question using the wiki:

1. **Search** wiki pages using `tools/search.py` or MCP search tool
2. **Read** the most relevant pages (aim for 3-7 sources)
3. **Synthesize** an answer, citing wiki pages with wikilinks
4. **Identify gaps** — if the wiki lacks information to fully answer, say so explicitly
5. **Suggest ingestion** — recommend specific sources to fill identified gaps
6. Do NOT fabricate information that is not in the wiki. The wiki is the ground truth.

## Gap Analysis Workflow

When the user says **"gap analysis: TOPIC"** (e.g., "gap analysis: options trading"), run this workflow:

### Step 1: Find Gaps
```bash
python tools/gap_finder.py --topic "TOPIC" --deep
```
This uses Perplexity deep research (~$1) to compare wiki coverage against real-world knowledge. Uses `--deep` by default for thorough results. For cheaper/faster runs, drop `--deep` (~$0.03).

The tool:
- Auto-finds related wiki pages for the topic
- Scans for unresolved wikilinks and thin pages (internal gaps)
- Asks Perplexity what entities, concepts, strategies, and data sources are missing (external gaps)
- Saves results to `raw/articles/`

### Step 2: Review & Prioritize
Present the results to the user. Categorize gaps:
- **Missing pages** — entities/concepts that should have their own wiki page
- **Thin pages** — existing stubs/drafts that need expansion
- **False positives** — skip generic terms, celebrities, and things not relevant to trading

### Step 3: Fill Gaps
Create new pages and upgrade existing ones. Use parallel agents for speed. Rules:
- All new pages get `status: draft` with proper YAML frontmatter
- Focus on **trading-relevant** content: strategies, risk frameworks, actionable data
- Link generously with wikilinks
- Cross-reference between new pages
- Update `wiki/index.md` and `wiki/log.md`
- **NEVER** use simulation output as wiki content — only real, factual information

### Step 4: Commit
Commit all changes with a descriptive message summarizing pages created/upgraded.

### Quick Reference
```bash
# Deep analysis (recommended, ~$1)
python tools/gap_finder.py --topic "TOPIC" --deep

# Standard analysis (fast, ~$0.03)
python tools/gap_finder.py --topic "TOPIC"

# Internal only (free, no Perplexity)
python tools/gap_finder.py --topic "TOPIC" --internal-only

# Scan specific pages
python tools/gap_finder.py --pages wiki/path/to/page.md --deep
```

## Lint Workflow

Run `tools/lint.py` periodically (or via MCP) to check wiki health:

### Checks Performed
1. **Frontmatter completeness**: every page has all required fields
2. **Broken wikilinks**: links to pages that do not exist (flag pages with >5 broken links)
3. **Orphan pages**: pages with no inbound links
4. **Stale pages**: pages not updated in >90 days with status below `good`
5. **Missing source citations**: wiki pages with no `(Source: [[...]])` references
6. **Empty pages**: pages with no content beyond frontmatter
7. **Index sync**: verify `wiki/index.md` lists all pages that exist
8. **Tag consistency**: flag non-standard tags
9. **Duplicate content**: flag pages with very similar titles or content

### Approved Tags

```
# Markets
crypto, stocks, forex, commodities, options, futures, bonds, defi, nft

# Strategy types
technical-analysis, fundamental-analysis, quantitative, algorithmic,
day-trading, swing-trading, position-trading, scalping, arbitrage,
mean-reversion, trend-following, momentum, breakout, pairs-trading

# Concepts
risk-management, portfolio-theory, market-microstructure, order-types,
indicators, behavioral-finance, valuation, leverage, margin, derivatives,
volatility, correlation, liquidity, slippage

# Asset-specific
bitcoin, ethereum, altcoins, sp500, nasdaq, gold, oil, treasuries

# Meta
history, news, education, book, person, company, exchange, regulation,
ai-trading, machine-learning, backtesting, data-provider, market-regime,
regime-detection, methodology, event-driven
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
5. **Related** — wikilinks to related pages
6. **Sources** — list of source summaries that contributed to this page

### Dataview Integration
Category index pages (`_index.md`) should include Dataview queries for auto-listing:
```dataview
TABLE status, updated
FROM "wiki/markets/crypto"
WHERE type != "index"
SORT updated DESC
```

## Source Types Reference

| Source Type | R2 Prefix | Naming Convention | Notes |
|-------------|-----------|-------------------|-------|
| Web article | `articles/` | `YYYY-MM-DD-slug.md` | Include URL as first line comment |
| PDF | `pdfs/` | `YYYY-MM-DD-slug.pdf` | Convert with `tools/pdf_to_markdown.py`; companion `.md` with extracted text |
| Video/YouTube transcript | `transcripts/` | `YYYY-MM-DD-slug.md` | Transcript text with video URL and timestamps |
| Tweet/thread | `tweets/` | `YYYY-MM-DD-@handle-slug.md` | Full thread text, include tweet URLs |
| Screenshot | `screenshots/` | `YYYY-MM-DD-slug.png` | Companion `.md` with description/OCR |
| Data file | `data/` | `YYYY-MM-DD-slug.csv/json` | Include data dictionary in companion `.md` |
| Book excerpt | `books/` | `author-title-chapter.md` | Include ISBN, page numbers |
| Other | `misc/` | `YYYY-MM-DD-slug.*` | Always include companion `.md` |

All raw files are stored in Cloudflare R2 bucket `trader-wiki`. Full path: `r2://trader-wiki/<prefix>/<filename>`
Upload: `python tools/raw_sync.py upload raw/<prefix>/<filename>`
Download: `python tools/raw_sync.py download <prefix>/<filename>`

## Conversion Tools

| Format | Tool | Command |
|--------|------|---------|
| **PDF** | `tools/pdf_to_markdown.py` (OpenDataLoader) | `python tools/pdf_to_markdown.py <path>` |
| Everything else (.docx, .pptx, .xlsx, etc.) | `tools/convert.py` (MarkItDown) | `python tools/convert.py <path>` |

**PDFs always go through OpenDataLoader** — it preserves headings, tables, lists, and reading order that MarkItDown loses on complex documents. MarkItDown remains the converter for all other binary formats.

## Rules for the LLM

1. **NEVER modify files in R2** after initial upload (raw sources are immutable)
2. **ALWAYS update `wiki/log.md`** after any wiki operation
3. **ALWAYS add frontmatter** to every new page
4. **ALWAYS use wikilinks** for cross-references
5. **NEVER fabricate sources** — only reference sources that exist in `raw/`
6. **NEVER silently overwrite** — when updating, preserve existing content and add new information
7. **Cite sources inline** using `(Source: [[source-id]])` format
8. **Update `wiki/index.md`** when creating new pages
9. **Maintain tag consistency** — use only approved tags (or propose new ones in the log)
10. **Handle contradictions explicitly** — see the contradiction workflow above
11. **Prefer specificity** — "BTC dropped 15% on 2024-03-05" over "BTC dropped significantly"
12. **Date all claims** — include when the information was true/published

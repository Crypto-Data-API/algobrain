---
title: "stockmarketapi.ai — Fred-McNaught Fundamentals (2026-05-10)"
type: source
source_type: data
source_url: "https://stockmarketapi.ai/api/v1/companies/{ticker}/metrics/summary"
source_author: "stockmarketapi.ai"
source_date: 2026-05-10
created: 2026-05-10
updated: 2026-06-10
status: good
tags: [data-provider, fundamentals, stocks, sp500, asx200]
confidence: high
related: ["[[alfred-fundamental-analysis]]", "[[fred-mcnaught]]", "[[s-and-p-500]]", "[[asx-200]]"]
---

Bulk fundamentals snapshot pulled from [stockmarketapi.ai](https://stockmarketapi.ai)'s `/metrics/summary` and `/metrics/history` endpoints on 2026-05-10. Covers S&P 500 + ASX 200 constituents and includes the Fred-McNaught-aligned metric set: 5-year averages (dividend yield, EBITDA margin, ROE, ROA), debt-to-equity (interest-bearing only), liabilities-to-equity, quick ratio, interest coverage, franking credits (ASX-only), and per-period history for trend visibility.

This snapshot is point-in-time. The API caches responses for ~5 minutes, but the underlying data is filings-based and updates on issuer reporting cadence. Pages cite this source via `[[stockmarketapi-fundamentals-2026-05-10]]`.

> **Refresh 2026-06-10:** full re-pull of the same endpoints for all 684 covered tickers (same metric set, same tooling); enriched pages now show `pulled 2026-06-10` in their `## Fundamentals` header. A `--scope all` probe confirmed API coverage is limited to the S&P 500 + ASX 200 universe — the ~225 wiki tickers outside both indices (options-stocks, AI singletons) return 404 and are excluded.

## Endpoints used

- `GET /api/v1/companies/metrics/bulk?tickers=...&exchange=...` — batched at 25 tickers per call
- `GET /api/v1/companies/{ticker}/metrics/history?periods=5` — per-ticker history with 5y averages
- `GET /api/v1/companies/{ticker}` — sector / industry / exchange context (already in wiki frontmatter from prior ingestions)

Tooling: `tools/fetch_fundamentals.py` + `tools/enrich_fundamentals.py`.

## Coverage

| Scope | Tickers in wiki |
|---|---|
| S&P 500 (`sp500: true`) | 497 |
| ASX 200 (`asx200: true`) | 194 |
| Dual-flagged | 6 |
| **Distinct in scope** | **685** |

Pages outside both indices (singleton AI stocks, options-stocks, etc.) are not included in this run.

## What each enriched page gets

1. **Frontmatter mirror** — headline metrics surfaced for Dataview queries: `pe_ratio`, `debt_to_equity`, `roa_5y_avg`, `roe_5y_avg`, `ebitda_margin_5y_avg`, `dividend_yield_5y_avg`, `data_completeness_pct`, `fundamentals_period_end`, `fundamentals_updated`, `fred_profile`.
2. **`## Fundamentals` section** with three sub-blocks:
   - **Snapshot** — latest period + 5y avg + Fred's bar for ~17 metrics
   - **5-period trend** — EBITDA margin, operating margin, ROE, D/E across the most recent 5 fiscal periods
   - **Fred-framework view** — soft portfolio-archetype label + suits / watch-for / sector context
3. **Removal of legacy thin `## Financial Snapshot`** — the three-row P/E / Operating Margin / ROE table from the April 2026 ingest is superseded.

## Provenance

Each per-ticker JSON in `raw/data/fundamentals/{ticker}.json` carries an API-supplied `provenance` block: `primary_source` (e.g. `sec_edgar`), `last_updated_at`, `data_completeness_pct`. Pages where `data_completeness_pct < 60%` get the metrics rendered raw but skip the Fred-framework verdict (label: "Insufficient data").

## Caveats

- **Ratio definitions are the API's, not necessarily Fred's verbal definitions.** The `dividend_yield` field for AAPL returns ~35% (book-equity-based, not market-cap-based); ROE of 150%+ for AAPL similarly reflects buyback-shrunken book equity, not the conventional reading. Treat headline values as inputs to Fred's framework, not finished verdicts. Cross-reference `GET /api/v1/formulas/{name}` for definitions.
- **Fred-framework verdicts are advisory, never trade signals.** The wiki uses soft "Suits / Watch for / Sector context" framing rather than buy/sell calls. See [[fred-mcnaught]] and [[alfred-fundamental-analysis]] for the underlying methodology.
- **Sector-aware bars.** Fred's standard hurdles (D/E <1.0, current ratio >2, interest coverage >3x) are explicitly relaxed in pages tagged `Utilities`, `Real Estate`, `Financials`, and `Communication Services` (high-leverage-tolerant), and the current-ratio bar is N/A for `Consumer Discretionary` / `Consumer Staples` (retail).

## Profile labels

| Label | Trigger |
|---|---|
| `Quality compounder` | passes D/E + EBITDA + ROA bars and 5y ROE > 15% |
| `Defensive income candidate` | pays a dividend and passes ROA bar |
| `Cyclical / leveraged` | sector ∈ Utilities / REIT / Financials / Communication Services |
| `Speculative / unprofitable` | net margin < 0 OR interest coverage < 1.5x |
| `Balanced` | passes all available bars but no exceptional dimension |
| `Mixed-quality` | passes ≥50% of bars but fails at least one |
| `Value with concerns` | passes <50% of bars |
| `Insufficient data` | API completeness < 60% |

## Related

- [[alfred-fundamental-analysis]] — Fred's methodology as encoded in the Alfred analyst
- [[fred-mcnaught]] — biographical / framework page
- [[s-and-p-500]] — index page
- [[asx-200]] — index page
- [[stockmarketapi-sp500-2026-04-13]] — earlier ingest from same provider (constituent + thin snapshot)
- [[stockmarketapi-asx200-2026-04-15]] — earlier ASX 200 ingest

---
title: "CryptoDataAPI — Strategy & Indicator Library (AlgoBrain API)"
type: source
created: 2026-09-28
updated: 2026-09-28
status: good
tags: [data-provider, crypto, api, strategy-development, indicators, agents, ai-trading, llm, backtesting, methodology, open-source]
aliases: ["CryptoDataAPI Strategy Library", "CDA Strategy Library", "Strategy Library API", "Indicator Catalog API", "AlgoBrain API", "Hosted AlgoBrain Search", "/strategies endpoint", "/algobrain/search"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
source_author: "CryptoDataAPI"
confidence: high
related: ["[[cryptodataapi]]", "[[cryptodataapi-mcp]]", "[[cryptodataapi-indicators]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-strategy-baskets]]", "[[cryptodataapi-regimes]]", "[[strategies-overview]]", "[[indicators-overview]]", "[[external-strategy-sources]]", "[[edge-taxonomy]]", "[[hypothesis-to-backtest-workflow]]", "[[overfitting-detection]]"]
---

The Strategy & Indicator Library family of [[cryptodataapi]] serves **this wiki** as structured JSON. `/strategies` exposes 317 crypto strategy playbooks in 22 groups, each with its summary, indicators, feeding endpoints and two copy-paste AI-agent prompts. `/indicators/catalog` exposes 187 indicator definitions in 12 groups. `/algobrain/search`, `/algobrain/page` and `/algobrain/stats` give BM25 search and raw-markdown reads over the whole AlgoBrain index (~5k pages). The `/algobrain/*` routes shipped 2026-09-19, the strategy filters on search 2026-09-27, and the two catalogues 2026-09-28. All nine routes accept any API key, Free included, and the content is licensed **CC BY 4.0**.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/strategies/groups | `groups[]` (`slug`, `name`, `description`, `strategy_count`), `group_count`, `strategy_count`, `source` | — | Any key |
| GET | /api/v1/strategies | `strategies[]` (`slug`, `name`, `group`, `summary`, `timeframe`, `complexity`, `indicators[]`, `endpoints[]`), `group` (filter applied, or null), `count`, `source` | group | Any key |
| GET | /api/v1/strategies/{slug} | List-row fields plus `edge`, `edge_source[]`, `markets[]`, `data_required[]`, `backtest_status`, `tags[]`, `wiki_path`, `prompts[]` | slug (path) | Any key |
| GET | /api/v1/indicators/catalog/groups | `groups[]` (`slug`, `name`, `description`, `indicator_count`, `endpoints[]`), `group_count`, `indicator_count`, `source` | — | Any key |
| GET | /api/v1/indicators/catalog | `indicators[]` (`slug`, `name`, `group`, `summary`, `aliases[]`, `endpoints[]`), `group`, `count`, `source` | group | Any key |
| GET | /api/v1/indicators/catalog/{slug} | List-row fields plus `tags[]`, `difficulty`, `used_by[]` (up to 12 strategies), `wiki_path`, `prompts[]` | slug (path) | Any key |
| GET | /api/v1/algobrain/search | `results[]` (`path`, `title`, `type`, `status`, `category`, `tags`, `updated`, `snippet`, `score`, `strategy`, `read`, `url`), `query`, `count`, `license`, `source` | q (≤200 chars), type, tag, category, backtest_status, horizon, strategy_type, complexity, crowding_risk, market, limit (1-50, default 10) | Any key |
| GET | /api/v1/algobrain/page | One page: `path`, `title`, `type`, `status`, `category`, `tags`, `updated`, `markdown`, `url`, `license` | path (required, ≤300 chars) | Any key |
| GET | /api/v1/algobrain/stats | `total_pages`, `built_at` (unix s), `source_commit`, `by_category`, `by_type`, `by_backtest_status`, `license`, `source` | — | Any key |

"Any key" means a valid `X-API-Key` on any plan. A keyless call returns 401 (checked on `/strategies/groups`, 2026-09-28).

### Field notes

- **`slug`** is stable and matches this wiki's filename. `funding-rate-arbitrage` is [[funding-rate-arbitrage]] and `rsi` is [[rsi]]. The spec notes that the slug is also the anchor on the public `/trading-strategies/{group}` and `/trading-indicators/{group}` pages.
- **`timeframe`** on a strategy is a holding style, not a bar interval. The spec lists `scalp | intraday | day | swing | position | long-term`.
- **`indicators`** is `[{slug, name, group}]` for what the playbook links to or requires. It is empty when the playbook declares none, as for `ai-agent-token-arbitrage`.
- **`endpoints`** is the list of CDA paths that feed the strategy's inputs, or that serve the indicator or its raw inputs. Indicator groups also carry a group-level `endpoints` list.
- **`edge`** is the playbook's edge-mechanism sentence, and is empty when the page states none. `edge_source` uses the [[edge-taxonomy]] labels.
- **`wiki_path`** is the repo-relative path of the full page (e.g. `wiki/strategies/arbitrage/funding-rate-arbitrage.md`). Pass it to `/algobrain/page?path=` to get the markdown.
- **`prompts`** holds `[{title, prompt}]`. A strategy carries two: "Build it with an AI agent" and "Backtest it". An indicator carries one: "Compute it with an AI agent". The prompts use real CDA paths. The 2026-09-28 build prompt for `funding-rate-arbitrage` pins 1d bars, a 500-bar lookback, BTC/ETH/SOL, 1% risk per trade and a regime gate on `/regimes/current`, and ends "Research only — do not place orders." The backtest prompt pins 4.5 bps taker per side, 2 bps slippage, funding every 8h, bar-close signals and a 70/30 in-sample/out-of-sample split, and it points at `/backtesting/klines` and `/backtesting/funding` (both Pro).
- **`used_by`** on an indicator lists up to 12 catalogue strategies as `{slug, name, group}`. `rsi` returned exactly 12 on 2026-09-28, so a popular indicator's list is truncated.
- **`strategy`** on a search result holds the page's frontmatter: `backtest_status`, `horizon`, `strategy_type`, `complexity`, `crowding_risk`, `markets`, `edge_source`, `expected_sharpe`, `expected_max_drawdown`, `breakeven_cost_bps` and `expected_sharpe_source: "author_estimate"`. It is null on non-strategy pages. `score` is null when only filters were given.
- **`read`** on a search result is the `/algobrain/page` URL for that result. `url` is the GitHub blob URL.

### Search filters (added 2026-09-27)

`backtest_status`, `horizon`, `strategy_type`, `complexity`, `crowding_risk` and `market` are each an any-of match against the page's own values. For example, `horizon=swing` also finds pages whose horizon is `swing|position`. The query side takes a single value: on 2026-09-28 comma and pipe lists returned nothing, and a repeated parameter kept only the last value. `q` becomes optional once any filter is given. `horizon` takes `scalp`, `intraday`, `swing`, `position` or `long-term`. The spec states that it is **not** a bar interval, because the wiki has no 1h/4h field. `/algobrain/stats` gained `by_backtest_status` in the same release.

## Author labels, not measured results

**`backtest_status`, `expected_sharpe`, `expected_max_drawdown` and `breakeven_cost_bps` are the wiki authors' own labels and estimates.** CryptoDataAPI did not measure them. The changelog describes `backtest_status` as "the playbook's own validation label, not a result we measured". Search tags the performance figures `expected_sharpe_source: "author_estimate"` and **never ranks by them**. The spec calls them "literature expectations, not results measured on any venue".

This matches the wiki's own convention. The frontmatter fields in `CLAUDE.md` record what a page's author believed, and a status of `live` means only that a page claims a live deployment. Treat every figure as a hypothesis for [[hypothesis-to-backtest-workflow]] and [[overfitting-detection]], and check the claim against the page's `## Performance characteristics` section before relying on it. The recommended use is to *filter* on `backtest_status` (e.g. `cost-corrected`, `walk-forward-validated`, `live`) to surface pages with more evidence behind them. Do not rank by `expected_sharpe`.

`by_backtest_status` on 2026-09-28 (build of 2026-09-27): untested 251, naive-backtested 39, live 36, paper-traded 18, retired 13, cost-corrected 13, pilot 8, walk-forward-validated 6, paused 2, speculative 1. `speculative` is not a value in the wiki's `backtest_status` enum, so one strategy page carries a non-schema label.

## Groups (live, 2026-09-28)

### Strategy groups: 22 groups, 317 strategies

| Slug | Name | Count |
|------|------|-------|
| `options-strategies` | Options Strategies | 46 |
| `momentum` | Momentum & Rotation | 29 |
| `defi-yield-onchain` | DeFi Yield & On-Chain | 22 |
| `funding-carry-basis` | Funding, Carry & Basis | 20 |
| `volatility-trading` | Volatility Trading | 20 |
| `defi-arbitrage` | DeFi & On-Chain Arbitrage | 20 |
| `liquidation-positioning` | Liquidation & Positioning | 19 |
| `event-driven` | Event-Driven & News | 14 |
| `breakout` | Breakout | 13 |
| `mev-onchain-execution` | MEV & On-Chain Execution | 12 |
| `trend-following` | Trend Following | 12 |
| `market-making-microstructure` | Market Making & Microstructure | 11 |
| `sentiment-contrarian` | Sentiment & Contrarian | 11 |
| `statistical-arbitrage` | Statistical Arbitrage & Pairs | 10 |
| `portfolio-risk` | Portfolio & Risk Management | 10 |
| `cex-arbitrage` | CEX & Cross-Venue Arbitrage | 9 |
| `mean-reversion` | Mean Reversion | 9 |
| `macro-fundamental` | Macro & Fundamental | 9 |
| `special-situations` | Special Situations | 7 |
| `ai-machine-learning` | AI & Machine Learning | 7 |
| `multi-strategy` | Multi-Strategy Combinations | 4 |
| `regime-switching` | Regime Switching | 3 |

The groups are a CryptoDataAPI taxonomy. They do not mirror this wiki's folders under `wiki/strategies/`. The catalogue's 317 strategies are also fewer than the index's 363 `type: strategy` pages, so some strategy pages are not in the catalogue.

### Indicator groups: 12 groups, 187 indicators

| Slug | Name | Count | Group endpoints |
|------|------|-------|-----------------|
| `volatility` | Volatility | 31 | /volatility/index, /volatility/regime, /indicators/technical, /hyperliquid/candles |
| `options-greeks` | Options & Greeks | 26 | /market-intelligence/options, /volatility/implied, /quant/gex |
| `trend-moving-averages` | Trend & Moving Averages | 24 | /indicators/technical, /indicators/signum-rgg, /hyperliquid/candles |
| `volume-order-flow` | Volume & Order Flow | 21 | /hyperliquid/trade-flow, /market-intelligence/taker-buy-sell, /volume/scanner, /hyperliquid/l2-book |
| `momentum-oscillators` | Momentum & Oscillators | 21 | /indicators/technical, /indicators/signum-rgg, /hyperliquid/candles |
| `chart-patterns-price-action` | Chart Patterns & Price Action | 21 | /hyperliquid/candles, /market-data/klines, /indicators/technical |
| `macro-cross-asset` | Macro & Cross-Asset | 12 | /sentiment/macro, /event/calendar, /market-intelligence/etf/{asset}/flows |
| `on-chain` | On-Chain Metrics | 9 | /on-chain/score, /on-chain/exchange-flows/spike-alerts, /market-intelligence/btc/cycle-indicators, /on-chain/whales |
| `derivatives-positioning` | Derivatives & Positioning | 8 | /derivatives/funding-rates, /derivatives/open-interest, /market-intelligence/liquidations, /derivatives/binance/long-short-ratio |
| `market-breadth-regime` | Market Breadth & Regime | 6 | /market-health/altcoin-breadth, /regimes/current, /quant/market, /market-health |
| `quant-statistical` | Quant & Statistical | 6 | /backtesting/klines, /backtesting/funding, /quant/coins |
| `sentiment` | Sentiment | 2 | /sentiment/fear-greed, /market-intelligence/fear-greed-history, /news/pulse |

(All group endpoint paths are under `/api/v1`.) The indicator catalogue holds **definitions only**. Live values stay on `/indicators/technical`, `/indicators/signum-rgg` and the other signal routes documented on [[cryptodataapi-indicators]].

## Errors

| Status | `error` | When | Body |
|--------|---------|------|------|
| 400 | `unknown_group` | `?group=` on `/strategies` or `/indicators/catalog` names no group | `valid_groups` lists every valid slug for that catalogue |
| 404 | `strategy_not_found` | `/strategies/{slug}` with an unknown slug | Message points to `/api/v1/strategies` |
| 404 | `indicator_not_found` | `/indicators/catalog/{slug}` with an unknown slug | Message points to `/api/v1/indicators/catalog` (seen live 2026-09-28; the changelog does not name it) |
| 404 | `page_not_found` | `/algobrain/page` with an unknown `path` | Message points to `/api/v1/algobrain/search` |
| 503 | `algobrain_index_unavailable` | The hosted index is not loaded (2026-09-19 release) | — |
| 503 | `algobrain_index_outdated` | A strategy filter is sent to a server whose index predates the 2026-09-27 fields | — |

Errors come back wrapped in FastAPI's `detail` object, e.g. `{"detail": {"error": "unknown_group", "message": "No group 'nope'.", "valid_groups": [...]}}`. A 503 is transient. Retry it or fall back to the local wiki. It does not mean the query was wrong.

## Relationship to this wiki

The API serves this repository's content. Every strategy and indicator record carries a `wiki_path` into the same `wiki/` tree, and `/algobrain/page` returns that file's markdown. The same fields exist in the local file's frontmatter.

**The hosted index lags the repo.** `/algobrain/stats` on 2026-09-28 reported `built_at` 1790473789 (2026-09-27 01:49 UTC), `source_commit` `bc587c5` and `total_pages` 4960. In this repo `bc587c5` is the 2026-08-26 commit "Merge concurrent loop: reconcile duplicate news category page", 20 commits behind `HEAD` (`06b7daa`, 2026-09-28). The build date is recent, but the content it was built from is about a month old. Pages created or edited since then, such as [[external-strategy-sources]] (created 2026-09-28), are absent or stale in the API. To check the lag at any time:

```bash
curl -s -H "X-API-Key: $CDA_KEY" https://cryptodataapi.com/api/v1/algobrain/stats | jq -r .source_commit
git log -1 --format='%h %ci %s' <that-commit> && git rev-list --count <that-commit>..HEAD
```

The stats `source` field names `https://github.com/Crypto-Data-API/algobrain` and search `url` values point at that repo's `main` branch. This checkout's `origin` is `Crypto-Data-API/ai-crypto-trading-strategy-wiki-brain`, but the commit hash above resolves in local history.

Practical consequences:
- **Local edits are ahead of the API.** When the wiki itself is the question, read the local file. Use the API for agents that cannot see the repo.
- **Frontmatter fixes reach API consumers only after a rebuild.** Correcting `backtest_status` or `expected_sharpe` on a page changes what `/strategies/{slug}` and search return only once a new `source_commit` shows up.
- **Slugs are a public contract.** Renaming or moving a strategy or indicator page breaks the API `slug` and `wiki_path` for downstream agents. Leave a `type: redirect` page behind.

## Relationship to the MCP servers

There are two separate MCP surfaces.

- **Local wiki MCP server** (`tools/mcp_server.py`). It runs from this checkout and exposes `wiki_search`, `wiki_read`, `wiki_stats`, `wiki_lint` and `wiki_ingest` over the *current* files, so it has no index lag. Every `wiki_search` response carries the `data_instruction` block that points at CryptoDataAPI.
- **Hosted `/algobrain/*` routes.** These are read-only search and page reads over the published index, and they were built "for agents that cannot run its local MCP server" (changelog, 2026-09-19). An agent connected to the hosted CryptoDataAPI MCP ([[cryptodataapi-mcp]]) can reach them and the `/strategies` and `/indicators/catalog` catalogues through its generic API tooling. See that page for connection setup.

As a rule of thumb, use the local server when working *on* the wiki and the hosted routes when an agent only needs to *use* it.

## Agent use cases

- **Pick a strategy by group.** Call `GET /strategies/groups`, choose a group (e.g. `funding-carry-basis`), then `GET /strategies?group=funding-carry-basis` and filter rows on `timeframe` and `complexity`.
- **Get the build and backtest prompts.** `GET /strategies/{slug}` returns the two `prompts` ready to hand to a coding agent, plus the `wiki_path` for the full playbook.
- **Pull the feeding data.** Call each path in `endpoints` (live), then the `/backtesting/*` routes named in the backtest prompt (history, Pro) on [[cryptodataapi-backtesting]].
- **Filter by evidence, not by promise.** Run `GET /algobrain/search?type=strategy&backtest_status=walk-forward-validated`, then repeat with `cost-corrected`, to find pages with the most validation behind them. Each filter takes **one value per call**. On 2026-09-28 a comma list (`cost-corrected,walk-forward-validated`) or pipe list returned 0 results, and a repeated parameter used only the last value. Treat `expected_sharpe` as an author prior only.
- **Go from indicator to strategies.** `GET /indicators/catalog/{slug}` returns `used_by` to find strategies built on an indicator, and `endpoints` for where to get its inputs.
- **Check duplicates before writing a new page.** Search the catalogue before harvesting an outside idea (see [[external-strategy-sources]]). Remember the index lag.

## Examples

```bash
# The 22 strategy groups with counts
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/strategies/groups"

# All strategies in one group
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/strategies?group=funding-carry-basis"

# One strategy in full, including its build + backtest prompts
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/strategies/funding-rate-arbitrage"

# One indicator: definition, used_by, feeding endpoints, compute prompt
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/indicators/catalog/rsi"

# Filter-only search (no q): swing-horizon strategies labelled cost-corrected
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/algobrain/search?type=strategy&horizon=swing&backtest_status=cost-corrected&limit=20"

# Read a page's markdown by the path a result returned
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/algobrain/page?path=wiki/strategies/arbitrage/funding-rate-arbitrage.md"
```

## Licence

The content is **CC BY 4.0**. The `license` field reads "CC BY 4.0 — attribute AlgoBrain / CryptoDataAPI", and catalogue `source` fields read "AlgoBrain wiki (CC BY 4.0) — https://cryptodataapi.com/algobrain". Redistributing or embedding a playbook requires attribution.

## Related

- [[cryptodataapi]]: hub page with auth, plans and the full category map
- [[cryptodataapi-mcp]]: hosted MCP server and agent setup (the only place for connection boilerplate)
- [[cryptodataapi-indicators]]: the *live* indicator values that the catalogue's definitions point to
- [[cryptodataapi-backtesting]]: the history that the "Backtest it" prompts pull from
- [[cryptodataapi-strategy-baskets]]: the separate 50-basket signal family, mirrored in [[trading-strategy-baskets]] and [[hyperliquid-baskets-overview]]
- [[strategies-overview]], [[indicators-overview]]: the wiki hubs that these catalogues expose
- [[external-strategy-sources]]: the harvesting funnel, which should check this catalogue for duplicates first
- [[edge-taxonomy]]: the `edge_source` vocabulary
- [[hypothesis-to-backtest-workflow]], [[overfitting-detection]], [[deflated-sharpe-ratio]]: how to turn an `author_estimate` into evidence

## Sources

- https://cryptodataapi.com/api/docs, OpenAPI spec (fetched 2026-09-28): paths `/api/v1/strategies*`, `/api/v1/indicators/catalog*`, `/api/v1/algobrain/*` and schemas `StrategyDetail`, `IndicatorDetail`, `AlgoBrainSearchResponse`, `AlgoBrainStatsResponse`
- https://cryptodataapi.com/api/v1/changelog: 2026-09-19, 2026-09-27 and 2026-09-28 entries (fetched 2026-09-28)
- Live calls on 2026-09-28 to all nine routes, including the error cases (group and count figures above)

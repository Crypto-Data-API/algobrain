---
title: "CryptoDataAPI — News & Catalysts"
type: source
created: 2026-08-25
updated: 2026-08-25
status: good
tags: [data-provider, crypto, api, news, event-driven, hyperliquid, backtesting, sentiment]
aliases: ["CryptoDataAPI News", "CDA News", "CryptoDataAPI Catalysts", "CryptoDataAPI News & Catalysts"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
source_author: "CryptoDataAPI"
source_date: 2026-08-25
confidence: high
related: ["[[cryptodataapi]]", "[[cryptodataapi-market-intelligence]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-mcp]]", "[[news-and-sentiment-sources]]", "[[event-driven-trading]]", "[[news-trading]]", "[[sentiment-analysis]]", "[[liquidation]]", "[[hyperliquid]]"]
---

The News & Catalysts category of [[cryptodataapi]] shipped 2026-08-18: a free, keyless catalyst pipeline over publisher RSS (The Block, CoinDesk, Cointelegraph, Decrypt, The Defiant, CryptoSlate, Bitcoin Magazine), OKX announcements, and ~25 project blogs, reduced to per-coin pressure/tilt features, a filtered catalyst tape, per-coin qualified events, feed-health monitoring, and a backtestable archive of measured post-catalyst price response. A 2026-08-21 follow-up release added a shared policy-catalyst taxonomy after a major regulatory/macro day produced zero tape entries.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/news/pulse | Per-coin news feature series (pressure, tilt, event count, top impact, headline count) | hours | — |
| GET | /api/v1/news/market-moving | Filtered catalyst tape — only events clearing the impact threshold | symbol, hours, min_impact, limit | Free: BTC/ETH/MARKET, 24h, top 10; Pro: full HL universe, 7d; Pro Plus: full history + score components + market_response |
| GET | /api/v1/news/coin/{symbol} | Qualified events + features for one perp | symbol*, hours | Free: BTC/ETH only; Pro+: any perp; Pro Plus adds score components + market_response |
| GET | /api/v1/news/sources | Per-feed health, funnel counts, coverage gap | — | — |
| GET | /api/v1/backtesting/news-events | Archived tape with measured market-response labels | start*, symbol, end, min_impact, bounds, limit | Pro Plus |

Tier "—" means the docs list no tier restriction for that endpoint.

## Live Data

`/news/pulse` returns one row per Hyperliquid perp, cross-sectionally ranked and joinable straight onto price: `news_pressure` (0-1, recency-weighted sum of impact scores, saturating), `news_tilt` (-1 to +1 impact-weighted direction; negative is risk-off), `event_count` and `top_impact` (a steady drip of small stories vs. one big one), and `headlines` (raw coverage — stories naming the coin at high confidence, whether or not any qualified as a catalyst). The catalyst funnel discards roughly 95% of what it reads, so most coins sit at `news_pressure: 0` while `headlines` keeps counting. **A coin high on headlines with no pressure is being talked about without anything happening** — that's attention, not an event.

`/news/market-moving` is the filtered tape: only events clearing the impact threshold survive. Pro Plus responses add `impact_score` components (`severity`, `confidence`, `match_mode`, `sources`) and the measured `market_response` at +15m/+1h/+4h. `bias` is signed (negative = risk-off); `corroboration` counts independent sources carrying the same `(symbol, category)` inside the scoring window — described as the strongest single indicator a story is real rather than syndicated. `/news/coin/{symbol}` is the same qualified-event view scoped to one perp, gated the same way by tier.

Every event states how its coin was identified via `match_mode` (`cashtag`, `name`, `venue_ticker`, `entity_hint`, `venue_native`, `ticker_context`) and a `confidence` between 0.6 and 1.0. `category: hl_listing` / `hl_delisting` is sourced from CryptoDataAPI's own Hyperliquid universe diff rather than any news feed.

`/news/sources` reports per-feed health plus `funnel_24h` hourly counts (`ingested`, `dropped_noise`, `dropped_no_catalyst`, `dropped_no_entity`, `dropped_below_threshold`, `qualified`) — no titles or URLs. `sources[].not_modified` distinguishes "answered 304, nothing new" from "dead"; both otherwise look like zero fresh items, which is how a silently broken feed hides. `unresolvable` lists active perps whose ticker is a common English word with no safe project name — matchable only by cashtag, published as a field rather than left a silent blind spot.

**2026-08-21 policy-catalyst release.** Nine new `category` values are now shared across `/news/market-moving`, `/news/coin/{symbol}`, and `/backtesting/news-events` (additive — existing categories are unchanged): `legislation`, `executive_signal`, `rulemaking`, `restrictive_policy`, `sovereign_bid`, `strategic_reserve`, `pro_crypto_eo`, `macro_liquidity`, `macro_tightening`. All are market-wide and resolve to `symbol: "MARKET"` when a headline names no specific coin — any consumer switching on `category` needs a default branch for values it doesn't recognize. It shipped after a 2026-08-20 White House crypto event, a presidential push for the CLARITY Act, and a doubling of US Treasury debt buybacks moved BTC roughly 10% and liquidated about $3B of shorts while producing **zero** `/news/market-moving` events — the taxonomy had no rule for legislation, executive action, agency rulemaking, or a sovereign buyer, so each headline scored as "not a catalyst" before entity resolution ran. A classification bug was fixed at the same time: `treasury_buy` had matched the "buy" in "buybacks", so "US Treasury Doubles Debt Buybacks" filed as a corporate crypto purchase; that headline shape is now `macro_liquidity`, while `treasury_buy` (still corporate/public-company purchases) joined the market-wide set. Scoring windows were also tuned for policy-heavy days: corroboration window 6h to 24h, and novelty damping 12h to 6h for policy categories (every market-wide story shares `symbol: MARKET`, so one 12h bucket per category was collapsing a busy policy day into a single tape entry). The impact threshold itself (0.45) is unchanged, so expect a denser tape on policy-heavy days going forward.

## Historical Data

`/backtesting/news-events` (Pro Plus) is the backtestable form of `/news/market-moving`: every qualified catalyst with `impact_score`, signed `bias`, `corroboration`, `match_mode`, `confidence`, and the *measured* move that followed — `ret_15m`, `ret_1h`, `ret_4h`, `vol_mult` (vs. that coin's own 30-day baseline), `oi_change_pct`, `funding_shift`, and a combined `abnormality`. `start` is required; `symbol`, `end`, `min_impact`, `bounds`, and `limit` narrow the query. Two constraints to respect: **only qualified events are archived** — stories that failed the noise gate or scored below threshold were discarded at ingest and no row exists for them, so this is not "all news"; and **history starts 2026-08-18, when the family shipped, and cannot be backfilled** — the RSS sourcing behind it serves only a recent window, so no earlier tape will ever exist. The 2026-08-21 policy-catalyst `category` values (see above) apply to this archive too. For the wider point-in-time archive this endpoint sits inside, see [[cryptodataapi-backtesting]].

## Trading Applications

- **Catalyst-gated entries** — [[event-driven-trading]] and [[news-trading]] systems can gate entries on `/news/market-moving` events clearing `min_impact`, using `corroboration` (independent sources on the same symbol+category inside the window) as the strongest single signal a story is real rather than syndicated
- **Continuous news feature for sentiment/regime models** — `news_pressure` and `news_tilt` from `/news/pulse` are cross-sectionally comparable and join straight onto price for [[sentiment-analysis]] pipelines; remember most coins sit at zero pressure while `headlines` keeps counting — that's attention without an event, not a signal on its own
- **Policy-day awareness** — the 2026-08-21 category set (`legislation`, `executive_signal`, `sovereign_bid`, `macro_liquidity`, etc.) resolves to `symbol: MARKET`, so a book that only watches per-coin events misses market-wide regulatory and macro-liquidity catalysts entirely
- **Backtestable catalyst response** — `/backtesting/news-events` supplies measured `ret_15m` / `ret_1h` / `ret_4h` / `vol_mult` / `abnormality` outcomes for building or validating a [[news-trading]] or [[event-driven-trading]] response model, subject to the qualified-events-only and no-backfill caveats above
- **Feed-health monitoring** — `/news/sources`' `funnel_24h` counts and `not_modified` flag catch a silently broken RSS feed before a strategy starves on stale data; `unresolvable` flags perps whose ticker collides with common English words (matchable only by cashtag)
- **Complementary tripwire for the lag** — news is 15-45 minutes behind a breaking cascade; pair with `/market-intelligence/squeeze-alerts` on [[cryptodataapi-market-intelligence]] for a same-second forced-[[liquidation]] signal while the story is still being written

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/news/market-moving?symbol=BTC&hours=24&min_impact=0.6&limit=20"
```

## Related

- [[cryptodataapi]] — hub page with auth, tiers, and the full category map
- [[cryptodataapi-market-intelligence]] — `/market-intelligence/squeeze-alerts`, the same-second liquidation-flow complement to this family's 15-45min-lagged news
- [[cryptodataapi-regimes]] — `/policy/regime` and `/policy/headlines` share the same catalyst taxonomy and news-flow sourcing
- [[cryptodataapi-backtesting]] — the wider point-in-time archive `/backtesting/news-events` sits inside
- [[cryptodataapi-mcp]] — hosted MCP server for agent access to this and every other category
- [[news-and-sentiment-sources]] — the wiki's general news/sentiment provider catalog
- [[event-driven-trading]], [[news-trading]], [[sentiment-analysis]], [[liquidation]], [[hyperliquid]]

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-08-25)
- https://cryptodataapi.com/api/openapi.json (fetched 2026-08-25)

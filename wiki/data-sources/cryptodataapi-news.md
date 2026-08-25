---
title: "CryptoDataAPI — News & Catalyst Detection"
type: source
created: 2026-08-26
updated: 2026-08-26
status: good
tags: [data-provider, crypto, api, news, event-driven, sentiment, hyperliquid, regulation]
aliases: ["CryptoDataAPI News", "CDA News", "News & Catalyst Detection API", "Market-Moving News API"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
source_author: "CryptoDataAPI"
confidence: high
related: ["[[cryptodataapi]]", "[[cryptodataapi-market-intelligence]]", "[[cryptodataapi-sentiment]]", "[[cryptodataapi-backtesting]]", "[[crypto-policy-shock-trading]]", "[[news-trading]]", "[[policy-shock-regime]]", "[[event-catalyst-regime]]", "[[hyperliquid]]"]
---

The News & Catalyst Detection family of [[cryptodataapi]] (shipped 2026-08-18) turns the ~300-500 crypto and policy stories ingested daily from free RSS and announcement feeds into a filtered, per-coin catalyst tape: a `news_pressure`/`news_tilt` feature series for every Hyperliquid perp, a qualified-events tape with an `impact_score` and signed `bias`, feed-health diagnostics, and a Parquet-archived history for backtesting. It is the wiki's structured alternative to manually watching a news terminal for crypto-moving headlines.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/news/pulse | Per-coin news feature series for every active HL perp: `news_pressure` (0..1), `news_tilt` (-1..+1), `event_count`, `top_impact`, `headlines` (raw coverage count), cross-sectional `rank` | hours (1-168, default 24) | Free = top 10 rows; Pro/Pro Plus = full universe |
| GET | /api/v1/news/market-moving | Filtered catalyst tape: `symbol` (HL perp or `MARKET`), `category`, `impact_score` (0..1), signed `bias`, `corroboration`; Pro Plus adds `severity`/`confidence`/`match_mode`/`sources` and `market_response` | symbol, hours (1-336, default 24), min_impact (default 0.45), limit (max 500) | Free = BTC/ETH/MARKET, 24h, top 10; Pro = full universe, 7d; Pro Plus = full retained history + score components |
| GET | /api/v1/news/coin/{symbol} | Qualified events plus `news_pressure`/`news_tilt` for one perp | symbol (path), hours (1-336, default 72) | Free = BTC/ETH only; Pro/Pro Plus = any perp (Pro Plus adds `market_response`) |
| GET | /api/v1/news/sources | Per-feed health, hourly funnel counts (`ingested`/`dropped_noise`/`dropped_no_catalyst`/`dropped_no_entity`/`dropped_below_threshold`/`qualified`), `unresolvable` ticker list | — | — |
| GET | /api/v1/backtesting/news-events | Archived catalyst tape with measured market response: `ret_15m`/`ret_1h`/`ret_4h`, `vol_mult`, `oi_change_pct`, `funding_shift`, `abnormality` | start (required), end (exclusive), symbol, min_impact, limit (max 5000) | Pro Plus |

Tier "—" = not gated beyond a valid API key per the docs.

## Live Data

`/news/pulse` is the strategy-ready join: **every active perp gets a row**, and a quiet coin reads `news_pressure: 0` rather than being absent — the cross-sectional ranking needs the zeros, and a silently missing symbol should mean a pipeline failure, not a quiet market. `headlines` is a separate field from `news_pressure`: it is raw attention (how many stories name the coin at all), while the catalyst funnel discards roughly 95% of what it reads before anything reaches `news_pressure` — a coin high on `headlines` with `news_pressure: 0` is being talked about without anything qualifying as an event.

`/news/market-moving` is the filtered tape itself, and `/news/coin/{symbol}` is the same tape scoped to one perp. `/news/sources` exposes the ingestion funnel so a silently over-tightening filter (or a dead feed masquerading as a quiet one via `not_modified`) can be caught.

## Historical Data

`/backtesting/news-events` is the backtestable form of `/news/market-moving`, archived daily to Parquet as the `news_events` type, with the same qualified events plus their *measured* post-event returns and volume/OI/funding response so `impact_score` can be validated against what actually happened rather than taken on trust.

**History starts 2026-08-18 (the family's ship date) and cannot be backfilled** — RSS only serves a recent window, so no earlier tape will ever exist. This is a hard start date for any backtest built on this data: a 2026-08-20 BTC move that the tape initially missed entirely (see below) will never appear retroactively no matter how the category taxonomy has since improved.

## Coverage & Caveats

- **This is a filtered tape, not a news archive.** Of the ~300-500 stories ingested daily, only ~15-40 clear the 0.45 default impact threshold and get stored or served — sub-threshold stories are discarded outright at ingest. **There is no raw-feed endpoint at any tier**; an integration cannot query "all news about a coin," only what qualified as a catalyst.
- **`match_mode` and `confidence` exist because the HL perp universe is full of ordinary English words** as tickers (`TRUMP`, `MOVE`, `NOT`, `S`, `W`, `ME`, `GAS`, `SAND`) that can only be matched via a cashtag or the full project name, never a bare ticker. Every event states how it was matched — `cashtag`, `name`, `venue_ticker`, `entity_hint`, `venue_native`, or `ticker_context` — with a `confidence` in the 0.6-1.0 range (`name` matches sit at 0.90; the weakest mode, `ticker_context`, used for project names that are also common words like Optimism, Stellar, or Sky, sits at 0.60). Filter on `match_mode`/`confidence` if a strategy cannot tolerate a false-positive word collision.
- **`corroboration`** counts how many independent sources carried the same `(symbol, category)` inside the window — the strongest single indicator that a story is real rather than one outlet syndicated by others.
- **`category` spans crypto-native and macro/policy catalysts.** `hl_listing`/`hl_delisting` are sourced from CryptoDataAPI's own Hyperliquid universe diff rather than any news feed — exact and immediate, and the only coverage a brand-new listing gets before it has a profile or press coverage. On 2026-08-21 the taxonomy gained nine market-wide policy/macro categories (`legislation`, `executive_signal`, `rulemaking`, `restrictive_policy`, `sovereign_bid`, `strategic_reserve`, `pro_crypto_eo`, `macro_liquidity`, `macro_tightening`) after a White House crypto event, a CLARITY Act push, and a doubling of Treasury debt buybacks moved BTC roughly 10% and liquidated about $3B of shorts on 2026-08-20 while `/news/market-moving` recorded **zero** events — the taxonomy had no rule yet for legislation, executive action, agency rulemaking, or a sovereign buyer. These policy categories resolve to `symbol: "MARKET"` when a headline names no coin. Existing crypto-native categories continue alongside them, e.g. `treasury_buy` for corporate/public-company crypto purchases.
- **A related sign-error fix landed the same day (2026-08-21).** The separate `/api/v1/policy/headlines` feed (see [[crypto-policy-shock-trading]]) had an unbounded "ban" rule that scored any headline containing "banking", "banks", or "banner" as a maximum-severity regulatory ban — including constructive stories like "Banking Regulator Races to Finalize GENIUS Act Stablecoin Rules." Policy-adjacent reliability across both the headline sidecar and this news family's new policy categories has been more trustworthy since that fix.
- **Sourcing is free and keyless throughout**: publisher RSS (The Block, CoinDesk, Cointelegraph, Decrypt, The Defiant, CryptoSlate, Bitcoin Magazine), OKX announcements, whitehouse.gov, and roughly 25 project blogs, Discourse governance forums, and GitHub release feeds for larger perps. Latency runs **~30 seconds to 5 minutes behind the source** — this is a context and event-study feed, not a listing-sniping race winner. There is **no X/Twitter coverage** (no free read tier exists for it), so anything breaking there reaches this feed minutes later via the outlets that pick it up.
- **For a faster forced-flow tripwire**, see `/market-intelligence/squeeze-alerts` on [[cryptodataapi-market-intelligence]] — it reads the liquidation stream directly rather than RSS, and on 2026-08-19 flagged a BTC short-liquidation spike 23 minutes before the first related headline qualified for this tape.

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/news/market-moving?min_impact=0.6"
```

## Related

- [[cryptodataapi]] — hub page with auth, plans, and the full category map
- [[cryptodataapi-market-intelligence]] — `/market-intelligence/squeeze-alerts`, the faster liquidation-stream tripwire that complements this RSS-latency feed
- [[cryptodataapi-sentiment]] — Fear & Greed and stablecoin sentiment context alongside catalyst-level signals
- [[cryptodataapi-backtesting]] — the wider historical/Parquet archive this family's `news_events` type joins
- [[crypto-policy-shock-trading]], [[news-trading]] — strategy pages built to consume this data
- [[policy-shock-regime]], [[event-catalyst-regime]] — regime pages this news family feeds
- [[hyperliquid]] — the perp universe this family is scoped to

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-08-26)
- https://cryptodataapi.com/changelog — 2026-08-18, 2026-08-19, and 2026-08-21 entries (fetched 2026-08-26)

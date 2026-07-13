---
title: "CryptoDataAPI — Coins"
type: source
created: 2026-07-13
updated: 2026-07-13
status: good
tags: [data-provider, crypto, api, coins, market-cap, screening]
aliases: ["CDA Coins", "CryptoDataAPI Coins", "cryptodataapi coins endpoints"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
source_author: "CryptoDataAPI"
confidence: high
related: ["[[cryptodataapi]]", "[[cryptodataapi-market-data]]", "[[cryptodataapi-dex]]", "[[cryptodataapi-strategy-baskets]]", "[[market-cap]]", "[[crypto-overview]]", "[[coingecko]]"]
---

The Coins category of [[cryptodataapi]] serves aggregated profiles for 500+ crypto assets: paginated market-cap rankings, name/symbol search, top-N lists, and a category/theme taxonomy. It is the universe-definition layer of the API — the place strategies go to answer "which coins exist, how big are they, and what theme do they belong to" before pulling prices or signals from other categories.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/coins | Paginated coin list by market cap | page, per_page (max 250) | Free |
| GET | /api/v1/coins/search | Search by name/symbol | q | Free |
| GET | /api/v1/coins/top | Top N by market cap | limit (1-100, default 20) | Free |
| GET | /api/v1/coins/categories | All unique categories | — | Free |
| GET | /api/v1/coins/category-groups | Curated 20+ category themes | limit | Free |
| GET | /api/v1/coins/{symbol} | Single coin profile | symbol (e.g. BTC) | Pro+ |

## Live Data

Every endpoint in this category returns **current state**: today's market-cap ordering (`/coins`, `/coins/top`), the present category taxonomy (`/coins/categories`, `/coins/category-groups`), and the latest profile snapshot for a single asset (`/coins/{symbol}`). Rankings and profiles reflect the market as of the request.

## Historical Data

The Coins category has no history endpoints of its own. For price and volume history on a coin surfaced here, use the klines and history endpoints in [[cryptodataapi-market-data]]; for point-in-time historical universes (what the ranking looked like on a past date), use the dated snapshots in [[cryptodataapi-backtesting]].

## Trading Applications

- **Universe construction** — pull `/coins?per_page=250` to define a tradable universe ranked by [[market-cap]], then filter by liquidity before strategy assignment
- **Thematic rotation** — `/coins/category-groups` maps assets into 20+ curated themes, the raw input for sector-rotation ideas across the [[crypto-overview]] landscape
- **Symbol resolution** — `/coins/search?q=` normalises tickers and names before joining data from other providers such as [[coingecko]]
- **Basket seeding** — categories feed directly into the curated meta-baskets served by [[cryptodataapi-strategy-baskets]]
- **Screening pipeline entry point** — top-N by market cap (`/coins/top`) is the standard first stage before regime and momentum filters from other API categories

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/coins/top?limit=50"
```

## Related

- [[cryptodataapi]] — hub page with auth, tiers, and the full category map
- [[cryptodataapi-market-data]] — Binance spot prices and klines for coins in this universe
- [[cryptodataapi-dex]] — long-tail DEX/memecoin tokens not in the aggregated 500+ set
- [[cryptodataapi-strategy-baskets]] — thematic meta-baskets built on the category taxonomy
- [[cryptodataapi-backtesting]] — historical point-in-time snapshots
- [[market-cap]], [[crypto-overview]], [[coingecko]]

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)

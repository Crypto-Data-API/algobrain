---
title: "CryptoDataAPI — On-Chain Intelligence"
type: source
created: 2026-07-13
updated: 2026-09-03
status: good
tags: [data-provider, crypto, api, on-chain, exchange-flows, miners, whales, stablecoins, mvrv]
aliases: ["CryptoDataAPI On-Chain", "CDA On-Chain", "On-Chain Intelligence API"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
confidence: high
related: ["[[cryptodataapi]]", "[[exchange-netflow]]", "[[mvrv]]", "[[miner-capitulation-bottom]]", "[[whale-onchain-flows]]", "[[stablecoin-supply]]", "[[cryptodataapi-market-intelligence]]", "[[cryptodataapi-sentiment]]", "[[glassnode]]"]
---

The On-Chain Intelligence category of [[cryptodataapi]] reads blockchain-native supply and flow signals: CEX stablecoin reserves and a dry-powder z-score, per-symbol exchange inflow/outflow, real-time whale-deposit spike alerts, BTC miner reserves and the Hash Ribbon state, MVRV-based dormancy zones, whale accumulation scores, and a composite On-Chain Health score. It is the API-first counterpart to dashboards like [[glassnode]].

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/on-chain/stablecoin-reserves | CEX stablecoin reserves (ETH/Tron/BSC); rising = dry powder | — | — |
| GET | /api/v1/on-chain/stablecoin-reserves/dry-powder | Dry-powder z-score signal (accumulating/neutral/depleting) | — | — |
| GET | /api/v1/on-chain/exchange-flows/{symbol} | CEX inflow/outflow, 1h/6h/24h/7d windows, per-exchange 24h breakdown | symbol | — |
| GET | /api/v1/on-chain/exchange-flows/spike-alerts | Large transfers (>=$1M default), real-time whale deposits to CEX | — | — |
| GET | /api/v1/on-chain/miners/reserves | BTC miner pool reserves + flows (Foundry/AntPool/F2Pool/ViaBTC/Binance Pool) | — | — |
| GET | /api/v1/on-chain/miners/hash-ribbon | Hash Ribbon state (30dMA vs 60dMA): capitulation/recovery/normal | — | — |
| GET | /api/v1/on-chain/dormancy/btc | BTC MVRV + supply-shock signals, zone classification (capitulation-euphoria) | — | — |
| GET | /api/v1/on-chain/whales | Top-100 non-CEX holders (ERC-20s) | — | — |
| GET | /api/v1/on-chain/whales/{symbol} | Top holders per token + balance deltas | symbol | — |
| GET | /api/v1/on-chain/whales/accumulation-score | Aggregate `signal` across all tracked ERC-20s + per-token counts | — | — |
| GET | /api/v1/on-chain/whales/accumulation-score/{symbol} | Per-token `signal` + per-window deltas, ERC-20 only | symbol | — |
| GET | /api/v1/on-chain/score | On-Chain Health composite 0-100 | — | — |

Tier "—" = not marked with a plan gate in the API docs; standard plan rate limits apply.

> [!warning] Whole `/on-chain/whales*` family temporarily disabled (2026-09-02 recheck)
> `/on-chain/whales`, `/on-chain/whales/{symbol}`, `/on-chain/whales/accumulation-score`, and `/on-chain/whales/accumulation-score/{symbol}` all now return the API's "🚧 Coming soon" placeholder — the entire whale-tracking family is temporarily disabled, not just the top-holder pair. There is currently **no working CryptoDataAPI whale-accumulation signal**. Fall back to `/quant/whales` ([[cryptodataapi-regimes]] — live Hyperliquid ≥$100k-account positioning, a perp-book proxy rather than on-chain spot accumulation) and `/on-chain/exchange-flows/spike-alerts` (still live) until the family is re-enabled.
>
> **Path history:** the endpoint used to be a flat `/on-chain/whale-score/{symbol}`; the live spec now nests it as `/on-chain/whales/accumulation-score/{symbol}` (plus a bare `/on-chain/whales/accumulation-score` aggregate) under the same family as the disabled top-holder routes.
>
> **Scope change:** once re-enabled, both accumulation-score routes cover **ERC-20 tokens only — USDT/USDC/WBTC/WETH** — not native BTC. Pages on this wiki that cite it for BTC (e.g. via `WBTC` as the closest wrapped proxy) should be read with that caveat.
>
> **Response shape changed too:** the live schema (`WhaleAccumulationScoreResponse`) is `{signal: string, counts?: {token: int}, tracked_tokens?: [string], symbol?: string, deltas?: {window: {available: bool, delta: number|null, pct_change: number|null}}, reason?: string}`. The API's own docs confirm `signal` is a categorical verdict — **`accumulating` / `neutral` / `distributing` / `unknown`** (the aggregate route's description spells this out) — **not** a continuous 0-100 score, and per-symbol signals stay `unknown` until the collector has ≥7 days of history. Any page on this wiki describing a numeric "≥ 60/100" or "≥ 65" whale-score threshold is describing the pre-rename endpoint's assumed shape, not this one; those thresholds need recalibrating to the `accumulating`/`neutral`/`distributing` verdict once the endpoint ships.

## Live Data

Current-state reads: `/stablecoin-reserves` and its `/dry-powder` signal, `/exchange-flows/{symbol}` (rolling 1h-7d windows with a per-exchange 24h breakdown), `/exchange-flows/spike-alerts` (real-time large transfers), `/miners/reserves`, `/miners/hash-ribbon`, `/dormancy/btc`, and the composite `/score`.

## Historical Data

`/whales/accumulation-score/{symbol}` is meant to return a historical accumulation-score timeseries via its `deltas` windows, but see the disabled/ERC-20-scope warning above — it is not currently usable for majors like BTC/ETH. Longer stablecoin market-cap history lives in [[cryptodataapi-market-intelligence]] (`/market-intelligence/stablecoin-history`) and [[cryptodataapi-sentiment]] (`/sentiment/stablecoins/remote-history`), with point-in-time snapshots in [[cryptodataapi-backtesting]].

## Trading Applications

- [[exchange-netflow]] — per-symbol inflow/outflow windows plus spike alerts flag whale deposits to CEXs (sell pressure) versus withdrawals (accumulation)
- [[mvrv]] — `/dormancy/btc` maps MVRV and supply-shock signals onto a capitulation-to-euphoria zone classification for cycle positioning
- [[miner-capitulation-bottom]] — the Hash Ribbon endpoint (30d vs 60d hashrate MA) plus miner pool reserves time contrarian entries around miner stress
- [[whale-onchain-flows]] — whale accumulation scores and >=$1M transfer alerts turn large-holder behaviour into tradeable signals
- [[stablecoin-supply]] — CEX stablecoin reserves and the dry-powder z-score measure sidelined buying power before it hits order books

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/on-chain/exchange-flows/BTC"
```

## Related

- [[cryptodataapi]] — hub page with auth, plans, and the full category map
- [[cryptodataapi-market-intelligence]] — exchange BTC balance, ETF flows, cycle indicators
- [[cryptodataapi-sentiment]] — stablecoin flows and Fear & Greed
- [[cryptodataapi-backtesting]] — historical snapshot archives
- [[exchange-netflow]], [[mvrv]], [[whale-onchain-flows]], [[stablecoin-supply]] — concept pages
- [[glassnode]] — dashboard-first on-chain analytics alternative

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)

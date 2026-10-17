---
title: "CryptoDataAPI — On-Chain Intelligence"
type: source
created: 2026-07-13
updated: 2026-10-17
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
| GET | /api/v1/on-chain/exchange-flows/{symbol}/history | Archived CEX inflow/outflow from 2026-05-28: trailing 1h/24h `inflow`/`outflow`/`net`, `chains`, `per_exchange_1h` (new 2026-10-08) | symbol, start, end (≤93 days, default last 7), interval (`1h` / `raw`), exchange, chain | — |
| GET | /api/v1/on-chain/exchange-flows/spike-alerts | Large transfers (>=$1M default), real-time whale deposits to CEX; each alert carries `source` (2026-10-08) | min_amount, limit, symbol, exchange, chain, direction, source | — |
| GET | /api/v1/on-chain/miners/reserves | BTC miner pool reserves + flows (Foundry/AntPool/F2Pool/ViaBTC/Binance Pool) | — | — |
| GET | /api/v1/on-chain/miners/hash-ribbon | Hash Ribbon state (30dMA vs 60dMA): capitulation/recovery/normal | — | — |
| GET | /api/v1/on-chain/dormancy/btc | BTC MVRV + supply-shock signals, zone classification (capitulation-euphoria) | — | — |
| GET | /api/v1/on-chain/whales | Top-100 non-CEX holders (ERC-20s) — **disabled** (503 `coming_soon`; not in the spec since 2026-10-09) | — | — |
| GET | /api/v1/on-chain/whales/{symbol} | Top holders per token + balance deltas — **disabled** (503 `coming_soon`; not in the spec since 2026-10-09) | symbol | — |
| GET | /api/v1/on-chain/whales/accumulation-score | Aggregate `signal` across all tracked ERC-20s + per-token counts — **disabled** (503 `coming_soon`; not in the spec since 2026-10-09) | — | — |
| GET | /api/v1/on-chain/whales/accumulation-score/{symbol} | Per-token `signal` + per-window deltas, ERC-20 only — **disabled** (503 `coming_soon`; not in the spec since 2026-10-09) | symbol | — |
| GET | /api/v1/on-chain/score | On-Chain Health composite 0-100 | — | — |

Tier "—" = not marked with a plan gate in the API docs; standard plan rate limits apply.

> [!warning] Whole `/on-chain/whales*` family temporarily disabled (2026-09-02 recheck; unlisted from the spec 2026-10-09)
> **Update 2026-10-09:** the four `/on-chain/whales*` routes are no longer listed in the OpenAPI spec while whale tracking is disabled. They still answer `503` with `{"detail": {"status": "coming_soon", ...}}` (confirmed live 2026-10-17), and they return to the spec when tracking ships. They stay in the table above for reference.
>
> `/on-chain/whales`, `/on-chain/whales/{symbol}`, `/on-chain/whales/accumulation-score`, and `/on-chain/whales/accumulation-score/{symbol}` all now return the API's "🚧 Coming soon" placeholder — the entire whale-tracking family is temporarily disabled, not just the top-holder pair. There is currently **no working CryptoDataAPI whale-accumulation signal**. Fall back to `/quant/whales` ([[cryptodataapi-regimes]] — live Hyperliquid ≥$100k-account positioning, a perp-book proxy rather than on-chain spot accumulation) and `/on-chain/exchange-flows/spike-alerts` (still live) until the family is re-enabled.
>
> **Path history:** the endpoint used to be a flat `/on-chain/whale-score/{symbol}`; the live spec now nests it as `/on-chain/whales/accumulation-score/{symbol}` (plus a bare `/on-chain/whales/accumulation-score` aggregate) under the same family as the disabled top-holder routes.
>
> **Scope change:** once re-enabled, both accumulation-score routes cover **ERC-20 tokens only — USDT/USDC/WBTC/WETH** — not native BTC. Pages on this wiki that cite it for BTC (e.g. via `WBTC` as the closest wrapped proxy) should be read with that caveat.
>
> **Response shape changed too:** the live schema (`WhaleAccumulationScoreResponse`) is `{signal: string, counts?: {token: int}, tracked_tokens?: [string], symbol?: string, deltas?: {window: {available: bool, delta: number|null, pct_change: number|null}}, reason?: string}`. The API's own docs confirm `signal` is a categorical verdict — **`accumulating` / `neutral` / `distributing` / `unknown`** (the aggregate route's description spells this out) — **not** a continuous 0-100 score, and per-symbol signals stay `unknown` until the collector has ≥7 days of history. Any page on this wiki describing a numeric "≥ 60/100" or "≥ 65" whale-score threshold is describing the pre-rename endpoint's assumed shape, not this one; those thresholds need recalibrating to the `accumulating`/`neutral`/`distributing` verdict once the endpoint ships.

### Exchange-flow history (new 2026-10-08)

**`GET /on-chain/exchange-flows/{symbol}/history`** archives the rolling windows of the live `/exchange-flows/{symbol}` route. They have been sampled roughly every 30 minutes since **2026-05-28** (the changelog says every ~10-40 minutes). Each point carries:

- `ts`, in unix **seconds**, not milliseconds (verified live 2026-10-17: BTC points read `ts: 1792110244`, and the response's `start` / `end` echo seconds too). Most other CryptoDataAPI routes stamp milliseconds, so convert before joining to candles or funding bars.
- The trailing **1h** and **24h** `inflow_*`, `outflow_*` and `net_*`, summed across chains, and across exchanges unless `exchange` is given.
- `chains`, the list of chains summed.
- `per_exchange_1h`, the 1h window per exchange.

`interval=1h` (default) keeps the last sample in each UTC hour. `raw` returns every sample, and their 1h windows overlap. Filter with `exchange` (e.g. `binance`) and `chain` (e.g. `eth`, `tron`). `start` / `end` accept ISO 8601, unix seconds or unix ms. `end` is exclusive, the default range is the last 7 days, and the maximum is 93 days.

**Amounts are in the token's own units, except USDT/USDC/DAI, which are USD.** The response's `unit` field says which. Live check on 2026-10-17 for USDT (2026-10-16 00:00 to 02:00 UTC): `unit: "USD"`, chains `arb, bsc, eth, sol`, and `net_24h` of +$178.5M and then +$145.2M. The rows are trailing windows sampled on a timer, so do not sum successive `net_24h` points.

### Spike alerts: `source`, filters and an archive (2026-10-08)

- Each alert now has **`source`**. `transfer` is a decoded Transfer event with a real counterparty address. `balance_delta` is inferred from a CEX wallet's balance change, and can be the exchange moving funds between its own hot and cold wallets. Live rows on 2026-10-17 showed `balance_delta` alerts with `counterparty: "balance_delta"`. **Filter to `source=transfer` for a signal about real deposits and withdrawals.**
- New optional filters: `symbol`, `exchange`, `chain`, `direction` (`inflow` / `outflow`) and `source`, alongside `min_amount` (USD, default $1M) and `limit`.
- **Timestamps are unix seconds (verified 2026-10-17).** `alerts[].ts` and the top-level `as_of` are seconds (`ts: 1792235340`), not milliseconds. In the `exchange_flow_spikes` archive the snapshot `time` is milliseconds while each row's `data[].ts` stays in seconds.
- **Archived.** Every alert is written to the new `exchange_flow_spikes` snapshot type on `/backtesting/snapshots`, from **2026-10-08 00:25 UTC**. Each 5-minute snapshot holds only the rows first seen in that tick. The live route keeps only the last 500 rows (about 10 hours). See [[cryptodataapi-backtesting]].

### On-Chain Health score: `exchange_flow` fix and weighting (2026-10-08)

> [!warning] `exchange_flow` scores before 2026-10-08 are wrong
> Until 2026-10-08 the `exchange_flow` component of `/on-chain/score` summed **every** tracked token's 24h flow in its own native units. PEPE, SHIB and BONK token counts therefore showed up as $100B-$1T of "net flow" and pinned the component at 20 or 80. It now scores the **USDT/USDC/DAI 24h net only**. Treat any `exchange_flow` score or `reason` from before this change as wrong, and the composite `score` that included it as biased. To rebuild the stablecoin net for past days, use `/exchange-flows/USDT/history` (and USDC, DAI), which reaches back to 2026-05-28. Live on 2026-10-17 the component read `reason: "net_24h=$-338,860,658"` with `raw.net_24h_usd`, `total_in` and `total_out`.

**Docs correction: missing components are excluded, not scored 50.** A component with no data gets weight 0 and the remaining weights are renormalised. It does not contribute a neutral 50, as `llms-full.txt` used to say. When no component has data, `sentiment` is `unknown`. `whale_accumulation` is currently always excluded, because whale tracking is disabled. It reports `reason: "no_data"` with a placeholder `score` of 50 at `weight: 0`. `mvrv` showed the same pattern live (`zone=unknown`, weight 0) on 2026-10-17. A component's displayed `score` of 50 therefore does not mean it is neutral; check its `weight`.

## Live Data

Current-state reads: `/stablecoin-reserves` and its `/dry-powder` signal, `/exchange-flows/{symbol}` (rolling 1h-7d windows with a per-exchange 24h breakdown), `/exchange-flows/spike-alerts` (real-time large transfers), `/miners/reserves`, `/miners/hash-ribbon`, `/dormancy/btc`, and the composite `/score`.

## Historical Data

**Exchange flows** now have a history route: `/exchange-flows/{symbol}/history` back to 2026-05-28, plus the `exchange_flow_spikes` snapshot archive from 2026-10-08 (both above). `/whales/accumulation-score/{symbol}` is meant to return a historical accumulation-score timeseries via its `deltas` windows, but see the disabled/ERC-20-scope warning above — it is not currently usable for majors like BTC/ETH. Longer stablecoin market-cap history lives in [[cryptodataapi-market-intelligence]] (`/market-intelligence/stablecoin-history`) and [[cryptodataapi-sentiment]] (`/sentiment/stablecoins/remote-history`), with point-in-time snapshots in [[cryptodataapi-backtesting]].

## Trading Applications

- [[exchange-netflow]] — per-symbol inflow/outflow windows plus spike alerts flag whale deposits to CEXs (sell pressure) versus withdrawals (accumulation); `/exchange-flows/{symbol}/history` makes netflow rules backtestable from 2026-05-28
- [[mvrv]] — `/dormancy/btc` maps MVRV and supply-shock signals onto a capitulation-to-euphoria zone classification for cycle positioning
- [[miner-capitulation-bottom]] — the Hash Ribbon endpoint (30d vs 60d hashrate MA) plus miner pool reserves time contrarian entries around miner stress
- [[whale-onchain-flows]] — whale accumulation scores and >=$1M transfer alerts turn large-holder behaviour into tradeable signals
- [[stablecoin-supply]] — CEX stablecoin reserves and the dry-powder z-score measure sidelined buying power before it hits order books

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/on-chain/exchange-flows/BTC"

# Hourly stablecoin CEX netflow history (USD), last 30 days
curl -H "X-API-Key: $CDA_KEY"   "https://cryptodataapi.com/api/v1/on-chain/exchange-flows/USDT/history?start=2026-09-17"

# Only decoded transfers, not wallet-balance inferences
curl -H "X-API-Key: $CDA_KEY"   "https://cryptodataapi.com/api/v1/on-chain/exchange-flows/spike-alerts?source=transfer&direction=inflow"
```

## Related

- [[cryptodataapi]] — hub page with auth, plans, and the full category map
- [[cryptodataapi-market-intelligence]] — exchange BTC balance, ETF flows, cycle indicators
- [[cryptodataapi-sentiment]] — stablecoin flows and Fear & Greed
- [[cryptodataapi-backtesting]] — historical snapshot archives
- [[exchange-netflow]], [[mvrv]], [[whale-onchain-flows]], [[stablecoin-supply]] — concept pages
- [[glassnode]] — dashboard-first on-chain analytics alternative

## Sources

- CryptoDataAPI changelog releases 2026-10-08 and 2026-10-09 (via `GET /api/v1/changelog`, fetched 2026-10-17), the live OpenAPI spec (`/api/v1/on-chain/exchange-flows/{symbol}/history` params and description, spike-alert filter params, `/api/v1/on-chain/score` description; the `/on-chain/whales*` routes absent; fetched 2026-10-17), and live calls on 2026-10-17 to `/exchange-flows/USDT/history`, `/spike-alerts?source=balance_delta`, `/backtesting/snapshots?data_type=exchange_flow_spikes`, `/on-chain/score` and `/on-chain/whales` (503 `coming_soon`)
- https://cryptodataapi.com/api/docs (fetched 2026-07-13)

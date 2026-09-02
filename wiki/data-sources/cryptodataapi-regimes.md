---
title: "CryptoDataAPI — Market & Quant Regimes"
type: source
created: 2026-07-13
updated: 2026-09-02
status: good
tags: [data-provider, crypto, api, market-regime, regime-detection, hmm, volatility, liquidity, gamma-exposure, event-risk]
aliases: ["CryptoDataAPI Regimes", "CDA Regimes", "CryptoDataAPI Quant Probabilities", "CryptoDataAPI Regime Engine"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
confidence: high
related: ["[[cryptodataapi]]", "[[cryptodataapi-indicators]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-strategy-baskets]]", "[[cryptodataapi-market-health]]", "[[cryptodataapi-derivatives]]", "[[cryptodataapi-supply]]", "[[crypto-market-regime-taxonomy]]", "[[regime-strategy-playbook]]", "[[regime-detection]]", "[[market-regime-detection-ml]]", "[[volatility-regime]]", "[[regime-matrix]]", "[[gamma-exposure]]", "[[hidden-markov-models]]"]
---

CryptoDataAPI's regime endpoints are the largest signal surface on the API: eight complementary regime families that classify the market by long-horizon cycle state, short-horizon HMM probabilities, volatility, liquidity fragility, meme-coin lifecycle, forward catalysts, security stress, and geopolitical/policy shock. Together they map directly onto this wiki's [[crypto-market-regime-taxonomy]] and drive the [[regime-strategy-playbook]] — each family exposes a current-state endpoint, most add a 0-100 composite score, per-symbol detail, and a refresh trigger.

## Endpoints

### Market Regimes (long-horizon, 10 states)

The slow-moving cycle classifier. Taxonomy: **Structural Shock, Established Bear, Capitulation, Bottoming, Early Recovery, BTC-Led Bull, Broadening Bull, Broad Bull, Speculative Euphoria, Distribution/Deleveraging**.

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/regimes | 10-state taxonomy + current regime + rationale | — | — |
| GET | /api/v1/regimes/current | Current regime only (trimmed) | — | — |

### Quant Probabilities (HMM 6-regime engine)

A [[hidden-markov-models|Hidden Markov Model]] engine refreshed every 15 minutes. Taxonomy: **strong_trend_bull, strong_trend_bear, range_low_vol, choppy_high_vol, vol_spike, squeeze**. Beyond regime probabilities it covers positioning splits, [[gamma-exposure|Gamma Exposure]], and whale activity.

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/quant/market | Whole-market regime + probability buckets | 4h/24h horizons | Pro+ |
| GET | /api/v1/quant/coins | All ~200 HL perps (trimmed) | — | Pro |
| GET | /api/v1/quant/coins/risk | Bulk per-coin risk model | — | Pro |
| GET | /api/v1/quant/coins/{symbol} | Full per-coin probability matrix | symbol | Pro |
| GET | /api/v1/quant/history | Point-in-time probability records (backtest) | — | Pro Plus |
| GET | /api/v1/quant/regimes/history | Full 6-regime Parquet download (2020-yesterday) | — | Pro Plus |
| GET | /api/v1/quant/timeline | Daily market regime labels (2019-now) | — | Pro Plus |
| GET | /api/v1/quant/positioning | Trader type split (MM/whale/other) | per-coin optional | Pro |
| GET | /api/v1/quant/gex | Gamma Exposure (MM inventory + liquidation profile) | per-coin optional | Pro |
| GET | /api/v1/quant/whales | >=$100k account whale activity summary | — | Pro+ |
| GET | /api/v1/quant/whales/history | Daily whale positioning timeseries | days 7-540 | Pro Plus |
| GET | /api/v1/quant/model | Model transparency (version, metrics, sha256) | — | — |
| GET | /api/v1/quant/regimes | 6-regime taxonomy (id, label, stance) | — | — |
| POST | /api/v1/quant/refresh | Force immediate inference | — | Pro Plus |

`/quant/gex` and `/quant/positioning` moved to the **Pro** tier on 2026-07-10 — Pro keys had been incorrectly 403'ing on both before the fix.

**`/quant/gex` breaking change (2026-06-27):** a single-symbol query (`?symbol=X`) now returns the same bulk envelope as the unfiltered call — `{scope, note, timestamp, meta, coins:{X:{...}}}` — narrowed to one coin, rather than a bare per-coin object. Any integration or example that expects `?symbol=X` to return a flat per-coin object needs updating to read `coins[X]` out of the envelope. The response also gained:
- **`regime.confidence`** (0-1) — scales with market-maker account count and gross book depth behind the read, so thin-sample regimes can be down-weighted
- **Capped `regime.flip_price` / `gamma_flip`** — now bounded to within +/-30% of mark and returns `null` when there is no in-band liquidation crossover, instead of the previously possible absurd out-of-range levels
- **Per-coin `distribution_context`** — trailing-30-day percentile ranks of near-mark cluster density, `|distance to flip|`, normalized MM skew (`mm_net_delta/mm_gross`), regime score, and funding rate; history is forward-only from the change date, hourly samples
- **`regime.inputs.realized_liq`** now populates for Hyperliquid's 1000x-multiplier meme perps (kPEPE, kBONK, etc.), which previously had no realized-liquidation input

### Volatility Regime

Per-asset [[volatility-regime]] classifier. Taxonomy: **compressed, expanding, vol_shock, mean_reverting, normal**.

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/volatility/regime | Per-asset vol regimes | backfillable from daily klines | — |
| GET | /api/v1/volatility/regime/score | Market-wide vol-stress composite 0-100 | — | — |
| GET | /api/v1/volatility/regime/{symbol} | Per-asset detail + 60d history | symbol | Pro+ |
| POST | /api/v1/volatility/regime/refresh | Force recompute | — | Pro+ |

### Liquidity & Market Depth

Order-book-derived regime detection: depth, spread, and OI-vs-price divergence rolled into a fragility score.

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/liquidity/depth | Per-coin depth/spread at 10/25/50/100 bps (live) | — | — |
| GET | /api/v1/liquidity/oi-divergence | OI vs price divergence | 1h/4h/24h windows | — |
| GET | /api/v1/liquidity/regime | Regime label + fragility score 0-100 | — | Pro+ |
| GET | /api/v1/liquidity/regime/score | Composite score + sentiment band | — | Pro+ |
| GET | /api/v1/liquidity/depth/{coin} | 24h rolling depth history, 1-min samples | coin | BTC free; full universe Pro+ |

### Meme Regime (lifecycle classifier)

Meme-coin lifecycle states plus a market-wide hype gauge. Taxonomy: **euphoric, distribution, ignition, bleeding, dormant**.

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/meme/regime | Per-asset meme lifecycle | — | — |
| GET | /api/v1/meme/regime/score | Market-wide meme-hype 0-100 + meme_season flag | — | — |
| GET | /api/v1/meme/regime/{symbol} | Per-asset detail + 60d history | symbol | Pro+ |
| POST | /api/v1/meme/regime/refresh | Force recompute | — | Pro+ |

Per-asset meme-metrics fields include a return-window ladder — `ret_1d`, `ret_7d`, `ret_30d`, and (added 2026-08-25) `ret_90d` — plus `vol_spike`, `vol_pctile_30`, `sma20_extension_pct`, `funding_rate`, `oi_usd`, and `days_in_regime`. `ret_90d` is null for a coin with less than 91 days of daily kline history, and it is not part of the `euphoric`/`distribution`/`ignition`/`bleeding`/`dormant` classifier itself (which uses only `ret_7d`/`ret_30d`) — it is context for judging how the current lifecycle stage fits into the coin's longer-run trend.

### Event / Catalyst Regime

Forward-looking catalyst calendar (unlocks, macro prints, depeg risk, stablecoin mint/burn steps) with a directional bias per event.

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/event/regime | Forward catalyst calendar (unlock/macro/depeg bias) | — | — |
| GET | /api/v1/event/regime/score | Event Risk composite 0-100, baseline 0 | — | — |
| GET | /api/v1/event/calendar | Filterable events up to 30d out | type, symbol, bias | — |
| GET | /api/v1/event/regime/{symbol} | Per-symbol pending catalysts | symbol | Pro+ |
| POST | /api/v1/event/regime/refresh | Force recompute | — | Pro+ |

**`mint` event type (2026-08-19):** `/event/calendar` and `/event/regime*` gained a fourth catalyst type alongside `unlock`/`macro_print`/`depeg` — dated stablecoin mint/burn steps, with `delta_usd` (signed) and `pct_of_supply` fields sizing the move. Bias is `long` on a mint and `short` on a redemption. These are **observed, not scheduled** — they carry `days_until <= 0` since a mint/burn is reported after it happens rather than forecast in advance, unlike the forward-looking unlock and macro-print entries in the same calendar. See also [[cryptodataapi-supply]] for the dedicated `/supply/unlocks` cliff-calendar view that now backs the `unlock` type here.

### Security / Black-Swan Regime

Tail-risk overlay tracking hacks, depegs, and abnormal flows.

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/security/regime | Recent hacks/depegs + Security Stress score | — | — |
| GET | /api/v1/security/regime/score | Composite 0-100: 45% hack, 30% flow, 25% depeg | — | — |
| GET | /api/v1/security/events | Filterable recent events | 10d lookback | — |
| GET | /api/v1/security/regime/{symbol} | Per-symbol security overlay | symbol | Pro+ |
| POST | /api/v1/security/regime/refresh | Force recompute | — | Pro+ |

### Geopolitical / Policy Regime

Regulatory and macro-policy shock detection built on GDELT news flow, cross-asset stress, and the rate calendar.

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/policy/regime | Policy Risk + signed tilt + rate calendar | — | — |
| GET | /api/v1/policy/regime/score | Composite 0-100: 40% GDELT, 35% cross-asset, 25% rate | — | — |
| GET | /api/v1/policy/headlines | Live regulatory feed (Federal Register/SEC/CFTC) | — | — |
| POST | /api/v1/policy/regime/refresh | Force recompute | — | Pro+ |

## Live Data

Every family's base endpoint returns current state: `/regimes/current` for the 10-state cycle label, `/quant/market` for live HMM probabilities (15-min refresh), and the `/regime` + `/regime/score` pairs for volatility, liquidity, meme, event, security, and policy. `/liquidity/depth` and `/policy/headlines` are live feeds; the POST `/refresh` endpoints force an immediate recompute when you cannot wait for the next scheduled cycle.

## Historical Data

History is concentrated in the quant family at the Pro Plus tier: `/quant/history` serves point-in-time probability records for backtests, `/quant/regimes/history` downloads the full 6-regime Parquet archive (2020-yesterday), `/quant/timeline` gives daily market regime labels back to 2019, and `/quant/whales/history` covers 7-540 days of whale positioning. Per-symbol detail endpoints for volatility, meme, and the indicators family include a rolling 60d history; `/liquidity/depth/{coin}` keeps a 24h rolling window at 1-min resolution. For anything deeper, pair these with [[cryptodataapi-backtesting]].

## Trading Applications

- **Regime-gated strategy selection** — map the 10-state and 6-state labels onto the [[regime-strategy-playbook]] and [[regime-matrix]] to switch between trend, mean-reversion, and defensive books
- **HMM signal research** — `/quant/history` and `/quant/timeline` provide labelled data for [[market-regime-detection-ml]] and validating your own [[regime-detection]] models against a production [[hidden-markov-models|HMM]]
- **Volatility positioning** — the `compressed`/`expanding`/`vol_shock` states from [[volatility-regime]] time straddle-style entries and position-size cuts before expansion
- **Dealer-flow awareness** — `/quant/gex` exposes [[gamma-exposure]] and liquidation profiles, flagging pin zones and squeeze fuel; `/liquidity/regime` fragility warns when books cannot absorb a shock
- **Tail-risk overlays** — event, security, and policy scores act as risk-off gates in the [[crypto-market-regime-taxonomy]]: de-gross when Security Stress or Event Risk spikes off its 0 baseline

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/quant/market"
```

## Related

- [[cryptodataapi]] — provider hub (auth, tiers, category map)
- [[cryptodataapi-indicators]] — Signum RGG and technical state, natural companions to regime labels
- [[cryptodataapi-backtesting]] — point-in-time archive for regime-aware backtests
- [[cryptodataapi-strategy-baskets]] — meta-baskets to deploy per regime
- [[cryptodataapi-market-health]] — dual-score health composite
- [[cryptodataapi-derivatives]], [[cryptodataapi-market-intelligence]] — the raw positioning data behind several regime inputs
- [[crypto-market-regime-taxonomy]], [[regime-strategy-playbook]], [[regime-detection]]

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)

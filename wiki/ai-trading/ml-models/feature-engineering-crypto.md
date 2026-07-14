---
title: "Feature Engineering for Crypto ML"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [ai-trading, machine-learning, crypto, on-chain, funding-rate]
aliases: ["Crypto Feature Engineering", "Crypto ML Features"]
domain: [machine-learning, crypto, market-microstructure]
prerequisites: ["[[feature-engineering-finance]]", "[[funding-rates]]", "[[stationarity]]"]
difficulty: advanced
related: ["[[feature-engineering-finance]]", "[[feature-selection-trading]]", "[[crypto-signal-library]]", "[[information-coefficient]]", "[[signal-orthogonalization]]", "[[funding-rates]]", "[[open-interest]]", "[[exchange-netflow]]", "[[order-book]]", "[[ml-trading-pipeline]]"]
---

Feature engineering for crypto ML is the craft of turning crypto-native raw data — perpetual [[funding-rates|funding]], [[open-interest]], L2 [[order-book]] state, cross-venue [[basis]], and [[on-chain-analysis|on-chain]] flows — into stationary, leakage-free predictors. It inherits the discipline of [[feature-engineering-finance|financial feature engineering]] (returns over levels, rolling z-scores, no look-ahead) but adds a distinct set of data sources and a distinct set of traps: markets that never close, a funding cash-flow that behaves like a carry yield, thin low-float alts, and a universe of tokens that constantly dies and delists.

## Why crypto is a different feature problem

- **24/7 markets, no session boundaries.** Equity features lean on the open/close/overnight structure (gap returns, opening auction imbalance, RTH vs. globex). Crypto has none of it — there is no daily reset, no weekend gap in the same sense, and "daily" bars are an arbitrary UTC cut. Features built around session anchors silently break. Use rolling windows anchored to UTC only for reproducibility, and prefer decay-weighted statistics over calendar-day resets.
- **Funding is a real cash flow, not just a sentiment gauge.** In equities the analogue would be a continuously-paid dividend that flips sign; the perp [[funding-rates|funding rate]] is both a positioning signal *and* the carry you actually earn/pay. That dual role means it belongs in features as both a level (positioning z-score) and a return-contribution (carry).
- **Reflexive leverage.** OI, funding, and liquidations feed back on price within hours ([[liquidation-cascade|liquidation cascades]]), so many crypto features are most informative at 1h-24h horizons and decay fast — unlike slow equity value factors.
- **Fragmented venues.** The same asset trades on Binance, [[hyperliquid|Hyperliquid]], Bybit, OKX, Coinbase, plus DEXs. Cross-venue divergences (basis, [[coinbase-premium]]) are themselves signals, but naive aggregation blends incompatible order books.

## Core feature families

### 1. Perp funding features
The [[funding-rates|funding rate]] is the workhorse crypto feature. Derived features:
- **Funding level z-score** — current 8h rate normalized against a trailing 30-90d window. Extreme positive (>0.05%/8h, ~55% annualized) flags crowded longs; deeply negative (<-0.03%/8h) flags capitulation.
- **Funding-carry** — realized cumulative funding paid to a delta-neutral short-perp/long-spot book over the horizon; this is a *return* feature, not a positioning feature (see [[funding-rate-arbitrage]]).
- **Cross-venue funding dispersion** — spread between Binance and Hyperliquid funding for the same coin; wide dispersion signals venue-specific positioning stress.
- **Funding momentum / mean-reversion** — sign and slope of funding over the last N settlements.

### 2. Open interest features
- **OI change vs. price change ([[open-interest|OI]] divergence)** — rising OI with rising price = new longs (continuation bias); rising OI with falling price = new shorts; falling OI = deleveraging. The 1h/4h/24h OI-vs-price divergence is a compact regime feature.
- **OI-normalized liquidations** — liquidation notional divided by OI, a cleaner "how much of the book just got flushed" than raw liquidation USD.
- **OI/market-cap** — leverage intensity per asset; low-float alts can carry OI several times their real float.

### 3. L2 order-book imbalance
From a top-of-book / depth snapshot ([[order-book]], [[order-flow]]):
- **Depth imbalance** — `(bid_depth - ask_depth) / (bid_depth + ask_depth)` at fixed bps bands (10/25/50/100 bps). Positive = buy-side pressure.
- **Microprice deviation** — size-weighted mid vs. arithmetic mid; a short-horizon (seconds-minutes) directional predictor.
- **Spread and depth regime** — spread widening and depth thinning precede volatility expansion; useful as a risk-off gate rather than a directional signal.
- **Slope of the book** — how fast depth accumulates away from mid; steep = resilient, flat = fragile.

### 4. Cross-venue basis
- **Perp-spot basis** — perp mid minus spot index, in bps; persistent positive basis = leveraged-long demand.
- **Calendar/futures basis** — dated-future price vs. spot annualized (see [[basis]], [[basis-trading]]).
- **Coinbase premium** — Coinbase spot minus Binance spot; a proxy for US-institutional net demand.
- **Inter-exchange price dispersion** — standard deviation of the same asset's price across venues; spikes during stress and fragmentation.

### 5. On-chain flow features
- **Exchange netflow** — CEX inflow minus outflow ([[exchange-netflow]]); large *inflows* often precede selling, large *outflows* signal accumulation / self-custody. Normalize by a trailing flow z-score, not raw coin count.
- **Dormancy / MVRV** — coin-days-destroyed and [[mvrv|MVRV]] / [[mvrv-z-score|MVRV-Z]] capture long-term holder behavior; slow features best at multi-week horizons, and BTC-specific.
- **Whale-score** — accumulation/distribution among large holders; per-token when available.
- **Dry-powder (stablecoin reserves)** — rising CEX stablecoin reserves = buying power building; a z-scored macro tailwind feature.
- **Miner reserves / hash-ribbon** — BTC-only supply-side stress signals.

## Crypto-specific stationarity & normalization pitfalls

- **No session reset → use decay-weighted rolling stats.** Because there is no daily close, prefer EWMA means/vols and expanding-then-rolling z-scores over fixed calendar-day windows. Anchor any UTC-day feature explicitly and test that it isn't just encoding the arbitrary cut time.
- **Regime-conditional z-scoring.** A global z-score computed across a full bull+bear sample is non-stationary: a funding z of +2 means something very different in a low-vol range than in a squeeze. Condition normalization on the prevailing [[market-regime]] / [[volatility-regime]] (e.g., separate rolling stats per HMM regime — see [[hidden-markov-model]]) or use a short trailing window so the baseline tracks the regime.
- **Funding as carry vs. funding as signal — keep them separate.** Do not let the same raw funding series enter a model twice under two transforms without acknowledging the collinearity; orthogonalize (see [[signal-orthogonalization]]).
- **Low-float alt illiquidity.** For thin alts, order-book and OI features are dominated by a handful of actors; depth imbalance and OI/float can be manipulated. Winsorize aggressively, floor by dollar-volume, and treat sub-threshold-liquidity names as a separate (or excluded) universe. Numbers derived from <$1-2M daily depth are noise more than signal (rule-of-thumb threshold; tune per book).
- **Dead-token survivorship bias.** A backtest run only over today's listed tokens silently drops the hundreds that delisted or went to zero — manufacturing phantom cross-sectional alpha. Build the feature panel from a *point-in-time* universe that includes tokens as of each historical date, including ones later delisted (use point-in-time daily snapshots).
- **Token age / listing effects.** New listings have unstable funding, no on-chain history, and reflexive early price action. Include a `token_age_days` feature and/or gate features until a minimum history exists; a funding z-score over 20 days of data is not comparable to one over 2 years.
- **Cross-sectional vs. time-series normalization.** For a basket, cross-sectionally rank/z-score each feature *at each timestamp* so BTC's absolute funding doesn't dominate; for a single-asset timing model, use time-series z-scores. Mixing the two leaks cross-sectional information.
- **Look-ahead via revised on-chain data.** On-chain and flow series are sometimes backfilled/revised; a naive pull of "history" may embed later revisions. Prefer the point-in-time snapshot endpoints for training labels.

## Worked normalization example

For a cross-sectional alt basket refreshed every 4h:
1. Pull funding, OI, netflow-z, and depth-imbalance for each coin in the *point-in-time* universe.
2. Winsorize each raw feature at the 1st/99th percentile of the trailing 30d.
3. Compute a **regime-conditional** rolling z-score (window = last 30d of the current [[volatility-regime]] bucket).
4. Cross-sectionally rank within the timestamp so the output is a comparable [-1, 1] score per coin.
5. Screen each candidate feature by [[information-coefficient|rank-IC]] before it ever enters the model (see [[feature-selection-trading]]).

Estimated per-feature rank-IC for durable crypto features sits in the 0.02-0.06 band at 1-7d horizons — comparable to equity factor ICs (speculative; depends heavily on universe, horizon, and cost model). Treat anything much higher in a backtest as a look-ahead or survivorship red flag.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding (Binance + Hyperliquid) for the funding features
- `GET /api/v1/derivatives/open-interest?coin=BTC` and `GET /api/v1/liquidity/oi-divergence` — OI level and OI-vs-price divergence
- `GET /api/v1/hyperliquid/l2-book?coin=BTC` — L2 order-book snapshot for depth-imbalance / microprice
- `GET /api/v1/liquidity/depth` and `GET /api/v1/liquidity/depth/{coin}` — depth/spread at 10/25/50/100 bps
- `GET /api/v1/market-intelligence/coinbase-premium` — Coinbase-vs-Binance premium (US-institutional proxy)
- `GET /api/v1/on-chain/exchange-flows/{symbol}` — CEX inflow/outflow (1h/6h/24h/7d)
- `GET /api/v1/on-chain/dormancy/btc` — BTC MVRV + dormancy zone
- `GET /api/v1/on-chain/whale-score/{symbol}` — whale accumulation score
- `GET /api/v1/on-chain/stablecoin-reserves/dry-powder` — dry-powder z-score

**Historical / point-in-time (for a leakage-free training panel):**
- `GET /api/v1/backtesting/klines` — OHLCV archive (returns, realized vol)
- `GET /api/v1/backtesting/funding` — deep funding archive
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time daily snapshot (defeats survivorship bias)
- `GET /api/v1/backtesting/snapshots/{type}` — historical snapshot by type

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/liquidity/oi-divergence"
```

Auth: `X-API-Key` header. Category pages: [[cryptodataapi-derivatives]], [[cryptodataapi-on-chain]], [[cryptodataapi-market-intelligence]], [[cryptodataapi-backtesting]].

## Related

- [[feature-engineering-finance]] — the general financial-ML feature discipline this specializes
- [[crypto-signal-library]] — the browsable menu of crypto signals and their endpoints
- [[feature-selection-trading]] — pruning the feature set once built
- [[information-coefficient]] — triaging each raw feature before modeling
- [[signal-orthogonalization]] — removing BTC-beta and inter-feature redundancy
- [[funding-rates]], [[open-interest]], [[exchange-netflow]], [[order-book]] — underlying data pages

## Sources

- [[book-advances-in-financial-ml]] — fractional differentiation, point-in-time labeling, and feature-quality-over-model principle, adapted here to crypto data
- [[book-machine-learning-for-asset-managers]] — normalization, multicollinearity, and survivorship pitfalls
- CryptoDataAPI endpoint catalog (verified 2026-07-13) for the data mappings above

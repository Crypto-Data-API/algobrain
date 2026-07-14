---
title: "ML Crypto Price Prediction"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [ai-trading, machine-learning, backtesting, crypto]
aliases: ["ML Crypto Price Prediction", "Crypto ML Pipeline", "Machine Learning Crypto Prediction"]
domain: [machine-learning, ai-trading]
prerequisites: ["[[ml-trading-pipeline]]", "[[feature-engineering-crypto]]", "[[triple-barrier-labeling]]"]
difficulty: advanced
related: ["[[feature-engineering-crypto]]", "[[triple-barrier-labeling]]", "[[meta-labeling]]", "[[purged-kfold-cv]]", "[[probability-of-backtest-overfitting]]", "[[fractional-differentiation]]", "[[ml-trading-pipeline]]", "[[deflated-sharpe-ratio]]", "[[xgboost-trading]]", "[[composite-alpha-blending]]"]
---

# ML Crypto Price Prediction

This is a **buildable, end-to-end pipeline** for predicting crypto price moves with machine learning — not an essay on whether ML "works." It threads together the crypto-specific pieces documented elsewhere in this wiki: a crypto [[feature-engineering-crypto|feature pipeline]] → [[triple-barrier-labeling|triple-barrier labels]] → [[meta-labeling|meta-labeled]] primary/secondary models → [[purged-kfold-cv|purged/combinatorial cross-validation]] → walk-forward validation → deployment. It follows the general [[ml-trading-pipeline]] but is specialized for crypto's data sources, 24/7 microstructure, and — critically — its **short history and thin statistical power** (see the limits section, which you should read before trusting any result).

## Pipeline at a Glance

```
raw data ─► features ─► labels ─► CV/validation ─► model ─► filter/sizing ─► backtest ─► deploy ─► monitor
 (CDA)      (crypto)   (triple-   (purged +        (XGB)   (meta-label)     (costed)   (paper)  (drift)
                        barrier)   walk-forward)
```

## Stage 1 — Feature Pipeline

Build point-in-time features with strictly no look-ahead. Crypto affords data families equities lack; see [[feature-engineering-crypto]] for the full catalog. Core groups:

- **Price/volatility** — returns, realized vol, [[average-true-range|ATR]], and **memory-preserving** transforms via [[fractional-differentiation]] (so a stationary feature still encodes price *level*).
- **Derivatives** — [[funding-rate]] level and z-score, [[open-interest]] change, OI-vs-price divergence, long/short ratio.
- **On-chain** — exchange netflows, whale accumulation score, MVRV/dormancy, stablecoin dry-powder.
- **Regime** — HMM regime probabilities, volatility-regime label, market breadth.
- **Positioning/flow** — liquidation imbalance, whale positioning, taker buy/sell ratio.

Every feature is computed on a rolling window from data available *at that timestamp*, then stored immutably. Consider event-driven bars (dollar or volume bars) rather than fixed time bars so information content per sample is more uniform.

## Stage 2 — Labels (Triple-Barrier)

Label with the [[triple-barrier-labeling|triple-barrier method]]: profit-take, stop-loss, and time barriers, with widths scaled to volatility (ATR or EWMA σ). This yields path-dependent labels that respect crypto's wicks and [[liquidation|liquidation]]-prone paths — a close-to-close label would mislabel a trade that was liquidated mid-window. Record each label's resolution time for purging downstream.

## Stage 3 — Primary Model + Meta-Labeling

Two-model architecture ([[meta-labeling]]):

1. **Primary (side).** Decides direction — can be an economic rule (funding fade, trend, a [[hyperliquid-baskets-overview|basket]] signal) or a first-pass classifier. Tune for **high recall**.
2. **Secondary (meta) filter.** An [[xgboost-trading|XGBoost]] binary classifier predicting whether each primary bet will hit its profit barrier (label from Stage 2). It **vetoes** weak bets and **sizes** strong ones via the classifier probability. This raises precision and F1 without touching the side.

Where several signals feed the side decision, blend them first with [[composite-alpha-blending|composite alpha blending]].

## Stage 4 — Validation Without Leakage

Triple-barrier labels overlap in time, so a random-shuffle split leaks the future. Use:

- **[[purged-kfold-cv|Purged, embargoed k-fold]] / CPCV** — drop training observations whose label windows overlap the test set, add an embargo, and (via combinatorial purged CV) produce a *distribution* of out-of-sample paths rather than a single lucky curve.
- **Sample-uniqueness weights** — down-weight concurrent (redundant) labels so the effective sample is honest.
- **Walk-forward** — refit on an expanding/rolling window that mirrors live deployment, giving one realistic path for deployment simulation. Use CPCV and walk-forward together — they answer different questions.

## Stage 5 — Overfitting Diagnostics

A good backtest number is not evidence of edge until it survives multiple-testing scrutiny:

- **[[probability-of-backtest-overfitting|Probability of Backtest Overfitting (PBO)]]** — from the CPCV path distribution, how often does the in-sample-best configuration underperform out-of-sample? High PBO means the "edge" is selection noise.
- **[[deflated-sharpe-ratio|Deflated Sharpe Ratio]]** — corrects the observed Sharpe for the number of trials, non-normality, and sample length. Report it, not the naïve Sharpe.

## Stage 6 — Backtest, Deploy, Monitor

- **Costed backtest.** Include taker fees, [[slippage]], market impact, and — for perps — expected [[funding-rate|funding]] over the holding window. A gross-profitable model is routinely net-negative in crypto.
- **Paper trade** for 3–6 months on live data; compare realized precision and P&L to the gated backtest.
- **Deploy** with hard risk controls: position limits, daily loss limits, and a kill switch.
- **Monitor** feature drift, realized-vs-expected IC, and meta-model precision; retrain on schedule or on decay ([[alpha-decay]]).

## The Short-History Statistical-Power Problem (read this)

Crypto ML is **fundamentally sample-starved**, and this is its dominant, under-appreciated risk — not model choice.

- **Few independent observations.** Liquid crypto history is short: BTC has traded liquidly since roughly 2013–2015; most alts and perps have only a few years, and Hyperliquid perps far less. Daily bars over "10 years" sound like ~3,600 samples, but they are heavily autocorrelated and dominated by only **~3–4 halving/market cycles** — a handful of genuinely independent macro episodes.
- **Effective sample ≪ nominal sample.** Overlapping triple-barrier labels and serial correlation mean the *effective* number of independent bets is a fraction of the row count. The Fundamental Law's breadth term (see [[composite-alpha-blending]]) is smaller than it looks.
- **Fat tails and regime breaks.** A single event (COVID crash, LUNA/UST, FTX) can dominate the sample and never recur in the same form; a model fit across a regime break can be worse than useless.
- **Multiple testing is rampant.** Cheap data and easy tooling invite thousands of feature/parameter trials; without PBO/DSR correction, a great-looking backtest is the *expected* outcome of enough trials, not evidence of skill.

Practical implications: prefer **simple, regularized models** (start with [[xgboost-trading|gradient-boosted trees]] or logistic regression, not deep nets); prefer **broad cross-sectional breadth** (many coins) over deep single-asset history; **always** report deflated Sharpe and PBO; and treat any single-cycle backtest as a hypothesis, not a validated edge. *[Speculative:]* claims of high-Sharpe crypto ML models trained on a few years of data should be treated with strong skepticism until shown to survive purged CV, PBO, and out-of-sample deployment.

## Getting the Data (CryptoDataAPI)

The whole pipeline is feedable from the CryptoDataAPI market, derivatives, on-chain, regime, and backtesting endpoints.

**Live / recent (features and signals):**
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=1000` — OHLCV for features and label paths
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding features
- `GET /api/v1/liquidity/oi-divergence` — OI-vs-price divergence
- `GET /api/v1/on-chain/exchange-flows/BTC` — netflow features
- `GET /api/v1/quant/market` — HMM regime probabilities
- `GET /api/v1/volatility/regime` — volatility regime labels
- `GET /api/v1/market-intelligence/liquidations` — liquidation imbalance

**Historical (training, labeling, and backtests):**
- `GET /api/v1/backtesting/klines` — full OHLCV archive (Parquet since 2020)
- `GET /api/v1/backtesting/funding` — funding archive
- `GET /api/v1/backtesting/liquidations` — historical liquidations
- `GET /api/v1/quant/history` — point-in-time regime probability records
- `GET /api/v1/on-chain/whale-score/BTC` — whale-score timeseries

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=1000"
```

Auth: `X-API-Key` header. Endpoint catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-hyperliquid]], [[cryptodataapi-derivatives]], [[cryptodataapi-on-chain]], [[cryptodataapi-backtesting]].

## Related

- [[feature-engineering-crypto]] — Stage 1 feature catalog
- [[triple-barrier-labeling]] — Stage 2 labels
- [[meta-labeling]] — Stage 3 primary/secondary architecture
- [[purged-kfold-cv]] — Stage 4 leakage-free validation
- [[probability-of-backtest-overfitting]] — Stage 5 overfitting diagnostic
- [[fractional-differentiation]] — stationary, memory-preserving features
- [[composite-alpha-blending]] — fusing multiple signals into the side model
- [[ml-trading-pipeline]] — the general (asset-agnostic) pipeline this specializes
- [[deflated-sharpe-ratio]] — honest performance inference under multiple testing
- [[xgboost-trading]] — recommended starting model

## Sources

- [[book-advances-in-financial-ml]] — López de Prado, M. (2018). *Advances in Financial Machine Learning* — features, triple-barrier labeling, meta-labeling, purged/combinatorial CV, and backtest-overfitting diagnostics.

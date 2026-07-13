---
title: "Market Regime Detection (Machine Learning)"
type: concept
created: 2026-05-05
updated: 2026-06-21
status: excellent
tags: [machine-learning, backtesting, regime-detection, crypto, quantitative]
aliases: ["ML Regime Detection", "Regime Classification", "HMM Regime Models", "Adaptive Regime Models"]
domain: [backtesting, quantitative]
difficulty: advanced
prerequisites: ["[[regime-detection]]", "[[overfitting]]", "[[walk-forward-analysis]]"]
related: ["[[walk-forward-analysis]]", "[[regime-matrix]]", "[[market-regime]]", "[[crypto-market-regime-taxonomy]]", "[[2026-market-regime-overview]]", "[[crypto-perp-backtesting-pitfalls]]", "[[overfitting]]", "[[funding-rate]]", "[[volatility]]", "[[volatility-regime-switching]]", "[[machine-learning]]", "[[selection-bias-research]]", "[[lookahead-bias]]", "[[regime-detection]]", "[[regime-adaptive-strategy]]", "[[pybroker]]"]
---

Market regime detection with machine learning is the use of unsupervised or semi-supervised statistical models — Hidden Markov Models (HMMs), clustering algorithms, neural networks, and change-point detectors — to classify the current market into a discrete state (high-vol, trend, mean-reversion, crash, low-liquidity) so that backtests and live strategies can adapt their parameters to the regime they actually face. In crypto perpetuals, where regime shifts every ~3-12 months are the norm rather than the exception, static-parameter backtests produce dangerously optimistic Sharpe ratios that collapse the moment the regime rotates. Modern ML regime detection combines volatility, funding, basis, on-chain flow, and dominance features to deliver a probabilistic regime label that downstream strategies can condition on.

## Why Static Parameters Fail in Crypto

A backtest with one fixed parameter set across 2018-2026 averages over at least eight distinct crypto regimes:

| Period | Regime | Defining feature |
|---|---|---|
| 2018 | Crypto winter / bear trend | -85% BTC drawdown |
| 2020 H1 | Covid crash + recovery | March 2020 -50% in a day, then V-shape |
| 2020 H2 - 2021 H1 | DeFi summer + bull | Funding > 50% APY, basis > 30% |
| 2021 H2 - 2022 | LUNA / 3AC / FTX cascade | Liquidity collapse, contagion |
| 2023 - 2024 H1 | ETF rumor + approval rally | Spot BTC ETF Jan 2024, ETH ETF Jul 2024 |
| 2024 H2 - 2025 H1 | Funding compression | Funding crushed from ~19% APY to <4% |
| 2025-10-10/11 | ADL crisis | $20B liquidations, neutral hedges broke |
| 2026 | Stagflation regime | Oil $100-120, zero Fed cuts, BTC ~$69K (see [[2026-market-regime-overview]]) |

A [[funding-rate]] arbitrage strategy that earned 19% APY in 2024 H1 returned sub-Treasury yields by mid-2025. A trend-following CTA that thrived from 2020-2023 was whipsawed in 2025's compressed-vol regime. Without regime conditioning, a single Sharpe ratio across this period is a meaningless average that hides which regimes the edge actually came from — a textbook failure documented in [[selection-bias-research]].

## Types of Regimes Commonly Modeled

ML regime detection in crypto typically separates **four orthogonal regime axes**, each modeled independently or jointly:

1. **Volatility regime** — realized vol bucketed into low (RV < 30% annualized), medium (30-70%), high (70-120%), crisis (>120%). Feature: 30-day realized vol, GARCH(1,1) conditional variance, jump-frequency from BNS test.
2. **Trend / mean-reversion regime** — Hurst exponent, ADF test on log-prices, autocorrelation at lag-1 of returns. Trending regime: Hurst > 0.55, AR(1) > 0. Mean-reverting: Hurst < 0.45, AR(1) < 0.
3. **Liquidity regime** — order-book depth at 10bps, top-of-book bid-ask spread, Kyle's lambda, [[market-impact-models|impact coefficient]]. Crashes are defined as much by liquidity withdrawal as by price.
4. **Funding regime** — sign and term-structure of [[funding-rate]] across exchanges. Positive crowded longs (> 50% APY annualized funding) is a different regime than negative-funding shorts-paying-longs, and predicts very different forward returns.

Joint regime models (e.g., a 4-state HMM on a vector of vol + funding + basis) capture cross-feature interactions but require more data to estimate stably.

## Detection Methods

### Hidden Markov Models (HMM with Gaussian emissions)
The workhorse for small datasets. An HMM assumes the market is in one of N hidden states; each state emits returns from a Gaussian with state-specific mean and variance. The Baum-Welch algorithm learns transition probabilities and emission parameters from price data; the Viterbi algorithm decodes the most likely regime sequence. Strengths: interpretable, sample-efficient (works with 500-2000 daily observations), gives regime probabilities (not just hard labels). Weaknesses: assumes Markovian transitions and Gaussian emissions — both violated in crypto where regime persistence and fat tails dominate.

Library: `hmmlearn` (`from hmmlearn import hmm; model = hmm.GaussianHMM(n_components=4)`).

### Clustering (K-means, GMM, DBSCAN on rolling features)
Compute a feature vector on a rolling window (e.g., last 30 days: realized vol, funding, basis, BTC dominance, on-chain net flow). Cluster the feature vectors with K-means or a Gaussian Mixture Model. Each cluster is a regime. Strengths: model-free, captures non-Markovian structure. Weaknesses: must pick K (number of regimes); regimes are time-symmetric (clustering ignores temporal order).

### Neural networks (LSTM, Transformer-based)
Sequence models trained either supervised (predict next-period vol bucket) or unsupervised (variational autoencoders that learn a latent regime representation). Used by quant funds with > 5 years of high-frequency data. Strengths: capture long-range dependencies and non-linear feature interactions. Weaknesses: heavy data hunger, black-box interpretability, high overfitting risk on the < 10 distinct regime episodes crypto offers.

### Change-point detection (CUSUM, Bayesian online change-point)
Instead of classifying regimes, change-point methods detect *when* the regime changes. CUSUM tracks cumulative deviation of a feature from its baseline; when the deviation exceeds a threshold, a regime change is flagged. Bayesian online change-point (Adams & MacKay 2007) gives a posterior probability of a change at every step. Strengths: low-latency detection, useful for real-time strategy adaptation. Weaknesses: only signals change, not regime identity — must be paired with a classifier.

Library: `ruptures` (`import ruptures as rpt; algo = rpt.Pelt(model="rbf").fit(signal)`).

### Method Selection Table

Picking a detection method is mostly a function of how much data you have and whether you need a regime *identity* or just a regime *change* signal:

| Method | Min data | Output | Interpretable | Latency | Best when |
|--------|----------|--------|---------------|---------|-----------|
| **Gaussian HMM** | ~500–2000 obs | Regime probability vector | High | Medium (weeks) | Small dataset, need probabilistic labels |
| **Clustering (K-means / GMM)** | ~500 obs | Hard cluster label | Medium | N/A (offline) | Model-free exploration, non-Markovian structure |
| **Change-point (CUSUM / BOCPD)** | ~200 obs | Change flag / posterior | High | Low (days) | Real-time "something changed" alerting |
| **LSTM / Transformer** | >5 yrs HF data | Latent state / vol bucket | Low (black box) | Medium | Lots of data, non-linear interactions, fund-grade infra |
| **Markov-switching GARCH** | ~1000+ obs | Regime-conditional variance | Medium | Medium | Need regime-conditional *risk*, not just labels |

In practice the workhorse pairing is a **HMM (or Markov-switching model) for regime identity** plus a **change-point detector for low-latency alerting** — the change-point method flags that *something* shifted before the slower HMM can re-decode *which* regime is active. This mirrors the fast/slow signal split recommended in [[volatility-regime-switching]] (HMM smoother plus term-structure overlay).

## Feature Engineering for Crypto

Crypto regimes are best characterized by a multi-asset, multi-domain feature set:

| Feature | Why it matters |
|---|---|
| Realized volatility (30d) | Primary regime axis |
| Funding rate (BTC, ETH, top-10) | Crowding signal; sign change marks regime shift |
| Basis (perp vs spot, 3M futures vs spot) | Carry regime; spikes in 2025 H2 to 50% on SOL/XRP |
| BTC dominance | Risk-on (alt season, dominance falling) vs risk-off (BTC bid, dominance rising) |
| On-chain net exchange flow | Accumulation vs distribution regime; uses [[point-in-time-data]] to avoid lookahead |
| Stablecoin market cap delta | Liquidity regime |
| Hyperliquid open interest / fills | Sentiment proxy; see [[2026-04-06-hyperliquid-volume-surge]] |
| Liquidation cascade frequency | Stress regime; CoinGlass data |
| MOVE index analog (crypto-VIX) | Forward-vol expectation |

## Crypto-Specific Challenges

**Regimes don't repeat exactly.** The 2024 ETF era is structurally different from pre-ETF — institutional flows, basis dynamics, and funding patterns changed permanently. The October 10-11, 2025 ADL crisis defined a new "crash with neutral-hedge breakdown" regime that didn't exist before because [[auto-deleveraging]] mechanics had not been stress-tested at that scale. A model trained on 2020-2024 data cannot recognize the 2025 regime as a distinct cluster.

**Few independent observations.** Crypto has perhaps 10-15 distinct regime episodes in its full history. With four regime types and a vector of 8 features, parameter estimation is fragile — overfitting is the dominant risk.

**Regime-shift latency.** ML models lag the true regime change by 5-30 days depending on window size. In fast crashes (March 2020, October 2025), the lag can wipe out a quarter of the strategy's annual return before the model rotates.

**Funding regime can flip in hours.** Unlike equity vol regimes (which persist for months), crypto funding can flip from heavily positive to heavily negative within a single 8-hour funding period after a liquidation cascade. Models calibrated to slow regime persistence under-react.

## Worked Example: 4-State HMM on BTC

A representative pipeline used by mid-tier crypto funds:

1. **Features** — daily log-returns, 30-day realized vol, BTC dominance, perp funding rate, basis (perp-spot), normalized cross-section across 2018-2026.
2. **Model** — `hmmlearn.GaussianHMM(n_components=4, covariance_type="diag")`, trained on 2018-01-01 through 2024-12-31.
3. **Regime labels post-hoc** (Viterbi decode + manual interpretation):
   - State 0: low-vol grind (RV ~25%, funding +5% APY) — typical 2023 H2 - 2024 H1.
   - State 1: trending bull (RV ~55%, funding +30% APY, basis +15%) — 2020 H2, 2021 H1.
   - State 2: chop / mean-revert (RV ~40%, funding ~0, BTC dominance flat) — much of 2019, 2022 H2.
   - State 3: crash / capitulation (RV >100%, funding negative, basis backwardated, dominance spiking) — March 2020, May 2022, October 2025.
4. **Out-of-sample test** (2025-01-01 onward) — model correctly labeled the October 10-11, 2025 ADL crisis as State 3 with three days lag; a strategy that flipped to defensive mode on the State-3 signal cut peak drawdown from -34% to -19%.
5. **Stability check** — bootstrap-resample the training period; 30% of bootstrap samples produced a different number of "natural" states by BIC, confirming the model is moderately fragile. Real-world deployment uses a 3-of-5 ensemble vote across resampled HMMs.

The output is not a single label but a regime probability vector that downstream strategies condition on.

## Filtered vs. Smoothed Probabilities (the live-trading trap)

The single most consequential implementation detail in ML regime detection is which probability you act on:

| Quantity | Uses data through | Valid for | Risk if misused |
|----------|-------------------|-----------|-----------------|
| **Filtered** `P(s_t = k \| r_{1:t})` | time *t* only | Live / real-time decisions | None — this is the correct live signal |
| **Smoothed** `P(s_t = k \| r_{1:T})` | the *entire* sample (incl. future) | Post-hoc analysis, labeling history | Severe [[lookahead-bias\|look-ahead bias]] if used live |

The forward-backward algorithm produces *smoothed* probabilities — they read the whole sample, including bars after *t*, to refine the estimate of the state at *t*. A backtest that conditions trades on smoothed probabilities is quietly clairvoyant and will report an inflated Sharpe. For any decision the strategy will make in production, condition on the **filtered** probability (forward pass only). This is the regime-detection-specific manifestation of [[lookahead-bias]] and is called out again under Pitfalls below. The same trap appears in [[volatility-regime-switching#Common Mistakes|Markov-switching volatility models]].

## Application to Backtesting

Regime-aware backtesting transforms how performance is reported:

1. **Regime-conditional Sharpe and drawdown.** Report Sharpe per regime, not just a pooled average. A strategy with Sharpe 2.5 in trend regime and -1.0 in chop is materially different from one with a uniform Sharpe of 0.7 — the [[regime-matrix]] formalizes this.
2. **Regime-aware walk-forward splits.** Standard [[walk-forward-analysis]] uses calendar-based train/test windows. Regime-aware walk-forward ensures each test window contains a representative mix of regimes (or explicitly tests on regimes not seen in training). Prevents the failure mode where a model trained on 2020-2023 bull regime is "validated" on 2024 H1 bull regime — both samples from the same regime.
3. **Regime-conditional parameter switching.** Live strategies switch parameter sets (or even strategies entirely) based on the regime classifier output. The classifier itself must be backtested separately — its lag is a cost that eats into the strategy's edge.
4. **Stress testing.** Force-feed the strategy a synthetic crash regime (e.g., October 2025 path) to test whether the regime classifier detects it in time and whether the rotation logic protects capital.

Frameworks that own the temporal split — notably [[pybroker]] with built-in [[purged-kfold-cv|purged, embargoed CV]] and [[walk-forward-analysis|walk-forward]] retraining — make regime-aware ML backtesting far less leak-prone than hand-rolled loops, because the classifier is retrained only on past data inside each fold.

## Decision Table: Conditioning Strategies on Regime Output

| Classifier output | Sizing rule | Rationale |
|-------------------|-------------|-----------|
| High-confidence calm/trend (`P > 0.9`) | Full risk in the regime-appropriate strategy | Sticky regime, edge is real here |
| Mixed (`P ≈ 0.5/0.5`) | Blend allocations by probability, not flip | Hard-labeling discards information |
| High-confidence stress/crash (`P > 0.9`) | Cut risk, switch to defensive/convex book | Short but extreme regime |
| Change-point fired, identity unresolved | De-risk pre-emptively, await HMM re-decode | Latency hedge — fast signal leads slow one |

The recurring theme: **size on the probability, not the hard label**, and treat classifier *lag* as an explicit cost that eats into the strategy's edge (a strategy that needs an instant regime call has no edge).

## Pitfalls

- **Overfitting the regime count.** Choosing N=10 regimes on 2000 daily observations gives 200 observations per regime — too few to estimate stably. Rule of thumb: at least 500 observations per regime, ideally 1000+. Use AIC/BIC or cross-validated likelihood to pick N.
- **Label leakage from forward-looking features.** A "trending" label computed using forward returns is useless for live trading. All regime features must be computable using only data available at time t.
- **Data revision and survivorship.** On-chain features in particular are routinely re-labeled (Glassnode entity updates change historical exchange-balance metrics). Use [[point-in-time-data|point-in-time]] versions or accept that backtests systematically overperform.
- **Confusing regime detection with prediction.** Detecting that we are in a high-vol regime tells you which strategy to use, not which direction the market goes. Conflating the two is the canonical beginner mistake.
- **Regime probability vs regime label.** Hard-classifying into a single regime discards information. A 60/40 mix of "trend" and "chop" probability should weight strategy allocations 60/40, not flip entirely to trend.
- **In-sample regime invention.** Clustering will always produce K clusters even on random noise. Validate that detected regimes are stable out-of-sample using techniques from [[selection-bias-research]] and the [[deflated-sharpe-ratio]] adjustment.

## Tools

| Tool | Purpose |
|---|---|
| `hmmlearn` | Gaussian HMMs in Python |
| `ruptures` | Change-point detection (PELT, BinSeg, Window-based) |
| `scikit-learn` | K-means, GMM, hierarchical clustering |
| `statsmodels` | MarkovRegression for regime-switching regressions |
| `bayesian-changepoint-detection` (Adams & MacKay) | Online Bayesian change-point |
| `pytorch` / `tensorflow` | LSTM, Transformer regime models |
| `arch` | GARCH-family volatility regime estimation |

## Related

- [[regime-detection]] — the broader strategy-level overview
- [[market-regime]] — the foundational concept of market regimes
- [[volatility-regime-switching]] — the econometric sibling (HMM/Markov-switching for vol)
- [[regime-adaptive-strategy]] — how to deploy a regime-conditioned book
- [[regime-matrix]] — strategy-by-regime mapping table
- [[walk-forward-analysis]] — validation framework regime detection plugs into
- [[pybroker]] — ML framework with leak-free walk-forward retraining
- [[2026-market-regime-overview]] — current regime example
- [[crypto-perp-backtesting-pitfalls]] — parent gap-analysis page
- [[lookahead-bias]] — filtered-vs-smoothed and label-leakage risks
- [[overfitting]], [[selection-bias-research]] — overfitting risks specific to regime models
- [[funding-rate]], [[volatility]] — primary regime features
- [[machine-learning]] — broader ML context

## Sources

- Hamilton, J.D. (1989). "A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle." *Econometrica*. The foundational regime-switching model paper.
- Adams, R.P. & MacKay, D.J.C. (2007). "Bayesian Online Changepoint Detection." arXiv:0710.3742.
- Glassnode Insights (2024). "Why Use Point-in-Time Data?" insights.glassnode.com — argues PiT data is essential to avoid backtest contamination, cited in [[2026-04-22-gap-finder-backtesting-pitfalls-in-particular-with]] gap analysis.

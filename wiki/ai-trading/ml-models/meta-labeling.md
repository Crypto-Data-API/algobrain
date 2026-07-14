---
title: "Meta-Labeling"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [ai-trading, machine-learning, quantitative]
aliases: ["Meta-Labeling", "Meta Labeling", "Secondary ML Filter", "Bet Sizing Model"]
domain: [machine-learning, ai-trading]
prerequisites: ["[[triple-barrier-labeling]]", "[[funding-rate]]"]
difficulty: advanced
related: ["[[triple-barrier-labeling]]", "[[ml-crypto-price-prediction]]", "[[ml-trading-pipeline]]", "[[purged-kfold-cv]]", "[[feature-engineering-crypto]]", "[[open-interest]]", "[[funding-rate]]", "[[book-advances-in-financial-ml]]"]
---

# Meta-Labeling

**Meta-labeling** is a two-model machine-learning architecture from Marcos López de Prado's *Advances in Financial Machine Learning* (Chapter 3). A **primary model** decides the *side* of a trade (long/short/flat) — the directional bet. A **secondary ("meta") model**, a binary classifier, then decides *whether to act on that bet and how large to make it*. The meta-model never changes the side; it only vetoes weak signals and sizes strong ones. This separation lets you combine a high-recall primary signal (catches most opportunities but with many false positives) with a high-precision ML filter that removes the false positives (Source: [[book-advances-in-financial-ml]]).

The name captures the idea: the secondary model learns a *label about the primary model's labels* — specifically, "was the primary right this time?"

## Why Split Side From Size

In a conventional one-model system, a single classifier both picks direction and implies conviction. Meta-labeling decouples these two decisions, which has several advantages (Source: [[book-advances-in-financial-ml]], Ch. 3.6):

- **You can build the side model from economic logic**, not ML. A funding-fade rule, a moving-average cross, or a [[hyperliquid-baskets-overview|basket]] signal can be the primary. The ML lives only in the filter.
- **Precision and recall are tuned independently.** Set the primary to catch nearly every real move (high recall), then let the meta-model raise precision by discarding the losers.
- **Position sizing falls out of the classifier probability.** The meta-model outputs P(primary is correct); that probability maps directly to bet size.
- **The F1 score improves.** Meta-labeling is a way to lift the F1 of a system whose primary model already has acceptable recall but poor precision.

The critical constraint: **meta-labeling cannot create signal that is not already in the primary.** If the primary is no better than random on direction, the filter has nothing correct to keep. It amplifies a real edge; it does not manufacture one.

## The Confusion Matrix View

Meta-labeling operates on the *positives* the primary emits. Recall the four outcomes when the primary says "trade":

| | Primary says trade | Primary says flat |
|---|---|---|
| **Move happens** | True Positive | False Negative |
| **No move** | False Positive | True Negative |

A high-recall primary produces many True Positives but also many False Positives. The meta-model is trained only on the cases where the primary fired, learning to separate the TPs from the FPs. It **cannot recover False Negatives** (opportunities the primary missed) — those are gone. This is why the primary must err toward over-firing.

## Constructing the Meta-Label

The meta-label is binary and comes from the *realized outcome of the primary's bet*, most naturally via [[triple-barrier-labeling]]:

1. Run the primary over history. Each time it fires, record the side and entry.
2. Apply the [[triple-barrier-labeling|triple-barrier method]] on that side: did the trade hit its profit-take barrier before its stop-loss or time barrier?
3. Meta-label = **1** if the primary's bet was profitable (hit the profit target), **0** if it was stopped out or expired flat/against.
4. Train the secondary classifier on features observed *at entry* to predict this 1/0 outcome.

Because the label already encodes the side, the meta-model only needs to answer "will this specific bet win?" — a cleaner, better-posed problem than forecasting raw direction.

## Crypto Worked Example: Funding-Fade + ML Confidence Gate

A concrete crypto instantiation pairs a structural primary with an ML filter built from crypto-native features.

**Primary (economic side model).** Fade crowded perpetual positioning — the logic behind the [[crowded-long-funding-fade]] and [[crowded-short-funding-fade]] baskets. Rule: when the 8h-equivalent [[funding-rate]] z-score over a 30-day window exceeds **+2.0** (euphoric, over-leveraged longs), the primary emits a **short**; when it falls below **−2.0**, it emits a **long**. This is high-recall by design — it fires on every funding extreme, including the many that keep running.

**Secondary (ML confidence gate).** A gradient-boosted classifier ([[xgboost-trading|XGBoost]]) predicting whether each funding-fade bet will hit its profit barrier, trained on features available at entry:

| Feature family | Example features | CryptoDataAPI source |
|---|---|---|
| Funding structure | funding z-score, funding slope, cross-venue funding spread | `derivatives/funding-rates` |
| [[open-interest|Open interest]] | OI change %, OI-vs-price divergence (1h/4h/24h) | `liquidity/oi-divergence` |
| Whale positioning | whale long/short skew, whale accumulation score | `quant/whales`, `on-chain/whale-score/{symbol}` |
| Regime | HMM regime probabilities, volatility regime label | `quant/market`, `volatility/regime` |
| Liquidation pressure | recent long/short liquidation imbalance | `market-intelligence/liquidations` |
| Breadth | % of alts above their 200D MA | `market-health/altcoin-breadth` |

The intuition: a positive-funding extreme is far more likely to *revert* (rewarding the fade) when OI is diverging bearishly, whales are net short, and the regime is `choppy_high_vol` or `distribution` — and far more likely to *keep running* (a losing fade) when whales are still accumulating and the regime is `strong_trend_bull`. The meta-model learns exactly this conditional structure, which a static funding threshold cannot.

**Result.** Only funding-fade signals the gate scores above a probability threshold are traded; the rest are vetoed. In practice this trades far less often but with materially higher win rate — the classic precision-for-recall trade meta-labeling is designed to make.

## Bet Sizing From the Meta-Probability

The meta-model's output probability `p` (that the bet wins) sizes the position, so conviction scales continuously rather than being on/off (Source: [[book-advances-in-financial-ml]], Ch. 10). De Prado's mapping for a two-class problem:

```
z = (p - 0.5) / sqrt(p * (1 - p))     # test statistic
m = 2 * Φ(z) - 1                       # bet size in [-1, 1], Φ = normal CDF
```

At `p = 0.50` the size is 0 (no edge → no bet); at `p = 0.70`, `z ≈ 0.87` and `m ≈ 0.62` of the maximum position; at `p ≈ 0.90`, size approaches the cap. A **veto threshold** (e.g. trade only when `p > 0.60`) sits underneath this so marginal bets are dropped entirely. Position size is then `m × max_size`, further scaled by volatility targeting.

## Validation and Pitfalls

- **The meta-model inherits label overlap.** Consecutive funding-fade bets can resolve over shared windows, so their meta-labels are concurrent and non-independent. Train and validate with [[purged-kfold-cv|purged, embargoed CV]] and sample-uniqueness weights, never a random shuffle.
- **Class imbalance.** If the primary is decent, most fires are winners (or most are losers), skewing the meta-label. Use balanced class weights and evaluate with F1/precision-recall, not raw accuracy.
- **Do not fit the primary on the meta-model's outcome.** The side model must be specified independently (economics or a separately trained model); otherwise the split collapses and leakage creeps in.
- **A weak primary poisons everything.** Confirm the primary has genuine directional edge (positive expectancy before filtering) before adding the gate. The filter multiplies edge; 0 × anything is 0.
- **Regime drift.** The conditional "when does the fade work" relationship changes across [[market-regime|regimes]]; retrain on a rolling window and monitor realized precision versus the backtested gate.

## Getting the Data (CryptoDataAPI)

Features for the secondary model come from the derivatives, positioning, regime, and on-chain endpoints.

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding (primary signal input)
- `GET /api/v1/liquidity/oi-divergence` — OI-vs-price divergence at 1h/4h/24h
- `GET /api/v1/quant/whales` — whale positioning summary (>=$100k accounts)
- `GET /api/v1/quant/market` — HMM regime probabilities (4h/24h horizons)
- `GET /api/v1/volatility/regime` — per-asset volatility regime labels
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidation imbalance
- `GET /api/v1/market-health/altcoin-breadth` — % of coins above their moving average

**Historical data (for building meta-labels and training):**
- `GET /api/v1/backtesting/klines` — OHLCV path for triple-barrier resolution
- `GET /api/v1/backtesting/funding` — funding archive for the primary signal
- `GET /api/v1/quant/whales/history?days=90` — whale positioning timeseries
- `GET /api/v1/on-chain/whale-score/BTC` — historical whale accumulation score

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/liquidity/oi-divergence"
```

Auth: `X-API-Key` header. Endpoint catalogs: [[cryptodataapi-derivatives]], [[cryptodataapi-regimes]], [[cryptodataapi-on-chain]].

## Related

- [[triple-barrier-labeling]] — supplies the 1/0 outcome the meta-model learns
- [[ml-crypto-price-prediction]] — the full pipeline this filter plugs into
- [[ml-trading-pipeline]] — general ML trading workflow
- [[purged-kfold-cv]] — how to validate the meta-model without leakage
- [[feature-engineering-crypto]] — the feature set feeding the gate
- [[crowded-long-funding-fade]] / [[crowded-short-funding-fade]] — primary-signal baskets
- [[funding-rate]] / [[open-interest]] — core signal inputs
- [[xgboost-trading]] — typical secondary-model choice

## Sources

- [[book-advances-in-financial-ml]] — López de Prado, M. (2018). *Advances in Financial Machine Learning*, John Wiley & Sons. Chapter 3 ("Labeling," meta-labeling, §3.6) and Chapter 10 ("Bet Sizing").

---
title: "Regime-Conditional Validation"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [backtesting, crypto, market-regime, regime-detection, validation, methodology]
aliases: ["Regime-Stratified Backtesting", "Per-Regime Validation", "Regime-Conditional Backtesting"]
domain: [backtesting]
prerequisites: ["[[crypto-market-regime-taxonomy]]", "[[walk-forward-analysis]]"]
difficulty: advanced
related: ["[[crypto-market-regime-taxonomy]]", "[[regime-strategy-playbook]]", "[[walk-forward-analysis]]", "[[crypto-perp-backtesting-pitfalls]]", "[[point-in-time-data]]", "[[lookahead-bias]]", "[[crypto-short-history-statistical-power]]", "[[deflated-sharpe-ratio]]", "[[market-regime-detection-ml]]", "[[hypothesis-to-backtest-workflow]]", "[[cryptodataapi-regimes]]"]
---

# Regime-Conditional Validation

A single blended Sharpe hides which market states actually paid you. Regime-conditional validation asks the sharper question: **does this edge survive every crypto regime, or is one bull leg carrying the whole backtest?** The [[crypto-market-regime-taxonomy|14-basket crypto regime taxonomy]] gives the state definitions; this page is the *validation protocol* that attributes performance across those states, stratifies holdouts by regime, and refuses to trust a strategy that has never been tested in the regimes where it will actually be deployed. It is the regime-aware layer on top of [[walk-forward-analysis]] and the discipline that [[crypto-perp-backtesting-pitfalls]] demands when it warns that walk-forward windows must not straddle regime breaks.

## Why Blended Performance Lies

A strategy's headline Sharpe is an average over whatever mix of regimes happened to occur in the sample. Two failure shapes hide inside it:

- **Regime concentration.** A momentum strategy backtested over 2023–2024 may owe its entire Sharpe to a few trending months; in chop and cascades it bleeds. The blended number says "0.9 Sharpe"; the truth is "2.5 in trend, −0.4 everywhere else." Deployed into a non-trending regime, it loses.
- **Regime absence.** Crypto's short history (see [[crypto-short-history-statistical-power]]) means many regimes appear only once or not at all in a given window. A strategy that has *never seen* a liquidation cascade or a funding-compression regime has an untested tail, and the backtest cannot tell you it is dangerous — it simply has no data there.

The [[crypto-market-regime-taxonomy]] makes the point structural: each regime implies a different coin set, leverage ceiling, holding duration, and funding tolerance. A strategy is not one strategy across regimes — it is a different bet in each. Validation must be conditional to see that.

## Per-Regime Sharpe Attribution

The first tool is to decompose performance by regime rather than reporting a single number.

**Procedure.**
1. **Label every bar** with its regime, point-in-time (the label must use only information available at that bar — see the point-in-time warning below).
2. **Tag every trade** by the regime prevailing at entry (or hold a regime vector across the trade's life for long holds).
3. **Compute per-regime statistics**: Sharpe, hit rate, average trade, max drawdown, and trade count within each regime.
4. **Attribute the blended Sharpe** to its regime contributions — which states earned the return, which lost, which were never sampled.

**What to look for.** A robust edge shows *positive-or-flat* performance across most regimes and a coherent story for where it loses (e.g. a mean-reversion edge that gives back in vol-expansion, by design). A fragile edge shows one or two dominant regimes and negatives elsewhere. An untested edge shows empty cells — regimes with too few trades to say anything.

| Regime (basket) | Trades | Sharpe | Hit rate | Max DD | Read |
|---|---:|---:|---:|---:|---|
| Macro Trend (bull) | 140 | 2.3 | 61% | 8% | Carries the strategy |
| Chop / range | 90 | 0.1 | 49% | 12% | Marginal |
| Derivatives-fragile | 22 | −0.6 | 41% | 24% | Loses; too few trades to trust |
| Vol expansion | 6 | — | — | — | Untested — dangerous |

*(Illustrative. The empty vol-expansion row is the finding, not a footnote: the strategy has never been validated in the regime most likely to hurt it.)*

## Regime-Stratified Holdouts

Standard out-of-sample splitting by *time* can accidentally put an entire regime in-sample and none of it out-of-sample. Regime-stratified holdouts fix this by ensuring each regime is represented in both training and test.

- **Stratify the holdout by regime**, not only by date, so that the test set contains bull, bear, chop, cascade, and compression periods in proportion to their occurrence.
- **Leave-one-regime-out (LORO).** Train on all regimes but one, test on the held-out regime. This is the most honest answer to "how does the edge do in a regime it was not fitted on?" — the crypto analogue of leave-one-group-out cross-validation.
- **Respect time order within the stratification.** Purge and embargo around regime boundaries so a trade's label window does not straddle a regime change and leak (see [[purged-kfold-cv]]). Regime transitions are exactly where labels bleed.
- **Never let a walk-forward window span a known break.** The October 2025 ADL cascade and the subsequent funding compression are regime boundaries; a window fitted before and tested after is fitting a regime that no longer exists (see [[crypto-perp-backtesting-pitfalls]]).

## Minimum Trades Per Regime

Per-regime attribution is only meaningful if each regime has enough trades to compute a statistic. In crypto this is the binding constraint, because rare regimes are both the most important (they hold the tail risk) and the least populated.

- **Set a minimum trade count per regime** below which you report "insufficient data" rather than a Sharpe. A common floor is **~30 trades** before a per-regime Sharpe is even suggestive, and far more before it is significant — a single-digit trade count in a regime tells you nothing.
- **Rare regimes rarely clear the floor.** Cascades and depegs are days-long and infrequent; a strategy may accumulate only a handful of trades there across all of history. That is a *finding*: the tail is untested, and position sizing must reflect it, not a fabricated per-regime number.
- **Do not pool distinct regimes to reach the floor.** Merging chop and trend to get "enough" trades destroys the whole point. If a regime is under-sampled, say so and treat that regime as unproven (see [[crypto-short-history-statistical-power]] on why crypto's effective N is small).
- **Deflate for the regimes you searched.** Slicing performance many ways is itself multiple testing; the best-looking regime is upward-biased. Feed the number of regime cuts into the [[deflated-sharpe-ratio|DSR]] N.

## Point-in-Time Regime Labels — the Leakage Trap

The subtlest error in regime-conditional validation is labelling bars with a regime computed using *future* data. If your regime classifier smooths over a window centred on each bar, or is fitted on the whole sample and then applied historically, the label at time `t` encodes what happened after `t` — and conditioning on it is [[lookahead-bias|look-ahead bias]]. The strategy then looks great "in bull regimes" because the label already knew the bull continued.

The defenses:
- **Causal labelling only.** The regime at `t` must be computable from data up to `t`, exactly as a live system would classify it in real time.
- **Use a point-in-time regime archive**, not a recomputed one. Query the regime as it was published on each date rather than re-deriving it with today's model (see [[point-in-time-data]]).
- **Test the classifier's own lag.** A regime label that flips only *after* the move is honest but late; budget that latency into the strategy, don't assume instant, clairvoyant classification.

## A Validation Protocol

Putting it together, a regime-conditional validation run:

1. **Attach point-in-time regime labels** to every bar from a causal archive.
2. **Run the strategy** and tag every trade by entry regime.
3. **Attribute per-regime** Sharpe, hit rate, drawdown, and trade count.
4. **Enforce the minimum-trades floor**; mark under-sampled regimes as unproven.
5. **Stratify holdouts by regime** and run leave-one-regime-out.
6. **Deflate** the best regime's Sharpe for the number of regime slices.
7. **Decide**: deploy only into the regimes the edge actually survived, gated by live regime detection (the logic in [[regime-strategy-playbook]]).

The output is not "the strategy works" but "the strategy works *in these regimes*, is untested *in those*, and must be gated off *in the rest*." That is a deployable conclusion; a blended Sharpe is not.

## Getting the Data (CryptoDataAPI)

Regime-conditional validation needs a **point-in-time regime archive** — regime labels as they were published on each historical date, never recomputed with a current model. CryptoDataAPI's quant engine provides exactly this:

- **Point-in-time regime records** — `GET /api/v1/quant/history` (Pro Plus) returns the HMM regime probabilities as recorded at each timestamp, the causal labels regime-conditional validation requires
- **Daily regime timeline** — `GET /api/v1/quant/timeline` (Pro Plus) gives daily market regime labels from 2019 to now for stratifying trades and holdouts
- **Full regime archive** — `GET /api/v1/quant/regimes/history` (Pro Plus) downloads the 6-regime Parquet archive (2020–yesterday) for bulk per-regime attribution
- **Regime taxonomies** — `GET /api/v1/quant/regimes` (6-state HMM), `GET /api/v1/regimes` (10-state long-horizon) for label definitions
- **Overlay states** — `GET /api/v1/volatility/regime/score` and `GET /api/v1/liquidity/regime/score` for the volatility and fragility overlays in the 14-basket taxonomy

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/quant/timeline"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-regimes]].

## Related

- [[crypto-market-regime-taxonomy]] — the 14 regime states this protocol validates across
- [[regime-strategy-playbook]] — the regime → deployable-strategy mapping the validation output feeds
- [[walk-forward-analysis]] — the time-ordered validation this specialises by regime
- [[market-regime-detection-ml]] — the causal classifiers that produce the labels
- [[crypto-perp-backtesting-pitfalls]] — why windows must not span regime breaks
- [[point-in-time-data]], [[lookahead-bias]] — the leakage trap in regime labelling
- [[purged-kfold-cv]] — purge/embargo around regime boundaries
- [[deflated-sharpe-ratio]] — deflating for the number of regime slices
- [[crypto-short-history-statistical-power]] — why rare regimes stay under-sampled
- [[hypothesis-to-backtest-workflow]] — where regime attribution slots into the pipeline
- [[cryptodataapi-regimes]] — the point-in-time regime archive endpoints

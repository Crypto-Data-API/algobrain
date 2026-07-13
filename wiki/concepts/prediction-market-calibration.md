---
title: "Prediction Market Calibration"
type: concept
created: 2026-05-14
updated: 2026-06-21
status: excellent
tags: [backtesting, behavioral-finance, event-driven, crypto]
aliases: ["Calibration", "Forecast Calibration", "Probability Calibration", "Brier Score"]
domain: [behavioral-finance, backtesting]
prerequisites: ["[[prediction-markets]]"]
difficulty: intermediate
related: ["[[prediction-markets]]", "[[polymarket]]", "[[metaculus]]", "[[polymarket-as-crypto-leading-indicator]]", "[[backtesting-pitfalls]]", "[[overconfidence-bias]]", "[[data-snooping-and-p-hacking]]", "[[kalshi]]", "[[manifold-markets]]", "[[overfitting]]"]
---

Calibration is the measurable property that asks whether a [[prediction-markets|prediction market]]'s stated probabilities correspond to real-world outcome frequencies. For a trader, calibration is the bridge between "the market said 70%" and "should I bet against it?" — a perfectly calibrated venue offers no expected-value edge to a fade trader, while a systematically miscalibrated one *is* the edge.

## Core definition

A prediction market is **well-calibrated** if, across the universe of all markets that resolved at price X¢, the underlying event actually occurred X% of the time. Formally, for binary contracts with stated probability `p`, the empirical frequency of "YES" outcomes within the bucket centered on `p` should equal `p`.

Calibration is **distinct from accuracy**. A forecaster who assigns 51% to every coin flip is perfectly calibrated but useless; a forecaster who assigns 99% to every event and is right 99% of the time has both high calibration and high resolution. Calibration measures honesty of uncertainty; resolution measures information content.

## Why calibration matters for trading

If a market is systematically miscalibrated, the deviation is exploitable. The canonical example is the **favorite-longshot bias** documented across pari-mutuel betting and many prediction markets: events priced at ~70% historically resolve YES at a lower rate (e.g. ~55%), while events priced at ~5% resolve YES more often than 5% — bettors overpay for longshots and underpay for favorites. See [[prediction-markets]] for the broader literature.

The trading implication is direct:
- **Perfectly calibrated market** → zero expected return to systematic fading or favoring of any price bucket
- **Miscalibrated market** → fade the bucket that overshoots; back the bucket that undershoots
- **Time-varying calibration** → the edge appears and disappears with participant mix, liquidity, and venue regime

### Calibration state → trading decision

| Calibration state | What it means | Trader action |
|---|---|---|
| Calibrated *and* high resolution | Honest *and* informative prices | Treat as a signal to follow, not fade |
| Calibrated *but* low resolution | Honest but uninformative (e.g. everything near 50%) | No edge in either direction |
| Miscalibrated (favourite-longshot) | Predictable bucket-level mispricing | Fade overshooting buckets, back undershooting ones |
| Miscalibrated but time-varying | Edge exists only in some regimes | Condition on participant mix / liquidity; expect decay |

Crucially, a calibration *edge* is a statement about a *population of similarly-priced markets*, not any single contract. You cannot read miscalibration off one market's price; you need the resolved distribution of a whole bucket — which is why the measurement methods below operate over populations, and why the [[backtesting-pitfalls|pitfalls]] section warns so heavily about how that population is selected.

## Measurement methods

### Brier score

Mean squared error between the forecast probability `p` and the binary outcome `o ∈ {0, 1}`:

```
Brier = (1/N) Σ (p_i − o_i)²
```

Lower is better. Range `[0, 1]` for binary outcomes. A constant 0.5 forecaster scores 0.25; a random coin-flip outcome series has irreducible Brier of 0.25.

### Log score (logarithmic scoring rule)

```
LogScore = −(1/N) Σ [ o_i · log(p_i) + (1 − o_i) · log(1 − p_i) ]
```

The log score penalizes **confident wrong** predictions far more harshly than Brier — a forecast of 0.99 that resolves NO is essentially infinitely punished. Preferred when overconfidence is the failure mode being audited.

### Calibration plot / reliability diagram

Bin all forecasts by stated probability (e.g. 10 bins of width 0.1). For each bin, plot:
- x-axis: mean forecast probability within the bin
- y-axis: empirical frequency of YES outcomes within the bin

A perfectly calibrated venue traces the diagonal `y = x`. Systematic deviations reveal the structure of miscalibration: bowing below the diagonal at high `p` indicates overconfidence on favorites.

### Reliability–Resolution decomposition

Brier score decomposes into three additive components:

```
Brier = Reliability − Resolution + Uncertainty
```

- **Reliability** — squared deviation of bin mean from bin frequency (calibration error proper; lower is better)
- **Resolution** — variance of bin frequencies around base rate (information content; higher is better)
- **Uncertainty** — variance of outcomes (irreducible; property of the event set, not the forecaster)

This decomposition is what allows a trader to separate "the market is miscalibrated" from "the market is uninformative" — two very different diagnoses with different trading implications.

### Scoring rule comparison

| Method | Formula core | Range (binary) | Penalises confident-wrong | Best for |
|---|---|---|---|---|
| Brier score | `mean((p − o)²)` | [0, 1], lower better | Quadratically | General accuracy + the reliability/resolution split |
| Log score | `−mean(o·ln p + (1−o)·ln(1−p))` | [0, ∞), lower better | Severely (→∞ at p=0/1) | Auditing overconfidence ([[overconfidence-bias]]) |
| Reliability (Brier component) | bin-mean vs bin-frequency | [0, ~], lower better | — | Isolating calibration error proper |
| Reliability diagram | plotted `y=x` deviation | visual | — | Diagnosing *the shape* of miscalibration |

Both Brier and log score are **strictly proper** scoring rules: a forecaster minimises expected score only by reporting its true subjective probability, so neither can be gamed by shading forecasts toward the extremes. The choice between them is about *which* errors to weight — log score is the right tool when the failure mode you are hunting is overconfidence, because it punishes a 0.99 that resolves NO almost without bound.

### Reading a reliability diagram — worked example

> Illustrative shape, not a measured Polymarket result.

Suppose you bin a year of resolved binary contracts into deciles and plot bin-mean forecast (x) against empirical YES frequency (y). Three signatures and their trades:

| Diagram shape | Interpretation | Trade |
|---|---|---|
| Points hug the diagonal `y = x` | Well-calibrated | No systematic fade edge; look elsewhere |
| High-`p` points bow *below* the line (e.g. 70¢ bucket resolves ~58%) | Overpricing favourites | Fade the favourite bucket |
| Low-`p` points sit *above* the line (e.g. 5¢ bucket resolves ~9%) | Underpricing longshots | Back the longshot bucket |

The bottom two rows together are the classic **favourite–longshot bias**: an S-shaped reliability curve that crosses the diagonal once. The size of the vertical gap at each bucket is the gross edge before fees, slippage, and the [[backtesting-pitfalls|biases below]] are netted out.

## Documented empirical findings on Polymarket calibration

During the 2024 US election cycle, [[polymarket]] odds proved more accurate than mainstream polling aggregates on the eventual outcome (see [[polymarket-wiki-guide]] for the detailed account). This is an *outcome-accuracy* claim — Polymarket called the winner correctly when polls did not — and is not by itself a calibration claim. Calibration would require a population of similarly-priced markets to assess whether the bucket as a whole was honest.

Separately, favorite-longshot bias has been documented on Polymarket on tail outcomes (see [[prediction-markets]]) — markets priced at single-digit probabilities have historically over-represented in YES resolutions relative to their stated odds, consistent with the broader pari-mutuel literature.

## The leading-indicator question

Calibration says nothing about **timing**. A market that updates its price the moment an outcome becomes public knowledge can be perfectly calibrated at every instant and still be useless as a leading indicator — it is merely a fast mirror of consensus.

The trader's actionable question is **temporal**: does the market price at time `T` predict the realized outcome at time `T + Δ` better than alternative information sources observable at time `T`? This requires a forward-looking, time-stamped calibration analysis — not just the standard backward calibration over final settlement prices.

The relevant comparisons:
- Market price at `T` vs. polling consensus at `T`, both predicting the binary outcome
- Market price at `T` vs. the *eventual* market price at `T + Δ` (does early price-discovery lead late price-discovery?)
- Market price at `T` vs. an exogenous asset move over `[T, T + Δ]` (does the prediction market price-shift Granger-cause the linked asset move?)

## Backtest methodology for "is Polymarket a leading indicator?"

Concrete steps to test the leading-indicator hypothesis for crypto-relevant Polymarket contracts:

1. **Pull historical CLOB data** via the [[polymarket-api]] Data API endpoints, or query the [[the-graph]] Subgraph for full order-book history
2. **Sample price snapshots** for each market at `T − 7d`, `T − 24h`, `T − 1h`, and at resolution
3. **Pair with exogenous outcomes** — for event-driven crypto-relevant markets (Fed decisions, ETF approvals, regulatory rulings), record the realized BTC/ETH return over the window `T` to `T + 24h` post-resolution
4. **Hypothesis test** — does the Polymarket price-shift at time `T` predict the realized crypto-asset move over `[T, T + Δ]` *better* than consensus indicators observable at `T` (CME FedWatch implied probabilities, polling averages, analyst surveys)?
5. **Null hypothesis** — zero cross-correlation between Polymarket price changes and subsequent asset returns, after controlling for contemporaneously available consensus signals
6. **Reporting** — Brier and log scores by sampling horizon, reliability diagrams by horizon, and information coefficient (IC) of Polymarket signals against realized returns

See [[polymarket-as-crypto-leading-indicator]] for the full study design.

## Pitfalls

The standard cautions from [[backtesting-pitfalls]] apply with extra force to prediction-market analysis:

- **Survivorship bias** — restricting analysis to *resolved* markets ignores cancelled, disputed, or never-settled contracts. Polymarket has a non-trivial population of ambiguous-resolution markets that bias the surviving sample
- **P-hacking and multiple comparisons** — Polymarket hosts thousands of markets; sufficient slicing will manufacture spurious "leading indicator" relationships. Use Bonferroni correction or false-discovery-rate control. This is the same [[data-snooping-and-p-hacking|data-snooping]] trap that plagues strategy backtests; the more buckets, horizons, and filters you try, the more a calibration "edge" is just [[overfitting|noise mistaken for signal]]
- **Liquidity confound** — thin markets are noisy, not informative. Filter for minimum daily volume and minimum order-book depth before drawing conclusions; otherwise the "signal" is microstructure jitter
- **Regime change** — pre-2024 Polymarket (small, crypto-native, geographically restricted) and post-ICE-investment Polymarket (larger, broader participant pool, US-regulated future) are different markets with different participant distributions. Pooling across regimes is unsafe
- **Look-ahead bias** — knowing in retrospect which markets resolved decisively (and which exploded into news) colors the choice of markets to study. Pre-register the universe of markets before computing any statistics
- **Resolution-source bias** — markets that resolve based on a single oracle or news source may show artificially high "predictive" power if the oracle source itself is the leading indicator the market is merely echoing

## Calibration of competing forecasting platforms

Brief comparison of the major prediction-market and forecasting venues, framed by their structural exposure to miscalibration:

| Platform | Stakes | Structural calibration concern |
|---|---|---|
| [[polymarket]] | Real money (USDC) | Favorite-longshot bias documented on tail outcomes; thin-market noise on long-tail contracts |
| [[kalshi]] | Real money (USD, CFTC-regulated) | Smaller historical sample; restricted market universe; calibration evidence still accumulating |
| [[metaculus]] | Reputation / non-monetary | Long track record on geopolitical and scientific forecasts; calibration is professionally curated and openly published |
| [[manifold-markets]] | Play money (mana) | Zero-stake forecasting suffers from non-economic incentives; calibration is structurally weaker than real-money venues |

The cross-platform comparison is itself a tradeable signal: when a real-money market diverges from a well-calibrated non-monetary forecaster like [[metaculus]], one of them is wrong — and identifying which is the basis of an edge.

## Related

- [[prediction-markets]]
- [[polymarket]]
- [[polymarket-api]]
- [[polymarket-as-crypto-leading-indicator]]
- [[polymarket-wiki-guide]]
- [[metaculus]]
- [[kalshi]]
- [[manifold-markets]]
- [[the-graph]]
- [[backtesting-pitfalls]]
- [[data-snooping-and-p-hacking]]
- [[overconfidence-bias]]
- [[overfitting]]

## Sources

- [[polymarket-wiki-guide]] — 2024 US election outcome-accuracy comparison between Polymarket and polling aggregates
- [[prediction-markets]] — favorite-longshot bias literature and broader prediction-market context
- [[backtesting-pitfalls]] — survivorship, p-hacking, look-ahead, and regime-change pitfalls applied to historical market data

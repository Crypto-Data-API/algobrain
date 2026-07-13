---
title: "Quantitative Momentum — Wesley Gray & Jack Vogel (2016)"
type: source
created: 2026-04-15
updated: 2026-04-28
status: good
tags: [book, education, momentum, quantitative, factor-investing]
source_type: book
source_author: "Wesley R. Gray and Jack R. Vogel"
source_date: 2016
confidence: high
aliases: ["Quantitative Momentum", "QM", "Gray Vogel Momentum"]
related:
  - "[[momentum]]"
  - "[[cross-sectional-momentum]]"
  - "[[time-series-momentum]]"
  - "[[trend-following]]"
  - "[[factor-investing]]"
  - "[[fama-french-factors]]"
  - "[[behavioral-finance]]"
  - "[[smart-beta]]"
---

## Overview

**Quantitative Momentum: A Practitioner's Guide to Building a Momentum-Based Stock Selection System** by Wesley Gray and Jack Vogel, published in 2016, is the definitive practitioner book on equity [[cross-sectional-momentum]] — the systematic strategy of buying stocks that have outperformed over the past 3-12 months and selling those that have underperformed. The authors run Alpha Architect, an asset management firm, and built their flagship Quantitative Momentum (QMOM) ETF directly on the methodology described in the book.

Their core argument: the academic literature on [[momentum]] (Jegadeesh & Titman 1993, Asness 1994, and dozens of follow-ups) has documented one of the most robust anomalies in finance — but most "momentum" funds water it down with diversification, low turnover, and sector neutrality that strip out most of the premium. Gray and Vogel argue that if you want momentum's premium, you have to take momentum's drawdowns: a concentrated, high-turnover, sector-unconstrained portfolio of the top 50-100 momentum stocks rebalanced quarterly.

## The Quantitative Momentum System

Gray & Vogel specify a complete, replicable system:

1. **Universe**: Mid-to-large cap US equities (top ~1,000 by market cap)
2. **Liquidity filter**: Remove illiquid names
3. **Quality filter**: Remove stocks with very low quality (financial distress, accounting red flags)
4. **Momentum metric**: 12-month return excluding the most recent month (the "12-2" or "skip-month" momentum)
5. **Smoothness filter**: Among top momentum stocks, prefer those with smooth price paths (lower "frog-in-the-pan" volatility) — a key empirical refinement Gray and Vogel popularized
6. **Selection**: Top 50 stocks by momentum-quality composite
7. **Weighting**: Equal-weighted
8. **Rebalance**: Quarterly

Backtests on 1927-2014 US data show 16-18% gross annual returns vs. ~10% for the market, with higher volatility (~25% vs. 20%) and brutal drawdowns in momentum-crash years (1932, 2009).

## Key Takeaways

- **Cross-sectional momentum is the most robust anomaly in finance.** It works in the US, internationally, in commodities, in currencies, and in fixed income. It has been documented continuously since the 1990s and continues to work despite being widely known.
- **Momentum's premium comes from its drawdowns.** Momentum crashes (rapid mean-reversion after sustained momentum) are catastrophic — 2009 saw momentum lose 80%+ peak-to-trough. Investors who can't sit through the crashes don't earn the premium.
- **Skip-month momentum (12-2) outperforms naive 12-month momentum.** The most recent month exhibits short-term reversal; excluding it improves the signal.
- **Smoothness matters.** Two stocks with the same 12-month return but different paths perform differently going forward. Smooth uptrends continue more reliably than choppy ones — the [[behavioral-finance|behavioral]] explanation is "frog in the pan": investors under-react to smooth changes more than to choppy ones.
- **Quality screens prevent value-trap-style momentum disasters.** A simple distress filter (avoid bottom decile of profitability/Z-score) removes the worst momentum disasters without diluting the premium meaningfully.
- **Concentration is essential.** A 500-stock momentum portfolio has only 100 bps/year edge; a 50-stock concentrated portfolio has 4-6%. Diversification is the enemy of factor harvesting.
- **Quarterly rebalance is the sweet spot.** More frequent rebalancing eats returns in costs; less frequent loses signal as winners fade.
- **Behavioral biases sustain the anomaly.** Investors anchor to past prices, under-react to news, and chase performance with delay. These biases persist because they're hard-wired, not because investors lack information.

## Who Should Read This

Anyone running or evaluating equity momentum strategies. Allocators evaluating momentum ETFs (MTUM, QMOM, etc.) will gain a clear framework for what differentiates a "diluted" momentum product from a "concentrated" one. Quant practitioners will appreciate the detailed implementation choices and the empirical sensitivity analyses.

## How It Applies to AI Trading

The Gray-Vogel system is a benchmark every ML-equity researcher should beat (or honestly compare against). Many "ML alpha" strategies, when decomposed, turn out to be reproducing 12-2 momentum with extra steps. Before claiming ML alpha, attribute against a Gray-Vogel-style baseline.

For systematic strategy design, the book's lessons are directly applicable:
- **Concentration > diversification** for factor harvesting
- **Quality overlays** improve robustness without diluting edge
- **Rebalancing frequency** is a parameter, not a default
- **Drawdown tolerance** is the binding constraint, not signal quality

The companion volume *Quantitative Value* (2012) covers the same methodology applied to value investing. Together they form a complete systematic equity factor framework.

## Companion Volume

- *Quantitative Value* (Gray & Carlisle, 2012) — Same authors, same methodology, applied to value investing

## Rating

**9/10** — The most thorough practitioner book on equity momentum. Concrete, replicable, intellectually honest about both the edge and the drawdowns. Read alongside [[asset-management-andrew-ang|Asset Management (Ang)]] for the broader factor context.

## Sources

- Gray, Wesley R. and Vogel, Jack R. (2016). *Quantitative Momentum: A Practitioner's Guide to Building a Momentum-Based Stock Selection System*. Wiley.
- Jegadeesh, Narasimhan and Titman, Sheridan (1993). "Returns to Buying Winners and Selling Losers." *Journal of Finance*.

## Related

- [[momentum]] — The core anomaly
- [[cross-sectional-momentum]] — The specific strategy variant
- [[time-series-momentum]] — The companion strategy class
- [[trend-following]] — Closely related strategy (futures-applied)
- [[factor-investing]] — The broader discipline
- [[fama-french-factors]] — Where momentum lives in the factor zoo
- [[behavioral-finance]] — The mechanism behind the anomaly
- [[smart-beta]] — The product category for momentum ETFs

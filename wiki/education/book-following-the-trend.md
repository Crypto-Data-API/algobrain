---
title: "Following the Trend — Andreas Clenow (2013)"
type: source
created: 2026-04-15
updated: 2026-04-28
status: good
tags: [book, education, trend-following, systematic, futures, ctas]
source_type: book
source_author: "Andreas F. Clenow"
source_date: 2013
confidence: high
aliases: ["Following the Trend", "Clenow Trend"]
related:
  - "[[trend-following]]"
  - "[[managed-futures]]"
  - "[[ctas]]"
  - "[[momentum]]"
  - "[[turtle-traders]]"
  - "[[risk-parity]]"
  - "[[atr-position-sizing]]"
  - "[[walk-forward-validation]]"
---

## Overview

**Following the Trend: Diversified Managed Futures Trading** by Andreas Clenow, published in 2013, is the clearest practitioner explanation available of how systematic [[managed-futures|trend-following]] CTAs actually work. Clenow — a former hedge fund CIO who ran systematic futures portfolios — strips away the marketing mystique around CTAs and reveals what their strategies actually do: a diversified, slow-moving, breakout-and-trail trend-following system applied across roughly 50 liquid futures markets, sized by inverse-volatility (ATR) position sizing, with a target portfolio volatility of around 15% annualized.

The book includes complete trading rules, full-period backtests on 25+ years of data, and an honest accounting of the long, painful drawdowns trend strategies suffer when markets are choppy. Clenow's argument: the CTA "edge" is not a secret indicator or proprietary signal — it's the systematic discipline to take every trend signal across a deeply diversified universe and to size positions so no single market dominates portfolio risk.

## The Core System

Clenow describes a complete trend-following system that anyone can replicate:

1. **Universe**: ~50 liquid futures across equities, fixed income, currencies, energies, metals, grains, and softs
2. **Entry**: 50-day vs 100-day moving average crossover (or breakout of N-day high)
3. **Exit**: 3-ATR trailing stop or moving-average reversal
4. **Position size**: Risk a fixed percentage of equity (e.g. 0.2%) per trade, with ATR setting per-contract risk → equal *risk* contribution from each position regardless of asset volatility
5. **Portfolio constraint**: Cap total position count and sector exposure

This system, applied with discipline, has historically produced ~10-15% returns with ~15% volatility and 3-year drawdowns approaching -25% — close to the long-run profile of CTA indices like the SG Trend Index.

## Key Takeaways

- **CTAs are commodity trading advisors, but the strategy applies to all asset classes.** Modern "trend-following" includes equity index, bond, FX, and commodity futures — not just commodities.
- **Diversification across markets is the engine, not the indicator.** A trend system on 5 markets is fragile; on 50 markets, the law of large numbers smooths returns. The math of trend-following requires breadth.
- **ATR-based [[atr-position-sizing|position sizing]] is essential.** Without volatility-adjusted sizing, energy futures dominate portfolio P&L and bond futures contribute nothing. Equal risk weighting (not equal capital) is the foundation.
- **Long flat periods are the price of admission.** Trend-following has 30-50% of months losing, multi-year drawdowns, and brutal whipsaw periods (e.g. 2011-2013, 2015-2017). Investors who can't sit through them harvest none of the long-run premium.
- **Trend works because of structural slowness in market participants.** Pension funds, central banks, and corporates rebalance slowly, creating persistent drift in asset prices that fast traders are too small to arbitrage away. See [[trend-following#why-it-works]].
- **Rule simplicity beats rule complexity.** Clenow's tests show that adding filters, machine-learning overlays, and discretionary adjustments mostly degrade out-of-sample performance. The robust core is dumb-simple breakout + ATR trail.
- **Crisis alpha is real.** Trend systems were among the only strategies to make money in 2008, 2020, and 2022 — these are precisely the periods when investors most need diversification.
- **Sector concentration risk is a hidden killer.** Without sector caps, an entire trend system can pile into correlated commodity positions and lose in unison when the trend breaks.

## Who Should Read This

Anyone building or evaluating systematic futures strategies. Allocators evaluating CTAs will gain a clear picture of what they're paying for. Retail traders who want to run a slow, diversified, capacity-friendly system can literally implement Clenow's rules. The book is short (~250 pages) and the math is accessible (no calculus required).

## How It Applies to AI Trading

Clenow's system is a benchmark every systematic trader should beat (or honestly compare against) before deploying anything more complex. Modern ML trend-following models often add little after costs over the simple rules he describes — see [[walk-forward-validation]] for the methodology to honestly test whether your fancy model improves on the dumb baseline.

For backtesting hygiene, Clenow's open-data, fully-specified rules let you replicate his results exactly — a rare feature in trading literature. If your backtest engine can't reproduce his 1990-2013 performance to within reasonable tolerance, your engine has a bug.

The book pairs naturally with [[trend-following|Trend Following (Covel)]] (narrative + history) and [[fortune-formula|Fortune's Formula]] (Kelly sizing theory) for a complete picture of mechanical systematic trading.

## Companion Volumes

Clenow has written follow-ups extending the same systematic framework:
- *Stocks on the Move* (2015) — applying momentum/trend rules to single-name equities
- *Trading Evolved* (2019) — full Python implementation of his systems with code

## Rating

**9/10** — The clearest, most honest book on systematic trend-following ever written. If you want to actually run a CTA-style system, this is the book. Read it before signing up to any expensive trend-following course.

## Sources

- Clenow, Andreas F. (2013). *Following the Trend: Diversified Managed Futures Trading*. Wiley.

## Related

- [[trend-following]] — The strategy class
- [[managed-futures]] — The asset class CTAs trade
- [[ctas]] — Commodity Trading Advisors
- [[momentum]] — Closely related signal type
- [[turtle-traders]] — Predecessor system Clenow's rules echo
- [[risk-parity]] — Sister approach in portfolio construction
- [[atr-position-sizing]] — Position sizing technique central to the book
- [[walk-forward-validation]] — Backtesting methodology
- [[trend-following|Trend Following (Covel)]] — Narrative companion

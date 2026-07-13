---
title: "Regime Detection"
type: strategy
created: 2026-04-06
updated: 2026-07-13
status: good
tags: [regime-detection, hidden-markov-model, hmm, clustering, market-regimes, quantitative, adaptive-allocation]
aliases: ["Regime Switching", "Market Regime Detection", "HMM Trading", "Regime-Based Allocation"]
strategy_type: quantitative
timeframe: swing|position
markets: [stocks, futures]
complexity: advanced
backtest_status: untested
related: ["[[trend-following-cta]]", "[[mean-reversion]]", "[[garch-volatility]]", "[[kalman-filter-trading]]", "[[risk-budgeting]]", "[[book-the-man-who-solved-the-market]]", "[[book-probabilistic-ml-for-finance]]", "[[cryptodataapi]]"]
---

# Regime Detection

## Overview

Regime detection uses statistical models -- primarily **Hidden Markov Models (HMMs)** and clustering algorithms -- to identify the current market state and switch strategies accordingly. Markets do not behave uniformly: they alternate between distinct **regimes** such as low-volatility trending, high-volatility mean-reverting, and crisis/crash states. A [[trend-following-cta]] strategy that thrives in trending regimes will bleed capital in choppy, mean-reverting conditions. A [[mean-reversion]] strategy that profits in ranges will get destroyed in strong trends.

Regime detection solves this by acting as a **meta-strategy** -- a strategy-of-strategies. Rather than forcing a single approach across all market conditions, it identifies the current regime and allocates capital to the strategy best suited for that environment. In a trending regime, it deploys [[trend-following-cta]] or [[momentum-rotation]]. In a mean-reverting regime, it activates [[pairs-trading]] or [[rsi-mean-reversion]]. In a crisis regime, it raises cash, hedges, or activates [[tail-risk-hedging]].

The approach is grounded in academic research (Hamilton 1989 regime-switching models) and is used extensively by CTAs, macro hedge funds, and institutional asset managers. The core insight is that market return distributions are **mixtures** of different underlying distributions, and identifying which distribution is currently generating prices dramatically improves trading decisions.

## How It Works

### Hidden Markov Models (HMMs)
An HMM assumes the market exists in one of N hidden states (regimes), each with its own return distribution (mean, variance) (Source: [[book-the-man-who-solved-the-market]]) (Source: [[book-probabilistic-ml-for-finance]]). The model estimates:
- **Transition probabilities:** The likelihood of switching from one regime to another (e.g., 95% chance of staying in trend, 5% of switching to mean-reversion).
- **Emission parameters:** The return distribution for each regime (e.g., Regime 1: mean=+0.1%/day, vol=0.8%; Regime 2: mean=0%, vol=2.5%).
- **Current state probability:** Given recent observations, the posterior probability of being in each regime.

The Baum-Welch algorithm trains the model on historical data, and the Viterbi algorithm or forward-backward algorithm infers the current regime in real-time (Source: [[book-probabilistic-ml-for-finance]]).

### Clustering Approaches
An alternative to HMMs uses **k-means clustering** or **Gaussian mixture models** on feature vectors (rolling returns, volatility, correlation, volume) to group historical periods into regimes. New observations are classified into the nearest cluster. This approach is simpler but loses the temporal transition structure that HMMs capture.

## Rules / Application

1. **Define regimes:** Typically 2-4 states. A common three-regime model: (a) Bull/trending -- positive drift, low vol; (b) Neutral/mean-reverting -- zero drift, moderate vol; (c) Crisis -- negative drift, high vol.
2. **Train the HMM** on 5-10 years of daily returns for the target market (e.g., S&P 500, crude oil futures). Use 2-3 states and Gaussian emissions as a starting point.
3. **Infer current regime** each day using the forward algorithm. Assign the regime with the highest posterior probability.
4. **Strategy mapping:**
   - **Trending regime:** Deploy [[trend-following-cta]], [[momentum-rotation]], or increase equity allocation.
   - **Mean-reverting regime:** Deploy [[pairs-trading]], [[mean-reversion]], [[grid-trading]], or reduce position sizes.
   - **Crisis regime:** Raise cash, activate [[tail-risk-hedging]], or go to 100% bonds/short positions.
5. **Rebalance** when the regime probability crosses a threshold (e.g., >70% probability of a new regime for at least 2 consecutive days to avoid whipsaw).
6. **Retrain** the model quarterly or semi-annually on expanding or rolling windows to capture evolving market structure.

## Example

**Market:** S&P 500 daily returns, three-regime HMM.

1. The HMM is trained on 2015-2024 data. It identifies: Regime A (bull: mean +0.06%/day, vol 0.7%), Regime B (choppy: mean -0.01%/day, vol 1.2%), Regime C (crisis: mean -0.3%/day, vol 3.0%).
2. Through January 2025, the model assigns 92% probability to Regime A. The portfolio is 80% equities using a [[trend-following-cta]] overlay.
3. In early February, vol picks up and returns become erratic. Regime B probability rises to 75%. The system shifts to a [[mean-reversion]] strategy with reduced position sizes (50% equities, 50% bonds).
4. In March, a sharp selloff triggers Regime C at 85% probability. The system moves to 20% equities, 60% bonds, 20% [[tail-risk-hedging]] via long puts.
5. The crisis fades by May. Regime A probability exceeds 70% for 3 consecutive days. The system re-allocates to trend-following.
6. **Result:** The regime-aware portfolio avoids the worst of the drawdown and re-enters the recovery earlier than a static allocation.

## Advantages

- **Adaptive:** Automatically adjusts strategy selection to current market conditions instead of forcing a one-size-fits-all approach
- Provides a principled, probabilistic framework for the intuitive idea that "different markets need different strategies"
- Dramatically reduces [[drawdown]] by detecting crisis regimes early and shifting to defensive positioning
- HMMs capture temporal persistence (markets tend to stay in regimes) through transition probabilities
- Combines naturally with [[risk-budgeting]] and [[garch-volatility]] for regime-conditional risk management
- Academically grounded with decades of research (Hamilton 1989, Ang & Bekaert 2002)

## Disadvantages

- **Regime detection is inherently lagging** -- by the time the model identifies a new regime with high confidence, the transition has already begun
- **Overfitting risk:** HMMs with too many states or features will fit noise in historical data and fail out-of-sample (Source: [[book-the-man-who-solved-the-market]])
- The number of regimes (states) must be chosen a priori -- BIC/AIC can help, but there is no definitive answer
- **Whipsaw:** Rapid regime switches produce frequent strategy changes, increasing transaction costs and potentially destroying returns
- Regime definitions are **model-dependent** -- different models may disagree on the current regime
- HMM training requires significant historical data and computational expertise; implementation is non-trivial
- The assumption that future regimes will resemble historical regimes may fail during truly novel market events

## Sources

- [[book-the-man-who-solved-the-market]] — Renaissance Technologies' use of Hidden Markov Models and signal processing techniques for market regime detection, drawing on the team's speech recognition and codebreaking backgrounds
- [[book-probabilistic-ml-for-finance]] — Tatsat et al. (2023) provide detailed HMM implementations for regime detection in Python, including Baum-Welch training, Viterbi decoding, and Gaussian mixture emission models for financial time series

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/regimes/current` — current long-horizon market regime (10-state taxonomy)
- `GET /api/v1/quant/market` — HMM regime probabilities, 4h/24h horizons (15-min refresh)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/liquidity/regime/score` — liquidity fragility composite (0-100)

**Historical data:**
- `GET /api/v1/quant/timeline` — daily market regime labels, 2019-now
- `GET /api/v1/quant/regimes/history` — full 6-regime Parquet download (2020-yesterday)
- `GET /api/v1/quant/history` — point-in-time probability records for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/regimes/current"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

## See Also

- [[trend-following-cta]] -- the strategy deployed during detected trending regimes
- [[mean-reversion]] -- the strategy deployed during detected mean-reverting regimes
- [[garch-volatility]] -- volatility forecasting that complements regime detection
- [[kalman-filter-trading]] -- adaptive estimation that can be combined with regime-switching models
- [[tail-risk-hedging]] -- crisis-regime defensive strategy
- [[risk-budgeting]] -- regime-conditional risk allocation framework

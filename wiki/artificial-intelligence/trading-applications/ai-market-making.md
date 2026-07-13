---
title: "AI Market Making"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, algorithmic, market-microstructure, liquidity]
aliases: ["AI Market Making", "ML Market Making", "Machine Learning Market Making"]
domain: [market-microstructure, ai-trading]
difficulty: advanced
related: ["[[ai-trading-agents]]", "[[market-microstructure-overview]]", "[[market-making]]", "[[hummingbot]]", "[[hyperliquid]]", "[[foundation-models]]", "[[reinforcement-learning-trading]]", "[[liquidity]]", "[[artificial-intelligence]]"]
---

# AI Market Making

**AI market making** uses machine learning models to dynamically provide [[liquidity]] by quoting bid and ask prices. Unlike traditional algorithmic market makers that use fixed rules, AI-powered systems adapt their spreads, inventory, and risk parameters in real-time using [[reinforcement-learning-trading|reinforcement learning]], [[foundation-models|LLM]]-based regime detection, and predictive models.

## How market makers earn (and lose)

A market maker quotes a bid and an ask simultaneously, aiming to capture the **spread** when buyers and sellers both trade against it. The business has two structural risks that every model must manage:

- **Inventory risk** — accumulating a one-sided position (e.g. ending up long after a sell-off) and being exposed to adverse price moves.
- **Adverse selection** — being picked off by *informed* traders who know something the maker doesn't; the maker tends to buy right before prices fall and sell right before they rise.

The canonical academic baseline is the **Avellaneda–Stoikov model** (2008), which derives optimal bid/ask quotes as a function of inventory, volatility, and time horizon, skewing quotes to mean-revert inventory toward zero. AI market making generalises this: instead of assuming a fixed stochastic model, it *learns* the quoting policy from data.

## How AI Improves Market Making

| Function | Traditional Approach | AI Approach |
|----------|---------------------|-------------|
| **Spread setting** | Fixed or volatility-based | Dynamic based on order flow prediction |
| **Inventory management** | Mean-reversion rules | RL-optimized hedging |
| **Adverse selection** | Basic toxicity filters | Predictive models of informed flow |
| **Regime detection** | Manual parameter switching | Automatic regime classification |
| **Cross-asset hedging** | Pre-defined correlations | Real-time correlation learning |

## Modelling approaches

| Approach | What it does | Where it fits |
|----------|-------------|---------------|
| **Avellaneda–Stoikov + extensions** | Closed-form/optimal-control quoting from inventory & volatility | Strong, interpretable baseline; many "AI" systems are calibrated versions of this |
| **Reinforcement learning** (PPO, SAC, DQN) | Learns a quoting/hedging policy that maximises risk-adjusted P&L | Adapts spread/skew to live order flow; hard to train safely (sim-to-real gap) |
| **Supervised microstructure models** | Predict short-horizon price move / [[order-flow-imbalance|order-flow imbalance]] to skew quotes | Feed a signal into a rules engine; easier to validate than end-to-end RL |
| **LLM/regime classifiers** | Classify market regime (calm/volatile/news-driven) and switch parameter sets | Slow-loop overlay, not in the latency-critical hot path |

## Adverse selection: the core ML problem

The single most valuable thing a market-making model can do is predict **toxic flow** — order flow likely to be informed. Microstructure features used for this include order-book imbalance, trade sign autocorrelation, quote-to-trade ratios, and **VPIN** (Volume-Synchronised Probability of Informed Trading). When toxicity is high, the model widens spreads or pulls quotes; when it's low, it tightens to win volume. Getting this wrong is how market makers blow up — they keep quoting tight into a one-directional informed market and bleed on every fill.

## Tools & Frameworks

- **[[hummingbot]]**: Open-source market making bot (Avellaneda–Stoikov and other strategies) with extensible ML/strategy plugins; widely used in crypto
- **Custom RL agents**: PPO/SAC agents trained on historical limit-order-book data, typically with [[pytorch|PyTorch]] + Stable-Baselines3
- **LLM regime detection**: [[foundation-models|Claude/GPT-class models]] for classifying market regimes from news as a slow overlay (never in the per-quote latency path)

## Where It's Applied

- **Crypto DEXes**: [[hyperliquid|Hyperliquid]] (on-book perps), [[uniswap|Uniswap]] v3 concentrated liquidity (passive AMM-style provision)
- **Centralized exchanges**: [[binance|Binance]], Coinbase liquidity-provider programs
- **Institutional**: firms such as Citadel Securities, Jump Trading, and Wintermute run proprietary, heavily quantitative market-making across equities, options, and crypto

## What kills AI market makers

- **Sim-to-real gap** — an RL agent trained on a backtest assumes its quotes don't move the market; in production its own fills change the book, breaking the policy.
- **Regime breaks** — a model tuned on a calm regime quotes far too tight into a volatility spike or flash crash and accumulates a catastrophic one-sided inventory.
- **Latency disadvantage** — slower makers are systematically adversely selected by faster participants; ML inference in the hot path can itself be the disadvantage.
- **Overfitting microstructure** — order-book patterns are non-stationary and exchange-specific; a model that nails one venue/period can be worthless the next.

## See Also

- [[market-making]] — The underlying business and classic strategies
- [[ai-trading-agents]] — Agent architectures
- [[reinforcement-learning-trading]] — RL for trading decisions
- [[market-microstructure-overview]] — The microstructure context
- [[hummingbot]] — Open-source market making bot
- [[hyperliquid]] — DEX where market makers operate
- [[artificial-intelligence]] — AI section hub

## Sources

- Avellaneda, M. & Stoikov, S., "High-frequency trading in a limit order book" (Quantitative Finance, 2008) — the canonical optimal-quoting model.
- Easley, López de Prado & O'Hara, "Flow Toxicity and Liquidity in a High-Frequency World" (Review of Financial Studies, 2012) — VPIN and adverse selection.
- Guéant, O., *The Financial Mathematics of Market Liquidity* (2016) — inventory-management market-making theory.
- Hummingbot documentation (hummingbot.org) — open-source market-making implementation.

---
title: Backtesting Checklist — Strategy Validation Framework
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [education, backtesting, methodology, checklist]
related:
  - "[[quantconnect-bootcamp]]"
  - "[[python-quant-stack]]"
  - "[[financial-datasets]]"
---

# Backtesting Checklist — Is This Strategy Real?

This is a practical checklist for validating any trading strategy, ML-based or otherwise. Most backtested strategies fail in live trading because of avoidable methodological errors. Check every box before risking real capital.

## Pre-Backtest: Data Quality

- [ ] **Survivorship bias** — Does your dataset include delisted and bankrupt stocks? If your stock universe only contains companies that survived to today, your backtest is inflated. Use survivorship-bias-free data from [[financial-datasets]]
- [ ] **Look-ahead bias** — Are you using any information that would not have been available at the time of the trade? Point-in-time data is essential. Earnings revisions, index reconstitutions, and late-reported data are common culprits
- [ ] **Data adjustments** — Are prices adjusted for splits, dividends, and mergers? Unadjusted data creates phantom signals
- [ ] **Sufficient history** — Does your data cover multiple market regimes (bull, bear, sideways, high/low volatility)? A strategy tested only in a bull market proves nothing

## During Backtest: Realistic Simulation

- [ ] **Transaction costs** — Include commissions, spread costs, and market impact. A strategy with a 0.1% daily edge disappears with 0.05% round-trip costs
- [ ] **Slippage** — Can you actually execute at the price your backtest assumes? Illiquid assets and large orders move the market against you
- [ ] **Proper train/test split** — Time series data must be split chronologically, never randomly. The test set must come after the training set. Use walk-forward or expanding window validation
- [ ] **No future information leakage** — Features computed from the full dataset (z-scores, normalizations) must use only past data at each point
- [ ] **Realistic position sizing** — Are position sizes achievable given the asset's liquidity? Can you actually trade the volume your backtest assumes?

## Post-Backtest: Validation

- [ ] **Out-of-sample performance** — Does the strategy work on data it has never seen? If OOS performance drops dramatically, you have overfit
- [ ] **Parameter sensitivity** — Does the strategy break if you change parameters slightly? Robust strategies work across a range of parameter values, not just one magic number
- [ ] **Walk-forward analysis** — Re-optimize periodically on expanding windows and test on subsequent periods. This simulates how the strategy would be managed in real time
- [ ] **Monte Carlo simulation** — Randomize trade order and entry timing to estimate the distribution of possible outcomes, not just the single backtest path
- [ ] **Regime analysis** — How does the strategy perform in different market conditions? A strategy that only works in trending markets will blow up in range-bound periods

## Before Going Live

- [ ] **Paper trading period** — Run the strategy in real time with simulated money for at least 1-3 months. Verify that live fills match backtest assumptions
- [ ] **Drawdown tolerance** — Can you psychologically and financially survive the maximum drawdown shown in your backtest? Real drawdowns are typically worse
- [ ] **Kill switch criteria** — Define in advance: at what drawdown or underperformance level do you stop the strategy? Write this down before going live
- [ ] **Position sizing for real capital** — Start with a fraction of intended capital. Scale up only after confirming live performance matches expectations

## The Hard Truth

If your strategy passes every item on this checklist and still shows meaningful edge, you likely have something real. Most strategies fail at step one. That is normal — the checklist is not the obstacle, it is the filter that protects your capital. See [[quantconnect-bootcamp]] for a platform that enforces many of these checks automatically.

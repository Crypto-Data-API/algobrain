---
title: Stop-Loss
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [stop-loss, risk-management]
aliases: [stop-loss-order, stop]
related:
  - "[[position-sizing]]"
  - "[[atr]]"
  - "[[support-and-resistance]]"
  - "[[leverage]]"
  - "[[slippage]]"
  - "[[book-market-wizards]]"
  - "[[book-reminiscences-of-a-stock-operator]]"
  - "[[trade-repair-and-rolling]]"
  - "[[iron-condors]]"
  - "[[credit-spread]]"
---

# Stop-Loss

A stop-loss is a predetermined price level or order type designed to exit a losing position and cap the maximum loss on a trade.

## Overview

The stop-loss is the most fundamental risk management tool. It removes emotion from the exit decision by defining in advance the point at which a trade thesis is invalidated. Without stops, small losses can grow into account-destroying drawdowns. Every serious trading plan specifies stop placement before entry. [[jesse-livermore]] learned this lesson through repeated, costly experience -- his principle of "cut your losses quickly" is one of the most enduring maxims in trading history (Source: [[book-reminiscences-of-a-stock-operator]]).

## Types of Stops

- **Hard stop (fixed)**: A stop-loss order placed on the exchange at a specific price. Executes automatically when triggered. Guarantees exit but may experience [[slippage]] in fast markets.
- **Trailing stop**: Moves with the price in the favorable direction, locking in profits as the trade progresses. Set as a fixed dollar/percent distance or based on [[atr]].
- **Mental stop**: A price level at which the trader intends to exit but no order is placed. Requires discipline and is not recommended for most traders -- emotions tend to override intentions.
- **Time stop**: Exiting a trade after a specified duration if the expected move has not materialized.

## Stop Placement Methods

- **Technical levels**: Place stops below [[support-and-resistance|support]] (for longs) or above resistance (for shorts), with a small buffer for noise.
- **ATR-based**: Set stops at a multiple of [[atr]] (e.g., 1.5x-3x ATR) from entry. Adapts to current [[volatility]].
- **Percentage-based**: Fixed percentage from entry (e.g., 2% or 5%). Simple but does not adapt to market conditions.
- **Structure-based**: Below the most recent swing low (long) or above the most recent swing high (short).

## Common Mistakes

- Setting stops too tight (stopped out by normal noise)
- Setting stops too wide (excessive risk per trade)
- Moving stops further away to "give the trade room" -- this increases risk after the fact
- Not using stops at all, especially with [[leverage]]

Nearly every trader interviewed in *Market Wizards* emphasized the importance of predetermined exits, with many citing failure to use stops as the most common cause of catastrophic losses among new traders (Source: [[book-market-wizards]]).

## Options-Specific Exit Rules

Options positions — particularly premium-selling strategies like [[credit-spread|credit spreads]], [[iron-condors]], and [[wheel-strategy|the wheel]] — use a different exit framework than equity stop-losses:

- **Loss exit**: Close when the position reaches 2× the credit received. For example, a short put spread sold for $1.00 credit is closed if it reaches $2.00. This prevents small losses from becoming the maximum loss.
- **Profit target**: Close at 50% of maximum profit. This captures the majority of the available profit while reducing time exposure to [[gamma]] risk as expiration approaches.
- **Time exit (21-DTE rule)**: Many premium sellers mechanically close or roll positions at ~21 days to expiration, because at that point [[theta]] decay accelerates but gamma risk spikes — the "gamma trap." See [[trade-repair-and-rolling]] for rolling mechanics.

These pre-defined exit rules remove emotion from the decision and prevent the sunk-cost fallacy of "holding to see if it comes back." (Source: [[recovering-losing-options-positions]])

## Trading Relevance

The stop-loss directly determines the risk per trade and feeds into [[position-sizing]] calculations. Proper stop placement is a balance: tight enough to control risk, wide enough to avoid being triggered by normal market fluctuation. ATR-based stops offer the best compromise by adapting to the asset's current volatility regime.

## Sources

- [[book-market-wizards]] — Top traders unanimously stress predetermined exits and cutting losses as the foundation of survival
- [[book-reminiscences-of-a-stock-operator]] — Livermore's career illustrates the catastrophic cost of failing to cut losses and the power of disciplined stop usage
- (Source: [[recovering-losing-options-positions]]) — Options-specific exit rules: 2× credit loss exit, 50% profit target, 21-DTE time exit

## Related

- [[position-sizing]] -- stop distance determines position size
- [[atr]] -- used for adaptive stop placement
- [[support-and-resistance]] -- common anchor for stop levels
- [[leverage]] -- makes stops even more critical
- [[slippage]] -- stops may execute at worse prices in volatile markets

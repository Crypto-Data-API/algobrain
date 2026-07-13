---
title: Position Sizing
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [position-sizing, risk-management, volatility]
aliases: [position-size, "Bet Sizing", "Trade Sizing"]
domain: [risk-management]
prerequisites: ["[[stop-loss]]", "[[volatility]]"]
difficulty: beginner
related:
  - "[[stop-loss]]"
  - "[[leverage]]"
  - "[[atr]]"
  - "[[volatility]]"
  - "[[diversification]]"
  - "[[correlation]]"
  - "[[kelly-criterion]]"
  - "[[risk-of-ruin]]"
  - "[[options-position-sizing]]"
  - "[[atr-position-sizing]]"
  - "[[risk-management]]"
  - "[[book-market-wizards]]"
  - "[[book-trading-in-the-zone]]"
---

# Position Sizing

Position sizing is the process of determining how much capital to allocate to each individual trade, balancing potential return against the risk of loss.

## Overview

Position sizing is arguably the most important element of risk management. A great trading strategy with poor position sizing can blow up an account, while a mediocre strategy with disciplined sizing can survive and compound. The goal is to risk enough to make meaningful gains, but not so much that a string of losses becomes catastrophic. Bruce Kovner, interviewed in *Market Wizards*, described position sizing as the single most important factor in his success, stating that he would reduce size whenever he was losing and increase it only when his trading was going well (Source: [[book-market-wizards]]).

## Key Methods

### Fixed Fractional (Percent Risk) — The 2% Rule

The most common approach. Risk a fixed percentage of total capital on each trade (typically 1–2%).

- **Formula**: Position size = (Account size × Risk %) / (Entry price - [[stop-loss]] price)
- **Options variant**: Position size = (Account Value × Risk %) / Max Loss Per Contract
- Example: $100,000 account, 1% risk ($1,000), entry at $50, stop at $48. Position size = $1,000 / $2 = 500 shares.

**Survivability math**: At 2% risk per trade, a trader can survive roughly 50 consecutive full losses before the account is depleted — a statistically implausible streak with any rational edge. Exceeding 5% per trade is classified as gambling rather than trading, because a much shorter losing streak becomes account-threatening. (Source: [[recovering-losing-options-positions]])

### ATR-Based Sizing

Use [[atr]] to normalize position sizes across assets with different volatility profiles.

- **Formula**: Position size = Risk amount / (ATR multiplier x ATR value)
- This ensures each position carries roughly equal risk regardless of the asset's inherent [[volatility]].

### Kelly Criterion

The [[kelly-criterion|Kelly criterion]] is a mathematical formula that calculates the theoretically optimal fraction of capital to risk to maximise long-run *geometric* (compound) growth, based on win rate and average win/loss ratio.

- **Formula**: `Kelly % = W - ((1 - W) / R)`, where W = win rate, R = win/loss ratio.
- **Worked example**: a strategy with W = 0.55 and R = 1.0 gives `f* = 0.55 - (0.45 / 1.0) = 0.10` — full Kelly says risk 10% per trade. Most traders run **half Kelly (5%)** or **quarter Kelly (2.5%)** instead.
- In practice, traders use fractional Kelly to reduce aggressiveness and account for estimation error: W and R are *estimated* with noise, and over-estimating either pushes you above full Kelly, where long-run growth turns **negative** despite a positive edge. The drawdown reduction from fractional Kelly is super-linear while the growth-rate cost is sub-linear — see [[risk-of-ruin]].

### Volatility Targeting

Size positions inversely to their [[volatility]] so each contributes roughly equal *risk* (not equal *capital*) to the portfolio.

- **Formula**: `Position weight ∝ target_vol / asset_vol` — a high-vol asset gets a smaller allocation, a low-vol asset a larger one.
- Normalises the dollar risk contribution of every position; the basis of [[risk-parity]] and most institutional systematic books.
- [[atr-position-sizing|ATR-based sizing]] is the practical per-trade implementation of this idea.

## Trading Relevance

Key principles:
- Never risk more than 1–2% of capital on a single trade
- Scale position size to [[volatility]] — smaller positions in volatile assets
- Account for [[correlation]] — correlated positions compound risk
- Reduce size during drawdowns; increase cautiously during winning streaks
- Position sizing determines whether you survive your inevitable losing streaks (Source: [[book-trading-in-the-zone]])
- **Concentration limit**: No more than 15–20% of capital should sit in a single underlying, because concentrated single-name positions are vulnerable to earnings, headline, or CEO risk (Source: [[recovering-losing-options-positions]])
- **Diversify dimensions**: Spread risk across underlyings, sectors, strategies (e.g., [[covered-calls]], [[protective-puts]], [[iron-condors]]), and expiration dates so uncorrelated trades can offset each other (Source: [[recovering-losing-options-positions]])

### Correlation and effective bet count

Per-trade risk limits are necessary but not sufficient. Ten positions each sized to 1% risk are *not* a 10% aggregate exposure if they are highly [[correlation|correlated]] — in stress, correlations spike toward +1 and a "diversified" book behaves like a single concentrated bet. The practical adjustment is to size against the *portfolio's* risk under stressed correlations, capping the summed risk of any correlated cluster (sector, factor, or theme) the same way you cap a single name. This is the link between per-trade sizing and [[risk-of-ruin]]: convex losses and correlated concentration are the two effects that make realised ruin probability far higher than naive per-trade sizing implies.

### Sizing across the equity curve

A recurring theme from elite traders is that sizing should *adapt to recent performance*: cut size in drawdowns (when you may be out of sync with the regime) and add cautiously after sustained wins. This is the opposite of the instinctive Martingale impulse to "size up to recover" — adding risk after losses is the single most reliable path to ruin (Source: [[book-market-wizards]]).

## Sources

- [[book-market-wizards]] — Kovner and other top traders cite position sizing as the key to long-term survival and compounding
- [[book-trading-in-the-zone]] — Douglas emphasizes that proper sizing allows traders to maintain psychological equilibrium during losing streaks
- (Source: [[recovering-losing-options-positions]]) — The 2% rule survivability math, 5% gambling threshold, and concentration limits

## Related

- [[stop-loss]] -- defines the risk per trade for sizing calculations
- [[atr]] -- volatility-based sizing input
- [[leverage]] -- amplifies effective position size
- [[diversification]] -- spreading capital across multiple positions

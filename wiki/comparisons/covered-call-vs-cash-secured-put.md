---
title: Covered Call vs Cash-Secured Put
type: comparison
created: 2026-04-07
updated: 2026-04-07
status: good
tags:
  - options
  - premium-selling
  - income
subjects:
  - "[[covered-call]]"
  - "[[wheel-strategy]]"
comparison_dimensions:
  - bias
  - capital
  - assignment
  - premium
  - risk
  - taxes
  - equivalence
related:
  - "[[put-call-parity]]"
  - "[[options-greeks]]"
  - "[[theta-decay]]"
---

# Covered Call vs Cash-Secured Put

## Overview

The [[covered-call]] and cash-secured put are the two foundational premium-selling strategies in options trading. They form the two halves of the popular [[wheel-strategy]]: sell puts until assigned, then sell calls until shares are called away, and repeat. Despite looking like different strategies, they are synthetically equivalent thanks to put-call parity. Understanding their differences in practice -- assignment outcomes, capital use, and tax treatment -- matters for choosing the right one for your situation.

## Comparison Table

| Dimension | Covered Call | Cash-Secured Put |
|-----------|-------------|-----------------|
| **Directional Bias** | Neutral to mildly bullish | Bullish (want to buy at lower price) |
| **Capital Required** | Own 100 shares of stock | Cash to buy 100 shares at strike |
| **Position Setup** | Long stock + short call | Cash reserve + short put |
| **Max Profit** | Premium + (strike - stock cost) | Premium received |
| **Max Loss** | Stock drops to zero minus premium | Strike price minus premium (stock drops to zero) |
| **Assignment Outcome** | Shares called away at strike (sell stock) | Shares assigned at strike (buy stock) |
| **When Premium Is Highest** | At-the-money calls on volatile stocks | At-the-money puts on volatile stocks |
| **Break-Even** | Stock cost minus premium received | Strike minus premium received |
| **Margin Treatment** | No margin required (covered by shares) | Cash or margin required for full assignment |
| **Tax Considerations** | May trigger capital gains on shares if assigned | Cost basis is strike minus premium received |
| **Synthetic Equivalence** | Equivalent to short put at same strike | Equivalent to covered call at same strike |

## Key Differences

**What you already own.** The most practical difference is your starting position. If you already own shares and want income, write covered calls. If you have cash and want to acquire shares at a discount, sell cash-secured puts. The starting point drives the choice more than any theoretical advantage.

**Assignment outcomes.** When a covered call is assigned, you sell your shares at the strike price. This can be painful if the stock has rallied well above your strike. When a cash-secured put is assigned, you buy shares at the strike price. This can be painful if the stock has fallen well below your strike. The emotional experience differs even though the risk/reward math is identical.

**Capital efficiency.** In a margin account, cash-secured puts may require less capital than owning 100 shares outright, especially on high-priced stocks. This can improve return on capital. However, in a cash account or IRA, both strategies tie up similar amounts of capital.

**Tax treatment.** Covered calls can create complex tax situations. If the call is assigned, the premium is added to the stock sale proceeds. If you have held the shares for over a year, assignment could trigger long-term capital gains. Cash-secured puts are simpler: premium received reduces the cost basis of acquired shares, and the holding period starts on assignment.

**Synthetic equivalence.** Put-call parity proves that a covered call (long stock + short call) has the same payoff profile as a short put at the same strike. This is not just theoretical -- if you chart the P/L of both positions at expiration, they are identical. The differences are practical: tax treatment, margin requirements, and what happens on assignment.

## When to Use Each

**Use covered calls when:**
- You already own shares and want to generate income
- You would be happy to sell at the strike price
- You want to reduce your cost basis over time
- The stock is range-bound and you expect limited upside
- You are in a tax-advantaged account (IRA) where assignment taxes do not matter

**Use cash-secured puts when:**
- You want to buy a stock but at a lower price
- You are comfortable owning the stock if assigned
- You have cash sitting idle and want to earn premium on it
- The stock has pulled back and you believe support will hold
- You want a simpler tax treatment than covered calls

**Use both in the [[wheel-strategy]].** Sell puts until assigned, then sell calls on the assigned shares until called away. This creates a continuous income cycle and is one of the most popular systematic options strategies for retail traders.

## Verdict

Covered calls and cash-secured puts are functionally the same strategy viewed from different starting points. The choice is purely practical: sell calls if you own shares, sell puts if you have cash. For traders running the full [[wheel-strategy]], you will use both continuously. The key insight is not which is better but understanding that put-call parity makes them equivalent -- so choose based on your current holdings, tax situation, and whether you want to acquire or exit a position.

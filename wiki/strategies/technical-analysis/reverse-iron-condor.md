---
title: "Reverse Iron Condor"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, reverse-iron-condor, breakout, volatility, debit-spread, defined-risk]
strategy_type: quantitative
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: ["[[iron-condor]]", "[[straddle-strangle]]", "[[strip-strap]]", "[[implied-volatility]]", "[[bull-call-spread]]"]
---

# Reverse Iron Condor

## Overview

The Reverse Iron Condor is the **opposite of an [[iron-condor]]**: instead of selling the wings to collect premium, the trader buys OTM spreads on both sides to profit from a large move in either direction. Specifically, you buy a [[bull-call-spread]] above the current price and buy a [[bear-put-spread]] below it. The result is a debit strategy with **defined risk** on both sides that profits when the underlying breaks out of a range. It is a breakout play suited for situations where you expect a significant move but are uncertain about direction.

## Setup

1. **Buy 1 OTM call** and **sell 1 further OTM call** (bull call spread above the stock price).
2. **Buy 1 OTM put** and **sell 1 further OTM put** (bear put spread below the stock price).
3. All four legs share the **same expiration** -- 30-60 DTE to allow time for the breakout.
4. **Net debit paid** = cost of both spreads combined. This is the maximum possible loss.
5. Choose spread widths and distances from the stock price based on the expected magnitude of the move.

## Payoff Profile

| Scenario | Outcome |
|---|---|
| Stock rallies past the call spread | Call spread reaches max value; put spread expires worthless; profit |
| Stock drops past the put spread | Put spread reaches max value; call spread expires worthless; profit |
| Stock stays in the range | Both spreads lose value; max loss = total debit paid |

**Max profit** = width of one spread minus total debit paid (achieved when one side is fully ITM). **Max loss** = total debit paid. **Break-evens** = upper spread lower strike + debit, and lower spread upper strike - debit.

## When to Use

- You expect a **breakout** from a consolidation range but are unsure of the direction.
- A high-impact event (earnings, Fed meeting, product launch) is approaching that will drive a large move.
- [[implied-volatility]] is relatively low, making the debit spreads inexpensive.
- You want the defined-risk profile that a naked [[straddle-strangle]] purchase does not offer on cost.

## Advantages
- Defined risk -- max loss is the debit paid, known at entry
- Profits from big moves in either direction (a pure breakout play)
- Lower capital requirement than buying a straddle or strangle outright
- No margin stress or unlimited-loss scenarios

## Disadvantages
- Both spreads can expire worthless if the stock stays range-bound -- total debit is lost
- Max profit is capped by the width of the spreads (unlike an unlimited-profit straddle)
- Requires a large enough move to overcome the debit cost on at least one side
- [[theta]] decay works against you on both sides simultaneously

## See Also
- [[iron-condor]] -- the opposite strategy that profits from range-bound conditions
- [[straddle-strangle]] -- an uncapped breakout alternative with higher cost
- [[strip-strap]] -- directionally biased volatility plays
- [[bull-call-spread]] / [[bear-put-spread]] -- the individual spread components

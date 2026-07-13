---
title: "Delta-Neutral"
type: concept
created: 2026-04-07
updated: 2026-06-22
status: excellent
tags: [options, risk-management, hedge-funds]
aliases: ["Delta Neutral", "Delta-Neutral Strategy"]
related: ["[[delta]]", "[[delta-hedging]]", "[[gamma-scalping]]", "[[volatility-arbitrage]]", "[[market-neutral]]", "[[hedging]]", "[[options]]", "[[the-greeks]]", "[[implied-volatility]]"]
domain: [risk-management, derivatives]
difficulty: advanced
---

A delta-neutral portfolio is one whose total [[delta]] is zero, meaning it has no directional exposure to the underlying asset's price movements. By combining long and short positions in options and the underlying stock (or other derivatives), a trader eliminates first-order price risk and instead profits from changes in [[volatility]], time decay ([[theta]]), or the curvature of the options payoff ([[gamma]]). Delta-neutral positioning is the foundation of options market making, [[volatility-arbitrage]], and several hedge fund strategies.

## Overview

Delta measures how much an option's price changes for a $1 move in the underlying. A call option with delta 0.50 gains $0.50 when the stock rises $1. To create a delta-neutral position, a trader offsets the delta of their options with an opposing position in the underlying. For example, buying 10 call contracts (each controlling 100 shares) with delta 0.50 creates a total delta of +500 shares. Shorting 500 shares of stock brings the total delta to zero.

[[ed-thorp]], widely regarded as the pioneer of quantitative hedge fund strategies, developed delta-neutral hedging techniques in the 1960s after working out option pricing formulas that preceded the Black-Scholes model. In [[book-a-man-for-all-markets|A Man for All Markets]], Thorp describes how he used delta-neutral positions to exploit mispriced warrants and convertible bonds, generating consistent returns regardless of market direction.

Delta neutrality is not static — as the underlying price moves, the delta of the options changes (this change is measured by [[gamma]]). A position that is delta-neutral at $100 will develop directional exposure as the stock moves to $105. This requires continuous rehedging, known as [[delta-hedging|dynamic hedging]] or [[gamma-scalping]].

## The Greeks of a Delta-Neutral Book

Removing delta does not remove risk — it changes *which* risks you carry. A delta-neutral book is a bet on the remaining [[the-greeks|Greeks]]. The table below summarizes what each Greek does once delta is zeroed:

| Greek | Measures | Long-options (long gamma) book | Short-options (short gamma) book |
|-------|----------|-------------------------------|----------------------------------|
| **[[delta]]** | Directional exposure | ≈ 0 by construction (rehedged) | ≈ 0 by construction (rehedged) |
| **[[gamma]]** | Rate of change of delta | Positive — profits from big moves either way | Negative — loses from big moves |
| **[[theta]]** | Time decay per day | Negative — bleeds premium daily | Positive — collects premium daily |
| **[[vega]]** | Sensitivity to [[implied-volatility]] | Typically positive — gains if IV rises | Typically negative — gains if IV falls |
| Net P&L driver | Realized vol > implied vol | Realized vol < implied vol |

The fundamental trade-off is **gamma vs. theta**: long gamma costs you theta (you pay rent to own convexity), while short gamma pays you theta (you collect rent for selling convexity but assume tail risk). A delta-neutral position is therefore a pure expression of the [[volatility-arbitrage|realized-vs-implied volatility]] view.

## How It Works

**Setting up a delta-neutral position**:

1. Calculate the total delta of all option positions (sum of individual deltas x contract size).
2. Offset with shares of the underlying: if total options delta is +300, short 300 shares; if delta is -300, buy 300 shares.
3. Monitor continuously — delta changes as the underlying moves, as time passes, and as [[implied-volatility]] shifts.

**What you are exposed to when delta-neutral**:

- **Gamma**: The rate at which delta changes. Long gamma positions profit from large moves in either direction (but lose from time decay). Short gamma positions profit from stability (collect theta) but lose from large moves.
- **Theta**: Time decay. Long options positions lose value daily; short options positions gain. Delta-neutral positions that are short gamma collect theta as compensation for the risk of large moves.
- **Vega**: Sensitivity to [[implied-volatility]]. Delta-neutral positions can be constructed to be long or short vega, profiting from volatility changes.
- **Higher-order Greeks**: Charm (delta decay over time), vanna (delta sensitivity to volatility), and volga (vega sensitivity to volatility) become relevant for large or complex positions.

**Rehedging frequency**: Market makers rehedge continuously; portfolio managers may rehedge daily or when delta exceeds a threshold (e.g., rehedge when portfolio delta exceeds 50 deltas). More frequent rehedging reduces directional risk but increases [[transaction-costs]].

## Worked Example: Setting Up and Rehedging

*Illustrative numbers, rounded for clarity.* A trader believes [[implied-volatility]] on a $100 stock is too cheap and wants to be long volatility while neutral on direction.

1. **Establish the position.** Buy 10 at-the-money call contracts, each delta 0.50. Each contract controls 100 shares, so option delta = 10 × 100 × 0.50 = **+500 deltas**.
2. **Neutralize.** Short 500 shares of stock (−500 deltas). Net delta = 0. The book is now long gamma, long vega, and short theta.
3. **Stock rises to $105.** Because the position is long gamma, the calls' delta rises (say to 0.62), pushing option delta to +620. The short stock is still −500, leaving net delta of **+120** — the book has become directionally long. To rehedge, the trader **shorts 120 more shares**, locking in a gain from the favorable move.
4. **Stock falls back to $100.** Call delta drops back toward 0.50, so option delta falls to ~+500 while the trader is now short 620 shares (−620). Net delta ≈ **−120** — directionally short. To rehedge, the trader **buys back 120 shares** — buying low after having sold high.

Each round trip of "sell high on the way up, buy low on the way down" harvests cash. That harvesting is [[gamma-scalping]]: the long-gamma book monetizes movement. The catch is [[theta]] — every day the stock fails to move enough, time decay erodes the premium paid. The position is profitable only if **realized volatility exceeds the implied volatility paid** for the options, net of [[transaction-costs|rehedging costs]]. A short-gamma (option-selling) trader runs the same mechanic in reverse: they collect theta daily but are forced to buy high and sell low when rehedging, losing money in fast markets — the classic "picking up pennies in front of a steamroller."

## Trading Applications

- **Options market making**: Market makers quote bid-ask spreads on options and immediately hedge directional risk by taking offsetting positions in the underlying. Their profit comes from the bid-ask spread and managing the Greeks, not from directional bets.
- **[[volatility-arbitrage]]**: If a trader believes [[implied-volatility]] is mispriced relative to expected [[realized-volatility]], they can buy (or sell) options and delta-hedge to isolate the volatility bet. If realized vol exceeds implied vol, a long gamma position profits through [[gamma-scalping]].
- **[[convertible-bond-arbitrage]]**: Buying convertible bonds and shorting the underlying stock to isolate the embedded option's value. A strategy used by [[ed-thorp]], [[ken-griffin]], and many hedge funds.
- **Pairs and statistical arbitrage**: Many [[market-neutral]] strategies achieve approximate delta neutrality by holding equal dollar amounts long and short within correlated sectors.
- **Risk management**: Even directional traders use delta-neutral techniques to hedge portions of their portfolio during uncertain periods, maintaining exposure to other Greeks while removing market direction risk.
- **Delta-neutral income**: Selling [[options]] structures (iron condors, strangles, calendar spreads) constructed to open near zero delta to harvest [[theta]] while remaining indifferent to small directional moves. These are short-gamma strategies that profit in quiet, range-bound markets and require disciplined rehedging or strict stops.

## How Traders Use This

- **Volatility view, not price view.** Reach for delta-neutral structures when you have a conviction about *how much* an asset will move, not *which way*. Long gamma if you expect realized vol to exceed implied; short gamma if you expect calm.
- **Choosing rehedge bands.** Rehedge too often and [[transaction-costs]] eat the gamma P&L; rehedge too rarely and unhedged delta drift dominates. Many desks use a fixed delta band (e.g., ±50 deltas) or a fixed time interval, tuned to the asset's [[volatility]] and spread.
- **Reading the order book through dealer gamma.** Because options market makers run delta-neutral books, their aggregate gamma positioning shapes intraday flow. When dealers are net long gamma they dampen volatility (sell rallies, buy dips while rehedging); when net short gamma they amplify it (chase the move). This "dealer gamma" lens is widely used to anticipate pinning near large strikes and accelerating moves on [[options-expiration]].

## Common Pitfalls and Risks

- **Delta neutral is not risk neutral.** The biggest beginner error is treating a delta-neutral book as "safe." A short-gamma position can be flat on delta and still suffer catastrophic losses in a gap move.
- **Gap and overnight risk.** Rehedging assumes you can trade continuously. Earnings, news, and weekend gaps move the underlying before you can adjust — devastating for short gamma.
- **Hedging slippage and costs.** Each rehedge pays the bid-ask spread and [[market-impact]]. In illiquid underlyings, rehedging frictions can exceed the theoretical edge.
- **Vega and skew risk.** A delta-and-gamma-neutral book can still be heavily exposed to a shift in the [[implied-volatility]] surface or volatility skew. Neutralizing only the first two Greeks leaves vega, vanna, and volga live.
- **Pin risk at expiration.** Near expiry, a stock hovering at the strike makes delta unstable (it whips between 0 and 1), making the position nearly impossible to hedge cleanly.
- **Borrow and financing.** Shorting the underlying to hedge requires locating borrow; hard-to-borrow names carry fees that erode the strategy, and forced buy-ins can blow up the hedge.

## Related

- [[delta]] — The first-order Greek measuring directional exposure
- [[delta-hedging]] — The mechanic of offsetting delta with the underlying
- [[gamma-scalping]] — Profiting from rehedging a long-gamma, delta-neutral position
- [[the-greeks]] — Full set of option sensitivities a neutral book trades
- [[volatility-arbitrage]] — Trading mispriced volatility via delta-hedged options
- [[implied-volatility]] — The vol level paid or collected by the position
- [[market-neutral]] — Broader category of strategies with zero market beta
- [[hedging]] — Risk reduction techniques
- [[convertible-bond-arbitrage]] — Classic delta-neutral strategy
- [[options-expiration]] — When pin risk and dealer-gamma effects peak

## Sources

- (Source: [[book-option-volatility-and-pricing]]) — Natenberg's comprehensive treatment of delta-neutral trading
- (Source: [[book-a-man-for-all-markets]]) — Ed Thorp's development and application of delta-neutral hedging

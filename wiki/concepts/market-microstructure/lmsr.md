---
title: "Logarithmic Market Scoring Rule (LMSR)"
type: concept
created: 2026-05-14
updated: 2026-06-11
status: good
tags: [prediction-markets, market-microstructure, automated-market-maker, behavioral-finance]
aliases: ["LMSR", "Hanson Scoring Rule", "Log Market Scoring Rule"]
domain: [market-microstructure]
prerequisites: ["[[prediction-markets]]", "[[market-microstructure]]"]
difficulty: advanced
related: ["[[prediction-markets]]", "[[manifold-markets]]", "[[augur]]", "[[polymarket]]", "[[automated-market-maker]]", "[[constant-product-amm]]"]
---

The **Logarithmic Market Scoring Rule (LMSR)** is an automated market maker designed for prediction markets, invented by [[robin-hanson|Robin Hanson]] in 2003. It provides infinite liquidity at a bounded cost to the market operator and is the canonical mechanism for binary and categorical event markets, used in some form by nearly every prediction-market platform that predates the deep crypto-native order books of the 2020s.

## The cost function

LMSR is defined by a single cost function over the vector of outstanding shares across outcomes:

```
C(q) = b · log( Σ_i exp(q_i / b) )
```

where `q_i` is the number of shares outstanding on outcome `i`, and `b > 0` is the **liquidity parameter** (chosen by the market operator). The cost to move the market from share vector `q` to `q'` is simply `C(q') − C(q)`. A trader buying `Δ` shares of outcome `i` pays `C(q + Δ·e_i) − C(q)`.

The **instantaneous price** of outcome `i` is the partial derivative of the cost function:

```
p_i = ∂C/∂q_i = exp(q_i / b) / Σ_j exp(q_j / b)
```

This is the softmax of the share vector, scaled by `1/b`.

### Binary market example

For a binary market with outcomes YES and NO, holding `q_Y` and `q_N` shares respectively:

```
p_YES = exp(q_Y/b) / ( exp(q_Y/b) + exp(q_N/b) )
p_NO  = exp(q_N/b) / ( exp(q_Y/b) + exp(q_N/b) )
```

Starting from `q_Y = q_N = 0`, both prices are 0.5. Buying YES shares pushes `q_Y` up, which raises `p_YES` and lowers `p_NO`. The price impact per share is governed by `b`.

## Properties

- **Prices always sum to 1** — by construction, the softmax over outcomes is a probability distribution. This makes LMSR prices directly interpretable as the market's consensus probability of each outcome.
- **Liquidity parameter `b`** — controls how much the price moves per share traded. A higher `b` means larger trades barely move the price (deep liquidity), but it costs the operator more to subsidise. A lower `b` makes the market thinner and more responsive to individual trades.
- **Bounded operator loss** — the worst-case loss to the market operator across the entire life of the market is at most `b · log(N)` for `N` outcomes. For a binary market, that is `b · log(2)`. This is the explicit subsidy the operator pays in exchange for bootstrapping liquidity.
- **Always quotes, no spread** — in its pure form, LMSR continuously provides a buy and sell price equal to the same marginal `p_i`. There is no bid/ask spread (real implementations often add a small fee).
- **Path independence** — the final cost of arriving at a share vector `q` depends only on `q`, not on the sequence of trades that produced it. Two traders splitting a large order into many small pieces pay the same total as one large fill at the same final state.

## Why prediction markets historically chose LMSR over a CLOB

Early prediction markets had a chicken-and-egg liquidity problem. A traditional [[central-limit-order-book|CLOB]] requires two-sided interest at every price level: someone has to be willing to post a bid and someone else has to post an ask. On a niche question — "Will candidate X win the 2008 Iowa caucus?" — there often was no one waiting to take the other side at any given moment.

LMSR sidesteps this entirely. The market maker is a deterministic function, not a counterparty deciding whether to quote. It always provides a price on both sides. The market operator effectively underwrites the liquidity, capped at `b · log(N)`. This was a reasonable trade for academic, research, and play-money platforms where the goal was information aggregation, not trading-venue economics.

## Where LMSR is used today

- **[[manifold-markets|Manifold Markets]]** — uses a "Maniswap" variant for binary markets, derived from LMSR with adjustments for its play-money economy
- **[[augur]] v1** — used LMSR before later versions transitioned toward order-book hybrids
- **Academic and research prediction-market platforms** — including Iowa Electronic Markets descendants and PredictIt-style research venues
- **Hanson's original Foresight Exchange** and follow-on academic projects
- **Internal corporate prediction markets** — companies like Google, Microsoft, and HP have used LMSR for internal forecasting markets

## Why [[polymarket]] uses a hybrid CLOB instead

Polymarket bootstrapped enough liquidity via crypto-native users and market makers that a traditional order book became viable. The platform runs a CLOB matched off-chain with on-chain settlement. The trade-offs vs LMSR:

**CLOB advantages**:

- True price discovery from competing limit orders — prices reflect actual capital willing to take each side, not a fixed mathematical curve
- No operator subsidy required — Polymarket does not pay a `b · log(N)` cost per market
- Better behaviour in thick markets — with deep books, bid/ask spreads compress toward zero, beating LMSR's deterministic price impact
- Limit orders are possible — traders can post passive bids and earn the spread, which itself attracts more liquidity

**CLOB downsides** (where LMSR would have helped):

- Thin Polymarket markets have wide spreads or no quotes at all on one side, exactly the regime an LMSR would have continued quoting through
- New markets need an explicit market-maker incentive program to bootstrap

Polymarket's bet is that in 2026 crypto-native capital and professional market makers solve the liquidity bootstrap problem better than a subsidised mathematical AMM.

## Trading implications

- **No limit orders on pure LMSR** — you accept the AMM's quoted price at the moment of execution. No resting bids/asks, no maker rebates
- **Deterministic slippage** — your cost is computable directly from the cost function before you trade. There are no order-book-imbalance surprises, no hidden orders, no last-look rejections
- **No sandwich attacks or front-running** in the on-chain MEV sense (for pure LMSR) — the price function is deterministic from current state, so a front-runner gains nothing by ordering ahead of you beyond moving the price you pay. There is no mempool race for a specific bid/ask
- **Cross-venue arbitrage** — when an LMSR market and a CLOB venue (e.g. [[polymarket]]) quote the same event, arbitrage execution dynamics are predictable on the LMSR side and depend on order-book state on the CLOB side. Spreads can persist when one venue is thin
- **Position exit cost is symmetric to entry** — selling back into the LMSR walks down the same curve you walked up. Large positions cannot be exited without round-trip slippage cost, even when other traders agree with the price

## Limitations

- **Operator subsidy is real** — `b · log(N)` is a genuine cash cost. For high-volume commercial venues, this either eats into margin or has to be funded by fees layered on top
- **Slow convergence with high `b`** — if `b` is set high enough to provide CLOB-like liquidity depth, the price moves so little per share that converging to a new consensus requires moving large share volume
- **Cannot exit instantly without slippage** — even when every other trader agrees the price should move, you still pay the curve cost to unwind your position. There is no equivalent of crossing a thick book at a single clearing price
- **No price-time priority or limit order semantics** — pure LMSR cannot express "I will buy at 0.42 but not at 0.43". Traders who want passive execution have no native mechanism
- **Binary / categorical only in canonical form** — LMSR is naturally suited to a finite outcome set. Extending to continuous outcomes (e.g. "what will CPI print?") requires combinatorial or interval encodings that complicate implementation

## Related

- [[prediction-markets]]
- [[manifold-markets]]
- [[augur]]
- [[polymarket]]
- [[automated-market-maker]]
- [[constant-product-amm]]
- [[central-limit-order-book]]
- [[robin-hanson]]
- [[market-microstructure]]

## Sources

- Hanson, Robin. "Combinatorial Information Market Design." *Information Systems Frontiers*, vol. 5, no. 1, 2003. (Original LMSR paper)
- Hanson, Robin. "Logarithmic Market Scoring Rules for Modular Combinatorial Information Aggregation." *Journal of Prediction Markets*, 2007.

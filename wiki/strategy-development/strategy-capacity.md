---
title: "Strategy Capacity"
type: concept
created: 2026-06-22
updated: 2026-06-22
status: good
tags: [methodology, quantitative, risk-management, liquidity, slippage, market-microstructure]
aliases: ["Capacity", "Strategy Capacity Limits", "AUM Capacity", "Alpha Capacity"]
domain: [strategy-development, market-microstructure]
difficulty: advanced
related: ["[[edge-taxonomy]]", "[[market-impact]]", "[[alpha-decay]]", "[[liquidity]]", "[[slippage]]", "[[crowding]]", "[[sharpe-ratio]]", "[[transaction-costs]]", "[[position-sizing]]", "[[failure-modes]]", "[[average-daily-volume]]"]
---

# Strategy Capacity

**Strategy capacity** is the maximum amount of capital (AUM) a strategy can deploy before its own trading degrades the returns it is trying to capture. Below capacity, adding capital scales profits roughly linearly; above capacity, [[market-impact|market-impact costs]] and [[alpha-decay|alpha decay]] grow faster than gross alpha, so net returns flatten and then fall. Capacity is the single most under-appreciated number in strategy development: a strategy with a stellar small-account backtest can be worthless at scale, and conversely a low-Sharpe strategy with enormous capacity can be more valuable to a large fund than a high-Sharpe one that saturates at \$5M. Every deployed strategy should carry a capacity estimate, just as it carries an [[edge-taxonomy|edge source]] and a kill-criteria block.

## Overview

The reason capacity exists is that **you are not a price-taker once you are big.** A small trader fills at the quoted price. A large trader's own orders push price against them — buying lifts the offer, selling presses the bid — so the *marginal* dollar of capital earns less than the first dollar. The strategy's gross edge is a fixed pool (e.g., "stocks that gapped down on no news mean-revert ~40 bps over three days"); the more capital chasing that fixed pool of mispricing, the more each participant pays in impact to access it, until impact eats the edge entirely. Capacity is the AUM at which **net alpha is maximized** (or, depending on definition, the AUM at which net alpha hits zero). The two are different and worth stating explicitly.

## What drives capacity

| Driver | Effect on capacity | Why |
|---|---|---|
| **Liquidity of the universe** ([[average-daily-volume\|ADV]]) | Higher ADV → higher capacity | You can trade a larger absolute size while staying a small % of volume |
| **Turnover / holding period** | Faster turnover → lower capacity | Impact is paid every round-trip; a 1-day strategy pays it ~250x/year, a 1-year strategy once |
| **Edge size (gross alpha in bps)** | Bigger edge → higher capacity | A fat edge can absorb more impact before going negative |
| **Number of independent positions** | More breadth → higher capacity | Capital spreads across many names, so each name carries a smaller % of ADV |
| **Signal decay speed** | Slow-decaying signal → higher capacity | You can trade patiently (VWAP/TWAP), spreading orders over time to cut impact |
| **Concentration in time** | Time-clustered trades → lower capacity | If everyone's signal fires the same minute (breakouts, open/close), impact spikes |
| **Crowding** ([[crowding]]) | More crowding → lower capacity | Other funds compete for the same fixed edge pool, raising the cost of accessing it |
| **Shortability / borrow** | Tight borrow → lower capacity on short side | Hard-to-borrow names cap short capacity regardless of ADV |

## Market-impact models (the core mechanism)

Capacity is fundamentally a statement about [[market-impact]]. The widely used **square-root law** of impact says the price move from trading a quantity Q is approximately:

```
impact_bps ≈ Y * sigma * sqrt( Q / ADV )
```

where `sigma` is daily volatility, `Q/ADV` is the order size as a fraction of average daily volume, and `Y` is a market-specific constant (empirically order ~0.5-1). The key feature: impact grows with the **square root** of participation, so doubling your size raises per-share impact by ~41%, not 100% — but you are paying that higher rate on twice as many shares, so *total* impact cost grows faster than capital. Net edge per dollar therefore declines as size grows, and crosses zero at the capacity limit.

A practical participation heuristic: keep daily trading under **5-10% of ADV** per name to keep impact modest. Trading 20%+ of ADV makes you the market and impact dominates.

## Capacity vs Sharpe trade-off

There is a structural tension between [[sharpe-ratio|Sharpe]] and capacity:

- **High-Sharpe strategies are often low-capacity.** The cleanest, fastest-reverting inefficiencies (intraday mean-reversion, stat-arb on small caps, latency edges) produce high Sharpe but saturate quickly — a few million to low hundreds of millions.
- **Low-Sharpe strategies can be high-capacity.** Slow factor tilts (value, low-vol, large-cap momentum) earn modest Sharpe but absorb billions because turnover is low and the universe is liquid.

For a large allocator, **capacity-weighted alpha** (dollars of net profit the strategy can actually generate) often matters more than Sharpe. A 2.0-Sharpe strategy capped at \$20M and a 0.6-Sharpe strategy that runs \$5B can produce wildly different absolute dollar profits. This is why the largest funds gravitate toward lower-Sharpe, high-capacity factor strategies, while capacity-constrained high-Sharpe edges stay in small prop shops and boutique funds.

## Worked example (illustrative)

*Hypothetical, round numbers, for illustration only.*

A daily mean-reversion strategy on US mid-caps:
- Gross edge: **40 bps per round-trip** (before costs)
- Universe: 200 names, average ADV \$50M each, daily turnover ~50% of the book
- Impact constant `Y * sigma` ≈ 2% (i.e., trading 100% of a name's ADV would cost ~200 bps)

If the strategy runs **\$100M**, with ~50% turnover spread over 200 names, each name's daily trade is roughly \$100M * 0.5 / 200 ≈ \$0.25M per name, i.e., 0.5% of that name's \$50M ADV. Square-root impact: `2% * sqrt(0.005)` ≈ 14 bps round-trip. Net edge ≈ 40 - 14 = **26 bps** — healthy.

Scale to **\$1B**: per-name trade ≈ \$2.5M = 5% of ADV. Impact: `2% * sqrt(0.05)` ≈ 45 bps. Net edge ≈ 40 - 45 = **-5 bps** — the strategy now *loses* money on the marginal dollar. Net dollar profit peaks somewhere *below* \$1B — that peak is the capacity. (A fuller treatment integrates net edge × capital across the size range to find the AUM that maximizes total net profit, which lands meaningfully below the break-even AUM.)

The takeaway: capacity here is in the low hundreds of millions, set entirely by how fast impact rises relative to the fixed 40 bps edge.

## How traders use this

- **Estimate capacity before deploying, not after.** Combine the gross edge (in bps), the turnover, and an impact model to find the AUM where net edge approaches zero. Deploy well below it.
- **Express trades as % of ADV.** A discipline of "never trade more than X% of any name's ADV" converts an abstract capacity limit into a concrete daily order constraint. See [[position-sizing]].
- **Trade patiently when the signal allows.** Slow signals can be worked with VWAP/TWAP/POV algos over hours or days, dramatically cutting impact and raising effective capacity. Fast signals cannot, which caps them.
- **Monitor realized vs modeled impact.** If your realized [[slippage]] starts exceeding the model, you are nearer capacity (or [[crowding|crowded]]) than you thought — a leading indicator of [[alpha-decay]].
- **Allocate by capacity-weighted alpha, not Sharpe alone.** For sizing across a book of strategies, weight by the net dollars each can generate at its capacity, not just its risk-adjusted ratio.

## Pitfalls

- **Assuming the small-account backtest scales.** The most common and most expensive mistake. A backtest implicitly assumes you are a price-taker; at scale you are not. Always overlay an impact model.
- **Ignoring time-clustering.** Two strategies with identical ADV footprints can have very different capacity if one trades evenly through the day and the other dumps everything on the close.
- **Forgetting the short side.** ADV-based capacity is symmetric, but borrow availability is not. Short capacity can be a fraction of long capacity in small or hard-to-borrow names.
- **Confusing break-even capacity with optimal capacity.** Net dollar profit peaks *below* the AUM where net edge hits zero. Running to break-even AUM maximizes nothing.
- **Treating capacity as static.** [[crowding|Crowding]] shrinks capacity over time as competitors arrive; a strategy comfortable at \$200M today may saturate at \$80M once it is widely known. Capacity erodes with the edge.
- **Letting AUM ambition override the edge.** Raising more capital than the strategy can hold guarantees [[alpha-decay]] — the marginal capital destroys returns for everyone already in.

## Sources

- Kyle, A. (1985). "Continuous Auctions and Insider Trading." *Econometrica* — foundational price-impact (lambda) model
- Almgren, R. & Chriss, N. (2000). "Optimal Execution of Portfolio Transactions." *Journal of Risk* — temporary vs permanent impact, execution scheduling
- Grinold, R. & Kahn, R. (1999). *Active Portfolio Management* — breadth, the fundamental law, and capacity intuition
- Tóth, B. et al. (2011). "Anomalous Price Impact and the Critical Nature of Liquidity." *Physical Review X* — empirical square-root impact law
- Pedersen, L. (2015). *Efficiently Inefficient* — practitioner treatment of capacity, crowding, and the capacity-Sharpe trade-off

General market knowledge; no specific wiki source ingested yet.

## Related

- [[market-impact]] — the cost mechanism that creates capacity limits
- [[alpha-decay]] — what happens when you exceed capacity
- [[liquidity]] / [[average-daily-volume]] — the primary capacity driver
- [[slippage]] — the realized symptom of impact
- [[crowding]] — competition that shrinks capacity over time
- [[sharpe-ratio]] — the metric that trades off against capacity
- [[transaction-costs]] — the broader cost stack capacity sits within
- [[position-sizing]] — how capacity limits translate into order sizes
- [[edge-taxonomy]] — capacity depends on which edge you harvest
- [[failure-modes]] — over-capacity deployment as a failure mode

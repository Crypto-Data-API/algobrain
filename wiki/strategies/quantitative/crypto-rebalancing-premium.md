---
title: "Crypto Rebalancing Premium"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [crypto, altcoins, quantitative, portfolio-construction, mean-reversion, market-neutral, diversification]
aliases: ["Rebalanced vs drift crypto basket", "Volatility harvesting in crypto", "Quantpedia #0701"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [structural, risk-bearing]
edge_mechanism: "A frequently rebalanced equal-weight basket mechanically sells relative winners and buys relative losers; with highly volatile, imperfectly correlated coins that mean-revert relative to one another, this earns a 'diversification return' over the drifting buy-and-hold basket, whose weights concentrate into whatever has already run — the counterparty is the passive holder who lets winners compound unchecked."
data_required: [ohlcv-daily]
min_capital_usd: 20000
capacity_usd: 5000000
crowding_risk: low
expected_sharpe: 0.6  # prior only; source claims 2.93 pre-cost (2018-2021) — daily rebalancing across 27 coins is cost-heavy
expected_max_drawdown: 0.25
breakeven_cost_bps: 20
decay_evidence: "Published 2021 (Hanicová & Vojtko). The premium is a mathematical consequence of volatility and low correlation rather than a behavioural anomaly, so publication decay should be limited — but it inverts when one coin trends persistently versus the rest (e.g. BTC dominance runs)."
kill_criteria: |
  - rolling 12-month spread (rebalanced minus drift leg) net of costs < 0
  - average pairwise 90-day correlation of the universe > 0.9 for 3 months
  - drawdown > 25%
related: ["[[quantpedia]]", "[[quantpedia-strategy-encyclopedia]]", "[[rebalancing]]", "[[crypto-allocation]]", "[[diversification]]", "[[pairs-trading]]", "[[crypto-momentum]]", "[[multi-strategy-crypto-portfolio]]"]
---

# Crypto Rebalancing Premium

Hold a daily-rebalanced equal-weight crypto basket and short a partially offsetting buy-and-hold (drifting) version of the same basket, isolating the return that rebalancing itself adds. Harvested from [[quantpedia|Quantpedia]] #0701, summarising Hanicová & Vojtko (2021) (Source: [[quantpedia-strategy-encyclopedia]]).

## Edge Source

**Structural + risk-bearing** ([[edge-taxonomy]]). The "rebalancing premium" (also called diversification return or volatility harvesting) is largely arithmetic: the gap between a rebalanced portfolio's growth rate and the weighted growth of its components rises with component volatility and falls with their correlation — see [[rebalancing]]. Crypto is the extreme case of both.

## Why This Edge Exists

A buy-and-hold basket lets weights drift toward past winners. A rebalanced basket continually trims winners and adds to losers, so it profits whenever coins mean-revert *relative to one another* (Source: [[quantpedia-strategy-encyclopedia]]). The passive holder's drift is the other side. The premium is paid for bearing the risk that relative mean reversion fails — i.e. one coin trends away from the pack for a long time, which is exactly when the rebalancer keeps selling the winner.

## Null Hypothesis

If coin returns were independent random walks with no relative mean reversion, the rebalanced basket would still show a small positive growth-rate advantage purely from variance reduction, but the long-rebalanced / short-drift spread would have near-zero expected arithmetic return and be eaten by daily rebalancing fees. The strategy needs the spread to exceed turnover costs by a clear margin.

## Rules

- **Universe:** 20-30 liquid coins (source used 27), with survivorship-free membership at each date.
- **Long leg:** equal-weight basket rebalanced to 1/N daily.
- **Short leg:** equal-weight basket set at inception and left to drift, sized at 70% of the long leg's notional (source ratio), with the ratio reset daily.
- **Implementation in practice:** because both legs share constituents, net them — the actual trades are the daily rebalancing trades plus a net ~30% long residual exposure to the basket.
- **Rebalance tolerance (adaptation):** only trade a coin when its weight deviates >20% from target, to cut turnover.

## Implementation Pseudocode

```python
# Crypto rebalancing premium — illustrative only
universe = liquid_coins(n=27, as_of=today)          # survivorship-free
w_long  = {c: 1/len(universe) for c in universe}      # rebalanced leg
w_drift = drift_weights(start_weights, returns)       # buy-and-hold leg
net = {c: w_long[c] - 0.70 * w_drift[c] for c in universe}

for c, target in net.items():
    if abs(current_weight(c) - target) > 0.2 * abs(target):
        trade_to(c, target * book_nav)
```

## Indicators / Data Used

- Daily closes for the universe; realised volatilities and average pairwise correlation (the premium's two drivers).
- Optional overlay: dominance / breadth data to detect a one-coin trending regime where the premium inverts (see [[crypto-momentum]]).

## Example Trade

Illustrative two-coin day: book $100k, long leg 50/50 in A and B. A rises 10%, B falls 10% → long weights become 55/45; the rebalance sells $5k A and buys $5k B. If the next day A −5% and B +5%, the rebalanced leg gains relative to the drifting leg, which kept its A overweight. The daily P&L is the sum of many such small relative reversions.

## Performance Characteristics

- **Source claim (pre-cost, 2018-2021):** 7.65% annual return, 2.6% volatility, Sharpe 2.93. The card also lists a maximum drawdown of −99.99%, which is inconsistent with the volatility figure and likely a data error — do not rely on it (Source: [[quantpedia-strategy-encyclopedia]]).
- **Cost overlay:** daily rebalancing of 27 coins can turn over well over 1,000% per year; at 10-20 bps round-trip on mid-cap alts this can consume most of a 7-8% gross spread. The tolerance band is essential.
- The long residual (~30% net long the basket) means real-world P&L includes significant crypto beta that the headline 2.6% volatility does not reflect unless hedged.

## Capacity Limits

Constrained by the least-liquid constituents: rebalancing trades on the smallest names hit thin books. A few million USD is reasonable for a top-30 universe; larger books should restrict to top-15 coins.

## What Kills This Strategy

- **Persistent relative trends** — a BTC-dominance run or a single-coin mania makes the rebalancer keep selling the winner.
- **Correlation convergence** — in crashes all coins move together, shrinking the premium to zero while costs continue.
- **Delistings / survivorship** — backtests on today's universe inflate results ([[survivorship-bias]]).
- Generic modes in [[failure-modes]].

## Kill Criteria

- Rolling 12-month net spread < 0.
- Average pairwise 90-day correlation > 0.9 for 3 consecutive months.
- Drawdown > 25%.

## Advantages

- Mechanism grounded in portfolio arithmetic rather than a fragile behavioural story.
- Low crowding: few traders run explicit rebalanced-vs-drift spreads.
- Doubles as a disciplined allocation rule for a long-only crypto sleeve ([[crypto-allocation]]).

## Disadvantages

- Turnover-heavy; highly fee-sensitive.
- Negative convexity to trending regimes — the opposite profile to [[crypto-momentum]].
- Headline source statistics contain an obvious inconsistency.

## Sources

- (Source: [[quantpedia-strategy-encyclopedia]]) — Quantpedia #0701; primary paper Hanicová & Vojtko (2021), with Willenbrock (cited on the card) on the diversification-return mechanism.

## Getting the Data (CryptoDataAPI)

Live: `GET /api/v1/coins/top` for the universe and `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d` for daily closes per coin. Historical: `GET /api/v1/backtesting/klines` plus `GET /api/v1/backtesting/symbols` and `GET /api/v1/backtesting/daily-snapshots/{date}` for point-in-time universe membership. See [[cryptodataapi-coins]], [[cryptodataapi-market-data]] and [[cryptodataapi-backtesting]].

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/daily-snapshots/2021-06-01"
```

### AI agent workflow

- **Universe** — rebuild the 27-coin universe on each historical date from `GET /api/v1/backtesting/daily-snapshots/{date}` so delisted coins stay in the test
- **Premium drivers** — compute realised vol and average pairwise correlation from `GET /api/v1/backtesting/klines`; the expected premium scales with vol² × (1 − correlation)
- **Regime gate** — pause when `GET /api/v1/market-health/altcoin-breadth` shows narrow, one-coin-led markets where relative mean reversion fails
- **Cost check** — simulate the 20% tolerance band vs strict daily rebalance and keep only the variant whose spread beats fees
- Orchestrate through [[cryptodataapi-mcp]]

## Related

- [[rebalancing]] · [[crypto-allocation]] · [[diversification]] · [[crypto-momentum]] · [[multi-strategy-crypto-portfolio]] · [[quantpedia]]

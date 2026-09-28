---
title: "Commodity Skewness Strategy"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [commodities, futures, quantitative, market-neutral, factor-investing, anomalies, crypto]
aliases: ["Skewness effect in commodities", "Commodity lottery factor", "Return asymmetry in commodity futures", "Quantpedia #0281", "Quantpedia #0664"]
strategy_type: quantitative
timeframe: position
markets: [commodities, futures, crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, risk-bearing]
edge_mechanism: "Speculators overpay for lottery-like, positively skewed commodity futures and underpay for negatively skewed ones; hedging pressure and short-selling frictions keep the mispricing alive. Longing low-skew and shorting high-skew contracts collects the premium those skew-seeking buyers leave behind."
data_required: [ohlcv-daily, futures-continuous-contracts]
min_capital_usd: 100000
capacity_usd: 200000000
crowding_risk: low
expected_sharpe: 0.4  # prior only; source claims 0.82 pre-cost (1990-2022)
expected_max_drawdown: 0.25
breakeven_cost_bps: 60
decay_evidence: "Skewness pricing in commodities documented by Fernandez-Perez, Frijns, Fuertes & Miffre (2018); Quantpedia's own replication (Dujava & Vojtko 2023) extends to 2022. No post-2023 out-of-sample evidence harvested."
kill_criteria: |
  - rolling 36-month net Sharpe < 0
  - drawdown > 25%
  - long-short skew spread collapses (rank dispersion of 12m skew in bottom decile of history) for 12 months
related: ["[[quantpedia]]", "[[quantpedia-strategy-encyclopedia]]", "[[max-anomaly]]", "[[lottery-stock-anomaly]]", "[[commodity-carry-strategy]]", "[[commodity-momentum]]", "[[commodity-value-strategy]]", "[[hedging-pressure]]", "[[skew-trading]]"]
---

# Commodity Skewness Strategy

A monthly long-short commodity futures portfolio that buys the contracts with the most negative trailing return skewness and sells those with the most positive skewness. Harvested from [[quantpedia|Quantpedia]] #0281 (Dujava & Vojtko, 2023), with the related return-asymmetry variant #0664 (Ďurian & Padyšák, 2020) (Source: [[quantpedia-strategy-encyclopedia]]).

## Edge Source

**Behavioral + risk-bearing** ([[edge-taxonomy]]). It is the commodity cousin of the equity [[lottery-stock-anomaly]] and [[max-anomaly]]: skew-loving speculators bid up right-tailed contracts; holding left-tailed contracts is compensated crash risk.

## Why This Edge Exists

Investors systematically misprice asymmetric risk, overpaying for positively skewed payoffs and underpaying for negatively skewed ones; in commodities, [[hedging-pressure]] and structural imbalances between producers and consumers reinforce this, while limits to arbitrage and short-selling frictions let it persist (Source: [[quantpedia-strategy-encyclopedia]]). The counterparty is the speculator buying "upside optionality" in a futures contract.

## Null Hypothesis

If skewness carried no price, a portfolio sorted on trailing 12-month skew would have zero expected return and would simply pay roll costs, commissions and slippage — roughly 0.5-1% a year for a monthly-rebalanced 6-contract book. The long-short must beat that and a multiple-testing haircut (skew windows, number of legs and the asymmetry measure are all choices).

## Rules

- **Universe:** 22 liquid commodity futures (energy, metals, grains, softs, livestock), front or most-liquid contract, rolled before delivery.
- **Signal:** skewness of daily returns over the past 12 months.
- **Portfolio:** long the 3 lowest-skew (most negative) contracts, short the 3 highest-skew; equal weight.
- **Rebalance:** monthly.
- **Asymmetry variant (#0664):** replace skewness with the IE asymmetry measure over 260 daily returns; long the bottom 7, short the top 7. Correlation with the skewness version ~0.46, so the two can be blended.
- **Sizing:** volatility-scale each leg to equal risk (adaptation; source is equal-weight).

## Implementation Pseudocode

```python
# Commodity skewness long-short — illustrative only
for month_end in calendar:
    rets = daily_returns(universe, lookback_days=252)
    skew = rets.skew()                         # per contract
    longs  = skew.nsmallest(3).index
    shorts = skew.nlargest(3).index
    target = {c:  1/6 for c in longs} | {c: -1/6 for c in shorts}
    rebalance(target, roll_rule="before_first_notice")
```

## Indicators / Data Used

- Continuous back-adjusted daily futures returns (see [[commodity-curve-rolls]]).
- 12-month rolling skewness; optional IE asymmetry measure.
- **Crypto adaptation:** the same sort can be run on a perp universe (skew of daily returns over 90-180 days), testing whether the lottery effect documented in crypto cross-sections survives funding costs — treat as an untested hypothesis.

## Example Trade

Illustrative month: trailing skew ranks natural gas and coffee as most positive (spiky upside), live cattle, gold and soybeans as most negative. Book: long cattle, gold, soybeans; short nat gas, coffee and the third-highest name, each 1/6 of risk capital. Hold one month, re-rank, roll contracts as needed.

## Performance Characteristics

- **Source claim, skewness (#0281, 1990-2022, pre-cost):** 9.51% annual return, 11.6% volatility, Sharpe 0.82, max drawdown −17.5% (Source: [[quantpedia-strategy-encyclopedia]]).
- **Source claim, asymmetry (#0664, 1991-2021, pre-cost):** 4.36% annual return, 7.5% volatility, Sharpe 0.58, max drawdown −47.6%.
- **Cost overlay:** monthly turnover of a 6-contract book is modest; roll and slippage on less-liquid softs/livestock are the main costs. Halve the Sharpe as a publication-decay prior ([[alpha-decay]]).
- Largely uncorrelated with [[commodity-carry-strategy]] and [[commodity-momentum]] by construction, but check realised overlap before combining.

## Capacity Limits

Liquid energy, metals and grains futures support hundreds of millions; livestock and softs constrain the short leg first.

## What Kills This Strategy

- **Short-leg squeeze** — the shorted contracts are by definition prone to upside spikes (e.g. natural gas); a single spike can dominate a year.
- **Regime shifts** in commodity supply chains that change skew persistence.
- **Estimation noise** — 12-month skew is unstable; ranks churn. See [[failure-modes]].

## Kill Criteria

- Rolling 36-month net Sharpe < 0.
- Drawdown > 25%.
- Skew-rank dispersion in the bottom decile of its history for 12 months (no signal to sort on).

## Advantages

- Low correlation to classic commodity carry/momentum factors.
- Monthly, low-turnover, market-neutral.
- Mechanism has a well-documented equity analogue.

## Disadvantages

- Short leg carries explicit right-tail risk.
- Requires futures infrastructure and roll handling.
- Mostly one research group's replication; limited independent confirmation in the harvested material.

## Sources

- (Source: [[quantpedia-strategy-encyclopedia]]) — Quantpedia #0281 (Dujava & Vojtko 2023; related Fernandez-Perez et al.) and #0664 (Ďurian & Padyšák 2020).

## Getting the Data (CryptoDataAPI)

CryptoDataAPI does not serve commodity futures; source continuous contracts elsewhere (see [[commodity-carry-strategy]] for data notes). For the **crypto adaptation**, pull daily bars per perp from `GET /api/v1/market-data/klines?symbol=SOLUSDT&interval=1d` and history from `GET /api/v1/backtesting/klines`; `GET /api/v1/sentiment/macro` supplies the gold level as a cross-asset reference. See [[cryptodataapi-market-data]] and [[cryptodataapi-backtesting]].

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/symbols"
```

### AI agent workflow

- **Crypto universe** — list tradable symbols with `GET /api/v1/backtesting/symbols` and rebuild point-in-time membership from `GET /api/v1/backtesting/daily-snapshots/{date}`
- **Signal** — rolling skew of daily returns from `GET /api/v1/backtesting/klines`; long lowest-skew, short highest-skew perps, monthly
- **Carry drag** — the short leg is typically memecoin-style high-skew names; check `GET /api/v1/backtesting/funding` since shorting them often *earns* funding, which changes the cost overlay vs commodities
- **Gate** — skip rebalances when `GET /api/v1/meme/regime` flags a meme mania, when short-leg squeezes cluster
- Run via [[cryptodataapi-mcp]]

## Related

- [[commodity-carry-strategy]] · [[commodity-momentum]] · [[commodity-value-strategy]] · [[max-anomaly]] · [[lottery-stock-anomaly]] · [[hedging-pressure]] · [[quantpedia]]

---
title: "Currency Value (PPP) Strategy"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [forex, macro, quantitative, position-trading, factor-investing, mean-reversion]
aliases: ["FX value factor", "PPP currency strategy", "Currency value factor", "Quantpedia #0009"]
strategy_type: fundamental
timeframe: position
markets: [forex]
complexity: intermediate
backtest_status: untested
edge_source: [risk-bearing, behavioral]
edge_mechanism: "Real exchange rates drift back toward purchasing-power-parity fair value over multi-year horizons; buying the most undervalued and selling the most overvalued currencies collects a premium from trend-following and flow-driven holders who push currencies away from fundamentals, plus compensation for holding currencies of countries in persistent macro stress."
data_required: [fx-spot-monthly, cpi-monthly, ppp-oecd, interest-rates]
min_capital_usd: 50000
capacity_usd: 1000000000
crowding_risk: low
expected_sharpe: 0.2  # prior only; source Sharpe 0.36 (1989-2009) with deteriorating out-of-sample alpha
expected_max_drawdown: 0.40
breakeven_cost_bps: 100
decay_evidence: "Quantpedia card flags deteriorating out-of-sample alpha after the 1989-2009 Deutsche Bank index sample."
kill_criteria: |
  - rolling 5-year net Sharpe < 0
  - drawdown > 40%
related: ["[[quantpedia]]", "[[quantpedia-strategy-encyclopedia]]", "[[value-anomaly]]", "[[currency-dynamics]]", "[[carry-trade]]", "[[currency-momentum]]", "[[dollar-carry-trade]]", "[[macro-relative-value]]", "[[dxy]]"]
---

# Currency Value (PPP) Strategy

A cross-sectional FX strategy that goes long the three G10-style currencies most undervalued versus purchasing-power parity and short the three most overvalued, rebalanced monthly or quarterly. It is the "value" leg of the classic FX carry/momentum/value trio, harvested from [[quantpedia|Quantpedia]] #0009 (Source: [[quantpedia-strategy-encyclopedia]]).

## Edge Source

**Risk-bearing + behavioral** ([[edge-taxonomy]]). Menkhoff, Sarno, Schmeling & Schrimpf show real-exchange-rate valuation measures predict FX excess returns, largely as compensation for persistent cross-country macro differences rather than pure mean reversion (Source: [[quantpedia-strategy-encyclopedia]]). See [[value-anomaly]] for the cross-asset value premium.

## Why This Edge Exists

Currencies overshoot fair value for years because flows (carry, momentum, reserve management, safe-haven demand) dominate fundamentals in the short run; only slow-moving PPP gravity pulls them back. The counterparty is the flow-driven holder of the overvalued currency. Part of the return is a risk premium: cheap currencies are often cheap because their economies are riskier.

## Null Hypothesis

If PPP deviations had no predictive power, the long-short would earn the interest differential between the legs (which may be positive or negative) and pay forward-point spreads and roll costs of ~5-20 bps per rebalance. Any residual after that is the value premium.

## Rules

- **Universe:** 10-20 liquid currencies vs USD.
- **Fair value:** latest OECD PPP rates, updated monthly for CPI inflation differentials and spot moves.
- **Signal:** percentage deviation of spot from PPP fair value.
- **Portfolio:** long the 3 most undervalued, short the 3 most overvalued, equal-weight; idle cash at overnight rates.
- **Rebalance:** quarterly (or monthly).
- **Instruments:** FX forwards, futures or CFDs.

## Implementation Pseudocode

```python
# Currency value (PPP) — illustrative only
for rebalance_date in quarterly_calendar:
    fair = oecd_ppp(universe) * cpi_ratio_since_ppp_date(universe)
    misval = spot(universe) / fair - 1          # >0 overvalued
    longs  = misval.nsmallest(3).index
    shorts = misval.nlargest(3).index
    set_forwards({c: 1/6 for c in longs} | {c: -1/6 for c in shorts})
```

## Indicators / Data Used

- OECD PPP conversion factors; CPI series; spot FX; short-term rates for forward pricing.
- Background: [[currency-dynamics]], [[dxy]].

## Example Trade

Illustrative quarter: PPP ranks JPY, NOK and SEK most undervalued, CHF, AUD and NZD most overvalued. Long JPY/NOK/SEK, short CHF/AUD/NZD forwards, 1/6 each. Held for the quarter unless ranks change. Gains accrue only if misvaluations narrow or carry on the longs exceeds that on the shorts.

## Performance Characteristics

- **Source claim (Deutsche Bank index, 1989-2009, pre-cost):** 7.82% annual return, 9.3% volatility, Sharpe 0.36, max drawdown −39.4%; out-of-sample alpha deteriorating (Source: [[quantpedia-strategy-encyclopedia]]).
- The card notes negative equity correlation in stress, i.e. it can hedge risk-on books — the opposite of [[carry-trade]].
- **Cost overlay:** low turnover; major-currency forwards are cheap (a few bps). Costs matter little; decay matters a lot.

## Capacity Limits

G10 FX is the deepest market in the world; capacity is effectively unbounded at wiki-relevant scales.

## What Kills This Strategy

- **Multi-year misvaluation persistence** — PPP convergence half-lives are 3-5 years; drawdowns last years.
- **Structural breaks** (e.g. terms-of-trade shifts) that change true fair value.
- **Publication decay** documented by the card itself ([[alpha-decay]]).

## Kill Criteria

- Rolling 5-year net Sharpe < 0.
- Drawdown > 40%.

## Advantages

- Low turnover and cost; very high capacity.
- Diversifies carry and momentum; can act as a crisis hedge.
- Transparent, public inputs.

## Disadvantages

- Weak standalone Sharpe; long drawdowns.
- Out-of-sample deterioration flagged by the source.
- Not directly tradable with crypto infrastructure — relevant to this wiki as macro context for USD and stablecoin demand.

## Crypto relevance

USD valuation against PPP is a slow input to the dollar cycle that drives global liquidity and crypto risk appetite (see [[global-liquidity-expansion-contraction]]). A deeply overvalued USD is one of several conditions that have historically preceded dollar weakness — a tailwind for BTC. Tokenised FX and non-USD stablecoins (e.g. EUR stablecoins) are a nascent on-chain route for expressing FX views.

## Sources

- (Source: [[quantpedia-strategy-encyclopedia]]) — Quantpedia #0009; Deutsche Bank (2009) currency value index; Menkhoff, Sarno, Schmeling & Schrimpf on currency value.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI is crypto-first and does not publish PPP or CPI series. `GET /api/v1/sentiment/macro` returns the current EUR/USD level, gold and yields — enough to monitor the dollar backdrop for crypto, not to run the strategy. Source PPP from the OECD. See [[cryptodataapi-sentiment]].

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/sentiment/macro"
```

### AI agent workflow

- **Macro backdrop** — read EUR/USD and yields from `GET /api/v1/sentiment/macro` monthly and log the USD PPP misvaluation alongside
- **Crypto transmission** — compare dollar-trend shifts with `GET /api/v1/sentiment/stablecoins` flow deltas to see whether a weakening USD coincides with stablecoin inflows
- **Regime gate** — use `GET /api/v1/regimes/current` to condition crypto beta on the dollar view rather than trading FX directly
- Run via [[cryptodataapi-mcp]]

## Related

- [[carry-trade]] · [[currency-momentum]] · [[dollar-carry-trade]] · [[value-anomaly]] · [[macro-relative-value]] · [[currency-dynamics]] · [[quantpedia]]

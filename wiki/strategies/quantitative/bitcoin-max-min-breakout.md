---
title: "Bitcoin MAX/MIN Breakout (10-Day High Trend, 10-Day Low Reversion)"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [crypto, bitcoin, quantitative, trend-following, mean-reversion, breakout, swing-trading]
aliases: ["BTC MAX strategy", "BTC MIN strategy", "Bitcoin 10-day high/low", "Quantpedia Bitcoin trend and reversion"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: beginner
backtest_status: untested
edge_source: [behavioral]
edge_mechanism: "MAX leg: late-arriving and under-reacting buyers keep chasing BTC after it prints a fresh N-day high (trend continuation / herding). MIN leg: forced and panic sellers overshoot at fresh N-day lows and prices bounce as that selling exhausts. The counterparties are, respectively, early profit-takers selling into strength and capitulating holders selling into weakness."
data_required: [ohlcv-daily]
min_capital_usd: 1000
capacity_usd: 50000000
crowding_risk: high
expected_sharpe: 0.6  # prior only; MAX leg survived out-of-sample 2022-2024 per source, MIN leg did not
expected_max_drawdown: 0.35
breakeven_cost_bps: 50
decay_evidence: "Quantpedia 2024-09-12 revisit (Beluská) of Padyšák & Vojtko (2022): MAX leg robust in the 2022-2024 out-of-sample bear/recovery, MIN leg underperformed significantly out-of-sample."
kill_criteria: |
  - MAX leg rolling 24-month net return below buy-and-hold BTC and below 0
  - MIN leg: retire if out-of-sample Sharpe < 0 over 18 months (already marginal per source)
  - drawdown > 35%
related: ["[[quantpedia]]", "[[quantpedia-strategy-encyclopedia]]", "[[donchian-channel-breakout]]", "[[turtle-trading]]", "[[time-series-momentum]]", "[[crypto-momentum]]", "[[max-anomaly]]", "[[bitcoin-overnight-seasonality]]"]
---

# Bitcoin MAX/MIN Breakout (10-Day High Trend, 10-Day Low Reversion)

Two simple daily Bitcoin rules from Quantpedia's own research: **MAX** buys BTC when it closes at its highest level of the last N days (trend-following), **MIN** buys when it closes at its lowest level of the last N days (mean-reversion). N = 10 worked best in-sample; the combined MIN+MAX book beat buy-and-hold with lower drawdowns in-sample, but only MAX held up out-of-sample (Source: [[quantpedia-strategy-encyclopedia]]).

## Edge Source

**Behavioral** ([[edge-taxonomy]]): herding/under-reaction feeds MAX; capitulation overshoot feeds MIN. The MAX rule is a special case of the [[donchian-channel-breakout]] used by the [[turtle-trading|Turtles]], applied to BTC with a short lookback.

## Why This Edge Exists

BTC's retail-heavy, leverage-heavy ownership amplifies both trend-chasing (fresh highs attract momentum buyers and short squeezes) and panic (fresh lows trigger liquidations that overshoot). Padyšák & Vojtko (2022) documented both effects on Gemini daily data from 2015; the 2024 revisit split the sample into in-sample (to 2022-02) and out-of-sample (2022-02 to 2024-08) (Source: [[quantpedia-strategy-encyclopedia]]). The out-of-sample result — MAX survives, MIN fails — is consistent with the view that crypto's [[time-series-momentum]] is more persistent than its short-term reversal.

## Null Hypothesis

With no edge, returns following an N-day high or low would equal the unconditional daily drift. A MAX or MIN book would then earn drift × time-in-market minus switching costs, underperforming buy-and-hold in a rising market. Since the source tested 5 lookbacks (10-50 days) and two directions, apply a multiple-testing haircut ([[data-snooping-and-p-hacking]]).

## Rules

The free-tier write-up gives the signal but not full exit specification; the following is a documented adaptation:

- **MAX entry:** daily close = max(close, last 10 days) → long BTC.
- **MIN entry:** daily close = min(close, last 10 days) → long BTC.
- **Exit (adaptation):** hold for a fixed horizon (e.g. until the next day the condition is not re-triggered, or a 10-day time stop), or exit MAX on a close below the 10-day low (Donchian-style).
- **Recommended live variant:** run MAX only; treat MIN as a research leg until it re-proves itself post-2022.
- **Sizing:** volatility-target the position (e.g. 20-30% annualised) rather than fixed notional.

## Implementation Pseudocode

```python
# Bitcoin MAX/MIN — illustrative only
N = 10
hi_n = close.rolling(N).max()
lo_n = close.rolling(N).min()

max_signal = close >= hi_n          # trend leg
min_signal = close <= lo_n          # reversion leg (research only)

position = 0
for t in days:
    if max_signal[t]:
        position = vol_target_size(t)
    elif position > 0 and close[t] <= lo_n[t]:
        position = 0                 # Donchian-style exit
```

## Indicators / Data Used

- Daily BTC closes; rolling N-day max/min (see [[donchian-channel-breakout]]).
- Realised volatility for sizing.

## Example Trade

Illustrative: BTC closes at $64,000, above the prior 10-day high of $63,500 → MAX long at the next open. It trends to $70,000 over three weeks; the 10-day low rises to $66,800 and the trade exits there on a pullback: +4.4% before costs (~10 bps on spot).

## Performance Characteristics

- **Source claims (pre-cost):** in-sample (2015-11 to 2022-02) both legs profitable with 10-day lookbacks, MAX with higher returns and lower drawdowns than MIN; combined MIN+MAX delivered high returns with lower drawdown than buy-and-hold. Out-of-sample (2022-02 to 2024-08): MAX resilient through the 2022 bear market; MIN underperformed significantly (Source: [[quantpedia-strategy-encyclopedia]]).
- The free write-up does not publish exact out-of-sample Sharpe/return figures; the frontmatter Sharpe is a prior.
- **Cost overlay:** low turnover (tens of trades per year) — fees are minor on spot; perp funding in bull markets (often 10-30% annualised on longs) is the bigger drag.

## Capacity Limits

BTC daily volume supports tens of millions of notional; the constraint is crowding — Donchian/breakout signals on BTC are among the most widely run systematic rules.

## What Kills This Strategy

- **Choppy ranges** — repeated false breakouts ([[failure-modes]]).
- **Crowding** at obvious breakout levels, producing stop-hunts ([[stop-hunting-and-liquidity-sweeps]]).
- **MIN leg in trending bear markets** — buying every fresh low in 2022 was the documented failure.

## Kill Criteria

- MAX: rolling 24-month net return below zero and below buy-and-hold.
- MIN: out-of-sample Sharpe < 0 over 18 months.
- Drawdown > 35%.

## Advantages

- Transparent, parameter-light, low turnover.
- Out-of-sample evidence exists (for MAX) from the source itself.
- Easily combined with a regime gate or funding filter ([[funding-filtered-momentum]]).

## Disadvantages

- Heavily crowded signal family.
- MIN leg's out-of-sample failure shows the combined in-sample result was partly regime luck.
- Exit rules not specified in the free write-up — adaptations add degrees of freedom.

## Sources

- (Source: [[quantpedia-strategy-encyclopedia]]) — Quantpedia blog "Revisiting Trend-following and Mean-reversion Strategies in Bitcoin" (2024-09-12); primary paper Padyšák & Vojtko (2022).

## Getting the Data (CryptoDataAPI)

Live: `GET /api/v1/market-data/btc-price-history?days=730` or `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d`. Historical: `GET /api/v1/backtesting/klines`. See [[cryptodataapi-market-data]] and [[cryptodataapi-backtesting]].

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000"
```

### AI agent workflow

- **Signal** — compute the 10-day rolling max/min from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=60` at each daily close
- **Regime gate** — take MAX entries only when `GET /api/v1/regimes/current` is not in a range/chop state; never run MIN when the regime is trending-bear
- **Carry check** — if expressing on perps, read `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT`; high positive funding erodes a long-breakout hold
- **Backtest** — replay from `GET /api/v1/backtesting/klines` and reproduce the source's in/out-of-sample split (2022-02 boundary) before extending
- Run via [[cryptodataapi-mcp]]

## Related

- [[donchian-channel-breakout]] · [[turtle-trading]] · [[time-series-momentum]] · [[crypto-momentum]] · [[short-term-reversal]] · [[bitcoin-overnight-seasonality]] · [[quantpedia]]

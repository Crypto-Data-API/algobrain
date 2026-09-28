---
title: "Bitcoin Overnight Seasonality (22:00-00:00 UTC)"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [crypto, bitcoin, quantitative, calendar-effects, day-trading, market-microstructure]
aliases: ["BTC 22-00 UTC effect", "Bitcoin intraday seasonality", "Bitcoin hour-of-day effect", "Quantpedia #0753"]
strategy_type: quantitative
timeframe: intraday
markets: [crypto]
complexity: beginner
backtest_status: untested
edge_source: [behavioral, structural]
edge_mechanism: "Between 22:00 and 00:00 UTC nearly every major equity venue is shut, so BTC is one of the few deep markets open for risk-on flow; the source hypothesises that this concentration of residual demand (late US retail, early Asia) produces a small positive drift in those two hours that sellers do not arbitrage because the per-trade edge is below most participants' cost threshold."
data_required: [ohlcv-1h]
min_capital_usd: 1000
capacity_usd: 20000000
crowding_risk: medium
expected_sharpe: 0.5  # prior only: source claims 1.58 pre-cost (2015-2021); halved for publication decay and ~730 round trips/year of fees
expected_max_drawdown: 0.35
breakeven_cost_bps: 8
decay_evidence: "Published 2022 (Padyšák & Vojtko); out-of-sample post-2022 behaviour not reported on the free card. The ETF era (2024+) shifted weekday/weekend flow — see crypto-weekday-weekend-etf-era."
kill_criteria: |
  - rolling 12-month net-of-cost return < 0
  - mean 22:00-00:00 UTC return over trailing 250 days not > 0 at t-stat 1.5
  - drawdown > 25%
related: ["[[quantpedia]]", "[[quantpedia-strategy-encyclopedia]]", "[[crypto-trading-sessions]]", "[[calendar-effects]]", "[[overnight-vs-intraday]]", "[[crypto-weekday-weekend-etf-era]]", "[[session-aware-mean-reversion]]", "[[funding-by-hour]]"]
---

# Bitcoin Overnight Seasonality (22:00-00:00 UTC)

A pure time-of-day rule: buy Bitcoin at 22:00 UTC and sell at 00:00 UTC, every day, otherwise flat. It is harvested from [[quantpedia|Quantpedia]] entry #0753, which summarises Padyšák & Vojtko (2022), "Seasonality, Trend-following, and Mean reversion in Bitcoin" (Source: [[quantpedia-strategy-encyclopedia]]).

## Edge Source

**Behavioral + structural** (see [[edge-taxonomy]]). Structural because the effect is tied to the global equity session clock — BTC trades 24/7 while traditional venues do not. Behavioral because the proposed driver is where discretionary retail flow lands when other markets are closed.

## Why This Edge Exists

The source's explanation: at 22:00-00:00 UTC the NYSE cash session has closed, European exchanges are shut, and Tokyo, Hong Kong, India and Australia have not yet reopened (or have closed), so BTC is one of the few liquid risk assets available. Capital that wants to express a view has fewer alternatives and bids into thin books, producing a mild upward drift (Source: [[quantpedia-strategy-encyclopedia]]). The counterparty is whoever sells into that window — market makers and hedgers who are not pricing a two-hour drift that is small relative to their spreads. See [[crypto-trading-sessions]] for the session map.

## Null Hypothesis

Under no edge, the mean BTC return in the 22:00-00:00 UTC window equals 2/24 of the mean daily return, and a strategy exposed to only those two hours earns roughly one-twelfth of buy-and-hold drift with one-twelfth of the time-in-market, minus ~730 round trips of fees per year. At 4-5 bps taker per side on a perp that is ~6-7% per year of cost drag — enough to erase a modest effect entirely. Any live result must beat this by a margin surviving a multiple-testing haircut (24 candidate hours were examined; see [[data-snooping-and-p-hacking]]).

## Rules

- **Instrument:** BTC spot or BTC-USDT perpetual on a deep venue.
- **Entry:** market or passive limit buy at 22:00 UTC.
- **Exit:** close at 00:00 UTC.
- **Sizing:** fixed notional equal to the sleeve allocation; no leverage beyond 1x in the reference rule. Volatility-scale if run alongside other sleeves.
- **Execution note:** use maker orders placed a few minutes before 22:00 to cut fees; a two-hour hold does not cross a Binance funding stamp (00:00 UTC is a stamp — exit just before it or accept one funding payment).

## Implementation Pseudocode

```python
# Bitcoin overnight seasonality — illustrative only
ENTRY_UTC, EXIT_UTC = 22, 0

def on_bar_close(ts_utc, position):
    if ts_utc.hour == ENTRY_UTC and position == 0:
        if not regime_filter_blocks():          # optional, see AI agent workflow
            buy_notional(SLEEVE_USD)
    elif ts_utc.hour == EXIT_UTC and position > 0:
        close_all()                              # before the 00:00 funding stamp if on perps
```

## Indicators / Data Used

- Hourly BTC OHLCV (entry/exit timestamps, hour-of-day return statistics)
- Optional: [[funding-by-hour]] and venue depth to judge whether the window's liquidity profile has changed

## Example Trade

Illustrative: BTC at $60,000 at 22:00 UTC; position $10,000 notional. By 00:00 UTC BTC is $60,120 (+0.2%). Gross P&L $20; fees at 2 × 4.5 bps = $9; net $11. A −0.2% night loses $29 net. The edge lives entirely in the small positive mean across hundreds of such nights.

## Performance Characteristics

- **Source claim (pre-cost, Gemini data, 2015-2021):** ~33% annual return, 20.9% volatility, Sharpe 1.58, max drawdown −34% (Source: [[quantpedia-strategy-encyclopedia]]).
- **Cost overlay:** ~730 fills/year. At 9 bps round trip (taker both sides) cost is ~6.6%/yr; at maker rates ~2-3%/yr. The source figure is gross.
- The 2015-2021 sample is mostly a strong bull period; the effect is partly BTC drift concentrated in the window. Post-publication and ETF-era behaviour are unverified — the weekday/weekend flow structure changed after spot ETFs launched in January 2024 (see [[crypto-weekday-weekend-etf-era]]).
- Expected Sharpe in frontmatter is a halved prior, not a result.

## Capacity Limits

BTC 2-hour volume at 22:00-00:00 UTC runs in the billions on major venues; a sleeve up to ~$20M notional can be worked with minimal impact if split across venues. Beyond that the strategy's own buying at a fixed time becomes the flow it is trying to harvest.

## What Kills This Strategy

- **Crowding / publication decay** — a fixed-clock rule is trivially copied ([[alpha-decay]]).
- **Session structure change** — ETF-era US-hours dominance, or Asian venues extending hours.
- **Cost drift** — a fee tier downgrade can erase a single-digit-bps edge.
- **Regime dependence** — the effect may just be bull-market drift; see [[failure-modes]].

## Kill Criteria

- Rolling 12-month net return < 0.
- Trailing 250-day mean window return t-stat < 1.5.
- Drawdown > 25% (see [[when-to-retire-a-strategy]]).

## Advantages

- Trivial to implement and audit; no parameters beyond the window.
- Only ~8% time-in-market — capital free for other sleeves most of the day.
- Directly testable on free hourly data.

## Disadvantages

- Edge per trade is a few bps; highly fee-sensitive.
- Chosen from 24 possible hours — severe multiple-testing risk.
- Long-only; drawdowns track BTC crashes that happen to fall in the window.

## Sources

- (Source: [[quantpedia-strategy-encyclopedia]]) — Quantpedia #0753; primary paper Padyšák & Vojtko (2022).

## Getting the Data (CryptoDataAPI)

Live data: `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h` — hourly bars for the entry/exit clock. Historical: `GET /api/v1/backtesting/klines` (1h bars back to 2017-08) for hour-of-day return studies. See [[cryptodataapi-market-data]] and [[cryptodataapi-backtesting]].

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=500"
```

### AI agent workflow

- **Re-test first** — pull 1h bars from `GET /api/v1/backtesting/klines` and compute the mean return per UTC hour for 2022-present, i.e. strictly post-publication, before trading anything
- **Regime gate** — skip entries when `GET /api/v1/volatility/regime` reports an extreme/high-vol state, where a two-hour window's variance swamps a few-bps drift
- **Funding stamp** — check `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT`; if running on perps and funding is strongly positive, exit at 23:59 to avoid paying the 00:00 stamp
- **Execution** — post maker bids before 22:00 UTC; the edge does not survive two taker fills at retail tiers
- Drive the whole loop via [[cryptodataapi-mcp]]

## Related

- [[crypto-trading-sessions]] · [[calendar-effects]] · [[overnight-vs-intraday]] · [[crypto-weekday-weekend-etf-era]] · [[session-aware-mean-reversion]] · [[bitcoin-max-min-breakout]] · [[quantpedia]]

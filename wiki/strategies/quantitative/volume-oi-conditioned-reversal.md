---
title: "Volume/OI-Conditioned Short-Term Reversal"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [crypto, futures, perpetual-futures, open-interest, volume, mean-reversion, quantitative, market-neutral]
aliases: ["Short-term reversal with futures", "Wang-Yu futures reversal", "Weekly perp reversal with OI filter", "Quantpedia #0071"]
strategy_type: quantitative
timeframe: swing
markets: [futures, crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, structural]
edge_mechanism: "Weekly price moves accompanied by a volume surge but falling open interest are driven by over-reacting, short-horizon traders churning and closing positions rather than by new informed positioning; those moves overshoot and reverse. A cross-sectional contrarian book that buys last week's losers and sells winners — only within that high-volume/low-OI bucket — takes the other side of the over-reaction."
data_required: [ohlcv-daily, open-interest, funding-rates]
min_capital_usd: 25000
capacity_usd: 20000000
crowding_risk: medium
expected_sharpe: 0.4  # prior only; source claims 0.82 pre-cost on US futures 1983-2000; crypto adaptation untested
expected_max_drawdown: 0.35
breakeven_cost_bps: 40
decay_evidence: "Wang & Yu (2004) sample ends 2000; no out-of-sample evidence harvested. Short-term reversal is known to decay and to be cost-sensitive (see short-term-reversal)."
kill_criteria: |
  - rolling 12-month net return < 0
  - drawdown > 35%
  - reversal spread (high-vol/low-OI bucket minus rest) not positive over trailing 52 weeks
related: ["[[quantpedia]]", "[[quantpedia-strategy-encyclopedia]]", "[[short-term-reversal]]", "[[overreaction-anomaly]]", "[[open-interest]]", "[[trading-volume]]", "[[oi-flush-reversion]]", "[[oi-price-exhaustion]]", "[[mean-reversion]]"]
gates:
  - id: top_perps_by_oi
    role: universe
    rule: "Universe: the top 30-50 USDT-margined perps by open interest"
    runnable: partial
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].open_interest_usd
    note: "Rank Hyperliquid perps by open_interest_usd and keep the top 30-50. Hyperliquid perps are USDC-margined, so the cross-section differs from the page's USDT-margined Binance list; Binance OI is served only one symbol at a time (/api/v1/derivatives/binance/open-interest?symbol=SOLUSDT), with no universe listing."
  - id: weekly_return
    role: entry
    rule: "7-day return per perp, measured on the weekly anchor (Wednesday to Wednesday in the original)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=9
    field: candles[].close
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&interval=1d&start={start}&end={end}
    replay_field: klines[].c
    note: "Latest closed daily close over the close 7 bars earlier, minus 1. Drop the forming bar named by forming_bar_timestamp. The weekday anchor is a degree of freedom the page warns about; daily bars close at 00:00 UTC."
  - id: volume_change
    role: entry
    rule: "Volume change: trailing 7-day volume over the prior 7 days, above the universe median"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=15
    field: candles[].volume
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&interval=1d&start={start}&end={end}
    replay_field: klines[].v
    note: "Sum volume x close over the last 7 closed daily bars and over the 7 before, take the ratio, then compare with the median ratio across the universe. Hyperliquid volume is base units and qv is null in the replay, so use v x c for notional."
  - id: oi_change_7d
    role: entry
    rule: "Open-interest change over 7 days, below the universe median"
    runnable: true
    endpoint: /api/v1/derivatives/hyperliquid/history?symbol={coin}&days=8
    field: history[].open_interest_usd
    replay: /api/v1/backtesting/hl-funding-bars?coin={coin}&interval=1d&start={start}&end={end}
    replay_field: data[].oi_close
    note: "Daily Hyperliquid OI; latest day over the day 7 earlier, minus 1, then compare with the universe median. Replay OI is populated from 2026-05-09 only (null before), and each replay call covers at most 93 days."
  - id: churn_bucket
    role: filter
    rule: "Trade only the bucket with volume change above the median AND OI change below the median"
    runnable: true
    input: derived
    inputs: [volume_change, oi_change_7d]
  - id: contrarian_weights
    role: sizing
    rule: "Within the bucket, weight each perp by -(r_i - mean r): long last week's below-average performers, short the above-average ones, scaled dollar-neutral"
    runnable: true
    input: derived
    inputs: [churn_bucket, weekly_return]
    note: "Normalise the weights by the sum of absolute deviations, as the pseudocode does."
  - id: vol_target_15
    role: sizing
    rule: "Scale the book to a 15% annual volatility target"
    runnable: partial
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=60
    field: candles[].close
    note: "Compute the weighted book's realized vol from daily closes and scale gross exposure to 15% annualised. The page names no lookback for the vol estimate, so the window is the desk's call."
  - id: skip_unlock_week
    role: filter
    rule: "Skip names in a major token-unlock week"
    runnable: partial
    endpoint: /api/v1/supply/unlocks?symbol={coin}&window_days=7
    field: items[].pct_of_float
    note: "An unlock dated inside the coming week flags the name. The page does not say how large counts as major; pct_of_float is the usual cut, and the threshold is the desk's call."
  - id: skip_delisting_week
    role: filter
    rule: "Skip names in a live delisting week"
    runnable: false
    note: "No exchange delisting calendar is served; announcements need the exchanges' own notices."
  - id: oi_divergence_cross_check
    role: filter
    rule: "Cross-check the bucket against price/OI divergence flags"
    runnable: partial
    endpoint: /api/v1/liquidity/oi-divergence
    field: rows[].divergence_4h
    note: "From the page's AI-agent workflow. It is a 4-hour divergence score, not the weekly bucket, and the page gives no rule for acting on it, so how it changes the book is the desk's call."
  - id: funding_carry_net
    role: sizing
    rule: "Net each leg's expected funding before sizing (shorting winners often collects positive funding; longing losers in negative funding also earns)"
    runnable: partial
    endpoint: /api/v1/hyperliquid/funding-rates?coin={coin}&limit=24
    field: history[].funding_rate
    replay: /api/v1/backtesting/hl-funding-bars?coin={coin}&interval=1d&start={start}&end={end}
    replay_field: data[].funding_sum
    note: "Hourly Hyperliquid funding. The page says to net carry but gives no rule for how it changes the weights."
  - id: conditioning_spread_kill
    role: filter
    rule: "Kill when the bucket's reversal spread versus the unconditioned universe is not positive over the trailing 52 weeks"
    runnable: partial
    input: derived
    inputs: [weekly_return, volume_change, oi_change_7d]
    note: "Needs 52 weeks of weekly OI changes. Live OI history is daily and the replay holds OI only from 2026-05-09, so the full 52-week test is not possible before May 2027."
  - id: drawdown_kill
    role: stop
    rule: "Kill on a rolling 12-month net return below 0 or a drawdown above 35%"
    runnable: true
    input: position
---

# Volume/OI-Conditioned Short-Term Reversal

A weekly cross-sectional contrarian strategy: among futures whose trading volume rose while open interest fell, buy last week's worst performers and short the best, weighting by distance from the group average. Harvested from [[quantpedia|Quantpedia]] #0071, summarising Wang & Yu (2004), "Trading Activity and Price Reversals in Futures Markets", and adapted here to crypto perpetuals, where volume and [[open-interest]] are published per contract (Source: [[quantpedia-strategy-encyclopedia]]).

## Edge Source

**Behavioral + structural** ([[edge-taxonomy]]). Behavioral: over-reaction by short-horizon traders ([[overreaction-anomaly]]). Structural: the OI filter distinguishes churn/closing flow from new positioning — a distinction that exists only in derivatives markets.

## Why This Edge Exists

Wang & Yu found contrarian profits in futures are positively related to lagged *volume* changes and negatively related to lagged *OI* changes: high volume signals over-confident trading that overshoots, while rising OI signals hedgers and new committed positions whose moves persist (Source: [[quantpedia-strategy-encyclopedia]]). In crypto perps the analogue is a week where volume spikes but OI drops — a liquidation or deleveraging week — where price moves reflect forced closing rather than new information. The counterparty is the forced or emotional closer.

## Null Hypothesis

With no edge, last week's return in the high-volume/low-OI bucket is uncorrelated with next week's return, and the long-short book earns zero minus weekly turnover costs (two legs × ~10-20 bps on mid-cap perps ≈ 10-20% a year of drag at full turnover) plus funding differentials. The OI/volume bucket choice (median splits) and weekday anchor are degrees of freedom — haircut accordingly.

## Rules

Original (US futures, 24 contracts):

- Weekly, Wednesday-to-Wednesday; nearest contract except in delivery month.
- Split contracts by change in volume (above/below median) and change in OI (top/bottom half).
- Within the **high-volume-change, low-OI-change** group: long contracts with below-group-average prior-week return, short those above, weights proportional to the return deviation from the group mean.

Crypto adaptation (untested):

- **Universe:** top 30-50 USDT-margined perps by OI.
- **Weekly signals:** Δvolume (7d vs prior 7d), ΔOI (7d), 7-day return.
- **Bucket:** Δvolume above median AND ΔOI below median.
- **Book:** within the bucket, weight_i ∝ −(r_i − mean(r)); scale to dollar-neutral and target volatility.
- **Filter:** skip names in a live delisting or major unlock week.

## Implementation Pseudocode

```python
# Volume/OI-conditioned weekly reversal — illustrative only
for week_end in weekly_calendar(anchor="Wed"):
    r   = weekly_return(universe)
    dv  = pct_change(volume_7d(universe))
    doi = pct_change(open_interest(universe), days=7)
    bucket = universe[(dv > dv.median()) & (doi < doi.median())]
    dev = r[bucket] - r[bucket].mean()
    w = -dev / dev.abs().sum()                  # contrarian, dollar-neutral
    rebalance(vol_target(w, annual_vol=0.15))
```

## Indicators / Data Used

- Weekly returns, [[trading-volume]], [[open-interest]] per contract.
- Funding rates to measure carry drag on each leg ([[funding-rate]]).

## Example Trade

Illustrative week: a deleveraging week drops OI across alts. In the high-volume/low-OI bucket, token A fell 18% (bucket mean −8%) and token B rose 6%. The book goes long A (deviation −10%) and short B (+14%), sized proportionally. If A retraces +6% and B gives back −3% the next week, the spread earns ~9% on the paired notional before ~30-40 bps of fees and funding.

## Performance Characteristics

- **Source claim (US futures, 1983-2000, pre-cost):** 29.6% annual return, 31.4% volatility, Sharpe 0.82, max drawdown −58.7% (Source: [[quantpedia-strategy-encyclopedia]]).
- The drawdown and volatility are large: this is a concentrated contrarian book.
- **Cost overlay:** weekly full turnover is expensive; in crypto add funding (shorting last week's winners often pays positive funding, which helps; longing losers during negative funding also earns). Net effect needs measurement.
- The crypto transplant is an untested hypothesis.

## Capacity Limits

Bounded by the liquidity of the mid-cap perps that populate the bucket; ~$20M gross is a reasonable ceiling across a top-50 universe before impact dominates weekly rebalances.

## What Kills This Strategy

- **Trending regimes** — losers keep losing in a sector rotation or alt bear market.
- **Event risk** — hacks, delistings and unlocks look like over-reaction but are information ([[failure-modes]]).
- **Costs** — weekly turnover on thin alts.

## Kill Criteria

- Rolling 12-month net return < 0.
- Drawdown > 35%.
- The conditioning bucket's reversal spread versus the unconditioned universe non-positive over 52 weeks (the OI filter no longer adds information).

## Advantages

- Uses data (volume and OI) that crypto perps publish more transparently than most futures markets.
- Market-neutral; diversifies trend sleeves.
- Clear, falsifiable conditioning test.

## Disadvantages

- High volatility and deep historical drawdowns.
- Weekly turnover is fee-heavy.
- Original evidence is 25+ years old and on a different asset class.

## Variant / External Source: QuantConnect

[[quantconnect|QuantConnect]]'s Strategy Library publishes an open-code LEAN port of the same Wang & Yu paper, "Short Term Reversal with Futures", on a small fixed list of futures contracts. It is a quick way to check this page's rules against a reference implementation. Its results are illustrative only: the universe is hand-picked and the backtest is pre-2020 (Source: [[quantconnect-strategy-library]]).

## Sources

- (Source: [[quantpedia-strategy-encyclopedia]]) — Quantpedia #0071; primary paper Wang & Yu (2004).

## Getting the Data (CryptoDataAPI)

Live: `GET /api/v1/derivatives/binance/open-interest?symbol=SOLUSDT` (OI + 30d trend), `GET /api/v1/derivatives/open-interest?coin=SOL` (cross-exchange), `GET /api/v1/market-data/klines?symbol=SOLUSDT&interval=1d` (price and volume). History: `GET /api/v1/derivatives/binance/history` (1-90 days of daily derivatives data), `GET /api/v1/backtesting/klines` and `GET /api/v1/backtesting/funding`. See [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]].

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/binance/open-interest?symbol=SOLUSDT"
```

### AI agent workflow

- **Bucket build** — each week pull `GET /api/v1/derivatives/binance/open-interest` per symbol and 7-day volume from `GET /api/v1/market-data/klines`; keep names with rising volume and falling OI
- **Cross-check** — `GET /api/v1/liquidity/oi-divergence` flags price/OI divergences that overlap with the low-OI bucket
- **Carry** — net each leg's expected funding from `GET /api/v1/derivatives/funding-rates` before sizing
- **Backtest limit** — OI history via the derivatives history endpoint is only 90 days deep; for longer tests reconstruct from `GET /api/v1/backtesting/daily-snapshots/{date}` if OI is present in the snapshot, else treat results as short-sample
- Run via [[cryptodataapi-mcp]]

## Related

- [[short-term-reversal]] · [[overreaction-anomaly]] · [[oi-flush-reversion]] · [[oi-price-exhaustion]] · [[mean-reversion]] · [[open-interest]] · [[quantpedia]]

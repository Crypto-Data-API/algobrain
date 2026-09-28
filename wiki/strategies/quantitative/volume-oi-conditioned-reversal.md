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

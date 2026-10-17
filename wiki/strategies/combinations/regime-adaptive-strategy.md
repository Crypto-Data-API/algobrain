---
title: "Regime-Adaptive Strategy"
type: strategy
created: 2026-04-06
updated: 2026-10-17
status: review
tags: [combinations, meta-strategy, regime-detection, adaptive, volatility, market-conditions, crypto]
strategy_type: hybrid
timeframe: varies by regime
markets: [crypto, futures]
complexity: advanced
backtest_status: untested
related: ["[[trend-following]]", "[[mean-reversion]]", "[[volatility]]", "[[dvol]]", "[[bollinger-bands]]", "[[cryptodataapi]]", "[[vol-targeted-trend-following]]", "[[funding-flush-reversal]]"]

# Edge characterization
edge_source: [analytical, structural]
edge_mechanism: "Regime persistence means that correctly detecting a trending vs ranging vs crisis regime and deploying the right sub-strategy generates above-average returns across each regime window; the counterparty is the static-allocation participant who runs a trending strategy during choppy regimes and a premium-selling strategy into a crash."

# Data and infrastructure requirements
data_required: [ohlcv-daily, volatility-regime, funding-rates, open-interest, fear-greed-index]
min_capital_usd: 20000
capacity_usd: 500000000
crowding_risk: low

# Performance expectations
expected_sharpe: 1.0
expected_max_drawdown: 0.20
breakeven_cost_bps: 25

# Kill criteria
kill_criteria: |
  - regime mis-classification rate > 40% for 3 consecutive months (validate against CryptoDataAPI /regimes/current)
  - rolling 12-month Sharpe < 0.4 after all costs and strategy switches
  - drawdown > 20% from equity peak while correctly classified in a "range" or "low-vol" regime
gates:
  - id: vol_low
    role: filter
    rule: "Low-vol range regime, vol leg: VIX below 15 (together with adx_low)"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].dvol
    note: "No VIX is served. The page's crypto stack translates VIX into a DVOL percentile but gives no DVOL cutoffs, so 15 has no crypto equivalent on the page. items[].history[].dvol holds about 180 daily points (from 2026-04-20) for a percentile; the history is Pro Plus."
  - id: adx_low
    role: filter
    rule: "Low-vol range regime, trend leg: ADX(14) below 20 on the market index"
    runnable: true
    endpoint: /api/v1/indicators/adx?coin=BTC&interval=1d
    field: items[].adx
    replay: /api/v1/backtesting/signum-rgg?date={date}
    replay_field: by_symbol.{coin}.adx
    note: "The Rules read ADX on the S&P 500; BTC's daily ADX is the crypto market stand-in. The SIGNUM archive's adx is the same daily ADX(14) that /indicators/adx serves for interval=1d."
  - id: vol_normal
    role: filter
    rule: "Normal trend regime, vol leg: VIX between 15 and 25 (together with adx_trend)"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].dvol
    note: "Same missing DVOL translation as vol_low."
  - id: adx_trend
    role: filter
    rule: "Normal trend regime, trend leg: ADX(14) above 25"
    runnable: true
    endpoint: /api/v1/indicators/adx?coin=BTC&interval=1d
    field: items[].adx
    replay: /api/v1/backtesting/signum-rgg?date={date}
    replay_field: by_symbol.{coin}.adx
    note: "ADX between 20 and 25 falls in neither regime; the page treats mixed signals as Transitional."
  - id: vol_crisis_level
    role: filter
    rule: "High-vol crisis: VIX above 25 (either this or vol_crisis_jump)"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].dvol
    note: "Same missing DVOL translation as vol_low."
  - id: vol_crisis_jump
    role: filter
    rule: "High-vol crisis: VIX up more than 30% in a week (either this or vol_crisis_level)"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].history[].dvol
    note: "A 30% weekly jump in DVOL is computable from the daily history, but the page never says the VIX rule carries over to DVOL unchanged."
  - id: rv_percentile
    role: filter
    rule: "Check 20-day realized volatility against its 1-year percentile rank"
    runnable: partial
    endpoint: /api/v1/hyperliquid/candles?coin=BTC&interval=1d&limit=400
    field: candles[].close
    note: "Computable from daily closes, but the page lists the check without a cutoff or a regime it decides."
  - id: crypto_regime_switch
    role: filter
    rule: "Crypto stack: deploy carry/short-vol in a high-funding bull, trend in a confirmed trend with rising OI, mean reversion in a capitulation or low-vol range, protection in a leverage-stressed cascade"
    runnable: partial
    endpoint: /api/v1/quant/market
    field: regime.label
    replay: /api/v1/quant/history?scope=market&start={start}
    replay_field: entries[].regime_label
    note: "The page names /regimes/current and /quant/market as the switch but maps none of their labels to its four crypto regimes, and gives no funding or OI-change cutoffs. range_low_vol, strong_trend_* and vol_spike are the obvious matches; the mapping is the desk's."
  - id: transitional_half_size
    role: sizing
    rule: "When signals conflict or no regime is clear, cut every strategy to half size and wait 3-5 trading days"
    runnable: partial
    input: derived
    inputs: [vol_low, adx_low, vol_normal, adx_trend, vol_crisis_level, vol_crisis_jump]
  - id: range_rsi_long
    role: entry
    rule: "Low-vol range book: buy RSI(14) oversold (below 30 in the example)"
    runnable: true
    endpoint: /api/v1/indicators/technical?symbol={symbol}
    field: items[].rsi.rsi_14_1d
    note: "The Rules say 'RSI oversold' without a number; the example uses 30 and 70."
  - id: range_rsi_short
    role: entry
    rule: "Low-vol range book: sell RSI(14) overbought (above 70 in the example)"
    runnable: true
    endpoint: /api/v1/indicators/technical?symbol={symbol}
    field: items[].rsi.rsi_14_1d
  - id: range_bollinger
    role: entry
    rule: "Low-vol range book: use the Bollinger Bands for entry and exit (sell the extremes)"
    runnable: partial
    endpoint: /api/v1/indicators/technical?symbol={symbol}
    field: items[].bollinger.upper
    note: "Daily bands; items[].bollinger.lower is the other side. The page does not say how a band touch combines with the RSI rule."
  - id: range_short_options
    role: entry
    rule: "Low-vol range book: sell iron condors or credit spreads (10-delta wings in the example)"
    runnable: false
    note: "No per-strike option chain, greeks or order routing is served. /api/v1/market-intelligence/options is aggregate BTC options OI, put/call ratio and max pain."
  - id: trend_above_50
    role: entry
    rule: "Trend book: long above the 50-day MA, short below (together with trend_above_200)"
    runnable: true
    endpoint: /api/v1/indicators/technical?symbol={symbol}
    field: items[].ma.above_50
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
    note: "The example buys 'above its 20-day MA' instead (items[].ma.above_20). Prose unchanged."
  - id: trend_above_200
    role: entry
    rule: "Trend book: long above the 200-day MA, short below (together with trend_above_50)"
    runnable: true
    endpoint: /api/v1/indicators/technical?symbol={symbol}
    field: items[].ma.above_200
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
  - id: trend_macd_confirm
    role: filter
    rule: "Trend book: use MACD for trend confirmation"
    runnable: partial
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=200
    field: candles[].close
    note: "Computable from closes, but the page gives no MACD settings or confirming condition."
  - id: trend_trailing_stop
    role: stop
    rule: "Trend book: let winners run with trailing stops"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
    note: "No trail distance is given."
  - id: crisis_half_size
    role: sizing
    rule: "Crisis book: cut all position sizes by 50%"
    runnable: partial
    input: derived
    inputs: [vol_crisis_level, vol_crisis_jump]
  - id: crisis_close_short_options
    role: exit
    rule: "Crisis book: close any short options positions"
    runnable: partial
    input: derived
    inputs: [vol_crisis_level, vol_crisis_jump]
  - id: crisis_buy_puts
    role: sizing
    rule: "Crisis book: buy protective puts (5% OTM in the example) and consider VIX calls or long volatility"
    runnable: false
    note: "No option chain or order routing is served, and VIX calls have no crypto listing named on the page."

---

# Regime-Adaptive Strategy

## Edge source

**Analytical** and **structural**. See [[edge-taxonomy]].

Market regimes are persistent — a trending regime lasts weeks to months, not days; volatility clusters; ranging markets persist until a catalyst breaks them. This persistence means correctly identifying the current regime lets you deploy the right strategy for most of its remaining duration. The structural component: most funds have static mandates (always trend-following, always market-neutral) and cannot switch. Regime-adaptive capital captures the premium paid by static strategies in unfavourable conditions.

**Crypto-specific regime stack:** CryptoDataAPI provides a 10-state regime taxonomy (via `/api/v1/regimes/current`) and HMM probability scores (`/api/v1/quant/market`). In crypto the relevant regimes are: (1) high-funding-carry bull (deploy short-vol and carry), (2) confirmed trend with rising OI (deploy trend-following), (3) capitulation/low-vol range (deploy mean-reversion), (4) leverage-stressed cascade (deploy protection, reduce exposure). The VIX-based framework in the equities section translates to DVOL percentile + funding rate + OI change rate in crypto.

## Null hypothesis

If regimes are not identifiable in real-time (only in hindsight), regime switching does not beat a static diversified allocation. The strategy would pay switching costs — wider spreads, funding flips, re-entry friction — without recouping them in improved timing. Evidence for the regime-persistence thesis: BTC entered the 2022 bear market on 2022-01-04 and stayed in it for 11+ months; the correct detection at any point in that window would have saved capital. The risk: regime transitions are faster in crypto than in equities.

## Overview

Every strategy has an environment where it thrives and an environment where it bleeds. [[trend-following]] prints money in directional markets and dies in chop. [[mean-reversion]] dominates in ranges and gets steamrolled by breakouts. [[options-selling]] earns steady income in low volatility and blows up in crashes. The regime-adaptive strategy accepts this reality and builds a meta-system that detects the current market regime and deploys the appropriate sub-strategy.

This is not about predicting the future. It is about accurately reading the present. Markets cycle through identifiable regimes — trending, ranging, low-volatility, high-volatility, risk-on, risk-off — and each regime has a strategy that fits. The edge is in the switching, not in any single strategy.

## The Synergy

The synergy comes from **negative correlation between strategy drawdowns.** When trend-following loses money (choppy markets), mean-reversion makes money. When mean-reversion loses money (breakout/trending markets), trend-following makes money. When both directional strategies struggle (high-volatility crash), defensive positioning preserves capital.

A static allocation across strategies provides some diversification, but regime-adaptive switching goes further: it **concentrates capital in the strategy currently favored by the environment.** Instead of always having dead weight from the wrong strategy, you put more money behind the approach the market is rewarding right now.

The key insight: market regimes are persistent. A trending market tends to keep trending. A ranging market tends to keep ranging. Volatility clusters — high vol begets high vol, low vol begets low vol. This persistence means that by the time you detect a regime, there is usually enough remaining duration to profit from deploying the correct strategy.

## Component Strategies

| Regime | Detection Signal | Deployed Strategy |
|--------|-----------------|-------------------|
| Low Volatility / Range | [[vix]] < 15, [[adx]] < 20 | [[options-selling]], [[mean-reversion]] (sell [[bollinger-bands]] extremes) |
| Normal Trend | [[vix]] 15-25, [[adx]] > 25 | [[trend-following]] ([[moving-averages]] crossover, [[breakout-trading]]) |
| High Volatility / Crisis | [[vix]] > 25, rapid VIX expansion | Reduce position size 50%, buy [[protective-puts]], hedge with [[vix-calls]] |
| Transitional | Mixed signals, regime unclear | Reduce to half size on all strategies, wait for clarity |

## Implementation

**Step 1 — Regime Classification.** Run the classification daily at market close.

*Simple approach (rules-based):*
- Check [[vix]] closing level and its 10-day moving average direction
- Check [[adx]] on the S&P 500 (14-period)
- Check 20-day realized volatility vs. its 1-year percentile rank
- If VIX < 15 AND ADX < 20 → Low-vol range regime
- If VIX 15-25 AND ADX > 25 → Normal trending regime
- If VIX > 25 OR VIX jumps more than 30% in a week → High-vol crisis regime

*Advanced approach:* Use a Hidden Markov Model (HMM) trained on returns, volatility, and correlation data to probabilistically classify the regime. The HMM naturally captures regime persistence and transition probabilities. Libraries like `hmmlearn` in Python make this accessible.

**Step 2 — Strategy Deployment.**

*Low-Vol Range:* Sell [[iron-condors]] or [[credit-spreads]] on indices. Trade [[mean-reversion]] setups — buy [[rsi]] oversold, sell [[rsi]] overbought. Use [[bollinger-bands]] for entry/exit. Position size normally.

*Normal Trend:* Deploy [[trend-following]] — go long above the 50-day and 200-day [[moving-averages]], short below them. Trade [[breakout-trading]] from consolidation. Use [[macd]] for trend confirmation. Let winners run with trailing stops.

*High-Vol Crisis:* Cut all position sizes by 50%. Close any short options positions (unlimited risk in crisis). Buy [[protective-puts]] on core holdings. Consider [[vix-calls]] or long volatility positions. If you have conviction, selectively add to highest-quality long positions at extreme oversold levels — but small size only.

**Step 3 — Transition Management.** Regimes do not switch cleanly. When signals conflict, do not force a classification. Instead, reduce overall exposure to half-size and wait 3-5 trading days for clarity. The cost of being cautious during transition is far less than the cost of deploying the wrong strategy.

**Step 4 — Monitoring and Recalibration.** Review regime classification weekly. Log the regime, the deployed strategy, and the result. Over time, tune your thresholds — your market may need VIX at 18 instead of 15 as the low-vol boundary, or ADX at 22 instead of 25 for trend confirmation.

## Example Setup

**Late 2024 scenario:**
1. VIX at 13, ADX on S&P at 18. Regime = Low-Vol Range.
2. Deploy: sell monthly [[iron-condors]] on SPX, 10-delta wings. Trade [[mean-reversion]] on individual stocks — buy RSI < 30, sell RSI > 70.
3. Early 2025: VIX spikes to 28 after a geopolitical shock. Regime flips to High-Vol Crisis.
4. Immediately: close all short options, cut stock positions by 50%, buy SPY puts 5% OTM.
5. Two weeks later: VIX settles to 20, ADX rises to 30. Regime transitions to Normal Trend.
6. Deploy: trend-following. Buy SPY above its 20-day MA, add to winners, trail stops.

## When It Excels

- **Volatile macro environments** where conditions shift between trending, ranging, and crisis multiple times per year (2020-2022 was a textbook example)
- Markets with **identifiable regime persistence** — where trends last weeks-to-months, not hours
- When the trader has **access to multiple strategy implementations** (can actually execute trend-following, mean-reversion, and options strategies)
- **Systematic/quantitative traders** who can automate regime detection and strategy switching without emotional interference

## When It Fails

- When **regime transitions are too fast** — by the time you detect the shift, the new regime is already ending. This happens in extremely choppy markets with no sustained direction.
- **Over-optimization of regime boundaries** — if you tune VIX thresholds on past data, they may not hold in the future. Regimes are fuzzy, not precise.
- **Execution complexity** — managing multiple strategy books simultaneously requires infrastructure, discipline, and capital. Most retail traders struggle to run even one strategy well.
- In markets where **regimes are not well-defined** (some individual stocks, small-cap crypto). Regime detection works best on broad indices and liquid markets.

## Real-World Usage

**Renaissance Technologies** famously adapts strategies to market conditions using statistical models far more sophisticated than simple VIX thresholds, but the core concept is the same — the models detect which patterns are currently working and allocate capital accordingly.

**AQR Capital Management** has published extensive research on regime-aware investing, particularly around combining [[momentum-investing]] and value-investing factors with volatility-scaling (reducing exposure when volatility rises, increasing when it falls).

**Managed futures CTAs** (commodity trading advisors) are natural regime-adaptive strategies. Most CTAs run trend-following as their core, but the better ones incorporate regime detection to adjust speed parameters, position sizing, and market selection based on current conditions.

**Bridgewater Associates** uses a form of regime thinking in their All-Weather portfolio — constructing a portfolio that is designed to perform acceptably across all economic regimes (growth/inflation rising or falling) rather than switching between strategies.

**See also:** [[trend-following]], [[mean-reversion]], [[volatility]], [[dvol]], [[hidden-markov-model]], [[position-sizing]], [[risk-management]]

## Capacity limits

Regime-adaptive strategies scale well because they are meta-frameworks applied to liquid instruments — BTC/ETH perps have $5B+ OI and can absorb $500M+ in directional strategies. The limit is operational: regime detection lag (12–24h for daily signals) means large books need to pre-position before the switch is confirmed, introducing lookahead risk.

## What kills this strategy

1. **Regime transitions faster than detection** — in a sudden cascade, the model may still classify "low-vol range" while the market is already in a crash.
2. **Over-fitted regime thresholds** — regime boundary calibration on historical data may not hold in future market structures.
3. **Execution friction** — switching between strategies (close short-vol, open trend-following) incurs spreads and funding; too-frequent switching destroys the edge.
4. **Multiple concurrent conflicting signals** — DVOL in the 40th pct (low-vol) but funding at +0.08%/8h (crowded-bull) and OI declining simultaneously — no clean regime classification.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- Regime mis-classification rate > 40% for 3 consecutive months
- Rolling 12-month Sharpe < 0.4 after all costs
- Drawdown > 20% while correctly in a "range" or "low-vol" regime

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/regimes/current` — current long-horizon market regime (10-state taxonomy)
- `GET /api/v1/quant/market` — HMM regime probabilities, 4h/24h horizons (15-min refresh)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/liquidity/regime/score` — liquidity fragility composite (0-100)

**Historical data:**
- `GET /api/v1/quant/timeline` — daily market regime labels, 2019-now
- `GET /api/v1/quant/regimes/history` — full 6-regime Parquet download (2020-yesterday)
- `GET /api/v1/quant/history` — point-in-time probability records for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/regimes/current"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes) · [long-term regimes](https://cryptodataapi.com/regimes) · [strategy baskets](https://cryptodataapi.com/trading-strategy-baskets)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this meta-strategy end-to-end:

- **Signal** — `GET /api/v1/regimes/current` (10-state cycle) + `GET /api/v1/quant/market` (6-state HMM, 15-min refresh) drive the strategy-selection switch
- **Filter** — `GET /api/v1/volatility/regime/score` and `GET /api/v1/liquidity/regime/score` veto deployments the headline regime would otherwise allow (e.g. a trend book into fragile liquidity)
- **Strategy mapping** — `GET /api/v1/trading-strategy-baskets` returns 50 pre-mapped regime-to-strategy baskets the agent can adopt directly or diff against this wiki's [[regime-strategy-playbook]]
- **Backtest** — `GET /api/v1/quant/regimes/history` (hourly HMM probabilities since 2020, Parquet, Pro Plus) and `GET /api/v1/quant/timeline` (daily labels 2019-now) are the switching-logic archive; pair with `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) so the backtest sees regimes as they were published, not as re-labelled
- **Tips** — poll the cached `GET /api/v1/daily` bundle hourly for regime check-ins; reserve `POST /api/v1/quant/refresh` for major-event moments rather than routine cycles
- **Prompt library** — the "Market Regime Detection" prompt (Pro tier, [prompt library](https://cryptodataapi.com/prompts)) supplies the regime read this adaptive switch consumes

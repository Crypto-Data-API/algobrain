---
title: "Trend Following CTA"
type: strategy
created: 2026-04-06
updated: 2026-10-17
status: review
tags: [trend-following, CTA, managed-futures, systematic, time-series-momentum, breakout, commodities]
aliases: ["Managed Futures", "CTA", "CTA Strategy", "CTA Strategies", "Commodity Trading Advisor", "Systematic Trend Following", "Time-Series Momentum"]
strategy_type: quantitative
timeframe: position
markets: [futures, commodities, forex, crypto]
complexity: advanced
backtest_status: untested
related: ["[[factor-investing]]", "[[moving-average-crossover]]", "[[turtle-trading]]", "[[momentum]]", "[[breakout-trading]]", "[[commodity-momentum]]", "[[commodity-carry-strategy]]", "[[cot-report-analysis]]", "[[commodities]]", "[[crisis-alpha]]", "[[convexity]]", "[[dragon-portfolio]]", "[[trend-plus-tail-hedge]]"]

# Edge characterization
edge_source: [behavioral, structural]
edge_mechanism: "Trend followers profit from the systematic under-reaction and delayed adjustment of price-insensitive participants (fundamental investors, passive rebalancers, hedgers) who are slow to exit losing positions; the crowded side of a persistent trend keeps paying as late arrivals chase and early holders average down."

# Data and infrastructure requirements
data_required: [ohlcv-daily, funding-rates, open-interest, volatility-regime]
min_capital_usd: 100000
capacity_usd: 2000000000
crowding_risk: high

# Performance expectations (crypto-adapted)
expected_sharpe: 0.6
expected_max_drawdown: 0.25
breakeven_cost_bps: 15

# Kill criteria
kill_criteria: |
  - rolling 24-month Sharpe < 0.2 after costs
  - drawdown > 30% from equity peak
  - signal frequency / number of regime transitions doubles vs historical norm (over-whipsawing regime)
gates:
  - id: futures_universe
    role: universe
    rule: "Trade 50-100 liquid futures: agricultural, metals and energy commodities, currencies, government bonds and equity indices (either this or crypto_perp_universe)"
    runnable: false
    note: "We serve no CME/ICE futures; the page's own data section says those come from futures data vendors. The signal gates below run on the crypto application instead."
  - id: crypto_perp_universe
    role: universe
    rule: "Crypto application: BTC/ETH and alt perps (either this or futures_universe)"
    runnable: partial
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].open_interest_usd
    note: "BTC and ETH are named. The page has no rule for which alt perps join; it only says alt perp markets hold $20M-$200M before impact dominates and the crypto book should stop near $100M. Ranking assets[] by open_interest_usd is one screen; the cut-off is the desk's."
  - id: ma_cross_long
    role: entry
    rule: "Long while the 50-day SMA is above the 200-day SMA (one of three signals; see signal_flip_entry)"
    runnable: true
    endpoint: /api/v1/indicators/technical?symbol={symbol}
    field: items[].ma.sma_50
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
    note: "Compare with items[].ma.sma_200 on the same row: daily SMAs on the Hyperliquid perp series (the default source). A symbol listed in not_covered needs the SMAs computed from 200+ closed daily closes on /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=250. Replay: start at least 200 days before the test window."
  - id: ma_cross_short
    role: entry
    rule: "Short while the 50-day SMA is below the 200-day SMA (one of three signals; see signal_flip_entry)"
    runnable: true
    endpoint: /api/v1/indicators/technical?symbol={symbol}
    field: items[].ma.sma_50
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
    note: "Same comparison as ma_cross_long, with items[].ma.sma_200."
  - id: channel_breakout_long
    role: entry
    rule: "Long when price breaks above the highest high of the past 100 days (one of three signals; see signal_flip_entry)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=110
    field: candles[].high
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].high
    note: "N = 100 is the page's example ('e.g., 100 days') and the window its example trade uses; the Turtle 20/55-day channels are the other common choice. The page does not say whether a close or a trade through the level counts; the channel excludes the forming bar named by forming_bar_timestamp."
  - id: channel_breakout_short
    role: entry
    rule: "Short when price breaks below the lowest low of the past 100 days (one of three signals; see signal_flip_entry)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=110
    field: candles[].low
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].low
  - id: tsmom_long
    role: entry
    rule: "Long when the 12-month return is positive (one of three signals; see signal_flip_entry)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=400
    field: candles[].close
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
    note: "Last closed daily close against the close 365 bars earlier. A coin listed on Hyperliquid less than a year ago has no 12-month return yet."
  - id: tsmom_short
    role: entry
    rule: "Short when the 12-month return is negative (one of three signals; see signal_flip_entry)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=400
    field: candles[].close
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
  - id: multi_lookback_blend
    role: filter
    rule: "Confirm with several lookbacks (20, 60 and 200 days) and blend their signals to smooth entries"
    runnable: partial
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=250
    field: candles[].close
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
    note: "The closes give all three windows. The page says neither which signal each window runs (MA, channel or return sign) nor how the blend is weighted or thresholded; the desk sets both."
  - id: signal_flip_entry
    role: entry
    rule: "Enter when the chosen signal flips from neutral or opposite to the new direction, with a limit order at the next session's open"
    runnable: true
    input: derived
    inputs: [ma_cross_long, ma_cross_short, channel_breakout_long, channel_breakout_short, tsmom_long, tsmom_short]
    note: "Crypto has no session; the next daily bar's open at 00:00 UTC is our reading. Which signal runs, or which blend (multi_lookback_blend), is the desk's choice."
  - id: signal_reversal_exit
    role: exit
    rule: "Exit when the trend signal flips to the opposite direction (for the MA signal, the 50-day SMA crosses back through the 200-day)"
    runnable: true
    input: derived
    inputs: [ma_cross_long, ma_cross_short, channel_breakout_long, channel_breakout_short, tsmom_long, tsmom_short]
  - id: atr_trailing_stop
    role: stop
    rule: "Trail the stop 2-3x ATR from the best price to lock in profit before a full signal reversal"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=100&atr=14
    field: candles[].atr
    note: "The page never gives the ATR period; atr=14 is Wilder's default. The example's first stop is 2.4x ATR ($78 on a $72 short with ATR $2.50). Use the last closed bar's atr."
  - id: vol_doubling_derisk
    role: exit
    rule: "If realized volatility doubles, reduce position size or exit"
    runnable: partial
    endpoint: /api/v1/volatility/regime/{symbol}
    field: vol.rv_cc_30
    note: "history[].rv_cc_30 on the same response holds 60 daily values to compare against. The page sets no vol window, no baseline for 'doubles' and no size cut; whether to trim or exit is the desk's call."
  - id: risk_per_position
    role: sizing
    rule: "Size = target risk / (ATR x point value), targeting 1% risk per position"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=100&atr=14
    field: candles[].atr
    note: "On a linear perp the point value is 1 unit of the coin. The 1% is the page's example ('if targeting 1%'), and it names no ATR period; atr=14 is our reading."
  - id: portfolio_vol_target
    role: sizing
    rule: "Scale the whole book to 10-15% annualized volatility; scale every position down proportionally when the estimate is above target"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=250
    field: candles[].close
    note: "Book volatility comes from the positions and a return covariance of the daily closes. The page gives no estimation window, so that is the desk's."
  - id: correlation_cluster_cut
    role: sizing
    rule: "Reduce exposure when many markets trend in the same direction"
    runnable: partial
    input: derived
    inputs: [ma_cross_long, ma_cross_short, channel_breakout_long, channel_breakout_short, tsmom_long, tsmom_short]
    note: "Count the open signals pointing the same way. The page sets no count or share that triggers the cut, and no size for the cut."
  - id: choppy_regime_delever
    role: sizing
    rule: "De-lever while choppy_high_vol or range_low_vol dominates the HMM market regime"
    runnable: partial
    endpoint: /api/v1/quant/market
    field: regime.label
    replay: /api/v1/quant/history?scope=market&start={start}
    replay_field: entries[].regime_label
    note: "From the page's agent workflow, not its Rules. It gives neither a probability for 'dominate' nor how far to de-lever."
---

# Trend Following CTA

## Edge source

**Behavioral** (primary) and **structural** (secondary). See [[edge-taxonomy]].

The core behavioral source is the systematic under-reaction of price-insensitive participants — fundamental investors who average down, passive hedgers who must roll at scheduled dates, leveraged longs who exit only after forced margin calls. Their slow, predictable behaviour creates momentum that trend signals exploit. The structural component is the mandate-and-regulation architecture: pension rebalancing, futures-roll necessity, and index reconstitution force predictable flows that trend systems can front-run.

**Crypto application:** In crypto perp markets, the same mechanism operates via the liquidation cascade — leveraged positions cleared by exchange auto-liquidators are the crypto equivalent of the margin-call forced exit. BTC/ETH trend following applied to perps captures this plus funding-rate regime signals. See [[vol-targeted-trend-following]] for the crypto-native buildable implementation.

## Why this edge exists

Trend followers are paid for tolerating drawdowns that fundamental investors cannot stomach. The counterparty is the manager or investor forced to de-risk (sell) after a loss, or to double-down on a contrarian view that the trend will reverse. In commodity and forex markets, hedgers pay a risk premium to transfer price risk — trend followers are the natural risk-absorbers. In crypto, over-leveraged retail longs and shorts are the structural counterparty.

## Null hypothesis

Under random-walk prices, trend signals generate no edge above transaction costs. Sharpe would be ≈ 0 net of fees. If the time-series momentum premium has fully decayed (as the crowding literature argues for some equity markets), a naive CTA system should produce Sharpe < 0.3 after costs — barely above noise.

## Rules

### Entry is a systematic strategy that trades the direction of persistent price trends across a broad universe of **50-100+ futures markets** spanning commodities, currencies, government bonds, and equity indices. The strategy uses quantitative signals -- typically [[moving-average]] crossovers, channel breakouts, or time-series momentum -- to identify and ride trends until they reverse. It is the dominant strategy in the **managed futures** industry, employed by firms like **Man AHL**, **Winton Group**, **AQR**, **Graham Capital**, and **Millburn Ridgefield**.

The core principle is **time-series momentum**: assets that have been rising tend to continue rising, and assets that have been falling tend to continue falling, over horizons of 1-12 months. This persistence has been documented in academic literature across all major asset classes and over 100+ years of data. The CTA approach distinguishes itself from equity-only [[momentum]] by trading **both long and short** across **dozens of uncorrelated markets**, providing genuine diversification and the ability to profit in any market environment, including equity bear markets.

## Rules

### Entry
1. **Universe:** Trade 50-100 liquid futures contracts: agricultural [[commodities]] ([[corn]], [[wheat]], [[soybeans]]), metals ([[gold]], [[silver]], [[copper]]), energy ([[crude-oil|crude oil]], [[natural-gas|natural gas]]), currencies (EUR, JPY, GBP, AUD), bonds (U.S. Treasuries, German Bunds, JGBs), and equity indices (S&P 500, Euro Stoxx 50, Nikkei).
2. **Signal generation** (choose one or blend):
   - **Moving Average Crossover:** Go long when a short MA (e.g., 50-day) is above a long MA (e.g., 200-day). Go short when below. See [[moving-average-crossover]].
   - **Channel Breakout:** Go long when price breaks above the highest high of the past N days (e.g., 100 days). Short when price breaks below the lowest low. See [[turtle-trading]].
   - **Time-Series Momentum:** Go long if the 12-month return is positive. Go short if negative. Simplest and most robust signal.
3. **Confirmation:** Use multiple lookback windows (short: 20-day, medium: 60-day, long: 200-day) and blend their signals to smooth out entries and reduce whipsaws.
4. **Enter when the signal flips** from neutral/opposite to the new trend direction. Use limit orders at next session's open.

### Exit
1. **Signal reversal:** Exit when the trend signal flips to the opposite direction. For MA crossover, this means the short MA crosses back through the long MA.
2. **Trailing stop:** Use a 2-3x [[atr]] trailing stop to lock in profits during extended trends and exit before a full signal reversal.
3. **Volatility-based exit:** If realized volatility doubles (e.g., market enters crisis mode), reduce position size or exit to avoid outsized losses.

### Position Sizing
This is critical and often the most important component of a CTA system:
1. **Volatility targeting:** Size each position so that it contributes equal risk. Position size = Target Risk / (ATR x Point Value). If targeting 1% risk per position, a more volatile market gets fewer contracts.
2. **Portfolio volatility target:** Scale the total portfolio to target 10-15% annualized volatility. If all positions combined would produce 20% vol, scale everything down proportionally.
3. **Maximum correlation adjustment:** Reduce exposure when many markets are trending in the same direction (correlation clustering), as the portfolio becomes less diversified.

## Indicators Used
- [[simple-moving-average]] and [[exponential-moving-average]] (50, 100, 200-day)
- Channel breakout (Donchian Channel, highest high / lowest low over N days)
- Time-series momentum (12-month return sign)
- [[atr]] for position sizing and stop-loss placement
- Realized [[volatility]] for portfolio risk targeting
- Cross-market correlation for diversification monitoring

## Example Trade
**Market:** Crude Oil (CL) futures, daily chart
1. Crude oil has been falling for 3 months. The 50-day SMA crosses below the 200-day SMA. The 12-month return is -25%. The 100-day channel low is broken. All three signal types agree: short.
2. Sell 5 contracts at $72.00 (sized for 1% portfolio risk based on ATR of $2.50 and $1,000/point value). Trailing stop at $78.00 (2.4x ATR above entry).
3. Crude continues its downtrend over the next 4 months, reaching $54.00. The trailing stop has moved down to $60.00, locking in significant profit.
4. After 5 months, crude bounces sharply. The 50-day MA crosses above the 200-day. Exit short at $61.00 (trailing stop triggered).
5. **Result:** +$11.00/contract x 5 contracts x $1,000 = $55,000 profit. Simultaneously, the system was long gold and short EUR/USD during this period, adding diversified returns.

## Performance Characteristics
- **Win Rate:** 35-45%. Trend following has a low win rate but profits from fat-tailed, extended trends that produce outsized gains.
- **Profit Factor:** 1.3-2.0. The strategy relies on a few big winners each year to offset many small losses.
- **Best Market Conditions:** Strong, persistent trends in any direction across any market. Crisis periods (2008, 2022) often produce excellent CTA returns because bonds, currencies, and commodities trend violently.
- **Worst Market Conditions:** Choppy, range-bound, mean-reverting markets (2011-2013, 2015-2016). Extended low-volatility environments with no sustained trends.
- **Annual Returns:** 8-15% annualized at 10-12% volatility. Sharpe ratio: 0.5-0.8 over full cycles.
- **Crisis Alpha:** The strategy's greatest value is its negative correlation to equities during crashes. In 2008, trend-following CTAs returned +15-25% while equities fell 40%+.
- **Drawdowns:** Expect 15-25% peak-to-trough drawdowns lasting 1-3 years during trendless environments.

## Capacity limits

Traditional CTA programs are among the most scalable strategies in existence — Man AHL and Winton have run $10B+ with measurable but modest impact. Capacity is limited by liquidity of the futures markets traded, not by signal crowding (the signal is public, but most capital cannot hold through the drawdowns).

**Crypto-specific note:** A crypto perp trend system has meaningfully lower capacity: BTC/ETH perp markets are large ($5B+ OI each) but other altcoin perp markets have low capacity ($20M–$200M notional before impact dominates). A crypto-only trend system should limit deployment to ~$100M before scaling concerns become acute.

## What kills this strategy

1. **Sustained choppy, range-bound regime** — 2011–2013 and 2015–2016 saw Managed Futures SMA-based CTAs draw down 20-30% in assets and fire many whipsaws.
2. **Crowding and simultaneous exit** — when hundreds of CTAs hold the same positions, a regime-break causes all of them to reverse at once, amplifying the trend reversal and widening slippage.
3. **Rising transaction costs** — slippage, borrowing costs, and bid-ask spreads eat into the thin per-trade edge.
4. **Beta convergence** — in a liquidity event, trend positions in "uncorrelated" markets suddenly correlate (all trend followers are long the same things and short the same things).
5. **Crypto-specific:** Extreme funding costs on the losing side of a perp position, exchange auto-liquidation at a loss before the signal can exit cleanly, and weekend gap risk.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- Rolling 24-month Sharpe < 0.2 after all costs
- Drawdown > 30% from equity peak
- Signal whipsaw rate doubles vs historical norm over 6 months

## Advantages
- Genuine portfolio diversifier: low to negative correlation with stocks and bonds, especially during crises
- Trades both long and short across all major asset classes -- profits in any macro environment
- Over 100 years of backtested evidence and 40+ years of live track records from top CTAs
- Fully systematic and rules-based, removing emotional decision-making
- Benefits from [[volatility]] -- crisis periods often produce the best returns
- Scalable: manages billions of dollars without significantly impacting markets due to the liquidity of futures

## Disadvantages
- **Extended drawdowns in trendless markets** can last 2-3 years, testing investor patience severely
- Low win rate (35-45%) is psychologically difficult even when long-term results are positive
- **Capacity constraints:** As more capital enters trend following, the strategies can become crowded, and trend reversals become sharper as everyone exits simultaneously
- Requires sophisticated infrastructure: futures accounts, margin management, real-time data, and risk systems
- Transaction costs from frequent trading across dozens of markets reduce returns
- The "crisis alpha" benefit is episodic and unpredictable -- investors must hold through years of mediocre returns to capture the rare but lucrative crisis profits

## Commodity Futures: The Core CTA Asset Class

[[commodities|Commodity futures]] are the **core asset class** for most CTA programs and typically represent the largest allocation in diversified trend-following portfolios. This is for several reasons:

- **Trend persistence**: Commodities tend to exhibit stronger and more sustained trends than equities, driven by physical [[supply-demand-balance|supply/demand]] dynamics, [[commodity-super-cycle|super cycles]], and [[capex-cycle|capex cycles]] that unfold over years
- **Diversification**: Commodity markets (energy, metals, agriculture) have low correlation to each other and to financial assets, providing genuine portfolio diversification
- **Two-sided opportunity**: Commodity prices can decline as readily as they rise (unlike equities which have a long-term upward bias), making the short side equally productive for trend followers
- **Historical performance**: The original CTA programs (including [[turtle-trading|Turtle Trading]]) were primarily commodity-focused. Academic research (Moskowitz, Ooi, Pedersen 2012) shows time-series momentum is strongest in commodity and currency markets.
- **Related strategies**: CTA programs often combine trend signals with [[commodity-momentum|cross-sectional momentum]] and [[commodity-carry-strategy|carry]] signals to enhance returns. [[cot-report-analysis|COT positioning data]] can provide additional context for timing entries and exits.

A typical CTA program allocates 40-60% of its risk budget to commodity futures, with the remainder split between currencies, fixed income, and equity index futures. (Source: [[2026-04-14-commodities-research-framework]])

## Getting the Data (CryptoDataAPI)

For the crypto application (BTC/ETH/alt perp trend systems), CryptoDataAPI serves every input the signal stack needs; traditional futures data (CME/ICE contracts) comes from futures data vendors.

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=365` — daily OHLCV for MA / breakout / time-series-momentum signals
- `GET /api/v1/market-data/btc-price-history?days=730` — BTC with the 200D MA precomputed (the classic trend filter)
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1d&limit=365` — perp-side candles for the traded instrument
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the carry cost of holding the losing side of a perp trend position
- `GET /api/v1/volatility/regime` — per-asset vol states for the volatility-targeting layer

**Historical data:**
- `GET /api/v1/backtesting/klines` — Binance spot 1h/4h/1d back to 2017-08 (BTCUSDT), spanning several full crypto cycles
- `GET /api/v1/backtesting/funding` — Hyperliquid hourly funding since 2023-05 for cost-corrected perp replays
- `GET /api/v1/quant/regimes/history` — hourly 6-state HMM probabilities since 2020 (Parquet, Pro Plus) for regime-conditional performance analysis

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=365"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — daily `GET /api/v1/market-data/klines` per symbol, or bulk `GET /api/v1/daily/prices` (~2,500 pairs in one call) for the whole-universe momentum scan
- **Sizing** — ATR/vol targeting from the same klines, cross-checked against `GET /api/v1/quant/coins/risk?horizon=24h` (per-coin vol-target multipliers across 180+ coins)
- **Regime gate** — `GET /api/v1/quant/market` — the strategy's killer is the choppy regime; de-lever when `choppy_high_vol`/`range_low_vol` probabilities dominate, and track the whipsaw-rate kill criterion against the regime transition count
- **Backtest** — `GET /api/v1/backtesting/klines` (1h/4h/1d to 2017-08) with funding drag from `GET /api/v1/backtesting/funding` (Hyperliquid hourly since 2023-05); condition results on `GET /api/v1/quant/regimes/history` (since 2020) to verify the edge concentrates in trend states, not chop
- **Tips** — refresh signals once daily off the cached `/api/v1/daily` bundle — a trend system gains nothing from intraday polling; a crypto perp backtest without funding costs overstates Sharpe materially

## See Also
- [[turtle-trading]] -- the most famous trend-following system, which uses channel breakouts
- [[moving-average-crossover]] -- the core signal used by many CTA systems
- [[factor-investing]] -- time-series momentum is a factor that can be accessed in equities too
- [[momentum]] -- the underlying concept that drives trend following returns
- [[breakout-trading]] -- channel breakout methodology used in CTA systems
- [[commodity-momentum]] -- cross-sectional momentum in commodity futures
- [[commodity-carry-strategy]] -- systematic carry trading in commodity futures
- [[cot-report-analysis]] -- positioning data analysis for futures markets
- [[commodities]] -- the commodity markets overview

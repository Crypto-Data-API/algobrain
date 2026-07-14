---
title: "Moving Average Crossover"
type: strategy
created: 2026-04-06
updated: 2026-07-13
status: excellent
tags: [trend-following, moving-averages, technical-analysis, crossover, momentum, indicators]
aliases: ["MA Crossover", "Golden Cross Strategy", "Death Cross Strategy", "Golden/Death Cross", "50/200 SMA System"]
strategy_type: technical
timeframe: swing|position|long-term
markets: [crypto, forex, commodities, futures]
complexity: beginner
backtest_status: paper-traded
edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "Persistent trends arise from slow information diffusion, herding, and rebalancing inertia; trend-followers are paid by mean-reversion traders and impatient liquidity demanders"
data_required: [ohlcv-daily, atr-14]
min_capital_usd: 5000
capacity_usd: 100000000
crowding_risk: high
expected_sharpe: 0.5
expected_max_drawdown: 0.30
breakeven_cost_bps: 25
decay_evidence: "Brock et al 1992 edge largely arbitraged out post-publication. Time-series momentum (Moskowitz 2012) still robust in cross-asset universes but compressed in single-asset settings."
related: ["[[supertrend]]", "[[ichimoku-cloud]]", "[[parabolic-sar]]", "[[exponential-moving-average]]", "[[simple-moving-average]]", "[[macd]]", "[[atr]]", "[[trend-following]]", "[[time-series-momentum]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[live-journal]]", "[[book-technical-analysis-of-the-financial-markets]]", "[[cryptodataapi]]"]
---

# Moving Average Crossover

The Moving Average Crossover is the canonical [[trend-following]] strategy: enter long when a shorter-period [[moving-average]] crosses above a longer-period one, exit (or reverse short) when it crosses back. Its most famous form is the **Golden Cross** — the 50-day [[simple-moving-average]] crossing above the 200-day SMA — and its mirror the **Death Cross**. The rule is mechanically trivial, but the question of whether it actually generates positive expectancy net of costs has been litigated continuously in the academic finance literature since the early 1990s, with answers ranging from "yes, robustly" (Brock, Lakonishok, LeBaron 1992) to "no, after data-snooping correction" (Sullivan, Timmermann, White 1999) to "yes, when applied as a cross-asset time-series momentum portfolio" (Moskowitz, Ooi, Pedersen 2012; Hurst, Ooi, Pedersen 2017).

## Edge source

Three of the five categories from the [[edge-taxonomy]] apply here:

1. **Behavioral.** Investors herd into established trends and underreact to gradually-arriving information. The 200-day SMA functions as a coarse summary of the medium-term consensus; when price decisively breaks above it, late-arriving participants pile in, extending the move.
2. **Structural.** Large institutional flows — pension rebalances, ETF creations, target-date fund glide-paths, sovereign-wealth allocations — execute over weeks and months rather than seconds. This creates measurable autocorrelation at horizons from one to twelve months, the same horizons at which the 50/200 cross fires.
3. **Risk-bearing.** Trend-followers are by construction the natural counterparty to mean-reversion traders during sustained trends. When a market grinds up for six months and a fader keeps shorting tops looking for the snapback, the trend-follower's late, lagged long is what absorbs the impatient liquidity demander's flow. The trend-follower is paid for the willingness to look stupid in the middle of a trend (chasing) and to take large drawdowns at every reversal — a genuine risk premium, not a free lunch.

The strategy has **no informational edge** — the signal is computed from public price data — and **no latency edge** — fills happen at end-of-day or end-of-bar. Anyone claiming a moving-average crossover gives them an information advantage is confused; the entire premise is that the market price already contains the information and the trend persists because of how slowly humans and institutions act on it.

## Why this edge exists

The behavioral underpinnings have been mapped explicitly by Daniel Kahneman, Amos Tversky, and successors:

- **Underreaction to news.** Kahneman's *Thinking, Fast and Slow* (System 1 / System 2) framework predicts that fundamental news — earnings, macro data, regulatory change — is initially anchored to the prior price level and only fully repriced over weeks as analysts revise estimates and slow money reallocates. This is the diffusion mechanism that creates positive serial correlation at the one-to-twelve-month horizon documented by Moskowitz, Ooi, and Pedersen (2012).
- **Anchoring.** Traders anchor exit decisions to round-number price levels and recent highs/lows rather than re-evaluating from scratch. This produces clusters of stops that, when triggered, accelerate moves through prior congestion zones — exactly the kind of price action that converts a slow drift into a confirmed crossover.
- **Herding and confirmation bias.** Once a trend is visible to the financial media (and the 50/200 cross is media-friendly precisely because anyone can see it), reporting amplifies it. Confirmation bias makes existing longs hold, and the cross becomes a self-fulfilling on-ramp for new capital.
- **Institutional rebalancing inertia.** Mandates require quarterly or annual rebalances; large pension allocations to private equity or real estate that have appreciated force public-equity buys; risk-parity funds add to winning legs as realized vol falls. None of these flows happens in a single day. The 200-day window is roughly the timescale over which they unfold.

Hurst, Ooi, and Pedersen's *A Century of Evidence on Trend-Following Investing* (2017) extends this evidence across 137 years and finds positive returns to a simple time-series momentum strategy in every decade since 1880 — including, critically, the decades before any of the behavioral finance literature was written, before Markets in Financial Instruments Directive existed, and before the first CTA fund opened. The persistence across regimes argues for a structural rather than purely behavioral cause.

## Null hypothesis

Under a pure random walk with zero drift, the 50/200 SMA crossover should:

- Win exactly 50% of the time
- Have an expected reward-to-risk ratio of 1:1
- Generate negative expectancy after transaction costs and slippage

The **observed** behavior (when the strategy works) is:

- **Win rate of 35–45%** — *worse* than the null
- **Average winning trade roughly 2-3x average losing trade** — much *better* than the null
- **Net expectancy slightly positive** before costs, marginal-to-negative after costs in single-asset settings

The edge does not look like "the strategy wins more often." It looks like a fat right tail of trade outcomes — a small number of multi-month trends that pay for many small whipsaw losses. This distribution shape is the empirical signature of trend-following across all major studies and all asset classes, and it is what distinguishes a genuine trend strategy from a curve-fit one. A backtest that shows a moving-average crossover with a 65% win rate and tight risk:reward is almost certainly overfit (see [[overfitting-detection]]).

## Rules

### Variant 1 — Classic Golden/Death Cross (50/200 SMA, daily)

- **Long entry:** 50-day SMA closes above 200-day SMA
- **Short entry (or close long):** 50-day SMA closes below 200-day SMA
- **Stop:** initial stop at the 200-day SMA; or [[atr|ATR]]-based trailing stop after a defined profit
- **Position sizing:** fixed 1–2% of capital risked per trade
- Used canonically on cash equities and indices. This is the form Brock, Lakonishok, and LeBaron tested.

### Variant 2 — Inverse-Volatility-Sized 50/200 SMA (canonical for the reference bot)

- **Signal:** identical to Variant 1
- **Sizing:** position size scaled inversely to recent realized volatility (ATR-normalized) — see [[#Inverse-Volatility Sizing]] below
- **Exit:** trailing stop at 2.0× [[atr|ATR(14)]] from the highest reached price (high-water mark) for longs; mirror for shorts
- **Caps:** maximum 8% of book per asset, maximum 2× gross leverage
- **Hold horizon:** days to weeks; reversal exits via trailing stop, not signal flip
- **Venue:** crypto perpetual futures DEX
- This variant is the implementation in the live trading harness (see [[live-journal]]). It sacrifices the clean signal-flip exit of Variant 1 for tighter risk control on the high-volatility, high-whipsaw crypto perp universe.

### Variant 3 — 9/21 EMA Fast Crossover

- **Signal:** 9-period [[exponential-moving-average|EMA]] crossing 21-period EMA
- Used for swing trading on lower timeframes (4H, daily) and intraday futures
- Faster signal, more whipsaws, smaller average trade
- Common in retail futures and crypto-spot communities

### Variant 4 — 20/50 EMA Intermediate

- **Signal:** 20 EMA crossing 50 EMA
- Sits between fast and slow regimes; common in equity swing trading
- Higher signal frequency than the Golden Cross but smoother than 9/21

All four variants share the same edge mechanism and the same fundamental fragility (whipsaws in choppy regimes). They differ only in the trade-off between lag and noise.

## Implementation pseudocode

The following sketch matches the reference live bot. It computes the 50/200 SMA cross, sizes by inverse ATR-normalized vol, caps at 8% per asset and 2× total leverage, and trails exits at 2× ATR from the high-water mark.

```python
import numpy as np
import pandas as pd

# ---- Configuration ----
FAST = 50
SLOW = 200
ATR_PERIOD = 14
TRAIL_ATR_MULT = 2.0
MAX_POSITION_FRACTION = 0.08   # 8% of equity per asset
MAX_GROSS_LEVERAGE = 2.0
TARGET_RISK_PCT = 0.005        # 0.5% per-asset target daily vol contribution

def atr(df, n=ATR_PERIOD):
    high, low, close = df['high'], df['low'], df['close']
    prev_close = close.shift(1)
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs(),
    ], axis=1).max(axis=1)
    return tr.rolling(n).mean()

def signal(df):
    sma_fast = df['close'].rolling(FAST).mean()
    sma_slow = df['close'].rolling(SLOW).mean()
    long_cond  = (sma_fast > sma_slow) & (sma_fast.shift(1) <= sma_slow.shift(1))
    short_cond = (sma_fast < sma_slow) & (sma_fast.shift(1) >= sma_slow.shift(1))
    return long_cond.astype(int) - short_cond.astype(int)   # +1 / -1 / 0

def inverse_vol_size(equity, price, atr_value):
    """ATR-normalized inverse-vol sizing.
    Position notional = (equity * target_risk) / (ATR / price)
    so that per-asset contribution to portfolio vol is roughly constant.
    """
    atr_pct = atr_value / price
    raw_notional = (equity * TARGET_RISK_PCT) / atr_pct
    cap_notional = equity * MAX_POSITION_FRACTION
    return min(raw_notional, cap_notional)

def manage_trailing_stop(state, price, atr_value):
    """Update high-water-mark trailing stop at 2x ATR."""
    if state['side'] == +1:
        state['hwm'] = max(state['hwm'], price)
        stop = state['hwm'] - TRAIL_ATR_MULT * atr_value
        if price <= stop:
            return 'EXIT'
    elif state['side'] == -1:
        state['hwm'] = min(state['hwm'], price)
        stop = state['hwm'] + TRAIL_ATR_MULT * atr_value
        if price >= stop:
            return 'EXIT'
    return 'HOLD'

def step(portfolio, market_data):
    total_notional = sum(abs(p['notional']) for p in portfolio['positions'].values())
    for symbol, df in market_data.items():
        sig = signal(df).iloc[-1]
        a = atr(df).iloc[-1]
        price = df['close'].iloc[-1]
        pos = portfolio['positions'].get(symbol)

        # Manage open position first
        if pos is not None:
            action = manage_trailing_stop(pos, price, a)
            if action == 'EXIT':
                close_position(portfolio, symbol, price)
                continue

        # New entry
        if sig != 0 and pos is None:
            notional = inverse_vol_size(portfolio['equity'], price, a)
            if (total_notional + notional) / portfolio['equity'] > MAX_GROSS_LEVERAGE:
                continue   # leverage cap respected
            open_position(portfolio, symbol, side=sig, notional=notional, hwm=price)
```

A few implementation notes worth highlighting:

- **Signal evaluation on bar close only.** Intra-bar crossovers can flicker; commit only on closed bars to avoid double-counting fills.
- **ATR normalized to price.** ATR in dollar terms is meaningless across assets ($BTC vs $SOL); ATR/price (a unitless % daily range) is the correct sizing scalar.
- **Leverage check is global.** A new entry that pushes total gross above 2× is skipped, not pro-rated. This is conservative and matches the bot.
- **No funding-rate filter.** A more sophisticated version of this strategy on perp DEXs would skip new longs when [[funding-rate|funding]] is deeply positive (paying to hold) and skip shorts when funding is deeply negative.

## Indicators / data used

- [[simple-moving-average|SMA]](50) and SMA(200) on close prices, daily timeframe
- [[atr|ATR]](14) for both inverse-vol sizing and the 2× ATR trailing stop
- [[volume]] as an optional confirmation filter (rising volume on the cross strengthens the signal)
- For perp-DEX execution: real-time mark price, [[funding-rate]] for cost accounting, [[order-book-depth]] to confirm fillability of the inverse-vol-sized order

Data requirements are modest: clean daily OHLCV is sufficient. The strategy does not need tick data, options chains, fundamentals, or alternative data — which is part of why it has been in continuous use for over a century.

## Example trade

**Asset:** BTC/USD perpetual swap, daily
**Setup:** Q1 2023 Bitcoin recovery off the FTX-collapse low

1. **2023-02-06:** 50-day SMA crosses above the 200-day SMA. BTC closes at \$22,950. ATR(14) = \$1,180 (≈5.1% of price).
2. **Inverse-vol sizing.** Equity = \$100,000. Target per-asset risk = 0.5%. Raw notional = (\$100,000 × 0.005) / 0.051 ≈ \$9,800. The 8% cap = \$8,000, so the position is capped at \$8,000 notional, or roughly 0.349 BTC. With 2× allowable leverage and the position fitting comfortably, leverage check passes.
3. **Entry fill:** \$22,950, position 0.349 BTC, notional \$8,000. Initial trailing stop = \$22,950 − 2.0 × \$1,180 = **\$20,590**.
4. **Trend progression:**
   - Day 5: BTC \$24,400. New high-water mark \$24,400. Stop ratchets to \$24,400 − 2 × ATR(14) (now \$1,205) = \$21,990.
   - Week 4: BTC \$28,500. ATR(14) compresses to \$880 as realized vol cools. Stop = \$28,500 − \$1,760 = \$26,740.
   - Week 8: BTC tags \$31,000. Stop \$29,250.
   - Week 12: BTC \$30,500 (slight pullback). Stop unchanged at \$29,250.
   - Week 14: BTC reverses sharply on March-2023 banking-crisis volatility. Closes \$28,800 — below the \$29,250 trailing stop on the morning of the next bar.
5. **Exit fill:** \$28,800. Realized P&L per BTC = +\$5,850. On the 0.349 BTC position: **+\$2,041**, or roughly +25.5% on the \$8,000 notional, +2.0% on portfolio equity.
6. **Funding cost during hold.** Average funding while long: +0.012% / 8h ≈ +0.036% / day. Over 98 days the long paid roughly 3.5% of notional in funding, or **−\$280**, reducing the realized P&L to **+\$1,761**. The 50-day SMA at exit is still above the 200-day SMA — the trade exits on the trailing stop, not on a death cross. A pure Variant 1 implementation would have stayed long until the death cross fired in late 2023.

This is a textbook winner: the trailing stop captures the bulk of the trend and exits before the multi-month chop that followed. Approximately one out of every three to five trades produces a payoff in this size range; the rest are small whipsaws that sum to roughly the same magnitude but with the opposite sign, leaving a small net positive expectancy.

## Inverse-Volatility Sizing

The reference bot does not size every position equally. Instead, it sizes inversely to each asset's recent realized volatility, using ATR(14)/price as the volatility proxy. The formula:

```
position_notional = (equity * target_risk_pct) / (ATR / price)
```

with hard caps at 8% of equity per asset and 2× gross leverage across the portfolio.

The intuition is portfolio-vol budgeting. If BTC has ATR/price = 4% and DOGE has ATR/price = 8%, an equal-dollar position in DOGE contributes twice as much daily P&L variance as the BTC position. By scaling inversely, each position contributes roughly the same amount of variance, regardless of which asset is currently quiet or noisy. This is the same principle used in [[risk-parity]] portfolio construction and the same scaling Moskowitz, Ooi, and Pedersen (2012) apply to their 58-instrument time-series momentum portfolio.

For a trend-following strategy, inverse-vol sizing has three concrete benefits over equal-dollar sizing:

1. **Whipsaw losses are smaller in choppy assets.** Choppy assets have high ATR, which means small positions, which means small losses when the inevitable whipsaw arrives.
2. **Calm trends get amplified.** When an asset is grinding up smoothly with low ATR, the position is large and captures the trend in size. Calm trends are exactly the ones moving averages are best at catching.
3. **Drawdowns are less correlated.** When market-wide volatility spikes (March 2020, May 2022, FTX November 2022), every asset's ATR jumps simultaneously and every position size is automatically reduced, providing a portfolio-level vol target without a separate de-risking rule.

The cost of inverse-vol sizing is that during a quiet, persistent multi-month trend in a single dominant asset (the BTC bull leg of 2020–2021, for instance) the strategy can underweight the asset that is doing all the work. But for a multi-asset crypto perp universe with frequent rotation, the variance smoothing is worth the opportunity cost.

The 8% per-asset cap is a separate concentration constraint that overrides the vol-scaled output for unusually quiet assets. Without it, a stablecoin-pegged perp with ATR/price ≈ 0.1% would size to >100% of equity. The cap and the leverage cap together ensure the strategy stays inside its risk envelope even when the inverse-vol sizing logic would otherwise blow it out.

## Performance characteristics

### Equities (Brock, Lakonishok, LeBaron 1992 — and its decay)

Brock, Lakonishok, and LeBaron's *Simple Technical Trading Rules and the Stochastic Properties of Stock Returns* (Journal of Finance 47(5), 1992, pp. 1731–1764) tested 26 simple trading rules — including the 1/50, 1/150, 5/150, 1/200, and 2/200 moving-average crossovers — on the Dow Jones Industrial Average from 1897 to 1986, using bootstrap inference against four null models (random walk, AR(1), GARCH-M, EGARCH). Buy signals consistently produced returns of roughly 12% annualized vs sell-signal returns near zero, with t-statistics that survived bootstrap correction.

This paper is the empirical foundation that legitimized technical analysis in academic finance. It is also, in retrospect, the high-water mark for the cash-equity moving-average crossover edge. Sullivan, Timmermann, and White's 1999 follow-up *Data-Snooping, Technical Trading Rule Performance, and the Bootstrap* (Journal of Finance 54(5), 1999, pp. 1647–1691) re-tested Brock et al.'s universe using White's Reality Check methodology to correct for the multiple-comparison problem (testing many rules and reporting the best one). They found that while the in-sample evidence held up under proper correction through 1986, **out-of-sample on 1987–1996 the same rules generated essentially zero excess return**. The edge had degraded — a textbook case of post-publication arbitrage and one of the cleanest examples of strategy decay in the literature (see [[when-to-retire-a-strategy]] and [[failure-modes]]).

The takeaway for equities is sobering. The 50/200 cross on the S&P 500 in 2026 is not the same trade it was in 1986. Index futures arbitrage, ETF creation/redemption, and algorithmic momentum-on-momentum strategies have compressed the inefficiency that Brock et al. measured. Naively backtesting a Golden Cross on SPY since 2000 typically yields roughly market-equivalent returns with lower drawdown — the strategy survives mostly as a drawdown-management tool rather than an alpha generator.

### Futures and CTAs (time-series momentum, 1985–present)

Moskowitz, Ooi, and Pedersen's *Time Series Momentum* (Journal of Financial Economics 104(2), 2012, pp. 228–250) document significant positive serial correlation at 1- to 12-month horizons across 58 liquid futures instruments — equity indices, currencies, commodities, and bonds — from 1985 to 2009. A diversified portfolio of TSMOM strategies produced a Sharpe ratio above 1.0, far higher than any individual market, with low correlations to standard asset-pricing factors and the unusual property of performing best in extreme markets (both up and down).

This work, together with Hurst, Ooi, and Pedersen's *A Century of Evidence on Trend-Following Investing* (Journal of Portfolio Management 44(1), 2017, pp. 15–29), is the strongest extant evidence that the trend-following premium is real and stable across regimes. Hurst et al. extend the test back to 1880 across global markets and find positive returns to a simple TSMOM strategy in every decade. Critically, the strategy worked in 8 of the 10 worst drawdown periods for a 60/40 portfolio — the so-called "crisis alpha" property that institutional CTAs sell.

The 50/200 SMA crossover is a specific point in the moving-average parameter space that approximates a 12-month look-back. As such, it shares a common risk factor with any other trend-following formulation at similar horizons (12-month return sign, breakout-of-N-day-high, etc.). The Hurst et al. evidence applies to all of them.

### Crypto adaptation (2017–present)

Crypto markets are a distinct test case. Three properties differ materially from equity and futures markets:

- **Volatility is 4–8× higher.** ATR/price for major coins runs 3–8% daily vs 1–1.5% for SPY. Trends are sharper but so are the false starts.
- **Funding-rate carry on perps is non-trivial.** A 0.05%/8h positive funding rate compounds to roughly 5.5%/year. If you hold a long for 200 days during a bull run, you may pay 3% of notional in funding, eroding meaningfully into the trend P&L.
- **Regime structure is bimodal.** Crypto spends extended periods either trending hard or chopping hard with relatively little time in between. This rewards trend-following in trending regimes but punishes it severely in chop (the 2018 and 2022 bear-market chops are examples).

Empirical results from independent crypto-trend backtests (with realistic funding and DEX-fee modeling) typically show:
- **Annualized Sharpe of 0.3–0.7** on a multi-coin universe with inverse-vol sizing
- **Maximum drawdown 25–35%**, usually concentrated in chop transitions (Q2 2022, Q1 2025)
- **Expectancy heavily right-tail-dependent** — removing the top 10% of trades typically zeros the strategy out

This puts crypto trend-following in the same broad performance band as equity-futures trend-following (Sharpe ≈ 0.5, MaxDD ≈ 30%) but with more violent month-to-month variance.

### Realistic cost overlay on perp DEX

Frictions for the reference bot:

- **Taker fee on perp DEX:** roughly 5 bps per side, 10 bps round-trip
- **Average slippage on inverse-vol-sized orders:** 1–3 bps in liquid coins, more in alts
- **Funding paid while holding directional perps:** averages roughly +1.5% / year net for a long-biased strategy in bull regimes, can flip to a credit in bear regimes
- **Total round-trip cost budget:** roughly 25 bps + funding drag, vs typical trade P&L distribution where average winners are 800–2000 bps

Total cost is small relative to winning trades but can swallow whipsaws. The breakeven cost the strategy can absorb (the `breakeven_cost_bps` field above) is roughly 25 bps round-trip; above that the entire edge dissipates. This makes venue and execution discipline first-order — a 5-bp fee differential is the difference between a viable and a non-viable strategy.

## Capacity limits

Capacity is unusually high. The strategy:

- Holds only directional positions — no spreads, no options, no exotic structures
- Trades daily-close signals, not high-frequency
- Holds for days-to-weeks, giving time to enter and exit in chunks

The binding capacity constraint is per-asset depth at end-of-day. For BTC and ETH perps on a major DEX, single-day fills of \$50–100M are routine without market impact above 5–10 bps. Cross-portfolio capacity at the 8% / asset cap and 2× leverage scales linearly: a \$10M book can hold positions up to \$800k each across 25 coins; a \$1B book can hold \$80M positions across the same coins, well within liquidity at the top of the universe.

The strategy starts running into limits when:
- The universe is expanded to thinly-traded alts where the inverse-vol-sized notional exceeds 1% of daily volume
- The portfolio is large enough that signal-flip days (e.g., a market-wide death cross) require unwinding multiple coins simultaneously and slippage starts to interact with correlated flow

For a single trader running a personal book, capacity is effectively unlimited. For a fund running this style at \$500M+ AUM, execution algorithms and the breadth of the universe become the main constraints. AQR, Man-AHL, Winton, and other large CTAs implement broadly the same idea across hundreds of futures markets to absorb several billion in capacity per fund.

## What kills this strategy

Concrete failure modes from [[failure-modes]]:

1. **Choppy regime / lower autocorrelation.** Equities 2015–2016 (the famous "two-year flat" with multiple 10% drawdowns and recoveries), 2011–2013 in many global markets, and crypto Q2-Q4 2022 are textbook trend-following kills. ATR is high, trends fail to develop, and every 50/200 cross is followed within a month or two by the reverse cross at a worse price. Whipsaw losses compound. There is no trick to making moving averages work in a chop; the only response is either to widen the parameters (further lagging the entry) or to size down / step aside.
2. **Regime change in the underlying autocorrelation structure.** The Moskowitz-Pedersen TSMOM evidence shows 1- to 12-month positive autocorrelation has been stable for over a century in cross-asset portfolios, but individual markets can drift. A market dominated by a single, slow-moving order flow (institutional rebalances) supports trend; a market dominated by mean-reversion stat-arb shops kills it.
3. **Post-publication decay.** The Brock-Lakonishok-LeBaron edge in single-asset moving-average crossovers on the Dow effectively vanished after the early 1990s. Anything that runs in *Wall Street Journal* op-eds and CNBC headlines is, by construction, no longer an edge. The Golden Cross on SPY is in this category.
4. **Funding-cost regime shift.** On crypto perps, a sustained bull market drives funding rates very positive, eating into long-side trend P&L. If structural demand for leverage causes funding to average 30%+ annualized for extended periods, even a winning long trend trade can break even net of funding. The remedy is to filter entries by funding state.
5. **Liquidity collapse on the trail-stop fill.** Trailing stops are unconditional; in a flash-crash on a thin perp DEX the actual fill can be 5–10% worse than the stop level, far exceeding the 2× ATR cushion the strategy is designed around. This is a tail-risk failure mode unique to crypto venues.

## Kill criteria

For the bot, retire or pause the strategy if any of the following fire (these align with [[when-to-retire-a-strategy]]):

- **Six-month rolling Sharpe < 0** — the strategy has had ample time to find a trend; if it cannot it is in a regime it cannot trade
- **More than five consecutive whipsaw losses** across the universe (entries followed within 30 days by reverse-stop exits)
- **Universe-average ADX(14) < 20 over a 60-day window** — directly diagnoses chop regime
- **Maximum drawdown breach of 30%** — the `expected_max_drawdown` is itself the kill threshold; any deeper means the model is misspecified
- **Realized funding cost > 5% of notional / year on average** for longs, sustained over 90 days — funding regime has shifted enough to require a strategy revision

Pausing is preferred over retiring; the underlying edge has survived a century, so the appropriate response to a regime kill is usually to step out and re-test rather than to abandon the framework entirely.

## Advantages

- **Mechanically simple.** Two SMAs, one ATR, four lines of trade-management logic. Low surface area for bugs.
- **No discretion.** Signals are unambiguous. This is its own form of risk control — no late-night override decisions.
- **Robust across markets.** The same 50/200 idea works on equity indices, FX majors, commodities, bonds, and crypto. No reparameterization needed when adding a new asset to the universe.
- **Crisis alpha.** Trend-following has historically performed in 8 of the 10 worst 60/40 drawdowns (Hurst et al. 2017). Functions as portfolio insurance with positive expected cost rather than negative.
- **High capacity.** Scales to billions of dollars in a sufficiently broad universe.
- **Self-fulfilling component.** The 50/200 cross is so widely watched that the cross itself attracts marginal flow, modestly strengthening the signal.
- **Low data requirements.** Daily OHLCV is sufficient. No fundamentals, options chains, or alternative data.

## Disadvantages

- **Lagging by construction.** The 200-day window means by the time a cross fires, the trend has already been in place for weeks and a meaningful chunk of the move is gone.
- **Severe whipsaw risk.** In choppy markets, the strategy generates clusters of small losses with no offsetting wins. A 12-month chop can deliver −15% to −25% drawdowns purely from whipsaws.
- **Gives back open profit on signal-flip exits.** Variant 1 (no trailing stop) commonly exits 15–25% below the high. The trailing-stop variants improve this but introduce premature stop-outs in normal pullbacks.
- **Low win rate.** 35–45% wins is psychologically taxing; many discretionary traders abandon the strategy after 4–6 consecutive losers, exactly when the next big winner is statistically due.
- **Single-asset edge has decayed.** The Brock-Lakonishok-LeBaron result on the Dow has not survived the post-1990 period. The strategy needs cross-asset diversification or a vol-sized sleeve to be reliably positive expectancy.
- **Funding drag in crypto.** Long trends in crypto perps come with a structural funding cost that erodes a non-trivial fraction of the trade P&L.
- **No edge in a single backtest.** Naive backtesting on a single asset over a single window is the canonical way to fool yourself about this strategy. The signal looks genuine in 1990s Dow data, in 2017 BTC data, and in 2020 SPY data — and produces nothing in 2015 SPY data, 2018 BTC data, and 2022 crypto data. Only a multi-asset, multi-decade evaluation gives an honest read.

## Sources

- **Brock, William, Josef Lakonishok, and Blake LeBaron (1992)**, *Simple Technical Trading Rules and the Stochastic Properties of Stock Returns*, Journal of Finance 47(5), pp. 1731–1764. The seminal academic test of moving-average crossover rules on the Dow Jones 1897–1986. Established the empirical baseline.
- **Sullivan, Ryan, Allan Timmermann, and Halbert White (1999)**, *Data-Snooping, Technical Trading Rule Performance, and the Bootstrap*, Journal of Finance 54(5), pp. 1647–1691. Re-evaluated the Brock et al. result with proper data-snooping correction. Found the in-sample edge survives but out-of-sample 1987–1996 the same rules generated zero excess return — the canonical case of post-publication decay.
- **Moskowitz, Tobias J., Yao Hua Ooi, and Lasse Heje Pedersen (2012)**, *Time Series Momentum*, Journal of Financial Economics 104(2), pp. 228–250. Documents 1-to-12-month positive autocorrelation across 58 liquid futures markets 1985–2009. The cross-asset framework in which moving-average crossovers fit as one specific implementation.
- **Hurst, Brian, Yao Hua Ooi, and Lasse Heje Pedersen (2017)**, *A Century of Evidence on Trend-Following Investing*, Journal of Portfolio Management 44(1), pp. 15–29. AQR-authored extension showing positive returns to a simple TSMOM strategy in every decade since 1880 across global markets.
- [[book-technical-analysis-of-the-financial-markets]] — John Murphy. Standard practitioner reference on moving-average construction, signal generation, and the Golden/Death Cross terminology.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/indicators/technical` — price-structure state (SMA/BB/RSI) across assets
- `GET /api/v1/indicators/signum-rgg` — ADX(14)+DMI RED/GREY/GREEN state

**Historical data:**
- `GET /api/v1/indicators/technical/{symbol}` — per-asset detail + 60d history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — raw OHLCV for computing your own

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/indicators/technical"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-indicators]].

## Related

- [[trend-following]] — broader strategy category
- [[time-series-momentum]] — academic formulation of the same edge
- [[simple-moving-average]] / [[exponential-moving-average]] — the underlying indicators
- [[macd]] — uses MA crossover concepts with momentum overlay
- [[supertrend]] / [[ichimoku-cloud]] / [[parabolic-sar]] — alternative trend-following systems
- [[atr]] — volatility measure used for sizing and stops
- [[funding-rate]] — material cost driver for perp-DEX implementations
- [[risk-parity]] — same inverse-vol sizing principle in a portfolio-construction context
- [[edge-taxonomy]] — framework for the behavioral / structural / risk-bearing classification used here
- [[failure-modes]] — taxonomy of what kills strategies
- [[when-to-retire-a-strategy]] — kill-criteria methodology
- [[live-journal]] — current deployment status of this strategy in the reference bot
- [[overfitting-detection]] — why naive single-asset backtests of MA crossovers mislead

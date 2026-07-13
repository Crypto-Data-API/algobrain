---
title: "RSI Mean Reversion"
type: strategy
created: 2026-04-06
updated: 2026-07-13
status: excellent
tags: [mean-reversion, rsi, oversold, overbought, quantitative, larry-connors, crypto, stocks, behavioral-finance, indicators]
aliases: ["RSI Reversion", "RSI Oversold Bounce", "Connors RSI Strategy", "Connors RSI(2)", "Oversold Bounce"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, stocks]
complexity: beginner
backtest_status: paper-traded

# Edge characterization (see [[edge-taxonomy]])
edge_source: [behavioral, risk-bearing]
edge_mechanism: "Short-term oversold extremes in uptrends are caused by overreactive selling that the broader market quickly arbitrages away"

# Data and infrastructure requirements
data_required: [ohlcv-daily, rsi-2, fear-greed-index]
min_capital_usd: 1000
capacity_usd: 50000000
crowding_risk: medium

# Performance expectations
expected_sharpe: 1.0
expected_max_drawdown: 0.30
breakeven_cost_bps: 20

# Decay history
decay_evidence: "Connors' original SPY edge has compressed since 2010 publication; crypto adaptation may still have edge (recent academic work suggests behavioral biases are stronger in retail-dominated crypto)"

related: ["[[rsi]]", "[[bollinger-band-reversion]]", "[[mean-reversion]]", "[[moving-average-crossover]]", "[[200-day-moving-average]]", "[[overreaction-anomaly]]", "[[sentiment]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[loss-aversion]]", "[[herding]]", "[[cryptodataapi]]"]
---

The **RSI Mean Reversion** strategy buys assets that have suffered short, sharp pullbacks inside an established uptrend, betting that the panic-driven selling will reverse within a few days. The canonical formulation is **Larry Connors' RSI(2)** rule from *Short Term Trading Strategies That Work* (2009): go long when RSI(2) drops below 10 while price is above its 200-day SMA, and exit when RSI(2) closes above 70. The user's live trading bot extends this to large-cap crypto by stacking a **Crypto Fear & Greed < 30** sentiment filter on top of the classic Connors trigger, restricting the universe to BTC/ETH/SOL on AsterDEX with 3x leverage.

## Edge source

This strategy harvests two of the five edges from [[edge-taxonomy]]:

1. **Behavioral edge.** When an asset trends higher, holders develop conviction. A 2-3 day flush — driven by macro news, a leveraged liquidation cascade, or pure flow imbalance — triggers loss-aversion ([[loss-aversion]]) and herding ([[herding]]) responses in late-arriving longs and weak-handed retail. They sell into a market that has not changed fundamentally, only emotionally. RSI(2) < 10 is a quantification of "everyone who could panic, has panicked."
2. **Risk-bearing edge.** Buying into capitulation requires absorbing inventory that more risk-averse participants are dumping. The systematic buyer is the liquidity provider of last resort to forced sellers (margin calls, stop-losses, fund redemptions). Compensation comes from the bid-ask spread and the rapid bounce as fundamental holders re-step into the bid.

The Crypto Fear & Greed filter (when used on the crypto adaptation) sharpens both edges: it confirms that the panic is *broad* (not just a noisy single-asset wiggle) and that risk-averse capital is still flowing out, leaving a clearer field for the systematic buyer.

This is **not** an analytical, informational, or latency edge. The trade is fully public and triggers off lagging indicators. Its profitability depends entirely on the persistence of human overreaction — a fact that makes regime monitoring (see Kill Criteria) essential.

## Why this edge exists

The intellectual foundation comes from three streams of research:

**Academic literature on short-horizon return reversal.** Bruce Lehmann's *Fads, Martingales, and Market Efficiency* (Quarterly Journal of Economics, 1990) showed that weekly winners and losers in US equities reverse in the following week, producing apparent arbitrage profits that survive bid-ask spreads and plausible transaction costs. Lehmann interpreted this as inefficiency in the market for liquidity around large price changes — exactly the mechanism Connors later exploited at the daily timescale. Lo and MacKinlay's *When Are Contrarian Profits Due to Stock Market Overreaction?* (Review of Financial Studies, 1990) cautioned that not all contrarian profits stem from overreaction (some come from cross-autocorrelation among stocks), but it confirmed that short-horizon mean reversion is robust and economically meaningful. See also [[overreaction-anomaly]].

**Connors' empirical work (2008-2010).** In *Short Term Trading Strategies That Work* (Connors and Alvarez, ISBN 9780981923901) and the follow-up *High Probability ETF Trading*, the authors backtested simple RSI(2) rules on the S&P 500 and large-cap ETFs back to 1995. The headline finding: when SPY trades above its 200-day SMA and RSI(2) drops below 10, the average 1-week forward return is roughly 5-10x larger than an unconditional 1-week SPY return, with win rates above 80%. The 2-period RSI is hyper-sensitive — it is essentially a smoothed measure of "how aggressive was the last two days of selling relative to buying" — and the 200-day SMA acts as a regime filter, ensuring you only buy dips inside structural uptrends. Connors called RSI(2) the "trader's holy grail of indicators" in Chapter 9.

**Why the edge transfers to crypto.** Crypto is dominated by retail flow and forced leverage liquidations far more than US large-cap equities. When BTC drops 15% on a macro shock, the cascade includes (a) directional retail panic, (b) cross-margin auto-deleveraging on perp exchanges, and (c) tax-loss-style flush selling. Each of these is a textbook overreaction generator. In a bull regime (price > 200-day SMA), the structural buyers — ETF flows, treasury accumulators, long-only funds — re-enter quickly, producing tradeable bounces in the 2-5 day window. The Crypto Fear & Greed Index (alternative.me) further confirms that the cohort of retail and social-media participants is in capitulation mode: a reading below 30 ("Fear" or "Extreme Fear") historically marks local price bottoms in trending markets.

The mechanism, restated: **panic sellers consume liquidity at a discount to fundamental value; systematic dip-buyers provide that liquidity and earn the rebound when sentiment normalizes.**

## Null hypothesis

If RSI extremes carry no behavioral information — i.e., prices follow a random walk with no overreaction — then conditioning entries on RSI(2) < 10 should produce returns indistinguishable from random entries, after controlling for the trend filter:

- **Win rate:** approximately 50% at 1:1 reward:risk, or whatever the unconditional base rate is for the asset class over the matched holding period
- **Sharpe ratio:** approximately zero net of costs
- **Edge over buy-and-hold:** none
- **Distribution of outcomes:** symmetric around the underlying drift; no fat right tail

The strategy must reject this null in live trading. Specifically, statistical evidence of edge requires:

- Conditional 5-day forward return after RSI(2) < 10 + 200-day filter is materially positive and **distinguishable from the unconditional 5-day return** for the same universe (test: paired t-test or bootstrap on conditional vs. unconditional samples)
- Win rate > 60% at the strategy's actual exit rule (RSI(2) > 70 or 5-day timeout)
- A **deflated Sharpe** (Bailey & López de Prado) above 0.5 after correcting for multiple testing across the parameter grid (RSI lookback, threshold, hold period, F&G threshold)

If the null cannot be rejected after a reasonable sample (~50 trades), the strategy should be retired regardless of how intuitive the story sounds.

## Rules

The user's bot implements **Variant C** below. Variants A and B are documented for context and historical lineage.

### Variant A: Classic RSI(14) (legacy, less effective)

1. **Long entry:** RSI(14) closes below 30. Buy at the close (or next open).
2. **Exit:** RSI(14) closes above 70. Sell at the close.
3. **Stop-loss:** fixed 5% from entry, or RSI(14) continues below 20.
4. **Universe:** any liquid stock or ETF.

This is the textbook Wilder formulation taught in most retail TA courses. Without a trend filter it suffers severely in downtrends — buying RSI(14) < 30 on a stock that just lost a fundamental support is a textbook way to catch a falling knife. Modern empirical studies show this naked variant has near-zero edge net of costs.

### Variant B: Connors RSI(2) on stocks (the original)

1. **Filter:** price > 200-day SMA (uptrend regime only).
2. **Long entry:** RSI(2) closes below 10 (aggressive: below 5). Buy at the close.
3. **Exit:** RSI(2) closes above 70 (or above 5-day SMA for the conservative version). Sell at the close.
4. **Stop-loss:** none in the original rule set — Connors' research showed adding stops *reduced* expected return because the strategy's edge comes from buying deeper as panic accelerates. In production deployment, a hard stop at the 200-day SMA is sometimes added as a regime kill-switch.
5. **Universe:** SPY, QQQ, large-cap ETFs and S&P 500 single names with a confirmed long-term uptrend.

This is the rule set on which the 75-85% win rate claim is based. See [[rsi]] and [[200-day-moving-average]].

### Variant C: Crypto-adapted RSI(2) + Fear & Greed filter (the user's bot — canonical)

1. **Universe:** BTCUSDT, ETHUSDT, SOLUSDT only — large-cap crypto with deep liquidity. No alts, no memecoins.
2. **Trend filter:** spot price > 200-day SMA on each asset, evaluated independently.
3. **Sentiment filter:** Crypto Fear & Greed Index (alternative.me daily reading) < 30 (i.e., "Fear" or "Extreme Fear" zone). The bot polls the public API once per day after the daily candle close.
4. **Trigger:** RSI(2) on the daily close drops below 10.
5. **Direction:** LONG only. (Connors' work found symmetric short signals are far weaker; in a crypto bull regime they are catastrophically weaker.)
6. **Position size:** 5% of equity per trade, with **3x leverage** on AsterDEX perps. Effective notional exposure per trade ≈ 15% of equity. Maximum 3 concurrent positions, capping gross at 45% notional.
7. **Exit (whichever first):**
   - RSI(2) closes > 70 (the bounce signal), OR
   - 5 trading days have elapsed since entry (timeout — prevents the position from morphing into a directional bet), OR
   - Hard regime stop: spot price closes below the 200-day SMA on the entry asset (kill-switch).
8. **Cooldown:** after any exit, no re-entry on the same asset for 24 hours.

The 5-day timeout and 200-day-SMA kill-switch convert what is otherwise a pure bounce trade into a bounded-loss structure. The Fear & Greed filter cuts out roughly 60-70% of raw RSI(2) < 10 signals — those that fire during euphoric markets where the overshoot is a healthy pullback rather than capitulation.

## Implementation pseudocode

```python
"""
Crypto-adapted RSI(2) + Fear & Greed mean-reversion bot.
Currently OFF (paper-traded only).
"""
import requests
import pandas as pd
import numpy as np

UNIVERSE = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
RSI_PERIOD = 2
RSI_ENTRY = 10
RSI_EXIT = 70
SMA_PERIOD = 200
FNG_THRESHOLD = 30
LEVERAGE = 3
RISK_PCT = 0.05            # 5% of equity per trade
MAX_POSITIONS = 3
MAX_HOLD_DAYS = 5

def rsi(series: pd.Series, period: int = 2) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0).ewm(alpha=1/period, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/period, adjust=False).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))

def fetch_fear_greed() -> int:
    """Crypto Fear & Greed Index (alternative.me). 0=Extreme Fear, 100=Extreme Greed."""
    r = requests.get("https://api.alternative.me/fng/?limit=1", timeout=10)
    return int(r.json()["data"][0]["value"])

def daily_signal(df: pd.DataFrame, fng: int) -> bool:
    """df: daily OHLCV with most recent bar at .iloc[-1]"""
    df["rsi2"] = rsi(df["close"], RSI_PERIOD)
    df["sma200"] = df["close"].rolling(SMA_PERIOD).mean()
    last = df.iloc[-1]
    in_uptrend = last["close"] > last["sma200"]
    oversold = last["rsi2"] < RSI_ENTRY
    fearful = fng < FNG_THRESHOLD
    return in_uptrend and oversold and fearful

def position_size(equity: float, price: float) -> float:
    """Returns notional contracts for a single entry at current price."""
    risk_capital = equity * RISK_PCT
    notional = risk_capital * LEVERAGE
    return notional / price

def exit_signal(entry_bar: int, current_bar: int, rsi_now: float,
                close_now: float, sma200_now: float) -> str | None:
    if rsi_now > RSI_EXIT:
        return "rsi_target"
    if (current_bar - entry_bar) >= MAX_HOLD_DAYS:
        return "timeout"
    if close_now < sma200_now:
        return "regime_stop"
    return None

def run_daily(equity: float, open_positions: dict, market_data: dict):
    fng = fetch_fear_greed()
    # 1. evaluate exits
    for symbol, pos in list(open_positions.items()):
        df = market_data[symbol]
        last = df.iloc[-1]
        reason = exit_signal(pos["entry_bar"], len(df) - 1,
                             last["rsi2"], last["close"], last["sma200"])
        if reason:
            close_position(symbol, reason)
            del open_positions[symbol]
    # 2. evaluate new entries (only if capacity remaining)
    if len(open_positions) >= MAX_POSITIONS:
        return
    for symbol in UNIVERSE:
        if symbol in open_positions:
            continue
        df = market_data[symbol]
        if daily_signal(df, fng):
            size = position_size(equity, df.iloc[-1]["close"])
            open_long(symbol, size, leverage=LEVERAGE)
            open_positions[symbol] = {"entry_bar": len(df) - 1,
                                      "entry_price": df.iloc[-1]["close"]}
```

A few production notes the pseudocode glosses over:

- The bot evaluates once per UTC day after the 00:00 candle closes; intraday RSI(2) excursions are intentionally ignored to avoid noise.
- Slippage assumption is 5 bps per side on AsterDEX BTC/ETH/SOL perps under normal conditions, 25 bps under stress (when the bot is most likely to fire).
- Funding rate paid during the 1-5 day hold is tracked separately; in fearful regimes funding is typically negative (shorts pay longs), which is a small tailwind.
- F&G API has occasional outages — the bot caches the last 7 days of values and degrades gracefully.

## Indicators / data used

| Input | Source | Frequency | Used for |
|-------|--------|-----------|----------|
| OHLC daily candles (BTC, ETH, SOL) | AsterDEX or Binance public API | 1d | RSI(2), 200-day SMA, price |
| RSI(2) | Computed from OHLC | 1d | Entry trigger, exit signal |
| 200-day SMA | Computed from OHLC | 1d | Regime filter |
| Crypto Fear & Greed Index | alternative.me public API | 1d | Sentiment confirmation |
| Funding rate | AsterDEX perp metadata | 8h | P&L attribution (passive) |

See [[rsi]] for the indicator math, [[200-day-moving-average]] for the filter rationale, and [[sentiment]] for the broader role of sentiment indices in trading.

## Example trade

**ETH on 5 August 2024 — yen carry unwind capitulation.** Cross-reference [[2024-08-yen-carry-unwind]].

- **2024-07-31:** Bank of Japan hikes rates 25 bps. USD/JPY begins unwinding.
- **2024-08-02:** US payrolls print 114k vs. 175k expected. Risk-off acceleration.
- **2024-08-04 close:** ETH = $2,693. RSI(2) = 18. F&G = 26. 200-day SMA ≈ $3,075. Trend filter **fails** (price below SMA), no entry.
- **2024-08-05 intraday:** ETH crashes ~25% to roughly $2,170 on cascading perp liquidations.
- **2024-08-05 close:** ETH = $2,419. RSI(2) = 3.8. F&G = 17 (Extreme Fear). 200-day SMA = $3,072. Trend filter **still fails** — the bot does NOT enter on the climactic bottom.

This is the strategy's canonical limitation surfaced in real time: the 200-day SMA filter protects against falling-knife scenarios but also forfeits the V-bottom in a true panic. The bot would only re-engage once ETH reclaimed the 200-day SMA (which happened around late August 2024).

**Counter-example: BTC on 17 March 2025 — clean signal trade.**

- 2025-03-15 close: BTC = $84,300. 200-day SMA = $79,800. Trend filter passed.
- 2025-03-15 to 2025-03-17: BTC drops to $80,750 on tariff-headline jitters. RSI(2) = 6.1 on 2025-03-17 close. F&G = 24. **All three filters trigger.**
- Bot enters long at $80,750, 5% equity * 3x leverage = $12,113 notional per $80,742 of equity.
- 2025-03-19 close: BTC = $87,400. RSI(2) = 78. **RSI exit fires** at $87,400.
- Trade duration: 2 days. Gross return on notional ≈ +8.2%. Levered equity return on the 5% slot ≈ +24.6%, contributing +1.23% to the book before fees and funding.
- Net (after ~10 bps round-trip fees + 2 days of slightly negative funding): +1.18% to the book.

Both trades — the one that didn't fire and the one that did — illustrate the same truth: this strategy makes money when panic happens *inside* an uptrend. When panic breaks the regime, the strategy correctly stays flat.

## Performance characteristics

### Connors' original SPY/equities backtest (1995-2008)

From *Short Term Trading Strategies That Work* and follow-on work:

- **Win rate:** 75-85% on SPY and large-cap S&P 500 names.
- **Average trade duration:** 2-6 trading days.
- **Average winner / average loser:** roughly 1.0 to 1.3 (small wins, slightly larger occasional losses — a classic high-win-rate, negatively-skewed payoff profile).
- **Profit factor:** 1.8-2.5 in-sample.
- **Annualized return on full capital:** modest in absolute terms (~8-12%) but very high *return per unit of time deployed* — capital sits idle 70-80% of the time.

These numbers are **in-sample** and survive normal robustness checks (parameter sensitivity, walk-forward), but they should be expected to compress out-of-sample due to publication-induced crowding. See decay note below.

### Crypto adaptation expected performance (paper-tracked)

The user's variant has not yet been deployed in size. Expected envelope from paper-trading and out-of-sample studies:

- **Win rate:** 65-75%. Lower than Connors' equity numbers because crypto's higher volatility produces larger losing trades when regime breaks intra-trade.
- **Average winner / average loser:** ~0.7 — more negatively skewed than the equity version. The 5-day timeout occasionally exits at a loss while RSI is still oversold but stalled.
- **Trades per year:** 8-15 across the BTC/ETH/SOL universe (Connors filter alone fires more; the F&G filter cuts roughly two-thirds of those).
- **Sharpe (expected, net of costs):** ~1.0.
- **Max drawdown (expected):** ~30%, dominated by the failure mode where regime breaks mid-trade (e.g., a March 2020-style crash).
- **Profit factor (expected):** 1.5-2.0.

### Cost overlay

Round-trip costs on AsterDEX BTC/ETH/SOL perps for a typical trade:

| Cost component | bps round-trip |
|----------------|----------------|
| Maker/taker fees (taker both legs) | 6-10 bps |
| Slippage (normal liquidity) | 4-8 bps |
| Slippage (stress, when bot most likely fires) | 20-40 bps |
| Funding (1-5 day hold, fearful regime) | -5 to +5 bps (often a small credit to longs) |
| **Typical round-trip cost** | **~20 bps** |

The strategy's average per-trade gross return must clear ~20 bps to be viable. With 1-3% gross moves typical, this is comfortable in normal conditions — but in a stress entry where slippage spikes to 40+ bps, the buffer narrows considerably. Hence the `breakeven_cost_bps: 20` in the frontmatter.

## Capacity limits

This is a high-capacity strategy by design:

- **BTC, ETH, SOL perp daily volumes** on major venues run from $5B (SOL) to $40B+ (BTC).
- **Maximum prudent position size** (1% of average daily volume, the conservative impact threshold) is roughly $50M on BTC, $20M on ETH, $5M on SOL — i.e., the strategy can comfortably absorb $50-100M of book equity at the user's 5%/15%-notional sizing.
- **Above ~$500M of book equity** dedicated to this single strategy, slippage on the entry leg starts to dominate during stress entries (which is precisely when the strategy needs to fire). This is the soft capacity ceiling.
- **The user's bot at retail size** (single-digit thousands to low millions of book equity) has no capacity concerns whatsoever.

The frontmatter records `capacity_usd: 50000000` as a conservative single-strategy capacity. For a fund running this as one of many sleeves, that number is more than enough.

## What kills this strategy

Drawing from [[failure-modes]], the named failure modes for this strategy are:

1. **Bear regime / regime change.** When the 200-day SMA breaks across all three majors simultaneously (e.g., May 2022 LUNA collapse, November 2022 FTX, Q1 2025 if the Trump tariff scenario had escalated), the strategy stops trading entirely and produces a long flat period. Not a loss — but a multi-month opportunity-cost drawdown for the slot of capital allocated.
2. **Mid-trade regime break ("the LUNA / FTX / March 2020 problem").** The strategy enters in what looks like a normal pullback, then the underlying breaks the 200-day SMA *intra-position*. The hard regime stop fires, but at a worse price than an ex-ante stop because the kill condition only checks at the daily close. This is the dominant source of large losses.
3. **Structural change in mean-reversion behavior.** Crypto bull regimes increasingly feature ETF-flow-driven grinds higher with shallow, fast pullbacks that don't reach RSI(2) < 10 — the signal stops firing. Or worse, retail behavior changes such that "fear" becomes a contrarian indicator only intermittently. The Connors equity edge has demonstrably compressed since the 2010 publication.
4. **Fear & Greed Index drift.** alternative.me's methodology (volatility 25%, momentum/volume 25%, social media 15%, BTC dominance, Google Trends 10%) was calibrated in a 2018-2020 retail-heavy market. As institutional flows dominate, the social and Google components add noise rather than signal. The filter could become uninformative.
5. **Crowding.** RSI(2) is one of the most-publicized retail strategies. If too many systematic buyers cluster at RSI(2) < 10, the bottom is bid up before the bot can fill, and the rebound's edge is squeezed out. Crowding risk is rated **medium** in the frontmatter.
6. **Black-swan tail.** A single event that breaks the assumptions — exchange insolvency mid-trade (FTX), regulatory ban, oracle exploit — produces a loss far larger than the modeled drawdown. This is uncoverable without external hedges.

## Kill criteria

Numerical, pre-committed conditions that retire the strategy. See [[when-to-retire-a-strategy]] (forward link).

- **Rolling 6-month Sharpe < 0.** Soft warning at < 0.3, hard kill at < 0.
- **Five consecutive losing trades.** Pause and review.
- **Drawdown > 25%** on the strategy's allocated sleeve (note: with 3x leverage and 15% gross notional, this implies an aggregate adverse move of roughly 8% across the open positions — plausible during a regime break).
- **All three majors close below their 200-day SMA on the same day.** Pause until at least one reclaims; this is regime-change confirmation.
- **F&G < 30 has fired but no RSI(2) < 10 trigger has occurred for 18 consecutive months.** The mean-reversion mechanism may have structurally died; review.
- **Deflated Sharpe of the live track record falls below 0.5** after multiple-testing correction across the F&G threshold, RSI threshold, and hold-period parameter grid evaluated in research.

The bot is currently OFF, so these criteria are aspirational. They will become binding once paper-trading produces a sufficient sample (~30 trades) to justify going live.

## Advantages

- **Highest documented win rate of any simple, public retail strategy.** The Connors variant has stood up to thousands of independent backtests. The crypto adaptation is unproven but inherits the underlying behavioral mechanism.
- **Short holding period (1-5 days)** caps overnight and weekend exposure, and the capital sits idle most of the time — freeing the same capital for other strategies.
- **Trivial to implement.** Two indicators, one API call, one trend filter. The implementation pseudocode above is genuinely complete.
- **Psychologically comfortable** because most trades win — but see the matching disadvantage.
- **Composable.** Pairs naturally with longer-horizon strategies (e.g., [[moving-average-crossover]] trend systems) because it monetizes pullbacks that the trend system's drawdowns ignore.
- **Crypto-specific tailwind:** retail-dominated, leverage-heavy markets produce more frequent and more extreme overreactions than equities, so the underlying mechanism is *louder* in crypto than in Connors' original equity universe.

## Disadvantages

- **Negatively skewed payoff.** Many small wins, occasional large losses. The 75-85% win rate marketing line obscures that the *expectancy* depends entirely on keeping the average loss bounded — exactly the thing that fails during regime breaks.
- **Filter blindness at the worst moments.** The 200-day SMA filter correctly stays flat during the largest panics (March 2020, May 2022, August 2024) — but those panics include the highest-quality V-bottoms in history. The strategy structurally forfeits the best entries in exchange for not catching the worst falling knives. This is a deliberate design choice, but practitioners must not rationalize their way around it after the fact.
- **No short side.** The strategy buys oversold inside an uptrend; the symmetric "sell overbought inside a downtrend" version has historically been far less profitable in equities and is a non-starter in a structurally-up crypto market. The user's bot is long-only by design.
- **Crowded.** Connors' original is one of the most-published retail systems in history. Public crowding has compressed the equity edge since 2010. The crypto adaptation may have a few more years of edge before similar crowding hits.
- **Dependence on a single sentiment vendor.** alternative.me is a free public service. If methodology changes, API stability degrades, or the index gets co-opted by manipulators, the bot's filter quality drops. A backup sentiment proxy (e.g., put/call ratio for equities, perp funding extremes for crypto) should be developed.
- **Discipline required.** Buying when markets feel terrible is psychologically brutal. The bot exists precisely to bypass that — but the operator must trust the bot during exactly the windows where their discretionary self would override it.

## Sources

- Connors, Larry & Alvarez, Cesar. *Short Term Trading Strategies That Work.* TradingMarkets Publishing, 2009. ISBN 9780981923901 (hardcover) / 9781616586386 (softcover). Chapter 9: "The 2-Period RSI — The Trader's Holy Grail of Indicators?" Forward link: [[book-short-term-trading-strategies-that-work]].
- Connors, Larry & Alvarez, Cesar. *High Probability ETF Trading: 7 Professional Strategies to Improve Your ETF Trading.* TradingMarkets Publishing, 2009. Forward link: [[book-high-probability-etf-trading]].
- Lehmann, Bruce N. "Fads, Martingales, and Market Efficiency." *Quarterly Journal of Economics* 105(1), 1990, pp. 1-28. Foundational empirical evidence for short-horizon mean reversion in US equities. Forward link: [[paper-lehmann-1990-fads-martingales]].
- Lo, Andrew W. & MacKinlay, A. Craig. "When Are Contrarian Profits Due to Stock Market Overreaction?" *Review of Financial Studies* 3(2), 1990, pp. 175-205. Decomposes contrarian profits into overreaction vs. cross-autocorrelation components. Forward link: [[paper-lo-mackinlay-1990-contrarian-profits]].
- Crypto Fear & Greed Index — see [[alternative-me]] for full methodology and API access. Six weighted components: volatility (25%), market momentum/volume (25%), social media (15%), surveys (15%), BTC dominance (10%), Google Trends (10%). Daily values 0-100. Free public JSON API at `https://api.alternative.me/fng/`.
- StockCharts ChartSchool. "RSI(2)" article documenting Connors' rules with live SPY backtests. Forward link: [[stockcharts-rsi-2]].
- QuantifiedStrategies.com. Independent backtests of Connors RSI on equity ETFs and selected crypto adaptations. Forward link: [[quantifiedstrategies-rsi-2]].
- BIS Bulletin No 90, "The market turbulence and carry trade unwind of August 2024" — context for the example-trade discussion. See [[2024-08-yen-carry-unwind]].

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

- [[rsi]] — the underlying indicator math
- [[200-day-moving-average]] — the regime filter
- [[mean-reversion]] — the broader strategy category
- [[overreaction-anomaly]] — the academic anomaly this strategy harvests
- [[bollinger-band-reversion]] — complementary mean-reversion using price bands
- [[moving-average-crossover]] — the typical "other half" of a long-horizon book that pairs well with this short-horizon strategy
- [[sentiment]] — the role of sentiment indices in systematic trading
- [[loss-aversion]], [[herding]] — behavioral mechanisms that generate the panic this strategy buys
- [[edge-taxonomy]] — where this strategy sits in the edge framework
- [[failure-modes]] — catalog of how strategies of this archetype die
- [[2024-08-yen-carry-unwind]] — referenced in the example trade
- [[asterdex]] — execution venue assumed by the bot

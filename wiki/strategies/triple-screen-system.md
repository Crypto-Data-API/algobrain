---
title: "Triple Screen Trading System"
type: concept
created: 2026-04-15
updated: 2026-07-19
status: good
tags: [crypto, technical-analysis, trend-following, momentum, indicators, methodology, multi-timeframe]
aliases: ["Triple Screen System", "Triple Screen", "Elder Triple Screen"]
domain: [technical-analysis]
prerequisites: ["[[multi-timeframe-confluence]]", "[[trend-following]]", "[[macd]]"]
difficulty: intermediate
markets: [crypto]
related: ["[[multi-timeframe-confluence]]", "[[trend-following]]", "[[mean-reversion]]", "[[macd]]", "[[stochastic]]", "[[williams-percent-r]]", "[[moving-average-crossover]]", "[[volatility-regime]]", "[[funding-rate]]", "[[open-interest]]", "[[liquidation]]", "[[edge-taxonomy]]", "[[indicators-overview]]"]
---

# Triple Screen Trading System

The **Triple Screen Trading System** is a multi-timeframe *filtering methodology* developed by Dr. Alexander Elder and popularised in his 1993 book *Trading for a Living*. It combines three sequential "screens" — a higher-timeframe trend filter, an intermediate-timeframe oscillator for timing, and a lower-timeframe entry trigger — so that every trade is taken with the larger trend (the "tide"), entered against a short-term counter-move (the "wave"), and triggered precisely (the "ripple"). It is a structured discipline rather than a single indicator, designed to resolve the contradiction that trend and oscillator indicators routinely give opposite signals on the same chart. In crypto's 24/7 market the method is applied to a UTC timeframe cascade (e.g. weekly → daily → 4h, or daily → 4h → 1h) and benefits from an extra crypto-native confluence layer — [[funding-rate|funding]], [[open-interest|OI]], and [[volatility-regime]] — layered onto Elder's original oscillator screen.

## The Three Screens at a Glance

| Screen | Elder's metaphor | Timeframe | Question it answers | Typical tool |
|---|---|---|---|---|
| **1 — Tide** | The market tide | One order higher (e.g. weekly for a daily trader) | *Which direction am I allowed to trade?* | [[macd\|MACD]]-Histogram slope, or 13/26 EMA |
| **2 — Wave** | The wave against the tide | Primary (e.g. daily) | *Is there a counter-trend pullback to enter into?* | Force Index, [[stochastic\|Stochastic]], [[williams-percent-r\|Williams %R]], Elder-Ray |
| **3 — Ripple** | The ripple | Primary, intrabar | *Has the pullback actually turned?* | Trailing buy/sell-stop beyond the prior bar |

The design's insight is the **division of labour**: the trend tool decides *direction* on a slow timeframe where it is reliable, and the oscillator decides *timing* on a faster timeframe where it is useful — so the two never contradict each other on the same chart. This is the concrete application of [[multi-timeframe-confluence]].

## The Theory / Mechanism

The methodology encodes a behavioural discipline that most discretionary traders fail to keep. It does not exploit a structural inefficiency or private information; it enforces two psychologically hard behaviours — (1) only trading in the direction of the dominant trend, and (2) waiting for a pullback rather than chasing. Crypto trends persist longer than most traders expect because of anchoring, reflexive narratives (halving cycles, ETF adoption, sector rotations), and slow information diffusion. Retail traders systematically (a) chase strength after a move is extended, getting poor fills near local tops, and (b) try to pick tops and bottoms against strong trends, repeatedly stopping out. Triple Screen mechanically removes both errors: Screen 1 bans counter-trend trades; Screen 2 forces entry only on a short-term oscillator overshoot (a *discount* inside an uptrend); Screen 3 waits for the turn to confirm. The other side of the trade is the panicked seller in an uptrend pullback (often a liquidated leveraged long) or the euphoric buyer in a downtrend bounce. Because the discipline is uncomfortable, the behaviour does not get arbitraged away.

Read as a methodology, its value is the *filter*, not any single indicator — the system is deliberately indicator-agnostic on Screen 2. Under the null, multi-timeframe filtering adds nothing: pullback entries within a higher-timeframe trend would earn the same expected return as random entries, and match a naive single-timeframe MACD system after costs. The method is only worth using if conditioning entries on (trend agreement + intermediate oscillator extreme) produces better reward-to-risk than the trend signal alone — across instruments and regimes, net of slippage.

## The three screens

**Screen 1 — Market Tide (long-term trend filter).** Pick your primary trading timeframe, then go one order of magnitude higher (trade the daily → set the trend on the weekly; scalp the 1h → trend on the 4h/daily). Apply a trend indicator — Elder uses the slope of the higher-timeframe [[macd|MACD]]-Histogram (or a 13/26 EMA).
- Higher-timeframe trend up → only **long** trades permitted below.
- Down → only **short**.
- Flat/ambiguous → stand aside. (In crypto, add a **BTC overlay**: alt long setups rarely survive a confirmed BTC downtrend.)

**Screen 2 — Market Wave (intermediate oscillator, timing).** Drop to the primary timeframe. Apply an oscillator (Force Index, Stochastic, Williams %R, Elder-Ray).
- In an uptrend, **buy** when the oscillator is oversold (a pullback).
- In a downtrend, **short** when it is overbought (a bounce).
- Crypto confluence: the strongest discounts coincide with [[funding-rate|funding]] flipping negative and elevated [[open-interest|OI]] — leveraged shorts pressing the pullback into support.

**Screen 3 — Entry (the ripple / trigger).** Use a trailing stop-entry for precision.
- Long: buy-stop just above the prior bar's high; it fills only if price turns back up, confirming the pullback is ending. In crypto, buffer the stop *beyond* the likely stop-hunt wick and use a % / [[atr]] fraction, not a fixed tick.
- Short: sell-stop just below the prior bar's low.
- If unfilled, lower (long) or raise (short) the stop each bar while the screens stay aligned.

**Exit / stops.** Initial protective stop below the most recent swing low (long), buffered for crypto wick noise. Elder recommends a money-management stop plus scaling out — take partial profit when the oscillator reaches the opposite extreme, trail the remainder with the trend.

**Sizing.** Elder's "2% rule" — risk a fixed fraction of equity per trade based on the distance to the protective stop. In crypto, keep leverage low; the method's stop-entry math is destroyed by a leveraged liquidation wick.

## Second-screen oscillator choices

Screen 2 is **indicator-agnostic** — any well-behaved oscillator works as long as it cleanly flags counter-trend overshoots. Elder's own preference is the 2-period Force Index.

| Oscillator | Concept page | Signal in an uptrend (buy) | Character |
|---|---|---|---|
| **Force Index (2)** | — | Force Index dips below zero | Elder's favourite; combines price + volume, very responsive |
| **Stochastic** | [[stochastic]] | %K oversold (<20-30) | Smooth, classic; can stick at extremes in strong crypto trends |
| **Williams %R** | [[williams-percent-r]] | %R below -80 | Mirror of stochastic; fast |
| **Elder-Ray** | — | Bear Power turns up from negative | Elder's own bull/bear-power measure |
| **RSI** | [[rsi]] | RSI dips toward oversold | Common substitute; slower than Force Index |

See the [[indicators-overview]] hub for how each oscillator is calculated and its individual failure modes.

## Behaviour by regime

| Regime | Triple Screen behaviour | Why |
|---|---|---|
| **Strong trend** | Best — pullback entries get carried by the dominant move | The trend screen is reliable; pullbacks resolve in the trend's direction |
| **Trend with deep pullbacks** | Good — the system's sweet spot | Screen 2 catches the discount; Screen 3 confirms the turn |
| **Range-bound / choppy** | Worst — repeated whipsaw losses | The trend screen flips, producing false long-then-short bias |
| **Sharp reversal** | Poor on the turn, then re-aligns | The lagging trend filter keeps signalling the old direction until it flips |

The performance distribution is the classic trend-aligned pullback shape: many small losses and scratches in chop, a minority of large winners in sustained trends. As with all behavioural chart edges (see [[edge-taxonomy]]), the realistic expectation is a modest, cost-sensitive edge that depends far more on discipline than on indicator tuning.

## Failure Modes

- **Range-bound / choppy regimes (dominant failure).** The higher-timeframe trend filter flips repeatedly, generating long-then-short whipsaws. Filtering with [[volatility-regime]] (stand aside in choppy/vol-shock regimes) mitigates this.
- **Trend-definition ambiguity.** A flat MACD-Histogram gives no clean signal; discretion creeps in and discipline erodes.
- **Stop-entry slippage (crypto-acute).** In fast crypto markets and liquidation cascades, buy-stops fill far above the prior high — destroying the reward-to-risk math the whole method depends on.
- **Over-optimisation.** Tuning oscillator periods to historical crypto data is curve-fitting; the system is meant to be robust, not optimised.
- **Behavioural leakage.** The entire edge is discipline; a trader who overrides the screens "just this once" forfeits it.
- **Low frequency.** As a discretionary swing method it is naturally slow, so statistical validation and confidence accumulate slowly.

Retirement in practice: reassess if the rolling win rate falls below ~40% while average reward-to-risk drops below ~1.3, if drawdown exceeds ~30% of allocated capital, or after repeated whipsaw clusters from higher-timeframe trend reversals.

## Crypto Application

- **24/7 timeframe cascade.** With no cash close, the screens run on a continuous UTC cascade — weekly → daily → 4h for swing traders, or daily → 4h → 1h for faster styles. Keep the "one order of magnitude" spacing Elder intended.
- **Derivatives as a fourth confluence.** The crypto edge over the original: overlay [[funding-rate|funding]], [[open-interest|OI]], and [[liquidation]] data on Screen 2. A weekly-uptrend, daily-oversold pullback that arrives with negative funding, elevated OI, and a fresh long-liquidation flush is the highest-conviction "discount" the method can produce — max short-pain inside an intact uptrend.
- **BTC regime overlay.** Because alts have high BTC beta, a confirmed BTC downtrend invalidates most alt long setups regardless of the alt's own screens.
- **Volatility-regime gate.** Trade the method's pullback entries out of compressed/normal [[volatility-regime|volatility regimes]]; stand aside in vol-shock regimes where stop-entry slippage and whipsaw spike.
- **Majors vs thin alts.** On BTC/ETH and top perps the stop-entry fills cleanly and capacity is large; on thin alts the buy-stop above the prior high sits exactly where the book empties, so both slippage and stop-hunt risk are far worse.

## Worked Crypto Example

*(Illustrative, not a recorded trade.)* **BTC/USDT.** The **weekly** MACD-Histogram has been rising for three weeks → uptrend, longs only. On the **daily**, the 2-period Force Index turns negative as BTC pulls back ~5% over two sessions toward the rising 50-day, and — the crypto confluence — funding flips negative while OI stays elevated (shorts pressing the dip). A buy-stop is placed just above the prior daily high at **$61,200** with a wick buffer. The next session price turns up and fills at **$61,300**. Protective stop below the swing low (beyond the stop-hunt wick) at **$58,900** (risk ≈ $2,400, ~3.9%). With a $50,000 account risking 2% ($1,000), size ≈ 0.42 BTC. Price resumes the weekly uptrend; half is sold at **$65,000** when the daily Force Index spikes positive, the rest trailed and exited at **$67,500** — a roughly **2.6:1** reward-to-risk on the held portion. The negative-funding/elevated-OI confluence is what upgraded a routine pullback into a high-conviction entry.

## Getting the Data (CryptoDataAPI)

Triple Screen needs OHLCV on two aligned timeframes for the trend and oscillator screens, plus the crypto confluence layer (funding, OI, liquidations) and a volatility-regime gate. See [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]], and [[cryptodataapi-regimes]].

- **OHLCV on both timeframes** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1w&limit=200` (Screen 1) and `interval=1d` (Screens 2-3), live; `GET /api/v1/backtesting/klines` (archive from 2020) to validate the filter across the 2021 bull and 2022 bear.
- **Depth for stop-entry realism** — `GET /api/v1/liquidity/depth/BTC` to estimate slippage at the buy-stop level (exactly where the book thins).
- **Screen-2 confluence** — `GET /api/v1/derivatives/funding-rates?coin=BTC` and `GET /api/v1/derivatives/open-interest?coin=BTC` flag a short-heavy discount; `GET /api/v1/market-intelligence/liquidations` locates the long-liquidation flush the pullback bottoms into.
- **Regime gate** — `GET /api/v1/volatility/regime` to stand aside in vol-shock regimes where whipsaw and slippage spike.

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1w&limit=200"
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [open interest](https://cryptodataapi.com/open-interest) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run all three screens plus the crypto confluence layer:

- **Screen 1 (tide)** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1w&limit=200` for the higher-timeframe MACD-Histogram slope; only trade the permitted direction
- **Screens 2-3 (wave/ripple)** — the same endpoint at `interval=1d` (or `4h`) for the oscillator and the trailing stop-entry bar
- **Confluence** — `GET /api/v1/derivatives/funding-rates?coin=BTC` + `GET /api/v1/derivatives/open-interest?coin=BTC` + `GET /api/v1/market-intelligence/liquidations`: negative funding, elevated OI, and a fresh long-liquidation flush upgrade a routine pullback to the highest-conviction discount
- **Regime gate** — `GET /api/v1/volatility/regime`: stand aside in `vol_shock` (the whipsaw/slippage regime); `GET /api/v1/liquidity/depth/BTC` checks the book at the buy-stop level before sizing
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) validates the filter across the 2021 bull and 2022 bear; pair with `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) for point-in-time regime gating
- **Tips** — apply the BTC regime overlay before any alt setup: one BTC-trend call from the weekly klines invalidates most alt longs in one check

## Related

- [[multi-timeframe-confluence]] — the general principle the system formalises.
- [[trend-following]] — the broader strategy family.
- [[mean-reversion]] — the short-term pullback logic used inside a longer-term trend.
- [[macd]] — the Screen-1 trend indicator (concept page).
- [[stochastic]] / [[williams-percent-r]] — Screen-2 oscillator options.
- [[moving-average-crossover]] — an alternative trend filter for Screen 1.
- [[volatility-regime]] — the crypto regime gate for standing aside.
- [[funding-rate]] / [[open-interest]] / [[liquidation]] — the crypto confluence layer on Screen 2.
- [[edge-taxonomy]] — behavioural-edge classification.
- [[indicators-overview]] — concept hub for the indicators used in each screen.

## Sources

- Alexander Elder, *Trading for a Living* (Wiley, 1993) — original description of the Triple Screen Trading System.
- Alexander Elder, *The New Trading for a Living* (Wiley, 2014) — updated treatment with Force Index and the Impulse System.
- John J. Murphy, *Technical Analysis of the Financial Markets* — multiple-timeframe analysis context.
- Public crypto exchange documentation (Binance, Hyperliquid) — funding, OI, and liquidation mechanics used as the crypto confluence layer on Screen 2.

---
title: "Supertrend Indicator"
type: concept
created: 2026-04-06
updated: 2026-07-14
status: good
domain: [technical-analysis]
prerequisites: ["[[atr]]", "[[trailing-stop]]"]
difficulty: beginner
tags: [trend-following, supertrend, atr, trailing-stop, volatility, indicators, technical-analysis, crypto]
aliases: ["Supertrend", "Supertrend Strategy", "ATR Trailing Stop", "SuperTrend"]
markets: [crypto]
related: ["[[parabolic-sar]]", "[[atr]]", "[[moving-average-crossover]]", "[[ichimoku-cloud]]", "[[trailing-stop]]", "[[volatility]]", "[[bitcoin]]", "[[cryptodataapi]]"]
---

# Supertrend Indicator

The Supertrend is an **[[atr]]-based trend-following overlay** that plots a single line which flips from below price (bullish, green) to above price (bearish, red) as the trend changes. Because the line is anchored to volatility rather than a fixed distance, it widens in turbulent markets and tightens in calm ones, and it can only move *toward* price in the direction of the trend — behaving as a self-tightening [[trailing-stop]]. The **flip** from one side to the other is its buy/sell signal. Its clean one-line, two-color output made it a staple of Indian equity retail trading and, more relevantly here, of [[crypto]] charting, where 24/7 volatility rewards a volatility-adaptive trend tool. It is available on essentially every platform (TradingView, MetaTrader, Python/Pine libraries) and is often described as a modern successor to Wilder's [[parabolic-sar]].

## What It Is

Supertrend answers one question continuously: *are we in an up-leg or a down-leg, and where is the trailing line that would end it?* It is not a momentum oscillator and gives no overbought/oversold reading — it is purely directional. The single line does double duty as **trend indicator** and **stop level**: while price holds above a rising green line, longs stay valid; a close through the line flips the trend and the line jumps to the other side of price.

## Construction and Formula

Supertrend is built from the median price and the [[atr]]:

1. **Median price** (a.k.a. `hl2`) = (High + Low) / 2.
2. **Basic bands** around that median, scaled by ATR:
   - **Basic Upper Band** = hl2 + (Multiplier × ATR)
   - **Basic Lower Band** = hl2 − (Multiplier × ATR)
3. **Final bands** — the basic bands are "ratcheted" so they only move in the trend's favour, using the prior bar's band and close:
   - **Final Upper Band** = basic upper if (basic upper < prior final upper) **or** (prior close > prior final upper); otherwise carry the prior final upper.
   - **Final Lower Band** = basic lower if (basic lower > prior final lower) **or** (prior close < prior final lower); otherwise carry the prior final lower.
   This is the mechanism that lets the line tighten during a trend but never loosen against it.
4. **Supertrend value & trend state:**
   - In an **uptrend**, Supertrend = Final Lower Band (line sits below price). It stays an uptrend until price **closes below** the final lower band.
   - In a **downtrend**, Supertrend = Final Upper Band (line sits above price). It stays a downtrend until price **closes above** the final upper band.
   - A close through the active line **flips** the trend, and the line snaps to the opposite band — the signal event.

The `ATR` term is the only volatility input; most implementations compute it with Wilder's smoothing (RMA), though SMA/EMA-ATR variants exist and shift the line slightly.

## How to Read It

- **Green line below price** = uptrend; the line is your trailing stop and rises over time.
- **Red line above price** = downtrend; the line falls over time.
- **Flip (line crosses to the other side of price)** = trend-change signal and entry/exit trigger.
- **Distance from price to line** = current volatility-scaled risk; wide gap = high volatility / loose stop, narrow gap = tightening trend.
- **Line slope** = trend persistence; a steadily rising line with price riding above it is a healthy trend.

## Variants

- **Standard Supertrend** — the (ATR period, multiplier) form above; default 10 and 3.0.
- **Multi-timeframe (MTF) Supertrend** — read a higher-timeframe Supertrend as a directional gate for a lower-timeframe one (e.g., daily green required to take 1h longs).
- **Multiple / stacked Supertrends** — plot two or three Supertrends with different parameters (e.g., (10,1), (11,2), (12,3)); require agreement for confluence, a common crypto configuration.
- **Adaptive Supertrend** — vary the multiplier with a [[volatility]] regime or a volatility ratio so the line loosens in expansions and tightens in compressions.
- **Heikin-Ashi-sourced Supertrend** — compute it on [[heikin-ashi]] candles for smoother (but more lagging and more repaint-prone) flips.
- **ATR-smoothing variants** — RMA vs. EMA vs. SMA ATR change sensitivity modestly.

## Signals It Generates

1. **Long entry:** Supertrend flips red→green (line moves below price); typically taken at the close that triggers the flip.
2. **Short entry:** Supertrend flips green→red (line moves above price).
3. **Exit (flip):** the primary exit — close the trade when the line flips to the opposite color.
4. **Trailing stop:** trail the stop at the Supertrend value each period, whether or not you use the flip for exit.
5. **Trend gate:** use a higher-timeframe Supertrend's color to permit or block lower-timeframe entries.
6. **Fixed target (optional):** take profit at a set multiple of the entry-to-line distance (that distance is a natural, volatility-scaled risk unit).

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| ATR Period | 10 | Lookback for the [[atr]] calculation |
| Multiplier | 3.0 | ATR multiples from median price to the bands |

- **Higher multiplier** (e.g., 4.0): fewer signals, wider stops, holds trends longer, tolerates deeper pullbacks — but gives back more at the top and sits through bigger drawdowns.
- **Lower multiplier** (e.g., 1.5–2.0): more signals, tighter stops, earlier entries/exits — and many more whipsaws in chop.
- **Shorter ATR period**: more responsive, noisier. **Longer**: smoother, slower.
- A popular fast-crypto configuration is (7, 2.0) on lower timeframes; there is no universally optimal setting — it must be tuned per asset and regime, which is itself a curve-fitting hazard.

## Supertrend vs. Parabolic SAR

Both are always-directional trailing-stop indicators, and both flip trend on a price cross — but they differ in a way that matters for crypto:

| Aspect | Supertrend | [[parabolic-sar]] |
|--------|-----------|-------------------|
| Volatility input | Yes — [[atr]]-scaled bands | None — fixed acceleration factor |
| Adapts stop width to volatility | Automatically | No (same AF regardless of regime) |
| Visual | Continuous line | Discrete dots |
| Trigger basis | Candle close vs. band | Price touch of the dot |
| Whipsaw in chop | High | Very high |
| Crypto suitability | Better (auto-scales to volatility) | Needs manual tuning + filters |

Because Supertrend scales its stop to [[volatility]] and keys on the **close**, it tends to survive crypto's liquidation wicks better than SAR, which can be picked off intrabar by a single spike. Many crypto traders run both and only act when they agree.

## Confluence and Combinations

- **[[parabolic-sar]]** — a second volatility-based trailing stop; agreement between the two raises confidence, disagreement warns of chop.
- **[[moving-average-crossover]] / trend filter** — take Supertrend flips only in the direction of a longer MA or a higher-timeframe trend to cut counter-trend signals.
- **[[atr]]** — already inside the calculation, but an explicit ATR read helps judge whether the current stop distance is sane for position sizing.
- **[[volume]] / momentum ([[rsi]], [[macd]])** — confirm a flip with rising volume or a momentum shift to filter false flips in ranges.
- **[[ichimoku-cloud]]** — a richer trend framework; Supertrend flips that agree with cloud direction are stronger.
- **[[market-regime]] gate** — only trust flips when a regime read says "trending"; mute Supertrend in range regimes.

## Strengths

- **Extremely simple** — one line, two colors, no interpretation ambiguity.
- **Volatility-adaptive trailing stop** built in via [[atr]] — stops widen and tighten with the market automatically.
- **Works on all timeframes**, from sub-minute scalps to weekly position trades.
- **Low computational cost** — trivial to code in Pine, Python, or any backtester; easy to run across hundreds of crypto pairs.
- **Multi-timeframe stacking** meaningfully improves signal quality.
- **No repainting of closed bars** (see below) — a genuine advantage over some other "clean" chart types.

## Documented Weaknesses

- **Whipsaw-prone in ranges.** Like every trend follower, Supertrend flips repeatedly in sideways markets, producing a run of small losses — its dominant failure mode.
- **Lag / late entries.** By the time price closes through the band to flip the line, a meaningful portion of the move has already happened; you buy after the turn and exit after the top.
- **Repainting on the *forming* candle.** Supertrend uses the bar's close, so the current, still-open bar's line and color can move until the candle closes. Values on **closed** candles do **not** repaint, but intrabar signals do — bots that act on the live bar will over-perform in a naive backtest. Always evaluate flips on closed bars. Heikin-Ashi-sourced Supertrend repaints more.
- **Parameter dependence.** The (10, 3) default is not universally good; tuning per instrument invites curve-fitting that fails out-of-sample.
- **No momentum or volume component** — it is purely price/volatility; a flip carries no information about conviction.
- **Wide initial risk after a flip.** The line starts far from price right after a flip, so the first stop is often wide — costly if the new trend fails quickly.
- **False confidence.** Its clean look tempts beginners to trade every flip without regime or context.

## Typical Behaviour

As a pure trend-follower, Supertrend has a characteristic return shape rather than a fixed performance number: a **low-to-moderate hit rate offset by asymmetric winners** — most flips in a range are small losses, while the minority that catch a real trend leg pay for them and more. Commonly cited illustrative figures put a bare, unfiltered Supertrend around a 35–45% win rate that improves toward ~50%+ when gated by a higher-timeframe trend filter; profit factor is highly regime-dependent, strong in clean trends and negative in extended chop. These numbers are descriptive of the indicator's *shape*, not a guaranteed edge — actual results depend entirely on the asset, timeframe, parameters, costs, and above all the trend/range mix of the period. The practical takeaway: Supertrend earns its keep by catching and holding big directional moves, so its value is destroyed if it is traded through ranges without a regime filter.

## Common Mistakes

- **Trading every flip.** Taking signals without a regime or higher-timeframe filter, so chop bleeds capital between the occasional good trend.
- **Acting on the forming bar.** Reacting to the live, still-updating line before the candle closes; closed-bar flips only.
- **Over-tuning parameters.** Optimizing (period, multiplier) to past data until it curve-fits; the (10, 3) default exists precisely to resist this.
- **Ignoring the wide first stop.** The line starts far from price right after a flip; sizing off that wide distance without adjusting risk leads to oversized losses if the new trend fails.
- **Assuming no repainting anywhere.** Closed bars are fixed, but the live bar and Heikin-Ashi-sourced Supertrend do move — naive live-bar backtests overstate results.
- **No volume/momentum context.** Treating a flip as conviction when Supertrend contains no such information.

## Range / Whipsaw Scenario

The documented weakness made concrete: BTC ranges in a ~$4,000 band. On the 4h chart the Supertrend line flips green→red→green every few candles as each push stalls at the band edge. Each flip enters near an extreme and reverses shortly after — a run of six or seven small losses in a week, none individually large but collectively a steady drawdown. Nothing about the parameters fixes this; the tool is doing exactly what a trend-follower does in a trendless market. The remedy is a **regime gate** — require a higher-timeframe Supertrend (or a [[market-regime]] read) to agree, and simply stop taking flips while price is boxed in a range.

## Application to Crypto Charts

- **Volatility-adaptive by construction** — this is Supertrend's best fit for crypto, where [[volatility]] swings from dead-calm consolidations to violent expansions; the ATR term auto-scales the stop so the same multiplier stays usable across regimes.
- **24/7 tape.** No sessions or gaps means the flip is well-defined at any time, but you must fix a consistent candle close (e.g., UTC daily/hourly) since "the close" is otherwise arbitrary.
- **Perp liquidation wicks.** On [[perpetual-futures]], liquidation cascades can spike price through the line intrabar and then revert; because Supertrend keys on the **close**, using closed-candle flips avoids many of these fakeouts — a real practical benefit.
- **Whipsaw risk is higher.** Crypto ranges are choppy and frequent; pair Supertrend with a regime/higher-timeframe filter and consider a higher multiplier on noisy alts.
- **Cross-asset scanning.** Its low cost lets you run Supertrend across the whole liquid universe to rank which coins have flipped bullish — a common crypto screening use.
- **Funding-aware framing.** In strong trends, extreme [[funding-rate]] readings can flag that a Supertrend-confirmed move is crowded and vulnerable to a sharp counter-flip.

## Worked Crypto Example

**Asset:** BTC/USDT, 4-hour chart, Supertrend (10, 3), signals on closed candles.

1. BTC is trending down; the Supertrend line is **red** at ~$66,800, above price near $65,500.
2. A strong 4h candle **closes at $67,200**, above the red line. Supertrend **flips green**, snapping to ~$64,900 below price. Enter long at ~$67,200; stop = Supertrend line at ~$64,900. Risk ≈ $2,300.
3. The daily Supertrend is also green (MTF gate agrees), so the long is taken with trend.
4. BTC rallies over several days; the green line trails up: $65,600 → $66,900 → $68,400 → $70,100, each period tightening the stop.
5. BTC stalls near $73,500 and pulls back. On a 4h close at ~$70,000 the line (now ~$70,100) is breached — Supertrend **flips red**. Exit at ~$70,000.
6. **Result:** entry ~$67,200, exit ~$70,000, ≈ +$2,800/BTC (+4.2%) against ≈ $2,300 initial risk (~1.2:1). The volatility-scaled trail held through two sharp intra-trend dips (each a liquidation wick that did not *close* through the line); the trade-off was a late entry (~$1,700 above the actual low) and a give-back of ~$3,500 from the high — the built-in lag on both ends.

## Reading Across Timeframes

Supertrend's biggest quality improvement comes from multi-timeframe alignment — its single most documented enhancement:

- **Daily (or weekly)** — the regime gate. Only take longs when the daily Supertrend is green, shorts when red. This alone lifts a bare Supertrend from a coin-flip toward a workable trend follower.
- **4-hour** — the swing-signal layer where flips are actionable.
- **1-hour / lower** — the timing/scalp layer; flips here are noisy and should be filtered by the 4h and daily direction.
- **Stacked-parameter read** — instead of (or alongside) multiple timeframes, plot two–three Supertrends with different multipliers on one chart and require agreement; a common crypto configuration that trades responsiveness for fewer false flips.

The rule of thumb: **trade the lower timeframe, filter with the higher.** Never take a flip that fights the daily.

## Pre-Trade Checklist

1. Is the **higher-timeframe** Supertrend the same color as my intended direction? (regime gate)
2. Has the signal-timeframe candle **closed** with the flip? (no live-bar action — it can repaint intrabar)
3. Am I in a **trend** regime, not a range? (avoid the whipsaw scenario)
4. Is the **entry-to-line distance** (my stop) sane for sizing given current volatility?
5. Do parameters reflect the asset/timeframe without being **over-tuned** to history?
6. Is there **confluence** (volume, momentum, ADX, or a second Supertrend) backing the flip?

## Getting the Data (CryptoDataAPI)

Supertrend is computed from OHLCV (median price + ATR) — pull klines and calculate the bands yourself on closed candles. CryptoDataAPI also serves related computed indicator states you can use as filters.

**Live / recent candles:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=1000` — Binance spot OHLCV for computing Supertrend.
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=4h&limit=1000` — Hyperliquid perp OHLCV.

**Related computed indicator states (filters):**
- `GET /api/v1/indicators/technical` — price-structure state (SMA/BB/RSI) across assets.
- `GET /api/v1/indicators/signum-rgg` — ADX(14)+DMI RED/GREY/GREEN trend-strength state.

**Historical archive (backtesting):**
- `GET /api/v1/backtesting/klines` — full OHLCV archive (Parquet since 2020) for backtesting Supertrend flips on closed bars.

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=1000"
```

Auth: `X-API-Key` header. Endpoint catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]], [[cryptodataapi-indicators]], [[cryptodataapi-hyperliquid]].

## Key Takeaways

- Supertrend is an **ATR-scaled trend line** that flips sides on a close and doubles as a volatility-adaptive [[trailing-stop]].
- The **flip** is the buy/sell signal; the line's distance from price is a built-in, volatility-scaled stop.
- Default parameters are **(ATR 10, multiplier 3)** — higher multiplier holds trends longer, lower one is more sensitive and whipsaw-prone.
- **Closed bars do not repaint**, but the live bar and Heikin-Ashi-sourced Supertrend do — act on closed candles.
- It **lags** and **whipsaws in ranges**; a **higher-timeframe / multi-Supertrend filter** is its most important enhancement.
- Better crypto fit than [[parabolic-sar]] because it **auto-scales to volatility** and, keying on the close, resists liquidation-wick fakeouts.
- Behaviour is **low hit-rate, asymmetric winners** — value comes from catching and holding big trend legs, destroyed if traded through chop.

## Related

- [[parabolic-sar]] — Wilder's classic trailing stop; Supertrend is often seen as its modern successor
- [[atr]] — the volatility measure at the core of the calculation
- [[trailing-stop]] — the general concept Supertrend implements
- [[moving-average-crossover]] — another beginner trend signal; two lines instead of one
- [[ichimoku-cloud]] — a richer, more complex trend framework
- [[volatility]] — the regime input that governs Supertrend's stop width
- [[bitcoin]] — primary crypto instrument for Supertrend trend-reading

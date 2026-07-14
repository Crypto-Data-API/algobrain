---
title: "Renko Charts"
type: concept
created: 2026-04-06
updated: 2026-07-14
status: good
domain: [technical-analysis]
prerequisites: ["[[support-and-resistance]]", "[[atr]]"]
difficulty: beginner
tags: [renko, renko-charts, brick-charts, trend-following, noise-filter, atr-renko, time-independent, indicators, technical-analysis, crypto]
aliases: ["Renko Charts", "Renko Bricks", "Brick Charts", "Renko Strategy"]
markets: [crypto]
related: ["[[point-and-figure]]", "[[heikin-ashi]]", "[[supertrend]]", "[[moving-average-crossover]]", "[[parabolic-sar]]", "[[atr]]", "[[support-and-resistance]]", "[[bitcoin]]"]
---

# Renko Charts

Renko is a **price-driven, time-independent charting method** that draws the market as a staircase of fixed-size "bricks," adding a new brick only when price moves a set amount in one direction. The name comes from the Japanese *renga* (brick). Because a brick appears purely as a function of price movement — never on a clock — Renko strips out consolidation, minor fluctuations, and the whipsaw noise that clutters time-based candles, leaving an unusually clean picture of trend. A **brick color change** is the core signal: a run of green (up) bricks followed by a red (down) brick flags a possible reversal. In crypto, where 24/7 volatility fills time-based charts with noise, Renko's brick abstraction is appealing — but the same construction guarantees lag, can *repaint* on some implementations, and hides the volume and timing context that other methods rely on.

## What It Is

On a candlestick chart, every period produces a bar whether price moved or not; ranges therefore fill the screen with small, alternating candles. Renko discards time entirely and asks a single question repeatedly: *has price moved one full brick size beyond the last brick's close?* If yes, draw a brick; if not, draw nothing. A brick may represent five minutes of a fast move or two days of grinding — the chart does not care. The output is a diagonal staircase of uniform blocks: unbroken diagonals in trends, and a "brick wall" of alternating single bricks in ranges.

This makes Renko a **trend-clarity tool**. It answers "which way, and how persistently, is price moving in price-units?" far better than it answers "when" or "how much volume."

## Construction and Formula

Renko has two construction inputs: the **brick size** and the **reversal amount** (in bricks).

1. **Brick size** — the price distance one brick represents. This is the single most important choice.
   - **Fixed (traditional):** a static value — e.g., $500 for BTC, $20 for ETH, a fixed number of ticks. Simple and stable, but does not adapt as an asset's price or volatility changes (a $500 brick is huge for BTC at $20k and tiny at $100k).
   - **ATR-based:** set the brick size to the [[atr]] (commonly 14-period) of a chosen timeframe. Bricks widen automatically when [[volatility]] rises and tighten when it falls — the standard choice for crypto because BTC/alt volatility swings enormously.
   - **Percentage-based:** brick = a fixed % of price (e.g., 1%), keeping brick "weight" constant as price scales across orders of magnitude — well suited to assets that 10x.

2. **Reversal amount** — how far price must move *against* the current direction to start a brick in the opposite color. The classic Renko uses a **1-brick body but requires a full reversal of the brick size to flip**; many platforms implement a **2-brick reversal** (price must move two brick sizes the other way before a red brick appears after greens). The larger the reversal requirement, the more counter-moves are filtered and the more lag is added.

3. **Plotting rules** — starting from a reference close, each time price advances one brick size, a same-color brick is stacked diagonally up (or down). Bricks are **uniform blocks with no wicks and no gaps**; they connect corner-to-corner, producing the signature staircase. Only *completed* brick moves are drawn.

Because bricks depend only on close-to-brick distance, the same market can produce different Renko charts depending on the brick size, the reversal rule, and — critically — the **price source and anchor** the platform starts from.

## How to Read It

- **Trend:** an unbroken diagonal run of same-color bricks. Five green bricks in a row = a firm uptrend; five red = a firm downtrend. Longer diagonals = stronger, more persistent trends.
- **Reversal:** the first opposite-color brick after a run. The staircase changes direction.
- **Range / chop:** frequent single-brick color alternation — a "brick wall" that stays roughly horizontal. This is the pattern to avoid trading.
- **Support and resistance:** horizontal price levels where brick color changes repeatedly cluster mark meaningful [[support-and-resistance]] — often cleaner than on candlesticks because minor noise is removed.
- **Brick counts as measured moves:** the number of consecutive bricks gives a rough sense of trend extent in price-units, useful for projecting targets.

## Variants

- **Traditional (fixed-brick) Renko** — static brick size; the original form.
- **ATR Renko** — dynamic brick size from [[atr]]; the crypto default. Note that recomputing ATR changes historical bricks, so ATR Renko **repaints history** when new bars arrive — a real backtesting hazard (see Weaknesses).
- **Percentage Renko** — brick = % of price; scale-invariant, good for assets spanning large price ranges.
- **Median / range Renko and "Better Renko"** — variants that wick bricks or record the high/low touched, restoring a little of the intrabar information Renko normally discards.
- **Renko + Heikin-Ashi hybrids** — some platforms color or average bricks HA-style for extra smoothing.

## Renko vs. Point & Figure vs. Candlesticks

| Aspect | Candlesticks | Renko | [[point-and-figure]] |
|--------|-------------|-------|----------------------|
| Axis | Time | Price (bricks) | Price (X/O columns) |
| New mark appears when | Each period | Price moves 1 brick | Price moves 1 box |
| Wicks / intrabar | Full | None | None |
| Volume shown | Yes | No | No |
| Reversal filter | None inherent | Reversal amount (1–2 bricks) | Reversal amount (e.g., 3 boxes) |
| Signal | Patterns | Brick color change | Column breakout |
| Repaint risk | None | Forming brick; ATR bricks redraw history | Forming column |

Renko and P&F share the same philosophy — plot price, not time — but Renko produces a fixed-height staircase while P&F records directional columns and offers built-in count targets. Both discard volume and timing.

## Signals It Generates

1. **Brick color change (primary):** go long on the first green brick after reds; go short on the first red brick after greens.
2. **Two-brick confirmation:** wait for two consecutive new-color bricks before acting — fewer false flips, later entry.
3. **Trend hold:** stay in the position while bricks keep the same color; Renko's clean staircase makes "let it run" easy to follow.
4. **Trailing stop:** ratchet a stop one brick behind the most recent brick as the staircase advances.
5. **Range avoidance:** alternating single bricks are an explicit "do not trade this" signal — arguably as valuable as the entry signals.

Signals are typically read on **brick close**, and the practical stop unit is one (or two) brick sizes — a naturally volatility-scaled risk when using ATR bricks.

## Parameter Choices

- **Brick size** dominates everything. Too small → the chart fills with noise bricks and whipsaws; too large → few bricks, huge stops, and trades signalled far too late. There is no universally correct value; it is the main thing to calibrate per asset and regime.
- **Reversal amount** (1 vs. 2+ bricks) trades responsiveness against false-signal filtering.
- **ATR length** (for ATR Renko) controls how quickly brick size adapts — shorter reacts fast but jitters; longer is stable but slow.
- **Price source** — close-based vs. high/low ("wick") based Renko change how aggressively reversals register.

## Confluence and Combinations

- **[[moving-average-crossover]] on the Renko series** — a short MA (e.g., 10) overlaid on bricks; take longs only when bricks are above it. Filters counter-trend flips.
- **[[supertrend]]** — align a brick color change with a Supertrend flip on the same Renko chart for higher-confidence entries.
- **[[parabolic-sar]]** — an alternate brick-by-brick trailing stop.
- **Momentum ([[rsi]]/[[macd]])** — confirm that a color change coincides with a momentum shift, not a dead-cat brick in a range.
- **Time-based chart cross-check** — because Renko hides time and volume, glance at the standard chart to confirm a breakout brick came on real [[volume]] and not a thin-liquidity wick.

## Automation and Backtesting Notes

Renko is popular for algorithmic crypto bots precisely because the brick series is discrete and easy to code — a color change is a single boolean event. That same convenience hides the field's most common landmine:

- **Build bricks from closed candles only.** Iterate the OHLCV series bar by bar and emit a brick when the close crosses a boundary; never use an intrabar or still-forming value.
- **Freeze the brick size for the whole backtest** (or recompute ATR only from *past* bars, point-in-time). Letting a full-history ATR set the brick size leaks the future and inflates results — the repainting trap in code form.
- **Model costs on brick events, not bricks.** Several bricks can print from one fast candle without a tradeable fill at each level; assuming a fill at every brick overstates fills and understates slippage.
- **Validate against a candlestick backtest** of the same logic; large divergence usually signals a look-ahead bug in the Renko construction.

## Strengths

- **Removes time-based noise**, making trends and ranges visually unambiguous — the cleanest trend read of the common chart types.
- **Simple, objective signals** — a color change is binary; no candlestick-pattern interpretation required.
- **Built-in whipsaw filter** via the reversal requirement — minor counter-moves smaller than the brick/reversal size never appear.
- **ATR bricks auto-scale to [[volatility]]**, valuable in crypto where regimes shift from dead calm to violent within days.
- **Natural, volatility-scaled risk unit** — one brick = one stop increment.
- Beginner-friendly: no need to read divergences, wicks, or complex indicator stacks.

## Documented Weaknesses

- **Lag by design.** A reversal is only acknowledged after price has already moved a full reversal amount against the trend; you enter and exit late and forfeit the turn.
- **Repainting — the crucial crypto caveat.** The *forming* brick is provisional until the brick-size move completes, and, more seriously, **ATR/percentage Renko recomputes brick sizes as new data arrives, which can redraw historical bricks.** Naive backtests read these hindsight-adjusted bricks and produce wildly optimistic results. Always backtest on fixed-brick Renko or on bricks locked at bar close, and never trust live-forming bricks.
- **Brick-size sensitivity.** Performance swings dramatically with the brick size; it is easy to curve-fit a value that looks great in-sample and fails live.
- **No volume, no timing, no wicks.** Renko discards [[volume]], time, and intrabar extremes — so it is blind to exhaustion volume, session context, and the depth of wicks that liquidation cascades produce.
- **Whipsaw in ranges.** The "brick wall" of alternating bricks generates repeated small losses if traded — Renko does not escape the trend-follower's core weakness.
- **False sense of certainty.** The smooth staircase can make a fundamentally choppy market look decisively trending.

## Common Mistakes

- **Backtesting on ATR/percentage bricks naively.** The single biggest error: those brick sizes are recomputed as data arrives, redrawing historical bricks, so a hindsight-perfect chart flatters any strategy. Backtest on **fixed** bricks or bricks locked at bar close.
- **Acting on the forming brick.** Treating a partially built brick as complete; only completed bricks are real signals.
- **Over-tuning brick size.** Optimizing brick size to past data until it curve-fits, then watching it fail live.
- **Trading the brick wall.** Taking every color flip during a range's alternating single bricks — a guaranteed stream of small losses.
- **Ignoring volume and liquidity.** A breakout burst of bricks driven by a thin-book liquidation wick is not the same as one on real volume; Renko cannot tell you which, so cross-check.
- **Assuming platform parity.** Different platforms anchor and reverse bricks differently; two "Renko charts" of the same asset can disagree.

## Choosing a Brick Size

Brick size is the whole game. Practical guidance:

- **Percentage or ATR bricks for crypto** so the chart stays usable as price scales across orders of magnitude and volatility shifts.
- **Larger bricks** for higher-timeframe/position trading — fewer, more meaningful bricks, wider stops, less noise.
- **Smaller bricks** for intraday — more responsive but noisier and more whipsaw-prone.
- **Sanity check:** the brick size (your stop unit) should be a sane fraction of the move you intend to capture — if one brick is 30% of your target, the method is too coarse for that trade.

## Range / Whipsaw Scenario

The documented weakness made concrete: ETH chops in a ~$150 band with ATR bricks of ~$80. Price repeatedly moves ~two bricks up, triggering a green-brick long, then ~two bricks down, stopping out and triggering a red-brick short — which then reverses. Each round trip is a ~$160 (two-brick) loss plus costs. The "clean" staircase looks like alternating single bricks — the explicit range warning. The remedy is to require a trend filter (a rising MA on the brick series, or a higher-timeframe trend/[[market-regime]] read) and to sit out until a multi-brick diagonal establishes direction.

## Application to Crypto Charts

- **24/7 volatility → noisy time charts.** Crypto never closes, so candlestick charts accumulate continuous noise; Renko's time-independence is a genuine advantage for reading BTC/ETH trend without session gaps.
- **ATR or percentage bricks are near-mandatory.** Because crypto prices span orders of magnitude and volatility regimes flip fast, a fixed brick decays quickly; ATR- or percentage-sized bricks keep the chart usable — while introducing the repainting risk above.
- **Liquidation wicks.** Sharp [[liquidations]]-driven spikes on [[perpetual-futures]] can slam through several brick sizes in seconds, printing a burst of bricks — sometimes a real signal, sometimes a wick that instantly reverses. Cross-check with volume/time.
- **Altcoin caution.** Thin altcoin books make brick sizing unstable; small, illiquid moves can trip bricks that mean nothing.
- **Backtesting hygiene.** Given crypto's popularity for automated Renko bots, the repainting trap is especially dangerous here — validate on fixed bricks and closed-bar data via the archive.

## Worked Crypto Example

**Asset:** ETH/USDT, ATR Renko (14-period ATR ≈ $80, so brick size ≈ $80), 2-brick reversal, evaluated on closed bricks.

1. ETH has been declining: 7 consecutive red bricks from ~$3,200 down to ~$2,640.
2. Price reverses by two brick sizes (~$160) and a **green brick** completes at ~$2,800 — first color change.
3. A **second green brick** completes at ~$2,880, satisfying two-brick confirmation. The 10-period MA overlaid on the Renko series sits at ~$2,850; bricks are now above it, so the trend filter agrees.
4. Enter long at ~$2,880. Stop one brick below the reversal, ~$2,720 (≈ $160 = one brick of risk, volatility-scaled by ATR).
5. ETH trends up, stacking green bricks: $2,960, $3,040, $3,120, $3,200, $3,280, $3,360. The trailing stop ratchets one brick behind the latest brick.
6. A **red brick** completes at ~$3,280, hitting the trailing stop and closing the position.
7. **Result:** entry ~$2,880, exit ~$3,280, ≈ +$400/ETH (+13.9%) against ≈ $160 risk (~2.5:1). The two-brick reversal kept the trader out of two mid-trend single-brick counter-moves that would have shaken out a tighter candlestick stop — but note the entry came a full two bricks after the actual bottom (the lag cost).

## Reading Across Brick Sizes

Renko has no time axis, so its "multi-timeframe" analogue is **multi-brick-size** analysis:

- **Large bricks** (e.g., 2–3% of price, or a long-ATR value) — the regime/structure layer. A long diagonal of large bricks confirms a major trend; use it as the directional gate.
- **Medium bricks** (~1% / mid-ATR) — the swing-signal layer where color changes are actionable.
- **Small bricks** (<0.5%) — the timing layer, but noisy; useful only to refine entries within a trend confirmed by larger bricks, never as a standalone signal.
- Aligning two brick sizes — a small-brick flip in the direction of the large-brick trend — is the Renko equivalent of higher-timeframe confirmation and filters most range whipsaws.

Because ATR/percentage bricks repaint history, do this analysis and any backtest on **fixed** bricks or bricks locked at bar close.

## Pre-Trade Checklist

1. Is the **larger-brick-size** trend (a clear diagonal) aligned with my trade direction? (regime gate)
2. Has a **completed** brick — not a forming one — produced the color change / confirmation I need?
3. Is this a diagonal staircase, not the alternating **brick wall** of a range?
4. Is my brick size a sane fraction of the target (stop = 1–2 bricks)?
5. Did the breakout brick come on real **volume/liquidity**, or a thin-book wick? (cross-check the time chart)
6. Am I trading a **liquid** asset where brick sizing is stable?

## Getting the Data (CryptoDataAPI)

Renko is built entirely from OHLCV closes — pull klines and construct bricks yourself. For honest results, size fixed bricks or lock brick size at bar close, and build over the historical archive rather than live-forming bars.

**Live / recent candles:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1h&limit=1000` — Binance spot OHLCV.
- `GET /api/v1/hyperliquid/candles?coin=ETH&interval=1h&limit=1000` — Hyperliquid perp OHLCV.

**Historical archive (backtesting):**
- `GET /api/v1/backtesting/klines` — full OHLCV archive (Parquet since 2020) for constructing repaint-safe Renko series across history.

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ETHUSDT&interval=1h&limit=1000"
```

Auth: `X-API-Key` header. Endpoint catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]], [[cryptodataapi-hyperliquid]].

## Key Takeaways

- Renko plots **price, not time** — a fixed-size brick appears only when price moves the brick amount, filtering consolidation and noise.
- The **brick color change** is the core signal; a diagonal staircase = trend, an alternating brick wall = range (do not trade).
- **Brick size is the entire game** — use percentage/ATR sizing for crypto's wide price and volatility ranges.
- **Repainting is the critical trap:** ATR/percentage bricks redraw history, so backtest on fixed bricks / closed bars only.
- It **lags** by the reversal amount and **whipsaws** in ranges; discards volume, time, and wicks.
- Crypto fit is strong for trend-reading (no session gaps) but liquidation wicks and thin alt books can trip false bricks — cross-check volume.
- Natural, volatility-scaled risk unit: stop = one to two bricks.

## Related

- [[point-and-figure]] — the other classic time-independent chart; uses X/O columns instead of bricks
- [[heikin-ashi]] — noise-smoothing candles that keep the time axis, unlike Renko
- [[supertrend]] — ATR trend overlay that pairs well as a Renko brick-flip confirmer
- [[moving-average-crossover]] — simple trend filter for the Renko brick series
- [[parabolic-sar]] — alternative brick-by-brick trailing stop
- [[atr]] — the volatility measure behind ATR-sized bricks
- [[support-and-resistance]] — brick color-change clusters mark clean horizontal levels
- [[bitcoin]] — primary crypto instrument for Renko trend-reading

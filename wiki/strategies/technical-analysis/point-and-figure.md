---
title: "Point and Figure Charts"
type: concept
created: 2026-04-06
updated: 2026-07-19
status: good
domain: [technical-analysis]
prerequisites: ["[[support-and-resistance]]"]
difficulty: intermediate
tags: [point-and-figure, pnf, x-columns, o-columns, box-reversal, vertical-count, time-independent, noise-free, technical-analysis, crypto]
aliases: ["Point and Figure", "P&F Charting", "P&F Trading", "PnF", "Point & Figure"]
markets: [crypto]
related: ["[[renko-trading]]", "[[support-and-resistance]]", "[[darvas-box]]", "[[heikin-ashi]]", "[[donchian-channel-breakout]]", "[[bitcoin]]"]
---

# Point and Figure Charts

Point and Figure (P&F) is one of the oldest charting methods in [[technical-analysis]], pre-dating bar and candlestick charts to the late 1800s. Like [[renko-trading]] it is **time-independent**: it records only meaningful price movement, ignoring the clock entirely. Rising prices are plotted as columns of **X's**, falling prices as columns of **O's**. A new X (or O) is added each time price moves one **box size**; a new column begins only when price reverses by a set multiple of the box (classically the **3-box reversal**). This construction filters out minor fluctuations and renders the supply/demand balance as clean, objective breakout signals — the **Double Top/Bottom** and **Triple Top/Bottom** — while the **Vertical** and **Horizontal Count** methods project explicit price targets. For crypto's noisy 24/7 tape, P&F offers a disciplined, rule-based way to see structural breakouts and long-term [[support-and-resistance]] without time-axis clutter.

## What It Is

A P&F chart abstracts price into a grid. Movement in the trend direction extends the current column by one symbol per box; movement against the trend does nothing until it is large enough (the reversal threshold) to justify a new column. The chart therefore compresses long consolidations into a few symbols and stretches persistent trends into tall columns — the opposite of a time chart, which gives equal width to boring and important periods alike.

Because only price crossing box boundaries matters, P&F is inherently a **noise filter and structure detector**. It excels at answering "has a genuine breakout occurred, and by how much is the market being demanded or supplied?" It says nothing about *when* or with what *volume*.

## Construction and Formula

P&F has two construction inputs: the **box size** and the **reversal amount**.

1. **Box size** — the price increment one X or O represents. Determines sensitivity. Common schemes:
   - **Fixed:** a static value (e.g., $1,000 per box for BTC).
   - **Percentage:** box = a fixed % of price (e.g., 1%), keeping box "weight" constant as price scales — well suited to assets that move across orders of magnitude, as crypto does.
   - **ATR/traditional scaled:** classic equity P&F scaled box size by price band; the percentage method is the modern scale-invariant equivalent.

2. **Reversal amount** — how many boxes price must move *against* the current column to start a new, opposite column. The standard is the **3-box reversal**; smaller (1-box) reversals are more sensitive and noisier, larger reversals filter more.

3. **Plotting rules:**
   - In a rising (X) column, each time price advances one full box, add an X on top. Sideways or small down-moves are ignored.
   - When price falls by *reversal × box size* (e.g., 3 boxes), move one column right and plot O's **downward** from one box below the top X.
   - Continue plotting O's while price falls by whole boxes; reverse back to X's when price rises by the reversal amount.
   - A key convention: **a column never contains both X's and O's**, and the first plot in a new column starts one box off the prior column's extreme.

The result is alternating columns of X's and O's whose highs and lows define objective breakout levels.

A worked micro-illustration of the mechanics: with a $1,000 box and 3-box reversal on BTC, an X column stacking $65k → $66k → $67k → $68k continues adding X's while price makes higher $1,000 steps; a drop to $65k (three boxes down from $68k) triggers a new O column plotted from $67k down to $65k; a subsequent rise back to $68k (three boxes up) starts a fresh X column — and if that X column then prints $69k, one box above the prior $68k X high, a **Double Top Breakout** buy signal fires. Nothing in between those thresholds is recorded, which is exactly how the noise is stripped.

## How to Read It

Signals are pattern-based and unambiguous — price either exceeds a prior column's extreme or it does not.

- **Double Top Breakout (bullish):** the current X column rises **one box above the top of the previous X column**. The basic buy signal.
- **Double Bottom Breakdown (bearish):** the current O column falls one box below the previous O column's bottom. The basic sell signal.
- **Triple Top / Triple Bottom:** price exceeds the highs of **two** prior X columns (or breaks two prior O lows). Stronger, because the level was tested twice before giving way.
- **Bullish / Bearish Catapult:** a triple top breakout that pulls back, holds a higher low, then breaks out again — a high-conviction continuation pattern.
- **Bull/Bear Traps and pole patterns:** longer P&F pattern vocabulary (per Cohen/du Plessis) covering shakeouts and rapid extended columns.
- **Bullish/Bearish Signal Reversed:** a small counter-pattern that fails and reverses — a warning that a breakout is being rejected.
- **Long tail / one-step-back:** a single very long column (the "pole") often followed by a shallow retrace, projecting a strong measured move via the Vertical Count.

### Price Targets — the Counts

P&F's distinctive feature is objective targets:

- **Vertical Count:** (number of X's in the breakout column) × (box size) × (reversal amount) + (column low) = upside target. It measures the thrust of the breakout move.
- **Horizontal Count:** (width of the congestion base in columns) × (box size) × (reversal amount) + (breakout level) = target. It reads the "cause" built during a base and projects the "effect" — conceptually the same accumulation→markup logic as the [[wyckoff-method]].

### Trendlines

P&F draws **45-degree trendlines** from significant highs/lows on the grid: a **Bullish Support Line** up from a low, a **Bearish Resistance Line** down from a high. Because the grid is fixed, these lines are non-subjective — a rare property in charting.

## Variants

- **Traditional (Cohen/Wheelan) P&F** — the classic manual method; 3-box reversal, fixed box.
- **Percentage-box P&F** — scale-invariant boxes; the practical choice for crypto's wide price ranges.
- **1-box reversal** — the original 19th-century style (no separate reversal column rule); more sensitive, more patterns, more noise.
- **High/Low vs. Close-only construction** — using intraday high/low registers reversals sooner; close-only P&F is smoother and slower.
- **Optimized/relative-strength P&F** — used for ranking assets (e.g., a P&F relative-strength chart of an altcoin vs. BTC).
- **Log-scaled P&F** — plots on a logarithmic price axis so equal-percentage moves get equal box counts across the whole range; effectively the charting counterpart of percentage boxes and well suited to assets spanning several price decades.

## History and Development

P&F is the oldest of the systematic charting methods, its roots in the "figure charts" traders kept by hand in the 1880s–1890s before ticker tape made intraday recording practical. Charles Dow is said to have used a precursor. The method was formalized through the 20th century — Victor de Villiers and Owen Taylor codified the three-box reversal, A.W. Cohen popularized the modern buy/sell signal vocabulary and the count methods, and Thomas Dorsey (Dorsey Wright) later built relative-strength and sector-rotation frameworks on P&F. Its longevity owes to a property few methods share: signals and targets are **mechanical and reproducible** — two analysts with the same box/reversal settings draw the same chart and read the same signals. That objectivity is precisely what recommends it for crypto, a market awash in discretionary pattern-reading.

## Signals It Generates

1. **Buy:** Double or Triple Top Breakout.
2. **Sell / short:** Double or Triple Bottom Breakdown.
3. **Trend gate:** only take buys above the 45-degree Bullish Support Line; only take sells below the Bearish Resistance Line.
4. **Targets:** Vertical and Horizontal Counts give explicit exits.
5. **Stop:** the 3-box reversal level from entry — a natural, objective invalidation point.

## Parameter Choices

- **Box size** is the primary lever — too large filters out real trades and coarsens targets; too small reintroduces noise. Percentage boxes keep sensitivity constant across crypto's price range.
- **Reversal amount** (typically 3) balances noise-filtering against responsiveness; 1-box is very sensitive, 5-box very slow.
- **Price source** (high/low vs. close) shifts how quickly reversals and breakouts register.
- **Log vs. linear scaling** matters for assets that span large ranges — log/percentage boxes prevent early history from being compressed to nothing.

## Confluence and Combinations

- **[[support-and-resistance]]** — P&F's native strength; columns of X/O reversals at the same level mark clean horizontal zones that reinforce candlestick-chart levels.
- **[[donchian-channel-breakout]]** — automates the "new high/low breakout" that a Double Top formalizes; the two agree at true structural breaks.
- **[[darvas-box]]** — the same buy-strength-on-breakout philosophy from the same classical era; use together for confirmation on new highs.
- **[[volume]] cross-check** — P&F ignores volume, so confirm breakouts on a time chart that a Double/Triple Top broke on real participation, not a thin wick.
- **Relative strength** — P&F relative-strength charts (asset ÷ BTC) help rank which alts are structurally leading.

## Relative Strength and Screening

One of P&F's most practical modern uses is **relative-strength ranking**. Plotting a P&F chart of one asset **divided by another** (e.g., SOL ÷ BTC, or a coin ÷ a sector index) turns the same objective buy/sell-signal machinery into a leadership screen: an RS chart on a Buy signal and rising means the numerator is structurally outperforming. Dorsey Wright built entire equity sector-rotation systems on this idea, and it transfers directly to crypto — rank alts by their P&F RS versus BTC to find the structurally strongest names for a [[darvas-box]]-style breakout or momentum trade, and avoid those on RS Sell signals. Because the signals are mechanical, an RS-P&F screen across a liquid universe is easy to automate and free of the discretion that plagues eyeballed relative-strength.

## Strengths

- **Removes time-based noise** — only significant moves are plotted, yielding cleaner structure than candlesticks.
- **Objective, binary signals** — a breakout either happens or it does not; little room for interpretation bias.
- **Built-in price targets** via the Vertical and Horizontal Counts — few methods offer measured objectives this cleanly.
- **The 3-box reversal filters minor whipsaws** that plague time-based breakout systems.
- **Non-subjective 45-degree trendlines** — no debate about where to draw them.
- **Excellent for long-term [[support-and-resistance]]** and major trend-change identification.

## Documented Weaknesses

- **No timing context.** A breakout that took six months looks identical to one that took six days; P&F cannot tell you *when* anything happened or how fast a target may be reached.
- **Box-size sensitivity.** Signals and targets shift materially with box size; poor calibration either buries real trades or manufactures noise.
- **Reversal repainting on the forming column.** The current, still-building column is provisional — until a 3-box counter-move confirms, an in-progress column can extend or, once it reverses, be re-read; only *closed* structure should drive decisions.
- **No volume.** P&F is blind to participation, a real limitation versus volume-aware methods like the [[wyckoff-method]].
- **Tooling and familiarity gap.** Not natively supported on every crypto charting platform; manual construction is tedious, and few modern traders read P&F, making setups hard to discuss or verify.
- **Lag at reversals.** Like all reversal-confirmed methods, the 3-box requirement means turns are acknowledged only after price has already moved.

## Common Mistakes

- **Fixed boxes on wide-range crypto.** Using a static box size across an asset that 10×'s buries early signals or floods later ones with noise. Use **percentage/log** boxes.
- **Acting on the forming column.** Reading a signal from an in-progress column before a reversal or breakout is confirmed.
- **Treating counts as guarantees.** Vertical/Horizontal Counts are measured objectives, not promises — in crypto's fat tails they are frequently overshot or never reached; use them for planning, not certainty.
- **Ignoring the trend line.** Taking buy signals below the 45-degree Bearish Resistance Line (or sells above the Bullish Support Line) — the trend gate exists to filter counter-trend breakouts.
- **Skipping volume confirmation.** P&F is volume-blind; a breakout on a thin-book wick looks identical to one on real demand. Cross-check on a time chart.
- **Mismatching high/low vs. close construction** between analysis and backtest, which shifts when signals register.

## Renko and Candlesticks Comparison

See the comparison table on [[renko-trading]] — P&F and Renko are the two classic time-independent methods. P&F's distinctive advantages over Renko are its **count-based price targets** and its **objective 45-degree trend lines**; its distinctive cost is that it is less widely supported and less familiar to modern crypto traders.

## Range / Whipsaw Scenario

The documented weakness made concrete: BTC oscillates in a tight band. Small Double Top and Double Bottom signals fire alternately as price nips just past each prior column's extreme, then reverses within the 3-box threshold. A trader taking every basic signal is chopped up buying failed top-breaks and shorting failed bottom-breaks. P&F's own defenses help here: (1) demand **Triple** Tops/Bottoms rather than Doubles in suspected ranges (two prior tests before a break), (2) enforce the 45-degree trend-line gate, and (3) widen the box or reversal so intra-range noise never crosses a boundary. As with all these methods, the durable fix is a regime read — trade P&F breakouts in trends, not in acknowledged ranges.

## Application to Crypto Charts

- **Percentage boxes are essential.** Crypto assets routinely move 10–100×; a fixed box that suits BTC at $20k is useless at $100k or for a sub-dollar altcoin. Percentage/log boxes keep P&F sensitivity constant across the range.
- **24/7, no sessions.** P&F's time-independence sidesteps the "which session/close?" ambiguity that a global, always-on market creates — there are no daily gaps or session boundaries to reconcile.
- **Structural breakouts over noise.** Crypto's tape is full of stop-hunt wicks; the 3-box reversal ignores moves too small to matter, isolating genuine structural breaks — useful on higher-timeframe BTC/ETH.
- **Altcoin caution.** Thin books can print isolated boxes on low liquidity; cross-check breakouts against real [[volume]] and consider a larger box/reversal for illiquid names.
- **Targets as risk framing, not promises.** Vertical/Horizontal counts give measured objectives, but in crypto's fat-tailed moves treat them as planning levels, not guarantees.

## Worked Crypto Example

**Asset:** BTC/USDT, 1% percentage box, 3-box reversal (illustrative), read on confirmed columns.

1. BTC forms three separate X columns that each stall near **$68,000** — a triple-top resistance tested three times.
2. A new X column pushes one box above $68,000 to ~$68,700 — a **Triple Top Breakout** buy signal.
3. Enter long at ~$68,700. The 3-box-reversal stop sits ~$66,000 (three 1% boxes below the breakout). Risk ≈ $2,700.
4. **Vertical Count target:** the breakout column contains, say, 9 X's; target ≈ column low (~$62,000) + (9 × 1% box ≈ $680 × 3) ≈ $62,000 + ~$18,400 ≈ **$80,400** (rounded for illustration).
5. BTC advances in a clean sequence of rising X/O columns with rising lows — a structurally intact uptrend that holds above the 45-degree Bullish Support Line.
6. Near the count target, a **Double Bottom Breakdown** prints as momentum fades; exit ~$78,500.
7. **Result:** entry ~$68,700, exit ~$78,500, ≈ +$9,800/BTC (+14.3%) against ≈ $2,700 risk (~3.6:1). The triple-top break provided an objective trigger and the vertical count framed a sensible profit zone; the 3-box reversal kept the trader out of several intra-trend pullbacks that never breached structure.

## Reading Across Box Sizes

P&F, like Renko, is time-independent, so its multi-scale analogue is **multi-box-size** analysis:

- **Large box** (e.g., 2–3%) — the long-horizon structure layer; major Double/Triple Tops here mark cycle-scale breakouts and the dominant [[support-and-resistance]] grid.
- **Medium box** (~1%) — the swing-signal layer for tradeable breakouts and counts.
- **Small box** (<0.5%) — fine structure and timing; noisy, best used to refine entries within a larger-box trend.
- Confirming a medium-box breakout in the direction of a large-box uptrend (above the 45-degree Bullish Support Line on both) is P&F's version of higher-timeframe agreement.

Keep the box scheme (fixed vs. percentage) and price source (high/low vs. close) identical between the box sizes so the charts are comparable.

## Pre-Trade Checklist

1. Is the **larger-box** structure trending in my direction, above/below its 45-degree trend line? (regime gate)
2. Is the signal a **confirmed** Double or (better) Triple Top/Bottom on a completed column — not a forming one?
3. Are box size and reversal appropriate (percentage/log for wide-range crypto)?
4. What do the **Vertical/Horizontal Counts** project, and is the reward acceptable versus the 3-box stop?
5. Did the breakout occur on real **volume**? (cross-check a time chart — P&F is volume-blind)
6. Am I trading a **liquid** asset where isolated boxes are not just thin-book noise?

## Getting the Data (CryptoDataAPI)

P&F is constructed from price alone — pull klines and build the X/O grid yourself using a fixed or percentage box. Use closed candles and confirmed columns to avoid acting on a still-forming column.

**Live / recent candles:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — Binance spot OHLCV (use high/low for high-low construction).
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1d&limit=1000` — Hyperliquid perp OHLCV.

**Historical archive (backtesting):**
- `GET /api/v1/backtesting/klines` — full OHLCV archive (Parquet since 2020) for building long-horizon P&F charts and testing count-based targets.

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Endpoint catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]], [[cryptodataapi-hyperliquid]].

**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run a P&F system end-to-end:

- **Compute** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` (high/low or close construction) → build the X/O grid with percentage boxes; signal only on completed columns, never the forming one.
- **Screen** — the same klines pulls feed P&F relative-strength charts (asset ÷ BTC) for the leadership screen; `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1d&limit=1000` covers the perp universe.
- **Volume cross-check** — `GET /api/v1/market-data/volume-history` — P&F is volume-blind, so verify a Double/Triple Top broke on real participation before acting.
- **Regime gate** — `GET /api/v1/quant/market` — demand Triple (not Double) breakouts in `range_low_vol`/`choppy_high_vol`; take Doubles with the 45-degree trend line in trend states.
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1d back to 2017-08) for multi-cycle testing of box/reversal settings and count-target hit rates.

## Key Takeaways

- P&F is the **oldest systematic charting method** and, like Renko, plots price rather than time — X columns up, O columns down.
- Its two inputs are **box size** and **reversal amount** (classically 3-box); use percentage/log boxes for crypto.
- Signals are **objective and reproducible**: Double/Triple Top breakouts (buy) and bottom breakdowns (sell), gated by 45-degree trend lines.
- Uniquely offers **built-in price targets** via the Vertical and Horizontal Counts — plan levels, not guarantees.
- Weaknesses: **no time context, no volume**, box-size sensitivity, forming-column repaint, and lag at reversals.
- Strong crypto fit for **higher-timeframe structure and clean support/resistance**; less useful for timing or thin, manipulable alts.
- Its edge over other methods is **mechanical objectivity** — a real asset in crypto's discretion-heavy chart culture.

## Related

- [[renko-trading]] — the other classic time-independent chart; fixed bricks instead of X/O columns
- [[support-and-resistance]] — P&F excels at isolating clean horizontal levels
- [[darvas-box]] — a contemporaneous box-breakout approach; buy-strength philosophy
- [[heikin-ashi]] — noise-smoothing candles that keep the time axis
- [[donchian-channel-breakout]] — automates the new-high/low breakout a Double Top formalizes
- [[bitcoin]] — primary crypto instrument for higher-timeframe P&F structure

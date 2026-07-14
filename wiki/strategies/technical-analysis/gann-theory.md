---
title: "Gann Theory"
type: concept
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [gann, gann-angles, square-of-nine, time-cycles, geometric-trading, price-time, technical-analysis, crypto]
aliases: ["Gann Trading", "W.D. Gann Method", "Gann Angles", "Gann Fan", "Square of Nine", "Gann Square"]
domain: [technical-analysis]
prerequisites: ["[[support-and-resistance]]", "[[technical-analysis]]", "[[fibonacci-trading]]"]
difficulty: advanced
markets: [crypto]
related: ["[[fibonacci-trading]]", "[[elliott-wave]]", "[[harmonic-patterns]]", "[[support-and-resistance]]", "[[point-and-figure]]", "[[market-cycles]]", "[[seasonality]]"]
---

# Gann Theory

Gann Theory is the body of trading methods attributed to **William Delbert Gann** (1878-1955), built on the premise that markets obey **geometric and cyclical natural laws** relating **price and time**. Its three pillars are **Gann angles** (trendlines drawn at fixed price-per-time slopes), the **Square of Nine** (a numerical spiral used to project support, resistance and turning points), and **time cycles** (the idea that markets turn at recurring calendar intervals). The methods are esoteric — blending geometry, seasonality, numerology and astrology — and are among the most contested in [[technical-analysis]]. In [[crypto]], Gann's price-and-time framework attracts a niche following because the market's 24/7 calendar and clean ~4-year [[market-cycles|halving cycle]] suit its time-based reasoning, but the same subjectivity and unfalsifiability that dog Gann elsewhere apply in full.

## Origins and the Gann Legend

- Gann was born in Lufkin, Texas, and traded cotton, wheat and stocks from the early 1900s. He studied ancient geometry, the Bible, and astrology, and claimed to have discovered a **"Law of Vibration"** governing markets.
- A frequently cited 1909 interview in *The Ticker and Investment Digest* (Richard Wyckoff's publication) reported that, under observation, Gann made **286 trades over ~25 market days with roughly 264 winners (~92%)**, multiplying a small stake many-fold. Variants of the story cite turning ~$130 into ~$12,000 in 30 days.
- He authored ***Truth of the Stock Tape*** (1923), the allegorical ***Tunnel Thru the Air*** (1927, said to encode his methods), ***How to Make Profits in Commodities*** (1941), and ***45 Years in Wall Street*** (1949).
- **Skeptics note his estate was modest** (~$100k) and that his son reportedly said Gann earned more from selling expensive courses than from trading — a standing caution about the legend. Gann never published his complete method, which is why interpretations conflict to this day.

## The Three Pillars

### 1. Gann Angles (the Gann Fan)

Gann angles are trendlines drawn from a significant high or low at a fixed **rate of price change per unit of time** (dollars per bar). The nine standard angles form a **fan**:

| Angle | Slope (price:time) | Degrees* | Meaning |
|---|---|---|---|
| 1x8 | 1 unit / 8 bars | 7.5° | very shallow |
| 1x4 | 1 / 4 | 15° | shallow |
| 1x3 | 1 / 3 | 18.75° | |
| 1x2 | 1 / 2 | 26.25° | mild uptrend |
| **1x1** | **1 / 1** | **45°** | **equilibrium** |
| 2x1 | 2 / 1 | 63.75° | steep |
| 3x1 | 3 / 1 | 71.25° | |
| 4x1 | 4 / 1 | 75° | very steep |
| 8x1 | 8 / 1 | 82.5° | near-vertical |

\*Degrees are only literal when the chart is scaled so one price unit equals one time unit — see the scaling caveat below.

- The **1x1** is Gann's master line: above it the trend is strong/bullish, below it weak/bearish.
- A fan from a major low provides **dynamic [[support-and-resistance]]**; price tends to migrate from one angle to the next, and a break of one angle implies a move to the following one.

### 2. The Square of Nine

The Square of Nine ("Gann Square", "Square Root Calculator") is a **spiral of numbers** beginning at 1 in the center and winding outward, so that values a full rotation apart differ by a predictable amount tied to their **square roots**. It projects price levels rather than reading a chart directly.

- Numbers on the **cardinal cross** (0°, 90°, 180°, 270°) and **ordinal cross** (45°, 135°, 225°, 315°) share geometric relationships and act as support/resistance.
- A common projection: take **√(price)**, add a fraction of a rotation (e.g., **+0.5** for 90°, **+1.0** for 180°, **+2.0** for 360°), then **square the result** to get the next level. Example: √10,000 = 100; 100 + 2 = 102; 102² = **10,404** as a 360° target from 10,000.
- Related "master charts" include the **Square of 144**, **Square of 90**, and the **Hexagon** and **Circle of 360** charts, each ruling different cycle lengths.

### 3. Time Cycles and Price-Time Squaring

- Gann held that markets repeat at recurring intervals measured from a prior high or low: **30, 45, 60, 90, 120, 144, 180, 270, 360** calendar days; and longer cycles of ~1, 7, 10, 20, 30 and 60 years. The **90-day and 180-day** counts are the most watched.
- **Anniversary dates** — the calendar date of a major top or bottom — are candidate turning points in later years.
- **Seasonal dates** (solstices, equinoxes) were part of his cycle work.
- **Price-time squaring** is the theory's signature idea: when price traveled (in appropriate units) equals time elapsed (in bars/days) from a pivot, a trend change is "imminent" — e.g., a $90 move over 90 days "squares out."

### Time-Cycle Reference

| Cycle | Gann's basis | Crypto analog |
|---|---|---|
| 30 / 45 / 60 days | monthly divisions | short swing rhythm; continuous in 24/7 markets |
| **90 days** | quarter / 90° of the year | most-watched intermediate turn window |
| 120 / 144 days | 144 = 12² master number | intermediate cycle checkpoints |
| **180 days** | half-year / 180° | major turn window |
| 270 / 360 days | 3/4 year / full circle | annual anniversary of a pivot |
| ~4 years | (extension of yearly cycles) | maps to the [[bitcoin\|BTC]] **halving cycle** |
| 7 / 10 / 20 / 60 years | long-wave cycles | too long for crypto's history (yet) |

Because crypto trades every calendar day, a 90-day count equals 90 trading days with no holiday adjustment — the cleanest possible substrate for Gann's day-based cycles.

### Retracement Levels (Eighths and Thirds)

Gann divided ranges into **eighths** — 1/8 (12.5%), 2/8 (25%), 3/8 (37.5%), **4/8 (50%)**, **5/8 (62.5%)**, 6/8 (75%), 7/8 (87.5%) — and **thirds** (33.3%, 66.7%). He regarded **50% and 62.5%** as the most important, which places Gann's 5/8 almost exactly on the [[fibonacci-trading|Fibonacci]] golden pocket (0.618-0.65) — a rare point of agreement between the two frameworks.

## Rules and Signals

### Entry
1. **Gann-angle bounce:** go long when price rebounds from a rising angle (especially the 1x1 or 2x1); go short when it rejects a falling angle.
2. **Square-of-Nine level:** compute the next 90°/180°/360° projections from the current swing and act when price tests them with a reversal signal.
3. **Time-cycle confluence:** when a time-cycle date coincides with an angle or a Square-of-Nine level, the odds of a turn rise materially.
4. **Price-time squaring:** treat a "square-out" (price = time from the pivot) as a warning of trend change.

### Stops and targets
- Stop just beyond the angle that triggered entry; a broken 1x1 implies the next support is the 1x2.
- Target the next angle up (for longs) or the Square-of-Nine level at the next 180°/360° rotation.
- **Time-based exit:** if the trade has not reached target by the next major cycle date, reassess rather than hold indefinitely.

## Reading a Gann Fan, Step by Step

1. **Fix the scale first.** Decide the price-per-bar ratio (and log vs linear) *before* drawing — this determines every angle. For multi-percent BTC moves, use log.
2. **Anchor to a major pivot.** Start the fan from a significant, unambiguous swing low (for an uptrend fan) or high.
3. **Draw the 1x1.** The equilibrium line; note whether price is above (strong) or below (weak) it.
4. **Add the surrounding angles** (2x1, 1x2, and the extremes) to build dynamic support/resistance.
5. **Watch angle-to-angle migration.** Price tends to travel from one angle to the next; a break of the 1x1 implies a test of the 1x2 below.
6. **Overlay time cycles.** Mark 90/180/360-day counts and the halving anniversary; a bounce *on an angle at a cycle date* is the high-conviction Gann setup.
7. **Require confirmation.** Treat an angle touch as a decision point, not a signal — wait for a reversal candle before acting.

## Applying Gann to Crypto Charts

- **A continuous calendar suits time cycles.** Because crypto trades 7 days a week, **90 calendar days equals 90 trading days** — there is no weekend/holiday drift to reconcile, arguably making Gann's day-count cycles cleaner than in equities.
- **The halving as a master cycle.** [[bitcoin|BTC]]'s ~4-year halving rhythm and the anniversary dates of prior cycle tops/bottoms are natural inputs for Gann time analysis and [[market-cycles]] work.
- **Round numbers and eighths.** BTC respects large psychological levels ($20k, $50k, $100k); dividing a cycle range into Gann eighths (with 50% and 62.5% emphasized) often marks real reaction zones.
- **Square of Nine from cycle pivots.** Practitioners run √-based projections from major BTC lows/highs to derive candidate targets.
- **The scaling problem is worse in crypto.** Angles depend entirely on the chosen price-per-bar scale, and crypto's enormous ranges force a **logarithmic** chart or a carefully fixed $/bar scale; change the scale and every "45°" line changes with it.
- **Volatility overshoots.** Leverage-driven [[liquidation|liquidation]] wicks routinely blow through an angle and snap back, so — as with all Gann tools — a confirmation signal beats a mechanical touch.

## The Esoteric Layer (Honest Treatment)

Gann's methods span a spectrum from defensible to unfalsifiable, and a serious reference must separate them:

- **Defensible core.** Gann angles as *dynamic, scale-dependent* support/resistance; eighths/thirds retracements (which overlap [[fibonacci-trading|Fibonacci]]); and calendar time cycles anchored to real events (in crypto, the halving). These are ordinary chart tools dressed in Gann's vocabulary and can be used without accepting any metaphysics.
- **Contested middle.** The Square of Nine and price-time squaring — internally consistent arithmetic that produces many candidate levels, so their apparent accuracy is hard to distinguish from hindsight fitting.
- **Esoteric periphery.** **Astrology** (planetary cycles, heliocentric/geocentric longitudes), **Biblical numerology**, and the "Law of Vibration." These have **no empirical validation**, are not reproducible, and are the main reason quantitative traders dismiss Gann outright. A rigorous crypto practitioner can adopt the core and ignore the periphery without loss.

## Gann and Fibonacci Compared

Both are ratio-and-geometry systems from the early 20th century, and they frequently agree:

- **Levels.** Gann's **5/8 (62.5%)** sits almost exactly on the Fibonacci **golden pocket (0.618-0.65)**; his 50% and 37.5% roughly track Fibonacci's 0.5 and 0.382. Where the two systems mark the same price, the confluence is stronger.
- **Difference.** [[fibonacci-trading]] is **price-only** and one-click objective (given an anchor); Gann adds **time** (angles, cycles, squaring) but at the cost of **scaling subjectivity** and far greater complexity. Many crypto traders use Fibonacci for price targets and borrow only Gann's *time-cycle* thinking (halving anniversaries), taking the best of each.

## Confluence With Other Tools

- **[[fibonacci-trading]]** — Gann's 5/8 (62.5%) ≈ the Fibonacci golden pocket; the two ratio systems frequently corroborate the same level.
- **[[elliott-wave]]** — Gann and Elliott were near-contemporaries; Gann *time* cycles and Elliott *wave* structure are often combined for long-term forecasting.
- **[[harmonic-patterns]]** — shares Gann's geometric spirit, with precise ratio-defined structures.
- **[[support-and-resistance]]** — angles and Square-of-Nine values are specialized, derived S/R.
- **[[seasonality]] / [[market-cycles]]** — Gann's calendar cycles overlap with seasonal and halving-cycle analysis.
- **[[point-and-figure]]** — another classical, time-agnostic charting method from Gann's era.

## Strengths

- Unifies **price and time** in one framework — most methods model price alone.
- Gann angles give *dynamic* support/resistance that advances with the chart.
- The Square of Nine yields specific *calculated* targets rather than eyeballed levels.
- Time-cycle analysis attempts to answer *when* a move may occur, not only *where* — a rare and, when right, valuable dimension.
- A century of practitioners has documented and extended the techniques, and the calendar-continuity of crypto is unusually friendly to the time-cycle component.

## Criticisms and Limitations

- **Esoteric and unfalsifiable.** The astrology, numerology and "natural law" elements have no empirical validation and repel most quantitative traders.
- **Scaling subjectivity.** Because angles depend on chart scaling, different scales produce different "45° lines" — there is no objective slope, undercutting the method's claim to precision.
- **Hindsight fitting.** The Square of Nine and the dense grid of cycles generate so many candidate levels and dates that *something* is almost always "close," creating an illusion of accuracy after the fact.
- **Opaque source material.** Gann never published his full method, so competing schools disagree on the "correct" techniques.
- **Disputed track record.** The 92% legend rests on a single 1909 account; his modest estate and the "made money teaching, not trading" claim keep the record in doubt. Few successful modern traders publicly credit Gann as their primary edge.
- **No robust backtests.** Like other discretionary geometric systems, Gann resists systematic validation.

## Worked Crypto Example

**Asset:** [[bitcoin|BTC]]/USD, weekly, log scale.

1. BTC prints a major cycle low at **$16,000**. Fix a log-scaled chart and draw a Gann fan from the low; the **1x1** rises as the equilibrium line, with the 2x1 above it.
2. Over the next months BTC rallies to **$45,000**, running above the steep 2x1 angle — a strong-trend signal.
3. BTC then loses the 2x1 and pulls back toward the **1x1 angle near $38,000**. Critically, this pullback lands **~90 calendar days** from the cycle low — a Gann time-cycle confluence — and near the **62.5% (5/8) retracement** of the up-leg, which also sits in the [[fibonacci-trading|Fibonacci]] golden pocket.
4. A bullish weekly reversal candle forms on the 1x1; [[funding-rate|funding]] resets from richly positive toward neutral as over-leveraged longs [[liquidation|liquidate]]. **Enter long at ~$38,500**, stop at **$35,500** (below the 1x1). Risk ≈ $3,000.
5. **Square-of-Nine target:** a 360° projection from the $16,000 low points to the **~$52,000** region; set that as the objective.
6. BTC holds the 1x1 and advances to **~$52,500** over the following cycle window, reaching the projected level near the next time-cycle date.
7. **Result:** ~+$14,000/BTC on a ~$3,000 risk (~4.7:1). The trade combined an angle (1x1 support), a time cycle (~90 days), a retracement (5/8), and a Square-of-Nine target — the confluence, not any single tool, made the setup.

## Worked Square-of-Nine Calculation

The projection is a square-root method, easy to reproduce for any [[bitcoin|BTC]] pivot:

1. Take a reference price — say a swing low at **$40,000**. Compute **√40,000 = 200**.
2. Add a fraction of a full rotation: **+0.5** for 90°, **+1.0** for 180°, **+2.0** for 360° (a full turn of the spiral).
3. Square the result:
   - 90°: (200 + 0.5)² = 200.5² = **$40,200**
   - 180°: (200 + 1.0)² = 201² = **$40,401**
   - 360°: (200 + 2.0)² = 202² = **$40,804**
4. For larger, multi-percent BTC swings the same method scales: from a **$16,000** low, √16,000 = 126.5; a 360° turn = (126.5 + 2)² ≈ **$16,512** — for wide cycle projections, chain multiple rotations or work from the square root of the *range* rather than the price.

The output is a ladder of candidate support/resistance prices. Their value, as ever with Gann, depends on **confirmation** at the level, not the arithmetic alone.

## Gann's Trading Rules (Selected)

Beyond the geometry, Gann published pragmatic **money-management and discipline rules** that are his least controversial legacy and translate directly to crypto:

- **Trade with the trend**; never buck the dominant direction shown by the 1x1 angle.
- **Cut losses short and let profits run** — protect capital above all.
- **Use stop-loss orders on every trade**, placed at a logical invalidation (a broken angle or level).
- **Never overtrade** or risk too much on one position — a hard rule in leverage-heavy crypto.
- **Never turn a winning trade into a loser**; trail the stop as price advances.
- **Avoid trading in dull, rangebound markets**; wait for a clear trend or a defined turn.
- **Pyramid only in the direction of the trend**, adding on strength, not into losses.

These rules stand on their own merit regardless of whether one accepts the angles, squares, or cycles.

## Common Mistakes in Crypto

- **Inconsistent scaling.** Redraw the same fan on a linear vs log chart and the "45°" line moves; fix a scaling convention (log for multi-percent BTC moves) and keep it.
- **Level and cycle shopping.** The Square of Nine plus a dozen cycle lengths guarantee *something* is near price; pre-commit to which projections and dates you will honor, or the method becomes pure hindsight.
- **Treating a touch as a signal.** Crypto [[liquidation|liquidation]] wicks blow through angles and squares constantly; require a confirmation candle.
- **Over-weighting the esoterica.** The astrological/numerological layer has no validation; the defensible core is angles-as-dynamic-S/R, eighths/thirds retracements, and calendar cycles anchored to the halving.
- **Ignoring liquidity and regime.** A Gann level in a thin [[altcoins|altcoin]] is meaningless; apply the method to liquid majors and read the [[market-regime]] first.

## Getting the Data (CryptoDataAPI)

Gann angles, Square-of-Nine projections and cycle counts are derived from price and calendar time; charts are usually rendered on an exchange feed or TradingView, where scaling can be controlled. [[cryptodataapi|CryptoDataAPI]] supplies the **OHLCV klines** (with timestamps) needed to fix pivots, measure time between them, and project levels.

- **Live OHLCV (pivots + charting substrate):** `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1w&limit=1000` — see [[cryptodataapi-market-data]].
- **Historical OHLCV (archive since 2020, for cycle/anniversary analysis):** `GET /api/v1/backtesting/klines` — see [[cryptodataapi-backtesting]].
- **Reversal context at a projected level:** `GET /api/v1/derivatives/funding-rates?coin=BTC` and `GET /api/v1/market-intelligence/liquidations` (a liquidation flush into a Gann/time-cycle confluence).

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1w&limit=1000"
```

## Related
- [[fibonacci-trading]] — a parallel ratio framework; Gann's 5/8 ≈ the golden pocket
- [[elliott-wave]] — pairs Elliott's price structure with Gann's time cycles
- [[harmonic-patterns]] — geometric, ratio-defined structures in Gann's spirit
- [[support-and-resistance]] — angles and Square-of-Nine values are derived S/R
- [[point-and-figure]] — a classical, time-agnostic charting method from Gann's era
- [[market-cycles]] — the BTC halving rhythm as a modern time-cycle input
- [[seasonality]] — recurring calendar tendencies that overlap with Gann cycles

## Sources
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]]

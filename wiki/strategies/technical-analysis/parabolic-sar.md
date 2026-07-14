---
title: "Parabolic SAR"
type: concept
created: 2026-04-06
updated: 2026-07-14
status: good
domain: [technical-analysis]
prerequisites: ["[[trailing-stop]]", "[[adx]]"]
difficulty: beginner
tags: [trend-following, trailing-stop, parabolic-sar, welles-wilder, indicators, technical-analysis, crypto]
aliases: ["Parabolic SAR", "Parabolic Stop and Reverse", "PSAR", "SAR"]
markets: [crypto]
related: ["[[atr]]", "[[supertrend]]", "[[moving-average-crossover]]", "[[adx]]", "[[trailing-stop]]", "[[volatility]]", "[[j-welles-wilder]]", "[[bitcoin]]"]
---

# Parabolic SAR

The Parabolic SAR (Stop and Reverse) is a **trend-following indicator and trailing-stop mechanism** that prints a series of dots above or below price. Dots **below** price signal an uptrend; dots **above** signal a downtrend. The dots trace a parabola-like curve that accelerates toward price the longer a trend runs, so the stop tightens progressively until price finally touches it — at which point the system **reverses**, closing the current position and opening the opposite one. It is always in the market. Created by **J. Welles Wilder Jr.** and introduced in his 1978 *New Concepts in Technical Trading Systems* alongside the [[rsi]], [[adx]], and [[atr]], the SAR remains a widely used trailing stop. In [[crypto]], its volatility-agnostic acceleration makes it good at riding fast trends but notably fragile in the sideways chop that fills a 24/7 tape.

## What It Is

Parabolic SAR is best understood as a **self-tightening trailing stop that also flips direction**. It does not measure momentum or overbought/oversold conditions; it tracks trend direction and provides a concrete stop level (the current dot) every period. Its defining feature is the **Acceleration Factor**, which speeds the stop's approach to price as the trend extends new extremes — rewarding strong, persistent trends by locking in gains ever tighter, and punishing choppy markets by flipping constantly.

## Construction and Formula

The SAR is computed recursively. Within a trend it moves toward price each period; when price crosses it, the system reverses and reseeds.

- **SAR(next) = SAR(current) + AF × (EP − SAR(current))**
  - **EP (Extreme Point)** = the most extreme price reached in the current trend — the highest high in an uptrend, the lowest low in a downtrend.
  - **AF (Acceleration Factor)** = starts at **0.02**, increases by **0.02** each time a **new EP** is made, capped at a **maximum of 0.20**. AF only rises when the trend makes a fresh extreme; otherwise it holds.
- **Clamping rule:** in an uptrend the SAR is never placed above the prior two periods' lows (in a downtrend, never below the prior two highs). This prevents the stop from jumping inside recent price action.
- **Reversal (the "SAR"):** when price touches or crosses the SAR, the trend flips. The new SAR is set to the **prior trend's EP**, AF **resets to 0.02**, and the EP restarts from the new trend's first extreme.

Because AF grows only on new extremes, the dots stay far from price at a trend's start (loose stop, wide initial risk) and crowd toward price as the trend matures (tight stop, quick reversal) — the visual "parabola."

A short numeric illustration: right after a bullish flip, AF = 0.02 and the SAR sits well below price, so it advances slowly. As BTC makes successive new highs, AF steps to 0.04, 0.06, 0.08 … and each `AF × (EP − SAR)` increment grows, so the dots climb faster and faster toward price. By the time AF approaches its 0.20 cap late in a strong run, the SAR is hugging price closely — capturing most of the trend but ready to reverse on the first meaningful pullback. This is the mechanical reason SAR "gives back" the final part of a move.

## How to Read It

- **Dots below price** = uptrend; each dot is the current long trailing stop.
- **Dots above price** = downtrend; each dot is the short trailing stop.
- **Dot flip (below→above or above→below)** = stop-and-reverse signal.
- **Widening gap between dots and price** = early trend / accelerating move.
- **Dots crowding price** = mature trend; a reversal is increasingly likely as AF nears its cap.
- **Rapid alternation of dot sides** = a range — the "do not trade this on SAR alone" warning.

## Variants

- **Standard Wilder SAR** — AF 0.02 / step 0.02 / max 0.20, as above.
- **Tuned-AF variants** — raising the start/step/max makes the SAR tighter and faster (more flips); lowering them makes it looser and slower (later exits, fewer whipsaws). A common crypto tweak lowers the max (e.g., 0.10) to reduce premature reversals in volatile trends.
- **Non-reversal / stop-only mode** — use SAR purely as a trailing stop for a position entered by another system, ignoring its entry (reverse) signals.
- **Filtered SAR** — only act on SAR flips when a trend filter agrees ([[adx]] > 25, or a longer [[moving-average-crossover]]); the standard practical form.
- **Multi-timeframe SAR** — a higher-timeframe SAR direction gates lower-timeframe flips.
- **SAR + trend-strength overlay** — pairing SAR with [[adx]]/DMI or a moving-average slope to suppress flips outside a confirmed trend; the practical crypto default, since raw SAR alone is untradeable in ranges.

## Signals It Generates

1. **Long entry:** dots flip from above to below price.
2. **Short entry:** dots flip from below to above price.
3. **Stop-and-reverse exit:** the flip simultaneously closes the current trade and opens the reverse — the default, always-in-market behavior.
4. **Trailing stop:** trail the stop at the current dot each period; SAR is arguably strongest used purely this way.
5. **Partial-profit + trail:** bank part of the position at a fixed target (e.g., a set [[atr]] multiple) and trail the rest on the dots.
6. **Trend gate:** require [[adx]] > 25 or higher-timeframe agreement before taking a flip.

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| AF Start | 0.02 | Initial acceleration factor |
| AF Increment | 0.02 | Step increase per new extreme point |
| AF Maximum | 0.20 | Cap on the acceleration factor |

- **Higher AF start/step/max** → tighter, more sensitive SAR → more signals and more whipsaws.
- **Lower AF start/step/max** → looser SAR → fewer signals, later exits, more room for trends to breathe.
- SAR has **no volatility input** (unlike [[supertrend]]'s ATR), so the same AF behaves very differently across calm and violent regimes — a key reason to filter it.

## Parabolic SAR vs. Supertrend

The two are the classic pair of always-directional trailing-stop indicators. The decisive difference is volatility scaling:

| Aspect | Parabolic SAR | [[supertrend]] |
|--------|---------------|----------------|
| Volatility input | None (fixed AF) | Yes ([[atr]]-scaled) |
| Stop tightening | Accelerates with new extremes | Ratchets with volatility bands |
| Trigger | Price touch of the dot | Close vs. band |
| Sensitivity to intrabar wicks | High (touch-based) | Lower (close-based) |
| Crypto fit | Needs AF tuning + ADX filter | Auto-scales; generally friendlier |

Because SAR reverses on an intrabar **touch** and has no volatility term, it is more easily picked off by crypto's liquidation wicks than the close-based, ATR-scaled Supertrend — the main reason many crypto traders prefer Supertrend or run the two together and act only on agreement. SAR's compensating strength is its **accelerating** trail, which can hug a fast trend tighter than Supertrend near a climax.

## Confluence and Combinations

- **[[adx]]** — Wilder's own companion; ADX > 25 confirms a trending market where SAR flips are trustworthy. This is the single most important SAR filter.
- **[[atr]]** — calibrate additional/initial stops with ATR, since SAR's first post-flip dot can be far from price (wide risk).
- **[[supertrend]]** — a volatility-aware trailing stop; agreement between SAR and Supertrend strengthens a signal, disagreement flags chop.
- **[[moving-average-crossover]] / trend filter** — take SAR flips only in the direction of a longer MA to avoid counter-trend reversals.
- **[[volume]] / momentum** — confirm a flip with rising volume or an [[rsi]]/[[macd]] shift.
- **[[market-regime]] gate** — only trade SAR flips in trending regimes; disable in ranges.

## Strengths

- **Visually intuitive** — dots above or below price are immediately readable.
- **Built-in, self-tightening trailing stop** that automatically ratchets as a trend accelerates.
- **Always provides a concrete stop level** (the current dot) — no ambiguity about where to place risk.
- **Rewards strong trends** — the acceleration factor keeps you in longer as a move extends and locks gains tighter near the end.
- **Works on any timeframe**, from minute scalps to daily swings, and across every liquid crypto pair.
- **No repainting of closed bars** — once a bar closes, its SAR value is fixed (the live bar still updates intrabar; see below).

## Documented Weaknesses

- **Choppy-market killer.** In range-bound, low-[[adx]] conditions SAR flips constantly, producing a relentless string of small losses — its dominant, well-known failure mode.
- **Always-in-market design.** You are perpetually positioned long or short, which forces trades in conditions where standing aside would be better and can be psychologically taxing.
- **Wide initial risk / lag on trend start.** The first dots after a flip sit far from price, so the initial stop is wide, and the reversal only registers after price has already turned.
- **Repainting on the *forming* candle.** The current bar's SAR updates intrabar as new highs/lows print; only **closed-bar** SAR values are final. Systems that act on the live dot will look better in a naive backtest than in live trading — evaluate flips on closed bars.
- **No volatility scaling.** Unlike [[supertrend]], SAR has no ATR term, so fixed AF settings behave inconsistently across crypto's wildly varying volatility regimes.
- **No volume or momentum input** — purely price/extreme-based; blind to conviction behind a move.
- **Parameter sensitivity.** The fixed AF may not suit every instrument, and tuning it invites curve-fitting.

## Common Mistakes

- **Using SAR alone in chop.** Trading flips without an [[adx]] or higher-timeframe filter guarantees a stream of whipsaw losses in ranges — SAR's worst enemy.
- **Acting on the live dot.** Reversing on the forming bar's provisional SAR before the candle closes; use closed-bar flips.
- **Fixed AF on volatile alts.** Applying the default 0.20 max to a highly volatile coin tightens the stop into normal noise; lower the max and pair with an [[atr]] initial stop.
- **Sizing off the tight late stop.** Near a trend's end the dots crowd price; entering fresh there gives almost no room before a reversal.
- **Treating always-in as mandatory.** Feeling obliged to be long or short at all times; using SAR in stop-only mode (trailing a separately-entered position) sidesteps many bad reversals.
- **Ignoring the wide first stop.** The first post-flip dot is far from price — account for the wide initial risk in sizing.

## Range / Whipsaw Scenario

The documented weakness made concrete: ETH ranges quietly with [[adx]] near 15. The SAR flips above price, then a small bounce touches it and flips it below, then a small dip touches it and flips it back — the dots ping-pong across price every few candles. Each flip is a stop-and-reverse: a small loss, immediately reversed into another small loss. Over a week this produces a dozen tiny losses that add up. No AF setting cures it because there is no trend to catch. The fix is Wilder's own prescription — **require [[adx]] > 25** (or a higher-timeframe trend / [[market-regime]] agreement) before acting on any SAR flip, and stand aside otherwise.

## Application to Crypto Charts

- **Rides fast crypto trends well.** During sustained BTC/alt trend legs the accelerating dots trail tightly and capture much of the move — a genuine strength in crypto's tendency toward extended, momentum-driven runs.
- **Chop is more common and more punishing.** Crypto ranges are frequent and volatile; without an [[adx]] or higher-timeframe filter, SAR's constant flipping bleeds capital quickly. Filtering is close to mandatory here.
- **No native volatility scaling — a real gap.** Because SAR ignores volatility while crypto volatility swings enormously, consider lowering the AF max (e.g., 0.10) on volatile assets so the stop does not tighten into normal noise, and pair it with an [[atr]]-based initial stop.
- **Perp liquidation wicks.** Sharp intrabar spikes on [[perpetual-futures]] can touch the SAR and trigger a reversal on a wick that immediately reverts; using **closed-bar** flips reduces these fakeouts.
- **24/7, no gaps.** SAR is well-defined at all times, but fix a consistent candle close (e.g., UTC) so "the flip" is reproducible.
- **Cross-asset scanning.** Cheap to compute across the liquid universe to flag which coins have just flipped direction.

## Worked Crypto Example

**Asset:** ETH/USDT, 4-hour chart, standard SAR (0.02 / 0.02 / 0.20), signals on closed candles.

1. ETH is in a downtrend with SAR dots above price; ETH bottoms near $2,800.
2. Price rallies and **closes above** the dots; the SAR flips to below price at ~$2,870 — long entry. Initial stop = the first dot, ~$2,830 (note the still-wide gap right after the flip).
3. [[adx]] reads 32, confirming a trending environment — the filter permits the trade.
4. Over the next three days ETH makes new highs; each new EP bumps AF, and the dots accelerate up: $2,850 → $2,880 → $2,920 → $2,970, tightening the trailing stop.
5. ETH pushes to ~$3,200 then reverses. The accelerating SAR has climbed to ~$3,100; a 4h **close** below it flips the system — exit (and, in stop-and-reverse mode, open short) at ~$3,100.
6. **Result:** entry ~$2,870, exit ~$3,100, ≈ +$230/ETH (+8.0%). The acceleration factor let the stop tighten from ~$40 of initial slack to riding just under price near the top, banking most of the trend; the cost was a wide initial stop and a give-back of ~$100 from the $3,200 high — SAR's built-in lag on the exit.

## Backtesting Evidence

One illustrative backtesting study across US equities reported Parabolic SAR with a 44.7% win rate. As a trend-following/exit system, SAR is designed to capture large trending moves while accepting frequent small losses during choppy conditions — its value lies in the asymmetry of its risk/reward (big winners, small losers) rather than in a high hit rate. The same asymmetry applies in crypto, where trends can extend far but ranges are frequent, making the [[adx]]/trend filter essential to avoid the whipsaw regime (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Reading Across Timeframes

SAR is fragile alone, so a top-down read plus a trend filter is close to mandatory in crypto:

- **Daily** — the regime gate. Take SAR flips only in the direction of the daily trend; a daily [[adx]] > 25 confirms it is worth trading at all.
- **4-hour** — the swing-signal layer where dot flips are actionable when the daily agrees.
- **1-hour / lower** — scalp timing; SAR flips here whipsaw badly and should be gated by both the 4h and daily direction.
- **Stop-only usage across scales** — a durable pattern is to enter with a separate higher-timeframe signal and use the lower-timeframe SAR dots purely as a trailing stop, sidestepping SAR's worst reversals.

The rule of thumb: **filter every flip with ADX and the higher timeframe; never trade SAR in a low-ADX range.**

## Pre-Trade Checklist

1. Is **[[adx]] > 25** (or the higher-timeframe trend clearly directional) — i.e., not a range? (the essential SAR filter)
2. Is the higher-timeframe trend aligned with my direction? (regime gate)
3. Has the signal candle **closed** with the flip? (no live-dot action — it updates intrabar)
4. Have I accounted for the **wide first stop** right after the flip in my sizing?
5. On a volatile alt, have I **lowered the AF max** and set an [[atr]]-based initial stop?
6. Am I comfortable being **always-in**, or should I use SAR in stop-only mode here?

## Getting the Data (CryptoDataAPI)

Parabolic SAR is computed from the OHLC series (highs/lows drive the EP and the recursion) — pull klines and calculate the dots yourself on closed candles.

**Live / recent candles:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=4h&limit=1000` — Binance spot OHLCV for computing SAR.
- `GET /api/v1/hyperliquid/candles?coin=ETH&interval=4h&limit=1000` — Hyperliquid perp OHLCV.

**Related computed indicator state (filter):**
- `GET /api/v1/indicators/signum-rgg` — ADX(14)+DMI RED/GREY/GREEN state, useful as the SAR trend filter.

**Historical archive (backtesting):**
- `GET /api/v1/backtesting/klines` — full OHLCV archive (Parquet since 2020) for backtesting SAR flips on closed bars.

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ETHUSDT&interval=4h&limit=1000"
```

Auth: `X-API-Key` header. Endpoint catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]], [[cryptodataapi-indicators]], [[cryptodataapi-hyperliquid]].

## Key Takeaways

- Parabolic SAR is a **stop-and-reverse trailing stop** (Wilder, 1978): dots below price = uptrend, above = downtrend, always in the market.
- Its signature is the **Acceleration Factor** (0.02 → 0.20), which tightens the stop as a trend makes new extremes.
- The **dot flip** simultaneously exits and reverses; SAR can also be used purely as a **stop-only** trail on positions entered elsewhere.
- It has **no volatility input**, so fixed AF behaves inconsistently across crypto regimes — lower the AF max on volatile alts and add an [[atr]] stop.
- **Closed bars are fixed**, but the live dot updates intrabar; a touch-based trigger makes SAR easy to pick off by liquidation wicks.
- Its dominant weakness is **relentless whipsaw in ranges** — an [[adx]] > 25 or higher-timeframe filter is essential, not optional.
- Return shape is **low win rate with asymmetric winners** (illustrative ~44.7% in one equity study); value is in the risk/reward asymmetry.

## Related

- [[supertrend]] — a modern ATR-based alternative serving a similar trailing-stop role, with volatility scaling SAR lacks
- [[adx]] — Wilder's companion indicator; the essential SAR trend filter
- [[atr]] — another Wilder creation, useful for calibrating stops alongside SAR
- [[trailing-stop]] — the general concept SAR implements
- [[moving-average-crossover]] — a slower, less whipsaw-prone trend approach
- [[volatility]] — the regime input SAR ignores but that governs its whipsaw risk
- [[j-welles-wilder]] — SAR's creator, from the same 1978 book as RSI and ADX
- [[bitcoin]] — primary crypto instrument for SAR trend-reading

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — win-rate/backtesting characterization of Parabolic SAR as a trend-following/exit system

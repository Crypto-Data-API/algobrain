---
title: "Gap Trading"
type: strategy
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [technical-analysis, day-trading, swing-trading, breakout, stocks]
aliases: ["gap trading", "gap and go", "gap fill", "gap fade", "trading gaps", "opening gap"]
strategy_type: technical
timeframe: intraday|swing
markets: [stocks, futures, crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, structural, informational]
edge_mechanism: "Overnight news repriced at the open creates an order imbalance; the gap either runs as fresh information attracts momentum (continuation) or reverts as the imbalance was an overreaction (fill)"
data_required: [ohlcv-daily, ohlcv-intraday, premarket-volume, earnings-calendar]
crowding_risk: medium
related:
  - "[[support-and-resistance]]"
  - "[[breakout-trading]]"
  - "[[volume]]"
  - "[[vwap]]"
  - "[[gap-risk]]"
  - "[[earnings-calendar]]"
  - "[[trend]]"
  - "[[mean-reversion]]"
  - "[[stop-loss]]"
  - "[[atr]]"
  - "[[swing-high]]"
  - "[[swing-low]]"
---

**Gap trading** exploits the price gap that forms when a security opens at a materially different price than its previous close, leaving an empty "gap" on the chart with no trading in between. Gaps are caused by an order imbalance that builds while the market is closed — most often from overnight news, earnings, or macro events — and traders take one of two opposing stances: **gap-and-go** (trade in the direction of the gap, betting the move continues) or **gap fade / gap fill** (trade against it, betting price retraces to "fill" the gap back to the prior close). Which stance is correct depends almost entirely on the *type* of gap and the [[volume]] and context surrounding it.

## Edge source

Gap trading draws on three of the categories in the edge taxonomy:

1. **Informational.** A true catalyst gap (earnings beat, guidance change, merger, drug approval) reflects genuinely new information that the market is still digesting. The earliest, most aggressive repricing happens at the open; continuation traders are paid for taking on the direction the news implies before the slower money fully reacts.
2. **Behavioral.** Many gaps — especially small ones with no hard catalyst — are overreactions to overnight sentiment, thin pre-market liquidity, or a single large order. These tend to mean-revert and "fill," paying the fade trader who supplies liquidity against the panic or euphoria.
3. **Structural.** The opening auction concentrates a day's worth of accumulated overnight orders into one print, creating a measurable imbalance and a burst of liquidity that defines the day's early range. The gap level and the prior close become reference points other participants anchor to.

The strategy has **no latency edge** for a discretionary trader and depends heavily on correctly classifying the gap — which is where most of the difficulty (and most of the losses) lie.

## Why this edge exists

Markets are closed for the majority of each 24-hour cycle, but information is not. Earnings are reported after the close or before the open precisely so the market has time to absorb them in the auction rather than mid-session. The result is that the open is the single point where overnight supply and demand collide. Two persistent human tendencies create the opportunity:

- **Underreaction to genuine news** (the post-earnings-announcement drift family of effects) means a real catalyst gap often *keeps going* in its direction for hours or days as analysts revise and slow money repositions — favouring continuation.
- **Overreaction to noise** means a gap with no real catalyst, on thin pre-market volume, is frequently an emotional or liquidity-driven dislocation that the regular session corrects — favouring the fade.

The trader's job is to distinguish which regime they are in, using volume, the presence/absence of a catalyst, and the location of the gap relative to [[support-and-resistance]] and the prevailing [[trend]].

## Types of gaps

| Gap type | Where it occurs | Typical behaviour | Bias |
|----------|-----------------|-------------------|------|
| **Common gap** | Inside a range, no catalyst | Usually fills quickly | Fade / fill |
| **Breakaway gap** | Out of a base or through major [[support-and-resistance]], on a catalyst + heavy volume | Starts a new trend; often does *not* fill | Continuation |
| **Runaway (continuation) gap** | Mid-trend, in the direction of an established move | Confirms trend strength; often does not fill | Continuation |
| **Exhaustion gap** | Late in an extended trend, on climactic volume | Marks a top/bottom; tends to reverse | Fade |
| **Earnings gap** | At the open after a report | Direction set by the surprise; can run or fill | Depends on volume/follow-through |

The single most useful tell is **volume**: a breakaway or runaway gap is validated by volume well above average, while a low-volume gap with no news is a fill candidate.

## Null hypothesis

Under a random walk with no information content, a gap would have no directional edge: continuation and fill would be roughly equally likely and, after costs, expectancy would be negative. The observed, exploitable behaviour is regime-dependent — high-volume catalyst gaps continue more often than chance, while low-volume no-news gaps fill more often than chance. A backtest showing a *single* rule ("always fade gaps" or "always chase gaps") with a high win rate across all gap types is almost certainly overfit; the edge lives in the *classification*, not in a blanket direction.

## Rules

### Gap-and-go (continuation)

- **Setup:** Stock gaps up out of a base or in the direction of its [[trend]], on a real catalyst and heavy pre-market/opening [[volume]].
- **Entry:** Buy a break of the opening-range high (e.g. the first 5–15 minute high) or a hold above the gap level and [[vwap]].
- **Stop:** Below the opening range, the gap level, or [[vwap]] — whichever defines invalidation.
- **Target:** Trail with [[atr]] or prior [[swing-high|swing highs]]; continuation gaps can run all session.

### Gap fade / fill

- **Setup:** Stock gaps against its trend or with no clear catalyst, on unremarkable volume, into an established [[support-and-resistance]] level.
- **Entry:** Fade the open once momentum stalls (e.g. failure to make new highs, rejection candle), targeting the prior close (the fill).
- **Stop:** Beyond the pre-market extreme; gaps that *don't* fill can run hard, so the stop must be respected.
- **Target:** The prior session's close (full fill) or the halfway point (partial fill).

Position sizing for both: risk a fixed small percentage of capital per trade and let the wide-but-defined gap structure set the [[stop-loss]] distance.

## Implementation pseudocode

```python
# Discretionary-style gap classifier sketch (not investment advice)
def classify_gap(bar, prev_close, avg_volume, has_catalyst, trend, level_context):
    gap_pct = (bar.open - prev_close) / prev_close
    if abs(gap_pct) < 0.005:
        return "no_trade"                      # too small to matter
    strong_volume = bar.premarket_volume > 1.5 * avg_volume
    with_trend = (gap_pct > 0 and trend == "up") or (gap_pct < 0 and trend == "down")

    if has_catalyst and strong_volume and (with_trend or level_context == "breakaway"):
        return "gap_and_go"                    # trade WITH the gap
    if (not has_catalyst) and (not strong_volume) and level_context == "into_resistance":
        return "gap_fade"                      # trade AGAINST the gap toward fill
    return "wait"                              # ambiguous: stand aside

# Execution then keys off the opening range (e.g. first 15 minutes) and VWAP:
#   gap_and_go -> buy opening-range break, stop below VWAP/gap, trail to swing highs
#   gap_fade   -> short failure of the open, target prior close (the fill)
```

## Indicators / data used

- Previous close and the opening price (defines the gap and its size)
- Pre-market and opening [[volume]] vs average volume (the key validation filter)
- The **opening range** (first 5–15 minutes) for breakout/failure triggers
- [[vwap]] as the intraday line in the sand between buyers and sellers
- [[support-and-resistance]] and [[trend]] context to locate the gap
- [[earnings-calendar]] and a news feed to know whether a real catalyst exists
- [[atr]] for stop and target sizing

## Example trade

A stock closed at $40. Overnight it reports an earnings beat and raised guidance, and opens at $44 (a +10% breakaway gap) on roughly three times its average opening volume, clearing a multi-month resistance shelf at $41. A gap-and-go trader waits for the first 15-minute range to form ($43.80–$44.60), buys the break above $44.60, and places a stop under [[vwap]] near $43.50. Price trends up through the session to $47 as the new information attracts momentum buyers; the trader trails the stop under intraday [[swing-low|swing lows]] and exits into the close.

Contrast with a fade: the same stock, on a quiet day with no news, gaps up $0.60 to $40.60 on below-average volume directly into the $41 resistance it has rejected three times. With no catalyst and weak volume, a fade trader shorts the failure of the open and covers near the prior close of $40 (the fill). (Both are illustrative scenarios, not recorded trades.)

## What kills this strategy

- **Misclassification.** Fading a breakaway gap that keeps running, or chasing an exhaustion gap that reverses, is the dominant way to lose. The whole edge is in correct classification.
- **Gaps that don't fill.** The popular belief that "all gaps get filled" is false; strong catalyst gaps can take months to fill or never do. A fade with a loose stop can suffer outsized losses — this is the [[gap-risk]] that the strategy directly courts.
- **Thin pre-market liquidity.** Wide spreads and slippage at the open erode the edge, especially in small caps where the gap is largest.
- **Crowding and front-running.** Opening-range-breakout and gap-fill setups are widely known; algorithms react in milliseconds, so discretionary fills are often worse than the backtest assumes.
- **Overnight risk on swing holds.** Holding a gap trade overnight re-exposes the position to the same gap risk in the opposite direction.

## Kill criteria

Pause or revise the approach if: the win rate on *classified* setups deteriorates over a meaningful sample; fades are repeatedly stopped out by non-filling catalyst gaps (sign the classifier is broken); or realised slippage at the open consistently exceeds the planned risk per trade.

## Advantages

- Catalysts concentrate opportunity into a predictable, well-defined moment (the open).
- Clear structural reference points — the gap level, prior close, opening range, [[vwap]] — make stops and targets objective.
- Works across stocks, futures, and crypto, and on both intraday and swing horizons.

## Disadvantages

- Requires fast, disciplined execution and accurate gap classification; unforgiving of hesitation.
- The "gaps always fill" myth lures beginners into fading strong trends — a classic blow-up.
- Heavily reliant on pre-market data, news/[[earnings-calendar]] awareness, and tight spreads.
- Crowded and partly automated; the easy version of the edge is largely arbitraged.

## Related

- [[gap-risk]] — the overnight risk this strategy both exploits and is exposed to
- [[breakout-trading]] — gap-and-go is a breakout variant off the opening range
- [[support-and-resistance]] / [[trend]] — context that determines fade vs follow
- [[vwap]] — the key intraday reference line for gap setups
- [[volume]] — the primary filter separating real gaps from noise
- [[earnings-calendar]] — the most common gap catalyst
- [[mean-reversion]] — the logic behind the gap-fill side of the trade
- [[opening-range-breakout]] — closely related intraday execution method

## Sources

- Murphy, John J. *Technical Analysis of the Financial Markets* — classification of common, breakaway, runaway, and exhaustion gaps.
- Edwards, R. & Magee, J. *Technical Analysis of Stock Trends* — original taxonomy of price gaps and their trend implications.
- Bulkowski, T. *Encyclopedia of Chart Patterns* — empirical study of gap behaviour and fill tendencies.

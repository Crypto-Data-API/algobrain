---
title: "ARC (Area-Range-Candle) Strategy"
type: strategy
created: 2026-06-19
updated: 2026-06-21
status: excellent
tags: [technical-analysis, day-trading, breakout, mean-reversion, momentum]
aliases: ["ARC Strategy", "Area Range Candle", "Area-Range-Candle", "ARC day trading"]
related: ["[[box-and-swing-structure]]", "[[john-wick-candle]]", "[[support-and-resistance]]", "[[candlestick-patterns]]", "[[liquidity-pools]]", "[[vwap]]", "[[initial-balance]]", "[[ninjatrader]]"]
strategy_type: technical
timeframe: intraday
markets: [stocks, futures, forex, crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, structural]
edge_mechanism: "Retail reversal trades at prior-day/swing levels where stop-order liquidity clusters; the counterparty is late breakout traders and swept stops."
data_required: [ohlcv-intraday, pre-market-data]
min_capital_usd: 2000
capacity_usd: 5000000
crowding_risk: medium
expected_sharpe: null
expected_max_drawdown: null
breakeven_cost_bps: null
---

> **Disambiguation.** "ARC" here means the **Area-Range-Candle** discretionary price-action *day-trading method* popularised on YouTube. It is unrelated to **ARC/USDT**, the crypto token/perpetual-futures pair traded on Binance Futures — the two share only an acronym (Source: [[2026-06-19-gap-finder-arc-strategy]]).

> **Not investment advice.** ARC is a discretionary retail strategy. The rules below are documented from its popularised description; there is **limited independent backtest evidence**, and the headline performance claims attached to it ("$1k/day") are promotional and unverified. Treat it as a framework to study and test, not a validated edge.

The **ARC strategy** is a three-step intraday method that trades reversals from a small set of institutional levels. The name is an acronym for its sequence: define the **A**rea (key levels from the prior day and nearest swings), measure the **R**ange (use the box height as both a movement filter and a target), and wait for a **C**andle (a long-wick "John Wick" reversal candle at a level) before entering (Source: [[2026-06-19-gap-finder-arc-strategy]]).

## At a glance

| Attribute | Value |
|-----------|-------|
| Method type | Discretionary intraday price-action reversal |
| Sequence | **A**rea → **R**ange → **C**andle (strict order) |
| Direction | Counter-trend (fade) at key levels |
| Edge source | Behavioral + structural (stop-liquidity sweeps) |
| Markets | Equities, futures, forex, crypto (market-agnostic) |
| Timeframe | Intraday (typically 1-5 min execution, daily levels) |
| Indicators | None core; price + levels only |
| Backtest status | **Untested** — no independent walk-forward evidence |
| Headline claims | "$1k/day" — promotional, **unverified** |
| Crowding risk | Medium (obvious, widely-shared levels) |

## Edge source

ARC draws on **behavioral** and **structural** edges (see [[edge-taxonomy]]). The behavioral component is that retail and institutional flow concentrates at obvious reference prices — the prior day's high/low and the nearest swing high/low — and that late participants chase breakouts beyond those levels. The structural component is **stop-order liquidity**: clusters of resting stops sit just beyond key levels, and the long wicks ARC trades into are the footprint of those stops being swept (see [[liquidity-pools]], [[stop-hunting-and-liquidity-sweeps]] and [[john-wick-candle]]) (Source: [[2026-06-19-gap-finder-arc-strategy]]).

| Edge component | Mechanism | Who is on the other side |
|----------------|-----------|--------------------------|
| **Behavioral** | Participants anchor to memorable prices (prior-day H/L, swings); breakout chasers pile in past the level | Late breakout buyers/sellers |
| **Structural** | Resting stop clusters just beyond levels get swept; the sweep leaves a long wick | Earlier counter-trend traders whose stops were run |
| **Mean-reversion overlay** | After the sweep exhausts, price reverts into the prior range | Trapped participants forced to cover |

## Why this edge exists

Markets repeatedly transact at a handful of memorable prices because participants anchor decisions to them. The trader on the other side of an ARC entry is typically a **breakout buyer** (or seller) who entered as price pushed past the level, plus the stops of earlier counter-trend traders. When aggressive flow exhausts itself sweeping that liquidity, price reverses back into the prior range — leaving a long wick. ARC tries to enter *after* the sweep, with the swept participants now trapped and forced to cover. This is the same mechanism formalised by "liquidity pool" indicators that mark long-wick zones as magnets for future price.

## Null hypothesis

Under no edge, prior-day and swing levels carry no information, long wicks form randomly, and a "20% of range" pre-move filter selects no better than random entries. Expected outcome: win rate and payoff near break-even after costs, with results indistinguishable from random level-touch entries. Because ARC has **not been independently walk-forward tested**, this null is not yet rejected — a serious adopter should encode the rules and backtest them before trusting the discretionary version.

## Rules

ARC is applied in strict order — Area, then Range, then Candle (Source: [[2026-06-19-gap-finder-arc-strategy]]).

### 1. Area — the four levels

Only four levels matter; everything between them is "no man's land" to be avoided (see [[box-and-swing-structure]]):

- **Box high** — prior day's regular-session high
- **Box low** — prior day's regular-session low
- **Swing high** — the *next* prominent high above the box high (scan back left to find it, regardless of when it occurred)
- **Swing low** — the *next* prominent low below the box low

Rule: **sell at / above / near the box high or swing high; buy at / below / near the box low or swing low.** Do not trade in the middle.

**Gap handling.** If the day gaps *above* the prior box, treat the prior box as obsolete and draw a fresh box from the **pre-market high and pre-market low**, then locate new swing levels beyond it. Mirror the logic for gap-downs. (See [[box-and-swing-structure]].)

### 2. Range — filter and target

- Measure **box range = box high − box low**.
- **Minimum-move filter:** require an *unabated, uninterrupted* move of at least **20% of the box range** in one direction before considering a reversal setup. (Example: a \$3.00 box → \$0.60 minimum move.)
- **Target:** **50-100% of the box range**, often aligned with the opposite box or swing level. (Example: a \$3.00 box → \$1.50-\$3.00 target.)

### 3. Candle — the entry trigger

After the range move unfolds *at* a level, wait for a **[[john-wick-candle|long-wick "John Wick" candle]]** — a hammer or inverted hammer whose long shadow shows rejection at the level.

- For a **short** at the box/swing high: a candle with a long *upper* wick rejecting higher prices.
- For a **long** at the box/swing low: a candle with a long *lower* wick rejecting lower prices.
- **Entry / stop:** stops are placed just beyond the confirming candle's wick. Continuation vs reversal is judged by whether subsequent price trades *above the wick high* (buyers in control) or *below the wick low* (sellers back in).

## Implementation pseudocode

```text
# Daily setup
box_high  = prior_session_high
box_low   = prior_session_low
if gap_up or gap_down:
    box_high = premarket_high
    box_low  = premarket_low
swing_high = nearest_high_above(box_high)
swing_low  = nearest_low_below(box_low)
box_range  = box_high - box_low

# Intraday loop
for bar in session:
    near_resistance = close >= box_high or close >= swing_high
    near_support    = close <= box_low  or close <= swing_low

    moved_enough = one_way_move_since_level() >= 0.20 * box_range

    if near_resistance and moved_enough and is_john_wick(bar, side="upper"):
        enter_short(stop = bar.high + buffer,
                    target = entry - rand(0.5, 1.0) * box_range)

    if near_support and moved_enough and is_john_wick(bar, side="lower"):
        enter_long(stop = bar.low - buffer,
                   target = entry + rand(0.5, 1.0) * box_range)
```

## Indicators / data used

ARC is deliberately **not indicator-heavy** — it is price-action plus levels. Data required: intraday OHLCV and **pre-market** data (for gap-day boxes). Optional contextual overlays used by some traders include [[vwap]]-based trend filters, volume-delta confirmation, and liquidity-pool markers, but none are core to the method (Source: [[2026-06-19-gap-finder-arc-strategy]]).

## Example trade

A stock's prior-session box is \$3.00 wide (box high \$103, box low \$100). The next morning, price trends up an uninterrupted \$0.70 (>20% of \$3.00) into the box high at \$103, where a candle prints with a long upper wick (rejection). The trader shorts on confirmation, places a stop just above the wick high, and targets 50-100% of the box range (\$1.50-\$3.00) toward the box low / swing low. If price subsequently trades *below* the wick low, the short thesis is reinforced; a trade back *above* the wick high invalidates it.

## Performance characteristics

No independent, cost-adjusted performance data exists for ARC specifically. Promotional claims should be discounted. Realistically, an intraday reversal method trading multiple times per session is **highly sensitive to costs** (spread, commission, slippage on stop sweeps) and to the discretionary judgment of what counts as a valid "John Wick" candle or an "unabated" move — both of which resist rigid specification and invite hindsight bias. Any edge must be demonstrated by encoding the rules and walk-forward testing them, not assumed.

**Why cost sensitivity is acute.** A counter-trend intraday method living at the exact zone where stops are swept faces the worst-case slippage profile: entries fire into fast, one-directional flow, and stops sit just beyond the wick — precisely where price is most likely to gap on the next sweep. The frontmatter leaves `expected_sharpe`, `expected_max_drawdown`, and `breakeven_cost_bps` deliberately `null` because no honest figure can be quoted without a real backtest; populating them with promotional numbers would violate the no-fabrication rule.

| Performance dimension | Realistic expectation |
|-----------------------|-----------------------|
| Trade frequency | Multiple per session (high cost drag) |
| Win rate | Unknown; subject to discretionary selection bias |
| Reward:risk | Range-based targets (50-100% of box) vs wick-buffer stops |
| Cost sensitivity | **High** — spread + slippage on swept stops |
| Drawdown driver | Trend days where the fade is run over |
| Validation status | **None** — `null` Sharpe/DD/breakeven by design |

> **Backtesting note.** ARC's discretionary inputs ("John Wick" candle, "unabated" move, "near" a level) must be hard-coded before any backtest is meaningful. See [[backtesting-pitfalls]] and [[overfitting-in-trading]] — the act of systematising subjective rules is where most of the apparent edge tends to evaporate.

## Capacity limits

As a small-cap-capable intraday reversal strategy keyed to a single instrument's prior-day levels, capacity is modest. Entries at swept levels target relatively thin liquidity; scaling size increases slippage on the very wicks the method trades. Estimated capacity is on the order of low single-digit millions per instrument before market impact degrades fills.

## What kills this strategy

- **Trend days / strong range extension.** When price *accepts* beyond a level rather than rejecting it, ARC's fade is run over — the same failure mode as fading a held [[initial-balance]] range extension.
- **Choppy, low-range sessions.** The 20%-of-range filter triggers on tiny moves; entries cluster in noise.
- **Discretionary drift / overfitting.** "John Wick" candle and "unabated move" are subjective; performance evaporates when the judgment is honestly systematised.
- **Crowding.** As more traders fade the same obvious levels, the levels stop holding (medium crowding risk).
- **Cost overrun.** Frequent stop placement just beyond wicks means stops sit in the exact zone of maximum slippage.

## Regime fit

ARC is a **mean-reversion / fade** method and inherits mean-reversion's regime dependence (see [[market-regime]] and [[regime-matrix]]).

| Regime | ARC fit | Why |
|--------|---------|-----|
| Range-bound / balanced | **Good** | Levels hold; sweeps revert into the range |
| Choppy / low-range | Poor | 20%-of-range filter fires on noise; entries cluster |
| Trend day / range extension | **Bad** | Price accepts beyond the level; the fade is run over |
| High-volatility / event | Dangerous | Stops beyond wicks sit in the maximum-slippage zone |

## Kill criteria

| Condition | Action | Reference |
|-----------|--------|-----------|
| Encoded backtest shows no positive expectancy net of realistic costs across multiple instruments/regimes | Do not deploy | [[when-to-retire-a-strategy]] |
| Live rolling 1-month win rate below break-even given chosen reward:risk | Pause | [[live-journal]] |
| Drawdown beyond pre-set discretionary limit (e.g., 15-20% of allocated capital) | Retire | [[risk-management]] |
| Levels stop holding as crowding rises (sweeps no longer revert) | Re-evaluate edge | [[edge-taxonomy]] |

## Advantages

- Simple, memorable, market-agnostic (equities, futures, forex, crypto).
- Few inputs; no indicator stack required.
- Built-in risk framework (stop beyond wick, range-based targets).

## Disadvantages

- Discretionary; hard to test rigorously; prone to hindsight bias.
- **No independent backtest evidence**; promotional performance claims.
- Fails badly on trend days; cost-sensitive; modest capacity.

## Related

- [[box-and-swing-structure]] — the four ARC levels and gap-adjusted box
- [[john-wick-candle]] — the entry-trigger candle
- [[liquidity-pools]] — why long wicks at levels matter
- [[support-and-resistance]] — the broader level framework
- [[candlestick-patterns]] — hammer / inverted-hammer context
- [[initial-balance]] — an alternative way to frame the day's decision zones
- [[vwap]] — optional trend-context overlay
- tradingview / [[ninjatrader]] — platforms ARC traders use
- [[edge-taxonomy]] — the behavioral/structural edge framework ARC draws on
- [[risk-management]] — stop placement and position sizing discipline
- [[stop-hunting-and-liquidity-sweeps]] — the sweep mechanic ARC fades

## Sources

- [[2026-06-19-gap-finder-arc-strategy]] — gap-finder Perplexity deep research (2026-06-19)
- Reference video: https://www.youtube.com/watch?v=T7QN-yqryr4
- General market knowledge

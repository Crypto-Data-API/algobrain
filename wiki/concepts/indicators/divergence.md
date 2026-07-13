---
title: Divergence
type: concept
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [technical-analysis, indicators, momentum]
aliases: ["bullish divergence", "bearish divergence", "hidden divergence", "regular divergence"]
domain: [indicators]
prerequisites: ["[[oscillators]]", "[[trend]]"]
difficulty: intermediate
related:
  - "[[momentum-trading]]"
  - "[[trend]]"
  - "[[cci]]"
  - "[[rsi]]"
  - "[[relative-strength-index]]"
  - "[[macd]]"
  - "[[stochastic]]"
  - "[[relative-strength]]"
  - "[[delta-divergence]]"
  - "[[chaikin-money-flow]]"
  - "[[mcclellan-oscillator]]"
  - "[[support-and-resistance]]"
---

**Divergence** occurs when the price of an asset moves in the opposite direction to a technical indicator that measures the strength behind that move, suggesting momentum is weakening and warning of a possible trend reversal or continuation. It is a core concept in [[momentum-trading]] and one of the most common ways traders use [[oscillators]].

## How It Works

Most divergence is read between price and a momentum [[oscillators|oscillator]] — [[relative-strength-index|RSI]], [[macd|MACD]], [[cci]], or [[stochastic]]. The logic: price extremes (a new high or new low) *should* be accompanied by a corresponding extreme in momentum. When they are not — price makes a fresh high but the oscillator does not — the move is being made with diminishing force, hinting that the prevailing trend is running out of fuel.

The comparison is always between **two pivots** (two swing highs, or two swing lows): you connect the price pivots with a line and the corresponding oscillator pivots with a line, and ask whether the two lines slope the *same* way (no divergence / convergence) or *opposite* ways (divergence).

### Regular (reversal) divergence

- **Regular bullish divergence** — price makes a *lower low* but the indicator makes a *higher low*. Downward momentum is fading; warns of a bottom.
- **Regular bearish divergence** — price makes a *higher high* but the indicator makes a *lower high*. Upward momentum is weakening; warns of a top.

### Hidden (continuation) divergence

- **Hidden bullish divergence** — price makes a *higher low* while the indicator makes a *lower low*. Signals trend *continuation* within an uptrend (a pullback that resumes higher).
- **Hidden bearish divergence** — price makes a *lower high* while the indicator makes a *higher high*. Signals continuation within a downtrend.

A related order-flow-based variant, [[delta-divergence]], applies the same comparison using cumulative buy/sell aggression instead of a lagging oscillator.

### The four types at a glance

| Type | Price action | Indicator action | Signals | Where it's used |
|------|-------------|------------------|---------|-----------------|
| **Regular bullish** | Lower low | Higher low | Reversal up (bottom) | End of downtrend / range lows |
| **Regular bearish** | Higher high | Lower high | Reversal down (top) | End of uptrend / range highs |
| **Hidden bullish** | Higher low | Lower low | Continuation up | Pullback entry in an uptrend |
| **Hidden bearish** | Lower high | Higher high | Continuation down | Pullback entry in a downtrend |

Mnemonic: **regular** divergence compares the *price* extreme that's the more extreme (price makes the new high/low, indicator doesn't → exhaustion). **Hidden** divergence is the reverse (the *indicator* makes the new extreme, price doesn't → the trend is just resting).

### Worked example (regular bearish on RSI)

A stock rallies to a swing high of $52 with [[relative-strength-index|RSI]] printing 78. It pulls back, then rallies again to a *higher* high of $55 — but this time RSI only reaches 68. Price made a higher high; RSI made a lower high. That is textbook regular bearish divergence: the second leg up carried less momentum than the first. A trader notes it as a warning but waits for confirmation — say price losing a rising trendline or closing back below the prior swing — before shorting, because the divergence alone could persist for several more bars.

## How Traders Use It

### Trading Relevance

Divergence is a **leading** signal — it can flag a momentum shift before price confirms it — which is both its appeal and its danger. Practical guidance:

- **It is a warning, not a trigger.** Divergence can persist for a long time in strong trends ("divergence can stay divergent"); price may keep grinding to new highs while the oscillator keeps weakening. Acting on the first sign of divergence in a powerful trend is a classic way to get run over.
- **Combine with confirmation.** Traders pair divergence with a [[support-resistance|support/resistance]] break, a [[candlestick-patterns|candlestick reversal]], a trendline break, or a moving-average cross before committing.
- **Context matters.** Regular divergence works best near the late stage of a trend or in ranging markets; hidden divergence is used to time pullback entries in an established trend.

### Beyond oscillators: divergence everywhere

The same two-pivot logic applies to many non-price series. Traders watch for divergence between price and:

- **Volume-flow indicators** — [[chaikin-money-flow]] or [[obv]] failing to confirm a price high warns the move runs on thinning participation.
- **[[market-breadth|Breadth]] indicators** — a price index making a new high while the [[mcclellan-oscillator]] makes a lower high signals a *narrowing* rally (fewer stocks participating), one of the most reliable distribution warnings.
- **[[relative-strength]]** — a stock making a new high while its ratio versus the index does not, flagging leadership rotation.
- **Order flow** — [[delta-divergence]] using cumulative buy/sell aggression.

## Pitfalls and Limitations

- **Subjectivity.** The analyst chooses which swing highs/lows to compare; different lookbacks or pivot definitions can show divergence where another setting shows none. Two traders can disagree on whether divergence even exists.
- **"Divergence can stay divergent."** In strong trends the oscillator can diverge for weeks while price keeps grinding to new extremes. Acting on the first sign of divergence in a powerful trend is a classic way to get run over — this is the dominant failure mode.
- **It is leading, hence early.** Its value (warning before price confirms) is also its danger: many divergences resolve by the oscillator simply catching up, with no price reversal at all (a "failed" divergence).
- **Not a standalone trigger.** Reliability rises sharply when filtered by [[trend]] context and confirmed by an *independent* signal — a [[support-and-resistance|support/resistance]] break, a [[candlestick-patterns|candlestick reversal]], a trendline break, or a moving-average cross.
- **Timeframe sensitivity.** Divergence on a 5-minute chart is far less significant than the same pattern on a daily chart; higher-timeframe divergences carry more weight.

## Sources

- Murphy, John J. *Technical Analysis of the Financial Markets.* New York Institute of Finance, 1999.
- Pring, Martin J. *Technical Analysis Explained.* McGraw-Hill, 2014.
- Elder, Alexander. *Trading for a Living.* Wiley, 1993.

## Related

- [[relative-strength-index|RSI]], [[macd]], [[cci]], [[stochastic]] — oscillators commonly used to spot divergence
- [[chaikin-money-flow]], [[obv]] — volume-flow series that also produce divergence
- [[mcclellan-oscillator]], [[market-breadth]] — breadth divergence (narrowing rallies)
- [[delta-divergence]] — the order-flow analogue using cumulative delta
- [[relative-strength]] — relative-strength divergence (leadership rotation)
- [[momentum-trading]] — the broader discipline divergence supports
- [[trend]] — divergence is interpreted relative to the prevailing trend
- [[support-and-resistance]] — the confirmation layer divergence is best paired with

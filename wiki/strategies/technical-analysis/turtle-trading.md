---
title: "Turtle Trading"
type: strategy
created: 2026-04-06
updated: 2026-04-20
status: good
tags: [trend-following, breakout, position-sizing, systematic, turtle-traders, richard-dennis]
aliases: ["Turtle Trading System", "Turtle Breakout", "Dennis Turtle Strategy"]
strategy_type: algorithmic
timeframe: swing|position
markets: [futures, commodities, forex]
complexity: intermediate
backtest_status: untested
related: ["[[donchian-channel-breakout]]", "[[atr]]", "[[position-sizing]]", "[[risk-management]]", "[[richard-donchian]]", "[[bill-eckhardt]]", "[[donchian-channels]]"]
---

# Turtle Trading

## Overview

The Turtle Trading system is one of the most famous systematic trading strategies in history. In 1983, legendary commodities trader Richard Dennis bet his partner William Eckhardt that trading could be taught. He recruited a group of novices -- the "Turtles" -- and gave them a complete rule-based system. The Turtles collectively earned over $175 million in profits. The system was later published by Curtis Faith, one of the original Turtles, in his book *Way of the Turtle*.

The core system is a [[donchian-channel-breakout]] combined with [[atr]]-based [[position-sizing]] and strict [[risk-management]]. There are two systems: System 1 (shorter-term, 20-day breakout) and System 2 (longer-term, 55-day breakout). The genius of the strategy lies not just in the entries but in the position sizing using the "N" value (the 20-day [[atr]]), which normalizes risk across different instruments.

## Rules

### Entry (System 1 -- Short Term)
1. **Long:** Buy when price exceeds the 20-day highest high (the upper [[donchian-channel-breakout|Donchian Channel]]).
2. **Short:** Sell short when price drops below the 20-day lowest low.
3. **Filter:** Skip the signal if the previous breakout was profitable (to catch the bigger moves that often follow a failed breakout).

### Entry (System 2 -- Long Term)
1. **Long:** Buy when price exceeds the 55-day highest high.
2. **Short:** Sell short when price drops below the 55-day lowest low.
3. **No filter:** Take every signal regardless of the previous breakout's outcome.

### Exit
1. **System 1 Exit:** Exit longs on a 10-day lowest low. Exit shorts on a 10-day highest high.
2. **System 2 Exit:** Exit longs on a 20-day lowest low. Exit shorts on a 20-day highest high.
3. **Stop-Loss:** 2N (2x the 20-day ATR) from entry price. Non-negotiable.

### Position Sizing (The Key Innovation)
1. Calculate **N** = 20-day exponential moving average of True Range (essentially [[atr|ATR(20)]]).
2. **Dollar Volatility** = N x Dollars per Point.
3. **Unit Size** = 1% of Account / Dollar Volatility. This is one "unit."
4. Maximum 4 units per market, added at 0.5N intervals as price moves favorably (pyramiding).
5. Maximum 12 units in one direction across correlated markets.

## Indicators Used
- [[donchian-channel-breakout|Donchian Channel]] (20-period and 55-period)
- [[atr]] (20-period) for position sizing and stops
- True Range for the "N" calculation

## Example Trade
**Asset:** Crude Oil Futures (CL), daily chart
1. Account: $100,000. CL 20-day ATR (N) = $2.50. Each contract = 1,000 barrels.
2. Dollar Volatility = $2.50 x 1,000 = $2,500.
3. Unit Size = ($100,000 x 1%) / $2,500 = **0.4 contracts** (round to 1 mini contract or adjust with micro).
4. CL breaks above the 20-day high at $78.00. Buy 1 unit at $78.00.
5. Price rises 0.5N ($1.25) to $79.25 -- add unit 2. Repeat at $80.50 (unit 3) and $81.75 (unit 4, max).
6. Stop-loss set 2N ($5.00) below each entry. Lowest stop: $78.00 - $5.00 = $73.00.
7. After 6 weeks, CL hits a 10-day low at $88.00. Exit all units.
8. **Result:** Average entry ~$79.75, exit $88.00 = +$8.25/barrel across 4 units.

## Performance Characteristics
- **Win Rate:** Approximately 35-40%. Most breakouts fail, and the system accepts many small losses.
- **Profit Factor:** 2.0-3.0 historically. The large winners from sustained trends far outweigh the frequent small losses.
- **Expectancy:** Positive due to strict risk management and pyramiding into winners.
- **Drawdowns:** Can be significant (30-40%) during extended choppy periods. The Turtles themselves experienced painful losing streaks.

## Advantages
- Fully systematic -- removes all emotion and discretion from trading
- [[position-sizing]] based on volatility (N) automatically adapts risk across instruments
- Pyramiding into winners maximizes profits during strong trends
- One of the most documented and historically validated strategies available
- Teaches foundational lessons about [[risk-management]] applicable to any strategy

## Disadvantages
- **Low win rate** is psychologically difficult for most traders to endure
- **Extended drawdowns** during range-bound markets can last months
- Requires trading across many uncorrelated markets to achieve the diversification the system was designed for
- The original edge may have diminished since the system became public in 1993
- **Capital requirements** are high for futures markets -- difficult to implement with small accounts

## Leverage and Risk Profile

Turtle position sizing via ATR-normalised "N" units produced effective gross leverage commonly 4×–10× capital across the diversified futures portfolio. Each unit risked approximately 1% of equity per 1N of ATR. The leverage was a natural consequence of futures margin requirements (intrinsic 10–25× via margin) combined with stacking up to 4 units per market across 20+ markets. [[j-welles-wilder|Wilder]] himself emphasised that ATR-based position sizing — not raw leverage — is what separates durable systems from blow-ups (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## See Also
- [[donchian-channel-breakout]] -- the channel system that forms the core of Turtle entries
- [[donchian-channels]] -- indicator concept page for the N-period high/low channels
- [[atr]] -- the volatility measure behind the "N" calculation
- [[position-sizing]] -- the Turtle approach to position sizing is a masterclass
- [[risk-management]] -- the true edge of Turtle Trading
- [[trend-following]] -- the broader philosophy
- [[richard-donchian]] -- creator of the channels underlying the system
- [[bill-eckhardt]] -- Dennis's partner who argued trading required innate talent

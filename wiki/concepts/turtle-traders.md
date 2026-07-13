---
title: "Turtle Traders"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [trend-following, algorithmic, history, education]
domain: [trend-following, risk-management]
difficulty: intermediate
aliases: ["Turtle Traders", "Turtle Trading Experiment", "The Turtles", "turtle-traders"]
related: ["[[turtle-trading]]", "[[trend-following]]", "[[position-sizing]]", "[[breakout]]", "[[richard-dennis]]", "[[bill-eckhardt]]", "[[richard-donchian]]", "[[risk-management]]", "[[systematic-trading]]", "[[donchian-channels]]", "[[donchian-channel-breakout]]", "[[atr]]"]
---

The Turtle Traders were a group of novice traders recruited and trained by legendary commodities trader [[richard-dennis|Richard Dennis]] and his partner [[bill-eckhardt|Bill Eckhardt]] in 1983-1984 as part of a famous experiment to determine whether trading could be taught. The Turtles went on to earn a combined profit of approximately $175 million over five years using a systematic [[trend-following]] strategy, proving that a rule-based approach to trading could be successfully transferred to people with no prior market experience.

## The Experiment

In the early 1980s, Richard Dennis — who had reportedly turned a $1,600 stake into over $200 million trading commodities — had a long-running debate with his partner William Eckhardt. Dennis believed trading could be taught like any other skill; Eckhardt argued that successful trading required innate talent. Dennis funded each Turtle with $200K–$2M to trade the system (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]). To settle the bet, they decided to recruit and train a group of ordinary people.

They placed ads in the Wall Street Journal and Barron's in late 1983, receiving over 1,000 applications. From these, they selected 13 individuals for the first class (January 1984) and 10 more for the second class (December 1984). The recruits came from diverse backgrounds — a professional blackjack player, a fantasy game designer, an accountant, a pianist, and others with no trading experience.

Dennis named them the "Turtles" after visiting turtle farms in Singapore, where he reportedly said: "We are going to grow traders just like they grow turtles in Singapore."

## The System

The Turtles were taught a complete [[trend-following]] system with explicit rules for every decision. The rules were originally kept secret but were published by former Turtle Curtis Faith in 2003 and later in his book *Way of the Turtle* (2007). The system had two variants:

### System 1 (Shorter-Term)
- **Entry**: Buy when price makes a new 20-day high; sell short when price makes a new 20-day low (a [[breakout|Donchian Channel breakout]])
- **Exit**: Exit long positions on a 10-day low; exit short positions on a 10-day high
- **Filter**: Skip a signal if the previous breakout in that market was a winner (since breakouts tend to cluster and many fail)

### System 2 (Longer-Term)
- **Entry**: Buy on a 55-day high; sell short on a 55-day low
- **Exit**: Exit long positions on a 20-day low; exit short positions on a 20-day high
- **Filter**: Take every signal (no skipping)

### Position Sizing (ATR-Based)
The position sizing methodology was arguably the most important part of the system. The Turtles used [[average-true-range|Average True Range]] (ATR), which they called "N," to normalize position sizes across different markets:

- **Unit size** = 1% of account equity / (N x dollar value per point)
- This meant a position in a volatile market like crude oil would be smaller than a position in a less volatile market like corn, ensuring equal dollar risk across all positions.
- **Maximum position**: 4 units per market, 6 units in a single direction across correlated markets, 10 units net long or short overall.

### Stop Losses
- Each unit had a stop loss at 2N (2x ATR) from the entry price.
- As additional units were added (at 0.5N intervals above the entry), stops for all existing units were raised to maintain 2N from the newest entry.

## Markets Traded

The Turtles traded a diversified portfolio of liquid futures markets including U.S. Treasury bonds, Eurodollars, gold, silver, copper, crude oil, heating oil, coffee, cocoa, sugar, cotton, the S&P 500, and several foreign currencies. The diversification was essential — the system expected most trades to be small losses, with a few large winners in strongly trending markets generating the bulk of profits. A typical win rate was around 35-40%, with profits coming from outsized winning trades.

## Results and Legacy

The Turtles collectively earned approximately $150–175 million in profits over the period from 1984 to 1988, averaging roughly 80% per year — one of the most famous trading experiments in history (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]). Some of the most successful Turtles, including Jerry Parker (Chesapeake Capital), Liz Cheval (EMC Capital), and Curtis Faith, went on to manage significant funds and build long careers in trend following.

### Key Lessons

1. **Trading can be taught** — Dennis won the bet. A set of clear rules, combined with discipline, was sufficient for novices to trade profitably.
2. **[[position-sizing]] matters more than entry signals** — The ATR-based sizing and risk limits were the system's core edge, not the breakout entries themselves.
3. **Discipline is the hard part** — Not all Turtles succeeded equally. Those who deviated from the rules — skipping trades, cutting winners short, or sizing positions inconsistently — underperformed. The psychological challenge of following a system through inevitable drawdowns was the true differentiator.
4. **Trend following works but has drawdowns** — The system could lose money for months during choppy, range-bound markets. The ability to stay disciplined during these periods was essential.
5. **Edge decay** — The Turtle system's specific parameters (20-day breakout, etc.) became widely known after publication, and pure Donchian Channel breakout systems have been less profitable in subsequent decades as more capital has pursued similar trend-following signals.

## Related

- [[trend-following]] — the strategy category the Turtle system belongs to
- [[position-sizing]] — the ATR-based sizing methodology that was central to the system
- [[breakout]] — the entry signal type used
- [[systematic-trading]] — the Turtles demonstrated the power of fully rule-based trading
- [[turtle-trading]] — the mechanical strategy page (entry/exit/sizing rules in strategy format)
- [[richard-dennis]] — co-creator of the experiment
- [[bill-eckhardt]] — co-creator who bet against teachability
- [[risk-management]] — the Turtle system's risk controls were its defining feature

## Sources

- Curtis Faith, *Way of the Turtle* (McGraw-Hill, 2007) — first-hand account and the published rules.
- Michael Covel, *The Complete TurtleTrader: How 23 Novice Investors Became Overnight Millionaires* (HarperBusiness, 2007).
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — wiki source summary on the experiment's results and sizing.

---
title: "Elliott Wave Theory"
type: strategy
created: 2026-04-06
updated: 2026-04-20
status: good
tags: [elliott-wave, wave-theory, fractal, fibonacci, impulse-wave, corrective-wave, technical-analysis, swing-trading]
aliases: ["Elliott Wave", "Wave Theory", "EWT", "Ralph Nelson Elliott"]
strategy_type: technical
timeframe: swing
markets: [stocks, crypto, forex]
complexity: advanced
backtest_status: untested
related: ["[[fibonacci-trading]]", "[[wyckoff-method]]", "[[harmonic-patterns]]", "[[support-and-resistance]]", "[[gann-theory]]", "[[ralph-nelson-elliott]]", "[[robert-prechter]]"]
---

# Elliott Wave Theory

## Overview

Elliott Wave Theory, developed by **[[ralph-nelson-elliott|Ralph Nelson Elliott]]** (1871–1948), an American accountant, during an illness-forced retirement in the 1930s, proposes that market prices unfold in recognizable patterns driven by collective investor psychology. Elliott published *The Wave Principle* (1938) and later *Nature's Laws: The Secret of the Universe* (1946). The theory was subsequently popularised by [[robert-prechter|Robert Prechter]] through his *Elliott Wave Theorist* newsletter, which famously called the 1980s bull market (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]). The core principle is that markets move in **five impulse waves** in the direction of the main trend, followed by **three corrective waves** against the trend, forming a complete **5-3 cycle**. The theory is **fractal** in nature -- each wave subdivides into smaller waves of the same pattern, and those waves subdivide further, creating waves within waves across every timeframe. Elliott believed these patterns reflected the natural rhythm of mass psychology, oscillating between optimism and pessimism. The framework is heavily intertwined with [[fibonacci-trading]] ratios, which define the expected relationships between wave lengths. Despite being highly subjective in real-time application, Elliott Wave remains one of the most widely followed analytical frameworks in [[technical-analysis]], particularly among long-term forecasters in stocks, [[crypto]], and [[forex]].

## How It Works

The complete Elliott Wave cycle consists of **eight waves**: five in the motive (trending) phase and three in the corrective phase. In a bull market, waves 1, 3, and 5 move upward (impulse waves), while waves 2 and 4 move downward (corrective waves). The subsequent A-B-C correction retraces a portion of the entire five-wave advance. Each impulse wave itself contains a five-wave subdivision, and each corrective wave contains a three-wave subdivision. This creates a **fractal structure** where the same patterns repeat at the grand supercycle level (decades), the primary level (years), the intermediate level (months), and down to the minute level. Corrective patterns come in several forms: **zigzags** (sharp A-B-C corrections), **flats** (sideways corrections), and **triangles** (converging trendlines). [[fibonacci-trading]] ratios govern wave relationships -- Wave 3 is commonly 1.618x Wave 1, Wave 5 often equals Wave 1, and Wave 2 typically retraces 50-61.8% of Wave 1.

## Rules and Guidelines

### Three Inviolable Rules
1. **Wave 2 cannot retrace more than 100% of Wave 1.** If it does, your count is wrong. Period.
2. **Wave 3 can never be the shortest impulse wave** when compared to Waves 1 and 5. Wave 3 is typically the longest and most powerful wave.
3. **Wave 4 cannot overlap the price territory of Wave 1** (except in diagonal triangles and leveraged markets like [[crypto]]).

### Entry Signals
- **Wave 3 entry:** After identifying a completed Wave 1 advance and Wave 2 correction (retracing 50-61.8% via [[fibonacci-trading]]), enter long at the end of Wave 2. This captures the strongest wave.
- **Wave 5 entry:** After Wave 4 corrects (typically 38.2% of Wave 3), enter long expecting a final push. Riskier -- Wave 5 can truncate.
- **Wave C entry (counter-trend):** After Wave A and Wave B complete in a correction, trade Wave C for a counter-trend move.

### Exit and Stop-Loss
- Stop-loss below the origin of the wave you are trading (e.g., below Wave 2's low when trading Wave 3).
- Target the [[fibonacci-trading]] extension of the wave -- 1.618x for Wave 3, 1.0x (equal to Wave 1) for Wave 5.
- Exit all positions when the five-wave sequence completes and the A-B-C correction begins.

## Example Trade

**Asset:** BTC/USD weekly chart, bull market
1. BTC establishes a clear Wave 1 from $16,000 to $31,000 (+$15,000). Volume expands on the advance.
2. Wave 2 retraces to $22,700 (a 55% retracement of Wave 1 -- within the 50-61.8% [[fibonacci-trading]] zone). A bullish engulfing candle appears.
3. Enter long at $23,000. Stop-loss at $15,800 (below Wave 1 origin -- the inviolable rule).
4. Target Wave 3 at 1.618x Wave 1: $22,700 + ($15,000 x 1.618) = $46,970.
5. BTC rallies to $48,000 in a powerful Wave 3 advance. Take profit on 70% of the position.
6. Wave 4 corrects to $38,500 (38.2% retracement of Wave 3). Re-enter for Wave 5 targeting equality with Wave 1: $38,500 + $15,000 = $53,500.
7. **Result:** Wave 3 trade yielded +$25,000/BTC from a $23,000 entry. Risk-reward approximately 3.5:1.

## Advantages
- Provides a comprehensive framework for understanding market structure at any timeframe and in any market
- Fractal nature allows analysis from minute charts to multi-decade supercycles
- Deep integration with [[fibonacci-trading]] ratios provides objective price targets and retracement zones
- When the count is correct, Wave 3 entries offer exceptional risk-reward ratios
- Helps traders anticipate where a trend is in its lifecycle -- early (Wave 1), middle (Wave 3), or late (Wave 5)
- Well-established body of knowledge with decades of literature and community analysis

## Disadvantages
- **Extremely subjective:** Ten experienced Elliott Wave practitioners can produce ten different wave counts on the same chart
- Real-time wave counting is far harder than retrospective labeling -- you often only know the correct count after the fact
- Multiple valid alternate counts can exist simultaneously, making definitive trade decisions difficult
- The rules have enough flexibility (especially in corrective patterns) that almost any price action can be fit into the theory
- Requires extensive study and experience -- years of practice before reliable application
- Not reliably backtestable due to the subjective nature of wave identification
- Can lead to strong conviction in wrong counts, causing traders to hold losing positions waiting for "their wave" to play out

## Notable Practitioners

[[paul-tudor-jones|Paul Tudor Jones]] used Elliott Wave analysis and classic chart patterns to call and short the 1987 crash, earning approximately 200% that year — one of the most famous applications of Elliott Wave in real-time trading (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## See Also
- [[fibonacci-trading]] -- the mathematical backbone of Elliott Wave relationships
- [[wyckoff-method]] -- another structural approach to market cycles with accumulation/distribution phases
- [[harmonic-patterns]] -- uses similar Fibonacci-based geometric structures
- [[gann-theory]] -- another early 20th-century framework combining geometry, time, and price
- [[smart-money-concepts]] -- modern institutional flow analysis that complements wave structure
- [[ralph-nelson-elliott]] -- Elliott Wave's creator
- [[robert-prechter]] -- popularised Elliott Wave via his newsletter

---
title: Market Breadth
type: concept
created: 2026-04-06
updated: 2026-07-13
status: excellent
tags: [indicators, technical-analysis, market-internals, market-breadth]
aliases: ["breadth indicators", "advance-decline", "market internals", "Market Breadth"]
domain: [indicators]
prerequisites: ["[[trend]]", "[[trading-volume]]"]
difficulty: intermediate
related:
  - "[[cryptodataapi]]"
  - "[[trend]]"
  - "[[divergence]]"
  - "[[relative-strength]]"
  - "[[trading-volume]]"
  - "[[advance-decline-line]]"
  - "[[mcclellan-oscillator]]"
  - "[[breadth-thrust]]"
  - "[[arms-index]]"
  - "[[momentum-breadth]]"
  - "[[vix]]"
---

# Market Breadth

Market breadth measures the degree of participation in a market move — how many individual stocks are advancing versus declining — to assess the health and sustainability of a trend. Because the major indices are cap-weighted, a rising index can mask weakness when only a few mega-cap names are doing the work; breadth indicators reveal that divergence.

## Overview

A market advance supported by the *majority* of its constituents (broad breadth) is structurally healthier than one driven by a handful of large stocks (narrow breadth). Breadth analysis is a form of [[market-microstructure|market-internals]] study: rather than asking "what is the index price?", it asks "how many soldiers are marching behind the generals?" Broad participation tends to precede durable trends, while a narrowing advance — fewer stocks making new highs even as the index climbs — is one of the most reliable early warnings of a market top.

## Key Breadth Indicators

- **[[advance-decline-line|Advance/Decline Line (A/D Line)]]** — a cumulative running total of (advancing issues − declining issues) each day. A rising A/D line that confirms new index highs signals a healthy, broad uptrend; an A/D line that fails to confirm new highs flags a [[divergence]].
- **New Highs vs. New Lows** — the count of stocks making 52-week highs versus 52-week lows. Expanding new highs confirms strength; a surge in new lows during a rally is a red flag. The Hindenburg Omen formalizes a simultaneous spike in both as a fragility signal.
- **Percentage of Stocks Above a Moving Average** — e.g., the % of S&P 500 stocks above their 50-day or 200-day [[moving-averages|MA]]. Readings below ~20% often mark oversold capitulation; above ~80% mark overbought breadth.
- **[[mcclellan-oscillator|McClellan Oscillator]]** — created by Sherman and Marian McClellan (1969). Measures breadth momentum as the difference between 19-day and 39-day EMAs of NYSE net advances. Positive = broadening participation (bullish); negative = narrowing (bearish) (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).
- **[[arms-index|Arms Index (TRIN)]]** — created by Richard Arms (1967). The ratio of (advancing/declining issues) to (advancing/declining volume). Counter-intuitively, readings below 1.0 are bullish and above 1.0 bearish; extreme readings (>2.0) often mark capitulation (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).
- **[[breadth-thrust|Breadth Thrust (Zweig)]]** — a 10-day average of advancers ÷ (advancers + decliners) surging from below 0.40 to above 0.615 within 10 trading days. Rare and historically followed by powerful new uptrends (see [[breadth-thrust]]).
- **Up/Down Volume** — total volume in advancing stocks versus declining stocks; a volume-weighted view of participation that ties breadth to [[trading-volume]].

### Formulas and Reference

| Indicator | Formula | Bullish / bearish reading |
|---|---|---|
| [[advance-decline-line\|A/D Line]] | `AD_t = AD_{t−1} + (Advancers − Decliners)` | Rising and confirming new index highs = healthy; failing to confirm = warning |
| A/D Ratio | `Advancers ÷ Decliners` | > 1 = more issues up; extreme (e.g. > 3) = strong thrust |
| Net New Highs | `52wk New Highs − 52wk New Lows` | Positive & expanding = strength; flipping negative in a rally = breakdown |
| % Above 200-day MA | `(# members above 200-day MA) ÷ (total members)` | > 60-70% healthy; < 20% oversold capitulation; > 80% overbought |
| [[mcclellan-oscillator\|McClellan Oscillator]] | `EMA19(net adv) − EMA39(net adv)` | > 0 broadening; < 0 narrowing; ±100 extremes |
| McClellan Summation | running cumulative sum of the McClellan Oscillator | Trend of breadth momentum (above/below zero) |
| [[arms-index\|TRIN]] | `(Adv ÷ Dec) ÷ (Adv Volume ÷ Dec Volume)` | < 1 bullish, > 1 bearish, > 2 capitulation |
| Up/Down Volume Ratio | `Volume in advancers ÷ Volume in decliners` | High ratio days (≥ 9:1) = thrust conviction |

### Worked Example — the A/D Line and a Divergence

Take a simplified 1,000-stock index over three sessions:

| Session | Index level | Advancers | Decliners | Net (A−D) | Cumulative A/D Line |
|---|---|---|---|---|---|
| 1 | 4,000 (start) | 620 | 380 | +240 | +240 |
| 2 | 4,030 (new high) | 540 | 460 | +80 | +320 |
| 3 | 4,055 (new high) | 470 | 530 | −60 | +260 |

By session 3 the **index is making new highs**, yet the **A/D line has turned down** (from +320 to +260) because fewer stocks are participating — declining issues now outnumber advancing ones even as the cap-weighted index rises on a few large names. This price-vs-breadth **[[divergence]]** is the canonical bearish non-confirmation: the "generals" are advancing but the "soldiers" are retreating. (Illustrative numbers only.)

## Trading Relevance

Breadth analysis helps distinguish broad-based rallies (healthy) from narrow rallies driven by a few large-cap names (fragile). The canonical use is **non-confirmation/divergence**: a market making new price highs while the [[advance-decline-line|A/D line]], new-highs count, or [[mcclellan-oscillator|McClellan Oscillator]] deteriorates is a classic warning that the advance is running out of soldiers. [[breadth-thrust|Breadth thrusts]] work the other way — a sudden surge from very few stocks above their MA to a large majority (e.g., the Zweig Breadth Thrust) has historically marked the start of powerful new uptrends. Traders use breadth as **context and confirmation** for index-level and ETF positioning, not as a precise entry trigger.

How practitioners actually deploy it:

- **De-risking overlay.** Systematic books trim gross exposure when % of members above the 200-day [[moving-averages|MA]] rolls under a threshold, treating breadth as a risk-off filter.
- **Confirmation gate.** A breakout in an index is given more weight when up/down volume and the A/D line confirm; a breakout on narrow breadth is faded or sized down.
- **Capitulation hunting.** Washed-out readings (TRIN > 2, % above 200-day MA < 10-20%, surging new lows) are used to *look for* bottoms, not to call them precisely.
- **Sequencing with [[momentum-breadth]].** Pairing breadth with price [[momentum]] turns "how many are participating" into a tradable regime signal — see [[momentum-breadth]] and [[breadth-thrust]].

## Historical Examples

Before many major market tops, breadth begins deteriorating months in advance while indices continue rising on the strength of a few mega-cap names — the 1999-2000 dot-com top, the 2007 pre-GFC top, and the notably narrow mega-cap-tech-led markets of 2021 and 2023-2025 all exhibited this pattern. Conversely, breadth thrusts off the March 2009 and March/April 2020 lows confirmed durable new bull phases.

## Limitations

- Best suited for **index-level** analysis; far less useful for individual-stock trading.
- A **confirming, not timing** tool — narrow breadth can persist for many months before a correction materializes, so it generates frequent "early" warnings.
- Raw advance-decline counts are sensitive to the universe (NYSE includes many interest-rate-sensitive closed-end funds and ETFs, which can distort the line); analysts often use common-stock-only or ratio-adjusted versions.

## Sources

- John J. Murphy, *Technical Analysis of the Financial Markets* (NYIF, 1999) — market-internals and breadth chapter.
- Gregory Morris, *The Complete Guide to Market Breadth Indicators* (McGraw-Hill, 2005) — comprehensive catalog of breadth measures.
- Martin Zweig, *Winning on Wall Street* — the Zweig Breadth Thrust.
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — McClellan Oscillator and Arms Index construction.
- General market knowledge — A/D-line worked example, formula table, and divergence interpretation are standard technical-analysis material.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-health/summary` — dual health scores + sentiment
- `GET /api/v1/market-health/altcoin-breadth` — % of coins above N-day MA (default 200)

**Historical data:**
- `GET /api/v1/market-health/history?days=730` — historical health scores

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-health/altcoin-breadth"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-health]].

## Related

- [[advance-decline-line]] -- the foundational cumulative breadth measure
- [[divergence]] -- the primary breadth signal (price vs. participation)
- [[mcclellan-oscillator]] -- breadth momentum oscillator
- [[breadth-thrust]] -- the bullish regime-shift breadth signal
- [[arms-index]] -- volume-weighted breadth indicator
- [[momentum-breadth]] -- breadth combined with price momentum
- [[trading-volume]] -- up/down volume breadth
- [[relative-strength]] -- per-stock leadership that aggregates into breadth
- [[trend]] -- breadth confirms or warns of trend health
- [[vix]] -- complementary fear/internals gauge

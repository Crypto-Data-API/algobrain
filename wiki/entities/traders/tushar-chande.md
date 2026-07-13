---
title: "Tushar Chande"
type: entity
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [person, technical-analysis, indicators, momentum, quantitative]
entity_type: person
aliases: ["Chande", "Tushar S. Chande"]
website: "https://chandeindicators.substack.com"
related: ["[[aroon]]", "[[chande-momentum-oscillator]]", "[[vidya]]", "[[rsi]]", "[[stochastic-oscillator]]", "[[stochrsi]]", "[[moving-average]]", "[[momentum-(indicator)]]", "[[adaptive-indicators]]", "[[backtesting]]", "[[trading-system-design]]"]
---

# Tushar Chande

Tushar S. Chande is an engineer-turned-quantitative trader and one of the most prolific technical-indicator designers of the 1990s. He created the [[aroon|Aroon]] indicator, the [[chande-momentum-oscillator|Chande Momentum Oscillator (CMO)]], the Variable Index Dynamic Average ([[vidya|VIDYA]]), and QStick, and co-developed [[stochrsi|StochRSI]] and the Dynamic Momentum Index with money-management author Stanley Kroll. His unifying theme — that an indicator should *adapt its parameters to current market conditions* rather than rely on a fixed lookback — places him among the founders of [[adaptive-indicators|adaptive technical analysis]]. His indicators ship as standard tools on virtually every modern charting platform, making his work directly relevant to any trader using [[momentum-(indicator)|momentum]] or adaptive trend tools.

## Key Facts

| | |
|---|---|
| **Name** | Tushar S. Chande, PhD |
| **Education** | PhD in engineering, University of Illinois; MBA, University of Pittsburgh |
| **Pre-trading career** | R&D at General Electric; nine US patents (laser-fiber transmission) |
| **Known for** | [[aroon\|Aroon]], [[chande-momentum-oscillator\|CMO]], [[vidya\|VIDYA]], QStick, [[stochrsi\|StochRSI]], Dynamic Momentum Index |
| **Signature theme** | [[adaptive-indicators\|Adaptive]], volatility-responsive indicators and rule-based [[trading-system-design\|system design]] |
| **Books** | *The New Technical Trader* (1994); *Beyond Technical Analysis* (1997/2001) |
| **Co-author** | Stanley Kroll (StochRSI, Dynamic Momentum Index) |
| **Published in** | *Technical Analysis of Stocks & Commodities* (multiple indicators debuted here) |
| **Current activity** | "Chande Indicators" Substack (market analysis) |

## Background

Chande holds a PhD in engineering from the University of Illinois and an MBA from the University of Pittsburgh. Before trading, he worked in research and development at General Electric and holds nine US patents (in laser-fiber transmission technology). He later became a professional trader, money manager, and a regular contributor to *Technical Analysis of Stocks & Commodities* magazine, where several of his indicators were first published. As of the mid-2020s he remains active, publishing market analysis through his "Chande Indicators" Substack.

## Indicators Created

Chande developed [[aroon|Aroon]] in 1995 — the name derives from Sanskrit for "dawn's early light." The indicator measures the time since the most recent N-period high/low to detect emerging trends. Chande also created the [[chande-momentum-oscillator|Chande Momentum Oscillator]] and QStick indicator (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

| Indicator | Year | What it does |
|-----------|------|--------------|
| [[vidya\|VIDYA]] (Variable Index Dynamic Average) | 1992 (*Stocks & Commodities*, March 1992) | A [[moving-average\|moving average]] whose smoothing speed adapts to volatility — faster in trending markets, slower in chop |
| [[chande-momentum-oscillator\|Chande Momentum Oscillator (CMO)]] | 1994 (*The New Technical Trader*) | A pure momentum oscillator bounded -100 to +100; unlike [[rsi\|RSI]] it uses unsmoothed up/down day data in both numerator and denominator |
| QStick | 1994 | Moving average of (close - open), quantifying intraday buying/selling pressure visible in candlesticks |
| [[aroon\|Aroon]] / Aroon Oscillator | 1995 | Measures bars since the N-period high (Aroon Up) and low (Aroon Down) to time trend emergence |
| [[stochrsi\|StochRSI]] (with Stanley Kroll) | 1994 | Applies the [[stochastic-oscillator\|stochastic]] formula to RSI values, increasing sensitivity for overbought/oversold timing |
| Dynamic Momentum Index (with Stanley Kroll) | 1994 | An RSI variant whose lookback period varies with volatility |

### Mechanics of the signature indicators

**Aroon Up / Aroon Down** time how *recently* an extreme occurred within a lookback of N bars (commonly 14 or 25):

```
Aroon Up   = ((N − periods since the highest high in N) / N) × 100
Aroon Down = ((N − periods since the lowest low  in N) / N) × 100
Aroon Oscillator = Aroon Up − Aroon Down
```

If today is the highest high of the window, "periods since" is 0 and Aroon Up = 100; the longer ago the high was, the lower the value. A reading near 100 on Aroon Up with Aroon Down near 0 signals a fresh, strong uptrend; the two crossing flags a possible trend change. Crucially, Aroon measures *time* rather than price magnitude, which lets it detect a new trend's emergence before price-based oscillators react.

**Chande Momentum Oscillator (CMO)** is a pure momentum measure bounded −100 to +100:

```
CMO = 100 × (Sum of up-day changes − Sum of down-day changes)
            ÷ (Sum of up-day changes + Sum of down-day changes)   [over N periods]
```

Where [[rsi|RSI]] smooths its up/down averages (Wilder smoothing) and divides differently, CMO uses raw, *unsmoothed* sums in both numerator and denominator and measures both up and down momentum directly — making it more responsive and symmetric around zero. Readings near +50/+100 indicate strong upside momentum (potentially overbought), near −50/−100 strong downside.

**VIDYA** scales an EMA's smoothing constant by a volatility ratio (Chande originally used CMO magnitude, later standard deviation): when volatility/momentum is high the average tracks price quickly, and in quiet ranges it slows down — reducing whipsaws in chop while staying responsive in trends. It is one of the earliest widely used [[adaptive-indicators|adaptive moving averages]], a lineage that includes Kaufman's KAMA.

## Books

- *The New Technical Trader: Boost Your Profit by Plugging into the Latest Indicators* (with Stanley Kroll, Wiley, 1994) — introduced CMO, StochRSI, QStick, and the Dynamic Momentum Index
- *Beyond Technical Analysis: How to Develop and Implement a Winning Trading System* (Wiley, 1997; 2nd edition 2001) — an early systematic treatment of trading-system design, [[backtesting]], and risk control that anticipated the modern quantitative workflow

## Trading Relevance

Chande's core contribution is the idea that indicators should *adapt* to market conditions rather than use fixed parameters — [[vidya|VIDYA]] and the Dynamic Momentum Index are among the earliest [[adaptive-indicators|adaptive indicators]] in wide use. His [[chande-momentum-oscillator|CMO]] underpins volatility-adjusted momentum screens (and is itself used as the variability input that drives VIDYA), and [[aroon|Aroon]] remains a standard trend-emergence filter. *Beyond Technical Analysis* is frequently cited as a foundational text for retail traders moving from discretionary chart-reading to rule-based [[trading-system-design|system development]].

## Influence and Legacy

Chande helped move retail technical analysis from a collection of fixed-period indicators toward two ideas now considered standard: indicators that *self-adjust to volatility*, and the discipline of treating a trading method as a *system* to be specified, [[backtesting|backtested]], and risk-managed rather than discretionarily interpreted. *Beyond Technical Analysis* (1997) anticipated the modern quantitative workflow — explicit entry/exit rules, position sizing, money management, and out-of-sample testing — years before retail backtesting software made it routine. His indicators are bundled by default in TradingView, MetaStock, NinjaTrader, and similar platforms, and the [[aroon|Aroon Oscillator]] and CMO appear in countless screeners. As an inventor with nine engineering patents who carried an experimentalist's mindset into markets, Chande is a frequently cited example of the engineer-to-quant career path.

## Related

- [[aroon]] — Chande's 1995 trend-timing indicator
- [[chande-momentum-oscillator]] — his bounded pure-momentum oscillator
- [[vidya]] — his adaptive (volatility-scaled) moving average
- [[stochrsi]] — his stochastic transform of RSI (with Kroll)
- [[adaptive-indicators]] — the category his work helped found
- [[rsi]] — the oscillator CMO and StochRSI build upon
- [[stochastic-oscillator]] — basis of the StochRSI transformation
- [[moving-average]] — VIDYA is an adaptive variant
- [[momentum-(indicator)]] — the family his oscillators belong to
- [[trading-system-design]] — the discipline *Beyond Technical Analysis* teaches
- [[backtesting]] — central topic of *Beyond Technical Analysis*

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)
- Chande, T. S. & Kroll, S., *The New Technical Trader*, Wiley, 1994 (ISBN 978-0471597803)
- Chande, T. S., *Beyond Technical Analysis*, Wiley, 1997/2001
- Traders Union biography — PhD (University of Illinois), MBA (Pittsburgh), GE career, nine patents: https://tradersunion.com/persons/tushar-chande/
- Technical Analysis of Stocks & Commodities author archive: http://technical.traders.com/archive/combo/display5.asp?author=Tushar+S+Chande+PhD
- Chande Indicators Substack (current activity): https://chandeindicators.substack.com
- Biography and indicator years verified via Perplexity (sonar) and web search, 2026-06-10

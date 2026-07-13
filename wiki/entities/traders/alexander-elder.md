---
title: "Alexander Elder"
type: entity
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [person, education, technical-analysis, indicators, behavioral-finance]
entity_type: person
founded: 1950
headquarters: "New York, USA"
website: "https://www.elder.com"
aliases: ["Alexander Elder", "Dr. Alexander Elder", "Alex Elder"]
related: ["[[triple-screen-trading-system]]", "[[force-index]]", "[[elder-ray-index]]", "[[trading-psychology]]", "[[risk-management]]", "[[position-sizing]]", "[[technical-analysis]]"]
---

Dr. Alexander Elder (born 1950) is a Soviet-born American psychiatrist-turned-trader, best known as the author of *Trading for a Living* (1993), one of the best-selling trading books ever written. For traders his lasting contributions are the [[triple-screen-trading-system|Triple Screen]] multi-timeframe methodology, the [[force-index|Force Index]] and [[elder-ray-index|Elder-ray]] indicators, and a psychology-first framing of trading ("the markets are a psychological battlefield") that helped found the modern [[trading-psychology]] discipline.

## Key Facts

| Field | Detail |
|-------|--------|
| Born | 1950, Leningrad, USSR (raised in Estonia) |
| Background | Trained psychiatrist; entered medical school at 16; taught at Columbia University |
| Defection | Jumped ship from a Soviet vessel in Abidjan (1974); granted U.S. political asylum |
| Known for | *Trading for a Living* (1993); the [[triple-screen-trading-system\|Triple Screen]] system; [[force-index\|Force Index]] & [[elder-ray-index\|Elder-ray]]; the Impulse System |
| Core thesis | Most traders fail for psychological and money-management reasons, not analytical ones |
| Framework | The Three M's — **Mind** (psychology), **Method** (edge), **Money** ([[risk-management\|risk management]]) |
| Risk rules | The 2% rule (max risk per trade) and the 6% rule (monthly drawdown stop) |
| Ventures | Financial Trading, Inc. (elder.com); co-founder of SpikeTrade (with Kerry Lovvorn) |
| Status (2026) | Alive and active educator; elder.com operating; listed MoneyShow 2026 speaker |

## Overview

Elder was born in Leningrad in 1950 and grew up in Estonia, entering medical school at age 16. Working as a ship's doctor on a Soviet vessel, he jumped ship in Abidjan, Côte d'Ivoire in 1974 and received political asylum in the United States. He worked as a psychiatrist in New York City and taught at Columbia University before becoming a full-time trader and trading educator. His psychiatric training directly shaped his core thesis: most traders fail for psychological and money-management reasons, not analytical ones.

He runs the educational firm Financial Trading, Inc. (elder.com) and co-founded the **SpikeTrade** group with trader Kerry Lovvorn, where members compete on weekly stock picks. As of June 2026 Elder remains active — elder.com still operates, and he is a listed speaker at 2026 MoneyShow events (verified via Perplexity, 2026-06-10).

## Key Books

| Book | Year | Notes |
|------|------|-------|
| *Trading for a Living* | 1993 | International bestseller; psychology, tactics, money management |
| *Come Into My Trading Room* | 2002 | Barron's "Book of the Year"; introduced the 2% and 6% risk rules |
| *Entries & Exits* | 2006 | Visits to 16 real traders' rooms |
| *Sell and Sell Short* | 2008 | Exits and short selling |
| *The New Trading for a Living* | 2014 | Updated edition for electronic markets |

## Core Concepts

- **The Three M's — Mind, Method, Money.** Success requires psychology (Mind), an edge (Method), and [[risk-management|money management]] (Money); most retail traders obsess over Method only.
- **[[triple-screen-trading-system|Triple Screen Trading System]]** (first published in *Futures* magazine, 1986) — analyze three timeframes: the tide (weekly trend, e.g. [[macd|MACD-Histogram]] slope), the wave (daily oscillator pullback against the tide), and the ripple (intraday entry timing). Only trade in the direction of the higher timeframe.
- **[[force-index|Force Index]]** — combines price change and volume to measure the force of bulls/bears behind a move.
- **[[elder-ray-index|Elder-ray]]** — Bull Power and Bear Power: distance of the high/low from a 13-period EMA, gauging the strength of buyers and sellers relative to consensus value.
- **Impulse System** — combines EMA slope and MACD-Histogram into a censorship system that forbids (rather than commands) trades against momentum.
- **2% and 6% rules** — never risk more than 2% of equity on a single trade; stop trading for the month if account drawdown reaches 6%. These rules are widely cited in [[position-sizing]] and [[risk-management]] literature.

### Triple Screen mechanics

The system's core insight is that any single timeframe is **internally contradictory** — an oscillator that says "oversold, buy" on the daily chart may be sitting inside a brutal weekly downtrend. Triple Screen resolves this by ranking timeframes and forcing them to agree before acting:

1. **Screen 1 — the tide (trend).** Take a timeframe one order of magnitude *above* your trading timeframe (a swing trader using daily charts uses the **weekly**). Read a [[trend-following|trend]]-following tool — Elder favors the slope of the weekly [[macd|MACD-Histogram]] or a long EMA. This screen sets the *only direction* you are allowed to trade. Up-tide → longs only; down-tide → shorts only.
2. **Screen 2 — the wave (correction).** Drop to your trading timeframe (daily) and use an **oscillator** ([[force-index|Force Index]], [[stochastic-oscillator|stochastics]], or Elder-ray) to find a pullback *against* the tide. In an up-tide you wait for the oscillator to dip into oversold — i.e. you buy weakness, not strength, but only in an uptrend.
3. **Screen 3 — the ripple (entry).** Use a tight entry technique (a buy-stop above the prior bar's high in an up-tide, sometimes on an intraday chart) so you are triggered only when price actually resumes in the tide's direction, with the protective stop placed just beyond the recent extreme.

The net effect is a disciplined "trend-with-pullback" pattern: trade *with* the higher timeframe, *enter on* a counter-trend dip, and *time* the trigger — a structure now ubiquitous in retail and prop multi-timeframe playbooks.

### Force Index mechanics

The **[[force-index|Force Index]]** quantifies the conviction behind a move by multiplying its size by its participation: **Force Index = (today's close − yesterday's close) × today's volume**. A large up-day on heavy volume yields a large positive value (strong bulls); a small move or thin volume yields a value near zero (no real force). The raw 1-period series is noisy, so Elder smooths it with an EMA: a **2-period EMA** for short-term entry/exit timing (Screen 3 signals) and a **13-period EMA** to confirm the longer trend (Screen 1). Practical reads: a 13-period Force Index above zero and rising confirms bullish power; a new price high *not* confirmed by a new Force-Index high is a [[divergence|bearish divergence]] warning of fading demand; and spikes to extreme negative values often mark capitulation lows. Because it folds [[volume]] into a momentum reading, the Force Index is one of the few classic oscillators that explicitly tests whether price moves are "backed by money."

## Trading Relevance

Elder's framework remains a default reference for discretionary swing traders: multi-timeframe alignment (Triple Screen) is now a standard pattern in retail and prop methodology, his indicators ship in virtually every charting platform (TradingView, MetaTrader, thinkorswim), and his 2%/6% rules are among the most-quoted concrete risk limits in trading education. His psychiatric framing of crowd behavior is an accessible on-ramp to [[behavioral-finance]].

## Related

- [[triple-screen-trading-system]]
- [[force-index]]
- [[elder-ray-index]]
- [[macd]]
- [[stochastic-oscillator]]
- [[divergence]]
- [[volume]]
- [[swing-trading]]
- [[trend-following]]
- [[trading-psychology]]
- [[risk-management]]
- [[position-sizing]]
- [[technical-analysis]]
- [[behavioral-finance]]

## Sources

- Alexander Elder, *Trading for a Living* (Wiley, 1993, ISBN 978-0471592242) and *The New Trading for a Living* (Wiley, 2014).
- Alexander Elder, *Come Into My Trading Room* (Wiley, 2002).
- Official site: https://www.elder.com (bio; accessed June 2026).
- Traders Union biography: https://tradersunion.com/persons/alexander-elder/
- MoneyShow 2026 speaker listing: https://online.moneyshow.com/2024/september/accredited-virtual-expo/speakers/2026spk/dr-alexander-elder/
- Perplexity verification of current status, 2026-06-10 (alive, active educator; no notable 2025-2026 news).

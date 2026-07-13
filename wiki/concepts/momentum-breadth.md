---
title: "Momentum Breadth"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [indicators, technical-analysis, momentum, market-regime]
aliases: ["Breadth Momentum", "Advance-Decline Momentum", "Breadth Thrust"]
related: ["[[momentum-anomaly]]", "[[momentum]]", "[[market-breadth]]", "[[breadth-thrust]]", "[[advance-decline-line]]", "[[mcclellan-oscillator]]", "[[market-cycles]]", "[[regime-detection]]", "[[relative-strength]]", "[[divergence]]", "[[sector-rotation]]", "[[volatility]]", "[[risk-management]]"]
domain: [indicators, technical-analysis]
prerequisites: ["[[momentum]]", "[[indicators]]"]
difficulty: intermediate
---

**Momentum breadth** is the combination of price [[momentum]] with [[market-breadth|market breadth]]: it measures not just *that* an index is moving and *how many* securities are participating, but whether the participation itself is *accelerating or decelerating*. A rally led by hundreds of advancing stocks with breadth still expanding is "broad" and healthy; a rally where the index rises but breadth is fading — carried by a handful of mega-caps — is "narrow" and fragile. Momentum-breadth indicators turn the cross-section of advances, declines, new highs, and stocks above their moving averages into momentum signals about the *internal strength* of a trend. Breadth divergences are among the most reliable early warnings of a [[market-cycles|cycle]] turning, while breadth *thrusts* (see [[breadth-thrust]]) are among the most reliable bullish regime triggers.

> This page focuses on the *fusion* of momentum and breadth. For the underlying breadth indicators themselves (A/D line, McClellan, TRIN, new highs-lows), see [[market-breadth]]; for the specific bullish-thrust signal, see [[breadth-thrust]].

## Why Breadth Matters

A capitalisation-weighted index can rise even as the *typical* stock falls, because a few of the largest constituents dominate the average. In 2023-2024, for example, US large-cap indices made new highs while the median stock lagged badly — the "Magnificent Seven" carried the tape. Breadth strips out this distortion: it asks whether the move is supported by the broad market or by a thinning group of leaders. Narrowing breadth into an index high is a classic **bearish divergence** — the engine is running on fewer cylinders — and historically precedes corrections. Conversely, sudden broad participation off a low (a "breadth thrust") signals a durable regime shift to risk-on.

## Core Breadth Indicators

| Indicator | Construction | Reads as |
|---|---|---|
| **[[advance-decline-line\|Advance-Decline Line (A/D Line)]]** | Running cumulative sum of (advancing issues − declining issues) each day | Rising = broad participation; A/D diverging below a price high = warning |
| **% of stocks above 200-day MA** | Share of index members trading above their 200-day [[moving-averages\|moving average]] | >60-70% = healthy uptrend; falling under 50% while index holds = deterioration |
| **% above 50-day MA** | Same, shorter horizon | Faster, noisier regime gauge |
| **New Highs − New Lows (NH-NL)** | 52-week new highs minus new lows | Expanding new lows in an "uptrend" = internal breakdown |
| **[[mcclellan-oscillator\|McClellan Oscillator]] / Summation Index** | EMA-smoothed (19-day − 39-day) of net advances | Breadth momentum oscillator; zero-line crosses flag thrusts |
| **Up/Down Volume Ratio** | Volume in advancing vs. declining issues | Confirms conviction behind breadth |
| **[[breadth-thrust\|Zweig Breadth Thrust]]** | 10-day MA of advancers/(advancers+decliners) moving from <0.40 to >0.615 within 10 days | Rare, powerful bullish-regime signal |

## Breadth as Momentum

Two distinct uses link breadth to [[momentum]]:

1. **Confirmation / divergence of trend momentum.** When index price momentum is positive *and* breadth momentum (e.g. the A/D line, % above 200-day MA) is also rising, the trend is confirmed. When price makes a higher high but breadth makes a lower high, momentum is *internally* weakening even though price has not yet rolled over. This [[divergence]] is the breadth signal traders watch most.

2. **Breadth thrusts as regime triggers.** A sharp surge from very low to very high participation ([[breadth-thrust|Zweig thrust]], McClellan thrust, or "90% up-volume days" clustering) marks the violent broadening that accompanies the start of a new markup phase in the [[market-cycles|market cycle]]. These are statistically rare and have historically been followed by strong forward 6-12 month returns.

### Worked Example — A Zweig Breadth Thrust

The Zweig Breadth Thrust fires when the 10-day moving average of `advancers ÷ (advancers + decliners)` climbs from **below 0.40** to **above 0.615 within 10 trading days** — i.e. participation goes from washed-out to overwhelmingly broad very fast.

| Day | 10-day MA of A/(A+D) | State |
|---|---|---|
| 0 | 0.38 | Oversold — below 0.40 trigger floor |
| 3 | 0.46 | Rebuilding |
| 6 | 0.55 | Broadening |
| 9 | 0.63 | **Above 0.615 → thrust confirmed** |

Crossing from 0.38 to 0.63 in nine sessions means the *rate of change* of participation — breadth momentum — was extreme: nearly every stock flipped from declining to advancing in under two weeks. That is the signature of a durable risk-on regime change, not a dead-cat bounce. Such signals are rare (a handful per decade) precisely because they require breadth momentum, not just breadth level. (Illustrative numbers only; see [[breadth-thrust]].)

## Trading Relevance

- **Regime detection.** Breadth is a leading internal input to discretionary and quantitative [[regime-detection]]: deteriorating breadth into highs flags distribution; thrusting breadth off lows flags accumulation-to-markup transition (see [[market-cycles]]).
- **Risk management overlay.** Many systematic books reduce gross exposure when the % of stocks above the 200-day MA rolls over below a threshold, treating it as a [[risk-management|risk-off]] filter rather than a precise timing tool.
- **Cross-sectional context for momentum strategies.** Narrow markets crowd [[momentum-anomaly|momentum]] into fewer names, raising concentration and crash risk; broad participation lowers it. Breadth informs how aggressively to size momentum.
- **Sector and factor breadth.** The same logic applies within [[sector-rotation]] and factors: leadership concentrated in one sector is more fragile than broad-based leadership.

### Caveats
Breadth signals are notoriously early — divergences can persist for many months before price confirms (the late-1990s US bull market ran for years on deteriorating breadth). Breadth is a probabilistic context indicator, not a precise trigger; it works best as one input combined with price trend and [[volatility]] regime, not as a standalone signal.

## Related

- [[market-breadth]] — the underlying breadth indicators in detail
- [[breadth-thrust]] — the specific bullish thrust signal
- [[advance-decline-line]] — foundational cumulative breadth measure
- [[mcclellan-oscillator]] — the breadth-momentum oscillator
- [[momentum]] — the price property breadth momentum fuses with
- [[momentum-anomaly]] — the cross-sectional return effect breadth contextualises
- [[market-cycles]] — breadth diverges before cycle phase turns
- [[regime-detection]] — breadth as a regime-classification feature
- [[relative-strength]] — per-stock leadership that aggregates into breadth
- [[divergence]] — the core breadth-vs-price warning pattern
- [[sector-rotation]] — sector-level breadth and leadership
- [[risk-management]] — breadth as a de-risking overlay

## Sources

- McClellan, S. and M. — McClellan Oscillator and Summation Index methodology (mcoscillator.com).
- Zweig, M. — *Winning on Wall Street* — the Zweig Breadth Thrust indicator and breadth-momentum framework.
- Fosback, N. — *Stock Market Logic* — advance/decline and new-high/new-low breadth measures.
- Stockcharts.com / S&P Dow Jones Indices — standard definitions of A/D line, NH-NL, and percent-above-moving-average breadth indicators.
- General market knowledge — the Zweig-thrust worked example and the momentum/breadth fusion framing are standard technical-analysis material.

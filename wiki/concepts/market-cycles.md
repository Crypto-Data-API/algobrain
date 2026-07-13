---
title: "Market Cycles"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [market-regime, behavioral-finance, technical-analysis, regime-detection]
aliases: ["Market Cycle", "Price Cycle", "Sentiment Cycle", "Bull-Bear Cycle"]
related: ["[[business-cycle]]", "[[wyckoff-method]]", "[[market-regime-detection-ml]]", "[[regime-detection]]", "[[behavioral-finance]]", "[[sector-rotation]]", "[[momentum-anomaly]]", "[[mean-reversion]]"]
domain: [market-regime, behavioral-finance]
prerequisites: ["[[behavioral-finance]]", "[[supply-and-demand]]"]
difficulty: beginner
---

A **market cycle** is the recurring four-phase pattern through which an asset's price and the collective sentiment of its participants move — accumulation, markup (uptrend), distribution, and markdown (downtrend) — before repeating. Unlike the [[business-cycle]] (which tracks the *real economy* of GDP, employment, and inflation), the market cycle describes the *price and psychology* cycle of a tradeable instrument, and the two are related but not synchronous: markets typically lead the economy, bottoming before the recession ends and peaking before the expansion does.

## The Four Phases

The canonical framing, formalised by Richard Wyckoff in the early 20th century and echoed by countless technicians since, divides a full cycle into four phases driven by the transfer of supply between "smart money" (informed, well-capitalised participants) and the "public" (late, sentiment-driven participants).

### 1. Accumulation
After a prolonged decline, price stops falling and trades sideways in a range. Sentiment is maximally pessimistic; volume is low and apathetic. Informed buyers absorb the supply being dumped by exhausted sellers without pushing price up (so as not to reveal their hand). This is the bottoming phase — hard to recognise in real time because it looks like more of the same downtrend until it resolves upward. Wyckoff's "spring" (a final false breakdown that shakes out the last weak holders) often marks the end of accumulation.

### 2. Markup (Uptrend)
Price breaks above the accumulation range on rising volume. The trend becomes self-reinforcing: rising prices attract momentum buyers, [[momentum-anomaly|momentum]] and trend-following capital pile in, and media coverage turns positive. Higher highs and higher lows define the structure. Pullbacks are bought. This is where [[trend-following]] and [[momentum-investing]] strategies earn most of their return. Late in the markup, euphoria, leverage, and "this time is different" narratives appear.

### 3. Distribution
Price stalls at high levels and chops sideways in a range, mirroring accumulation but at the top. Smart money quietly sells into the strength of an enthusiastic, fully-invested public. Volatility rises, breakouts fail ("upthrusts"), and breadth deteriorates (see [[momentum-breadth]]) even as headline indices hold up. Sentiment is greedy and complacent. This is the hardest phase to trade because the trend appears intact while internals weaken.

### 4. Markdown (Downtrend)
Price breaks down out of the distribution range. Selling feeds on itself: stop-losses trigger, leverage unwinds, [[margin]] calls force liquidation, and fear replaces greed. Lower highs and lower lows define the structure. Rallies are sold. Capitulation — a high-volume, panic-selling climax — typically marks the transition back toward accumulation, completing the cycle.

## The Sentiment Overlay

Each price phase maps to a recognisable emotional arc, often drawn as the "Wall Street Cheat Sheet": disbelief → hope → optimism → belief → thrill → euphoria (the top) → complacency → anxiety → denial → panic → capitulation → despondency (the bottom) → back to disbelief. The practical lesson from [[behavioral-finance]] is that the points of maximum *financial opportunity* (the bottom) coincide with maximum *emotional pain*, and the points of maximum *risk* (the top) coincide with maximum *comfort*. This is why most participants buy high and sell low — they trade their emotions, not the cycle.

## Cycles Are Fractal and Irregular

Two cautions temper the clean four-phase model:

- **Fractal nesting.** Cycles exist at every timescale. A multi-year secular bull market contains shorter cyclical bears; an intraday session contains its own accumulation and distribution. The phase you identify depends on the timeframe you analyse.
- **No fixed period.** Market cycles are *not* a clock. They do not repeat on a fixed calendar like a sine wave; their duration and amplitude vary enormously (the 2009-2020 equity bull ran ~11 years; the 2020 COVID crash-and-recovery cycle compressed into months). Treating cycles as predictably periodic is the classic error — the pattern is qualitative (phase sequence) not quantitative (fixed length).

## Trading Relevance

The market cycle is the conceptual backbone of regime-aware trading. Different strategies have an edge in different phases:

- **Accumulation / markdown bottoms** favour [[mean-reversion]] and contrarian value entries.
- **Markup** favours [[trend-following]], [[momentum-investing]], and breakout strategies.
- **Distribution** favours reducing leverage, tightening stops, and watching [[momentum-breadth|breadth divergences]] for the regime flip.
- **Markdown** favours short exposure, defensive [[sector-rotation]], cash, and volatility-long positioning.

Quantitatively, classifying the current phase is exactly the problem [[regime-detection]] and [[market-regime-detection-ml]] attempt to solve with HMMs, change-point detectors, and breadth/volatility features. The Wyckoff phase model is the discretionary analogue of those statistical regime labels. Crucially, phase identification is most reliable *after the fact* — the trading challenge is acting on probabilistic, lagged signals near the transitions rather than waiting for confirmation that arrives too late.

## Related

- [[business-cycle]] — the real-economy cycle the market cycle leads
- [[wyckoff-method]] — the formal accumulation/distribution framework
- [[regime-detection]] / [[market-regime-detection-ml]] — quantitative phase classification
- [[behavioral-finance]] — the emotional drivers behind each phase
- [[sector-rotation]] — which sectors lead in each phase
- [[momentum-breadth]] — internal breadth that diverges before phase tops
- [[momentum-anomaly]] / [[mean-reversion]] — strategies matched to phases

## Sources

- Wyckoff, R.D. — *The Richard D. Wyckoff Method of Trading and Investing in Stocks* (1930s); the accumulation/markup/distribution/markdown framework and "composite operator" concept.
- Pring, M.J. — *Technical Analysis Explained* — standard treatment of price cycles and phase analysis.
- Rhea, R. — *The Dow Theory* (1932) — the three-phase (accumulation/public participation/distribution) bull-and-bear framing that predates and parallels Wyckoff.
- National Bureau of Economic Research (NBER) — for the distinction between market cycles and the economic ([[business-cycle|business]]) cycle they lead.

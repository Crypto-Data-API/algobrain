---
title: "John Ehlers"
type: entity
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [person, indicators, technical-analysis, quantitative]
entity_type: person
aliases: ["John F. Ehlers", "Ehlers", "J.F. Ehlers"]
website: "https://mesasoftware.com"
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[frama]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[zero-lag-exponential-moving-average]]", "[[jurik-moving-average]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[kama]]", "[[vidya]]", "[[alma]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[kalman-filter-trading]]", "[[fractal-dimension]]", "[[hurst-exponent]]", "[[microstructure-noise-low-timeframe]]", "[[tushar-chande]]", "[[john-bollinger]]", "[[perry-kaufman]]", "[[alan-hull]]", "[[patrick-mulloy]]", "[[arnaud-legoux]]", "[[mark-jurik]]", "[[technical-analysis]]"]
---

# John Ehlers

John F. Ehlers is an electrical engineer who brought **digital signal processing** into technical analysis, arguing that a market indicator should be designed and judged as a filter — by its frequency response — rather than as an intuitive weighting of past prices. Through MESA Software and four books they introduced cycle-measurement methods and a family of DSP-derived smoothers that are now standard on most charting platforms. Of the fourteen baseline estimators in the [[stretch-revert]] family, **four trace directly to their work**: [[frama|FRAMA]], the [[laguerre-filter|Laguerre Filter]], the [[supersmoother-filter|SuperSmoother]], and (with Ric Way) [[zero-lag-exponential-moving-average|ZLEMA]] — making Ehlers the single most load-bearing name in this vault's estimator layer.

## Key Facts

| | |
|---|---|
| **Name** | John F. Ehlers |
| **Field** | Electrical engineering; digital signal processing applied to markets |
| **Education** | BSEE and MSEE, University of Missouri; doctoral work at George Washington University |
| **Engineering career** | Aerospace and defence electronics, including Raytheon |
| **Firm** | MESA Software (mesasoftware.com) — Chief Scientist and President |
| **Known for** | MESA (Maximum Entropy Spectral Analysis) applied to price series; DSP-based filters and cycle indicators |
| **[[stretch-revert]] baselines** | [[frama\|FRAMA]], [[laguerre-filter\|Laguerre Filter]], [[supersmoother-filter\|SuperSmoother]], [[zero-lag-exponential-moving-average\|ZLEMA]] (with Ric Way) |
| **Books** | *MESA and Trading Market Cycles*; *Rocket Science for Traders*; *Cybernetic Analysis for Stocks and Futures*; *Cycle Analytics for Traders* (Wiley, 2013) |
| **Published in** | *Technical Analysis of Stocks & Commodities* (many indicators debuted there); technical papers hosted at mesasoftware.com |
| **Signature argument** | Conventional moving averages do not remove the high-frequency content they claim to; filter design should start from frequency response |

## Background

Ehlers trained as an electrical engineer, holding BSEE and MSEE degrees from the University of Missouri and completing doctoral work at George Washington University. Their engineering career was in aerospace and defence electronics — antenna and electronic-countermeasures systems work, including a long tenure at Raytheon — before and alongside a second career in markets. They are Chief Scientist and President of **MESA Software**, which publishes their cycle-analysis software and hosts an open archive of their technical papers.

The intellectual pivot is documented in their own retelling: as a newly-arrived engineer in technical analysis, they asked why [[rsi|RSI]] defaults to a 14-day lookback, and were told "because that's what Wells Wilder said to do." That answer — a convention with no stated relationship to the actual rhythm of the data — set off decades of work on the question of what lookback period, if any, is *correct* for a given market at a given time. Ehlers' answer was to measure the market's dominant cycle directly and let indicators inherit their period from it, rather than from habit.

> **Verification note:** the MESA Software biography page returns HTTP 403 to automated fetching. Employer and career details above come from its indexed text and from a *Better System Trader* interview page that was read directly. Ehlers' education and DSP orientation are corroborated across both. No PhD is claimed here — the sources say "doctoral work," not a completed doctorate.

## The central argument

Ehlers' unifying claim is that technical analysis inherited its tools from chart-reading rather than from filter theory, and that this shows up as a specific, measurable defect.

An [[simple-moving-average|SMA]] is usually described as "averaging out the noise." Viewed as a filter, its transfer function is sinc-shaped: a main lobe that passes the trend, followed by **sidelobes** that pass high-frequency content at reduced but non-trivial amplitude — the first sidelobe only about 13 dB down. That leaked content reappears in the output as wiggles that look like market structure and are not. Ehlers' further point about **aliasing** is that on a bar series the shortest resolvable cycle is two bars, so anything faster in the underlying tick process folds back into the bar series as spurious *low*-frequency content that no amount of averaging will remove after the fact.

The practical consequence for this vault is direct: if the baseline in a mean-reversion strategy is itself passing noise, then some measured "stretch" is filter artifact rather than dislocation, and the strategy will fade its own smoother. See [[supersmoother-filter]] for the full treatment.

## Indicators Created

| Indicator | Source | What it does |
|---|---|---|
| [[frama\|FRAMA]] (Fractal Adaptive Moving Average) | *Stocks & Commodities*, October 2005 | An EMA whose smoothing constant is driven by the measured [[fractal-dimension\|fractal dimension]] of the recent price series — fast in trends, heavily smoothed in chop |
| [[laguerre-filter\|Laguerre Filter]] | "Time Warp — Without Space Travel"; *Cybernetic Analysis for Stocks and Futures* | A four-stage Laguerre-polynomial cascade that achieves heavy smoothing from a **very short data window**, with a single damping coefficient (gamma) stretching the effective lookback |
| [[supersmoother-filter\|SuperSmoother]] | *Cybernetic Analysis for Stocks and Futures*; *Cycle Analytics for Traders* (2013) | A two-pole Butterworth-style low-pass filter built specifically to suppress the sidelobe leakage and aliasing described above |
| [[zero-lag-exponential-moving-average\|ZLEMA]] (with Ric Way) | "Zero Lag (Well, Almost)," *Stocks & Commodities*, November 2010 | De-lags the *input* before smoothing — an error-correcting term with a tunable gain that trades between tracking price exactly (no smoothing) and tracking the EMA (full lag) |
| MESA / MAMA / FAMA, Sinewave Indicator, Fisher Transform, and others | *MESA and Trading Market Cycles*; *Rocket Science for Traders*; *Cycle Analytics for Traders* | Cycle-measurement and cycle-adaptive tools; not currently used as [[stretch-revert]] baselines |

**Ric Way** is credited as co-author on the ZLEMA article. No page exists for them in this vault — the public record is too thin to support one.

## Books

- *MESA and Trading Market Cycles: Forecasting and Trading Strategies from the Creator of MESA* (Wiley) — the cycle-measurement framework
- *Rocket Science for Traders: Digital Signal Processing Applications* (Wiley) — DSP concepts for a trading audience
- *Cybernetic Analysis for Stocks and Futures* (Wiley) — source of the Laguerre filter and the SuperSmoother
- *Cycle Analytics for Traders* (Wiley, 2013, ISBN 978-1118728512) — the most recent, and the standard citation for the SuperSmoother derivation and the aliasing argument

## Relevance to this wiki

Ehlers is the primary literature behind **four of the fourteen** [[stretch-revert]] members, which is more than any other single author in the family:

| Family member | Ehlers estimator | Why it was chosen |
|---|---|---|
| `frama_stretch_revert` | [[frama\|FRAMA]] | Adaptive — "extended" self-adjusts with the regime. Currently the family's only meaningfully profitable member |
| `laguerre_stretch_revert` | [[laguerre-filter\|Laguerre]] | EMA-grade smoothness at lower lag, from a short window |
| `hl_supersmoother_stretch_revert` | [[supersmoother-filter\|SuperSmoother]] | Keeps [[microstructure-noise-low-timeframe\|bid-ask bounce]] out of the baseline — *late but clean* |
| `zlema_stretch_revert` | [[zero-lag-exponential-moving-average\|ZLEMA]] | Hugs price, so only violent extensions register as stretch |

Two implications follow, and they point in opposite directions.

**The concentration risk.** The [[stretch-revert]] family's stated defence against estimator-specific artifacts is that a real reversion premium should survive a change of smoother. But four of the fourteen smoothers come from one author and one design philosophy — DSP filter theory — and share assumptions about what counts as noise. They are not fourteen independent opinions; they are closer to a signal-processing cluster, a lag-cancellation cluster ([[hull-moving-average|HMA]], [[triple-exponential-moving-average|TEMA]], ZLEMA), an adaptive cluster ([[kama|KAMA]], [[vidya|VIDYA]], FRAMA), and a regression cluster. Correlated estimators produce correlated signals, which is exactly the [[stretch-revert#Capacity limits|correlated-fills]] concentration the per-member sizing does not see.

**The reproducibility upside.** Everything Ehlers published is *specified*. The formulas, coefficients, and derivations are in the books and in the free papers at mesasoftware.com, so a backtest and a live bot can be checked against each other and against the original. That is the direct contrast with [[mark-jurik]] and [[jurik-moving-average|JMA]], where the algorithm has never been disclosed and no such audit is possible. In a vault whose central worry is [[overfitting]] and unverifiable results, the difference between a published filter and a licensed black box is a first-class property of the baseline, not a footnote.

Ehlers also belongs to a broader lineage this wiki tracks: the move from fixed-parameter indicators toward [[adaptive-moving-averages|adaptive]] ones, alongside [[tushar-chande]] ([[vidya|VIDYA]]) and [[perry-kaufman]] ([[kama|KAMA]]). Where Chande and Kaufman made the smoothing constant respond to volatility or trend efficiency, Ehlers reframed the whole question as filter design — a stricter and more falsifiable framing, since a filter's behaviour can be derived rather than merely observed.

## Related

- [[stretch-revert]] — the strategy family that depends on four of their estimators
- [[frama]] · [[laguerre-filter]] · [[supersmoother-filter]] · [[zero-lag-exponential-moving-average]] — their four baselines in this vault
- [[moving-averages]] · [[adaptive-moving-averages]] — the estimator landscape
- [[simple-moving-average]] · [[exponential-moving-average]] — the conventional filters their argument targets
- [[fractal-dimension]] · [[hurst-exponent]] — the roughness measures FRAMA is built on
- [[microstructure-noise-low-timeframe]] — the noise the SuperSmoother exists to reject
- [[kalman-filter-trading]] — the other state-space/DSP baseline in the family
- [[perry-kaufman]] · [[tushar-chande]] — the adaptive-moving-average lineage
- [[mark-jurik]] · [[jurik-moving-average]] — the proprietary counterexample
- [[alan-hull]] · [[patrick-mulloy]] · [[arnaud-legoux]] — the other baseline authors in the family
- [[john-bollinger]] — band construction around a baseline
- [[technical-analysis]]

## Sources

- John Ehlers, *Cycle Analytics for Traders* (Wiley, 2013, ISBN 978-1118728512) — SuperSmoother derivation and the aliasing/Nyquist argument
- John Ehlers, *Cybernetic Analysis for Stocks and Futures* (Wiley) — Laguerre filter and SuperSmoother
- John Ehlers, *Rocket Science for Traders* and *MESA and Trading Market Cycles* (Wiley)
- John Ehlers, "Fractal Adaptive Moving Averages," *Technical Analysis of Stocks & Commodities*, October 2005 — http://traders.com/documentation/feedbk_docs/2005/10/Abstracts_new/Ehlers/ehlers.html
- John Ehlers, "Time Warp — Without Space Travel" — https://www.mesasoftware.com/papers/TimeWarp.pdf (Laguerre filter)
- John Ehlers and Ric Way, "Zero Lag (Well, Almost)," *Technical Analysis of Stocks & Commodities*, November 2010 — https://www.mesasoftware.com/papers/ZeroLag.pdf
- MESA Software technical-paper archive — https://www.mesasoftware.com/TechnicalArticles.htm
- *Better System Trader* episode 048, "Indicator Lag, DSP and Market Cycles with John Ehlers" — https://bettersystemtrader.com/048-john-ehlers/ (education; the RSI-14 anecdote; DSP orientation)

*Verification note: the mesasoftware.com biography page and the CMT Association presenter page both returned HTTP 403 to direct fetching. Raytheon employment, the "private trader since 1976" claim, and the 1978 MESA-discovery anecdote appear in the indexed text of the MESA bio but were not read from the live page and are stated here only in general terms. No birth year, awards, or completed doctorate are asserted. No source-summary page exists for the Ehlers material in this vault.*

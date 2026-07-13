---
title: "Put/Call Ratio"
type: concept
created: 2026-05-06
updated: 2026-06-21
status: excellent
tags: [options, indicators, behavioral-finance, derivatives]
aliases: ["Put/Call Ratio", "Put-Call Ratio", "P/C Ratio", "PCR"]
domain: [behavioral-finance, indicators]
difficulty: beginner
related: ["[[options-greeks]]", "[[implied-volatility]]", "[[vix]]", "[[put-call-parity]]", "[[max-pain]]", "[[volatility-skew]]", "[[cboe]]", "[[sentiment-analysis]]", "[[market-breadth]]"]
---

The put/call ratio (P/C ratio) is a sentiment indicator computed as the ratio of put option activity to call option activity over a given window, typically using either total volume or open interest. It is most often interpreted as a contrarian gauge: extreme readings of fear (high P/C) or greed (low P/C) tend to precede mean reversion in the underlying market. The ratio is published daily by the [[cboe|CBOE]] for both equity options and broad index options, and the two series carry meaningfully different interpretations.

> **Note:** This page is about the put/call **ratio** (a sentiment indicator). It is *not* the same as [[put-call-parity]], which is a no-arbitrage pricing identity linking call, put, strike, and underlying. The two share three letters and nothing else.

## Overview

A put option benefits from a falling underlying; a call option benefits from a rising underlying. If traders in aggregate buy more puts than calls, the raw demand suggests bearish positioning. The P/C ratio quantifies this:

```
P/C ratio = put activity / call activity
```

"Activity" can mean **volume** (number of contracts traded that day) or **open interest** (total contracts outstanding). Volume-based ratios react quickly and are noisier; open-interest ratios are smoother but laggier.

| Basis | Measures | Responsiveness | Noise | Best for |
|---|---|---|---|---|
| **Volume** | New flow / daily activity | Fast (same-day) | High | Spotting daily fear/greed spikes, intraday extremes |
| **Open interest** | Standing positioning | Slow (accumulated) | Low | Regime classification, slow sentiment shifts |

Most contrarian signal work uses the **volume-based equity P/C** smoothed over 5-21 days; open-interest ratios are more useful for [[max-pain]] and positioning analysis than for timing.

The CBOE publishes three primary daily series:

| Series | Symbol | Universe | Typical interpretation |
|---|---|---|---|
| Total P/C | `$CPC` | All CBOE-listed options | Composite gauge |
| Equity P/C | `$CPCE` | Single-name equity options only | Cleanest retail/speculator sentiment |
| Index P/C | `$CPCI` | Broad index options (SPX, OEX, NDX) | Dominated by institutional hedging |

A reading of `1.0` means equal put and call activity. Equity P/C historically averages around `0.6-0.7`, while index P/C averages closer to `1.5-2.0` because institutions persistently buy index puts as portfolio hedges.

## How it works / Calculation

### Volume-based ratio

```
Equity P/C (volume) = sum(equity put volume) / sum(equity call volume)
```

Computed at the close each session and timestamped. Available intraday from the CBOE in 30-minute increments.

### Open-interest-based ratio

```
P/C (OI) = total put open interest / total call open interest
```

Open-interest ratios are typically computed weekly or monthly and are used for slower-moving sentiment regime classification.

### Smoothing

Raw daily P/C is noisy. Common practice is to apply a moving average (5-day, 10-day, or 21-day) to identify regime-level extremes. Many traders also use a Bollinger-band overlay (P/C +/- 2 standard deviations over a rolling window) to flag statistical extremes.

### Indicator construction (pseudocode)

```python
import pandas as pd

def pc_signal(pc_series: pd.Series, window: int = 21, z_thresh: float = 2.0):
    rolling_mean = pc_series.rolling(window).mean()
    rolling_std = pc_series.rolling(window).std()
    z = (pc_series - rolling_mean) / rolling_std
    # Contrarian: high P/C z-score -> bullish signal; low P/C z-score -> bearish
    bullish = z >  z_thresh
    bearish = z < -z_thresh
    return bullish, bearish
```

## Practical use / Trading applications

### As a contrarian gauge

The orthodox interpretation is contrarian: when fear pushes equity P/C above `1.0`, retail and small speculators are loaded up on puts and historically the market is closer to a bottom than a top. When greed compresses equity P/C below `0.5`, the same crowd is loaded up on calls and the market is more vulnerable.

Rough historical reference points (equity P/C, daily, smoothed):

| Reading | Regime |
|---|---|
| > 1.0 | Capitulation / panic; contrarian buy zone |
| 0.7 - 1.0 | Bearish lean |
| 0.5 - 0.7 | Neutral |
| < 0.5 | Euphoric / complacent; contrarian sell zone |

### Combined with VIX and AAII

P/C is strongest as a signal when it agrees with other sentiment series. A confluence of (1) elevated [[vix|VIX]], (2) high equity P/C, and (3) extreme bearish reading in the AAII sentiment survey is a classic capitulation setup. Conversely, low VIX + low P/C + extreme AAII bullishness is a complacency setup.

#### Confluence signal matrix

The contrarian signal is far more reliable when multiple sentiment series align at an extreme:

| Equity P/C | [[vix|VIX]] | AAII | Composite read | Contrarian implication |
|---|---|---|---|---|
| > 1.0 (high) | Elevated / spiking | Extreme bearish | Capitulation / panic | Contrarian **buy** zone |
| 0.7 - 1.0 | Rising | Bearish lean | Risk-off building | Watch for bottom |
| 0.5 - 0.7 | Mid | Neutral | No edge | Stand aside |
| < 0.5 (low) | Low / suppressed | Extreme bullish | Euphoria / complacency | Contrarian **sell** caution |

Single-series extremes are noise; three-way alignment at an extreme is the historically tradeable configuration (see the October 2008, March 2020 examples below). The same logic underpins composite [[sentiment-analysis]] scores.

### Index versus equity P/C

The two cannot be interpreted the same way:

- **Equity P/C** is dominated by retail and small-trader speculation, so contrarian logic applies cleanly.
- **Index P/C** is dominated by institutional hedging. A high index P/C may simply mean pension funds and mutual funds are rolling their hedges -- it is not a directional bet, and treating it contrarian-bullish is a common mistake.

For sentiment work, equity P/C (`$CPCE`) is the cleaner signal.

### Strategy applications

- **Mean-reversion trade triggers** in oversold/overbought composite scoring
- **Filter for long entries** on broader trend-following systems (avoid buying when complacency is extreme)
- **Volatility-regime input** for systems that switch between long-vol and short-vol postures
- See earnings-plays and earnings-volatility-trading for related volatility-sentiment workflows

## Limitations / What can go wrong

| Pitfall | Effect on the signal | Mitigation |
|---|---|---|
| 0DTE flow | Inflates volume with non-directional gamma/hedging trades | Use a "clean" P/C that excludes 0DTE; lean on equity P/C |
| Hedging vs speculation | A protective put looks identical to a bearish bet | Cross-check with [[volatility-skew]] and dealer positioning |
| Trend regimes | Extremes persist for months without reverting | Require price-action confirmation; never trade standalone |
| Strike heterogeneity | OTM single-name vs ATM index puts counted equally | Use dollar/premium-weighted ratios |
| Methodology drift | CBOE universe changes shift the baseline | Use vintage (point-in-time) data in backtests |

### 0DTE distortion

The explosion of zero-days-to-expiration (0DTE) options on SPX, QQQ, and large-cap names since roughly 2022 has materially distorted modern P/C readings. 0DTE puts and calls are increasingly used for very short-term hedging, gamma trading, and overwriting -- not directional sentiment expression. As a result:

- Index P/C readings are even less informative than they were historically.
- Equity P/C on names with active 0DTE (TSLA, NVDA, AAPL, etc.) is noisier and less reliable as a contrarian signal.
- Some analysts now exclude 0DTE flow when computing a "clean" P/C.

### Hedging vs. speculation is not separable

The raw ratio cannot distinguish between (a) a trader buying a put as a directional bearish bet and (b) a trader buying a put to hedge a long stock position. Two opposite intentions show up identically in the data.

### Trend regimes break contrarian logic

In strong uptrends, low P/C readings can persist for months without producing a top. In bear markets, high P/C readings can persist without producing a bottom. P/C extremes need to be combined with price-action confirmation (e.g., reversal candles, breadth thrusts) rather than used as standalone triggers.

### Not all puts/calls are equal

A deep out-of-the-money put on a single stock and an at-the-money index put trade for very different reasons. Volume-weighted ratios treat them the same. More sophisticated sentiment work uses dollar-weighted or premium-weighted ratios.

### Survivorship and methodology shifts

CBOE has changed the universe of products included in `$CPC` over time, and the introduction of new products (mini index options, weekly options, 0DTE) keeps shifting the baseline. Long-horizon backtests of P/C strategies should use vintage data, not the modern reconstructed series.

## Examples

### October 2008 -- capitulation low

In the October 2008 financial-crisis selloff, the CBOE equity P/C (10-day moving average) spiked above `1.0` on multiple sessions, an extreme rarely seen in modern data. The S&P 500 made its initial selling-climax low in late October 2008, and the eventual final low came in March 2009 on still-elevated P/C readings. Combined with a [[vix|VIX]] reading above 80 and AAII bearish sentiment near record highs, this was a textbook contrarian-bullish confluence.

### January 2018 -- complacency top

In the run-up to the early-February 2018 "volmageddon" event, equity P/C compressed into the low 0.5s for an extended stretch and total P/C dipped well below historical norms. VIX was sitting near multi-decade lows. The S&P 500 then dropped roughly 10% in nine sessions starting late January, with several short-volatility ETPs (XIV, SVXY) blowing up on February 5.

### March 2020 -- COVID panic

Equity P/C 5-day moving average pushed above 0.9 in mid-March 2020 alongside [[vix|VIX]] above 80. The market bottomed on March 23, 2020 -- contrarian signals from P/C, VIX, and breadth all aligned within a few sessions of the low.

### Worked calculation

Suppose on a given day:
- Equity put volume: 12.4 million contracts
- Equity call volume: 18.6 million contracts

```
Equity P/C = 12.4 / 18.6 = 0.667
```

This is near the long-term average -- a neutral reading. Compare against the 21-day moving average (say, 0.62) and rolling standard deviation (say, 0.08): the z-score is `(0.667 - 0.62) / 0.08 = +0.59`, well inside the no-signal band.

## Related

- [[put-call-parity]] -- distinct concept (an arbitrage relationship), not to be confused with the put/call ratio
- [[implied-volatility]]
- [[volatility-skew]]
- [[vix]]
- [[max-pain]]
- [[options-greeks]]
- [[sentiment-analysis]]
- [[market-breadth]]
- [[cboe]]

## Sources

- CBOE -- official daily put/call ratio data publication ($CPC, $CPCE, $CPCI)
- Bernie Schaeffer, *The Option Advisor* -- popularized retail use of equity P/C as a contrarian indicator
- Larry McMillan, *Options as a Strategic Investment* -- chapter on sentiment indicators
- CBOE white papers on the rise of 0DTE and its impact on traditional sentiment indicators (2023-2024)

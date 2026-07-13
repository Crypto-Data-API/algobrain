---
title: "Chaikin Money Flow"
type: concept
created: 2026-04-20
updated: 2026-06-22
status: excellent
tags: [indicators, technical-analysis, volume]
aliases: ["CMF", "Chaikin Money Flow"]
domain: [indicators]
prerequisites: ["[[volume]]", "[[accumulation-distribution]]"]
difficulty: intermediate
related: ["[[marc-chaikin]]", "[[volume]]", "[[obv]]", "[[money-flow-index]]", "[[accumulation-distribution]]", "[[divergence]]", "[[chaikin-oscillator]]", "[[bollinger-bands]]", "[[relative-strength-index]]"]
---

Chaikin Money Flow (CMF) is a volume-based [[oscillators|oscillator]] created by [[marc-chaikin|Marc Chaikin]] in the 1980s. It measures the accumulation/distribution of money flow over a specified period, designed to identify institutional buying and selling pressure (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]). It bounds between −1 and +1 and is read as a gauge of whether a price move is backed by genuine [[volume]] conviction.

## How It Works

CMF is built from the same **Money Flow Multiplier** as the [[accumulation-distribution|Accumulation/Distribution Line]], but normalized over a fixed window so it oscillates around a zero line rather than running cumulatively forever:

```
Money Flow Multiplier (MFM) = ((Close − Low) − (High − Close)) / (High − Low)
Money Flow Volume (MFV)      = MFM × Volume
CMF = Σ(MFV over n periods) / Σ(Volume over n periods)
```

- The **Money Flow Multiplier** locates the close *within* the bar's high-low range. A close at the high gives MFM = +1 (full accumulation); a close at the low gives MFM = −1 (full distribution); a close at the midpoint gives MFM = 0.
- Multiplying by [[volume]] yields **Money Flow Volume**, weighting the signal by participation — a strong close on heavy volume counts far more than the same close on light volume.
- Summing MFV over N periods and dividing by total volume produces CMF, bounded in [−1, +1] but in practice oscillating within roughly ±0.5. The default window is **20 or 21 days**; shorter windows are more responsive but noisier.

(Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]])

### Worked example

A single bar: High = 50, Low = 46, Close = 49, Volume = 100,000.

```
MFM = ((49 − 46) − (50 − 49)) / (50 − 46)
    = (3 − 1) / 4
    = +0.50
MFV = 0.50 × 100,000 = +50,000   (net accumulation for the bar)
```

The close finished in the upper part of the range, so half the bar's volume counts as buying pressure. To get the 20-day CMF you sum each bar's MFV over the trailing 20 days and divide by the trailing 20-day total volume. If, say, ΣMFV = +1,800,000 and ΣVolume = 9,000,000, then CMF = +0.20 — a moderately bullish, accumulation reading.

### Interpreting the value

| CMF reading | Interpretation |
|-------------|----------------|
| > +0.25 | Strong, sustained buying pressure (accumulation) |
| +0.05 to +0.25 | Mild accumulation / bullish bias |
| ≈ 0 (±0.05) | Neutral / indecision — no clear flow |
| −0.05 to −0.25 | Mild distribution / bearish bias |
| < −0.25 | Strong, sustained selling pressure (distribution) |

## Key Signals

- **CMF > 0**: buying pressure (accumulation) — bullish
- **CMF < 0**: selling pressure (distribution) — bearish
- **Divergences**: CMF diverging from price warns of potential reversals
- Strength of the signal increases with the magnitude of CMF values

(Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]])

## How Traders Use It

CMF is read as a gauge of whether a price move is backed by genuine volume conviction. A trader watches for:

- **Zero-line crossings** — CMF crossing above zero hints accumulation is taking over; crossing below hints distribution. Many traders require the cross to *hold* for several bars to filter whipsaws.
- **Sustained extremes** — readings held above +0.25 or below −0.25 indicate strong, persistent buying or selling pressure rather than a transient tick.
- **[[divergence]]** — the highest-value signal. Price making a new high while CMF makes a lower high warns the rally is running on thinning volume; the inverse warns a sell-off is losing seller conviction.
- **Confirmation filter** — because CMF is a volume-confirmation tool, it is most useful as a filter on price-based signals (breakouts, S/R tests) rather than a standalone trigger. A breakout with CMF > 0 has more conviction than one with CMF fading.

## CMF vs Related Money-Flow Indicators

| Indicator | Built from | Range | Key difference |
|-----------|-----------|-------|----------------|
| **CMF** | MFM × volume, summed over N | −1 to +1 (oscillator) | Uses *intrabar* close location; ignores prior close |
| **[[accumulation-distribution]]** | same MFM × volume, but *cumulative* | unbounded line | Running total; no fixed window — used for long-term divergence |
| **[[obv|On-Balance Volume]]** | full volume added/subtracted by close-vs-prior-close | unbounded line | All-or-nothing sign from close direction, ignores range location |
| **[[money-flow-index|Money Flow Index (MFI)]]** | typical-price money flow, RSI-style | 0 to 100 | A "volume-weighted RSI"; uses overbought/oversold bands |
| **[[chaikin-oscillator]]** | MACD of the A/D line | unbounded | Momentum of accumulation, not its level |

## Best-Practice Combination

CMF works well alongside [[obv|OBV]] and price-based indicators. The professional stack of 50/200 EMA + [[relative-strength-index|RSI]] + [[bollinger-bands|Bollinger Bands]] + OBV can be enhanced by adding CMF for institutional flow confirmation (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Pitfalls and Risks

- **Gap distortion.** CMF's main failure mode: when a bar gaps, the open is outside the prior range and the close can sit anywhere in a stretched high-low band, distorting the multiplier. A stock that gaps up and closes mid-range can read as *distribution* even though it rallied sharply — because MFM only sees the bar's own range, never the gap.
- **Ignores the gap/overnight move.** Because MFM uses only Close vs the *current* bar's High/Low, it discounts overnight gaps entirely. Compare with [[obv]], which keys off close-to-close direction.
- **Lag and whipsaw.** With a 20-period window CMF is smoothed and lags; with a short window it whipsaws across zero. There is no setting that avoids both.
- **Low-volume / illiquid names.** Sparse, lumpy volume makes the weighting unreliable — see [[liquidity]].
- **Not directional on its own.** A positive CMF in a clear downtrend is a weak counter-signal, not a buy. Always read it relative to [[trend]] and price structure.

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)

## Related

- [[marc-chaikin]] -- creator of CMF and the Chaikin Oscillator
- [[volume]] -- the participation input CMF weights by
- [[accumulation-distribution]] -- the cumulative line CMF normalizes
- [[obv]] -- alternative close-direction volume series
- [[money-flow-index]] -- the bounded 0–100 money-flow oscillator
- [[chaikin-oscillator]] -- momentum (MACD) of the A/D line
- [[divergence]] -- CMF's highest-value signal type

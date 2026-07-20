---
title: "SuperSmoother Filter"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, crypto]
aliases: ["SuperSmoother", "Super Smoother", "Ehlers SuperSmoother", "Two-Pole SuperSmoother", "Butterworth Smoother"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[z-score]]", "[[hurst-exponent]]", "[[overfitting]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[john-ehlers]]", "[[microstructure-noise-low-timeframe]]", "[[laguerre-filter]]", "[[jurik-moving-average]]", "[[alma]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[least-squares-moving-average]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[kalman-filter-trading]]", "[[bid-ask-spread]]", "[[false-signals]]", "[[standard-deviation]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis]
prerequisites: ["[[moving-averages]]", "[[exponential-moving-average]]"]
difficulty: advanced
---

# SuperSmoother Filter

The SuperSmoother is a two-pole Butterworth-style low-pass filter introduced by [[john-ehlers|John Ehlers]] in *Cycle Analytics for Traders* (2013). It exists to fix a specific complaint Ehlers makes about conventional [[moving-averages]]: they are marketed as noise removers, but they **do not actually remove the high-frequency content they claim to** — an [[simple-moving-average|SMA]] or [[exponential-moving-average|EMA]] leaves substantial energy above the Nyquist limit, which aliases back into the output as apparent structure. In [[stretch-revert]] it is the baseline behind `hl_supersmoother_stretch_revert`, where its job is precisely to keep [[microstructure-noise-low-timeframe|bid-ask bounce]] out of the mean.

With the [[laguerre-filter|Laguerre Filter]] and the proprietary [[jurik-moving-average|JMA]], it forms the **signal-processing group** of baselines — estimators specified by their frequency response rather than by a weighting scheme over past bars.

## Construction

Two-pole recursive filter, with coefficients derived from the target period `n`:

```
a1 = exp(-1.414*pi / n)
b1 = 2*a1*cos(1.414*pi / n)

c2 = b1
c3 = -a1*a1
c1 = 1 - c2 - c3

Filt = c1*(price + price[1])/2 + c2*Filt[1] + c3*Filt[2]
```

Three details are load-bearing:

- **`1.414` is √2**, the Butterworth damping constant for a two-pole section. It is what makes the passband maximally flat — no ripple in the frequencies you intend to keep.
- **`c1 = 1 - c2 - c3` normalises DC gain to exactly 1.** A constant price in gives the same constant out, with no offset. This matters for a reversion baseline: any gain error would bias the residual systematically in one direction.
- **The input is `(price + price[1])/2`, not `price`.** That two-bar average is a deliberate pre-filter — a one-tap FIR that puts a null at the Nyquist frequency, killing the bar-to-bar alternation that is the signature of [[bid-ask-spread|bid-ask]] bounce before the recursive section ever sees it.

State is three floats: the previous close and the two previous filter outputs. No rolling window is required.

## Filter behaviour

The averaging framing and the DSP framing genuinely disagree here, and the disagreement is the point of the indicator.

**The averaging framing** says an SMA(10) "removes noise" because it averages ten bars. **The DSP framing** asks what the transfer function actually does, and the answer for an SMA is a sinc-shaped response: a main lobe that passes the trend, then a series of **sidelobes** that pass high-frequency content at reduced but non-trivial amplitude, with the first sidelobe only about 13 dB down. Those sidelobes are the aliasing Ehlers objects to. Content that should have been rejected instead leaks through and appears in the output as wiggles that look like market structure and are not.

The SuperSmoother's response is different in kind:

- **Monotonic rolloff, no sidelobes.** Above the corner frequency, attenuation increases continuously. High-frequency content is genuinely removed, not partially passed at a reduced amplitude.
- **Maximally flat passband.** Butterworth damping means the cycles you intend to keep pass with essentially unmodified amplitude — the filter does not distort the swing it is measuring.
- **No ringing or overshoot.** This distinguishes it sharply from the lag-cancelling family. [[zero-lag-exponential-moving-average|ZLEMA]] and [[triple-exponential-moving-average|TEMA]] reduce lag by subtracting an estimate of it, which mathematically means boosting high frequencies — they buy responsiveness by amplifying exactly the noise a filter is supposed to reject, and they overshoot after sharp moves. SuperSmoother buys its cleanliness the honest way: it attenuates, and accepts the phase delay that comes with it.
- **Nyquist handling.** On a bar series, the shortest resolvable cycle is two bars. Anything shorter than that in the underlying tick process folds back into the bar series as spurious low-frequency content. The two-bar input pre-average plus the two-pole rolloff is Ehlers' answer to that fold-back.

## Lag and smoothing trade-off

The comparison Ehlers actually makes is not "less lag than an EMA" but **"much cleaner output at comparable lag"**. Roughly, at 15m bars:

| Baseline | High-frequency rejection | Lag character | State |
|---|---|---|---|
| SMA(n) | poor — sinc sidelobes leak | fixed, (n-1)/2 bars | n bars |
| EMA(n) | mediocre — single-pole, 6 dB/octave | ~(n-1)/2 at low frequencies | 1 |
| SuperSmoother(n) | strong — two-pole, 12 dB/octave, no sidelobes | comparable to EMA(n), modestly more | 3 |
| ZLEMA / TEMA | **negative** — HF is amplified | near zero, with overshoot | 2-3 |

So SuperSmoother(20) will sit at roughly the same delay as EMA(20) but with a visibly quieter line — the small wiggles that survive an EMA do not survive it. The trade is that you cannot get that rejection for free: if you want a SuperSmoother as fast as a ZLEMA you have to shorten `n`, and shortening `n` raises the corner frequency and lets the noise back in.

Practical periods in the [[stretch-revert]] context: `n = 10` on 15m for a fast, still-clean baseline; `n = 20-30` for a slower mean that only registers substantial extensions.

## Use as a mean-reversion baseline

This is the reason the page exists. In [[stretch-revert]], the fade triggers on `price - baseline` normalised into a [[z-score]] — so whatever noise survives the baseline is *added to the residual* and read as stretch. A baseline that leaks high-frequency content manufactures false stretch out of nothing.

**SuperSmoother flags stretch late, and that is the design intent.** It will not fire on a two-bar spike, a single wide print, or a thin-book wobble, because none of that survives the filter. Compared with [[hull-moving-average|HMA]] or ZLEMA baselines, which hug price and only register violent extensions, and compared with an SMA baseline, which registers extensions late *and* noisily, SuperSmoother sits in a distinctive corner: **late but clean**. The signals it does produce are dominated by genuine multi-bar displacement.

**The connection to [[microstructure-noise-low-timeframe|microstructure noise]] is direct and is the family's single most expensive failure mode.** On a thin alt perp at 1m or 5m, price alternates between bid and offer bar after bar. That alternation is a Nyquist-frequency oscillation. An SMA or EMA baseline passes part of it, so `price - baseline` inherits a component that is *literally the spread*, and a fixed z-threshold starts triggering on it. The backtest books that as profit because it fills at the mid; the live bot crosses the spread and pays it. The two-bar pre-average places a null exactly on that alternation and the two-pole section removes what is left — which is why this member is specifically valuable on the lower timeframes and thinner books where the rest of the family is least trustworthy.

**Regimes that flatter it:**

- **Low-timeframe and thin-book trading.** Its comparative advantage is largest exactly where noise-to-signal is worst.
- **Choppy ranges with occasional real flushes.** The filter ignores the chop and registers the flush, which is close to the ideal selectivity profile for a fade.
- **High-frequency-noise regimes** — post-listing alts, low-liquidity hours — where SMA/EMA baselines generate the most [[false-signals]].

**Regimes that expose it:**

- **Trends, like every member.** Clean measurement of a stretch that keeps stretching is still a losing fade. The regime gate does this work, not the filter.
- **Genuinely fast reversals.** Late detection means an entry several bars after the extreme. If reversion is quick, the filter's own delay eats the move — the residual peaks after the bottom is in.
- **Volatility regime shifts.** `n` is fixed. Doubling realised vol widens the residual distribution under a static threshold, the same non-adaptivity limitation the Laguerre baseline has and which [[frama|FRAMA]]/[[vidya|VIDYA]]/[[kama|KAMA]] exist to address.
- **Gap and single-print events.** A real gap is broadband; the filter treats it partly as noise and responds slowly, so the residual understates a genuine dislocation for several bars.

Against its siblings: [[laguerre-filter|Laguerre]] is the lower-lag smoother; SuperSmoother is the better noise rejector. Where the two disagree on a bar is diagnostically useful — it usually means the stretch was high-frequency in origin, i.e. probably not tradeable.

## Parameters and tuning

| Parameter | Typical | Effect |
|---|---|---|
| `n` (period) | 10 - 30 on 15m | Corner frequency. Lower = faster and noisier; higher = cleaner and laggier. |
| `entry_z` | 2.0 - 3.0 | Stretch threshold on the residual |
| `z_window` | 50 - 200 bars | Window for residual sigma |
| input series | `(H+L)/2` or close | Must be identical in backtest and live |

**Overfitting warning.** `n` is a single integer knob, which is comparatively safe — but "comparatively safe" is not safe. This filter is one of fourteen [[stretch-revert]] baselines evaluated against one history, and sweeping `n` across 8-40 in steps of 2 is seventeen variants of one member. The best (member, period) pair from that joint grid will look strong in-sample regardless of whether reversion is real. See [[overfitting]].

Discipline that applies specifically here:

- **Choose `n` from the noise you are trying to reject**, not from P/L. If bid-ask alternation is the target, `n` needs to be comfortably above 2 bars — anything in 10-30 achieves that, so pick by desired smoothness and stop.
- **Test the plateau.** A P/L surface that is flat across `n = 14, 16, 18, 20` is a believable setting. A spike at `n = 17` is a fitted one.
- **Do not tune `n` per asset.** Per-asset periods multiply the search space by the universe size and are the fastest route to a result that will not replicate.
- Any optimised period must be deflated for the number of variants searched before its Sharpe is interpretable.

## Advantages

- **Genuine high-frequency rejection**, not the partial leakage of an SMA/EMA — the residual reflects displacement, not spread.
- **No ringing or overshoot**, so the residual sigma measures price dispersion rather than filter artifacts.
- **Directly attacks the family's most expensive failure mode** — mistaking [[microstructure-noise-low-timeframe|bid-ask bounce]] for dislocation, the canonical backtest-to-live divergence.
- **Flat passband** — the swing being measured is not amplitude-distorted by the filter.
- **Cheap and stateless-ish**: three floats, O(1) per bar, easy to keep bit-identical between backtest and live.
- **Fully published and reproducible**, unlike [[jurik-moving-average|JMA]].
- **One integer parameter**, a small and defensible degree of freedom relative to adaptive alternatives.

## Limitations

- **Late by construction.** You cannot ask for both this rejection and low lag; entries land after the extreme, and fast V-reversions are partly missed.
- **Non-adaptive.** Fixed `n` through a volatility regime change means a static z-threshold on a shifting residual distribution.
- **Understates true gaps.** Broadband events are attenuated along with the noise, so a genuine dislocation reads smaller than it is for the first few bars.
- **Warm-up sensitivity.** The two-pole recursion needs roughly 3-5× `n` bars to settle; a filter seeded mid-history disagrees with one seeded from the same anchor date, which will make near-boundary backtest and live signals differ.
- **Numerical care with very small `n`.** As `n` approaches 2-3 the coefficients approach the stability edge and the filter becomes ill-behaved. Keep `n` comfortably above ~6.
- **Does not solve trend risk.** A cleaner measurement of the wrong regime is still the wrong trade.
- Some implementations feed `(high+low)/2`, some feed the close, and outputs differ; the vault member name (`hl_supersmoother`) implies the HL midpoint, and that choice must be mirrored exactly in any replication.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/l2-book?coin=X` — **the key call for this filter**: read the live spread, then compare it against the residual the filter produced. If `|price - Filt|` is not several multiples of the spread, the "stretch" is the thing SuperSmoother was built to reject and the fade will pay it as cost
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the OHLCV the two-pole recursion runs over (use `interval=1m` when testing the noise-rejection claim, where it matters most)
- `GET /api/v1/derivatives/funding-rates?coin=X` — carry drag on held reversions
- `GET /api/v1/derivatives/open-interest?coin=X` — OI building into the stretch argues trend rather than dislocation

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for replaying the filter over full cycles
- `GET /api/v1/volatility/regime/{symbol}` — volatility state, since a fixed `n` has no defence against a vol regime change
- `GET /api/v1/quant/regimes/history` — hourly HMM labels for regime-stratified scoring

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/l2-book?coin=ETH"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [order-book depth](https://cryptodataapi.com/quant-order-books) · [market regimes](https://cryptodataapi.com/market-regimes) · [funding rates](https://cryptodataapi.com/funding-rates)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can both run this filter and use it as a noise diagnostic:

- **Spread-vs-residual gate** — before every entry, pull `GET /api/v1/hyperliquid/l2-book?coin=X` and require the residual to exceed the half-spread by a wide margin. This is the check the SuperSmoother member is uniquely positioned to make credibly, because its residual is not itself contaminated by bounce.
- **Prove the rejection claim** — compute SuperSmoother and an EMA of matched lag over the same `interval=1m` candles and compare residual autocorrelation at lag 1. Strong negative lag-1 autocorrelation in the EMA residual and its absence in the SuperSmoother residual is the empirical signature of [[microstructure-noise-low-timeframe|bid-ask bounce]] being filtered out.
- **Timeframe sweep** — run the same `n` on 1m, 5m, and 15m candles; the filter's advantage over EMA should be largest on 1m. If it is not, the noise being rejected is not microstructural and the member's rationale is wrong.
- **Backtest with matched warm-up** — `GET /api/v1/backtesting/klines`, discarding the first 3-5× `n` bars so seed transients do not create phantom early signals.
- **Vol-regime overlay** — `GET /api/v1/volatility/regime/{symbol}` alongside signals; a fixed-`n` filter's residual sigma drifts with vol, so entry thresholds should be validated per vol state rather than pooled.
- **Regime gate** — `GET /api/v1/quant/market` stands the member down in trending states, which no amount of filter quality substitutes for.

## Related

[[stretch-revert]] · [[laguerre-filter]] · [[jurik-moving-average]] · [[john-ehlers]] · [[moving-averages]] · [[adaptive-moving-averages]] · [[simple-moving-average]] · [[exponential-moving-average]] · [[alma]] · [[frama]] · [[vidya]] · [[kama]] · [[hull-moving-average]] · [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] · [[least-squares-moving-average]] · [[theil-sen-regression]] · [[quadratic-regression]] · [[kalman-filter-trading]] · [[mean-reversion]] · [[bollinger-bands]] · [[z-score]] · [[standard-deviation]] · [[hurst-exponent]] · [[microstructure-noise-low-timeframe]] · [[bid-ask-spread]] · [[false-signals]] · [[overfitting]] · [[cryptodataapi-hyperliquid]] · [[cryptodataapi-mcp]]

## Sources

- John Ehlers, *Cycle Analytics for Traders* (2013) — the SuperSmoother derivation, the Butterworth two-pole coefficients, and the aliasing/Nyquist argument against conventional moving averages.
- John Ehlers, *Cybernetic Analysis for Stocks and Futures* (2004) — earlier treatment of DSP filter design applied to price series; see also [[laguerre-filter]].
- Trading application, regime framing, and failure modes are drawn from vault pages: [[stretch-revert]], [[mean-reversion]], [[microstructure-noise-low-timeframe]], [[moving-averages]], [[overfitting]].

No source-summary page exists for the Ehlers material in this vault yet, and no independent backtest of a SuperSmoother baseline has been reviewed here.

---
title: "Signal Processing"
type: concept
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [quantitative, machine-learning, indicators, technical-analysis]
aliases: ["Signal Processing", "Digital Signal Processing", "DSP"]
related: ["[[feature-engineering]]", "[[indicators]]", "[[bollinger-bands]]", "[[hidden-markov-models]]", "[[jim-simons]]", "[[noise-vs-signal]]", "[[machine-learning-overview]]"]
difficulty: advanced
domain: [quantitative]
---

**Signal processing** is the set of mathematical techniques for analyzing, filtering, and extracting information from time-varying data ("signals"). It originated in engineering — telecommunications, audio, radar, speech recognition — and treats a price or return series as a noisy signal from which a true underlying component must be separated. In quantitative trading, signal-processing tools are used to smooth, detrend, denoise, and decompose market data, and to build features and filters for systematic strategies.

## Core techniques

- **Filtering / smoothing** — moving averages, exponential filters, the Kalman filter, and Savitzky-Golay filters extract a slow-moving trend from noisy prices. Most technical [[indicators]] (e.g. moving averages) are low-pass filters.
- **Fourier analysis** — the Fourier transform decomposes a series into frequency components, exposing cycles and periodicity. Useful for detecting dominant cycles but fragile on non-stationary, noisy markets.
- **Wavelet transforms** — like Fourier but localized in time *and* frequency, better suited to bursty, non-stationary financial data; used for multi-scale denoising and feature extraction.
- **Spectral / cycle analysis** — estimating dominant cycle lengths to time entries (e.g. Ehlers' cycle indicators, adapted explicitly from DSP).
- **Kalman filtering** — a recursive state estimator that tracks a hidden state (e.g. a fair-value spread or hedge ratio) under noise; widely used in [[pairs-trading]] for dynamic hedge ratios.
- **Signal-to-noise framing** — quantifying how much of a series is exploitable signal vs noise, central to setting reasonable expectations for any strategy.

## Trading and finance relevance

Signal processing is one of the deepest links between engineering and quant finance:

- **Denoising and trend extraction** — filtering price series before feeding them to a model or indicator reduces whipsaw and overfitting to noise.
- **Feature engineering** — spectral features, wavelet coefficients, and filtered series are inputs to ML models; see [[feature-engineering]] and [[feature-engineering-finance]].
- **Dynamic spreads** — Kalman filters give time-varying hedge ratios for [[pairs-trading]] and statistical arbitrage.
- **Cycle timing** — spectral methods attempt to identify recurring cycles, though markets' non-stationarity makes this unreliable in isolation.
- **The Renaissance connection** — [[jim-simons|Renaissance Technologies]] recruited signal-processing, speech-recognition, and cryptography experts; the firm's edge is often described as treating markets as a noisy signal-extraction problem rather than an economics problem (Source: [[book-the-man-who-solved-the-market]]). Hidden Markov Models (see [[hidden-markov-models]]) come from the same signal-processing lineage.

## Cautions

Markets are non-stationary and overwhelmingly noise; classical DSP assumes more structure (stationarity, clean periodicity) than markets provide. Fourier-based cycle "discoveries" are a notorious source of overfitting — apparent cycles vanish out-of-sample. Filters introduce *lag* (a smoothed series tells you about the past), so a denoised signal is not a free lunch for timing. Validate any signal-processing feature walk-forward. See [[overfitting-in-trading]].

## Related

- [[feature-engineering]] — building model inputs
- [[indicators]] — most are filters in disguise
- [[hidden-markov-models]] — regime detection from the same lineage
- [[pairs-trading]] — Kalman-filtered spreads
- [[jim-simons]]

## Sources

- [[book-the-man-who-solved-the-market]] — Renaissance Technologies' signal-extraction approach.
- A. V. Oppenheim & R. W. Schafer, *Discrete-Time Signal Processing* (standard DSP reference).
- J. F. Ehlers, *Cybernetic Analysis for Stocks and Futures* — DSP applied to markets.

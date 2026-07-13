---
title: "xLSTM-TS (Extended LSTM for Time Series)"
type: concept
created: 2026-05-14
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, deep-learning]
domain: [machine-learning, ai-trading]
difficulty: advanced
related:
  - "[[lstm-trading]]"
  - "[[transformer-trading]]"
  - "[[deep-learning]]"
  - "[[stock-prediction]]"
  - "[[time-series-forecasting]]"
  - "[[market-regime-detection-ml]]"
---

xLSTM-TS (Extended LSTM for Time Series) is a modernised LSTM architecture purpose-built for time-series forecasting, including financial price-direction prediction. In published benchmarks on daily equity data it has outperformed a wide field of competing deep-learning forecasters, positioning it as a state-of-the-art building block for short-horizon directional models (Source: [[2026-04-22-gap-finder-ai-2026-major-news-stories]]).

## Overview

xLSTM-TS is an extended Long Short-Term Memory architecture adapted to the demands of time-series forecasting. It builds on the original [[lstm-trading|LSTM]] family while incorporating modernisations that allow it to compete with — and on certain financial benchmarks beat — newer architectures such as [[transformer-trading|transformers]], Temporal Convolutional Networks, and N-BEATS. For traders, xLSTM-TS is most interesting as a high-accuracy direction predictor on daily equity series, where it has produced some of the strongest reported results in recent literature.

## How it works

xLSTM-TS retains the core LSTM idea of gated recurrent units that can carry information across long sequences, while extending the architecture for the specific structure of time-series data. Inputs are typically rolling windows of price and volume features (often with [[feature-engineering-finance|engineered indicators]]) and the model is trained to predict the next-step direction or value.

A practical detail from the benchmark study is the importance of denoising. Applying **wavelet denoising** to inputs significantly improved performance across all deep-learning models tested, including xLSTM-TS itself — suggesting that signal-to-noise enhancement is at least as important as architectural choice on noisy daily financial data (Source: [[2026-04-22-gap-finder-ai-2026-major-news-stories]]).

## Performance / Results

On the daily **EWZ (Brazil ETF)** stock price direction prediction task, xLSTM-TS achieved:

- **72.82% accuracy** on next-day direction prediction
- **73.16% F1 score**
- **MASE** (Mean Absolute Scaled Error) significantly exceeding naive forecasts

xLSTM-TS outperformed a broad benchmark set of competing deep-learning architectures on the same task, including:

- **Temporal Convolutional Networks (TCN)**
- **N-BEATS**
- **Temporal Fusion Transformers (TFT)** — see [[transformer-trading]]
- **N-HiTS**
- **TiDE**

Wavelet denoising significantly improved performance across all models tested, not just xLSTM-TS (Source: [[2026-04-22-gap-finder-ai-2026-major-news-stories]]).

## Trading Applications

- **Short-horizon direction prediction** — daily directional models for systematic equity strategies, particularly on single-name or ETF series similar to the benchmarked EWZ setup
- **Component in ensemble forecasters** — xLSTM-TS-derived signals can be combined with [[transformer-trading|transformer]] and gradient-boosting outputs in ensemble systems
- **Feature for [[market-regime-detection-ml|regime detection]]** — direction-probability output can feed downstream regime classifiers
- **Baseline for new models** — given strong reported results, xLSTM-TS provides a useful benchmark when evaluating new deep-learning architectures on similar [[stock-prediction|stock prediction]] tasks

## Limitations

- Published benchmarks are concentrated on a small set of datasets (notably daily EWZ); generalisation across markets, instruments, and timeframes remains to be demonstrated more broadly
- High accuracy on direction prediction does not directly imply tradeable PnL — costs, slippage, and capacity constraints can erode the apparent edge, see [[overfitting-in-trading]]
- Wavelet denoising lifts all models, raising the question of how much of the reported improvement is architectural vs. preprocessing
- Like all deep [[time-series-forecasting|time-series forecasting]] models, xLSTM-TS is exposed to non-stationarity and regime change

## Related

- [[lstm-trading]] — base LSTM architecture that xLSTM-TS extends
- [[transformer-trading]] — competing architecture family (TFT was among the benchmarked models)
- [[deep-learning]] — broader context
- [[stock-prediction]] — application domain
- [[time-series-forecasting]] — general task framing
- [[market-regime-detection-ml]] — downstream use of direction signals
- [[feature-engineering-finance]] — input design strongly affects xLSTM-TS performance
- [[overfitting-in-trading]] — applies to all deep-learning forecasters

## Sources

- [[2026-04-22-gap-finder-ai-2026-major-news-stories]] — documents xLSTM-TS performance benchmarks (72.82% accuracy, 73.16% F1 on daily EWZ), comparison against TCN, N-BEATS, TFT, N-HiTS, and TiDE, and the impact of wavelet denoising

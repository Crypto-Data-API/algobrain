---
title: "Recurrent Neural Networks (RNNs & LSTMs)"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["RNN", "Recurrent Neural Network", "LSTM", "GRU"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[lstm-trading]]", "[[neural-networks]]", "[[deep-learning-overview]]", "[[convolutional-neural-networks]]", "[[transformer-architecture]]", "[[supervised-learning]]", "[[artificial-intelligence]]"]
---

# Recurrent Neural Networks (RNNs & LSTMs)

**Recurrent Neural Networks** (RNNs) are deep learning architectures designed for sequential data — they process inputs one timestep at a time while maintaining a hidden state that acts as "memory" of previous inputs. **Long Short-Term Memory** (LSTM) networks are the most successful RNN variant, solving the vanishing gradient problem that plagued earlier RNNs. In trading, LSTMs are the classic deep learning approach for time-series forecasting.

## Architecture Variants

| Variant | Innovation | Trading Use |
|---------|-----------|-------------|
| **Vanilla RNN** | Simple recurrent connections | Rarely used — vanishing gradient makes it unable to learn long sequences |
| **LSTM** | Gates (forget, input, output) control information flow | Price forecasting, volatility prediction — the workhorse |
| **GRU** | Simplified LSTM (2 gates instead of 3) | Faster training, similar performance to LSTM |
| **Bidirectional** | Processes sequence forward and backward | Not suitable for trading (uses future data) — useful for NLP only |
| **Encoder-Decoder** | Sequence-to-sequence mapping | Multi-step ahead forecasting |

## How LSTMs Work

An LSTM cell has three gates controlling information flow:

1. **Forget gate**: Decides what old information to discard ("yesterday's volume spike is no longer relevant")
2. **Input gate**: Decides what new information to store ("today's earnings surprise is important")
3. **Output gate**: Decides what to output as the prediction ("bullish signal based on accumulated context")

This gate mechanism lets LSTMs selectively remember or forget information across long sequences — critical for financial time series where patterns span days, weeks, or months.

## Trading Applications

See [[lstm-trading]] for detailed implementations.

| Application | Input Sequence | Output | Typical Performance |
|-------------|---------------|--------|-------------------|
| **Next-day return prediction** | 30-60 days of OHLCV | Direction (up/down) | Marginally above random |
| **Volatility forecasting** | Rolling returns, VIX history | Next-day/week volatility | Better than GARCH in some studies |
| **Multi-asset forecasting** | Cross-asset returns | Portfolio signals | Captures cross-asset dependencies |
| **Order flow prediction** | Tick-level trade data | Short-term direction | Works at HFT timescales |

## LSTMs vs Transformers

[[transformer-architecture|Transformers]] have largely superseded LSTMs for NLP tasks but the picture is more nuanced for financial time series:

| Dimension | LSTM | Transformer |
|-----------|------|-------------|
| **Sequential bias** | Built-in (processes in order) | Learned (via positional encoding) |
| **Long-range dependencies** | Good (via gates) | Excellent (via self-attention) |
| **Training data needed** | Moderate | Large |
| **Interpretability** | Low | Low (but attention weights can be visualized) |
| **Maturity for finance** | Well-studied, many papers | Newer, [[transformer-trading|growing evidence]] |
| **Computational cost** | Lower | Higher |

For pure time-series forecasting with limited data, LSTMs remain competitive. For tasks involving text or very long sequences, transformers dominate.

## Common Pitfalls

- **[[overfitting-in-trading|Overfitting]]**: LSTMs have many parameters — regularization (dropout, early stopping) is essential
- **Stationarity assumption**: Financial time series are non-stationary; LSTMs trained on one regime may fail in another
- **Sequence length selection**: Too short = misses patterns; too long = noise overwhelms signal
- **Look-ahead bias**: Bidirectional LSTMs use future data — never use for prediction tasks

## See Also

- [[lstm-trading]] — Applied LSTM implementations for trading
- [[deep-learning-overview]] — Deep learning hub
- [[convolutional-neural-networks]] — Alternative for spatial/image data
- [[transformer-architecture]] — The architecture that succeeded RNNs for NLP
- [[transformer-trading]] — Transformers applied to financial time series
- [[neural-networks]] — The building block
- [[supervised-learning]] — The paradigm RNNs operate in
- [[artificial-intelligence]] — AI section hub

## Sources

- Hochreiter & Schmidhuber, "Long Short-Term Memory" (1997) — the foundational LSTM paper
- Cho et al., "Learning Phrase Representations using RNN Encoder-Decoder" (2014) — introduced the GRU
- Survey literature on deep learning for financial time-series forecasting (LSTM vs GARCH vs transformer comparisons)

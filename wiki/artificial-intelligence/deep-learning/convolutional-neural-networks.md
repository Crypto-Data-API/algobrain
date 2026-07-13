---
title: "Convolutional Neural Networks (CNNs)"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["CNN", "Convolutional Neural Network", "ConvNet"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[cnn-chart-recognition]]", "[[neural-networks]]", "[[deep-learning-overview]]", "[[computer-vision-trading]]", "[[recurrent-neural-networks]]", "[[artificial-intelligence]]"]
---

# Convolutional Neural Networks (CNNs)

A **Convolutional Neural Network** (CNN) is a deep learning architecture designed to process grid-structured data — primarily images, but also applicable to time-series data arranged as 2D matrices. In trading, CNNs are used for [[cnn-chart-recognition|chart pattern recognition]], [[computer-vision-trading|satellite imagery analysis]], and converting OHLCV data into image representations for visual pattern detection.

## How CNNs Work

### Core Operations

| Layer Type | What It Does | Trading Analogy |
|-----------|-------------|-----------------|
| **Convolutional layer** | Slides small filters across the input, detecting local patterns (edges, shapes) | Scanning a chart for candlestick patterns within a small window |
| **Pooling layer** | Downsamples, keeping the strongest activations | Zooming out to see the bigger pattern |
| **Fully connected layer** | Combines detected patterns into a final prediction | Synthesizing all patterns into a bullish/bearish signal |

### The Key Insight: Local Patterns

CNNs learn **hierarchical features**:
- **Early layers**: Detect simple patterns (lines, edges → support/resistance levels)
- **Middle layers**: Combine into shapes (triangles, channels → chart patterns)
- **Deep layers**: Recognize complex structures (head-and-shoulders, cup-and-handle)

This matches how technical analysts read charts — from individual candles to patterns to formations.

## Trading Applications

### 1. Chart Pattern Recognition
Convert OHLCV data to candlestick chart images, train CNN to classify:
- Head and shoulders, double top/bottom
- Ascending/descending triangles
- Bull/bear flags, pennants
- Cup and handle

See [[cnn-chart-recognition]] for implementation details.

### 2. Satellite & Alternative Data
| Application | Input | Signal |
|-------------|-------|--------|
| Retail foot traffic | Parking lot aerial images | Predict quarterly revenue |
| Oil storage | Satellite images of tank farms | Estimate crude inventory |
| Shipping activity | Port/harbor imagery | Global trade flow signals |
| Crop health | Agricultural satellite data | Commodity price forecasting |

### 3. Time-Series as Images
Convert price/volume data into 2D representations:
- **Gramian Angular Fields**: Encode time series as images preserving temporal structure
- **Recurrence Plots**: Visualize phase-space dynamics as 2D matrices
- **Spectrogram-style**: Frequency decomposition of price action

## CNN vs Other Architectures for Trading

| Task | CNN | [[recurrent-neural-networks|RNN/LSTM]] | [[transformer-architecture|Transformer]] |
|------|-----|---------|-------------|
| **Chart pattern recognition** | Best | Poor | Moderate |
| **Time-series forecasting** | Moderate | Good | Best |
| **Sentiment analysis** | Poor | Moderate | Best |
| **Satellite imagery** | Best | N/A | Moderate (multimodal) |

## Limitations

- **Requires image conversion**: Raw time-series data must be converted to 2D format, which can lose information
- **No temporal awareness**: Standard CNNs don't understand sequence order — need 1D temporal convolutions or hybrid architectures
- **Chart pattern validity**: Even if a CNN perfectly identifies a head-and-shoulders, the empirical evidence for chart pattern profitability is mixed
- **Data hungry**: Need thousands of labeled chart examples for training

## See Also

- [[cnn-chart-recognition]] — Applied CNN chart pattern recognition
- [[computer-vision-trading]] — Broader computer vision in trading
- [[neural-networks]] — The building block
- [[deep-learning-overview]] — Deep learning hub
- [[recurrent-neural-networks]] — Alternative for sequential data
- [[transformer-architecture]] — Alternative for sequence modeling
- [[artificial-intelligence]] — AI section hub

## Sources

- LeCun et al., "Gradient-Based Learning Applied to Document Recognition" (1998) — LeNet, the foundational CNN
- Krizhevsky, Sutskever, Hinton, "ImageNet Classification with Deep CNNs" (AlexNet, NeurIPS 2012)
- Sezer & Ozbayoglu, "Algorithmic Financial Trading with Deep Convolutional Neural Networks: Time Series to Image Conversion Approach" (Applied Soft Computing, 2018)
- Wang & Oates, "Imaging Time-Series to Improve Classification and Imputation" (IJCAI 2015) — Gramian Angular Fields

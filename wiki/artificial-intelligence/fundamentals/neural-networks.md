---
title: "Neural Networks"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Neural Network", "Artificial Neural Network", "ANN", "Deep Neural Network"]
domain: [ai-trading]
difficulty: beginner
related: ["[[types-of-ai]]", "[[machine-learning-vs-deep-learning]]", "[[transformer-architecture]]", "[[lstm-trading]]", "[[cnn-chart-recognition]]", "[[history-of-ai]]", "[[foundation-models]]", "[[artificial-intelligence]]"]
---

# Neural Networks

A **neural network** is a computing system inspired by biological brains, composed of layers of interconnected nodes (neurons) that learn patterns from data. Neural networks are the fundamental building block of all modern AI — from simple price prediction models to [[foundation-models|foundation models]] like GPT-4 and Claude.

## How They Work

### The Neuron

A single artificial neuron:
1. **Receives inputs** (numbers — e.g., price, volume, sentiment score)
2. **Multiplies each input** by a learned weight (importance)
3. **Sums the weighted inputs** and adds a bias
4. **Applies an activation function** (introduces non-linearity)
5. **Produces an output** passed to the next layer

### Network Structure

| Layer | Function | Analogy |
|-------|----------|---------|
| **Input layer** | Receives raw data | Market data feed |
| **Hidden layers** | Learns intermediate representations | Internal analysis |
| **Output layer** | Produces prediction or classification | Trading signal |

A network with many hidden layers is called a **deep** neural network — hence "[[machine-learning-vs-deep-learning|deep learning]]."

### Training (Backpropagation)

1. Network makes a prediction on training data
2. Prediction is compared to the correct answer (loss function)
3. Error is propagated backward through the network
4. Weights are adjusted to reduce the error
5. Repeat millions of times across the dataset

## Types Relevant to Trading

| Type | Architecture | Trading Use |
|------|-------------|-------------|
| **Feedforward** | Simple layers, one direction | Basic price/sentiment prediction |
| **[[lstm-trading|LSTM/RNN]]** | Recurrent connections, memory | Time-series forecasting |
| **[[cnn-chart-recognition|CNN]]** | Convolutional filters | Chart pattern recognition |
| **[[transformer-architecture|Transformer]]** | Self-attention mechanism | [[foundation-models|LLMs]], [[nlp-sentiment-analysis|sentiment analysis]] |
| **GAN** | Generator + discriminator | [[gan-synthetic-data|Synthetic data generation]] |

## Why Traders Should Understand This

You don't need to build neural networks to use AI for trading, but understanding the basics explains:

- **Why models need data**: More data → better weight calibration → better predictions
- **Why models fail**: Trained on historical patterns that may not repeat ([[overfitting-in-trading|overfitting]])
- **Why context windows matter**: [[foundation-models|LLMs]] are neural networks with fixed input sizes
- **Why inference costs money**: Larger networks require more computation ([[model-inference-vs-training]])
- **Why [[fine-tuning-llms|fine-tuning]] works**: You're adjusting existing weights rather than learning from scratch

## See Also

- [[machine-learning-vs-deep-learning]] — Where neural networks fit in the hierarchy
- [[types-of-ai]] — Classification of AI approaches
- [[transformer-architecture]] — The neural network architecture powering modern LLMs
- [[lstm-trading]] — Recurrent neural networks for trading
- [[cnn-chart-recognition]] — CNNs for chart pattern analysis
- [[foundation-models]] — Very large neural networks
- [[overfitting-in-trading]] — When neural networks learn noise instead of signal
- [[artificial-intelligence]] — AI section hub

## Sources

- McCulloch & Pitts (1943); Rosenblatt, the Perceptron (1958)
- Rumelhart, Hinton & Williams, backpropagation (1986)
- Goodfellow, Bengio & Courville, "Deep Learning" (2016) — standard reference text
- López de Prado, "Advances in Financial Machine Learning" (2018) — neural networks applied to markets

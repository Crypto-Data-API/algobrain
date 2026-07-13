---
title: "Adversarial Attacks"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, regulation, education]
aliases: ["Adversarial Attack", "Adversarial Examples", "Adversarial ML"]
domain: [risk-management]
difficulty: advanced
related: ["[[ai-security-overview]]", "[[model-poisoning]]", "[[convolutional-neural-networks]]", "[[supervised-learning]]", "[[cnn-chart-recognition]]", "[[ai-security-trading]]", "[[artificial-intelligence]]"]
---

# Adversarial Attacks

**Adversarial attacks** craft inputs that are nearly indistinguishable from legitimate data but cause AI models to make incorrect predictions. A perturbation invisible to human eyes can flip a classifier's output with high confidence. In trading, adversarial attacks threaten [[cnn-chart-recognition|chart recognition]], [[nlp-sentiment-analysis|sentiment models]], and any ML system making automated decisions.

## How They Work

An adversarial example adds a small, carefully computed perturbation to an input:

```
Original input (correctly classified):
  Chart image → Model says: "Head and shoulders" (confidence: 92%)

Adversarial input (misclassified):
  Chart image + tiny pixel changes → Model says: "Bull flag" (confidence: 88%)
  
Human sees: identical charts
Model sees: completely different patterns
```

## Attack Types

| Attack | Method | Threat Level |
|--------|--------|-------------|
| **White-box** | Attacker has full access to model architecture and weights | Highest — can compute exact perturbations |
| **Black-box** | Attacker can only query the model | High — transferability: attacks crafted on one model often work on others |
| **Physical** | Perturbations applied in the real world | Medium — adversarial patches on stop signs fool self-driving cars |
| **Targeted** | Force model to predict a specific wrong class | High — attacker controls the misclassification |
| **Untargeted** | Just make the model wrong (any wrong class) | Medium — easier to execute |

### Key Attack Algorithms

| Algorithm | Method | Year |
|-----------|--------|------|
| **FGSM** (Fast Gradient Sign Method) | Single gradient step in the direction that maximises loss | 2015 |
| **PGD** (Projected Gradient Descent) | Iterative FGSM with constraint projection | 2018 |
| **C&W** (Carlini & Wagner) | Optimisation-based, finds minimal perturbation | 2017 |
| **AutoAttack** | Ensemble of attacks, standard benchmark | 2020 |
| **Patch attacks** | Adversarial patch placed on part of image | 2018 |

## Trading-Specific Threats

### Manipulating Chart Pattern Recognition

If a trading system uses [[cnn-chart-recognition|CNN-based chart recognition]], an adversary who understands the model could:
- Subtly manipulate displayed chart data to trigger false patterns
- Exploit transfer attacks: perturbations designed for common model architectures work across similar models

### Adversarial Order Flow

An adversary could craft sequences of orders designed to:
- Trigger false signals in order flow prediction models
- Create adversarial microstructure patterns that fool market-making algorithms
- Generate sequences that look like accumulation/distribution to ML models but are actually manipulation

### Sentiment Model Manipulation

Craft social media posts or news text that:
- Appears neutral to humans but registers as strongly bullish/bearish to [[finbert|FinBERT]] or LLM classifiers
- Exploits known weaknesses in [[tokenization-nlp|tokenisation]] or embedding spaces
- Coordinates adversarial text across multiple accounts to amplify signal

## Defences

| Defence | How | Effectiveness |
|---------|-----|-------------|
| **Adversarial training** | Include adversarial examples in training data | Moderate — improves robustness but never eliminates vulnerability |
| **Input preprocessing** | Compress, smooth, or transform inputs before model | Moderate — removes some perturbations |
| **Ensemble methods** | Multiple models vote — harder to fool all simultaneously | Good — [[ensemble-methods|ensemble]] approaches reduce attack surface |
| **Certified defences** | Mathematical guarantees within perturbation bounds | Strong but limited to small perturbations |
| **Detection** | Separate model detects adversarial inputs | Moderate — arms race with attackers |
| **Human oversight** | Human reviews high-stakes decisions | Best — but doesn't scale |

## The Fundamental Problem

Adversarial vulnerability is **inherent** to high-dimensional neural networks — it's not a bug that can be patched. All current deep learning models ([[convolutional-neural-networks|CNNs]], [[transformer-architecture|transformers]], [[foundation-models|LLMs]]) are vulnerable to some form of adversarial attack. The practical response is defence in depth, not elimination.

## See Also

- [[ai-security-overview]] — AI security hub
- [[model-poisoning]] — Attacking the training process instead of inference
- [[ai-security-trading]] — Trading-specific adversarial risks
- [[cnn-chart-recognition]] — A model vulnerable to visual adversarial attacks
- [[ensemble-methods]] — Defence through multiple models
- [[artificial-intelligence]] — AI section hub

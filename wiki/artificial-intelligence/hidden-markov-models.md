---
title: "Hidden Markov Models (HMM)"
type: concept
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [machine-learning, quantitative, regime-detection, market-regime]
aliases: ["Hidden Markov Models", "HMM", "Hidden Markov Model", "Markov regime-switching"]
related: ["[[regime-detection]]", "[[market-regime-detection-ml]]", "[[volatility-regime-switching]]", "[[machine-learning-overview]]", "[[unsupervised-learning]]", "[[jim-simons]]"]
difficulty: advanced
domain: [quantitative, regime-detection]
---

A **Hidden Markov Model (HMM)** is a statistical model in which a system is assumed to move between a finite set of *unobservable* ("hidden") states according to Markov transition probabilities, while emitting *observable* outputs whose distribution depends on the current state. In trading, the hidden states are typically interpreted as latent market regimes (e.g. low-volatility bull, high-volatility crash, choppy range) and the observations are returns, volatility, or volume. The model lets you infer which regime the market is probably in *right now* and how likely it is to switch.

## How it works

An HMM is defined by:

- **Hidden states** `S = {s_1, ..., s_N}` — e.g. 2-4 market regimes.
- **Transition matrix** `A` — `A[i][j]` = probability of moving from state `i` to state `j` next period. The Markov property means the next state depends only on the current state, not the full history.
- **Emission distributions** `B` — for each state, the distribution of the observable (commonly a Gaussian over returns, giving a *Gaussian HMM*).
- **Initial distribution** `π` — probability of starting in each state.

Three canonical problems and their algorithms:

1. **Evaluation** — probability of an observed sequence given the model → *Forward algorithm*.
2. **Decoding** — most likely hidden-state sequence given observations → *Viterbi algorithm*.
3. **Learning** — fit `A`, `B`, `π` from data → *Baum-Welch* (an expectation-maximization / EM procedure). This is unsupervised: regimes are discovered, not labelled.

```python
# Sketch: fit a 2-state Gaussian HMM to daily returns and tag the current regime
from hmmlearn.hmm import GaussianHMM
import numpy as np

returns = np.diff(np.log(close)).reshape(-1, 1)        # observations
model = GaussianHMM(n_components=2, covariance_type="full", n_iter=200)
model.fit(returns)                                      # Baum-Welch
states = model.predict(returns)                         # Viterbi decoding
# Inspect each state's mean/variance to label "calm" vs "stressed"
means = model.means_.flatten()
calm_state = int(np.argmin(model.covars_.flatten()))   # lowest-variance regime
```

## Trading and finance relevance

HMMs are one of the workhorses of quantitative [[regime-detection]] because regimes are exactly the kind of latent, persistent, switching structure HMMs model well:

- **Regime-aware allocation** — switch a strategy on/off, or scale leverage, depending on the decoded regime. A trend strategy may only run in the "trending" state; a mean-reversion book may only run in the "range" state. See [[regime-adaptive-strategy]] and [[risk-on-risk-off-framework]].
- **Volatility-regime switching** — a 2-3 state HMM on realized volatility separates calm vs stressed markets, feeding position sizing and options exposure. See [[volatility-regime-switching]] and [[vol-regime-detection]].
- **Risk management** — the transition matrix gives a forward-looking probability of entering a high-drawdown regime, useful for de-risking before the variance actually spikes.
- **Renaissance / quant lineage** — HMMs trace back to speech recognition (IBM, 1970s-80s); [[jim-simons|Renaissance Technologies]] famously hired speech-recognition and signal-processing researchers, and Markov-style state models are part of that toolkit (Source: [[book-the-man-who-solved-the-market]]).

HMMs sit alongside other regime tools: simple rule-based thresholds, [[market-regime-detection-ml|ML classifiers]], and changepoint detection. They are favoured when you want a *probabilistic*, generative account of regime persistence rather than a black-box label.

## Strengths and weaknesses

**Strengths:** unsupervised (no need to hand-label regimes); interpretable states; gives transition probabilities, not just point labels; cheap to fit; long academic pedigree.

**Weaknesses:** the number of states must be chosen by the modeller and is easy to overfit; the Markov assumption ignores longer-memory dynamics; Gaussian emissions miss fat tails; regimes fit in-sample can be unstable out-of-sample and prone to *look-ahead* if the whole series is used to fit then label past points. Always validate with walk-forward / out-of-sample decoding and treat decoded regimes as noisy estimates, not ground truth. See [[overfitting-in-trading]].

## Related

- [[regime-detection]] — strategy-level use of regime models
- [[market-regime-detection-ml]] — ML approaches to regimes
- [[volatility-regime-switching]] — vol-specific HMM use
- [[unsupervised-learning]] — the broader learning paradigm
- [[machine-learning-overview]]

## Sources

- L. R. Rabiner, "A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition," *Proceedings of the IEEE*, 1989 — the canonical HMM reference.
- [[book-the-man-who-solved-the-market]] — Renaissance Technologies' use of speech/signal models.
- [[book-probabilistic-ml-for-finance]] — probabilistic state-space modelling in finance.
- `hmmlearn` documentation — common Python implementation of Gaussian HMMs.

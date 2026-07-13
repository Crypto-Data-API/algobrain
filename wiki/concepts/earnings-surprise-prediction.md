---
title: "Earnings Surprise Prediction"
type: concept
created: 2026-05-14
updated: 2026-06-11
status: good
tags: [stocks, machine-learning, fundamental-analysis, earnings]
aliases: ["Earnings Surprise Forecasting", "EPS Surprise Prediction", "Multimodal Earnings Prediction"]
domain: [equities, machine-learning]
difficulty: advanced
related: ["[[earnings-plays]]", "[[earnings-call-analysis]]", "[[earnings-quality]]", "[[transformer-trading]]", "[[claude]]", "[[llm-market-analysis]]", "[[finbert]]"]
---

Earnings surprise prediction is the use of machine-learning models — increasingly **multimodal LLMs** that ingest earnings-call transcripts, audio recordings, and presentation slides — to forecast whether a company will beat, miss, or meet consensus EPS expectations before the announcement. Because earnings surprises drive disproportionate intraday and multi-day price moves, even modest improvements in surprise prediction translate into tradable alpha. Recent research using the **FinCall-Surprise** dataset shows that multimodal approaches provide measurable gains over text-only models, but current systems still struggle to leverage audio and visual signals effectively, and class-imbalance pitfalls mean a high-accuracy model may simply be predicting the majority class.

## Why Earnings Surprises Matter

Around scheduled earnings releases, equity prices move on the gap between reported numbers and the analyst consensus. A "beat" or a "miss" of even a few cents can produce single-day moves of 5-20%. Implied volatility collapses through the announcement window ("IV crush"), so options-based [[earnings-plays|earnings plays]] depend on a directional or magnitude view of the surprise rather than a pure volatility view.

Any model that predicts the *sign* or *magnitude* of the surprise — even with modest accuracy improvements over baseline — generates trading signals: pre-announcement positioning in the underlying, calendar-spread structuring around the event, or volatility-arbitrage trades that lean directionally.

## The Multimodal Approach

A single earnings event produces three synchronized data streams:

1. **Text** — the full transcript of the conference call (management remarks plus Q&A) and the prepared earnings release.
2. **Audio** — the actual recording of the call, capturing tone, hesitation, pauses, and prosody that a transcript flattens out.
3. **Visual** — slides accompanying the call, supplementary charts, and any presented financial summaries.

Each modality carries non-redundant signal. Tone of voice from a CFO answering a Q&A question on guidance can imply doubt that the printed transcript does not capture. A slide showing a steep cohort-revenue chart adds quantitative context that the verbal remarks may downplay. Multimodal transformers attempt to fuse the three streams into a single representation that downstream classifiers use to predict the surprise label.

## The FinCall-Surprise Dataset

Recent research released **FinCall-Surprise**, a benchmark dataset of **2,688 corporate conference calls** with synchronized text transcripts, audio recordings, and presentation slides, each labeled with the eventual earnings-surprise outcome. The dataset enables apples-to-apples comparison of text-only, audio+text, slides+text, and full-multimodal models.

Two key findings emerged from the benchmark:

- **Multimodal gains are real but modest.** Adding audio and visual signals to a text-only baseline produced measurable improvements in surprise classification, but the gains were smaller than the multimodal-AI literature in other domains (e.g., sentiment from face+voice) might suggest. Current models do not yet leverage the non-text modalities efficiently.
- **Class imbalance is the dominant failure mode.** Real-world earnings outcomes are unbalanced — beats outnumber misses, and small surprises outnumber large ones. A model that simply predicts "beat" can score >70% accuracy on a beat-heavy sample while providing zero tradable signal. Benchmark designers must report per-class precision and recall, not just accuracy, and traders evaluating vendor models should demand the same.

(Source: [[2026-04-22-gap-finder-ai-2026-major-news-stories]])

## Architectural Components

A representative multimodal earnings-surprise model has the following layout:

1. **Text encoder** — a financial LLM (FinBERT, FinLlama, or a general-purpose LLM with finance post-training) embeds the transcript into a fixed-dimension vector. Section-aware encoding (separating prepared remarks, MD&A-style discussion, and analyst Q&A) outperforms a single bag-of-text pass.
2. **Audio encoder** — a speech model (wav2vec-style) extracts prosodic and tonal features, especially from Q&A segments where unscripted answers are most informative.
3. **Visual encoder** — a vision-language model extracts text and chart structure from slides; OCR alone loses the visual hierarchy that highlights which numbers management emphasizes.
4. **Cross-modal fusion** — a transformer block with cross-attention layers that lets each modality attend to the others; the alternative (late fusion via concatenation) consistently underperforms.
5. **Classification head** — produces a probability distribution over surprise buckets (large miss / small miss / in-line / small beat / large beat).

## Trading Relevance and Cautions

- **Signal strength.** A modest accuracy lift over consensus generates alpha because the alternative is the analyst consensus itself, which is already priced into the option chain. Even a 2-3 percentage-point edge on directional surprise is tradable around earnings.
- **Liquidity and IV crush.** A correct directional surprise is worthless if execution slippage and post-event IV crush eat the move. Sizing must account for the [[earnings-plays|standard earnings-event volatility structure]].
- **Benchmark vs live.** Reported accuracies in academic benchmarks are upper bounds. Live performance is reduced by data latency (the model needs the call transcript and audio before competing flow does), by selection effects in the labelled training set, and by class imbalance leaking into the test set.
- **Survivorship bias in the labelled set.** Companies that stopped holding calls (delisted, acquired, took going-private routes) are absent from any retrospective dataset, biasing the model toward survivors.
- **Class-imbalance defence.** Use cost-sensitive loss functions (weighted cross-entropy, focal loss) or stratified resampling; never trust raw accuracy.
- **Combine with options-implied move.** The market already prices an expected post-earnings move into the straddle. The trade is in the *gap* between model-implied surprise probability and option-implied move — not in the model output alone.

## Limitations of Current Models

The FinCall-Surprise research highlighted that even specialized financial multimodal models fail to:

- Leverage audio prosody reliably across speakers and call styles.
- Extract structured numbers from slides without OCR-driven errors.
- Generalize cross-sector — a model tuned on tech earnings underperforms on bank earnings where the language register differs.
- Beat a strong text-only baseline by a large margin, suggesting the multimodal frontier is still open.

These are exactly the gaps that next-generation models — Anthropic's [[claude]] family with native multimodal input, plus the multimodal transformer variants surveyed in [[transformer-trading]] — are being benchmarked against.

## Related

- [[earnings-plays]] — the broader event-trading strategy family
- [[earnings-call-analysis]] — qualitative methods for parsing conference calls
- [[earnings-quality]] — fundamental complement to short-window surprise prediction
- [[transformer-trading]] — architectural family these models inherit from
- [[claude]] — multimodal LLM applicable to this task
- [[llm-market-analysis]] — broader LLM-in-trading context
- [[finbert]] — domain-specific text encoder used as the text backbone

## Sources

- [[2026-04-22-gap-finder-ai-2026-major-news-stories]] — Perplexity deep-research gap analysis surfacing FinCall-Surprise and multimodal earnings-prediction literature.

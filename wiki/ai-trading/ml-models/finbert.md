---
title: FinBERT
type: entity
entity_type: protocol
created: 2026-04-06
updated: 2026-04-06
status: good
website: https://huggingface.co/ProsusAI/finbert
tags: [nlp, sentiment, ml-models]
related: ["[[llm-market-analysis]]", "[[sentiment-analysis]]"]
---

# FinBERT

FinBERT is a pre-trained NLP model built on the [[bert]] architecture, fine-tuned specifically on financial text. It understands the nuances of financial language that generic sentiment models miss entirely.

## Why Financial-Specific Models Matter

Generic NLP models fail on financial text because the same words carry different meanings:

- **"Overweight"** — in finance, this means BUY (not heavy)
- **"Underperform"** — means SELL (not doing badly at a task)
- **"Neutral"** — a specific analyst rating, not just lacking sentiment
- **"Restructuring"** — could be positive (efficiency) or negative (distress)
- **"Volatility"** — not inherently negative; traders profit from it

FinBERT was trained on financial news, analyst reports, and corporate communications, so it correctly interprets these domain-specific meanings.

## How It Works

FinBERT takes text input and outputs probability scores across three classes:

```
Input:  "The company reported strong earnings beating expectations"
Output: { positive: 0.92, negative: 0.03, neutral: 0.05 }
```

The model processes text in chunks (max 512 tokens per input). For longer documents like earnings-call-analysis transcripts, you split into sentences or paragraphs and aggregate scores.

## Applications in Trading

- **Earnings call sentiment**: Score each segment of a quarterly call to detect shifts in management confidence
- **News sentiment scoring**: Real-time classification of financial headlines for signal generation
- **Analyst report parsing**: Quantify the tone of research reports beyond their headline rating
- **SEC filing analysis**: Detect subtle language changes between quarterly filings
- **Social media filtering**: Score financial tweets and Reddit posts for actionable sentiment

## Technical Details

| Property | Value |
|----------|-------|
| Base model | BERT-base (110M parameters) |
| Training data | Financial PhraseBank, Reuters financial news |
| Available on | HuggingFace (ProsusAI/finbert) |
| Input limit | 512 tokens |
| Output | 3-class probability (positive/negative/neutral) |
| Inference speed | ~10ms per sentence on GPU |

## Compared to LLMs

FinBERT is much smaller and faster than models like [[gpt-4]] or [[Claude]], making it suitable for high-throughput sentiment scoring where you need to process thousands of documents quickly. However, it only does sentiment classification — it cannot summarize, reason, or generate text like [[llm-market-analysis]] tools can.

For most trading applications, the best approach combines FinBERT for bulk sentiment scoring with LLMs for deeper qualitative analysis on flagged items.

## See Also

- [[llm-market-analysis]] — complementary LLM-based approaches
- [[sentiment-analysis]] — broader overview of sentiment in trading

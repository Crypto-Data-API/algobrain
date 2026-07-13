---
title: "Speech & Audio AI"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Speech AI", "Audio AI", "Speech-to-Text", "TTS", "Whisper"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[chatbot-architectures]]", "[[nlp-overview]]", "[[foundation-models]]", "[[openai]]", "[[natural-language-processing]]", "[[artificial-intelligence]]"]
---

# Speech & Audio AI

**Speech and audio AI** encompasses speech-to-text (STT), text-to-speech (TTS), speaker identification, and audio analysis. In trading, these technologies power voice interfaces (Alfred), earnings call analysis, central bank speech processing, and real-time audio monitoring of financial broadcasts.

## Core Technologies

### Speech-to-Text (STT / ASR)

| Model | Provider | Strengths | Trading Use |
|-------|---------|-----------|-------------|
| **Whisper** | [[openai]] | Best open-source STT, 99+ languages, robust to noise | Transcribe earnings calls, central bank speeches, trading floor audio |
| **Deepgram** | Deepgram | Real-time, streaming, low latency | Live transcription of financial broadcasts |
| **Google Speech-to-Text** | Google | High accuracy, streaming | Production STT pipelines |
| **AssemblyAI** | AssemblyAI | Speaker diarization, summarization built-in | Earnings call analysis with speaker separation |

### Text-to-Speech (TTS)

| Model | Provider | Quality | Trading Use |
|-------|---------|---------|-------------|
| **ElevenLabs** | ElevenLabs | Most natural voices, voice cloning | Alfred's voice interface |
| **OpenAI TTS** | [[openai]] | Good quality, simple API | Audio alerts, portfolio summaries |
| **Bark** | Suno | Open-source, expressive | Self-hosted voice bots |
| **Coqui TTS** | Open-source | Fully local, customizable | Privacy-sensitive deployments |

### Speaker Diarization
Identify who said what in a multi-speaker recording:
- Separate CEO from CFO in earnings calls
- Distinguish analyst questions from management responses
- Track specific speakers across multiple calls

## Trading Applications

### Earnings Call Pipeline
```
Audio recording → Whisper (STT) → Speaker diarization → Transcript
→ NER (extract entities) → Sentiment analysis (per speaker)
→ Compare CEO tone Q/Q → Generate trading signal
```

Management tone in earnings calls has been shown to predict post-earnings price drift — CFOs who use more hedging language ("somewhat", "approximately") tend to precede negative surprises.

### Voice-Activated Trading Assistant
Alfred demonstrates the full pipeline:
1. User speaks → Deepgram STT → text
2. Text → [[anthropic|Claude]] (reasoning, tool calls, wiki search)
3. Response text → ElevenLabs TTS → audio playback

This enables hands-free market queries while monitoring screens.

### Central Bank Speech Analysis
Fed chairs' speeches and press conferences are market-moving. Real-time STT + [[nlp-sentiment-analysis|sentiment analysis]] enables:
- Detect hawkish/dovish shifts seconds after words are spoken
- Compare tone to prepared text (spontaneous answers are more informative)
- Track linguistic patterns that precede policy changes

### Audio Sentiment (Beyond Words)
Advanced models analyze vocal features beyond transcribed text:
- **Pitch variation**: Confidence vs uncertainty
- **Speaking pace**: Rushed delivery may indicate nervousness
- **Pause patterns**: Longer pauses before answers may indicate difficult questions
- **Vocal stress**: Detectable markers of emotional state

This is research-stage for trading but has shown promise in deception detection and confidence estimation.

## Sources

- Radford et al., "Robust Speech Recognition via Large-Scale Weak Supervision" (Whisper), OpenAI, 2022.
- Mayew & Venkatachalam, "The Power of Voice: Managerial Affective States and Future Firm Performance," *Journal of Finance*, 2012 — vocal cues in earnings calls predict performance.
- Hollander, Pronk & Roelofsen, research on earnings-call tone and post-earnings drift.
- ElevenLabs / Deepgram / AssemblyAI product documentation — TTS, streaming STT, and diarization capabilities.

## See Also

- [[chatbot-architectures]] — Conversational AI systems
- [[nlp-overview]] — NLP pipeline hub
- [[openai]] — Creator of Whisper
- [[natural-language-processing]] — NLP fundamentals
- [[nlp-sentiment-analysis]] — Downstream from speech transcription
- [[artificial-intelligence]] — AI section hub

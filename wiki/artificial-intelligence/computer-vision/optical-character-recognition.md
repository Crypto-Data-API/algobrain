---
title: "Optical Character Recognition (OCR)"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["OCR", "Optical Character Recognition"]
domain: [ai-trading]
difficulty: beginner
related: ["[[computer-vision-overview]]", "[[text-preprocessing-finance]]", "[[named-entity-recognition]]", "[[foundation-models]]", "[[convolutional-neural-networks]]", "[[artificial-intelligence]]"]
---

# Optical Character Recognition (OCR)

**OCR** extracts machine-readable text from images, scanned documents, and PDFs. In trading, OCR is essential for processing financial documents that exist as images rather than structured text — brokerage statements, scanned contracts, chart screenshots, and legacy filings.

## OCR Engines

| Engine | Type | Strengths | Best For |
|--------|------|-----------|---------|
| **Tesseract** | Open-source | Free, widely supported | Basic document OCR |
| **Google Document AI** | Cloud | Layout understanding, table extraction | Complex financial documents |
| **AWS Textract** | Cloud | Table + form extraction | Structured financial forms |
| **Azure Document Intelligence** | Cloud | Pre-built financial models | Invoices, receipts, statements |
| **PaddleOCR** | Open-source | Fast, multi-language | High-volume processing |
| **GPT-4V / Claude** | Multimodal LLM | Understands context, not just characters | Screenshots, charts, complex layouts |

## Trading Applications

### Financial Document Processing
| Document | OCR Challenge | Solution |
|----------|--------------|---------|
| **PDF brokerage statements** | Tables, mixed fonts, logos | Document AI with table extraction |
| **Scanned contracts** | Handwriting, signatures, stamps | Tesseract + post-processing |
| **Chart screenshots** | Numbers embedded in images | Multimodal LLM (Claude/GPT-4V) |
| **Trade confirmations** | Dense tabular data | AWS Textract with form extraction |
| **Historical filings** | Pre-digital scanned documents | Tesseract + [[named-entity-recognition|NER]] pipeline |

### Screenshot-to-Data
Traders share screenshots of positions, PnL, and charts on social media. OCR extracts:
- Position sizes and entry prices from brokerage screenshots
- PnL numbers from trading platform screenshots
- Price levels and indicators from chart images

### Legacy Data Digitization
Converting historical financial documents (pre-2000s SEC filings, old annual reports) from scanned images into searchable, analyzable text for long-term historical analysis.

## Modern Approach: Multimodal LLMs

[[foundation-models|Multimodal LLMs]] (GPT-4V, Gemini, Claude) are increasingly replacing traditional OCR for trading use cases:

| Dimension | Traditional OCR | Multimodal LLM |
|-----------|----------------|---------------|
| **Character accuracy** | 95-99% | 90-98% |
| **Context understanding** | None — just reads characters | Understands the document's meaning |
| **Table extraction** | Requires specialized models | Handles natively |
| **Chart interpretation** | Cannot — just reads text | Can describe chart patterns and data |
| **Cost** | Low (self-hosted) | Higher (API per image) |
| **Setup** | Requires pipeline engineering | Single API call |

For most trading workflows, sending a screenshot to Claude/GPT-4V and asking "What data is in this image?" is simpler and more powerful than a traditional OCR pipeline.

## See Also

- [[computer-vision-overview]] — CV hub
- [[text-preprocessing-finance]] — Processing extracted text
- [[named-entity-recognition]] — Extracting entities from OCR'd text
- [[foundation-models]] — Multimodal LLMs replacing traditional OCR
- [[convolutional-neural-networks]] — Architecture powering OCR models
- [[artificial-intelligence]] — AI section hub

## Sources

- Tesseract OCR project documentation (Apache 2.0, originally HP / now Google-sponsored)
- Google Document AI, AWS Textract, and Azure AI Document Intelligence product documentation (cloud OCR with table/form extraction)
- PaddleOCR (Baidu) open-source documentation
- Anthropic Claude and OpenAI GPT-4V/GPT-4o vision API documentation — multimodal document understanding
- Comparative accuracy figures (traditional OCR ~95–99% character accuracy vs multimodal LLM ~90–98%) are approximate industry rules of thumb and vary by document quality

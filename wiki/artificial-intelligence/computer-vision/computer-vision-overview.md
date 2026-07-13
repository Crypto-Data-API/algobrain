---
title: "Computer Vision"
type: overview
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Computer Vision", "CV"]
related: ["[[computer-vision-trading]]", "[[object-detection]]", "[[image-segmentation]]", "[[image-generation-ai]]", "[[optical-character-recognition]]", "[[video-analysis-trading]]", "[[convolutional-neural-networks]]", "[[cnn-chart-recognition]]", "[[deep-learning-overview]]", "[[artificial-intelligence]]"]
---

# Computer Vision

**Computer vision** (CV) is the branch of AI that enables machines to interpret and act on visual information. For trading, CV extracts signals from charts, documents, satellite imagery, and video — data sources that text-based models cannot process. This section covers the core CV tasks and their financial applications.

For a high-level introduction, see [[computer-vision-trading]]. For the neural architecture powering most CV, see [[convolutional-neural-networks]].

## Core CV Tasks

| Task | What It Does | Page | Trading Application |
|------|-------------|------|-------------------|
| **Image Classification** | Assign a label to an entire image | [[convolutional-neural-networks]] | Chart pattern recognition (head-and-shoulders, flag) |
| **[[object-detection]]** | Find and locate objects within an image | [[object-detection]] | Count cars in parking lots, ships at ports |
| **[[image-segmentation]]** | Label every pixel in an image | [[image-segmentation]] | Measure oil tank fill levels from satellite, crop health mapping |
| **[[optical-character-recognition|OCR]]** | Extract text from images | [[optical-character-recognition]] | Parse screenshots, brokerage PDFs, hand-written trade tickets |
| **[[image-generation-ai|Image Generation]]** | Create new images from descriptions or noise | [[image-generation-ai]] | Synthetic chart data, scenario visualization |
| **Video Analysis** | Process video frame-by-frame | [[video-analysis-trading]] | Foot traffic counting, trading floor monitoring |

## The CV Pipeline for Trading

```
Visual Data Source → Preprocessing → Model → Structured Output → Trading Signal
```

| Source | Preprocessing | Model | Output |
|--------|--------------|-------|--------|
| Candlestick chart | Crop, normalize, resize | CNN classifier | Pattern label + confidence |
| Satellite photo | Geo-align, cloud filter | [[object-detection|Object detector]] | Object counts + locations |
| PDF statement | Page extraction | [[optical-character-recognition|OCR]] + NER | Structured financial data |
| Parking lot image | Perspective correction | [[image-segmentation|Segmentation]] | Occupancy percentage |
| Earnings slide deck | Slide extraction | Multimodal LLM | Text + table extraction |

## CV Models by Era

| Era | Model | Innovation | Trading Relevance |
|-----|-------|-----------|-------------------|
| **2012** | AlexNet | Deep CNNs beat traditional CV | Proved deep learning works for images |
| **2014** | VGG, GoogLeNet | Deeper networks, inception modules | Better feature extraction |
| **2015** | ResNet | Skip connections, 100+ layers | Foundation for most CV transfer learning |
| **2015** | Faster R-CNN | Real-time [[object-detection|object detection]] | Enabled satellite imagery analysis at scale |
| **2016** | YOLO (You Only Look Once) | Single-pass detection, very fast | Real-time video analysis |
| **2017** | Mask R-CNN | Instance [[image-segmentation|segmentation]] | Pixel-level measurement (tank fill, crop area) |
| **2020** | Vision Transformer (ViT) | [[attention-mechanism|Attention]] for images | Bridged CV and NLP architectures |
| **2021** | CLIP (OpenAI) | Image-text alignment | Zero-shot image classification from text descriptions |
| **2022** | Stable Diffusion | [[diffusion-models|Diffusion]]-based [[image-generation-ai|generation]] | Synthetic data, visualization |
| **2023+** | GPT-4V, Gemini | Multimodal [[foundation-models|LLMs]] | Send a chart screenshot, get analysis in natural language |

## Multimodal AI: The Convergence

Modern [[foundation-models|foundation models]] (GPT-4o, Gemini, Claude) are **multimodal** — they process both text and images simultaneously. This changes CV for trading:

- **Before**: Build a custom CNN, train on labeled charts, deploy separately from text analysis
- **Now**: Upload a chart screenshot to Claude/GPT-4 and ask "What pattern is this? What's the likely direction?"

Multimodal models don't replace specialized CV (satellite analysis still needs object detectors), but they dramatically lower the barrier for visual analysis in trading research.

## See Also

- [[computer-vision-trading]] — High-level introduction with trading focus
- [[object-detection]] — Locating objects in images
- [[image-segmentation]] — Pixel-level image understanding
- [[optical-character-recognition]] — Extracting text from images
- [[image-generation-ai]] — Creating synthetic visual data
- [[convolutional-neural-networks]] — The architecture powering CV
- [[cnn-chart-recognition]] — Applied chart pattern recognition
- [[video-analysis-trading]] — Video/foot-traffic analysis for alt data
- [[deep-learning-overview]] — Deep learning hub
- [[artificial-intelligence]] — AI section hub

## Sources

- Foundational CV architecture papers: AlexNet (2012), VGG/GoogLeNet (2014), ResNet (2015), Faster R-CNN (2015), YOLO (2016), Mask R-CNN (2017), Vision Transformer (2020), CLIP (2021).
- Stable Diffusion (Stability AI, 2022) and multimodal foundation models (GPT-4V, Gemini, Claude) — vendor documentation.
- General industry knowledge of the computer-vision field and its alternative-data applications in trading (no proprietary source ingested for this page).

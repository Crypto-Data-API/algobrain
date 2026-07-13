---
title: "Image Segmentation"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Image Segmentation", "Semantic Segmentation", "Instance Segmentation"]
domain: [ai-trading]
difficulty: advanced
related: ["[[computer-vision-overview]]", "[[object-detection]]", "[[convolutional-neural-networks]]", "[[computer-vision-trading]]", "[[deep-learning-overview]]", "[[artificial-intelligence]]"]
---

# Image Segmentation

**Image segmentation** assigns a class label to every pixel in an image, providing the most detailed understanding of visual content. While [[object-detection|object detection]] draws bounding boxes, segmentation draws exact boundaries — critical when precise measurement matters, such as estimating oil tank fill levels or mapping agricultural crop health from satellite imagery.

## Types of Segmentation

| Type | What It Does | Output | Trading Example |
|------|-------------|--------|----------------|
| **Semantic** | Labels every pixel by class | "This pixel is road, this is building" | Land use mapping for real estate analysis |
| **Instance** | Distinguishes individual objects of same class | "This is car #1, this is car #2" | Count specific vehicles in a parking lot |
| **Panoptic** | Combines semantic + instance | Complete scene understanding | Full infrastructure monitoring |

## Key Models

| Model | Type | Innovation |
|-------|------|-----------|
| **U-Net** | Semantic | Encoder-decoder with skip connections — excellent for medical/satellite |
| **Mask R-CNN** | Instance | Extends Faster R-CNN with pixel-level masks |
| **DeepLab v3+** | Semantic | Atrous convolutions for multi-scale features |
| **SAM** (Segment Anything, Meta) | Universal | Zero-shot segmentation — segment any object with a point/box prompt |
| **SAM 2** | Universal + Video | Extends SAM to video sequences |

### SAM: A Game Changer

Meta's **Segment Anything Model** (2023) can segment any object in any image without task-specific training. For trading alternative data:
- Point at an oil tank in a satellite image → SAM segments it precisely → measure shadow angle → estimate fill level
- No custom training needed — works out of the box on novel targets

## Trading Applications

### Precise Measurement from Satellite Imagery

| Target | Measurement | Signal |
|--------|------------|--------|
| **Oil tank fill level** | Segment floating roof → measure shadow → calculate volume | Crude inventory → oil futures |
| **Crop health** | Segment farmland → calculate NDVI (vegetation index) per field | Yield forecast → grain futures |
| **Solar farm output** | Segment panel area → estimate capacity | Renewable energy production |
| **Flood/fire damage** | Segment affected area | Insurance claims → insurance stock impact |
| **Urban development** | Segment construction vs completed buildings | Real estate market activity |

### Document Understanding

Segment document regions (tables, charts, text blocks, headers) for automated extraction:
- SEC filings with complex layouts
- Earnings presentation slide decks
- Financial statements with nested tables

## Segmentation vs Detection: When to Use Which

| Criterion | [[object-detection|Detection]] | Segmentation |
|-----------|-----------|--------------|
| **Need** | Count objects, rough location | Precise boundaries, area measurement |
| **Speed** | Faster | Slower |
| **Data labeling** | Bounding boxes (faster to label) | Pixel masks (expensive to label) |
| **Use case** | "How many ships?" | "What's the exact area of this oil slick?" |

## See Also

- [[computer-vision-overview]] — CV hub
- [[object-detection]] — Bounding-box-level detection
- [[convolutional-neural-networks]] — Architecture foundation
- [[computer-vision-trading]] — Trading applications overview
- [[deep-learning-overview]] — Deep learning hub
- [[artificial-intelligence]] — AI section hub

## Sources

- Segmentation architecture papers: U-Net (2015), Mask R-CNN (2017), DeepLab v3+ (2018), Meta Segment Anything SAM (2023) and SAM 2 (2024, video).
- Established alternative-data methodology: satellite-imagery tank-fill estimation via floating-roof shadow geometry; NDVI crop-health mapping for agricultural-futures forecasting.
- General industry knowledge of pixel-level CV and its trading alternative-data uses (no proprietary source ingested for this page).

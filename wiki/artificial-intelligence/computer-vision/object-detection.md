---
title: "Object Detection"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Object Detection", "YOLO", "Faster R-CNN"]
domain: [ai-trading]
difficulty: advanced
related: ["[[computer-vision-overview]]", "[[image-segmentation]]", "[[convolutional-neural-networks]]", "[[computer-vision-trading]]", "[[deep-learning-overview]]", "[[artificial-intelligence]]"]
---

# Object Detection

**Object detection** locates and classifies multiple objects within an image, outputting bounding boxes and class labels for each detected object. Unlike image classification (one label per image), detection answers "what objects are where?" In trading, object detection powers alternative data strategies based on satellite imagery, foot traffic, and physical-world monitoring.

## Key Architectures

| Model | Speed | Accuracy | Best For |
|-------|-------|----------|---------|
| **YOLO v8/v9** (You Only Look Once) | Very fast (real-time) | Good | Real-time video, streaming analysis |
| **Faster R-CNN** | Moderate | High | High-accuracy satellite analysis |
| **DETR** (Detection Transformer) | Moderate | High | End-to-end detection without anchors |
| **RT-DETR** | Fast | High | Best of both — fast + accurate |

### Two-Stage vs One-Stage

| Approach | How | Example |
|----------|-----|---------|
| **Two-stage** | First propose regions, then classify each | Faster R-CNN — accurate but slower |
| **One-stage** | Detect and classify in a single pass | YOLO — faster, slightly less accurate |

## Trading Applications

### Satellite Imagery — Alternative Data

| Target | What to Detect | Trading Signal |
|--------|---------------|---------------|
| **Retail parking lots** | Cars | Foot traffic → quarterly revenue prediction for WMT, TGT, COST |
| **Shipping ports** | Container ships, cranes | Global trade volume → shipping stocks, commodity prices |
| **Oil storage** | Floating-roof tank shadows | Crude inventory levels → oil price direction |
| **Construction sites** | Cranes, equipment | Real estate activity → homebuilder stocks, materials |
| **Airport activity** | Aircraft on tarmac | Airline capacity utilization → airline stocks |
| **Agricultural fields** | Crop health, harvested areas | Yield estimates → corn, wheat, soy futures |

### Foot Traffic Analysis

Detect and count people at specific locations:
- Mall entrances → retail REIT performance
- Restaurant chains → same-store sales prediction
- Theme parks → entertainment company revenue

### Supply Chain Monitoring

Detect trucks, trains, containers at logistics hubs:
- Amazon warehouse activity → AMZN quarterly estimates
- Port congestion (ships waiting) → supply chain bottleneck signals
- Rail car counts → industrial production proxy

## Data Sources

| Provider | Coverage | Resolution | Cost |
|----------|----------|-----------|------|
| **Planet Labs** | Daily global coverage | 3-5m | $$ |
| **Maxar** | High-resolution on demand | 30cm | $$$ |
| **Sentinel-2** (ESA) | Global, free | 10m | Free |
| **Google Earth Engine** | Aggregated satellite + aerial | Varies | Free (research) |
| **Orbital Insight** | Pre-processed trading signals | N/A (processed) | $$$$ |

## The Alternative Data Moat

Object detection on satellite imagery was once a hedge fund secret weapon (firms like Two Sigma, Citadel). As providers like Orbital Insight and SpaceKnow commercialized the signals, the alpha decayed. The lesson: detection *technology* is commoditized; the edge comes from proprietary data sources, faster processing, or novel targets nobody else is counting.

## See Also

- [[computer-vision-overview]] — CV hub
- [[image-segmentation]] — Pixel-level analysis (more precise than detection)
- [[convolutional-neural-networks]] — The architecture powering detection
- [[computer-vision-trading]] — Trading applications overview
- [[deep-learning-overview]] — Deep learning hub
- [[artificial-intelligence]] — AI section hub

## Sources

- Redmon et al., "You Only Look Once: Unified, Real-Time Object Detection" (CVPR 2016) — the original YOLO architecture
- Ren et al., "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks" (NeurIPS 2015)
- Carion et al., "End-to-End Object Detection with Transformers" (DETR, ECCV 2020)
- Ultralytics YOLOv8/YOLOv11 documentation — current real-time detection reference
- Planet Labs, Maxar, ESA Sentinel-2, and Orbital Insight public product documentation (satellite imagery providers and resolutions)
- General industry reporting on hedge-fund use of satellite alternative data (e.g., parking-lot car counts for retail revenue estimation) and subsequent alpha decay as providers commercialized the signals

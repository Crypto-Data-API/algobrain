---
title: "Sensor Fusion"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["Sensor Fusion", "Multi-Sensor Perception"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[robotics-overview]]", "[[autonomous-vehicles]]", "[[computer-vision-overview]]", "[[object-detection]]", "[[artificial-intelligence]]"]
---

# Sensor Fusion

**Sensor fusion** combines data from multiple sensor types to create a unified, robust perception of the environment. No single sensor is sufficient for reliable autonomy — cameras struggle at night, lidar is expensive and sparse, radar is low-resolution. Fusing them together compensates for individual weaknesses. The approach mirrors how traders combine multiple data sources for a more complete market picture.

## Sensor Modalities

| Sensor | Measures | Strengths | Weaknesses | Cost |
|--------|---------|-----------|-----------|------|
| **Camera** | 2D images, colour, texture | Rich detail, cheap, dense | No native depth, struggles in darkness/glare | $20-200 |
| **Lidar** | 3D point cloud (laser) | Precise 3D geometry, works in darkness | Expensive, sparse, degraded in rain/snow | $1K-10K+ |
| **Radar** | Distance + velocity | Works in all weather, measures speed directly | Low resolution, false positives from clutter | $50-500 |
| **Ultrasonics** | Short-range distance | Very cheap, reliable for parking | Very short range (<5m), no detail | $5-20 |
| **IMU** (Inertial) | Acceleration, rotation | Instant response, no external dependency | Drifts over time, needs calibration | $10-100 |
| **GPS/GNSS** | Global position | Global reference frame | Inaccurate in cities (multipath), latency | $10-1K |

## Fusion Architectures

| Architecture | How | Used By |
|-------------|-----|---------|
| **Early fusion** | Combine raw sensor data before processing | Produces richest representation, most complex |
| **Late fusion** | Process each sensor independently, combine detections | Simpler, modular, easier to debug |
| **Mid-level fusion** | Combine intermediate features | Balance of richness and modularity |
| **BEV fusion** (Bird's Eye View) | Project all sensors into top-down spatial grid | Dominant in modern AV (Tesla, Waymo) |

## The Trading Analogy

Sensor fusion in robotics parallels **multi-source data integration** in trading:

| Robotics                      | Trading                                      |
| ----------------------------- | -------------------------------------------- |
| Camera (rich but no depth)    | Price action (rich but lagging)              |
| Lidar (precise 3D)            | Order book depth (precise but expensive)     |
| Radar (velocity, all-weather) | Volume data (flow speed, always available)   |
| GPS (global position)         | Macro data (where we are in the cycle)       |
| IMU (instant acceleration)    | Tick data (instant momentum)                 |
| **Fused perception**          | **Multi-factor model combining all sources** |

The principle is the same: no single data source gives complete information. Robust decisions require fusing multiple sources while accounting for each source's reliability and latency.

## Investment Angle

| Company | Sensor Focus | Ticker |
|---------|-------------|--------|
| **[[luminar-technologies|Luminar]]** | Automotive lidar | LAZR |
| **Innoviz** | Automotive lidar | INVZ |
| **Aeva** | Frequency-modulated lidar (velocity + range) | AEVA |
| **[[mobileye-global|Mobileye]]** (Intel) | Camera-centric + radar fusion | MBLY |
| **ON Semiconductor** | Image sensors for automotive | ON |
| **Texas Instruments** | Automotive radar chips | TXN |

## See Also

- [[robotics-overview]] — Broader robotics context
- [[autonomous-vehicles]] — Primary application
- [[computer-vision-overview]] — Visual perception
- [[object-detection]] — Detecting objects from fused sensor data
- [[artificial-intelligence]] — AI section hub

## Sources

- Standard references on Kalman filtering and Bayesian sensor fusion
- Tesla / Waymo published perception-stack descriptions (BEV fusion, occupancy networks)
- Company product disclosures: Luminar (LAZR), Innoviz (INVZ), Aeva (AEVA), Mobileye (MBLY)

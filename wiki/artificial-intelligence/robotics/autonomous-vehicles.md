---
title: "Autonomous Vehicles"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["Autonomous Vehicles", "Self-Driving", "AV", "FSD"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[robotics-overview]]", "[[motion-planning]]", "[[sensor-fusion]]", "[[sim-to-real]]", "[[reinforcement-learning]]", "[[computer-vision-overview]]", "[[nvidia-ai]]", "[[artificial-intelligence]]"]
---

# Autonomous Vehicles

**Autonomous vehicles** (AVs) are the highest-value application of robotics AI — the global automotive market exceeds $5 trillion, and autonomy promises to transform transportation, logistics, ride-hailing, trucking, and last-mile delivery. For traders, AV represents one of the largest AI-driven sector transformations underway, with direct exposure through automakers, sensor companies, and AI compute providers.

## SAE Autonomy Levels

| Level | Name | What It Means | Examples |
|-------|------|--------------|---------|
| **0** | No Automation | Human does everything | Most cars today |
| **1** | Driver Assistance | System controls steering OR speed | Adaptive cruise control |
| **2** | Partial Automation | System controls steering AND speed, human monitors | Tesla Autopilot, GM Super Cruise |
| **2+** | Advanced Assistance | L2 with less required attention | Tesla FSD (supervised) |
| **3** | Conditional Automation | System drives in specific conditions, human as fallback | Mercedes Drive Pilot (limited roads) |
| **4** | High Automation | System handles all driving in defined area, no human needed | Waymo (geofenced robotaxi), Tesla robotaxi (Austin, supervised launch 2025) |
| **5** | Full Automation | System handles all driving everywhere | Does not exist |

## Key Players

| Company | Approach | Status | Ticker/Exposure |
|---------|---------|--------|----------------|
| **Tesla** | Vision-only (cameras), end-to-end neural nets | L2+ (FSD supervised); robotaxi launched in Austin mid-2025 (geofenced, supervised), pursuing wider L4 | TSLA |
| **Waymo** (Alphabet) | Lidar + cameras + radar, HD maps | L4 driverless robotaxi in SF, Phoenix, LA, Austin; expanding to Atlanta, Miami, Dallas, Nashville | GOOGL |
| **Cruise** (GM) | Lidar + cameras, HD maps | **Robotaxi shut down** — GM ended Cruise robotaxi development Dec 2024, folded the team into GM's personal-autonomy / Super Cruise effort (~$1B+ annual savings) | GM |
| **Aurora** | Trucking-first, lidar-heavy | Launched driverless commercial trucking (Dallas–Houston) in 2024; scaling lanes | AUR |
| **Mobileye** (Intel) | Camera + radar, chipset supplier | L2+ technology provider to OEMs | MBLY |
| **Pony.ai** | Robotaxi in China | L4 in Chinese cities | PONY |
| **NVIDIA** | Compute platform (DRIVE) | Infrastructure provider | NVDA |

## The Technology Stack

```
Sensors (see, hear, feel)
  → Perception (what's around me?)
    → Prediction (what will other agents do?)
      → Planning (what should I do?)
        → Control (execute the plan)
```

| Layer | Technology | Key Challenge |
|-------|-----------|--------------|
| **Sensors** | [[sensor-fusion|Cameras + lidar + radar + ultrasonics]] | Cost, reliability, weather degradation |
| **Perception** | [[object-detection|Object detection]], [[image-segmentation|segmentation]], 3D scene understanding | Edge cases (construction, emergency vehicles, pedestrians) |
| **Prediction** | Motion forecasting, intent prediction | Predicting what other drivers/pedestrians will do |
| **[[motion-planning|Planning]]** | Route planning + trajectory generation | Safe, comfortable, efficient paths in dynamic environments |
| **Control** | Steering, acceleration, braking | Sub-millisecond response, smooth execution |

## The Vision vs Lidar Debate

| | Tesla (Vision-Only) | Waymo/Cruise (Lidar + Vision) |
|---|---|---|
| **Sensor cost** | ~$200 (cameras) | ~$10,000+ (lidar + cameras + radar) |
| **3D perception** | Inferred from 2D images via neural nets | Direct 3D point cloud from lidar |
| **Scalability** | Every Tesla is a data collector | Expensive sensor suite limits fleet size |
| **Night/weather** | Cameras degrade in rain/fog | Lidar works in darkness, partially in weather |
| **Data advantage** | Billions of miles from customer fleet | Millions of miles from dedicated test fleet |
| **Path to L5** | Bet on scaling neural nets | Bet on sensor fusion + HD maps |

This is one of the most consequential technology bets in AI. Tesla's approach (cheaper sensors + more data + end-to-end learning) vs Waymo's (better sensors + engineered redundancy) will determine which companies capture the autonomous market.

## Trading Angles

- **Tesla (TSLA)**: Priced as an AI/autonomy company, not just a car company. FSD progress is the key catalyst. Earnings calls mentioning FSD milestones move the stock dramatically
- **NVIDIA (NVDA)**: DRIVE platform powers AV compute. Revenue from automotive segment growing as L2+/L4 deployments scale
- **Lidar companies** (LAZR, INVZ, AEVA): Existential risk if Tesla's vision-only approach wins. High optionality if lidar proves necessary
- **Ride-hailing** (UBER, LYFT): Autonomous robotaxis could either destroy their business (no human drivers) or save it (zero driver cost). Uber has pivoted toward an aggregator model, partnering with Waymo and others rather than building its own AV stack
- **Trucking** (AUR, autonomous freight): Potentially faster path to deployment than robotaxis (highways are simpler than cities). Aurora's 2024 driverless launch is an early proof point
- **Insurance**: Autonomous vehicles could dramatically reduce accidents — disrupting the ~$300B auto insurance market — but shift liability from drivers to manufacturers/operators

## Catalysts to Watch

- Tesla FSD version releases and robotaxi geographic expansion (each new city is a re-rating catalyst)
- Waymo paid-trip volume milestones and new-city launches
- Regulatory decisions (NHTSA rules on driverless deployment, state-level permits)
- Disengagement / safety incident data (a high-profile accident can stall an entire program — see Cruise's 2023 pedestrian incident that preceded its shutdown)
- Lidar cost curves (sub-$500 automotive lidar would weaken Tesla's cost argument)

## See Also

- [[robotics-overview]] — Broader robotics landscape
- [[motion-planning]] — How AVs plan trajectories
- [[sensor-fusion]] — How AVs perceive the world
- [[sim-to-real]] — How AVs train in simulation
- [[nvidia-ai]] — AV compute platform
- [[computer-vision-overview]] — Perception technology
- [[reinforcement-learning]] — End-to-end driving policies
- [[artificial-intelligence]] — AI section hub

## Sources

- SAE International — J3016 Levels of Driving Automation standard
- GM / Cruise — Dec 2024 announcement ending Cruise robotaxi development and refocusing on Super Cruise
- Waymo — operational service updates (San Francisco, Phoenix, Los Angeles, Austin; expansion cities)
- Tesla — robotaxi (Austin) launch communications and FSD release notes, 2025
- Aurora Innovation — driverless commercial trucking launch (Dallas–Houston), 2024
- NVIDIA — DRIVE platform automotive documentation

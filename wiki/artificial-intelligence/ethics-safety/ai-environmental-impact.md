---
title: "AI Environmental Impact"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["AI Environmental Impact", "AI Energy", "AI Carbon"]
domain: [risk-management]
difficulty: beginner
related: ["[[ethics-safety-overview]]", "[[model-inference-vs-training]]", "[[nvidia-ai]]", "[[foundation-models]]", "[[artificial-intelligence]]"]
---

# AI Environmental Impact

Training and running AI models consumes large amounts of energy. Published estimates put GPT-4's training at roughly tens of GWh (commonly cited ~50 GWh — equivalent to several thousand US households for a year), though exact figures are unverified and contested. As AI scales, energy consumption has become a material concern for ESG-focused investors, data-centre companies, and energy markets — and, as of 2026, the single biggest driver of the data-centre power-demand thesis.

## The Numbers

| Activity | Energy Estimate | Equivalent |
|----------|----------------|-----------|
| **Training GPT-4** | ~50 GWh | 5,000 US households/year |
| **Training LLaMA 2 70B** | ~8 GWh | 800 households/year |
| **One ChatGPT query** | ~10x a Google search | ~0.01 kWh vs 0.001 kWh |
| **Global AI compute** (2024) | ~4% of US electricity | Growing 30-40% annually |

## Trading Implications

### Data Centre Power Demand
AI is the primary driver of data centre electricity growth:
- Data centre electricity demand projected to double by 2030
- Utilities near major data centres (Virginia, Texas, Ireland) benefit
- Nuclear power is being reconsidered for AI compute (Microsoft + Three Mile Island, Amazon + Talen Energy)

### Investable Themes

| Theme | Companies | Thesis |
|-------|----------|-------|
| **Data centre REITs** | EQIX, DLR, QTS | AI compute demand drives occupancy and pricing |
| **Utilities** | NEE, VST, CEG | Power demand from hyperscale data centres |
| **Nuclear** | CEG (Constellation), SMR | Clean baseload for AI compute |
| **Cooling** | VRT (Vertiv), SNPS | Liquid cooling for dense GPU clusters |
| **Power infrastructure** | ETN (Eaton), PWR (Quanta) | Grid upgrades for data centre loads |
| **Chip efficiency** | [[nvidia-ai|NVDA]], AMD | More efficient chips reduce energy per computation |

### ESG Considerations
- AI companies face scrutiny on Scope 2 emissions (electricity consumption)
- [[foundation-models|Foundation model]] providers (Microsoft/OpenAI, Google, Anthropic) publish sustainability reports
- Carbon offset purchasing by AI companies is growing
- Efficient architectures (Mixture of Experts, distillation, quantisation) reduce per-query energy — [[model-inference-vs-training|inference efficiency]] is improving

## The Efficiency Counterargument

AI also enables energy savings:
- Smart grid optimisation reduces energy waste
- AI-designed materials improve solar/battery efficiency
- Autonomous vehicles (properly deployed) could reduce transport energy
- [[ai-science|AI weather forecasting]] improves renewable energy integration

The net impact is debated — AI consumes energy but also creates energy efficiencies elsewhere.

## See Also

- [[ethics-safety-overview]] — Ethics hub
- [[model-inference-vs-training]] — Compute economics driving energy demand
- [[nvidia-ai]] — GPU efficiency improvements
- [[foundation-models]] — The models consuming the energy
- [[artificial-intelligence]] — AI section hub

## Sources

- International Energy Agency (IEA) reports on data-centre and AI electricity demand
- Public reporting on AI-nuclear power deals: Microsoft-Constellation (Three Mile Island restart), Amazon-Talen Energy
- Hyperscaler sustainability reports (Microsoft, Google, Anthropic) on Scope 2 emissions
- Energy-per-query and training-energy estimates from AI energy research (figures are estimates and vary by methodology)

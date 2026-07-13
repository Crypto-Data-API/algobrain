---
title: Arm Holdings plc
type: entity
created: 2026-04-13
updated: 2026-06-19
status: excellent
tags: [company, stocks, ai-trading, machine-learning, technology, options, derivatives]
entity_type: company
founded: 1990
headquarters: Cambridge, England
website: https://www.arm.com
aliases: ["ARM", "Arm Holdings plc"]
ticker: ARM
exchange: NASDAQ
sector: Semiconductors
industry: Semiconductors
sp500: false
ai_category: Semiconductors
market_cap_tier: Large Cap
related: ["[[ai-trading-overview]]", "[[amd]]", "[[artificial-intelligence]]", "[[broadcom]]", "[[intel]]", "[[model-inference-vs-training]]", "[[nvidia]]", "[[nvidia-ai]]", "[[qualcomm]]", "[[technology]]", "[[options]]", "[[implied-volatility]]"]
options_liquidity_tier: "Tier 2 - High Liquidity"
options_volume: "High"
---

Arm Holdings plc (NASDAQ: ARM) is a British semiconductor and software design company that licenses the ARM instruction set architecture used in the vast majority of mobile devices and an increasing share of [[artificial-intelligence|AI]] accelerators worldwide. Founded in 1990 as a joint venture between Acorn Computers, Apple, and VLSI Technology, and headquartered in Cambridge, England, Arm operates a design-and-license business model rather than manufacturing chips directly. Majority-owned by SoftBank Group since 2016, Arm re-listed on NASDAQ in September 2023 in one of the year's largest IPOs, with its architecture powering an estimated 99% of the world's smartphones and expanding rapidly into data center AI inference workloads.

## Business Overview

Arm earns revenue from two streams: **licensing** (upfront fees for architecture and compute-subsystem licenses) and **royalties** (per-chip fees, rising with Armv9 adoption, which carries roughly double the royalty rate of v8). Growth vectors are data-center CPUs (Graviton, Grace, Axion, Cobalt are all Arm-based), edge/automotive AI, and a move up the value chain via Compute Subsystems (CSS) and exploratory chiplet/full-SoC work. SoftBank still owns ~88-90% of shares, leaving a small public float that amplifies volatility.

## Business Segments (Detail)

Arm is fabless and capital-light — it designs and licenses intellectual property rather than manufacturing silicon. Its economics run on a two-stage model that traders must understand because the two streams behave very differently:

| Revenue stream | What it is | Timing | Driver |
|---|---|---|---|
| **Licensing** | Upfront and term fees for access to architecture (architecture license, ARM Total Access / ATA subscriptions) and Compute Subsystems (CSS) | Lumpy, recognized at/over signing; leading indicator of future royalties | New design starts, AI/data-center customers, SoftBank-related deals |
| **Royalties** | Per-chip fees on every Arm-based chip shipped, set as a percentage of chip ASP or a fixed per-unit fee | Recurring, lagging (chips ship years after the license) | Unit volumes × royalty rate; **Armv9 mix** (≈2× the v8 rate) and **CSS adoption** (higher rate again) |

The strategic flywheel: licensing seeds future royalties. Each Armv9 and CSS design win raises the *rate per chip*, so Arm can grow royalty revenue even if unit volumes are flat. Product lines by end-market:

- **Mobile / client** — the historical core; ~99% of smartphone application processors. Mature, cyclical with the handset market.
- **Data center / cloud** — the inflection driver. Hyperscaler custom CPUs (AWS Graviton, NVIDIA Grace, Google Axion, Microsoft Cobalt) are all Arm-based; cloud/networking royalties trending toward 15–20% of total royalties.
- **Automotive** — ADAS and in-vehicle compute; long design cycles, rising content per car.
- **IoT / embedded** — broad, fragmented, lower ASP.

## Competitive Positioning / Peers

Arm is the architecture layer beneath much of computing; it both competes with and is licensed by the rest of the semiconductor complex.

| Company | Relationship to ARM | Axis |
|---|---|---|
| [[nvidia]] | Customer (Grace CPU is Arm-based) + ecosystem partner | AI data-center compute |
| [[qualcomm]] | Largest mobile licensee; also a litigation counterparty (Nuvia/Oryon dispute) | Mobile + PC SoCs, licensing terms |
| [[intel]] | Architecture rival (x86) | Data-center and PC CPUs |
| [[amd]] | Architecture rival (x86); also explores Arm | Data-center and client CPUs |
| [[broadcom]] | Custom-silicon / ASIC designer using Arm IP | Custom AI accelerators, networking |
| RISC-V (open ISA) | The key long-term *substitute* threat | Royalty-free alternative architecture |
| [[taiwan-semiconductor-manufacturing]] | Foundry that fabs Arm-based chips (not a competitor) | Manufacturing ecosystem |

Arm's moat is the **software/ecosystem lock-in** of the world's most widely deployed instruction set plus the power-efficiency lead that matters more as energy becomes the binding constraint in data centers. The principal architectural threat is **RISC-V**, an open, royalty-free ISA that customers can adopt to design around Arm royalties.

## Bull vs Bear Case

**Bull case**
- **Armv9 + CSS rate mix** lifts royalty per chip structurally — revenue grows faster than unit volumes.
- **Data-center inflection**: hyperscaler custom Arm CPUs and AI-server CPUs are a multi-year secular tailwind; power efficiency is a decisive advantage as compute scales.
- **Capital-light, high-margin** IP model with a vast installed base and decades-long ecosystem lock-in.
- **Up-the-stack move** into Compute Subsystems and potentially full chips raises take per design.

**Bear case**
- **Premium valuation** versus royalty growth — the stock fell ~24% in calendar 2025 on exactly this concern.
- **Smartphone-cycle dependence** — the royalty base is still heavily mobile; handset softness hits results.
- **RISC-V** erosion of the royalty model over time.
- **Customer in-housing / design-around** risk and licensing disputes (e.g., the [[qualcomm]] Nuvia/Oryon litigation).
- **SoftBank concentration** — ~90% ownership means a tiny float (extreme volatility) and a constant secondary-offering supply overhang; SoftBank is also a large *related-party customer*.

## Valuation Framework (Qualitative)

Arm trades on a **royalty + licensing growth** multiple that is closer to a software/IP company than to a cyclical chipmaker, because of its capital-light model and recurring royalty stream. The multiple is driven by:

1. **Royalty growth trajectory** — the recurring, compounding base; the market pays for rising royalty *per chip* (Armv9/CSS mix) on top of unit growth.
2. **Licensing momentum** — leading indicator; big license signings (AI, data center, SoftBank-related) presage future royalties.
3. **Data-center royalty mix** — the share of royalties from cloud/AI, the highest-conviction secular leg.
4. **Operating leverage** — incremental royalty revenue is near-pure margin given the fixed R&D base (~$2.6B TTM).
5. **Optionality** — Compute Subsystems and any full-SoC business model expanding take per design.

The risk to the multiple is that royalty growth must continually justify a rich valuation; deceleration (smartphone weakness, RISC-V) compresses it quickly. Because of the SoftBank float dynamics, the share price can dislocate from fundamentals on supply/sentiment alone. See [[price-to-earnings-ratio]] and [[discounted-cash-flow]].

## Capital Return

Arm prioritizes reinvestment (R&D ~$2.6B TTM into CSS, chiplets, and AI) over shareholder returns. It does not run a meaningful buyback or dividend; the constrained public float (SoftBank ~90%) and growth orientation make capital return a secondary consideration. The dominant capital-markets variable is the opposite of return — the **risk of SoftBank secondary offerings** adding supply.

## 2025–2026 Developments

- **FY2026 (ended 31 Mar 2026):** record revenue of $4.92B, with royalty revenue $2.61B (+21%) and licensing $2.31B (+25%). Q2 FY2026 (Sep quarter, reported Nov 5, 2025) topped $1B revenue for a third consecutive quarter.
- **Data-center inflection:** Q4 FY2026 data-center royalty more than doubled year-over-year; cloud/networking royalties trending toward 15–20% of total royalties (from ~10% a year earlier).
- **SoftBank as customer:** following SoftBank's Ampere and Graphcore acquisitions and its AI compute build-out (including the OpenAI/Stargate orbit), SoftBank-related entities became a ~$200M-per-quarter licensing customer — a structural revenue anchor but also a related-party concentration flag.
- **Chip ambitions:** management has flagged R&D (~$2.6B TTM) into CSS and chiplets, saying full-SoC business-model announcements await tape-out and customer orders.
- **Stock action:** ARM fell ~24% in calendar 2025 on smartphone royalty softness and valuation compression; BofA downgraded in early 2026 citing smartphone and royalty headwinds.

## AI Involvement

[[artificial-intelligence|AI]] chip architecture IP - powers AI accelerators globally

## Options Trading Profile

**Liquidity Tier:** Tier 2 - High Liquidity
**Avg Daily Options Volume:** High

AI chip IP giant; growing options activity since 2023 IPO; tight spreads on liquid chain

## Trading Relevance

- Small free float (~10-12%) + AI narrative = elevated realized and implied volatility; earnings moves are routinely double-digit.
- Catalysts: quarterly earnings, Armv9/CSS adoption disclosures, SoftBank stake actions (any secondary offering is a major supply event), hyperscaler custom-CPU announcements, Qualcomm-style licensing disputes.
- Correlated names: [[nvidia]], [[qualcomm]], [[broadcom]], [[taiwan-semiconductor-manufacturing]], SoftBank (9984.T).
- Key risks: smartphone cycle dependence, customers designing around Arm (RISC-V), related-party revenue from SoftBank, premium valuation versus royalty growth.

## Trading & Options Playbook

- **Catalyst calendar**: quarterly earnings (fiscal year ends 31 March, so Q1 ≈ Aug, Q2 ≈ Nov, Q3 ≈ Feb, Q4/FY ≈ May print) — watch royalty vs licensing split, Armv9/CSS mix, and data-center royalty growth. Other movers: SoftBank secondary-offering filings, hyperscaler custom-CPU launches ([[nvidia]] Grace, AWS Graviton, Google Axion, Microsoft Cobalt), RISC-V adoption headlines, and licensing-dispute rulings.
- **Index & ETF membership**: lists on [[nasdaq]]; included in semiconductor and AI-themed baskets such as [[smh-vaneck-semiconductor-etf]] and [[qqq]]. The file records ARM as **not** an [[s-and-p-500]] member (low public float, foreign issuer).
- **Float dynamics**: with SoftBank holding ~90%, the tradable float is tiny — this amplifies both realized volatility and the impact of any index-inclusion or secondary-offering supply event.
- **Volatility behavior**: elevated [[implied-volatility]] driven by the AI narrative and thin float; earnings moves are routinely double-digit. A popular underlying for earnings-volatility and directional AI-theme expression; tight spreads on a liquid chain.
- **Setups to know**: pre-earnings IV ramp, AI-theme beta trades alongside [[nvidia]]/[[broadcom]], and event-driven plays around SoftBank stake actions.

## Risks

- **Premium valuation vs royalty growth** — rich multiple, sensitive to any growth deceleration (drove the ~24% 2025 decline).
- **Smartphone-cycle dependence** — royalty base still heavily mobile.
- **RISC-V substitution** — open, royalty-free ISA erodes the licensing model over time.
- **Customer in-housing / design-around** and **licensing disputes** (e.g., [[qualcomm]] Nuvia/Oryon).
- **SoftBank concentration** — secondary-offering supply overhang, related-party revenue, and tiny float.
- **Geopolitical / export-control** exposure given global customer base and China.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NASDAQ: ARM |
| **AI Category** | Semiconductors |
| **Market Cap Tier** | Large Cap |
| **FY2026 Revenue** | $4.92B (record; FY ends March) |
| **Majority Owner** | SoftBank Group (~90%) |

## Related

- [[artificial-intelligence]]
- [[ai-trading-overview]]
- [[amd]]
- [[broadcom]]
- [[intel]]
- [[model-inference-vs-training]]
- [[nvidia]]
- [[nvidia-ai]]
- [[qualcomm]]
- [[technology]]
- [[taiwan-semiconductor-manufacturing]]
- [[asml-holding]]
- [[astera-labs]]
- [[ambarella]]
- [[synaptics]]
- [[smh-vaneck-semiconductor-etf]]
- [[qqq]]
- [[nasdaq]]
- [[s-and-p-500]]
- [[implied-volatility]]

## Sources

- (Source: [[stockmarketapi-ai-stocks-2026-04-13]])
- [Arm Q2 FYE26 results — Arm Newsroom](https://newsroom.arm.com/news/arm-q2-fye26-results)
- [Arm FY2026 Q4 6-K exhibit — SEC](https://www.sec.gov/Archives/edgar/data/0001973239/000197323926000062/exhibit992fye26q431-marx26.htm)
- [TIKR: Why Arm Can Recover in 2026 After Falling 24%](https://www.tikr.com/blog/heres-why-arm-holdings-can-offer-25-recovery-in-2026-after-falling-24-last-year)
- Verified via Perplexity (sonar) + WebSearch, 2026-06-10

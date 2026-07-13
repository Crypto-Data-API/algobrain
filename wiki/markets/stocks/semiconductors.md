---
title: "Semiconductors (Industry)"
type: market
created: 2026-07-02
updated: 2026-07-02
status: good
tags: [stocks, nasdaq, sector-rotation, fundamental-analysis]
aliases: ["Semiconductors", "semiconductors", "Semis", "Chips", "Semiconductor Industry"]
related: ["[[technology]]", "[[gics-classification]]", "[[smh-vaneck-semiconductor-etf]]", "[[semiconductor-earnings-cycle]]", "[[nvidia]]", "[[taiwan-semiconductor-manufacturing]]", "[[broadcom]]", "[[sector-rotation]]", "[[s-and-p-500]]"]
---

Semiconductors are the integrated circuits ("chips") that process, store, and move information in virtually every electronic device — from smartphones and cars to the GPUs that train AI models. As a stock-market grouping, the semiconductor industry is one of the highest-beta, most cyclical, and most strategically important corners of the equity market, and its largest names ([[nvidia]], [[taiwan-semiconductor-manufacturing|TSMC]], [[broadcom]]) rank among the biggest companies in the world. Global chip sales run into the hundreds of billions of dollars annually, and the industry underpins the entire technology stack.

## GICS Placement

Semiconductors are **not a top-level [[gics-classification|GICS]] sector** — they sit *inside* the [[technology|Information Technology]] sector. Under GICS, Information Technology contains the **Semiconductors & Semiconductor Equipment** industry group, which resolves into two industries:

| Industry Group | Industries | What it covers |
|---|---|---|
| **Semiconductors & Semiconductor Equipment** | Semiconductors | Chip designers and manufacturers (logic, memory, analog, power) |
| | Semiconductor Materials & Equipment | Fab tools, lithography, metrology, materials, and (per most index providers) EDA software |

Because it is an industry rather than a sector, semiconductors have no dedicated "select sector SPDR." Traders access the group through **thematic industry ETFs** (see [[smh-vaneck-semiconductor-etf|SMH]], SOXX) and the **[[technology|Information Technology]]** sector, where the mega-cap chip names carry heavy weight. Chips are also a major reason the [[technology]] sector and the [[s-and-p-500]] have become concentrated in the AI theme.

## The Business-Model Split

The single most important thing to understand about the industry is that "making a chip" is split across several distinct business models, each with different economics, margins, and risk:

### Fabless (design-only)

Fabless companies design chips but own no factories — they outsource manufacturing to foundries. This is a high-margin, capital-light, IP-driven model.

- **Examples:** [[nvidia]] (GPUs / AI accelerators), [[amd|AMD]] (CPUs + GPUs), [[broadcom]] (networking, custom ASICs), [[qualcomm]] (mobile SoCs, modems). [[arm-holdings|Arm]] is a step further removed — it licenses the *instruction-set architecture and core designs* rather than selling chips at all.
- **Economics:** highest gross margins in the industry, but dependent on foundry capacity (chiefly [[taiwan-semiconductor-manufacturing|TSMC]]) and exposed to design-cycle risk.

### Foundry (pure-play manufacturing)

Foundries manufacture chips designed by others. They own the fabs, the process technology, and the enormous capital base.

- **Examples:** [[taiwan-semiconductor-manufacturing|TSMC]] (the dominant pure-play foundry and leading-edge leader), [[samsung-electronics|Samsung Foundry]], [[globalfoundries]] (mature nodes), and Intel Foundry (Intel's contract-manufacturing arm).
- **Economics:** extreme capital intensity — a single leading-edge fab costs tens of billions of dollars. Scale and yield are everything; leading-edge foundry is effectively a duopoly-to-oligopoly.

### IDM (integrated device manufacturer)

IDMs both design *and* manufacture their own chips in-house — the classic model.

- **Examples:** [[intel]] (CPUs), [[micron]] (memory), [[texas-instruments]] and [[analog-devices]] (analog, mostly in-house fabs), Samsung, Infineon, STMicroelectronics, and [[nxp-semiconductors|NXP]] (fab-lite hybrid).
- **Economics:** control the full stack but carry the fab capex burden. Many analog/auto IDMs run "fab-lite" — internal fabs for mature nodes plus outsourced leading-edge.

### Equipment & Materials

The "picks and shovels" of the industry — the toolmakers that sell the machines and materials fabs need.

- **Examples:** [[asml-holding|ASML]] (the *sole* supplier of EUV lithography — a genuine monopoly at the leading edge), [[applied-materials]] (deposition, etch, ion implant), [[lam-research]] (etch and deposition), [[kla|KLA]] (process control, metrology, inspection), and Tokyo Electron.
- **Economics:** oligopolistic, high-margin, and a leading indicator — equipment orders precede fab output. ASML's EUV backlog is a closely-watched capex signal.

### EDA (electronic design automation)

The software used to design chips. Without it, no modern chip gets made.

- **Examples:** [[synopsys]] and [[cadence-design-systems|Cadence]] (a near-duopoly), plus Siemens EDA.
- **Economics:** recurring-revenue software with very high margins and deep customer lock-in; effectively a toll on all chip design.

## Product Categories: Memory vs Logic vs Analog/Power

Chips are not fungible — the industry splits into product families with very different cyclical behaviour:

| Category | What it does | Representative names | Cyclical profile |
|---|---|---|---|
| **Logic** | Compute — CPUs, GPUs, SoCs, ASICs | [[nvidia]], [[amd|AMD]], [[intel]], [[broadcom]], [[qualcomm]] | Driven by AI/data-center, PCs, mobile |
| **Memory** | Storage — DRAM, NAND, HBM | [[micron]], [[samsung-electronics|Samsung]], SK Hynix | The most violently cyclical — commodity-like boom/bust; HBM is the AI bottleneck |
| **Analog / Mixed-signal** | Real-world signal handling — power management, sensors, connectivity | [[texas-instruments]], [[analog-devices]], [[nxp-semiconductors|NXP]] | Longer product cycles, stickier, less commoditized; auto/industrial exposed |
| **Power / Discretes** | Power conversion and switching (Si, SiC, GaN) | [[on-semiconductor|onsemi]], [[navitas-semiconductor|Navitas]], Infineon, Wolfspeed | Secular EV/electrification tailwind; SiC and GaN are the growth frontier |

**Memory is the classic commodity cycle** — near-identical products, priced by supply and demand, with brutal boom/bust swings. **Analog and power** are more diversified across thousands of long-lived parts and are less cyclical. **High-bandwidth memory (HBM)** stacked next to AI GPUs has become a critical, supply-constrained product tying memory makers directly to the AI theme.

## Process Nodes & the Foundry Oligopoly

Chips are made at a **process node** — loosely, the size of the smallest features (measured in nanometers). This creates a two-tier structure:

- **Leading-edge** (e.g. 3nm/5nm-class): the newest, densest, most power-efficient nodes. Used for AI accelerators, flagship CPUs/GPUs, and premium mobile SoCs. Fabrication here is essentially a **duopoly-to-oligopoly**: [[taiwan-semiconductor-manufacturing|TSMC]] is the clear leader, with [[samsung-electronics|Samsung]] and Intel Foundry attempting to compete. Only leading-edge fabs need [[asml-holding|ASML]] EUV tools.
- **Lagging-edge / mature nodes** (e.g. 28nm and older): cheaper, well-understood, and perfectly suited to analog, power, microcontrollers, and automotive chips. Much of the 2021 shortage was concentrated here, and China has been aggressively adding mature-node capacity.

The concentration of leading-edge capacity in a handful of players — and geographically in Taiwan — is the central structural feature (and risk) of the whole industry.

## Cyclicality: The Silicon Cycle

Semiconductors are the **archetypal cyclical industry**, prone to sharp inventory-driven boom/bust swings often called the **"silicon cycle"** (see [[semiconductor-earnings-cycle]]):

- **Upcycle:** demand outstrips supply → lead times stretch → customers **double-order** to secure allocation → chipmakers raise capex and add capacity.
- **Downcycle:** demand cools while the new capacity arrives → customers sit on **excess inventory** → orders collapse, pricing falls, and the industry works off the glut.
- **Book-to-bill ratio:** a classic tell — new orders divided by shipments. Above 1.0 signals expansion; below 1.0 signals contraction. Equipment orders (ASML, Applied Materials) lead the cycle.

Because the industry adds capacity in large, lumpy, expensive increments (fabs take years to build), supply chronically over- or under-shoots demand. The result is high earnings volatility and stocks that move violently on the cycle turn — often *ahead* of the reported numbers.

## Demand Drivers & End Markets

Chip demand is a bet on the underlying end markets:

- **AI / data-center** — the dominant driver of the current cycle: GPUs, custom AI ASICs, networking, and HBM memory. This is the super-cycle powering [[nvidia]] and [[broadcom]].
- **Smartphones** — a mature, large volume market ([[qualcomm]], mobile SoCs); upgrade cycles drive demand.
- **PCs** — cyclical, tied to refresh cycles and enterprise IT spend ([[intel]], [[amd|AMD]]).
- **Automotive** — a fast-growing share: EVs and ADAS multiply the chip content per car (power, analog, MCUs). Key for [[nxp-semiconductors|NXP]], [[on-semiconductor|onsemi]], [[texas-instruments]], Infineon.
- **Industrial** — factory automation, energy, IoT — a broad, [[analog-devices|ADI]]/TI-heavy market.
- **Power & electrification** — SiC/GaN for EVs, solar, and data-center power ([[navitas-semiconductor|Navitas]], onsemi, Wolfspeed).

## The AI / Data-Center Super-Cycle

Since roughly 2023, generative-AI demand for accelerated computing has driven an unusually powerful up-leg. AI accelerators ([[nvidia]] GPUs, [[broadcom]]/hyperscaler custom ASICs), the [[asml-holding|ASML]] tools and [[taiwan-semiconductor-manufacturing|TSMC]] leading-edge capacity that build them, and the HBM memory that feeds them have all seen extraordinary demand. This has partially **decoupled** AI-exposed names from the traditional consumer-electronics cycle: data-center chips boomed even while parts of the smartphone/PC market were soft. The key open question for traders is whether AI capex is a durable secular shift or a capex bubble that will eventually mean-revert like every prior semi cycle.

## Geopolitics, CHIPS Act & Concentration Risk

Semiconductors are now a front-line issue in US-China strategic competition, which adds a policy/geopolitics overlay absent from most industries:

- **Taiwan concentration risk** — the large majority of the world's leading-edge logic is fabricated by [[taiwan-semiconductor-manufacturing|TSMC]] in Taiwan. Any disruption to Taiwan (military, natural disaster) is a systemic tail risk for the entire tech economy — sometimes called the "silicon shield."
- **CHIPS Act (US, 2022)** — tens of billions in subsidies and tax credits to re-shore fab construction in the United States (Intel, TSMC Arizona, Samsung Texas, Micron). The EU and others have parallel programs. This is a multi-year capex tailwind for equipment makers.
- **Export controls to China** — since 2022 the US has restricted the sale of advanced AI chips and leading-edge fab equipment (notably EUV, and later some DUV) to China, with periodic tightening. This caps a large end market for [[nvidia]] and the toolmakers, and has spurred Chinese domestic capacity (largely at mature nodes).
- **Supply-chain reshoring** — the push to diversify manufacturing away from a single geography is reshaping fab investment globally.

Policy headlines — new export rules, subsidy awards, China-demand commentary — routinely move the whole group.

## How Traders Access It

| Vehicle | What it is | Notes |
|---|---|---|
| **[[smh-vaneck-semiconductor-etf|SMH]]** | VanEck Semiconductor ETF | The most-traded semi ETF; cap-weighted and top-heavy in [[nvidia]], [[taiwan-semiconductor-manufacturing|TSMC]], [[broadcom]] |
| **SOXX** | iShares Semiconductor ETF | The other large semi ETF; tracks a semiconductor index, slightly broader/less concentrated than SMH |
| **[[sox-philadelphia-semiconductor-index|SOX]]** | Philadelphia Semiconductor Index | The benchmark *index* (not directly tradable) that traders watch as the group's barometer |
| **Single names** | NVDA, AMD, TSM, AVGO, etc. | Highest-beta expression; earnings are marquee events for the whole tape |
| **Options** | Listed options on the big names | Liquidity concentrates in [[nvidia|NVDA]], [[amd|AMD]], and TSM; SMH/SOXX options for group-level views |

Because the mega-cap chip names dominate index weight, a semiconductor view is increasingly also a view on the [[technology]] sector, the [[nasdaq]]-100, and the [[s-and-p-500]] as a whole.

## Key Characteristics

- **High beta / high volatility** — chips amplify moves in the broad market and in risk appetite.
- **Deeply cyclical** — the silicon cycle drives large earnings and price swings.
- **Capex-intensive** — leading-edge fabs cost tens of billions; the industry is among the most capital-hungry anywhere.
- **Concentrated** — leading-edge manufacturing, EUV tools, and EDA are each dominated by one or a few players (TSMC, ASML, Synopsys/Cadence).
- **Cross-border and policy-exposed** — global supply chains sit squarely inside US-China tech tensions.
- **IP-driven** — value migrates to whoever owns the best designs, process technology, or tools.

## Economic Drivers & Sensitivity

| Driver | Direction | Mechanism |
|---|---|---|
| **AI / data-center capex** | Positive | The current dominant driver — hyperscaler spend on accelerators, networking, HBM |
| **Inventory / book-to-bill cycle** | Positive when rising | The silicon cycle — restocking lifts orders; excess inventory crushes them |
| **Consumer electronics demand** | Positive | Smartphone and PC refresh cycles drive volume for logic and memory |
| **Auto / EV chip content** | Positive | Electrification and ADAS multiply chips per vehicle (power, analog, MCUs) |
| **Fab capex / equipment orders** | Leading indicator | Tool orders (ASML, AMAT) precede output; a read on future supply |
| **Interest rates / risk appetite** | Inverse | High-beta, long-duration growth names de-rate when rates rise or risk-off hits |
| **US-China export controls** | Inverse (to affected sales) | Restrictions cap China demand for advanced chips and tools |
| **Taiwan / geopolitical stability** | Tail risk | Any Taiwan disruption is a systemic shock to leading-edge supply |
| **Memory pricing (DRAM/NAND)** | Positive for memory | Commodity-like pricing swings drive memory-maker earnings |

Semiconductors sit at the aggressive, high-beta end of the cyclical spectrum — more volatile than the broad [[technology]] sector and far more so than defensives.

## Cyclicality & Regime Behavior

Chips are a **classic high-beta cyclical** and a leading tell for risk appetite:

- **Early cycle / risk-on:** strong leadership as the inventory cycle turns up and capex restarts; semis often lead the [[nasdaq]] higher ([[sector-rotation]]).
- **Mid cycle:** broad participation while demand runs and book-to-bill holds above 1.0.
- **Late cycle / cycle rolling over:** sharp de-rating as inventory builds and orders soften — semis frequently top out *before* the broad market.
- **Recession / downcycle:** deep drawdowns, especially in memory and high-multiple logic; the group can fall 40-50%+ peak-to-trough in a bust.
- **Secular overlay:** the AI/data-center theme has, for now, added a growth narrative on top of the cycle — but has not repealed the cycle.

The SOX index and equipment-order trends are the group's leading tells; semis' beta to the [[nasdaq]] and [[s-and-p-500]] is among the highest of any major industry.

## Notable Episodes & History

- **2020-2021 pandemic demand + 2021-2022 chip shortage** — a demand surge (WFH, autos) collided with constrained capacity, producing a global chip shortage that idled auto plants and concentrated pain in mature-node parts. Chipmakers over-ordered into the boom.
- **2022-2023 memory glut & downturn** — the shortage flipped to a glut; DRAM/NAND pricing collapsed and memory makers ([[micron]] et al.) swung to heavy losses as the industry worked off inventory. A broad semi downcycle.
- **2022 US export controls** — the US imposed sweeping restrictions on advanced AI chips and fab equipment to China, later tightened — reshaping the demand map for [[nvidia]] and the toolmakers.
- **2023-2026 AI boom** — generative-AI demand drove an extraordinary up-leg in data-center silicon; [[nvidia]] became one of the largest companies in the world, and [[taiwan-semiconductor-manufacturing|TSMC]], [[broadcom]], [[asml-holding|ASML]], and HBM memory rode the wave. AI-exposed names partly decoupled from the softer consumer cycle.

## Risks

- **Cyclicality** — the dominant risk; the silicon cycle produces deep, fast drawdowns when demand rolls over or inventory builds.
- **AI-capex disappointment** — a large share of the current up-leg rests on sustained hyperscaler spend; any pause or "AI bubble" unwind hits the leaders hardest.
- **Capex intensity** — building fabs costs tens of billions; over-building into a peak is a recurring, margin-destroying mistake.
- **China / Taiwan geopolitics** — export controls cap end markets, and Taiwan concentration is a systemic tail risk to leading-edge supply.
- **Node-transition execution** — leading-edge progress is hard; yield problems or missed node ramps (as Intel has experienced) can hand share to rivals for years.
- **Customer concentration & competition** — a handful of hyperscalers drive AI demand, and custom ASICs are a competitive threat to merchant GPUs.
- **Valuation / rate sensitivity** — high multiples on the AI names mean sharp de-rating risk if rates rise or growth disappoints.

## Semiconductor Constituents (S&P 500)

```dataview
TABLE ticker AS "Ticker", industry AS "Industry"
FROM "wiki/entities/companies"
WHERE sp500 = true AND contains(industry, "Semiconductor")
SORT title ASC
```

## All Semiconductor & Equipment Companies

```dataview
TABLE ticker AS "Ticker", industry AS "Industry", country AS "Country"
FROM "wiki/entities/companies"
WHERE contains(industry, "Semiconductor")
SORT title ASC
```

## Related

- [[technology]] — the parent Information Technology GICS sector
- [[gics-classification]] — sector/industry taxonomy
- [[semiconductor-earnings-cycle]] — the silicon cycle in detail
- [[smh-vaneck-semiconductor-etf]] — the most-traded semiconductor ETF
- [[nvidia]], [[amd|AMD]], [[broadcom]], [[qualcomm]], [[arm-holdings|Arm]] — fabless / design leaders
- [[taiwan-semiconductor-manufacturing|TSMC]], [[intel]], [[globalfoundries]], [[samsung-electronics|Samsung]] — foundry / IDM
- [[micron]] — memory
- [[texas-instruments]], [[analog-devices]], [[nxp-semiconductors]], [[on-semiconductor]], [[navitas-semiconductor]], [[microchip-technology]] — analog / power
- [[asml-holding|ASML]], [[applied-materials]], [[lam-research]], [[kla]] — equipment
- [[synopsys]], [[cadence-design-systems|Cadence]] — EDA
- [[sector-rotation]] — semis as a high-beta, early-cycle leadership group
- [[s-and-p-500]] / [[nasdaq]] — parent indices where chips carry heavy weight

## Sources

- MSCI / S&P GICS classification methodology (Information Technology sector; Semiconductors & Semiconductor Equipment industry group)
- Semiconductor Industry Association (SIA) — industry structure and end-market overviews
- World Semiconductor Trade Statistics (WSTS) — global chip sales and the silicon cycle
- VanEck — Semiconductor ETF (SMH) fund documentation; iShares Semiconductor ETF (SOXX)
- Philadelphia Semiconductor Index (SOX) methodology

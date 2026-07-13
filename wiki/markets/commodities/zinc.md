---
title: "Zinc"
type: market
created: 2026-04-14
updated: 2026-06-22
status: excellent
tags: [commodities, industrial-metals, futures]
aliases: ["Zinc", "Zn"]
related: ["[[copper]]", "[[aluminum]]", "[[nickel]]", "[[iron-ore]]", "[[london-metal-exchange]]", "[[commodities]]", "[[lme-nickel-squeeze-2022]]", "[[lme]]", "[[contango]]", "[[backwardation]]", "[[futures]]", "[[global-financial-crisis]]", "[[silver]]"]
---

# Zinc

Zinc (Zn) is an industrial metal primarily used for galvanizing steel — applying a protective zinc coating to prevent corrosion. It is the fourth most consumed metal globally after iron, [[aluminum]], and [[copper]]. Traded on the [[london-metal-exchange|LME]], zinc demand is closely tied to construction and infrastructure spending cycles, which makes it a sensitive barometer of the global building economy — especially China's.

## How Zinc Is Traded

| Venue | Contract / Unit | Notes |
|-------|-----------------|-------|
| [[london-metal-exchange\|LME]] | USD per tonne, 25-tonne lots | Primary global benchmark; physically deliverable |
| SHFE (Shanghai) | RMB per tonne | Chinese domestic pricing |
| CME | USD per tonne (cash-settled) | Smaller, used by some North American hedgers |

Zinc trades on the LME's distinctive **prompt-date** structure: a continuous run of daily settlement dates out to three months, then weekly and monthly dates further out, rather than the discrete monthly contracts used on most other [[futures]] exchanges. This lets industrial users match a hedge to the exact day a physical cargo settles. Pricing is anchored by the LME's official **open-outcry "ring"** sessions alongside electronic trading.

## Supply and Demand

China is both the largest producer and largest consumer of zinc globally. Major mining operations are distributed across China, Australia, Peru, India, and the United States. Zinc concentrate (mined ore) is refined into zinc metal at smelters, with **treatment charges (TCs)** reflecting the balance between mine supply and smelter demand.

**Key demand sectors:**

| Sector | Share | Use |
|--------|-------|-----|
| Galvanizing | ~60% | Corrosion-proof coating on construction/automotive/infrastructure steel |
| Alloys | ~15% | Brass (copper-zinc), die-casting |
| Chemicals | ~10% | Zinc oxide for rubber, cosmetics, pharmaceuticals |
| Other | ~15% | Batteries (zinc-air, zinc-carbon), rolled zinc |

### The concentrate–metal chain and treatment charges

Zinc has a two-stage market that traders must understand: **mines** produce concentrate, and **smelters** convert it to refined metal. The **treatment charge (TC)** is the fee (paid by miners to smelters, in $/tonne of concentrate) that clears this market. When mine supply is abundant relative to smelter capacity, TCs rise (smelters can demand more); when concentrate is scarce, TCs fall and can even go negative, squeezing smelter margins and eventually curtailing refined output. Falling TCs are therefore an early-warning signal of tightening refined-metal supply.

## Price Drivers

| Driver | Direction when it rises | Why |
|--------|-------------------------|-----|
| China construction / infrastructure | Bullish | ~half of global demand is China-linked |
| LME warehouse stocks | Bearish | Visible inventory caps prices |
| Energy costs (European smelters) | Bullish | Smelting is highly electricity-intensive |
| Treatment charges (TCs) | Bearish for refined supply tightness | Falling TCs flag concentrate shortage |
| Mine disruptions (weather, labor, mine end-of-life) | Bullish | Tightens concentrate |
| US dollar strength | Bearish | Metal is USD-priced |

## Historical Price Context

Zinc prices have experienced significant cyclicality over the past two decades, driven by the interaction of mine supply constraints and Chinese demand. The metal traded in a range of roughly $1,000–$2,000 per tonne through the early 2000s before surging to an all-time high of approximately $4,580 per tonne in late 2006 during the commodity supercycle, when mine supply could not keep pace with explosive Chinese industrial growth. Prices collapsed during the 2008 [[global-financial-crisis]] before recovering. A notable supply-side squeeze occurred in 2015–2017 when several large zinc mines (including Glencore's Century mine and Vedanta's Lisheen mine) reached end-of-life, tightening concentrate supply and pushing prices back above $3,000.

The 2022 European energy crisis had an outsized impact on zinc because smelting is extremely energy-intensive. Several major European zinc smelters (notably Nyrstar's plants in Belgium and the Netherlands) curtailed or halted production when electricity prices spiked, removing significant refined zinc capacity from the market. This episode highlighted zinc's vulnerability to energy cost shocks — a structural feature that distinguishes it from metals like [[copper]], where smelting is less energy-intensive. The energy disruption also demonstrated how the LME metals market can be affected by geopolitical events far removed from the traditional supply-demand narrative, echoing the dynamics seen in the [[lme-nickel-squeeze-2022|LME nickel squeeze of 2022]].

## Worked Example: A Galvanizer Hedging Input Cost (illustrative)

A steel galvanizing plant knows it will consume **500 tonnes** of zinc over the next quarter and wants to lock in its cost. With LME three-month zinc at, say, **$2,800/tonne**, the plant **buys** 20 LME lots (20 × 25 t = 500 t) to fix the price.

- If the spot price later rises to $3,100/t, the plant pays $300/t more for physical metal but its long futures gain ~$300/t — net cost stays near $2,800/t.
- If the price falls to $2,500/t, the plant enjoys cheaper physical metal but loses ~$300/t on the futures — again netting near $2,800/t.

The hedge converts an uncertain input cost into a known one. The residual exposure is **[[basis-risk|basis risk]]** (the gap between the LME price and the plant's actual delivered cost, including regional premiums and the [[contango]]/[[backwardation]] of the curve) — see [[hedge-ratio]] for how to size such a hedge optimally.

## Trading Considerations

Zinc [[futures]] on the LME use an open-outcry ring-trading session for official pricing alongside electronic trading. The LME's unique forward date structure (daily settlement dates out to three months, then weekly and monthly) differs from the standardized monthly contracts on most other futures exchanges. Zinc's relatively small market size compared to [[copper]] or [[aluminum]] means it can be more susceptible to short-term squeezes and warehouse stock manipulation. Traders monitor the [[contango]]/[[backwardation]] structure of the LME zinc curve as a signal of near-term supply tightness — persistent **backwardation** (near-term prices above forward prices) typically indicates physical shortage, while **contango** suggests adequate supply and rewards carrying inventory.

## How Traders Use Zinc

- **Macro / China growth proxy**: Long zinc to express a bullish view on Chinese construction and global infrastructure spending; short to express the opposite.
- **Base-metals relative value**: Zinc-vs-[[copper]] or zinc-vs-[[aluminum]] spreads isolate metal-specific supply stories (e.g., a smelter curtailment) from the broad metals beta.
- **Curve / inventory trades**: Trading the spread between near and far LME dates around stock draws, TC moves, and backwardation episodes.
- **Energy-cost catalyst**: Tactical longs around European power-price spikes that threaten smelter output.

## Common Pitfalls and Risks

- **Squeeze risk**: Zinc's smaller float and concentrated warehouse stocks make it vulnerable to short squeezes and dominant-holder positions on the LME.
- **LME settlement quirks**: The prompt-date system and ring pricing differ from standard exchanges; the nickel episode showed the LME will, in extremis, **cancel trades** — a tail risk for leveraged players.
- **Demand concentration**: With ~60% of demand in galvanizing and a heavy China tilt, a single sector or country shock dominates the price.
- **Energy sensitivity is two-sided**: Power-price spikes can curtail supply (bullish) but also crush industrial demand (bearish) — the net effect is regime-dependent.
- **Leverage and margin**: As with all LME [[futures]], a modest adverse move can trigger margin calls.

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])
- General market knowledge (LME prompt-date structure, treatment-charge economics, galvanizing demand split). No additional specific wiki source ingested yet.

## Related

- [[copper]] — fellow base metal
- [[aluminum]] — fellow LME-traded industrial metal
- [[nickel]] — fellow LME-traded industrial metal; see [[lme-nickel-squeeze-2022]]
- [[iron-ore]] — steelmaking connection (zinc galvanizes steel)
- [[london-metal-exchange]] — primary trading venue
- [[silver]] — partly mined as a byproduct of zinc ore
- [[hedge-ratio]] — sizing a futures hedge
- [[commodities]] — sector overview

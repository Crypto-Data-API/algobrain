---
title: "Terra/LUNA Collapse"
type: news
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [crypto, crash, stablecoin, defi, history, terra, luna, algorithmic-stablecoin, contagion]
aliases: ["terra-luna-collapse", "UST-depeg", "terra-crash", "LUNA crash"]
event_date: 2022-05-09
markets_affected: [crypto]
impact: high
verified: true
sources_count: 3
related: ["[[crypto-winter]]", "[[crypto-markets]]", "[[defi]]", "[[ftx]]", "[[voyager-digital]]", "[[blockfi]]", "[[three-arrows-capital]]", "[[stablecoin-depegs]]", "[[stablecoins]]", "[[2022-05-terra-luna-depeg-arb]]", "[[algorithmic-stablecoin]]"]
---

# Terra/LUNA Collapse

The **Terra/LUNA collapse** was the catastrophic failure of the Terra blockchain ecosystem in May 2022, triggered by the depegging of its algorithmic stablecoin **UST** (TerraUSD). The event wiped out approximately **$40 billion** in market value within days, set off a contagion cascade that defined the 2022 [[crypto-winter|crypto winter]], and led to the arrest and criminal prosecution of founder Do Kwon. It remains the single largest wealth destruction event in crypto history and the definitive case study in algorithmic stablecoin failure.

---

## The Setup: Anchor Protocol and UST Growth

UST's explosive growth was driven almost entirely by **Anchor Protocol**, a lending platform on the Terra blockchain that offered approximately **19.5% APY** on UST deposits. This rate was not market-driven — it was subsidized by the Luna Foundation Guard (LFG) and Terraform Labs using LUNA reserves and venture capital. The yield attracted over **$14 billion** in deposits by April 2022, creating massive concentrated demand for UST.

| Metric | Value |
|---|---|
| UST market cap (peak, May 2022) | ~$18.7 billion |
| LUNA market cap (peak, April 2022) | ~$41 billion |
| Anchor TVL (peak) | ~$14 billion |
| Anchor yield rate | ~19.5% APY |
| LUNA price (ATH) | $119.18 (April 5, 2022) |
| Bitcoin reserves held by LFG | ~80,000 BTC (~$3.5B) |

The fundamental problem: the 19.5% yield was unsustainable. Anchor's borrowing demand was far below its deposit base, meaning the yield was being paid from reserves rather than organic lending revenue. Anchor's "yield reserve" had been declining for months, and multiple analysts publicly flagged the sustainability problem.

## Cast of Characters

| Entity / person | Role | Fate |
|-----------------|------|------|
| **Do Kwon** | Co-founder, Terraform Labs; public face of Terra | Arrested Montenegro Mar 2023; extradited to US; criminal/civil proceedings |
| **Daniel Shin** | Co-founder, Terraform Labs / Chai | Faced charges in South Korea |
| **Terraform Labs (TFL)** | Issuer of UST / LUNA | Found liable in SEC civil case; $4.47B settlement |
| **Luna Foundation Guard (LFG)** | Non-profit holding the ~80,000 BTC reserve | Reserve exhausted defending the peg |
| **Anchor Protocol** | Lending platform paying ~19.5% APY on UST | Demand engine; collapsed with UST |
| **Jump Crypto** | Early backer / market maker | Reportedly profited from earlier 2021 depeg defense; named in litigation |
| **Galaxy Digital** | LUNA investor | Disclosed large gains booked before the collapse |
| **[[three-arrows-capital\|Three Arrows Capital]]** | Leveraged LUNA holder | Defaulted, bankrupt — first domino of contagion |

## The Peg Mechanism

UST maintained its $1 peg through a **mint/burn arbitrage** with LUNA:

- **UST below $1**: Arbitrageurs buy cheap UST and burn it to mint $1 worth of LUNA. They sell the LUNA for profit; UST supply shrinks, pushing price toward $1
- **UST above $1**: Arbitrageurs burn LUNA to mint UST at $1, sell UST above par; UST supply increases, pushing price toward $1

This mechanism worked under normal conditions but contained a fatal flaw: the arbitrage **relied on LUNA maintaining value**. If LUNA's price collapsed, the redemption mechanism would hyperinflate LUNA supply to satisfy UST redemptions, creating a reflexive death spiral. See [[2022-05-terra-luna-depeg-arb]] for a detailed analysis of the arbitrage mechanics.

## Timeline

| Date | Event |
|------|-------|
| **May 7** | ~$2B in UST unstaked from Anchor; large UST sells on Curve destabilize the peg to $0.985 |
| **May 8** | UST briefly recovers; Do Kwon tweets "deploying more capital" |
| **May 9** | **UST falls below $0.90**; panic accelerates. LFG begins deploying BTC reserves to defend the peg. ~$1.5B in BTC sold |
| **May 10** | UST drops to $0.68. LUNA falls from $64 to $30. Arbitrage mechanism activates at scale — LUNA supply begins hyperinflating |
| **May 11** | UST at $0.35. LUNA crashes to $4.40. Supply has ballooned from 350M to 1.5B tokens. Terra blockchain briefly halted |
| **May 12** | **LUNA drops from $80 to under $0.01**. UST at $0.10-$0.20. LUNA supply exceeds 6 billion tokens |
| **May 13** | Terra blockchain halted a second time. LUNA supply reaches **6.5 trillion** tokens (from 350 million — an 18,500x increase). ~$40B in combined value destroyed |
| **May 25** | Do Kwon proposes "Terra 2.0" — a fork without the algorithmic stablecoin. Community votes to approve |
| **May 28** | Terra 2.0 (LUNA) launches; original chain rebranded to "Terra Classic" (LUNC) |

## The Death Spiral in Numbers

| Date | UST Price | LUNA Price | LUNA Supply | Notes |
|------|-----------|------------|-------------|-------|
| May 7 | $1.00 | $80 | ~350 million | Peg intact |
| May 9 | $0.98 | $64 | ~350 million | First depeg; LFG deploys BTC |
| May 10 | $0.68 | $30 | ~400 million | Arb kicks in at scale |
| May 11 | $0.35 | $4.40 | ~1.5 billion | Supply inflation accelerating |
| May 12 | $0.20 | $0.10 | ~6 billion | Full bank run |
| May 13 | $0.10 | $0.00001 | ~6.5 **trillion** | Hyperinflation complete |

## Why the Mechanism Failed

The Terra/LUNA arbitrage was designed for **small deviations from peg under normal conditions**. It was catastrophically underprepared for:

1. **Reflexive feedback loops**: The arbitrage itself created selling pressure on LUNA, which undermined the arb's profitability, which accelerated the depeg — a [[reflexivity|reflexive]] doom loop. The mechanism that was supposed to stabilize became the engine of destruction.

2. **Concentrated deposits**: $14B locked in Anchor meant a single exit event could overwhelm the mechanism. There was no circuit breaker, no gradual wind-down.

3. **No external collateral**: Unlike [[dai|DAI]] (over-collateralised by real assets) or [[usdc|USDC]] (1:1 fiat-backed), UST had **no hard assets backing it**. The peg relied entirely on market confidence in LUNA's value — confidence that evaporated the moment LUNA's price dropped.

4. **Bitcoin reserves were insufficient**: LFG's ~80,000 BTC ($3.5B) could not defend an $18.7B stablecoin. The reserves were exhausted within 48 hours. The BTC sales also pressured Bitcoin's price, contributing to broader market contagion.

5. **Speed of confidence collapse**: The mechanism assumed gradual re-pegging. Instead, the bank run dynamics were exponential — once the death spiral started, there was no equilibrium between total depeg and full restoration.

## The Reflexive Death Spiral, step by step

The collapse is the canonical example of [[reflexivity]] — where the price of an asset feeds back into the fundamentals that supposedly determine its price. The mint/burn arbitrage that stabilised UST in calm markets *inverted* into an accelerant once confidence broke:

1. **Trigger.** Large UST is unstaked from [[anchor-protocol|Anchor]] and sold on [[curve-finance|Curve]]; the peg slips below $1.
2. **Arb activates.** Arbitrageurs burn UST to mint $1 of LUNA and sell the LUNA — *correct* behaviour, but it dumps fresh LUNA into the market.
3. **LUNA falls.** The new LUNA supply plus panic selling drives LUNA's price down.
4. **Redemption cost explodes.** Because each $1 of UST mints $1 *worth* of LUNA, a falling LUNA price means *more LUNA tokens* must be minted per UST redeemed — supply hyperinflates.
5. **Confidence evaporates.** Holders see LUNA's market cap (the implicit "backing") shrinking below UST's market cap; the rational move is to exit *first*, accelerating the run.
6. **Equilibrium fails.** The system has two attractors — full peg or full collapse — and once it leaves the peg basin there is no restoring force. Supply went from ~350M to ~6.5 **trillion** LUNA (an ~18,500x increase) in days.

The fatal property: the stabilisation mechanism's strength was *proportional to LUNA's market cap*, but LUNA's market cap was itself a function of confidence in UST. When confidence fell, both fell together — there was no exogenous anchor. Contrast [[dai]] (over-collateralised by exogenous assets) and [[usdc]] (fiat reserves), which have a floor the algorithm-only design lacked. See [[algorithmic-stablecoin]] and [[stablecoin-depeg-history]].

## Contagion Cascade

The Terra collapse triggered the most devastating contagion chain in crypto history:

| Entity | Exposure | Outcome |
|--------|----------|---------|
| **[[three-arrows-capital|Three Arrows Capital (3AC)]]** | Massive LUNA position (reportedly ~$600M); also leveraged crypto bets | Defaulted on loans from multiple lenders. Filed bankruptcy July 2022. Founders Su Zhu and Kyle Davies fled, later arrested |
| **Celsius** | Lent to 3AC; also had stETH liquidity problems | Froze withdrawals June 12, 2022. Filed bankruptcy July 2022. ~$4.7B in liabilities |
| **[[voyager-digital|Voyager Digital]]** | $660M exposure to 3AC (unsecured loan) | Filed bankruptcy July 5, 2022. Eventually acquired by FTX (then FTX also collapsed) |
| **[[blockfi|BlockFi]]** | Lent to 3AC; balance sheet impaired | Accepted bailout from FTX ($400M credit facility). When [[ftx|FTX collapsed]] in November 2022, BlockFi filed bankruptcy |
| **Babel Finance** | $280M in losses from exposure to 3AC and LUNA | Restructured, laid off staff |
| **Hodlnaut** | Significant LUNA/UST exposure | Froze withdrawals August 2022; Singapore police investigation |

The domino chain — Terra → 3AC → lenders → FTX → BlockFi — destroyed the entire centralized crypto lending sector in 6 months.

## Do Kwon and Legal Aftermath

| Date | Event |
|------|-------|
| May 2022 | Do Kwon proposes Terra 2.0 fork; faces immediate public backlash |
| June 2022 | South Korean prosecutors open investigation |
| September 2022 | Interpol issues Red Notice for Do Kwon; South Korean passport revoked |
| March 2023 | **Do Kwon arrested in Montenegro** traveling on a falsified Costa Rican passport |
| December 2023 | Extradited to the United States |
| January 2024 | SEC files civil fraud charges against Terraform Labs and Do Kwon |
| April 2024 | **Terraform Labs found liable** in SEC civil trial; jury determines UST and LUNA were securities |
| June 2024 | Terraform Labs agrees to $4.47 billion settlement with SEC (the agency's largest crypto penalty) |
| 2024-2025 | Criminal proceedings ongoing in the US; Do Kwon faces wire fraud and securities fraud charges |

## Regulatory Impact

The Terra collapse was a catalyst for global stablecoin regulation:

- **United States**: Accelerated bipartisan stablecoin legislation; SEC intensified enforcement against crypto projects
- **European Union**: Strengthened MiCA (Markets in Crypto-Assets) regulation provisions for stablecoins, including reserve requirements and stress testing
- **South Korea**: Enacted comprehensive crypto regulation (Digital Asset Basic Act) partly in response to Terra
- **Singapore**: MAS tightened rules for stablecoin issuers, requiring full reserve backing
- **Global consensus**: Purely algorithmic stablecoins are effectively dead as a category. Post-Terra, no major new algorithmic stablecoin project has gained meaningful traction

## Terra in the context of stablecoin depegs

Terra is the worst case in a longer history of stablecoin failures and scares — see [[stablecoin-depeg-history]] for the full timeline. The distinguishing feature is the *absence of exogenous collateral*: most other depegs were temporary because there was a redeemable asset behind the token.

| Event | Stablecoin | Backing model | Depth of depeg | Recovered? |
|-------|------------|---------------|----------------|------------|
| **May 2022 Terra** | UST | Algorithmic (LUNA only) | → ~$0.01 | **No — total loss** |
| Mar 2023 USDC scare | [[usdc\|USDC]] | Fiat reserves (SVB exposure) | ~$0.88 | Yes, within days |
| 2021/2022 DAI stress | [[dai\|DAI]] | Over-collateralised crypto | minor | Yes, by design |
| Iron Finance (Jun 2021) | IRON/TITAN | Partial-algorithmic | → ~$0 | No (smaller scale) |

The pattern: **collateralised stablecoins depeg and re-peg; purely algorithmic stablecoins depeg and die.** Post-Terra, no purely algorithmic design has regained meaningful market share. See [[algorithmic-stablecoin]].

## Trading Lessons

- **Unsustainable yield is a red flag** — 19.5% APY on a stablecoin with no organic demand source is a subsidy being paid from reserves. When reserves run out, the scheme collapses. Always ask: where does the yield come from?
- **Reflexive mechanisms can become death spirals** — When the stabilization mechanism itself creates the selling pressure, you get a positive feedback loop that accelerates collapse rather than restoring equilibrium. See [[reflexivity]]
- **No external collateral = no floor** — Algorithmic stablecoins backed only by their own ecosystem token have no anchor to external value. A loss of confidence has no natural stopping point
- **Contagion mapping is a survival skill** — During the Terra aftermath, identifying which entities were exposed to 3AC (and later, which were exposed to Celsius/Voyager) was the single most important trade. Counterparty risk analysis became more valuable than any technical or fundamental analysis
- **Bitcoin reserves do not save a broken mechanism** — LFG's $3.5B in BTC was large in absolute terms but trivial relative to the $18.7B in UST that needed defending. The reserves bought hours, not stability
- **Size does not equal safety** — UST was a top-10 crypto asset with an $18.7B market cap. LUNA was top-10 at its peak. Neither size nor institutional backing (Jump Trading, Galaxy Digital were LUNA investors) prevented the collapse
- **Bank runs are universal** — Whether in [[traditional-finance]] or DeFi, concentrated withdrawals overwhelm any mechanism not backed by sufficient liquid reserves. The dynamic is identical to a 1930s bank run, just faster

## Related Pages

- [[2022-05-terra-luna-depeg-arb]] — Detailed analysis of the arbitrage death spiral mechanics
- [[crypto-winter]] — The broader bear market the Terra collapse triggered
- [[three-arrows-capital]] — Hedge fund that collapsed from LUNA exposure
- [[ftx]] — The next major collapse in the 2022 contagion chain
- [[voyager-digital]] — Broker that failed due to Terra/3AC contagion
- [[blockfi]] — Lender that failed from 3AC and FTX contagion
- [[stablecoin-depegs]] — History of stablecoin de-peg events
- [[stablecoin-depeg-history]] — Timeline of depeg events, Terra in context
- [[stablecoins]] — Stablecoin types and risk analysis
- [[anchor-protocol]] — The 19.5% APY demand engine behind UST
- [[2025-10-crypto-liquidation-cascade]] — Later forced-unwind cascade (different mechanism)
- [[dai]] — Contrast: over-collateralised stablecoin that survived
- [[makerdao]] — Contrast: how proper collateralisation works
- [[algorithmic-stablecoin]] — The category Terra represented
- [[defi]] — DeFi ecosystem where Anchor operated
- [[reflexivity]] — The feedback loop theory behind the death spiral

## Sources

- Terra blockchain on-chain data and LFG reserve disclosures
- SEC v. Terraform Labs (civil case), S.D.N.Y.
- (Source: [[2022-05-terra-luna-depeg-arb]])

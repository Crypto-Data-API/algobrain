---
title: "Cocoa"
type: market
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [commodities, futures]
aliases: ["Cocoa", "CC", "Cocoa Beans"]
related: ["[[coffee]]", "[[sugar]]", "[[cotton]]", "[[commodities]]", "[[intercontinental-exchange]]", "[[commodity-seasonality-patterns]]", "[[seasonal-spread-trading]]", "[[cot-report-analysis]]", "[[contango]]", "[[backwardation]]"]
---

Cocoa is one of the most **geographically concentrated** agricultural commodities, with West Africa producing ~60% of the world's supply. ICE Cocoa futures (CC) trade in New York, with a parallel London ICE contract. The 2024 cocoa price spike was one of the most dramatic commodity moves in recent history -- prices **tripled** from ~$3,000/tonne to over $10,000 in months due to El Nino-related drought, swollen shoot virus disease, aging tree stock, and chronic underinvestment by smallholder farmers in West Africa. This concentration risk makes cocoa uniquely vulnerable: a single weather event in one region can move global prices 50%+. (Source: [[2026-04-14-commodities-research-framework]])

## Key Specifications

| Attribute | Detail |
|-----------|--------|
| **Exchange** | [[intercontinental-exchange|ICE US (New York)]], ICE Europe (London) |
| **Ticker** | CC (New York), C (London) |
| **Contract size** | CC: 10 metric tonnes |
| **Tick size** | $1/tonne = $10 per contract |
| **Trading months** | Mar (H), May (K), Jul (N), Sep (U), Dec (Z) |
| **Settlement** | Physical delivery |
| **Typical price range** | CC: $2,000-$12,000/tonne (2020-2025) |

## How Cocoa Trades: The Two-Exchange Structure

Cocoa is unusual among softs in that it has **two deep, simultaneously traded futures markets** for essentially the same physical commodity:

| Contract | Exchange | Currency / unit | Role |
|----------|----------|-----------------|------|
| **CC (New York)** | [[intercontinental-exchange|ICE US]] | USD per tonne, 10 t | Global benchmark; deepest speculative flow |
| **C ("London cocoa")** | ICE Europe | GBP per tonne, 10 t | European physical/grindings hub; reflects EUR/GBP demand |

**The London-New York arbitrage.** Because the two contracts price the same bean in different currencies (GBP vs USD), the **NY-London spread** embeds both a quality/origin-preference differential and a [[forex|GBP/USD]] currency view. Traders who trade the arb must hedge the FX leg or they are taking an unintended cable position. The spread widens when European demand (grindings) diverges from US speculative positioning, and it is one of the few clean relative-value structures in the cocoa market.

**Curve shape and certificated stock.** Like other deliverable softs, cocoa swings between [[contango]] (carry market -- ample warehouse stock, storage rewarded) and [[backwardation]] (inverse -- prompt scarcity, the dominant 2023-2024 regime as deliverable supply collapsed). ICE-certified warehouse stocks are a closely watched real-time supply gauge; falling certified stock into a delivery month can force violent short-covering, which compounded the 2024 spike.

## Production and Supply

### West African Dominance

Cocoa production is extraordinarily concentrated:

| Country | Share of Global Production | Notes |
|---------|---------------------------|-------|
| **Ivory Coast (Cote d'Ivoire)** | ~40% | Largest single producer |
| **Ghana** | ~15% | Second largest; higher quality reputation |
| **Ecuador** | ~8% | Largest Latin American producer; fine flavor |
| **Cameroon** | ~6% | West African origin |
| **Nigeria** | ~5% | West African origin |
| **Indonesia** | ~5% | Asian production |
| **Brazil** | ~4% | Bahia region; historically significant |

This means **two countries (Ivory Coast + Ghana) produce over 55% of the world's cocoa.** No other major commodity has this level of geographic concentration. A drought, disease outbreak, or political instability in West Africa directly affects over half of global supply.

### Structural Supply Challenges

The cocoa supply chain faces deep structural problems:

- **Smallholder farming:** ~90% of cocoa is produced by farms under 5 hectares. Farmers earn ~$1-2/day in many West African producing regions
- **Aging tree stock:** Average cocoa tree age in West Africa exceeds 25 years (peak productivity is 10-25 years). Replanting rates are insufficient
- **Swollen shoot virus disease (CSSVD):** A devastating viral disease with no cure; infected trees must be destroyed. Ghana has lost hundreds of thousands of hectares
- **Climate change:** Shifting rainfall patterns and rising temperatures threaten traditional growing zones
- **Deforestation limits:** Expansion into new forest area is increasingly restricted by regulation and certification requirements
- **Low farmer investment:** Poverty-level incomes mean farmers cannot afford fertilizers, pesticides, or replanting -- creating a negative feedback loop

(Source: [[2026-04-14-commodities-research-framework]])

## Demand and Processing

### The Bean-to-Bar Supply Chain

1. **Cocoa beans** → harvested, fermented, dried at origin
2. **Grinding** → beans are roasted and ground into cocoa liquor (butter + powder)
3. **Cocoa butter** → the fat component; used in chocolate, cosmetics, pharmaceuticals
4. **Cocoa powder** → the non-fat component; used in beverages, baking, confectionery
5. **Chocolate manufacturing** → final consumer products

### Grindings Data: The Key Demand Indicator

**Grindings** (the volume of cocoa beans processed) is the most important demand metric:

- **European Cocoa Association (ECA):** Quarterly European grindings data
- **Cocoa Association of Asia (CAA):** Quarterly Asian grindings data
- **National Confectioners Association (NCA):** North American grindings
- **ICCO (International Cocoa Organization):** Global supply/demand estimates

Year-over-year grindings growth indicates demand trends. Declining grindings signal demand destruction, typically from high prices.

### Demand Elasticity

- At moderate price levels ($2,000-$4,000/tonne), demand is relatively inelastic -- chocolate manufacturers adjust margins rather than reduce production
- Above $5,000/tonne, **demand destruction** becomes significant: manufacturers reduce cocoa content, increase substitution with vegetable fats, or pass costs to consumers
- **Luxury chocolate** is less price-sensitive than mass-market confectionery
- **Emerging market growth:** Per-capita chocolate consumption in Asia is a fraction of European levels, providing a long-term demand story

## The 2024 Cocoa Crisis

The 2024 price spike deserves special attention as it was one of the most extreme commodity moves in modern history:

- **Starting point (Jan 2023):** ~$2,500/tonne (CC)
- **Peak (Apr 2024):** >$11,000/tonne -- an increase of over 340%
- **Causes (compounding):**
  1. El Nino-induced dry conditions across West Africa reduced the 2023/24 main crop
  2. CSSVD (swollen shoot virus) continued destroying tree stock in Ghana
  3. Heavy rains and black pod disease during the mid-crop further reduced output
  4. Years of underinvestment in replanting and farm maintenance left no buffer
  5. Speculative positioning amplified the move as managed money piled in
- **Consequences:**
  - Chocolate manufacturers faced margin compression or massive price increases
  - Some physical traders suffered large losses on short positions
  - Raised fundamental questions about the long-term sustainability of cocoa supply from West Africa

**The margin-call feedback loop.** A defining feature of the 2024 move was a self-reinforcing liquidity spiral that traders should study as a microstructure case:

1. Producer-country marketing boards and commercial hedgers (e.g. Ivory Coast's CCC, Ghana's COCOBOD) and chocolate makers held large **short futures hedges** against physical they expected to deliver.
2. As prices tripled, those shorts faced enormous **variation-margin calls** -- while the physical crop that backed them was failing to materialize.
3. To meet margin (or to avoid it), some hedgers and weaker speculative shorts were forced to **buy back futures**, adding fuel to the rally.
4. ICE repeatedly **raised margin requirements** as volatility spiked, which forced position reduction and **drained liquidity** -- thinner books then amplified each subsequent move. Open interest fell sharply even as price soared, a hallmark of a liquidity-starved squeeze rather than fresh fundamental buying.

This event demonstrated the risks of **extreme geographic concentration** in commodity supply chains, and of being short a deliverable commodity into a genuine physical shortfall. (Source: [[2026-04-14-commodities-research-framework]])

## Price Drivers

1. **West African weather:** Rainfall during the main crop season (October-March) and mid-crop season (April-September) is the dominant supply variable
2. **Disease (CSSVD, black pod):** Swollen shoot virus has no cure and requires destruction of infected trees; black pod thrives in wet conditions
3. **Ivory Coast/Ghana government policy:** Both countries set farmgate prices and have attempted to coordinate floor prices through the Living Income Differential (LID) program
4. **Grindings data:** Quarterly grindings reports from Europe, Asia, and North America measure processing demand
5. **Stocks-to-grindings ratio:** The ICCO estimates this quarterly; low ratios signal tightness
6. **El Nino/La Nina:** El Nino tends to bring drought to West Africa (bearish for supply, bullish for prices); La Nina brings wetter conditions (mixed -- good for main crop, can cause black pod)
7. **Speculation and fund positioning:** Cocoa has attracted significant speculative interest, especially during the 2024 rally
8. **Chocolate industry demand:** Global chocolate market (~$130B annually) drives underlying cocoa demand

## Seasonal Patterns

Cocoa follows [[commodity-seasonality-patterns|seasonal patterns]] tied to the West African crop cycle:

- **October-December:** Main crop harvest begins in West Africa. New supply enters the market; prices may face seasonal pressure
- **January-March:** Main crop continues. Quality and volume become clearer; weather for the mid-crop starts to matter
- **April-June:** Mid-crop period. Smaller crop (~30-40% of annual output); weather during this period affects total annual production
- **July-September:** Post-mid-crop. Markets assess total crop year production; anticipation of next main crop begins

The marketing year for cocoa runs **October-September**. (Source: [[2026-04-14-commodities-research-framework]])

## Trading Considerations

- **Extreme volatility:** Cocoa can move 5-10% in a single session during supply scares, as the 2024 crisis demonstrated
- **Low liquidity relative to grains:** Open interest and volume in CC are lower than corn, wheat, or soybeans; bid-ask spreads can widen during stress
- **Geographic concentration risk:** Two countries control >55% of supply; political instability, coups (Ivory Coast has experienced multiple), or natural disasters in West Africa are existential risks
- **Physical market complexity:** Cocoa quality varies significantly by origin; the futures contract does not capture this
- **London vs New York:** The London contract is priced in GBP/tonne; the NY contract in USD/tonne. The London-NY arbitrage is actively traded (and carries an implicit [[forex|GBP/USD]] exposure that must be hedged) -- see the two-exchange section above
- **Margin and liquidity risk:** Exchanges raise initial/variation margin during volatility spikes; rising margin in a thin market can force liquidation and worsen moves, as the 2024 squeeze showed
- **Certificated stock watch:** Falling ICE-certified warehouse stock into a delivery month is a leading squeeze signal
- **Positioning:** [[cot-report-analysis|COT data]] flags when managed money is crowded long, raising reversal risk
- **Options:** Available but less liquid than grain or energy options

## Advantages of Trading Cocoa

- Well-defined supply concentration creates clear analytical framework
- Extreme weather sensitivity produces large, tradeable moves
- Structural supply challenges provide a long-term bullish backdrop
- Grindings data provides reliable demand tracking
- Relatively straightforward seasonal patterns tied to crop cycles

## Disadvantages and Risks

- Extreme geographic concentration amplifies tail risk
- Political instability in West Africa (coups, civil wars, land disputes) is difficult to model
- Disease (CSSVD) could structurally reduce production capacity over years
- Thin liquidity can cause disorderly moves and wide spreads
- Physical market complexity (origin, quality, certification) creates basis risk
- Climate change threatens long-term viability of current growing regions
- Speculative positioning can cause violent short-term dislocations from fundamental value

## Related

- [[coffee]] -- tropical soft commodity with weather sensitivity
- [[sugar]] -- soft commodity; also weather-sensitive with geographic concentration
- [[cotton]] -- soft commodity complex
- [[commodity-seasonality-patterns]] -- seasonal trading analysis
- [[seasonal-spread-trading]] -- main-crop/mid-crop and NY-London calendar/arb spreads
- [[cot-report-analysis]] -- managed-money positioning, crowding signals
- [[forex]] -- the GBP/USD leg embedded in the London-NY arbitrage
- [[contango]] / [[backwardation]] -- curve shape and certificated-stock dynamics
- [[intercontinental-exchange]] -- exchange listing cocoa futures
- [[commodities]] -- commodity markets overview

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])

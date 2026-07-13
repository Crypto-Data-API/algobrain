---
title: "Supply and Demand"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, technical-analysis, liquidity, commodities]
aliases: ["Supply and Demand", "Supply/Demand", "Law of Supply and Demand"]
related: ["[[supply-demand-zones]]", "[[supply-demand-balance]]", "[[support-and-resistance]]", "[[support]]", "[[resistance]]", "[[order-book]]", "[[liquidity]]", "[[market-microstructure]]", "[[commodities-overview]]", "[[contango]]", "[[backwardation]]", "[[convenience-yield]]"]
domain: [fundamental-analysis, market-microstructure]
prerequisites: []
difficulty: beginner
---

Supply and demand is the foundational economic principle that price is set where the quantity buyers wish to purchase equals the quantity sellers wish to provide. In markets, every observed price is a momentary equilibrium between aggregate buying pressure (demand) and aggregate selling pressure (supply); price moves whenever that balance shifts. It is the conceptual root of essentially all market analysis, from commodity fundamentals to the [[order-book]] microstructure and the technical idea of [[support-and-resistance]].

## The Mechanism

A **demand curve** slopes downward — buyers want more at lower prices. A **supply curve** slopes upward — producers supply more at higher prices. Their intersection is the **market-clearing price** and quantity. Two distinct things move markets:

- **A shift in the curves** (a change in fundamentals — new mine output, a demand shock, a regulatory change) moves the equilibrium price to a new level.
- **A movement along the curves** (a change in price without a change in fundamentals) re-balances quantity supplied and demanded.

**Elasticity** governs how violently price responds. When supply or demand is inelastic — energy, grains, anything with no near-term substitute — a small imbalance produces a large price move. The April 2020 negative WTI crude print and recurrent natural-gas spikes are textbook inelastic-supply events (see [[crude-oil]], [[commodities-overview]]).

### Shift vs. movement — and what moves each curve

| | Demand curve shifts when… | Supply curve shifts when… |
|---|---|---|
| Cause | Incomes, tastes, substitutes, expectations change | Input costs, technology, capacity, regulation change |
| Equities | Index inclusion, flows, sentiment, buybacks | New issuance / dilution, lock-up expiry |
| Commodities | Weather, growth cycle, stimulus | Mine/well output, OPEC quotas, harvest |
| Crypto | Adoption, ETF flows, narrative | Issuance schedule, [[2024-04-19-bitcoin-halving\|halving]], miner selling |
| Result | New equilibrium price | New equilibrium price |

A **shift** moves the whole curve and resets the clearing price; a **movement along** a fixed curve is just price rationing the existing quantity. The distinction matters because a price change driven by a genuine curve shift (new fundamentals) is more durable than one driven by transient flow that mean-reverts.

### Worked example: a demand shift

A copper market clears at $4.00/lb with 100 units traded. A government announces a large grid-electrification programme; expected demand jumps. With near-term mine output fixed (inelastic supply), the new demand curve intersects the old supply curve at, say, $4.60 and 104 units. Almost all of the adjustment shows up as **price** (+15%), very little as quantity (+4%) — the signature of inelastic supply. A trader who modelled the inventory draw before the price fully adjusted captured the imbalance; one who chased after $4.60 paid for information already in the price.

## Supply and Demand in Financial Markets

In a continuous market the principle operates at the level of the [[order-book]]: resting bids represent demand, resting offers represent supply, and trades occur where they cross. Large resting orders create the visible price levels that technical traders call [[support-and-resistance|support and resistance]] — [[support]] is a price floor where demand has historically absorbed selling, [[resistance]] a ceiling where supply has capped buying. The [[supply-demand-zones]] strategy and broader [[supply-demand-balance]] microstructure analysis formalise this — a "demand zone" is a price area where buying previously overwhelmed selling and is expected to do so again; a "supply zone" is the reverse.

Key market-specific applications:

- **Commodities** — physical inventory, production, and consumption drive curves; [[contango]] and [[backwardation]] in the futures curve encode the market's read on the supply/demand balance and [[convenience-yield]]. Inventory reports (EIA, USDA) are pure supply/demand catalysts.
- **Equities** — float, dilution, buybacks, and index inclusion change effective supply; flows and sentiment change demand. Tight float plus a demand surge produces squeezes.
- **Crypto** — fixed or programmatic issuance schedules (e.g. the [[2024-04-19-bitcoin-halving|Bitcoin halving]]) are explicit supply shocks; exchange balances and [[on-chain-analysis|on-chain]] flows proxy demand.
- **Liquidity** — thin [[liquidity]] means the same imbalance moves price more; [[slippage]] is the cost of demanding immediacy against limited supply.

## Trading Relevance

- **Imbalance is the edge.** Most profitable strategies are bets that current price misstates the true supply/demand balance — fundamental commodity traders model inventories; technical traders read [[order-flow-analysis|order flow]] and zones; quants model flow imbalance ([[order-flow-imbalance]], [[vpin]]).
- **Catalysts move curves.** Earnings, inventory data, halvings, OPEC decisions and macro prints are all supply/demand-curve shifts — trading them is event-driven by nature.
- **Beware reflexivity.** Price itself feeds back into supply and demand (high prices invite production and ration consumption), so equilibria are dynamic, not static — a core idea behind [[reflexivity]] and [[market-cycles]].
- **Distinguish flow from fundamentals.** A price move on heavy [[volume]] driven by a genuine fundamental shift is more durable than one driven by transient flow imbalance that mean-reverts.

### How traders operationalise it

| Trader type | What they measure | The imbalance bet |
|-------------|-------------------|-------------------|
| Commodity fundamental | Inventories, production, consumption (EIA/USDA) | Price misreads the physical balance |
| Technical / price-action | [[supply-demand-zones\|S&D zones]], [[support]]/[[resistance]] | Demand/supply re-asserts at a known level |
| Microstructure / quant | [[order-book]] depth, [[order-flow-imbalance]], [[vpin]] | Short-horizon flow imbalance forecasts the next move |
| Macro / event | Catalysts that shift the curves (OPEC, prints, halvings) | Position ahead of the curve shift |

A common workflow: identify a demand zone where price previously turned up sharply on volume, wait for price to return to it, and look for [[order-flow-analysis|order-flow]] confirmation (absorption of selling) before buying — risk defined just below the zone where the demand thesis would be proven wrong.

## Pitfalls and Risks

- **Zones are not magic walls.** A "demand zone" or [[support]] level holds until it doesn't; in a strong [[trend]] the prevailing imbalance simply runs through prior levels. Treat them as areas of likely reaction, not guarantees.
- **Spoofing and hidden liquidity.** Visible [[order-book]] depth can be faked (spoofed) or hidden (iceberg orders), so resting size is an unreliable read of true supply/demand.
- **Reflexivity.** High prices invite production and ration demand, so an imbalance is self-correcting over time — static supply/demand reasoning fails when [[reflexivity]] feedback is strong.
- **Flow ≠ fundamentals.** A flow-driven spike (forced liquidation, index rebalance) can look like a fundamental shift but mean-reverts; misreading which one you're seeing leads to fading durable moves or chasing transient ones.
- **Inelastic markets gap.** In inelastic commodities a small balance change can move price far and fast, blowing through stops — size for the tail, not the average move.
- **Stale levels.** Old zones lose relevance as the orders that created them are filled or cancelled; the freshest, highest-volume levels carry the most weight.

## Related

- [[supply-demand-zones]] — the technical-trading expression of demand/supply imbalance
- [[supply-demand-balance]] — microstructure treatment of order-book imbalance
- [[support-and-resistance]] — price levels created by clustered supply and demand
- [[support]] / [[resistance]] — the demand-floor and supply-ceiling levels
- [[order-book]], [[order-flow-imbalance]], [[liquidity]] — the microstructure layer
- [[contango]], [[backwardation]], [[convenience-yield]] — futures-curve signals of commodity balance
- [[reflexivity]], [[market-cycles]] — dynamic feedback in supply and demand

## Sources

- Marshall, A. *Principles of Economics* (1890) — origin of the supply/demand curve framework.
- Murphy, J. *Technical Analysis of the Financial Markets* (1999) — supply/demand as the basis of support and resistance.
- Pindyck, R. and Rubinfeld, D. *Microeconomics* — elasticity and market equilibrium.

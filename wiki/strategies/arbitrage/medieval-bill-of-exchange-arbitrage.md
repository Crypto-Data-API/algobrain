---
title: "Medieval Bill of Exchange Arbitrage"
type: strategy
created: 2026-04-25
updated: 2026-06-10
status: good
tags: [arbitrage, history, forex]
aliases: ["Bill of Exchange Arbitrage", "Cambium per Litteras", "Medieval Triangular Arbitrage"]
related: ["[[champagne-fairs]]", "[[medieval-italian-banking]]", "[[triangular-arbitrage]]", "[[gold-point-arbitrage]]", "[[bill-broking-arbitrage]]"]
strategy_type: hybrid
timeframe: position
markets: [forex]
complexity: advanced
backtest_status: retired
edge_source: [structural, informational, risk-bearing]
edge_mechanism: "Counterparties at distant fairs cannot quote consistent cross-rates without slow correspondence; merchant-banker syndicates with branches in multiple cities net positions on books and pocket the triangle."
data_required: [fair-rate-tables, mercantile-correspondence]
min_capital_usd: 1000000    # modern-dollar equivalent of multi-branch banking infrastructure
capacity_usd: 50000000      # modern-dollar equivalent of the largest houses' bill books
crowding_risk: low
expected_sharpe: 1.0        # rough modern-equivalent estimate; see Performance Characteristics
expected_max_drawdown: 0.50 # sovereign-default tail was total loss (Bardi-Peruzzi)
breakeven_cost_bps: 200
decay_evidence: "Fair-cycle inconsistencies compressed as Lyon and Antwerp emerged as continuous markets and as direct sea routes (Genoese galleys to Bruges, 1278) bypassed land fairs."
---

# Medieval Bill of Exchange Arbitrage

Triangular FX arbitrage executed via bills of exchange (*lettera di cambio*) at Europe's medieval and Renaissance trade fairs — the foundational venue for cross-border arbitrage from the 12th century until the rise of permanent bourses. Florentine, Genoese, and Lucchese merchant-bankers exploited rate inconsistencies across the [[champagne-fairs]], [[lyon-fairs]], Bruges, and Castilian fairs by writing bills payable at one fair and remitting at another.

## Edge Source

Edge sources: **structural**, **informational**, **risk-bearing**.

- **Structural:** Each fair set its own *conto* exchange rates by collective negotiation. Without continuous quotation between fairs, rates drifted out of cross-parity until the next settlement window.
- **Informational:** Branches of the same banking house (Bardi, Peruzzi, Medici) had private correspondence networks that out-paced merchants without offices abroad.
- **Risk-bearing:** Banker capital absorbed counterparty failure (the Bardi-Peruzzi 1343-1346 collapse after Edward III's English-throne default).

## Why This Edge Exists

Communication between Bruges and Florence took 20-30 days by horse-courier. Bills written in January at the Lagny fair might not settle until the Saint-Ayoul fair at Provins in the autumn — the Champagne cycle ran six fairs a year (Lagny, Bar-sur-Aube, Provins May, Troyes "hot", Provins September, Troyes "cold"). Merchants without multi-branch operations had no way to verify cross-rates; banking houses with offices in 6-10 cities did.

Canon-law usury prohibitions ruled out explicit interest charges, so banks dressed the time-value-of-money up as foreign-exchange spread. *Cambium et recambium* (exchange-and-re-exchange / "dry exchange") was a round-trip bill — Florence to Bruges and back — that earned a guaranteed return purely through the FX legs. Effectively a synthetic loan at 8-15% per annum, but legally a commercial transaction.

## Null Hypothesis

Under random no-edge conditions, fair rates would mean-revert to mint parity within a single settlement cycle, and round-trip "dry exchange" P&L would equal expected FX volatility times the time horizon. Empirically (Roover 1948, Spufford 1986) round trips earned a persistent positive return for 200+ years.

## Rules

1. Maintain branches in at least 3 fair cities (Florence, Bruges, Lyon — or Florence, Champagne, London).
2. At each fair settlement (4-6 weeks): collect bills in foreign currency owed to the house.
3. Compute implicit cross-rates among the 3-4 currencies in play.
4. Where the cross-rate triangle is inconsistent, write new bills along the profitable leg.
5. Settle through the banker's network of correspondents — internal book transfers — not physical specie.
6. Only ship physical specie when the inconsistency exceeds the [[gold-point-arbitrage|gold point]] including bandit and shipwreck losses.

## Implementation Pseudocode

```
for fair_cycle in [Lagny, Bar, Provins-May, Troyes-Hot, Provins-Sept, Troyes-Cold]:
    rates = collect_correspondence_quotes(branches=[Florence, Bruges, Lyon, London])
    for (a, b, c) in permutations(currencies, 3):
        triangle = rates[a→b] * rates[b→c] * rates[c→a]
        if triangle > 1 + cost_threshold:
            write_bill(from=a, to=b, amount=working_capital)
            forward_bill_to_branch(b)
            write_bill(from=b, to=c, ...)
            settle_at_next_fair(c → a)
            net_to_book(profit=triangle - 1 - costs)
```

## Indicators / Data Used

- *Conto* tables published at each fair.
- Branch correspondence (surviving examples: Datini Archive in Prato, ~150,000 letters 1382-1410).
- Mint records (Royal Mint, Florentine Zecca, Castilian mints).
- Sterling-Flemish *escu* parity at Bruges.

## Example Trade

**c. 1470, Florence-Lyon-Bruges triangle (illustrative reconstruction — the Lyon fairs were chartered in 1463, and the Medici Bruges branch operated 1439-1480).**

The Medici Bank's Bruges branch holds 10,000 *écus de Flandre* receivable. Lyon quotes 1 *écu* = 4 Florentine *fiorini* di sigillo. Bruges quotes 1 *écu* = 24 *gros tournois* and Florence-Lyon: 1 fiorino = 5.8 gros. Triangle: 1 écu → 4 fiorini → 23.2 gros, but direct Bruges quote is 24 gros — 3.4% inconsistency.

Trade: write bill in Bruges payable to Lyon in fiorini, remit Lyon to Florence in écus, collect at next fair. Round-trip yields ~3.4% gross over 90-120 days, net ~2% after assay and courier costs — annualized ~6-8%.

## Performance Characteristics

de Roover (1963) reconstructs Medici Bruges-branch returns at 8-15% per annum on bill-of-exchange operations 1430-1480, dwarfing trade-financing margins. Returns persisted because the network of 8-10 branches was effectively non-replicable infrastructure.

Frontmatter risk figures (Sharpe ~1.0, max drawdown 0.50) are rough modern-equivalent estimates: returns were steady for the dominant houses across decades, but the sovereign-default tail was total loss of capital — the Bardi and Peruzzi were destroyed outright in 1343-1346.

## Capacity Limits

Bound by working capital + fair settlement liquidity. Medici Bank balance sheet ~150,000 fiorini in 1450 (Roover). Larger flows would have crashed fair *conto* rates.

## What Kills This Strategy

- Direct sea routes bypass land fairs (Genoese galleys to Bruges 1278+).
- Permanent exchanges replace fair cycles (Antwerp Bourse 1531; Amsterdam 1602).
- Telegraph/cable from 1850s collapses information advantage entirely (see [[telegraph-impact-on-arbitrage]]).
- Sovereign defaults (Edward III 1343 → Bardi/Peruzzi collapse).

## Kill Criteria

- Replacement of *cambium* by spot FX (post-1700).
- Compression of cross-rate inconsistency to <0.5%.

## Advantages

- Long-duration edge (200+ years of profitability for top houses).
- Compounding via internal book settlement — minimal physical specie risk.
- Disguised interest skirts canon-law usury.

## Disadvantages

- Requires multi-branch infrastructure.
- Sovereign-default tail risk wipes out the largest houses.
- Information asymmetry decays with each generation of communication tech.

## Sources

- Raymond de Roover, *The Rise and Decline of the Medici Bank, 1397-1494* (1963).
- Raymond de Roover, *Money, Banking and Credit in Mediaeval Bruges* (1948).
- Edwin S. Hunt, *The Medieval Super-Companies* (1994).
- Peter Spufford, *Money and Its Use in Medieval Europe* (1986).
- Federigo Melis, *Documenti per la storia economica dei secoli XIII-XVI* (1972).
- Datini Archive, Prato.

## Related

[[champagne-fairs]] · [[medieval-italian-banking]] · [[lyon-fairs]] · [[gold-point-arbitrage]] · [[triangular-arbitrage]] · [[bill-broking-arbitrage]] · [[covered-interest-arbitrage]]

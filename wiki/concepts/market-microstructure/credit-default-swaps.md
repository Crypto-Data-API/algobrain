---
title: Credit Default Swaps
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - derivatives
  - history
aliases:
  - CDS
  - credit-default-swap
  - Credit Default Swap
domain: [market-microstructure]
prerequisites: ["[[derivatives]]", "[[bond-market]]"]
difficulty: intermediate
related: ["[[derivatives]]", "[[collateralized-debt-obligations]]", "[[2008-global-financial-crisis]]", "[[moral-hazard]]", "[[aig]]", "[[credit-cycle]]", "[[counterparty-risk]]"]
---

# Credit Default Swaps

A **Credit Default Swap (CDS)** is a [[derivatives]] contract that functions as insurance against the default of a debt issuer. The buyer pays periodic premiums; the seller pays out if a credit event occurs.

CDS contracts on [[mortgage-backed-securities]] were central to the [[2008-global-financial-crisis]], with AIG's massive CDS exposure nearly collapsing the global financial system.

## How CDS Works

A CDS functions like insurance on debt. The **buyer** pays periodic premiums (the "spread," quoted in basis points per year) to the **seller**. In return, the seller agrees to compensate the buyer if a defined "credit event" occurs -- typically a default, bankruptcy, or restructuring of the referenced entity's debt. If no credit event occurs, the seller simply collects the premiums.

Unlike traditional insurance, CDS buyers do not need to own the underlying debt. This means speculators can buy CDS purely as a bet that a company or country will default -- so-called "naked" CDS positions. This was how traders like Michael Burry profited from the subprime crisis.

## The AIG Collapse

AIG Financial Products sold an enormous volume of CDS contracts guaranteeing [[collateralized-debt-obligations]] backed by subprime mortgages, collecting billions in premiums while assuming the underlying debt would never default at scale. When housing prices collapsed, AIG faced simultaneous payouts it could not cover. By 2007, the total notional value of outstanding CDS contracts globally exceeded $60 trillion -- dwarfing the actual underlying bond market. AIG required a $185 billion government bailout to prevent a systemic cascade. See [[aig]] for more detail.

## Market Significance

CDS spreads are now widely watched as real-time indicators of credit risk. A rising CDS spread on a company or sovereign entity signals that the market perceives increasing default risk. CDS indices (CDX for North America, iTraxx for Europe) are actively traded and serve as barometers of overall credit market health.

## Trading Relevance

CDS serve three roles for market participants. **Hedgers** (bond holders, banks) buy protection to offload default risk without selling the underlying bond. **Speculators** express directional credit views — buying "naked" CDS to bet against a company or sovereign, as Michael Burry and others did in the run-up to 2008. **Relative-value traders** exploit the **CDS-bond basis** (the gap between a CDS spread and the credit spread implied by the cash bond), which is a classic [[arbitrage]]-style trade that blows out during liquidity crises. Because CDS spreads update in real time and are forward-looking, they are among the cleanest market-implied probabilities of default and a leading input to [[credit-cycle]] analysis.

## Related

- [[derivatives]]
- [[collateralized-debt-obligations]]
- [[2008-global-financial-crisis]]
- [[credit-cycle]]
- [[counterparty-risk]]
- [[moral-hazard]]
- [[aig]]

## Sources

- International Swaps and Derivatives Association (ISDA), CDS definitions and market data.
- Bank for International Settlements (BIS), OTC derivatives statistics (CDS notional outstanding).
- Lewis, M. (2010). *The Big Short.* (Naked CDS, the subprime trade, AIG.)
- Stulz, R. (2010). "Credit Default Swaps and the Credit Crisis." *Journal of Economic Perspectives.*

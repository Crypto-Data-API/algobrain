---
title: "Sumitomo Copper Scandal — Yasuo Hamanaka (1995-1996)"
type: news
created: 2026-04-26
updated: 2026-06-12
status: good
tags: [history, commodities, copper, rogue-trader, sumitomo, lme]
aliases: ["Mr. 5%", "Mr. Copper", "Hamanaka Copper Scandal", "Sumitomo $2.6B Loss"]
event_date: 1996-06-13
markets_affected: [commodities]
impact: high
verified: true
sources_count: 4
related: ["[[corner-the-market]]", "[[lme-nickel-squeeze-2022]]", "[[grain-futures-basis-arbitrage]]", "[[liverpool-cotton-exchange]]"]
---

# Sumitomo Copper Scandal — Yasuo Hamanaka (1995-1996)

**Yasuo Hamanaka** — chief copper trader at Japan's **Sumitomo Corporation** from the early 1980s through 1996 — ran a decade-long unauthorized trading scheme that produced a final reported loss of **$2.6 billion** when revealed in June 1996. At his peak, Hamanaka was reportedly responsible for **5% of global annual copper consumption** in his trading book — earning him the nickname **"Mr. 5%"** or **"Mr. Copper"**. The scandal triggered:

- The **largest single trading loss** at any Japanese firm at that point.
- Multi-year LME (London Metal Exchange) reform.
- The largest individual rogue-trading loss before [[2008-01-socgen-kerviel-rogue-trade|Kerviel]] (€4.9B, 2008).

For arbitrageurs, the case is the canonical study of how a *single trader cornering an industrial metal market* can sustain artificial prices for years before collapse.

## Background

**Yasuo Hamanaka** (born 1948) joined Sumitomo's copper trading desk in 1968 and rose to chief copper trader by mid-1980s. Sumitomo Corporation was Japan's largest copper merchant, handling physical copper shipments, refining, and trading on the LME.

Through the 1980s-1990s, Hamanaka:
1. Built massive **long copper futures positions** on the LME (particularly the famous "ring" floor trading).
2. Coordinated with **physical copper warehouses** (especially LME-warehoused stocks) to limit availability.
3. Falsified trading records to hide losses from Sumitomo's risk management.
4. Used "off-balance-sheet" derivatives with major banks (Merrill Lynch, Credit Lyonnais) to extend leverage.

## Mechanics of the Cornering

LME copper trading (1985-1996) was vulnerable to cornering because:
- Physical stocks held in LME-registered warehouses were limited (~200,000 tonnes typically vs millions of tonnes annual demand).
- "Backwardation" — when nearby copper trades premium to forward — could be engineered by holding spot supply.
- Most copper trade was **bilateral OTC**; LME prices set the global reference rate.

Hamanaka:
1. **Bought LME copper futures aggressively** during off-peak periods.
2. **Took physical delivery** to remove copper from circulating supply.
3. **Charged premium prices** to physical buyers needing prompt delivery.
4. **Squeezed shorts** at contract expiry (forced them to pay backwardation).

This worked for ~10 years. The scheme generated paper profits Hamanaka used to grow Sumitomo's copper trading reputation; Sumitomo management didn't investigate because the desk was "profitable."

## The Discovery

By early 1996:
- Global copper supply was rising (new mines in Chile, Peru).
- Hamanaka's positions were too large to maintain backwardation.
- Real losses had accumulated to billions.

**June 5, 1996:** LME's review of trading patterns flagged Hamanaka's positions.

**June 13, 1996:** Sumitomo internal investigation revealed unauthorized positions; Hamanaka confessed.

**June 14, 1996:** Sumitomo announced **$1.8B initial loss estimate**; final number reached **$2.6B**.

**Copper price reaction:** LME copper crashed from $2,800/tonne to $1,800/tonne (-36%) over the following weeks as Hamanaka's massive long position unwound.

## Triangular Arb Aspects

The scandal created arbitrage opportunities for participants who anticipated or rapidly responded:

**Pre-discovery (1990-1996):** Hamanaka's chronic backwardation forced physical buyers to pay premium. Specialist arbs **shorted LME futures + bought physical from non-LME warehouses** — capturing the backwardation premium when their shorts settled below his squeeze price. Estimated $200-500M extracted by 5-10 specialist arb desks.

**Discovery week (June 13-21, 1996):** Anticipating Hamanaka's forced unwind, sophisticated traders short copper from $2,800 captured 30%+ within 2 weeks.

**Post-discovery cleanup (1996-1997):** Sumitomo took 18 months to fully unwind Hamanaka's positions; specialist arbs traded the unwind path.

## Aftermath

- **Sumitomo:** Reported Y200B (~$2B) net loss for 1996; multi-year recovery.
- **Hamanaka:** Convicted of fraud / forgery; sentenced to 8 years in prison (2002 sentence; served 7).
- **LME reform:** Stricter position-disclosure rules; large-trader reporting requirements; warehouse-stock transparency.
- **Sumitomo executives:** Resignations (Tomiichi Akiyama, others).
- **Bank counterparties:** Merrill Lynch and Credit Lyonnais ($60M settlement to LME).
- **Cross-firm scrutiny:** Other Japanese trading houses tightened internal controls.

## Lessons for Traders

1. **Long-running rogue trading is rarely "rogue"** — Hamanaka's scheme operated for a decade with implicit Sumitomo benefit (reputation, position size). Internal controls were structurally absent.
2. **Physical commodity cornering is harder to sustain than financial.** Eventually new supply or demand destruction breaks the squeeze.
3. **LME mechanism vulnerable to single-trader cornering.** The 2022 nickel squeeze ([[lme-nickel-squeeze-2022|Tsingshan / Bill Hwang of nickel]]) repeated the pattern.
4. **Post-cornering crashes are violent.** Copper -36% in 2 weeks; specialist arbs anticipating the discovery profited.
5. **Off-balance-sheet derivatives + bank counterparties are systemic risk vectors.** Same pattern as Madoff (offshore "feeder funds"), Archegos (TRS at multiple PBs), LTCM (multi-counterparty leverage).

## Comparable Events

| Event | Trader | Loss | Year |
|-------|--------|------|------|
| Nick Leeson / Barings | Nick Leeson | $1.4B | 1995 |
| **Sumitomo Copper / Hamanaka** | **Yasuo Hamanaka** | **$2.6B** | **1996** |
| LTCM | n/a (collective) | $4.6B | 1998 |
| Allied Irish Banks / Rusnak | John Rusnak | $691M | 2002 |
| Société Générale / Kerviel | Jérôme Kerviel | €4.9B | 2008 |
| UBS / Adoboli | Kweku Adoboli | $2.3B | 2011 |
| Archegos / Hwang | Bill Hwang | $10-12B | 2021 |
| LME Nickel / Tsingshan | Xiang Guangda | $8B+ | 2022 |

The Hamanaka case sits in the "individual rogue + institutional complicity" tradition that runs through Leeson, Kerviel, Adoboli, and Hwang.

## Sources

- *Wall Street Journal*, *Financial Times* coverage June 1996 - January 1997.
- LME Special Investigation report 1996.
- *Sumitomo: Annual Report 1996, 1997*.
- *Mr. Copper: Yasuo Hamanaka and the Sumitomo Affair* — various retrospective books.
- David Greising, Laurie Morse, *Brokers, Bagmen, and Moles* (1991, prescient).

## Related

[[corner-the-market]] · [[lme-nickel-squeeze-2022]] · [[grain-futures-basis-arbitrage]] · [[liverpool-cotton-exchange]] · [[shipping-certificate-arbitrage]] · [[1991-salomon-treasury-auction-scandal]] · [[2008-01-socgen-kerviel-rogue-trade]]

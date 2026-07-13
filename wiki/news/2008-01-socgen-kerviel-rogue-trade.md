---
title: "Société Générale Kerviel Rogue Trade (January 2008)"
type: news
created: 2026-04-26
updated: 2026-06-12
status: good
tags: [news, history, stocks, futures, derivatives, risk-management]
aliases: ["Kerviel Scandal", "SocGen €4.9B Loss", "January 2008 Market Crash"]
event_date: 2008-01-21
markets_affected: [equities, futures]
impact: high
verified: true
sources_count: 5
related: ["[[counterparty-stress-arbitrage]]", "[[index-arbitrage]]", "[[archegos-blowup-2021]]", "[[ltcm-collapse-1998]]", "[[2008-global-financial-crisis]]", "[[risk-management]]", "[[fastest-profitable-trades]]"]
---

# Société Générale Kerviel Rogue Trade (January 2008)

On **January 24, 2008**, Société Générale (SocGen) revealed a **€4.9 billion ($7.2B) trading loss** — the largest single rogue-trading loss in history at that point — caused by **Jérôme Kerviel**, a 31-year-old junior trader on SocGen's Paris arbitrage desk. Kerviel had built unauthorized **€50 billion notional positions** in European equity index futures (Eurostoxx 50, DAX, FTSE) — a position larger than SocGen's entire market capitalization.

SocGen's panicked unwinding of Kerviel's positions over **January 21-23, 2008** coincided with — and is widely (though not conclusively) credited with amplifying — the global equity sell-off that preceded the **Federal Reserve's emergency 75 bp rate cut on January 22** (the first inter-meeting cut since 1984). The causal link to the Fed's decision is debated: the Fed cited deteriorating economic conditions, but the timing has fueled persistent speculation that Bernanke's committee acted partly in response to a sell-off that was, in part, one bank dumping €50B of futures into a thin market. Either way, the episode is the canonical case study in how a **forced-unwind** by a single distressed counterparty can masquerade as macro news — and create a window for traders who can tell the difference.

## Background

**Jérôme Kerviel** (born 1977) joined SocGen in 2000 in the back-office (compliance/middle-office). Promoted to junior trader on the **Delta One** desk in 2005 — responsible for arbitrage between European equity index futures and the underlying baskets of stocks (a [[index-arbitrage|classic index arbitrage]] strategy).

**Delta One desk:**
- Officially ran market-neutral arbitrage between futures and underlying baskets.
- Position limits: typically €100M-€500M notional.
- Reporting: daily mark-to-market + position reports to risk committee.

Kerviel's unauthorized scheme (2005-2008):
1. Built large directional long positions in European index futures.
2. Created **fake offsetting forward contracts** in the firm's internal systems to hide the positions from middle-office reconciliation.
3. Used his back-office knowledge to know exactly which controls would catch which fake trades.
4. Position grew incrementally from a few hundred million to **€50B notional** by January 2008.

The positions were nominally profitable through 2007 (markets were rallying); by January 2008 the subprime crisis triggered a sell-off, and Kerviel's positions began bleeding.

## The Discovery

**January 18, 2008 (Friday):** Risk committee detected unusual exposure pattern.

**January 19-20, 2008 (weekend):** Internal investigation revealed €50B unauthorized position.

**January 21, 2008 (Monday) — "Black Monday Europe":**
- SocGen began emergency unwinding of Kerviel's €50B futures position.
- European equity futures dropped 6-7%.
- DAX and CAC 40 had their largest single-day drops in years.
- Initial market interpretation: subprime crisis broadening.

**January 22, 2008:** US Federal Reserve emergency cuts rate **75 bp** (Fed Funds 4.25% → 3.50%) — first inter-meeting emergency cut since 1984. Markets initially interpreted as response to broader crisis.

**January 23, 2008:** Final SocGen position unwind completed.

**January 24, 2008:** SocGen publicly disclosed the Kerviel scandal. Markets realized the Monday-Tuesday selloff had been partly Kerviel-driven; rallied on the news (the "real" crisis hadn't worsened).

## The Cascade

| Date | Event | Market Impact |
|------|-------|---------------|
| Jan 18 | Risk committee flag | None (private) |
| Jan 19-20 | Internal investigation | Weekend |
| Jan 21 | SocGen forced unwinding begins | DAX -7.2%, CAC 40 -6.8% |
| Jan 22 | Fed emergency 75 bp cut | DAX -4.9%, S&P -1.1% (cushioned) |
| Jan 23 | SocGen unwind completed | Markets stabilize |
| Jan 24 | Public disclosure | DAX +1.2% (relief) |
| Jan 25 | Kerviel arrested | n/a |

Total market notional moved by SocGen unwind: estimated **€100-150B equivalent** in cascading effects (Kerviel's €50B + market's reaction).

## The Trial

**January 25, 2008:** Kerviel arrested, charged with breach of trust + fraud + IT abuse.

**October 2010:** Convicted on all counts. Sentenced to **5 years prison (3 suspended)** + ordered to repay **€4.9B** to SocGen (clearly impossible).

**June 2014:** Final court ruling reduced repayment to **€1M** civil penalty.

Kerviel's defense: **"Everyone knew."** Argued his managers were aware of the unauthorized positions but tolerated them while profitable. Internal SocGen culture allegedly winked at limit violations as long as P&L was positive.

## Trading the forced unwind

The Kerviel scandal created arbitrage opportunities for traders who anticipated the unwind — a classic [[counterparty-stress-arbitrage|counterparty-stress]] setup where a distressed seller must dump a position larger than market-clearing liquidity:

**Pre-disclosure (Jan 21-23, 2008):** A few sophisticated traders observed the abnormal European futures selling pressure (no clear macro driver) and shorted into the move. Captured 6-8% over 3 days. Estimated $100-300M extracted by 5-10 specialist arb desks.

**Post-disclosure Fed-cut interaction:** The Fed's 75 bp emergency cut (responding to perceived crisis) inflated risk-asset prices once Kerviel was disclosed. Long risk assets at the dip captured the bounce.

**Index-arbitrage convergence:** During the unwind, futures-vs-cash basis dislocated; specialist [[index-arbitrage|index arb]] desks captured the convergence as basis closed.

## Lessons for Traders

1. **Back-office knowledge enables fraud.** Kerviel exploited his back-office training to know exactly which controls to bypass. Same lesson as Hamanaka, Leeson, Adoboli.
2. **"Profitable rogue trading" gets winked at.** Internal cultures that prioritize P&L over compliance enable fraud — until the trade goes wrong.
3. **Forced-unwind selling pressure can be detected.** Specialist traders flagged the Jan 21-23 selling as anomalous; pre-positioned shorts profited.
4. **Central-bank reactions to crises can be wrong-cause.** The Fed's emergency cut was partly responding to forced-unwind pressure that didn't reflect underlying economic conditions. Pattern: be skeptical of "crisis-driven" central-bank actions when forced-seller dynamics may be the trigger.
5. **The 2008 subprime crisis wasn't yet at Sept-2008 acute phase.** The Kerviel-driven January panic was a preview; real systemic stress came 8 months later. But the Fed had already used emergency tools — limiting later flexibility.

## Comparable Events

| Event | Trader | Loss | Year |
|-------|--------|------|------|
| Nick Leeson / Barings | Nick Leeson | $1.4B | 1995 |
| Sumitomo Copper / Hamanaka | Yasuo Hamanaka | $2.6B | 1996 |
| LTCM | n/a | $4.6B | 1998 |
| Allied Irish Banks / Rusnak | John Rusnak | $691M | 2002 |
| **Société Générale / Kerviel** | **Jérôme Kerviel** | **€4.9B** | **2008** |
| UBS / Adoboli | Kweku Adoboli | $2.3B | 2011 |
| JPMorgan / "London Whale" | Bruno Iksil | $6.2B | 2012 |
| Archegos / Hwang | Bill Hwang | $10-12B | 2021 |
| LME Nickel / Tsingshan | Xiang Guangda | $8B+ | 2022 |

## Aftermath

- **2008-2010:** SocGen wrote down losses; recapitalized via €5.5B rights issue (Feb 2008) — see [[rights-issue-arbitrage]].
- **2008:** Stock dropped 50%+ over 2008; eventually recovered.
- **2010:** Daniel Bouton (CEO during scandal) resigned.
- **2014:** Kerviel sued SocGen for unfair dismissal; mixed court rulings.
- **2016:** Kerviel filed lawsuit alleging SocGen had defrauded the French government via auditor reports; court rejected.
- **Ongoing:** Kerviel periodic public commentary; occasional media appearances.
- **2025:** Kerviel writes/speaks publicly on banking culture; remains controversial figure.

## Sources

- Société Générale, *Communication on Trading Loss* (January 24, 2008).
- *Le Figaro*, *Le Monde*, *Financial Times* contemporaneous coverage Jan-Feb 2008.
- Jérôme Kerviel, *L'Engrenage: Mémoires d'un Trader* (2010, autobiography).
- *Société Générale Annual Report 2008*.
- French Cour de Cassation rulings 2010-2016.

## Related

[[risk-arbitrage]] · [[1995-sumitomo-copper-scandal]] · [[1991-salomon-treasury-auction-scandal]] · [[archegos-blowup-2021]] · [[ltcm-collapse-1998]] · [[index-arbitrage]] · [[rights-issue-arbitrage]] · [[2008-global-financial-crisis]]

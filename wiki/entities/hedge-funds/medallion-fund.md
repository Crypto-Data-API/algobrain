---
title: "Medallion Fund"
type: entity
entity_type: fund
created: 2026-04-06
updated: 2026-06-10
status: good
tags: [company, quantitative, algorithmic, machine-learning]
founded: 1988
headquarters: "East Setauket, New York, USA"
website: "https://www.rentec.com"
aliases: ["medallion", "Medallion", "RenTech Medallion"]
related: ["[[renaissance-technologies]]", "[[jim-simons]]", "[[the-man-who-solved-the-market]]", "[[quantitative-trading]]", "[[algorithmic-trading]]", "[[machine-learning]]", "[[risk-management]]", "[[statistical-arbitrage]]", "[[two-sigma]]", "[[de-shaw]]"]
---

# Medallion Fund

[[renaissance-technologies]]' flagship quantitative hedge fund, widely considered the most successful investment fund in history with approximately 66% average annual returns before fees (roughly 39% net of the fund's steep 5-and-44 fee structure) since 1988. Founded and led for decades by [[jim-simons]], who died on May 10, 2024; the fund continues to operate under Renaissance CEO Peter Brown.

## Performance and Structure

Since its inception in 1988, the Medallion Fund has generated cumulative returns that dwarf any other known investment vehicle. The fund has had only one losing year (1989, a minor loss) and delivered positive returns even during the [[2008-global-financial-crisis]] (a reported ~152% gross / ~80% net in 2008) and the 2020 COVID crash (reported gains around 76% in 2020, a year in which Renaissance's public-facing funds RIEF and RIDA suffered double-digit losses — a striking demonstration that Medallion's edge is distinct from the firm's longer-horizon products). Its track record through 2018 is documented in detail in [[the-man-who-solved-the-market]] by Gregory Zuckerman: roughly $100 billion+ in cumulative trading profits, 66.1% average gross and 39.1% average net annual returns 1988-2018.

The fund is capped at approximately **$10-15 billion** in assets and is **closed to outside investors** — the last outside money was bought out in 2005, and only current and former employees of [[renaissance-technologies]] can invest. Profits above the cap are distributed back to investors each year. This size constraint is deliberate: the strategies trade short-term patterns that would lose their edge at larger scale. Fees are famously the highest in the industry: a 5% management fee and a 44% performance fee.

## Strategy and Methods

Medallion's approach relies on **machine learning**, **signal processing**, and **statistical pattern recognition** applied to enormous datasets of market prices, volume, and other signals. The firm hires mathematicians, physicists, computer scientists, and statisticians — not finance professionals. Holding periods are typically very short, ranging from seconds to a few weeks, and the book runs thousands of simultaneous positions with substantial leverage (reportedly via basket-option structures with banks).

The fund's methods remain among the most closely guarded secrets in finance. Renaissance employees sign strict non-disclosure agreements, and remarkably little is known about the specific signals or models used. What is known is that the fund trades across equities, futures, currencies, and fixed income markets with high diversification and rigorous [[risk-management]]. It is the canonical example of [[statistical-arbitrage]] executed at industrial scale.

## Status After Jim Simons (2024-2026)

- Simons retired as CEO in 2009 (succeeded by co-CEOs Peter Brown and Robert Mercer) and stepped back from the board in 2021; he remained invested in Medallion until his death on **May 10, 2024**, at age 86.
- **Peter Brown** has led the firm since Mercer stepped down as co-CEO in November 2017, and continues to lead it after Simons's death. The firm's operations and the employee-only Medallion structure are unchanged as of 2026.
- No audited Medallion performance figures are published; post-2018 numbers circulate only via press reports (e.g., the widely reported 76% gain in 2020). Renaissance's secrecy means any specific post-2020 annual return figure should be treated as unverified.

## Trading Relevance

- **Existence proof for quant edge.** Medallion is the strongest public evidence that persistent, scalable-but-capped exploitation of short-horizon market inefficiencies is possible — the reference point in any debate about the [[efficient-market-hypothesis]].
- **Capacity discipline as alpha preservation.** The hard cap and annual profit distribution are the canonical case study in why high-frequency/short-horizon edges must stay small — directly relevant to the `capacity_usd` field on every strategy page in this wiki.
- **Signal half-life.** Zuckerman documents that Medallion's individual signals are often weak (barely better than coin flips) but combined across thousands of bets — the practical illustration of the law of large numbers applied to low-information-ratio signals.
- **Talent model.** Hiring scientists rather than traders, and compensating via fund participation rather than salary, became the template for [[two-sigma]], [[de-shaw]], and the modern quant industry.

## Related

- [[renaissance-technologies]] — the parent firm
- [[jim-simons]] — founder (1938-2024)
- [[the-man-who-solved-the-market]] — definitive book-length account
- [[quantitative-trading]] / [[algorithmic-trading]] — the discipline
- [[statistical-arbitrage]] — the strategy family
- [[machine-learning]] — the method
- [[risk-management]]
- [[two-sigma]], [[de-shaw]] — peer quant firms
- [[efficient-market-hypothesis]] — the theory Medallion challenges

## Sources

- Zuckerman, Gregory. *The Man Who Solved the Market: How Jim Simons Launched the Quant Revolution* (Portfolio, 2019). ([[the-man-who-solved-the-market]]) — source for 66.1% gross / 39.1% net 1988-2018, fee structure, 1989 losing year, methods.
- *Wall Street Journal* / *Bloomberg* reporting on Medallion's 2008 (~80% net) and 2020 (~76%) returns and on RIEF/RIDA's 2020 losses.
- Renaissance Technologies obituary coverage of Jim Simons (died May 10, 2024): NYT, Bloomberg, FT, May 2024.
- QuantifiedStrategies.com, "Decoding the Medallion Fund Returns": https://www.quantifiedstrategies.com/medallion-fund-returns/
- Quartr, "Renaissance Technologies and The Medallion Fund": https://quartr.com/insights/edge/renaissance-technologies-and-the-medallion-fund
- Verified via web search 2026-06-10: Peter Brown leads the firm post-Simons; Medallion remains employee-only at ~$10-15B; no losing year since 1989.

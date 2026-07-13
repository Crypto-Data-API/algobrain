---
title: "Rule of 40"
type: concept
created: 2026-07-02
updated: 2026-07-02
status: good
tags: [fundamental-analysis, valuation, stocks]
aliases: ["Rule of 40", "rule-of-40", "40% Rule"]
domain: [fundamental-analysis]
difficulty: intermediate
related: ["[[revenue-growth]]", "[[free-cash-flow]]", "[[ebitda]]", "[[operating-margin]]", "[[net-margin]]", "[[price-to-sales-ratio]]", "[[growth-investing]]", "[[deferred-revenue]]", "[[saas-valuation]]"]
---

The Rule of 40 is a rule-of-thumb used to judge the health of a software or [[saas-valuation|SaaS]] company: a company's annual [[revenue-growth]] rate (in %) plus its profit margin (in %) should sum to at least 40. It is a shorthand for the fundamental trade-off every subscription-software business faces — spending on sales, marketing, and R&D drives growth but suppresses margin, while restraint boosts margin but slows growth. A company scoring 40 or above is deemed to be balancing the two acceptably; one below 40 is spending inefficiently for the growth it is buying.

## What it measures

Software businesses can create value along two axes: growing revenue quickly, or converting revenue into profit and cash. Early on, most SaaS firms sacrifice profitability to grow — customer-acquisition cost is paid upfront while subscription revenue arrives over years, so aggressive growth *looks* unprofitable even when the underlying unit economics are excellent. The Rule of 40 packages both axes into a single number so an investor can compare a fast-growing but loss-making company against a slower, cash-generative one on a common footing.

**Rule-of-40 score = revenue growth rate (%) + profit margin (%)**

- A hyper-growth start-up growing 60% while burning cash at a −15% margin scores 45 — it passes, because the growth more than compensates for the losses.
- A mature platform growing 10% at a 35% margin scores 45 — it also passes, from the opposite direction, on profitability rather than growth.
- A company growing 20% at a 5% margin scores 25 — it fails, signalling it is neither growing fast enough nor profitable enough to justify its spending.

The elegance of the heuristic is that it does not prescribe *how* a company should reach 40, only that the combination of the two levers clears the bar.

## Which margin to use

There is **no single canonical definition** of the "margin" term, and this is the metric's biggest ambiguity. Common variants include:

| Variant | Margin used | Notes |
|---------|-------------|-------|
| FCF Rule of 40 | [[free-cash-flow]] margin (FCF / revenue) | Often favoured because it reflects real cash generation and is harder to flatter with accounting choices; can be distorted by working-capital swings and [[deferred-revenue]] timing. |
| EBITDA Rule of 40 | [[ebitda]] margin | Popular with private-equity and later-stage investors; excludes [[capex]] and [[share-based-compensation]], so it can overstate true profitability for software firms with heavy stock comp. |
| Operating-margin Rule of 40 | [[operating-margin]] (GAAP or non-GAAP) | Closest to reported operating performance; sensitive to whether stock-based compensation is included. |
| Net-margin Rule of 40 | [[net-margin]] | Least common; distorted by tax, interest, and one-off items. |

The **growth** term is usually year-over-year total revenue growth, though some analysts substitute [[deferred-revenue|ARR]] or subscription-revenue growth to focus on the recurring core rather than one-off or services revenue. Because both the growth and margin inputs can be defined several ways, two analysts can compute very different Rule-of-40 scores for the same company. Best practice is to state the exact definitions used and apply them consistently across a peer set, and to be wary of management presentations that quietly choose the most flattering margin (frequently non-GAAP or adjusted EBITDA that excludes stock-based compensation).

## Worked example

A subscription-software company grows revenue 30% year over year and converts 12% of revenue into free cash flow:

- Revenue growth = 30
- FCF margin = 12
- **Score = 30 + 12 = 42 → passes** (comfortably above 40)

Now suppose the same company matures: growth slows to 18% but the FCF margin expands to 20% as it stops over-spending on acquisition:

- Score = 18 + 20 = 38 → **just fails**, flagging that the profitability gain did not fully offset the growth slowdown.

A negative-margin case: a younger firm growing 55% but burning cash at a −20% margin scores 55 + (−20) = 35 → **fails**, indicating its growth is not fast enough to justify the size of its losses. These illustrations use round numbers for teaching; they are not tied to any specific company.

## Why investors use it

- **One-number screen.** It collapses two dimensions — growth and profitability — into a single comparable figure, useful for quickly ranking a universe of software names.
- **Guards against "growth at any cost."** In cheap-capital environments SaaS firms are tempted to buy revenue regardless of economics; the rule penalises growth that comes with deep losses, tying the growth story back to eventual profitability.
- **Trade-off neutrality.** It does not force a company to be profitable *now*, acknowledging that a business with strong unit economics can rationally run losses while growing — as long as growth is fast enough to compensate.
- **Valuation context.** Rule-of-40 status is often used alongside a [[price-to-sales-ratio]] or EV/Revenue multiple: passing companies are frequently argued to deserve richer revenue multiples, and the score helps explain why two firms on similar sales multiples may not be equally attractive.

## Limitations

- **Rewards opposite profiles equally.** A 40 from 55% growth and −15% margin is treated the same as a 40 from 10% growth and 30% margin, even though the two carry very different risk, durability, and capital-intensity profiles. The score says nothing about *which* mix is more valuable or durable.
- **Margin-definition gaming.** Because the margin term is undefined, management can pick the flattering measure (adjusted EBITDA excluding stock-based compensation is a common choice) to clear the bar cosmetically. Stock-based comp is a real cost to shareholders, so a Rule-of-40 "pass" built on excluding it can be misleading.
- **Arbitrary threshold.** 40 is a convention, not a law; there is nothing magic about the number, and a company at 38 is not meaningfully worse than one at 41.
- **Point-in-time and volatile.** A single quarter's growth or margin can be distorted by timing, one-off deals, or [[deferred-revenue]] recognition; the trend across several periods is more informative than one reading.
- **Not for non-software.** The heuristic was calibrated for high-gross-margin, recurring-revenue subscription software. Applying it to low-margin, capital-intensive, or cyclical businesses (retail, manufacturing, banks) produces meaningless results, because those industries have entirely different growth-vs-margin economics. Even within technology, its usefulness varies — it fits a [[cybersecurity]] SaaS vendor far better than a capital-heavy [[semiconductors|semiconductor]] manufacturer.
- **Ignores scale and quality of growth.** It treats a percentage point of growth the same at any revenue base and ignores retention, gross margin, and customer concentration — dimensions that matter enormously for a software company's long-run value.

## Related

[[revenue-growth]] · [[free-cash-flow]] · [[ebitda]] · [[operating-margin]] · [[net-margin]] · [[price-to-sales-ratio]] · [[growth-investing]] · [[deferred-revenue]] · [[share-based-compensation]] · [[saas-valuation]] · [[cybersecurity]] · [[semiconductors]]

## Sources

- General, widely-taught venture-capital and software-investing knowledge. The Rule of 40 emerged from SaaS and growth-equity practice in the 2010s as a rule-of-thumb for balancing growth against profitability; the relationships, variants, and caveats described here are standard market convention rather than a proprietary formula. No specific company figures are cited — the numeric examples above are illustrative round numbers.

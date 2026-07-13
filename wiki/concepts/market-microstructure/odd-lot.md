---
title: "Odd Lot"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [market-microstructure, liquidity, stocks]
aliases: ["Odd Lot", "Odd Lots", "Odd-Lot", "Round Lot", "Round Lots", "Board Lot", "Lot Size", "Mixed Lot", "Odd-Lot Order"]
domain: [market-microstructure]
prerequisites: ["[[order-book]]", "[[liquidity]]", "[[bid-ask-spread]]"]
difficulty: beginner
related: ["[[order-book]]", "[[liquidity]]", "[[bid-ask-spread]]", "[[market-maker]]", "[[ticker-symbol]]", "[[stock-split]]", "[[market-hours]]", "[[slippage]]"]
---

A **lot** is the conventional trading unit for a stock. A **round lot** is the standard block — historically and most commonly **100 shares** — while an **odd lot** is any order for **fewer than one round lot** (1–99 shares) and a **mixed lot** is an order that is not an exact multiple of the round lot (e.g. 250 shares = two round lots plus a 50-share odd lot). The distinction is a piece of market plumbing, but it quietly shapes which quotes you see, how your small order is treated, and what the "best price" on a screen actually represents.

## Why 100 shares?

The 100-share round lot is a convention from the era of paper certificates and floor trading, when exchanges standardised an order size that was efficient to clear and quote. It persists today in the market's data structure even though most retail orders are far smaller. Some very high-priced or specialised securities use a different round-lot size, and exchanges outside the US set their own "board lot" sizes by price band.

## Why odd lots were second-class citizens

For most of market history, odd-lot orders were treated as inferior to round lots:

- **Not in the protected quote.** Under Reg NMS, a quotation for fewer than a round lot is **not a "protected quotation"** and does not set the National Best Bid and Offer ([[bid-ask-spread|NBBO]]). An odd-lot bid better than the round-lot best bid could be ignored by the order-protection rule.
- **Invisible on the tape.** Odd-lot *trades* were **excluded from the consolidated tape** until **December 2013** (effective into 2014). Before that, a large share of small-investor activity simply did not appear in reported volume — a real gap in the data.
- **Worse handling.** Odd lots were often routed to a specialist or dealer and filled at the round-lot price rather than competing directly, so odd-lot traders historically faced wider effective [[slippage|slippage]].

## Why odd lots now dominate

Two structural shifts made odd lots a large and growing share of activity rather than a rounding error:

- **High nominal share prices.** As marquee names ran to hundreds or thousands of dollars per share (pre-split Amazon, Alphabet, Booking, and Berkshire's never-split BRK.A), a 100-share round lot became unaffordable for ordinary investors, so most orders in those names are odd lots. A [[stock-split|stock split]] lowers the price and pushes activity back toward round lots — one of the practical reasons companies split.
- **Fractional shares.** Brokers introduced dollar-based and fractional-share investing around 2019–2020, so a "$50 of AAPL" order is intrinsically an odd lot (or a fraction of a share). Odd lots now make up a very large fraction of trades in high-priced stocks — in some names, a majority.

## Regulatory catch-up: odd lots in core data

Regulators have moved to give odd-lot quotes more standing as they have grown more important:

- Since late 2013, **odd-lot transactions are reported to the consolidated tape**, so reported volume finally reflects small-order activity.
- The SEC's **Market Data Infrastructure Rule (adopted 2020)** introduced **variable, price-tiered round-lot sizes** — for the highest-priced stocks a round lot can be far fewer than 100 shares — and added the **best odd-lot order** to the core ("round-lot-plus") market data that vendors must disseminate. The intent is that the screen price better reflects where small investors can actually trade.

## Practical takeaways for dashboard users

- The headline **bid/ask you see is built from round lots**; in a high-priced stock the real best price for a small order can sit *inside* that quote as an odd-lot order.
- **Odd-lot orders execute normally** at retail brokers today — you are not penalised for buying 7 or 37 shares — but in very thin names the available size at the best price may be small.
- A **[[stock-split|stock split]]** shifts a name back toward affordable round lots; a soaring share price does the opposite.
- **Fractional-share orders are odd lots by nature**, which is why they may be aggregated by the broker before reaching the market.

## Related

- [[order-book]] — where round-lot and odd-lot interest sits
- [[bid-ask-spread]] — the NBBO is a round-lot construct; odd lots can price inside it
- [[liquidity]] — round-lot depth is the usual liquidity measure
- [[market-maker]] — historically internalised odd-lot flow
- [[ticker-symbol]] — the security being traded in lots
- [[stock-split]] — lowers price and restores round-lot affordability
- [[slippage]] — odd lots historically faced worse effective execution
- [[market-hours]] — odd-lot handling is thinnest outside regular hours

## Sources

- SEC, "Market Data Infrastructure" final rule (2020) — variable round-lot sizes and inclusion of the best odd-lot order in core data, sec.gov.
- FINRA / consolidated tape (CTA, UTP) rule changes adding odd-lot trade reporting, effective December 2013.
- SEC Reg NMS — definition of protected quotations and round lots.
- Industry and academic studies documenting the rising share of odd-lot volume in high-priced US equities.

---
title: Payment for Order Flow
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [market-microstructure, regulation, company, liquidity]
aliases: [PFOF, "Payment for Order Flow", order flow payment, selling order flow]
domain: [market-microstructure, regulation]
prerequisites: ["[[order-flow]]", "[[bid-ask-spread]]", "[[market-maker]]"]
difficulty: intermediate
related:
  - "[[order-flow]]"
  - "[[market-maker]]"
  - "[[bid-ask-spread]]"
  - "[[liquidity]]"
  - "[[adverse-selection]]"
  - "[[high-frequency-trading]]"
---

# Payment for Order Flow

Payment for order flow (PFOF) is the practice where retail brokers receive compensation from wholesale market makers in exchange for routing customer orders to them for execution, rather than sending those orders directly to a public exchange. It is the economic engine behind "commission-free" retail trading in the US and one of the most contested features of modern equity and options [[market-microstructure]].

## How It Works

1. A retail trader places an order through their broker (e.g., to buy 100 shares of AAPL).
2. Instead of routing to a public exchange (NYSE, Nasdaq), the broker sends the order to a wholesale [[market-maker]] / internalizer (e.g., Citadel Securities, Virtu Financial, Susquehanna/G1X, Jane Street).
3. The market maker executes the order — typically at a price slightly better than the public best bid/offer (NBBO), called *price improvement* — and pays the broker a small rebate per share or per contract (often fractions of a cent for stocks; meaningfully more for options).
4. The market maker profits from the [[bid-ask-spread]] and from the informational characteristics of retail flow.

## Why Retail Flow Is Valuable

Retail order flow is prized because it is largely **uninformed** (or "non-toxic"): retail orders are uncorrelated with short-term price direction, so the wholesaler faces little [[adverse-selection]] risk when filling them. Contrast this with institutional/HFT flow, which is often informed and moves the market against the liquidity provider. A wholesaler can therefore quote inside the spread to retail and still capture a reliable margin — and shares some of that margin back to the broker as PFOF. This is the same toxic-vs-benign flow distinction central to [[order-flow]] and [[market-maker]] economics.

## The Controversy

**Proponents argue:**
- PFOF enables zero-commission trading for retail investors.
- Wholesalers routinely provide price improvement over the public exchange quote, so customers often get *better* prices than they would on-exchange.
- For typical small retail orders, the net benefit (no commission + price improvement) exceeds any execution-quality loss.

**Critics argue:**
- It creates a conflict of interest — brokers are incentivized to route for maximum PFOF revenue, not necessarily best execution.
- Concentrating retail flow in a handful of internalizers removes it from public exchanges, harming on-exchange [[price-discovery]] and competition.
- Price-improvement metrics are measured against the NBBO, which itself may be wider than it would be if retail flow competed on-exchange.
- The practice obscures the true cost of trading and makes execution quality hard for retail to assess.

## Regulatory Status

- **United States — legal but heavily scrutinized.** PFOF remains permitted. The SEC's December 2022 market-structure package included the proposed **Rule 615 ("Order Competition Rule")**, which would require certain retail orders to be exposed to competitive auctions before internalization. As of mid-2026 Rule 615 has **not been adopted** and remains a pending proposal (Source: Perplexity sonar, 2026-06-11; SEC release 34-96495, Dec 14 2022).
- **Rule 605 amendments adopted.** In March 2024 the SEC adopted amendments to **Rule 605** expanding and modernizing execution-quality disclosure (broker-dealers must publish standardized stats), increasing transparency around the execution quality retail receives (Source: Perplexity sonar, 2026-06-11; SEC press release 2024-32). This sits alongside related tick-size and access-fee reforms.
- **Banned elsewhere.** PFOF is prohibited in the **United Kingdom**, **Canada**, and **Australia**, and the **European Union** agreed (2023) to phase out PFOF across member states by 2026.

## Trading Relevance

Retail traders should understand that "commission-free" trading is not truly free — the cost is embedded in the spread captured by the wholesaler and the routing economics of the PFOF model. For small marketable orders the net effect is usually favorable (price improvement often exceeds the implicit cost). For larger, time-sensitive, or limit orders, traders who care about execution quality may prefer brokers offering direct market access, exchange-routing choice, or order-by-order disclosure. Reviewing a broker's Rule 605/606 reports is the concrete way to assess where orders go and how well they fill.

## Related

- [[order-flow]] — the underlying commodity being sold
- [[market-maker]] — the wholesalers that pay for and internalize retail flow
- [[adverse-selection]] — why uninformed retail flow is the valuable kind
- [[bid-ask-spread]] — the source of the wholesaler's margin
- [[high-frequency-trading]] — the technology layer wholesalers use to internalize profitably

## Sources

- SEC, "Order Competition Rule" proposal, Release No. 34-96495 (December 14, 2022) — the proposed Rule 615 auction requirement (status: pending as of mid-2026).
- SEC press release 2024-32 (March 6, 2024) — adopted amendments to Rule 605 on execution-quality disclosure.
- SEC Rule 606 — broker order-routing disclosure, including PFOF received.
- Perplexity (sonar), 2026-06-11 — confirmation that Rule 615 remains pending and Rule 605 amendments were adopted in March 2024.

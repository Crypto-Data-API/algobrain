---
title: "Smart Order Routing"
type: concept
created: 2026-04-14
updated: 2026-04-14
status: good
tags: [market-microstructure, algorithmic-trading, order-types, stocks]
aliases: ["smart order routing", "SOR", "smart router"]
domain: [market-microstructure]
difficulty: intermediate
prerequisites: ["[[market-microstructure]]"]
related: ["[[flash-crash-2010]]", "[[high-frequency-trading]]", "[[dark-pools]]", "[[order-types]]", "[[flash-crashes]]", "[[best-execution]]", "[[algorithmic-trading]]"]
---

Smart order routing (SOR) is the automated process of directing trade orders across multiple trading venues — stock exchanges, dark pools, alternative trading systems (ATSs), and electronic communication networks (ECNs) — to achieve the best available execution price. In fragmented modern markets where the same stock trades on 15+ venues simultaneously, SOR is essential for complying with best-execution obligations and minimizing market impact. SOR failures during stress are a contributing factor to [[flash-crashes|flash crashes]], as routers can fail to find liquidity when order books thin out across all venues simultaneously.

## How It Works

### Basic SOR Logic

1. **Receive order** — e.g., buy 10,000 shares of AAPL
2. **Scan venues** — check real-time order books on NYSE, Nasdaq, BATS, IEX, dark pools, etc.
3. **Evaluate** — compare prices, available size, fees/rebates, and expected fill probability
4. **Route** — split the order across venues to minimize cost:
   - 3,000 shares at NYSE (best price, but only 3K available)
   - 2,000 shares at Nasdaq (next best)
   - 5,000 shares to a dark pool (to avoid information leakage)
5. **Adapt** — if fills don't happen, re-route remaining shares to alternative venues

### Factors Considered

| Factor | Description |
|--------|-------------|
| **NBBO** (National Best Bid/Offer) | The best available price across all venues — Reg NMS requires routing to NBBO |
| **Depth** | How much size is available at each price level |
| **Fees / rebates** | Maker-taker fee structures vary by venue ($0.20-0.30 per 100 shares) |
| **Latency** | Round-trip time to each venue (microseconds matter for HFT) |
| **Fill probability** | Historical fill rates at each venue for similar orders |
| **Information leakage** | Risk that showing the order on a lit exchange will move the price (dark pools reduce this) |

## Regulatory Context

### Reg NMS (US, 2005)

Regulation National Market System requires that trade orders be routed to the venue displaying the best price (NBBO). This regulation:
- Made SOR mandatory for broker-dealers
- Created the fragmented multi-venue market structure
- Incentivized speed — the fastest routers can capture the best prices before they disappear

### MiFID II (EU, 2018)

Requires brokers to demonstrate best execution across all EU venues, including reporting execution quality metrics. Expanded SOR obligations to cover all asset classes, not just equities.

## SOR and Market Stability

### Flash Crash Contribution

During the [[flash-crash-2010|2010 Flash Crash]], SOR systems contributed to the cascade:
- Routers found no bids on primary exchanges and routed orders to thinner venues
- Thinner venues had wider spreads and less depth, producing worse fills
- Some routers routed sell orders to venues with "stub quotes" (placeholder bids at $0.01), producing absurd fills (Accenture at $0.01)
- The speed of SOR meant these bad fills happened in milliseconds, before any human could intervene

### Liquidity Mirage

SOR can create a "liquidity mirage" — the same liquidity appears to be available on multiple venues because market makers quote on all of them, but they cancel quotes on other venues when filled on one. The aggregate displayed liquidity across all venues overstates the *unique* liquidity available.

## Evolution

### First Generation (2000s)
Simple price comparison — route to the venue with the best price. No intelligence about fill probability, information leakage, or fee optimization.

### Second Generation (2010s)
ML-based models that predict fill probability, optimize fee/rebate capture, and adapt routing based on real-time conditions. Anti-gaming logic to detect venues where quotes are likely to fade.

### Third Generation (2020s)
Reinforcement learning-based routers that continuously optimize across hundreds of venues and dark pools, incorporating real-time signals about market maker behavior, short-term price prediction, and toxicity analysis.

## Related

- [[flash-crash-2010]] — SOR failures contributed to cascade
- [[high-frequency-trading]] — HFT firms invest heavily in SOR for latency advantage
- [[dark-pools]] — a key destination for SOR to minimize information leakage
- [[flash-crashes]] — SOR fragility under stress
- [[algorithmic-trading]] — SOR is a core component of execution algorithms
- [[order-types]] — SOR interacts with various order types across venues

## Sources

- (Source: [[book-flash-boys]]) — Michael Lewis's account of SOR and HFT market structure
- (Source: [[book-dark-pools]]) — Scott Patterson on the history of electronic market fragmentation
_Additional content based on SEC/FINRA SOR guidance, Reg NMS documentation, and public market microstructure research. No raw sources ingested._

---
title: "Historical Cable Arbitrage (1920s–1930s Transatlantic FX)"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, forex, history, market-microstructure, gold]
aliases: ["Cable Arb", "Transatlantic Triangular Arbitrage", "Interwar FX Arbitrage"]
strategy_type: algorithmic
timeframe: intraday
markets: [forex]
complexity: advanced
backtest_status: retired
edge_source: [latency, informational]
edge_mechanism: "Cable transmission delays between London, New York, and Paris meant quoted cross-rates lagged reality by 2–10 minutes, allowing a dealer with simultaneous visibility on all three legs to lock in inconsistencies."
data_required: [tick-fx-london, tick-fx-new-york, tick-fx-paris, cable-transmission-log]
min_capital_usd: 100000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 2.0
expected_max_drawdown: 0.10
breakeven_cost_bps: 3
decay_evidence: "Eliminated progressively by shortwave radio (late 1930s), teleprinter networks, and ultimately the Reuters Monitor (1973)."
---

# Historical Cable Arbitrage (1920s–1930s Transatlantic FX)

Historical cable arbitrage was [[triangular-arbitrage]] executed across the London, New York, and Paris foreign-exchange markets during the interwar period, exploiting the finite transmission time of telegraph cables to capture cross-rate inconsistencies before they were reconciled. The term "cable" itself — still used today for GBP/USD — originated because the pound-dollar rate was literally quoted by transatlantic submarine cable. It is the direct ancestor of modern [[latency-arbitrage]].

> **Historical lineage.** The trade is older than the interwar window documented here. The **first transatlantic telegraph cable (1858, and the durable 1866 cable)** collapsed quote-transmission time between London and New York from roughly **ten days (by ship) to minutes**, creating the very latency gap this strategy exploits. Bullion and bill dealers ran rate-reconciliation arbitrage across the Atlantic from the 1860s onward; the **1925-1931 gold-standard window** described below is simply the best-documented, best-reconstructed era of the practice. All dates and figures on this page are preserved from that documented record.

## At a Glance

| Attribute | Value |
|-----------|-------|
| Strategy family | [[triangular-arbitrage]] across three FX venues |
| Active window | ~1860s telegraph era; best-documented 1925-1931 gold standard |
| Venues | London (GBP/USD), New York (USD/FRF), Paris (GBP/FRF) |
| Edge source | Latency (primary) + informational (secondary) |
| Quote staleness exploited | 2-10 minutes round-trip on cables |
| Realized cross-rate deviation | ~1-10 bps (Einzig; Accominotti & Chambers 2016) |
| Typical execution size | £100,000-£500,000 per round trip (largest houses) |
| Breakeven cost | ~3 bps round trip |
| Status | **Retired** — killed by faster transmission + end of gold standard |
| Modern descendant | [[latency-arbitrage]] (Chicago-NY microwave), [[covered-interest-arbitrage]] |

## Edge Source

Primarily **latency**, with a secondary **informational** component.

| Edge component | Source | Decay driver |
|----------------|--------|--------------|
| **Latency** | Cable round-trip of 2-10 minutes left quotes stale | Shortwave radio (1927+), teleprinters, Reuters Monitor (1973) |
| **Informational** | Simultaneous three-venue visibility vs single-venue correspondents | Wider real-time quote dissemination |
| **Structural (gold points)** | Gold-shipment costs bounded FX deviation, defining the no-arb band | End of the gold standard (sterling 1931, franc 1936) |
 A dealer with staff simultaneously watching all three markets — typically via leased lines into the Commercial Cable Company or Western Union — could see a pound-dollar-franc triangle go out of parity on one leg and execute before the other two legs received and repriced on the new information. Round-trip quote-and-acknowledge cycles on cables ran 2–10 minutes; dedicated "flash" circuits operated by the largest houses were materially faster.

## Why This Edge Exists

Between Britain's April 1925 return to the gold standard (at the prewar parity of $4.86 5/8 per pound) and sterling's September 1931 suspension, the London–New York–Paris triangle priced three freely convertible currencies — all three gold-anchored once the franc stabilized de facto in December 1926 (de jure with the Monetary Law of June 1928). In theory, if GBP/USD, USD/FRF, and GBP/FRF were all quoted live, their product should equal one. In practice, quotes were struck on different venues at different moments, and any quote a dealer saw on the tape was already 30 seconds to several minutes stale.

The counterparty was the slower dealer: the correspondent bank executing a customer order at a quote it believed was live but was in fact minutes behind. Paul Einzig's *The Theory of Forward Exchange* (1937) documents the practice in detail and was the standard reference used by interbank arbitrage desks through the 1950s. Einzig argued that realized interwar cross-rate spreads of 1–10 basis points were the observable equilibrium between the cost of cable time and the profit available from exploiting it — essentially an early formulation of the [[covered-interest-parity]] condition as an arbitrage limit rather than an identity.

## Null Hypothesis

Under instantaneous, noise-free transmission, the product of GBP/USD × USD/FRF × FRF/GBP would equal 1 to within bid-ask spread on every observation. Empirically, tape reconstructions (Einzig; Accominotti & Chambers, 2016, "If You're So Smart...") show persistent deviations of 1–10 bps through most of 1925–1930, collapsing after sterling floated in 1931.

## Rules

### Entry
1. Maintain simultaneous live quotes on **GBP/USD** (London), **USD/FRF** (New York), and **GBP/FRF** (Paris).
2. Compute implied GBP/FRF from the two direct legs: `implied = GBP/USD × USD/FRF`.
3. Compare against the Paris quote. If `|implied − paris_quote| > (total_cable_fees + dealer_spread + slippage)`, signal.
4. Verify the cross-rate dislocation is visible on at least two venues (not a single stale print).
5. Dispatch three simultaneous orders via separate cable circuits to minimize serialized-execution risk.

### Exit
Positions are closed by the nature of the trade: the triangle begins and ends in the starting currency (usually sterling, because the largest settlement balances were at London clearing banks). Any leg that fails to fill creates an unwanted open FX exposure that must be closed at market on the next available quote.

### Position Sizing
Sized to (a) the liquidity on the thinnest of the three legs and (b) the dealer's available clearing balances at each of the three settlement points. Practical sizes at the largest houses (rothschild-family, baring-brothers, J.P. Morgan, Hambros) reached £100,000–£500,000 per execution (several million to tens of millions in 2026 dollars).

## Implementation Pseudocode

```
loop:
    london_quote   = cable_read("GBP/USD", london)
    ny_quote       = cable_read("USD/FRF", new_york)
    paris_quote    = cable_read("GBP/FRF", paris)
    timestamp_gap  = max(quote_age(all))
    if timestamp_gap > 180_seconds:
        continue   # quotes too stale to trust

    implied = london_quote * ny_quote
    spread  = abs(implied - paris_quote) / paris_quote

    if spread > breakeven_bps:
        direction = sign(implied - paris_quote)
        simultaneously:
            cable_order(london, "GBP/USD", direction, size)
            cable_order(new_york, "USD/FRF", direction, size)
            cable_order(paris, "GBP/FRF", -direction, size)
        monitor_fills(timeout=5_minutes)
        if any_leg_unfilled:
            close_at_market(open_leg)
```

## Indicators / Data Used

- **GBP/USD cable quotes** from the London Stock Exchange and the Commercial Cable Company tape
- **USD/FRF** from the New York Foreign Exchange Committee
- **GBP/FRF** from the Paris Bourse coulisse
- **Cable transmission timestamps** — the age of each quote was itself a traded input
- **Bank rate** (Bank of England discount rate) — influenced forward points and the no-arbitrage band for [[covered-interest-arbitrage]]
- **Gold points** — upper and lower bounds on nominal FX fluctuation implied by physical gold shipment costs (see [[gold-point-arbitrage]])

## Example Trade

**Date:** March 1928. A London arbitrage clerk at a merchant bank observes:
- GBP/USD cable quote: **4.8665** (age: 45 seconds)
- USD/FRF New York quote: **25.52 FRF** (age: 60 seconds)
- Paris GBP/FRF quote: **124.35** (age: 90 seconds)

Implied GBP/FRF via USD: 4.8665 × 25.52 = **124.19**. Paris quotes 124.35 — sterling is 13 bps **overpriced** in Paris.

Action: Sell GBP/FRF in Paris (£200,000), buy GBP/USD in London, sell USD/FRF in New York, simultaneously via three cable lines. Total cable and commission costs: approximately 4 bps. **Net expected profit: ~9 bps on £200,000 ≈ £180** (roughly £12,000 in 2026 sterling) per round trip, executed 5–15 times per trading day by the largest desks.

## Performance Characteristics

Accominotti and Chambers (2016) reconstruct interwar FX returns and estimate Sharpe ratios well above 1.0 for cable-arbitrage-adjacent strategies during the classical gold-standard years (1925–1931), collapsing after sterling's float and the broader disintegration of the gold standard through 1936. Einzig's contemporary anecdotal accounts match: typical daily P&L was small per trade but highly consistent, with rare blow-ups around political events (Ruhr occupation, UK strike, sterling suspension).

## Capacity Limits

Constrained by (a) clearing-balance availability at the three settlement venues, (b) cable circuit capacity, and (c) the depth of the thinnest leg — typically Paris. Effective industry-wide capacity in the late 1920s is estimated at roughly $100M–$250M nominal at any time, distributed across perhaps a dozen major houses.

## What Kills This Strategy

- **Technological improvement**: shortwave radio (from ~1927), automated teleprinters, and eventually the **Reuters Monitor dealing system (1973)** collapsed quote-update latency from minutes to seconds to sub-second.
- **Regime change**: sterling's suspension of gold convertibility on 21 September 1931 destroyed the stable three-currency triangle. The franc followed in 1936.
- **Capital controls**: wartime and postwar exchange controls (1939 onward) made multi-venue execution legally impossible for decades.
- **Modern competition**: the surviving pure-latency version of this trade is the microwave-tower arbitrage between Chicago and New York ([[latency-arbitrage]]).

## Kill Criteria

Historically retired. Framed as the numerical retirement conditions a desk of the era would have used:

- Average captured spread < breakeven cost (3 bps) for 60 consecutive trading days
- Third-leg fill rate < 80% over a rolling month (serialized-execution risk dominating)
- Any of the three settlement venues suspends gold convertibility or imposes exchange controls (regime kill — triggered 21 September 1931 for sterling)

The direct intellectual descendants — covered-interest arbitrage and modern triangular FX latency arbitrage — operate on sub-millisecond horizons.

## Modern Descendants

| Era | Strategy | Latency exploited | Page |
|-----|----------|-------------------|------|
| 1860s-1930s | Cable / transatlantic FX arb | Minutes (telegraph) | *this page* |
| 1920s-present | Covered-interest arbitrage | Forward-point mispricing | [[covered-interest-arbitrage]], [[covered-interest-parity]] |
| Gold-standard era | Gold-point / specie-flow arb | Physical shipment cost band | [[gold-point-arbitrage]], [[specie-flow-arbitrage]] |
| 1980s-present | Triangular FX arbitrage | Sub-second cross-rate | [[triangular-arbitrage]] |
| 2010s-present | Microwave / colocation latency arb | Microseconds | [[latency-arbitrage]] |

## Advantages

- **Near-zero directional exposure** when executed atomically
- **Scalable** within the constraints of clearing balances
- **Statistically stable** edge during the 1925–1931 gold-standard window
- **Educational ancestor** of every modern latency strategy

## Disadvantages

- **Execution risk**: a failed leg was an open FX position of substantial size
- **Political-regime risk**: one sovereign decision (sterling's float) ended the game
- **Capital intensity**: required clearing balances in three currencies simultaneously
- **Cable infrastructure cost**: leased circuits were a meaningful fixed overhead

## Sources

- Paul Einzig, *The Theory of Forward Exchange* (1937) — the foundational contemporary text
- Olivier Accominotti and David Chambers, "If You're So Smart: John Maynard Keynes and Currency Speculation in the Interwar Years" (*Journal of Economic History*, 2016)
- Marc Flandreau and Clemens Jobst, "The Ties That Divide: A Network Analysis of the International Monetary System, 1890–1910" (*Journal of Economic History*, 2005)

## Related

- [[triangular-arbitrage]]
- [[covered-interest-arbitrage]]
- [[covered-interest-parity]]
- [[gold-point-arbitrage]]
- [[gold-standard-mechanics]]
- [[specie-flow-arbitrage]]
- [[latency-arbitrage]]
- [[regional-currency-arbitrage]]
- [[bill-broking-arbitrage]]

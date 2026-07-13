---
title: High-Frequency Trading
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - market-microstructure
  - algorithmic-trading
  - hft
aliases:
  - hft
  - HFT
  - high-frequency
domain: [market-microstructure]
prerequisites: ["[[algorithmic-trading]]", "[[market-maker]]"]
difficulty: advanced
related:
  - "[[algorithmic-trading]]"
  - "[[market-maker]]"
  - "[[co-location]]"
  - "[[low-latency-trading]]"
  - "[[flash-crash-2010]]"
  - "[[spoofing]]"
---

# High-Frequency Trading

**High-frequency trading (HFT)** is a subset of [[algorithmic-trading]] characterised by ultra-low-latency execution (microseconds to nanoseconds), very high order-to-trade ratios, and near-zero overnight inventory. HFT firms exploit fleeting price discrepancies and earn the [[bid-ask-spread]] (plus exchange maker rebates) through automated [[market-maker|market making]]. They account for a large share of daily equity volume -- commonly estimated at 50-60% of U.S. equity trading volume (peaking higher in the early 2010s), with comparable shares in liquid futures and FX. Dominant firms include Citadel Securities, Virtu Financial, Jump Trading, Hudson River Trading, Jane Street, Tower Research, and DRW.

## How It Works

HFT competes on **speed of reaction to information**. The same public market data reaches every participant, but the firm that processes it and routes an order fastest captures the opportunity. The edge is therefore an arms race in latency, measured end-to-end from a market-data packet arriving at the firm's network card to its responding order reaching the exchange's matching engine. Top firms now operate at single-digit-microsecond round trips, with the fastest tick-to-trade paths in the hundreds of nanoseconds. Because the opportunity (a stale quote, a cross-venue dislocation) exists for only that long, being second is often worth nothing -- HFT is a **winner-take-most** game where the marginal nanosecond has economic value.

## Key Characteristics

- **Microsecond to nanosecond execution** -- HFT systems operate on timescales invisible to human traders, with round-trip latencies measured in single-digit microseconds.
- **Co-location** -- HFT firms pay exchanges to place their servers physically adjacent to the exchange's matching engine, minimizing network latency. See [[co-location]].
- **FPGA and custom hardware** -- many top firms use Field-Programmable Gate Arrays or even custom ASICs to process market data and generate orders faster than software-based systems can.
- **Massive order-to-trade ratios** -- HFT strategies may submit and cancel thousands of orders for every trade executed, continuously updating quotes as market conditions shift.

## Common HFT Strategies

- **Electronic market making** -- continuously quoting bid and ask prices across thousands of instruments, earning the [[bid-ask-spread]] while managing inventory risk. See [[market-making-strategy]].
- **Latency arbitrage** -- exploiting tiny price differences that exist for milliseconds between exchanges or related instruments. This is the core of the [[low-latency-trading]] edge.
- **Statistical arbitrage** -- using quantitative models to identify and trade short-lived mispricings between correlated securities.

## Controversy

Michael Lewis's book *Flash Boys* (2014) brought public attention to concerns that HFT creates an uneven playing field, with co-located firms able to anticipate and trade ahead of slower participants ("latency arbitrage" / electronic front-running). Critics argue HFT adds fragility -- it provides "fair-weather" liquidity that withdraws precisely when markets stress, as during the May 6, 2010 [[flash-crash-2010|Flash Crash]] -- and extracts value from long-term investors. Defenders counter that HFT has dramatically tightened [[bid-ask-spread]] widths, improved [[liquidity]], and reduced trading costs for all participants. The IEX exchange (the protagonist of *Flash Boys*) responded with a 350-microsecond "speed bump" designed to neutralise the latency edge.

## Trading Relevance

For a non-HFT trader, the practical takeaways are about **interacting with** the HFT-dominated tape rather than competing on speed:

- **Slippage and adverse selection.** Resting passive orders are picked off by faster participants when news arrives; aggressive marketable orders pay the spread to liquidity that may flicker away. Sizing and order type matter more than ever.
- **Execution algos and dark pools.** Institutions split parent orders into child orders (VWAP/TWAP/POV) and route through dark venues to reduce the footprint that HFT signal-detection can exploit. See [[algorithmic-trading]].
- **Liquidity is conditional.** Displayed depth can vanish in microseconds; the order book looks deeper than it is. This is why flash-crash-style dislocations propagate so fast.
- **Spreads are tight in calm, wide in stress.** HFT compresses costs in normal conditions but is not a committed liquidity provider, so models that assume the calm-state spread underestimate stressed execution cost.

## Related

- [[flash-crashes]] — HFT's role as fragile, fair-weather liquidity provider
- [[flash-crash-2010]] — the canonical example of HFT withdrawal under stress
- [[spoofing]] — manipulation technique often associated with HFT speed
- [[market-manipulation]] — broader manipulation taxonomy
- [[algorithmic-trading]] — HFT as a subset of algo trading
- [[market-maker]] — electronic market making as core HFT strategy
- [[low-latency-trading]] — the speed arms race
- [[co-location]] — physical proximity to exchange matching engines
- [[market-making-strategy]]
- [[book-flash-boys]] — Michael Lewis's investigation into HFT

## Sources

- Lewis, Michael. *Flash Boys: A Wall Street Revolt* (W. W. Norton, 2014).
- Aldridge, Irene. *High-Frequency Trading: A Practical Guide to Algorithmic Strategies and Trading Systems*, 2nd ed. (Wiley, 2013).
- U.S. SEC / CFTC, *Findings Regarding the Market Events of May 6, 2010* (Sept. 30, 2010) — the joint Flash Crash report.
- SEC, *Concept Release on Equity Market Structure* (Release No. 34-61358, 2010) — regulatory framing of HFT.
- Budish, Cramton & Shim, "The High-Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response," *Quarterly Journal of Economics* (2015).

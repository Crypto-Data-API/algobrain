---
title: "Low-Latency Trading"
type: concept
created: 2026-04-06
updated: 2026-04-13
status: good
tags: [infrastructure, hft, latency, market-microstructure]
aliases: ["Latency in Trading", "Low Latency", "Ultra-Low Latency"]
domain: [market-microstructure]
difficulty: advanced
related: ["[[co-location]]", "[[fix-protocol]]", "[[order-management-systems]]", "[[jump-trading]]", "[[jane-street]]", "[[book-algorithmic-and-high-frequency-trading]]", "[[book-high-frequency-trading-aldridge]]", "[[edge-taxonomy]]", "[[latency-arbitrage]]", "[[market-making-strategy]]", "[[information-arbitrage]]", "[[fastest-profitable-trades]]"]
---

# Low-Latency Trading

Low-latency trading is the engineering discipline of building systems that execute trades in microseconds (Source: [[book-high-frequency-trading-aldridge]]). At this scale, every nanosecond of optimization matters — the physics of signal propagation becomes a competitive factor.

## Hardware Stack

**FPGAs (Field-Programmable Gate Arrays)**: Custom logic circuits that process market data and generate orders in hardware, bypassing the CPU entirely. Firms like [[jump-trading]] invest heavily in FPGA development. Latencies: sub-microsecond tick-to-trade.

**Custom NICs**: Network interface cards with hardware timestamping and direct memory access. Solarflare (now Xilinx) and Mellanox are standard choices.

**Kernel bypass**: Technologies like DPDK (Data Plane Development Kit) and Solarflare OpenOnload route network packets directly to userspace, skipping the operating system kernel. This eliminates 10-50us of kernel overhead.

**Zero-copy networking**: Data moves from NIC to application memory without being copied through kernel buffers. Every memory copy adds latency.

## Software Architecture

- **C/C++ only** — Python is 100-1000x too slow; even Java's garbage collector pauses are unacceptable
- **Lock-free data structures** — mutexes and locks cause unpredictable blocking; use atomic operations and compare-and-swap
- **Memory-mapped I/O** — pre-allocate all memory at startup; no dynamic allocation during trading hours
- **Busy-wait loops** — spin on CPU cores rather than sleeping; wastes power but eliminates wake-up latency
- **Cache optimization** — keep hot data in L1/L2 cache; a cache miss costs ~100 nanoseconds

## Latency Budget

| Component | Typical Latency |
|-----------|----------------|
| Exchange matching engine | 10-100 us |
| Network (co-located) | 1-5 us |
| Network (remote) | 50-500 us |
| Strategy logic (FPGA) | 0.1-1 us |
| Strategy logic (C++) | 1-10 us |
| Strategy logic (Python) | 100-10,000 us |

## Network Optimization

[[co-location]] is table stakes. Beyond that:

- **Microwave links**: Electromagnetic signals through air travel faster than light through fiber (~30% faster). Firms build microwave tower networks between exchanges (e.g., Chicago to New Jersey).
- **Direct market access (DMA)**: Connect directly to exchange matching engines, bypassing broker intermediaries
- **Cross-connects**: Physical cable runs within a data center, measured in feet

## Who Needs This

This level of optimization is **only relevant for HFT firms and market makers**. If your strategy holds positions for hours or days, spending millions on latency infrastructure is wasteful. Retail traders should focus on [[cloud-trading-infrastructure]] instead.

The rule of thumb: if your signal decays in less than a second, you need low-latency infrastructure (Source: [[book-algorithmic-and-high-frequency-trading]]). If it decays over minutes or hours, you don't.

## Latency Measurement

How you measure latency determines whether your numbers are meaningful:

- **Tick-to-trade**: time from receiving a market data update to submitting an order to the exchange. The most common benchmark — sub-microsecond for FPGA-based systems
- **Tick-to-ack**: time from market data receipt to receiving the exchange's order acknowledgment. Includes network round-trip
- **Percentile reporting**: mean latency is meaningless; what matters is the 99th or 99.9th percentile (tail latency). A system with 1μs mean but 100μs p99 will lose to a system with 5μs mean and 10μs p99
- **Timestamping**: hardware timestamping (PTP/IEEE 1588) on NICs is essential. Software timestamps add microseconds of jitter

## The Regulatory Landscape

Regulators have responded to the rise of low-latency trading with various measures:

- **Speed bumps**: IEX's 350μs delay on incoming orders, designed to neutralize latency advantages. TSX Alpha also uses a speed bump. The debate: does slowing everyone down help or hurt market quality?
- **Batch auctions**: some venues (EBS in FX, Cboe periodic auctions) batch orders and execute at discrete intervals, eliminating the continuous race to be first
- **MiFID II (EU)**: requires algorithmic trading firms to register, test algorithms, and maintain records. Mandates clock synchronization to 100μs (1μs for HFT)
- **SEC Reg NMS**: the order protection rule inadvertently *encourages* speed by requiring venues to honor the best price across all markets, creating cross-venue arbitrage opportunities that only fast firms can exploit

## Edge Category

In the [[edge-taxonomy]], low-latency trading is the canonical **latency edge**. The edge exists because:

- Only a handful of firms can afford the infrastructure ($10M+ annually)
- Winner-take-all dynamics: the fastest firm captures disproportionate profits from [[latency-arbitrage]] and [[market-making-strategy|market making]]
- The edge decays *very fast* as competitors upgrade — a 100ns advantage today may be worthless in 6 months

For strategies with signal decay measured in minutes or hours, latency infrastructure is irrelevant. See the decay table in [[edge-taxonomy#Edge Decay Patterns]].

## Sources

- [[book-algorithmic-and-high-frequency-trading]] — Cartea et al. (2015) cover the mathematical foundations of optimal execution in low-latency environments, including signal decay analysis and latency-sensitive strategy design
- [[book-high-frequency-trading-aldridge]] — Aldridge (2013) provides detailed coverage of HFT infrastructure, including FPGA hardware, kernel bypass, tick data processing, and latency measurement methodologies

## See Also

- [[co-location]] — physical proximity to exchanges
- [[jump-trading]] — a firm known for extreme latency optimization
- [[fix-protocol]] — the messaging standard these systems use
- [[latency-arbitrage]] — the strategy most dependent on low latency
- [[market-making-strategy]] — electronic market making requires competitive latency
- [[edge-taxonomy]] — latency as one of six edge categories

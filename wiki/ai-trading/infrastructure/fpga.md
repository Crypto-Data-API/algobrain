---
title: "FPGA (Field-Programmable Gate Array)"
type: concept
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [technology, market-microstructure, high-frequency-trading, latency]
aliases: ["FPGA", "Field-Programmable Gate Array", "FPGAs"]
domain: [market-microstructure]
related:
  - "[[low-latency-trading]]"
  - "[[high-frequency-trading]]"
  - "[[latency]]"
  - "[[fix-protocol]]"
  - "[[cloud-trading-infrastructure]]"
  - "[[market-microstructure]]"
---

An FPGA (Field-Programmable Gate Array) is a reconfigurable silicon chip whose logic gates can be wired in hardware to implement a custom digital circuit. In trading, FPGAs are the workhorse of the lowest-latency tier: market-data parsing, risk checks, and order generation are implemented directly in hardware so that a price update can turn into an order in **tens to low-hundreds of nanoseconds**, far faster than software running on a CPU.

## How It Works

A CPU executes instructions sequentially against a general-purpose architecture; an FPGA is configured (via a hardware description language such as Verilog or VHDL) into a dedicated pipeline that does exactly one job. Because the logic is physically laid out in gates rather than fetched and decoded as software, an FPGA can:

- **Parse exchange feeds in-line** — decode Nasdaq ITCH or CME MDP 3.0 packets as bytes arrive off the wire (often straight from the network MAC), with deterministic, jitter-free latency.
- **Maintain an order book in hardware** and compute simple signals (e.g., top-of-book change, imbalance).
- **Run pre-trade risk checks** (fat-finger limits, position caps) required by regulation, in nanoseconds rather than the microseconds a software check costs.
- **Emit orders** directly to the exchange NIC ("tick-to-trade" wholly on the FPGA).

The trade-off is rigidity: changing FPGA logic means re-synthesizing and re-deploying a bitstream, a far slower development loop than editing software. So firms typically keep complex/changing logic in software (CPU) and push only the latency-critical hot path to the FPGA.

## Trading Relevance

FPGAs sit at the apex of the [[low-latency-trading]] stack and are essential infrastructure for the fastest [[high-frequency-trading]] strategies:

- **Latency arbitrage / market making** — being first to react to a price change wins the queue and avoids adverse selection; nanoseconds of [[latency]] edge translate directly into fill rates and P&L.
- **Exchange-mandated risk gates** — regulators require pre-trade risk controls; FPGAs let firms meet them without giving up speed.
- **Co-location** — FPGA NICs (e.g., from AMD/Xilinx, Intel/Altera, and vendors like Exablaze/Cisco Nexus SmartNICs) are deployed in [[cloud-trading-infrastructure|co-located cages]] inside exchange data centers.

For the vast majority of traders — retail, swing, and even most systematic funds — FPGAs are irrelevant: their alpha lives on horizons of seconds to days where software latency is immaterial. FPGAs matter only where the edge *is* speed. Understanding them clarifies why certain strategies (sub-millisecond latency arb) are structurally inaccessible without seven-figure infrastructure budgets.

## Alternatives in the Latency Stack

- **Kernel-bypass software** (Solarflare/Onload, DPDK) — microsecond-class, far cheaper and more flexible than FPGAs; the standard tier just below.
- **ASICs** — even faster and lower-power than FPGAs but non-reconfigurable and enormously expensive to fabricate; rare in trading.
- **GPUs** — high throughput, high latency; used for model training and batch analytics, not the order hot path.

## Related

- [[low-latency-trading]] — the broader latency-minimization discipline
- [[high-frequency-trading]] — the strategies FPGAs enable
- [[latency]] — the resource FPGAs optimize
- [[fix-protocol]] — higher-latency messaging FPGAs bypass for raw binary feeds
- [[cloud-trading-infrastructure]] — co-location vs. cloud trade-offs
- [[market-microstructure]] — the domain where nanoseconds matter

## Sources

- General knowledge of FPGA architecture and HFT infrastructure; vendor documentation (AMD/Xilinx, Intel/Altera FPGA NICs). No raw sources ingested yet.

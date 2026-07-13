---
title: Co-Location
type: concept
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [infrastructure, hft]
related: ["[[low-latency-trading]]", "[[fix-protocol]]", "[[jump-trading]]", "[[jane-street]]", "[[two-sigma]]", "[[book-high-frequency-trading-aldridge]]", "[[book-algorithmic-and-high-frequency-trading]]"]
---

# Co-Location

Co-location (co-lo) means placing your trading servers physically inside the same data center as the exchange's matching engine (Source: [[book-high-frequency-trading-aldridge]]). When speed-of-light latency matters, physical distance is the ultimate bottleneck.

## Why Distance Matters

Light through fiber optic cable travels at roughly **200,000 km/s** (about two-thirds the speed of light in vacuum). That translates to approximately **8 microseconds per mile** of fiber. A round trip from Manhattan to Chicago (800 miles) takes around 13 milliseconds — an eternity in [[low-latency-trading]].

By co-locating, you reduce network latency to the length of a cross-connect cable within the data center: typically **1-5 microseconds** round trip. That gives roughly a **100 microsecond advantage** over a connection from even a few miles away.

## Major Co-Location Facilities

| Facility | Exchange | Location |
|----------|----------|----------|
| Equinix NY5 | NYSE, NASDAQ | Secaucus, New Jersey |
| Aurora (CME) | CME Group | Aurora, Illinois |
| Equinix LD4 | LSE, ICE Futures | Slough, London |
| Equinix TY3 | JPX (Tokyo Stock Exchange) | Tokyo, Japan |
| Equinix SG1 | SGX | Singapore |

## What You Get

A co-location agreement typically includes:

- **Rack space**: Physical cabinet space for your servers (42U standard rack)
- **Power**: Redundant power feeds, often metered per kW
- **Cross-connects**: Direct fiber runs to the exchange feed handler and order gateway
- **Network**: Connectivity to other co-located participants
- **Physical security**: Biometric access, 24/7 surveillance, mantraps

## Cost

Co-location is expensive:

- **Rack rental**: $5,000-$50,000/month depending on facility and rack size
- **Cross-connects**: $200-$500/month per connection
- **Power**: $100-$300/month per kW
- **Network bandwidth**: Additional monthly fees
- **Hardware**: Your own servers, switches, and NICs — $50K-$500K upfront

Total cost for a competitive HFT setup: **$100K-$1M+ annually** before you even build the trading system.

## Who Needs Co-Location

**Essential for**: HFT firms, market makers, statistical arbitrage with sub-second holding periods, exchange-level latency arbitrage (Source: [[book-algorithmic-and-high-frequency-trading]])

**Irrelevant for**: Swing traders, position traders, retail investors, strategies with holding periods measured in hours or longer

If your [[backtesting]] shows that adding 10 milliseconds of latency doesn't change your strategy's performance, you don't need co-lo. Use [[cloud-trading-infrastructure]] instead.

## Cross-Connects

The most critical piece is the **cross-connect** — a dedicated fiber cable running directly from your rack to the exchange's infrastructure within the same facility. This eliminates routing through switches and routers, providing the lowest possible latency path to the matching engine.

Exchanges typically offer both **market data feeds** (prices, order book) and **order entry gateways** (submit/cancel orders) as separate cross-connect endpoints.

## Sources

- [[book-high-frequency-trading-aldridge]] — Aldridge (2013) covers co-location infrastructure, costs, and the competitive dynamics of physical proximity to exchange matching engines
- [[book-algorithmic-and-high-frequency-trading]] — Cartea et al. (2015) discuss co-location within the broader context of optimal execution and the economics of latency advantages

## See Also

- [[low-latency-trading]] — the broader engineering discipline
- [[fix-protocol]] — what your co-located servers speak
- [[cloud-trading-infrastructure]] — the alternative for non-HFT strategies

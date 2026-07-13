---
title: "Latency Arbitrage"
type: strategy
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [arbitrage, latency, hft, co-location, fpga, microwave, market-making, speed, equities]
aliases: ["Latency Arb", "Speed Arbitrage", "HFT Arbitrage"]
strategy_type: algorithmic
timeframe: scalp
markets: [stocks, futures]
complexity: advanced
backtest_status: untested
related: ["[[low-latency-trading]]", "[[co-location]]", "[[high-frequency-trading]]", "[[cross-exchange-arbitrage]]", "[[market-microstructure]]", "[[information-arbitrage]]", "[[fastest-profitable-trades]]"]
---

# Latency Arbitrage

## Overview

Latency arbitrage exploits microsecond speed advantages to trade on price discrepancies across venues before slower participants can react. When a price changes on one exchange, there is a brief window -- measured in microseconds to low milliseconds -- before that information propagates to other exchanges. The fastest trader detects the stale quote on the slower venue and trades against it, capturing a near-certain profit.

This strategy accounts for an estimated 30-50% of equity market volume in the US and is dominated by a small number of [[high-frequency-trading]] firms (Citadel Securities, Virtu Financial, Jump Trading, Tower Research). It requires extraordinary infrastructure: [[co-location]] at exchange data centers ($5,000-$50,000/month), FPGA or ASIC hardware for sub-microsecond processing, and microwave or laser transmission links between exchange locations. The IEX exchange was created specifically with a 350-microsecond speed bump to counter latency arbitrage and protect slower participants.

## How It Works

The core mechanism is simple: information travels at finite speed, and exchanges are physically separated. When a large buy order lifts the offer on the NYSE, the new higher price is observable at NYSE's data center before it arrives at Nasdaq's data center (even via the fastest possible link). A latency arbitrageur co-located at NYSE detects the price change, transmits an order to Nasdaq via private microwave link (faster than the public fiber SIP feed), and buys at the stale, lower price on Nasdaq before the quote updates.

The infrastructure stack typically includes:
- **Co-location:** Servers physically located in the same building as the exchange matching engine, minimizing network hops.
- **FPGA/ASIC processing:** Field-programmable gate arrays process market data and generate orders in nanoseconds, bypassing software latency entirely.
- **Microwave/millimeter-wave links:** Private point-to-point wireless links between Chicago (CME) and New Jersey (NYSE/Nasdaq) transmit data ~40% faster than fiber optic cable.
- **Direct market access (DMA):** Bypassing broker intermediaries for direct connection to the exchange matching engine.

## Entry/Exit Rules

### Entry
1. **Detect a price change** on Exchange A via the direct data feed.
2. **Calculate the expected stale price** on Exchange B based on latency models.
3. **Send an order to Exchange B** via the fastest available link before the quote updates.
4. **Trade against the stale quote** -- buy if the price is about to rise, sell if about to fall.

### Exit
1. **Immediate exit:** The position is typically held for microseconds to milliseconds. Once the price on Exchange B updates to reflect the new information, sell at the new price.
2. **Flat by design:** Latency arb positions are designed to be round-tripped almost instantly. Inventory should be near zero at all times.
3. **Risk limits:** If the market moves adversely (unexpected reversal), automated systems flatten the position immediately.

## Example Trade

**Setup:** AAPL is quoted at $195.20 bid / $195.22 ask on NYSE. A large buy order lifts the NYSE ask to $195.25.

1. **Detect** the NYSE price change at co-located server: latency ~5 microseconds.
2. **Transmit** order to Nasdaq via private microwave link: latency ~8 milliseconds (vs. ~14ms for public SIP feed).
3. **Buy 5,000 shares of AAPL** on Nasdaq at $195.22 (the stale ask, which has not yet updated).
4. **Nasdaq quote updates** to $195.25 within ~6 milliseconds as the public feed catches up.
5. **Sell 5,000 shares** at $195.25 on Nasdaq.
6. **Gross profit:** ($195.25 - $195.22) x 5,000 = **$150**.
7. **Fees:** Exchange rebate (maker) offsets taker fee. Net fee ~$5.
8. **Net profit:** ~$145 in ~15 milliseconds. Repeated thousands of times per day across hundreds of symbols.

## Risk Management

- **Technology failure:** Hardware or network outages can leave positions unhedged. Redundant systems and kill switches are mandatory.
- **Adverse selection:** When a latency arb trade fills, it could indicate the other side has even faster information. Strict loss limits per trade.
- **Regulatory risk:** Regulators globally are scrutinizing latency arbitrage. The SEC, [[sec|MiFID II]], and other bodies have proposed speed bumps and batch auctions.
- **Arms race economics:** Infrastructure costs escalate continuously. A firm that falls behind by even microseconds loses all profitability.
- **Capital requirements:** While individual trade sizes are small, the aggregate position and margin requirements demand significant capital.
- **[[slippage]] and partial fills:** Stale quotes may have limited depth; the order may only partially fill at the target price.

## Advantages
- **Near-certain profit per trade** when speed advantage is maintained
- **Market-neutral** -- positions are held for microseconds with no directional bias
- **High Sharpe ratio** -- win rates above 95% are common for the fastest firms
- **Scales with technology investment** -- faster infrastructure directly equals more captured opportunities
- **Enormous addressable market** -- operates across every listed equity and futures contract

## Disadvantages
- **Prohibitive entry cost** -- infrastructure costs run $10M+ annually for competitive firms
- **Winner-take-all dynamics** -- only the single fastest firm on a given route captures the arb; second place earns nothing
- **Socially controversial** -- critics argue it taxes slower investors and adds no economic value
- **Regulatory headwinds** -- speed bumps (IEX), batch auctions (proposed), and transaction taxes threaten the strategy
- **Diminishing returns** -- as speeds approach physical limits (speed of light), incremental improvements yield smaller advantages
- **Talent scarcity** -- requires rare expertise in FPGA engineering, network physics, and ultra-low-latency software

## Real-World Examples
- **IEX speed bump:** Brad Katz and the IEX team (chronicled in Michael Lewis's *Flash Boys*) introduced a 350-microsecond delay specifically to neutralize latency arbitrage, arguing it harmed long-term investors.
- **Spread Networks (2010):** Invested $300M to build a straighter fiber-optic cable between Chicago and New Jersey, cutting latency by 3 milliseconds. The advantage lasted until competitors built microwave networks that were even faster.
- **Jump Trading microwave towers:** Jump purchased a decommissioned military tower in Belgium to shave microseconds off the London-Frankfurt latency path for Eurex-LSE arbitrage.

## See Also
- [[high-frequency-trading]] -- the broader category that includes latency arbitrage
- [[co-location]] -- physical proximity to exchange servers, essential for this strategy
- [[low-latency-trading]] -- the technology stack that enables microsecond execution
- [[market-microstructure]] -- the academic study of how exchange mechanics create arb opportunities
- [[cross-exchange-arbitrage]] -- a related strategy that operates at slower timescales

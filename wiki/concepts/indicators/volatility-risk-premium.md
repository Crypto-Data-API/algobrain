---
title: "Volatility Risk Premium"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [volatility, options, quantitative]
aliases: ["VRP", "Vol Risk Premium"]
related: ["[[implied-volatility]]", "[[realized-volatility]]", "[[vix]]", "[[options-selling]]", "[[iron-condor]]", "[[short-straddle]]"]
domain: [volatility, options]
difficulty: advanced
---

The **volatility risk premium** (VRP) is the persistent tendency for [[implied-volatility]] to exceed [[realized-volatility]] on average. Options buyers systematically overpay for protection, and options sellers collect this premium as compensation for bearing the risk of large, sudden market moves. The VRP is one of the most well-documented risk premia in financial markets and forms the foundation of systematic options income strategies.

## Overview

The VRP exists because market participants are willing to pay a premium for insurance against adverse price movements, much like homeowners overpay for fire insurance relative to expected losses. The [[vix|VIX]] (implied volatility) has historically averaged around 19-20%, while the S&P 500's [[realized-volatility]] has averaged roughly 15-16%. This gap of approximately 3-5 percentage points (annualized) represents the VRP.

Studies consistently show that the VRP is positive roughly 80-85% of the time. However, it turns sharply negative during market crises when realized moves exceed what was priced in -- these are the moments when options sellers face catastrophic losses. The VRP is therefore not "free money" but compensation for absorbing [[tail-risk|tail risk]].

## How It Works

**Measuring the VRP:**

The simplest VRP measure is: VRP = IV - RV (forward-looking)

In practice, the VRP is measured retrospectively:
- At time t, observe 30-day IV (e.g., [[vix|VIX]] level)
- 30 days later, calculate the realized volatility over that period
- VRP = IV_t - RV_{t to t+30}

**Why Does the VRP Exist?**

Several factors sustain the premium:
1. **Risk aversion** -- investors are more sensitive to losses than gains, so they pay up for downside protection
2. **Hedging demand** -- institutional portfolio managers systematically buy [[put-options|puts]] as insurance, driving up IV
3. **Leverage constraints** -- selling naked options requires significant margin; not all market participants can supply volatility
4. **Jump risk** -- implied volatility prices in the possibility of rare, large moves ([[black-swan|black swans]]) that may not appear in recent RV history

**VRP by Market Regime:**

| Regime | VRP Behavior | Strategy Implication |
|--------|-------------|---------------------|
| Low vol, trending | Large positive VRP | Best environment for selling premium |
| Normal vol | Moderate positive VRP | Standard premium selling profitable |
| Elevated vol | Small or variable VRP | Be selective, reduce size |
| Crisis / crash | Sharply negative VRP | RV exceeds IV; sellers face losses |

## Trading Applications

**Harvesting the VRP:** The most common approach is systematically selling options to collect the premium:

- **Selling [[short-straddle|straddles]] or [[short-strangle|strangles]]** on indices or individual stocks
- **[[iron-condor|Iron condors]]** -- defined-risk version that caps potential losses
- **Covered calls** or cash-secured puts -- lower-risk variants
- **Selling VIX futures or puts** -- direct volatility exposure

**Practitioner Approach:** Professional premium sellers emphasize selling options when the VRP is elevated, using the IV/RV ratio as a primary filter. When the ratio exceeds 1.2-1.3, the odds favor premium sellers. When it collapses near 1.0 or below, the edge disappears and sellers should reduce exposure. (Source: [[book-option-volatility-and-pricing]])

**Risk Management is Critical:** The VRP's positive average return masks the extreme left-tail risk. Unhedged premium selling strategies can lose months or years of gains in a single event. Successful VRP harvesting requires:
- [[position-sizing|Position sizing]] that survives tail events
- Defined-risk structures (spreads rather than naked options)
- Scaling down when VRP compresses or VIX term structure inverts
- Discipline to accept small, frequent gains and rare large losses

**Institutional Scale:** Many hedge funds, pension funds, and insurance companies systematically harvest the VRP. This institutional participation has compressed the premium over time but has not eliminated it, because the demand for insurance is structural.

## Related

- [[implied-volatility]] -- the "ask" side of the premium
- [[realized-volatility]] -- the "reality" against which IV is compared
- [[vix]] -- the most visible measure of IV, and proxy for the VRP
- [[options-selling]] -- the primary method of harvesting the VRP
- [[iron-condor]] -- a defined-risk structure for VRP capture
- [[tail-risk]] -- the risk that makes the VRP necessary

## Sources

- (Source: [[book-option-volatility-and-pricing]]) -- foundational treatment of the relationship between implied and realized volatility and the economic rationale for premium selling

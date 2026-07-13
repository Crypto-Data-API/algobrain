---
title: "CPPI (Constant Proportion Portfolio Insurance)"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [cppi, portfolio-insurance, dynamic-allocation, risk-management, floor, drawdown-protection, quantitative]
aliases: ["Constant Proportion Portfolio Insurance", "CPPI Strategy", "Portfolio Insurance"]
strategy_type: quantitative
timeframe: position
markets: [stocks, bonds, crypto]
complexity: intermediate
backtest_status: untested
related: ["[[risk-budgeting]]", "[[tail-risk-hedging]]", "[[black-litterman]]", "[[position-sizing]]", "[[regime-detection]]"]
---

# CPPI (Constant Proportion Portfolio Insurance)

## Overview

Constant Proportion Portfolio Insurance (CPPI) is a dynamic asset allocation strategy that provides **downside protection** while maintaining upside participation. It guarantees a minimum portfolio value (the **floor**) by systematically shifting between a risky asset (stocks, crypto) and a safe asset (bonds, cash) based on how far the portfolio is above the floor. When the portfolio is well above the floor, CPPI allocates aggressively to the risky asset. As the portfolio approaches the floor, it de-risks, shifting toward the safe asset.

Developed by Fischer Black and Robert Jones in 1987, CPPI was designed as an alternative to option-based portfolio insurance (which failed catastrophically in the 1987 crash due to liquidity constraints). Unlike options-based approaches, CPPI requires no derivatives -- it is purely a rebalancing rule applied to the two assets.

The mechanism is simple and elegant. The **cushion** is the difference between the current portfolio value and the floor: Cushion = Portfolio - Floor. The allocation to the risky asset is: **Risky Allocation = Multiplier x Cushion**. The multiplier (typically 3-5) determines how aggressively the strategy invests in the risky asset. A higher multiplier means more upside participation but faster de-risking during drawdowns. The remainder goes to the safe asset. As the portfolio rises, the cushion grows, and risky allocation increases (a ratchet-up effect). As the portfolio falls, the cushion shrinks, and risky allocation decreases (automatic de-risking).

## How It Works

**Core formula:** Risky Allocation = m x (V - F)

Where:
- **m** = multiplier (typically 3-5, set by the investor's risk tolerance)
- **V** = current portfolio value
- **F** = floor value (the minimum guaranteed amount, can be fixed or growing at the risk-free rate)
- **(V - F)** = cushion

**Safe Allocation** = V - Risky Allocation = V - m x (V - F)

**Key dynamics:**
- When V >> F: cushion is large, risky allocation is high. The portfolio behaves like a leveraged equity portfolio if the multiplier allows allocation > 100%.
- When V approaches F: cushion approaches zero, risky allocation approaches zero. The portfolio is almost entirely in the safe asset, protecting the floor.
- When V = F: risky allocation = 0. The portfolio is 100% safe assets, locked at the floor. This is the **cash lock** scenario -- the portfolio can no longer recover because it has no risky exposure.

**Rebalancing frequency:** Daily or when the portfolio drifts by more than a threshold (e.g., 5% deviation from target allocation). More frequent rebalancing provides better floor protection but incurs higher transaction costs.

## Rules / Application

### Setup
1. Define the **floor (F):** Typically 80-90% of the initial portfolio value. For a $100K portfolio with 80% floor, F = $80K.
2. Choose the **multiplier (m):** 3 for conservative, 5 for aggressive. Higher m = more upside but faster cash-lock risk.
3. Choose **risky asset** (S&P 500 ETF, BTC) and **safe asset** (Treasury bills, short-term bonds, stablecoins).
4. Calculate initial allocation: Cushion = $100K - $80K = $20K. Risky = 5 x $20K = $100K (100% risky at start with m=5).

### Rebalancing Rules
1. Rebalance daily or when risky allocation deviates by more than 5% from the CPPI target.
2. Recalculate: Cushion = V_current - F. Risky = m x Cushion. Safe = V_current - Risky.
3. **Cap risky allocation at 100%** (or at a leverage limit if leverage is permitted).
4. If Cushion <= 0 (portfolio hits the floor), move 100% to safe asset. **Cash lock triggered.**

### Floor Variants
- **Fixed floor:** F stays constant (e.g., $80K). Simple but inflation erodes the real guarantee over time.
- **Rising floor:** F grows at the risk-free rate: F_t = F_0 x e^(r x t). Guarantees real purchasing power.
- **Ratcheting floor:** F is reset upward as the portfolio reaches new highs: F = max(F, 0.9 x portfolio_peak). This locks in gains but makes cash-lock more likely.

## Example

**Setup:** $100K portfolio, 80% floor ($80K), multiplier m=4, S&P 500 ETF (risky), Treasury bills (safe).

1. **Day 0:** Cushion = $100K - $80K = $20K. Risky = 4 x $20K = $80K (80% stocks). Safe = $20K (20% T-bills).
2. **Month 3:** S&P rises 10%. Portfolio = $108K. Cushion = $28K. Risky = 4 x $28K = $112K -- **capped at $108K** (100% stocks). CPPI ratchets up to full equity exposure.
3. **Month 6:** S&P drops 15% from peak. Portfolio = $91.8K. Cushion = $11.8K. Risky = 4 x $11.8K = $47.2K (51% stocks). CPPI has automatically de-risked.
4. **Month 9:** S&P drops another 10%. Portfolio = $86.5K. Cushion = $6.5K. Risky = 4 x $6.5K = $26K (30% stocks). Further de-risking.
5. **Month 12:** S&P recovers 20%. With 30% equity exposure, portfolio rises to $92.4K. Cushion = $12.4K. Risky = $49.6K (54% stocks). Gradually re-risking.
6. **Result:** Portfolio never breached the $80K floor despite a 25% peak-to-trough market drawdown. Final value ($92.4K) lagged a buy-and-hold portfolio ($99K) but avoided the worst of the drawdown.

## Advantages

- **Downside protection:** Guarantees a minimum portfolio value (the floor), providing psychological and financial security
- Simple, rules-based: no forecasting, no subjective judgment -- just a mechanical rebalancing formula
- **Participates in upside:** Unlike fixed allocations or buying puts, CPPI increases risky exposure as the portfolio grows, capturing bull market returns
- No derivatives required (unlike option-based portfolio insurance) -- can be implemented with any two assets
- Natural fit for [[crypto]] portfolios where drawdowns are extreme and investors want floor protection while maintaining BTC/ETH upside
- Flexible: the multiplier and floor can be customized to any risk tolerance
- Integrates well with [[risk-budgeting]] frameworks and institutional mandates with return guarantees

## Disadvantages

- **Cash lock:** If the portfolio hits the floor, risky allocation goes to zero permanently (or until the floor is reset). The portfolio cannot recover even if markets rebound strongly
- **Gap risk:** In a flash crash or overnight gap, the portfolio can breach the floor before rebalancing occurs. The guarantee is only as good as the rebalancing frequency
- **Whipsaw costs:** In volatile, choppy markets, CPPI de-risks on dips and re-risks on rallies, buying high and selling low -- the opposite of [[mean-reversion]]
- The multiplier is a critical parameter with no optimal value -- too high increases cash-lock risk, too low sacrifices upside
- **Underperforms in strong bull markets:** The safe asset allocation creates a drag on returns vs 100% risky asset
- Transaction costs from frequent rebalancing can erode returns, especially in taxable accounts
- Does not protect against **inflation risk** unless the floor is explicitly inflation-adjusted

## See Also

- [[risk-budgeting]] -- broader framework for risk-aware portfolio construction
- [[tail-risk-hedging]] -- an alternative downside protection approach using options
- [[black-litterman]] -- institutional portfolio optimization that can complement CPPI
- [[position-sizing]] -- CPPI is fundamentally a dynamic position sizing rule
- [[regime-detection]] -- can enhance CPPI by adjusting the multiplier based on detected market regime

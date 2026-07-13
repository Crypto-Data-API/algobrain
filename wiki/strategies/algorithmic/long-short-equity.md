---
title: "Long-Short Equity"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [long-short, equity, hedge-fund, market-neutral, alpha, beta-neutral, factor-investing, quantitative]
aliases: ["Long/Short Equity", "L/S Equity", "130/30 Strategy", "Equity Hedge"]
strategy_type: quantitative
timeframe: position
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[factor-investing]]", "[[pairs-trading]]", "[[statistical-arbitrage]]", "[[risk-budgeting]]", "[[portable-alpha]]"]
---

# Long-Short Equity

## Overview

Long-short equity is the classic hedge fund strategy: go **long stocks expected to outperform** and **short stocks expected to underperform**, profiting from the spread in returns between the two books. Unlike a long-only portfolio that rises and falls with the market, a long-short portfolio derives its return from **stock selection alpha** -- the ability to identify which stocks will do better or worse than their peers, regardless of overall market direction.

The strategy was pioneered by Alfred Winslow Jones in 1949 when he created the first hedge fund. His insight was that by holding both long and short positions, he could hedge out market risk (beta) while retaining the return from picking winners and losers. Today, long-short equity is the largest hedge fund strategy by AUM, comprising roughly 25-30% of the industry.

**Market-neutral** variants maintain zero net exposure (equal dollar amounts long and short), isolating pure alpha. **Directional** variants maintain a net long or short bias (e.g., 70% long, 30% short for a net 40% long exposure). The **130/30** variant uses leverage to go 130% long and 30% short, allowing the manager to express negative views without reducing long exposure below 100%. This structure is popular with institutional mandates that require a long-biased framework but want to benefit from short selling.

## How It Works

1. **Alpha Model:** Rank a universe of stocks using a quantitative model or fundamental analysis. The model scores stocks on factors such as [[value-investing-strategy|value]], [[momentum-rotation|momentum]], quality, [[earnings-momentum|earnings revisions]], or a composite multi-factor signal.
2. **Long Book:** Buy the top-ranked stocks (e.g., top decile or quintile). These are expected to outperform.
3. **Short Book:** Sell short the bottom-ranked stocks (e.g., bottom decile). These are expected to underperform.
4. **Hedging:** Adjust gross and net exposure to target the desired beta. Market-neutral = beta ~0. Directional = beta 0.3-0.6 typically.
5. **Risk Management:** Sector-neutralize (equal sector weights in long and short books), factor-neutralize (hedge out unintended factor exposures), and size positions to limit single-stock risk.
6. **Rebalance:** Periodically (weekly, monthly) re-rank the universe and rebalance both books. Turnover depends on the signal frequency.

The return decomposition is: **Portfolio Return = Alpha_long + Alpha_short + Beta * Market_Return + Short_Rebate - Borrow_Costs - Transaction_Costs**.

## Rules / Application

### Portfolio Construction
1. Define a stock universe (e.g., Russell 1000, S&P 500, or a sector-specific universe).
2. Score each stock using the alpha model. Normalize scores to a z-score.
3. **Long allocation:** Top 30-50 stocks, weighted by signal strength or equal-weighted. Target 100% (or 130% for 130/30).
4. **Short allocation:** Bottom 30-50 stocks, weighted by signal strength or equal-weighted. Target 100% for market-neutral, 30% for 130/30.
5. **Sector constraints:** Long and short books should have similar sector weights to avoid unintended sector bets.
6. **Position limits:** Max 3-5% per stock on either side to limit idiosyncratic risk.

### Beta Management
1. Calculate portfolio beta daily using a rolling regression against the market index.
2. If targeting market-neutral: adjust long/short sizing to keep beta within +/- 0.05.
3. Use index futures (e.g., S&P 500 E-mini) to fine-tune residual beta exposure.

### Risk Controls
1. **Gross exposure** (long% + short%) typically 150-250%. Higher gross = more alpha opportunity but more risk.
2. **Net exposure** (long% - short%) reflects directional bias. Market-neutral = 0%. Directional = 20-60%.
3. **Maximum drawdown stop:** If the portfolio draws down more than 10-15%, reduce gross exposure.
4. Monitor **factor exposures** (value, momentum, size, volatility) to ensure the portfolio is not inadvertently loading on a single factor.

## Example

**Setup:** Quantitative long-short equity fund, Russell 1000 universe, multi-factor alpha model.

1. Alpha model scores all 1000 stocks monthly on value (P/E, P/B), momentum (12-1 month return), quality (ROE, debt/equity), and earnings revisions.
2. **Long book:** Top 50 stocks, equal-weighted at 2% each = 100% long. Stocks include high-quality value names with positive earnings revisions.
3. **Short book:** Bottom 50 stocks, equal-weighted at 2% each = 100% short. Stocks include expensive, low-quality names with negative revisions.
4. Portfolio beta: -0.03 (approximately market-neutral).
5. **Month results:** Market falls 4%. Long book falls 2% (alpha: +2% vs market). Short book falls 6% (alpha: +2% from shorts).
6. **Portfolio return:** -2% (longs) + 6% (short profits) = **+4%** in a down market. Pure alpha, no beta.

## Advantages

- **Alpha from both directions:** Profits from identifying both winners and losers, doubling the opportunity set vs long-only
- **Market-neutral option:** Can eliminate systematic market risk, producing returns uncorrelated to indices -- highly valued by [[risk-budgeting|risk-budget]] allocators
- Flexible: Can adjust net exposure based on market outlook (increase longs in bull markets, increase shorts in bear markets)
- The 130/30 variant allows institutional investors to benefit from shorting within a long-only benchmark framework
- Natural fit for [[factor-investing]] -- long-short is the purest expression of factor returns
- Deep academic and industry infrastructure: tools, data, and talent are widely available

## Disadvantages

- **Short selling is hard:** Borrow costs (1-10%+ annualized for hard-to-borrow stocks), short squeeze risk, regulatory restrictions (uptick rules, bans), and unlimited theoretical loss
- **Alpha is scarce:** The spread between long and short book returns (the "long-short spread") has compressed as more capital competes for the same signals
- **Crowding risk:** Popular long-short factors (e.g., momentum, low-vol) are heavily traded, and crowded unwinds can cause severe losses (August 2007 quant crisis)
- High operational complexity: requires prime brokerage, securities lending, margin management, and sophisticated risk systems
- **Leverage amplifies mistakes:** A 200% gross exposure portfolio that picks the wrong stocks loses twice as fast as a long-only portfolio
- Transaction costs erode alpha, especially with high-turnover quantitative signals and in less liquid names
- **Short alpha is harder to generate** than long alpha -- stocks go up over time (equity risk premium), so shorts face a structural headwind

## See Also

- [[factor-investing]] -- the alpha models driving stock selection in long-short portfolios
- [[pairs-trading]] -- a specific long-short implementation focused on paired positions
- [[statistical-arbitrage]] -- systematic, high-turnover variant of long-short equity
- [[portable-alpha]] -- separating the alpha generated by long-short from market beta
- [[risk-budgeting]] -- framework for allocating risk across factors and positions

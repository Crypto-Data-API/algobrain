---
title: "Derisking"
type: concept
created: 2026-04-06
updated: 2026-06-20
status: excellent
tags: [risk-management, portfolio, concepts]
aliases: ["De-risking", "Risk Reduction"]
domain: [risk-management, portfolio-theory]
prerequisites: ["[[risk-management]]", "[[position-sizing]]"]
difficulty: intermediate
related:
  - "[[risk-management]]"
  - "[[position-sizing]]"
  - "[[leverage]]"
  - "[[portfolio-theory]]"
  - "[[stop-loss]]"
  - "[[hedging]]"
  - "[[drawdown]]"
  - "[[drawdown-management]]"
  - "[[maximum-drawdown]]"
  - "[[correlation]]"
  - "[[volatility]]"
  - "[[vix]]"
  - "[[derisking]]"
  - "[[risk-off]]"
  - "[[crisis-alpha]]"
  - "[[cash-as-asset]]"
---

# Derisking

**Derisking** is the process of reducing a portfolio's exposure to risk, typically by selling positions, reducing [[leverage]], increasing hedges, or moving capital into safer assets. It is a deliberate defensive action taken when market conditions deteriorate, uncertainty increases, or a trader's maximum drawdown tolerance is approached.

Derisking is not failure -- it is the [[risk-management]] discipline that enables long-term survival. The best traders preserve capital during adverse conditions so they can deploy it aggressively when opportunities arise. It is the operational counterpart of [[position-sizing]]: where sizing sets how much risk to take *before* a trade, derisking governs how to *shed* risk once it is on and conditions deteriorate.

## The Mechanics: Why Derisking Works Mathematically

Derisking is rooted in two unforgiving arithmetic facts that make capital preservation the dominant objective.

### Drawdown asymmetry (the recovery problem)

The gain required to recover from a loss grows faster than the loss itself, because the recovery is computed off a smaller base. This is the single most important reason to cut risk before a drawdown deepens.

| Drawdown | Gain required to recover |
|----------|--------------------------|
| -10% | +11% |
| -20% | +25% |
| -30% | +43% |
| -50% | +100% |
| -75% | +300% |
| -90% | +900% |

The formula is `recovery = 1/(1 - drawdown) - 1`. A trader who derisks at -10% and stops the bleed needs an 11% recovery; one who rides it to -50% needs to double their remaining capital just to get back to even. See [[drawdown]] and [[maximum-drawdown]].

### Volatility drag and the ergodicity argument

For a sequence of returns, the *compound* (geometric) growth rate is lower than the *average* (arithmetic) return by approximately half the variance: `g ≈ μ − σ²/2`. Higher volatility mechanically erodes compounded wealth even at the same average return. Derisking — cutting exposure when realized [[volatility]] spikes — directly attacks the `σ²` term, raising the long-run geometric growth rate. This is the [[ergodicity|ergodicity]] argument for risk reduction: the time-average outcome of a single trader's capital path is dominated by avoiding large drawdowns, not by maximizing expected return per trade.

### Volatility targeting (the continuous version of derisking)

The systematic expression of derisking is volatility targeting: scale position size inversely to current realized volatility so that the *risk contribution* of a position stays constant.

```
target_exposure = (target_vol / realized_vol) * base_exposure
```

When realized vol doubles, exposure is halved automatically. This converts derisking from a discrete, emotional decision into a continuous, mechanical one — and is the engine behind the [[risk-parity]] funds discussed under [[#Institutional Derisking]].

## When to Derisk

### Drawdown Thresholds

The most mechanical trigger for derisking. Pre-define levels at which risk reduction becomes mandatory:

- **10% portfolio drawdown**: Begin reducing position sizes by 25-50%
- **15% drawdown**: Cut all positions to half size or smaller; close highest-risk trades
- **20% drawdown**: Move to largely cash/hedged; only keep highest-conviction positions
- **25%+ drawdown**: Full risk-off; preserve remaining capital for recovery

The specific thresholds depend on strategy type, historical [[maximum-drawdown]], and personal risk tolerance. A systematic trend-following strategy with 30% expected max drawdown would use different thresholds than a mean-reversion strategy with 10% expected max drawdown.

### Regime Change Signals

Market regimes shift, and strategies that work in one regime can fail in another:

- **Trend to range**: Momentum strategies suffer when trends break down
- **Low vol to high vol**: Strategies calibrated to calm markets blow up during [[volatility]] expansions
- **Risk-on to [[risk-off]]**: Broad shift from growth assets to safety assets
- **Liquidity withdrawal**: Central bank tightening, credit spread widening, [[liquidity-risk]] increasing

Indicators of regime change include: [[vix]] crossing above 25-30, yield curve inversion, credit spreads widening, and cross-asset [[correlation]] spikes.

### Correlation Spike

When [[correlation]] between portfolio holdings increases sharply:

- Positions that appeared diversified begin moving in lockstep
- Effective portfolio risk can double or triple even without adding new positions
- A portfolio of 10 "uncorrelated" positions that suddenly correlate at 0.8 behaves like 2-3 positions in terms of risk
- Monitor rolling correlation across holdings; trigger derisking when average pairwise correlation exceeds historical norms

### Volatility Expansion

When [[volatility]] rises beyond normal ranges:

- [[vix]] above 30 indicates significant market stress
- Individual position volatility exceeding 2x its 90-day average
- ATR expansion signaling larger-than-normal daily ranges
- If position sizes were set for normal volatility, they are now too large for the current environment

### Pre-Event Uncertainty

Reduce risk ahead of known high-impact events:

- FOMC rate decisions and press conferences
- CPI, NFP, and other major macro releases
- Earnings announcements for concentrated positions
- Geopolitical events with binary outcomes (elections, referendums, policy decisions)

### Strategy Degradation

When a strategy's performance metrics deteriorate:

- Rolling [[sharpe-ratio|Sharpe ratio]] declining toward zero or negative
- Win rate dropping below historical norms
- Average winner shrinking relative to average loser
- Increasing frequency of maximum adverse excursion
- Signs of [[crowding-risk]]: the edge may be getting arbitraged away

## Derisking Methods

### Reduce Position Sizes

The simplest and most common method:

- Cut all positions by a uniform percentage (e.g., reduce everything by 50%)
- Or selectively reduce the largest, most volatile, or most correlated positions first
- Maintains directional exposure at a lower risk level
- Allows participation if the market recovers

### Hedge with Options

Use options to limit downside while maintaining upside exposure:

- **Buy protective puts**: Pay a premium to cap downside loss at the strike price
- **Buy put spreads**: Lower-cost downside protection with a floor on the protection
- **Buy [[vix]] calls**: Hedge against broad market [[volatility]] spikes (portfolio-level hedge)
- **Collar strategy**: Buy puts funded by selling calls -- zero or low cost, but caps upside

Options hedging is particularly useful when you do not want to liquidate positions (e.g., to avoid tax events or because you believe in the long-term thesis). See [[hedging]] for detailed strategies.

### Hedge with Futures

- Short index futures to reduce market beta without selling individual positions
- Short sector ETF futures to hedge specific exposures
- In crypto: short [[perpetual-futures]] to hedge spot holdings

### Move to Cash

The most aggressive form of derisking:

- Liquidate positions and hold cash (or cash equivalents like T-bills)
- [[cash-as-asset|Cash is an asset class]] -- holding it is a deliberate portfolio decision
- Preserves optionality: cash can be deployed rapidly when conditions improve
- Zero correlation with all other assets

### Tighten Stops

Reduce risk without closing positions by moving [[stop-loss]] levels closer:

- Move stops to breakeven on profitable positions (risk-free trades)
- Tighten trailing stops from 2x ATR to 1x ATR
- Add time-based stops to positions that are stagnating
- Warning: tighter stops in volatile markets increase the probability of being stopped out by noise

### Reduce Leverage

For leveraged strategies, reducing [[leverage]] is the most direct form of derisking:

- In [[perpetual-futures]]: reduce position size or add margin to lower effective leverage
- In margin accounts: reduce margin utilization
- Target: bring leverage below your maximum tolerance level for the current volatility environment

### Methods Compared

| Method | Speed | Cost | Keeps upside? | Best when |
|--------|-------|------|---------------|-----------|
| **Reduce position size** | Fast | Spread + commissions | Partial (reduced) | Default; clear, simple, always available |
| **Buy protective puts** | Fast | High (premium decay) | Yes | You want to keep the thesis but cap the tail; tax-sensitive holdings |
| **Put spreads** | Fast | Medium | Yes (to floor) | Cheaper protection when extreme tail is acceptable |
| **Collar** | Fast | Low/zero | Capped | Free protection if you accept upside cap |
| **Short index futures** | Very fast | Low (financing) | Yes (hedged beta) | Reduce market beta without selling individual names |
| **Buy [[vix]] calls** | Fast | High (theta bleed) | Yes | Portfolio-level convexity against broad vol spikes |
| **Move to cash** | Fast | Spread + tax events | No | Maximum risk reduction; regime clearly adverse |
| **Tighten stops** | Passive | Whipsaw risk | Yes (until stopped) | Locking gains; ambiguous early signals |
| **Reduce leverage** | Fast | Low | Partial | Leveraged books; most direct lever |

The trade-off axis is always the same: faster, cheaper risk reduction (selling, cutting leverage) gives up upside; options-based hedging keeps upside but costs premium and decays. See [[hedging]] for the detailed hedge menu.

## Systematic vs Discretionary Derisking

### Systematic (Rules-Based)

Pre-defined rules that trigger automatically:

- **Drawdown circuit breakers**: "If portfolio drops 10% from peak, cut all positions by 50%"
- **Volatility targeting**: Automatically reduce position sizes when realized [[volatility]] exceeds the target
- **Correlation alerts**: Reduce exposure when average pairwise correlation exceeds 0.6
- **Time-based**: Reduce risk heading into weekends, holidays, or known event windows

**Advantages**: Removes emotion, ensures consistent execution, prevents paralysis during stress. **Disadvantages**: Can trigger at suboptimal times (e.g., derisking at the bottom of a V-shaped recovery).

### Discretionary

Human judgment applied to risk reduction decisions:

- Trader assesses market conditions, news flow, and personal conviction
- Can incorporate qualitative factors that rules cannot capture
- Allows for nuanced responses to novel situations

**Advantages**: Flexibility, can avoid false signals. **Disadvantages**: Vulnerable to [[cognitive-biases|cognitive biases]] -- [[loss-aversion]], [[anchoring]], [[overconfidence]] -- that cause traders to derisk too late or not at all.

### Hybrid Approach (Recommended)

Combine systematic rules with discretionary overlay:

- Hard rules for maximum drawdown limits (non-negotiable)
- Systematic volatility targeting for position sizing
- Discretionary judgment for event-driven and qualitative risks
- Override protocol: discretion can add risk reduction beyond what rules require, but cannot override rules to take more risk

## Derisking Speed: Gradual vs Immediate

### Gradual Derisking

Reduce exposure over days or weeks:

- Avoids market impact from liquidating large positions at once
- Allows time for conditions to improve (false alarm)
- Appropriate when signals are ambiguous or early-stage
- Example: Reduce by 10% per day over five days

### Immediate Derisking

Liquidate or hedge aggressively within hours:

- Appropriate when drawdown limits are breached
- When a clearly adverse regime change is underway (e.g., unexpected central bank action, geopolitical shock)
- When [[liquidity-risk|liquidity]] is at risk of evaporating (get out while you still can)
- Accept worse execution quality in exchange for faster risk reduction

## Institutional Derisking

When large institutions derisk simultaneously, it creates cascading sell pressure that can accelerate market declines:

- **[[long-liquidation]]**: Forced selling begets more selling as margin calls cascade
- **[[deleveraging]]**: Funds reducing leverage sell their most liquid holdings first, distorting relative prices
- **Risk parity unwinds**: When [[volatility]] spikes, [[risk-parity]] funds mechanically sell equities, amplifying the move
- **Redemption-driven selling**: Hedge fund redemptions force liquidation regardless of valuation

Understanding institutional derisking dynamics helps traders anticipate forced selling, identify dislocations, and position for recovery.

## Common Derisking Mistakes

### Derisking Too Late

The most common mistake. By the time a trader decides to reduce risk, the damage is often already done:

- [[loss-aversion]] causes traders to hold losing positions hoping for recovery
- "It will come back" is the most expensive phrase in trading
- Solution: pre-commit to drawdown limits and enforce them systematically

### Re-Entering Too Early

After derisking, traders often rush back in before conditions have stabilized:

- Fear of missing the recovery drives premature re-entry
- Markets often have multiple legs down before bottoming
- Solution: require positive confirmation signals before re-risking (e.g., [[volatility]] returning to normal, correlation normalizing, price reclaiming key levels)

### Derisking the Wrong Positions

Cutting winners to keep losers:

- [[disposition-effect]]: the psychological tendency to sell winners and hold losers
- Traders should derisk the most vulnerable positions first, not the most profitable
- Solution: rank positions by risk contribution, not by P&L, when deciding what to cut

### Uniform Derisking When Selective Is Better

Cutting everything by 50% when only certain positions are problematic:

- Some positions may be natural hedges that should be kept
- Correlated positions should be reduced more aggressively
- Solution: analyze position-level risk contribution before deciding what to cut

### Not Having a Re-Risking Plan

Derisking without a plan for when and how to add risk back:

- Can leave a trader in cash indefinitely, missing the recovery
- Solution: pre-define re-risking criteria (e.g., "re-enter at 25% of normal size when VIX drops below 20 and portfolio drawdown recovers to -5%")

## Worked Example (Illustrative)

> Numbers are hypothetical and chosen only to illustrate the decision flow.

A swing trader runs a $200,000 book of 8 long equity positions, sized at roughly 12.5% each, with a pre-committed maximum drawdown tolerance of 15% and a volatility-targeting rule. The market has been calm for months; realized vol on the book is low and positions are full size.

1. **Signal cluster appears.** Over three sessions: [[vix]] jumps from 14 to 26, the [[vix-term-structure|VIX term structure]] flips toward backwardation, [[high-yield-credit-spreads|HY credit spreads]] widen, and average pairwise [[correlation]] across the 8 holdings rises from ~0.3 to ~0.7. The portfolio's effective diversification has collapsed — 8 "independent" names now behave like ~2-3 (see [[#Correlation Spike]]).
2. **Volatility-targeting fires first (systematic).** Realized vol has roughly doubled, so the `target_vol / realized_vol` rule mechanically halves target exposure. The trader trims each position toward ~6% — no judgment required.
3. **Drawdown check.** The book is down 8% from its peak — inside the 15% hard limit, so the mandatory circuit breaker has not triggered, but the trader is now in the discretionary-overlay zone.
4. **Selective reduction (discretionary overlay).** Rather than cutting uniformly, the trader ranks positions by risk contribution and cuts the most correlated, highest-vol names hardest; a low-beta defensive holding acting as a natural hedge is kept.
5. **Cheap convexity instead of full liquidation.** To avoid realizing gains (tax) on a high-conviction holding, the trader buys a small slug of index puts and a few [[vix]] calls to bring net beta down without selling, per the [[#Methods Compared]] table.
6. **Pre-commit the re-risking plan.** Before finishing, the trader writes the re-entry rule: scale back toward full size only when VIX < 20, term structure returns to contango for 5+ sessions, and average correlation normalizes below 0.5 (see [[#Not Having a Re-Risking Plan]]).

Outcome logic: whether or not the selloff continues, the trader has converted a fragile, fully-correlated, full-size book into a smaller, hedged, optionality-preserving one — and has a written trigger to re-deploy. The regime, not emotion, drove every action. (Compare the regime-aware short-vol de-risking in [[volatility-regime-classification#Worked Example]].)

## Derisking Checklist

1. Are any drawdown thresholds breached? If yes, execute the corresponding reduction immediately
2. Has [[volatility]] expanded beyond 1.5x the 90-day average? If yes, reduce position sizes proportionally
3. Has [[correlation]] between holdings spiked above historical norms? If yes, reduce the most correlated positions
4. Are there major known events in the next 48 hours? If yes, consider pre-event hedges or size reduction
5. Is the strategy's rolling performance degrading? If yes, begin gradual derisking and investigate
6. Is there a clear plan for re-entering risk? If no, define re-risking criteria before completing the derisking

## Related

- [[risk-management]] -- The broader discipline that derisking is part of
- [[risk-management-overview]] -- Comprehensive risk management guide
- [[drawdown]] -- Understanding drawdowns
- [[drawdown-management]] -- Recovering from drawdowns
- [[maximum-drawdown]] -- The worst peak-to-trough decline
- [[hedging]] -- Hedging strategies and techniques
- [[stop-loss]] -- Stop loss strategies
- [[position-sizing]] -- How position size relates to risk
- [[leverage]] -- Managing leverage exposure
- [[volatility]] -- Volatility as a risk measure
- [[vix]] -- The market's "fear gauge"
- [[correlation]] -- How asset co-movement affects portfolio risk
- [[risk-off]] -- Broad market shift to safety assets
- [[crisis-alpha]] -- Strategies that profit during crises
- [[cash-as-asset]] -- Cash as a deliberate portfolio allocation
- [[ergodicity]] -- Why the single-path argument favors capital preservation
- [[risk-parity]] -- Volatility-targeting at the portfolio level
- [[volatility-regime-classification]] -- Regime framework that often drives the derisking decision

## Sources

General market knowledge; no specific wiki source ingested yet. The drawdown-recovery arithmetic and the `g ≈ μ − σ²/2` volatility-drag relationship are standard results in [[portfolio-theory]]; the [[ergodicity]] framing of capital preservation follows the time-average vs ensemble-average distinction discussed under that page.

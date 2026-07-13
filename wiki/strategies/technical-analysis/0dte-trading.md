---
title: "0DTE Options Trading"
type: strategy
created: 2026-04-13
updated: 2026-06-20
status: excellent
tags: [options, day-trading, scalping, gamma, 0dte]
aliases: ["Zero DTE", "0 DTE", "Zero Days to Expiration", "Same-Day Options", "0DTE"]
strategy_type: technical
timeframe: intraday
markets: [stocks, options]
complexity: advanced
backtest_status: untested
edge_source: [structural, behavioral]
edge_mechanism: "Extreme gamma creates non-linear payoffs from small moves; retail participants consistently misprice intraday gamma risk while market makers hedge predictably"
data_required: [ohlcv-1min, options-chain, gamma-exposure]
min_capital_usd: 5000
capacity_usd: 50000000
crowding_risk: high
expected_sharpe: 0.3
expected_max_drawdown: 0.40
breakeven_cost_bps: 50
related: ["[[options]]", "[[gamma]]", "[[theta]]", "[[iron-condor]]", "[[straddle-strangle]]", "[[gamma-scalping]]", "[[second-order-greeks]]", "[[gamma-exposure-trading]]"]
---

0DTE (zero-days-to-expiration) options are contracts that expire on the same trading day they are bought or sold. Since 2022, when the CBOE expanded SPX expirations to every trading day (Monday through Friday), 0DTE has become the dominant force in US options markets — accounting for 40-50% of total SPX options volume. They offer extreme leverage, defined risk, and lottery-ticket-like payoffs that have attracted both sophisticated traders and retail speculators.

## Edge Source

**Structural**: 0DTE options have extreme [[gamma]] that creates non-linear payoffs — small underlying moves produce outsized percentage returns. Market makers who are short these options must hedge aggressively, creating predictable intraday flow patterns ([[gamma-exposure-trading|GEX flows]]) that informed traders can anticipate.

**Behavioral**: Retail participants systematically misprice intraday gamma risk. Buyers treat 0DTE as binary lottery tickets without understanding that [[theta]] decay at this timescale is measured in hours, not days. Sellers underestimate the probability of intraday 2-3 sigma moves.

## Why This Edge Exists

The other side of 0DTE trades consists of:
- **Retail buyers** seeking lottery-ticket leverage who accept negative expected value
- **Market makers** who must provide liquidity and manage gamma dynamically — their hedging flows create exploitable patterns
- **Institutional sellers** who collect theta but face concentrated tail risk (a single large move can wipe out weeks of premium collected)

The edge is narrow and contested. It is not a reliable source of consistent profit for most participants.

## Greeks at 0DTE: Why the Day Is Different

0DTE is not "options with less time" — it is a qualitatively different instrument because [[time-to-expiration]] is measured in hours, pushing every Greek to an extreme (see [[expiration-selection]] for the full DTE spectrum and [[non-linear-payoff]] for the curvature math).

| Greek | 0DTE behavior | Practical consequence |
|---|---|---|
| [[theta]] | Decays intraday, fastest in the morning, near-total by the close | A seller's edge is collected in hours; a buyer bleeds by the minute |
| [[gamma]] | At its absolute maximum, exploding near ATM in the final 1-2 hours | A 0.5% move can take a strike from worthless to 5x; deltas flip violently |
| [[delta]] | Increasingly binary as expiry nears (approaches 0 or 1) | The position behaves like a digital/binary bet by mid-afternoon |
| [[vega]] | Tiny in absolute terms (little time left for IV to matter) | This is a *realized-vol* game, not an *implied-vol* game |
| [[second-order-greeks\|charm]] | Extreme — delta drifts fast purely from time passing | Hedges must be re-struck constantly; "set and forget" is impossible |

The headline: **0DTE trades the [[gamma]]/[[theta]] axis almost exclusively** — vega is negligible because there is no time for IV to play out. A 0DTE short condor is the most concave bet retail can place (maximum negative gamma per dollar of premium); a 0DTE long straddle is the most convex. This is the [[non-linear-payoff]] concept at its sharpest: the [[convexity]] term dominates and the linear delta term is almost irrelevant by the final hour.

## Null Hypothesis

Under random walk assumptions, 0DTE options are fairly priced by the market. Theta collected by sellers equals the expected cost of gamma-driven losses. Any apparent strategy performance is likely explained by variance (a few lucky/unlucky sessions dominate results), bid-ask spread costs, and survivorship bias in published track records.

## Rules

### 0DTE Iron Condor (Premium Selling)

**Entry**:
- Sell [[iron-condor]] on SPX/SPY at market open or after the first 30 minutes
- Short strikes at 10-15 delta (approximately 0.5-1.0% OTM)
- Wings 5-10 points wide (SPX) for defined risk
- Target credit: 20-30% of wing width

**Exit**:
- Close at 50% of max profit (do not hold to expiration)
- Stop loss at 2x credit received
- Close immediately if underlying breaches short strike

**Position sizing**:
- Maximum 2-3% of account per trade
- Never exceed 5 simultaneous 0DTE positions

### 0DTE Straddle/Strangle (Volatility Buying)

**Entry**:
- Buy ATM or near-ATM [[straddle-strangle|straddle]] when expecting a large intraday move
- Best setups: FOMC announcement days, CPI releases, major earnings before open
- Entry immediately before the catalyst

**Exit**:
- Take profit at 50-100% gain (do not get greedy — gamma works both ways)
- Close if the underlying hasn't moved within 1-2 hours (theta is destroying value)
- Never hold losing straddles hoping for a move — the math worsens every hour

### GEX-Informed Directional

**Entry**:
- Use [[gamma-exposure-trading|gamma exposure]] data (SpotGamma, GEX indicators) to identify key levels
- Buy 0DTE calls/puts in the direction of anticipated dealer hedging flow
- Enter when underlying approaches a gamma flip level (from positive to negative GEX)

**Exit**:
- Target the next significant gamma level as profit target
- Tight stop — 50% of premium paid
- Close within 1-2 hours regardless

## Implementation Pseudocode

```python
# 0DTE Iron Condor — simplified decision logic
def zero_dte_condor(chain, underlying_price, account_value):
    # Select expiration = today
    today_chain = chain[chain.expiration == today]
    
    # Find ~10-delta strikes
    short_put = find_strike(today_chain, delta=-0.10, side='put')
    short_call = find_strike(today_chain, delta=0.10, side='call')
    
    # Wings: 5 points wide (SPX)
    long_put = short_put.strike - 5
    long_call = short_call.strike + 5
    
    # Calculate credit
    credit = (short_put.bid + short_call.bid 
              - long_put.ask - long_call.ask)
    max_loss = 5.0 - credit  # wing width minus credit
    
    # Position size: max 2% of account at risk
    max_contracts = int(account_value * 0.02 / (max_loss * 100))
    
    # Require minimum credit/width ratio
    if credit / 5.0 < 0.20:
        return None  # not enough premium
    
    return {
        'contracts': min(max_contracts, 3),
        'profit_target': credit * 0.50,
        'stop_loss': credit * 2.0
    }
```

## Indicators / Data Used

- **[[gamma-exposure-trading|Gamma Exposure (GEX)]]**: Aggregate dealer gamma positioning — positive GEX = market pinning (mean-reverting), negative GEX = momentum amplification
- **Intraday IV levels**: Compare 0DTE IV to intraday realized vol to assess if premium is rich or cheap
- **Volume/open interest**: Unusual concentration at specific strikes indicates potential pin targets
- **[[vix]] intraday**: VIX spikes during the session often correspond to 0DTE-driven flows
- **Time of day**: Gamma effects intensify in the final 2-3 hours; theta decay is fastest in the morning

## Example Trade

**0DTE Iron Condor on SPX (April 10, 2026)**:
- SPX at 5,200 at 10:00 AM
- Sell 5170/5165 put spread (5-wide) for $0.60
- Sell 5230/5235 call spread (5-wide) for $0.55
- Total credit: $1.15 per contract ($115)
- Max loss: $5.00 - $1.15 = $3.85 per contract ($385)
- SPX closes at 5,195 — both spreads expire worthless
- Profit: $115 per contract (full credit retained)
- Trade time: 6 hours. Annualized theta on this structure would be extreme, but any single day can produce max loss.

## Performance Characteristics

| Metric | 0DTE Selling | 0DTE Buying |
|--------|-------------|-------------|
| Win rate | 70-85% (high, but wins are small) | 15-30% (low, but wins can be very large) |
| Avg win/loss ratio | 0.2-0.5x (small wins, large losses) | 2-5x (large wins, small losses) |
| Sharpe (realistic) | 0.2-0.5 (after costs) | -0.5 to 0.3 (high variance) |
| Key risk | Single large loss wipes weeks of gains | Chronic theta bleed |
| Cost sensitivity | Moderate (bid-ask matters) | High (bid-ask is a large % of premium) |

The bid-ask spread on 0DTE options is typically $0.05-$0.20 per leg, which on a $0.50 option represents 10-40% of the premium. Transaction costs are a dominant factor.

## Capacity Limits

0DTE SPX options have enormous liquidity — billions of dollars of notional trade daily. Individual retail traders face no capacity constraints. However, at institutional scale, the predictability of GEX flows diminishes as more participants trade the same signals, and execution quality degrades for large orders near key gamma levels.

## What Kills This Strategy

- **Intraday gap moves**: FOMC decisions, unexpected news, or flash crashes can move SPX 2-3% in minutes, blowing through iron condor wings before any exit is possible
- **Bid-ask spread erosion**: In volatile conditions, market makers widen spreads dramatically — the cost to exit can exceed the premium collected
- **Gamma acceleration**: Near ATM strikes in the final hour, gamma becomes extreme. A position that was safe at 2:00 PM can be in crisis by 3:30 PM
- **Behavioral ruin**: The high win rate of 0DTE selling creates a false sense of mastery. Traders increase size, skip stops, or hold through breaches — then one session destroys them
- **Structural crowding**: As 0DTE selling becomes more popular, premiums compress, reducing the margin of safety. The trade works until too many participants do it.

## Kill Criteria

- Rolling 30-day loss exceeding 15% of allocated capital
- Three consecutive max-loss days
- Bid-ask spread costs exceeding 30% of gross premium collected
- Consistent inability to exit at stop-loss prices (fills significantly worse than theoretical)

## Advantages

- **Defined risk**: Maximum loss is known at entry (for spreads)
- **No overnight risk**: Positions expire same day
- **Capital efficiency**: Small absolute premium controls large notional
- **High frequency of opportunities**: Every trading day is a new setup
- **Theta works fast**: Premium selling collects decay in hours rather than weeks

## Disadvantages

- **Extreme gamma risk**: Small moves produce large P&L swings near expiration
- **Transaction costs**: Bid-ask spreads consume a large percentage of profit
- **Concentration risk**: One bad day can erase many good days (negative skew of returns)
- **Psychological pressure**: Requires real-time monitoring and rapid decisions
- **Market impact debate**: Aggregate 0DTE flows may destabilize intraday markets, creating self-referential feedback loops that are hard to model
- **Regulatory risk**: If regulators conclude that 0DTE trading amplifies systemic risk, restrictions could follow

## The Market Impact Debate

There is active academic and industry debate about whether 0DTE flows amplify or dampen market volatility:

**Amplification argument**: When market makers are short gamma (common in 0DTE), they must buy as the market rises and sell as it falls — a destabilizing positive feedback loop. This can amplify intraday moves and contribute to "0DTE-driven" rallies and selloffs.

**Dampening argument**: When market makers are long gamma, they do the opposite — buy dips and sell rallies — which dampens volatility. Additionally, the sheer volume of 0DTE trading provides liquidity that tightens spreads.

The truth likely depends on aggregate dealer positioning. Services like [[spotgamma|SpotGamma]] track this positioning to determine which regime is dominant on any given day.

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg's treatment of gamma acceleration near expiration
- [[gamma-exposure-trading]] — GEX-based market analysis framework

## Related

- [[options]] — foundational options concepts
- [[gamma]] — the dominant force in 0DTE pricing
- [[theta]] — intraday time decay dynamics
- [[second-order-greeks]] — charm and speed are extreme near expiration
- [[iron-condor]] — the most common 0DTE structure
- [[straddle-strangle]] — 0DTE volatility buying
- [[gamma-exposure-trading]] — dealer hedging flows
- [[gamma-scalping]] — dynamic hedging of gamma positions
- [[spotgamma]] — 0DTE analytics provider
- [[zero-dte-options]] — instrument and market-structure overview
- [[expiration-selection]] — where 0DTE sits on the DTE spectrum
- [[non-linear-payoff]] — gamma/convexity dominance near expiry
- [[convexity]] — the curvature that drives 0DTE P/L
- [[time-to-expiration]] — intraday decay dynamics
- [[options-strategies]] — the broader structure catalog
- [[market-regime]] — positive vs negative GEX regimes

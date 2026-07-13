---
title: "Currency Peg Break Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, forex, history, risk-management, event-driven]
aliases: ["Peg Break Trade", "Broken Peg Trade", "Anti-Peg Speculation", "Central Bank Fade"]
strategy_type: fundamental
timeframe: position
markets: [forex, options]
complexity: advanced
backtest_status: paper-traded
edge_source: [analytical, risk-bearing, structural]
edge_mechanism: "Central banks defending unsustainable pegs must eventually capitulate; the asymmetric payoff (bounded loss if peg holds, unbounded gain if it breaks) rewards traders who correctly identify which pegs are economically indefensible versus those backed by credible institutions."
data_required: [fx-spot, fx-options, reserves-data, balance-of-payments, interest-rates, political-risk]
min_capital_usd: 250000
capacity_usd: 2000000000
crowding_risk: medium
expected_sharpe: 0.6
expected_max_drawdown: 0.25
breakeven_cost_bps: 50
decay_evidence: "Capacity constant across decades; quality of individual opportunities varies with macro regime. EM peg breaks continue to occur regularly."
related: ["[[arbitrage]]", "[[forex]]", "[[macro-trading]]", "[[soros-erm-trade]]", "[[asian-financial-crisis]]", "[[chf-floor-break-2015]]", "[[argentina-peso-crisis]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[volatility-arbitrage]]"]
---

# Currency Peg Break Arbitrage

A **currency peg** is a commitment by a central bank or monetary authority to maintain the exchange rate of its currency within a narrow band against another currency (or basket). Pegs range from soft ranges (the 1992 ERM) to hard currency boards (Argentina 1991-2001, Hong Kong 1983-present) to outright floors (Switzerland 2011-2015). **[[currency-peg-break-arbitrage|Peg break arbitrage]]** is a speculative strategy that takes large short positions against a peg believed to be economically unsustainable, profiting when the central bank eventually capitulates. The payoff is asymmetric: limited loss if the peg holds (the currency can only move to one edge of the band), potentially unlimited gain if it breaks. Despite the name, it is closer to a long-volatility / convexity trade than a textbook [[arbitrage]] — there is no riskless convergence leg, only an asymmetric bet that the [[limits-to-arbitrage]] (here, a central bank's finite reserves and finite political will) eventually bind.

### Anatomy of a peg

| Peg type | Example | Defence mechanism | Typical failure mode |
|----------|---------|-------------------|----------------------|
| Soft band | ERM sterling (1992) | Reserves + rate hikes within a band | Political cost of high rates exceeds benefit |
| Hard currency board | Argentina (1991-2001) | 1:1 convertibility law, full reserve backing | Fiscal/banking crisis breaks convertibility |
| One-sided floor | SNB EUR/CHF ≥ 1.20 (2011-15) | Unlimited *printing* of own currency to buy euros | Balance-sheet/political limit on FX accumulation |
| Credible board | Hong Kong (1983-present) | Massive reserves + rigid currency-board rules | Has *not* failed — the canonical null |

The canonical case is **George Soros's September 1992 trade against the British pound** in the European Exchange Rate Mechanism, which netted Quantum Fund roughly **$1 billion** when the UK exited the ERM on "Black Wednesday." Other landmark episodes include the **1997 Thai baht** break that triggered the Asian Financial Crisis, the **2001-2002 Argentine peso** collapse from the 1:1 USD currency board, and the **15 January 2015 Swiss National Bank floor abandonment** that moved EUR/CHF by nearly 30% in minutes and blew up retail FX brokers (Alpari UK, FXCM nearly bankrupt). A key counter-example is the **Hong Kong Dollar peg**, which has held since 1983 despite repeated speculative attacks, thanks to HKMA's massive reserves and institutional credibility. This strategy lives at the intersection of [[macro-trading]], [[volatility-arbitrage]], and [[risk-management]].

## Edge Source

**Analytical**, **risk-bearing**, and **structural**. Analytical: identifying which pegs are indefensible requires serious macro work on reserves-to-imports ratio, current-account deficit, political resolve, and interest-rate differential. Risk-bearing: taking the other side of a central bank's defense requires tolerance for large negative carry (often 500-2000 bps annualized) while waiting for the break. Structural: once a central bank runs out of reserves or political will, the peg breaks discretely and the payoff is realized in hours rather than months. See [[edge-taxonomy]].

| Edge component | Category | What it rewards | Failure if you lack it |
|----------------|----------|-----------------|------------------------|
| Reserve / BOP / REER analysis | Analytical | Correctly ranking defensible vs indefensible pegs | Shorting Hong Kong-style credible boards forever |
| Carry / decay tolerance | Risk-bearing | Surviving negative carry until the break | Margined out before the move you predicted |
| Convexity at the break | Structural | Option payoff that realises in hours, not months | Using spot/forward and bleeding negative carry |
| Jump-risk mispricing | Behavioral | Buying cheap tail because realised vol is ~0 while peg holds | Paying fair value and netting nothing |

## Why This Edge Exists

Pegs are held in place by central banks willing to burn FX reserves, raise interest rates, and impose capital controls. The counterparty to a peg-break short is effectively the central bank itself, which has an **asymmetric loss function**: it loses credibility if the peg breaks, but it loses real money continuously while defending it. Politicians often instruct central banks to defend pegs past the economically rational exit point (ERM 1992, Argentina 2001). Meanwhile, domestic corporates and consumers under-hedge against peg breaks because "the government says it will hold" -- creating natural liquidity for short positions. See [[behavioral-finance]] on institutional over-commitment.

## Null Hypothesis

Under no-edge conditions, the market forward rate would already price in the probability of a break, and buying out-of-the-money puts on the pegged currency would offer no positive expected value. Empirically, option markets chronically **under-price** jump risk on pegged currencies because realized volatility (while the peg holds) is near zero and standard models extrapolate that forward. The null outcome: you pay negative carry for years, the peg holds, and you lose exactly your premium budget. Hong Kong 1997-present is the textbook null.

## Rules

### Entry

1. **Screen for indefensible pegs** via a checklist:
   - Current-account deficit > 5% of GDP, sustained
   - FX reserves covering < 6 months of imports
   - Real effective exchange rate > 20% overvalued (REER vs 10-year average)
   - Rising political cost of defense (election cycle, public sentiment)
   - Interest-rate differential insufficient to compensate for break risk

   The scorecard (matching the pseudocode below) weights these:

   | Signal | Threshold | Score weight |
   |--------|-----------|--------------|
   | Reserves / monthly imports | < 6 months | 2 |
   | REER overvaluation | > 20% vs 10y avg | 2 |
   | Current-account deficit / GDP | < -5% | 2 |
   | Political stress index | > 0.7 | 1 |
   | **Trade trigger** | **total ≥ 5** | — |
2. **Confirm with market signals**: forward points widening, NDF premiums, credit default swaps on sovereign widening
3. **Size via out-of-the-money puts** on the pegged currency (e.g., 3-month 10% OTM EUR/CHF puts in 2014-2015), not via spot/forward which has large negative carry
4. **Stagger expiries**: ladder options across 3-, 6-, 12-month tenors so you remain in the trade across a long defense
5. **Cap budget** at 1-2% of capital per named peg; never bet more than 5% across correlated pegs (e.g., multiple EM Asian pegs in 1997)

### Exit

1. **Peg breaks**: liquidate options immediately into the jump; intrinsic value usually moves 10-50x in minutes
2. **Peg tightens credibility**: if reserves grow, current-account improves, or political support for peg strengthens, cut position
3. **Option decay**: roll forward before expiry if thesis intact; accept that 50-70% of premium will decay without a break

### Position Sizing

Kelly-style sizing based on estimated break probability and expected payoff. Typical Soros-style position: 3-5% of capital in puts, with expected loss of that full amount and expected gain of 15-40x if the peg breaks within the option window.

## Implementation Pseudocode

```python
def peg_break_screen(country):
    reserves_months_imports = country.reserves / country.monthly_imports
    real_overvaluation = country.reer / country.reer_10y_avg - 1
    current_account_gdp = country.ca_deficit / country.gdp
    political_stress = country.political_risk_index

    score = (
        (reserves_months_imports < 6) * 2 +
        (real_overvaluation > 0.20) * 2 +
        (current_account_gdp < -0.05) * 2 +
        (political_stress > 0.7) * 1
    )
    return score >= 5

def position_sizer(break_prob, option_cost, option_payoff_if_break, capital):
    ev_multiple = break_prob * option_payoff_if_break - (1 - break_prob) * option_cost
    if ev_multiple > 2 * option_cost:
        return min(0.03 * capital, option_cost)  # cap at 3% of capital
    return 0

candidate_pegs = [c for c in all_pegged_currencies if peg_break_screen(c)]
for peg in candidate_pegs:
    size = position_sizer(...)
    buy_otm_puts(peg, tenor=[3m, 6m, 12m], strike=spot * 0.90, notional=size)
```

## Indicators / Data Used

- **FX reserves** (weekly, monthly from central bank releases)
- **Current-account balance** (quarterly BOP data)
- **Real effective exchange rate** (BIS monthly REER series)
- **NDF premium** (non-deliverable forwards) where available — a cleaner signal than on-shore forwards when capital controls exist
- **Sovereign CDS spreads** as a risk proxy
- **FX option implied volatility and risk-reversal skew** — rising put skew signals market stress
- **Political risk indices** (EIU, PRS Group)
- **Short-term interest rate differential** — rising defensive-rate hikes often precede capitulation

## Example Trade

### Soros vs Bank of England, 16 September 1992 (Black Wednesday)

- **Context**: Sterling was in the ERM at a central rate of DM 2.95/GBP with a 6% band. UK inflation running higher than Germany; real pound overvalued ~15%; reserves limited; political cost of defense rising.
- **Position**: Quantum Fund built a **$10 billion short** in sterling via forwards and options in summer 1992, funded by long positions in DM assets.
- **Defense**: BOE raised base rate from 10% to 12% in the morning, announced a planned further hike to 15%, and spent £27 billion of reserves buying sterling.
- **Capitulation**: At 7:30pm local time, Chancellor Norman Lamont announced UK withdrawal from ERM. Sterling fell 15% over the next week.
- **P&L**: Quantum Fund earned approximately **$1 billion** on the trade; Soros's personal reputation as "the man who broke the Bank of England" was made.
- **BOE loss**: estimated at £3.3 billion to UK taxpayers.

### SNB Floor Break, 15 January 2015

- **Context**: SNB had defended a 1.2000 floor in EUR/CHF since September 2011 by buying euros (and expanding reserves to 70%+ of Swiss GDP).
- **Position**: traders long CHF via EUR/CHF puts at strikes 1.1800-1.2000 paid 20-40 bps per month for multi-year tenor. Cost of the trade: small and bounded.
- **Break**: at 10:30 local time on 15 Jan 2015, SNB abandoned the floor without warning. EUR/CHF fell from 1.2010 to an intraday low near 0.8500, a 30% move in ~20 minutes.
- **P&L**: out-of-the-money puts struck at 1.1800 with 3-month tenor moved from ~0.1% of notional to ~15% of notional -- **150x payoff**.
- **Collateral damage**: FXCM required $300M emergency loan, Alpari UK entered insolvency, Everest Capital's Global Fund ($830M) went to zero.

## Performance Characteristics

> **No fabricated backtest.** The numbers below are qualitative practitioner ranges and the convexity arithmetic of *historical* episodes (the ~150x SNB-put figure is an illustrative reconstruction of a deep-OTM put moving from ~0.1% to ~15% of notional, not an audited trade). Expected value is positive *only* if screening is accurate and capital is patient — and the realised distribution is extremely lumpy and right-skewed.

The return profile is the mirror image of selling insurance: many small losses (premium decay while pegs hold) punctuated by rare, very large gains when a peg breaks inside the option window.

| Outcome | Frequency (qualitative) | P&L shape |
|---------|-------------------------|-----------|
| Peg holds through option life | Majority of candidate-cycles | Lose the premium budget (bounded) |
| Peg breaks inside window | Minority | 10-50x premium on the winning leg |
| Whipsaw / overshoot-and-snap-back | Occasional | Puts can still expire worthless despite a brief break |
| Counterparty/broker failure at break | Tail | Win on paper, can't collect (FXCM/Alpari 2015) |

- **Hit rate (qualitative)**: a minority of identified candidate pegs break within a 12-month window; the rest hold or strengthen.
- **Cost discipline**: `breakeven_cost_bps: 50` (frontmatter) — execution and rolling costs are real; staggered OTM puts keep carry bounded versus a spot/forward short.
- **Best conditions**: global tightening cycles, commodity-price shocks for exporters, EM political crises.
- **Worst conditions**: sustained global easing that hands pegged central banks free defensive ammunition; unlimited-printing one-sided floors that can defend for years.

## Capacity Limits

Capacity is enormous for major currencies -- Soros deployed $10B in 1992 and today's global macro funds routinely run positions of similar size. Option-market liquidity in a peg break is actually **enhanced** by the break (dealer desks scramble to unwind), so exits are usually possible. For smaller EM pegs, option markets may not exist or may trade only OTC with tight limits; there capacity is $50-250M per trade.

## What Kills This Strategy

1. **Peg holds**: premium decays to zero. The Hong Kong dollar has absorbed every attack since 1983 because HKMA has >$400B reserves and rigid currency-board mechanics. See [[failure-modes]].
2. **Capital controls**: a central bank can impose them overnight (Malaysia 1998, Argentina 2019, Nigeria 2023), stranding your offshore short.
3. **Option-market seizure**: during crisis, option dealers widen spreads and may refuse new tenors, making rolls impossible.
4. **Whipsaw after break**: currencies sometimes overshoot and snap back, leaving puts that expire worthless despite temporary break.
5. **Regulatory action**: post-1992, many countries passed laws allowing emergency capital controls specifically to deter Soros-style attacks.
6. **Unlimited-defense regimes**: if the pegging central bank can print unlimited currency (as with the SNB buying euros), the defense can persist for years.

## Kill Criteria

- Three consecutive option cycles with no peg break: reduce size 50%
- 12-month rolling realized Sharpe < -0.5: pause strategy
- Regulatory action (new capital controls on short sellers) in target currency
- Option-market liquidity vanishes (bid-ask on 3-month OTM puts > 100% of premium)

## Advantages

- Asymmetric payoff is the textbook definition of a good risk-reward trade
- Bounded downside (option premium) with unbounded upside
- Macro clarity: peg sustainability is often openly debated in policy press long before break
- Works in markets that lack short-selling otherwise (via offshore NDFs and options)
- Creates historical reputation and political influence for successful managers (Soros 1992)

## Disadvantages

- Long periods of premium decay between break events -- requires patient capital and client base that tolerates drawdowns
- Timing is nearly impossible -- you can be right about the break and still lose every option tenor leading up to it
- Political and legal risks: governments have publicly threatened (Malaysia's Mahathir in 1998 famously called Soros a "moron") and occasionally litigated against speculators
- Counterparty risk during a break: your prime broker, option dealer, or retail FX broker may fail (FXCM/Alpari 2015)
- Crowding: when obvious, trade becomes self-defeating as central bank anticipates and defends harder
- Requires sophisticated macro analysis far beyond typical technical signals

## Sources

- George Soros, *The Alchemy of Finance* (1987) and *Soros on Soros* (1995)
- Barry Eichengreen, writings on the ERM and the 1992-93 crises (e.g., *Globalizing Capital*, 1996)
- Paul Blustein, *The Chastening* (2001) — the IMF and the Asian Financial Crisis
- SNB statements and post-mortems of the 15 January 2015 floor abandonment
- Sebastian Mallaby, *More Money Than God* (2010) — Quantum's 1992 sterling trade
- HM Treasury internal estimate of Black Wednesday cost (~£3.3B), released 2005 under Freedom of Information

## Related

- [[arbitrage]] -- parent concept
- [[convergence-arbitrage]] -- the convergence-trade family this strategy borrows option mechanics from
- [[limits-to-arbitrage]] -- the central bank's finite reserves/will are the binding limit here
- [[forex]] -- market context
- [[macro-trading]] -- parent discipline
- [[soros-erm-trade]] -- canonical historical example
- [[asian-financial-crisis]] -- multi-peg cascade
- [[chf-floor-break-2015]] -- modern extreme
- [[argentina-peso-crisis]] -- currency-board failure
- [[volatility-arbitrage]] -- related construction via options
- [[behavioral-finance]] -- institutional over-commitment to a peg
- [[edge-taxonomy]], [[failure-modes]] -- methodology
- [[risk-management]] -- essential discipline

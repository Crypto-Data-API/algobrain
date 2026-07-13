---
title: "Trade Repair and Rolling"
type: concept
created: 2026-04-07
updated: 2026-06-20
status: excellent
tags: [risk-management, options, trade-management, itpm, portfolio-management]
aliases: ["Rolling Trades", "Trade Repair", "Position Repair", "Rolling Options", "Options Adjustment"]
domain: [risk-management]
prerequisites: ["[[options]]", "[[call-options]]", "[[put-options]]", "[[options-greeks]]"]
difficulty: advanced
related: ["[[risk-management-overview]]", "[[position-sizing]]", "[[options]]", "[[covered-call]]", "[[iron-condors]]", "[[vertical-spread]]", "[[credit-spread]]", "[[protective-puts]]", "[[collar]]", "[[hedging]]", "[[gamma]]", "[[theta]]", "[[wheel-strategy]]", "[[compounding]]", "[[trading-journal]]", "[[calendar-spread]]"]
---

# Trade Repair and Rolling

Trade repair and rolling are position management techniques used to adjust losing or underperforming options positions rather than simply closing them at a loss. Rolling — closing an existing option and simultaneously opening a new one at a different strike, expiration, or both — is the single most important adjustment technique in professional options management. (Source: [[recovering-losing-options-positions]])

## Core Principle: Manage, Don't Revenge-Trade

The first rule professionals follow is to separate the *loss on the original trade* from the *decision about what to do next*. CBOE guidance emphasizes that rolling a position is not a way to erase a loss — it realizes the loss on the existing contract and opens a new trade that must stand on its own probability of success given current market conditions. Experts view every adjustment as a brand-new trade decision, which prevents the sunk-cost fallacy of averaging down into a broken thesis. (Source: [[recovering-losing-options-positions]])

Before any adjustment, disciplined traders do a post-mortem: why did the trade fail — wrong direction, wrong volatility assumption, poor sizing, or poor timing? Without that step, the "recovery" trade often repeats the same mistake.

## Overview

In a long-short-equity portfolio using options, not every trade will work. Even with strong fundamental analysis, timing may be off, catalysts may be delayed, or the market may move against the thesis temporarily. Rather than viewing a losing position as binary (hold or cut), professional traders employ repair and rolling strategies to actively manage the position.

[[anton-kreil]] and the itpm methodology emphasize that trade management is where professionals differentiate themselves from retail traders. The goal is not to avoid losing trades but to minimize losses on losers while maximizing gains on winners. (Source: [[itpm-god-like-trader-status]])

## Rolling Trades

Rolling involves closing an existing options position and simultaneously opening a new one with different parameters (strike price, expiration date, or both).

### The Three Types of Rolls

| Roll Type | Mechanic | Purpose |
|-----------|----------|---------|
| **Roll Out** | Same strike, later expiration | Buy more time for thesis; offset [[theta]]-decay |
| **Roll Up / Roll Down** | Same expiration, different strike | Adjust [[delta]]; move away from danger or lock in gains |
| **Roll Out and Up/Down** | New strike and new expiration | Most common defensive adjustment for tested credit positions |

(Source: [[recovering-losing-options-positions]])

### Roll Mechanics Reference

A roll is two simultaneous legs — closing the existing contract and opening the replacement — so its net cash flow and its effect on the position [[options-greeks|Greeks]] depend on the direction of the roll relative to the underlying. The table below summarizes the mechanics a trader should expect *before* clicking, so the roll can be evaluated as a fresh trade rather than a reflex:

| Roll | When to use | Credit / debit expectation | Greek effect |
|------|-------------|----------------------------|--------------|
| **Roll out (same strike, later expiry)** | Thesis intact, ran out of time | Net **credit** (later expiry has more extrinsic) | Resets [[theta]] decay clock; adds [[vega]] (longer-dated = more vol sensitivity); reduces [[gamma]] |
| **Roll down (short put), same expiry** | Underlying fell, short put tested | Usually a **debit** to move further OTM, or scratch | Lowers [[delta]] exposure; gives more room before assignment; reduces near-term [[gamma]] risk |
| **Roll up (short call), same expiry** | Underlying rose, short call tested | Usually a **debit** to chase the move | Raises strike, cuts upside [[delta]] loss; trades current loss for time |
| **Roll out and down/up** | Tested credit position needing both room and time | Aim for **net credit or small debit** — the cardinal rule | Combines the above; the standard defensive repair for tested credit spreads / strangles |
| **Roll up the untested side (iron condor / strangle)** | One side breached, want to offset | Net **credit** (collect more premium on the safe side) | Adds [[delta]] toward the breach to recoup, raises [[theta]]; raises tail risk if overdone |
| **Roll a long option up/out** | Winning long, take risk off | **Credit** (sell the ITM, keep cheaper OTM) | Locks gains, lowers [[delta]] and capital at risk; converts to a [[vertical-spread]] |

The governing constraint, from the "When NOT to Roll" rules below, is that a defensive roll should be executed for a **net credit or at worst a small net debit**. A roll that requires meaningful net debit is adding [[risk-management|risk]] to a losing trade and is usually a disguised double-down. (Source: [[recovering-losing-options-positions]])

### Roll vs Cut vs Hedge — Decision Table

The prose throughout this page reduces to a single triage decision: for any position moving against you, the choice is between *rolling* (manage the same position forward), *cutting* (realize the loss and stop), and *hedging* (add an offsetting position while preserving the original). The deciding variables are whether the thesis is intact and whether the adjustment can be done without adding risk:

| Situation | Thesis | Action | Why |
|-----------|--------|--------|-----|
| Tested credit position, time short, thesis valid | Intact | **Roll out (± down/up) for credit** | Buy time without adding risk; new strike stands on its own |
| Position losing, thesis broken | Broken | **Cut** — close and accept the loss | "Do not roll a dead thesis" — adding time ≠ adding edge |
| Portfolio bleeding, individual theses still valid | Intact | **Hedge** (index/correlated overlay) | Reduce net exposure, stay functional, preserve the cores (Cathey rule) |
| Roll requires net debit / uncapped risk | Any | **Do not roll** — cut or hedge instead | The cardinal rule: never add net debit or uncapped risk to a loser |
| Single-name / sector exposure already at limit | Any | **Cut or hedge, never roll bigger** | Rolling that compounds [[options-concentration-risk|concentration]] is a sizing failure, not a repair |
| Winner near expiry, more upside likely | Intact | **Book + roll out 3 months** | Lock the equity-curve node, keep exposure (ITPM monthly discipline) |

(Source: [[recovering-losing-options-positions]]; ITPM monthly expiry discipline, Source: [[itpm-god-like-trader-status]])

### Rolling a Losing Short Put — Worked Example

A common professional playbook: a $95 short put sold for $1.50 when the stock was at $100. The stock falls to $92 and the put is now worth $4.50 (a $300 unrealized loss). Rather than take the loss, the trader:

1. Buys back the $95 put for $4.50 (realizes the loss)
2. Sells a $90 put 60 days out for $5.00
3. Collects a $0.50 net credit on the roll

This lowers the strike by $5 (more room to be right), extends duration by 60 days, and raises total premium collected from $1.50 to $2.00. The new $90 put is a fresh trade that stands on its own merits at the current stock price of $92. (Source: [[recovering-losing-options-positions]])

### Rolling a Long Call

Schwab's adjustment framework shows the mirror image for long calls: when an ITM long call has moved in your favor, you can "roll up" to a higher strike by executing a [[vertical-spread]] — selling the in-the-money strike and buying a further OTM call — to take risk off the table while keeping directional exposure.

For a losing long vertical, the defensive move is to roll the whole spread out in time *and* further OTM, but only if it can be done without adding net debit, because adding debit adds risk to an already losing trade. (Source: [[recovering-losing-options-positions]])

### Rolling a Tested Iron Condor

When one side of an [[iron-condors|iron condor]] is breached, institutional traders often roll the *untested* side closer to the stock price to collect additional premium that offsets the tested side's loss. In extreme moves the untested short strike can even be rolled past the tested one, locking in a defined maximum loss while maximizing premium recovery. (Source: [[recovering-losing-options-positions]])

### The 21-Day Rule

Many professional premium sellers — particularly those running the [[wheel-strategy|wheel]] or short-premium strategies — mechanically roll short positions at roughly 21 days to expiration. At that point [[theta]] decay accelerates but [[gamma]] risk spikes, creating the **"gamma trap"** where small underlying moves cause violent option price swings. Rolling at 21 DTE sidesteps that dangerous zone. (Source: [[recovering-losing-options-positions]])

### When to Roll

- The fundamental thesis remains valid but timing was off
- A catalyst has been delayed (earnings pushed back, regulation delayed)
- The position is approaching expiry with insufficient time remaining
- You want to lock in partial profits while maintaining exposure
- The roll can be done for a net credit or at worst a small net debit

### When NOT to Roll

- The fundamental thesis has been invalidated (cut the loss instead)
- Rolling would increase overall portfolio risk beyond acceptable levels
- The cost of the roll exceeds the expected recovery value
- Rolling "for hope" without valid thesis support — this typically deepens losses
- The adjustment adds net debit or uncapped risk to an already losing trade

## Other Loss-Recovery Strategies

### Convert to a Spread

Selling a further OTM option against a losing long option converts it into a [[vertical-spread]], reducing cost basis and capping further loss:

- **Losing long call** → Sell a higher strike call against it (creates a [[bull-call-spread|bull call spread]])
- **Losing long put** → Sell a lower strike put against it (creates a [[bear-put-spread|bear put spread]])
- The credit from the short leg reduces the overall position cost

(Source: [[recovering-losing-options-positions]])

### Scaling In, Not Doubling Down

Adding to a losing position gradually — with pre-defined size limits — rather than a single revenge-trade "double up." This is only appropriate when the fundamental thesis is stronger than when you entered and the addition is sized relative to portfolio risk, not the desire to "break even." (Source: [[recovering-losing-options-positions]])

### Defined-Risk Replacement Trades

Rather than adjust a broken trade, close it entirely and redeploy capital into a structure with known max loss such as a [[debit-spread]], [[credit-spread]], or [[iron-condors|iron condor]]. This is often preferable when the original thesis is invalidated but a related opportunity exists. (Source: [[recovering-losing-options-positions]])

### Take a Trading Break

After a string of losses, pausing trading is itself a recognized risk-management tactic to reset emotional capital. This prevents the compounding effect of revenge trading where each recovery attempt deepens the drawdown. (Source: [[recovering-losing-options-positions]])

### Hedging Overlays

[[protective-puts|Protective puts]], [[collar|collars]], and [[covered-call|covered calls]] can be layered on top of an existing position to cap downside or generate income that offsets the loss. Index puts on SPX/QQQ can hedge broad portfolio beta without disturbing underlying holdings. (Source: [[recovering-losing-options-positions]])

Instead of repairing the individual trade, adding a portfolio-level hedge can protect the overall P&L:

- If your put options are losing because the market is rallying, add a hedge (e.g., TLT calls, SPY calls) that profits from the rally
- The hedge doesn't fix the individual trade but protects the portfolio P&L
- Example: [[anton-kreil]]'s TLT hedge competition where a $882 spend could produce $31,500–$57,000 if the market rallied against a bearish portfolio (Source: [[itpm-god-like-trader-status]])

## The Professional Playbook

| Pillar | Key Tactics |
|--------|-------------|
| **Prevention** | 1–2% [[position-sizing]], diversification, defined-risk structures, [[options-greeks|Greeks]] monitoring |
| **Early Defense** | 21-DTE roll rule, pre-set [[stop-loss|stop-losses]], profit-taking at 50% max |
| **Active Repair** | Roll out, roll down/up, roll untested side, convert to spread |
| **Hedging** | [[protective-puts]], [[collar|collars]], index-level overlays |
| **Process** | Post-mortem every loss, trade log, pause after loss streaks |

(Source: [[recovering-losing-options-positions]])

## ITPM Monthly Expiry Discipline

The itpm methodology has specific rules for managing positions at monthly options expiry (third Friday of each month). [[anton-kreil]]'s directive: **"You are not allowed to bank a loss at monthly expiry."** The decision framework:

1. **Position is winning** → Bank the profit. Book it to your [[equity-curve]].
2. **Position could go further** → Book the profit now and roll the trade out 3 months to re-enter the thesis with fresh time. This locks in a winning node on the equity curve while keeping exposure.
3. **Position is losing but thesis is intact** → Roll out 3 months. Do not book the loss. The 3-month roll buys time for the thesis to play out while maintaining the position.
4. **Thesis is broken** → Close the trade and accept the loss. Do not roll a dead thesis.

Plan expiry management **weeks in advance**, not on expiry day. The goal is to make the [[equity-curve]] go up at every monthly node — banking more winners than losers creates the compounding engine. (Source: [[itpm-god-like-trader-status]])

Kreil notes that reactive risk management — how to handle positions that move against you or in your favor — "can only be taught via mentoring, not video series." The framework above captures the rules, but the judgment of when a thesis is "intact" versus "broken" requires experience and mentorship. (Source: [[itpm-god-like-trader-status]])

## How Ratio Structures Mechanically Cap Losses

One of the most powerful loss-mitigation mechanisms in the ITPM methodology is not a repair *decision* but a structural feature built into the trade at entry. When using [[calendar-spread|calendar spreads]] or [[vertical-spread|vertical spreads]] with a short leg, the credit collected from the short leg automatically reduces the maximum loss if the trade fails.

### Real Examples from Philip Klein's Portfolio

Philip Klein (ITPM junior trading mentor) demonstrated this with actual TradeStation broker data over 32 months:

**Snowflake put calendar spread** (trade went against him):
- Long October $110 puts (30 contracts at $6.22)
- Short September $108 puts (15 contracts at $2.55 — 2:1 ratio)
- Collected $2,900 credit (75% of max) after 6 days
- Trade went against him — long leg wrote off at **-$18,669**
- But the short leg credit reduced total loss to **-$15,770**
- The structure saved $2,900 automatically — no decision required

**Boeing vertical spread** (trade went against him):
- Long/short put vertical (1:1, 39 contracts)
- Nearly full loss on the long leg
- But the short leg reduced loss from **-$18,000 to -$12,380**
- Structure saved ~$5,600 mechanically

**ON Holdings calendar spread** (trade worked):
- Long October $42.50 calls (64 contracts at $2.97)
- Short August $43 calls (32 contracts at $1.39 — 2:1 ratio)
- Collected $3,800 credit (85% of max) in 18 trading days
- Then stock moved in his favor — booked **$30,000** on the long leg
- Total profit: ~$33,800 — the credit was "free" income on top of the directional payoff

The key insight: **credits are asymmetric**. During winning periods, credits add on top of trading profits. During losing periods, credits save you from the full loss. The structure provides automatic loss mitigation regardless of the trader's emotional state. (Source: [[itpm-master-compounding]])

### Credits as Portfolio-Level Loss Armor

Over 32 months and ~102 credit-collecting trades, Klein accumulated **$254,000 in total credits** — approximately $8,000 per month, averaging ~$2,500 per individual credit. The credit equity curve (short legs only) formed a "nearly perfect 45-degree line" — stable monthly additions with minimal variation. This anchored the total equity curve even during flat or difficult trading periods. (Source: [[itpm-master-compounding]])

This is the portfolio-level answer to "how do professionals survive losing streaks?" Not through individual trade recovery, but through systematic credit collection that compounds over time. Even with a 52.5% win rate and a below-target 1.28 R-core, Klein achieved ~100% annual returns because the credit engine kept the equity curve moving upward. (Source: [[itpm-master-compounding]])

## Thesis-Preservation Hedging vs. Panic Covering

A critical distinction that separates professional from retail recovery: **hedging to preserve an intact thesis** versus **panic-covering to stop the bleeding**.

### The Goldman Sachs Crisis Example

[[chris-cathey]] described a day at goldman-sachs around 2001 during the NASDAQ bear market. The desk was very short — approximately $500 million — in telecoms and technology stocks. A vicious bear market rally squeezed their positions; by lunchtime they were down significantly.

Three possible responses:
1. **Panic and cover everything** — locks in the full loss, abandons the thesis
2. **Freeze** ("rabbit in headlights") — equally bad; position keeps deteriorating
3. **Hedge the portfolio while preserving the thesis** — the professional response

They chose option 3: bought Euro Stoxx futures to reduce their net short exposure, even though they believed the rally was temporary. This accomplished three things:
- Reduced the bleeding on the portfolio P&L
- Allowed them to remain functional as market makers
- Preserved their core short thesis for when the rally exhausted itself

They literally printed the high tick of the day on the Euro Stoxx purchase. When the market turned in the afternoon, they increased short positions again. **Ended the day slightly positive**, and over the next two days made a "very big amount of money." (Source: [[itpm-trading-legends-chris-cathey]])

### The Cathey Rule

> "Do not increase losing positions. Only add to positions when they are working. When a position moves against you and triggers your stop loss, exit. Then, when you get confirmation the trade is working again, increase. Adding to winners and cutting losers is exactly the same process — all you're doing is risk managing and putting the risk-reward in your favor." — [[chris-cathey]] (Source: [[itpm-trading-legends-chris-cathey]])

This creates a clear framework:
- **Thesis intact, position losing** → Hedge (add a correlated offsetting position), don't increase the losing side
- **Thesis intact, position recovering** → Scale back in on confirmation
- **Thesis broken** → Exit completely, no hedging, no rolling

## The Psychology of Executing Repairs

The emotional challenge of trade repair is as important as the mechanical technique. The itpm methodology treats emotional detachment as a trainable skill, not an innate trait.

### Why Repairs Fail Psychologically

[[chris-cathey]] identifies the core problem: **"The natural human nature is to take profits too quickly and to cut losers too late. We teach the reverse — cut losers quickly and let profits run — which is counterintuitive to human nature."** (Source: [[itpm-professional-traders-amazing-advice]])

This directly undermines repair decisions:
- Traders hold losing positions too long hoping for recovery, reducing the available repair options (time decay erodes alternatives)
- When they finally act, they over-repair — adding too much risk to "make back" what was lost
- After booking a loss, they revenge-trade into the next position with inflated size

### The ITPM Emotional Framework

1. **"Money is unemotional; you must be unemotional about your trading decisions and your P&L."** Losses are a cost of doing business, not a personal failure. (Source: [[itpm-professional-traders-amazing-advice]])

2. **"The moment you press the button, you are losing"** — because you buy at the offer and are marked on the bid. Every trade starts in the red. Accepting this eliminates the shock of seeing red P&L. (Source: [[itpm-professional-traders-amazing-advice]])

3. **"When stopped out, you are admitting to yourself that you are wrong... that is very very difficult to learn how to do."** Once mastered, emotion leaves trading. (Source: [[itpm-professional-traders-amazing-advice]])

4. **Trading is 50% idea generation, 50% risk management.** The repair decision is the risk management half — treat it with the same rigor as the original thesis. (Source: [[itpm-professional-traders-amazing-advice]])

5. **Paper trading cannot teach this.** Emotional detachment from P&L can only be learned with real money at stake. "You need to have skin in the game." (Source: [[itpm-professional-traders-amazing-advice]])

Record every repair decision in your [[trading-journal]] — diagnosis, action taken, and outcome. Over time, this builds the data-driven confidence needed to execute repairs without emotional interference.

## Can Experts Turn Every Losing Month Into a Winner?

No. This is the question retail traders most want answered, and the honest professional answer is that a single month is too short a window to guarantee recovery:

- **Rolling is not magic.** CBOE's position is explicit: rolling realizes the original loss and initiates a new trade. If the new trade also loses, the total drawdown compounds.
- **Adding time ≠ adding edge.** Rolling out works only if the original thesis is still valid and market conditions support it.
- **Don't add risk to recover.** The cardinal rule of adjustment — never add net debit or uncapped risk to a losing trade — explicitly forbids aggressive "make it back this month" behavior.
- **Expected value governs outcomes.** With proper sizing (≤2% per trade) a losing streak is mathematically survivable but may still produce a red month; professionals measure success over quarters and years.
- **Volatility regime matters.** Sudden volatility spikes can overwhelm even well-adjusted short-premium books, making [[hedging]] — not recovery — the priority.

What experts *do* accomplish consistently is (a) keeping individual losses small enough that a single bad trade cannot end a career, (b) using rolls and spreads to convert many would-be full losses into partial losses or scratches, and (c) relying on a positive expectancy process so that winners fund losers across many months. (Source: [[recovering-losing-options-positions]])

## The [[edward-shek|Shek]] Approach

[[edward-shek]]'s approach to trade management includes:

1. **Start with half positions** when market conditions are unclear
2. **Scale up** once you receive confirmation (news, earnings, price action)
3. **Cut losing trades early** at around 50% loss on the option premium
4. **Repair positions later** — re-enter at better prices with fresh thesis confirmation rather than holding a deteriorating position

This contrasts with the common retail approach of "holding and hoping." (Source: [[itpm-education-methodology-overview]])

## Connection to Position Sizing and Greeks Aggregation

Trade repair does not happen in a vacuum — every roll, spread conversion, or hedge changes the book's aggregate risk, so the repair decision must be made against the *portfolio* picture, not the single line item. This is where rolling connects to the broader risk framework:

- **Sizing governs whether repair is even an option.** The reason ITPM and CBOE insist on ≤1–2% [[position-sizing|position sizing]] is that a correctly sized loser can always be rolled or cut without threatening the account. An oversized position removes the option to be patient — you are forced to act at the worst moment. Repair technique is downstream of disciplined sizing; it cannot rescue a position that was too big at entry. (Source: [[recovering-losing-options-positions]])

- **A roll changes the aggregate Greeks.** Rolling out adds [[vega]] and resets [[theta]]; rolling the untested side of an iron condor adds [[delta]] and [[theta]] while raising tail risk. Before executing, re-check the book-level numbers via [[portfolio-greeks-aggregation|Greeks aggregation]] — a roll that "fixes" one position can push net [[vega]] or beta-weighted [[delta]] outside the [[options-risk-budgeting|risk budget]]. The repair is only valid if the *post-roll book* is within limits.

- **Rolling the untested side is a sizing decision, not just a repair.** Collecting more credit on the safe side of a tested condor increases directional exposure toward the breach. If that addition takes the book over its [[options-concentration-risk|single-name or sector concentration]] limits, the "repair" has quietly doubled down. Check concentration before adding premium.

- **Stress the repaired book, not just the trade.** A defensive roll should be followed by an [[options-stress-testing|options stress test]] of the whole book: does the rolled position still survive a [[volatility|vol]] spike and a gap? On a [[portfolio-margin]] account this matters doubly — rolling into a longer-dated, higher-vega position can *increase* the broker's stressed margin requirement even as it reduces near-term [[gamma]] risk.

- **Theta targeting and repair interact.** A book run to a [[theta-targeting|daily theta target]] will see rolls change aggregate theta. Closing a tested position and re-opening further out typically *lowers* near-term theta — the repair may temporarily put the book below target, which is acceptable; chasing the target by rolling into richer, riskier strikes is the [[theta-targeting#The Theta Trap|theta trap]].

- **VaR and tail metrics frame "how bad can the roll go."** A roll that buys time also extends the window over which a tail event can hit the position. Re-running [[value-at-risk|VaR]] / [[expected-shortfall]] on the rolled book keeps the decision honest about what was actually accomplished — risk was *moved in time*, not eliminated.

The throughline: repair is the risk-management half of trading (Cathey's "50% idea generation, 50% risk management"), and risk management is always portfolio-level. Evaluate every adjustment as a fresh trade *and* as a change to the aggregate book. (Source: [[itpm-professional-traders-amazing-advice]])

## Key Principles

1. **Every adjustment is a new trade** — Evaluate on current merits, not sunk cost
2. **Never hold options to zero** — If a position has lost 50%+ of its premium and the thesis is weakening, exit and reassess
3. **Repair is cheaper than replacement** — Rolling a losing position often costs less than closing and opening a new one, because you retain remaining time value
4. **Portfolio context matters** — A losing individual trade may be acceptable if the overall portfolio is performing. Don't repair in isolation
5. **Time is the enemy of losing options** — The longer you wait to act, the fewer repair options available due to [[theta-decay|time decay]]
6. **Don't throw good money after bad** — Only repair if the thesis is still valid. If the thesis is broken, take the loss
7. **Never add net debit or uncapped risk** to a losing trade — this is the cardinal rule of adjustment

## Related

- [[risk-management-overview]] — Portfolio-level risk framework
- [[position-sizing]] — How much to allocate per trade (the 2% rule)
- [[stop-loss]] — Pre-defined exit rules for losses and profits
- [[hedging]] — Portfolio protection via options overlays
- [[iron-condors]] — Common structure requiring rolling adjustments
- [[vertical-spread]] — Spread conversion target for losing long options
- [[credit-spread]] — Defined-risk credit structures
- [[protective-puts]] — Downside insurance via long puts
- [[collar]] — Combined put protection + call income
- [[wheel-strategy]] — Short-premium strategy using the 21-DTE roll rule
- [[gamma]] — The risk that spikes near expiration (gamma trap)
- [[gamma-risk]] — The gamma trap and 21-DTE rule explained
- [[theta]] — Time decay driving the 21-DTE roll threshold
- [[calendar-spread]] — The ITPM ratio structure that mechanically caps losses
- [[compounding]] — Credits as portfolio-level loss armor
- [[trading-journal]] — Post-mortem framework for diagnosing and recording repair decisions
- [[options]] — Underlying instruments for these techniques
- [[portfolio-greeks-aggregation]] — Book-level Greeks a roll must respect
- [[options-stress-testing]] — Stress the repaired book, not just the trade
- [[portfolio-margin]] — How a roll can change stressed margin
- [[options-concentration-risk]] — Rolling the untested side can compound concentration
- [[theta-targeting]] — Repair interacts with the daily theta target
- [[value-at-risk]] — Re-framing tail risk after a roll moves it in time
- [[options-portfolio-construction]] — Building books that are repairable by design
- [[vega]] — Roll-out adds vega; check it post-roll
- [[delta]] — Roll up/down adjusts directional exposure
- [[volatility]] — The regime that dictates whether to repair or hedge

## Sources

- (Source: [[recovering-losing-options-positions]])
- (Source: [[itpm-god-like-trader-status]]) — Monthly expiry discipline, reactive risk management
- (Source: [[itpm-master-compounding]]) — Phil Klein's real trade examples, credit compounding as loss armor
- (Source: [[itpm-trading-legends-chris-cathey]]) — Goldman crisis example, thesis-preservation hedging, the Cathey rule
- (Source: [[itpm-professional-traders-amazing-advice]]) — Emotional framework for executing repairs
- (Source: [[itpm-education-methodology-overview]]) — The Shek approach to trade management

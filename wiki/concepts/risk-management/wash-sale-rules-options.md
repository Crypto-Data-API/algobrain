---
title: "Wash Sale Rules and Options"
type: concept
created: 2026-05-06
updated: 2026-06-21
status: excellent
tags: [risk-management, regulation, options, derivatives]
aliases: ["Wash Sale Options", "IRC 1091 Options", "Section 1091"]
domain: [risk-management]
prerequisites: ["[[tax-implications-trading]]", "[[options-overview]]"]
difficulty: intermediate
related: ["[[wash-sale]]", "[[section-1256-contracts]]", "[[tax-implications-trading]]", "[[trade-repair-and-rolling]]", "[[tax-loss-harvesting]]", "[[options-portfolio-construction]]", "[[options-premium-selling]]", "[[short-strangle]]", "[[short-straddle]]", "[[short-put-spread]]", "[[calendar-spread]]", "[[iron-fly]]", "[[regulation]]"]
---

# Wash Sale Rules and Options

The IRS wash sale rule (**IRC §1091**) disallows a capital loss when a taxpayer sells a security at a loss and acquires a "substantially identical" security within a 61-day window — 30 days before through 30 days after the loss sale. The disallowed loss is added to the cost basis of the replacement position, deferring (not eliminating) the loss. The rule explicitly applies to **options** as well as stocks: buying a call after selling stock at a loss, rolling a losing put into a new put on the same underlying with similar terms, or repurchasing the same option series can all trigger disallowance. A critical carve-out for active options traders: **Section 1256 contracts** (broad-based index options like SPX, NDX, RUT, and most futures) are **not subject** to the wash sale rule because they are marked to market at year end under §1256(a).

This is a tax-mechanics page, not tax advice. Consult a qualified tax professional for your specific facts.

> **Bottom line for ITPM-style options portfolios:** The wash sale rule is one of the largest hidden cost layers in single-stock options trading, especially when "trade repair" or rolling losers is part of the playbook. Routing index/macro exposure through SPX rather than SPY can convert this from a major accounting headache into a non-issue.

## Overview

| Element | Detail |
|---|---|
| Statute | IRC §1091 (loss disallowance) and §1091(d) (basis adjustment) |
| Window | 61 days total: 30 days before the loss sale + day of sale + 30 days after |
| Trigger | Acquiring a "substantially identical" security in the window |
| Applies to | Stocks, bonds, options, ETFs, mutual funds — any "stock or securities" |
| Does NOT apply to | Section 1256 contracts (SPX, NDX, RUT, VIX, futures), commodities, currencies (in most cases), crypto (as of 2026 — not yet enacted) |
| Effect | Loss is **disallowed** in the year of sale; added to basis of replacement |
| Holding period | Holding period of the disallowed lot **carries over** to the replacement |
| Reporting | Brokers must flag wash sales on Form 1099-B at the **account level** (since 2011) |

## How the Rule Works

The mechanic is simple to state and surprisingly hard to apply:

```
1. You sell Security A at a loss on day T.
2. Within [T-30, T+30], you acquire a "substantially identical" security
   (could be Security A itself, or a different instrument that is substantially identical).
3. The loss on the original sale is disallowed for the current tax year.
4. The disallowed loss is added to the cost basis of the replacement.
5. The replacement inherits the original lot's holding period.
```

### Worked Example — Stock Followed by Option

```
Day 1:  Buy 100 AAPL @ $200 (basis $20,000)
Day 30: Sell 100 AAPL @ $180 (realized loss = -$2,000)
Day 45: Buy 1 AAPL Jan $180 call for $5 (cost $500)

Result:
  - $2,000 loss is DISALLOWED in current year
  - The call's basis becomes $500 + $2,000 = $2,500
  - Holding period of the disallowed stock lot carries to the call
```

The loss is not gone — it is deferred until the call is sold or expires. But cash flow and current-year tax planning are impacted.

## "Substantially Identical" Test for Options

The IRS has never published a bright-line test. The case law and IRS guidance (notably **Rev. Rul. 56-406** and **Rev. Rul. 85-87**) leave large gray areas. Practitioner consensus on common cases:

| Scenario | Wash Sale? | Notes |
|---|---|---|
| Sell AAPL stock at loss → buy AAPL stock | Yes | The textbook case |
| Sell AAPL stock at loss → buy AAPL call (any strike/expiry) | **Yes** | IRS treats calls on the same stock as substantially identical to the stock (Rev. Rul. 56-406) |
| Sell AAPL stock at loss → buy AAPL put | No | Puts are not substantially identical to long stock (per Rev. Rul. 56-406) |
| Sell AAPL stock at loss → sell AAPL puts (collect premium) | **Yes** (selling deep ITM puts) | A short put functionally replicates long stock; deep ITM short puts are flagged |
| Close AAPL Jun 100 call at loss → open AAPL Jun 100 call | Yes | Same series — clearly substantially identical |
| Close AAPL Jun 100 call at loss → open AAPL **Jun 105** call | Likely yes | Same expiry, near strike — generally treated as substantially identical |
| Close AAPL Jun 100 call at loss → open AAPL **Aug 105** call | **Probably no** | Different strike and different expiration; most practitioners treat as not substantially identical, but this is the gray zone |
| Close AAPL Jun 100 call at loss → open AAPL **Jan (next year) 200** LEAP | No | Different expiration cycle and meaningfully different delta |
| Close SPY put at loss → open SPX put | Disputed | Same economic exposure but different securities; aggressive position is "no", conservative is "yes" |
| Close SPY put at loss → open ES future put | **No** | ES put is a §1256 contract — separate regime |
| Close TQQQ at loss → buy QQQ | No | Different ETFs even if correlated |

The further apart the strike and expiration, the safer the position. Practitioners often use a heuristic of **>1 strike apart AND >30 days apart in expiration** as a margin of safety, but no statute or ruling formally blesses this.

### Quick decision flow (indicative, not advice)

A fast triage for "did I just create a wash sale?" The answers below are the *common practitioner read*, not a ruling — the [[wash-sale|wash-sale rule]] has large gray areas:

| Question | If YES | If NO |
|---|---|---|
| 1. Did you close the position at a **loss**? | continue → Q2 | no wash sale (gains are never washed) |
| 2. Is the instrument a **§1256 contract** (SPX, NDX, RUT, VIX, futures)? | **no wash sale** — exempt; year-end MTM | continue → Q3 |
| 3. Did you acquire a "substantially identical" position in the **[T−30, T+30]** window? | continue → Q4 | no wash sale |
| 4. Was the replacement in a **taxable** account you/spouse control? | loss **disallowed**, added to replacement basis | if in an **IRA**: loss **permanently disallowed** (no basis carryover) |

The two worst outcomes are the IRA case (permanent loss) and the cross-account/cross-broker case (invisible to broker 1099-B reporting, your responsibility to track).

## Wash Sale and Section 1256 — The Index Option Exemption

Section 1256 contracts are exempt from the wash sale rule because they are marked to market at year-end under §1256(a). All gain or loss is recognized annually regardless of whether the position is closed, so there is no mechanism for a wash to occur.

**Section 1256 contracts include:**

- Regulated futures contracts (CME, ICE US, etc.)
- **Broad-based index options**: SPX, XSP, NDX, RUT, MNX, VIX options
- Foreign currency contracts (interbank market)
- Non-equity options on broad-based indices
- Dealer equity options and dealer securities futures

**Section 1256 contracts do NOT include:**

- Single-stock options (AAPL, NVDA, etc.) → wash sale applies
- Narrow-based index options (some sector indices) → wash sale applies
- ETF options (SPY, QQQ, IWM) — these are equity options on an ETF, **not** §1256 → wash sale applies
- Single-stock futures → wash sale applies

This is why high-turnover index option strategies — [[volatility-carry]], delta-hedged short strangles, [[options-premium-selling]] on indexes — are dramatically simpler at tax time when run through SPX/XSP rather than SPY. Same economic exposure, completely different tax regime: 60/40 blended rate, no wash sale, year-end mark-to-market with one number per contract on Form 6781.

| Index Exposure Choice | Wash Sale? | Tax Rate |
|---|---|---|
| SPY options (equity option on ETF) | Yes | Up to 40.8% on shorts; full wash-sale tracking |
| **SPX / XSP options** (§1256) | **No** | ~30.5% blended (60/40 + NIIT); annual MTM |
| ES futures options | No | Same §1256 regime |

For a portfolio that turns over a meaningful fraction of notional each year, the **structural tax difference is often worth 5-10% of returns**. See [[section-1256-contracts]] for the full rate analysis.

## Common Wash-Sale Triggers in Options Trading

### 1. Rolling a losing position

The classic trap. A short put is challenged → the trader closes for a debit (loss) and opens a further-out put for credit. If the new put is "substantially identical" (same or near strike, near expiration), the loss on the close is disallowed.

```
Day 1:  Sell AAPL Jun 180 put @ $4.00 (credit $400)
Day 20: AAPL drops; buy back the Jun 180 put @ $7.00 (loss = -$300)
Day 20: Sell AAPL Jul 180 put @ $5.00 (credit $500)
       → $300 loss is DISALLOWED, added to basis of new put
```

Mitigations: roll to a different strike (e.g., 175 instead of 180), wait 31 days, or use SPX where the rule does not apply. See [[trade-repair-and-rolling]].

### 2. Year-end loss harvesting in equity options

Closing a losing single-stock option position in late December and re-opening a similar position in January: if the gap is less than 31 days, the loss is disallowed for the current year. This defeats the entire purpose of the harvest.

### 3. Replacing stock with options after a tax-loss sale

Selling stock at a loss in December and buying calls in January looks like avoidance — and it is. The IRS treats long calls on the same underlying as substantially identical to the stock (Rev. Rul. 56-406). See [[tax-loss-harvesting]] for compliant alternatives.

### 4. Multiple accounts and IRAs

Wash sale tracking is required at the **taxpayer level**, not the account level — even though brokers only report at the account level on 1099-B. Selling a stock at a loss in your taxable account and buying it back in your **IRA** within 30 days is a wash sale, and the loss is **permanently disallowed** (no basis carryover into an IRA). This is the worst-case wash sale: gone, not deferred.

### 5. Spousal accounts

A loss in your account paired with a buy in your spouse's account within the window also triggers a wash sale. The IRS treats married-filing-jointly taxpayers as a single unit for §1091.

### 6. Rebuilding a "broken" position

Trader closes a losing iron condor and immediately opens a new iron condor on the same underlying with adjusted strikes. If any leg is substantially identical to a leg of the closed position, that portion of the loss is disallowed.

## How to Avoid Wash Sales

| Approach | Mechanism | Tradeoffs |
|---|---|---|
| **Use §1256 instruments** | SPX/XSP/NDX/RUT options exempt from §1091 | Limited to broad-based indices |
| **Wait 31+ days** before re-entering | Closes the wash sale window | Capital sits idle; market may move |
| **Substitute non-identical exposure** | Replace AAPL with sector ETF (XLK) or competitor (MSFT) | Imperfect hedge; tracking error |
| **§475(f) mark-to-market election** | Active traders qualifying as TTS can elect MTM, eliminating wash sale tracking entirely | Converts all gains to ordinary income; permanent election |
| **Separate strategies per account** | Run mean-reversion in one account, momentum in another to reduce overlap in same names | Operational complexity |
| **Roll to different strike AND expiry** | Heuristic: >1 strike + >30 days different | Not statutorily blessed; gray zone |
| **Hold the broken position to expiration** | Loss is realized at expiration with no replacement | May incur larger loss; assignment risk |

The **§475(f) trader tax status mark-to-market election** is the cleanest fix for active multi-strategy options traders. It eliminates wash sale tracking and uncaps loss deductions, at the cost of converting all P&L to ordinary income (forfeiting any §1256 60/40 advantage). For traders who already run mostly short-term, the simplification typically pays for itself. See [[tax-implications-trading]] for qualification criteria.

## Tracking and Reporting

Since the **Emergency Economic Stabilization Act of 2008** (effective 2011), brokers must report wash sales on **Form 1099-B**, including:

- The disallowed loss amount (Box 1g)
- The adjusted basis on replacement positions
- Holding period adjustments

**Critical limitations of broker tracking:**

1. **Account-level only**: Brokers track wash sales within a single account. Cross-account wash sales (especially taxable ↔ IRA, or spouse accounts) are the **taxpayer's** responsibility to track and report.
2. **Identical CUSIPs only**: Most brokers only flag exact-match CUSIPs. They generally do **not** detect option-to-option substantially-identical wash sales across different strikes/expiries, or stock-to-option wash sales. Practitioners must self-track these.
3. **No cross-broker tracking**: A loss at Broker A and a buy at Broker B in the window is invisible to both brokers.

For active options traders, dedicated software (TradeLog, GainsKeeper, Cointracker for crypto) or a CPA specializing in trader taxes is effectively required.

## Interaction with common options strategies

How §1091 interacts with the strategies catalogued elsewhere in this wiki (all indicative, single-name unless noted):

| Strategy | Wash-sale exposure | Why | Mitigation |
|---|---|---|---|
| [[options-premium-selling]] on SPX/XSP/NDX/RUT | **None** | §1256 exempt; year-end MTM | already optimal; route index exposure here |
| [[options-premium-selling]] / [[short-strangle]] on SPY, QQQ, single names | **High** when rolling losers | each roll closes a loss and reopens a near-identical leg | roll to a different strike, or wait 31 days |
| [[short-put-spread]] (single name) | **High** | rolling a challenged short put down/out is the textbook trigger (see Trigger #1) | change strike on the roll; or trade SPX-based spreads |
| [[calendar-spread]] (single name) | **Medium** | rolling the short front leg can re-create a substantially identical leg | re-strike the new short leg (becomes a diagonal); avoid same-strike same-cycle |
| [[iron-fly]] / [[iron-condor]] (single name) | **Medium-High** | rebuilding a broken structure can re-create substantially identical legs (Trigger #6) | adjust strikes meaningfully on the rebuild |
| Index versions of all the above (SPX/XSP) | **None** | §1256 regime | the structural reason index premium-selling is simpler at tax time |

The pattern is consistent: **single-name rolling is the high-risk activity, and routing through §1256 index products removes the entire problem.** This is the same conclusion the [[options-premium-selling]] and [[section-1256-contracts]] pages reach from the trading-cost side.

## ITPM Implications

The [[itpm-playbook|ITPM]] approach emphasizes options portfolios with structured rolling, position repair, and aggressive trade management — all of which interact heavily with §1091. Practical implications for an ITPM-style book:

1. **Macro index hedges via SPX, not SPY** — avoids the entire wash sale regime on the largest, most-rolled positions.
2. **Single-stock structures should size for the assumption that mid-trade losses are deferred, not deducted** in the current year. This affects after-tax expected return calculations and position sizing.
3. **Rolling losers** ([[trade-repair-and-rolling]]) on single-name options is the highest wash-sale-risk activity in the playbook. Strike and expiration selection on the roll matters not just for [[delta]] and [[theta]] but for tax treatment.
4. **Year-end review** is mandatory. Close any loss-harvesting trades by mid-November to give a clean 31-day window before year-end.
5. **§475(f) qualification** is worth evaluating once annual options trade count exceeds ~500 round trips. The simplification dominates the rate cost for high-turnover books.
6. **Capital allocation** should account for the cash-flow drag of disallowed losses — a strategy with a 40% win rate and tight rolls may have meaningful current-year tax even when economically flat.

## Related

- [[wash-sale]] — the general wash-sale rule (stocks and securities) this page specializes for options
- [[section-1256-contracts]] — the index/futures exemption
- [[tax-implications-trading]] — overall tax framework
- [[trade-repair-and-rolling]] — the activity most prone to wash sale issues
- [[tax-loss-harvesting]] — strategy that runs head-on into §1091
- [[pattern-day-trader-rule]] — the other major regulatory friction for options traders
- [[options-portfolio-construction]]
- [[options-premium-selling]] — the high-turnover short-vol family most affected by rolling
- [[short-strangle]]
- [[short-straddle]]
- [[short-put-spread]] — single-name rolling is a frequent trigger
- [[calendar-spread]] — short-leg rolling can re-create substantially identical legs
- [[iron-fly]] / [[iron-condor]] — rebuilding broken structures and the §1256 vs equity-option distinction
- [[regulation]]
- [[itpm-playbook]]

## Sources

- IRC §1091 (wash sale loss disallowance)
- IRS Publication 550, "Investment Income and Expenses" — wash sale section
- IRS Rev. Rul. 56-406 (calls and puts vs. underlying stock)
- IRS Rev. Rul. 85-87 (substantially identical guidance)
- IRC §1256 (mark-to-market for regulated contracts)
- IRC §475(f) (trader mark-to-market election)
- Emergency Economic Stabilization Act of 2008, broker basis reporting provisions
- [[tax-implications-trading]]

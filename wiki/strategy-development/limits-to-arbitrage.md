---
title: "Limits to Arbitrage"
type: concept
created: 2026-06-22
updated: 2026-06-22
status: good
tags: [behavioral-finance, methodology, risk-management, market-microstructure, arbitrage]
aliases: ["Limits of Arbitrage", "Limited Arbitrage", "Shleifer-Vishny"]
domain: [strategy-development, behavioral-finance, market-microstructure]
difficulty: intermediate
related: ["[[edge-taxonomy]]", "[[arbitrage]]", "[[noise-trader-risk]]", "[[efficient-market-hypothesis]]", "[[reflexivity]]", "[[anomalies-overview]]", "[[short-selling]]", "[[margin]]", "[[mean-reversion]]", "[[failure-modes]]", "[[behavioral-finance]]"]
---

# Limits to Arbitrage

**Limits to arbitrage** is the theory explaining why rational, informed traders ("arbitrageurs") cannot always force prices back to fair value, so mispricings can be large and persist for long periods. The canonical formulation is Andrei Shleifer and Robert Vishny's 1997 paper *"The Limits of Arbitrage"* (Journal of Finance), which showed that textbook arbitrage — riskless, costless, instantaneous correction of mispricing — is a fiction. Real arbitrage is risky, capital-constrained, and conducted by specialists managing other people's money, and those frictions cap how much corrective force can be applied. The concept is the central bridge between [[behavioral-finance]] (which explains *why* mispricings appear) and the persistence of [[anomalies-overview|anomalies]] (which explains why they are not instantly competed away).

## Overview

The [[efficient-market-hypothesis]] rests on an arbitrage argument: if a security is mispriced, rational traders will buy the cheap one and short the expensive one until prices converge, so prices should always reflect fundamentals. Limits-to-arbitrage theory accepts that arbitrageurs exist and are smart, but argues that the *act* of arbitrage is itself risky and resource-constrained. As a result, the corrective force is finite. When [[noise-trader-risk|noise traders]] push a price away from value, the arbitrageur's response is bounded by how much risk, capital, and time they can commit. Mispricings therefore persist until the frictions relax — not instantly. This is why the [[edge-taxonomy|behavioral and structural edges]] in a trading strategy can survive: someone *would* arbitrage them away if it were free and riskless, but it is neither.

## The core mechanisms

### 1. Noise-trader risk

The most important contribution of Shleifer-Vishny and the earlier De Long, Shleifer, Summers & Waldmann (1990) model. An arbitrageur who shorts an overpriced asset faces the risk that irrational traders push it *even further* from value before it converges. "The market can stay irrational longer than you can stay solvent" (attributed to Keynes) is the folk version. Because the arbitrageur has a finite horizon and possibly leverage, an adverse move can force liquidation at the worst possible moment — locking in a loss on a position that was *correct* about fundamentals. See [[noise-trader-risk]].

### 2. The agency / separation-of-brains-and-capital problem

Real arbitrage is performed by specialized agents (hedge funds, prop desks, bank trading books) managing outside capital. Investors judge these agents on short-term performance and *withdraw capital after losses*. This creates a perverse dynamic: precisely when mispricing is widest (and the opportunity best), the arbitrageur has suffered mark-to-market losses, investors redeem, and the fund must *cut* its position rather than add to it. The corrective capital flees exactly when it is most needed. This is the heart of the Shleifer-Vishny model and explains why arbitrage capital is "slow-moving."

### 3. Funding, margin, and leverage constraints

Arbitrage positions are financed. A widening mispricing triggers [[margin]] calls; rising haircuts and funding costs can force deleveraging (a "margin spiral"). Short positions can be subject to recall, hard-to-borrow fees, or forced buy-ins. When funding dries up market-wide (e.g., 2008), even riskless arbitrages like covered-interest parity or on-the-run/off-the-run Treasury spreads blew out because nobody had balance sheet to put on the trade.

### 4. Short horizons

Arbitrageurs do not have infinite patience. Capital has a cost, investors have memories, and risk managers cut positions that bleed. A trade that converges "eventually" is useless if "eventually" is past the arbitrageur's tolerance. Convergence timing risk is itself a limit.

### 5. Fundamental / model risk

The "arbitrage" may not be a true arbitrage at all — the apparent mispricing may reflect a risk or information the arbitrageur is missing, or the fair-value model may be wrong. Shorting an "overvalued" stock that then triples on a genuine fundamental surprise is not a noise-trader loss; it is being wrong. Distinguishing the two ex ante is hard.

### 6. Transaction and implementation costs

Bid-ask spreads, commissions, borrow costs, taxes, and [[market-impact]] all erode or eliminate small mispricings. A 30 bps mispricing is not exploitable if the round-trip cost is 40 bps. Costs set a "no-trade band" around fair value inside which mispricing is rationally ignored.

## Summary table

| Limit | Mechanism | Who/what it constrains | Classic example |
|---|---|---|---|
| Noise-trader risk | Irrational flow pushes price further from value before convergence | Short-horizon, leveraged arbitrageurs | Dot-com shorts blown out 1999-2000 |
| Agency / slow-moving capital | Redemptions hit after losses, forcing position cuts at the worst time | Hedge funds, managed money | LTCM 1998; quant quake Aug 2007 |
| Funding & margin | Margin spirals, borrow recalls, haircut increases | Levered relative-value books | 2008 CIP and Treasury basis blowouts |
| Short horizon | Limited patience; cost of carrying capital | All professional arbitrage | Closed-end fund discounts persisting for years |
| Fundamental risk | "Mispricing" is actually a missed risk or wrong model | Anyone fading apparent value | Shorting a stock that re-rates correctly |
| Transaction costs | Spreads, borrow, impact, taxes | Small-edge, high-turnover trades | Sub-cost index/ETF micro-mispricings |

## Worked example (illustrative)

*Hypothetical, round numbers, for illustration only.*

Two near-identical assets — call them A and B — should trade at parity (e.g., the same company's [[twin-shares|Royal Dutch / Shell-style]] dual listings, a textbook limits-to-arbitrage case). Fundamentals say A = B. The market prices A at 100 and B at 115 — a 15% mispricing with no fundamental basis.

A naive efficient-markets view: arbitrageurs short B, buy A, and the 15% closes immediately. The limits-to-arbitrage view:

- The arbitrageur puts on the trade at a 15% gap with, say, 5x leverage.
- Noise traders keep buying B; the gap widens to 25%. The position is now down ~50% on a mark-to-market basis.
- Investors in the arbitrageur's fund see the loss and redeem 30% of capital. The risk manager cuts the position to stay within limits — *selling A and buying back B at the worst possible prices*, pushing the gap wider still.
- The convergence the arbitrageur predicted *does* eventually happen 18 months later — but by then they have been stopped out. Being right about value was not enough; the *path* and the *funding* killed the trade.

The lesson: the mispricing was real, the analysis was correct, and the trade still lost money. That gap between "correct" and "profitable" is exactly what limits to arbitrage describes — and it is why such gaps persist for outsiders to see.

## How traders use this

- **Set realistic expectations for "free money."** If you find an apparent mispricing, the first question is *why has nobody else closed it?* Usually the answer is a limit to arbitrage (borrow cost, capacity, model risk), not that you alone are smart. See [[edge-taxonomy]] and [[failure-modes]].
- **Size for the path, not the destination.** Because convergence is uncertain in timing, size relative-value trades so a 2-3x adverse widening does not force liquidation. Use [[position-sizing]] and keep dry powder to *add* into widening rather than being forced to cut.
- **Exploit other arbitrageurs' constraints.** Strategies that *provide* liquidity when constrained arbitrageurs are forced to dump (forced selling, deleveraging, fire sales) are a structural edge — see [[edge-taxonomy]] "structural" and "risk-bearing." The limit on one trader is the opportunity for a better-capitalized one.
- **Treat persistent anomalies as compensated risk, not free lunch.** A factor that survives decades (value, momentum, low-vol) likely persists *because* arbitraging it is risky or costly. The premium is partly payment for bearing that limit. See [[anomalies-overview]].
- **Watch funding conditions as a regime signal.** When funding tightens market-wide, *all* relative-value spreads widen together regardless of fundamentals — a predictable consequence of synchronized limits to arbitrage.

## Pitfalls

- **Confusing a limit to arbitrage with a free edge.** The mispricing persists because it is *hard* to capture, not because you found something others missed. The difficulty is the whole story.
- **Underestimating noise-trader risk.** "It must converge" ignores that the path can bankrupt you first. Convergence is a destination, not a guarantee about the journey.
- **Ignoring the agency channel in your own book.** If you trade outside capital, *you* are subject to redemption-after-losses dynamics. Your own investors are a limit to your arbitrage.
- **Assuming small mispricings are exploitable.** Below the round-trip cost band (spread + borrow + impact + tax), a "mispricing" is just noise you cannot monetize.
- **Treating fundamental risk as noise-trader risk.** If you keep losing on a "value" short, consider that the market may be right and your model wrong. Limits-to-arbitrage protects correct analyses; it does not rescue incorrect ones.

## Sources

- Shleifer, A. & Vishny, R. (1997). "The Limits of Arbitrage." *Journal of Finance*, 52(1) — the canonical paper; agency and slow-moving-capital channels
- De Long, J.B., Shleifer, A., Summers, L. & Waldmann, R. (1990). "Noise Trader Risk in Financial Markets." *Journal of Political Economy* — formal noise-trader-risk model
- Gromb, D. & Vayanos, D. (2010). "Limits of Arbitrage." *Annual Review of Financial Economics* — survey of the literature and funding-constraint extensions
- Lamont, O. & Thaler, R. (2003). "Can the Market Add and Subtract? Mispricing in Tech Stock Carve-outs" (3Com/Palm) — a clean empirical demonstration
- Mitchell, M., Pulvino, T. & Stafford, E. (2002). "Limited Arbitrage in Equity Markets." *Journal of Finance* — twin-shares and negative-stub mispricings

General market knowledge; no specific wiki source ingested yet.

## Related

- [[arbitrage]] — the idealized version this concept qualifies
- [[noise-trader-risk]] — the central risk that limits arbitrage
- [[efficient-market-hypothesis]] — the theory limits-to-arbitrage challenges
- [[edge-taxonomy]] — where structural and behavioral edges come from
- [[anomalies-overview]] — anomalies persist precisely because arbitrage is limited
- [[reflexivity]] — Soros's complementary view of self-reinforcing mispricing
- [[short-selling]] — short constraints are a key limit
- [[margin]] — funding/margin spirals as a limit
- [[failure-modes]] — how being "right but broke" kills relative-value trades
- [[behavioral-finance]] — the source of the mispricings arbitrage fails to fully correct

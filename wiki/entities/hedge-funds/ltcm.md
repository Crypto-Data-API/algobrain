---
title: "Long-Term Capital Management (LTCM)"
type: entity
created: 2026-04-06
updated: 2026-06-10
status: good
tags: [company, history, leverage, arbitrage, risk-management]
aliases: ["Long-Term Capital Management", "LTCM"]
entity_type: fund
founded: 1994
headquarters: "Greenwich, Connecticut, USA"
related: ["[[leverage]]", "[[arbitrage]]", "[[risk-management]]", "[[federal-reserve]]", "[[nassim-taleb]]", "[[george-soros]]", "[[book-when-genius-failed]]", "[[tail-risk]]", "[[liquidity]]", "[[value-at-risk]]", "[[2008-global-financial-crisis]]", "[[fat-tails]]", "[[pairs-trading]]"]
---

# Long-Term Capital Management (LTCM)

Long-Term Capital Management was a hedge fund that collapsed spectacularly in 1998, nearly triggering a systemic financial crisis. Founded by bond trader John Meriwether and staffed by Nobel Prize-winning economists Myron Scholes and Robert Merton, LTCM's failure remains the definitive cautionary tale about [[leverage]], model overconfidence, and [[tail-risk]]. The full story is documented in Roger Lowenstein's *When Genius Failed* (Source: [[book-when-genius-failed]]).

## Overview

LTCM launched in February 1994 with $1.25 billion in capital — the largest hedge fund launch to that date — and employed convergence [[arbitrage]] strategies: betting that spreads between related securities (on-the-run vs. off-the-run Treasuries, interest rate swaps, mortgage-backed securities, European convergence bonds) would narrow to their historical means. The strategies appeared low-risk individually, but LTCM amplified returns through extreme [[leverage]], reaching a ratio of roughly 25:1 on balance sheet (about $4.7 billion of capital against ~$125 billion of assets in early 1998) and far higher on a notional basis through [[derivatives]] — over $1 trillion in off-balance-sheet swap and option notional.

The partnership roster was unmatched: founder **John Meriwether** (former head of bond arbitrage at Salomon Brothers), **Myron Scholes** and **Robert C. Merton** (who shared the 1997 Nobel Prize in Economics for option-pricing theory while partners at the fund), and **David Mullins** (former Vice Chairman of the [[federal-reserve|Federal Reserve]]). This pedigree allowed LTCM to borrow from major banks at near-zero haircuts — a key enabler of the leverage that destroyed it.

## The Collapse

The fund generated stellar net returns from 1994-1997 (roughly 21%, 43%, 41%, and 17% annually, after fees). At the end of 1997 it returned $2.7 billion of capital to outside investors while keeping positions largely unchanged — mechanically increasing leverage. Then on August 17, 1998, Russia defaulted on its domestic government debt (GKOs) and devalued the ruble. Global markets panicked, and the "flight to quality" caused spreads to widen dramatically — the exact opposite of LTCM's bets, simultaneously across supposedly uncorrelated markets. Positions that models said would lose a few hundred million in a worst case lost billions (Source: [[book-when-genius-failed]]). LTCM lost $1.85 billion in August 1998 alone, including $553 million on Friday August 21. By late September 1998, LTCM had lost $4.6 billion — over 90% of its capital — and its ~$125 billion balance sheet (plus >$1 trillion of derivatives notional) threatened counterparties across the financial system.

On September 23, 1998, the [[federal-reserve|Federal Reserve]] Bank of New York orchestrated a $3.625 billion recapitalization by a consortium of 14 major banks (Bear Stearns famously declined to participate) to prevent a disorderly liquidation that could have cascaded through global markets. No public money was injected — the Fed convened the bailout but did not fund it. The consortium took 90% of the fund's equity; existing partners were largely wiped out.

## Aftermath

The portfolio was unwound in an orderly fashion and the fund was liquidated by early 2000; the consortium banks recovered their capital. Meriwether founded a successor fund, JWM Associates, in 1999 — it ran similar relative-value strategies at lower leverage and was itself wound down in 2009 after ~44% losses in the [[2008-global-financial-crisis]], a second demonstration that the strategy's tail risk was structural, not a one-off. The LTCM episode prompted the President's Working Group report on hedge funds and leverage (1999) and remains the canonical case study in counterparty risk management at every major bank.

## Trading Relevance

LTCM proves that models based on historical correlations fail during crises, that [[leverage]] transforms manageable losses into existential ones, and that [[liquidity]] disappears precisely when you need it most (Source: [[book-when-genius-failed]]). Specific lessons traders still draw from it:

- **Correlations go to one in stress.** LTCM's positions were diversified across geographies and asset classes, but they were all the same trade — short liquidity premium, short volatility, long convergence. In August-September 1998 they all lost together.
- **[[value-at-risk|VaR]] understates [[fat-tails|fat-tailed]] risk.** LTCM's models put the August 1998 loss at many standard deviations beyond plausibility; the event happened anyway. [[nassim-taleb]]'s [[black-swan]] critique of Gaussian risk models uses LTCM as Exhibit A.
- **Crowded trades unwind violently.** Rival desks held similar positions and knew LTCM's book; once trouble started, front-running and forced deleveraging by copycats amplified the spread widening.
- **Size and leverage destroy the exit.** Positions sized far beyond market depth cannot be cut without moving the market against you — the same mechanism seen later in the [[2008-global-financial-crisis]] and the [[ftx-collapse]].

## Related

- [[book-when-genius-failed]] — the definitive account
- [[leverage]] — the amplifier
- [[arbitrage]] — the strategy family (convergence / relative value)
- [[pairs-trading]] — retail-scale cousin of convergence trades
- [[risk-management]] — the discipline LTCM's failure reshaped
- [[value-at-risk]] — the risk model that failed
- [[tail-risk]] / [[fat-tails]] — the statistical blind spot
- [[liquidity]] — the resource that vanished
- [[federal-reserve]] — orchestrated the bailout
- [[nassim-taleb]] — leading critic of LTCM-style model confidence
- [[2008-global-financial-crisis]] — the rhyme a decade later

## Sources

- Lowenstein, Roger. *When Genius Failed: The Rise and Fall of Long-Term Capital Management* (Random House, 2000). ([[book-when-genius-failed]])
- Federal Reserve Bank of New York, statement on the LTCM private-sector recapitalization, September 23, 1998.
- President's Working Group on Financial Markets, "Hedge Funds, Leverage, and the Lessons of Long-Term Capital Management" (April 1999): https://home.treasury.gov/system/files/276/Report-HedgeFunds-1999.pdf
- Jorion, Philippe. "Risk Management Lessons from Long-Term Capital Management." *European Financial Management* 6 (2000): 277-300.
- GAO, "Long-Term Capital Management: Regulators Need to Focus Greater Attention on Systemic Risk" (GAO/GGD-00-3, October 1999).
- Key figures (founding capital $1.25B; 1994-97 net returns ~21/43/41/17%; ~25:1 balance-sheet leverage; $4.6B loss; $3.625B 14-bank bailout on 1998-09-23) cross-checked against Lowenstein (2000) and Jorion (2000), reviewed 2026-06-10.

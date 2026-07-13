---
title: "Zero Lower Bound"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [macro, risk-management, volatility]
aliases: ["Zero Lower Bound", "ZLB", "Effective Lower Bound", "ELB"]
related: ["[[zero-interest-rate-policy]]", "[[liquidity-trap]]", "[[quantitative-easing]]", "[[forward-guidance]]", "[[monetary-policy]]", "[[interest-rates]]", "[[taylor-rule]]", "[[deflation]]", "[[real-interest-rate]]", "[[duration]]", "[[convexity]]", "[[risk-parity]]"]
domain: [portfolio-theory, market-microstructure]
prerequisites: ["[[interest-rates]]", "[[monetary-policy]]"]
difficulty: intermediate
---

The **zero lower bound (ZLB)** is the constraint that a central bank's conventional policy tool — the short-term nominal interest rate — cannot be cut far below zero, because holders of money can always earn a nominal return of zero simply by holding physical cash. When a central bank wants to ease policy further but has already cut rates to (or near) zero, it hits the ZLB and must switch to **unconventional policy** such as [[quantitative-easing]] and [[forward-guidance]]. In practice the binding constraint is slightly below zero — the **effective lower bound (ELB)** — because storing, insuring, and transacting in physical cash carries small costs, which is why several central banks (ECB, BoJ, SNB, Riksbank, Danmarks Nationalbank) successfully pushed policy rates modestly negative in the 2010s.

## Why the bound exists

Cash is a zero-yield bearer asset. If a central bank set deposit rates deeply negative, depositors would convert balances to banknotes to avoid the penalty, draining the banking system. The cost of hoarding cash (storage, security, insurance, inconvenience) creates a small wedge, so the *effective* floor is mildly negative rather than exactly zero — empirically estimated around -0.5% to -1.0% before large-scale cash hoarding becomes attractive. The ZLB therefore truncates the policy rule: a [[taylor-rule]] prescription that calls for, say, a -4% policy rate during a deep recession simply cannot be implemented through the conventional rate channel.

## Macroeconomic consequences

- **Monetary policy loses traction.** With the policy rate pinned at zero and inflation falling, the *real* rate (nominal minus expected inflation) can rise exactly when the economy needs lower real rates — a perverse tightening. In a severe case this becomes a [[liquidity-trap]], where additional reserves are hoarded rather than lent and conventional easing stops stimulating demand.
- **Deflation risk.** Persistent below-target inflation or [[deflation]] raises real debt burdens (debt-deflation) and entrenches low inflation expectations, which is why the BoJ has spent decades near the ZLB.
- **Fiscal policy becomes relatively more powerful.** Fiscal multipliers are larger at the ZLB because stimulus is not offset by the central bank raising rates.

### Worked Example — The Real-Rate Trap

The [[real-interest-rate|real rate]] is the nominal rate minus expected inflation: `r = i − π`. Suppose a downturn pushes expected inflation from +2% to −1% while the nominal policy rate is already pinned at the floor (`i ≈ 0`):

| Scenario | Nominal rate `i` | Expected inflation `π` | Real rate `r = i − π` |
|---|---|---|---|
| Normal slack | 0% | +2% | −2% (stimulative) |
| Slipping toward deflation | 0% (can't cut) | −1% | **+1% (tightening!)** |

The real rate *rose* by 3 percentage points precisely when the economy needed easing — a self-reinforcing spiral, because higher real rates depress demand, which deepens deflation, which raises real rates again. This is the core mechanism behind the [[liquidity-trap]] and why central banks at the ZLB fight so hard to keep inflation *expectations* anchored: away from the bound a rate cut breaks the spiral; at the bound that lever is gone. *(Numbers illustrative.)*

## Unconventional tools used at the ZLB

| Tool | Mechanism | Channel | Main market effect |
|---|---|---|---|
| **[[quantitative-easing]] (QE)** | Large-scale purchases of government bonds and other assets | Compresses long-term yields and term premia; expands the balance sheet | Bull-flattens / steepens the curve; lifts long-duration assets |
| **[[forward-guidance]]** | Committing to keep rates low for an extended period (calendar- or state-based) | Lowers the *expected path* of short rates → lower long yields | Anchors front end; lowers rate volatility |
| **Negative interest rate policy (NIRP)** | Charging banks on excess reserves | Pushes the effective floor slightly below zero | Front-end yields go negative; pressures bank margins |
| **Yield curve control (YCC)** | Pegging a longer-maturity yield (e.g. the BoJ's 10-year JGB target) | A hybrid of QE and forward guidance | Caps a specific maturity; can require unlimited buying to defend |

These tools share a common aim — easing financial conditions when the conventional rate lever is exhausted — by working on the *long end* and on *expectations* rather than the overnight rate. Their effectiveness and exit dynamics are contested: QE can inflate asset prices more reliably than it stimulates the real economy, and unwinding (quantitative tightening, abandoning YCC) can be disruptive, as the strain on the BoJ's YCC peg in 2022-2023 illustrated.

## Historical episodes

- **Japan (1999–present):** the original and longest ZLB experience; BoJ cut to ~0% in 1999, pioneered QE in 2001, and adopted YCC in 2016.
- **United States (Dec 2008–Dec 2015, and Mar 2020–Mar 2022):** the [[federal-reserve|Fed]] cut to 0–0.25% in the Global Financial Crisis and again during COVID, deploying multiple QE rounds and forward guidance.
- **Eurozone, Switzerland, Sweden, Denmark (2014–2022):** pushed policy rates negative, demonstrating the ELB sits somewhat below zero.

The 2022–2023 global inflation surge lifted most major economies well clear of the ZLB, but the episode reinforced the policy lesson that the bound can re-bind quickly in the next deep downturn, keeping QE and forward guidance in the standard toolkit.

## Trading and portfolio relevance

- **Bond convexity and duration:** near the ZLB, short-rate volatility is suppressed and the yield curve typically steepens via the long end as QE compresses the front. Duration becomes the dominant return driver; see [[convexity]] and [[us-treasury-bonds]].
- **Equity valuations:** a pinned discount rate plus QE-driven liquidity historically inflates long-duration / growth equity multiples (low rates raise the present value of distant cash flows). Reversal *off* the ZLB (2022) crushed those same multiples.
- **Correlation regime shifts:** prolonged ZLB periods can flip the stock–bond correlation, weakening the classic 60/40 hedge — directly relevant to [[risk-parity]] and [[all-weather-portfolio]] construction (see [[correlation-regime]]).
- **Carry and FX:** with policy rates clustered near zero across DM, [[interest-rate-parity]] carry differentials compress and capital chases yield into EM and credit (a [[capital-flows]] driver).
- **Tail hedging:** because the central bank's conventional cushion is gone at the ZLB, downside shocks can be larger and faster, raising the value of convexity-based hedges (see [[dragon-portfolio]]).

## Related

- [[zero-interest-rate-policy]] — the policy stance of holding the rate at (near) zero; ZLB is the constraint, ZIRP the response
- [[liquidity-trap]] — the demand-side failure that can accompany the ZLB
- [[quantitative-easing]], [[forward-guidance]] — the principal escape tools
- [[taylor-rule]] — the policy rule the ZLB truncates
- [[monetary-policy]], [[interest-rates]], [[deflation]]

## Sources

- Krugman, P. (1998). "It's Baaack: Japan's Slump and the Return of the Liquidity Trap." *Brookings Papers on Economic Activity.*
- Eggertsson, G. & Woodford, M. (2003). "The Zero Bound on Interest Rates and Optimal Monetary Policy." *Brookings Papers on Economic Activity.*
- Bernanke, B. (2020). "The New Tools of Monetary Policy." *American Economic Review* (AEA Presidential Address).
- Federal Reserve Bank of San Francisco — Economic Letters on the effective lower bound and unconventional policy.
- Bank for International Settlements — research on negative interest rate policy and the effective lower bound.
- General market knowledge; no specific wiki source ingested yet beyond the above references. Current policy rates and spreads are intentionally left qualitative.

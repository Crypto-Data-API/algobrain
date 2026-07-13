---
title: "Pensions"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [portfolio-theory, bonds, risk-management, education]
aliases: ["Pension", "Pension Fund", "Defined Benefit", "Defined Contribution", "Retirement Income"]
domain: [portfolio-theory, market-microstructure]
prerequisites: ["[[compounding]]", "[[duration-risk]]"]
difficulty: intermediate
related: ["[[superannuation]]", "[[smsf]]", "[[duration-risk]]", "[[ldi]]", "[[liability-driven-investing]]", "[[treasuries]]", "[[move-index]]", "[[compounding]]", "[[diversification]]"]
---

A **pension** is a long-term arrangement that provides income in retirement, funded by contributions invested over a working life. Pension **funds** — the institutional pools that manage these assets — are among the largest investors in global markets, and their structural constraints (long liabilities, regulatory funding rules, [[duration-risk|duration]] matching) make them important, occasionally market-moving, participants. Understanding how pensions are structured explains a major source of demand for bonds, equities, and long-duration assets, and a recurring source of systemic fragility.

## Two core designs

| Design | Who bears investment risk | How it pays out |
|---|---|---|
| **Defined Benefit (DB)** | The sponsor (employer/state) | A formula-based guaranteed income (e.g. % of final salary × years served) |
| **Defined Contribution (DC)** | The individual | Whatever the invested pot is worth at retirement |

The global shift over the last 40 years has been from **DB to DC** — transferring investment and longevity risk from employers to individuals. Australia's [[superannuation]] system is a large, compulsory DC scheme; the US 401(k) and IRA are DC; traditional corporate and public-sector "final salary" plans are DB.

The **public pension** (state pension / Age Pension / Social Security) is a separate, usually pay-as-you-go pillar funded by current taxpayers rather than pre-funded investments.

A useful way to see the three pillars side by side:

| Pillar | Funding model | Who pays | Investment risk | Example |
|---|---|---|---|---|
| **Pillar 1 — Public** | Pay-as-you-go (PAYG) | Current taxpayers | State (demographic) | US Social Security, AU Age Pension, UK State Pension |
| **Pillar 2 — Occupational** | Pre-funded | Employer / employee | Sponsor (DB) or individual (DC) | Corporate DB plans, [[superannuation]], 401(k) |
| **Pillar 3 — Personal** | Pre-funded | Individual | Individual | IRA, [[smsf|SMSF]], personal pension |

## Funding ratio — the single most important DB number

A DB plan's **funding ratio** (or funded status) is the ratio of plan assets to the present value of its liabilities:

$$\text{Funding ratio} = \frac{\text{Plan assets}}{\text{Present value of liabilities}}$$

- **>100% (overfunded/surplus)** — assets exceed liabilities; the sponsor may de-risk into bonds.
- **=100% (fully funded)** — assets exactly match the discounted liabilities.
- **<100% (underfunded/deficit)** — a shortfall the sponsor must eventually plug from cash flow.

The liability is discounted at a rate tied to long-bond yields, so **rising rates *shrink* the present value of liabilities** (good for funding) while **falling rates inflate them** (bad). This is why a DB plan is, in economic terms, short duration on its liabilities and must buy [[duration-risk|duration]] to hedge.

**Worked example.** A plan holds $900m of assets against liabilities with a present value of $1,000m at a 4% discount rate. Funding ratio = 900 / 1,000 = **90% (a $100m deficit)**. Now suppose long yields rise 100bp to 5%. If the liabilities have a duration of ~15 years, their present value falls by roughly 15% to ~$850m. If the plan's assets are *not* duration-matched and barely move, the new ratio is 900 / 850 ≈ **106%** — the plan swings from deficit to surplus purely on the rate move. The mirror image (rates falling) is the nightmare: an unhedged plan's liabilities balloon while assets lag. This volatility is exactly what [[liability-driven-investing|LDI]] exists to neutralise.

## Pension funds as market participants

- **Bond demand and duration matching.** DB funds owe long-dated, often inflation-linked liabilities. To hedge them they buy long-dated government bonds and use derivatives, making them structural buyers of [[treasuries|duration]]. This anchors long-end demand and influences the yield curve.
- **Liability-Driven Investing (LDI).** DB funds increasingly run [[liability-driven-investing|LDI]] programs: leveraged exposure to long bonds (via swaps/repo) to match the present value of liabilities, freeing capital for return-seeking assets. LDI is efficient in calm markets but introduces hidden leverage.
- **Equity and alternatives allocation.** DC defaults and DB return-seeking sleeves are giant, steady buyers of equities, real estate, infrastructure, and private markets — a structural bid that underpins long-run equity demand.
- **Rebalancing flows.** Large funds rebalance to policy weights, selling what rose and buying what fell — a stabilizing (mean-reverting) force most of the time, and a quarter-/year-end flow worth being aware of.

A stylised glide between the two regimes:

| Phase | Typical posture | Asset-mix tilt | Market footprint |
|---|---|---|---|
| **Return-seeking** (underfunded / young plan) | Reach for return | Heavy equities, real estate, infrastructure, private markets | Structural equity bid; risk-on demand |
| **De-risking / hibernation** (well-funded / mature plan) | Lock in surplus | Shift to long bonds + [[liability-driven-investing\|LDI]] hedges | Structural long-end bond bid; liability-matching |

As a DB plan's members age and the plan matures (or once it reaches surplus), it tends to **de-risk** — rotating from equities into liability-matching bonds. In aggregate this is a slow but persistent rotation that pension consultants call the "glide path."

## The trading relevance: when pensions break

Pension structure is normally a slow, stabilizing force — but its hidden leverage can become a systemic accelerant:

- **The 2022 UK gilt / LDI crisis.** When UK gilt yields spiked in September–October 2022 (after the mini-budget), leveraged LDI funds faced margin calls on their bond hedges. To raise cash they sold *more* gilts, pushing yields higher in a doom loop, until the Bank of England intervened with emergency gilt purchases. This is the textbook case of pension-fund leverage converting a rates move into a fire-sale spiral — and it coincided with a spike in the [[move-index|MOVE Index]].
- **Forced sellers, not opportunists.** In stress, pension/LDI funds sell because rules and margin require it, not because of price views. Traders model this as predictable, price-insensitive supply — a setup for liquidity provision (at a fat premium) or for staying out of the way.
- **Duration as the key risk.** A pension fund's health is dominated by the gap between asset duration and liability duration. Rising long-end rate volatility (high [[move-index|MOVE]]) is when DB funding ratios and LDI plumbing are most stressed.
- **DC flows = passive bid.** DC contributions (like [[superannuation]]) are automatic, regular, and price-insensitive — a continuous [[dollar-cost-averaging|dollar-cost-averaging]] flow into default funds, dominated by [[index-fund|index]] and target-date strategies.

## How traders and allocators use this

- **Trade the forced seller, not the view.** When an LDI doom loop or a quarter-end de-risking flow is in motion, the supply is price-insensitive and mechanical. The edge is to *provide liquidity at a premium* (buy the gilts/equities being dumped) or simply *stand aside* until the forced selling exhausts — never to fade a fundamental thesis you don't have.
- **Watch rate volatility, not just the level.** DB funding ratios and LDI collateral plumbing are most fragile when long-end *volatility* spikes. A surging [[move-index|MOVE Index]] is a leading tell that pension-hedging machinery may be under collateral stress, independent of the direction of yields.
- **Anticipate de-risking demand.** A reflationary backdrop that pushes funding ratios into surplus tends to trigger pension rotation *out of equities and into long bonds* — a structural bid for [[treasuries|duration]] and a headwind for the equity risk premium at the margin.
- **Calendar awareness.** Large pension and target-date funds rebalance toward policy weights at month-, quarter-, and year-end. After a big divergence between stocks and bonds, the expected rebalance can create a predictable, well-telegraphed flow (e.g. "sell the outperformer") that desks position around.
- **Demographics as a slow tide.** An ageing population means more plans entering the pay-out (de-accumulation) phase — net sellers of assets over decades — a slow structural factor in long-run return assumptions.

## Common pitfalls and risks

- **Hidden leverage.** LDI and repo-funded duration hedges look benign in calm markets but embed leverage that turns a rate move into a margin spiral (see the 2022 gilt crisis below).
- **Discount-rate sensitivity.** Reported funding ratios swing violently with the chosen discount rate; a "fully funded" plan can flip to deficit on a modest fall in long yields. Beware comparing funding ratios computed on different discount-rate conventions (accounting vs. regulatory vs. economic).
- **Longevity risk.** If members live longer than assumed, liabilities are understated — a slow, one-directional drag that DC schemes push entirely onto the individual.
- **Procyclical de-risking.** Plans that de-risk *after* equities have rallied lock in gains but can also crystallise losses if forced to sell into a drawdown to meet collateral or benefit payments.
- **Sponsor covenant risk (DB).** A DB promise is only as good as the sponsor's ability to fund deficits; corporate insolvency throws the plan onto a backstop (e.g. the US PBGC, the UK PPF) at reduced benefit levels.

## Related

- [[superannuation]] — Australia's compulsory defined-contribution pension system
- [[smsf]] — self-managed Australian retirement vehicle
- [[liability-driven-investing]] / [[ldi]] — the leveraged hedging at the heart of the 2022 crisis
- [[duration-risk]] — the dominant pension-fund exposure
- [[move-index]] — rate-volatility gauge that flags LDI stress
- [[treasuries]] — the core duration-matching asset
- [[compounding]] — the engine of long-horizon pension saving

## Sources

- OECD, *Pensions at a Glance* and *Pension Markets in Focus* (annual)
- Bank of England, *Financial Stability Report* and statements on the September–October 2022 LDI intervention
- Investment Company Institute, *Defined Contribution Plan and IRA* research
- Willis Towers Watson / Thinking Ahead Institute, *Global Pension Assets Study*

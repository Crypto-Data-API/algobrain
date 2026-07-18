---
title: "Terra Luna 2.0 Fork Arbitrage (May 2022)"
type: news
created: 2026-04-27
updated: 2026-06-12
status: good
tags: [crypto, history, hard-fork, airdrop, terra, stablecoins, cosmos]
aliases: ["Luna 2.0 Fork", "Terra Revival", "LUNC Airdrop", "Terra Classic Split"]
event_date: 2022-05-28
markets_affected: [crypto]
impact: high
verified: true
sources_count: 5
related: ["[[hard-fork]]", "[[fork-airdrop-triangulation]]", "[[2022-09-ethereum-merge-fork-arbitrage]]"]
---

# Terra Luna 2.0 Fork Arbitrage (May 2022)

On **May 28, 2022**, the Terra ecosystem executed Governance Proposal 1623 — relaunching as **"Terra 2.0"** (LUNA, the new chain) while abandoning the existing chain (renamed **Terra Classic / LUNC** with stablecoin renamed **USTC**). The fork was a defensive response to the catastrophic UST de-peg and Luna death-spiral of May 7-12, 2022 that wiped out ~$60B in value within 5 days. Unlike a standard chain-split fork, this was a **chain-swap** with an **eligibility-cliff airdrop** — the new Luna 2.0 was distributed to **specific** historical holder snapshots (pre-attack and post-attack), creating one of the most operationally complex fork-arbitrage events in crypto history.

## Background

Terra's algorithmic stablecoin UST relied on a mint/burn arbitrage with LUNA: 1 UST always redeemable for $1 of LUNA. This was supported by Anchor Protocol's 19.5% deposit rate which absorbed most of UST issuance. As of May 2022, UST market cap was ~$18B; Luna was ~$80, with $40B market cap.

**Timeline:**
- **May 7, 2022:** Anchor TVL outflows accelerate; large UST sells observed on Curve.
- **May 8-9, 2022:** UST de-pegs to $0.97-$0.95; Luna falls to $60.
- **May 10-12, 2022:** "Death spiral" — UST falls to $0.10; LUNA hyperinflates from supply expansion (mint mechanism creates supply each time UST is burned). Luna falls from $60 to $0.0001 in 72 hours.
- **May 13, 2022:** Terra blockchain halted by validators; resumed shortly after.
- **May 16, 2022:** Do Kwon proposes "Terra Ecosystem Revival Plan" via Governance Proposal 1623.
- **May 25, 2022:** Proposal passes (65% approval); Luna 2.0 chain confirmed.
- **May 28, 2022:** New Luna 2.0 chain launches (genesis block); old chain renamed Luna Classic (LUNC).

## The Airdrop Allocation

This is the critical structural detail. Terra 2.0 distributed 1B Luna 2.0 tokens via **eligibility-cliff snapshots**:

| Bucket | Allocation | Eligible holders |
|--------|------------|-----------------|
| Pre-attack LUNA holders (snapshot May 7 23:59 UTC) | 35% | LUNA holders before depeg started |
| Pre-attack aUST holders | 10% | Anchor depositors before depeg |
| Post-attack LUNA holders (snapshot May 27 23:59 UTC) | 10% | LUNA holders after collapse |
| Post-attack UST holders | 10% | UST holders after collapse |
| Post-attack LUNA <10k holders | additional weighting | retail-friendly bucket |
| Community Pool | 25% | Future development |
| Dev allocation | varies | Vesting |

The bifurcated snapshot was the operational center of gravity. **Pre-attack holders received the bulk of the airdrop** (45% combined); post-attack buyers received only ~20%, even though they were the ones still holding the asset at fork time. This created a sophisticated market for **OTC pre-attack-snapshot holdings**.

## The Trade

### Trade 1: Buy LUNC at $0.0001 for the post-attack snapshot

After Luna collapsed to ~$0.0001 (May 12-15), the question for arb desks was: **what is the post-attack LUNA snapshot allocation worth?** Modeling required estimating Luna 2.0 launch price (consensus: $5-15) × per-LUNC airdrop ratio (variable, depending on total supply at snapshot).

Post-attack LUNC supply ballooned to **~6.5 trillion LUNC** (from ~340M pre-attack — a >19,000x dilution). Per-LUNC Luna 2.0 entitlement was therefore minuscule: ~0.0000015 Luna 2.0 per LUNC.

Math: at $10 launch, that's $0.000015 of Luna 2.0 per LUNC. Buying LUNC at $0.0001 implied Luna 2.0 launching at $66 to break even — way above realistic estimates. **Naive LUNC buying for the airdrop was unprofitable.**

The smarter trade: **buy LUNC pre-attack snapshot data** (holders before May 7) **OTC**.

### Trade 2: OTC pre-attack LUNA snapshot holdings

Pre-attack snapshot holders had a much better ratio: LUNA pre-attack supply was ~340M; the 35% pre-attack bucket was 350M Luna 2.0. So **~1.03 Luna 2.0 per pre-attack LUNA**. At $10 launch, $10.30 per pre-attack LUNA. Pre-attack LUNA had been worth $80; the airdrop alone was ~13% of the lost value.

Sophisticated OTC desks bought claims on pre-attack-snapshot wallets at 30-50% discount to airdrop fair value. Because the airdrop was non-transferable until claim, this required **trust-based agreements** with wallet owners (or escrow via Vesta, Anchorage). $50-200M in OTC volume during May 20-30, 2022.

### Trade 3: Short Luna 2.0 launch

Pre-launch IOU futures were thinly traded ($1-5 range, illiquid). Luna 2.0 launched May 28 with significant cross-exchange variance — initial prints ranged widely (roughly $5 up to the high-teens on thin books) before most venues converged near $5-8 within 24 hours; within 30 days, ~$1.50.

The reverse-IOU trade (short the IOU at $5, deliver at launch from airdrop allocation, cover the launch sell-off) was profitable in absolute terms but limited by IOU market depth.

### Trade 4: Long ATOM / short LUNA pair

Cosmos's ATOM token (Terra was a Cosmos chain) initially crashed in sympathy. Smart traders bought ATOM at $7-8 in mid-May (down from $25 pre-Terra collapse) and shorted LUNA into the death spiral. ATOM recovered to $11-12 by early June; LUNA went to zero. 200%+ return on the pair in 4 weeks.

### Trade 5: USTC speculation (failed)

After the depeg, USTC traded $0.05-0.10. Some speculators bought USTC betting on a community proposal to reactivate the burn mechanism (which would create demand). USTC briefly rallied to $0.05 → $0.10 in late 2022 on speculation but never recovered to $1. **Long-USTC was a high-conviction loss for most retail.**

## Price Action

| Date | LUNA / LUNC | Luna 2.0 | UST / USTC | Notes |
|------|-------------|----------|------------|-------|
| May 7, 2022 | $80 | n/a | $1.00 | Pre-collapse |
| May 9, 2022 | $60 | n/a | $0.98 | Initial depeg |
| May 12, 2022 | $0.0002 | n/a | $0.10 | Death spiral complete |
| May 16, 2022 | $0.0001 | n/a | $0.06 | Do Kwon plan announced |
| May 28, 2022 (fork) | $0.00009 | $5-19 (variable launch) | $0.04 | Luna 2.0 launches; cross-exchange spreads |
| Jun 2, 2022 | $0.00009 | $5 | $0.03 | Luna 2.0 collapses |
| Sep 2022 | $0.00026 | $1.80 | $0.025 | Post-collapse equilibrium |
| End 2024 | $0.00006 | $0.45 | $0.018 | Long-tail decline |

Total Luna ecosystem destruction: ~$60B in market cap; airdrop redistribution: ~$2B in eventual Luna 2.0 value, mostly captured by pre-attack holders.

## Was It Obvious?

**The fork itself: yes, after May 16.** Do Kwon's revival plan was telegraphed publicly and Terra's validator set committed. **The eligibility cliff: only partially obvious.** The pre/post-attack snapshot rules were finalized only days before launch and changed once during governance debate.

The realistic Luna 2.0 launch price was *not* obvious — pre-launch FTX IOUs were thinly traded ($1-5 range) while Luna 2.0's opening prints ranged widely across venues (roughly $5 to the high-teens on thin books before converging near $5-8). The post-launch collapse was, in retrospect, predictable for anyone who had modeled supply dilution and lack of fundamentals.

## Who Made Money?

- **Pre-attack LUNA holders.** Received ~1.03 Luna 2.0 per LUNA, worth $5-18 at peak. Effective ~10-25% recovery on lost value.
- **OTC desks buying pre-attack claims.** $50-200M in volume at 30-50% discount to airdrop fair value.
- **Long-ATOM / short-LUNA pair traders.** 200%+ in 4 weeks.
- **Short-Luna-2.0-launch traders.** Captured the high-teens → $5 collapse via short IOU on FTX.
- **Pre-attack UST holders who claimed properly.** Received Luna 2.0 allocation worth ~5-10% of lost UST value.

## Who Lost Money?

- **Anchor Protocol depositors.** $14B+ in UST principal. Most lost 95-99%; the airdrop recovered ~5-10%.
- **Post-attack LUNC speculators.** Vast majority bought LUNC at $0.0001-0.001 expecting recovery. Most never broke even.
- **Luna 2.0 launch buyers.** Anyone who bought at $18 at launch lost 90% within a month.
- **USTC longs.** Reflexive speculation on stablecoin reactivation; never materialized.
- **Do Kwon and Terraform Labs.** Reputation destroyed; criminal charges in South Korea (extradited 2024) and the US.
- **Sister stablecoin issuers.** UST collapse triggered USDD (Tron), USDN (Waves), DEI (DEUS), MIM (Abracadabra) all losing parity in May 2022 contagion.

## Risks

1. **Eligibility-cliff snapshot ambiguity.** The pre-attack vs post-attack snapshot rules and exact UTC cutoffs were finalized close to fork. Holders had to track multiple deadlines simultaneously.
2. **OTC custody risk.** Pre-attack-snapshot OTC trades required trusting the wallet owner to deliver airdropped Luna 2.0. Some defaulted; legal recourse limited.
3. **Hyperdilution of LUNC.** The 19,000x supply expansion during the death spiral made post-attack LUNC airdrop economics fundamentally unattractive — a non-obvious calculation for retail.
4. **Luna 2.0 launch venue risk.** Bybit, Binance, KuCoin had different launch times and prices. Cross-exchange launch arbitrage required pre-positioned capital on multiple venues.
5. **Regulatory risk.** Terra's stablecoin model was subject to securities/derivatives scrutiny across jurisdictions. SEC enforcement actions began in late 2022.
6. **Operational airdrop risk.** Some claimants reported delays or denied claims. Verified claim rate was ~70-80% of eligible Luna 2.0 supply.

## Lessons for Fork Arbitrage

1. **Death-spiral chain-swaps create eligibility-cliff airdrops.** Distinct from standard hard forks. The "snapshot" is multi-tier and discriminates by holding-time.
2. **Hyperdilution destroys naive recovery trades.** Buying the parent token after collapse for the airdrop is rarely profitable when supply has expanded 1000x+. Math the dilution explicitly.
3. **OTC pre-snapshot claim trading is a real market.** Pre-attack holdings traded at deep discount; sophisticated desks captured the discount with trust-based settlement.
4. **The pre-launch IOU may underprice the launch.** Luna 2.0 IOUs at $1-5 vs initial venue prints of $5-19 — partly the inverse of the [[2022-09-ethereum-merge-fork-arbitrage|ETHW]] case where IOUs over-priced the launch. The asymmetry is event-specific; thin pre-launch markets and exchange-by-exchange opening-print divergence both contributed.
5. **Post-launch collapse is predictable when fundamentals are absent.** Luna 2.0 had no UST burn mechanism, no Anchor demand, no stablecoin product. A pure "narrative recovery" launch typically collapses 70-90% in 30 days. The reverse-IOU short was the high-Sharpe trade.
6. **Defensive forks vs death-spiral forks differ.** [[2020-03-steem-hive-fork-arbitrage|Steem→Hive]] was a defensive fork by a community against an attacker. Terra was a defensive fork by a *team* against systemic failure. The team's accountability differs — Do Kwon's situation was much worse for Luna 2.0 than the Steem witnesses' was for Hive.

## Aftermath

- **2022-2023:** Luna 2.0 traded $0.50-2.00; LUNC traded $0.00006-0.0003 with reflexive burns reducing supply.
- **2023:** Do Kwon arrested in Montenegro on falsified-passport charges; extradition disputes between US and South Korea.
- **2024-2025:** Do Kwon convicted in US on fraud charges (multiple counts); extradition to South Korea ongoing. Terra Classic community continues to operate as a small social DAO.
- **Stablecoin policy:** Terra's collapse drove regulatory action — EU's MiCA stablecoin framework (2024), US Stable Act discussions. Algorithmic stablecoins are de facto banned across most major jurisdictions.

## Related

[[hard-fork]] · [[fork-airdrop-triangulation]] · [[2022-09-ethereum-merge-fork-arbitrage]] · [[2020-03-steem-hive-fork-arbitrage]] · [[stablecoin-depeg-arbitrage]] · [[failure-modes]]

## Sources

- Do Kwon / Terraform Labs: "Terra Ecosystem Revival Plan 2" (May 16, 2022).
- Terra Governance Proposal 1623 (passed May 25, 2022).
- *CoinDesk*: "Terra's $40 Billion Crash" (May 13, 2022).
- US v. Do Kwon, SDNY indictment (March 2023).
- Galaxy Research, "The Terra Aftermath" (June 2022).

---
title: "USDC Depegs During Silicon Valley Bank Collapse (Mar 2023)"
type: news
created: 2026-04-24
updated: 2026-06-12
status: good
tags: [news, crypto, stablecoins, defi, history, depeg, banking, regulation]
event_date: 2023-03-11
markets_affected: [crypto, stablecoins, defi]
impact: high
verified: true
sources_count: 5
related:
  - "[[usdc]]"
  - "[[circle]]"
  - "[[silicon-valley-bank]]"
  - "[[stablecoin-pair-arbitrage]]"
  - "[[depeg-risk]]"
  - "[[2022-05-terra-luna-depeg-arb]]"
---

# USDC Depegs During Silicon Valley Bank Collapse (Mar 2023)

On the night of **Friday, 2023-03-10**, [[circle|Circle]] disclosed that approximately **$3.3 billion** of [[usdc|USDC]]'s cash reserves were stuck at [[silicon-valley-bank|Silicon Valley Bank (SVB)]], which had been seized by the FDIC earlier that day. With US banking infrastructure closed for the weekend and no clarity on whether SVB depositors above the $250K FDIC limit would be made whole, USDC depegged from $1.00, trading as low as **$0.88** on Saturday 2023-03-11 before recovering to ~$0.97 by Sunday and fully repegging by Tuesday 2023-03-14 after the Federal Reserve and Treasury announced a backstop for SVB depositors. The episode is one of the cleanest stablecoin arbitrage opportunities in crypto history — and a textbook example of weekend banking risk in a 24/7 crypto market.

## Timeline

| Date / Time (UTC) | Event |
|---|---|
| 2023-03-08 | SVB announces a $1.75B share sale and $1.8B loss on bond portfolio. Stock crashes after-hours |
| 2023-03-09 | Bank run on SVB; depositors attempt to withdraw $42B in a single day |
| 2023-03-10 ~16:00 | California DFPI closes SVB; FDIC named receiver. SVB is the second-largest US bank failure ever |
| 2023-03-10 ~22:00 | [[circle|Circle]] tweets confirming exposure: **"Silicon Valley Bank is one of six banking partners Circle uses for managing the ~25% of USDC reserves held in cash"** |
| 2023-03-11 ~00:00-04:00 | USDC begins depegging on [[curve-finance|Curve 3pool]] and [[uniswap|Uniswap]]; price falls through $0.95 |
| 2023-03-11 ~12:00 | Circle confirms **$3.3B of $40B USDC reserves** stuck at SVB |
| 2023-03-11 ~14:00 | USDC hits weekend low **~$0.87-0.88** on Curve 3pool; [[usdt|USDT]] trades to **$1.02-1.03** premium as flight-to-quality |
| 2023-03-11 ~17:00 | [[dai|DAI]] depegs to ~$0.90 (DAI was >50% USDC-backed via Maker's Peg Stability Module) |
| 2023-03-12 (Sun) ~22:00 | US Treasury, Fed, and FDIC jointly announce **all SVB depositors made whole**, including uninsured |
| 2023-03-13 (Mon) | USDC recovers to ~$0.99; Coinbase resumes USDC <-> USD conversions |
| 2023-03-14 (Tue) | USDC fully repegs to ~$1.00; trade window closes |

## The Mechanics of the Depeg

[[usdc|USDC]] was widely considered the "safest" stablecoin going into 2023 — fully reserved (per attestations), audited, and US-regulated. The SVB exposure broke that thesis in three ways simultaneously:

1. **Direct loss risk.** Until the Fed announcement, the market priced a meaningful probability that the $3.3B at SVB would suffer a 20-50% haircut, implying USDC's NAV would fall to roughly $0.96-0.98.
2. **Redemption gating.** With Circle's primary banking rails (SVB, and partly Signature Bank which collapsed two days later) offline, **1:1 redemption was suspended over the weekend**. The mint/burn arbitrage that normally keeps USDC at $1 was broken.
3. **Reflexive selling.** DeFi protocols holding USDC as collateral (Aave, Compound, MakerDAO) saw users panic-swap USDC for USDT, ETH, or DAI, draining Curve 3pool and pushing USDC progressively lower.

[[curve-finance|Curve]]'s 3pool (DAI-USDC-USDT), which normally has near-equal weights, swung to **>70% USDC** as panic sellers dumped USDC for the other two stables. The pool's bonding curve absorbed the imbalance but at a worsening exchange rate, which is how USDC reached $0.87 on-chain even while OTC desks quoted $0.92-0.94.

## The Arb Trade

The opportunity was unusually clean and required only a directional view: that the US government **would** backstop SVB by Sunday night.

**Setup (Saturday 2023-03-11):**

1. **Buy USDC** in size on Curve / Uniswap at $0.87-0.92, paid for in USDT or ETH.
2. **Optionally short USDT** at $1.01-1.03 against USDC long, capturing the convergence on both legs.
3. **Hold through the weekend.**
4. **Sunday night:** Fed/Treasury announces depositor backstop.
5. **Monday morning:** USDC retraces to $0.97-0.99 immediately; full repeg by Tuesday.
6. **Exit** by selling USDC into Curve as it normalises, or redeeming 1:1 with Circle once banking rails reopen.

**Realised return:**
- Buy USDC at $0.90, sell at $0.99 → **+10%** in 72 hours, or **~10x annualised** if achieved consistently.
- Best fills (those who bought the wick at $0.87 on Saturday morning UTC) made **~14%** gross.
- Larger participants who could redeem 1:1 with Circle on Monday-Tuesday locked in essentially a risk-free 5-12% depending on entry.

The trade was not riskless — a Friday/Saturday view that the Fed *wouldn't* backstop SVB would have meant USDC plausibly dropping further (estimates ranged $0.80-0.85 in a "no bailout" scenario). The risk/reward ratio was widely judged to be 3:1 to 5:1 in favour of buying the depeg, given the systemic implications of letting a top-20 US bank's depositors take losses.

## Cascading Effects

- **[[dai|DAI]]** depegged to ~$0.90 because it was >50% backed by USDC via MakerDAO's Peg Stability Module. MakerDAO emergency-voted to reduce USDC exposure in the following weeks.
- **[[usdt|USDT]]** traded at **$1.02-1.03** premium as flight-to-quality, marking a rare reversal of the usual "Tether risk premium" narrative. Notably, Tether's reserves were reportedly at non-US banks and had no SVB exposure.
- **FRAX, agEUR, and other minor stablecoins** experienced varying depegs based on USDC backing exposure.
- **Centralised exchanges** paused USDC deposits/withdrawals over the weekend; **[[binance|Binance]] auto-converted user USDC balances to BUSD** at par (a controversial move that effectively forced users out of the depeg trade).
- **DeFi liquidations**: some leveraged positions using USDC as collateral were liquidated when on-chain USDC oracles marked the stable down. Aave, Compound, and others quickly froze USDC-denominated lending markets to limit damage.

## Why the Repeg Was Fast

The Fed/Treasury weekend backstop was decisive because it removed the only material risk: that of a permanent loss on the SVB-held cash. Once depositors were confirmed whole:

- Circle's NAV per USDC was unambiguously **$1.00**.
- Mint/burn arbitrage resumed Monday: APs and large players bought USDC at $0.97 on-chain, redeemed at $1.00 with Circle, and arbed the spread closed in hours.
- By Tuesday morning, USDC was indistinguishable from $1.00 on every venue.

## Aftermath and Lessons

- **Circle reduced concentration risk** by diversifying banking partners (post-SVB, USDC reserves were spread across BNY Mellon, Cross River Bank, and other smaller banks rather than concentrated at SVB and Signature).
- **MakerDAO accelerated diversification away from USDC**, increasing allocations to T-bills via real-world asset (RWA) facilities.
- **Stablecoin regulation accelerated**: the [[sec|SEC]], CFTC, and Congress all increased focus, ultimately contributing to legislation like the GENIUS Act and Clarity Act discussions in 2024-2025.
- **USDT gained market share** at USDC's expense for several quarters, reversing the prior trend of USDC catching up to Tether.
- **The "weekend gap" risk** between 24/7 crypto and 9-5 banking is now a recognised systemic vulnerability for fiat-backed stablecoins.

## Trading Lessons

- **Stablecoins are credit instruments, not money.** USDC's $1.00 peg is a *liability* of Circle, backed by *assets* whose quality varies by counterparty. When a counterparty fails, the peg breaks until the credit question is resolved.
- **Weekend banking risk is real for fiat-backed crypto.** US banks close Friday 17:00; crypto trades 24/7. Any catalyst that hits Friday night creates a 60-hour window where redemption arbitrage is impossible.
- **The fastest mover wins, but the smartest mover wins more.** OTC desks who quoted $0.92-0.94 to large buyers Saturday morning made the cleanest spreads; on-chain wick-buyers at $0.87 had better entries but worse fills due to slippage.
- **Macro/political views matter in crypto.** This was fundamentally a bet on US government policy, not on crypto fundamentals.
- **[[depeg-risk]] is universal.** Compare with [[2022-05-terra-luna-depeg-arb|Terra/LUNA]] (algorithmic stablecoin, terminal collapse) and various LST depegs ([[lst-depeg-arbitrage]]) — different mechanisms, same arbitrage shape: identify whether the depeg is recoverable, size accordingly.

## Sources

- Circle (Jeremy Allaire / Circle) public statements, March 10-13, 2023 — disclosure of $3.3B of USDC reserves held at Silicon Valley Bank.
- US Treasury, Federal Reserve, and FDIC joint statement, March 12, 2023 — backstop confirming all SVB depositors (including uninsured) made whole.
- Curve Finance 3pool and Uniswap on-chain price data — USDC weekend low of ~$0.87-0.88 on March 11, 2023.
- MakerDAO governance forum and votes (March 2023) — DAI depeg to ~$0.90 and subsequent USDC-exposure reduction.
- Bloomberg, CoinDesk, *The Block* — contemporaneous March 2023 coverage of the SVB failure, USDC depeg, and Signature Bank closure.

## Related

- [[usdc]]
- [[circle]]
- [[silicon-valley-bank]]
- [[stablecoin-pair-arbitrage]]
- [[lst-depeg-arbitrage]]
- [[depeg-risk]]
- [[curve-finance]]
- [[dai]]
- [[usdt]]
- [[2022-05-terra-luna-depeg-arb]]
- [[bankruptcy-claim-arbitrage]]
- [[liquidation-cascade-arbitrage]]

---
title: "Terra/LUNA Depeg — The Arbitrage Death Spiral"
type: news
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [news, arbitrage, crypto, crashes, defi]
event_date: 2022-05-09
markets_affected: [crypto]
impact: high
verified: true
sources_count: 1
related:
  - "[[terra-luna]]"
  - "[[staking-yield-arbitrage]]"
  - "[[algorithmic-stablecoin]]"
---

# Terra/LUNA Depeg -- The Arbitrage Death Spiral

The collapse of Terra/LUNA in May 2022 is the most catastrophic failure of an arbitrage-based stabilization mechanism in financial history. An arbitrage loop designed to maintain a dollar peg instead became a reflexive death spiral that destroyed over **$40 billion** in value in less than a week.

## The Mechanism

UST was an [[algorithmic-stablecoin|algorithmic stablecoin]] pegged to $1.00 through a mint/burn arbitrage mechanism with its companion token, LUNA:

- **If UST < $1.00**: Arbitrageurs buy cheap UST and burn it to mint $1.00 worth of LUNA. They sell the LUNA for profit, and the UST supply reduction pushes the price back toward $1.
- **If UST > $1.00**: Arbitrageurs burn LUNA to mint UST at $1.00, sell the UST above par, and the increased UST supply pushes the price down.

This mechanism had maintained the peg through previous stress events. The Anchor Protocol offered ~19.5% yield on UST deposits via [[staking-yield-arbitrage|staking yields]], attracting over $14 billion in deposits and creating massive concentrated demand.

## What Happened

On **May 7-8, 2022**, approximately **$2 billion** in UST was unstaked from Anchor. On **May 9**, a coordinated sell of roughly **$285 million in UST on Curve Finance** depegged UST to $0.985. The arbitrage mechanism activated as designed -- arbers began burning UST to mint LUNA.

But the mechanism that was supposed to restore the peg became its destroyer:

1. **UST depegs** -- arbers burn UST for LUNA (working as designed)
2. **Massive LUNA minting** -- LUNA supply inflates rapidly
3. **LUNA selling pressure** -- arbers and panicking holders dump newly minted LUNA
4. **LUNA price crashes** -- each LUNA token is now worth less
5. **Arb payouts shrink** -- burning $1 of UST yields LUNA worth less and less
6. **Confidence collapses** -- holders realize the peg cannot be restored
7. **Bank run** -- everyone tries to exit simultaneously

## The Death Spiral in Numbers

| Date | UST Price | LUNA Price | LUNA Supply |
|------|-----------|------------|-------------|
| May 7 | $1.00 | $80 | ~350 million |
| May 9 | $0.98 | $64 | ~350 million |
| May 10 | $0.68 | $30 | ~400 million |
| May 11 | $0.35 | $4.40 | ~1.5 billion |
| May 12 | $0.20 | $0.10 | ~6 billion |
| May 13 | $0.10 | $0.00001 | ~6.5 TRILLION |

The LUNA supply hyperinflated from 350 million to **6.5 trillion tokens** -- an 18,500x increase in under a week.

## Why the Arb Mechanism Failed

The Terra/LUNA arbitrage was designed for small deviations from peg under normal conditions. It was never stress-tested against:

- **Reflexive feedback loops**: The arb itself created selling pressure on LUNA, which undermined the arb's profitability, which accelerated the depeg -- a [[reflexivity|reflexive]] doom loop.
- **Concentrated deposits**: $14B in Anchor meant a single exit event could overwhelm the mechanism.
- **No external collateral**: Unlike [[dai]] or [[usdc]], UST had no hard assets backing it. The peg relied entirely on market confidence in LUNA's value.
- **Speed of confidence collapse**: The mechanism assumed gradual re-pegging. Instead, the bank run dynamics were exponential.

## Aftermath

- **$40+ billion** in combined UST and LUNA market cap destroyed
- Do Kwon, Terra's founder, was arrested in Montenegro (March 2023) and charged with fraud and securities violations
- The [[sec]] and regulators worldwide accelerated stablecoin regulation
- Multiple crypto funds (Three Arrows Capital, Celsius, Voyager) collapsed from Terra exposure, triggering a contagion cascade across the industry
- The event became a case study in [[regulatory-arbitrage|regulatory gaps]] in DeFi

## Trading Lessons

- **Arbitrage mechanisms can become death spirals**: When the stabilization mechanism itself creates the selling pressure, you get reflexive feedback loops. The arb was the disease, not the cure.
- **Algorithmic stability is fragile**: Without external collateral, a stablecoin's peg depends on collective belief. See [[2020-03-bond-etf-dislocation]] for a similar (but resolved) arb failure in traditional finance.
- **Yield is not free**: The 19.5% Anchor yield attracted capital that became a concentrated liability. Unsustainable yields are a red flag.
- **Test mechanisms at extremes**: A stabilization mechanism that works at 1% deviation may fail catastrophically at 5%. Always ask: "What happens if this arb runs in reverse?"
- **Bank runs are universal**: Whether in [[traditional-finance]] or [[defi-yield-farming|DeFi]], concentrated withdrawals overwhelm any mechanism not backed by sufficient liquid reserves.

Terra/LUNA demonstrated that [[arbitrage]] is not inherently stabilizing -- when the arb mechanism itself is reflexive, it can amplify instability rather than correct it.

---
title: Cross Margin vs Isolated Margin
type: concept
created: 2026-06-24
updated: 2026-06-24
status: good
tags: [market-microstructure, margin, leverage, derivatives, risk-management]
aliases: [cross-margin, isolated-margin, cross-vs-isolated, margin-mode]
domain: [market-microstructure, risk-management]
prerequisites: ["[[maintenance-margin]]", "[[leverage]]", "[[liquidation]]"]
difficulty: intermediate
related:
  - "[[maintenance-margin]]"
  - "[[mark-price]]"
  - "[[liquidation]]"
  - "[[liquidation-cascade]]"
  - "[[crypto-perpetual-futures]]"
  - "[[leverage]]"
  - "[[perpetual-futures]]"
---

# Cross Margin vs Isolated Margin

Cross and isolated margin are the two main ways a derivatives account can allocate collateral to leveraged positions. In **cross margin**, the whole account balance backs the positions — capital-efficient, but a single bad position can draw down and even liquidate the entire account. In **isolated margin**, each position is ring-fenced with a fixed slice of margin, so a loss is capped at that slice but the position liquidates sooner once its dedicated margin is exhausted.

## How Each Mode Works

- **Cross margin** — all available equity is shared collateral. Unrealized profit on one position can offset unrealized loss on another, and a position can keep drawing on free balance to stay alive. The trade-off: if the combined account equity falls to the aggregate [[maintenance-margin]] requirement, the engine liquidates against the *whole* account, so one losing trade can take everything.
- **Isolated margin** — a fixed amount of margin is assigned to a specific position. Its [[liquidation]] price is computed from only that allocated margin. If it is wiped out, the loss is limited to that allocation and the rest of the account is untouched — but the position also has a thinner buffer and liquidates earlier than the same position would under cross.

Both modes evaluate equity and liquidation at the [[mark-price]], and both are subject to the venue's [[maintenance-margin]] tiers.

## Worked Illustrative Example

A trader has 1,000 of account equity and opens one leveraged long.

- **Isolated:** they assign 100 to the position. If the trade goes against them, the most they can lose on it is that 100; the position liquidates when those 100 are exhausted, and the remaining 900 is safe.
- **Cross:** the position is backed by the full 1,000. It survives a much larger adverse move because it can draw on the whole balance — but if the move is large enough, the liquidation engine can consume the entire 1,000.

(Figures are illustrative; exact liquidation levels depend on the venue's [[maintenance-margin]] and fees.)

## Tradeoffs and Use-Cases

- **Capital efficiency vs blast radius** — cross maximizes survivability and lets profits net against losses, but concentrates the failure into a single account-wide event. Isolated caps the blast radius per trade at the cost of efficiency and earlier liquidation.
- **Hedged / multi-leg books** — cross is natural for offsetting positions (e.g. spreads, [[delta-neutral]] structures) because gains and losses net.
- **Speculative single bets / high leverage** — isolated is common for high-conviction, high-leverage punts where the trader wants a hard, known maximum loss.

## Auto-Deleveraging Interaction

When a liquidation cannot be filled in the market without further loss and the venue's insurance fund is insufficient, exchanges may use **auto-deleveraging (ADL)**: profitable opposing traders are forcibly partially closed at the bankruptcy price to absorb the shortfall. Margin mode interacts with this — large cross positions that blow through their entire account are a common source of ADL events, and traders running winning positions can be deleveraged through no fault of their own during a [[liquidation-cascade]].

## How Traders Use It / Why It Matters

- **Risk containment** — isolated turns each trade into a bounded bet; cross treats the account as one risk pool.
- **Survivability tuning** — switching a position to cross can rescue it from a near liquidation by lending it the rest of the balance — at the risk of the whole account.
- **Portfolio construction** — netting under cross can dramatically lower total margin for hedged books.

## Risks and Pitfalls

- **Cross account wipeouts** — a single mismanaged position can liquidate everything, including unrelated winners.
- **False security under isolated** — capped loss is comforting, but the position liquidates faster, so it is easier to get stopped out by noise.
- **ADL surprises** — even a correct, profitable position can be auto-deleveraged during cascades.
- **Mode-switch mistakes** — flipping modes mid-trade changes the liquidation price; do it deliberately, not in a panic.

## Related

- [[maintenance-margin]]
- [[mark-price]]
- [[liquidation]]
- [[liquidation-cascade]]
- [[crypto-perpetual-futures]]
- [[delta-neutral]]
- [[leverage]]
- [[perpetual-futures]]

## Sources

General market knowledge; no specific wiki source ingested yet.

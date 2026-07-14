---
title: "Liquidation-Price-Aware Sizing"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [crypto, risk-management, position-sizing, leverage, margin, liquidations, perpetual-futures]
aliases: ["Liquidation-Aware Sizing", "Liquidation-Distance Sizing", "Stress-Move Position Sizing", "Liquidation Price Sizing"]
domain: [risk-management, market-microstructure]
prerequisites: ["[[leverage]]", "[[maintenance-margin]]", "[[liquidation]]"]
difficulty: advanced
related: ["[[hyperliquid-margining-modes]]", "[[maintenance-margin]]", "[[leverage]]", "[[cross-margin-vs-isolated-margin]]", "[[mark-price]]", "[[liquidation]]", "[[liquidation-cascade]]", "[[funding-aware-position-sizing]]", "[[position-sizing]]", "[[crypto-perpetual-futures]]", "[[covid-crash]]"]
---

# Liquidation-Price-Aware Sizing

**Liquidation-price-aware sizing** sets leverage so that a position's **liquidation price sits beyond a deliberately-chosen stress move** — a 3σ excursion or, better, a named historical crypto wick — rather than sizing to a target notional and discovering the liquidation price after the fact. The discipline inverts the usual question: instead of "how much leverage can I take?", it asks "how far can the market move against me before I am force-closed, and is that further than the worst move I actually expect?" Because crypto perps liquidate on the [[mark-price]] the instant equity falls below [[maintenance-margin]], and because crypto tails are far fatter than Gaussian, getting this wrong means a routine wick — not a thesis being wrong — ends the position at the worst possible price.

## The Liquidation-Distance Formula

For an isolated perp (ignoring fees/funding for the moment), the liquidation price and the distance to it are:

```
long:   P_liq = P0 × (1 − 1/L + m)
short:  P_liq = P0 × (1 + 1/L − m)

distance_to_liq (fraction of price) = 1/L − m
```

where `L` is chosen [[leverage]] and `m` is the [[maintenance-margin]] ratio. The chosen leverage sets initial margin (`1/L`); the venue's maintenance ratio `m` is the floor. The gap `1/L − m` is your runway. On [[hyperliquid-margining-modes|Hyperliquid]], `m` is *half the initial margin at max leverage*, so a 40x-cap market has `m ≈ 1.25%` and a 3x-cap market `m ≈ 16.7%` — lower-leverage-cap markets bake in a wider maintenance buffer precisely because they are thinner and more manipulable.

## Sizing to a Stress Move

Pick a stress move `S` (the fractional adverse excursion you want to survive). Require the liquidation distance to exceed it, with a buffer `β`:

```
1/L − m ≥ S + β        ⟹        L ≤ 1 / (S + m + β)
```

That inequality *is* the sizing rule: it caps leverage, and notional follows (`notional = equity × L`). With `m ≈ 1.25%` (a BTC-style high-cap market) and no extra buffer:

| Stress move `S` | Anchor | Max safe leverage `L ≤ 1/(S+m)` |
|---|---|---|
| ~10% | 3σ BTC daily move (σ ≈ 3-4%/day) | ~8x |
| ~20% | Aug 5 2024 yen-carry wick (BTC ~−18-20%) | ~4-5x |
| ~30% | May 19 2021 intraday | ~3x |
| ~40% | Black Thursday, [[covid-crash|12 Mar 2020]] (BTC ~−40% intraday) | ~2x |

Add a buffer `β` (e.g. `β = 0.5·S`) and each cap drops further: surviving a 40% wick with buffer wants ~1.6x or less. The table is the whole argument for why serious crypto perp traders run *single-digit* leverage on majors — anything higher is sized to be liquidated by an ordinary crypto tail.

## Why 3σ Is Not Enough: Anchor to a Named Wick

Crypto returns are **fat-tailed and reflexive** — [[liquidation-cascade|liquidation cascades]] manufacture moves far larger than a Gaussian 3σ. A "3σ" daily move for BTC is only ~10-12%, yet BTC has wicked 30-50% intraday multiple times (Black Thursday 2020, May 2021, the October 2025 cascade). Sizing to 3σ therefore *systematically under-sizes the buffer*. The robust rule is:

```
S = max( k·σ ,  named_historical_wick )      # k ≈ 3, wick from the asset's own history
```

For a major, anchor to something like the COVID/Black-Thursday ~40% or at least the 2024 yen-carry ~20%. For a mid-cap alt — which can wick 50-70% and whose thin book makes the *realized* liquidation price far worse than mark — anchor higher still. The named wick, not the volatility estimate, should usually bind.

## Mark Price and the Single-Venue Wick

Liquidation triggers on the **[[mark-price]]** (an index blended across venues), not the last trade on your venue. This cuts both ways:

- **Protective:** a brief single-venue flash wick that does not move the cross-venue index generally will *not* liquidate you — the mark filters venue-specific spikes.
- **Dangerous:** in a genuine market-wide cascade the index *does* move, and it moves alongside a thinning book, so the position both liquidates *and* closes into poor depth. The realized closeout can be worse than `P_liq` because the engine market-sells into whatever bids remain (see [[hyperliquid-margining-modes]]).

Measure your stress move `S` on the *mark/index*, and remember your true worst case includes the exit slippage on top of the mark move.

## Buffer and Add-Margin Rules

Sizing sets the entry; rules govern the hold:

- **Do not size to the edge.** Keep the liquidation price beyond `S + β`, never exactly at `S`. The buffer is what absorbs funding debits, fees, and the estimation error in `S` itself.
- **Pre-commit an add-margin / de-lever trigger.** When the [[maintenance-margin|margin ratio]] deteriorates to a set level (e.g. equity falls to ~2× maintenance margin, or the position is within ~1.5× of `P_liq`), either add margin or cut size — *by rule, decided in advance*, not in the panic of the move.
- **Account for funding drain.** [[funding-aware-position-sizing|Funding]] and fees debit equity every interval and walk `P_liq` toward the mark even with price flat; a position that was safe at entry can drift into range. Re-underwrite periodically.
- **Fees/funding shift the formula.** The clean `1/L − m` distance shrinks once accrued funding and fees are netted from equity — bake a margin of safety in for it.

## Isolated vs Cross Margin

The margin mode determines *what* a liquidation costs (see [[cross-margin-vs-isolated-margin]] and [[hyperliquid-margining-modes]]):

- **Isolated** ring-fences collateral per position: a liquidation consumes only that position's margin, capping the loss to a known amount. Preferred for stress-sized, uncorrelated, or long-tail bets — you *want* the failure localized.
- **Cross** shares one collateral pool: more capital-efficient and gives each position a larger effective buffer (the whole account backs it), but a single bad wick can draw down — and cascade through — the *entire* account. A cross-margin liquidation is an account-level event, so the stress move must be underwritten against total equity, not one position's margin.
- **Rule of thumb:** isolated for anything you sized to a stress move you are not certain about; cross only for correlated majors where you actively want the shared buffer and are watching the whole account's liquidation level.

## Scaling In and Tier Creep

Adding to a winning position is not free from a liquidation standpoint — it moves the blended entry and can silently shrink the buffer:

- **Averaging up a long** raises `P0` (the blended entry), which raises `P_liq` toward the mark unless margin is added in proportion. Scaling in without adding margin *reduces* the stress move the position can survive.
- **Tier creep.** [[maintenance-margin|Tiered (risk-limit) margin]] raises the maintenance ratio `m` as notional grows past each tier boundary, and lowers the max leverage the venue permits. A position that survived a 40% wick at small size may only survive 30% after it is scaled up, because `m` stepped higher. Re-run the `L ≤ 1/(S+m+β)` check at the *new* tier's `m` every time you add.
- **Rule:** size the *final intended position* to the stress move up front, or add margin alongside each scale-in so the liquidation distance never contracts below `S + β`.

## Worked Example

Trader has **$50k equity**, wants a BTC long, and decides the position must survive the **Black-Thursday-class 40% wick** with a 0.5× buffer (`S = 40%`, `β = 20%`, `m = 1.25%`).

```
L ≤ 1 / (0.40 + 0.20 + 0.0125) ≈ 1.63x
notional ≤ 50,000 × 1.63 ≈ $81,500
P_liq (long) = P0 × (1 − 1/1.63 + 0.0125) ≈ P0 × 0.399   → ~60% below entry
```

The position is sized so that even a 40% mark crash leaves a ~20% cushion before liquidation — the trader is stopped out by a thesis review long before the engine ever touches it. Compare a naive 20x long: `distance = 1/20 − 0.0125 = 3.75%` — liquidated by an ordinary daily range, let alone a wick. Same equity, same view; the sizing rule is the entire difference between surviving and being force-closed. (Figures illustrative.)

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/l2-book?coin=BTC` — L2 book depth to estimate the *realized* liquidation exit price, not just the mark
- `GET /api/v1/volatility/regime?` — per-asset vol regime (compressed / expanding / vol_shock) to set the σ input to `S`
- `GET /api/v1/hyperliquid/summary?coin=BTC` — mark, funding, OI for the equity/margin calc

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — daily candles to measure realized σ and the asset's worst historical wick
- `GET /api/v1/backtesting/klines` — deep OHLCV archive (2020-) to locate named wicks (Black Thursday, May 2021, Aug 2024)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidation flow (cascade context)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Category pages: [[cryptodataapi-hyperliquid]] (L2 book), [[cryptodataapi-regimes]] (volatility regime), [[cryptodataapi-market-data]] / [[cryptodataapi-backtesting]] (klines for σ and historical wicks).

## Related

- [[hyperliquid-margining-modes]] — cross/isolated/no-cross and how `m = ½ IM at max leverage` sets the maintenance ratio
- [[maintenance-margin]] — the threshold the liquidation-distance formula is built on
- [[leverage]] — the variable the sizing rule caps
- [[cross-margin-vs-isolated-margin]] — what a liquidation costs under each mode
- [[mark-price]] — what liquidation actually triggers on
- [[liquidation]] / [[liquidation-cascade]] — the event being sized against and the fat tail it creates
- [[funding-aware-position-sizing]] — the other binding constraint on perp size; funding drains the buffer
- [[position-sizing]] — the broader discipline
- [[covid-crash]] — the Black-Thursday wick used as an anchor

## Sources

- Hyperliquid documentation — liquidation on mark price when equity < maintenance margin; `m = ½ IM at max leverage`; max leverage ~3-40x → `m` ~16.7%→1.25% (via [[hyperliquid-margining-modes]]).
- Historical crypto wick magnitudes: BitMEX/Deribit records for 12 Mar 2020, 19 May 2021, 5 Aug 2024; October 2025 cascade.
- General derivatives risk knowledge; figures illustrative.

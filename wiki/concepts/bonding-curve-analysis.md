---
title: "Bonding Curve Analysis"
type: concept
created: 2026-05-04
updated: 2026-07-13
status: excellent
tags: [crypto, defi, bonding-curve, memecoin, sniping, market-microstructure]
aliases: ["Bonding Curve", "BC Analysis", "Pump.fun Bonding Curve"]
domain: [defi, market-microstructure]
prerequisites: ["[[automated-market-maker]]", "[[liquidity-pool]]"]
difficulty: intermediate
related: ["[[pump-fun]]", "[[letsbonk]]", "[[heaven-launchpad]]", "[[memecoin-sniping]]", "[[token-migration-sniping]]", "[[holder-concentration-analysis]]", "[[cryptodataapi]]"]
---

A **bonding curve** is a deterministic mathematical formula that prices a token as a function of its circulating supply. On memecoin launchpads like [[pump-fun]], [[letsbonk]], and [[heaven-launchpad]], the curve replaces traditional order-book or AMM-style price discovery: every buy pushes price up the curve, every sell pushes it down, with no counterparty other than the curve itself. This makes early-entry vs late-entry tradeoffs, time-to-graduation, and rug risk *legible* to a trader — if you know how to read the curve.

## What a bonding curve is

In a launchpad context, the bonding curve is a smart-contract-enforced pricing function `P(S)` where `S` is current supply (or, equivalently, current reserves of the quote asset). The contract acts as the sole market maker:

- A buyer sends SOL (or ETH/BNB) and receives newly-minted tokens at price `P(S)`.
- A seller burns tokens and receives SOL out of the curve's reserve.
- There is no order book, no MEV-style toxic flow against external LPs, and no need for a seed liquidity pool.

This is the launchpad's core innovation versus traditional [[liquidity-pool]] launches: the team does not need to provide initial liquidity, and the price discovery is fully on-chain and deterministic.

## Math and formulas

### Constant-product (Uniswap-style)

Most familiar to DeFi traders: `x * y = k`. Not strictly a bonding curve in the issuance sense, but the same shape governs how AMMs price tokens. Price increases as one side of the pool is depleted.

### Linear curve

`P(S) = m * S + b`

Price rises linearly with supply. Simple, but front-runs early buyers heavily relative to late ones — late buys cost dramatically more in absolute terms even though percentage gains are similar across the curve.

### Exponential / power curve

`P(S) = a * S^n` (with `n > 1`)

Common in older bonding curve protocols. Late buyers pay disproportionately more, which means early buyers can realize very large multiples if the token graduates.

### Pump.fun's curve

Pump.fun uses a deterministic constant-product-style virtual reserves curve where each token starts with a small virtual SOL reserve (~$2 of SOL liquidity is conceptually seeded by the curve, not the deployer). The curve targets a specific market cap at "graduation" — approximately **$69k market cap** — at which point the contract automatically migrates liquidity to a DEX (historically [[raydium]], more recently [[pumpswap]]) and burns the LP tokens (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]], [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]]).

The exact polynomial is published in Pump.fun's contract; the practical takeaway for a trader is:

- **Early portion of the curve is steep in % terms** — first buyers can realize 10–50× before graduation if the token bonds.
- **Most of the absolute SOL needed to reach $69k MC arrives in the back half of the curve.** This is why "% to graduation" is a more useful trader signal than "tokens sold."

### Comparison of curve shapes

| Curve | Formula | Early-buyer advantage | Late-buyer cost | Typical use |
|-------|---------|-----------------------|-----------------|-------------|
| Linear | `P(S) = m·S + b` | Modest | Linear in supply | Simple fixed-price-ish launches |
| Power / exponential | `P(S) = a·S^n`, `n>1` | Large (convex) | Disproportionate | Older bonding-curve tokens |
| Constant-product (virtual reserves) | `x·y = k` | Large, smooth | Rises sharply near depletion | [[pump-fun]] and most modern launchpads |
| Sigmoid / logistic | S-shaped | Front-loaded then flattens | Cheap tail | Designs that want a "fair" middle zone |

The convexity of the curve is what creates the early-vs-late asymmetry that drives [[memecoin-sniping]]: the steeper the curve early on, the larger the multiple a first buyer captures by graduation — and the more aggressively snipers compete for the first block.

### Worked example — price impact on a constant-product curve

Take a simplified [[pump-fun]]-style virtual-reserves curve with virtual reserves of `1000 SOL × 1,000,000,000 tokens` (so `k = 1e12`). A buyer spends `10 SOL`:

```
Before:  SOL_reserve = 1000,  token_reserve = 1,000,000,000,  k = 1e12
Buyer adds 10 SOL  ->  SOL_reserve' = 1010
token_reserve' = k / SOL_reserve' = 1e12 / 1010 = 990,099,009.9
Tokens received = 1,000,000,000 - 990,099,009.9 = 9,900,990 tokens
Effective price = 10 SOL / 9,900,990 = 0.00000101 SOL/token
Spot price before = 1000 / 1,000,000,000 = 0.000001 SOL/token
Slippage paid     = ~1.0% on this small buy
```

The same 10 SOL buy executed when the curve is 80% filled (reserves far more depleted) moves price far more — this is why **absolute SOL needed to advance the curve grows toward graduation**, and why "% to graduation" (a curve-position metric) is a better trader signal than tokens sold. The math is identical in spirit to [[slippage]] and [[price-impact]] on any [[automated-market-maker|AMM]]; the curve is just an AMM with one synthetic counterparty.

## How prices evolve as supply grows

A useful mental model:

| Curve progress | Approx market cap | Trader stance |
|---|---|---|
| 0–10 % | < ~$7k | Snipe risk: highest reward, highest rug risk |
| 10–40 % | ~$7k–$27k | "Early momentum" zone — holder count starts to matter |
| 40–80 % | ~$27k–$55k | Mid-curve; late-snipe with confirmation |
| 80–99 % | ~$55k–$69k | Pre-graduation buy zone for migration snipers |
| 100 % | ~$69k → DEX | Graduation — see [[token-migration-sniping]] |

Percentages are illustrative, not exact — the curve is convex, so % MC ≠ % supply ≠ % SOL deposited.

## How to read curve progress as a trader

Bonding curve analysis comes down to four signals:

1. **% to graduation.** Most launchpad UIs and analytics tools surface this directly. It is the cleanest single metric.
2. **Time-to-bond (velocity).** A token that travels 0 → 50 % in five minutes is on a different trajectory than one that takes five hours. Fast curves attract more snipers, more attention, and more graduation odds — but also more bundling risk (see [[rug-detection-checklist]]).
3. **Buy-vs-sell pressure on the curve.** Because the curve is the only counterparty, every transaction is fully on-chain and visible. A wave of sells from a few wallets near the top of the curve is a graduation killer.
4. **Holder breadth at each curve stage.** A token that hits 50 % graduation with only 12 holders is almost certainly bundled. See [[holder-concentration-analysis]].

The combination of curve velocity *and* holder breadth is the practical rug filter most sniping bots automate (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]).

## Comparison: Pump.fun vs LetsBonk vs Heaven

All three use bonding-curve issuance models, but their tokenomics and fee structures differ:

| Launchpad | Curve style | Graduation venue | Distinct feature |
|---|---|---|---|
| [[pump-fun]] | Virtual-reserves constant-product, ~$69k MC graduation | [[raydium]] / [[pumpswap]] | One-click free launches, originator of the model |
| [[letsbonk]] | Bonding-curve launchpad on Solana | Solana DEX | Briefly dethroned Pump.fun in daily deployments; ~600 % revenue surge in early 2026 |
| [[heaven-launchpad]] | Bonding-curve launchpad with dual-token (LIGHT/DARK) tokenomics | Solana DEX | 100 % revenue burn model |

(Source: [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]])

Cross-launchpad comparison is what a trader uses to decide where the *meta* attention is. Migration of deployments from one launchpad to another is itself a tradable signal — see [[low-cap-crypto-trading-map]].

## Sniping implications: early entry vs late entry

The bonding curve creates a structural asymmetry:

- **Early entry (0–20 % progress).** Highest payoff if the token graduates, but most tokens never bond. Survivorship bias is brutal — a quoted "100×" win rate is often filtered through tens or hundreds of zero-trades.
- **Mid-curve entry (20–70 %).** Payoff multiple is smaller, but you can use holder data and velocity as confirmation that the token is not bundled.
- **Pre-graduation entry (80–99 %).** Lower multiple on the curve itself, but graduates trigger volatility spikes on the destination DEX. This is the [[token-migration-sniping]] play.
- **Post-graduation entry (DEX).** No longer a bonding-curve trade — now a normal AMM trade subject to MEV, liquidity, and external price action.

See [[pump-fun-bonding-curve-sniping]] and [[memecoin-sniping]] for full strategy pages.

## Graduation: the ~$69k threshold

When a Pump.fun token's curve fills (approximately $69k market cap), the contract:

1. Stops accepting buys/sells against the curve.
2. Automatically deposits the accumulated SOL and a corresponding token allocation as liquidity into a DEX pool.
3. Burns the LP tokens, locking that liquidity permanently.

The exact threshold and destination DEX have shifted over time — early Pump.fun graduated to [[raydium]]; the platform later launched its own DEX, [[pumpswap]], for graduates (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]). The migration moment itself is highly tradable: a token leaving the curve at $69k MC frequently spikes 5–50× on the destination DEX in the minutes that follow, then often round-trips. See [[token-migration-sniping]].

## Limitations and edge cases

Bonding curves are deterministic on-chain, but the *behavior* around them is not.

- **Bundled launches.** A deployer can use multiple wallets (often via tools like Jito bundles) to buy the bottom of the curve in a single transaction, then dump on retail before graduation. Holder concentration analysis flags this — see [[rug-detection-checklist]].
- **Wash trading the curve.** Cycling buys and sells against the curve is expensive (every round-trip pays curve fees), but a determined deployer can fake velocity to attract snipers. Filter on unique holders, not just transaction count.
- **Dev sells near graduation.** Some deployers reserve a wallet allocation that they dump on the DEX immediately after graduation, capturing the migration spike at retail's expense.
- **Hidden mint authority.** If the underlying token contract retains mint authority, the deployer can dilute holders post-graduation. Standard rug check.
- **Curve manipulation off-chain.** While the curve itself cannot be manipulated, the *signals around it* (Twitter/X hype, KOL endorsements, bot activity) frequently are. The curve is honest; the meta is not.

## Graduation economics and base rates

The single most important fact for sizing bonding-curve trades is the **graduation base rate**: the overwhelming majority of launched tokens never fill their curve. Reported figures vary by launchpad and period, but only a low-single-digit-percent share of [[pump-fun]] launches have historically graduated to a DEX — the rest stall and decay to near-zero. This makes the expected value of indiscriminate early sniping deeply negative once fees and the time cost of dead positions are included.

| Outcome | Approx frequency (illustrative) | Trader implication |
|---------|-------------------------------|--------------------|
| Never leaves bottom of curve | majority | Total loss minus exit fees |
| Partial progress then stalls | common | Slow bleed; exit on velocity stall |
| Graduates to DEX | small minority | The fat-tailed winners that fund the strategy |
| Graduates then round-trips | most graduates | Migration spike then mean-revert — see [[token-migration-sniping]] |

Frequencies above are indicative orderings, not precise statistics — they vary by launchpad, meta, and time period. The point is structural: bonding-curve sniping is a **fat-tailed, low-base-rate** game where survivorship bias makes naive win-rate quotes meaningless. Position sizing must assume most entries go to zero. See [[holder-concentration-analysis]] and [[rug-detection-checklist]] for the filters that lift the base rate.

### Fee drag

Every buy and sell against the curve pays a protocol fee (and, on graduation, the migration consumes part of the accumulated reserve). Round-tripping the curve to fake velocity is therefore costly to the deployer — but it is also a real drag on a sniper's edge, because high turnover compounds fees against a low base rate of winners. Account for fees explicitly in any expected-value model.

## Trader's quick-reference checklist

Before entering a bonding-curve position:

1. **% to graduation** and **curve velocity** — is it moving, and how fast? (See the four signals above.)
2. **Unique holders vs curve progress** — high progress with few holders = likely bundled. See [[holder-concentration-analysis]].
3. **Mint authority / contract checks** — renounced mint? LP burn on graduation? See [[rug-detection-checklist]].
4. **Buy/sell flow near the top** — concentrated sells pre-graduation kill the bond.
5. **Meta context** — which launchpad has attention right now? See [[low-cap-crypto-trading-map]].
6. **Exit plan** — define the migration-spike exit *before* entry; most graduates round-trip. See [[token-migration-sniping]].

## Tools that visualize curves

| Tool | What it shows | Notes |
|---|---|---|
| [[bitquery]] | GraphQL feed of Pump.fun trades, OHLCV, bonding progress, top traders | Powers most custom sniping dashboards |
| [[birdeye]] | Curve progress, holder distribution, MC and volume | Solana-focused; good for live alerts |
| [[dex-screener]] | New pairs, holder counts, bonding curve progress | First-stop for spotting bonds and early momentum |
| Pump.fun native UI | Curve % filled, recent trades, holder list | Simplest, but limited filtering |
| Dune Analytics | Custom SQL on Pump.fun data — e.g., "tokens bonding in <5 min" | Good for backtesting/research, not live ops |

(Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]])

## Sources

- [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]]
- [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/dex/trending` — trending DEX pools (Solana/Ethereum/Base/BSC/Arbitrum)
- `GET /api/v1/dex/new-pools` — newest launches, multi-chain
- `GET /api/v1/dex/security/{chain}/{address}` — token security report (rug/honeypot detection)
- `GET /api/v1/meme/regime/score` — market-wide meme-hype score + meme_season flag

**Historical data:**
- `GET /api/v1/meme/regime/{symbol}` — per-asset meme lifecycle + 60d history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/trending"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-dex]].

## Related

- [[pump-fun]]
- [[letsbonk]]
- [[heaven-launchpad]]
- [[automated-market-maker]]
- [[liquidity-pool]]
- [[memecoin-sniping]]
- [[token-migration-sniping]]
- [[pump-fun-bonding-curve-sniping]]
- [[holder-concentration-analysis]]
- [[rug-detection-checklist]]
- [[bitquery]]
- [[birdeye]]
- [[dex-screener]]
- [[low-cap-crypto-trading-map]]
- [[slippage]]
- [[price-impact]]
- [[raydium]]
- [[pumpswap]]

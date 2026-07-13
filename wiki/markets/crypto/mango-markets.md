---
title: "Mango"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi, derivatives, perpetuals, dex]
aliases: ["MNGO", "Mango Markets"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://mango.markets"
related: ["[[crypto-markets]]", "[[solana]]", "[[perpetual-futures]]", "[[oracle-manipulation]]", "[[margin-trading]]", "[[dex]]", "[[defi]]", "[[decentralized-exchange]]", "[[liquidation]]"]
---

# Mango

**Mango** (MNGO) is the governance token of **Mango Markets**, a [[decentralized-exchange|decentralized]] [[defi|DeFi]] trading platform on [[solana|Solana]] offering [[margin-trading|margin trading]] (up to ~10x [[leverage]]), spot, and [[perpetual-futures|perpetual]] markets. The protocol is governed by a DAO and aggregates liquidity across multiple sources on Solana.

Mango Markets is best known both as one of Solana's earliest on-chain margin/perp venues and as the target of a landmark October 2022 [[oracle-manipulation|oracle-manipulation]] exploit that drained roughly **$117M** from the protocol.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | MNGO |
| **Chain** | [[solana|Solana]] (also Neon EVM) |
| **Market Cap Rank** | #601 |
| **Price** | $0.0297385 |
| **Market Cap** | ~$33.23M |
| **24h Volume** | ~$481 |
| **24h Change** | -2.43% |
| **7d Change** | +2.33% |
| **All-Time High** | $0.498845 (2021-09-09) — current ~-94% |
| **All-Time Low** | $0.00147576 — current ~+1,915% |
| **Circulating Supply** | ~1.12B MNGO (~22% of max) |
| **Total Supply** | 5.00B MNGO |
| **Max Supply** | 5.00B MNGO |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Trading backdrop: the broad crypto market is in **extreme fear** (Crypto [[fear-and-greed-index|Fear & Greed Index]] = **23**) within an **Established Bear Market** as of 2026-06-20. Note the extremely thin reported 24h volume (~$481) against a ~$33M market cap — MNGO is effectively illiquid on tracked spot venues, so price prints carry low confidence and any size order would cause major [[slippage]].

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~1.12B MNGO |
| **Total Supply** | 5,000,000,000 MNGO |
| **Max Supply** | 5,000,000,000 MNGO |
| **Fully Diluted Valuation** | ~$148.7M (price × max supply) |
| **Market Cap / FDV** | ~0.22 |

**Dilution flag:** only ~22% of max supply circulates, so FDV (~$148.7M) is roughly 4.5x the market cap (~$33.23M). In a normal token this would flag heavy unlock overhang, but most non-circulating MNGO sits in the **Mango DAO treasury** rather than on a vesting cliff to insiders — it is governance-controlled supply. Still, any DAO decision to deploy or sell treasury MNGO into a ~$481/day market would be highly price-disruptive. MNGO is a DAO governance token; holders vote on protocol parameters and treasury decisions. The token gained governance notoriety after the 2022 exploit, when the attacker used the very MNGO governance process to attempt to approve their own settlement (see Notable History).

### Categories

Decentralized Finance (DeFi), Derivatives, Perpetuals, Solana Ecosystem, Alleged SEC Securities, FTX Holdings, Neon Ecosystem, Governance.

### Contract Addresses

| Chain | Address |
|---|---|
| [[solana|Solana]] | `MangoCzJ36AjZyKwVj3VnYU4GTonjfVEnJmvvWaxLac` |
| Neon EVM | `0x6d12eaa69f8e4902d3f83d546b31f7318717014c` |

---

## How & Where It Trades

### Spot venues

| Exchange | Pair | Type |
|---|---|---|
| [[kraken|Kraken]] | MNGO/USD | CEX spot |
| Orca | MNGO/USDC | [[decentralized-exchange\|DEX]] spot (Solana) |

Tracked MNGO spot liquidity is extremely thin (~$481 reported 24h volume). Most of the token's lifecycle activity has been governance- and exploit-related rather than active trading.

### Protocol mechanics (margin & perps)

Mango Markets' on-chain "market" is a cross-margined trading platform on [[solana|Solana]]:

1. **Depositors** post collateral into the protocol, which can be borrowed/lent and used as cross-margin.
2. **Traders** open spot, [[margin-trading|margin]], and [[perpetual-futures|perpetual]] positions with up to ~10x [[leverage]], with profit/loss and borrowing settled against deposited collateral.
3. **Price oracles** value collateral and positions; positions are [[liquidation|liquidated]] when margin falls below maintenance. (This oracle-dependence was the exact surface exploited in 2022.)
4. The protocol is steered by the **Mango DAO**, with MNGO as the voting token.

---

## Use Case, Narrative & Category

Mango sits in the **Solana DeFi / on-chain derivatives** category — one of the first margin-and-perp venues native to [[solana|Solana]]. Its narrative is now inseparable from the 2022 exploit, which became a defining case study in DeFi [[oracle-manipulation|oracle-manipulation]] risk, governance attacks, and the legal grey zone around on-chain "market manipulation."

### DEX model & fee capture (qualitative)

Mango Markets is a **cross-margin trading [[decentralized-exchange|DEX]]**, not a constant-product [[automated-market-maker|AMM]] like [[sushi|SushiSwap]] or [[sun-token|SunSwap]]. It runs a central-limit-order-book and lending/borrowing money market on [[solana|Solana]]: depositors supply collateral that is lent out and used as cross-margin, while traders take spot, [[margin-trading|margin]], and [[perpetual-futures|perp]] positions up to ~10x [[leverage]]. Protocol revenue historically came from borrow-interest spreads, perp [[funding-rate|funding]], and trading fees — but the **MNGO token does not have a strong direct fee-capture claim**; it is primarily a governance asset. That weak value-accrual link, combined with reputational damage from the exploit and near-zero volume, is central to why MNGO trades at a micro-cap despite Mango's pioneering role.

## Peer Comparison (on-chain derivatives / DEX tokens)

| Token | Rank | Market Cap | Category | Note |
|---|---|---|---|---|
| **Mango (MNGO)** | #601 | ~$33.23M | Solana margin/perp DEX | Illiquid; exploit legacy; governance-only |
| [[asterdex\|Aster (ASTER)]] | #48 | ~$1.74B | Multi-chain perp DEX | #2 perp DEX by volume |
| [[hyperliquid\|Hyperliquid (HYPE)]] | top-tier | multi-$B | Perp DEX (own L1) | Category leader |
| [[sushi\|Sushi (SUSHI)]] | #471 | ~$48.09M | Multi-chain spot DEX/AMM | DeFi-1.0 blue chip |
| [[sun-token\|Sun (SUN)]] | #133 | ~$328.94M | TRON DEX/launchpad | Buyback-and-burn |

*Caps reflect the 2026-06-20 snapshot where available; HYPE shown qualitatively.*

## Valuation Framing (qualitative)

MNGO is effectively a **distressed / legacy governance token** rather than an active revenue play. With ~$481/day of volume and a market cap (~$33M) far below FDV (~$149M), price discovery is unreliable and the token behaves more like a claim on the Mango DAO treasury and brand than on live protocol cash flow. Bull case: a relaunch or treasury redeployment revives the venue and gives MNGO a real fee-capture role on a recovering [[solana|Solana]]. Bear case: the exploit stigma, regulatory "Alleged SEC Securities" tag, weak token utility, and dead liquidity leave it a thin, headline-driven micro-cap. *This is framing, not a price target or recommendation.*

---

## Notable History

### The October 2022 Mango Markets exploit (~$117M)

On **2022-10-11**, trader **Avraham (Avi) Eisenberg** drained an estimated **~$117 million** from Mango Markets via [[oracle-manipulation|oracle manipulation]]:

- Eisenberg used two accounts to take large opposing [[perpetual-futures|perpetual]] positions in MNGO-PERP, then aggressively bought spot MNGO across thin venues to **pump the MNGO price ~5–10x** in a short window.
- Because Mango valued collateral using that manipulated MNGO price, his long position showed enormous unrealized "profit," which he then **borrowed against**, withdrawing ~$117M of other assets (USDC, SOL, BTC, etc.) from the protocol — far more than the real value of his collateral.
- Eisenberg publicly described the act as a **"highly profitable trading strategy"** that was legal, framing it as using the protocol "as designed."
- He then used the protocol's **governance** mechanism, voting borrowed MNGO to try to approve a settlement that would let him keep ~$47M while returning the rest. Mango DAO ultimately negotiated the return of a large portion of the funds.
- **Legal aftermath:** Eisenberg was arrested in December 2022 and, in 2024, **convicted** in U.S. federal court on commodities fraud and market-manipulation charges related to the exploit — a precedent-setting case for whether on-chain manipulation constitutes criminal fraud. (Separately, regulators including the SEC and CFTC brought civil actions.)

The episode is a canonical example of why DeFi protocols must use robust, manipulation-resistant price oracles and conservative collateral parameters — see [[oracle-manipulation]].

### Other history

- Token reached an all-time high of **$0.4988** on 2021-09-09 during the prior Solana bull run; it trades far below that today.
- All-time low of **$0.00147576** was printed on 2025-12-18.
- Mango is tagged among "FTX Holdings" and "Alleged SEC Securities," reflecting both prior FTX/Alameda exposure across Solana DeFi and ongoing regulatory ambiguity around governance tokens.

> *Additional verified protocol events and news will be added through the wiki's source-ingestion workflow.*

---

## Risks

- **Oracle / manipulation risk:** the 2022 exploit demonstrated this directly; thinly traded collateral assets remain vulnerable to [[oracle-manipulation]].
- **Liquidity risk:** MNGO spot volume is near-zero (~$481/24h), so exits at size are effectively impossible without major [[slippage]].
- **Leverage / liquidation risk:** margin and perp products carry standard [[liquidation]] tail-risk for users.
- **Governance-attack risk:** as the exploit showed, a sufficiently capitalized actor can borrow/acquire governance tokens to influence DAO outcomes.
- **Regulatory risk:** "Alleged SEC Securities" tag and the criminal/civil cases tied to the exploit underscore ongoing legal uncertainty.
- **Market regime:** with the Fear & Greed Index at 23 (extreme fear) in an Established Bear Market, an illiquid governance token like MNGO is exposed to sharp, low-volume price swings.

---

## Related

- [[crypto-markets]]
- [[solana]]
- [[perpetual-futures]]
- [[margin-trading]]
- [[oracle-manipulation]]
- [[liquidation]]
- [[decentralized-exchange]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-20: cryptodataapi.com / CoinGecko top-1000 markets data.
- The October 2022 exploit, Eisenberg arrest/conviction, and oracle-manipulation framing reflect widely reported, publicly documented events.

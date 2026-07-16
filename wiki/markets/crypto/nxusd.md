---
title: "NXUSD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoin]
aliases: ["NXUSD", "Nereus USD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://nereus.finance/"
related: ["[[avalanche-2]]", "[[avalanche]]", "[[collateral]]", "[[crypto-markets]]", "[[stablecoins]]"]
---

# NXUSD

**NXUSD** is a crypto-collateralized [[stablecoin|stablecoin]] (a [[synthetic-dollar]] designed to track US$1.00) issued by Nereus Finance, a decentralised, non-custodial liquidity-market protocol native to the [[avalanche-2|Avalanche]] ecosystem. On the Nereus money market, depositors supply liquidity to earn passive yield while borrowers draw against collateral on either an over-collateralised (perpetual) or one-block (flash) basis; NXUSD is the protocol's algorithmic dollar unit minted against that collateral.

Unlike the fiat-backed ([[usdh-2|USDH]]) or reinsurance-RWA ([[re-protocol-reusd|reUSD]]) dollars elsewhere in this category, NXUSD is **endogenously collateralized** — its backing is volatile crypto held inside the Nereus money market, and its peg is sustained by over-collateralization, price oracles, and arbitrage rather than by any off-chain reserve. That makes it structurally closer to a [[makerdao|MakerDAO]]-style crypto-backed dollar than to a reserve coin, and explains why, at low liquidity, it currently trades at a modest discount to par rather than dead-on $1.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* NXUSD trades at **$0.981737** (rank **#854**, market cap **$18,617,508**, 24h **+1.42%**, 7d **-0.72%**). This is a mild **~1.8% soft-peg discount** to the $1.00 target — common for low-liquidity crypto-backed stablecoins and not a severe [[depeg]] event, though it does signal weak secondary-market demand and thin arbitrage activity at this size.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NXUSD |
| **Market Cap Rank** | #854 |
| **Market Cap** | $18,617,508 |
| **Current Price** | $0.981737 |
| **Peg Target** | US$1.00 (~1.8% below peg) |
| **Categories** | Stablecoins, Avalanche Ecosystem, Crypto-backed Stablecoin |
| **Website** | [https://nereus.finance/](https://nereus.finance/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Nereus is a decentralised, non-custodial liquidity-market protocol in which users participate as depositors or borrowers. Depositors provide liquidity to earn passive income, while borrowers can borrow in an over-collateralised (perpetual) or undercollateralised (one-block / flash) fashion. Nereus is optimised to provide dynamic and fixed interest rates with lower collateral requirements, with a focus on use cases beyond trading and price speculation. NXUSD is the algorithmic, crypto-[[collateral|collateralized]] dollar stablecoin issued by Nereus Finance.

## Architecture — How NXUSD Works

### Collateral / reserve model
NXUSD holds **no off-chain fiat reserves**. It is **minted against on-chain crypto collateral** within the Nereus money market — a [[collateralized-debt-position|collateralized-debt-position (CDP)]]-style design where a borrower locks volatile crypto and mints NXUSD against it, subject to a collateralization ratio. Backing value therefore moves with the price of the underlying crypto, and solvency depends on positions staying above their liquidation thresholds. The protocol also supports one-block (flash) borrowing for atomic, same-transaction leverage and arbitrage.

### Peg / stability mechanism
NXUSD targets a 1:1 value with the US dollar, sustained by three pillars: (a) **sufficient over-collateralization**, so each NXUSD is backed by >$1 of crypto; (b) **reliable price oracles**, which value collateral and trigger liquidations; and (c) **active arbitrageurs** who mint when NXUSD trades above $1 and redeem/buy when it trades below. As of 2026-06-22 the token sits at **$0.981737**, a modest ~1.8% discount that reflects thin liquidity (24h volume historically very low) rather than a collateral failure — the arbitrage loop is simply uneconomic to run at this small size.

### Yield / money-market mechanics
NXUSD's "yield" is not a reserve coupon but the **money-market spread**: depositors earn interest from borrowers who pay to mint/borrow against collateral. There is no exogenous T-bill or funding-rate yield stream backing the token itself; the economics are those of a lending market.

### Mint / redeem & gating
Minting is opening a collateralized position; "redeeming" is repaying NXUSD to unlock collateral, or liquidation if a position falls below threshold. Peg restoration relies on these CDP mechanics plus secondary arbitrage — both of which weaken when liquidity is as thin as NXUSD's current ~$2.7K/24h.

---

## Comparison vs Peer Crypto-Backed / Stablecoins

| Dimension | **NXUSD** (Nereus) | DAI ([[makerdao\|MakerDAO]]) | [[ethena-usde\|USDe]] (Ethena) | [[usdh-2\|USDH]] (Native) |
|---|---|---|---|---|
| **Peg model** | Crypto-collateralized CDP | Crypto-collateralized CDP | Synthetic, delta-neutral | Fiat, 1:1 reserve |
| **Backing** | Volatile crypto (over-coll.) | Crypto + RWA | Crypto + perp shorts | Cash + T-bills |
| **Chain** | [[avalanche-2\|Avalanche]] | Ethereum | Ethereum (+) | Hyperliquid |
| **Current peg** | ~$0.982 (−1.8%) | ~$1.00 | ~$1.00 | ~$1.00 |
| **Key risk** | Collateral crash + oracle + thin liquidity | Collateral / governance | Funding flips negative | Custodian/banking |
| **Scale** | ~$18.6M cap, very thin | Multi-billion | Multi-billion | ~$21M, active |

NXUSD shares DAI's crypto-CDP archetype but at a fraction of the scale and liquidity; the small-cap, thin-liquidity profile — not the mechanism itself — is what drives its persistent sub-par quote.

---

## How & Where It Trades / Is Used

- **Primary venue:** native to [[avalanche-2|Avalanche]] (contract `0xf14f4ce569cb3679e99d5059909e23b07bd2f387`); used within the Nereus money market as the borrow/mint unit and on Avalanche DEX pools. No major centralized-exchange listings were found in CoinGecko data.
- **Composability:** as an Avalanche-native dollar, NXUSD can be paired in DEX pools or used as collateral/quote within Avalanche DeFi, but its tiny float and thin volume limit practical integration.
- **Liquidity caveat:** ~$2,725 of 24h volume against a ~$18.6M cap is extremely thin — the 24h range ($0.9810–$1.02) shows how easily the price swings around par on minimal flow. Treat any size as slippage-prone and the peg-restoring arbitrage loop as effectively dormant at this liquidity.

---

## Narrative / Category & Catalysts

NXUSD belongs to the **crypto-collateralized (CDP) stablecoin** lineage — the "decentralized dollar backed by on-chain crypto" model that DAI popularized — tied specifically to the [[avalanche-2|Avalanche]] DeFi ecosystem and the Nereus lending market. Catalysts:

- **Avalanche DeFi activity:** NXUSD demand is a function of borrowing/leverage demand on Nereus and Avalanche broadly; a revival of Avalanche DeFi TVL is the main tailwind.
- **Liquidity bootstrapping:** the persistent sub-par quote is fundamentally a liquidity problem — deeper pools and more active arbitrage would tighten it toward $1; that is the key thing to watch.
- **Collateral-market regime:** crypto-backed dollars are most stable in calm, range-bound markets; sharp Avalanche-collateral drawdowns are the dominant downside catalyst.
- **Risk-off backdrop:** in the current Extreme-Fear / bottoming regime, thin crypto-backed coins like NXUSD see the widest peg deviations because arbitrage capital is scarce.

---

## History / Timeline

- **2022-08-02** — All-time low of **$0.0344** (per CoinGecko price history) — a catastrophic early de-peg/illiquidity print, a reminder that small crypto-backed dollars carry tail risk.
- **2024-12-17** — All-time high of **$2.43** — a large upside dislocation, again symptomatic of thin liquidity rather than fundamentals.
- **2026-04-09** — Captured in the wiki via the CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]); page created.
- **2026-06-22** — Market-data refresh: price $0.981737 (~1.8% below peg), cap ~$18.6M, rank #854, ~$2.7K 24h volume.
- **2026-06-23** — Page expanded to `excellent`.

> Note: only wiki-verified dates are listed; the dramatic 2022 ATL and 2024 ATH come from CoinGecko price history and reflect thin-liquidity dislocations, not confirmed protocol events.

---

## Risks

- **Soft-peg / [[depeg]] risk** — the present ~1.8% discount illustrates how low-cap crypto-backed stablecoins can drift from par when arbitrage is uneconomic at small size; the historical $0.0344 ATL and $2.43 ATH show the deviations can be extreme under thin liquidity.
- **Collateral risk** — backing is volatile crypto assets; sharp drawdowns can push positions below the liquidation threshold, stressing the peg (the algorithmic/crypto-backed-stablecoin failure mode; see [[algorithmic-stablecoin]]).
- **Oracle / smart-contract risk** — mispriced or stale oracles can allow undercollateralised mints or unfair liquidations; flash-borrow functionality widens the attack surface for oracle-manipulation exploits.
- **Liquidity risk** — minimal secondary-market depth (~$2.7K/24h) makes large redemptions slippage-prone and weakens the peg-restoring arbitrage loop.
- **Regulatory risk** — algorithmic / crypto-collateralized dollars face evolving stablecoin-regime scrutiny, particularly post-Terra.
- **Macro backdrop** — at the 2026-06-23 snapshot the market is in **Extreme Fear (F&G 21)**, market-health 29/100, regime **bottoming / accumulation**; this is exactly the environment in which thin crypto-backed coins see the widest peg deviations as arbitrage capital withdraws.

---

## Trading / Usage Playbook

- **Do not treat NXUSD as a hard $1 dollar.** It is a thin, crypto-collateralized CDP coin trading ~1.8% below par; the discount can widen further on minimal flow. Size accordingly and assume slippage.
- **Liquidity is the whole story.** Before any position, check on-chain pool depth — at ~$2.7K daily volume, entering or exiting more than trivial size will move the price materially.
- **Mechanism is sound; scale is the weakness.** The CDP/over-collateralization design is the same family as DAI, but without DAI's liquidity the arbitrage that restores the peg is largely dormant — do not rely on a quick mean-reversion to $1.
- **Tail-risk awareness:** the 2022 $0.0344 print is a standing reminder that small crypto-backed dollars can dislocate hard in stress; treat NXUSD as a risk asset, not a cash equivalent.

> *Not financial advice. Crypto-collateralized stablecoins carry collateral-crash, oracle, liquidation, and severe liquidity risk and can de-peg sharply.*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 18.96M NXUSD |
| **Total Supply** | 18.96M NXUSD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $18.97M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2.43 (2024-12-17) |
| **Current vs ATH** | -58.80% |
| **All-Time Low** | $0.0344 (2022-08-02) |
| **Current vs ATL** | +2805.10% |
| **24h Change** | +1.42% |
| **7d Change** | -0.72% |

---

## Platform & Chain Information

**Native Chain:** Avalanche

### Contract Addresses

| Chain | Address |
|---|---|
| Avalanche | `0xf14f4ce569cb3679e99d5059909e23b07bd2f387` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://nereus.finance/](https://nereus.finance/) |
| **Twitter** | [@nereusfinance](https://twitter.com/nereusfinance) |
| **Discord** | [https://discord.gg/4tw3VsuTf9](https://discord.gg/4tw3VsuTf9) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2,725.23 |
| **Market Cap Rank** | #839 |
| **24h Range** | $0.9810 — $1.02 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[avalanche-2]]
- [[stablecoins]]
- [[synthetic-dollar]]
- [[collateralized-debt-position]]
- [[makerdao]]
- [[algorithmic-stablecoin]]
- [[stablecoin-depegs]]
- [[collateral]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge and Nereus Finance public documentation; market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). No additional specific wiki source ingested yet.

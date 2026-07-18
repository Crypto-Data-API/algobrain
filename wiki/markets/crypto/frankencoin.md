---
title: "Frankencoin"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoins]
aliases: ["ZCHF"]
entity_type: protocol
headquarters: "Decentralized (Switzerland-aligned community)"
website: "https://www.frankencoin.com"
related: ["[[crypto-markets]]", "[[dai]]", "[[defi]]", "[[depeg]]", "[[ethereum]]", "[[forex]]", "[[stablecoin]]", "[[swiss-franc]]", "[[usda-2]]"]
---

# Frankencoin

**Frankencoin** (ticker **ZCHF**; native chain [[ethereum|Ethereum]], with deployments on Polygon, Base, Optimism, Arbitrum, Gnosis and Avalanche) is a decentralized, **over-collateralized** [[stablecoin]] that tracks the **[[swiss-franc|Swiss franc]] (CHF)**, not the US dollar. Its defining feature is that it uses **no price oracle**: anyone can mint ZCHF against approved collateral through an adversarial **Dutch-auction price-discovery mechanism** rather than a centralized price feed. The peg model is collateral-redemption plus auction liquidation; "yield" in the system accrues to equity providers (the Frankencoin Pool Share, FPS) who bear first-loss risk, not to ZCHF holders directly. ZCHF is one of the few sizeable non-USD FX stablecoins, alongside euro coins like EURe and real coins like [[brz]] / [[brla-digital-brla]].

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*
>
> *Disclaimer: figures below are a point-in-time snapshot and are not investment advice. Verify live data and the protocol's own attestations before trading.*

## Why the ~$1.24 USD price is the peg, not a depeg

ZCHF is pegged to **one Swiss franc**, and one Swiss franc is currently worth roughly **1.24 US dollars** on the [[forex]] market. So a USD-denominated quote of **$1.24** for ZCHF is exactly the peg holding correctly — it reflects the CHF/USD exchange rate, **not** a stablecoin trading above its target. Reading ZCHF against USD will always show it near the prevailing CHF/USD rate (historically ~1.05–1.30). To judge whether ZCHF is on-peg, compare it to **CHF**, where it should sit at ~1.00 CHF. This is the same framing that applies to any non-USD FX stablecoin (compare [[brz]] and [[brla-digital-brla]] for the Brazilian real).

## Market Snapshot (2026-06-21)

| Field | Value |
|---|---|
| **Ticker** | ZCHF |
| **Price (USD)** | $1.24 (≈ 1.00 CHF — on peg) |
| **Market Cap Rank** | #491 |
| **Market Cap** | $45,053,158 |
| **24h Change** | -0.07% |
| **7d Change** | -1.39% |
| **Currency tracked** | Swiss franc (CHF) |

The small 24h/7d moves in USD terms (-0.07% / -1.39%) are largely the CHF/USD exchange rate drifting, not the peg breaking.

## Issuer & Jurisdiction

Frankencoin is a **decentralized protocol** rather than a corporate issuer. It originated from the Swiss/DeFi community and is governed by ZCHF holders and "equity" (FPS) providers via on-chain governance. There is no single legal issuer holding fiat reserves; the franc backing is achieved through crypto collateral locked in smart contracts. Source code is open at the [Frankencoin GitHub](https://github.com/Frankencoin-ZCHF/Frankencoin/), and the design is described in the project's thesis preprint. Because the franc peg is synthesised from on-chain collateral rather than a Swiss bank account, ZCHF sidesteps the single-issuer counterparty risk of fiat-reserve coins but inherits the collateral and auction risks described below.

## Architecture — How Frankencoin Works

### Oracle-free collateral & Dutch-auction price discovery

Frankencoin's distinguishing feature is that it uses **no price oracle**. Instead the protocol relies on an adversarial market process:

- A user who wants to mint ZCHF opens a **position** by proposing collateral (e.g., blue-chip crypto such as [[bitcoin|WBTC]]/[[ethereum|WETH]], LSTs, or RWA-style tokens) and a price at which they are willing to back it. They post a small proposal fee and the position sits behind an **initialization period** before minting is allowed.
- During the position's life, anyone can **challenge** that valuation by initiating a **Dutch auction** of the collateral. The challenger posts collateral of the same type; the auction price starts high and decays over time. If nobody bids above the position's claimed price, the collateral really is worth less than claimed and the challenger buys it cheaply, **liquidating** the position; if a counter-bid appears, the challenger is penalised. This game-theoretic design rewards honest valuations and punishes over-claiming.
- This adversarial market replaces a centralized oracle, making the system resistant to oracle manipulation (a common DeFi exploit vector) but slower and more capital-intensive than oracle-fed designs.

ZCHF is therefore an **over-collateralized crypto-backed** stablecoin — a CHF analogue to how [[dai]]-style USD CDP systems work, and to BTC-CDP designs like [[usda-2|USDa]] — distinct from fiat-reserve coins like [[straitsx-xusd]].

### Peg & stability mechanism

The peg is anchored from two directions. **Minters** are incentivised to mint when ZCHF trades above 1 CHF (they can sell newly minted francs at a premium) and to repay/close when it trades below par (buying back cheap ZCHF to unlock collateral). **Equity providers** absorb shortfalls so the system stays solvent. There is no algorithmic supply rebase and no fiat redemption desk — par is enforced economically through collateral redemption and arbitrage rather than by an issuer standing ready to swap 1 ZCHF for 1 CHF cash.

### Yield source & distribution

ZCHF itself is **not** yield-bearing for passive holders. Minters pay an **interest rate** (set per position) on the francs they create; that interest, plus auction penalties and fees, flows to the **Frankencoin Pool Share (FPS)** equity token. FPS holders provide the first-loss capital buffer and in exchange earn the protocol's net income — making FPS the system's risk-bearing, yield-bearing leg. This separates the *stable* unit (ZCHF) from the *risk/return* unit (FPS), in contrast to single-token yield dollars like [[ethena-usde]] where the holder bears strategy risk directly.

## Tokenomics & Supply

- **ZCHF** is minted on demand against collateral and burned on repayment, so circulating supply expands and contracts with borrowing demand rather than being fixed. At the snapshot, supply backs a ~$45M (≈ CHF 36M) market cap — small versus USD stablecoin majors.
- **FPS** (Frankencoin Pool Share) is the equity/governance token. Capital flows in and out of the equity pool via a bonding-curve-style mechanism; FPS holders vote on collateral approvals, parameters, and minter onboarding.
- Governance is **permissionless to propose but vetoable**: new collateral types and minting modules pass through a proposal-and-veto window before activation, giving FPS holders a chance to block risky additions.

## Comparison vs Peer Stablecoins

| Feature | **Frankencoin (ZCHF)** | [[dai\|MakerDAO DAI]] | EURe (Monerium) | [[ethena-usde\|Ethena USDe]] |
|---|---|---|---|---|
| Peg target | Swiss franc (CHF) | US dollar | Euro (EUR) | US dollar |
| Backing | Over-collateralized crypto, **oracle-free** | Crypto + RWA CDPs, oracle-fed | Fiat e-money reserves (1:1 EUR) | BTC/ETH collateral + delta-neutral hedge |
| Price discovery | Dutch-auction challenges | Chainlink oracles | Issuer attestation | Oracles + perp venues |
| Holder yield | None (yield → FPS equity) | DSR (sDAI) optional | None | Funding-rate carry (sUSDe) |
| Issuer | Decentralized, no fiat issuer | Decentralized (Sky) | Regulated EMI | Single protocol issuer |
| Main risk | Collateral/auction, FX for USD holders | Oracle, RWA, governance | Issuer/bank, regulatory | Negative funding, venue/custody |

## How & Where It Trades / Is Used

- **DEX liquidity:** ZCHF trades primarily on-chain — Uniswap V3 pools (ZCHF/USDC, ZCHF/WETH) and CHF-pair pools are the main venues. It is the deepest CHF-denominated stablecoin on Ethereum, making it the default building block for franc-denominated DeFi.
- **Composability:** ZCHF is used as a savings/borrowing unit by Swiss-franc-minded users who want dollar-free exposure, and the FPS equity token offers a yield instrument for those willing to take protocol risk.
- **FX read-through:** because pricing screens quote ZCHF in USD, holders should mentally convert to CHF (~1.00) to judge the peg — see the framing section above.

## Narrative / Category & Catalysts

Frankencoin sits in the **non-USD / FX stablecoin** and **oracle-free CDP** narratives. Its bull case is structural: nearly all stablecoin liquidity is USD-denominated, leaving a gap for credible EUR/CHF units, and the oracle-free design is a differentiated answer to the oracle-manipulation exploits that have repeatedly hit DeFi. Catalysts include CHF/USD FX swings (which change the USD-quoted price without affecting the peg), growth in Swiss/European on-chain finance, MiCA-driven demand for compliant non-USD units, and any expansion of approved collateral or L2 deployments. In the current **bottoming/accumulation** crypto regime (Fear & Greed 21, Extreme Fear, as of 2026-06-22), niche stablecoins like ZCHF see muted volume, so liquidity risk is elevated.

## History / Timeline

- **2023** — Frankencoin protocol launches on Ethereum mainnet as an oracle-free CHF stablecoin from the Swiss DeFi community.
- **2024–2025** — Expansion across L2s/sidechains (Polygon, Base, Optimism, Arbitrum, Gnosis, Avalanche); collateral set and FPS equity pool grow.
- **2026-06-21** — Snapshot: ZCHF ~$1.24 USD (≈ 1.00 CHF, on peg), market cap ~$45M, rank #491. No depeg is evident in the recorded data; USD-quoted moves track CHF/USD FX, not peg breaks.

## Risks

- **FX risk for USD holders:** Because ZCHF tracks CHF, a USD-based holder is implicitly long the Swiss franc and exposed to CHF/USD [[forex]] moves — the single biggest reason the USD quote drifts.
- **Collateral / liquidation risk:** As an over-collateralized crypto-backed coin, a sharp drop in collateral value or **failed/illiquid auctions** during a crash could under-collateralize the system and threaten the peg ([[depeg]] risk). FPS equity is the first-loss buffer; if losses exceed it, ZCHF holders bear the shortfall.
- **Auction / mechanism risk:** The oracle-free model depends on challengers having capital and incentive to police bad positions; in thin markets or fast crashes, mispriced positions may go unchallenged.
- **Yield-source / counterparty (FPS) risk:** FPS holders earn minter interest but absorb defaults; their return is compensation for genuine credit/liquidation risk, not a deposit rate.
- **Redemption-gating risk:** There is no fiat redemption window — exiting at par relies on DEX liquidity and minter arbitrage, which can break down in stress.
- **Smart-contract risk:** Bugs in the minting, auction, or governance contracts could be exploited.
- **Liquidity risk:** With a market cap of ~$45M and modest on-chain volume, large redemptions or trades can move the price away from peg temporarily.
- **Governance risk:** Decentralized governance can be slow to respond to a crisis and is subject to capture by large FPS holders.

## Trading / Usage Playbook

- **Judge the peg in CHF, not USD.** Convert the USD quote by the live CHF/USD rate (~1.24); on-peg ≈ 1.00 CHF. A USD-quoted move is usually FX, not a depeg.
- **Use ZCHF for franc-denominated, dollar-free crypto exposure**; pair with EURe/USDC to manage cross-currency basis.
- **For yield, FPS — not ZCHF — is the vehicle**, and it is a leveraged claim on protocol income with first-loss exposure; size accordingly.
- **Watch auction activity and collateral concentration** as health signals; thin challenge participation in a downturn is a warning.
- **Mind liquidity:** at ~$45M cap, exit large positions gradually; deep par redemption is not guaranteed in a crunch.

## See Also

- [[stablecoin]]
- [[swiss-franc]]
- [[forex]]
- [[dai]] — USD CDP analogue
- [[usda-2]] — BTC-CDP design
- [[ethena-usde]] — single-token yield dollar (contrast)
- [[crypto-markets]]
- [[ethereum]]
- [[defi]]
- [[depeg]]

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- General market knowledge; no specific wiki source ingested yet.


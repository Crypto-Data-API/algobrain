---
title: "Liquity"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoin]
aliases: ["BOLD", "LQTY", "LUSD", "Liquity"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.liquity.org/"
related: ["[[collateralization]]", "[[crypto-markets]]", "[[dai]]", "[[defi]]", "[[depeg]]", "[[ethereum]]", "[[frax-share]]", "[[governance-token]]", "[[liquid-staking]]", "[[stablecoin]]"]
---

# Liquity

**Liquity** is a decentralized borrowing protocol that lets users draw **interest-free** loans against [[ethereum|Ether]] collateral, denominated in its native [[stablecoin]] **LUSD** (which targets a soft $1.00 peg). **LQTY** is the protocol's secondary token: it captures protocol fee revenue via staking and incentivizes early liquidity. Liquity is notable for being **immutable and governance-free** at its core — the original v1 contracts cannot be upgraded — and for a [[collateralization|collateral]] ratio as low as 110%. It ranks **#836** by market capitalization. The protocol later launched **Liquity v2**, issuing a separate stablecoin, **BOLD**, with user-set interest rates.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, the LQTY token trades at **$0.20051** with a market cap of about **$19.77M** (rank **#836**). It was down **-0.63%** over 24 hours and down **-2.62%** over the trailing 7 days, in a bear-market regime ([[bitcoin|BTC]] near $64,508; Fear & Greed Index 21, "Extreme Fear"). **Note:** LQTY is the volatile secondary/fee token; it is distinct from **LUSD**, the protocol's $1.00-targeting stablecoin, and from **BOLD**, the v2 stablecoin.

---

## Key Facts

| Field | Detail |
|---|---|
| **Secondary / Fee Token** | LQTY |
| **Stablecoin (v1)** | LUSD (interest-free, ETH-collateralized, targets $1.00) |
| **Stablecoin (v2)** | BOLD (user-set borrow rates, multi-collateral) |
| **Market Cap Rank** | #836 |
| **Market Cap (LQTY)** | $19,769,579 |
| **Current Price (LQTY)** | $0.20051 |
| **24h Change** | -0.63% |
| **7d Change** | -2.62% |
| **Min Collateral Ratio (v1)** | 110% |
| **Governance** | Governance-free / immutable core (v1) |
| **Categories** | Decentralized Finance (DeFi), Ethereum Ecosystem, Arbitrum Ecosystem |
| **Website** | [https://www.liquity.org/](https://www.liquity.org/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Liquity (launched 2021) lets a borrower deposit ETH into a position called a **Trove** and mint **LUSD** against it at **0% interest**, paying only a one-time borrowing fee, while maintaining a minimum [[collateralization|collateral]] ratio of **110%** — far more capital-efficient than collateral-heavy peers. LUSD is a decentralized [[stablecoin]] redeemable against the system's ETH collateral, which gives it a hard arbitrage-enforced peg mechanism.

The protocol is **non-custodial, immutable, and governance-free**: the v1 smart contracts are fixed and cannot be changed by any DAO or admin, removing a major attack/centralization surface but also meaning the system cannot be patched if a flaw is found. LQTY is the protocol's secondary token, earned by Stability Pool depositors and others, and stakeable to receive a share of borrowing and redemption fees.

---

## How LUSD Holds Its Peg

LUSD uses a multi-layered, arbitrage-driven peg rather than discretionary management:

1. **Hard redemption floor (~$1.00).** Anyone can redeem LUSD for **$1.00 worth of ETH** from the riskiest Troves at any time. If LUSD trades below $1, redeemers profit by buying cheap LUSD and redeeming it for $1 of ETH, pushing the price back up. This creates a strong lower bound near $1.00.
2. **Borrowing-cost ceiling (~$1.10).** Because a borrower can mint 1 LUSD for as little as $1 of effort (and the system is willing to issue at par when demand is high), arbitrage tends to cap LUSD's upside; the practical band is roughly $1.00–$1.10.
3. **Stability Pool.** LUSD deposited in the Stability Pool absorbs liquidations: when a Trove falls below 110%, its debt is cancelled against pooled LUSD and depositors receive the liquidated ETH (typically at a discount), keeping the system solvent and the stablecoin fully backed.
4. **Redistribution / Recovery Mode.** If the Stability Pool is empty, liquidated debt and collateral are redistributed across remaining Troves. A system-wide "Recovery Mode" tightens requirements when the total collateral ratio drops below 150%.

### Worked example: a Trove and its liquidation

Suppose ETH is $3,000 and a borrower opens a Trove by depositing **10 ETH** ($30,000) and minting **20,000 LUSD** (plus a one-time borrowing fee and a 200 LUSD gas-reserve). Their collateral ratio is 30,000 / 20,000 = **150%**. Now ETH falls to **$2,150**: collateral is worth $21,500, so the ratio drops to ~107.5% — below the 110% minimum. The Trove becomes liquidatable. A liquidation cancels the Trove's ~20,000 LUSD debt against the **Stability Pool** (burning 20,000 pooled LUSD) and distributes the Trove's ~10 ETH to Stability Pool depositors. Because depositors receive ~$21,500 of ETH for ~$20,000 of burned LUSD, they net a ~7–8% gain on the absorbed collateral — the incentive that keeps the pool funded. The borrower keeps the LUSD they minted but loses their collateral. This is why Troves near the 110% floor are dangerous: a modest ETH drop wipes them out.

### Stablecoin landscape: where LUSD/BOLD fit

| Stablecoin | Backing | Peg mechanism | Governance | Key trait |
|---|---|---|---|---|
| **LUSD** (Liquity v1) | ETH only | Hard redemption to $1 of ETH; 110% min CR | **Governance-free / immutable** | Most decentralized; trades at a *premium* in stress |
| **BOLD** (Liquity v2) | ETH + [[liquid-staking\|LSTs]] | Redemption + user-set rates | Minimal | Yield-bearing for SP depositors |
| [[dai\|DAI]] (MakerDAO/Sky) | Multi-collateral incl. RWA/USDC | Redemption + PSM + DSR | MKR/SKY DAO | Largest decentralized stablecoin |
| frxUSD ([[frax-share\|Frax]]) | RWA/T-bills + crypto | AMO + collateral | Frax DAO | Yield from reserve AMOs |
| USDC / USDT | Off-chain fiat/T-bills | Issuer redemption | Centralized | Fully centralized, deepest liquidity |

Liquity's niche is being the **most censorship-resistant** of the crypto-collateralized stablecoins: no admin keys, no off-chain collateral, no DAO that can change the rules — a deliberate trade of upgradeability for credible neutrality.

### Liquity v2 and BOLD

In 2025, Liquity launched **v2**, introducing the **BOLD** stablecoin. Unlike v1's fixed 0% model, v2 lets borrowers **set their own interest rate**, with that rate determining redemption priority (lower-rate Troves are redeemed first). v2 broadens collateral options (e.g., ETH liquid-staking tokens) and routes much of the interest income to LUSD/BOLD stability providers and to LQTY stakers, strengthening LQTY's fee-capture role. v1 (LUSD) continues to operate alongside v2.

**Why user-set rates matter:** v1's 0% interest was elegant but inflexible — the only lever to defend the peg was the redemption queue, which always hit the lowest-collateral Troves regardless of their owners' preferences. In v2, the borrower chooses an interest rate that signals how badly they want to avoid being redeemed: a borrower who sets a higher rate moves further back in the redemption queue (they "pay" for redemption protection), while low-rate Troves are first in line. This creates a market-driven term structure for borrowing costs and lets BOLD's effective supply respond to demand, addressing v1's chronic issue of LUSD trading at a *premium* (because borrowers had little incentive to mint more when the peg ran hot). BOLD interest income is then paid out to Stability Pool depositors and a portion to **staked LQTY**, giving LQTY a clearer, usage-linked cash flow than the one-off-fee model of v1.

| Dimension | Liquity v1 (LUSD) | Liquity v2 (BOLD) |
|---|---|---|
| Interest model | **0% interest**, one-time borrow fee | **User-set interest rate** (ongoing) |
| Collateral | ETH only | ETH + [[liquid-staking\|LSTs]] (e.g., wstETH, rETH) |
| Redemption priority | Lowest collateral ratio first | Lowest interest rate first |
| Min collateral ratio | 110% | Per-collateral (e.g., ~110–120%) |
| Governance | Fully immutable / governance-free | Minimal governance (e.g., incentive direction) |
| LQTY value accrual | Share of borrow/redemption fees | Plus a share of ongoing interest income |

---

## Token Roles

- **LUSD** — the v1 decentralized [[stablecoin]] (the product). Targets $1.00 via the redemption mechanism above.
- **BOLD** — the v2 stablecoin with market-set borrow rates.
- **LQTY** — the protocol's value-accrual/fee token. Stakers earn a pro-rata share of borrowing and redemption fees; LQTY also funded early Stability Pool / liquidity incentives. LQTY is **not** a stablecoin and is freely volatile.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 98.67M LQTY |
| **Total Supply** | 100.00M LQTY |
| **Max Supply** | 100.00M LQTY |
| **Fully Diluted Valuation** | $27.39M |
| **Market Cap / FDV Ratio** | 0.99 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $146.94 (2021-04-05) |
| **Current vs ATH** | -99.81% |
| **All-Time Low** | $0.2606 (2026-02-13) |
| **Current vs ATL** | +5.15% |
| **24h Change** | -1.03% |
| **7d Change** | -1.39% |
| **30d Change** | -0.79% |
| **1y Change** | -40.33% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x6dea81c8171d0ba574754ef6f8b412f2ed88c54d` |
| Arbitrum One | `0xfb9e5d956d889d91a82737b9bfcdac1dce3e1449` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | LQTY/USDT | N/A |
| Kraken | LQTY/EUR | N/A |
| Bitget | LQTY/USDT | N/A |
| KuCoin | LQTY/USDT | N/A |
| Crypto.com Exchange | LQTY/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X6DEA81C8171D0BA574754EF6F8B412F2ED88C54D/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0X6DEA81C8171D0BA574754EF6F8B412F2ED88C54D/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.liquity.org/](https://www.liquity.org/) |
| **Twitter** | [@LiquityProtocol](https://twitter.com/LiquityProtocol) |
| **Reddit** | [https://www.reddit.com\/r/Liquity/](https://www.reddit.com\/r/Liquity/) |
| **Discord** | [https://discord.gg/2up5U32](https://discord.gg/2up5U32) |
| **GitHub** | [https://github.com/liquity/dev](https://github.com/liquity/dev) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 352 |
| **GitHub Forks** | 339 |
| **Pull Requests Merged** | 47 |
| **Contributors** | 5 |

---

## Risks

- **Depeg risk (LUSD).** Although the redemption mechanism gives LUSD a strong ~$1.00 floor, it has historically traded at a *premium* (above $1.00) during stress because it is a flight-to-safety decentralized asset; sustained premiums can hurt borrowers and reduce usability. Hard [[depeg|depegs]] below $1 are arbitraged away by redemptions but are not impossible under extreme conditions.
- **Immutability trade-off.** Governance-free immutability removes admin/centralization risk but means a discovered bug in v1 **cannot be patched** — the only remedy is migration. This is a deliberate, double-edged design choice.
- **ETH collateral / liquidation risk.** Troves at the 110% minimum are highly sensitive to ETH price drops; rapid declines can trigger liquidations, and during severe events the Stability Pool can be depleted, forcing debt redistribution onto remaining borrowers.
- **Redemption risk for borrowers.** Low-collateral (v1) or low-interest (v2) Troves are redeemed first; a borrower can have their position partially closed against their wishes when LUSD/BOLD trades below peg.
- **LQTY token risk.** LQTY is a small-cap (~$19.8M, rank ~#836), volatile fee token whose value depends on protocol borrowing/redemption activity; it is sensitive to broad [[bitcoin|BTC]]-led sentiment and is ~99.8% below its 2021 ATH (~$146.94).
- **General DeFi risk.** Oracle dependence (ETH price feeds), smart-contract risk in v2's newer contracts, and regulatory uncertainty around stablecoins.

*Nothing here is investment advice; figures are point-in-time snapshots that can change rapidly. LQTY (fee token) is distinct from LUSD/BOLD (stablecoins).*

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

- **2021** — Liquity v1 launched on Ethereum (interest-free ETH-backed LUSD borrowing, 110% min collateral, governance-free).
- **2025** — Liquity v2 launched, introducing the **BOLD** stablecoin with user-set interest rates and expanded collateral, strengthening LQTY fee accrual.

> *Additional events will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[stablecoin]]
- [[collateralization]]
- [[depeg]]
- [[defi]]
- [[dai]]
- [[frax-share]]
- [[liquid-staking]]
- [[governance-token]]
- [[usual]]
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge (incl. publicly documented Liquity v1 mechanism — Troves, Stability Pool, redemption peg — and the v2/BOLD launch with user-set interest rates); no specific narrative wiki source ingested yet.

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.26M |
| **Market Cap Rank** | #913 |
| **24h Range** | $0.1653 — $0.1714 |
| **Last Updated** | 2026-07-16 |

---

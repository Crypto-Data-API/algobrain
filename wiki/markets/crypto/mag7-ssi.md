---
title: "MAG7.ssi"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, real-world-assets]
aliases: ["MAG7.SSI"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://sosovalue.com/"
related: ["[[base]]", "[[bitcoin]]", "[[crypto-markets]]", "[[defi-index]]", "[[ethereum]]", "[[real-world-assets]]"]
---

# MAG7.ssi

**MAG7.ssi** (ticker **MAG7.SSI**) is a tokenized **spot crypto index** wrapper issued through the **SoSoValue Index (SSI) Protocol**. It repackages a basket of the **top-7 crypto projects by market cap** (its "Magnificent-7 of crypto") into a single on-chain **Wrapped Token** that tracks the value of the underlying basket — passive index investing delivered as one ERC-20 on [[base|Base]]. Each MAG7.SSI token represents a proportional claim on the underlying spot crypto assets held by the protocol, making it a structured, index-style on-chain asset for diversified crypto beta. (Note: this is a **crypto-asset index**, not a tokenized equity index — the basket holds spot crypto, so it moves with the crypto market, not the stock market.)

## Market Data

| Field | Value |
|---|---|
| **Ticker** | MAG7.SSI |
| **Market Cap Rank** | #349 |
| **Current Price** | $0.4232 |
| **Market Cap** | $71.4M |
| **24h Volume** | $606,558 |
| **24h Change** | +2.41% |
| **Circulating Supply** | 168.61M MAG7.SSI |
| **Total Supply** | 168.61M MAG7.SSI |
| **All-Time High** | $1.35 |
| **All-Time Low** | $0.3850 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

At $0.4232 the token sits roughly 69% below its $1.35 all-time high and just above its $0.3850 all-time low — reflecting the broad crypto drawdown, since the index holds spot crypto assets and therefore moves with the underlying basket. With ~$0.6M/24h volume it is the most actively traded of this RWA/index cohort, consistent with a wrapped index that is meant to be bought and held on-chain.

---

## Architecture: mechanism, backing & index methodology

- **Underlying assets.** A basket of the **top-7 crypto projects by market cap** with strong liquidity and social consensus, held as **spot**. The structure uses an initial ~**10% equal-weight floor** allocation to give meaningful weight to second-tier leaders beyond [[bitcoin|BTC]] and [[ethereum|ETH]] — i.e. it deliberately caps the dominance of the very largest names so the basket is genuinely diversified across seven assets rather than being a de-facto BTC/ETH tracker.
- **Wrapper / issuer.** The **SoSoValue Index (SSI) Protocol** mints a **Wrapped Token (SSI)** backed by the underlying spot basket via on-chain smart contracts. Market cap equals the value of the held assets, so the token is a **1:1 claim** on the basket (NAV-backed).
- **Index methodology — selection & weighting.** Constituents are chosen by **market-cap ranking** plus liquidity and consensus screens; weighting starts from the equal-weight floor described above, which is what differentiates this from a pure market-cap-weighted index (where BTC alone would dominate).
- **Rebalancing.** **Monthly rebalance** with a **buffer setting** — designed to admit emerging large-caps promptly while minimizing turnover/trading friction from over-frequent reconstitution. The buffer reduces "churn" at the boundary (an asset must clearly cross the threshold, not merely flicker around it, to enter or exit).
- **Custody / backing.** Assets are held **on-chain** by the protocol's smart contracts (a crypto-native index), distinguishing it from tokenized TradFi products where the underlying is off-chain Treasuries, ETF shares, or vaulted gold. Backing is therefore on-chain verifiable rather than dependent on an off-chain custodian/auditor.
- **Access / permissioning.** As a DeFi index token on [[base|Base]], MAG7.SSI is generally **permissionless** to hold and trade on-chain, unlike the KYC-gated tokenized-fund products in this cohort.
- **Mint / redeem (NAV arbitrage).** Holders can mint/redeem against the underlying basket through the SSI protocol or trade the wrapped token directly on-chain. This mint/redeem path is the arbitrage mechanism that keeps the token price aligned with basket NAV: when the token trades above NAV, arbitrageurs mint and sell; when below, they buy and redeem.

---

## Comparison vs alternative ways to get crypto-index exposure

| Approach | What it is | Diversification | Custody | Access |
|---|---|---|---|---|
| **MAG7.SSI** | On-chain wrapped top-7 spot index, monthly rebalance, ~equal-weight floor | 7 large-caps, capped concentration | On-chain (smart contract) | Permissionless on [[base|Base]] |
| Hold BTC + ETH directly | Two-asset DIY | 2 assets, heavy BTC/ETH | Self-custody | Permissionless |
| DIY top-7 basket | Manually buy/rebalance 7 tokens | 7 assets, your weights | Self-custody | Permissionless, but high effort/gas |
| Tokenized-equity index (e.g. xStock / Ondo S&P-style) | Wrapper on a **stock** index | Equities, not crypto | Off-chain shares + custodian | Often KYC-gated |

MAG7.SSI's value proposition versus a DIY basket is **automated construction, monthly rebalancing, and one-token composability** — you get diversified crypto beta without manually buying, weighting, and periodically rebalancing seven assets (which is costly in gas and attention). Versus simply holding BTC+ETH, it adds breadth to five more large-caps with a concentration cap. It is fundamentally **different from a tokenized-equity index** ([[real-world-assets|RWA]] stock wrappers) because its underlying is on-chain spot crypto, so its risk and return are pure crypto beta, not equity beta.

---

## How / where it trades

- **Primary market.** Mint/redeem the wrapped token against the underlying basket via the SoSoValue Index protocol (the NAV-arbitrage path).
- **Secondary market.** On-chain DEX liquidity on [[base|Base]] (its native chain); ~$0.6M/24h volume, the **deepest secondary activity** among the RWA/index tokens in this cohort.
- **Hours.** Trades and transfers **24/7** on-chain — there is no off-chain market to close, since the underlying is spot crypto (unlike tokenized-stock indices, which reference market-hours equities).
- **Tracking.** Tracks the net asset value of the top-7 basket; on-chain price can deviate slightly from basket NAV between rebalances or under thin liquidity, with mint/redeem arbitrage pulling it back to NAV.
- **Composability.** As an ERC-20 on Base, MAG7.SSI can be used as a single, diversified collateral or LP asset on-chain — convenient for treasuries or strategies that want broad crypto beta in one token.

---

## Narrative & catalysts

MAG7.SSI sits in the **on-chain index / "crypto beta in one token"** narrative — the DeFi analog of an index fund or ETF, riding the broader theme of structured products and RWA-style wrappers moving on-chain. The branding borrows the equity market's "Magnificent Seven" framing but applies it to crypto's largest names. Catalysts: growth of the [[base|Base]] DeFi ecosystem where it is native; integrations that let MAG7.SSI serve as collateral/LP across protocols; and broader demand for passive, diversified crypto exposure as opposed to single-asset bets. Its return is **pure crypto beta**, so in the current bottoming/accumulation macro regime (Fear & Greed 21, "Extreme Fear", as of 2026-06-22) it is directly exposed to the risk-off tape — but that same regime is where accumulation of diversified beta is a recognized (if higher-risk) playbook.

---

## History / timeline

- **Launch** — issued via the SoSoValue Index (SSI) Protocol as a wrapped top-7 crypto spot index token on [[base|Base]], with a ~10% equal-weight floor and monthly buffered rebalancing.
- **All-time high $1.35 / all-time low $0.3850** — the historical band tracks the crypto market's own swing; the token holds spot crypto and therefore mirrors the basket (exact dates not in the snapshot, so not asserted).
- **2026-06-21** — snapshot: $0.4232 (≈ -69% from ATH, just above ATL), ~$71.4M market cap, ~$0.6M/24h volume (deepest in this cohort), rank #349, deployed on Base.

---

## Risks

- **Market risk (crypto beta).** Full exposure to crypto drawdowns — the token fell from $1.35 to ~$0.42 (roughly -69%) tracking the basket. It is diversified across seven large-caps but offers **no protection from broad crypto declines**.
- **Smart-contract risk.** The wrapper, custody of the underlying basket, and rebalancing all run through smart contracts; a contract exploit could impair backing — the principal tail risk for an on-chain-custodied index.
- **NAV-gap / tracking & rebalance risk.** Monthly rebalancing with a buffer means the index can lag fast-moving market-cap changes, and the token price can dislocate from NAV between rebalances or in low liquidity.
- **Concentration / methodology risk.** Top-7-by-market-cap is inherently weighted to a few assets even with the equal-weight floor; returns hinge on the methodology and SoSoValue's index governance (selection screens, buffer, rebalance cadence).
- **Issuer / protocol risk.** Dependence on the SoSoValue Index protocol for accurate construction, rebalancing, and redemption.
- **Liquidity risk.** Although the most liquid in this cohort, secondary depth is still modest relative to market cap, which can widen slippage in stressed markets.
- **Macro backdrop.** As of 2026-06-22 the crypto [[fear-and-greed-index|Fear & Greed Index]] reads 21 ("Extreme Fear"). Unlike the Treasury/gold tokens here, MAG7.SSI is pure crypto beta and is directly exposed to this risk-off regime.

---

## Trading / usage playbook

- **Use it as a one-token diversified crypto beta sleeve.** MAG7.SSI is most useful when you want broad large-cap crypto exposure without managing seven positions and their rebalancing — a passive-index substitute for a DIY basket.
- **Mind it is beta, not a hedge.** It will fall with the market; it diversifies single-name risk but provides no downside protection in a broad selloff. Pair with a non-correlated asset (e.g. tokenized gold like [[matrixdock-gold]]) if a hedge is the goal.
- **Arbitrage NAV gaps via mint/redeem.** If the token trades meaningfully off basket NAV, the protocol's mint/redeem path is the mechanism to capture the gap; for ordinary holders this same mechanism is why price tends to revert to NAV.
- **Size to ~$0.6M/24h depth.** It is the most liquid token in this cohort but still modest; large orders should account for slippage on the Base DEX pools.

---

## Platform & chain information

**Deployment:** [[base|Base]] (Base Native)

| Chain | Address |
|---|---|
| Base | `0x9e6a46f294bb67c20f1d1e7afb0bbef614403b55` |

---

## See Also

- [[real-world-assets]] / [[rwa]] — broader tokenized-asset context
- [[defi-index]] — on-chain index products
- [[bitcoin]], [[ethereum]] — largest basket constituents
- [[crypto-markets]]
- [[base]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.


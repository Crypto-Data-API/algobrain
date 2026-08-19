---
title: "Exchange Tokens"
type: concept
created: 2026-07-17
updated: 2026-08-19
status: draft
tags: [crypto, exchange, market-microstructure, on-chain]
aliases: ["CEX Tokens", "Exchange Coins", "Exchange Utility Tokens"]
domain: [crypto, market-microstructure]
prerequisites: ["[[centralized-exchange]]"]
difficulty: beginner
---

# Exchange Tokens

**Exchange tokens** — BNB, OKB, KCS, BGB — are utility tokens issued by, and economically tied to, a single [[centralized-exchange|centralized exchange's]] business: they earn fee discounts, launchpad access, and (usually) a share of the exchange's profit via buyback-and-burn. This makes them a distinct sub-category from [[governance-token|governance tokens]]: a governance token (UNI, AAVE, COMP) grants voting rights over a *decentralized protocol* that no single company controls, while an exchange token's value tracks the solvency, trading volume, and regulatory standing of *one specific centralized company* — a corporate-equity-like claim wrapped in a token, not a DAO membership right.

## How It Works

Exchange tokens typically launch as a standard ERC-20 (BNB launched on Ethereum in 2017; migrated to its own chain later) and accrue value through three overlapping mechanisms:

1. **Fee discounts.** Paying trading fees in the exchange's native token, or simply holding a balance of it, reduces the fee rate charged on that exchange — a direct, mechanical demand driver tied to the exchange's own trading volume.
2. **Profit-funded buyback-and-burn.** The exchange periodically uses a portion of its trading revenue to buy the token on the open market and permanently destroy it, shrinking supply. Unlike a DeFi protocol's fee switch (which is a governance decision token holders vote on), a CEX buyback is a discretionary corporate policy — token holders benefit from it but have no binding vote to enforce or expand it.
3. **Ecosystem utility.** Many exchange tokens have grown into gas tokens for the exchange's own chain or L2 (BNB → BNB Chain; OKB → OKX's X Layer; BGB → the Morph L2 since a September 2025 partnership), giving them a second demand source beyond the exchange itself.

**The concentration risk this creates is structural, not incidental.** Because an exchange token's value is a claim on one company's ongoing solvency, it inherits that company's counterparty risk in full — a risk that governance tokens, spread across a decentralized validator/holder set, do not carry in the same way.

## Concrete Examples

- **BNB (Binance):** 200M max supply, ~67% circulating as of mid-2026, reduced via a formula-driven **quarterly Auto-Burn** (scaled to BNB Chain block production and price) plus a real-time **BEP-95** gas-fee burn, both running until supply reaches a 100M floor.
- **OKB (OKX):** the sharpest recent supply-shock case study — in **August 2025**, OKX burned **52% of OKB's supply in a single stroke**, hard-capping it at **21,000,000 tokens** (a deliberate echo of Bitcoin's cap). Price roughly tripled within days of the announcement before giving back most of the re-rate as flows normalized — a clean illustration of how a discretionary corporate action, not a governance vote, moves these tokens.
- **KCS (KuCoin Token):** quarterly buyback-and-burn funded by **10% of KuCoin's net profit**, targeting a long-run 100M supply.
- **BGB (Bitget Token):** an aggressive buyback-and-burn program targeting a final 100M supply, plus a September 2025 role expansion into gas/governance token for the Morph L2.
- **FTT (FTX Token, defunct) — the cautionary tale:** FTX's affiliated trading firm Alameda Research held a large FTT position as loan collateral and balance-sheet asset. A November 2022 CoinDesk report detailing how much of Alameda's balance sheet was illiquid FTT, followed by Binance publicly announcing it would liquidate its own FTT holdings, triggered the bank run that collapsed FTX within days and wiped out an estimated **$8-10 billion** in customer funds — the starkest demonstration that an exchange token's value can evaporate exactly when the exchange behind it fails.

## Trading Relevance

- **Burn events as calendar catalysts:** scheduled or announced burns (BNB's quarterly Auto-Burn, OKB's one-off August 2025 cap) are tradable, dated supply-reduction events, structurally the mirror image of the unlock-driven selling most altcoins face — relevant to the same calendar-event framing used in [[token-unlock-supply-event]].
- **[[narrative-trading]]:** exchange tokens often decouple from broad crypto beta and instead trade on exchange-specific news (regulatory settlements, volume share shifts, listing wars), making them a distinct rotation sleeve rather than a pure BTC/ETH-beta proxy.
- **Counterparty concentration risk:** holding an exchange token is functionally closer to holding unsecured exposure to a single company than to holding a decentralized protocol's governance rights — the FTT/[[ftx]] precedent is the standard reference case for sizing this risk, and it is why proof-of-reserves disclosures are watched specifically around exchange-token exposure.
- **[[cross-exchange-arbitrage]]:** BNB, OKB, and KCS each have thinner order-book depth on their own perp/spot markets than the majors, meaning cross-venue basis and funding on these names can dislocate more than on BTC/ETH — a liquidity-driven opportunity and risk in the same trade.
- **Regulatory-event sensitivity:** because value accrues from one exchange's *ongoing legal ability to operate*, a DOJ settlement, license revocation, or delisting action is a first-order price driver for exchange tokens in a way it typically is not for protocol governance tokens.

## Related

- [[centralized-exchange]] — the business each exchange token is a claim on
- [[governance-token]] — the protocol-governance sub-category exchange tokens are distinct from
- [[bnb]] — Binance's exchange token
- [[okb]] — OKX's exchange token, the 2025 supply-shock case study
- [[kucoin-shares]] — KuCoin's exchange token
- [[bitget-token]] — Bitget's exchange token
- [[ftx]] — the collapse that shows exchange-token concentration risk realized
- [[binance]] — issuer of BNB
- [[okx]] — issuer of OKB

## Sources

- General crypto market-structure knowledge; no specific wiki source ingested yet.

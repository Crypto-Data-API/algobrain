---
title: "Avant USD"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stablecoins]
aliases: ["AVUSD", "avUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.avantprotocol.com/"
related: ["[[stablecoins]]", "[[ethena-usde]]", "[[usde]]", "[[avalanche]]", "[[crypto-markets]]"]
---

# Avant USD

**Avant USD** (ticker AVUSD, styled "avUSD") is a DeFi stable-value dollar token issued by the **Avant** protocol, primarily on **[[avalanche|Avalanche]]**. It targets a soft peg of **1 avUSD ≈ US$1**. avUSD is the transactional, non-yield token; **savUSD** is its staked, yield-bearing counterpart. Avant was established in June 2024 with the stated goal of bridging DeFi and TradFi yield within a single stable-value token family. It belongs to the **yield-bearing / synthetic-dollar** category alongside [[ethena-usde]]'s [[usde]], rather than to fiat-reserve dollars like [[usdc]].

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | AVUSD |
| **Price** | $0.999832 |
| **Peg target** | US$1.00 |
| **Market cap** | $110.95M |
| **Market-cap rank** | #252 |
| **24h volume** | $4,201 |
| **24h change** | +0.11% |
| **Circulating supply** | 110.97M AVUSD |
| **Total supply** | 110.97M AVUSD |
| **All-time high** | $1.061 (2026-05-19) |
| **All-time low** | $0.951733 (2026-04-20) |

avUSD held its peg tightly at the snapshot (~$0.9998), but reported 24h volume of only ~$4.2K is extremely thin relative to its ~$111M market cap — consistent with a token held for savings/yield rather than actively traded.

---

## Architecture: the avUSD / savUSD two-token model

Avant uses a **two-token, stake-for-yield design** that has become the standard pattern for the new wave of yield-bearing [[stablecoins]]:

- **avUSD — the stable leg.** The dollar-pegged, liquid, transactional token. It is intended for liquidity, payments, and collateral, and **does not accrue yield while simply held** in a wallet. This keeps the "money" token clean and composable, and (importantly) sidesteps the regulatory friction that attaches to instruments that pay holders a return directly.
- **savUSD — the yield leg.** A user stakes avUSD to mint savUSD, which **accrues the protocol's generated yield over time**. savUSD typically appreciates against avUSD in a vault-share (ERC-4626-style) accrual model: the redemption rate of savUSD → avUSD rises as yield is earned, rather than via rebasing balances. Unstaking returns avUSD (subject to any protocol unbonding/cooldown terms).

### Where the yield comes from

Avant's stated model generates yield from **DeFi strategies and stable-value deployment** rather than from a single pass-through fiat-reserve interest stream. This places it in the same broad family as synthetic / yield-bearing dollars such as [[usde]], where returns are produced from on-chain and market-based strategies. The crucial implication for risk: unlike a fiat-reserve dollar whose yield is bank/T-bill interest on safe assets, a strategy-based yield dollar's backing and return depend on the **performance and solvency of those strategies** — if they underperform or take a loss, both savUSD yield and the avUSD backing can be impaired. (The precise current strategy mix is set by the protocol and is not detailed in the CoinGecko snapshot.)

### Mint / redeem

avUSD is minted and redeemed through the Avant protocol against its backing; savUSD is obtained by staking avUSD and redeemed by unstaking. Peg defense relies on this primary mint/redeem path plus secondary-market arbitrage: when avUSD trades below $1, arbitrageurs can buy and redeem at par; when above, they mint and sell.

---

## Comparison vs peer yield-bearing & reserve dollars

| Token | Yield source | Stable / yield split | Backing | Issuer |
|---|---|---|---|---|
| **avUSD / savUSD** | DeFi strategies + stable-value deployment | avUSD (flat) + savUSD (yield) | On-chain strategy collateral | Avant |
| [[usde]] / [[susde]] | Delta-neutral basis (staked-ETH yield + perp funding) | USDe (flat) + sUSDe (yield) | Crypto collateral + short perps | [[ethena-usde]] |
| [[usdm]] | Tokenized US Treasuries (rebasing) | Single rebasing token | Off-chain T-bills | Mountain Protocol |
| [[usdc]] | Reserve interest (kept by issuer) | Single token, no holder yield | Off-chain cash + T-bills | Circle |

avUSD's closest structural peer is **[[usde]]**: both split a flat "money" token from a staked yield token, and both source yield from market/on-chain strategies rather than from passed-through bank interest. The principal difference is the **strategy engine** — Ethena's is a specific, transparent delta-neutral basis trade, whereas Avant's is a broader, protocol-managed DeFi strategy book — and scale, where avUSD (~$111M) is a fraction of USDe's size, implying thinner liquidity and a smaller arbitrage backstop.

---

## How and where it trades

avUSD is an on-chain token concentrated in the [[avalanche|Avalanche]] ecosystem; CoinGecko shows **no major centralized-exchange listings**. Liquidity is DEX-based, and the very low ~$4.2K daily volume indicates avUSD is held mostly as a **savings/collateral instrument** (often staked into savUSD) rather than actively traded — so the quoted price reflects only thin secondary flow. Composability is real but shallow at current scale: avUSD can be used as collateral and in liquidity pools, but the limited depth caps how much can move without slippage.

Contract address:

| Chain | Address |
|---|---|
| Avalanche | `0x24de8771bc5ddb3362db529fc3358f2df3a0e346` |

---

## Narrative & catalysts

avUSD rides the **2024–2026 "yield-bearing dollar" narrative** — the migration of stablecoin demand from non-yielding fiat dollars toward tokens that route DeFi/TradFi yield back to stakers. Catalysts that would matter for avUSD specifically: growth of the [[avalanche|Avalanche]] DeFi ecosystem where it is native; integrations that make savUSD usable as collateral and in money markets (driving demand for the yield leg); and the competitiveness of its yield versus [[usde]] and tokenized-Treasury dollars. The main headwind is the regulatory trajectory for yield-bearing dollar tokens, which is still being defined across jurisdictions and could constrain distribution.

---

## History / timeline

- **June 2024** — Avant protocol established, launching the avUSD / savUSD stable-value family.
- **2026-04-20** — avUSD prints its all-time low of **$0.951733** (~5% under peg), evidence it can drift below par under stress and thin liquidity.
- **2026-05-19** — avUSD prints its all-time high of **$1.061** (~6% over peg), the symmetric upside dislocation.
- **2026-06-21** — snapshot: peg tightly held at ~$0.9998 on ~$4.2K daily volume; ~$111M market cap, rank #252.

---

## Risks

- **De-peg risk.** avUSD reached an ATL of $0.952 on 2026-04-20, showing it can drift below peg under stress; extremely thin secondary liquidity means even small redemptions can move the price. The current "Extreme Fear" regime (crypto Fear & Greed ~21 as of 2026-06-22, bottoming/accumulation phase) raises stress risk.
- **Collateral / strategy risk.** Yield depends on the protocol's underlying DeFi strategies; if those strategies underperform or incur losses, both savUSD yield and the avUSD backing can be impaired. This is the defining risk of strategy-based yield dollars versus reserve dollars.
- **Issuer / smart-contract risk.** Users rely on the Avant protocol's contracts, custody of strategy collateral, and accounting (the savUSD vault-share math in particular).
- **Redemption-gating / cooldown risk.** Unstaking savUSD may be subject to unbonding terms; in a rush for the exit, the cooldown can trap holders in the yield token while the peg moves.
- **Liquidity risk.** Near-negligible on-chain trading volume makes orderly exit difficult in a panic.
- **Regulatory risk.** Yield-bearing dollar tokens face evolving regulatory treatment across jurisdictions.

---

## Trading / usage playbook

- **Hold the right leg for the job.** Use **avUSD** when you need a liquid, composable dollar (payments, collateral, LP); stake into **savUSD** only when you intend to hold for yield and can tolerate any unbonding cooldown.
- **Mind the thin book.** With ~$4.2K daily volume, treat avUSD as a held instrument, not a trading vehicle — large entries/exits should go through the protocol's primary mint/redeem rather than the secondary market where possible.
- **Compare net yield, not headline yield.** Weigh savUSD's yield against [[susde]] and tokenized-Treasury dollars ([[usdm]]) on a risk-adjusted basis — strategy yield carries strategy risk that reserve yield does not.
- **Watch the peg band.** The ~$0.95–$1.06 historical range is the practical band; entries near the lower edge offer a better redemption-arbitrage margin of safety, but only if the primary redemption path is open.

---

## Related

- [[stablecoins]] — landscape overview
- [[ethena-usde]], [[usde]] — synthetic / yield-bearing dollar peers (closest analog)
- [[usdc]], [[usdt]], [[dai]] — peer dollars
- [[avalanche]] — host chain
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- Protocol description from Avant ([https://www.avantprotocol.com/](https://www.avantprotocol.com/)). General market knowledge; no specific wiki source ingested yet for the avUSD/savUSD yield mechanism.

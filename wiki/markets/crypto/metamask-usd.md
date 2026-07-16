---
title: "MetaMask USD"
type: market
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoin]
aliases: ["MUSD", "MetaMask USD", "mUSD"]
entity_type: protocol
headquarters: "Decentralized (Consensys / MetaMask)"
website: "https://metamask.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[linea]]", "[[metamask]]", "[[pyusd]]", "[[stablecoin]]", "[[tether]]", "[[usdc]]"]
---

# MetaMask USD

**MetaMask USD** (ticker **MUSD / mUSD**) is a **fiat-reserve [[stablecoin]]** designed to hold a 1:1 peg to the U.S. dollar, built as the wallet-native dollar for the [[metamask|MetaMask]] ecosystem on [[ethereum|Ethereum]] and **Linea**. MetaMask itself does not custody reserves; issuance runs through specialist stablecoin infrastructure — **Bridge** (the stablecoin-issuance platform acquired by Stripe) and the **M0** shared-issuance framework — while MetaMask supplies distribution, in-wallet swaps, fiat on/off-ramps, and real-world spend via the MetaMask Card. In substance MUSD is a distribution play: a recognized consumer wallet brand wrapped around a regulated issuer's reserves, competing with [[usdc]], [[tether]], and [[pyusd|PayPal USD]] for the default in-app dollar balance.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, MUSD trades at **$0.999677**, holds market-cap rank **#564**, and carries a market capitalization of **$36,174,154**. It was essentially perfectly anchored over the window (**24h +0.01%**, **7d 0.00%**) — a tighter print to $1 than several legacy peers, consistent with active issuance and reasonable redemption confidence. The broader tape was risk-off (Fear & Greed 21, Extreme Fear; [[bitcoin|BTC]] ~$64,568), conditions under which small stablecoins often see minor discounts; MUSD did not.

> *Informational only, not investment advice. Stablecoins can and do break their peg.*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MUSD (mUSD) |
| **Price (2026-06-21)** | $0.999677 |
| **Market Cap Rank** | #564 |
| **Market Cap** | $36,174,154 |
| **24h Change** | +0.01% |
| **7d Change** | 0.00% |
| **Peg target** | 1 MUSD = 1 USD |
| **Backing model** | Fiat reserves (via Bridge / M0 issuance framework) |
| **Distributor** | [[metamask\|MetaMask]] (Consensys) |
| **Native chains** | [[ethereum\|Ethereum]] and Linea |
| **Website** | [https://metamask.io/](https://metamask.io/) |

---

## Architecture — How It Works

MUSD splits the stablecoin stack into a **reserve/issuance layer** (operated by partners) and a **distribution/utility layer** (operated by MetaMask). This is the defining design choice: MetaMask is a wallet, not a bank, so it outsources the regulated, reserve-holding parts.

### Reserve and issuance layer

- **Bridge** — a stablecoin-issuance-as-a-service platform (acquired by Stripe) that handles minting, redemption, KYC/AML on authorized parties, and reserve management for partner-branded dollars. Bridge is the operational backbone that turns deposited fiat into on-chain MUSD and back.
- **M0** — an open, shared stablecoin framework that lets compliant issuers mint against a common, fiat-backed dollar standard. M0's model separates the "minter" (who posts eligible collateral such as short-dated U.S. Treasuries) from the branded token surface, so multiple front-ends can share a common reserve discipline.

Because the backing dollars and short-dated cash-equivalents sit with the regulated issuance partner, MUSD is a **fiat-reserve stablecoin in substance** even though its branding is a wallet's. This is the same architectural family as [[usdc]] (reserves at a regulated issuer) rather than the crypto-collateralized [[dai|DAI]] / CDP family.

### Distribution and utility layer

MetaMask (developed by Consensys) supplies everything the end user touches: in-wallet token swaps, fiat on/off-ramps, and the **MetaMask Card** for spending MUSD at real-world merchants. The strategic logic is that the wallet that already holds a user's keys can make its own dollar the path-of-least-resistance balance — earning issuance economics on float that would otherwise accrue to [[usdc]] or [[tether]].

### Peg-maintenance mechanism

As a fiat-backed stablecoin, MUSD holds its peg through **mint/redeem at par** by the issuance partner: authorized parties create MUSD against deposited dollars and redeem it 1:1, so any secondary-market gap is arbitraged shut. There is no over-collateralization buffer and no algorithmic component — peg confidence rests entirely on the partner holding full reserves and honoring redemptions. The 2026-06-21 print of $0.999677 is consistent with that mechanism working smoothly. MUSD's all-time low (~$0.98 in the historical record) was a brief low-liquidity print shortly after launch, not a reserve-driven [[depeg]].

---

## Tokenomics & Supply

MUSD has **no fixed supply** — like other fiat-backed stables, supply expands and contracts with net mint/redeem demand, and circulating supply equals reserves backing it 1:1. At a ~$36M market cap it is a small-cap stablecoin; its supply trajectory is a direct read on MetaMask's success in steering in-app balances into MUSD. There is no separate governance or fee token: economics flow to the issuance partners (reserve yield) and to MetaMask/Consensys (distribution).

---

## Comparison vs Peer Dollars

| Stablecoin | Backing model | Distribution edge | Peg mechanism | Notes |
|---|---|---|---|---|
| **MUSD** (this page) | Fiat reserves via Bridge / M0 | MetaMask wallet + MetaMask Card | Mint/redeem at par | Wallet-native dollar; small cap (~$36M) |
| **[[usdc]]** | Cash + short-dated Treasuries (Circle) | Broad CEX/DeFi + Coinbase | Mint/redeem at par | Largest regulated fiat stable; deep liquidity |
| **[[tether]] (USDT)** | Mixed reserves (Tether) | Largest CEX footprint | Mint/redeem at par | Largest stablecoin by cap; less reserve transparency |
| **[[pyusd]] (PayPal USD)** | Fiat reserves (Paxos) | PayPal/Venmo consumer rails | Mint/redeem at par | Closest analog — a consumer-brand wallet dollar |

MUSD's nearest strategic comparable is **[[pyusd|PayPal USD]]**: both are consumer-brand dollars riding an existing user base and a regulated issuer (Paxos for PYUSD; Bridge/M0 for MUSD), rather than competing primarily on liquidity depth. Against [[usdc]] / [[tether]] it is a tiny entrant whose only durable advantage is wallet integration.

---

## How & Where It Trades / Is Used

MUSD's primary venue is the **MetaMask wallet itself** — in-app swaps, ramps, and Card spending — plus on-chain liquidity on [[ethereum|Ethereum]] and **Linea** (Consensys's L2, where MetaMask can route cheaper transfers). Centralized-exchange listings are limited; on-chain DEX pools are the main secondary market. DeFi composability is nascent: as an ERC-20 it can in principle be paired in AMM pools and lending markets, but with a ~$36M cap its on-chain depth is thin relative to [[usdc]]. In practice MUSD is held and spent inside the wallet rather than actively traded.

---

## Narrative, Category & Catalysts

- **Category:** wallet-distributed / consumer-brand fiat stablecoin — alongside [[pyusd|PayPal USD]] — competing for default in-app dollar balances.
- **Bull catalysts:** MetaMask Card adoption and merchant spend; making MUSD the default swap-settlement and ramp currency in-wallet; Linea growth lowering transfer costs; the broader trend of consumer brands launching own-stablecoins to capture reserve float.
- **Bear catalysts:** users defaulting to deeper, more liquid [[usdc]]/[[tether]] balances; stablecoin regulation tightening issuance for branded/wallet dollars; reliance on third-party issuers (Bridge/M0) whose terms MetaMask does not fully control.

---

## History / Timeline

| Date | Event |
|---|---|
| ~late 2025 | Earliest MUSD price history in the wiki record; relatively new entrant. |
| (early) | All-time low ~$0.98 — a brief low-liquidity print shortly after launch, not a reserve-driven depeg. |
| 2026-06-21 | Trades $0.999677, rank #564, ~$36.2M cap; flat 7d, essentially on-peg. |

*Only events with on-page provenance are listed. The MUSD launch is described qualitatively as the wiki record lacks a precise listing date.*

---

## Risks

- **Issuer / counterparty risk** — Peg depends on the Bridge/M0 issuance partner holding full reserves and honoring redemptions. MetaMask is the distributor, not the reserve custodian, so holders take credit risk on parties they do not directly control.
- **Newness risk** — Short track record; reserve-attestation and redemption practices are less battle-tested than [[usdc]]/[[usdt]].
- **Redemption-gating risk** — Direct par redemption is available only to authorized parties; retail holders exit via secondary DEX liquidity, which can gap in stress.
- **Liquidity risk** — Limited CEX listings and modest on-chain depth can widen spreads outside the wallet.
- **Smart-contract / framework risk** — Exposure to the M0 framework and the deployed ERC-20 contracts on Ethereum and Linea.
- **Regulatory risk** — Stablecoin regulation could constrain branded/wallet-distributed dollars and their issuance partners.

See [[stablecoin]] and [[depeg]] for the general framework.

---

## Trading / Usage Playbook

- **Use case:** MUSD is best understood as a *utility balance*, not a trade — a dollar to hold, swap, and spend inside MetaMask, with the MetaMask Card as the real-world off-ramp.
- **What to watch:** any deviation of the secondary price from $1 (a depeg signal given thin liquidity); reserve-attestation cadence from the Bridge/M0 partners; MUSD circulating supply as a proxy for wallet adoption.
- **Risk-off framing:** in the current Extreme-Fear tape, MUSD's value is precisely that it is *not* a directional bet — but its thin liquidity means it is a worse risk-off parking spot than [[usdc]]/[[usdt]] if you need to exit size on-chain quickly.

---

## Related

- [[stablecoin]]
- [[metamask]]
- [[usdc]]
- [[tether]]
- [[pyusd]]
- [[depeg]]
- [[collateralization]]
- [[ethereum]]
- [[linea]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge (MetaMask/Bridge/M0 issuance model); no specific wiki source ingested yet.

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

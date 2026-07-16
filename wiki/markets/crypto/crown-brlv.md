---
title: "Crown BRLV"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, forex, stablecoins]
aliases: ["BRLV"]
entity_type: protocol
headquarters: "São Paulo, Brazil (Crown)"
website: "https://crown-brlv.com"
related: ["[[base]]", "[[brazilian-real]]", "[[brla-digital-brla]]", "[[brz]]", "[[crypto-markets]]", "[[depeg]]", "[[forex]]", "[[stablecoins]]"]
---

# Crown BRLV

**Crown BRLV (BRLV)** is a non-rebasing **[[brazilian-real|Brazilian Real (BRL)]] [[stablecoins|stablecoin]]** issued by **Crown** (a São Paulo–based fintech), deployed on [[base|Base]] (with an Ethereum deployment as well). It targets a 1:1 peg to the Brazilian Real and is **backed 1:1 by Brazilian government bonds held in a bankruptcy-remote structure**. Positioned as the "institutional-grade" BRL coin — sometimes described as aiming to be "the Circle of Brazil" — it is designed for payments, DeFi integration, and institutional treasury management, and competes with [[brz|BRZ]] and [[brla-digital-brla|BRLA]]. As of the latest snapshot it ranks **#347** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). Note: BRLV pegs to the Brazilian Real, not the US Dollar — its USD price reflects the BRL/USD FX rate (1 BRL ≈ $0.19), so a quote near $0.19 is the token holding its peg, not a de-peg.*

| Field | Detail |
|---|---|
| **Ticker** | BRLV |
| **Peg target** | Brazilian Real (1 BRLV ≈ R$1.00) |
| **Issuer / chain** | Crown — Base (also Ethereum) |
| **Current price** | $0.193964 (= ~R$1.00 at prevailing BRL/USD FX) |
| **Market cap** | $71.67M |
| **Market cap rank** | #347 |
| **24h volume** | $501 |
| **Circulating supply** | 369.51M BRLV |
| **Total supply** | 369.51M BRLV |
| **24h change** | -0.00% |
| **7d change** | -1.68% |
| **All-time high** | $0.204849 (2026-05-09) |
| **All-time low** | $0.186777 (2026-03-16) |

The USD quote of ~$0.194 is **the BRL exchange rate, not a broken peg** — one BRLV is worth roughly one Brazilian Real, which currently converts to about 19 US cents. The small 7d move (-1.7%) and the ATH/ATL band ($0.187–$0.205) reflect ordinary BRL/USD currency fluctuation rather than peg instability.

---

## Issuer & backers

Crown is a **São Paulo–based fintech** that raised **$8.1M** in seed funding to launch BRLV. The round was led by **Framework Ventures**, with participation from **Valor Capital Group, Coinbase Ventures, Norte Ventures, and Paxos**, plus **Ed Wible (co-founder of Nubank)**, who joined Crown's board. This investor base signals an institutional, compliance-first positioning relative to the retail-distributed [[brz|BRZ]] and the B2B-focused [[brla-digital-brla|BRLA]].

---

## Architecture — peg & backing mechanism

BRLV is a fiat-referenced, **asset-backed** stablecoin built on a sovereign-bond reserve model:

- **Backing**: reserves are held 1:1 in **Brazilian government bonds** (the collateral layer is tracked separately as **BRLY**). Reserves sit in a **bankruptcy-remote structure under Brazilian fiduciary assignment law**, and holders are represented by a **collateral agent** who can enforce the collateral if the issuer becomes insolvent — an enforceable legal claim over reserves intended to eliminate counterparty risk. This is materially different from a plain cash-reserve coin: it carries Brazilian **sovereign credit and interest-rate** exposure but offers stronger legal segregation.
- **Non-rebasing**: unlike rebasing yield stablecoins, BRLV keeps a fixed token supply relative to deposits, making it natively compatible with AMMs, lending protocols, and standard ERC-20 integrations.
- **Yield**: the yield earned on the bond reserves accrues at the **collateral (BRLY) layer**; surplus is redeemable in BRLV via a "Rewards Claiming" mechanic. Rewards are computed off-chain and, for now, **only primary holders may claim them** — a key nuance for secondary buyers, who get the peg but not the yield.
- **Redemption**: primary issuance/redemption is intermediated by the issuer against the bond reserves; secondary holders rely on market liquidity.
- **Mint/redeem & KYC gating**: primary mint/redeem runs through Crown's permissioned, KYC-gated institutional channel against the bond reserve; secondary holders acquire/exit on-chain.

---

## Tokenomics & supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 369.51M BRLV |
| **Total Supply** | 369.51M BRLV |
| **Max Supply** | Unlimited |
| **Market Cap / FDV Ratio** | 1.00 |

Circulating equals total supply (FDV ratio 1.00) — there is no locked/unvested overhang, consistent with a deposit-backed stablecoin where every token in existence is collateralised. Supply is elastic to mint/redeem demand. Note the **yield-accrual split**: economic yield concentrates at the BRLY collateral layer and is claimable by primary holders, so BRLV itself behaves as a pure peg token for most secondary users.

---

## Comparison vs Other BRL Stablecoins

| | **Crown BRLV** | **[[brz\|BRZ]]** | **[[brla-digital-brla\|BRLA]]** |
|---|---|---|---|
| **Peg** | Brazilian real (BRL) | Brazilian real (BRL) | Brazilian real (BRL) |
| **Issuer** | Crown (São Paulo; Framework/Coinbase/Paxos-backed) | Transfero Group (Brazil/Switzerland) | BRLA Digital (Brazil) |
| **Reserve model** | **Brazilian gov't bonds**, bankruptcy-remote (BRLY layer) | BRL cash reserves | BRL reserves (managed by Avenia) |
| **Legal protection** | Enforceable claim via collateral agent | Standard issuer redemption | Standard issuer redemption |
| **Yield** | Accrues at BRLY layer; primary holders claim | None to holders | None to holders |
| **Primary chain(s)** | Base (+ Ethereum) | Multi-chain | Polygon (+ several EVM) |
| **Positioning** | Institutional / "Circle of Brazil" | Retail distribution, longevity | Audited B2B, Pix-native |
| **Mkt cap (snapshot)** | ~$71.7M | ~$51.6M | ~$40.8M |

BRLV is the **largest of the three by market cap at snapshot** and the only one with sovereign-bond backing and an explicit bankruptcy-remote legal wrapper.

---

## How & where it trades / is used

BRLV is a niche, region-specific stablecoin. Liquidity is concentrated on-chain on [[base|Base]] (and Ethereum), and **external trading volume is extremely thin (~$500/24h)** — effectively no meaningful secondary order book at snapshot time. Practical acquisition and exit run through the issuer's primary channel rather than open exchanges.

- **Treat as highly illiquid** for any size; exits depend on issuer redemption or shallow DEX pools.
- Primary use case is **BRL-denominated payments, institutional treasury, and DeFi** inside the Brazilian web3 ecosystem.
- DeFi composability is a deliberate design goal (non-rebasing ERC-20), but realised on-chain depth at this snapshot is minimal.

---

## Narrative, category & catalysts

BRLV is a **regional / FX-denominated stablecoin** aimed squarely at the **institutional** tier of Brazil's BRL market. Catalysts: institutional and treasury adoption (its differentiator vs retail BRZ); Brazil's **Pix** rails and large crypto user base; the central bank's **Drex** (digital real) programme and evolving stablecoin/Brazilian-central-bank rules, where a bond-backed, legally segregated coin is comparatively well-positioned; and yield demand drawing capital to the BRLY collateral layer. The marquee backer set (Framework, Coinbase Ventures, Paxos, Nubank's Ed Wible) is itself a credibility catalyst. The 2026 macro backdrop (Extreme Fear, bottoming/accumulation) compresses liquidity for small regional stablecoins.

---

## History / timeline

- **Crown raised $8.1M seed** funding (led by Framework Ventures; Valor Capital, Coinbase Ventures, Norte Ventures, Paxos, and Nubank co-founder Ed Wible participating) to launch BRLV.
- **2026-03-16** — recorded all-time low of **$0.186777** (BRL/USD-driven).
- **2026-05-09** — recorded all-time high of **$0.204849** (BRL/USD-driven).

*(Exact public-launch date is not verified in available wiki sources and is deliberately not stated. ATH/ATL dates are from the CoinGecko snapshot.)*

---

## Risks

- **FX risk (not a stablecoin flaw, but a holder risk)**: a US-dollar-based holder is exposed to BRL depreciation; the token holds its BRL peg but its USD value moves with BRL/USD.
- **De-peg risk**: failure of the bond-redemption process, reserve shortfalls, or loss of confidence could push BRLV away from R$1.00 ([[depeg]]).
- **Collateral / sovereign risk**: backing is Brazilian government bonds, so the peg carries **Brazilian sovereign credit and rate risk** — a bond-price or sovereign shock is a reserve-value shock.
- **Issuer / custodial risk**: reserves and the rewards calculation are issuer-controlled and partly off-chain; holders depend on the bankruptcy-remote structure being honored in practice.
- **Yield-asymmetry risk**: secondary holders carry the token but cannot claim the BRLY yield, which accrues to primary holders.
- **Liquidity risk**: near-zero secondary volume means large exits are difficult without slippage or reliance on the issuer.
- **Regulatory risk**: subject to Brazilian regulation (including evolving central-bank stablecoin/Drex rules) and broader global stablecoin regulation.
- **Macro backdrop**: as of the 2026-06-22 snapshot the broader crypto market is in **Extreme Fear (Fear & Greed 21)** and a bearish, bottoming/accumulation regime, which can compress liquidity for small regional stablecoins.

---

## Trading / usage playbook

- **As FX exposure:** BRLV is a **long-BRL** instrument with sovereign-bond backing; USD P&L is dominated by BRL/USD.
- **Yield seekers:** to capture the bond yield, hold at the **primary (BRLY) layer**; buying BRLV on the secondary market gives the peg but not the rewards.
- **On/off-ramp use:** primary mint/redeem (KYC-gated) is the realistic entry/exit given near-zero secondary depth — do not assume open-market liquidity.
- **Peg monitoring:** "on-peg" = ~R$1.00, not $1.00; watch for a gap vs the live BRL/USD rate as the real depeg signal.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 369.51M BRLV |
| **Total Supply** | 369.51M BRLV |
| **Max Supply** | Unlimited |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Platform & Chain Information

**Native Chain:** Base

### Contract Addresses

| Chain | Address |
|---|---|
| Base | `0xd2047ebdb205ee6862b69ae9fb3501652cc97d36` |
| Ethereum | `0xd7ca0e2c36d647446b782d1b72308e598373e2f5` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://crown-brlv.com](https://crown-brlv.com) |
| **GitHub** | [https://github.com/crown-xyz](https://github.com/crown-xyz) |

---

## Related

- [[stablecoins]]
- [[base]]
- [[brazilian-real]]
- [[brz]]
- [[brla-digital-brla]]
- [[forex]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## See Also

- [[crypto-markets]]
- [[base]]

---

---
title: "Collateral"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [risk-management, leverage, margin, derivatives, defi]
aliases: ["Collateral", "Collateralization", "Posting Collateral"]
related: ["[[margin]]", "[[margin-trading]]", "[[leverage]]", "[[liquidation]]", "[[counterparty-risk]]", "[[perpetual-futures]]", "[[defi]]", "[[stablecoins]]", "[[liquidity-risk]]", "[[haircut]]", "[[rehypothecation]]", "[[treasuries]]"]
domain: [risk-management, market-microstructure]
prerequisites: ["[[margin]]", "[[leverage]]"]
difficulty: beginner
---

**Collateral** is an asset pledged by a borrower or trader to secure an obligation, which the lender or counterparty can seize if the obligation is not met. In trading it is the capital backing a leveraged position: it absorbs losses before the lender is exposed, and its sufficiency is continuously tested against the position's mark-to-market value. Collateral is the mechanism that lets [[leverage]] exist while bounding the lender's [[counterparty-risk|counterparty risk]].

## How It Works

When a trader opens a leveraged position — a [[margin-trading|margin]] stock purchase, a futures contract, or a crypto [[perpetual-futures|perpetual]] — the broker or exchange requires collateral (the [[margin]]) to be posted. As the position moves, the collateral balance is marked to market:

- **Initial margin** — the collateral required to open the position.
- **Maintenance margin** — the minimum collateral that must be retained; falling below it triggers a margin call or, on most crypto venues, automatic [[liquidation]].
- **[[haircut|Haircut]]** — the discount applied to an asset's value when used as collateral. A volatile asset accepted at a 50% haircut means $100 of it backs only $50 of exposure, reflecting the risk that its value falls before it can be sold.
- **Variation margin** — daily (or, in crypto, continuous) transfers that settle gains and losses, topping the collateral back up.

Collateral types are ranked by quality. Cash and short-dated government bonds (e.g., [[treasuries]]) carry the smallest haircuts; equities, corporate bonds, and crypto assets carry larger ones because they are more volatile and less liquid. **[[rehypothecation|Rehypothecation]]** — a counterparty reusing posted collateral to back its own borrowing — increases system leverage and was a key amplifier of the 2008 crisis.

### Collateral quality ladder

Lenders and clearinghouses tier eligible collateral by liquidity and volatility, applying a [[haircut]] that widens as quality falls. Representative (illustrative) haircuts:

| Collateral type | Typical haircut | Why |
|-----------------|-----------------|-----|
| Cash (same currency) | ~0% | No price or liquidity risk |
| Short-dated [[treasuries|government bonds]] | ~0.5–2% | Deep, liquid, low duration risk |
| Long-dated government bonds | ~3–8% | Interest-rate / duration risk |
| Investment-grade corporate bonds | ~5–15% | Credit + liquidity risk |
| Blue-chip equities | ~15–30% | Daily volatility, gap risk |
| Crypto majors (BTC, ETH) | ~20–50%+ | High volatility, 24/7 gap risk |
| Volatile altcoins | 50%+ or ineligible | Thin liquidity, extreme volatility |

The same asset can attract very different haircuts across venues, and haircuts are *raised in stress* — exactly when traders can least afford it.

### Worked example: haircut and borrowing power

A trader pledges **$100,000 of a blue-chip equity** as collateral against a margin loan. The broker applies a **25% haircut**, so the *collateral value* recognized is $100,000 × (1 − 0.25) = **$75,000**. If the maintenance requirement is that the loan cannot exceed the collateral value, the trader can borrow up to **$75,000**.

Now the equity falls 20% to **$80,000** market value. Recognized collateral value = $80,000 × 0.75 = **$60,000**. If the outstanding loan was $75,000, the account is now **$15,000 under-collateralized** — triggering a margin call to post more collateral or a forced [[liquidation]] of part of the position. Notice how the haircut *and* the price drop compound: the buffer erodes faster than the headline price move suggests.

## Cross vs Isolated Collateral

A practical distinction, especially in crypto derivatives:

- **Cross-margin / cross-collateral** — the entire account balance backs all open positions. More capital-efficient, but one losing position can drain collateral shared with others, risking liquidation of the whole account.
- **Isolated margin** — collateral is ring-fenced per position; a liquidation is contained to that position's allocated margin. Less efficient, but limits contagion.

## Trading Relevance

Collateral management is a core [[risk-management|risk-management]] discipline, not an afterthought:

- **Liquidation risk** — under-collateralized leveraged positions are force-closed at the worst possible moment, often into thin [[liquidity-risk|liquidity]], crystallizing losses. Cascading liquidations can drive sharp, self-reinforcing moves (common in crypto sell-offs).
- **Collateral quality matters in stress** — accepting volatile assets at thin haircuts looks efficient until correlations spike and the collateral and the position fall together (wrong-way risk).
- **DeFi over-collateralization** — decentralized lending ([[defi]]) protocols like Aave and Maker cannot pursue defaulters, so they require *over*-collateralization (e.g., $150 of ETH to borrow $100 of a [[stablecoins|stablecoin]]) and liquidate automatically via smart contract when the collateral ratio breaches a threshold. This makes collateral the entire trust model.
- **Capital efficiency** — sophisticated traders optimize which assets to post (lowest-haircut, lowest-opportunity-cost) and use portfolio/cross margin to free capital, accepting higher contagion risk in exchange.

The prudent rule mirrors all leverage discipline: keep a collateral buffer well above maintenance so normal volatility does not trigger liquidation, and assume haircuts and margins can be raised by the venue precisely when markets are most stressed.

## Rehypothecation and System Leverage

[[rehypothecation|Rehypothecation]] is when the entity holding your posted collateral re-pledges (reuses) it to back *its own* borrowing. A single underlying asset can then support multiple layers of credit through a chain of counterparties. This is capital-efficient in calm markets but builds hidden, system-wide [[leverage]]: in a panic, every link in the chain demands its collateral back at once, and the same asset cannot satisfy all claims simultaneously. This dynamic amplified the 2008 crisis (the collapse of the repo and prime-brokerage chains) and the 2011 failure of MF Global, whose customers found their supposedly segregated collateral entangled in the firm's own borrowing. The practical lesson for a trader: understand whether your broker can rehypothecate your assets, and prefer segregated/custodied arrangements for capital you cannot afford to have frozen.

## Collateral in Derivatives vs DeFi

| Dimension | Traditional / derivatives | [[defi|DeFi]] lending |
|-----------|---------------------------|-----------|
| Trust model | Legal recourse, [[counterparty-risk|counterparty]] credit, clearinghouses | Code-enforced; no legal recourse |
| Collateralization | Can be *under*-collateralized for trusted counterparties (netting, credit lines) | Always *over*-collateralized (e.g. 150%) |
| Margin call / cure | Hours to days; human intervention possible | Instant, automatic [[liquidation]] by smart contract |
| Eligible collateral | Cash, bonds, equities — tiered by [[haircut]] | Whitelisted crypto assets with on-chain price feeds |
| Reuse | [[rehypothecation|Rehypothecation]] common | Generally not reused (locked in contract) |

DeFi protocols like Aave and Maker cannot pursue a defaulter, so they replace legal recourse with *over*-collateralization and ruthless automatic liquidation. That makes the collateral ratio and the reliability of the price [[oracle]] the entire trust model — an oracle failure or a sharp gap can liquidate healthy positions or, conversely, leave the protocol holding bad debt.

## Common Pitfalls

- **Wrong-way risk.** Posting collateral correlated with the position you are backing (e.g. crypto collateral against a crypto perp): in a selloff the collateral and the position fall *together*, so the buffer evaporates exactly when needed. Prefer uncorrelated, low-haircut collateral.
- **Thin buffers.** Running collateral just above maintenance leaves no room for normal volatility; one routine wick can trigger [[liquidation]]. Keep a wide buffer.
- **Procyclical haircuts and margins.** Venues raise haircuts and [[margin]] requirements in stress, forcing deleveraging into falling markets — a self-reinforcing liquidation cascade ([[liquidity-risk|liquidity]] dries up precisely when you must sell).
- **Cross-margin contagion.** Under [[#Cross vs Isolated Collateral|cross-margin]], a single bad position can drain shared collateral and liquidate the whole account. Isolate risk you want ring-fenced.
- **Assuming segregation.** Believing your collateral is safely set aside when terms permit [[rehypothecation|rehypothecation]] — read the agreement before pledging assets you cannot afford to lose access to.

## Sources

- Hull, John C. *Options, Futures, and Other Derivatives.* Pearson — chapters on margin, collateralization, and central clearing.
- BIS / IOSCO, *Margin requirements for non-centrally cleared derivatives* — standards on initial and variation margin.
- Aave and MakerDAO protocol documentation — over-collateralization and liquidation mechanics in DeFi lending.

## Related

- [[margin]] — collateral posted to support a leveraged position
- [[margin-trading]] — borrowing against collateral to trade
- [[leverage]] — what collateral enables and bounds
- [[haircut]] — the discount applied to collateral value
- [[rehypothecation]] — reuse of posted collateral and the system leverage it creates
- [[liquidation]] — what happens when collateral falls below maintenance
- [[counterparty-risk]] — the risk collateral is designed to mitigate
- [[perpetual-futures]] — crypto derivatives with continuous collateral marking
- [[defi]] — over-collateralized decentralized lending
- [[treasuries]] — the highest-quality, lowest-haircut collateral

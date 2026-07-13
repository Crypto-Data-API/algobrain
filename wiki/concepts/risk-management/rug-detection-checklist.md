---
title: "Rug Detection Checklist"
type: concept
created: 2026-05-04
updated: 2026-06-11
status: good
tags: [crypto, risk-management, defi, security, memecoin, scams]
aliases: ["rug check", "pre-trade rug check", "rug filter", "scam check"]
domain: [risk-management]
difficulty: beginner
prerequisites: ["[[rug-pulls]]"]
related: ["[[rug-pulls]]", "[[holder-concentration-analysis]]", "[[pump-fun]]", "[[memecoin-sniping]]", "[[birdeye]]", "[[gmgn]]", "[[axiom-pro]]", "[[trojan-bot]]"]
---

A rug detection checklist is the short, mechanical list of contract and wallet checks a trader runs in the seconds before clicking buy on a low-cap or freshly launched memecoin. Where [[rug-pulls]] is the conceptual / historical reference page, this page is the **operational checklist** — the items a sniper, copy-trader, or low-cap discretionary trader actually ticks off (or has a bot tick off automatically) before every trade. On launchpads like [[pump-fun|Pump.fun]], where the base rate of profitable tokens is on the order of 1%, running this checklist is what separates a process from a slot machine.

## When to run it

- **Always**, on any token under ~$10M FDV on Solana, BSC, Base, or any EVM L2 launchpad.
- **Before every entry**, not just the first — token state changes (LP unlocks, dev sells, mint events) over the life of a position.
- **Even on copy-trades** — the wallet you copy may itself be a bundler, or the trade you're following may already be a coordinated dump.

## The checklist

### Liquidity

1. **Liquidity pool exists and is non-trivial.** $10k+ for very early plays, $50k+ before sizing up.
2. **LP tokens are locked or burned.** Use the LP page on Dexscreener / Birdeye / GMGN. Acceptable: burn address, or a time-lock contract (Team Finance, Unicrypt, PinkSale) with a future unlock date.
3. **Lock duration covers your hold horizon** — a 24-hour lock is meaningless for a multi-day swing.
4. **Migration status (Pump.fun-specific):** if the token has bonded to [[raydium|Raydium]] or [[pumpswap|PumpSwap]], confirm LP was actually seeded and locked at migration; the bonding curve no longer protects you.

### Contract authorities

5. **Mint authority renounced / revoked.** On Solana, check `mintAuthority: null` in the SPL token account. On EVM, no `mint()` function or owner is `0x0`.
6. **Freeze authority revoked** (Solana). A live freeze authority means the issuer can blacklist your wallet and prevent you from selling.
7. **Update authority renounced** if applicable (Solana metadata).
8. **Contract source verified** on the block explorer (EVM). Unverified bytecode is an automatic skip outside of the very-earliest sniping window.
9. **No proxy / upgradeable pattern** without a credible governance / time-lock — proxies are how the AnubisDAO-class drains happen.
10. **No hidden mints, blacklists, max-tx caps, or transfer taxes >5%.** Token Sniffer, GoPlus, De.Fi Scanner, and the Honeypot.is family of tools test these automatically.

### Holder distribution

11. **Bundle % low** (ideally < ~10-20%). See [[holder-concentration-analysis]] for the full method.
12. **Dev wallet % low** (ideally < ~5%, with the dev-funded cluster summed).
13. **Top 10 holders excluding LP / burn < ~25-30%** on a fresh launch.
14. **Holder count consistent with age and MC** — too few holders for the volume is a bundling fingerprint.
15. **No single wallet > ~5-10%** of circulating supply other than the LP itself.

### Dev wallet behavior

16. **Deployer history clean** — no rugs in the prior 24-72 hours. GMGN and Cielo show this directly.
17. **Deployer has not sold its own bag.** A dev market-sell into the curve is the textbook soft-rug signal.
18. **Deployer funding source is not a freshly funded mixer / bridge wallet** (FixedFloat, ChangeNOW, Tornado Cash). Dirty funding is a strong rug prior.
19. **Deployer is not the same entity as the top sniper** — same-funder relationships between deployer and "first buyer" are bundling.

### Social / off-chain

20. **Real, organic socials (or, for a pure memecoin, a credible meta).** Bot-farm Twitter accounts and locked Telegrams are red flags.
21. **No paid-callout pump pattern** — check if the token appears on known shill lists, paid Telegram groups, or KOL "alpha" channels right before launch. These are exit liquidity signals.
22. **Reasonable narrative** — the token is *something*, not just a 5-minute Lambo emoji ticker with no anchor.

### Market microstructure

23. **Volume is organic** — buys and sells from many wallets, not ping-pong between 3 addresses (wash trading).
24. **Buy / sell ratio not pathologically skewed** — 100% buys with no sells often means selling is disabled (honeypot).
25. **Slippage to round-trip your intended size is bearable** — simulate a buy *and* a sell of your size before entering.
26. **No abnormal sell-tax behavior** — try a tiny test sell before sizing up if anything feels off.

A practical ruleset: **any single hard fail (items 5, 6, 8, 9, 10, 24) is an automatic skip.** Soft fails (high but not extreme top-holder %, short LP lock, thin socials) compound — two or more soft fails and you skip.

## Tools that automate the checklist

| Tool | Coverage |
|------|----------|
| [[gmgn|GMGN]] (`gmgn.ai`) | One-page rug-check for Solana memecoins: bundle %, dev %, top 10, mint/freeze authority, dev history |
| [[birdeye|Birdeye]] | Holder distribution, security tab, whale tracking |
| Dexscreener "Audit" panel | LP lock, mint, freeze, top 10, links out to GMGN |
| [[axiom-pro|Axiom Pro]] | Inline rug-check inside the order ticket — checklist items show as red/green pills before submit |
| [[trojan-bot|Trojan Bot]], BonkBot, Photon, Bullx | Pre-trade safety panel in Telegram / web before each buy |
| Token Sniffer, GoPlus, De.Fi Scanner, Honeypot.is | EVM-side automated contract auditing |
| RugCheck.xyz | Solana-specific automated risk score |

The point of automation is not to skip the checklist — it is to make running it cost less than a second per trade so you actually run it on every trade.

## Examples

- **Honeypot skip (EVM):** a Base token has $80k LP locked for a year, mint renounced, but Honeypot.is reports a 99% sell tax. Hard fail item 10. Skip.
- **Bundle skip (Pump.fun):** GMGN shows 32% bundle and a deployer with three rugs in the last 24 hours. Hard fail items 11, 16. Skip.
- **Soft-fail compound:** clean contract, clean deployer, but top 10 = 38%, LP locked only 7 days, and Twitter is 6 hours old with 12 followers. Three soft fails. Skip.
- **Pass:** post-bond Pump.fun token, mint and freeze revoked, LP burned at migration, top 10 = 18% (mostly known smart-money wallets), deployer has shipped two prior survivors, organic holder growth. Proceed to [[market-cap-level-trading|MC-level]] analysis for entry.

## Limitations

- **Soft rugs evade the checklist.** Slow-bleed dev sells, abandonment, and stealth allocation increases over weeks pass every pre-trade check. Position sizing and exits matter more than any pre-trade filter for this failure mode.
- **Sophisticated bundlers spoof every metric.** Aged wallets, multi-hop funding, and CEX-routed cost basis can produce a checklist-clean launch that is still one entity.
- **Tools lag the chain.** A "clean" scan can be seconds out of date during a busy launch; the dev may already be selling.
- **The checklist filters scams, not edge.** Passing every item only means the token is *not provably a rug right now*. It says nothing about whether the trade will be profitable.
- **Network coverage gaps.** Tools are strongest on Solana, Ethereum, Base, BSC. Newer chains and cross-chain memes often have no automated scanners — you must do the checks manually or pass.

## Related

- [[rug-pulls]] — historical and conceptual reference for the failure mode this checklist defends against
- [[holder-concentration-analysis]] — the deep-dive on items 11-15
- [[pump-fun]] — the launchpad where this checklist runs hundreds of times a day
- [[memecoin-sniping]] — the strategy class that requires this checklist as table stakes
- [[birdeye]], [[gmgn]], [[axiom-pro]], [[trojan-bot]] — tools that automate it
- [[market-cap-level-trading]] — what comes after the checklist passes

## Sources

- [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]] — Pump.fun tooling and rug-detection workflow
- Public documentation of GMGN, Birdeye, RugCheck, Honeypot.is, GoPlus

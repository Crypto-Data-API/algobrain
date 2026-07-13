---
title: "Insider Trading"
type: concept
created: 2026-04-13
updated: 2026-06-11
status: good
tags: [market-microstructure, regulation]
aliases: ["MNPI Trading", "Material Non-Public Information", "Insider Dealing"]
domain: [market-microstructure]
prerequisites: ["[[regulation]]", "[[market-efficiency]]"]
difficulty: intermediate
related: ["[[market-manipulation]]", "[[regulation]]", "[[asx]]", "[[insider-trading-australia]]", "[[spoofing]]", "[[sec]]", "[[information-arbitrage]]", "[[market-efficiency]]"]
---

Insider trading is the buying or selling of securities based on material non-public information (MNPI). It is illegal in most jurisdictions, including Australia under the Corporations Act 2001. Fred McNaught references insider trading in his Poseidon-era stories from the 1960s-70s, when enforcement was far weaker and information asymmetry between insiders and retail investors was extreme. The practice undermines [[market-efficiency|market efficiency]] and erodes investor confidence. For details on the Australian regulatory framework, see [[insider-trading-australia]].

## What Makes Trading Illegal: The Three-Element Test

US insider-trading law (Securities Exchange Act of 1934 §10(b) and SEC Rule 10b-5) prohibits trading on information that is simultaneously:

1. **Material** — a reasonable investor would consider it important to a buy/sell decision (e.g., upcoming earnings, M&A, FDA decisions, drilling results).
2. **Non-public** — not yet disseminated broadly to the market.
3. **Acquired in breach of a duty** — the trader, or the person who tipped them, owed a fiduciary or confidentiality duty that was violated. Under the misappropriation theory, even outsiders who steal confidential information from a source owed a duty can be liable.

If any element is missing the trade is generally legal. This is exactly the boundary that separates illegal insider trading from legitimate [[information-arbitrage]]: info-arb uses information that is *or will be* public (SEC filings, exchange feeds, satellite imagery, on-chain data), failing the "non-public" element. The 2014 *US v. Newman* and 2016 *Salman v. United States* decisions refined the tipper-tippee "personal benefit" requirement that governs when passing a tip is itself a violation.

## Why It Matters to Traders

Insider trading sits at the centre of [[market-microstructure]] because it is the limiting case of [[information-arbitrage|information asymmetry]]. Two practical angles for a legitimate trader:

- **As a risk to price into thin/illiquid names.** A wide bid-ask [[spread]] and a sudden one-sided run before a corporate announcement often reflect informed flow. [[market-maker|Market makers]] widen quotes to protect against [[adverse-selection|adverse selection]] from informed (sometimes illegally informed) counterparties; this is a tax all uninformed participants pay.
- **As a legal, public signal.** Insider *transactions* that are properly disclosed (Form 4 in the US, Appendix 3Y in Australia) are a legitimate dataset. Systematic insider-buying clusters — especially open-market purchases by multiple officers — have historically carried modest predictive alpha, the basis of a long-standing market anomaly (see Lakonishok & Lee, 2001). The edge has compressed as the data became free and widely scraped.

## Enforcement and Penalties

In the United States, the [[sec|SEC]] enforces insider trading laws under the Securities Exchange Act of 1934 (primarily Rule 10b-5). Penalties can include civil disgorgement of profits, fines up to three times the profit gained or loss avoided, and criminal prosecution carrying up to 20 years imprisonment. The SEC uses sophisticated surveillance tools including pattern analysis, communications monitoring, and tips from whistleblowers (who can receive 10-30% of sanctions exceeding $1 million). In Australia, ASIC enforces insider trading provisions under Part 7.10 of the Corporations Act, with criminal penalties of up to 15 years imprisonment and civil penalties of up to $1.05 million for individuals.

## Famous Cases

Several high-profile cases have shaped insider trading law and enforcement. **Martha Stewart** (2001) was convicted of obstruction of justice related to the sale of ImClone stock ahead of an FDA drug rejection, serving five months in prison. **Raj Rajaratnam** (2011), founder of the Galleon Group hedge fund, received 11 years imprisonment -- one of the longest sentences in insider trading history -- after an investigation that pioneered the use of wiretaps in securities fraud cases. **SAC Capital** (Steven A. Cohen's fund) paid $1.8 billion in penalties in 2013 and pled guilty to securities fraud, though Cohen himself was not criminally charged. These cases illustrate that enforcement has intensified significantly compared to the lax regulatory environment of earlier decades.

## Legal Insider Transactions

Not all insider trading is illegal. Corporate officers, directors, and significant shareholders (insiders) are permitted to buy and sell their company's stock provided they are not acting on MNPI and they report their transactions. In the US, these transactions must be disclosed via **SEC Form 4** filings within two business days. Investors often track legal insider buying as a bullish signal -- the logic being that insiders have deep knowledge of their company's prospects and are more likely to buy when they believe the stock is undervalued. Systematic insider-buying signals have been shown to generate modest alpha in academic studies, though the edge has diminished as the data has become more widely accessible. In Australia, directors must disclose changes in their interests via Appendix 3Y filings with the [[asx|ASX]].

## Related

- [[regulation]] -- the broader framework governing market conduct
- [[sec]] -- the primary US enforcement agency for securities fraud
- [[market-manipulation]] -- related category of illegal market conduct
- [[insider-trading-australia]] -- Australian-specific regulatory framework
- [[spoofing]] -- another form of illegal market activity
- [[information-arbitrage]] -- the legal counterpart: profiting from public information acquired faster
- [[market-efficiency]] -- the theoretical frame insider trading violates

## Sources

- Securities Exchange Act of 1934, §10(b); SEC Rule 10b-5. https://www.sec.gov/
- *Dirks v. SEC*, 463 U.S. 646 (1983) — tipper-tippee liability and the personal-benefit test.
- *United States v. Newman*, 773 F.3d 438 (2d Cir. 2014); *Salman v. United States*, 580 U.S. 39 (2016) — refinements of the personal-benefit standard.
- STOCK Act of 2012 — application of insider-trading prohibitions to members of Congress.
- Australian Corporations Act 2001 (Cth), Part 7.10 — Australian insider-trading provisions enforced by ASIC.
- Lakonishok, J. & Lee, I. (2001), "Are Insider Trades Informative?" *Review of Financial Studies* 14(1) — academic evidence on the signal value of legal insider transactions.
- *US v. Wahi* (2022) — SEC/DOJ action establishing crypto-listing-decision insider trading liability.

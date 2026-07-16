#!/usr/bin/env python3
"""
Compute the *tradable* crypto subset for Phase-2 enrichment:
  Binance-listed (CoinGecko tickers)  UNION  Hyperliquid perps (HL public info API).

Writes raw/data/crypto-coins/_tradable.json and prints a summary.
No API key needed (Hyperliquid /info is public; Binance flags come from cached CoinGecko JSON).
"""
import json
import re
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "raw" / "data" / "crypto-coins"
CRYPTO = ROOT / "wiki" / "markets" / "crypto"
OUT = DATA / "_tradable.json"

BINANCE_MARKETS = {"binance", "binance_futures", "binance_us"}


def hyperliquid_perps():
    """Return a set of uppercase HL perp symbols (with de-k'd variants)."""
    r = requests.post("https://api.hyperliquid.xyz/info", json={"type": "meta"}, timeout=30)
    r.raise_for_status()
    names = [a["name"].upper() for a in r.json().get("universe", [])]
    syms = set(names)
    for n in names:
        if n.startswith("K") and len(n) > 1:   # kPEPE -> PEPE (1000x markets)
            syms.add(n[1:])
    return syms, len(names)


def index_pages():
    """Map stem->path and ALIAS(upper)->stem for existing crypto pages."""
    by_stem, by_alias = {}, {}
    for f in CRYPTO.glob("*.md"):
        by_stem[f.stem] = f.name
        head = f.read_text(encoding="utf-8", errors="ignore")[:600]
        m = re.search(r'aliases:\s*\[([^\]]*)\]', head)
        if m:
            for a in re.findall(r'"([^"]+)"', m.group(1)):
                by_alias.setdefault(a.upper(), f.stem)
    return by_stem, by_alias


def resolve_page(cg_id, symbol, by_stem, by_alias):
    if cg_id in by_stem:
        return by_stem[cg_id]
    if symbol.upper() in by_alias:
        return by_stem[by_alias[symbol.upper()]]
    if symbol.lower() in by_stem:
        return by_stem[symbol.lower()]
    return None


def main():
    coin_list = json.loads((DATA / "_coin_list.json").read_text(encoding="utf-8"))
    hl_syms, hl_count = hyperliquid_perps()
    by_stem, by_alias = index_pages()
    print(f"Hyperliquid perp universe: {hl_count} markets")

    tradable = []
    for c in coin_list:
        cid = c["id"]
        symbol = (c.get("symbol") or "").upper()
        detail = DATA / f"{cid}.json"
        binance = False
        if detail.exists():
            try:
                d = json.loads(detail.read_text(encoding="utf-8"))
                for t in (d.get("tickers") or []):
                    if (t.get("market") or {}).get("identifier") in BINANCE_MARKETS:
                        binance = True
                        break
            except Exception:
                pass
        hl = symbol in hl_syms
        if binance or hl:
            tradable.append({
                "cg_id": cid,
                "symbol": symbol,
                "name": c.get("name"),
                "rank": c.get("market_cap_rank"),
                "binance": binance,
                "hyperliquid": hl,
                "page": resolve_page(cid, symbol, by_stem, by_alias),
            })

    tradable.sort(key=lambda x: (x["rank"] is None, x["rank"] or 1e9))
    OUT.write_text(json.dumps(tradable, indent=2), encoding="utf-8")

    both = [t for t in tradable if t["binance"] and t["hyperliquid"]]
    bonly = [t for t in tradable if t["binance"] and not t["hyperliquid"]]
    honly = [t for t in tradable if t["hyperliquid"] and not t["binance"]]
    no_page = [t for t in tradable if not t["page"]]
    print(f"\nTRADABLE SUBSET: {len(tradable)}")
    print(f"  Binance + Hyperliquid: {len(both)}")
    print(f"  Binance only:          {len(bonly)}")
    print(f"  Hyperliquid only:      {len(honly)}")
    print(f"  (no wiki page resolved: {len(no_page)})")
    print(f"\nWrote {OUT}")
    print("\nTop 20 tradable:")
    for t in tradable[:20]:
        v = ("B" if t["binance"] else "-") + ("H" if t["hyperliquid"] else "-")
        print(f"  #{t['rank']:<5} [{v}] {t['symbol']:<8} {t['page']}")


if __name__ == "__main__":
    main()

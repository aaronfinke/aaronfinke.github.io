#!/usr/bin/env python3
"""Convert finke_publications.bib into _data/publications.yml.

Usage: python3 scripts/bib_to_yaml.py path/to/finke_publications.bib
Re-run whenever the .bib changes, then commit _data/publications.yml.
"""
import re, sys, yaml

ACCENTS = {
    "'": {"c":"ć","C":"Ć","e":"é","E":"É","a":"á","o":"ó","i":"í","u":"ú","y":"ý","n":"ń","s":"ś","z":"ź"},
    '"': {"o":"ö","O":"Ö","a":"ä","A":"Ä","u":"ü","U":"Ü","e":"ë","i":"ï"},
    "v": {"c":"č","C":"Č","s":"š","S":"Š","z":"ž","Z":"Ž","r":"ř","e":"ě"},
    "`": {"e":"è","a":"à","o":"ò","u":"ù"},
    "^": {"o":"ô","e":"ê","a":"â","i":"î"},
    "~": {"n":"ñ","a":"ã","o":"õ"},
    "c": {"c":"ç","C":"Ç"},
}
GREEK = {r"\gamma": "γ", r"\alpha": "α", r"\beta": "β"}

def accents(s):
    def rep(m):
        kind, ch = m.group(1), m.group(2)
        return ACCENTS.get(kind, {}).get(ch, ch)
    s = re.sub(r"\{?\\([\'\"v`^~c])\s*\{?([A-Za-z])\}?\}?", rep, s)
    return s.replace(r"{\o}", "ø").replace(r"{\O}", "Ø").replace(r"\aa", "å")

def clean(s, html=True):
    s = accents(s)
    for k, v in GREEK.items():
        s = s.replace(k, v)
    s = re.sub(r"\\(?:textit|emph)\{((?:[^{}]|\{[^{}]*\})*)\}", r"<em>\1</em>" if html else r"\1", s)
    s = re.sub(r"\{\\(?:textit|emph)\s+([^{}]*)\}", r"<em>\1</em>" if html else r"\1", s)
    s = re.sub(r"\$_(\w)\$", r"<sub>\1</sub>" if html else r"\1", s)
    s = re.sub(r"_\{([^{}]*)\}", r"<sub>\1</sub>" if html else r"\1", s)
    s = re.sub(r"\^\{([^{}]*)\}", r"<sup>\1</sup>" if html else r"\1", s)
    s = s.replace("$", "").replace(r"\_", "_").replace("--", "–").replace("``", "“").replace("''", "”")
    s = s.replace(r"\&", "&")
    prev = None
    while prev != s:          # strip protective braces, keep tags
        prev = s
        s = re.sub(r"\{([^{}]*)\}", r"\1", s)
    s = s.replace("\\", "")
    return re.sub(r"\s+", " ", s).strip()

def parse(text):
    text = re.sub(r"^%.*$", "", text, flags=re.M)
    out = []
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,]+),", text):
        typ, key, i = m.group(1), m.group(2), m.end()
        depth, j = 1, m.end()
        while depth:
            c = text[j]; depth += (c == "{") - (c == "}"); j += 1
        body = text[i:j-1]
        fields = {}
        for fm in re.finditer(r"(\w+)\s*=\s*\{", body):
            d, k = 1, fm.end()
            while d:
                c = body[k]; d += (c == "{") - (c == "}"); k += 1
            fields[fm.group(1).lower()] = body[fm.end():k-1]
        if "month" not in fields:
            mm = re.search(r"month\s*=\s*(\w+)", body)
            if mm: fields["month"] = mm.group(1)
        out.append((typ, key.strip(), fields))
    return out

def public_note(raw):
    """Drop bookkeeping notes (Crossref lookups, CV corrections); keep reader-facing ones."""
    n = clean(raw)
    if not n or "Crossref" in n or n.startswith("CV "):
        return None
    return n

def fmt_author(a):
    a = clean(a, html=False)
    if "," in a:
        last, first = [x.strip() for x in a.split(",", 1)]
        return f"{first} {last}".strip()
    return a

def main(path):
    entries = []
    for typ, key, f in parse(open(path, encoding="utf-8").read()):
        authors = [fmt_author(a) for a in re.split(r"\s+and\s+", f.get("author", f.get("editor", ""))) if a.strip()]
        year = int(f["year"])
        venue = clean(f.get("journal") or f.get("howpublished") or f.get("booktitle") or "")
        e = {
            "key": key, "type": typ, "year": year,
            "title": clean(f.get("title", "")),
            "authors": authors,
            "venue": venue,
            "volume": clean(f.get("volume", "")) or None,
            "pages": clean(f.get("pages", "")) or None,
            "doi": f.get("doi") or None,
            "url": f.get("url") or None,
            "note": public_note(f.get("note", "")),
            "preprint": typ == "misc" or "preprint" in f.get("howpublished", "").lower(),
        }
        if typ == "incollection":
            e["venue"] = clean(f.get("booktitle", "")) ; e["publisher"] = clean(f.get("publisher", "")) or None
        entries.append({k: v for k, v in e.items() if v not in (None, "")})
    # keep bib order (CV order) but make sure it is newest-first by year
    entries.sort(key=lambda e: -e["year"])
    with open("_data/publications.yml", "w", encoding="utf-8") as fh:
        yaml.safe_dump(entries, fh, allow_unicode=True, sort_keys=False, width=1000)
    print(f"wrote {len(entries)} entries")

if __name__ == "__main__":
    main(sys.argv[1])

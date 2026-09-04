# -*- coding: utf-8 -*-
"""
IndexNow: gewijzigde pagina's aanmelden bij Bing en Yandex.

    python _bron/indexnow.py              proefdraaien, dient niets in
    python _bron/indexnow.py --indienen   werkelijk indienen

Waarom dit nuttig is: Bing voedt Copilot. Sneller geïndexeerd worden bij Bing
werkt dus direct door in de AI-zichtbaarheid waar deze site op mikt. Google
doet niet mee aan IndexNow; daar blijft de sitemap plus Search Console de weg.

Hoe het werkt: er wordt bijgehouden welke HTML er bij de vorige indiening
stond. Alleen pagina's waarvan de inhoud werkelijk is veranderd worden
aangemeld. Niet-indexeerbare pagina's (noindex) en alles buiten de sitemap
blijven eruit; anders meldt u zichzelf aan voor pagina's die u niet wilt laten
indexeren.

VEILIGHEID
  - Zonder sleutel gebeurt er niets, ook niet met --indienen.
  - Proefdraaien is de standaard. Indienen vraagt een expliciete vlag.
  - De IndexNow-sleutel is per ontwerp openbaar: hij moet als bestand op het
    domein staan, anders kan de zoekmachine niet controleren of u de eigenaar
    bent. Dat is geen wachtwoord. Gebruik hem nergens anders voor.

SLEUTEL AANMAKEN
  1. Verzin een reeks van 8 tot 128 tekens (letters en cijfers), of genereer
     er een op https://www.bing.com/indexnow
  2. Zet hem in _bron/inhoud.py bij INDEXNOW["sleutel"]
  3. python _bron/bouw.py  -- die schrijft <sleutel>.txt in de site
  4. Publiceer, controleer dat https://capitalbb.nl/<sleutel>.txt de sleutel
     toont, en dien daarna pas in
"""

import hashlib
import io
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inhoud import CONTACT, INDEXNOW

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMEIN = "https://" + CONTACT["domein"]
MANIFEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "indexnow-staat.json")
EINDPUNT = "https://api.indexnow.org/IndexNow"


def sitemap_urls():
    """Alleen wat in de sitemap staat: canoniek, indexeerbaar, 200."""
    pad = os.path.join(WORTEL, "sitemap.xml")
    if not os.path.exists(pad):
        return []
    import re
    return re.findall(r"<loc>([^<]+)</loc>", io.open(pad, encoding="utf-8").read())


def bestand_voor(url):
    rest = url.replace(DOMEIN, "").strip("/")
    return os.path.join(WORTEL, rest, "index.html") if rest else os.path.join(WORTEL, "index.html")


def vingerafdruk(pad):
    """Hash van de pagina zonder de versiestempels op css en js: die
    veranderen bij elke stijlwijziging en zeggen niets over de inhoud."""
    import re
    h = io.open(pad, encoding="utf-8").read()
    h = re.sub(r"\?v=[0-9a-f]{8}", "", h)
    return hashlib.sha256(h.encode("utf-8")).hexdigest()[:16]


def laad_staat():
    if os.path.exists(MANIFEST):
        try:
            return json.load(io.open(MANIFEST, encoding="utf-8"))
        except Exception:
            return {}
    return {}


def bewaar_staat(staat):
    io.open(MANIFEST, "w", encoding="utf-8", newline="\n").write(
        json.dumps(staat, ensure_ascii=False, indent=1, sort_keys=True))


def main():
    indienen = "--indienen" in sys.argv
    sleutel = (INDEXNOW.get("sleutel") or "").strip()

    print("IndexNow" + ("" if indienen else "  (proefdraaien, er wordt niets ingediend)"))
    print("=" * 64)

    urls = sitemap_urls()
    if not urls:
        print("Geen sitemap gevonden. Draai eerst python _bron/bouw.py")
        return 1

    staat = laad_staat()
    nieuw, gewijzigd, ongewijzigd = [], [], []
    verse_staat = {}

    for u in urls:
        pad = bestand_voor(u)
        if not os.path.exists(pad):
            print(f"  overgeslagen, bestaat niet: {u}")
            continue
        vf = vingerafdruk(pad)
        verse_staat[u] = vf
        if u not in staat:
            nieuw.append(u)
        elif staat[u] != vf:
            gewijzigd.append(u)
        else:
            ongewijzigd.append(u)

    testuren = nieuw + gewijzigd
    print(f"  {len(nieuw)} nieuw, {len(gewijzigd)} gewijzigd, {len(ongewijzigd)} ongewijzigd\n")
    for u in nieuw:
        print("  nieuw      ", u)
    for u in gewijzigd:
        print("  gewijzigd  ", u)

    if not testuren:
        print("\nNiets te melden. Alle pagina's zijn ongewijzigd sinds de vorige keer.")
        return 0

    if not sleutel:
        print("\nGeen IndexNow-sleutel ingesteld in _bron/inhoud.py bij INDEXNOW.")
        print("Zie de uitleg bovenin dit bestand. Er is niets ingediend.")
        return 0

    if not indienen:
        print(f"\n{len(testuren)} URL's zouden worden ingediend.")
        print("Werkelijk indienen: python _bron/indexnow.py --indienen")
        return 0

    lading = {
        "host": CONTACT["domein"],
        "key": sleutel,
        "keyLocation": f"{DOMEIN}/{sleutel}.txt",
        "urlList": testuren,
    }
    verzoek = urllib.request.Request(
        EINDPUNT, data=json.dumps(lading).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(verzoek, timeout=30) as r:
            code = r.status
    except urllib.error.HTTPError as e:
        code = e.code
    except Exception as e:
        print(f"\nIndienen mislukt: {e}")
        print("De staat is niet bijgewerkt, dus een volgende poging probeert het opnieuw.")
        return 1

    if code in (200, 202):
        print(f"\nIngediend: {len(testuren)} URL's. Antwoord {code}.")
        bewaar_staat(verse_staat)
        print("Staat bijgewerkt; deze pagina's worden pas opnieuw gemeld als ze wijzigen.")
        return 0

    uitleg = {
        400: "ongeldig verzoek",
        403: "sleutel niet geldig; staat het sleutelbestand wel online?",
        422: "URL's horen niet bij dit domein, of de sleutel klopt niet",
        429: "te vaak ingediend; probeer het later",
    }.get(code, "onverwacht antwoord")
    print(f"\nNiet ingediend. Antwoord {code}: {uitleg}")
    print("De staat is niet bijgewerkt.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

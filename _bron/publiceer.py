# -*- coding: utf-8 -*-
"""
Zet de publicatiemap `_site/` klaar: uitsluitend de bestanden die een bezoeker
mag zien, en niets uit de bouwbron.

    python _bron/bouw.py
    python _bron/controle.py
    python _bron/publiceer.py

Waarom dit bestaat: GitHub Pages publiceerde de hele repository vanaf de root
van main. Daardoor was https://capitalbb.nl/_bron/inhoud.py gewoon op te
vragen, met de complete prijsopbouw en bouwlogica erin. robots.txt houdt
crawlers weg maar blokkeert geen bezoekers.

De oplossing is niet "verstoppen" maar "niet publiceren": dit script kopieert
alleen wat op de lijst staat naar `_site/`, en de GitHub Action zet uitsluitend
die map online. Wat hier niet expliciet is toegelaten, komt er dus nooit op,
ook niet als er later een bestand bij komt.

Het script weigert dienst als er iets verdachts in de output zit. Liever een
mislukte deployment dan opnieuw broncode online.
"""

import io
import os
import shutil
import sys

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOEL = os.path.join(WORTEL, "_site")

# Losse bestanden die mee mogen. Alles wat hier niet staat, gaat niet mee.
BESTANDEN = [
    "index.html",
    "404.html",
    "robots.txt",
    "sitemap.xml",
    "llms.txt",
    "CNAME",
    ".nojekyll",
]

# Mappen met statische assets die integraal mee mogen.
MAPPEN = ["css", "js", "img"]

# Nooit publiceren, ongeacht waar het staat.
VERBODEN_EXT = {".py", ".pyc", ".md", ".yml", ".yaml", ".toml", ".ini", ".log",
                ".bak", ".env", ".sh", ".ps1", ".json"}
VERBODEN_NAAM = {"_bron", "__pycache__", ".github", ".git", ".remember",
                 "node_modules", "_site", "scripts"}


def paginamappen():
    """Alle gebouwde paginamappen: mappen met een index.html erin, zonder
    punt of underscore aan het begin."""
    uit = []
    for naam in sorted(os.listdir(WORTEL)):
        pad = os.path.join(WORTEL, naam)
        if not os.path.isdir(pad):
            continue
        if naam.startswith((".", "_")) or naam in VERBODEN_NAAM or naam in MAPPEN:
            continue
        if os.path.exists(os.path.join(pad, "index.html")):
            uit.append(naam)
    return uit


def kopieer():
    if os.path.exists(DOEL):
        shutil.rmtree(DOEL)
    os.makedirs(DOEL)

    meegenomen = []

    # IndexNow-sleutelbestand meenemen als het er is.
    import re as _re
    for naam in os.listdir(WORTEL):
        if _re.fullmatch(r"[A-Za-z0-9]{8,128}\.txt", naam):
            shutil.copy2(os.path.join(WORTEL, naam), os.path.join(DOEL, naam))
            meegenomen.append(naam)

    for naam in BESTANDEN:
        bron = os.path.join(WORTEL, naam)
        if os.path.exists(bron):
            shutil.copy2(bron, os.path.join(DOEL, naam))
            meegenomen.append(naam)
        elif naam not in (".nojekyll",):
            print(f"  let op: {naam} bestaat niet, overgeslagen")

    # .nojekyll moet er hoe dan ook zijn: zonder dat bestand gooit Jekyll op
    # GitHub Pages mappen met een underscore weg en kan het HTML verbouwen.
    nj = os.path.join(DOEL, ".nojekyll")
    if not os.path.exists(nj):
        io.open(nj, "w", encoding="utf-8").write("")
        meegenomen.append(".nojekyll")

    for naam in MAPPEN:
        bron = os.path.join(WORTEL, naam)
        if os.path.isdir(bron):
            shutil.copytree(bron, os.path.join(DOEL, naam))
            meegenomen.append(naam + "/")

    for naam in paginamappen():
        os.makedirs(os.path.join(DOEL, naam), exist_ok=True)
        shutil.copy2(os.path.join(WORTEL, naam, "index.html"),
                     os.path.join(DOEL, naam, "index.html"))
        meegenomen.append(naam + "/index.html")

    return meegenomen


def controleer():
    """Laatste zeef. Vindt hij hier nog iets interns, dan faalt de publicatie."""
    fouten = []
    for map_, mappen, bestanden in os.walk(DOEL):
        mappen[:] = [m for m in mappen if m not in VERBODEN_NAAM]
        for m in list(os.listdir(map_)):
            if m in VERBODEN_NAAM and os.path.isdir(os.path.join(map_, m)):
                fouten.append(f"interne map in de publicatie: {os.path.relpath(os.path.join(map_, m), DOEL)}")
        for b in bestanden:
            rel = os.path.relpath(os.path.join(map_, b), DOEL)
            ext = os.path.splitext(b)[1].lower()
            if ext in VERBODEN_EXT:
                fouten.append(f"intern bestandstype in de publicatie: {rel}")
            if b.startswith("."):
                if b != ".nojekyll":
                    fouten.append(f"verborgen bestand in de publicatie: {rel}")
    # De site moet wel compleet zijn.
    for nodig in ("index.html", "404.html", "robots.txt", "sitemap.xml",
                  "llms.txt", "CNAME", ".nojekyll"):
        if not os.path.exists(os.path.join(DOEL, nodig)):
            fouten.append(f"ontbreekt in de publicatie: {nodig}")
    return fouten


if __name__ == "__main__":
    print("Publicatiemap klaarzetten in _site/")
    print("=" * 62)
    meegenomen = kopieer()
    fouten = controleer()

    paginas = [m for m in meegenomen if m.endswith("index.html")]
    print(f"  {len(paginas)} pagina's, {len(MAPPEN)} assetmappen, "
          f"{len([m for m in meegenomen if not m.endswith('/') and '/' not in m])} losse bestanden")

    if fouten:
        print("\nPUBLICATIE GEWEIGERD:\n")
        for f in fouten:
            print("  -", f)
        sys.exit(1)

    print("\n_site/ bevat uitsluitend de gepubliceerde website. Geen bronbestanden.")

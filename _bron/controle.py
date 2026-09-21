# -*- coding: utf-8 -*-
"""
Controleert de gebouwde site. Draaien na elke bouw:

    python _bron/bouw.py && python _bron/controle.py

Geen afhankelijkheden, alleen de standaardbibliotheek. Elke controle print
OK of een lijst met fouten; de exitcode is 1 zodra er iets mis is, zodat dit
in een pipeline gebruikt kan worden.

Wat er gecontroleerd wordt:
  1  elke JSON-LD-block is geldige JSON
  2  geen dubbele @id binnen een pagina
  3  elke @id-verwijzing wijst naar een bestaande entiteit (site-breed)
  4  zichtbaar kruimelpad en BreadcrumbList zijn gelijk
  5  zichtbare FAQ en FAQPage-schema zijn letterlijk gelijk
  6  canonical staat er en klopt met het pad
  7  titles en descriptions zijn uniek en aanwezig
  8  precies één H1 per pagina, en geen gaten in de koppenhierarchie
  9  interne links wijzen naar bestaande pagina's, met slash, zonder index.html
 10  geen weespagina's: elke pagina is intern gelinkt
 11  sitemap bevat precies de indexeerbare pagina's, en geen noindex
 12  robots.txt is intern consistent en heeft één user-agentgroep
 13  llms.txt verwijst alleen naar bestaande pagina's
 14  prijzen zijn overal gelijk aan de bron in inhoud.py
 15  privacyverklaring klopt met de werkelijke verzendroute
 16  beide formulieren hebben een honeypot tegen spambots
 17  elke img heeft alt, width en height
 18  lang, viewport, charset en og-velden staan er
"""

import io
import json
import os
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inhoud import (CONTACT, FORMULIER, METEN, PRIJS_WEB, PRIJS_CRM, PRIJS_SYS,
                    PRIJS_OS, PRIJS_ZICHT, PRIJS_ONDERHOUD)
from zoekintentie import ZOEKINTENTIE
from cases import CASES, STATUS_LABEL

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMEIN = "https://" + CONTACT["domein"]

fouten = []


def fout(pagina, regel):
    fouten.append(f"{pagina}: {regel}")


def paginas():
    """Alle gebouwde pagina's: pad (zonder slashes) -> bestandsnaam."""
    uit = {"": os.path.join(WORTEL, "index.html")}
    for naam in sorted(os.listdir(WORTEL)):
        map_ = os.path.join(WORTEL, naam)
        if naam.startswith((".", "_")) or not os.path.isdir(map_):
            continue
        bestand = os.path.join(map_, "index.html")
        if os.path.exists(bestand):
            uit[naam] = bestand
    return uit


def lees(pad):
    return io.open(pad, encoding="utf-8").read()


def tekst(h):
    """HTML-tags eruit, entiteiten terug, witruimte normaliseren. Zo is
    zichtbare tekst vergelijkbaar met wat er in de structured data staat."""
    h = re.sub(r"<br\s*/?>", " ", h)
    h = re.sub(r"<[^>]+>", "", h)
    for a, b in [("&euro;", "€"), ("&eacute;", "é"), ("&Eacute;", "É"),
                 ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'),
                 ("&middot;", "·"), ("&hellip;", "…"), ("&apos;", "'"),
                 ("&nbsp;", " ")]:
        h = h.replace(a, b)
    return re.sub(r"\s+", " ", h).strip()


# ---------------------------------------------------------------------------
PAGINAS = paginas()
HTML = {p: lees(b) for p, b in PAGINAS.items()}
HTML["404"] = lees(os.path.join(WORTEL, "404.html"))

ALLE_IDS = set()
GRAPHS = {}

print("Capital BB, controle van de gebouwde site")
print("=" * 62)
print(f"{len(PAGINAS)} pagina's plus 404.html\n")


# --- 1, 2: JSON-LD geldig, geen dubbele @id ---------------------------------
for p, h in HTML.items():
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    ids = []
    graph = []
    for b in blocks:
        try:
            data = json.loads(b)
        except Exception as e:
            fout(p, f"ongeldige JSON-LD: {e}")
            continue
        graph.extend(data.get("@graph", [data]))
    for node in graph:
        if isinstance(node, dict) and "@id" in node and len(node) > 1:
            ids.append(node["@id"])
            ALLE_IDS.add(node["@id"])
    for i in set(ids):
        if ids.count(i) > 1:
            fout(p, f"dubbele @id in de graph: {i}")
    GRAPHS[p] = graph

# --- 3: elke verwijzing wijst naar een bestaande entiteit -------------------
def verwijzingen(node, uit):
    if isinstance(node, dict):
        if set(node.keys()) == {"@id"}:
            uit.add(node["@id"])
        for v in node.values():
            verwijzingen(v, uit)
    elif isinstance(node, list):
        for v in node:
            verwijzingen(v, uit)

for p, graph in GRAPHS.items():
    verw = set()
    verwijzingen(graph, verw)
    for v in verw - ALLE_IDS:
        fout(p, f"@id-verwijzing zonder entiteit: {v}")

# --- 4: kruimelpad zichtbaar == BreadcrumbList ------------------------------
for p, h in HTML.items():
    nav = re.search(r'<nav class="kruimels".*?</nav>', h, re.S)
    bc = [n for n in GRAPHS[p] if n.get("@type") == "BreadcrumbList"]
    if not nav and not bc:
        continue
    if bool(nav) != bool(bc):
        fout(p, "kruimelpad en BreadcrumbList komen niet allebei voor")
        continue
    zicht = [tekst(m) for m in re.findall(r'<(?:a|span)[^>]*>(.*?)</(?:a|span)>', nav.group(0), re.S)]
    zicht = [z for z in zicht if z and z != "/"]
    schema = [i["name"] for i in bc[0]["itemListElement"]]
    if zicht != schema:
        fout(p, f"kruimelpad wijkt af van schema: zichtbaar {zicht} vs schema {schema}")
    posities = [i["position"] for i in bc[0]["itemListElement"]]
    if posities != list(range(1, len(posities) + 1)):
        fout(p, f"BreadcrumbList-posities niet oplopend vanaf 1: {posities}")
    urls = [i["item"] for i in bc[0]["itemListElement"]]
    if len(set(urls)) != len(urls):
        fout(p, f"BreadcrumbList bevat dezelfde URL twee keer: {urls}")

# --- 5: zichtbare FAQ == FAQPage-schema -------------------------------------
for p, h in HTML.items():
    zicht = [(tekst(v), tekst(a)) for v, a in
             re.findall(r'<details class="faq-item"><summary>(.*?)</summary><p>(.*?)</p></details>', h, re.S)]
    schema = []
    for n in GRAPHS[p]:
        t = n.get("@type")
        if t == "FAQPage" or (isinstance(t, list) and "FAQPage" in t):
            schema = [(q["name"], q["acceptedAnswer"]["text"]) for q in n.get("mainEntity", [])]
    if schema and not zicht:
        fout(p, "FAQPage-schema zonder zichtbare FAQ")
    if zicht and not schema:
        fout(p, "zichtbare FAQ zonder FAQPage-schema")
    if zicht and schema:
        if len(zicht) != len(schema):
            fout(p, f"aantal FAQ-vragen wijkt af: {len(zicht)} zichtbaar, {len(schema)} in schema")
        for (zv, za), (sv, sa) in zip(zicht, schema):
            if zv != tekst(sv):
                fout(p, f"FAQ-vraag wijkt af van schema: {zv!r} vs {sv!r}")
            if za != tekst(sa):
                fout(p, f"FAQ-antwoord wijkt af van schema bij {zv!r}")

# --- 6: canonical -----------------------------------------------------------
for p, b in PAGINAS.items():
    h = HTML[p]
    m = re.search(r'<link rel="canonical" href="([^"]+)"', h)
    verwacht = DOMEIN + "/" + ((p + "/") if p else "")
    if not m:
        fout(p, "geen canonical")
    elif m.group(1) != verwacht:
        fout(p, f"canonical klopt niet: {m.group(1)} in plaats van {verwacht}")
    og = re.search(r'<meta property="og:url" content="([^"]+)"', h)
    if og and og.group(1) != verwacht:
        fout(p, f"og:url wijkt af van canonical: {og.group(1)}")
if re.search(r'<link rel="canonical"', HTML["404"]):
    fout("404", "404.html hoort geen canonical te hebben")

# --- 7: unieke titles en descriptions ---------------------------------------
titels, descs = defaultdict(list), defaultdict(list)
for p, h in HTML.items():
    t = re.search(r"<title>(.*?)</title>", h, re.S)
    d = re.search(r'<meta name="description" content="([^"]*)"', h)
    if not t or not t.group(1).strip():
        fout(p, "geen title")
    else:
        titels[t.group(1)].append(p)
        if len(t.group(1)) > 70:
            fout(p, f"title is {len(t.group(1))} tekens (>70): {t.group(1)}")
    if not d or not d.group(1).strip():
        fout(p, "geen description")
    else:
        descs[d.group(1)].append(p)
        n = len(d.group(1))
        if n > 175:
            fout(p, f"description is {n} tekens (>175)")
for t, ps in titels.items():
    if len(ps) > 1:
        fout(", ".join(ps), f"dezelfde title: {t}")
for d, ps in descs.items():
    if len(ps) > 1:
        fout(", ".join(ps), f"dezelfde description: {d[:60]}...")

# --- 8: één H1, geen gaten in de koppenhierarchie ---------------------------
for p, h in HTML.items():
    koppen = [int(n) for n in re.findall(r"<h([1-6])[ >]", h)]
    aantal_h1 = koppen.count(1)
    if aantal_h1 != 1:
        fout(p, f"{aantal_h1} H1's in plaats van 1")
    vorig = 0
    for k in koppen:
        if vorig and k > vorig + 1:
            fout(p, f"gat in de koppenhierarchie: h{vorig} gevolgd door h{k}")
            break
        vorig = k

# --- 9, 10: interne links ---------------------------------------------------
bestaand = set(PAGINAS)
inkomend = defaultdict(set)
for p, h in HTML.items():
    diep = "../" if p not in ("", "404") else ""
    for href in re.findall(r'href="([^"]+)"', h):
        if href.startswith(("http", "mailto:", "tel:", "#")):
            continue
        if "index.html" in href:
            fout(p, f"link naar index.html: {href}")
        doel = href.split("#")[0].split("?")[0]
        if not doel:
            continue
        if doel.startswith("../"):
            doel = doel[3:]
        elif doel == "/" or doel == "":
            doel = ""
        elif doel.startswith("/"):
            doel = doel[1:]
        doel = doel.rstrip("/")
        if doel.startswith(("css/", "js/", "img/")) or doel in ("robots.txt", "sitemap.xml", "llms.txt"):
            continue
        if doel not in bestaand:
            fout(p, f"interne link naar niet-bestaande pagina: {href}")
            continue
        # Links naar een map moeten op een slash eindigen, anders volgt een
        # redirect en gaat er een hop verloren.
        if doel and not href.split("#")[0].split("?")[0].endswith("/"):
            fout(p, f"interne link zonder afsluitende slash: {href}")
        if doel != p:
            inkomend[doel].add(p)
for p in bestaand:
    if p and not inkomend[p]:
        fout(p, "weespagina: geen enkele interne link wijst hierheen")

# --- 11: sitemap ------------------------------------------------------------
sm = lees(os.path.join(WORTEL, "sitemap.xml"))
in_sitemap = set(re.findall(r"<loc>([^<]+)</loc>", sm))
def is_indexeerbaar(h):
    m = re.search(r'<meta name="robots" content="([^"]*)"', h)
    return "noindex" not in (m.group(1) if m else "")

indexeerbaar = {DOMEIN + "/" + ((p + "/") if p else "")
                for p, h in HTML.items()
                if p != "404" and is_indexeerbaar(h)}
if in_sitemap - indexeerbaar:
    fout("sitemap.xml", f"bevat niet-indexeerbare of onbekende URL's: {sorted(in_sitemap - indexeerbaar)}")
if indexeerbaar - in_sitemap:
    fout("sitemap.xml", f"mist indexeerbare pagina's: {sorted(indexeerbaar - in_sitemap)}")
for loc in in_sitemap:
    if not loc.startswith("https://"):
        fout("sitemap.xml", f"geen absolute https-URL: {loc}")
    if "index.html" in loc:
        fout("sitemap.xml", f"index.html in de sitemap: {loc}")
if not re.match(r'^<\?xml version="1\.0" encoding="UTF-8"\?>', sm):
    fout("sitemap.xml", "geen XML-declaratie")
if sm.count("<url>") != sm.count("</url>") or sm.count("<loc>") != sm.count("<lastmod>"):
    fout("sitemap.xml", "onvolledige of ongebalanceerde XML")

# --- 12: robots.txt ---------------------------------------------------------
rb = lees(os.path.join(WORTEL, "robots.txt"))
groepen = re.findall(r"(?im)^user-agent:\s*(.+)$", rb)
if len(groepen) != len(set(groepen)):
    fout("robots.txt", f"dubbele user-agentgroepen: {groepen}")
if "Disallow: /_bron/" not in rb:
    fout("robots.txt", "/_bron/ is niet geblokkeerd")
if f"Sitemap: {DOMEIN}/sitemap.xml" not in rb:
    fout("robots.txt", "geen of verkeerde sitemapverwijzing")
for g in groepen:
    blok = rb.split("User-agent: " + g, 1)[1].split("User-agent:", 1)[0]
    if re.search(r"(?im)^disallow:\s*/\s*$", blok) and re.search(r"(?im)^allow:\s*/\s*$", blok):
        fout("robots.txt", f"tegenstrijdige regels in de groep {g}")

# --- 13: llms.txt -----------------------------------------------------------
lt = lees(os.path.join(WORTEL, "llms.txt"))
for url in set(re.findall(re.escape(DOMEIN) + r"/([a-z0-9-]*/?)", lt)):
    doel = url.rstrip("/")
    if doel and doel not in bestaand and doel not in ("sitemap.xml", "robots.txt"):
        fout("llms.txt", f"verwijst naar een niet-bestaande pagina: /{url}")
for p in bestaand:
    if p and p not in ("privacy",) and f"{DOMEIN}/{p}/" not in lt:
        fout("llms.txt", f"belangrijke pagina ontbreekt: /{p}/")

# --- 14: prijzen overal gelijk ----------------------------------------------
BRON = {}
for lijst in (PRIJS_WEB, PRIJS_CRM, PRIJS_SYS, PRIJS_OS, PRIJS_ZICHT, PRIJS_ONDERHOUD):
    for it in lijst:
        BRON[it[0]] = it[1]
alle_tekst = "\n".join(tekst(h) for h in HTML.values()) + "\n" + tekst(lt)
# Elk bedrag dat als vanafprijs op de site staat, moet in de bron voorkomen.
GELDIG = set(BRON.values()) | {
    # Eenmalige inrichtingskosten die bij de abonnementen horen.
    "395", "695", "1.250", "1.195", "1.995", "3.495", "2.250",
    # Koppelingen, migratie, dashboards, uurtarief, AI-inrichting, maatwerk.
    "295", "650", "65", "750", "4.945",
    # Bedragen die géén Capital BB-prijs zijn maar de markt beschrijven, in de
    # vergelijkingstabel op /website-laten-maken/. Bewust toegestaan.
    "0", "500", "1.500",
}
# Alleen hele bedragen, met duizendtallen op zijn Nederlands en zonder de punt
# van de zin erachter.
for bedrag in set(re.findall(r"€\s?([0-9]{1,3}(?:\.[0-9]{3})*)(?![0-9])", alle_tekst)):
    if bedrag not in GELDIG:
        fout("prijzen", f"bedrag €{bedrag} staat op de site maar niet in inhoud.py")
# Andersom: elke prijs uit de bron moet ergens zichtbaar zijn.
for naam, bedrag in BRON.items():
    if f"€{bedrag}" not in alle_tekst and f"€ {bedrag}" not in alle_tekst:
        fout("prijzen", f"prijs {bedrag} ({naam}) staat in inhoud.py maar nergens op de site")

# --- 14b: privacyverklaring klopt met de werkelijke verzendroute -------------
# Dit is de controle die er echt toe doet: zodra formulieren naar een externe
# dienst posten, mag /privacy/ niet meer beweren dat de site niets opslaat.
mailt_direct = bool(FORMULIER.get("sleutel"))
pv = tekst(HTML.get("privacy", ""))
scanpagina = tekst(HTML.get("scan", ""))
if mailt_direct:
    if "slaat die gegevens nergens op" in pv:
        fout("privacy", "beweert dat er niets wordt opgeslagen terwijl formulieren "
                        "wél naar een verzenddienst gaan")
    if "Web3Forms" not in pv:
        fout("privacy", "noemt de verzenddienst niet terwijl die wel wordt gebruikt")
    if "verstuurt uw gegevens" not in scanpagina:
        fout("scan", "vermeldt bij het formulier niet dat de gegevens worden verstuurd")
else:
    if "Web3Forms" in pv:
        fout("privacy", "noemt een verzenddienst die niet is ingesteld")
    if "slaat die gegevens nergens op" not in pv:
        fout("privacy", "zegt niet meer dat de site niets opslaat, terwijl dat wel zo is")
for p in ("scan", "contact"):
    if 'name="botcheck"' not in HTML.get(p, ""):
        fout(p, "formulier zonder honeypot tegen spambots")

# --- 14c: zoekintentie: geen twee pagina's op dezelfde vraag -----------------
# Dit is de controle die kannibalisatie tegenhoudt. /websites/ en
# /website-laten-maken/ groeiden eerder naar elkaar toe tot ze dezelfde CTA
# droegen; dat mag niet ongemerkt terugkomen.
def _kop(h, tag):
    m = re.search(r"<" + tag + r"[^>]*>(.*?)</" + tag + r">", h, re.S)
    return tekst(m.group(1)) if m else ""

def _cta_kop(h):
    m = re.search(r'<section class="sectie cta-slot">.*?<h2[^>]*>(.*?)</h2>', h, re.S)
    return tekst(m.group(1)) if m else ""

def _intro(h):
    m = re.search(r'<p class="lede">(.*?)</p>', h, re.S)
    return tekst(m.group(1)) if m else ""

def _lijkt(a, b):
    """Ruwe gelijkenis op woordniveau. Twee pagina's mogen best wat woorden
    delen; boven 0.75 gaat het over dezelfde zin."""
    wa, wb = set(a.lower().split()), set(b.lower().split())
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / len(wa | wb)

for p, gegevens in ZOEKINTENTIE.items():
    if p not in HTML:
        fout("zoekintentie", f"kaart noemt /{p}/ maar die pagina bestaat niet")
        continue
    for ander in gegevens.get("botst_niet_met", []):
        if ander not in HTML:
            continue
        for naam, haal in (("H1", lambda h: _kop(h, "h1")),
                           ("introductie", _intro),
                           ("CTA-kop", _cta_kop)):
            a_, b_ = haal(HTML[p]), haal(HTML[ander])
            if a_ and b_ and (a_ == b_ or _lijkt(a_, b_) > 0.75):
                fout(f"{p} vs {ander}",
                     f"vrijwel dezelfde {naam}, terwijl deze pagina's een eigen "
                     f"zoekintentie horen te hebben: {a_[:60]!r}")

# Elke indexeerbare pagina hoort een plek in de kaart te hebben, anders is er
# een pagina bijgekomen zonder dat iemand de intentie heeft bepaald.
for p, h in HTML.items():
    if p == "404" or not is_indexeerbaar(h):
        continue
    if p not in ZOEKINTENTIE:
        fout(p, "staat niet in de zoekintentiekaart in _bron/zoekintentie.py")

# Twee pagina's mogen niet dezelfde primaire intentie claimen.
_gezien = {}
for p, gegevens in ZOEKINTENTIE.items():
    sleutel = gegevens["intentie"].strip().lower()
    if sleutel in _gezien:
        fout("zoekintentie", f"/{p}/ en /{_gezien[sleutel]}/ claimen dezelfde "
                             f"primaire intentie: {gegevens['intentie']}")
    _gezien[sleutel] = p

# --- 14d: geen trackingcode zonder geldige configuratie ---------------------
for p, h in HTML.items():
    if "googletagmanager" in h or "gtag/js" in h or "connect.facebook.net" in h:
        fout(p, "laadt een trackingscript rechtstreeks in de HTML; dat hoort "
                "pas na toestemming door de JS te gebeuren")
if METEN.get("ga4"):
    if not re.match(r"^G-[A-Z0-9]{6,}$", METEN["ga4"]):
        fout("meten", f"ga4-ID heeft niet de vorm G-XXXXXXXXXX: {METEN['ga4']}")
    if "cookiebalk" not in lees(os.path.join(WORTEL, "js", "site.js")):
        fout("meten", "meet-ID ingesteld maar er is geen cookiebanner in de JS")
    if "Google Analytics" not in tekst(HTML.get("privacy", "")):
        fout("privacy", "meet-ID ingesteld maar de privacyverklaring noemt geen analytics")
else:
    if "Google Analytics" in tekst(HTML.get("privacy", "")):
        fout("privacy", "noemt analytics terwijl er geen meet-ID is ingesteld")

if METEN.get("meta_pixel"):
    if not re.match(r"^\d{15,16}$", str(METEN["meta_pixel"])):
        fout("meten", f"meta_pixel is geen pixel-ID van 15 of 16 cijfers: {METEN['meta_pixel']}")
    if "cookiebalk" not in lees(os.path.join(WORTEL, "js", "site.js")):
        fout("meten", "pixel-ID ingesteld maar er is geen cookiebanner in de JS")
    if "Meta-pixel" not in tekst(HTML.get("privacy", "")):
        fout("privacy", "pixel-ID ingesteld maar de privacyverklaring noemt de pixel niet")
else:
    if "Meta-pixel" in tekst(HTML.get("privacy", "")):
        fout("privacy", "noemt de Meta-pixel terwijl er geen pixel-ID is ingesteld")

# --- 14e: cases, demo's en resultaatclaims ----------------------------------
# De belangrijkste eerlijkheidscontrole op deze site. Een demo die als
# klantopdracht wordt gepresenteerd is geen slordigheid maar een onwaarheid,
# en een resultaatcijfer zonder bron is precies wat de site belooft niet te
# doen.
for c in CASES:
    if c["status"] not in STATUS_LABEL:
        fout("cases", f"{c['sleutel']}: onbekende status {c['status']!r}")
    if c["toestemming"] not in ("naam", "anoniem", "geen"):
        fout("cases", f"{c['sleutel']}: onbekende toestemming {c['toestemming']!r}")
    # Resultaat mag alleen bestaan mét bron.
    if c.get("resultaat") and not c.get("bewijs"):
        fout("cases", f"{c['sleutel']}: resultaatclaim zonder bewijsbron. "
                      f"Vul 'bewijs' in of laat 'resultaat' leeg.")
    if c.get("quote") and c["toestemming"] == "geen":
        fout("cases", f"{c['sleutel']}: citaat terwijl er geen toestemming is")
    # Andersom net zo belangrijk: een case die als klantopdracht is gelabeld
    # terwijl de eigen tekst zegt dat er nooit een opdracht was. Dat is de
    # sabotage die een puur model-versus-pagina-controle niet ziet, omdat het
    # label dan keurig klopt met een status die zelf niet waar is.
    if c["status"] == "klantcase":
        tekst_k = " ".join(str(v) for v in c.values() if isinstance(v, str)).lower()
        for tegenspraak in ("ongevraagd", "geen opdracht", "niet voor betaald",
                            "zonder opdracht", "als kennismaking gebouwd",
                            "heeft er niet om gevraagd"):
            if tegenspraak in tekst_k:
                fout("cases", f"{c['sleutel']}: staat als klantopdracht maar de eigen "
                              f"tekst zegt {tegenspraak!r}. Klopt de status wel?")

    # Een demo of concept mag nooit als klantopdracht worden aangeprezen.
    if c["status"] in ("demo", "concept"):
        tekst_c = " ".join(str(v) for v in c.values() if isinstance(v, str)).lower()
        for verboden in ("in opdracht van", "onze klant", "de klant vroeg",
                         "opdrachtgever"):
            if verboden in tekst_c:
                fout("cases", f"{c['sleutel']}: is een {c['status']} maar de tekst "
                              f"suggereert een opdracht ({verboden!r})")

# Elke case die getoond wordt, moet zijn status ook zichtbaar op de pagina
# dragen. Anders is het model wel eerlijk maar de pagina niet.
werk = HTML.get("werk", "")
for c in CASES:
    if c["toestemming"] == "geen":
        continue
    label = STATUS_LABEL[c["status"]][0]
    if label not in werk:
        fout("werk", f"case {c['sleutel']} ({c['status']}) staat in het model maar "
                     f"het label {label!r} staat niet op de pagina")

# Geen resultaatclaims in de sitetekst zonder dat er ergens een bron bij staat.
_claims = re.findall(r"(\d{1,3})\s?%\s+(?:meer|hogere|stijging|groei|minder|omzet|conversie)", alle_tekst)
for cl in _claims:
    fout("claims", f"percentageclaim '{cl}%' op de site; die mag alleen met een "
                   f"controleerbare bron")

# --- 14f: sameAs niet leeg of nep -------------------------------------------
for p, graph in GRAPHS.items():
    for n in graph:
        if not isinstance(n, dict) or "sameAs" not in n:
            continue
        sa = n["sameAs"]
        sa = sa if isinstance(sa, list) else [sa]
        if not sa or any(not str(x).startswith("http") for x in sa):
            fout(p, f"sameAs bevat lege of ongeldige waarden: {sa}")
        for u in sa:
            if any(x in str(u).lower() for x in ("example.", "voorbeeld.", "your-", "jouw-")):
                fout(p, f"sameAs bevat een placeholder-URL: {u}")

# --- 14g: geen adres in het schema zonder bevestigde configuratie -----------
for p, graph in GRAPHS.items():
    for n in graph:
        if isinstance(n, dict) and "address" in n:
            adr = n["address"]
            if not isinstance(adr, dict) or not adr.get("streetAddress"):
                fout(p, "address in het schema zonder echt straatadres")

# --- 15: afbeeldingen -------------------------------------------------------
for p, h in HTML.items():
    for tag in re.findall(r"<img[^>]*>", h):
        if 'alt="' not in tag:
            fout(p, f"img zonder alt: {tag[:80]}")
        if "width=" not in tag or "height=" not in tag:
            fout(p, f"img zonder width/height (layout shift): {tag[:80]}")

# --- 16: basis-head ---------------------------------------------------------
for p, h in HTML.items():
    for nodig, omschrijving in [
        ('<html lang="nl">', "lang=nl"),
        ('<meta charset="utf-8">', "charset"),
        ('name="viewport"', "viewport"),
        ('property="og:title"', "og:title"),
        ('property="og:image"', "og:image"),
        ('name="twitter:card"', "twitter:card"),
        ('property="og:locale"', "og:locale"),
    ]:
        if nodig not in h:
            fout(p, f"ontbreekt in de head: {omschrijving}")


# ---------------------------------------------------------------------------
CONTROLES = [
    "JSON-LD geldig", "geen dubbele @id", "@id-verwijzingen sluitend",
    "kruimelpad == BreadcrumbList", "FAQ == FAQPage", "canonicals",
    "unieke titles en descriptions", "koppenhierarchie", "interne links",
    "geen weespagina's", "sitemap", "robots.txt", "llms.txt", "prijzen",
    "privacytekst klopt met de verzendroute", "honeypot op de formulieren",
    "zoekintentie zonder overlap", "trackingcode alleen met geldige config",
    "cases: demo niet als klantcase, geen claim zonder bron",
    "sameAs zonder placeholders", "geen adres zonder configuratie",
    "afbeeldingen", "head-basis",
]
print("Gecontroleerd: " + ", ".join(CONTROLES) + ".\n")

if fouten:
    print(f"{len(fouten)} probleem(en):\n")
    for f in fouten:
        print("  -", f)
    sys.exit(1)
print("Alles in orde.")

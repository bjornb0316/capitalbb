# -*- coding: utf-8 -*-
"""
Bouwt de complete Capital BB-site uit _bron/inhoud.py.

Draaien:  python _bron/bouw.py
Uitvoer:  gewone statische HTML in de hoofdmap, klaar voor GitHub Pages.

Waarom een generator: veertien pagina's delen navigatie, voettekst en
prijsblokken. Zonder generator betekent één tekstwijziging veertien
bestanden aanpassen. Crawlers en AI-systemen zien gewone HTML.
"""

import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inhoud import (CONTACT, MERKNAAM, SLOGAN, KETEN, NAV, NAV_CTA,
                    VOET_DIENSTEN, VOET_PRAKTISCH, PRIJS_WEB, PRIJS_CRM,
                    PRIJS_SYS, PRIJS_OS, PRIJS_ZICHT, PRIJS_ONDERHOUD,
                    ABON_VOORWAARDEN, SCAN_GROEPEN, NIET_DOEN, SPOREN, CASE,
                    PERSOON, KEUZEHULP, FAQ, CTA_PER_PAGINA, VERWANT, CASE2,
                    CASE_JEZZ, DEMOS, INTENTIES, FORMULIER, METEN, WIE, INDEXNOW)
from diensten import DIEP, FAQ_DIENST, FAQ_SCAN
from cases import CASES, STATUS_LABEL
from landing import LANDING, BACKLOG

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMEIN = "https://" + CONTACT["domein"]

# ---------------------------------------------------------------------------
# Dienstregister. Eén regel per dienst: (naam, serviceType, beschrijving,
# vanafprijs, per maand ja/nee). Voedt de Service-entiteiten, de
# OfferCatalog van de organisatie en de interne verwijzingen.
# ---------------------------------------------------------------------------
DIENSTEN = {
    "websites": ("Website en leadmachine", "Webdesign en webontwikkeling",
                 "Maatwerkwebsites en leadmachines die bezoekers omzetten in aanvragen "
                 "en afspraken, inclusief koppelingen met agenda, CRM en WhatsApp.",
                 "795", False),
    "online-marketing": ("Online marketing", "Online marketing en adverteren",
                        "Advertenties in Google en op social media, social media beheer, "
                        "contentproductie en e-mailmarketing, gekoppeld aan de website en het "
                        "CRM waar de aanvraag landt.",
                        None, False),
    "vindbaarheid": ("SEO en GEO", "Zoekmachineoptimalisatie en AI-vindbaarheid",
                     "Vindbaarheid in Google en in AI-assistenten: techniek, structured "
                     "data, lokale zichtbaarheid en citeerbare inhoud.",
                     "149", True),
    "ai-medewerkers": ("AI-medewerker en AI-telefonie", "AI-telefonie en digitale klantafhandeling",
                       "Een digitale medewerker die telefoon, WhatsApp, chat en e-mail "
                       "beantwoordt, afspraken inplant en doorgeeft wat hij niet zelf mag beslissen.",
                       "750", False),
    "crm": ("CRM-systeem", "CRM-implementatie en maatwerk-CRM",
            "Contacten, leads, offertes, opdrachten en opvolging in één systeem dat "
            "met de website, telefonie en AI-medewerker praat.",
            "159", True),
    "automatisering": ("Automatisering en bedrijfssystemen", "Workflowautomatisering en bedrijfssoftware",
                       "Workflows, koppelingen en bedrijfssystemen die terugkerend werk "
                       "overnemen en losse processen digitaliseren.",
                       "219", True),
    "business-os": ("Business OS", "Bedrijfsbreed softwareplatform",
                    "Het hele bedrijf vanuit één omgeving: CRM, projecten, planning, "
                    "medewerkers, documenten, rapportages en automatiseringen.",
                    "349", True),
}

# ---------------------------------------------------------------------------
# Laatste inhoudelijke wijziging per pagina. Stuurt zowel dateModified in de
# structured data als lastmod in de sitemap, zodat die twee nooit uit elkaar
# lopen. Alleen ophogen als de inhoud van díe pagina werkelijk veranderde.
# ---------------------------------------------------------------------------
GEWIJZIGD = {
    "*": "2026-09-03",
    "privacy": "2026-08-21",
}

# ---------------------------------------------------------------------------
# Extra tekst en vervolgroutes op de twee hubpagina's, zodat een hub niet
# alleen doorverwijst maar zelf ook iets zegt.
# ---------------------------------------------------------------------------
# Waar een dienst op de prijzenpagina staat, zodat een dienstpagina naar het
# juiste blok linkt in plaats van naar de bovenkant van een lange pagina.
PRIJSANKER = {
    "websites": "#websites",
    "crm": "#crm",
    "automatisering": "#automatisering",
    "business-os": "#business-os",
    "vindbaarheid": "#doorlopend",
    "online-marketing": "",
    "ai-medewerkers": "#doorlopend",
}

# De <title> van een hubpagina. De zichtbare kop blijft "Ik wil meer klanten";
# in een zoekresultaat zegt die zin te weinig over wat er te halen valt.
SPOOR_TITEL = {
    "meer-klanten": "Meer klanten online: website, vindbaarheid en opvolging",
    "slimmer-werken": "Slimmer werken: CRM, automatisering en Business OS",
}

SPOOR_EXTRA = {
    "meer-klanten": (
        "Meer klanten begint zelden bij meer bezoekers.",
        "In de meeste bedrijven komt er genoeg verkeer binnen en lekt het daarna weg: "
        "de site zegt niet duidelijk wat u doet, er is geen voor de hand liggende volgende "
        "stap, of de telefoon gaat over terwijl er niemand kan opnemen. Daarom staan deze "
        "drie oplossingen naast elkaar: gevonden worden, omzetten, en niets meer mislopen.",
        '<a class="tekstlink" href="../werk/">bekijk gebouwd werk</a>, '
        '<a class="tekstlink" href="../prijzen/">alle prijzen op één pagina</a> of '
        '<a class="tekstlink" href="../scan/">laat uw huidige website beoordelen</a>.',
    ),
    "slimmer-werken": (
        "Slimmer werken is één proces tegelijk.",
        "Bedrijven die alles tegelijk willen digitaliseren, komen zelden verder dan de "
        "inventarisatie. Daarom begint het bij het werk dat het vaakst terugkomt of het "
        "meest misgaat: eerst overzicht over klanten, dan het handwerk eruit, en pas "
        "daarna één omgeving voor het geheel.",
        '<a class="tekstlink" href="../werkwijze/">lees hoe een traject loopt</a>, '
        '<a class="tekstlink" href="../prijzen/">alle prijzen op één pagina</a> of '
        '<a class="tekstlink" href="../contact/">leg uw situatie voor</a>.',
    ),
}

# Versiestempel op css en js, zodat browsers na elke bouw de nieuwe bestanden
# ophalen in plaats van een oude cache te gebruiken.
import hashlib
def _stempel(pad):
    with open(os.path.join(WORTEL, pad), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]
V_CSS = _stempel("css/stijl.css")
V_JS = _stempel("js/site.js")

MERKTEKEN = (
    '<svg class="merkteken" viewBox="0 0 100 100" aria-hidden="true" focusable="false">'
    '<circle cx="50" cy="50" r="47" fill="none" stroke="currentColor" stroke-width="1.6"/>'
    '<circle cx="50" cy="50" r="36" fill="none" stroke="currentColor" stroke-width="1.1"/>'
    '<circle cx="9" cy="50" r="2.4" fill="currentColor"/>'
    '<circle cx="91" cy="50" r="2.4" fill="currentColor"/>'
    '<text x="50" y="62" text-anchor="middle" class="merk-cbb">CBB</text></svg>'
)


def kop_html(pad, titel, beschrijving, extra_head="", robots="index, follow"):
    canoniek = DOMEIN + "/" + (pad + "/" if pad else "")
    diep = "../" if pad else ""
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel}</title>
<meta name="description" content="{beschrijving}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0B0B0C">
<link rel="canonical" href="{canoniek}">
<link rel="icon" href="{diep}img/icoon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{diep}img/icoon-180.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{MERKNAAM}">
<meta property="og:url" content="{canoniek}">
<meta property="og:title" content="{titel}">
<meta property="og:description" content="{beschrijving}">
<meta property="og:image" content="{DOMEIN}/img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Het merkteken van Capital BB in goud op een donkere achtergrond.">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{diep}css/stijl.css?v={V_CSS}">
{extra_head}</head>
<body class="{'home' if not pad else 'inner-page'}">
<a class="skip" href="#hoofd">Naar de inhoud</a>
"""


def nav_html(pad, actief=""):
    diep = "../" if pad else ""
    links = "".join(
        f'<a href="{diep}{slug}/"{" aria-current=" + chr(34) + "page" + chr(34) if slug == actief else ""}>{naam}</a>'
        for slug, naam in ([("websites", "Websites"), ("online-marketing", "Marketing & social"), ("slimmer-werken", "Slimmer werken"), ("werk", "Werk"), ("contact", "Contact")] if not pad else NAV)
    )
    return f"""<nav class="nav" aria-label="Hoofdnavigatie">
  <a class="merk" href="{diep if pad else '#top'}">{MERKTEKEN}<span class="merk-woord">{MERKNAAM}</span><span class="vh">, naar de homepage</span></a>
  <div class="nav-links">{links}</div>
  <a class="btn btn-ghost btn-sm nav-cta" href="{diep}{NAV_CTA[0]}/">{NAV_CTA[1]}</a>
  <button class="nav-knop" id="nav-knop" aria-expanded="false" aria-controls="nav-menu" aria-label="Menu">
    <span></span><span></span><span></span>
  </button>
</nav>
<div class="nav-menu" id="nav-menu" hidden>
  {links}
  <a href="{diep}{NAV_CTA[0]}/">{NAV_CTA[1]}</a>
  <a href="{diep}contact/">Contact</a>
</div>
"""


def voet_html(pad):
    diep = "../" if pad else ""
    # Alleen op de contactpagina: de vaste lijst met intenties waaruit het
    # vraagveld alvast gevuld mag worden. Nooit tekst uit de URL zelf.
    import json as _json
    intenties = ("window.CBB_INTENTIES=" + _json.dumps(INTENTIES, ensure_ascii=False) + ";"
                 if pad == "contact" else "")
    formulier = ("window.CBB_FORMULIER=" + _json.dumps(FORMULIER, ensure_ascii=False) + ";"
                 if pad in ("contact", "scan") else "")
    meten = ("window.CBB_META=" + _json.dumps(METEN, ensure_ascii=False) + ";"
             if METEN.get("ga4") else "")
    # Toestemming intrekken moet net zo makkelijk zijn als geven. De link staat
    # er alleen als er iets te herzien valt, en wordt door de JS zichtbaar
    # gemaakt zodra er statistieken draaien.
    herzien = ('<a href="#" id="cookie-herzien" hidden>Cookievoorkeur wijzigen</a>'
               if METEN.get("ga4") else "")
    diensten = "".join(f'<a href="{diep}{s}/">{n}</a>' for s, n in VOET_DIENSTEN)
    praktisch = "".join(f'<a href="{diep}{s}/">{n}</a>' for s, n in VOET_PRAKTISCH)
    if CONTACT["telefoon"] or CONTACT["email"]:
        c = ""
        if CONTACT["telefoon"]:
            c += f'<a href="tel:{CONTACT["telefoon"].replace(" ", "")}">{CONTACT["telefoon"]}</a>'
        if CONTACT["email"]:
            c += f'<a href="mailto:{CONTACT["email"]}">{CONTACT["email"]}</a>'
        c += f'<span>{CONTACT["domein"]}</span>'
        c += f'<span>KvK {CONTACT["kvk"]}</span>'
    else:
        c = ('<p class="voet-todo">Nog in te vullen: telefoonnummer en e-mailadres. '
             'Zet ze in _bron/inhoud.py bij CONTACT en draai de bouw opnieuw.</p>')
    return f"""<footer class="voet">
  <div class="wrap voet-grid">
    <div>
      <span class="merk-woord voet-woord">{MERKNAAM}</span>
      <p class="voet-regel">{SLOGAN}. Werkgebied heel Nederland.</p>
    </div>
    <div class="voet-kolom"><h2>Oplossingen</h2>{diensten}</div>
    <div class="voet-kolom"><h2>Praktisch</h2>{praktisch}{herzien}</div>
    <div class="voet-kolom"><h2>Contact</h2>{c}</div>
  </div>
</footer>
<script>window.CBB_CONTACT={{"telefoon":"{CONTACT["telefoon"]}","whatsapp":"{CONTACT["whatsapp"]}","email":"{CONTACT["email"]}"}};{meten}{formulier}{intenties}</script>
<script src="{diep}js/site.js?v={V_JS}"></script>
</body>
</html>"""


def prijsblok(items, kolommen=3, cta=True, over="", knop="Laat het bouwen",
              tweede="Of start met de kosteloze scan", tweede_doel="../scan/"):
    """Prijskaarten. Elke rij eindigt standaard in een directe actie, want een
    prijs zonder volgende stap is een doodlopende gang. De actie krijgt de
    dienst mee, zodat het contactformulier weet waar het over gaat."""
    uit = [f'<div class="prijsrij kolommen-{kolommen}">']
    for it in items:
        naam, prijs, eenheid, tekst = it[0], it[1], it[2], it[3]
        top = len(it) > 4 and it[4]
        uit.append(
            f'<article class="prijskaart{" top" if top else ""}">'
            + (f'<span class="prijstag">Meest gekozen</span>' if top else "")
            + f'<h3>{naam}</h3>'
            f'<p class="prijs"><b>&euro;{prijs}</b><span>{eenheid}</span></p>'
            f'<p class="prijstekst">{tekst}</p></article>'
        )
    uit.append("</div>")
    if cta:
        doel = "../contact/" + (f"?over={over}" if over else "")
        uit.append(f'<div class="prijs-actie"><a class="btn btn-gold" href="{doel}">'
                   f'{knop}</a><a class="tekstlink" href="{tweede_doel}">'
                   f'{tweede}</a></div>')
    return "".join(uit)


def cta_blok(pad, kop="Wij bouwen eerst een voorstel. U beslist daarna.",
             tekst="Laat achter wat u doet en waar het wringt. U krijgt iets echts te zien, geen verkooppraatje.",
             knop="Plan een kennismaking"):
    """Slotblok. Kop, tekst en beide acties volgen de intentie van de pagina
    (CTA_PER_PAGINA). De scan is primair waar hij past en zakt elders naar de
    tweede plaats, of maakt plaats voor iets relevanters."""
    diep = "../" if pad else ""
    doel, tweede, tweede_doel = "contact/", "Start met de scan", "scan/"
    # Dienst- en hubpagina's uit CTA_PER_PAGINA, landingspagina's uit hun
    # eigen "cta". Beide zijn dezelfde zesdelige vorm.
    tabel = dict(CTA_PER_PAGINA)
    tabel.update({s: L["cta"] for s, L in LANDING.items()})
    if pad in tabel:
        kop, tekst, knop, doel, tweede, tweede_doel = tabel[pad]
    return f"""<section class="sectie cta-slot">
  <div class="wrap cta-inhoud">
    <h2 class="display">{kop}</h2>
    <p class="lede">{tekst}</p>
    <div class="cta-acties">
      <a class="btn btn-gold" href="{diep}{doel}">{knop}</a>
      <a class="btn btn-ghost" href="{diep}{tweede_doel}">{tweede}</a>
    </div>
    {direct_regel(pad)}
  </div>
</section>"""


def direct_regel(pad):
    """Onder elke CTA: appen of bellen, voor wie geen formulier wil invullen.
    Bewust kleiner dan de twee knoppen erboven; het is een alternatieve route,
    geen derde CTA die met de eerste twee concurreert."""
    if not CONTACT["whatsapp"] and not CONTACT["telefoon"]:
        return ""
    bel = (f'<a class="tekstlink" href="tel:{CONTACT["telefoon"].replace(" ", "")}">'
           f'bel {CONTACT["telefoon"]}</a>') if CONTACT["telefoon"] else ""
    wa = wa_knop(pad)
    if wa and bel:
        return f'<p class="cta-direct"><span>Liever direct?</span> {wa} <span>of {bel}</span></p>'
    return f'<p class="cta-direct"><span>Liever direct?</span> {wa or bel}</p>'


def kruimelpad(pad, titel, spoor=None, ouder=None):
    """Zichtbaar broodkruimelpad. Geeft de stappen terug zodat de
    BreadcrumbList in de centrale graph exact dezelfde reeks gebruikt.

    Een hubpagina staat nooit twee keer in haar eigen pad: als het spoor
    gelijk is aan de pagina zelf, is die stap de laatste en niet ook nog een
    tussenstap. Dat was de fout op /meer-klanten/ en /slimmer-werken/.
    """
    stappen = [("Home", DOMEIN + "/")]
    if spoor and spoor in SPOREN and spoor != pad:
        stappen.append((SPOREN[spoor]["titel"], f"{DOMEIN}/{spoor}/"))
    if ouder and ouder != pad:
        stappen.append((DIENSTEN[ouder][0], f"{DOMEIN}/{ouder}/"))
    stappen.append((titel, f"{DOMEIN}/{pad}/"))
    zichtbaar = '<nav class="kruimels" aria-label="Kruimelpad">' + " ".join(
        (f'<a href="{u.replace(DOMEIN + "/", "../")}">{n}</a>'
         f'<span aria-hidden="true">/</span>') if i < len(stappen) - 1
        else f'<span aria-current="page">{n}</span>'
        for i, (n, u) in enumerate(stappen)) + "</nav>"
    return zichtbaar, stappen


# ===========================================================================
# ENTITEITEN. Eén centrale graph met vaste @id's, op iedere pagina identiek.
# Zoekmachines en AI-systemen zien zo één Capital BB in plaats van vijftien
# losse bedrijfjes die toevallig dezelfde naam dragen.
# ===========================================================================
ID_ORG = DOMEIN + "/#organization"
ID_SITE = DOMEIN + "/#website"
ID_PERSOON = DOMEIN + "/#bjorn"
ID_LOGO = DOMEIN + "/#logo"

TELEFOON_E164 = "+" + CONTACT["whatsapp"] if CONTACT["whatsapp"] else ""

ORG_BESCHRIJVING = (
    "Capital BB bouwt websites en leadmachines, CRM- en bedrijfssystemen, Business OS, "
    "AI-medewerkers, AI-telefonie, workflowautomatisering en maatwerksoftware voor "
    "Nederlandse ondernemers, zzp'ers en mkb-bedrijven. Werkgebied heel Nederland."
)

KENT = [
    "Maatwerkwebsites", "Websites en leadgeneratie", "Conversieoptimalisatie",
    "CRM-systemen", "Bedrijfssystemen", "Business OS", "Maatwerksoftware",
    "AI-medewerkers", "AI-telefonie", "Digitale klantafhandeling",
    "Workflowautomatisering", "Systeemkoppelingen en API-integratie",
    "Zoekmachineoptimalisatie", "Generative Engine Optimization",
    "Vindbaarheid in AI-systemen", "Digitalisering van mkb-bedrijven",
]


def _org_entiteit():
    org = {
        "@type": ["Organization", "ProfessionalService"],
        "@id": ID_ORG,
        "name": MERKNAAM,
        "legalName": MERKNAAM,
        "url": DOMEIN + "/",
        "logo": {"@id": ID_LOGO},
        "image": {"@id": ID_LOGO},
        "description": ORG_BESCHRIJVING,
        "slogan": SLOGAN,
        "email": CONTACT["email"],
        "founder": {"@id": ID_PERSOON},
        "employee": {"@id": ID_PERSOON},
        "areaServed": {"@type": "Country", "name": "Nederland"},
        "identifier": {"@type": "PropertyValue", "propertyID": "KVK",
                       "value": CONTACT["kvk"]},
        "knowsAbout": KENT,
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Oplossingen van " + MERKNAAM,
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@id": _id_dienst(s)}}
                                for s in DIENSTEN],
        },
    }
    if TELEFOON_E164:
        org["telephone"] = TELEFOON_E164
        org["contactPoint"] = {
            "@type": "ContactPoint",
            "contactType": "customer service",
            "telephone": TELEFOON_E164,
            "email": CONTACT["email"],
            "areaServed": "NL",
            "availableLanguage": ["Dutch"],
        }
    # sameAs bewust leeg: er zijn geen bevestigde profielen om naar te wijzen.
    return org


def _basis_graph():
    return [
        _org_entiteit(),
        {
            "@type": "ImageObject",
            "@id": ID_LOGO,
            "url": DOMEIN + "/img/icoon-180.png",
            "contentUrl": DOMEIN + "/img/icoon-180.png",
            "width": 180, "height": 180,
            "caption": "Het merkteken van " + MERKNAAM,
        },
        {
            "@type": "Person",
            "@id": ID_PERSOON,
            "name": PERSOON["naam"],
            "givenName": "Björn",
            "familyName": "Beerntsen",
            "jobTitle": PERSOON["rol"],
            "description": ("Oprichter en bouwer van " + MERKNAAM +
                            ". Bouwt de systemen zelf en voert zelf de gesprekken."),
            "worksFor": {"@id": ID_ORG},
            "knowsAbout": KENT[:8],
            # image alleen bij een echte foto; geen placeholder in de data.
            **({"image": DOMEIN + "/" + WIE["foto"]} if WIE.get("foto") else {}),
            "mainEntityOfPage": DOMEIN + "/wie/",
        },
        {
            "@type": "WebSite",
            "@id": ID_SITE,
            "name": MERKNAAM,
            "url": DOMEIN + "/",
            "description": ORG_BESCHRIJVING,
            "publisher": {"@id": ID_ORG},
            "inLanguage": "nl-NL",
        },
    ]


def pagina_ld(pad, naam, beschrijving, stappen=None, faq=None, dienst=None,
              extra=None, over=None):
    """De volledige JSON-LD van één pagina: de centrale entiteiten plus de
    pagina zelf. Eén script, één @graph, geen dubbele @id's."""
    import json as _json
    url = DOMEIN + "/" + ((pad + "/") if pad else "")
    graph = _basis_graph()

    types = ["WebPage"]
    if faq:
        types.append("FAQPage")
    pagina = {
        "@type": types if len(types) > 1 else "WebPage",
        "@id": url + "#webpage",
        "url": url,
        "name": naam,
        "description": beschrijving,
        "isPartOf": {"@id": ID_SITE},
        "about": {"@id": over or ID_ORG},
        "publisher": {"@id": ID_ORG},
        "inLanguage": "nl-NL",
        "dateModified": GEWIJZIGD.get(pad, GEWIJZIGD["*"]),
        "primaryImageOfPage": {"@id": ID_LOGO},
    }
    if stappen:
        pagina["breadcrumb"] = {"@id": url + "#breadcrumb"}
    if faq:
        pagina["mainEntity"] = [
            {"@type": "Question", "name": v,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for v, a in faq]
    graph.append(pagina)

    if stappen:
        graph.append({
            "@type": "BreadcrumbList",
            "@id": url + "#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                for i, (n, u) in enumerate(stappen)],
        })
    if dienst:
        graph.append(dienst_entiteit(dienst, url))
    if extra:
        graph.extend(extra)

    # Compact: de graph is machineleesbaar, niet bedoeld om in de broncode te
    # lezen. Met inspringing was hij goed voor veertig procent van het
    # paginagewicht. De bron staat in dit bestand; wie hem wil lezen, gebruikt
    # de Rich Results Test of _bron/controle.py.
    return ('<script type="application/ld+json">'
            + _json.dumps({"@context": "https://schema.org", "@graph": graph},
                          ensure_ascii=False, separators=(",", ":"))
            + "</script>\n")


def verwant_blok(pad):
    """Interne routes: waar deze dienst logisch aan grenst."""
    if pad not in VERWANT:
        return ""
    links = ", ".join(
        f'<a class="tekstlink" href="../{d}/">{t}</a>' for d, t in VERWANT[pad][:-1])
    laatste = VERWANT[pad][-1]
    if links:
        links += f' of <a class="tekstlink" href="../{laatste[0]}/">{laatste[1]}</a>'
    else:
        links = f'<a class="tekstlink" href="../{laatste[0]}/">{laatste[1]}</a>'
    return (f'<section class="sectie verwant"><div class="wrap">'
            f'<p class="verwant-regel">Grenst hieraan: {links}.</p></div></section>')


def _id_dienst(slug):
    return f"{DOMEIN}/{slug}/#service"


def dienst_entiteit(slug, pagina_url=None):
    """Eén Service-entiteit, met de provider als verwijzing naar de centrale
    organisatie in plaats van een nieuw inline bedrijf."""
    naam, soort, beschrijving, prijs, per_maand = DIENSTEN[slug]
    if prijs is None:
        d = {
            "@type": "Service",
            "@id": _id_dienst(slug),
            "name": naam,
            "serviceType": soort,
            "description": beschrijving,
            "provider": {"@id": ID_ORG},
            "areaServed": {"@type": "Country", "name": "Nederland"},
            "audience": {"@type": "BusinessAudience",
                         "name": "Nederlandse zzp'ers en mkb-bedrijven"},
        }
        if pagina_url:
            d["mainEntityOfPage"] = {"@id": pagina_url + "#webpage"}
        else:
            d["url"] = f"{DOMEIN}/{slug}/"
        return d
    prijsspec = {
        "@type": "UnitPriceSpecification",
        "price": prijs.replace(".", ""),
        "priceCurrency": "EUR",
        "valueAddedTaxIncluded": False,
        "description": "Vanafprijs, exclusief 21% btw",
    }
    if per_maand:
        prijsspec["unitCode"] = "MON"
        prijsspec["billingIncrement"] = 1
    d = {
        "@type": "Service",
        "@id": _id_dienst(slug),
        "name": naam,
        "serviceType": soort,
        "description": beschrijving,
        "provider": {"@id": ID_ORG},
        "areaServed": {"@type": "Country", "name": "Nederland"},
        "audience": {"@type": "BusinessAudience", "name": "Nederlandse zzp'ers en mkb-bedrijven"},
        "offers": {"@type": "Offer", "priceCurrency": "EUR",
                   "availability": "https://schema.org/InStock",
                   "priceSpecification": prijsspec},
    }
    if pagina_url:
        d["mainEntityOfPage"] = {"@id": pagina_url + "#webpage"}
    else:
        d["url"] = f"{DOMEIN}/{slug}/"
    return d


def schrijf(pad, html):
    doel = os.path.join(WORTEL, pad) if pad else WORTEL
    os.makedirs(doel, exist_ok=True)
    bestand = os.path.join(doel, "index.html")
    io.open(bestand, "w", encoding="utf-8", newline="\n").write(html)
    return os.path.relpath(bestand, WORTEL)


def case_vlag(sleutel):
    """Zichtbaar label bij een case: klantopdracht, eigen merk of demo. Een
    bezoeker moet niet hoeven raden of hij naar betaald klantwerk kijkt of
    naar iets dat ongevraagd is gebouwd."""
    c = [x for x in CASES if x["sleutel"] == sleutel]
    if not c:
        return ""
    st = c[0]["status"]
    label, uitleg = STATUS_LABEL[st]
    return (f'<p class="casevlag vlag-{st}"><b>{label}</b>'
            f'<span>{uitleg}</span></p>')


def _landing_regel(slug):
    """Verwijzing van een dienstpagina naar de koopintentiepagina's die
    eronder hangen. Zonder deze regel zouden die pagina's alleen via de
    sitemap bereikbaar zijn."""
    kinderen = [(k, v) for k, v in LANDING.items() if v["ouder"] == slug]
    if not kinderen:
        return ""
    links = " &middot; ".join(f'<a class="tekstlink" href="../{k}/">{v["naam"]}</a>'
                              for k, v in kinderen)
    return f'<p class="route-regel"><b>Direct naar een specifieke vraag:</b> {links}</p>'


# ---------------------------------------------------------------------------
# Formulierverzending. Zolang er geen sleutel is ingevuld, openen de
# formulieren WhatsApp of het mailprogramma zoals altijd; met sleutel gaan ze
# rechtstreeks als e-mail de deur uit. Alle teksten die daarvan afhangen staan
# hier bij elkaar, zodat de pagina's nooit iets beweren wat niet klopt.
# ---------------------------------------------------------------------------
MAILT_DIRECT = bool(FORMULIER.get("sleutel"))

if MAILT_DIRECT:
    SUCCES_SCAN = ("Verstuurd. Uw aanvraag staat in de mailbox van Björn; u hoort binnen "
                   "één werkdag wat er uit de scan komt.")
    SUCCES_CONTACT = ("Verstuurd. Uw bericht staat in de mailbox van Björn; u krijgt binnen "
                      "één werkdag antwoord van een mens.")
    VERZENDNOOT = ("Het formulier verstuurt uw gegevens rechtstreeks naar het mailadres van "
                   f'{MERKNAAM}, via de verzenddienst Web3Forms. Zie de '
                   '<a class="tekstlink" href="../privacy/">privacyverklaring</a>.')
elif FORMULIER.get("terugval") != "whatsapp":
    # Geen sleutel: het formulier opent het mailprogramma van de bezoeker, met
    # het bericht er al in, gericht aan Capital BB.
    SUCCES_SCAN = ("Uw aanvraag staat klaar in uw mailprogramma, gericht aan "
                   f'{CONTACT["email"]}. Verstuur hem daar, dan gaat de scan lopen. Komt er '
                   f'niets in beeld? Mail of bel dan direct naar {CONTACT["telefoon"]}.')
    SUCCES_CONTACT = ("Uw bericht staat klaar in uw mailprogramma, gericht aan "
                      f'{CONTACT["email"]}. Verstuur hem daar, dan leest Björn hem vandaag '
                      f'nog. Komt er niets in beeld? Bel direct naar {CONTACT["telefoon"]}.')
    VERZENDNOOT = (f'Het formulier opent uw eigen mailprogramma met alles er al in, gericht '
                   f'aan {CONTACT["email"]}; u verstuurt het zelf en ziet precies wat er '
                   'weggaat. Liever niet mailen? Bellen of appen kan ook.')
else:
    SUCCES_SCAN = ("Uw aanvraag staat klaar in WhatsApp of uw mailprogramma. Verstuur hem "
                   "daar, dan gaat de scan lopen. Komt er niets in beeld? Bel of app direct "
                   f'naar {CONTACT["telefoon"]}.')
    SUCCES_CONTACT = ("Uw bericht staat klaar in WhatsApp of uw mailprogramma. Verstuur hem "
                      "daar, dan leest Björn hem vandaag nog. Komt er niets in beeld? Bel "
                      f'direct naar {CONTACT["telefoon"]}.')
    VERZENDNOOT = ("Het formulier opent WhatsApp of uw mailprogramma met alles er al in; "
                   "u verstuurt het zelf en ziet precies wat er weggaat.")


def honeypot():
    """Onzichtbaar veld tegen spambots. Een mens komt er nooit bij: buiten
    beeld, geen tabstop, en de schermlezer slaat hem over."""
    return ('<input type="text" name="botcheck" tabindex="-1" autocomplete="off" '
            'aria-hidden="true" class="vh-veld">')


def wa_knop(pad, tekst="Stuur een WhatsApp"):
    """WhatsApp als zichtbare alternatieve route, naast de gewone CTA's.
    Niet iedereen vult een formulier in; sommigen appen liever meteen."""
    if not CONTACT["whatsapp"]:
        return ""
    groet = "Hoi Björn, ik heb een vraag over "
    return (f'<a class="wa-knop" href="https://wa.me/{CONTACT["whatsapp"]}'
            f'?text={_url_tekst(groet + (pad or "Capital BB"))}" rel="noopener" target="_blank">'
            '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
            '<path d="M12 3.5c-4.7 0-8.5 3.4-8.5 7.6 0 2.4 1.2 4.5 3.1 5.9l-.8 3.5 3.6-1.6'
            'c.8.2 1.7.4 2.6.4 4.7 0 8.5-3.4 8.5-7.6S16.7 3.5 12 3.5z" fill="none" '
            'stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>'
            '<circle cx="8.6" cy="11.1" r="1.05" fill="currentColor"/>'
            '<circle cx="12" cy="11.1" r="1.05" fill="currentColor"/>'
            '<circle cx="15.4" cy="11.1" r="1.05" fill="currentColor"/></svg>'
            f'<span>{tekst}</span></a>')


def _url_tekst(t):
    from urllib.parse import quote
    return quote(t)


def antwoordblok(vraag, antwoord, kort=None):
    """Een citeerbaar antwoordblok: de vraag als kop, het antwoord er direct
    onder in één alinea die ook los van de pagina klopt. Zo halen AI-systemen
    het aan, en zo leest een haastige bezoeker het ook."""
    extra = f'<p class="antwoord-extra">{kort}</p>' if kort else ""
    return f"""<section class="sectie antwoord-sectie">
  <div class="wrap">
    <h2 class="display">{vraag}</h2>
    <p class="antwoord">{antwoord}</p>
    {extra}
  </div>
</section>"""


def diep_secties(slug, prijsdeel=""):
    """De inhoudelijke opbouw van een dienstpagina, uit diensten.py.
    Beantwoordt in vaste volgorde: wat is het, voor wie, welk probleem, wat
    bouwen wij, welke onderdelen, welk traject, welke koppelingen, wat kost
    het, wat is het verschil met alternatieven, en wat mag u verwachten."""
    d = DIEP[slug]
    naam = DIENSTEN[slug][0]

    voor_wie = "".join(f"<li>{x}</li>" for x in d["voor_wie"])
    bouwt = "".join(f'<div class="bouwt-item"><h3>{k}</h3><p>{t}</p></div>'
                    for k, t in d["bouwt"])
    onderdelen = "".join(f"<li>{x}</li>" for x in d["onderdelen"])
    traject = "".join(
        f'<li class="stapje"><span class="stapje-nr">{i+1}</span>'
        f'<div><b>{k}</b><span>{t}</span></div></li>'
        for i, (k, t) in enumerate(d["traject"]))
    koppel = "".join(f"<li>{x}</li>" for x in d["koppelingen"])
    verschil = "".join(f"<tr><th scope=\"row\">{a}</th><td>{b}</td></tr>"
                       for a, b in d["verschil"])
    branches = "".join(f'<div class="branche"><h3>{b}</h3><p>{t}</p></div>'
                       for b, t in d["branches"])

    vraag = d.get("vraag") or ("Wat is " + naam.lower() + "?")
    return f"""{antwoordblok(vraag, d["definitie"])}
<section class="sectie band">
  <div class="wrap split-tekst">
    <div>
      <h2 class="display">Voor wie dit is.</h2>
      <ul class="ticks">{voor_wie}</ul>
    </div>
    <div>
      <h2 class="display">Het probleem eronder.</h2>
      <p class="lede">{d["probleem"]}</p>
    </div>
  </div>
</section>

<section class="sectie">
  <div class="wrap">
    <h2 class="display">Wat Capital BB bouwt.</h2>
    <div class="bouwt-lijst">{bouwt}</div>
  </div>
</section>

<section class="sectie band">
  <div class="wrap split-tekst">
    <div>
      <h2 class="display">Wat erin kan zitten.</h2>
      <ul class="ticks kolomlijst">{onderdelen}</ul>
    </div>
    <div>
      <h2 class="display">Waarmee het koppelt.</h2>
      <ul class="ticks">{koppel}</ul>
    </div>
  </div>
</section>

<section class="sectie">
  <div class="wrap">
    <h2 class="display">Hoe het traject loopt.</h2>
    <ol class="stapjes">{traject}</ol>
  </div>
</section>

{prijsdeel}

<section class="sectie band">
  <div class="wrap">
    <h2 class="display">Hoe de prijs tot stand komt.</h2>
    <p class="lede">{d["prijsuitleg"]}</p>
    <p class="voetnoot"><a class="tekstlink" href="../prijzen/{PRIJSANKER.get(slug, "")}">Bekijk {naam.lower()} tussen alle prijzen</a>.</p>
  </div>
</section>

<section class="sectie">
  <div class="wrap">
    <h2 class="display">Het verschil met de alternatieven.</h2>
    <div class="tabelrol">
      <table class="vergelijk">
        <caption class="vh">Vergelijking van {naam.lower()} met de alternatieven</caption>
        <thead><tr><th scope="col">Aanpak</th><th scope="col">Wat dat in de praktijk betekent</th></tr></thead>
        <tbody>{verschil}</tbody>
      </table>
    </div>
  </div>
</section>

<section class="sectie band">
  <div class="wrap sec-kop">
    <h2 class="display">Wat u redelijk mag verwachten.</h2>
    <p class="lede">{d["verwachting"]}</p>
  </div>
</section>

<section class="sectie">
  <div class="wrap">
    <h2 class="display">Hoe dit er per branche uitziet.</h2>
    <p class="lede">Voorbeelden van wat er in zo'n bedrijf speelt. Capital BB werkt niet
    alleen voor deze branches, en dit zijn geen klantnamen of gerealiseerde resultaten.</p>
    <div class="branches">{branches}</div>
    {_landing_regel(slug)}
  </div>
</section>"""


def faq_blok(vragen, kop="Veelgestelde vragen."):
    """Zichtbare FAQ. Dezelfde lijst voedt het FAQPage-schema, zodat vraag en
    antwoord op de pagina letterlijk gelijk zijn aan de structured data."""
    if not vragen:
        return ""
    items = "".join(
        f'<details class="faq-item"><summary>{v}</summary><p>{a}</p></details>'
        for v, a in vragen)
    return f"""<section class="sectie faq-sectie">
  <div class="wrap">
    <h2 class="display">{kop}</h2>
    <div class="faq-lijst">{items}</div>
  </div>
</section>"""


# The three main entry pages share the approved homepage visual language.
DIENST_BEELD = {
    "websites": ("werk/demo-kapsalon.webp", 1024, 8560, "Websiteconcept voor een kapsalon", "Een eigen uitstraling. Tot in de details.", "Bespreek uw website", "websites"),
    "online-marketing": ("journey-marketing.png", 1024, 688, "Illustratieve contentshoot met camera en smartphone", "Content. Campagne. Contact.", "Bespreek uw marketing", "online-marketing"),
    "slimmer-werken": ("workspace-crm.png", 1024, 688, "Illustratief CRM op een laptop naast een telefoon", "Meer overzicht. Minder losse eindjes.", "Breng uw processen in kaart", "business-os"),
}


def dienst_opening(pad, kruimels, kop, tekst):
    img, w, h, alt, caption, knop, intentie = DIENST_BEELD[pad]
    beeldlabel = "Kapsalon · Websiteconcept" if pad == "websites" else "Illustratieve scène"
    return f'''<header class="dienst-opening"><div class="wrap">{kruimels}<div class="dienst-hero-grid"><div class="dienst-hero-copy"><h1 class="display">{kop}</h1><p class="lede">{tekst}</p><div class="cta-acties"><a class="btn btn-gold" href="../contact/?over={intentie}">{knop}</a><a class="dienst-verder" href="#in-praktijk">Bekijk hoe het werkt <span aria-hidden="true">↓</span></a></div></div><figure class="dienst-hero-media"><img src="../img/{img}" width="{w}" height="{h}" alt="{alt}" fetchpriority="high"><figcaption>{caption}<span>{beeldlabel}</span></figcaption></figure></div></div></header>'''


def dienst_praktijk(pad):
    if pad == "websites":
        return '''<section class="sectie dienst-praktijk" id="in-praktijk"><div class="wrap"><div class="praktijk-kop"><div><p class="eyebrow">Van idee naar ervaring</p><h2 class="display">Uw bedrijf heeft karakter.<br>Uw website ook.</h2></div><p class="lede">Geen vaste mal voor elk bedrijf. Deze websiteconcepten laten zien hoe sfeer, inhoud en een duidelijke vervolgstap samenkomen.</p></div><div class="dienst-concepten"><a class="dienst-concept" href="../werk/"><div class="concept-venster"><img src="../img/werk/demo-barbershop.webp" width="1280" height="6118" alt="Barbershop websiteconcept" loading="lazy"></div><span><b>Karakter dat blijft hangen.</b><small>Barbershop · Websiteconcept</small><i aria-hidden="true">↗</i></span></a><a class="dienst-concept" href="../werk/"><div class="concept-venster"><img src="../img/werk/demo-nagelstudio.webp" width="780" height="9366" alt="Nagelstudio websiteconcept" loading="lazy"></div><span><b>Verzorgd tot in de details.</b><small>Nagelstudio · Websiteconcept</small><i aria-hidden="true">↗</i></span></a></div><p class="voetnoot">Ontwerpvoorbeelden, geen klantresultaten. <a class="tekstlink" href="../werk/">Bekijk de toelichting bij ons werk</a>.</p></div></section>'''
    if pad == "online-marketing":
        return '''<section class="sectie dienst-praktijk" id="in-praktijk"><div class="wrap"><div class="praktijk-kop"><div><p class="eyebrow">Van aandacht naar actie</p><h2 class="display">Een goede campagne<br>stopt niet bij de klik.</h2></div><p class="lede">De boodschap in uw content, de pagina waarop iemand landt en de opvolging van een aanvraag moeten op elkaar aansluiten.</p></div><div class="marketing-verhaal"><figure><img src="../img/aftersales-flow.svg" width="1024" height="688" alt="Illustratief overzicht van servicecontact en feedback na oplevering" loading="lazy"><figcaption>Van bereik naar persoonlijk contact. Illustratieve scène.</figcaption></figure><div class="marketing-stappen"><details open><summary><span>01</span>Een verhaal dat aandacht verdient</summary><p>Content en social media laten zien wat u doet, voor wie en waarom dat relevant is. De campagne sluit aan op een concreet aanbod.</p></details><details><summary><span>02</span>Een pagina die de belofte waarmaakt</summary><p>De bezoeker komt op een passende landingspagina met uitleg, bewijs en een heldere aanvraagmogelijkheid.</p></details><details><summary><span>03</span>Een aanvraag die aandacht krijgt</summary><p>De aanvraag gaat naar de juiste plek. Een bevestiging en opvolgtaak zorgen dat iemand weet wat de volgende stap is.</p></details><details><summary><span>04</span>Contact dat na de verkoop doorgaat</summary><p>Service, feedback en relevante vervolgcommunicatie houden de klantrelatie actief. We stemmen af welke contactmomenten bij uw bedrijf passen.</p></details></div></div></div></section>'''
    return '''<section class="sectie dienst-praktijk" id="in-praktijk"><div class="wrap"><div class="praktijk-kop"><div><p class="eyebrow">Zo kan het samenwerken</p><h2 class="display">Eén aanvraag.<br>Iedere stap in beeld.</h2></div><p class="lede">Een voorbeeld van een verbonden werkproces. U ziet wie aan zet is, wat er moet gebeuren en waar een menselijke beslissing nodig blijft.</p></div><ol class="proces-baan"><li><span class="proces-nr">01 / Binnenkomst</span><h3>Nieuwe aanvraag</h3><p>Het formulier brengt de klantgegevens en de vraag bij elkaar.</p><span class="proces-label">Website → CRM</span></li><li><span class="proces-nr">02 / Opvolging</span><h3>Een duidelijke taak</h3><p>De juiste medewerker krijgt een taak en een afgesproken opvolgmoment.</p><span class="proces-label">CRM → Actie</span></li><li><span class="proces-nr">03 / Beslissing</span><h3>Persoonlijk voorstel</h3><p>U beoordeelt de vraag en bepaalt welke offerte of volgende stap past.</p><span class="proces-label">Mens → Voorstel</span></li><li><span class="proces-nr">04 / Relatie</span><h3>Ook na de verkoop</h3><p>Oplevering, service en feedback krijgen een plek in hetzelfde overzicht.</p><span class="proces-label">Klant → Service</span></li></ol><p class="voetnoot">Illustratief proces. We richten de stappen, verantwoordelijkheden en koppelingen in op uw bedrijf.</p></div></section>'''


def dienstpagina(pad, actief_spoor, titel, beschrijving, hero_kop, hero_tekst,
                 blokken, dienst=None, faq=None, paginatitel=None, over=None,
                 kruimel=None, ouder=None, robots="index, follow", extra_ld=None):
    """Standaardopbouw van een dienstpagina, met kruimelpad, FAQ en verwante
    routes. De structured data komt uit één centrale graph.

    titel      naam van de pagina in de structured data
    kruimel    korte naam in het kruimelpad (valt terug op titel)
    paginatitel  de <title>; valt terug op "titel | Capital BB"
    """
    spoor = actief_spoor if actief_spoor in SPOREN else None
    kruimels, stappen = kruimelpad(pad, kruimel or titel, spoor, ouder)
    ld = pagina_ld(pad, titel, beschrijving, stappen=stappen, faq=faq,
                   dienst=dienst, over=over or (_id_dienst(dienst) if dienst else None),
                   extra=extra_ld)
    h = kop_html(pad, paginatitel or f"{titel} | {MERKNAAM}", beschrijving, ld, robots)
    h += nav_html(pad, actief_spoor)
    opening = dienst_opening(pad, kruimels, hero_kop, hero_tekst) if pad in DIENST_BEELD else f'''<header class="pagina-kop">
  <div class="wrap">
    {kruimels}
    <h1 class="display">{hero_kop}</h1>
    <p class="lede">{hero_tekst}</p>
  </div>
</header>'''
    praktijk = dienst_praktijk(pad) if pad in DIENST_BEELD else ""
    klasse = f' class="dienst-editorial dienst-{pad}"' if pad in DIENST_BEELD else ""
    h += f"""<main id="hoofd"{klasse}>
{opening}
{praktijk}
{blokken}
{faq_blok(faq)}
{verwant_blok(pad)}
{cta_blok(pad)}
</main>
"""
    h += voet_html(pad)
    return schrijf(pad, h)


# ===========================================================================
# HOMEPAGE
# ===========================================================================
def bouw_home():
    # De hele entiteitsgraph plus de zes diensten, zodat de homepage het
    # ankerpunt is waar alle @id's samenkomen. FAQ-schema staat er alleen op
    # omdat de vragen verderop letterlijk zichtbaar zijn.
    ld = pagina_ld("", MERKNAAM + ", " + SLOGAN.lower(),
                   "Capital BB bouwt websites, CRM- en bedrijfssystemen, AI-medewerkers en "
                   "automatiseringen die samen één systeem vormen. Werkgebied heel Nederland.",
                   faq=FAQ,
                   extra=[dienst_entiteit(s) for s in DIENSTEN])
    faq_html = "".join(
        f'<details class="faq-item"><summary>{v}</summary><p>{a}</p></details>'
        for v, a in FAQ)

    sporen = ""
    for slug, sp in SPOREN.items():
        subs = "".join(
            f'<a class="spoor-sub" href="{d}/"><b>{t}</b><span>{u}</span></a>'
            for d, t, u in sp["links"]
        )
        sporen += (f'<div class="spoor"><a class="spoor-kop" href="{slug}/">'
                   f'<h3>{sp["titel"]}</h3><p>{sp["sub"]}</p><span class="spoor-pijl">Bekijk dit spoor</span></a>'
                   f'<div class="spoor-subs">{subs}</div></div>')

    koopvragen = "".join(
        f'<a class="keuze-rij" href="{slug}/"><span>{L["vraag"]}</span>'
        f'<b>{L["naam"]}</b></a>'
        for slug, L in LANDING.items())

    niet = "".join(f'<div class="creed-item"><h3>{k}</h3><p>{t}</p></div>' for k, t in NIET_DOEN)
    case_punten = "".join(f"<li>{p}</li>" for p in CASE["punten"])

    h = kop_html("", f"{MERKNAAM}, {SLOGAN.lower()}",
                 "Capital BB bouwt websites, CRM- en bedrijfssystemen, AI-medewerkers en automatiseringen "
                 "die samen één systeem vormen. Werkgebied heel Nederland.", ld)
    h += nav_html("")
    h += f"""<main id="hoofd">

<!-- Realistische Higgsfield-werkplek, tekst en bediening blijven echte HTML. -->
<section class="cinema" id="top" aria-label="Alles verbonden">
  <div class="cinema-media" aria-hidden="true"><img src="img/workspace-hero.png" width="1344" height="752" alt="" fetchpriority="high"></div>
  <div class="wrap cinema-copy">
    <h1>Uw bedrijf.<br>Alles verbonden.</h1>
    <p class="lede">Marketing, websites en opvolging. Alles verbonden.</p>
    <div class="cta-acties">
      <a class="btn btn-gold" href="#samenwerking">Ontdek wat mogelijk is</a>
      <a class="btn cinema-link" href="werk/">Bekijk ons werk <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M4 12h15m-6-6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></a>
    </div>
  </div>
  <div class="system-rail wrap" aria-label="De onderdelen van uw systeem"><span>Marketing &amp; social</span><span>Websites</span><span>Opvolging</span><span>Aftersales</span></div>
</section>
<section class="journey sectie" id="samenwerking" aria-labelledby="journey-heading">
  <div class="wrap">
    <header class="journey-heading"><p class="eyebrow">Eén verbonden klantreis</p><h2 class="display" id="journey-heading">Van eerste indruk.<br>Naar vaste klant.</h2><p class="lede">Meer dan losse oplossingen. Ontdek hoe elke stap de volgende sterker maakt.</p><p class="journey-scroll-hint">Scroll door de klantreis <span aria-hidden="true">↓</span></p></header>
    <div class="journey-grid">
      <div class="journey-visual" aria-hidden="true"><div class="journey-screen"><div class="journey-scene is-active" data-scene="0"><img src="img/journey-marketing.png" width="1024" height="688" alt="Illustratieve contentshoot met camera, smartphone en product" loading="lazy"><span class="journey-scene-label">Marketing &amp; social</span></div><div class="journey-scene" data-scene="1"><img src="img/workspace-hero.png" width="1344" height="752" alt="Illustratieve werkplek met een website op een groot beeldscherm" loading="lazy"><span class="journey-scene-label">Website &amp; aanvraag</span></div><div class="journey-scene" data-scene="2"><img src="img/workspace-crm.png" width="1024" height="688" alt="Illustratie van een laptop met CRM en een telefoon" loading="lazy"><span class="journey-scene-label">Leadopvolging</span></div><div class="journey-scene" data-scene="3"><img src="img/aftersales-flow.svg" width="1024" height="688" alt="Illustratieve opvolgroute met bedankbericht, servicecontact en feedbackvraag" loading="lazy"><span class="journey-scene-label">Aftersales</span></div><div class="journey-meter"><span class="journey-current">01</span><span class="journey-track"><i></i></span><span>04</span></div></div><p class="journey-caption">Een beeld van wat mogelijk is. Illustratieve scènes.</p></div>
      <div class="journey-chapters"><article class="journey-chapter" id="klantreis-1" data-chapter="0"><p class="journey-label"><span>01</span> Marketing &amp; social</p><h3>Word gezien.<br>Blijf hangen.</h3><p class="journey-body">Content, social media en campagnes brengen uw bedrijf onder de aandacht. Een herkenbaar verhaal dat de juiste mensen nieuwsgierig maakt.</p><p class="journey-tags">Content · Social media · Campagnes</p><div class="journey-fallback"><img src="img/journey-marketing.png" width="1024" height="688" alt="Illustratieve contentshoot met camera, smartphone en product" loading="lazy"></div></article><article class="journey-chapter" id="klantreis-2" data-chapter="1"><p class="journey-label"><span>02</span> Website &amp; aanvraag</p><h3>Van nieuwsgierig.<br>Naar geïnteresseerd.</h3><p class="journey-body">Uw website geeft het verhaal een plek. Met overtuigende pagina’s en een duidelijke volgende stap: een aanvraag, afspraak of aankoop.</p><p class="journey-tags">Websites · Landingspagina’s · Aanvragen</p><div class="journey-fallback"><img src="img/workspace-hero.png" width="1344" height="752" alt="Illustratieve werkplek met een website op een groot beeldscherm" loading="lazy"></div></article><article class="journey-chapter" id="klantreis-3" data-chapter="2"><p class="journey-label"><span>03</span> Leadopvolging</p><h3>Een goede lead.<br>Verdient aandacht.</h3><p class="journey-body">Het CRM bewaart de aanvraag. Opvolgtaken, offerteherinneringen en AI-ondersteuning helpen om op het juiste moment contact te houden.</p><p class="journey-tags">CRM · Offertes · Automatisering</p><div class="journey-fallback"><img src="img/workspace-crm.png" width="1024" height="688" alt="Illustratie van een laptop met CRM en een telefoon" loading="lazy"></div></article><article class="journey-chapter" id="klantreis-4" data-chapter="3"><p class="journey-label"><span>04</span> Aftersales</p><h3>Verkocht.<br>En dan begint het.</h3><p class="journey-body">Een bedankbericht. Even checken of alles goed gaat. Service, feedback en relevante herinneringen houden het contact persoonlijk, ook na de verkoop.</p><p class="journey-tags">Service · Feedback · Klantrelaties</p><div class="journey-fallback"><img src="img/aftersales-flow.svg" width="1024" height="688" alt="Illustratieve opvolgroute met bedankbericht, servicecontact en feedbackvraag" loading="lazy"></div></article></div>
    </div>
  </div>
</section>
<!-- WAT WIJ BOUWEN -->
<section class="sectie">
  <div class="wrap">
    <div class="sec-kop">
      <h2 class="display">Geen webbureau.<br>Een digitaliseringspartner.</h2>
      <p class="lede">Van marketing en social media tot websites, CRM en AI: wij verbinden de hele klantreis. Aanvragen en offertes krijgen opvolging. Na de verkoop blijven service, feedback en klantcontact op de agenda. Elk onderdeel is los af te nemen, maar de kracht zit in de samenwerking.</p>
    </div>
  </div>
</section>

<!-- DE TWEE SPOREN -->
<section class="sectie sporen-sectie">
  <div class="wrap">
    <h2 class="display center">Waar wil uw bedrijf naartoe?</h2>
    <div class="sporen">{sporen}</div>
  </div>
</section>

<!-- CASE -->
<section class="sectie case-sectie">
  <div class="wrap case-grid">
    <div>
      <p class="eyebrow">Gebouwd werk</p>
      <h2 class="display">Gebouwd om<br>te werken.</h2>
      <p class="lede">Van een overtuigende website tot een compleet bedrijfssysteem. Bekijk het gebouwde werk en de concepten, met de keuzes achter elk ontwerp.</p>
      <a class="btn btn-ghost" href="werk/">Bekijk dit werk en de andere cases</a>
    </div>
    <a class="case-beeld project-preview" href="werk/" aria-label="Bekijk ons werk en de concepten">
      <div class="project-browser" aria-hidden="true"><i></i><i></i><i></i><b>Barbershop · Websiteconcept</b></div>
      <div class="project-window"><img src="img/werk/demo-barbershop.webp" width="1280" height="6118" alt="Websiteconcept voor een barbershop" loading="lazy"></div>
      <span>Websiteconcept · Bekijk het werk <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M4 12h15m-6-6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></span>
    </a>
  </div>
</section>

<!-- SCAN-TEASER -->
<section class="sectie scan-teaser">
  <div class="wrap scan-grid">
    <div>
      <h2 class="display">Eerst inzicht.<br>Dan vooruit.</h2>
      <p class="lede">Laat uw website analyseren op conversie, techniek, vindbaarheid en groeikansen. Zeventien controlepunten, beoordeeld door een mens, binnen één werkdag.</p>
      <a class="btn btn-gold" href="scan/">Start de scan</a>
    </div>
    <div class="scan-punten" aria-hidden="true">
      <span>Conversie</span><span>Techniek</span><span>Vindbaarheid</span><span>Groeikansen</span>
    </div>
  </div>
</section>

<!-- WERKWIJZE KORT -->
<section class="sectie">
  <div class="wrap">
    <div class="sec-kop">
      <h2 class="display">Eerst bouwen, dan beslissen.</h2>
      <p class="lede">De meeste bureaus vragen een kennismakingsgesprek voordat u iets ziet. Wij draaien het om: u ziet eerst een werkend voorstel, en beslist daarna. <a class="tekstlink" href="werkwijze/">Zo werkt dat</a>.</p>
    </div>
  </div>
</section>

<!-- DE PERSOON ACHTER CAPITAL BB -->
<section class="sectie persoon-sectie" id="wie">
  <div class="wrap persoon-grid">
    <div class="persoon-teken" aria-hidden="true">{MERKTEKEN}</div>
    <div>
      <p class="eyebrow">Wie zit hierachter</p>
      <h2 class="display">U spreekt met de bouwer zelf.</h2>
      <p class="lede">{PERSOON["tekst"]}</p>
      <p class="persoon-visie">{PERSOON["visie"]}</p>
      <p class="persoon-naam">{PERSOON["naam"]}<span>{PERSOON["rol"]}, {MERKNAAM} · KvK {CONTACT["kvk"]}</span></p>
    </div>
  </div>
</section>

<!-- WAT WIJ NIET DOEN -->
<section class="sectie creed-sectie">
  <div class="wrap">
    <h2 class="display">Vier dingen die wij niet doen.</h2>
    <div class="creed-lijst">{niet}</div>
  </div>
</section>

<!-- PRIJZEN TEASER -->
<section class="sectie">
  <div class="wrap">
    <div class="sec-kop">
      <h2 class="display">Vanafprijzen, geen mistgordijn.</h2>
      <p class="lede">Websites vanaf &euro;795 eenmalig, CRM vanaf &euro;159 per maand, Business OS vanaf &euro;349 per maand. Alles exclusief btw, en wat u kiest bepaalt de prijs. <a class="tekstlink" href="prijzen/">Alle prijzen</a>.</p>
    </div>
  </div>
</section>

<!-- WAAR MENSEN MEE BINNENKOMEN -->
<section class="sectie">
  <div class="wrap">
    <h2 class="display">Waar ondernemers meestal mee binnenkomen.</h2>
    <p class="lede">Veelgestelde ondernemersvragen, elk met een eigen pagina waarop hij helemaal wordt beantwoord: kosten, doorlooptijd, de afweging en wat het u oplevert.</p>
    <div class="keuzehulp">{koopvragen}</div>
  </div>
</section>

<!-- VEELGESTELDE VRAGEN -->
<section class="sectie faq-sectie">
  <div class="wrap">
    <h2 class="display">Veelgestelde vragen.</h2>
    <div class="faq-lijst">{faq_html}</div>
  </div>
</section>

{cta_blok("")}
</main>
"""
    h += voet_html("")
    return schrijf("", h)


# ===========================================================================
# SPOORPAGINA'S
# ===========================================================================
def bouw_spoor(slug):
    sp = SPOREN[slug]
    ander = "slimmer-werken" if slug == "meer-klanten" else "meer-klanten"
    kaarten = "".join(
        f'<a class="dienstkaart" href="../{d}/"><h2>{t}</h2><p>{u}</p>'
        f'<span class="kaart-pijl">Bekijk {DIENSTEN[d][0].lower()}</span></a>'
        for d, t, u in sp["links"]
    )
    # Vervolgroutes: vanaf een hub moet je in één klik bij het bewijs, de
    # prijzen en de werkwijze kunnen. Anders is de hub een tussenstation
    # zonder eigen waarde.
    blokken = f"""<section class="sectie">
  <div class="wrap">
    <div class="dienstkaarten{" vier" if len(sp["links"]) > 3 else ""}">{kaarten}</div>
    <p class="ander-spoor">Zoekt u het andere: <a class="tekstlink" href="../{ander}/">{SPOREN[ander]["titel"].lower()}</a>?</p>
  </div>
</section>
<section class="sectie band">
  <div class="wrap sec-kop">
    <h2 class="display">{SPOOR_EXTRA[slug][0]}</h2>
    <p class="lede">{SPOOR_EXTRA[slug][1]}</p>
    <p class="verwant-regel">Verder kijken: {SPOOR_EXTRA[slug][2]}</p>
  </div>
</section>"""
    return dienstpagina(slug, slug, sp["titel"],
                        sp["sub"] + " Capital BB bouwt de systemen die daarbij horen.",
                        sp["titel"] + ".", sp["sub"], blokken,
                        paginatitel=f"{SPOOR_TITEL[slug]} | {MERKNAAM}")


# ===========================================================================
# DIENSTPAGINA'S
# ===========================================================================
def bouw_websites():
    prijsdeel = f"""<section class="sectie" id="prijzen">
  <div class="wrap">
    <h2 class="display">Vier niveaus, één lat.</h2>
    <p class="lede">Elke site, ook de kleinste, wordt gecontroleerd op mobiel gedrag, contrast, laadgewicht en vindbaarheid voordat hij live gaat. Alle bedragen eenmalig en exclusief btw.</p>
    {prijsblok(PRIJS_WEB, 4, over="websites", knop="Bespreek uw website", tweede="Of laat uw huidige site beoordelen")}
    <p class="voetnoot">Betaling in drie delen: 40% bij opdracht, 40% na goedkeuring van het ontwerp en 20% voor livegang.</p>
  </div>
</section>
<section class="sectie band">
  <div class="wrap">
    <h2 class="display">En daarna wordt hij onderhouden.</h2>
    <p class="lede">Een site die niemand bijhoudt, veroudert. Drie niveaus, per maand, exclusief btw. Onderhoud is een keuze, geen voorwaarde.</p>
    {prijsblok(PRIJS_ONDERHOUD, cta=False)}
  </div>
</section>"""
    return dienstpagina("websites", "meer-klanten", "Websites en leadmachines",
                        "Maatwerkwebsites die bezoekers omzetten in aanvragen en afspraken, "
                        "gekoppeld aan agenda, CRM en WhatsApp. Vanaf €795 eenmalig, exclusief btw.",
                        "Een website die werk oplevert.<br>Niet alleen bestaat.",
                        "Gebouwd om bezoekers om te zetten in aanvragen en afspraken, en gecontroleerd tot de laatste pagina.",
                        diep_secties("websites", prijsdeel),
                        dienst="websites", faq=FAQ_DIENST["websites"], kruimel="Websites",
                        paginatitel=f"Maatwerkwebsite en leadmachine laten maken | {MERKNAAM}")


def bouw_marketing():
    """Online marketing. Bewust zonder prijstabel: er is nog geen vanafprijs
    vastgesteld, en een verzonnen bedrag is erger dan geen bedrag. Wel staat
    er hoe de prijs wordt bepaald en dat het advertentiebudget erbuiten valt."""
    prijsdeel = f"""<section class="sectie band" id="budget">
  <div class="wrap split-tekst">
    <div>
      <h2 class="display">Uw advertentiebudget<br>blijft van u.</h2>
      <p class="lede">Het budget dat naar Google of Meta gaat, betaalt u rechtstreeks aan Google of Meta. Wij rekenen daar geen percentage over. Dat is in de markt gebruikelijk, maar het zou betekenen dat een hoger budget in ons eigen voordeel werkt, en dat is een slecht uitgangspunt voor advies.</p>
    </div>
    <div>
      <h2 class="display">Eerst rekenen,<br>dan adverteren.</h2>
      <p class="lede">Voordat er een euro weggaat, rekenen we samen door wat een gemiddelde opdracht u oplevert en hoeveel aanvragen klant worden. Daar rolt uit welk budget zin heeft. Komt daar geen werkbaar getal uit, dan zeggen we dat, ook als dat betekent dat u niets afneemt.</p>
    </div>
  </div>
</section>"""
    return dienstpagina("online-marketing", "meer-klanten", "Online marketing",
                        "Advertenties in Google en op social media, social media beheer, "
                        "contentproductie en e-mailmarketing, gekoppeld aan de website en het "
                        "CRM waar de aanvraag landt.",
                        "Campagnes die ergens<br>op uitkomen.",
                        "Marketing, social media en content trekken de aandacht. Opvolgsystemen begeleiden aanvragen en offertes. Aftersales houdt het contact na de verkoop warm.",
                        diep_secties("online-marketing", prijsdeel),
                        dienst="online-marketing", faq=FAQ_DIENST["online-marketing"],
                        kruimel="Online marketing",
                        paginatitel=f"Online marketing, adverteren en social media | {MERKNAAM}")


def bouw_vindbaarheid():
    prijsdeel = f"""<section class="sectie" id="prijzen">
  <div class="wrap">
    <h2 class="display">Twee zoekplekken, één aanpak.</h2>
    <p class="lede">Uw klant zoekt in Google, en steeds vaker stelt hij zijn vraag aan een AI-assistent. Wij bouwen voor allebei: techniek, lokale zichtbaarheid en inhoud die citeerbaar is. Per maand, exclusief btw.</p>
    {prijsblok(PRIJS_ZICHT, over="vindbaarheid", knop="Vraag een nulmeting aan", tweede="Of bespreek uw vindbaarheid", tweede_doel="../contact/?over=vindbaarheid")}
    <p class="eerlijk">Zichtbaarheid in AI-systemen verkopen wij niet als garantie. Wij bouwen wat het aantoonbaar mogelijk maakt: citeerbare antwoorden, kloppende bedrijfsgegevens, structured data, reviews en inhoudelijke autoriteit. Wie u een vaste plek in AI-antwoorden belooft, verkoopt iets wat hij niet in de hand heeft.</p>
  </div>
</section>"""
    return dienstpagina("vindbaarheid", "meer-klanten", "Vindbaarheid, SEO en GEO",
                        "Gevonden worden in Google én in AI-assistenten zoals ChatGPT en "
                        "Perplexity. SEO en GEO als één aanpak, vanaf €149 per maand exclusief btw.",
                        "Gevonden worden, ook waar<br>uw klant nu écht zoekt.",
                        "In de zoekmachine, en in de AI-assistenten die steeds vaker het eerste antwoord geven.",
                        diep_secties("vindbaarheid", prijsdeel),
                        dienst="vindbaarheid", faq=FAQ_DIENST["vindbaarheid"], kruimel="Vindbaarheid",
                        paginatitel=f"SEO en GEO voor bedrijven | {MERKNAAM}")


def bouw_ai():
    prijsdeel = f"""<section class="sectie">
  <div class="wrap split">
    <div>
      <h2 class="display">Om 21:42 gaat de telefoon.<br>Er wordt opgenomen.</h2>
      <p class="lede">Buiten werktijd, tijdens een klus, of als u al in gesprek bent. De AI-medewerker kent uw diensten, uw agenda en uw grenzen.</p>
      <ul class="ticks">
        <li>Praat via telefoon, WhatsApp, chat en e-mail</li>
        <li>Plant alleen in op tijden die u vrijgeeft</li>
        <li>Geeft aan u door zodra het over geld of uitzonderingen gaat</li>
        <li>Zet elke afspraak en elk gesprek direct in het CRM</li>
      </ul>
    </div>
    <div class="telefoon" aria-hidden="true">
      <div class="tel-top"><span class="tel-tijd">21:42</span><span class="tel-staat">Opgenomen door de assistent</span></div>
      <div class="tel-log">
        <p class="regel regel-klant">Goedenavond, kan ik deze week nog ergens terecht?</p>
        <p class="regel regel-ai">Dat kan. Donderdag om 09:15 of vrijdag om 14:00.</p>
        <p class="regel regel-klant">Donderdag is prima.</p>
        <p class="regel regel-ai">Genoteerd. U krijgt direct een bevestiging.</p>
        <p class="regel regel-sys">Afspraak vastgelegd. Klantkaart aangemaakt.</p>
      </div>
    </div>
  </div>
</section>
<section class="sectie band" id="prijzen">
  <div class="wrap">
    <h2 class="display">Wat het kost.</h2>
    <p class="lede">Inrichting vanaf <b class="goudcijfer">&euro;750</b>, exclusief verbruikskosten voor telefonie en AI. Het verbruik wordt apart doorbelast, zodat u ziet waar het geld heen gaat. Gekoppeld aan een <a class="tekstlink" href="../crm/">CRM-abonnement vanaf &euro;159 per maand</a> wordt de AI-medewerker onderdeel van het systeem in plaats van een losse tool.</p>
  </div>
</section>"""
    return dienstpagina("ai-medewerkers", "meer-klanten", "AI-medewerkers en AI-telefonie",
                        "Een digitale medewerker die telefoon, WhatsApp en e-mail beantwoordt, "
                        "afspraken inplant en doorgeeft wat hij niet mag beslissen. Inrichting vanaf €750.",
                        "Een medewerker die altijd opneemt.",
                        "Beantwoordt vragen, plant afspraken in en geeft door wat hij niet zelf mag beslissen.",
                        diep_secties("ai-medewerkers", prijsdeel),
                        dienst="ai-medewerkers", faq=FAQ_DIENST["ai-medewerkers"],
                        kruimel="AI-medewerkers",
                        paginatitel=f"AI-medewerker voor telefoon, WhatsApp en mail | {MERKNAAM}")


def bouw_crm():
    prijsdeel = f"""<section class="sectie" id="prijzen">
  <div class="wrap">
    <h2 class="display">Drie niveaus.</h2>
    <p class="lede">Als abonnement met eenmalige inrichting. Per maand, exclusief btw.</p>
    {prijsblok(PRIJS_CRM, over="crm", knop="Plan een CRM-demo", tweede="Of bekijk alle prijzen naast elkaar", tweede_doel="../prijzen/")}
    <p class="voetnoot">{ABON_VOORWAARDEN}</p>
  </div>
</section>"""
    return dienstpagina("crm", "slimmer-werken", "CRM-systeem",
                        "Klanten, offertes, opdrachten en opvolging op één plek, gekoppeld aan "
                        "uw website en telefonie. Vanaf €159 per maand plus €395 inrichting, exclusief btw.",
                        "Één plek voor elke klant.<br>In plaats van vier lijstjes.",
                        "Contacten, offertes, afspraken en opvolgtaken in één systeem dat met uw website en AI-medewerker praat.",
                        diep_secties("crm", prijsdeel),
                        dienst="crm", faq=FAQ_DIENST["crm"], kruimel="CRM",
                        paginatitel=f"CRM-systeem voor mkb en verkoopteams | {MERKNAAM}")


def bouw_automatisering():
    prijsdeel = f"""<section class="sectie" id="prijzen">
  <div class="wrap">
    <h2 class="display">Bedrijfssystemen.</h2>
    <p class="lede">Digitaliseren wat nu in Excel, WhatsApp en een map op de server tegelijk leeft: planning, werkbonnen, dossiers, aanvragen. Per maand, exclusief btw.</p>
    {prijsblok(PRIJS_SYS, over="automatisering", knop="Leg één proces voor", tweede="Of bekijk alle prijzen naast elkaar", tweede_doel="../prijzen/")}
    <p class="voetnoot">{ABON_VOORWAARDEN}</p>
  </div>
</section>
<section class="sectie band">
  <div class="wrap">
    <h2 class="display">Koppelingen en losse automatisering.</h2>
    <p class="lede">Eenvoudige koppeling vanaf <b class="goudcijfer">&euro;295</b>, standaard API-koppeling vanaf <b class="goudcijfer">&euro;650</b>, complexe koppeling vanaf <b class="goudcijfer">&euro;1.250</b>. Datamigratie vanaf <b class="goudcijfer">&euro;295</b>, extra dashboard vanaf <b class="goudcijfer">&euro;395</b>. Extra ontwikkeling op uurbasis vanaf <b class="goudcijfer">&euro;65</b>, na voorafgaand akkoord.</p>
  </div>
</section>"""
    return dienstpagina("automatisering", "slimmer-werken", "Automatisering en bedrijfssystemen",
                        "Workflows, koppelingen en bedrijfssystemen die terugkerend werk overnemen. "
                        "Losse koppeling vanaf €295, bedrijfssysteem vanaf €219 per maand, exclusief btw.",
                        "Wat u elke week opnieuw typt,<br>hoort één keer ingericht.",
                        "Bevestigingen, herinneringen, facturen en reviewverzoeken gaan vanzelf de deur uit. Processen krijgen een systeem.",
                        diep_secties("automatisering", prijsdeel),
                        dienst="automatisering", faq=FAQ_DIENST["automatisering"],
                        kruimel="Automatisering",
                        paginatitel=f"Bedrijfsprocessen automatiseren en bedrijfssystemen | {MERKNAAM}")


def bouw_os():
    prijsdeel = f"""<section class="sectie" id="prijzen">
  <div class="wrap">
    <h2 class="display">Drie niveaus.</h2>
    <p class="lede">Het hele bedrijf vanuit één omgeving: CRM, projecten, planning, medewerkers, documenten, rapportages en automatiseringen. Per maand, exclusief btw.</p>
    {prijsblok(PRIJS_OS, over="business-os", knop="Breng uw systemen in kaart", tweede="Of bekijk alle prijzen naast elkaar", tweede_doel="../prijzen/")}
    <p class="voetnoot">{ABON_VOORWAARDEN} Externe licenties en verbruik van AI, sms en e-mail worden apart doorbelast.</p>
  </div>
</section>"""
    return dienstpagina("business-os", "slimmer-werken", "Business OS",
                        "Het hele bedrijf vanuit één omgeving: CRM, projecten, planning, documenten "
                        "en automatisering. Vanaf €349 per maand plus €1.195 inrichting, exclusief btw.",
                        "Zeven losse abonnementen eruit.<br>Één omgeving erin.",
                        "CRM, projecten, planning, documenten en automatisering in één systeem dat het hele bedrijf aanstuurt.",
                        diep_secties("business-os", prijsdeel),
                        dienst="business-os", faq=FAQ_DIENST["business-os"], kruimel="Business OS",
                        paginatitel=f"Business OS voor groeiende mkb-bedrijven | {MERKNAAM}")


# ===========================================================================
# KOOPINTENTIEPAGINA'S
# Eén pagina per afgebakende zoekvraag, alleen waar hij iets zegt wat de
# dienstpagina niet zegt. De rest staat als backlog in landing.py.
# ===========================================================================
def bouw_landing(slug):
    L = LANDING[slug]

    wel = "".join(f"<li>{x}</li>" for x in L["wel"])
    niet = "".join(f"<li>{x}</li>" for x in L["niet"])

    secties = ""
    for kop, inleiding, punten in L["secties"]:
        regels = "".join(f"<li>{x}</li>" for x in punten)
        secties += f"""<section class="sectie">
  <div class="wrap">
    <h2 class="display">{kop}</h2>
    <p class="lede">{inleiding}</p>
    <ul class="ticks">{regels}</ul>
  </div>
</section>"""

    tabel = ""
    if L["tabel"]:
        ka, kb, rijen = L["tabel"]
        body = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td></tr>' for a, b in rijen)
        tabel = f"""<section class="sectie band">
  <div class="wrap">
    <h2 class="display">De routes naast elkaar.</h2>
    <div class="tabelrol">
      <table class="vergelijk">
        <caption class="vh">Vergelijking van de routes voor {L["naam"].lower()}</caption>
        <thead><tr><th scope="col">{ka}</th><th scope="col">{kb}</th></tr></thead>
        <tbody>{body}</tbody>
      </table>
    </div>
  </div>
</section>"""

    prijskop, prijstekst = L["prijs"]
    ouder = L["ouder"]
    blokken = f"""{antwoordblok(L["vraag"], L["antwoord"])}
<section class="sectie band">
  <div class="wrap">
    <h2 class="display">Voor wie dit wel en niet is.</h2>
    <div class="past">
      <div class="past-kolom past-wel"><h3>Dit past bij u als&hellip;</h3><ul>{wel}</ul></div>
      <div class="past-kolom past-niet"><h3>Dit past niet als&hellip;</h3><ul>{niet}</ul></div>
    </div>
  </div>
</section>
{secties}
{tabel}
<section class="sectie">
  <div class="wrap sec-kop">
    <h2 class="display">{prijskop}.</h2>
    <p class="lede">{prijstekst}</p>
    <p class="route-regel"><a class="tekstlink" href="../prijzen/{PRIJSANKER.get(ouder, "")}">Bekijk alle prijzen naast elkaar</a>.</p>
  </div>
</section>
<section class="sectie band">
  <div class="wrap sec-kop">
    <h2 class="display">Zo werkt het bij Capital BB.</h2>
    <p class="lede">Wij bouwen eerst een werkend voorstel; daarna beslist u. Bevalt het niet,
    dan kost het u niets. De volledige bouw start pas na uw akkoord, tegen de afgesproken
    prijs. <a class="tekstlink" href="../werkwijze/">Lees de volledige werkwijze</a>.</p>
    <p class="route-regel">{L["routes"]}</p>
  </div>
</section>"""

    return dienstpagina(slug, L["spoor"], L["naam"], L["beschrijving"],
                        L["h1"], L["lede"], blokken,
                        dienst=ouder, faq=L["faq"], ouder=ouder,
                        paginatitel=f"{L['titel']} | {MERKNAAM}")


# ===========================================================================
# SCAN
# ===========================================================================
def bouw_scan():
    groepen = ""
    totaal = 0
    for kop, punten in SCAN_GROEPEN:
        totaal += len(punten)
        groepen += ('<div class="scan-groep"><h3>' + kop + "</h3>"
                    + "".join(f'<p class="scan-punt"><em>{i+1}</em><span>{p}</span></p>'
                              for i, p in enumerate(punten)) + "</div>")

    beschrijving = ("Laat uw website kosteloos analyseren op conversie, techniek, vindbaarheid "
                    f"en groeikansen. {totaal} controlepunten, beoordeeld door een mens, "
                    "binnen één werkdag.")
    kruimels, stappen = kruimelpad("scan", "Website Performance Scan")
    h = kop_html("scan", f"Website Performance Scan, kosteloos | {MERKNAAM}", beschrijving,
                 pagina_ld("scan", "Website Performance Scan", beschrijving,
                           stappen=stappen, faq=FAQ_SCAN))
    h += nav_html("scan")
    h += f"""<main id="hoofd" class="scan-route">
<header class="pagina-kop">
  <div class="wrap">
    {kruimels}
    <p class="eyebrow">Kosteloos, binnen één werkdag</p>
    <h1 class="display">Waar laat uw website<br>aanvragen liggen?</h1>
    <p class="lede">Laat uw website analyseren op conversie, techniek, vindbaarheid en groeikansen. {totaal} controlepunten, beoordeeld door een mens die er werkelijk doorheen gaat.</p>
    <div class="cta-acties"><a class="btn btn-gold" href="#scanform">Vraag mijn kosteloze scan aan</a><a class="tekstlink" href="#voorbeeldrapport">Bekijk een voorbeeld</a></div>
  </div>
</header>

<section class="sectie scan-aanvraag" id="aanvragen">
  <div class="wrap scan-aanvraag-grid">
    <div class="scan-aanbod">
      <h2 class="display">Geen gokwerk.<br>Een helder verbeterplan.</h2>
      <p class="lede">U krijgt inzicht in wat goed werkt, waar bezoekers vastlopen en welke verbeteringen als eerste aandacht verdienen.</p>
      <ol class="scan-vervolg"><li><b>U deelt uw website</b><span>Vertel eventueel wat u ermee wilt bereiken.</span></li><li><b>Björn beoordeelt de website</b><span>17 controlepunten, met een menselijke beoordeling.</span></li><li><b>U krijgt het resultaat</b><span>Binnen één werkdag. Daarna beslist u zelf of u iets wilt laten verbeteren.</span></li></ol>
      <a class="tekstlink" href="#voorbeeldrapport">Bekijk hoe een bevinding eruitziet ↓</a>
    </div>
    <div><form class="scanform" id="scanform" novalidate>
      <h2>Vraag uw kosteloze scan aan</h2><p class="hint">Drie gegevens. Geen verplichting.</p>
      <div class="veld">
        <label for="s-url">Adres van uw website</label>
        <input id="s-url" type="text" inputmode="url" autocomplete="url" placeholder="uwbedrijf.nl" required>
      </div>
      <div class="veld">
        <label for="s-naam">Uw naam</label>
        <input id="s-naam" type="text" autocomplete="name" required>
      </div>
      <div class="veld">
        <label for="s-bereik">Telefoon of e-mail</label>
        <input id="s-bereik" type="text" required aria-describedby="s-bereik-hint">
        <p class="hint" id="s-bereik-hint">Vul uw e-mailadres of telefoonnummer in. Zo nemen we contact op over de scan.</p>
      </div>
      <div class="veld"><label for="s-doel">Wat wilt u verbeteren? <span class="hint">(optioneel)</span></label><select id="s-doel"><option value="">Kies uw belangrijkste doel</option><option>Meer aanvragen via mijn website</option><option>Beter gevonden worden</option><option>Leads en offertes beter opvolgen</option><option>Meer terugkerende klanten</option><option>Ik wil weten waar ik moet beginnen</option></select></div>
      {honeypot()}
      <p class="fout" id="s-fout" role="alert" hidden></p>
      <p class="succes" id="s-klaar" role="status" hidden>{SUCCES_SCAN}</p>
      <button class="btn btn-gold" type="submit">Vraag de scan aan</button>
      <p class="hint">Kosteloos, u zit nergens aan vast, en u hoeft niets technisch aan te leveren: uw websiteadres en contactgegevens zijn genoeg. {VERZENDNOOT}</p>
    </form>
    <div class="scan-ontvangen" id="scan-vervolg" hidden tabindex="-1"><h2>Dit is de volgende stap.</h2><p>Björn bekijkt uw website en neemt binnen één werkdag contact op over de uitkomst. Een kennismaking of offerte volgt alleen als u verder wilt.</p><a class="tekstlink" href="../werk/">Bekijk ondertussen ons werk →</a></div>
    <p class="cta-direct form-direct"><span>Liever appen dan typen?</span> {wa_knop("de Website Performance Scan", "App het adres van uw site")} <span>of bel <a class="tekstlink" href="tel:{CONTACT["telefoon"].replace(" ", "")}">{CONTACT["telefoon"]}</a></span></p></div>
  </div>
</section>

<section class="sectie scan-voorbeeld" id="voorbeeldrapport"><div class="wrap scan-twee"><div><p class="eyebrow">Voorbeeld, geen echte klantanalyse</p><h2 class="display">Van bevinding.<br>Naar volgende stap.</h2><p class="lede">Een bruikbaar rapport vertelt niet alleen wat er misgaat, maar ook wat u eraan kunt doen.</p><a class="btn btn-gold" href="#aanvragen">Laat mijn website bekijken</a></div><article class="voorbeeld-bevinding"><p class="eyebrow">Conversie / Voorbeeldbevinding</p><h3>De volgende stap is lastig te vinden.</h3><dl><dt>Observatie</dt><dd>Op de mobiele dienstenpagina staat de aanvraagknop pas na een lange lap tekst.</dd><dt>Waarom dit aandacht verdient</dt><dd>Een geïnteresseerde bezoeker moet zoeken naar een manier om contact op te nemen.</dd><dt>Eerste verbetering</dt><dd>Zet een duidelijke aanvraagknop bij het aanbod en controleer daarna of meer bezoekers een aanvraag afronden.</dd></dl><p class="hint">Illustratief voorbeeld. Uw rapport is gebaseerd op uw eigen website; resultaten worden niet vooraf beloofd.</p></article></div></section>
<section class="sectie band">
  <div class="wrap scan-twee">
    <div>
      <h2 class="display">Dit wordt nagelopen.</h2>
      <div class="scan-groepen">{groepen}</div>
    </div>
    <aside class="scan-rapport">
      <h2>Wat u terugkrijgt</h2>
      <div class="rapport-lijst">
        <div><b>Eén cijfer, met uitleg</b><span>Een totaalscore, en waar die vandaan komt.</span></div>
        <div><b>Wat er goed staat</b><span>Wat u niet moet aanraken, want dat werkt.</span></div>
        <div><b>De problemen, met bewijs</b><span>Per punt wat er misgaat en waarop dat te zien is.</span></div>
        <div><b>Urgentie per punt</b><span>Wat deze week moet en wat kan wachten.</span></div>
        <div><b>Verbeterkansen</b><span>Realistisch ingeschat, zonder beloofde percentages.</span></div>
        <div><b>Wat wij niet konden testen</b><span>Ook dat staat erin, want anders is het geen oordeel.</span></div>
      </div>
      <p class="eerlijk">Er wordt niets gemeten terwijl u hier wacht. Björn beoordeelt uw website na de aanvraag. U krijgt de uitkomst persoonlijk terug.</p>
    </aside>
  </div>
</section>
{faq_blok(FAQ_SCAN, "Over de scan.")}
{cta_blok("scan", "Liever meteen praten?", "Dat kan ook. De scan is een begin, geen verplicht voorportaal.")}
</main>
"""
    h += voet_html("scan")
    return schrijf("scan", h)


# ===========================================================================
# WERK / WERKWIJZE / PRIJZEN / CONTACT
# ===========================================================================
def bouw_werk():
    impact2 = "".join(f"<li>{p}</li>" for p in CASE2["impact"])
    impact_j = "".join(f"<li>{p}</li>" for p in CASE_JEZZ["impact"])
    # Drie ontwerprichtingen uit de demoreeks, gerenderd met generieke
    # teksten zodat geen enkel bedrijf herkenbaar is. Richting en gevoel,
    # geen herhalende lijst.
    # Echte schermafbeeldingen van drie demosites, met namen en herleidbare
    # gegevens onherkenbaar gemaakt. Gemaakt met scripts/schiet.mjs (headless
    # Edge via het DevTools-protocol) en geanonimiseerd met Pillow.
    # Drie demosites op drie apparaten: beeldscherm, laptop en telefoon, elk
    # scrollend door de volledige (geanonimiseerde) pagina. Opgenomen met
    # scripts/schiet-lang.mjs, namen en gegevens vóór de opname vervangen.
    demo_tegels = """
    <div class="bureau">
      <figure class="apparaat monitor">
        <div class="monitor-scherm scrol" style="--duur:64s"><img src="../img/werk/demo-barbershop.webp" width="1280" height="6118" loading="lazy" alt="Demosite voor een barbershop op een beeldscherm: donker interieur, groot serif-woordmerk, reserveren en appen. Naam en gegevens zijn vervangen."></div>
        <div class="monitor-hals"></div><div class="monitor-voet"></div>
        <figcaption>Barbershop: donker en filmisch, reserveren via het eigen boekingssysteem</figcaption>
      </figure>
      <figure class="apparaat laptop">
        <div class="laptop-scherm scrol" style="--duur:78s;--start:-26s"><img src="../img/werk/demo-kapsalon.webp" width="1024" height="8560" loading="lazy" alt="Demosite voor een kapsalon op een laptop: zwart-wit interieurfoto met rode accenten. Naam en gegevens zijn vervangen."></div>
        <div class="laptop-voet"></div>
        <figcaption>Kapsalon: rauw en direct, rond de eigen interieurfoto&apos;s</figcaption>
      </figure>
      <figure class="apparaat telefoon">
        <div class="telefoon-scherm scrol" style="--duur:58s;--start:-40s"><img src="../img/werk/demo-nagelstudio.webp" width="780" height="9366" loading="lazy" alt="Demosite voor een nagelstudio op een telefoon: lichte fotocollage van nagels met de kop Nagels, na werktijd. Gegevens zijn vervangen."></div>
        <figcaption>Nagelstudio, mobiel: licht en zacht, met de agenda van de studio erachter</figcaption>
      </figure>
    </div>"""
    blokken = f"""<section class="sectie">
  <div class="wrap case-jezz">
    <div>
      <p class="eyebrow">Live te bekijken</p>
      <h2 class="display">{CASE_JEZZ["kop"]}</h2>
      {case_vlag("jezz-media")}
      <div class="case-poi">
        <div><h3>Probleem</h3><p>{CASE_JEZZ["probleem"]}</p></div>
        <div><h3>Oplossing</h3><p>{CASE_JEZZ["oplossing"]}</p></div>
        <div><h3>Impact</h3><ul class="ticks">{impact_j}</ul></div>
      </div>
      <p class="case-link"><a class="btn btn-ghost" href="{CASE_JEZZ["url"]}" rel="noopener">Bekijk jezz-media.nl</a></p>
      <p class="route-regel"><b>Diensten die hierin zitten:</b>
        <a class="tekstlink" href="../websites/">websites en leadmachines</a>,
        <a class="tekstlink" href="../vindbaarheid/">SEO en GEO</a> voor een kennisbank die
        inhoudelijk mee kan groeien, en een structuur die klaar is voor
        <a class="tekstlink" href="../crm/">CRM voor verkoopopvolging</a>.</p>
      <p class="case-noot">{CASE_JEZZ["naam"]} is het makelaars- en hypotheekmerk van dezelfde oprichter; de site is door {MERKNAAM} gebouwd en draait live.</p>
    </div>
    <div class="laptop" aria-hidden="true">
      <div class="laptop-scherm">
        <div class="laptop-scroll"><img src="../img/werk/jezz-scroll.webp" width="1024" height="12864" alt="" loading="lazy"></div>
      </div>
      <div class="laptop-voet"></div>
    </div>
  </div>
</section>
<section class="sectie band">
  <div class="wrap case-grid">
    <div>
      <p class="eyebrow">{CASE["pakket"]}</p>
      <h2 class="display">{CASE["kop"]}</h2>
      {case_vlag("ijsseldal")}
      <div class="case-poi">
        <div><h3>Probleem</h3><p>Een {CASE["naam"].lower()} in {CASE["regio"]} zonder eigen website: klanten vinden de adviseur alleen via het profiel van een landelijk netwerk, zonder eigen verhaal, eigen vindbaarheid of eigen aanvraagroute.</p></div>
        <div><h3>Oplossing</h3><p>Een complete site van tien pagina's op een eigen designsysteem dat de blauwwitte huisstijl van de branche bewust vermijdt, met werkwijze, tarieven en veelgestelde vragen. Elke bewering op de site is nagetrokken tot de bron en met controledatum vastgelegd.</p></div>
        <div><h3>Impact</h3><p>De adviseur heeft een eigen plek waar bezoekers rechtstreeks een gesprek kunnen aanvragen, met inhoud die klopt en gecontroleerd is op contrast, mobiel gedrag, laadgewicht en toegankelijkheid.</p></div>
      </div>
      <p class="route-regel"><b>Diensten die hierin zitten:</b>
        <a class="tekstlink" href="../websites/">websites en leadmachines</a> op een eigen
        designsysteem, met de technische basis voor
        <a class="tekstlink" href="../vindbaarheid/">vindbaarheid in Google en AI-systemen</a>.
        Voor een praktijk met veel dossiers is
        <a class="tekstlink" href="../crm/">CRM voor dossieropvolging</a> de logische
        volgende stap.</p>
    </div>
    <div class="case-beeld" aria-hidden="true">
      <div class="venster-mini">
        <div class="vm-bar"><span class="vm-stippen"><i></i><i></i><i></i></span><span class="vm-url">Designsysteem IJsseldal</span></div>
        <div class="ijs">
          <div class="ijs-nav"><b>Adviespraktijk</b><span>Hypotheekadvies</span><span>Werkwijze</span><span>Tarieven</span><em>Afspraak maken</em></div>
          <div class="ijs-hero">
            <div class="ijs-tekst">
              <small>Onafhankelijk zelfstandig adviseur</small>
              <strong>Het hele aanbod, niet &eacute;&eacute;n bank</strong>
              <p>Een hypotheek kiezen is niet &eacute;&eacute;n beslissing maar tientallen kleine.</p>
              <em>Plan een gesprek</em>
            </div>
            <div class="ijs-portret"></div>
          </div>
          <div class="ijs-band">Eerst rekenen, dan pas praten over banken</div>
          <div class="ijs-rij"><span>Eerste woning</span><span>Oversluiten</span><span>Verbouwen</span></div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="sectie">
  <div class="wrap">
    <p class="eyebrow">Eigen werk als bewijs</p>
    <h2 class="display">{CASE2["kop"]}</h2>
    {case_vlag("demoreeks")}
    <div class="case-poi kolommen">
      <div><h3>Probleem</h3><p>{CASE2["probleem"]}</p></div>
      <div><h3>Oplossing</h3><p>{CASE2["oplossing"]}</p></div>
      <div><h3>Impact</h3><ul class="ticks">{impact2}</ul></div>
    </div>
    {demo_tegels}
    <p class="route-regel"><b>Diensten die hierin zitten:</b>
      <a class="tekstlink" href="../websites/">websites en leadmachines</a>, elk met een
      <a class="tekstlink" href="../automatisering/">koppeling met het bestaande boekingssysteem</a>.
      In zaken waar de telefoon overgaat tijdens het werk sluit
      <a class="tekstlink" href="../ai-medewerkers/">een AI-medewerker die opneemt</a> hierop aan.</p>
    <p class="case-noot">Elf demosites in totaal, voor kapsalons, barbershops, nagelstudio's en beautystudio's, gekoppeld aan onder meer Salonized, Knipklok, Altegio en Afspraakpro. Zonder naam of merk, want ze zijn ongevraagd gebouwd als kennismaking; de bedrijven bestaan echt en de koppelingen draaien op hun echte boekingssysteem.</p>
  </div>
</section>
<section class="sectie band">
  <div class="wrap">
    <h2 class="display">Waarom hier geen logowand staat.</h2>
    <p class="lede">Wij tonen alleen werk waarvoor de eigenaar toestemming gaf, en namen alleen mét die toestemming. Liever weinig werk dat klopt dan tien logo's die niets bewijzen. Dit overzicht groeit met het werk mee.</p>
    <p class="lede">Daarom staat er bij elk project wat het is. Dat onderscheid is bewust, want het scheelt nogal:</p>
    <div class="legenda">
      <div><b>Klantopdracht</b><span>Een betaalde opdracht voor een externe klant.</span></div>
      <div><b>Eigen merk, live</b><span>Echt gebouwd en online, maar voor een merk van de oprichter zelf. Geen externe opdrachtgever, dus ook geen bewijs van klanttevredenheid.</span></div>
      <div><b>Demonstratie</b><span>Ongevraagd gebouwd als kennismaking. Er is geen opdracht aan voorafgegaan en er is niet voor betaald.</span></div>
    </div>
    <p class="eerlijk">U vindt op deze pagina geen conversiepercentages of omzetstijgingen. Niet omdat er niets gebeurt, maar omdat wij alleen cijfers publiceren die de klant zelf heeft aangeleverd én waarvan de bron genoemd mag worden. Zodra dat er is, komt het erbij te staan, met bron en datum.</p>
  </div>
</section>"""
    return dienstpagina("werk", "werk", "Werk",
                        "Gebouwd werk van Capital BB: een live site, een compleet designsysteem en "
                        "elf demosites met werkende boekingskoppelingen. Per project wat er "
                        "werkelijk is opgeleverd.",
                        "Werk dat er echt staat.",
                        "Geen opgepoetste portfolio-tegels, maar wat er werkelijk is gebouwd, hoe, en met welke onderdelen.",
                        blokken,
                        paginatitel=f"Gebouwd werk en cases | {MERKNAAM}")


def bouw_werkwijze():
    niet = "".join(f'<div class="creed-item"><h3>{k}</h3><p>{t}</p></div>' for k, t in NIET_DOEN)
    blokken = f"""<section class="sectie">
  <div class="wrap">
    <div class="stappen">
      <div class="stap"><span class="stapnr">1</span><h2>U laat zien waar het wringt</h2>
        <p>Via de scan, het contactformulier of een gesprek. Wat kost tijd, wat loopt mis, wat blijft liggen.</p>
        <p class="route-regel"><a class="tekstlink" href="../scan/">Laat uw huidige website beoordelen</a> of <a class="tekstlink" href="../contact/?over=werkwijze">leg uw situatie direct voor</a>.</p></div>
      <div class="stap"><span class="stapnr">2</span><h2>Wij bouwen eerst een voorstel</h2>
        <p>Geen offerte van zes kantjes, maar een werkend concept dat u kunt aanklikken en beoordelen. Een voorstel, nog niet het volledige systeem.</p>
        <p class="route-regel"><a class="tekstlink" href="../werk/">Bekijk wat er eerder is gebouwd</a>.</p></div>
      <div class="stap"><span class="stapnr">3</span><h2>U beslist met iets tastbaars</h2>
        <p>Bevalt het voorstel niet, dan kost het u niets. Bevalt het wel, dan starten de volledige bouw en inrichting na uw akkoord, tegen de afgesproken prijs.</p>
        <p class="route-regel"><a class="tekstlink" href="../prijzen/">Bekijk vooraf alle vanafprijzen</a>.</p></div>
      <div class="stap"><span class="stapnr">4</span><h2>Het systeem groeit mee</h2>
        <p>Wat als website begint, kan doorgroeien naar CRM, AI-medewerker en automatisering. In dat tempo beslist u.</p>
        <p class="route-regel">Van <a class="tekstlink" href="../websites/">website en leadmachine</a> naar <a class="tekstlink" href="../crm/">CRM voor verkoopopvolging</a>, <a class="tekstlink" href="../automatisering/">geautomatiseerde bedrijfsprocessen</a> en <a class="tekstlink" href="../business-os/">een Business OS voor het hele bedrijf</a>.</p></div>
    </div>
  </div>
</section>
<section class="sectie band">
  <div class="wrap">
    <h2 class="display">Vier dingen die wij niet doen.</h2>
    <div class="creed-lijst">{niet}</div>
  </div>
</section>"""
    return dienstpagina("werkwijze", "werkwijze", "Werkwijze",
                        "Eerst bouwen, dan beslissen. U ziet een werkend voorstel voordat u "
                        "iets uitgeeft; bevalt het niet, dan kost het niets.",
                        "Eerst bouwen.<br>Dan beslissen.",
                        "De meeste bureaus laten u praten voordat u iets ziet. Wij draaien dat om.",
                        blokken,
                        paginatitel=f"Werkwijze: eerst bouwen, dan beslissen | {MERKNAAM}")


def bouw_prijzen():
    keuze = "".join(
        f'<a class="keuze-rij" href="../{d}/"><span>{vraag}</span><b>{product}</b></a>'
        for vraag, d, product in KEUZEHULP)
    blokken = f"""<section class="sectie keuze-sectie">
  <div class="wrap">
    <h2 class="display">Eerst: wat zoekt u eigenlijk?</h2>
    <p class="lede">Vijf producten lijken op elkaar tot je weet waar je voor komt. Kies de zin die op u slaat.</p>
    <div class="keuzehulp">{keuze}</div>
  </div>
</section>
<section class="sectie">
  <div class="wrap">
    <h2 class="display" id="websites">Websites</h2>
    <p class="route-regel"><a class="tekstlink" href="../websites/">Bekijk websites en leadmachines</a></p>
    <p class="lede">Eenmalig, exclusief btw. Betaling in drie delen: 40% bij opdracht, 40% na ontwerpgoedkeuring, 20% voor livegang.</p>
    {prijsblok(PRIJS_WEB, 4, cta=False)}
  </div>
</section>
<section class="sectie band">
  <div class="wrap">
    <h2 class="display" id="crm">CRM</h2>
    <p class="route-regel"><a class="tekstlink" href="../crm/">Bekijk CRM voor verkoopopvolging</a></p>
    {prijsblok(PRIJS_CRM, cta=False)}
    <h2 class="display ruimte" id="automatisering">Bedrijfssystemen</h2>
    <p class="route-regel"><a class="tekstlink" href="../automatisering/">Bekijk automatisering en bedrijfssystemen</a></p>
    {prijsblok(PRIJS_SYS, cta=False)}
    <h2 class="display ruimte" id="business-os">Business OS</h2>
    <p class="route-regel"><a class="tekstlink" href="../business-os/">Bekijk een Business OS in de praktijk</a></p>
    {prijsblok(PRIJS_OS, cta=False)}
    <p class="voetnoot">{ABON_VOORWAARDEN}</p>
  </div>
</section>
<section class="sectie">
  <div class="wrap">
    <h2 class="display" id="doorlopend">Doorlopend</h2>
    <p class="lede">Onderhoud en zichtbaarheid, per maand, exclusief btw.</p>
    <p class="route-regel"><a class="tekstlink" href="../vindbaarheid/">Bekijk SEO en GEO voor bedrijven</a> of <a class="tekstlink" href="../ai-medewerkers/">bekijk de AI-telefoniste</a>.</p>
    {prijsblok(PRIJS_ONDERHOUD, cta=False)}
    {prijsblok(PRIJS_ZICHT, over="prijzen", knop="Leg uw situatie voor", tweede="Of lees eerst de werkwijze", tweede_doel="../werkwijze/")}
    <p class="voetnoot">AI-assistent vanaf &euro;750 inrichting, exclusief verbruik. Koppelingen vanaf &euro;295. Extra ontwikkeling vanaf &euro;65 per uur, na voorafgaand akkoord. Spoed 20% toeslag.</p>
  </div>
</section>"""
    return dienstpagina("prijzen", "prijzen", "Prijzen",
                        "Alle vanafprijzen van Capital BB op één pagina: websites vanaf €795, "
                        "CRM vanaf €159 per maand, Business OS vanaf €349 per maand. Exclusief btw.",
                        "Alle prijzen.<br>Op één pagina.",
                        "Vanafprijzen, exclusief 21% btw. Wat u kiest bepaalt de prijs, niet hoe het gesprek loopt.",
                        blokken,
                        paginatitel=f"Prijzen: websites, CRM, Business OS en AI | {MERKNAAM}")


def bouw_wie():
    """De pagina over Björn. Geen E-E-A-T-taal, geen 'expert' of 'marktleider';
    alleen wat te controleren valt. Er komt pas een portret op zodra er een
    echte foto is: WIE["foto"] in inhoud.py."""
    blokken_html = "".join(
        f'<div class="wie-blok"><h2>{k}</h2><p>{t}</p></div>'
        for k, t in WIE["blokken"])

    if WIE.get("foto"):
        portret = (f'<figure class="wie-portret"><img src="../{WIE["foto"]}" '
                   f'width="640" height="800" alt="{WIE["foto_alt"]}" loading="lazy">'
                   f'</figure>')
    else:
        portret = (f'<div class="wie-portret leeg" aria-hidden="true">{MERKTEKEN}</div>')

    blokken = f"""<section class="sectie">
  <div class="wrap wie-grid">
    {portret}
    <div>
      <p class="eyebrow">{PERSOON["rol"]}</p>
      <h2 class="display">{WIE["kop"]}</h2>
      <p class="lede">{WIE["lede"]}</p>
      <p class="persoon-visie">{PERSOON["visie"]}</p>
      <p class="persoon-naam">{PERSOON["naam"]}<span>{PERSOON["rol"]}, {MERKNAAM} &middot; KvK {CONTACT["kvk"]}</span></p>
    </div>
  </div>
</section>
<section class="sectie band">
  <div class="wrap">
    <div class="wie-blokken">{blokken_html}</div>
  </div>
</section>
<section class="sectie">
  <div class="wrap sec-kop">
    <h2 class="display">Wat ik niet beweer.</h2>
    <p class="lede">{WIE["niet"]}</p>
    <p class="route-regel">Meer hierover: <a class="tekstlink" href="../werkwijze/">de werkwijze in vier stappen</a>, <a class="tekstlink" href="../werk/">wat er werkelijk is gebouwd</a> of <a class="tekstlink" href="../prijzen/">alle prijzen op één pagina</a>.</p>
  </div>
</section>"""

    persoon_ld = [{
        "@type": "AboutPage",
        "@id": DOMEIN + "/wie/#aboutpage",
        "url": DOMEIN + "/wie/",
        "mainEntity": {"@id": ID_PERSOON},
    }]
    return dienstpagina("wie", "", f"{PERSOON['naam']}, {PERSOON['rol'].lower()}",
                        f"{PERSOON['naam']} is oprichter en bouwer van {MERKNAAM}. "
                        "Wie belt of mailt, spreekt de persoon die het werk ook maakt.",
                        "Wie zit hierachter.",
                        f"{PERSOON['naam']}, oprichter en bouwer van {MERKNAAM}.",
                        blokken, kruimel="Over Björn", over=ID_PERSOON,
                        extra_ld=persoon_ld,
                        paginatitel=f"{PERSOON['naam']}, oprichter van {MERKNAAM}")


def bouw_privacy():
    """Feitelijk kloppend voor deze site. De tekst over de formulieren volgt
    de werkelijke verzendroute: zonder verzendsleutel opent het formulier
    WhatsApp of mail op het apparaat van de bezoeker, met sleutel gaat het via
    Web3Forms naar de mailbox. Beide worden hier eerlijk beschreven; wat er
    niet gebeurt, staat er ook niet."""
    if MAILT_DIRECT:
        verwerkt = ("<p>Alleen wat u zelf invult in het contact- of scanformulier: uw naam, "
                    "bedrijfsnaam, telefoonnummer of e-mailadres, het adres van uw website en "
                    "uw vraag en eventueel uw gekozen verbeterdoel. Daarnaast wordt meegestuurd vanaf welke pagina u het formulier "
                    "verstuurde, zodat duidelijk is waar uw vraag over gaat.</p>")
        daarna = ("<p>Het formulier verstuurt uw gegevens via de verzenddienst "
                  "<a class=\"tekstlink\" href=\"https://web3forms.com/privacy\" rel=\"noopener\">Web3Forms</a> "
                  "naar het e-mailpostvak van Capital BB. Web3Forms verwerkt het bericht alleen "
                  "om het af te leveren. Daarna staat uw bericht in het postvak van Capital BB "
                  "en wordt het gebruikt om uw vraag te beantwoorden. Uw gegevens worden niet "
                  "verkocht, niet gebruikt voor advertenties en niet gedeeld met andere "
                  "partijen dan de verzenddienst die nodig is om de mail te bezorgen.</p>"
                  "<p>Liever geen formulier? Bellen, appen of rechtstreeks mailen kan altijd; "
                  "die gegevens gaan dan alleen langs uw eigen telefoon- of mailaanbieder.</p>")
        bewaren = ("<h2>Hoe lang uw bericht bewaard blijft</h2>"
                   "<p>Uw bericht blijft in het mailpostvak van Capital BB staan zolang dat "
                   "nodig is om uw vraag af te handelen, en daarna zolang de administratie dat "
                   "vraagt. U kunt op elk moment vragen om verwijdering.</p>")
    else:
        verwerkt = ("<p>Alleen wat u zelf invult in het contact- of scanformulier: uw naam, "
                    "bedrijfsnaam, telefoonnummer of e-mailadres en uw vraag. Deze site slaat "
                    "die gegevens nergens op. Het formulier opent een WhatsApp- of "
                    "e-mailbericht op uw eigen apparaat; u ziet precies wat er wordt verstuurd "
                    "en u verstuurt het zelf.</p>")
        daarna = ("<p>Uw bericht komt binnen in de WhatsApp of het e-mailpostvak van Capital BB "
                  "en wordt gebruikt om uw vraag te beantwoorden. Uw gegevens worden niet "
                  "verkocht en niet gedeeld met derden, en niet gebruikt voor andere doelen dan "
                  "het contact waar u zelf om vroeg.</p>")
        bewaren = ""

    if METEN.get("ga4"):
        cookietekst = (
            "<h2>Cookies en meetsystemen</h2>"
            "<p>Deze site gebruikt Google Analytics om te zien welke pagina's worden gelezen "
            "en via welke route bezoekers binnenkomen. Daar horen cookies bij. Daarom wordt "
            "er eerst om toestemming gevraagd: <b>zolang u niets kiest of weigert, wordt "
            "Google Analytics niet geladen en wordt er niets gemeten</b>. De site werkt "
            "verder gewoon.</p>"
            "<p>Wat er bij toestemming wordt gemeten: welke pagina's u bekijkt, hoe lang, "
            "via welke website of zoekmachine u binnenkwam, en of u een formulier heeft "
            "verstuurd. Uw IP-adres wordt daarbij ingekort. Er worden geen advertentie- of "
            "profileringsfuncties gebruikt.</p>"
            "<p>Uw keuze wordt lokaal in uw eigen browser bewaard, niet in een cookie van "
            "ons. U kunt hem op elk moment wijzigen via <b>Cookievoorkeur wijzigen</b> "
            "onderaan elke pagina.</p>")
    else:
        cookietekst = (
            "<h2>Cookies en meetsystemen</h2>"
            "<p>Deze site plaatst geen cookies en gebruikt geen analytics of trackers. "
            "Daarom ziet u ook geen cookiemelding.</p>")

    blokken = f"""<section class="sectie">
  <div class="wrap privacy-tekst">
    <h2>Welke gegevens deze site verwerkt</h2>
    {verwerkt}
    <h2>Wat er daarna mee gebeurt</h2>
    {daarna}
    {bewaren}
    {cookietekst}
    <h2>Lettertypen</h2>
    <p>De lettertypen worden geladen via Google Fonts. Daarbij wordt uw IP-adres doorgegeven aan Google. Wilt u dat niet, dan werkt de site ook met de standaardletter van uw apparaat.</p>
    <h2>Uw rechten</h2>
    <p>U kunt altijd vragen welke gegevens van u bewaard zijn, en om correctie of verwijdering. Eén bericht naar <a class="tekstlink" href="mailto:{CONTACT["email"]}">{CONTACT["email"]}</a> is genoeg.</p>
  </div>
</section>"""
    return dienstpagina("privacy", "", "Privacyverklaring",
                        "Hoe Capital BB omgaat met uw gegevens: geen cookies, geen trackers, geen opslag op een server.",
                        "Privacyverklaring",
                        "Kort, want deze site verzamelt vrijwel niets.",
                        blokken,
                        # Wel bereikbaar en wel doorlinkend, maar geen zoekvraag
                        # om op te ranken. Daarom ook uit de sitemap.
                        robots="noindex, follow")


def bouw_404():
    h = kop_html("", f"Pagina niet gevonden | {MERKNAAM}",
                 "Deze pagina bestaat niet.", robots="noindex, follow")
    h = h.replace('<link rel="canonical" href="' + DOMEIN + '/">' + chr(10), "")
    h += nav_html("")
    h += f"""<main id="hoofd">
<header class="pagina-kop">
  <div class="wrap">
    <h1 class="display">Deze pagina bestaat niet.</h1>
    <p class="lede">Het adres klopt niet meer of heeft nooit bestaan. Wat u zoekt staat vrijwel zeker hieronder.</p>
    <div class="cta-acties" style="margin-top:28px">
      <a class="btn btn-gold" href="/">Naar de homepage</a>
      <a class="btn btn-ghost" href="/scan/">Website Performance Scan</a>
    </div>
  </div>
</header>
</main>
"""
    h += voet_html("")
    bestand = os.path.join(WORTEL, "404.html")
    io.open(bestand, "w", encoding="utf-8", newline="\n").write(h)
    return "404.html"


def bouw_contact():
    beschrijving = ("Neem contact op met Capital BB, Björn Beerntsen. Bellen, appen, mailen of "
                    "het formulier: u krijgt binnen één werkdag antwoord van een mens.")
    kruimels, stappen = kruimelpad("contact", "Contact")
    contact_ld = [{
        "@type": "ContactPage",
        "@id": DOMEIN + "/contact/#contactpage",
        "url": DOMEIN + "/contact/",
        "mainEntity": {"@id": ID_ORG},
    }]
    h = kop_html("contact", f"Contact opnemen met {MERKNAAM} | Björn Beerntsen", beschrijving,
                 pagina_ld("contact", "Contact", beschrijving, stappen=stappen,
                           extra=contact_ld))
    h += nav_html("contact")
    h += f"""<main id="hoofd">
<header class="pagina-kop">
  <div class="wrap">
    {kruimels}
    <h1 class="display">Vertel waar het wringt.</h1>
    <p class="lede">U krijgt binnen één werkdag antwoord van een mens, met iets tastbaars om over te praten.</p>
  </div>
</header>
<section class="sectie">
  <div class="wrap split split-boven">
    <div>
      <p class="onderteken">{PERSOON["naam"]}, {PERSOON["rol"].lower()} van {MERKNAAM}<br><span>Werkgebied heel Nederland · KvK {CONTACT["kvk"]}</span></p>
      <p class="persoon-kort">{PERSOON["tekst"]}</p>
      <div class="contact-direct" id="contact-direct"></div>
      <p class="cta-direct form-direct"><span>Liever appen dan een formulier invullen?</span> {wa_knop("mijn bedrijf", "Stuur een WhatsApp")}</p>
    </div>
    <form class="contactform" id="contactform" novalidate>
      <div class="veld"><label for="c-bedrijf">Bedrijfsnaam</label>
        <input id="c-bedrijf" type="text" autocomplete="organization" required></div>
      <div class="veld"><label for="c-naam">Uw naam</label>
        <input id="c-naam" type="text" autocomplete="name" required></div>
      <div class="veld"><label for="c-bereik">Telefoon of e-mail</label>
        <input id="c-bereik" type="text" autocomplete="tel" required>
        <p class="hint">Waar u het liefst bereikbaar bent.</p></div>
      <div class="veld"><label for="c-vraag">Wat speelt er?</label>
        <textarea id="c-vraag" rows="4"></textarea></div>
      {honeypot()}
      <p class="fout" id="c-fout" role="alert" hidden></p>
      <p class="succes" id="c-klaar" role="status" hidden>{SUCCES_CONTACT}</p>
      <button class="btn btn-gold" type="submit">Stuur het naar Björn</button>
      <p class="hint">{VERZENDNOOT}</p>
    </form>
  </div>
</section>
</main>
"""
    h += voet_html("contact")
    return schrijf("contact", h)


# ===========================================================================
# ROBOTS / SITEMAP / LLMS / CONFIG
# ===========================================================================
def bouw_randbestanden(paginas):
    # ---------------------------------------------------------------- robots
    # Eén user-agentgroep, geen tegenstrijdigheden, geen losse botregels.
    # Aparte groepen per crawler zijn hier niet nodig: alles mag alles lezen
    # behalve /_bron/, en dat geldt voor iedereen gelijk.
    #
    # LET OP: op productie zet Cloudflare hier een eigen "Managed robots.txt"
    # boven, met Content-Signals en Disallow-regels voor onder meer GPTBot,
    # ClaudeBot, Google-Extended, Applebot-Extended, Amazonbot, Bytespider,
    # CCBot en meta-externalagent. Die regels staan niet in deze repository en
    # zijn hier ook niet te overschrijven: een latere groep heft een eerdere
    # Disallow niet op. Wie AI-crawlers wél binnen wil laten, zet dat uit in
    # Cloudflare (AI Crawl Control / robots.txt-beheer). Zie LEES-DIT.md.
    io.open(os.path.join(WORTEL, "robots.txt"), "w", encoding="utf-8", newline="\n").write(
        "# Capital BB\n"
        "# Alles mag gelezen worden, ook door AI-crawlers. Dat is het hele punt:\n"
        "# wie gevonden wil worden in AI-antwoorden moet zich laten lezen.\n"
        "# Alleen de bouwbron blijft dicht; daar staat niets wat een bezoeker helpt.\n\n"
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /_bron/\n\n"
        f"Sitemap: {DOMEIN}/sitemap.xml\n")

    # --------------------------------------------------------------- sitemap
    # Alleen canonieke, indexeerbare pagina's die 200 geven. /privacy/ staat
    # er bewust niet in: die is noindex, follow. lastmod komt uit GEWIJZIGD,
    # dezelfde bron als dateModified in de structured data.
    regels = "".join(
        f"  <url><loc>{DOMEIN}/{(p + '/') if p else ''}</loc>"
        f"<lastmod>{GEWIJZIGD.get(p, GEWIJZIGD['*'])}</lastmod></url>\n"
        for p in paginas)
    io.open(os.path.join(WORTEL, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + regels + "</urlset>\n")

    # ------------------------------------------------------------- llms.txt
    diensten = "\n".join(
        f"- [{DIENSTEN[s][0]}]({DOMEIN}/{s}/) - {DIENSTEN[s][2]}"
        for s in DIENSTEN)
    koopvragen = "\n".join(
        f"- [{L['naam']}]({DOMEIN}/{s}/) - {L['vraag']}"
        for s, L in LANDING.items())
    hubs = "\n".join(
        f"- [{SPOREN[s]['titel']}]({DOMEIN}/{s}/) - {SPOREN[s]['sub']}"
        for s in SPOREN)

    io.open(os.path.join(WORTEL, "llms.txt"), "w", encoding="utf-8", newline="\n").write(f"""# {MERKNAAM}

> {MERKNAAM} bouwt websites en leadmachines, CRM- en bedrijfssystemen, Business OS,
> AI-medewerkers, AI-telefonie, workflowautomatisering en maatwerksoftware voor
> Nederlandse ondernemers, zzp'ers en mkb-bedrijven. Werkgebied: heel Nederland.
> Taal: Nederlands. Oprichter en bouwer: {PERSOON["naam"]}. KvK: {CONTACT["kvk"]}.

Laatste inhoudelijke update: {GEWIJZIGD["*"]}.

## Wat Capital BB is

Capital BB is een Nederlands digitaliseringsbedrijf. Het bouwt de systemen achter
een bedrijf: de website die aanvragen oplevert, het CRM waarin die aanvragen
landen, de AI-medewerker die opneemt als de ondernemer niet kan, en de
automatiseringen die het terugkerende werk overnemen. De onderdelen zijn los af
te nemen maar gebouwd om samen te werken.

Capital BB combineert marketing en social media met websites, CRM, AI en
opvolgsystemen. Ook na de verkoop: servicecontact, feedback en klantbehoud.
Er is één vaste identiteit op de site:
{DOMEIN}/#organization.

- Naam: {MERKNAAM}
- Oprichter en bouwer: {PERSOON["naam"]} ({DOMEIN}/#bjorn), zie {DOMEIN}/wie/
- KvK: {CONTACT["kvk"]}
- Werkgebied: heel Nederland, op afstand of op locatie
- Taal: Nederlands
- E-mail: {CONTACT["email"]}
- Telefoon: {CONTACT["telefoon"]}
- Website: {DOMEIN}/

## Diensten

{diensten}

## Verschil tussen CRM, bedrijfssysteem en Business OS

Dit onderscheid wordt vaak door elkaar gehaald; Capital BB hanteert het zo:

- **CRM**: gaat over klantcontact. Contacten, leads, offertes, afspraken,
  gespreksnotities en opvolgtaken op één plek. Vanaf 159 euro per maand plus 395
  euro inrichting.
- **Bedrijfssysteem**: digitaliseert één of meer interne processen, zoals
  planning, werkbonnen, dossiers of aanvragen. Niet primair klantcontact, maar
  hoe het werk door het bedrijf loopt. Vanaf 219 euro per maand plus 695 euro
  inrichting.
- **Business OS**: één omgeving voor het hele bedrijf. CRM, projecten, planning,
  medewerkers, documenten, rapportages en automatiseringen bij elkaar, in plaats
  van losse abonnementen die elkaars gegevens niet kennen. Vanaf 349 euro per
  maand plus 1.195 euro inrichting.

Vuistregel: gaat de vraag over klanten, dan CRM. Gaat hij over één proces, dan een
bedrijfssysteem. Moeten meerdere afdelingen in dezelfde omgeving werken, dan een
Business OS.

## Welk product hoort bij welke vraag

- Leads en klanten beheren: CRM
- Eén bedrijfsproces digitaliseren: bedrijfssysteem
- Meerdere processen verbinden: Business OS
- Terugkerend werk automatiseren: automatisering
- Telefoon en berichten laten afhandelen: AI-medewerker of AI-telefonie
- Meer aanvragen via internet: website en leadmachine
- Gevonden worden in Google en in AI-antwoorden: SEO en GEO

## Vanafprijzen (exclusief 21% btw)

Volledig overzicht: {DOMEIN}/prijzen/

- Websites: Basis 795, Premium 1.595, Signature 2.995, maatwerk vanaf 4.945 euro eenmalig
- Websites, betaling: 40% bij opdracht, 40% na ontwerpgoedkeuring, 20% voor livegang
- CRM: vanaf 159 euro per maand plus eenmalige inrichting vanaf 395 euro
- Bedrijfssystemen: vanaf 219 euro per maand plus inrichting vanaf 695 euro
- Business OS: vanaf 349 euro per maand plus inrichting vanaf 1.195 euro
- AI-medewerker en AI-telefonie: inrichting vanaf 750 euro, exclusief verbruik
- Hosting en techniek: 25 euro per maand; Onderhoud: 59 euro per maand; Actieve groei: 149 euro per maand
- Vindbaarheid (SEO en GEO): 149, 299 of 499 euro per maand
- Koppelingen: eenvoudig vanaf 295, standaard API vanaf 650, complex vanaf 1.250 euro
- Datamigratie vanaf 295 euro, extra dashboard vanaf 395 euro
- Extra ontwikkeling vanaf 65 euro per uur, na voorafgaand akkoord. Spoed 20% toeslag

{ABON_VOORWAARDEN}

## Werkwijze

1. De klant laat zien waar het wringt, via de scan, het formulier of een gesprek.
2. Capital BB bouwt eerst een werkend voorstel: een aanklikbaar concept, geen offerte.
3. Bevalt het voorstel niet, dan kost het niets. De volledige bouw start pas na
   akkoord, tegen de afgesproken prijs.
4. Het systeem groeit mee: van website naar CRM, AI-medewerker en automatisering.

Volledig: {DOMEIN}/werkwijze/

## Wat {MERKNAAM} bewust niet claimt

- Geen gegarandeerde zichtbaarheid in AI-systemen of in Google. Niemand heeft die
  in de hand.
- Geen resultaatpercentages, omzetstijgingen of conversiecijfers die niet
  aantoonbaar zijn.
- Geen valse schaarste, geen aflopende acties, geen laatste plekken.
- Geen klantnamen zonder toestemming van de eigenaar.
- Geen beloofd aantal aanvragen of leads.
- Branchevoorbeelden op de site zijn illustratief; het zijn geen klantnamen en
  geen gerealiseerde resultaten.

## Hubpagina's

{hubs}

## Veelgestelde koopvragen met een eigen pagina

{koopvragen}

## Bewijs en gebouwd werk

Overzicht: {DOMEIN}/werk/

- jezz-media.nl - live site, door Capital BB gebouwd voor een groeipartner van
  makelaars en hypotheekadviseurs. Vier diensten als één verhaal, met kennisbank,
  cases en veelgestelde vragen.
- Designsysteem IJsseldal - complete site van tien pagina's voor een zelfstandige
  hypotheekadviespraktijk in Oost-Nederland, geanonimiseerd getoond. Elke bewering
  nagetrokken tot de bron.
- Elf demosites voor kapsalons, barbershops, nagelstudio's en beautystudio's, elk
  met een eigen ontwerp en waar mogelijk een werkende koppeling met het
  boekingssysteem dat de zaak al gebruikt (onder meer Salonized, Knipklok,
  Altegio, Afspraakpro). Ongevraagd gebouwd als kennismaking, daarom zonder naam.

## Contact

- Telefoon en WhatsApp: {CONTACT["telefoon"]}
- E-mail: {CONTACT["email"]}
- Contactpagina: {DOMEIN}/contact/
- Kosteloze Website Performance Scan: {DOMEIN}/scan/
- Antwoord binnen één werkdag, van {PERSOON["naam"]} zelf.

## Over dit bestand

llms.txt is een hulpmiddel, geen rankingfactor. Het bestaat zodat AI-systemen de
feiten over Capital BB op één plek kunnen vinden in plaats van ze uit vijftien
pagina's te moeten afleiden. Prijzen en claims hier zijn gelijk aan die op de
website; wijkt iets af, dan is de website leidend.
""")

    # Sleutelbestand voor IndexNow. De zoekmachine haalt dit op om te
    # controleren of wij het domein beheren. Alleen schrijven als er een
    # sleutel is; een leeg bestand zou de verificatie juist laten falen.
    if INDEXNOW.get("sleutel"):
        io.open(os.path.join(WORTEL, INDEXNOW["sleutel"] + ".txt"), "w",
                encoding="utf-8", newline=chr(10)).write(INDEXNOW["sleutel"] + chr(10))

    # .nojekyll voorkomt Jekyll-verwerking; _bron blijft via robots.txt buiten beeld.
    io.open(os.path.join(WORTEL, ".nojekyll"), "w", encoding="utf-8").write("")
    io.open(os.path.join(WORTEL, "CNAME"), "w", encoding="utf-8").write(CONTACT["domein"] + chr(10))


# ===========================================================================
if __name__ == "__main__":
    gemaakt = [
        bouw_home(),
        bouw_spoor("meer-klanten"),
        bouw_spoor("slimmer-werken"),
        bouw_websites(),
        bouw_vindbaarheid(),
        bouw_marketing(),
        bouw_ai(),
        bouw_crm(),
        bouw_automatisering(),
        bouw_os(),
        bouw_scan(),
        bouw_werk(),
        bouw_werkwijze(),
        bouw_prijzen(),
        bouw_contact(),
        bouw_wie(),
        bouw_privacy(),
        bouw_404(),
    ] + [bouw_landing(s) for s in LANDING]
    paginas = ["", "meer-klanten", "slimmer-werken", "websites", "vindbaarheid",
               "online-marketing", "ai-medewerkers", "crm", "automatisering", "business-os",
               "scan", "werk", "werkwijze", "prijzen", "wie", "contact"] + list(LANDING)
    bouw_randbestanden(paginas)
    for g in gemaakt:
        print("geschreven:", g)
    print("plus robots.txt, sitemap.xml, llms.txt, .nojekyll")

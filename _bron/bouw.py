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
                    PERSOON, KEUZEHULP, FAQ, CTA_PER_PAGINA, VERWANT, CASE2)

WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMEIN = "https://" + CONTACT["domein"]

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


def kop_html(pad, titel, beschrijving, extra_head=""):
    canoniek = DOMEIN + "/" + (pad + "/" if pad else "")
    diep = "../" if pad else ""
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel}</title>
<meta name="description" content="{beschrijving}">
<meta name="robots" content="index, follow">
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
<body>
<a class="skip" href="#hoofd">Naar de inhoud</a>
"""


def nav_html(pad, actief=""):
    diep = "../" if pad else ""
    links = "".join(
        f'<a href="{diep}{slug}/"{" aria-current=" + chr(34) + "page" + chr(34) if slug == actief else ""}>{naam}</a>'
        for slug, naam in NAV
    )
    return f"""<nav class="nav" aria-label="Hoofdnavigatie">
  <a class="merk" href="{diep if pad else '#top'}" aria-label="{MERKNAAM}, naar de homepage">{MERKTEKEN}<span class="merk-woord">{MERKNAAM}</span></a>
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
    <div class="voet-kolom"><h2>Praktisch</h2>{praktisch}</div>
    <div class="voet-kolom"><h2>Contact</h2>{c}</div>
  </div>
</footer>
<script>window.CBB_CONTACT={{"telefoon":"{CONTACT["telefoon"]}","whatsapp":"{CONTACT["whatsapp"]}","email":"{CONTACT["email"]}"}};</script>
<script src="{diep}js/site.js?v={V_JS}"></script>
</body>
</html>"""


def prijsblok(items, kolommen=3, cta=True):
    """Prijskaarten. Elke rij eindigt standaard in een directe actie, want een
    prijs zonder volgende stap is een doodlopende gang."""
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
        uit.append('<div class="prijs-actie"><a class="btn btn-gold" href="../contact/">'
                   'Laat het bouwen</a><a class="tekstlink" href="../scan/">'
                   'Of start met de kosteloze scan</a></div>')
    return "".join(uit)


def cta_blok(pad, kop="Wij bouwen eerst een voorstel. U beslist daarna.",
             tekst="Laat achter wat u doet en waar het wringt. U krijgt iets echts te zien, geen verkooppraatje.",
             knop="Plan een kennismaking"):
    """Slotblok. De kop en de primaire knop volgen de intentie van de pagina
    (CTA_PER_PAGINA); de secundaire actie is overal de scan."""
    diep = "../" if pad else ""
    if pad in CTA_PER_PAGINA:
        kop, tekst, knop = CTA_PER_PAGINA[pad]
    return f"""<section class="sectie cta-slot">
  <div class="wrap cta-inhoud">
    <h2 class="display">{kop}</h2>
    <p class="lede">{tekst}</p>
    <div class="cta-acties">
      <a class="btn btn-gold" href="{diep}contact/">{knop}</a>
      <a class="btn btn-ghost" href="{diep}scan/">Start met de scan</a>
    </div>
  </div>
</section>"""


def kruimelpad(pad, titel, spoor=None):
    """Zichtbaar broodkruimelpad plus bijpassende BreadcrumbList."""
    stappen = [("Home", DOMEIN + "/")]
    if spoor and spoor in SPOREN:
        stappen.append((SPOREN[spoor]["titel"], f"{DOMEIN}/{spoor}/"))
    stappen.append((titel, f"{DOMEIN}/{pad}/"))
    zichtbaar = '<nav class="kruimels" aria-label="Kruimelpad">' + " ".join(
        (f'<a href="{u.replace(DOMEIN + "/", "../" if i < len(stappen) - 1 else "")}">{n}</a>'
         f'<span aria-hidden="true">/</span>') if i < len(stappen) - 1
        else f'<span aria-current="page">{n}</span>'
        for i, (n, u) in enumerate(stappen)) + "</nav>"
    # Home-link corrigeren: vanaf een subpagina is dat ../
    zichtbaar = zichtbaar.replace('href="../">Home', 'href="../">Home')
    import json as _json
    ld = ('<script type="application/ld+json">'
          + _json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList",
                         "itemListElement": [
                             {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                             for i, (n, u) in enumerate(stappen)]},
                        ensure_ascii=False)
          + "</script>")
    return zichtbaar, ld


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


def dienst_ld(naam, beschrijving, prijs, eenheid_maand=False):
    unit = '"unitCode": "MON", ' if eenheid_maand else ""
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "{naam}",
  "provider": {{ "@type": "ProfessionalService", "name": "{MERKNAAM}", "url": "{DOMEIN}/" }},
  "areaServed": {{ "@type": "Country", "name": "Nederland" }},
  "description": "{beschrijving}",
  "offers": {{ "@type": "Offer", "priceSpecification": {{ "@type": "UnitPriceSpecification",
    "price": "{prijs}", "priceCurrency": "EUR", {unit}"valueAddedTaxIncluded": false,
    "description": "Vanafprijs" }} }}
}}
</script>
"""


def schrijf(pad, html):
    doel = os.path.join(WORTEL, pad) if pad else WORTEL
    os.makedirs(doel, exist_ok=True)
    bestand = os.path.join(doel, "index.html")
    io.open(bestand, "w", encoding="utf-8", newline="\n").write(html)
    return os.path.relpath(bestand, WORTEL)


def dienstpagina(pad, actief_spoor, titel, beschrijving, hero_kop, hero_tekst,
                 blokken, ld=""):
    """Standaardopbouw van een dienstpagina, met kruimelpad en verwante routes."""
    spoor = actief_spoor if actief_spoor in SPOREN else None
    kruimels, kruimel_ld = kruimelpad(pad, titel, spoor)
    h = kop_html(pad, f"{titel} | {MERKNAAM}", beschrijving, ld + kruimel_ld + "\n")
    h += nav_html(pad, actief_spoor)
    h += f"""<main id="hoofd">
<header class="pagina-kop">
  <div class="wrap">
    {kruimels}
    <h1 class="display">{hero_kop}</h1>
    <p class="lede">{hero_tekst}</p>
  </div>
</header>
{blokken}
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
    ld = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "{DOMEIN}/#capitalbb",
  "name": "{MERKNAAM}",
  "url": "{DOMEIN}/",
  "image": "{DOMEIN}/img/og.png",
  "logo": "{DOMEIN}/img/icoon-180.png",
  "description": "Capital BB bouwt websites en leadmachines, CRM- en bedrijfssystemen, Business OS, AI-medewerkers, workflows en automatiseringen voor Nederlandse ondernemers.",
  "slogan": "{SLOGAN}",
  "inLanguage": "nl-NL",
  "telephone": "+31614664161",
  "email": "{CONTACT["email"]}",
  "identifier": {{ "@type": "PropertyValue", "propertyID": "KVK", "value": "{CONTACT["kvk"]}" }},
  "founder": {{ "@type": "Person", "name": "{PERSOON["naam"]}", "jobTitle": "{PERSOON["rol"]}" }},
  "areaServed": {{ "@type": "Country", "name": "Nederland" }},
  "knowsAbout": ["Websites en leadgeneratie", "CRM-systemen", "Bedrijfssystemen",
    "Business OS", "AI-medewerkers", "Workflowautomatisering",
    "Zoekmachineoptimalisatie", "Vindbaarheid in AI-systemen"]
}}
</script>
"""
    # FAQ: zichtbaar als uitklapbare vragen, plus FAQPage-data die er
    # letterlijk mee overeenkomt. Schema alleen waar de vragen echt staan.
    import json as _json
    faq_html = "".join(
        f'<details class="faq-item"><summary>{v}</summary><p>{a}</p></details>'
        for v, a in FAQ)
    ld += ('<script type="application/ld+json">'
           + _json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
                          "mainEntity": [
                              {"@type": "Question", "name": v,
                               "acceptedAnswer": {"@type": "Answer", "text": a}}
                              for v, a in FAQ]}, ensure_ascii=False)
           + "</script>\n")

    # Het stelsel: vijf onderdelen docken op een baan rond de kern (Business
    # OS), spaken verbinden ze, de buitenring sluit zich. De vorm echoot de
    # concentrische ringen van het CBB-merk. Alles in één SVG, dus niets kan
    # ooit buiten beeld vallen.
    import math
    HOEKEN = [-90, -18, 54, 126, 198]          # posities op de baan
    R_BAAN, R_KNOOP, R_KERN = 330, 84, 110
    knopen, spaken = "", ""
    for i, (hoek, naam) in enumerate(zip(HOEKEN, KETEN[:5])):
        rad = math.radians(hoek)
        x = 500 + R_BAAN * math.cos(rad)
        y = 500 + R_BAAN * math.sin(rad)
        dx = (x - 500) * 0.42
        dy = (y - 500) * 0.42
        # Label onder de knoop, behalve bovenaan: daar erboven, anders botst
        # hij met de kern.
        ly = y - R_KNOOP - 30 if hoek == -90 else y + R_KNOOP + 44
        knopen += (
            f'<g class="knoop k{i+1}" style="--dx:{dx:.0f}px;--dy:{dy:.0f}px">'
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{R_KNOOP}" class="ring-buiten"/>'
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{R_KNOOP - 18}" class="ring-binnen"/>'
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" class="kern-stip"/>'
            f'<text x="{x:.0f}" y="{ly:.0f}" class="knoop-label">{naam.upper()}</text></g>'
        )
        x1 = 500 + (R_KERN) * math.cos(rad);  y1 = 500 + (R_KERN) * math.sin(rad)
        x2 = 500 + (R_BAAN - R_KNOOP) * math.cos(rad)
        y2 = 500 + (R_BAAN - R_KNOOP) * math.sin(rad)
        spaken += (f'<line class="spaak s{i+1}" x1="{x1:.0f}" y1="{y1:.0f}" '
                   f'x2="{x2:.0f}" y2="{y2:.0f}"/>')
    # De blauwdruk: dezelfde geometrie, vaag en gestippeld, altijd zichtbaar.
    # Zo is het scherm bij binnenkomst al gevuld met het plan; het scrollen
    # bouwt het plan vol.
    blauwdruk = f'<circle class="bd" cx="500" cy="500" r="{R_BAAN}"/>'
    for hoek in HOEKEN:
        rad = math.radians(hoek)
        bx = 500 + R_BAAN * math.cos(rad)
        by = 500 + R_BAAN * math.sin(rad)
        blauwdruk += (f'<circle class="bd" cx="{bx:.0f}" cy="{by:.0f}" r="{R_KNOOP}"/>'
                      f'<circle class="bd-stip" cx="{bx:.0f}" cy="{by:.0f}" r="5"/>')
    blauwdruk += f'<circle class="bd" cx="500" cy="500" r="{R_KERN}"/>'

    stelsel = f"""<svg class="stelsel" viewBox="0 0 1000 1000" aria-hidden="true" focusable="false">
        <g class="blauwdruk">{blauwdruk}</g>
        <circle class="baan" cx="500" cy="500" r="{R_BAAN}"/>
        {spaken}
        {knopen}
        <g class="kern">
          <circle cx="500" cy="500" r="{R_KERN}" class="ring-buiten"/>
          <circle cx="500" cy="500" r="{R_KERN - 16}" class="ring-binnen"/>
          <text x="500" y="509" class="kern-label">{KETEN[5].upper()}</text>
        </g>
      </svg>"""
    ketting = " ".join(KETEN)

    sporen = ""
    for slug, sp in SPOREN.items():
        subs = "".join(
            f'<a class="spoor-sub" href="{d}/"><b>{t}</b><span>{u}</span></a>'
            for d, t, u in sp["links"]
        )
        sporen += (f'<div class="spoor"><a class="spoor-kop" href="{slug}/">'
                   f'<h3>{sp["titel"]}</h3><p>{sp["sub"]}</p><span class="spoor-pijl">Bekijk dit spoor</span></a>'
                   f'<div class="spoor-subs">{subs}</div></div>')

    niet = "".join(f'<div class="creed-item"><h3>{k}</h3><p>{t}</p></div>' for k, t in NIET_DOEN)
    case_punten = "".join(f"<li>{p}</li>" for p in CASE["punten"])

    h = kop_html("", f"{MERKNAAM}, {SLOGAN.lower()}",
                 "Capital BB bouwt websites, CRM- en bedrijfssystemen, AI-medewerkers en automatiseringen "
                 "die samen één systeem vormen. Werkgebied heel Nederland.", ld)
    h += nav_html("")
    h += f"""<main id="hoofd">

<!-- FILMISCHE HERO. Zes onderdelen komen tijdens het scrollen uit de diepte
     en verbinden zich tot één systeem. Scrollgestuurd waar de browser dat
     kan (CSS scroll-driven animations); anders speelt de opbouw vanzelf. -->
<section class="film" id="top">
  <div class="film-plak">
    <div class="film-licht" aria-hidden="true"></div>

    <div class="film-stage" aria-hidden="true">
      <div class="montage" id="montage">
        {stelsel}
      </div>
    </div>

    <div class="film-copy">
      <div class="wrap">
        <div class="merk-regel">{MERKTEKEN}<span>{MERKNAAM}</span></div>
        <h1 class="display">Uw bedrijf draait straks<br>op één systeem.</h1>
        <p class="lede">Website, CRM, AI-medewerkers en automatisering, gebouwd als één geheel. Niet als losse abonnementen die elkaar niet kennen.</p>
        <div class="cta-acties">
          <a class="btn btn-gold" href="scan/">Start de Website Performance Scan</a>
          <a class="btn btn-ghost" href="werk/">Bekijk het werk</a>
        </div>
      </div>
    </div>
  </div>
  <p class="vh">De onderdelen {ketting} verbinden zich tot één systeem.</p>
</section>

<!-- WAT WIJ BOUWEN -->
<section class="sectie">
  <div class="wrap">
    <div class="sec-kop">
      <h2 class="display">Geen webbureau.<br>Een digitaliseringspartner.</h2>
      <p class="lede">Een website is bij ons het beginpunt van een keten: bezoekers worden leads, leads landen in het CRM, de AI-medewerker neemt op als u niet kunt, en de workflows doen het terugkerende werk. Elk onderdeel is los af te nemen, maar ze zijn gebouwd om samen te werken.</p>
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
      <h2 class="display">{CASE["kop"]}</h2>
      <p class="lede">Een complete site voor een {CASE["naam"].lower()} in {CASE["regio"]}, gebouwd op het eigen {CASE["pakket"]}.</p>
      <ul class="ticks">{case_punten}</ul>
      <a class="btn btn-ghost" href="werk/">Meer over dit werk</a>
    </div>
    <div class="case-beeld" aria-hidden="true">
      <div class="case-mini">
        <div class="cm-nav"><span></span><i></i><i></i><i></i></div>
        <div class="cm-kop">{CASE["kop"]}</div>
        <div class="cm-band"></div>
        <div class="cm-rij"><span></span><span></span><span></span></div>
      </div>
    </div>
  </div>
</section>

<!-- SCAN-TEASER -->
<section class="sectie scan-teaser">
  <div class="wrap scan-grid">
    <div>
      <h2 class="display">Website Performance Scan</h2>
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
<section class="sectie persoon-sectie">
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
        f'<span class="kaart-pijl">Bekijken</span></a>'
        for d, t, u in sp["links"]
    )
    blokken = f"""<section class="sectie">
  <div class="wrap">
    <div class="dienstkaarten">{kaarten}</div>
    <p class="ander-spoor">Zoekt u het andere: <a class="tekstlink" href="../{ander}/">{SPOREN[ander]["titel"].lower()}</a>?</p>
  </div>
</section>"""
    return dienstpagina(slug, slug, sp["titel"],
                        sp["sub"] + " Capital BB bouwt de systemen die daarbij horen.",
                        sp["titel"] + ".", sp["sub"], blokken)


# ===========================================================================
# DIENSTPAGINA'S
# ===========================================================================
def bouw_websites():
    blokken = f"""<section class="sectie">
  <div class="wrap">
    <h2 class="display">Vier niveaus, één lat.</h2>
    <p class="lede">Elke site, ook de kleinste, wordt gecontroleerd op mobiel gedrag, contrast, laadgewicht en vindbaarheid voordat hij live gaat. Alle bedragen exclusief btw.</p>
    {prijsblok(PRIJS_WEB, 4)}
    <p class="voetnoot">Betaling in drie delen: 40% bij opdracht, 40% na goedkeuring van het ontwerp en 20% voor livegang.</p>
  </div>
</section>
<section class="sectie band">
  <div class="wrap">
    <h2 class="display">En daarna wordt hij onderhouden.</h2>
    <p class="lede">Een site die niemand bijhoudt, veroudert. Drie niveaus, per maand, exclusief btw.</p>
    {prijsblok(PRIJS_ONDERHOUD, cta=False)}
  </div>
</section>"""
    return dienstpagina("websites", "meer-klanten", "Websites en leadmachines",
                        "Websites die bezoekers omzetten in aanvragen en afspraken. Vanaf 795 euro, exclusief btw.",
                        "Een website die werk oplevert.<br>Niet alleen bestaat.",
                        "Gebouwd om bezoekers om te zetten in aanvragen en afspraken, en gecontroleerd tot de laatste pagina.",
                        blokken,
                        dienst_ld("Website en leadmachine",
                                  "Websites die bezoekers omzetten in aanvragen en afspraken.", "795"))


def bouw_vindbaarheid():
    blokken = f"""<section class="sectie">
  <div class="wrap">
    <h2 class="display">Twee zoekplekken, één aanpak.</h2>
    <p class="lede">Uw klant zoekt in Google, en steeds vaker stelt hij zijn vraag aan een AI-assistent. Wij bouwen voor allebei: techniek, lokale zichtbaarheid en inhoud die citeerbaar is. Per maand, exclusief btw.</p>
    {prijsblok(PRIJS_ZICHT)}
    <p class="eerlijk">Zichtbaarheid in AI-systemen verkopen wij niet als garantie. Wij bouwen wat het aantoonbaar mogelijk maakt: citeerbare antwoorden, kloppende bedrijfsgegevens, structured data, reviews en inhoudelijke autoriteit. Wie u een vaste plek in AI-antwoorden belooft, verkoopt iets wat hij niet in de hand heeft.</p>
  </div>
</section>"""
    return dienstpagina("vindbaarheid", "meer-klanten", "Vindbaarheid, SEO en GEO",
                        "Zichtbaarheid in Google en in AI-assistenten. Vanaf 149 euro per maand, exclusief btw.",
                        "Gevonden worden, ook waar<br>uw klant nu écht zoekt.",
                        "In de zoekmachine, en in de AI-assistenten die steeds vaker het eerste antwoord geven.",
                        blokken,
                        dienst_ld("Vindbaarheid, SEO en GEO",
                                  "Zichtbaarheid in zoekmachines en AI-assistenten.", "149", True))


def bouw_ai():
    blokken = f"""<section class="sectie">
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
<section class="sectie band">
  <div class="wrap">
    <h2 class="display">Wat het kost.</h2>
    <p class="lede">Inrichting vanaf <b class="goudcijfer">&euro;750</b>, exclusief verbruikskosten voor telefonie en AI. Het verbruik wordt apart doorbelast, zodat u ziet waar het geld heen gaat. Gekoppeld aan een CRM-abonnement wordt de AI-medewerker onderdeel van het systeem in plaats van een losse tool.</p>
  </div>
</section>"""
    return dienstpagina("ai-medewerkers", "meer-klanten", "AI-medewerkers",
                        "Een digitale medewerker die telefoon, WhatsApp en e-mail beantwoordt en afspraken inplant. Vanaf 750 euro.",
                        "Een medewerker die altijd opneemt.",
                        "Beantwoordt vragen, plant afspraken in en geeft door wat hij niet zelf mag beslissen.",
                        blokken,
                        dienst_ld("AI-medewerker",
                                  "Digitale medewerker voor telefoon, WhatsApp, chat en e-mail.", "750"))


def bouw_crm():
    blokken = f"""<section class="sectie">
  <div class="wrap">
    <h2 class="display">Drie niveaus.</h2>
    <p class="lede">Als abonnement met eenmalige inrichting. Per maand, exclusief btw.</p>
    {prijsblok(PRIJS_CRM)}
    <p class="voetnoot">{ABON_VOORWAARDEN}</p>
  </div>
</section>"""
    return dienstpagina("crm", "slimmer-werken", "CRM",
                        "Klanten, offertes, opdrachten en opvolging op één plek. Vanaf 159 euro per maand, exclusief btw.",
                        "Eén plek voor elke klant.<br>In plaats van vier lijstjes.",
                        "Contacten, offertes, afspraken en opvolgtaken in één systeem dat met uw website en AI-medewerker praat.",
                        blokken,
                        dienst_ld("CRM", "Klantcontact, leads en verkoop op één plek.", "159", True))


def bouw_automatisering():
    blokken = f"""<section class="sectie">
  <div class="wrap">
    <h2 class="display">Bedrijfssystemen.</h2>
    <p class="lede">Digitaliseren wat nu in Excel, WhatsApp en een map op de server tegelijk leeft: planning, werkbonnen, dossiers, aanvragen. Per maand, exclusief btw.</p>
    {prijsblok(PRIJS_SYS)}
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
                        "Workflows en bedrijfssystemen die terugkerend werk overnemen. Vanaf 219 euro per maand, exclusief btw.",
                        "Wat u elke week opnieuw typt,<br>hoort één keer ingericht.",
                        "Bevestigingen, herinneringen, facturen en reviewverzoeken gaan vanzelf de deur uit. Processen krijgen een systeem.",
                        blokken,
                        dienst_ld("Automatisering en bedrijfssystemen",
                                  "Workflows en bedrijfssystemen voor interne processen.", "219", True))


def bouw_os():
    blokken = f"""<section class="sectie">
  <div class="wrap">
    <h2 class="display">Drie niveaus.</h2>
    <p class="lede">Het hele bedrijf vanuit één omgeving: CRM, projecten, planning, medewerkers, documenten, rapportages en automatiseringen. Per maand, exclusief btw.</p>
    {prijsblok(PRIJS_OS)}
    <p class="voetnoot">{ABON_VOORWAARDEN} Externe licenties en verbruik van AI, sms en e-mail worden apart doorbelast.</p>
  </div>
</section>"""
    return dienstpagina("business-os", "slimmer-werken", "Business OS",
                        "Het hele bedrijf vanuit één omgeving. Vanaf 349 euro per maand, exclusief btw.",
                        "Zeven losse abonnementen eruit.<br>Eén omgeving erin.",
                        "CRM, projecten, planning, documenten en automatisering in één systeem dat het hele bedrijf aanstuurt.",
                        blokken,
                        dienst_ld("Business OS",
                                  "Het hele bedrijf vanuit één centrale omgeving.", "349", True))


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

    h = kop_html("scan", f"Website Performance Scan | {MERKNAAM}",
                 "Laat uw website analyseren op conversie, techniek, vindbaarheid en groeikansen. "
                 f"{totaal} controlepunten, beoordeeld door een mens, binnen één werkdag.")
    h += nav_html("scan")
    h += f"""<main id="hoofd">
<header class="pagina-kop">
  <div class="wrap">
    <p class="eyebrow">Kosteloos, binnen één werkdag</p>
    <h1 class="display">Website Performance Scan</h1>
    <p class="lede">Laat uw website analyseren op conversie, techniek, vindbaarheid en groeikansen. {totaal} controlepunten, beoordeeld door een mens die er werkelijk doorheen gaat.</p>
  </div>
</header>

<section class="sectie">
  <div class="wrap">
    <form class="scanform" id="scanform" novalidate>
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
        <input id="s-bereik" type="text" autocomplete="tel" required>
        <p class="hint">Daar krijgt u het resultaat op.</p>
      </div>
      <p class="fout" id="s-fout" role="alert" hidden></p>
      <p class="succes" id="s-klaar" role="status" hidden>Uw aanvraag staat klaar in WhatsApp of uw mailprogramma. Verstuur hem daar, dan gaat de scan lopen. Komt er niets in beeld? Bel of app direct naar {CONTACT["telefoon"]}.</p>
      <button class="btn btn-gold" type="submit">Vraag de scan aan</button>
      <p class="hint">Kosteloos, u zit nergens aan vast, en u hoeft niets technisch aan te leveren: het adres van uw site is genoeg.</p>
    </form>
  </div>
</section>

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
      <p class="eerlijk">Er wordt niets gemeten terwijl u hier wacht. Een pagina in uw browser mag andere websites niet uitlezen; de scan draait bij ons, en er kijkt een mens naar voordat u iets krijgt.</p>
    </aside>
  </div>
</section>
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
    blokken = f"""<section class="sectie">
  <div class="wrap case-grid">
    <div>
      <p class="eyebrow">{CASE["pakket"]}</p>
      <h2 class="display">{CASE["kop"]}</h2>
      <div class="case-poi">
        <div><h3>Probleem</h3><p>Een {CASE["naam"].lower()} in {CASE["regio"]} zonder eigen website: klanten vinden de adviseur alleen via het profiel van een landelijk netwerk, zonder eigen verhaal, eigen vindbaarheid of eigen aanvraagroute.</p></div>
        <div><h3>Oplossing</h3><p>Een complete site van tien pagina's op een eigen designsysteem dat de blauwwitte huisstijl van de branche bewust vermijdt, met werkwijze, tarieven en veelgestelde vragen. Elke bewering op de site is nagetrokken tot de bron en met controledatum vastgelegd.</p></div>
        <div><h3>Impact</h3><p>De adviseur heeft een eigen plek waar bezoekers rechtstreeks een gesprek kunnen aanvragen, met inhoud die klopt en gecontroleerd is op contrast, mobiel gedrag, laadgewicht en toegankelijkheid.</p></div>
      </div>
    </div>
    <div class="case-beeld" aria-hidden="true">
      <div class="case-mini">
        <div class="cm-nav"><span></span><i></i><i></i><i></i></div>
        <div class="cm-kop">{CASE["kop"]}</div>
        <div class="cm-band"></div>
        <div class="cm-rij"><span></span><span></span><span></span></div>
      </div>
    </div>
  </div>
</section>
<section class="sectie band">
  <div class="wrap">
    <p class="eyebrow">Eigen werk als bewijs</p>
    <h2 class="display">{CASE2["kop"]}</h2>
    <div class="case-poi kolommen">
      <div><h3>Probleem</h3><p>{CASE2["probleem"]}</p></div>
      <div><h3>Oplossing</h3><p>{CASE2["oplossing"]}</p></div>
      <div><h3>Impact</h3><ul class="ticks">{impact2}</ul></div>
    </div>
  </div>
</section>
<section class="sectie">
  <div class="wrap">
    <h2 class="display">Waarom hier geen logowand staat.</h2>
    <p class="lede">Wij tonen alleen werk waarvoor de eigenaar toestemming gaf, en namen alleen mét die toestemming. Liever twee cases die kloppen dan tien logo's die niets bewijzen. Dit overzicht groeit met het werk mee.</p>
  </div>
</section>"""
    return dienstpagina("werk", "werk", "Werk",
                        "Gebouwd werk van Capital BB, met per project wat er werkelijk is opgeleverd.",
                        "Werk dat er echt staat.",
                        "Geen opgepoetste portfolio-tegels, maar wat er werkelijk is gebouwd en hoe.",
                        blokken)


def bouw_werkwijze():
    niet = "".join(f'<div class="creed-item"><h3>{k}</h3><p>{t}</p></div>' for k, t in NIET_DOEN)
    blokken = f"""<section class="sectie">
  <div class="wrap">
    <div class="stappen">
      <div class="stap"><span class="stapnr">1</span><h2>U laat zien waar het wringt</h2>
        <p>Via de scan, het contactformulier of een gesprek. Wat kost tijd, wat loopt mis, wat blijft liggen.</p></div>
      <div class="stap"><span class="stapnr">2</span><h2>Wij bouwen eerst een voorstel</h2>
        <p>Geen offerte van zes kantjes, maar een werkend concept dat u kunt aanklikken en beoordelen. Een voorstel, nog niet het volledige systeem.</p></div>
      <div class="stap"><span class="stapnr">3</span><h2>U beslist met iets tastbaars</h2>
        <p>Bevalt het voorstel niet, dan kost het u niets. Bevalt het wel, dan starten de volledige bouw en inrichting na uw akkoord, tegen de afgesproken prijs.</p></div>
      <div class="stap"><span class="stapnr">4</span><h2>Het systeem groeit mee</h2>
        <p>Wat als website begint, kan doorgroeien naar CRM, AI-medewerker en automatisering. In dat tempo beslist u.</p></div>
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
                        "Eerst bouwen, dan beslissen. Zo werkt Capital BB.",
                        "Eerst bouwen.<br>Dan beslissen.",
                        "De meeste bureaus laten u praten voordat u iets ziet. Wij draaien dat om.",
                        blokken)


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
    <h2 class="display">Websites</h2>
    <p class="lede">Eenmalig, exclusief btw. Betaling in drie delen: 40% bij opdracht, 40% na ontwerpgoedkeuring, 20% voor livegang.</p>
    {prijsblok(PRIJS_WEB, 4, cta=False)}
  </div>
</section>
<section class="sectie band">
  <div class="wrap">
    <h2 class="display">CRM</h2>
    {prijsblok(PRIJS_CRM, cta=False)}
    <h2 class="display ruimte">Bedrijfssystemen</h2>
    {prijsblok(PRIJS_SYS, cta=False)}
    <h2 class="display ruimte">Business OS</h2>
    {prijsblok(PRIJS_OS, cta=False)}
    <p class="voetnoot">{ABON_VOORWAARDEN}</p>
  </div>
</section>
<section class="sectie">
  <div class="wrap">
    <h2 class="display">Doorlopend</h2>
    <p class="lede">Onderhoud en zichtbaarheid, per maand, exclusief btw.</p>
    {prijsblok(PRIJS_ONDERHOUD, cta=False)}
    {prijsblok(PRIJS_ZICHT)}
    <p class="voetnoot">AI-assistent vanaf &euro;750 inrichting, exclusief verbruik. Koppelingen vanaf &euro;295. Extra ontwikkeling vanaf &euro;65 per uur, na voorafgaand akkoord. Spoed 20% toeslag.</p>
  </div>
</section>"""
    return dienstpagina("prijzen", "prijzen", "Prijzen",
                        "Alle vanafprijzen van Capital BB op één pagina, exclusief btw.",
                        "Alle prijzen.<br>Op één pagina.",
                        "Vanafprijzen, exclusief 21% btw. Wat u kiest bepaalt de prijs, niet hoe het gesprek loopt.",
                        blokken)


def bouw_privacy():
    """Feitelijk kloppend voor deze site: geen cookies, geen analytics, geen
    opslag op een server. Formulieren openen WhatsApp of e-mail op het
    apparaat van de bezoeker zelf."""
    blokken = f"""<section class="sectie">
  <div class="wrap privacy-tekst">
    <h2>Welke gegevens deze site verwerkt</h2>
    <p>Alleen wat u zelf invult in het contact- of scanformulier: uw naam, bedrijfsnaam, telefoonnummer of e-mailadres en uw vraag. Deze site slaat die gegevens nergens op. Het formulier opent een WhatsApp- of e-mailbericht op uw eigen apparaat; u ziet precies wat er wordt verstuurd en u verstuurt het zelf.</p>
    <h2>Wat er daarna mee gebeurt</h2>
    <p>Uw bericht komt binnen in de WhatsApp of het e-mailpostvak van Capital BB en wordt gebruikt om uw vraag te beantwoorden. Uw gegevens worden niet verkocht en niet gedeeld met derden, en niet gebruikt voor andere doelen dan het contact waar u zelf om vroeg.</p>
    <h2>Cookies en meetsystemen</h2>
    <p>Deze site plaatst geen cookies en gebruikt geen analytics of trackers. Daarom ziet u ook geen cookiemelding.</p>
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
                        blokken)


def bouw_404():
    h = kop_html("", f"Pagina niet gevonden | {MERKNAAM}",
                 "Deze pagina bestaat niet.")
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
    h = kop_html("contact", f"Contact | {MERKNAAM}",
                 "Neem contact op met Capital BB. U krijgt binnen één werkdag antwoord van een mens.")
    h += nav_html("contact")
    h += f"""<main id="hoofd">
<header class="pagina-kop">
  <div class="wrap">
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
      <p class="fout" id="c-fout" role="alert" hidden></p>
      <p class="succes" id="c-klaar" role="status" hidden>Uw bericht staat klaar in WhatsApp of uw mailprogramma. Verstuur hem daar, dan leest Björn hem vandaag nog. Komt er niets in beeld? Bel direct naar {CONTACT["telefoon"]}.</p>
      <button class="btn btn-gold" type="submit">Stuur het naar Björn</button>
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
    io.open(os.path.join(WORTEL, "robots.txt"), "w", encoding="utf-8", newline="\n").write(
        "# Capital BB\n"
        "# Alles mag gelezen worden, ook door AI-crawlers. Dat is het hele punt:\n"
        "# wie gevonden wil worden in AI-antwoorden moet zich laten lezen.\n\n"
        "User-agent: *\nAllow: /\nDisallow: /_bron/\n\n"
        f"Sitemap: {DOMEIN}/sitemap.xml\n")

    regels = "".join(
        f"  <url><loc>{DOMEIN}/{(p + '/') if p else ''}</loc><lastmod>2026-08-21</lastmod></url>\n"
        for p in paginas)
    io.open(os.path.join(WORTEL, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + regels + "</urlset>\n")

    lijst = "\n".join(
        f"- [{n}]({DOMEIN}/{s}/)" for s, n in VOET_DIENSTEN + VOET_PRAKTISCH)
    io.open(os.path.join(WORTEL, "llms.txt"), "w", encoding="utf-8", newline="\n").write(f"""# {MERKNAAM}

> {MERKNAAM} bouwt websites en leadmachines, CRM- en bedrijfssystemen, Business OS,
> AI-medewerkers, workflows en automatiseringen voor Nederlandse ondernemers.
> Werkgebied: heel Nederland. Taal: Nederlands. Eigenaar: Björn.

Capital BB is een Nederlands digitaliseringsbedrijf dat websites, CRM-systemen,
AI-medewerkers, automatiseringen en Business OS-oplossingen ontwikkelt voor
bedrijven. Oprichter en bouwer: {PERSOON["naam"]}. KvK: {CONTACT["kvk"]}.

De onderdelen zijn los af te nemen maar gebouwd om samen te werken:
website, leads, CRM, AI-medewerkers, automatisering, Business OS.
De werkwijze: eerst een werkend voorstel bouwen, daarna pas beslissen.
Bevalt het voorstel niet, dan kost het niets; de volledige bouw start pas
na akkoord, tegen de afgesproken prijs.

## Welk product hoort bij welke vraag

- Leads en klanten beheren: CRM
- Eén bedrijfsproces digitaliseren: bedrijfssysteem
- Meerdere processen verbinden: Business OS
- Terugkerend werk automatiseren: automatisering
- Telefoon en berichten laten afhandelen: AI-medewerker
- Meer aanvragen via internet: website en leadmachine

## Vanafprijzen (exclusief 21% btw)

- Websites: Basis 795, Premium 1.595, Signature 2.995, maatwerk vanaf 4.945 euro eenmalig
- CRM: vanaf 159 euro per maand plus eenmalige inrichting vanaf 395 euro
- Bedrijfssystemen: vanaf 219 euro per maand plus inrichting vanaf 695 euro
- Business OS: vanaf 349 euro per maand plus inrichting vanaf 1.195 euro
- AI-medewerker: inrichting vanaf 750 euro, exclusief verbruik
- Onderhoud: 39, 79 of 149 euro per maand
- Vindbaarheid (SEO en GEO): 149, 299 of 499 euro per maand

{ABON_VOORWAARDEN}

## Wat {MERKNAAM} niet claimt

- Geen gegarandeerde zichtbaarheid in AI-systemen of Google
- Geen resultaatpercentages die niet aantoonbaar zijn
- Geen valse schaarste of aflopende acties

## Pagina's

{lijst}
""")

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
        bouw_ai(),
        bouw_crm(),
        bouw_automatisering(),
        bouw_os(),
        bouw_scan(),
        bouw_werk(),
        bouw_werkwijze(),
        bouw_prijzen(),
        bouw_contact(),
        bouw_privacy(),
        bouw_404(),
    ]
    paginas = ["", "meer-klanten", "slimmer-werken", "websites", "vindbaarheid",
               "ai-medewerkers", "crm", "automatisering", "business-os", "scan",
               "werk", "werkwijze", "prijzen", "contact", "privacy"]
    bouw_randbestanden(paginas)
    for g in gemaakt:
        print("geschreven:", g)
    print("plus robots.txt, sitemap.xml, llms.txt, .nojekyll")

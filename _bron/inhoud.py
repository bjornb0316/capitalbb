# -*- coding: utf-8 -*-
"""
Alle inhoud van de Capital BB-site staat in dit ene bestand.
Tekst wijzigen: hier aanpassen en daarna `python _bron/bouw.py` draaien.
De map _bron wordt door GitHub Pages genegeerd (naam begint met _).
"""

# ---------------------------------------------------------------------------
# CONTACT. VUL IN VOOR LIVEGANG. Lege velden = knoppen tonen een nette melding.
# whatsapp: internationaal, zonder plus en spaties, bijv. "31612345678"
# ---------------------------------------------------------------------------
CONTACT = {
    "telefoon": "06 14664161",
    "whatsapp": "31614664161",
    "email": "bjorn@capitalbb.nl",
    "domein": "capitalbb.nl",
    "kvk": "98747460",
}

# ---------------------------------------------------------------------------
# FORMULIERVERZENDING. VUL DE SLEUTEL IN OM ECHT TE GAAN MAILEN.
#
# Deze site draait op GitHub Pages en heeft dus geen eigen server. Om een
# formulier werkelijk als e-mail te laten aankomen is een externe verzenddienst
# nodig. Gekozen: Web3Forms.
#
# Zo kom je aan de sleutel:
#   1. Ga naar https://web3forms.com
#   2. Vul bjorn@capitalbb.nl in en klik op "Create Access Key"
#   3. Je krijgt de sleutel per mail. Geen account, geen wachtwoord.
#   4. Plak hem hieronder bij "sleutel" en draai `python _bron/bouw.py`
#
# Zolang "sleutel" leeg is, blijven de formulieren zich gedragen zoals ze
# altijd deden: ze openen WhatsApp of het mailprogramma met alles er al in.
# Er gaat dus nooit iets stuk; het wordt alleen beter zodra de sleutel er is.
#
# Let op: met een ingevulde sleutel gaan de ingevulde gegevens via Web3Forms
# naar de mailbox. De privacyverklaring past zich daar automatisch op aan.
# ---------------------------------------------------------------------------
FORMULIER = {
    "dienst": "web3forms",
    "sleutel": "204feaf1-f5db-4820-ad75-664004003919",
    # Waar de mail heen gaat. Leeg = het adres dat aan de sleutel hangt.
    "ontvanger": "",
    # Wat er gebeurt zolang er geen sleutel is, en waar het formulier op
    # terugvalt als het versturen mislukt: "email" of "whatsapp".
    # Staat op e-mail, want inzendingen horen in de mailbox te landen.
    "terugval": "email",
}

# ---------------------------------------------------------------------------
# METEN. VUL HET MEET-ID IN OM STATISTIEKEN AAN TE ZETTEN.
#
# "ga4" is het meet-ID van Google Analytics 4, in de vorm G-XXXXXXXXXX.
# Aanmaken op https://analytics.google.com: property maken voor capitalbb.nl,
# dan Beheer > Gegevensstromen > Web. Het ID staat rechtsboven.
#
# Zolang dit leeg is, wordt er niets geladen en verschijnt er geen
# cookiebanner. De privacyverklaring past zich daar automatisch op aan.
#
# LET OP: Google Analytics plaatst cookies. Daarom geldt met een ingevuld ID:
#   - er verschijnt een cookiebanner
#   - Analytics laadt pas NA toestemming, nooit ervoor
#   - weigeren is net zo makkelijk als accepteren
#   - de keuze is later te wijzigen via de link in de voettekst
# Dat is geen extra service maar wat de wet vereist. Zet het dus niet uit.
# ---------------------------------------------------------------------------
METEN = {
    "ga4": "G-ENESN5G33J",
}

# ---------------------------------------------------------------------------
# INDEXNOW. Meldt gewijzigde pagina's aan bij Bing, en daarmee bij Copilot.
# Google doet hier niet aan mee; daar blijft de sitemap de weg.
#
# Sleutel maken: verzin 8 tot 128 letters en cijfers, of genereer er een op
# https://www.bing.com/indexnow . Zet hem hieronder en draai de bouw; die
# schrijft <sleutel>.txt in de site, want de zoekmachine controleert daarmee
# of u de eigenaar van het domein bent.
#
# Deze sleutel is per ontwerp openbaar en is geen wachtwoord. Gebruik hem
# nergens anders voor. Zolang hij leeg is gebeurt er niets.
# ---------------------------------------------------------------------------
INDEXNOW = {
    "sleutel": "7e5ab4fb476a4c774ab2db1ca098504e",
}

MERKNAAM = "Capital BB"
SLOGAN = "Wij bouwen het systeem achter uw bedrijf"

# De keten die de hero vertelt en die op meer plekken terugkomt.
KETEN = ["Website", "Leads", "CRM", "AI-medewerkers", "Automatisering", "Business OS"]

# ---------------------------------------------------------------------------
# NAVIGATIE
# ---------------------------------------------------------------------------
NAV = [
    ("meer-klanten", "Meer klanten"),
    ("slimmer-werken", "Slimmer werken"),
    ("werk", "Werk"),
    ("prijzen", "Prijzen"),
    ("werkwijze", "Werkwijze"),
]
NAV_CTA = ("scan", "Website Performance Scan")

# Voettekst: dienstlinks (vindbaarheid) + praktisch.
VOET_DIENSTEN = [
    ("websites", "Websites en leadmachines"),
    ("vindbaarheid", "Vindbaarheid, SEO en GEO"),
    ("online-marketing", "Online marketing"),
    ("ai-medewerkers", "AI-medewerkers"),
    ("crm", "CRM"),
    ("automatisering", "Automatisering en bedrijfssystemen"),
    ("business-os", "Business OS"),
]
VOET_PRAKTISCH = [
    ("scan", "Website Performance Scan"),
    ("werk", "Werk"),
    ("prijzen", "Prijzen"),
    ("werkwijze", "Werkwijze"),
    ("wie", "Over Björn"),
    ("contact", "Contact"),
    ("privacy", "Privacyverklaring"),
]

# ---------------------------------------------------------------------------
# PRIJZEN (excl. 21% btw). Bron: prijslijsten Capital BB, websiteprijzen
# bijgewerkt 20 augustus 2026.
# ---------------------------------------------------------------------------
PRIJS_WEB = [
    ("Basis", "795", "eenmalig, vanaf",
     "Tot vijf pagina's, responsive, contactformulier, technische SEO-basis, één correctieronde."),
    ("Premium", "1.595", "eenmalig, vanaf",
     "Tot tien pagina's, maatwerk in homepage en secties, conversiegerichte opbouw, lokale SEO-basis, analytics, twee correctierondes.", True),
    ("Signature", "2.995", "eenmalig, vanaf",
     "Tot vijftien pagina's, uitgesproken maatwerkdesign, merkverhaal, geavanceerdere interacties, drie correctierondes."),
    ("Maatwerk", "4.945", "eenmalig, vanaf",
     "Eigen functionaliteit, koppelingen en een ontwerp dat nergens anders staat."),
]
PRIJS_CRM = [
    ("CRM Start", "159", "p/m, plus 395 eenmalig",
     "Contacten, leads, eenvoudige pipeline, taken en herinneringen. Tot vijf gebruikers."),
    ("CRM Groei", "269", "p/m, plus 695 eenmalig",
     "Offertes, automatische opvolging, rapportages, één koppeling, rollen en rechten. Tot vijftien gebruikers.", True),
    ("CRM Pro", "495", "p/m, plus 1.250 eenmalig",
     "Klantportaal, meerdere pipelines, autorisaties, meerdere koppelingen, maatwerkdashboards. Tot 35 gebruikers."),
]
PRIJS_SYS = [
    ("Start", "219", "p/m, plus 695 eenmalig",
     "Digitaliseert één duidelijk proces: planning, aanvragen, dossiers of werkbonnen."),
    ("Groei", "379", "p/m, plus 1.195 eenmalig",
     "Verbindt meerdere processen, met documenten, automatiseringen en rapportages.", True),
    ("Pro", "699", "p/m, plus 2.250 eenmalig",
     "Compleet intern platform met afdelingen, geavanceerde rechten en externe koppelingen."),
]
PRIJS_OS = [
    ("OS Start", "349", "p/m, plus 1.195 eenmalig",
     "CRM, taken, basisplanning en een centraal dashboard in één omgeving."),
    ("OS Groei", "649", "p/m, plus 1.995 eenmalig",
     "Plus projecten, medewerkers, documenten, workflows en automatiseringen.", True),
    ("OS Signature", "1.095", "p/m, plus 3.495 eenmalig",
     "Klantportaal, AI-functies, maatwerkautomatisering en uitgebreide koppelingen."),
]
PRIJS_ZICHT = [
    ("Basiscontrole", "149", "per maand", "Technische controle, rapportage en kleine optimalisaties."),
    ("Lokale groei", "299", "per maand", "Lokale SEO, bedrijfsprofiel, contentupdate en zichtbaarheid.", True),
    ("Actieve zichtbaarheid", "499", "per maand", "Doorlopende content, landingspagina's, autoriteit en GEO-monitoring."),
]
PRIJS_ONDERHOUD = [
    ("Hosting en techniek", "39", "per maand", "Hosting, monitoring, beveiliging, back-ups en updates."),
    ("Beheer", "79", "per maand", "Alles uit Hosting en techniek, plus kleine wijzigingen.", True),
    ("Actieve groei", "149", "per maand", "Alles uit Beheer, plus maandelijkse verbetering en prioriteit."),
]
ABON_VOORWAARDEN = ("Systemen hebben een minimale looptijd van 24 maanden en zijn daarna maandelijks "
                    "opzegbaar. Bij jaarlijkse betaling geldt 8% korting. U blijft altijd eigenaar van uw "
                    "eigen gegevens en kunt het systeem na de looptijd overnemen tegen zes maandtermijnen.")

# ---------------------------------------------------------------------------
# DE SCAN (17 punten uit het Ai Website Audit OS)
# ---------------------------------------------------------------------------
SCAN_GROEPEN = [
    ("Wat de bezoeker meemaakt", [
        "Gedrag op een telefoon, van 320 pixels breed tot tablet",
        "Visuele kwaliteit en of de site vertrouwen wekt",
        "Of binnen enkele seconden duidelijk is wat u doet en voor wie",
        "Navigatie en of iemand vindt wat hij zoekt",
        "Leesbaarheid en toegankelijkheid",
    ]),
    ("Of er iets binnenkomt", [
        "Bereikbaarheid: telefoon, formulier en afspraak maken",
        "Of de knoppen doen wat ze beloven",
        "Conversiegerichtheid van de opbouw",
        "Kansen voor opvolging, CRM en automatisering",
    ]),
    ("Of u gevonden wordt", [
        "Titels, beschrijvingen, koppen en indexeerbaarheid",
        "Lokale vindbaarheid en zoekintentie",
        "Vindbaarheid in AI-systemen en heldere bedrijfsgegevens",
        "Structured data en of uw gegevens kloppen",
    ]),
    ("Techniek en vertrouwen", [
        "Snelheid en de technische basis, voor zover meetbaar",
        "Beveiliging, privacy en cookiesignalen",
        "Actualiteit van teksten, team en contactgegevens",
        "Waarin u zich onderscheidt van uw concurrenten",
    ]),
]

# ---------------------------------------------------------------------------
# WAT WIJ NIET DOEN (uit de eigen werkregels)
# ---------------------------------------------------------------------------
NIET_DOEN = [
    ("Geen verzonnen cijfers",
     "Wij zetten geen percentages op een pagina die wij niet kunnen aantonen. Een ondernemer prikt daar doorheen, en terecht."),
    ("Geen valse schaarste",
     "Geen aflopende klok, geen laatste plek, geen actie die volgende week toevallig weer terug is."),
    ("Geen garanties die niemand kan geven",
     "Wij beloven geen vaste plek in Google of in AI-antwoorden. Wij bouwen wat de kans aantoonbaar vergroot."),
    ("Geen offerte als u eerst wilt zien",
     "Wij bouwen liever eerst iets echts. Daarna beslist u, met iets tastbaars voor u."),
]

# ---------------------------------------------------------------------------
# DE TWEE SPOREN
# ---------------------------------------------------------------------------
SPOREN = {
    "meer-klanten": {
        "titel": "Ik wil meer klanten",
        "sub": "Gevonden worden, bezoekers omzetten in aanvragen, en niets meer mislopen.",
        "links": [
            ("websites", "Website en leadmachine", "Een site die bezoekers omzet in aanvragen en afspraken."),
            ("vindbaarheid", "Gevonden worden", "In Google, en in de AI-assistenten waar klanten hun vraag stellen."),
            ("online-marketing", "Vraag aanjagen", "Advertenties, social media en e-mail die bezoekers naar u toe brengen."),
            ("ai-medewerkers", "Niets meer mislopen", "De telefoon wordt opgenomen, ook als u niet kunt."),
        ],
    },
    "slimmer-werken": {
        "titel": "Ik wil slimmer werken",
        "sub": "Overzicht over klanten en opdrachten, minder handwerk, één omgeving.",
        "links": [
            ("crm", "Overzicht over klanten", "Elke klant, offerte en opvolgtaak op één plek."),
            ("automatisering", "Minder handwerk", "Wat u elke week opnieuw typt, één keer inrichten."),
            ("business-os", "Alles in één omgeving", "Het hele bedrijf vanuit één systeem aansturen."),
        ],
    },
}

# ---------------------------------------------------------------------------
# CASE (geanonimiseerd, met toestemming van Bjorn: geen naam)
# ---------------------------------------------------------------------------
CASE = {
    "naam": "Zelfstandig hypotheekadviespraktijk",
    "regio": "Oost-Nederland",
    "pakket": "Designsysteem IJsseldal",
    "kop": "Het hele aanbod, niet één bank",
    "punten": [
        "Elke zin op de site nagetrokken tot de bron, met controledatum vastgelegd",
        "Eigen designsysteem dat de blauwwitte huisstijl van de branche bewust vermijdt",
        "Tien pagina's, waaronder werkwijze, tarieven en veelgestelde vragen",
        "Gecontroleerd op contrast, mobiel gedrag, laadgewicht en toegankelijkheid",
    ],
}


# ---------------------------------------------------------------------------
# DE PERSOON ACHTER CAPITAL BB. Alleen feiten; er is geen foto-asset, dus
# geen foto tot Bjorn er een aanlevert.
# ---------------------------------------------------------------------------
PERSOON = {
    "naam": "Björn Beerntsen",
    "rol": "Oprichter en bouwer",
    "tekst": ("Capital BB is het bedrijf van Björn Beerntsen. Wie belt, appt of het "
              "formulier invult, spreekt met de persoon die ook daadwerkelijk bouwt. "
              "Geen accountmanager ertussen, geen overdracht naar een team dat het "
              "gesprek niet heeft gevoerd."),
    "visie": ("Capital BB bestaat omdat de meeste bedrijven geen losse website, los "
              "CRM of losse AI-tool nodig hebben, maar één systeem waarin die "
              "onderdelen met elkaar praten. Dat systeem hoort te beginnen bij wat "
              "het bedrijf nodig heeft, niet bij wat er toevallig te verkopen valt."),
}

# ---------------------------------------------------------------------------
# DE PAGINA OVER BJORN. Alleen wat waar is en te controleren valt.
# "foto" blijft leeg tot er een echte foto is; er komt geen gegenereerd
# portret op de site, want een verzonnen gezicht bij een echt persoon is
# precies het soort ding waar deze site zich van probeert te onderscheiden.
# ---------------------------------------------------------------------------
WIE = {
    "foto": "",
    "foto_alt": "",
    "kop": "U spreekt met de bouwer.",
    "lede": ("Capital BB is geen bureau met accountmanagers. Wie belt, appt of het formulier "
             "invult, krijgt de persoon aan de lijn die het werk ook maakt."),
    "blokken": [
        ("Waarom dat uitmaakt",
         "Bij de meeste bureaus voert de een het gesprek en bouwt de ander. Wat u vertelt, "
         "moet dan worden doorgegeven, en onderweg gaat de helft van de nuance verloren. "
         "Hier zit die stap er niet tussen. Dat scheelt tijd, en het scheelt vooral "
         "misverstanden over wat u eigenlijk nodig had."),
        ("Wat ik doe",
         "Ik bouw de systemen achter een bedrijf: de website die aanvragen oplevert, het CRM "
         "waarin die aanvragen landen, de AI-medewerker die opneemt als u niet kunt, en de "
         "automatiseringen die het terugkerende werk overnemen. Los af te nemen, maar "
         "gebouwd om samen te werken."),
        ("Hoe ik werk",
         "Eerst bouwen, dan pas beslissen. U krijgt een werkend voorstel te zien voordat u "
         "iets uitgeeft. Bevalt het niet, dan kost het u niets. Ik werk liever met iets "
         "tastbaars dan met een offerte van zes kantjes waar niemand zich iets bij "
         "voorstelt."),
        ("Waar ik op let",
         "Elke bewering op een site die ik bouw moet ergens op slaan. Prijzen staan open, "
         "claims worden nagetrokken, en wat ik niet kan waarmaken zet ik er niet op. Dat is "
         "geen bescheidenheid maar eigenbelang: een ondernemer prikt door opgeklopte taal "
         "heen, en dan bent u uw geloofwaardigheid kwijt op het moment dat u hem nodig heeft."),
    ],
    "niet": ("Ik noem mezelf geen expert, geen marktleider en geen specialist in van alles. "
             "Capital BB is een klein bedrijf dat goed werk levert aan ondernemers die een "
             "systeem nodig hebben. Wat ik niet kan, zeg ik, en dan kijken we of iemand "
             "anders het beter kan."),
}

# ---------------------------------------------------------------------------
# KEUZEHULP. Welke vraag hoort bij welk product.
# ---------------------------------------------------------------------------
KEUZEHULP = [
    ("Leads en klanten beheren", "crm", "CRM"),
    ("Eén bedrijfsproces digitaliseren", "automatisering", "Bedrijfssysteem"),
    ("Meerdere processen verbinden", "business-os", "Business OS"),
    ("Terugkerend werk automatiseren", "automatisering", "Automatisering"),
    ("Telefoon en berichten laten afhandelen", "ai-medewerkers", "AI-medewerker"),
    ("Meer aanvragen via internet", "websites", "Website en leadmachine"),
    ("Adverteren en social media uitbesteden", "online-marketing", "Online marketing"),
]

# ---------------------------------------------------------------------------
# FAQ voor de homepage. Antwoorden alleen uit projectfeiten.
# ---------------------------------------------------------------------------
FAQ = [
    ("Wat kost een website bij Capital BB?",
     "Vanaf 795 euro exclusief btw voor het Basis-pakket, tot maatwerk vanaf 4.945 euro. "
     "Alle vanafprijzen staan open op de prijzenpagina; wat u kiest bepaalt de prijs."),
    ("Moet ik technische kennis hebben?",
     "Nee. U vertelt wat er in uw bedrijf wringt, in gewone taal. De techniek is ons werk, "
     "en u krijgt uitleg zonder vakjargon."),
    ("Wat betekent 'wij bouwen het eerst' precies?",
     "U krijgt eerst een werkend voorstel te zien: een concept dat laat zien hoe uw site of "
     "systeem eruit kan zien. Bevalt dat niet, dan kost het u niets. De volledige bouw en "
     "inrichting starten pas na uw akkoord, tegen de afgesproken prijs."),
    ("Werkt Capital BB in heel Nederland?",
     "Ja. Gesprekken kunnen op afstand of op locatie; de systemen zelf draaien online."),
    ("Kan ik klein beginnen?",
     "Ja, en dat is zelfs de bedoeling. Een website is een gebruikelijk beginpunt; CRM, "
     "AI-medewerkers en automatisering kunnen daarna aanhaken, in uw eigen tempo."),
]

# ---------------------------------------------------------------------------
# CTA per pagina-intentie.
# (kop, tekst, primaire knoptekst, primair doel, secundaire tekst, secundair doel)
#
# Waarom niet overal dezelfde twee knoppen: iemand op /crm/ wil zijn
# klantproces zien, niet zijn website laten scannen. De scan blijft de
# primaire actie waar hij past (websites en vindbaarheid) en zakt elders naar
# de tweede plaats of verdwijnt ten gunste van iets relevanters.
#
# Doelen zijn relatief vanaf de hoofdmap. "?over=" geeft de dienst mee aan het
# contactformulier, dat daarmee het vraagveld alvast invult; de bezoeker ziet
# en verstuurt dat zelf, de bezorging verandert niet.
# ---------------------------------------------------------------------------
CTA_PER_PAGINA = {
    # /websites/ is de overzichtspagina: wat er mogelijk is en hoe het werkt.
    # De koopvraag "wat kost het en hoe loopt het" hoort op
    # /website-laten-maken/, en die pagina heeft daarom een eigen CTA. Twee
    # pagina's met dezelfde slotvraag zouden elkaar in de weg zitten.
    "websites": (
        "Benieuwd wat er voor uw bedrijf mogelijk is?",
        "Vertel wat u verkoopt en aan wie. Wij laten zien welke opzet daarbij past, wat "
        "er gekoppeld kan worden en wat dat ongeveer kost.",
        "Bespreek uw situatie", "contact/?over=websites",
        "Of laat eerst uw huidige site beoordelen", "scan/"),
    "online-marketing": (
        "Laat één kanaal doorrekenen.",
        "Vertel wat een gemiddelde opdracht u oplevert. Daar rekenen wij mee door welk "
        "budget zin heeft, en of adverteren in uw geval überhaupt de snelste route is.",
        "Laat uw cijfers doorrekenen", "contact/?over=online-marketing",
        "Of bekijk SEO en GEO", "vindbaarheid/"),
    "vindbaarheid": (
        "Ontvang een nulmeting voor SEO en GEO.",
        "Waar staat u nu in Google, wat blokkeert er technisch, en wat zeggen "
        "AI-systemen op dit moment over uw bedrijf.",
        "Vraag de nulmeting aan", "scan/",
        "Of bespreek uw vindbaarheid", "contact/?over=vindbaarheid"),
    "ai-medewerkers": (
        "Laat \u00e9\u00e9n gemiste oproep uitwerken.",
        "Noem een gesprek dat u deze week miste. Wij laten zien wat een "
        "AI-medewerker daarin had gedaan, tot en met de afspraak in de agenda.",
        "Leg \u00e9\u00e9n gemiste oproep voor", "contact/?over=ai-medewerkers",
        "Of bekijk wat het kost", "prijzen/"),
    "crm": (
        "Bekijk uw klantproces in een CRM-demo.",
        "Vertel hoe een klant nu bij u binnenkomt en wordt opgevolgd. U krijgt "
        "een ingerichte omgeving te zien met uw eigen fases, voordat u beslist.",
        "Plan een CRM-demo", "contact/?over=crm",
        "Of bekijk de CRM-prijzen", "prijzen/"),
    "automatisering": (
        "Laat \u00e9\u00e9n terugkerend proces analyseren.",
        "Noem het werk dat elke week terugkomt. Wij rekenen op uw eigen aantallen "
        "door wat het nu kost en wat ervan te automatiseren valt.",
        "Leg \u00e9\u00e9n proces voor", "contact/?over=automatisering",
        "Of bekijk gebouwd werk", "werk/"),
    "business-os": (
        "Breng uw losse systemen in kaart.",
        "Welke pakketten gebruikt u, wat kosten ze samen, en welke gegevens staan "
        "er nu dubbel. Daar begint elk Business OS mee.",
        "Breng uw systemen in kaart", "contact/?over=business-os",
        "Of bekijk de Business OS-prijzen", "prijzen/"),
    "prijzen": (
        "Ontdek welke opzet bij uw bedrijf past.",
        "De vanafprijzen staan hierboven. Welke opzet u nodig heeft, hangt af van "
        "uw omvang, uw proces en wat u al draaien heeft.",
        "Leg uw situatie voor", "contact/?over=prijzen",
        "Of lees eerst de werkwijze", "werkwijze/"),
    "werk": (
        "Bekijk hoe dit voor uw bedrijf kan werken.",
        "Wat hierboven staat is gebouwd voor andere bedrijven. Vertel wat er bij u "
        "speelt, dan bouwen wij eerst een voorstel dat op uw situatie slaat.",
        "Bespreek uw situatie", "contact/?over=werk",
        "Of laat uw huidige site beoordelen", "scan/"),
    "werkwijze": (
        "Begin bij stap \u00e9\u00e9n: laten zien waar het wringt.",
        "Geen offerte van zes kantjes, maar een werkend voorstel dat u kunt "
        "aanklikken. Bevalt het niet, dan kost het u niets.",
        "Plan een kennismaking", "contact/?over=werkwijze",
        "Of start met de kosteloze scan", "scan/"),
    "meer-klanten": (
        "Waar lekt het nu weg?",
        "Meestal is het \u00e9\u00e9n van drie dingen: u wordt niet gevonden, bezoekers "
        "haken af, of de telefoon gaat over terwijl niemand kan opnemen.",
        "Laat uw huidige website beoordelen", "scan/",
        "Of leg uw situatie voor", "contact/?over=meer-klanten"),
    "slimmer-werken": (
        "Welk werk komt bij u elke week terug?",
        "Noem \u00e9\u00e9n proces dat te veel tijd kost of te vaak misgaat. Daar begint het, "
        "niet bij een plan om alles tegelijk te digitaliseren.",
        "Leg \u00e9\u00e9n proces voor", "contact/?over=slimmer-werken",
        "Of bekijk alle prijzen", "prijzen/"),
}

# Wat het contactformulier invult als een CTA een dienst meegeeft via ?over=.
# Vaste lijst: er komt nooit tekst uit de URL zelf in het formulier.
INTENTIES = {
    "websites": "Ik wil het hebben over een nieuwe website of leadmachine.",
    "vindbaarheid": "Ik wil het hebben over vindbaarheid in Google en in AI-systemen.",
    "online-marketing": "Ik wil het hebben over online marketing: adverteren, social media of e-mail.",
    "ai-medewerkers": "Ik wil het hebben over een AI-medewerker die de telefoon opneemt.",
    "crm": "Ik wil het hebben over een CRM voor onze klanten en opvolging.",
    "automatisering": "Ik wil het hebben over het automatiseren van terugkerend werk.",
    "business-os": "Ik wil het hebben over \u00e9\u00e9n omgeving voor het hele bedrijf.",
    "prijzen": "Ik wil weten welke opzet bij ons bedrijf past.",
    "werk": "Ik zag het gebouwde werk en wil weten wat dat voor ons kan betekenen.",
    "werkwijze": "Ik wil een kennismaking plannen.",
    "meer-klanten": "Ik wil meer klanten binnenkrijgen via internet.",
    "slimmer-werken": "Ik wil slimmer werken en minder handwerk.",
    "scan": "Ik wil mijn website laten beoordelen.",
}

# ---------------------------------------------------------------------------
# Verwante pagina's per dienst, voor interne routes.
# ---------------------------------------------------------------------------
VERWANT = {
    "websites":       [("vindbaarheid", "gevonden worden"), ("scan", "de kosteloze scan"), ("crm", "een CRM erachter")],
    "vindbaarheid":   [("websites", "een website die converteert"), ("online-marketing", "adverteren om het te overbruggen"), ("scan", "de kosteloze scan")],
    "online-marketing": [("vindbaarheid", "vindbaarheid die blijft"), ("websites", "de pagina waar de campagne op uitkomt"), ("crm", "een CRM dat de aanvraag opvolgt")],
    "ai-medewerkers": [("crm", "een CRM waarin gesprekken landen"), ("automatisering", "automatisering eromheen")],
    "crm":            [("ai-medewerkers", "AI-medewerkers"), ("business-os", "een volledig Business OS")],
    "automatisering": [("crm", "een CRM"), ("business-os", "een Business OS"), ("ai-medewerkers", "AI-medewerkers")],
    "business-os":    [("crm", "los beginnen met CRM"), ("automatisering", "losse automatisering")],
}

# ---------------------------------------------------------------------------
# Tweede case: de eigen leadmachine. Feitelijk: gebouwde demosites met echte
# boekingskoppelingen, als acquisitie voor Capital BB zelf.
# ---------------------------------------------------------------------------
CASE2 = {
    "naam": "De eigen leadmachine",
    "kop": "Elf demosites met live boekingssystemen",
    "probleem": ("Kapsalons, nagelstudio's en barbershops zonder eigen website zijn niet te "
                 "overtuigen met een offerte: die willen eerst iets zien."),
    "oplossing": ("Voor elf van zulke bedrijven bouwde Capital BB ongevraagd een complete "
                  "demonstratiewebsite, elk met een eigen ontwerp en waar mogelijk een werkende "
                  "koppeling met het boekingssysteem dat de zaak al gebruikt, waaronder "
                  "Salonized, Knipklok en Altegio."),
    "impact": [
        "Elke demo toont echte openingstijden, echte diensten en een echte boekingsflow",
        "Geen gedeelde sjablonen: elk ontwerp is op de zaak zelf gemaakt",
        "De aanpak is dezelfde die Capital BB voor klanten inzet: eerst bouwen, dan beslissen",
    ],
}


# ---------------------------------------------------------------------------
# Case met naam: jezz-media.nl. Live en verifieerbaar. Bewust omschreven als
# "gebouwd door Capital BB", zonder de klantrelatie te labelen: het merk is
# van dezelfde oprichter en de site voert een eigen gezicht. Feiten over de
# inhoud komen van de live site zelf (gecontroleerd 21 augustus 2026).
# ---------------------------------------------------------------------------
CASE_JEZZ = {
    "naam": "Jezz-Media",
    "url": "https://jezz-media.nl",
    "kop": "De site achter een groeipartner voor financiële dienstverleners",
    "probleem": ("Jezz-Media is een groeipartner voor makelaars, hypotheekadviseurs "
                 "en andere financiële dienstverleners: magazines, websites, CRM met "
                 "AI en vindbaarheid uit één hand. Dat verhaal vraagt om een site die "
                 "die samenhang ook echt laat zien, in plaats van vier losse "
                 "productpagina's."),
    "oplossing": ("Capital BB bouwde jezz-media.nl: één doorlopend verhaal waarin de "
                  "diensten in elkaar grijpen, met een kennisbank, cases, "
                  "veelgestelde vragen en een duidelijke gespreksroute. De opzet is "
                  "gebouwd om mee te groeien nu Jezz-Media naar nieuwe doelgroepen "
                  "en magazinetitels uitbreidt."),
    "impact": [
        "Vier diensten die als één verhaal worden verteld in plaats van als losse producten",
        "Een kennisbank en cases die de site inhoudelijk laten groeien",
        "Een structuur die nieuwe doelgroepen aankan zonder verbouwing",
        "Live te bekijken op jezz-media.nl",
    ],
}

# ---------------------------------------------------------------------------
# Geanonimiseerd werkoverzicht: gebouwde demosites, zonder naam of merk.
# (branche en plaats, bijzonderheid)
# ---------------------------------------------------------------------------
DEMOS = [
    ("Barbershop, Didam", "Zeskoppig team, gekoppeld aan Knipklok"),
    ("Kapsalon, Zevenaar", "Echte prijslijst en openingstijden, gekoppeld aan Knipklok"),
    ("Nagelstudio, Doetinchem", "Avondstudio, gekoppeld aan Salonized"),
    ("Barbershop, Zutphen", "Bewust zónder planner: de zaak werkt zonder afspraak"),
    ("Kapsalon, Zevenaar", "Zaak sinds 2008, gekoppeld aan Afspraakpro"),
    ("Barbershop, Zutphen", "Gekoppeld aan Knipklok, met live openingsstatus"),
    ("Kapsalon, Winterswijk", "Eigen afsprakenplanner op het echte weekrooster"),
    ("Beautystudio", "Gekoppeld aan Altegio"),
]

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
# KEUZEHULP. Welke vraag hoort bij welk product.
# ---------------------------------------------------------------------------
KEUZEHULP = [
    ("Leads en klanten beheren", "crm", "CRM"),
    ("Eén bedrijfsproces digitaliseren", "automatisering", "Bedrijfssysteem"),
    ("Meerdere processen verbinden", "business-os", "Business OS"),
    ("Terugkerend werk automatiseren", "automatisering", "Automatisering"),
    ("Telefoon en berichten laten afhandelen", "ai-medewerkers", "AI-medewerker"),
    ("Meer aanvragen via internet", "websites", "Website en leadmachine"),
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
# CTA per pagina-intentie. (kop, tekst, primaire knoptekst, primaire link)
# De secundaire actie is overal de scan.
# ---------------------------------------------------------------------------
CTA_PER_PAGINA = {
    "websites":       ("Benieuwd wat uw website kan opleveren?",
                       "Laat uw huidige site kosteloos beoordelen, of bespreek direct wat een nieuwe kan doen.",
                       "Bespreek uw website"),
    "vindbaarheid":   ("Weten waar u nu kansen laat liggen?",
                       "De scan laat zien waar uw vindbaarheid staat, in Google én in AI-antwoorden.",
                       "Bespreek uw vindbaarheid"),
    "ai-medewerkers": ("Benieuwd wat een AI-medewerker bij u zou doen?",
                       "Vertel hoe uw telefoon en berichten nu lopen, dan laten wij zien wat er over te nemen valt.",
                       "Bespreek een toepassing"),
    "crm":            ("Zien hoe uw klanten in één systeem passen?",
                       "Vertel hoe u nu klanten en offertes bijhoudt, dan laten wij zien hoe dat in één omgeving past.",
                       "Plan een demo"),
    "automatisering": ("Welk handwerk mag als eerste weg?",
                       "Noem het werk dat elke week terugkomt, dan laten wij zien wat er te automatiseren valt.",
                       "Bespreek uw processen"),
    "business-os":    ("Ontdekken wat één omgeving voor uw bedrijf betekent?",
                       "Vertel welke systemen en lijstjes er nu naast elkaar leven, dan laten wij zien hoe dat samenkomt.",
                       "Ontdek de mogelijkheden"),
}

# ---------------------------------------------------------------------------
# Verwante pagina's per dienst, voor interne routes.
# ---------------------------------------------------------------------------
VERWANT = {
    "websites":       [("vindbaarheid", "gevonden worden"), ("scan", "de kosteloze scan"), ("crm", "een CRM erachter")],
    "vindbaarheid":   [("websites", "een website die converteert"), ("scan", "de kosteloze scan")],
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

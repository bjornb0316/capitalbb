# -*- coding: utf-8 -*-
"""
Zoekintentiekaart: welke pagina welke vraag beantwoordt, en welke pagina's
elkaar niet in de weg mogen zitten.

Waarom dit bestaat: /websites/ en /website-laten-maken/ groeiden naar elkaar
toe. Allebei noemden ze prijzen, allebei eindigden ze in dezelfde CTA. Twee
pagina's die hetzelfde beantwoorden verdelen hun eigen zichtbaarheid en laten
een bezoeker raden waar hij moet zijn.

_bron/controle.py leest dit bestand en faalt als twee pagina's dezelfde
primaire intentie claimen, of als pagina's die hier als "botst_niet_met"
staan toch bijna dezelfde H1, introductie of CTA-kop krijgen.

Velden per URL:
  intentie      de primaire zoekintentie, in gewone taal
  termen        secundaire termen die bij dezelfde intentie horen
  doelgroep     voor wie deze pagina is
  fase          orientatie | overweging | koopintentie | bestaande klant
  vraag         de unieke vraag die deze pagina beantwoordt
  cta           de primaire actie
  steunt        pagina's die hiernaartoe linken of hierop aansluiten
  botst_niet_met  pagina's waarmee inhoudelijke overlap verboden is
"""

ZOEKINTENTIE = {

"": {
 "intentie": "Wie is Capital BB en wat bouwen ze",
 "termen": ["capital bb", "digitaliseringsbedrijf", "systeem achter uw bedrijf"],
 "doelgroep": "Iedereen die op de merknaam of via een verwijzing binnenkomt",
 "fase": "orientatie",
 "vraag": "Wat doet Capital BB en waar moet ik zijn voor mijn vraag?",
 "cta": "Scan of kennismaking",
 "steunt": ["meer-klanten", "slimmer-werken", "werk", "prijzen"],
 "botst_niet_met": [],
},

"websites": {
 "intentie": "Wat kan Capital BB op het gebied van websites en leadmachines",
 "termen": ["maatwerkwebsite", "leadmachine", "website met koppelingen",
            "conversiegerichte website"],
 "doelgroep": "Bedrijven die de mogelijkheden en de aanpak willen begrijpen",
 "fase": "overweging",
 "vraag": "Wat bouwt Capital BB precies, en wat kan er allemaal in een site zitten?",
 "cta": "Bespreek uw situatie",
 "steunt": ["website-laten-maken", "website-voor-startende-ondernemer",
            "vindbaarheid", "crm"],
 # Deze pagina gaat over het aanbod. De koopvraag hoort een niveau lager.
 "botst_niet_met": ["website-laten-maken"],
},

"website-laten-maken": {
 "intentie": "Een website laten maken: wat kost het, hoe lang duurt het, hoe kies ik",
 "termen": ["website laten maken", "professionele website laten maken",
            "bedrijfswebsite laten maken", "website laten maken kosten",
            "website voor ondernemers", "website voor mkb", "website voor zzp",
            "leadgeneratie website laten maken"],
 "doelgroep": "Ondernemers die op het punt staan een bouwer te kiezen",
 "fase": "koopintentie",
 "vraag": "Wat kost het om een website te laten maken en waar moet ik op letten?",
 "cta": "Vraag een voorstel aan",
 "steunt": ["websites", "prijzen", "werkwijze", "werk"],
 "botst_niet_met": ["websites", "website-voor-startende-ondernemer"],
},

"website-voor-startende-ondernemer": {
 "intentie": "Wat heeft een starter in het eerste jaar nodig aan een website",
 "termen": ["website voor startende ondernemer", "website starter",
            "eerste website bedrijf", "website net gestart"],
 "doelgroep": "Ondernemers korter dan een jaar bezig, zonder bestaande systemen",
 "fase": "koopintentie",
 "vraag": "Wat heb ik als starter wel en niet nodig, en wat kan wachten?",
 "cta": "Leg uw plan voor",
 "steunt": ["website-laten-maken", "websites", "prijzen"],
 "botst_niet_met": ["website-laten-maken"],
},

"website-laten-vernieuwen": {
 "intentie": "Bestaande website vernieuwen of verbeteren, en posities behouden",
 "termen": ["website laten vernieuwen", "website verbeteren", "website vervangen",
            "oude website opknappen", "website restylen", "website migreren"],
 "doelgroep": "Bedrijven met een bestaande site die twijfelen over vervangen",
 "fase": "koopintentie",
 "vraag": "Vervang ik mijn site of verbeter ik hem, en wat gebeurt er met mijn vindbaarheid?",
 "cta": "Laat eerst uw huidige website beoordelen",
 "steunt": ["scan", "website-laten-maken", "websites", "vindbaarheid"],
 "botst_niet_met": ["website-laten-maken", "websites"],
},

"websites-voor-salons": {
 "intentie": "Website voor een kapsalon of beautysalon, met online boeken",
 "termen": ["website kapsalon", "website voor salon", "website beautysalon",
            "kapper website laten maken", "online boeken kapsalon",
            "website nagelstudio", "website barbershop"],
 "doelgroep": "Kapsalons, barbershops, nagelstudio's en beautysalons",
 "fase": "koopintentie",
 "vraag": "Wat heeft een salon nodig aan een website, en hoe koppel ik mijn agenda?",
 "cta": "Bespreek uw salon",
 "steunt": ["websites", "werk", "ai-telefoniste", "scan"],
 "botst_niet_met": ["websites", "website-laten-maken"],
},

"vindbaarheid": {
 "intentie": "Gevonden worden in Google en in AI-antwoorden",
 "termen": ["seo", "geo", "generative engine optimization", "ai vindbaarheid",
            "seo uitbesteden", "vindbaarheid verbeteren"],
 "doelgroep": "Bedrijven die te weinig organisch verkeer krijgen",
 "fase": "overweging",
 "vraag": "Hoe word ik gevonden in zoekmachines en in AI-assistenten?",
 "cta": "Vraag een nulmeting aan",
 "steunt": ["online-marketing", "websites"],
 "botst_niet_met": ["online-marketing"],
},

"online-marketing": {
 "intentie": "Vraag aanjagen met advertenties, social media, content en e-mail",
 "termen": ["online marketing", "google ads uitbesteden", "meta ads",
            "social media beheer", "e-mailmarketing", "marketingcampagne"],
 "doelgroep": "Bedrijven die betaald verkeer en zichtbaarheid willen inkopen",
 "fase": "overweging",
 "vraag": "Wat levert adverteren mij op en welk budget heeft zin?",
 "cta": "Laat uw cijfers doorrekenen",
 "steunt": ["vindbaarheid", "websites", "crm"],
 # Vindbaarheid is onbetaald en duurt maanden; marketing is betaald en
 # direct. Dezelfde belofte op beide pagina's zou onzin zijn.
 "botst_niet_met": ["vindbaarheid"],
},

"ai-medewerkers": {
 "intentie": "Telefoon en berichten laten afhandelen door een digitale medewerker",
 "termen": ["ai medewerker", "ai receptionist", "digitale medewerker",
            "telefoon laten opnemen"],
 "doelgroep": "Bedrijven die oproepen missen",
 "fase": "overweging",
 "vraag": "Wat kan een AI-medewerker overnemen en waar houdt het op?",
 "cta": "Leg één gemiste oproep voor",
 "steunt": ["ai-telefoniste", "crm"],
 "botst_niet_met": ["ai-telefoniste"],
},

"ai-telefoniste": {
 "intentie": "Specifiek de telefoon laten opnemen door AI",
 "termen": ["ai telefoniste", "ai telefonie", "telefoon aannemen ai",
            "virtuele receptionist"],
 "doelgroep": "Bedrijven waar de telefoon overgaat tijdens het werk",
 "fase": "koopintentie",
 "vraag": "Hoe werkt doorschakelen en wat zegt de AI-telefoniste precies?",
 "cta": "Test het op uw eigen telefoon",
 "steunt": ["ai-medewerkers", "crm"],
 "botst_niet_met": ["ai-medewerkers"],
},

"crm": {
 "intentie": "Klantcontact en opvolging in één systeem",
 "termen": ["crm systeem", "crm mkb", "crm voor verkoopteams", "klantbeheer"],
 "doelgroep": "Bedrijven die klanten in Excel en hun hoofd bijhouden",
 "fase": "overweging",
 "vraag": "Wat zit er in een CRM en wat kost het?",
 "cta": "Plan een CRM-demo",
 "steunt": ["maatwerk-crm-laten-maken", "business-os", "automatisering"],
 "botst_niet_met": ["maatwerk-crm-laten-maken", "business-os"],
},

"maatwerk-crm-laten-maken": {
 "intentie": "De afweging tussen een maatwerk-CRM en een standaardpakket",
 "termen": ["maatwerk crm", "crm op maat laten maken", "eigen crm laten bouwen"],
 "doelgroep": "Bedrijven die een pakket ontgroeid zijn of erover twijfelen",
 "fase": "koopintentie",
 "vraag": "Wanneer heb ik maatwerk nodig en wanneer volstaat een pakket?",
 "cta": "Twijfelt u nog tussen maatwerk en een pakket?",
 "steunt": ["crm", "business-os"],
 "botst_niet_met": ["crm"],
},

"automatisering": {
 "intentie": "Terugkerend werk en losse processen automatiseren",
 "termen": ["workflowautomatisering", "bedrijfssysteem", "processen digitaliseren",
            "koppelingen tussen systemen"],
 "doelgroep": "Bedrijven met veel handwerk en overtypen",
 "fase": "overweging",
 "vraag": "Wat kan er geautomatiseerd worden en wat kost dat?",
 "cta": "Leg één proces voor",
 "steunt": ["bedrijfsprocessen-automatiseren", "business-os", "crm"],
 "botst_niet_met": ["bedrijfsprocessen-automatiseren"],
},

"bedrijfsprocessen-automatiseren": {
 "intentie": "Waar begin je met automatiseren en waarom mislukt het vaak",
 "termen": ["bedrijfsprocessen automatiseren", "processen automatiseren mkb",
            "welk proces eerst automatiseren"],
 "doelgroep": "Bedrijven die willen automatiseren maar niet weten waar te beginnen",
 "fase": "koopintentie",
 "vraag": "Welk proces automatiseer ik als eerste, en wat levert het op?",
 "cta": "Welk proces kiest u als eerste?",
 "steunt": ["automatisering", "crm", "business-os"],
 "botst_niet_met": ["automatisering"],
},

"business-os": {
 "intentie": "Het hele bedrijf in één omgeving",
 "termen": ["business os", "bedrijfssoftware mkb", "alles in één systeem",
            "erp voor mkb"],
 "doelgroep": "Bedrijven met meerdere afdelingen en losse abonnementen",
 "fase": "overweging",
 "vraag": "Wat is een Business OS en wanneer heb ik er een nodig?",
 "cta": "Breng uw systemen in kaart",
 "steunt": ["crm", "automatisering"],
 "botst_niet_met": ["crm"],
},

"scan": {
 "intentie": "Website laten beoordelen",
 "termen": ["website analyse", "website check", "website laten beoordelen",
            "gratis website scan"],
 "doelgroep": "Bedrijven met een bestaande site die twijfelen of hij goed genoeg is",
 "fase": "orientatie",
 "vraag": "Wat is er mis met mijn huidige website?",
 "cta": "Vraag de scan aan",
 "steunt": ["websites", "vindbaarheid"],
 "botst_niet_met": [],
},

"prijzen": {
 "intentie": "Wat kost het allemaal",
 "termen": ["prijzen", "tarieven", "wat kost een website", "wat kost een crm"],
 "doelgroep": "Iedereen die bedragen wil zien voordat hij belt",
 "fase": "koopintentie",
 "vraag": "Wat kosten de diensten van Capital BB?",
 "cta": "Leg uw situatie voor",
 "steunt": ["websites", "crm", "automatisering", "business-os"],
 "botst_niet_met": [],
},

"werk": {
 "intentie": "Bewijs zien van wat er gebouwd is",
 "termen": ["portfolio", "cases", "gebouwd werk", "voorbeelden"],
 "doelgroep": "Bedrijven die willen zien of het werk deugt",
 "fase": "overweging",
 "vraag": "Wat heeft Capital BB werkelijk gebouwd?",
 "cta": "Bespreek uw situatie",
 "steunt": ["websites", "crm", "vindbaarheid"],
 "botst_niet_met": [],
},

"werkwijze": {
 "intentie": "Hoe verloopt een traject",
 "termen": ["werkwijze", "hoe werkt het", "traject", "offerte"],
 "doelgroep": "Bedrijven die willen weten waar ze aan beginnen",
 "fase": "overweging",
 "vraag": "Hoe loopt een opdracht bij Capital BB?",
 "cta": "Plan een kennismaking",
 "steunt": ["prijzen", "werk"],
 "botst_niet_met": [],
},

"wie": {
 "intentie": "Wie zit er achter Capital BB",
 "termen": ["bjorn beerntsen", "capital bb oprichter", "wie is capital bb"],
 "doelgroep": "Bezoekers die willen weten met wie ze zaken doen",
 "fase": "overweging",
 "vraag": "Wie is Björn Beerntsen en werk ik rechtstreeks met hem?",
 "cta": "geen",
 "steunt": ["werkwijze", "werk", "contact"],
 "botst_niet_met": [],
},

"contact": {
 "intentie": "Contact opnemen",
 "termen": ["contact", "bellen", "afspraak", "capital bb contact"],
 "doelgroep": "Iedereen die klaar is om te praten",
 "fase": "koopintentie",
 "vraag": "Hoe bereik ik Capital BB?",
 "cta": "Formulier, telefoon of WhatsApp",
 "steunt": [],
 "botst_niet_met": [],
},

"meer-klanten": {
 "intentie": "Hub: ik wil meer klanten",
 "termen": ["meer klanten", "meer aanvragen", "online groeien"],
 "doelgroep": "Bedrijven met een omzetvraag, nog zonder gekozen oplossing",
 "fase": "orientatie",
 "vraag": "Welke oplossing past bij mijn vraag om meer klanten?",
 "cta": "Laat uw huidige website beoordelen",
 "steunt": ["websites", "vindbaarheid", "online-marketing", "ai-medewerkers"],
 "botst_niet_met": [],
},

"slimmer-werken": {
 "intentie": "Hub: ik wil slimmer werken",
 "termen": ["slimmer werken", "minder handwerk", "processen verbeteren"],
 "doelgroep": "Bedrijven met een efficiencyvraag, nog zonder gekozen oplossing",
 "fase": "orientatie",
 "vraag": "Welke oplossing past bij mijn vraag om slimmer te werken?",
 "cta": "Leg één proces voor",
 "steunt": ["crm", "automatisering", "business-os"],
 "botst_niet_met": [],
},

"privacy": {
 "intentie": "Geen zoekintentie: verplichte informatie",
 "termen": [],
 "doelgroep": "Bezoekers die willen weten wat er met hun gegevens gebeurt",
 "fase": "bestaande klant",
 "vraag": "Wat doet deze site met mijn gegevens?",
 "cta": "geen",
 "steunt": [],
 "botst_niet_met": [],
},

}


# ---------------------------------------------------------------------------
# BESLISMATRIX voor de kandidaat-landingspagina's uit de opdracht.
# Per kandidaat: zoekintentie, overlaprisico, beschikbare unieke inhoud,
# besluit en onderbouwing. Alleen wat hier op "maken" staat, is gemaakt.
# ---------------------------------------------------------------------------
BESLISMATRIX = [
 ("/bedrijfswebsite-laten-maken/",
  "Website laten maken voor een bedrijf",
  "Zeer hoog: identieke intentie als /website-laten-maken/",
  "Geen. Alles wat hier zou staan, staat daar al.",
  "samenvoegen",
  "'Bedrijfswebsite' en 'website laten maken' leveren dezelfde zoekresultaten en "
  "dezelfde vraag op. De term is verwerkt in de tekst en de termenlijst van "
  "/website-laten-maken/. Een eigen pagina zou een doorway page zijn."),

 ("/website-laten-maken-mkb/",
  "Website laten maken voor mkb-bedrijven",
  "Hoog: dezelfde koopvraag met een doelgroep ervoor",
  "Beperkt. Kansrijk verschil zou zijn: mkb met bestaande systemen die "
  "gekoppeld moeten worden.",
  "backlog",
  "Publiceren zodra de invalshoek 'koppelen aan wat u al draait' genoeg eigen "
  "inhoud heeft: welke pakketten, welke koppelingen, wat kost dat. Nu zou het "
  "een kopie met een ander woord zijn."),

 ("/website-laten-maken-zzp/",
  "Website laten maken voor zzp'ers",
  "Hoog: overlapt met de starterspagina",
  "Beperkt. /website-voor-startende-ondernemer/ dekt de kern al.",
  "samenvoegen",
  "Zzp'ers en starters stellen dezelfde vraag: wat heb ik minimaal nodig en wat "
  "kost het. Term verwerkt in /website-voor-startende-ondernemer/."),

 ("/professionele-website-laten-maken/",
  "Professionele website laten maken",
  "Zeer hoog: 'professioneel' is een bijvoeglijk naamwoord, geen eigen intentie",
  "Geen.",
  "samenvoegen",
  "Precies het geval waarvoor de opdracht waarschuwt: een pagina maken omdat "
  "een zoekwoord grammaticaal anders is. Term verwerkt in de tekst van "
  "/website-laten-maken/."),

 ("/website-laten-vernieuwen/",
  "Bestaande website laten vernieuwen of verbeteren",
  "Laag: andere uitgangssituatie en andere afweging",
  "Ja, en er is materiaal: de scan bepaalt of verbeteren volstaat, migratie van "
  "een bestaand domein, wat er behouden kan blijven, hoe je rankings niet "
  "kwijtraakt bij een nieuwe site.",
  "maken",
  "Wie al een site heeft, heeft een wezenlijk andere vraag: vervangen of "
  "verbeteren, en wat gebeurt er met mijn huidige vindbaarheid. Dat wordt "
  "nergens anders beantwoord."),

 ("/leadgeneratie-website-laten-maken/",
  "Website die aanvragen genereert",
  "Hoog: dit is de belofte van /websites/ en /website-laten-maken/ samen",
  "Beperkt.",
  "samenvoegen",
  "Leadgeneratie is bij Capital BB geen apart product maar het uitgangspunt van "
  "elke site. Een eigen pagina zou dezelfde belofte een derde keer doen."),

 ("/website-laten-maken-arnhem/",
  "Website laten maken in Arnhem",
  "Middel: landelijke pagina's dekken de vraag inhoudelijk al",
  "Onvoldoende zonder bevestigde lokale gegevens. Er is geen bevestigd "
  "vestigingsadres, geen lokale klantcase met toestemming en geen Google "
  "Bedrijfsprofiel.",
  "backlog",
  "Een lokale pagina zonder verifieerbare lokale binding is een lege huls, en "
  "'gevestigd in Arnhem' schrijven zonder adres is onjuist. Wat er nodig is "
  "staat in LOKALE_BACKLOG hieronder."),

 ("/website-laten-maken-duiven/",
  "Website laten maken in Duiven",
  "Hoog ten opzichte van een eventuele Arnhem-pagina",
  "Geen.",
  "backlog",
  "Alleen zinvol na Arnhem, en alleen met eigen lokale inhoud. Anders is het "
  "een plaatsnaam-sjabloon."),

 ("/website-laten-maken-gelderland/",
  "Website laten maken in Gelderland",
  "Hoog: provinciepagina's zijn zelden een eigen zoekintentie",
  "Geen.",
  "backlog",
  "Provinciezoekopdrachten zijn zeldzaam en de intentie valt samen met de "
  "landelijke pagina. Werkgebied staat al op elke pagina en in de schema-data."),
]


# ---------------------------------------------------------------------------
# Wat er nodig is voordat een lokale pagina waarde heeft. Zolang deze lijst
# niet is afgevinkt, is een pagina over Arnhem of Duiven niet eerlijk te maken.
# ---------------------------------------------------------------------------
LOKALE_BACKLOG = [
 "Een bevestigd vestigings- of bezoekadres, of het expliciete besluit dat er "
 "geen vestiging is en dat de pagina dat ook zo zegt",
 "Een aangemaakt en geverifieerd Google Bedrijfsprofiel met dat werkgebied",
 "Minstens één klant of project in de regio dat met naam genoemd mag worden",
 "Minstens één echte Google-review",
 "Een concreet verhaal over regionale samenwerking: hoe verloopt een gesprek "
 "op locatie, welk gebied wordt bereden, waarin verschilt dat van een "
 "landelijk bureau dat alles op afstand doet",
]

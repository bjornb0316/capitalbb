# -*- coding: utf-8 -*-
"""
Het casemodel. Eén vorm voor al het getoonde werk, zodat er nooit meer een
demo als klantopdracht kan worden gepresenteerd.

Waarom dit bestaat: op /werk/ stonden drie soorten werk door elkaar. Een live
site voor een merk van de oprichter zelf, een geanonimiseerde klantopdracht,
en elf demosites die ongevraagd zijn gebouwd als kennismaking. Voor een
bezoeker zag dat er hetzelfde uit. Dat is precies het soort suggestie dat een
ondernemer terecht wantrouwt.

STATUS is daarom verplicht en wordt zichtbaar op de pagina getoond:

  klantcase   Een echte, betaalde opdracht van een externe klant.
  eigen-merk  Echt gebouwd en live, maar voor een merk van de oprichter zelf.
              Geen externe opdrachtgever, dus geen bewijs van klanttevredenheid.
  demo        Ongevraagd gebouwd als kennismaking. Er is geen opdracht geweest
              en het bedrijf heeft er niet om gevraagd.
  concept     Ontwerp of prototype, niet live.

RESULTAAT mag alleen worden gerenderd als er een `bewijs` bij staat. Zonder
bron blijft het veld leeg en toont de pagina niets. Dat is de reden dat er nu
nergens een percentage staat: dat bewijs is er niet.

TOESTEMMING bepaalt of de naam getoond mag worden:
  "naam"    naam mag genoemd, met link
  "anoniem" wel tonen, geen naam of herleidbare gegevens
  "geen"    helemaal niet tonen (wordt overgeslagen bij het bouwen)

Velden per case:
  naam, branche, status, toestemming, datum
  beginsituatie, vraagstuk, oplossing
  onderdelen   wat er concreet is gebouwd
  integraties  koppelingen met externe systemen
  visueel      wat er getoond kan worden
  resultaat    alleen invullen mét bewijs
  bewijs       waar dat resultaat op gebaseerd is
  quote        alleen met toestemming van de klant
  diensten     welke Capital BB-diensten erin zitten (slugs)
  url          alleen als de site live en toonbaar is
"""

# ---------------------------------------------------------------------------
# Hoe elke status op de pagina heet en wordt uitgelegd. De bezoeker hoeft niet
# te raden wat hij ziet.
# ---------------------------------------------------------------------------
STATUS_LABEL = {
    "klantcase": ("Klantopdracht",
                  "Een betaalde opdracht voor een externe klant."),
    "eigen-merk": ("Eigen merk, live",
                   "Echt gebouwd en online, maar voor een merk van de oprichter zelf. "
                   "Geen externe opdrachtgever."),
    "demo": ("Demonstratie, ongevraagd gebouwd",
             "Als kennismaking gebouwd zonder opdracht. Het bedrijf heeft er niet "
             "om gevraagd en heeft er niet voor betaald."),
    "concept": ("Concept",
                "Ontwerp of prototype. Niet live."),
}


CASES = [

{
 "sleutel": "jezz-media",
 "naam": "Jezz-Media",
 "branche": "Groeipartner voor makelaars en financiële dienstverleners",
 "status": "eigen-merk",
 "toestemming": "naam",
 "datum": "2026-08",
 "url": "https://jezz-media.nl",
 "beginsituatie": ("Jezz-Media biedt magazines, websites, CRM met AI en vindbaarheid uit één "
                   "hand aan makelaars, hypotheekadviseurs en andere financiële "
                   "dienstverleners. Dat verhaal viel online uiteen in losse productpagina's, "
                   "waardoor de samenhang die het merk juist verkoopt niet zichtbaar was."),
 "vraagstuk": ("Hoe laat je vier diensten als één aanbod zien, op een manier die meegroeit "
               "als er doelgroepen en magazinetitels bij komen?"),
 "oplossing": ("Eén doorlopend verhaal waarin de diensten in elkaar grijpen, met een "
               "kennisbank, cases, veelgestelde vragen en een duidelijke gespreksroute. De "
               "structuur is opgezet om uit te breiden zonder verbouwing."),
 "onderdelen": [
   "Vier diensten verteld als één samenhangend aanbod",
   "Kennisbank waarmee de site inhoudelijk kan groeien",
   "Cases en veelgestelde vragen",
   "Een duidelijke route naar een gesprek",
   "Structuur die nieuwe doelgroepen aankan",
 ],
 "integraties": [],
 "visueel": "Volledige pagina, scrollend opgenomen van de live site",
 # Geen resultaat: er is geen meting gedeeld die hier gepubliceerd mag worden.
 "resultaat": "",
 "bewijs": "",
 "quote": "",
 "diensten": ["websites", "vindbaarheid"],
 "noot": ("Jezz-Media is het merk van dezelfde oprichter als Capital BB. De site is door "
          "Capital BB gebouwd en draait live, maar dit is geen externe klantopdracht."),
},

{
 "sleutel": "ijsseldal",
 "naam": "Zelfstandige hypotheekadviespraktijk",
 "branche": "Hypotheekadvies",
 "status": "klantcase",
 "toestemming": "anoniem",
 "datum": "2026-08",
 "url": "",
 "beginsituatie": ("Een zelfstandige adviespraktijk in Oost-Nederland zonder eigen website. "
                   "Klanten vonden de adviseur alleen via het profiel van een landelijk "
                   "netwerk: geen eigen verhaal, geen eigen vindbaarheid, geen eigen "
                   "aanvraagroute."),
 "vraagstuk": ("Hoe bouw je vertrouwen op in een branche waarin iedereen dezelfde blauwwitte "
               "huisstijl en dezelfde beloftes gebruikt?"),
 "oplossing": ("Een complete site van tien pagina's op een eigen designsysteem dat de "
               "conventies van de branche bewust vermijdt, met werkwijze, tarieven en "
               "veelgestelde vragen. Elke bewering op de site is nagetrokken tot de bron en "
               "met controledatum vastgelegd."),
 "onderdelen": [
   "Tien pagina's, waaronder werkwijze, tarieven en veelgestelde vragen",
   "Eigen designsysteem in plaats van een branchesjabloon",
   "Elke bewering nagetrokken tot de bron, met controledatum",
   "Gecontroleerd op contrast, mobiel gedrag, laadgewicht en toegankelijkheid",
   "Directe aanvraagroute voor een gesprek",
 ],
 "integraties": [],
 "visueel": "Gerenderde weergave van het ontwerp, met generieke teksten",
 "resultaat": "",
 "bewijs": "",
 "quote": "",
 "diensten": ["websites", "vindbaarheid"],
 "noot": ("Getoond met toestemming, zonder naam of herleidbare gegevens. Het beeld is een "
          "weergave van het ontwerp met generieke teksten."),
},

{
 "sleutel": "demoreeks",
 "naam": "Elf demosites voor salons en barbershops",
 "branche": "Kapsalons, barbershops, nagelstudio's en beautystudio's",
 "status": "demo",
 "toestemming": "anoniem",
 "datum": "2026-08",
 "url": "",
 "beginsituatie": ("Kapsalons, nagelstudio's en barbershops zonder eigen website zijn niet te "
                   "overtuigen met een offerte. Die willen eerst iets zien."),
 "vraagstuk": ("Hoe laat je zien wat een site voor zo'n zaak zou doen, zonder dat de "
               "ondernemer eerst moet betalen om het te ontdekken?"),
 "oplossing": ("Voor elf van zulke bedrijven is ongevraagd een complete demonstratiewebsite "
               "gebouwd, elk met een eigen ontwerp en waar mogelijk een werkende koppeling "
               "met het boekingssysteem dat de zaak al gebruikt."),
 "onderdelen": [
   "Elf afzonderlijke ontwerpen, geen gedeeld sjabloon",
   "Echte openingstijden, diensten en prijzen per zaak",
   "Werkende boekingsflow waar het boekingssysteem dat toeliet",
   "Mobiel als uitgangspunt, want daar komt vrijwel al het verkeer vandaan",
 ],
 "integraties": ["Salonized", "Knipklok", "Altegio", "Afspraakpro"],
 "visueel": "Drie van de elf, scrollend getoond op beeldscherm, laptop en telefoon",
 "resultaat": "",
 "bewijs": "",
 "quote": "",
 "diensten": ["websites", "automatisering", "ai-medewerkers"],
 "noot": ("Deze sites zijn ongevraagd gebouwd als kennismaking. Er is geen opdracht aan "
          "voorafgegaan en de bedrijven hebben er niet voor betaald. Namen en herleidbare "
          "gegevens zijn vervangen; de zaken bestaan echt en de koppelingen draaien op hun "
          "eigen boekingssysteem."),
},

]


# ---------------------------------------------------------------------------
# Aanleverchecklist. Wat er per nieuwe klant verzameld moet worden voordat een
# case gepubliceerd kan worden. Zonder toestemming en zonder bewijs komt er
# niets op de site; dat is geen formaliteit maar het verschil tussen een case
# en een verkooppraatje.
# ---------------------------------------------------------------------------
AANLEVERCHECKLIST = [
 ("Toestemming",
  "Schriftelijk, per mail is genoeg. Vraag expliciet: mag de bedrijfsnaam genoemd, "
  "mag er een link naar de site, mag er een screenshot, en mag een citaat worden "
  "gebruikt. Vier aparte vragen, want een ja op de ene is geen ja op de andere."),
 ("Beginsituatie",
  "Wat had de klant vóór de opdracht, en wat ging er mis. Leg dit vast vóór de start; "
  "achteraf is het altijd rooskleuriger dan het was."),
 ("Het vraagstuk",
  "In één zin: welk probleem moest worden opgelost. Niet 'ze wilden een nieuwe site' "
  "maar wat daar achter zat."),
 ("Wat er is gebouwd",
  "Concrete onderdelen en koppelingen. Dit is het deel dat een volgende klant "
  "overtuigt, want het is controleerbaar."),
 ("Beeldmateriaal",
  "Screenshots of foto's, met per beeld een alt-tekst. Vraag of er herleidbare "
  "klantgegevens in staan die eruit moeten."),
 ("Meetbaar resultaat, alleen mét bron",
  "Aantallen aanvragen, posities of omzet: alleen opnemen als de klant het cijfer "
  "aanlevert én mag worden genoemd waar het vandaan komt. Search Console, het CRM of "
  "de boekhouding. Zonder bron blijft het veld leeg; het model rendert dan niets."),
 ("Nulmeting",
  "Meet vóór livegang wat de uitgangssituatie is. Zonder nulmeting is elk later "
  "cijfer een bewering."),
 ("Citaat",
  "Alleen als de klant het zelf heeft geschreven of letterlijk heeft goedgekeurd. "
  "Zet de naam en functie erbij, anders is het waardeloos."),
 ("Datum",
  "Wanneer opgeleverd. Een case zonder datum veroudert ongemerkt."),
]

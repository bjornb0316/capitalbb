# -*- coding: utf-8 -*-
"""
De inhoudelijke verdieping van de zes dienstpagina's, plus de FAQ per dienst.

Waarom een apart bestand naast inhoud.py: dit is het leeuwendeel van de tekst
op de site. In inhoud.py staat wat overal terugkomt (prijzen, contact,
navigatie, sporen); hier staat wat per dienstpagina verschilt. Zo blijft
inhoud.py leesbaar.

Vorm per dienst, steeds dezelfde twaalf vragen in vaste blokken:

  definitie    korte, zelfstandig citeerbare uitleg (het GEO-antwoordblok)
  voor_wie     voor welk soort bedrijf dit is
  probleem     wat er misgaat zonder deze oplossing
  bouwt        (kop, tekst) van wat Capital BB concreet bouwt
  onderdelen   losse onderdelen die erin kunnen zitten
  traject      (fase, wat er gebeurt)
  koppelingen  waarmee gekoppeld kan worden
  prijsuitleg  hoe de prijs tot stand komt
  verschil     (alternatief, hoe dat verschilt) - wordt een vergelijkingstabel
  verwachting  wat een klant redelijk mag verwachten, en wat niet
  branches     (branche, wat daar speelt)

Alles hier is te herleiden tot wat Capital BB werkelijk bouwt en tot de
prijzen in inhoud.py. Branchevoorbeelden zijn illustratief: het zijn geen
klantnamen en geen gerealiseerde resultaten.
"""

DIEP = {

"online-marketing": {
 "vraag": "Wat houdt online marketing bij Capital BB in?",
 "definitie": ("Online marketing bij Capital BB verbindt zichtbaarheid met klantopvolging: advertenties in "
   "Google en op social media, beheer van de eigen kanalen, contentproductie en "
   "e-mailmarketing. Het verschil met een los marketingbureau is dat het hier op één keten "
   "zit: de campagne brengt bezoekers, de website zet ze om in aanvragen, het CRM bewaakt de "
   "opvolging en aftersales houdt het klantcontact na de verkoop op gang. Prijs op aanvraag; het advertentiebudget "
   "staat daar los van en gaat rechtstreeks naar Google of Meta."),
 "voor_wie": [
   "Bedrijven met een site die werkt, maar te weinig mensen die hem vinden",
   "Ondernemers die willen adverteren maar niet weten waar te beginnen of te stoppen",
   "Bedrijven die social media \"erbij doen\" en er daardoor niets uit halen",
   "Bedrijven met een klantenbestand waar niets meer mee gebeurt",
   "Wie campagnes draait maar niet kan zien wat er onderaan uitkomt",
 ],
 "probleem": ("Marketing wordt vaak los ingekocht van alles waar het op uitkomt. Het bureau "
   "levert kliks, de website vangt ze slecht op, de aanvraag belandt in een postvak dat "
   "niemand bewaakt, en aan het eind van de maand weet niemand wat het heeft opgeleverd. "
   "Dan lijkt marketing duur, terwijl het lek ergens anders zat."),
 "bouwt": [
   ("Advertenties die op iets uitkomen",
    "Campagnes in Google Ads, Meta en waar uw klant zit, met advertentieteksten en targeting "
    "die aansluiten op de pagina waar iemand landt. Geen verkeer naar een homepage die de "
    "vraag niet beantwoordt."),
   ("Social media die wordt bijgehouden",
    "Kanalen die worden beheerd in plaats van een keer per kwartaal gevuld: planning, "
    "plaatsing, en reageren op wat er binnenkomt."),
   ("Content die het werk doet",
    "Beeld, video en teksten die voor uw kanalen worden gemaakt, niet uit een beeldbank "
    "geplukt. Wat op de site staat en wat in een advertentie staat, vertelt hetzelfde verhaal."),
   ("Opvolgsystemen voor leads en offertes",
    "Een aanvraag krijgt een eigenaar en een volgende stap. Herinneringen, contactmomenten en "
    "offerte-opvolging worden gekoppeld aan uw CRM, zodat duidelijk is wie wanneer contact opneemt."),
   ("Aftersales die doorloopt na de verkoop",
    "Een bedankbericht, een check na levering, een feedbackvraag of een herinnering voor onderhoud. "
    "We richten contactmomenten in die passen bij uw dienst en het moment van de klant."),
   ("E-mail die uw bestaande klanten terughaalt",
    "Nieuwsbrieven en geautomatiseerde opvolging vanuit het CRM. Meestal het goedkoopste "
    "kanaal dat er is, en meestal het kanaal dat stilligt."),
 ],
 "onderdelen": [
   "Google Ads: zoek-, display- en remarketingcampagnes",
   "Meta Ads: Facebook en Instagram",
   "Advertenties op LinkedIn of andere kanalen waar uw klant zit",
   "Landingspagina's die bij de campagne horen",
   "Social media: planning, plaatsing en community-beheer",
   "Contentproductie: beeld, video, teksten en creatives",
   "E-mailmarketing en geautomatiseerde mailflows",
   "Lead- en offerteopvolging met CRM-taken en herinneringen",
   "Aftersales: servicecontact, feedbackvragen en onderhoudsherinneringen",
   "Klantbehoud: relevante vervolgcontacten en herhaalaankopen",
   "Campagnes rond een actie, seizoen of opening",
   "Meting: welke campagne welke aanvraag opleverde",
 ],
 "traject": [
   ("Uitvragen wat een klant waard is", "Zonder dat getal is elk advertentiebudget een gok. "
    "Wat levert een gemiddelde opdracht op, en hoeveel aanvragen worden er klant."),
   ("Controleren waar het verkeer landt", "Eerst kijken of de pagina de vraag beantwoordt. "
    "Adverteren naar een pagina die niet converteert, is geld in een lek gieten."),
   ("Klein beginnen", "E\u00e9n kanaal, een beperkt budget, en meten wat eruit komt voordat "
    "het budget omhoog gaat."),
   ("Meten en bijsturen", "Welke campagne, welke advertentie en welke pagina leverden de "
    "aanvraag op. Wat niets doet, gaat eruit."),
   ("Uitbreiden of stoppen", "Werkt het, dan schalen we op. Werkt het niet, dan zeggen we "
    "dat in plaats van het budget stil te laten doorlopen."),
 ],
 "koppelingen": [
   "Google Ads en Google Analytics",
   "Meta Business Suite",
   "Het CRM, zodat een aanvraag zijn campagne meedraagt",
   "De website en haar formulieren",
   "E-mailplatforms en nieuwsbriefsoftware",
   "WhatsApp Business",
 ],
 "prijsuitleg": ("Prijs op aanvraag. Anders dan bij de andere diensten staat hier geen "
   "vanafprijs, omdat het te veel uiteenloopt: het aantal kanalen, of er content gemaakt "
   "moet worden en hoe vaak er wordt bijgestuurd bepalen het werk. Wat er w\u00e9l vaststaat: "
   "het advertentiebudget staat los van het honorarium en gaat rechtstreeks van u naar "
   "Google of Meta. Wij nemen geen percentage over uw advertentiebudget, want dan zou een "
   "hoger budget in ons eigen voordeel werken. Voordat er iets loopt, rekenen we samen door "
   "wat een klant u waard is; komt daar geen werkbaar budget uit, dan zeggen we dat."),
 "verschil": [
   ("Zelf adverteren",
    "Kan prima voor een eenvoudige zoekcampagne. Het risico zit in wat u niet ziet: budget "
    "dat wegloopt op zoekwoorden die nooit een klant opleveren."),
   ("Een marketingbureau",
    "Levert kliks en rapportages. Wat er daarna met de aanvraag gebeurt, is meestal niet hun "
    "afdeling, en aan de website mogen ze vaak niets veranderen."),
   ("Een percentage van het advertentiebudget betalen",
    "Gebruikelijk in de markt, maar het beloont een hoger budget in plaats van een beter "
    "resultaat. Wij doen het niet."),
   ("Online marketing van Capital BB",
    "De campagne, de pagina waar hij op uitkomt, het CRM waarin de aanvraag landt en de "
    "opvolging zitten bij dezelfde partij. Loopt het ergens vast, dan is er niemand om naar "
    "te wijzen."),
 ],
 "verwachting": ("U mag verwachten dat er wordt gemeten, dat u per kanaal ziet wat er "
   "binnenkwam, en dat er wordt gestopt met wat niet werkt. Wat wij niet beloven: een aantal "
   "leads, een kostprijs per aanvraag of een rendement op advertentiebudget. Die hangen af "
   "van uw markt, uw prijs en uw concurrentie, en wie ze v\u00f3\u00f3raf garandeert, gokt met uw "
   "geld. Reken ook niet op resultaat binnen een week: een campagne heeft data nodig voordat "
   "bijsturen zin heeft."),
 "branches": [
   ("Autobedrijven en caravanbedrijven", "Aanbod verandert continu; advertenties op merk en "
    "model werken alleen als de voorraadpagina klopt en actueel is."),
   ("Kapsalons en beautysalons", "Lokaal en visueel. Social media en een werkende "
    "boekingsknop doen hier meer dan een zoekcampagne."),
   ("Hypotheekadviseurs", "Streng gereguleerd en gevoelig: geen loze beloftes over rente of "
    "slagingskans, wel uitleg die vertrouwen wekt."),
   ("Horeca", "Draait op actualiteit: openingstijden, kaartwijzigingen en acties, met een "
    "reserveerknop die het doet."),
   ("Verkooporganisaties", "Leads moeten gekwalificeerd binnenkomen, anders vult u een "
    "pipeline met mensen die nooit klant worden."),
 ],
},

"websites": {
 "vraag": "Wat is een leadmachine, en hoe verschilt die van een gewone website?",
 "definitie": ("Een website van Capital BB is geen digitale folder maar een leadmachine: "
   "een op maat gebouwde site die bezoekers naar één duidelijke actie leidt en die actie "
   "doorgeeft aan de rest van uw systeem. Prijzen lopen van €795 voor een compacte site "
   "tot vanaf €4.945 voor maatwerk met eigen functionaliteit, eenmalig en exclusief btw."),
 "voor_wie": [
   "Ondernemers die nu alleen zichtbaar zijn via een platformprofiel of social media",
   "Bedrijven met een site die er nog wel uitziet, maar nauwelijks aanvragen oplevert",
   "Startende ondernemers die vanaf dag één serieus willen overkomen",
   "Bedrijven die telefonisch goed lopen, maar online niets binnenkrijgen",
 ],
 "probleem": ("De meeste bedrijfssites vertellen wie het bedrijf is en stoppen daar. Er staat "
   "geen duidelijke volgende stap, het formulier komt in een postvak dat niemand "
   "structureel bijhoudt, en op een telefoon valt de helft weg. Bezoekers die klaar waren "
   "om te bellen, klikken weg."),
 "bouwt": [
   ("Een structuur die naar één actie leidt",
    "Elke pagina heeft een doel en eindigt in de stap die daarbij hoort: bellen, appen, een "
    "formulier of een afspraak in de agenda. Geen pagina loopt dood."),
   ("Een ontwerp dat op uw bedrijf is gemaakt",
    "Geen thema met uw logo erin. Kleur, typografie en opbouw komen uit uw vak en uw "
    "positie, en wijken bewust af van wat uw concurrenten doen."),
   ("Techniek die crawlers en AI-systemen kunnen lezen",
    "Semantische HTML, unieke titels en beschrijvingen, canonicals, structured data en een "
    "sitemap. De inhoud staat in de HTML, niet pas na het laden van JavaScript."),
   ("Een aanvraag die ergens landt",
    "Het formulier kan doorgezet worden naar een CRM, naar WhatsApp, naar uw agenda of naar "
    "een AI-medewerker die de eerste vragen alvast afhandelt."),
 ],
 "onderdelen": [
   "Contact-, offerte- en aanvraagformulieren met eigen velden",
   "Afspraken maken via een agenda- of boekingskoppeling",
   "WhatsApp-knop en klikbare telefoonnummers",
   "Een prijzen- of tarievenpagina met echte bedragen",
   "Veelgestelde vragen die ook als structured data meegaan",
   "Cases, referenties of werkvoorbeelden",
   "Meertalige of regionale varianten",
   "Een blog of kennisbank voor vindbaarheid op de lange termijn",
   "Analytics of serverlogging, als u wilt meten",
 ],
 "traject": [
   ("Uitvragen", "Wat verkoopt u, aan wie, en welke aanvraag is de moeite waard. Plus: wat "
    "er nu misgaat. Dit is een gesprek, geen vragenlijst."),
   ("Voorstel bouwen", "U krijgt een werkend concept te zien: aanklikbaar, in uw eigen "
    "kleuren, met uw eigen teksten. Bevalt het niet, dan kost het niets."),
   ("Bouwen na akkoord", "Na uw akkoord wordt de volledige site gebouwd, tegen de "
    "afgesproken prijs. Betaling in drie delen: 40% bij opdracht, 40% na goedkeuring van "
    "het ontwerp, 20% voor livegang."),
   ("Controle en livegang", "Mobiel gedrag, contrast, laadgewicht, toegankelijkheid, links "
    "en formulieren worden nagelopen voordat de site live gaat."),
   ("Onderhoud of doorbouwen", "Daarna kunt u kiezen voor onderhoud vanaf €59 per maand, "
    "of doorgroeien naar CRM, automatisering of een AI-medewerker."),
 ],
 "koppelingen": [
   "Agenda's en boekingssystemen, waaronder Salonized, Knipklok, Altegio en Afspraakpro",
   "WhatsApp Business",
   "Een CRM van Capital BB of een bestaand pakket",
   "E-mail en nieuwsbrieven",
   "Betaal- of aanbetalingslinks",
   "Voorraad- of aanbodfeeds, bijvoorbeeld voor occasions",
 ],
 "prijsuitleg": ("De prijs volgt de omvang en de mate van maatwerk, niet het gesprek. Basis "
   "€795 tot vijf pagina's, Premium €1.595 tot tien pagina's met conversiegerichte opbouw, "
   "Signature €2.995 tot vijftien pagina's met uitgesproken maatwerkdesign, en maatwerk "
   "vanaf €4.945 zodra er eigen functionaliteit of koppelingen bij komen. Alles eenmalig en "
   "exclusief btw. Koppelingen worden apart geprijsd, vanaf €295 voor een eenvoudige "
   "koppeling."),
 "verschil": [
   ("Zelf bouwen in een websitebouwer",
    "Goedkoop en snel, maar u bent zelf de bouwer, de tekstschrijver en de beheerder. "
    "Techniek en vindbaarheid blijven meestal liggen, en koppelen met uw eigen systemen kan "
    "vaak niet."),
   ("Een thema of template laten invullen",
    "Ziet er verzorgd uit, maar staat er bij tientallen anderen ook. De opbouw volgt het "
    "thema in plaats van uw verkoopverhaal, en overbodige code vertraagt de site."),
   ("Een website van Capital BB",
    "Op maat gebouwd rond uw aanvraagroute, met techniek die leesbaar is voor zoekmachines "
    "en AI-systemen, en klaar om aan CRM, telefonie en automatisering gekoppeld te worden."),
 ],
 "verwachting": ("U mag verwachten dat de site snel is, op elke telefoon werkt, indexeerbaar "
   "is, dat elke pagina een duidelijke volgende stap heeft en dat aanvragen aankomen waar u "
   "ze wilt hebben. Wat wij niet beloven: een vast aantal aanvragen of een vaste plek in "
   "Google. Hoeveel er binnenkomt hangt ook af van uw markt, uw prijs en uw bereik."),
 "branches": [
   ("Hypotheekadviseurs", "Vertrouwen en onafhankelijkheid moeten meteen zichtbaar zijn, met "
    "tarieven, werkwijze en een gespreksaanvraag in plaats van een offerteknop."),
   ("Autobedrijven en caravanbedrijven", "Het aanbod verandert wekelijks; de site moet "
    "voorraad kunnen tonen en proefrit- of bezichtigingsaanvragen opvangen."),
   ("Kapsalons en beautysalons", "Bijna al het verkeer is mobiel en de belangrijkste knop is "
    "'afspraak maken', gekoppeld aan het boekingssysteem dat de zaak al gebruikt."),
   ("Schilders en klusbedrijven", "Werk spreekt voor zich: foto's van uitgevoerd werk, "
    "werkgebied, en een aanvraagformulier dat genoeg vraagt om te kunnen inschatten."),
   ("Horeca", "Openingstijden, kaart en reserveren moeten binnen één scroll te vinden zijn, "
    "ook als iemand voor de deur staat."),
 ],
},

"vindbaarheid": {
 "vraag": "Wat is het verschil tussen SEO en GEO?",
 "definitie": ("SEO is zorgen dat u gevonden wordt in zoekmachines. GEO, Generative Engine "
   "Optimization, is zorgen dat AI-systemen zoals ChatGPT, Google AI Overviews, Perplexity "
   "en Copilot uw bedrijf begrijpen en kunnen aanhalen als antwoord. Capital BB doet beide "
   "als één aanpak, vanaf €149 per maand exclusief btw."),
 "voor_wie": [
   "Bedrijven die goed werk leveren maar nauwelijks online gevonden worden",
   "Ondernemers die zien dat klanten hun vraag steeds vaker aan een AI stellen",
   "Bedrijven met een nieuwe site die nog geen zichtbaarheid heeft opgebouwd",
   "Bedrijven die adverteren en ook zonder advertentiebudget iets willen binnenkrijgen",
 ],
 "probleem": ("Zoeken verandert. Een deel van uw klanten typt niet meer drie woorden in Google "
   "maar stelt een hele vraag aan een assistent, en krijgt één antwoord terug in plaats van "
   "tien blauwe links. Wie in dat antwoord niet voorkomt, bestaat voor die klant niet. "
   "Tegelijk blijft de klassieke zoekmachine gewoon bestaan; u kunt er dus niet één van de "
   "twee kiezen."),
 "bouwt": [
   ("Een technische basis die klopt",
    "Indexeerbaarheid, canonicals, structured data, sitemap, robots.txt, laadgewicht, "
    "interne links en statuscodes. Zonder die basis heeft inhoud weinig zin."),
   ("Een entiteit die herkenbaar is",
    "Één consistent bedrijfsprofiel over de hele site en daarbuiten: naam, KvK, werkgebied, "
    "diensten en contactgegevens die overal hetzelfde zijn. AI-systemen hebben dat nodig om "
    "u met zekerheid te kunnen noemen."),
   ("Inhoud die citeerbaar is",
    "Korte definities, directe antwoorden onder een vraag, vergelijkingen, prijsuitleg en "
    "stappenplannen. Zo geschreven dat een los stuk tekst ook zonder de rest van de pagina "
    "klopt, want zo wordt het aangehaald."),
   ("Lokale zichtbaarheid",
    "Bedrijfsprofiel, categorieën, dienstgebied, reviews en gegevens die overal gelijk zijn."),
 ],
 "onderdelen": [
   "Technische controle en herstel",
   "Zoekintentieonderzoek en een paginaplan",
   "Titels, beschrijvingen en koppenstructuur",
   "Structured data: bedrijf, diensten, kruimelpaden, veelgestelde vragen",
   "Antwoordblokken en vergelijkingen voor AI-citaties",
   "llms.txt en toegang voor AI-crawlers",
   "Lokaal bedrijfsprofiel en reviewsignalen",
   "Landingspagina's per zoekintentie",
   "Maandelijkse rapportage met wat er is gedaan en wat het deed",
 ],
 "traject": [
   ("Nulmeting", "Wat staat er nu, wat is indexeerbaar, waarop wordt u wel en niet gevonden, "
    "en wat zeggen AI-systemen op dit moment over uw bedrijf."),
   ("Techniek herstellen", "Eerst de blokkades weg: crawlfouten, ontbrekende of dubbele "
    "titels, kapotte links, verkeerde canonicals, ontbrekende structured data."),
   ("Structuur en intentie", "Bepalen welke pagina welke vraag beantwoordt, en waar pagina's "
    "ontbreken of elkaar in de weg zitten."),
   ("Inhoud en entiteit", "Antwoordblokken, definities en vergelijkingen schrijven, en "
    "bedrijfsgegevens overal gelijktrekken."),
   ("Meten en bijsturen", "Maandelijks: wat is er gedaan, wat beweegt er, en waar gaat de "
    "aandacht volgende maand heen."),
 ],
 "koppelingen": [
   "Google Search Console",
   "Bing Webmaster Tools",
   "Google Bedrijfsprofiel",
   "Analytics of serverlogs, als u die wilt gebruiken",
   "De website en het CRM, om aanvragen aan hun bron te koppelen",
 ],
 "prijsuitleg": ("Drie maandbedragen, exclusief btw. €149 voor technische controle, "
   "rapportage en kleine optimalisaties. €299 als daar lokale zichtbaarheid, bedrijfsprofiel "
   "en contentupdates bij komen. €499 voor doorlopende content, landingspagina's, "
   "autoriteitsopbouw en GEO-monitoring. Eenmalig technisch herstel op een bestaande site "
   "valt buiten het abonnement en wordt vooraf afgesproken."),
 "verschil": [
   ("Alleen SEO",
    "Richt zich op de klassieke zoekresultaten. Werkt nog steeds, maar mist het deel van uw "
    "markt dat de vraag inmiddels aan een assistent stelt."),
   ("Alleen adverteren",
    "Levert direct verkeer zolang u betaalt. Stopt het budget, dan stopt de zichtbaarheid, "
    "en in AI-antwoorden koopt u geen plek."),
   ("SEO en GEO samen",
    "Dezelfde technische basis en dezelfde inhoud werken voor allebei. Wat een zoekmachine "
    "moet kunnen crawlen, moet een AI-systeem kunnen lezen en aanhalen."),
 ],
 "verwachting": ("U mag verwachten dat de techniek klopt, dat uw bedrijfsgegevens overal "
   "gelijk zijn, dat er inhoud komt die uw klant echt zoekt, en dat u elke maand ziet wat "
   "er is gedaan. Wat wij niet beloven: een positie in Google of een vaste plek in "
   "AI-antwoorden. Niemand heeft die in de hand, en wie het wel belooft verkoopt iets wat "
   "hij niet levert. Vindbaarheid is bovendien werk van maanden, niet van weken."),
 "branches": [
   ("Hypotheekadviseurs", "Klanten vragen een assistent letterlijk om uitleg en "
    "vergelijking; wie die uitleg zelf publiceert, maakt kans om aangehaald te worden."),
   ("Autobedrijven", "Merk, model en plaats bepalen de zoekvraag, en het aanbod verandert "
    "continu. Structured data op de voorraad doet hier het meeste werk."),
   ("Klusbedrijven", "Zoekvragen zijn lokaal en concreet. Bedrijfsprofiel, werkgebied en "
    "reviews wegen zwaarder dan lange teksten."),
   ("Dienstverlenend mkb", "De vraag is meestal 'wie doet dit voor mijn soort bedrijf'. Daar "
    "horen pagina's per situatie bij, geen algemene dienstpagina."),
 ],
},

"ai-medewerkers": {
 "vraag": "Wat is een AI-medewerker?",
 "definitie": ("Een AI-medewerker is een digitale medewerker die uw telefoon opneemt en uw "
   "berichten beantwoordt: hij kent uw diensten, uw agenda en uw grenzen, plant afspraken "
   "in op tijden die u vrijgeeft, en geeft door aan u zodra het over geld of uitzonderingen "
   "gaat. Inrichting vanaf €750 exclusief btw, plus verbruikskosten voor telefonie en AI."),
 "voor_wie": [
   "Bedrijven waar de telefoon overgaat terwijl er niemand kan opnemen",
   "Ondernemers met hun handen in het werk: op locatie, in de stoel, onder de auto",
   "Bedrijven met veel dezelfde vragen: openingstijden, prijzen, beschikbaarheid",
   "Verkooporganisaties die geen inkomende lead willen laten liggen",
 ],
 "probleem": ("Een gemiste oproep is meestal een gemiste klant: wie niemand aan de lijn "
   "krijgt, belt de volgende. Voicemail lost dat niet op, want de meeste bellers spreken "
   "niets in. Een antwoordservice kent uw vak niet en kan geen afspraak in uw agenda zetten."),
 "bouwt": [
   ("Opnemen en te woord staan",
    "De AI-medewerker neemt op via telefoon, WhatsApp, chat of e-mail, beantwoordt "
    "veelgestelde vragen over uw diensten, prijzen en beschikbaarheid, en houdt zich aan wat "
    "u hem meegeeft."),
   ("Inplannen in uw agenda",
    "Alleen op tijden die u vrijgeeft, met de duur die bij de dienst hoort. De klant krijgt "
    "een bevestiging, u ziet de afspraak in uw agenda staan."),
   ("Doorgeven wat hij niet mag beslissen",
    "Korting, uitzonderingen, klachten en alles wat u zelf wilt doen: daar draagt hij over, "
    "met de context van het gesprek erbij."),
   ("Vastleggen in het systeem",
    "Elk gesprek en elke afspraak komt in het CRM te staan, zodat er een klantkaart is in "
    "plaats van een gebeld-en-vergeten nummer."),
 ],
 "onderdelen": [
   "Inkomende telefonie met een eigen stem en begroeting",
   "Doorschakeling vanaf uw huidige nummer, alleen als u niet opneemt of buiten werktijd",
   "WhatsApp-, chat- en e-mailafhandeling",
   "Afspraken plannen, verzetten en bevestigen",
   "Kwalificatievragen voordat een lead wordt doorgezet",
   "Warme of koude doorverbinding naar een medewerker",
   "Gespreksverslag en samenvatting in het CRM",
   "Terugbelverzoeken met prioriteit",
 ],
 "traject": [
   ("Uw telefoon in kaart", "Wie belt er, waarover, en wat gebeurt er nu als niemand "
    "opneemt. Meestal is één week meekijken genoeg om het patroon te zien."),
   ("Grenzen vastleggen", "Wat mag de AI-medewerker zelf afhandelen, wat vraagt hij na, en "
    "wanneer draagt hij over. Dit is de belangrijkste stap; hier wordt hij betrouwbaar."),
   ("Inrichten en koppelen", "Diensten, prijzen, openingstijden, agenda en CRM. De "
    "doorschakeling wordt zo ingericht dat u zelf blijft opnemen als u kunt."),
   ("Meeluisteren en bijstellen", "De eerste periode leest u de gespreksverslagen mee en "
    "wordt bijgesteld wat niet goed liep."),
   ("Uitbreiden", "Pas als telefonie staat, komen WhatsApp, chat of e-mail erbij."),
 ],
 "koppelingen": [
   "Uw bestaande telefoonnummer, via doorschakeling",
   "Agenda's en boekingssystemen",
   "Het CRM of Business OS van Capital BB",
   "WhatsApp Business",
   "E-mail en de formulieren van de website",
 ],
 "prijsuitleg": ("Inrichting vanaf €750 eenmalig, exclusief btw: uitvragen, instructies, "
   "stem, koppelingen en het bijstellen in de eerste periode. Daarbovenop komt verbruik: "
   "telefonieminuten en AI-gebruik. Dat verbruik wordt apart doorbelast en niet in een vast "
   "bedrag verstopt, zodat u ziet waar het geld heen gaat. Gekoppeld aan een "
   "CRM-abonnement vanaf €159 per maand wordt de AI-medewerker onderdeel van uw systeem in "
   "plaats van een losse tool."),
 "verschil": [
   ("Voicemail",
    "Kost niets en levert bijna niets op: de meeste bellers hangen op zonder in te spreken."),
   ("Een antwoordservice",
    "Er neemt een mens op, maar die kent uw vak niet, kan niet in uw agenda plannen en geeft "
    "meestal alleen een terugbelnotitie door."),
   ("Een chatbot op de website",
    "Helpt alleen wie al op uw site is. De telefoon blijft ondertussen overgaan."),
   ("Een AI-medewerker",
    "Neemt op, kent uw diensten en tarieven, plant in uw eigen agenda, draagt over wanneer "
    "het moet en legt alles vast in het CRM."),
 ],
 "verwachting": ("U mag verwachten dat er wordt opgenomen, dat veelgestelde vragen goed worden "
   "beantwoord, dat afspraken kloppen en dat u niets meer misloopt zonder het te weten. Wat "
   "wij niet beloven: dat hij elk gesprek aankan. Een AI-medewerker is bewust begrensd, en "
   "een gesprek dat buiten die grenzen valt hoort bij u terecht te komen, niet bij een "
   "systeem dat gaat gokken."),
 "branches": [
   ("Kapsalons en barbershops", "De telefoon gaat terwijl er geknipt wordt. Afspraken en "
    "openingstijden zijn negen van de tien vragen."),
   ("Autobedrijven", "Vragen over een specifieke occasion, proefritten en inruil, ook 's "
    "avonds als de zaak dicht is."),
   ("Schilders en klusbedrijven", "Bellers willen weten of u in hun regio werkt en wanneer u "
    "kunt komen kijken. Dat is uit te vragen zonder dat u van de ladder komt."),
   ("Verkooporganisaties", "Inkomende leads worden gekwalificeerd voordat ze bij een "
    "accountmanager landen."),
 ],
},

"crm": {
 "vraag": "Wat is een CRM-systeem?",
 "definitie": ("Een CRM is het systeem waarin al uw klantcontact bij elkaar staat: contacten, "
   "leads, offertes, afspraken, gespreksnotities en opvolgtaken. Bij Capital BB is het CRM "
   "geen los pakket maar het punt waar website, telefonie en AI-medewerker samenkomen. "
   "Vanaf €159 per maand plus €395 inrichting, exclusief btw."),
 "voor_wie": [
   "Bedrijven die klanten nu bijhouden in Excel, hun telefoon en hun hoofd tegelijk",
   "Ondernemers die offertes de deur uit doen en daarna vergeten na te bellen",
   "Verkooporganisaties met meerdere mensen op dezelfde leads",
   "Bedrijven die groeien en merken dat overdracht tussen mensen misgaat",
 ],
 "probleem": ("Zonder één plek leeft klantinformatie op vier plekken: een lijst in Excel, een "
   "appgesprek, een mailbox en het geheugen van degene die het gesprek voerde. Offertes "
   "blijven liggen omdat niemand ze bewaakt, en als iemand ziek is of vertrekt, gaat de "
   "klantrelatie mee."),
 "bouwt": [
   ("Één klantkaart",
    "Alle contactmomenten, offertes, afspraken en documenten van één klant op één plek, "
    "zichtbaar voor iedereen die het mag zien."),
   ("Een pipeline die uw verkoop volgt",
    "De fases die u werkelijk gebruikt, niet die van een standaardpakket. Van eerste contact "
    "tot opdracht, met de opvolgtaken die daarbij horen."),
   ("Opvolging die vanzelf gaat",
    "Een offerte die vijf dagen stil is, geeft zelf een seintje. Bevestigingen, "
    "herinneringen en reviewverzoeken gaan automatisch de deur uit."),
   ("Aansluiting op de rest",
    "Aanvragen van de website komen er rechtstreeks in, gesprekken van de AI-medewerker ook, "
    "en wat u in het CRM vastlegt kan weer een automatisering starten."),
 ],
 "onderdelen": [
   "Contacten, bedrijven en relaties",
   "Leads met bron, status en eigenaar",
   "Offertes met versies en akkoord",
   "Taken, herinneringen en opvolgmomenten",
   "Rollen en rechten per medewerker",
   "Rapportages en dashboards",
   "Een klantportaal voor uw eigen klanten",
   "Meerdere pipelines voor verschillende diensten",
   "Documenten en bijlagen bij de klantkaart",
 ],
 "traject": [
   ("Uw verkoopflow uittekenen", "Welke stappen doorloopt een klant bij u werkelijk, en waar "
    "blijft het nu liggen. Het systeem volgt uw proces, niet andersom."),
   ("Voorstel bouwen", "U krijgt een ingerichte omgeving te zien met uw eigen fases en "
    "velden, voordat u beslist."),
   ("Gegevens overzetten", "Bestaande klantgegevens uit Excel, een oud CRM of een "
    "boekhoudpakket worden gemigreerd. Datamigratie vanaf €295 exclusief btw."),
   ("Koppelen", "Website, e-mail, telefonie en agenda. Eenvoudige koppeling vanaf €295, "
    "standaard API-koppeling vanaf €650, complexe koppeling vanaf €1.250."),
   ("Invoeren en bijstellen", "Uitleg voor uw team en bijsturen in de eerste weken. Een CRM "
    "dat niemand gebruikt, is geld weggooien."),
 ],
 "koppelingen": [
   "De website en haar formulieren",
   "E-mail",
   "Telefonie en de AI-medewerker",
   "WhatsApp Business",
   "Agenda's en boekingssystemen",
   "Boekhoud- en facturatiepakketten, via API",
 ],
 "prijsuitleg": ("Een maandbedrag plus eenmalige inrichting, exclusief btw. CRM Start €159 per "
   "maand plus €395 inrichting, tot vijf gebruikers. CRM Groei €269 per maand plus €695, tot "
   "vijftien gebruikers, met offertes, automatische opvolging, rapportages en één "
   "koppeling. CRM Pro €495 per maand plus €1.250, tot 35 gebruikers, met klantportaal, "
   "meerdere pipelines en maatwerkdashboards. Wat de prijs bepaalt: het aantal gebruikers, "
   "het aantal koppelingen en hoeveel van uw proces afwijkt van de standaard."),
 "verschil": [
   ("Excel of een gedeeld document",
    "Gratis en vertrouwd, maar niemand wordt herinnerd, er is geen historie per klant en "
    "twee mensen overschrijven elkaar."),
   ("Een standaard CRM-pakket",
    "Snel te starten en goedkoop per gebruiker, maar u past uw proces aan het pakket aan. "
    "Koppelen met uw eigen systemen kost vaak extra abonnementen."),
   ("Een CRM van Capital BB",
    "Ingericht op uw verkoopflow, gekoppeld aan uw website en telefonie, en uit te breiden "
    "naar een Business OS zonder over te stappen."),
   ("Een Business OS",
    "Gaat verder dan klantcontact: ook projecten, planning, medewerkers en documenten. "
    "Zinvol zodra meerdere afdelingen in hetzelfde systeem moeten werken."),
 ],
 "verwachting": ("U mag verwachten dat u van elke klant weet wat er speelt, dat offertes "
   "worden bewaakt, dat aanvragen niet meer verdwijnen en dat overdracht tussen mensen geen "
   "gat meer slaat. Wat wij niet beloven: dat een CRM vanzelf omzet maakt. Een systeem dat "
   "niet wordt bijgehouden levert niets op; daarom hoort invoering en uitleg bij het "
   "traject."),
 "branches": [
   ("Verkooporganisaties", "Meerdere mensen op dezelfde markt: eigenaarschap per lead, "
    "duidelijke fases en rapportage per medewerker."),
   ("Hypotheekadviseurs", "Lange dossiers met veel documenten en vaste controlemomenten; de "
    "klantkaart is het dossier."),
   ("Autobedrijven en caravanbedrijven", "Interesse in een specifiek voertuig, proefritten, "
    "inruil en opvolging na bezichtiging."),
   ("Klus- en installatiebedrijven", "Offerte, akkoord, inplannen en nafacturering vormen "
    "één keten in plaats van vier losse acties."),
 ],
},

"automatisering": {
 "vraag": "Wat betekent bedrijfsprocessen automatiseren?",
 "definitie": ("Automatisering betekent dat werk dat elke week op dezelfde manier terugkomt "
   "één keer wordt ingericht en daarna vanzelf gaat: bevestigingen, herinneringen, facturen, "
   "reviewverzoeken en het doorzetten van gegevens tussen systemen. Een bedrijfssysteem "
   "gaat een stap verder en digitaliseert een heel proces, zoals planning, werkbonnen of "
   "dossiers. Vanaf €219 per maand plus €695 inrichting, exclusief btw. Losse koppelingen "
   "vanaf €295 eenmalig."),
 "voor_wie": [
   "Bedrijven waar dezelfde gegevens in twee of drie systemen worden overgetypt",
   "Ondernemers die avonden kwijt zijn aan administratie die geen omzet oplevert",
   "Bedrijven waar planning en werkbonnen in Excel en WhatsApp tegelijk leven",
   "Groeiende bedrijven die merken dat handwerk niet meeschaalt",
 ],
 "probleem": ("Handwerk is niet alleen duur, het is ook onbetrouwbaar. Wie op vrijdagmiddag "
   "vijftig regels overtypt, maakt fouten, en de bevestiging die iemand vergeet te sturen "
   "kost een klant. Het probleem groeit bovendien mee: elke nieuwe opdracht is weer dezelfde "
   "handelingen."),
 "bouwt": [
   ("Terugkerend werk wegnemen",
    "Bevestigingen, herinneringen, facturen, reviewverzoeken en interne meldingen gaan "
    "vanzelf, op het moment dat er iets gebeurt in uw proces."),
   ("Systemen laten praten",
    "Wat in de website wordt ingevuld, komt in het CRM. Wat in het CRM wordt afgerond, gaat "
    "naar de boekhouding. Zonder tussenstap met kopiëren en plakken."),
   ("Een proces een systeem geven",
    "Planning, werkbonnen, aanvragen of dossiers krijgen een eigen omgeving met vaste "
    "stappen, statussen en verantwoordelijken, in plaats van een gedeelde map."),
   ("Zichtbaar maken wat er gebeurt",
    "Een dashboard dat laat zien wat er loopt, wat vastzit en wat er vandaag moet."),
 ],
 "onderdelen": [
   "Automatische bevestigingen en herinneringen",
   "Facturatie en betaalherinneringen",
   "Reviewverzoeken na afronding",
   "Koppelingen tussen website, CRM, agenda en boekhouding",
   "Digitale werkbonnen en urenregistratie",
   "Planning en toewijzing",
   "Dossiers met vaste controlemomenten",
   "Interne meldingen en escalaties",
   "Rapportages en dashboards",
 ],
 "traject": [
   ("Één proces kiezen", "Niet alles tegelijk. We beginnen bij het werk dat het vaakst "
    "terugkomt of het meest misgaat, want daar is de winst het duidelijkst."),
   ("Uittekenen zoals het echt gaat", "Inclusief de uitzonderingen, want juist daar "
    "sneuvelen automatiseringen die op papier klopten."),
   ("Bouwen en meedraaien", "De automatisering draait eerst naast het handwerk, zodat u kunt "
    "zien of hij hetzelfde doet als u."),
   ("Overzetten", "Pas als het klopt, gaat het handwerk eruit. Met een terugvalroute als er "
    "iets uitvalt."),
   ("Volgende proces", "Daarna het volgende. Zo groeit het systeem mee in plaats van dat u "
    "een half jaar wacht op een groot project."),
 ],
 "koppelingen": [
   "Website en formulieren",
   "CRM en Business OS",
   "Agenda's en planning",
   "Boekhoud- en facturatiepakketten",
   "E-mail, sms en WhatsApp",
   "Bestaande pakketten met een API",
   "Bestandsuitwisseling voor systemen zonder API",
 ],
 "prijsuitleg": ("Bedrijfssystemen zijn een abonnement plus inrichting, exclusief btw: Start "
   "€219 per maand plus €695 voor één proces, Groei €379 plus €1.195 voor meerdere verbonden "
   "processen, Pro €699 plus €2.250 voor een compleet intern platform. Losse automatisering "
   "wordt per koppeling geprijsd: eenvoudige koppeling vanaf €295, standaard API-koppeling "
   "vanaf €650, complexe koppeling vanaf €1.250. Datamigratie vanaf €295, een extra "
   "dashboard vanaf €395, en extra ontwikkeling op uurbasis vanaf €65, altijd na "
   "voorafgaand akkoord."),
 "verschil": [
   ("Zelf koppelen met een automatiseringstool",
    "Werkt voor eenvoudige stappen, maar u bent zelf de beheerder. Zodra een koppeling "
    "stilvalt of een pakket verandert, ligt het bij u."),
   ("Een standaardpakket dat het 'allemaal kan'",
    "Dekt tachtig procent en dwingt u de resterende twintig procent handmatig te blijven "
    "doen, meestal precies waar uw bedrijf zich onderscheidt."),
   ("Automatisering van Capital BB",
    "Ingericht op uw eigen proces, inclusief de uitzonderingen, met beheer en een "
    "terugvalroute als een koppeling uitvalt."),
 ],
 "verwachting": ("U mag verwachten dat terugkerend werk verdwijnt, dat gegevens niet meer "
   "worden overgetypt, en dat u ziet waar iets vastloopt. Wat wij niet beloven: een "
   "percentage tijdwinst. Hoeveel het scheelt hangt af van hoe vaak het werk terugkomt; dat "
   "rekenen we vooraf samen door op uw eigen aantallen."),
 "branches": [
   ("Klus- en installatiebedrijven", "Werkbon, uren en materiaal in één keer vastleggen, en "
    "de factuur die daaruit volgt."),
   ("Autobedrijven", "Aanbod bijwerken, afspraken bevestigen, en na aflevering automatisch om "
    "een review vragen."),
   ("Salons", "Herinneringen voor afspraken en het terughalen van klanten die al een tijd "
    "niet zijn geweest."),
   ("Hypotheekadviseurs", "Documenten opvragen en bewaken, met vaste controlemomenten per "
    "dossier."),
   ("Horeca", "Reserveringen, bevestigingen en personeelsplanning die op elkaar aansluiten."),
 ],
},

"business-os": {
 "vraag": "Wat is een Business OS?",
 "definitie": ("Een Business OS is één omgeving waarin het hele bedrijf draait: CRM, "
   "projecten, planning, medewerkers, documenten, rapportages en automatiseringen, in "
   "plaats van zeven losse abonnementen die elkaar niet kennen. Een CRM gaat over "
   "klantcontact; een Business OS gaat over het hele bedrijf. Vanaf €349 per maand plus "
   "€1.195 inrichting, exclusief btw."),
 "voor_wie": [
   "Bedrijven met meerdere afdelingen of rollen die van elkaar afhankelijk zijn",
   "Ondernemers die per maand aan vijf of meer softwareabonnementen betalen",
   "Bedrijven waar dezelfde klant in drie systemen staat, elke keer net anders",
   "Groeiende mkb-bedrijven waar overzicht het knelpunt is geworden, niet het werk",
 ],
 "probleem": ("Losse tools zijn stuk voor stuk goed en samen een probleem. Niemand weet welk "
   "systeem gelijk heeft, rapportages moeten met de hand worden samengevoegd, en elke "
   "nieuwe medewerker moet in vijf omgevingen worden aangezet en weer uit. De optelsom van "
   "de abonnementen valt bovendien vaak hoger uit dan één omgeving."),
 "bouwt": [
   ("Één waarheid over uw klanten en werk",
    "Klant, opdracht, planning, uren en documenten hangen aan elkaar. Wat op de ene plek "
    "verandert, klopt overal."),
   ("Modules die u werkelijk gebruikt",
    "CRM, projecten, planning, medewerkers, documenten en rapportage, maar alleen wat u "
    "nodig heeft. Er komt niets bij dat leeg blijft staan."),
   ("Rollen en rechten die kloppen",
    "Per rol bepalen wat iemand ziet en mag. Een monteur ziet zijn werkbonnen, geen marges; "
    "een medewerker die vertrekt gaat er op één plek uit."),
   ("Automatisering ingebouwd",
    "Omdat alles in één omgeving staat, hoeven processen niet eerst gekoppeld te worden "
    "voordat ze geautomatiseerd kunnen worden."),
 ],
 "onderdelen": [
   "CRM en verkooppipelines",
   "Projecten en opdrachten",
   "Planning en agenda's",
   "Medewerkers, rollen en rechten",
   "Urenregistratie",
   "Documenten en dossiers",
   "Een klantportaal",
   "Dashboards en rapportages",
   "Workflows en automatiseringen",
   "AI-functies, zoals samenvatten en voorbereiden",
 ],
 "traject": [
   ("Uw systemen in kaart", "Welke pakketten gebruikt u, wat kosten ze samen, welke gegevens "
    "staan waar dubbel, en wat gebeurt er tussen die systemen met de hand."),
   ("Kiezen wat vervalt en wat blijft", "Niet alles hoeft eruit. Een boekhoudpakket dat goed "
    "werkt, koppelen we liever dan dat we het vervangen."),
   ("Voorstel bouwen", "U ziet een ingerichte omgeving met uw eigen structuur voordat u "
    "beslist."),
   ("Gefaseerd overzetten", "Module voor module, met datamigratie en een periode waarin oud "
    "en nieuw naast elkaar draaien."),
   ("Uitbreiden", "Er kunnen later modules, koppelingen en automatiseringen bij. Het systeem "
    "is gebouwd om mee te groeien."),
 ],
 "koppelingen": [
   "Boekhouding en facturatie",
   "E-mail en agenda",
   "Telefonie en de AI-medewerker",
   "De website en haar formulieren",
   "WhatsApp Business",
   "Branchespecifieke pakketten met een API",
 ],
 "prijsuitleg": ("Een maandbedrag plus eenmalige inrichting, exclusief btw. OS Start €349 per "
   "maand plus €1.195 voor CRM, taken, basisplanning en een centraal dashboard. OS Groei "
   "€649 per maand plus €1.995 met projecten, medewerkers, documenten en workflows. OS "
   "Signature €1.095 per maand plus €3.495 met klantportaal, AI-functies en "
   "maatwerkautomatisering. Externe licenties en verbruik van AI, sms en e-mail worden apart "
   "doorbelast. Wat de prijs bepaalt: het aantal modules, het aantal gebruikers en de "
   "hoeveelheid maatwerk."),
 "verschil": [
   ("Losse tools naast elkaar",
    "Elk pakket is goed in zijn eigen ding, maar u betaalt meerdere keren, de gegevens lopen "
    "uiteen en het koppelwerk blijft van u."),
   ("Een CRM",
    "Genoeg zolang uw vraag over klantcontact gaat. Zodra planning, uren, documenten en "
    "medewerkers meedoen, loopt een CRM vol met dingen waar het niet voor is."),
   ("Een groot ERP-pakket",
    "Dekt alles, kost navenant en dwingt uw bedrijf in zijn model. Voor de meeste "
    "mkb-bedrijven te zwaar en te traag in te voeren."),
   ("Een Business OS van Capital BB",
    "Alleen de modules die u gebruikt, ingericht op uw manier van werken, gefaseerd in te "
    "voeren en later uit te breiden."),
 ],
 "verwachting": ("U mag verwachten dat u één plek heeft waar het klopt, dat rapportages niet "
   "meer met de hand worden samengevoegd, en dat nieuwe mensen sneller mee kunnen. Wat wij "
   "niet beloven: dat u per maand goedkoper uit bent dan de optelsom van uw huidige "
   "abonnementen. Dat rekenen we vooraf uit op uw eigen cijfers, en als het niet uitkomt "
   "zeggen we dat."),
 "branches": [
   ("Klus- en installatiebedrijven", "Offerte, planning, werkbon, uren en factuur als één "
    "keten, met monteurs die alleen hun eigen werk zien."),
   ("Verkooporganisaties", "Pipeline, targets, medewerkers en rapportage in één omgeving, "
    "zonder wekelijkse exportronde."),
   ("Autobedrijven en caravanbedrijven", "Voorraad, klanten, afspraken en werkplaats aan "
    "elkaar geknoopt."),
   ("Dienstverlenend mkb", "Projecten, uren, documenten en facturatie zonder dat iemand 's "
    "avonds nog gegevens overtypt."),
 ],
},

}


# ===========================================================================
# FAQ PER DIENSTPAGINA. Deze lijsten voeden zowel de zichtbare FAQ als het
# FAQPage-schema, zodat vraag en antwoord op de pagina letterlijk gelijk zijn
# aan de structured data. Nooit schema zonder zichtbare tekst.
# ===========================================================================
FAQ_DIENST = {

"online-marketing": [
 ("Wat kost online marketing bij Capital BB?",
  "Prijs op aanvraag. Dat is bewust: het aantal kanalen, of er content gemaakt moet worden en "
  "hoe vaak er wordt bijgestuurd lopen te ver uiteen voor een eerlijke vanafprijs. Wat "
  "vaststaat is dat het advertentiebudget los staat van het honorarium en rechtstreeks van u "
  "naar Google of Meta gaat."),
 ("Rekenen jullie een percentage over ons advertentiebudget?",
  "Nee. Dat is in de markt gebruikelijk, maar het beloont een hoger budget in plaats van een "
  "beter resultaat. U betaalt voor het werk, niet voor de hoogte van uw eigen budget."),
 ("Hoeveel advertentiebudget heb ik nodig?",
  "Dat rekenen we vooraf samen door op uw eigen cijfers: wat levert een gemiddelde opdracht "
  "op en hoeveel aanvragen worden klant. Komt daar geen werkbaar budget uit, dan zeggen we "
  "dat voordat u begint. Een bedrag noemen zonder die cijfers zou een slag in de lucht zijn."),
 ("Welke kanalen doen jullie?",
  "Google Ads, Meta (Facebook en Instagram), LinkedIn en andere kanalen waar uw klant zit, "
  "plus social media beheer, contentproductie en e-mailmarketing. Welke daarvan zinvol zijn "
  "hangt af van uw markt; we beginnen liever met \u00e9\u00e9n kanaal dat werkt dan met vier tegelijk."),
 ("Kunnen jullie ook de content maken?",
  "Ja: beeld, video, teksten en creatives voor de kanalen. Wat in een advertentie staat en "
  "wat op uw site staat, vertelt dan hetzelfde verhaal, wat scheelt in wat een bezoeker moet "
  "uitzoeken."),
 ("Wanneer zie ik resultaat?",
  "Een campagne heeft eerst data nodig voordat bijsturen zin heeft; reken op weken, niet op "
  "dagen. Wat u wel meteen ziet, is of er verkeer binnenkomt en waar het blijft steken."),
 ("Wat is het verschil met SEO en GEO?",
  "Adverteren levert verkeer zolang u betaalt en is direct aan en uit te zetten. SEO en GEO "
  "bouwen zichtbaarheid op die blijft, maar kosten maanden. Ze bijten elkaar niet: adverteren "
  "overbrugt de periode waarin de vindbaarheid nog moet groeien."),
 ("Kunnen we stoppen wanneer we willen?",
  "Ja. Advertentiebudget zet u zelf aan en uit. Over de opzegtermijn van het beheer maken we "
  "vooraf een afspraak; u zit niet vast aan een looptijd van jaren."),
],

"websites": [
 ("Wat kost een website bij Capital BB?",
  "Een website kost eenmalig vanaf €795 exclusief btw voor het Basis-pakket tot vijf "
  "pagina's. Premium is vanaf €1.595 tot tien pagina's, Signature vanaf €2.995 tot vijftien "
  "pagina's, en maatwerk met eigen functionaliteit en koppelingen begint bij €4.945. Wat u "
  "kiest bepaalt de prijs; het gesprek doet dat niet."),
 ("Hoe lang duurt het bouwen van een website?",
  "Dat hangt af van het pakket en vooral van hoe snel teksten, beelden en feedback "
  "beschikbaar zijn. U ziet eerst een werkend voorstel, en na uw akkoord volgt de volledige "
  "bouw. Wij geven een doorlooptijd af zodra duidelijk is wat er gebouwd wordt, in plaats "
  "van vooraf een termijn te noemen die van uw aanlevering afhangt."),
 ("Kan Capital BB onze teksten en structuur verzorgen?",
  "Ja. De structuur maken wij altijd: welke pagina's er komen, wat er op elke pagina moet "
  "gebeuren en waar de aanvraag valt. Teksten schrijven wij op basis van wat u vertelt, en u "
  "leest ze na voordat ze live gaan. Wij verzinnen geen claims die u niet kunt waarmaken."),
 ("Kunnen boekingen, offertes of WhatsApp worden gekoppeld?",
  "Ja. Denk aan een boekingssysteem zoals Salonized, Knipklok, Altegio of Afspraakpro, aan "
  "een agenda, aan WhatsApp Business, of aan een CRM waarin de aanvraag als lead landt. Een "
  "eenvoudige koppeling begint bij €295, een standaard API-koppeling bij €650 en een "
  "complexe koppeling bij €1.250, exclusief btw."),
 ("Blijven wij eigenaar van onze website?",
  "Ja. U blijft eigenaar van uw domein, uw teksten, uw beeldmateriaal en uw gegevens. "
  "Onderhoud is geen voorwaarde om de site te mogen houden."),
 ("Kan onze huidige website worden verbeterd in plaats van vervangen?",
  "Soms wel. Als de basis technisch in orde is, is verbeteren goedkoper dan opnieuw bouwen. "
  "De Website Performance Scan is bedoeld om precies dat vast te stellen: wat werkt, wat kan "
  "blijven, en wat vervangen moet worden. Als opnieuw bouwen niet nodig is, zeggen wij dat."),
 ("Is onderhoud verplicht?",
  "Nee. Hosting en techniek kost €25 per maand voor hosting, monitoring, beveiliging, "
  "back-ups en updates. Onderhoud kost €59 per maand met kleine wijzigingen erbij. Actieve groei kost €149 per maand met maandelijkse "
  "verbetering en voorrang. Zonder onderhoud blijft de site van u; het bijhouden ervan wordt "
  "dan uw eigen verantwoordelijkheid."),
],

"vindbaarheid": [
 ("Wat is GEO en hoe verschilt het van SEO?",
  "SEO richt zich op zoekmachines: gevonden worden tussen de zoekresultaten. GEO, Generative "
  "Engine Optimization, richt zich op AI-systemen zoals ChatGPT, Google AI Overviews, "
  "Perplexity en Copilot, die één antwoord geven in plaats van een lijst links. De "
  "technische basis is grotendeels dezelfde; het verschil zit in inhoud die zelfstandig "
  "citeerbaar is en in bedrijfsgegevens die overal exact gelijk zijn."),
 ("Wat kost SEO en GEO bij Capital BB?",
  "Vanaf €149 per maand exclusief btw voor technische controle, rapportage en kleine "
  "optimalisaties. €299 per maand met lokale SEO, bedrijfsprofiel en contentupdates. €499 "
  "per maand met doorlopende content, landingspagina's, autoriteitsopbouw en GEO-monitoring."),
 ("Hoe lang duurt het voordat ik er iets van merk?",
  "Technisch herstel werkt vrijwel meteen door in hoe uw site gelezen wordt. Zichtbaarheid "
  "opbouwen is werk van maanden, niet van weken, en hoe lang het duurt hangt af van uw markt "
  "en van waar u nu staat. Wie u binnen een maand resultaat belooft, weet dat zelf ook."),
 ("Kunnen jullie een plek in Google of in ChatGPT garanderen?",
  "Nee, en niemand kan dat. Wij bouwen wat de kans aantoonbaar vergroot: een technische "
  "basis die klopt, kloppende bedrijfsgegevens, structured data, citeerbare antwoorden en "
  "inhoudelijke autoriteit. Een vaste positie beloven zou een claim zijn over een systeem "
  "dat wij niet in de hand hebben."),
 ("Hoe wordt mijn bedrijf zichtbaar in AI-antwoorden?",
  "Door leesbaar en eenduidig te zijn. Dat betekent: AI-crawlers toegang geven, uw "
  "bedrijfsgegevens overal identiek houden, structured data met vaste identiteiten "
  "gebruiken, en inhoud publiceren waarin een vraag direct wordt beantwoord in een stuk "
  "tekst dat ook los van de pagina klopt. AI-systemen halen namelijk passages aan, geen hele "
  "pagina's."),
 ("Werkt dit ook als mijn website niet door Capital BB is gebouwd?",
  "Ja, mits de site technisch aanpasbaar is. Bij een site die op slot zit of waar de inhoud "
  "pas na JavaScript verschijnt, is de eerste stap soms een technische ingreep. De scan laat "
  "zien of dat het geval is."),
 ("Wat krijg ik maandelijks te zien?",
  "Een rapportage met wat er is gedaan, wat er is veranderd in vindbaarheid, en waar de "
  "aandacht de volgende maand heen gaat. Geen dashboard vol cijfers zonder uitleg."),
],

"ai-medewerkers": [
 ("Wat kan een AI-medewerker afhandelen?",
  "Veelgestelde vragen over uw diensten, prijzen, openingstijden en beschikbaarheid, "
  "afspraken inplannen, verzetten en bevestigen, en het kwalificeren van een aanvraag "
  "voordat die bij u terechtkomt. Alles wat u hem meegeeft, en niets daarbuiten."),
 ("Kan een AI-medewerker de telefoon opnemen?",
  "Ja. Uw bestaande nummer wordt doorgeschakeld, bijvoorbeeld alleen als u niet opneemt of "
  "buiten werktijd. U blijft dus gewoon zelf opnemen wanneer u kunt."),
 ("Kan de AI afspraken inplannen?",
  "Ja, rechtstreeks in uw agenda, alleen op tijden die u vrijgeeft en met de duur die bij de "
  "dienst hoort. De klant krijgt een bevestiging en de afspraak staat direct bij u in de "
  "agenda."),
 ("Kan een gesprek worden doorgestuurd naar een medewerker?",
  "Ja. U bepaalt wanneer: bij bepaalde onderwerpen, bij een bestaande klant, of gewoon als "
  "de beller erom vraagt. Doorverbinden kan direct, of als terugbelverzoek met de context "
  "van het gesprek erbij."),
 ("Wat gebeurt er als de AI een vraag niet begrijpt?",
  "Dan gaat hij niet gokken. Hij zegt dat hij het laat uitzoeken en zet het door als "
  "terugbelverzoek of doorverbinding. Die grens leggen wij vooraf samen vast; dat is de "
  "belangrijkste stap in de inrichting."),
 ("Hoe worden persoonsgegevens beschermd?",
  "Er wordt alleen vastgelegd wat nodig is om de vraag af te handelen: naam, "
  "contactgegevens, de afspraak en een gespreksverslag. Dat komt in uw eigen CRM te staan, "
  "en u blijft eigenaar van die gegevens. Welke gegevens worden bewaard en hoe lang, wordt "
  "vooraf vastgelegd voordat de AI-medewerker in gebruik gaat."),
 ("Welke verbruikskosten zijn er?",
  "Naast de inrichting vanaf €750 exclusief btw betaalt u voor telefonieminuten en "
  "AI-gebruik. Dat verbruik wordt apart doorbelast in plaats van in een vast bedrag verwerkt, "
  "zodat u ziet waar het geld heen gaat. Hoeveel het is, hangt af van hoeveel gesprekken er "
  "binnenkomen en hoe lang ze duren."),
],

"crm": [
 ("Wat kost een CRM-systeem voor een mkb-bedrijf?",
  "CRM Start kost €159 per maand plus €395 eenmalige inrichting, tot vijf gebruikers. CRM "
  "Groei kost €269 per maand plus €695, tot vijftien gebruikers, met offertes, automatische "
  "opvolging, rapportages en één koppeling. CRM Pro kost €495 per maand plus €1.250, tot 35 "
  "gebruikers, met klantportaal en maatwerkdashboards. Alles exclusief btw."),
 ("Kunnen bestaande klantgegevens worden overgezet?",
  "Ja. Gegevens uit Excel, een bestaand CRM of een boekhoudpakket worden gemigreerd, "
  "inclusief historie voor zover die exporteerbaar is. Datamigratie begint bij €295 "
  "exclusief btw; wat het wordt hangt af van de staat van de gegevens."),
 ("Kan het CRM worden aangepast aan onze eigen verkoopflow?",
  "Ja, en dat is het uitgangspunt. De fases, velden en opvolgmomenten volgen uw proces. Wij "
  "tekenen eerst uit hoe een klant bij u werkelijk binnenkomt en verder gaat, en richten "
  "daarna pas in."),
 ("Kunnen e-mail, telefonie en WhatsApp worden gekoppeld?",
  "Ja. E-mail, agenda, telefonie inclusief de AI-medewerker, WhatsApp Business en de "
  "formulieren van uw website. Een eenvoudige koppeling begint bij €295, een standaard "
  "API-koppeling bij €650 en een complexe koppeling bij €1.250, exclusief btw."),
 ("Wat is het verschil tussen een CRM en een Business OS?",
  "Een CRM gaat over klantcontact: contacten, leads, offertes en opvolging. Een Business OS "
  "gaat over het hele bedrijf en heeft daarnaast projecten, planning, medewerkers, "
  "documenten en rapportage in dezelfde omgeving. Beginnen met CRM en later doorgroeien kan; "
  "u hoeft daarvoor niet over te stappen."),
 ("Blijven wij eigenaar van onze gegevens?",
  "Ja. U blijft altijd eigenaar van uw eigen gegevens en kunt ze exporteren. Systemen hebben "
  "een minimale looptijd van 24 maanden en zijn daarna maandelijks opzegbaar; na de looptijd "
  "kunt u het systeem overnemen tegen zes maandtermijnen."),
 ("Hoe zorgen jullie dat het CRM ook echt gebruikt wordt?",
  "Door het op uw manier van werken in te richten in plaats van andersom, door de invoer zo "
  "klein mogelijk te houden, en door in de eerste weken mee te kijken en bij te stellen. Een "
  "CRM dat niemand bijhoudt, levert niets op."),
],

"automatisering": [
 ("Welke processen kunnen worden geautomatiseerd?",
  "Alles wat vaak terugkomt en volgens vaste regels verloopt: bevestigingen, herinneringen, "
  "facturen en betaalherinneringen, reviewverzoeken, het doorzetten van aanvragen naar het "
  "CRM, urenregistratie, werkbonnen, planning en interne meldingen. Werk dat elke keer een "
  "eigen afweging vraagt, hoort bij een mens te blijven."),
 ("Kunnen bestaande systemen worden gekoppeld?",
  "Ja, zolang er een API of een andere uitwisselmogelijkheid is. Voor pakketten zonder API "
  "is bestandsuitwisseling vaak nog een werkbare route. Een eenvoudige koppeling begint bij "
  "€295, een standaard API-koppeling bij €650 en een complexe koppeling bij €1.250, "
  "exclusief btw."),
 ("Moet ons hele bedrijfssysteem worden vervangen?",
  "Nee. We beginnen bij één proces: het werk dat het vaakst terugkomt of het meest misgaat. "
  "Wat goed werkt, blijft. Een boekhoudpakket dat prima draait koppelen we liever dan dat we "
  "het vervangen."),
 ("Wat kost een automatisering?",
  "Losse automatisering wordt per koppeling geprijsd, vanaf €295 eenmalig. Een "
  "bedrijfssysteem dat een heel proces digitaliseert kost vanaf €219 per maand plus €695 "
  "inrichting; meerdere verbonden processen vanaf €379 plus €1.195, en een compleet intern "
  "platform vanaf €699 plus €2.250. Alles exclusief btw."),
 ("Wat gebeurt er wanneer een koppeling uitvalt?",
  "Dan hoort u dat, niet uw klant. Automatiseringen worden gebouwd met foutmeldingen en een "
  "terugvalroute: het werk blijft klaarstaan tot de koppeling weer loopt, in plaats van "
  "stilletjes te verdwijnen. Bij een onderhoudsabonnement wordt daar ook op gemonitord."),
 ("Hoeveel tijd levert het op?",
  "Dat rekenen we vooraf door op uw eigen aantallen: hoe vaak komt het werk terug en hoe "
  "lang duurt het nu. Wij zetten geen percentage op een pagina dat wij niet kunnen aantonen. "
  "Komt de rekensom niet uit, dan zeggen we dat voordat u iets uitgeeft."),
],

"business-os": [
 ("Wat is een Business OS?",
  "Een Business OS is één omgeving waarin het hele bedrijf draait: CRM, projecten, planning, "
  "medewerkers, documenten, rapportages en automatiseringen bij elkaar, in plaats van losse "
  "abonnementen die elkaars gegevens niet kennen."),
 ("Voor welk type bedrijf is een Business OS geschikt?",
  "Voor bedrijven waar meerdere rollen of afdelingen van elkaar afhankelijk zijn, en waar "
  "dezelfde klant of opdracht nu in meerdere systemen staat. Bent u alleen of met z'n "
  "tweeën en gaat uw vraag vooral over klantcontact, dan is een CRM waarschijnlijk genoeg."),
 ("Wat is het verschil met een CRM?",
  "Een CRM gaat over klantcontact: contacten, leads, offertes en opvolging. Een Business OS "
  "gaat over het hele bedrijf en heeft daarnaast projecten, planning, uren, medewerkers en "
  "documenten in dezelfde omgeving. Met een CRM beginnen en later doorgroeien kan."),
 ("Kunnen bestaande tools worden vervangen of gekoppeld?",
  "Allebei kan. We brengen eerst in kaart wat u gebruikt en wat het samen kost. Pakketten "
  "die goed werken, zoals een boekhoudpakket, koppelen we liever dan dat we ze vervangen. "
  "Wat vooral dubbel werk oplevert, verdwijnt."),
 ("Kan het systeem later worden uitgebreid?",
  "Ja. Het wordt gefaseerd ingevoerd, module voor module, en er kunnen later modules, "
  "koppelingen en automatiseringen bij. U begint niet met een systeem waarvan u de helft nog "
  "niet gebruikt."),
 ("Hoe worden rollen en rechten geregeld?",
  "Per rol wordt vastgelegd wat iemand ziet en mag wijzigen. Een monteur ziet zijn eigen "
  "werkbonnen en niet uw marges; een medewerker die vertrekt wordt op één plek "
  "gedeactiveerd in plaats van in vijf systemen."),
 ("Wat kost een Business OS?",
  "OS Start kost €349 per maand plus €1.195 inrichting. OS Groei €649 per maand plus €1.995. "
  "OS Signature €1.095 per maand plus €3.495. Alles exclusief btw; externe licenties en "
  "verbruik van AI, sms en e-mail worden apart doorbelast."),
 ("Blijven wij eigenaar van onze gegevens?",
  "Ja. U blijft eigenaar van uw eigen gegevens en kunt ze exporteren. Systemen hebben een "
  "minimale looptijd van 24 maanden en zijn daarna maandelijks opzegbaar; na de looptijd "
  "kunt u het systeem overnemen tegen zes maandtermijnen."),
],

}


# ===========================================================================
# FAQ op de scanpagina. Ook hier: zichtbaar op de pagina, letterlijk gelijk
# aan het FAQPage-schema.
# ===========================================================================
FAQ_SCAN = [
 ("Wat kost de Website Performance Scan?",
  "Niets. De scan is kosteloos en u zit nergens aan vast. Er volgt geen automatische offerte "
  "en geen belrondje; u krijgt de bevindingen en beslist zelf wat u ermee doet."),
 ("Wat moet ik aanleveren?",
  "Alleen het adres van uw website, uw naam en waar u bereikbaar bent. U hoeft geen "
  "inloggegevens, geen toegang tot uw hosting en niets technisch aan te leveren."),
 ("Hoe snel krijg ik het resultaat?",
  "Binnen één werkdag. Er kijkt een mens naar voordat u iets krijgt, dus het is geen "
  "automatisch rapport dat een minuut later in uw mailbox valt."),
 ("Krijg ik een geautomatiseerd rapport of een echt oordeel?",
  "Een echt oordeel. Zeventien controlepunten worden nagelopen op wat de bezoeker meemaakt, "
  "of er iets binnenkomt, of u gevonden wordt, en de techniek eronder. U krijgt per punt te "
  "zien wat er misgaat en waaraan dat te zien is, plus wat er juist goed staat en niet "
  "aangeraakt hoeft te worden."),
 ("Moet ik daarna iets afnemen?",
  "Nee. Als uw site het goed doet, staat dat in de scan. Als verbeteren volstaat en opnieuw "
  "bouwen niet nodig is, zeggen wij dat ook. De scan is bedoeld om te weten waar u staat, "
  "niet als voorportaal van een verkoopgesprek."),
 ("Werkt de scan ook voor een website die niet door Capital BB is gebouwd?",
  "Ja. Verreweg de meeste scans gaan over sites die iemand anders heeft gemaakt. Wie de site "
  "gebouwd heeft, maakt voor de beoordeling niets uit."),
 ("Wat gebeurt er met mijn gegevens?",
  "Het formulier op deze site slaat niets op: het opent een WhatsApp- of e-mailbericht op uw "
  "eigen apparaat, dat u zelf verstuurt. Uw gegevens worden gebruikt om uw vraag te "
  "beantwoorden en niet gedeeld met derden. Zie de privacyverklaring."),
]

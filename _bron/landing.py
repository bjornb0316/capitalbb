# -*- coding: utf-8 -*-
"""
Koopintentiepagina's: één pagina per duidelijk afgebakende zoekvraag.

Uitgangspunt: een landingspagina bestaat alleen als hij iets zegt wat de
dienstpagina niet zegt. Waar de zoekvraag samenvalt met een dienstpagina die
er al staat, komt er géén tweede pagina maar een regel in BACKLOG. Twee
pagina's die hetzelfde beantwoorden, verdelen hun eigen zichtbaarheid en
lezen voor een bezoeker als een doolhof.

Vorm per pagina:
  titel        de <title>
  naam         naam in de structured data en in het kruimelpad
  beschrijving meta description
  h1           de zichtbare H1
  lede         de zin onder de H1
  spoor        hubpagina waar hij onder hangt
  ouder        dienstpagina waar hij onder hangt
  vraag        de zoekvraag, letterlijk, als kop van het antwoordblok
  antwoord     het antwoord daarop in één alinea die ook los citeerbaar is
  wel / niet   voor wie deze pagina wel en niet is
  secties      (kop, inleiding, [opsommingsregels]) - de eigen inhoud
  tabel        (kolomkop-a, kolomkop-b, [(rij-a, rij-b)]) of None
  prijs        (kop, tekst)
  faq          [(vraag, antwoord)]
  cta          (kop, tekst, knop, doel, tweede knop, tweede doel) voor het slotblok
  routes       HTML-regel met vervolglinks
"""

LANDING = {

# =========================================================================
# Branchepagina. Anders dan de koopintentiepagina's gaat deze over één soort
# bedrijf. Voorwaarde was: alleen publiceren met echte branchespecifieke
# inhoud, en demo's nooit als klantwerk presenteren. De elf demonstratiesites
# leveren die inhoud (echte boekingskoppelingen, echte prijslijsten, echt
# mobiel gedrag); ze staan hieronder ook expliciet als demonstratie benoemd.
"websites-voor-salons": {
 "titel": "Website voor kapsalons en beautysalons",
 "naam": "Websites voor salons",
 "beschrijving": ("Een salonwebsite die klanten laat boeken in plaats van bellen. Koppeling "
                  "met Salonized, Knipklok of Altegio, mobiel als uitgangspunt, en prijzen "
                  "die u zelf bijwerkt."),
 "h1": "Uw agenda vult zich,<br>ook als u aan het knippen bent.",
 "lede": ("Bijna al uw bezoekers komen op een telefoon, buiten werktijd, en willen één ding: "
          "zien of u vrij bent en dan boeken. De rest is bijzaak."),
 "spoor": "meer-klanten",
 "ouder": "websites",
 "vraag": "Wat heeft een kapsalon of beautysalon nodig aan een website?",
 "antwoord": ("Een salonwebsite heeft drie dingen nodig en verder weinig: een boekingsknop die "
              "op een telefoon werkt en gekoppeld is aan het agendasysteem dat u al gebruikt, "
              "een actuele prijslijst met uw behandelingen, en kloppende openingstijden die "
              "ook in Google staan. Alles daarnaast, van een uitgebreide fotogalerij tot een "
              "blog, is pas interessant als die drie staan. Bij Capital BB begint zo'n site "
              "bij \u20ac795 eenmalig, exclusief btw, inclusief koppeling met het boekingssysteem "
              "vanaf \u20ac295."),
 "wel": [
   "U werkt op afspraak en heeft een agenda- of boekingssysteem",
   "De telefoon gaat terwijl u met een klant bezig bent",
   "U staat nu vooral op Instagram of Facebook en niet op een eigen site",
   "Uw prijzen of behandelingen veranderen en u wilt dat zelf kunnen bijwerken",
   "U wilt gevonden worden door mensen die in uw buurt zoeken",
 ],
 "niet": [
   "U werkt zonder afspraak en heeft geen agenda om aan te koppelen; dan volstaat een "
   "eenvoudige pagina met openingstijden en route",
   "U zit vol en wilt er geen klanten bij",
   "U zoekt iemand die uw Instagram overneemt; dat is online marketing, geen website",
 ],
 "secties": [
   ("Hoe een salonklant u werkelijk vindt",
    "De route is bijna altijd dezelfde, en hij is korter dan bureaus u willen doen geloven. "
    "Wie dit patroon kent, weet ook waar het misgaat.",
    [
     "<b>Op de telefoon, meestal 's avonds.</b> Iemand bedenkt na het eten dat zijn haar "
     "eraan toe is. Dat is het moment waarop u niet opneemt.",
     "<b>Via Google Maps of Instagram.</b> Niet via een zoekopdracht op uw naam, maar via "
     "'kapper in de buurt' of een tip van een vriendin.",
     "<b>Eerste vraag: kan ik terecht?</b> Niet wie u bent, niet uw verhaal. Beschikbaarheid.",
     "<b>Tweede vraag: wat kost het?</b> Een salon zonder prijzen op de site wordt "
     "overgeslagen, omdat mensen ervan uitgaan dat het duur is.",
     "<b>Derde stap: boeken of wegklikken.</b> Is er geen knop, dan moet iemand bellen. "
     "Een deel doet dat, de rest gaat naar de volgende.",
    ]),
   ("Wat er in de praktijk misgaat",
    "Dit zijn de problemen die wij bij het bouwen van elf demonstratiesites voor salons keer "
    "op keer tegenkwamen.",
    [
     "<b>Openingstijden die niet kloppen.</b> Op de site staat iets anders dan in Google, en "
     "in Google staat iets anders dan de werkelijkheid rond de feestdagen.",
     "<b>Geen boekingsknop, of eentje die naar een inlogscherm leidt.</b> Dat is voor een "
     "nieuwe klant het einde van de route.",
     "<b>Prijzen in een pdf.</b> Onleesbaar op een telefoon, en niemand werkt hem bij.",
     "<b>De site is een Facebookpagina.</b> Werkt, tot Facebook de opmaak verandert of "
     "iemand geen account heeft.",
     "<b>Foto's van modellen in plaats van eigen werk.</b> Een klant wil zien wat úw handen "
     "doen, niet wat een fotostudio kan.",
     "<b>Alleen een contactformulier.</b> Dat is een drempel; een agenda is dat niet.",
    ]),
   ("Koppelen met het systeem dat u al gebruikt",
    "U hoeft niet over te stappen. Bij de demonstratiesites is steeds gekoppeld aan het "
    "boekingssysteem dat de zaak zelf al draaide.",
    [
     "<b>Salonized</b>, veel gebruikt in kapsalons en beautysalons",
     "<b>Knipklok</b>, met live beschikbaarheid",
     "<b>Altegio</b>, ook voor nagelstudio's en beautystudio's",
     "<b>Afspraakpro</b>, bij zaken die er al jaren mee werken",
     "<b>Treatwell</b> of een andere marktplaats, als u daar klanten vandaan haalt",
     "Werkt u met een eigen weekrooster zonder pakket? Dan kan er een eigen planner komen op "
     "uw echte openingstijden. Dat is bij één van de demo's ook zo gedaan.",
    ]),
   ("No-shows en aanbetalingen",
    "Een lege stoel is direct verlies, en bij lange behandelingen loopt dat op. Wat er "
    "technisch mogelijk is hangt af van uw boekingssysteem, maar dit zijn de routes.",
    [
     "Automatische herinnering per e-mail, sms of WhatsApp, een dag van tevoren",
     "Bevestiging direct na het boeken, zodat de afspraak in de agenda van de klant staat",
     "Een aanbetaling bij lange of dure behandelingen, als uw systeem dat ondersteunt",
     "Een annuleringstermijn die zichtbaar op de bevestiging staat, niet alleen in de "
     "kleine lettertjes",
     "Klanten die al een tijd niet zijn geweest automatisch terughalen",
    ]),
   ("Behandelingen, prijzen en foto's",
    "Dit is het deel dat u zelf moet kunnen bijwerken, want in deze branche verandert het.",
    [
     "Een prijslijst per behandeling die u zelf aanpast, geen pdf",
     "Duur per behandeling, zodat het boekingssysteem het juiste blok reserveert",
     "Toeslagen voor lang haar of extra tijd, vooraf zichtbaar in plaats van bij het afrekenen",
     "<b>Voor-en-na-foto's alleen met toestemming.</b> Een foto van een klant is een "
     "persoonsgegeven. Vraag het schriftelijk, ook bij een foto waarop het gezicht niet te "
     "zien is, en leg vast waar u hem gebruikt.",
     "Eigen foto's van uw zaak en uw werk wegen zwaarder dan beeldbankfoto's",
    ]),
   ("Lokaal gevonden worden",
    "Voor een salon is dit belangrijker dan alle andere vindbaarheid bij elkaar. Uw klanten "
    "komen uit een straal van een paar kilometer.",
    [
     "Een Google Bedrijfsprofiel met kloppende openingstijden, ook rond feestdagen",
     "Reviews vragen na de behandeling, op het moment dat iemand tevreden de deur uitgaat",
     "Uw behandelingen als diensten in het profiel, niet alleen 'kapsalon'",
     "Foto's in het profiel, want die worden vaker bekeken dan uw website",
     "Dezelfde naam, hetzelfde adres en hetzelfde telefoonnummer overal",
    ]),
 ],
 "tabel": ("Route", "Wat dat voor een salon betekent", [
   ("Alleen Instagram of Facebook",
    "Gratis en vertrouwd. U bent afhankelijk van hun opmaak, boeken kan meestal niet, en u "
    "komt niet naar boven bij iemand die in Google zoekt."),
   ("Alleen een profiel op een boekingsplatform",
    "Klanten kunnen boeken, maar het platform is de eigenaar van de relatie, rekent commissie "
    "en zet uw concurrent ernaast."),
   ("Een sjabloonsite van een salonpakket",
    "Snel klaar en goedkoop, maar hij lijkt op tientallen andere en past zich niet aan uw "
    "manier van werken aan."),
   ("Een eigen site van Capital BB",
    "Eigen ontwerp, gekoppeld aan het boekingssysteem dat u al gebruikt, prijzen die u zelf "
    "bijwerkt, en u houdt de klantrelatie. Vanaf \u20ac795 eenmalig."),
 ]),
 "prijs": ("Wat het kost",
   "Voor de meeste salons volstaat het Basis-pakket: vanaf \u20ac795 eenmalig exclusief btw, tot "
   "vijf pagina's, mobiel als uitgangspunt, met een contactformulier en de technische "
   "SEO-basis. Wilt u meer maatwerk in het ontwerp, dan begint Premium bij \u20ac1.595. De "
   "koppeling met uw boekingssysteem komt daarbovenop: een eenvoudige koppeling vanaf \u20ac295, "
   "een standaard API-koppeling vanaf \u20ac650. Onderhoud is daarna optioneel vanaf \u20ac39 per "
   "maand; zonder onderhoud blijft de site gewoon van u."),
 "faq": [
   ("Kan mijn bestaande boekingssysteem gekoppeld worden?",
    "Meestal wel. Bij de demonstratiesites is gekoppeld met Salonized, Knipklok, Altegio en "
    "Afspraakpro. Welke koppeling mogelijk is hangt af van wat uw pakket toelaat; dat zoeken "
    "we uit voordat er een prijs op tafel komt. Een eenvoudige koppeling begint bij \u20ac295 "
    "exclusief btw."),
   ("Ik werk zonder afspraak. Heeft een website dan zin?",
    "Ja, maar een andere. Dan draait het om openingstijden, route, prijzen en of het druk is, "
    "niet om een boekingsknop. Bij één van de demonstratiesites is de planner er bewust "
    "uitgelaten, omdat die zaak zonder afspraak werkt."),
   ("Kan ik mijn prijzen en behandelingen zelf aanpassen?",
    "Ja. Dat is in deze branche geen luxe maar noodzaak, want prijzen en behandelingen "
    "veranderen. U hoeft er niemand voor te bellen."),
   ("Mag ik foto's van klanten op mijn site zetten?",
    "Alleen met toestemming. Een foto van een klant is een persoonsgegeven, ook als het "
    "gezicht er niet op staat. Vraag het schriftelijk, bijvoorbeeld per WhatsApp, en leg vast "
    "waarvoor u de foto gebruikt. Eigen werkfoto's zijn overigens waardevoller dan "
    "beeldbankfoto's."),
   ("Hoe voorkom ik no-shows?",
    "Met een automatische herinnering een dag van tevoren, een bevestiging direct na het "
    "boeken, en bij lange behandelingen eventueel een aanbetaling. Wat kan, hangt af van uw "
    "boekingssysteem. Wij beloven geen percentage minder no-shows; dat hangt te veel af van "
    "uw klantenkring."),
   ("Wat kost een website voor een kapsalon?",
    "Vanaf \u20ac795 eenmalig exclusief btw voor het Basis-pakket, plus vanaf \u20ac295 voor de "
    "koppeling met uw boekingssysteem. Onderhoud is optioneel vanaf \u20ac39 per maand."),
   ("Word ik hiermee bovenaan gevonden in mijn plaats?",
    "Dat belooft niemand eerlijk, en wij ook niet. Wat wél helpt en wat wij bouwen: een site "
    "die technisch klopt, kloppende bedrijfsgegevens, en een Google Bedrijfsprofiel dat is "
    "ingevuld. Voor een salon doen reviews en dat profiel meestal meer dan de website zelf."),
   ("Ik heb al een site van mijn salonpakket. Is dit dan nodig?",
    "Niet per se. Werkt hij, wordt u gevonden en kunnen mensen boeken, dan is er geen reden om "
    "iets te vervangen. Laat hem gerust kosteloos beoordelen; als er niets hoeft te gebeuren, "
    "zeggen we dat."),
 ],
 "routes": ('Verder lezen: <a class="tekstlink" href="../werk/">bekijk de demonstratiesites'
            ' voor salons</a>, <a class="tekstlink" href="../websites/">alles over websites en'
            ' leadmachines</a>, <a class="tekstlink" href="../ai-telefoniste/">een AI-telefoniste'
            ' die opneemt terwijl u knipt</a> of <a class="tekstlink" href="../scan/">laat uw'
            ' huidige site beoordelen</a>.'),
 "cta": ("Zien hoe het voor uw salon werkt?",
  "Vertel welk boekingssysteem u gebruikt en hoe uw prijslijst eruitziet. Dan laten wij zien "
  "hoe dat er als site uitziet, inclusief de boekingsroute op een telefoon.",
  "Bespreek uw salon", "contact/?over=websites",
  "Of bekijk het gebouwde werk", "werk/"),
},

# =========================================================================
"website-laten-vernieuwen": {
 "titel": "Website laten vernieuwen of verbeteren?",
 "naam": "Website laten vernieuwen",
 "beschrijving": ("Vervangen of verbeteren, en wat gebeurt er met uw huidige vindbaarheid? "
                  "De afweging, wat u meeneemt, en hoe u voorkomt dat u bezoekers kwijtraakt "
                  "bij de overstap."),
 "h1": "Vernieuwen of verbeteren?<br>Meestal is het dat laatste.",
 "lede": ("De vraag is zelden of uw site mooier kan. De vraag is of hij zijn werk doet, en of "
          "opnieuw bouwen dat oplost of alleen duurder maakt."),
 "spoor": "meer-klanten",
 "ouder": "websites",
 "vraag": "Moet ik mijn website laten vernieuwen of alleen laten verbeteren?",
 "antwoord": ("Vernieuwen is zinvol als de technische basis niet meer deugt: de site is traag, "
              "werkt slecht op een telefoon, is niet meer bij te werken, of de inhoud staat pas "
              "in beeld nadat JavaScript is geladen. Is de basis in orde en gaat het vooral om "
              "structuur, teksten en de route naar een aanvraag, dan is verbeteren bijna altijd "
              "goedkoper en sneller. Bij Capital BB begint verbeterwerk bij \u20ac65 per uur na "
              "akkoord vooraf; een nieuwe site begint bij \u20ac795 eenmalig, exclusief btw. De "
              "Website Performance Scan is er om die keuze te maken voordat u geld uitgeeft."),
 "wel": [
   "U heeft een site die er niet meer uitziet zoals u zou willen",
   "Uw site is jaren geleden gebouwd en niemand durft hem nog aan te raken",
   "Op een telefoon klopt er iets niet, maar u weet niet wat",
   "U krijgt bezoekers maar nauwelijks aanvragen",
   "U twijfelt of u geld in de oude site moet steken of aan een nieuwe moet beginnen",
 ],
 "niet": [
   "U heeft nog geen website; dan is dit de verkeerde pagina",
   "U wilt alleen een andere kleur of een nieuw logo erin",
   "U zoekt iemand die uw bestaande bouwpakket beheert waar geen toegang toe is",
 ],
 "secties": [
   ("Wanneer verbeteren volstaat",
    "In de meeste gevallen. Een site die technisch gezond is, hoeft niet weg om beter te gaan "
    "presteren. Dit zijn de ingrepen die het vaakst het verschil maken zonder dat er iets "
    "opnieuw gebouwd wordt.",
    [
     "De structuur herzien: welke pagina beantwoordt welke vraag, en waar loopt het dood",
     "Teksten herschrijven zodat binnen vijf seconden duidelijk is wat u doet en voor wie",
     "Een duidelijke volgende stap op elke pagina, in plaats van vier knoppen die elkaar bijten",
     "Formulieren die ergens landen, gekoppeld aan mail, agenda, WhatsApp of een CRM",
     "Technische SEO: titels, beschrijvingen, structured data, interne links, laadgewicht",
     "Mobiel gedrag, contrast en toegankelijkheid nalopen",
    ]),
   ("Wanneer opnieuw bouwen de goedkopere keuze is",
    "Soms is doorpoetsen duurder dan opnieuw beginnen. Dat is het geval als u tegen de bodem "
    "van het gebouw aanloopt in plaats van tegen de inrichting.",
    [
     "<b>De site is niet meer bij te werken.</b> Verouderd systeem, geen updates meer, of "
     "niemand die er nog bij kan.",
     "<b>De inhoud staat niet in de HTML.</b> Verschijnt tekst pas na het laden van "
     "JavaScript, dan hebben zoekmachines en AI-systemen er weinig aan.",
     "<b>Elke wijziging kost een dagdeel.</b> Als een prijs aanpassen een ontwikkelaar vraagt, "
     "betaalt u dat de rest van de looptijd terug.",
     "<b>Er kan niets aan gekoppeld worden.</b> Geen agenda, geen CRM, geen boekingssysteem.",
     "<b>Het laadgewicht is niet te repareren.</b> Een thema met tien plug-ins wordt zelden "
     "licht.",
    ]),
   ("Wat er met uw vindbaarheid gebeurt",
    "Dit is het onderdeel waar het bij een nieuwe site het vaakst misgaat, en waar bijna "
    "niemand vooraf over begint. Een site vervangen zonder plan kost u de posities die u in "
    "jaren heeft opgebouwd.",
    [
     "<b>URL's blijven of krijgen een redirect.</b> Elke oude pagina die verdwijnt, krijgt een "
     "permanente doorverwijzing naar de opvolger. Zonder dat verliest u de waarde van elke "
     "link die ooit naar u wees.",
     "<b>Inhoud gaat mee.</b> Pagina's die verkeer opleveren worden niet zomaar geschrapt "
     "omdat ze niet in het nieuwe ontwerp passen.",
     "<b>Titels en beschrijvingen worden overgenomen of bewust verbeterd</b>, niet per ongeluk "
     "vervangen door de standaardtekst van een thema.",
     "<b>De site gaat niet op noindex live.</b> Klinkt vanzelfsprekend; het is een van de "
     "meest voorkomende fouten bij een lancering.",
     "<b>Na livegang wordt er gecontroleerd</b> of alles geïndexeerd wordt en of er geen "
     "kapotte links zijn ontstaan.",
    ]),
   ("Wat u meeneemt en wat u achterlaat",
    "U begint zelden bij nul. Wat er al is en werkt, blijft.",
    [
     "Uw domein blijft van u en gaat mee",
     "Teksten die kloppen worden hergebruikt, niet weggegooid om het weggooien",
     "Beeldmateriaal van uw eigen werk gaat mee",
     "Reviews en uw bedrijfsprofiel staan buiten de site en blijven staan",
     "Wat achterblijft: verouderde plug-ins, pagina's die niemand bezoekt en teksten die niets "
     "beweren",
    ]),
 ],
 "tabel": ("Keuze", "Wat dat in de praktijk betekent", [
   ("Niets doen",
    "Kost vandaag niets. Het verschil met concurrenten die wel doorontwikkelen wordt elk jaar "
    "groter, en technische achterstand wordt duurder naarmate u wacht."),
   ("Zelf wat bijschaven",
    "Prima voor teksten en foto's. Structuur, techniek en vindbaarheid blijven meestal liggen, "
    "omdat je moet weten waar je naar zoekt."),
   ("Verbeteren door Capital BB",
    "Structuur, teksten, techniek en de aanvraagroute, op de bestaande site. Vanaf \u20ac65 per "
    "uur na akkoord vooraf. Begint met de scan, zodat u weet wat er nodig is."),
   ("Opnieuw bouwen",
    "Vanaf \u20ac795 eenmalig. Zinvol als de basis niet meer deugt. Inclusief redirects van de "
    "oude URL's, zodat u uw opgebouwde vindbaarheid niet weggooit."),
 ]),
 "prijs": ("Wat het kost",
   "De Website Performance Scan is kosteloos en bepaalt welke kant het op moet. Verbeterwerk "
   "op een bestaande site gaat op uurbasis vanaf \u20ac65, altijd na een akkoord vooraf, zodat u "
   "nooit voor een verrassing staat. Opnieuw bouwen begint bij \u20ac795 eenmalig voor het "
   "Basis-pakket en loopt via \u20ac1.595 en \u20ac2.995 naar maatwerk vanaf \u20ac4.945. Alles exclusief "
   "btw. Het overzetten van bestaande inhoud en het instellen van redirects hoort bij de bouw "
   "en wordt niet apart in rekening gebracht."),
 "faq": [
   ("Moet ik mijn website vervangen of kan hij verbeterd worden?",
    "Dat hangt af van de technische basis. Is die in orde, dan is verbeteren bijna altijd "
    "goedkoper: structuur, teksten en de aanvraagroute leveren meer op dan een nieuw uiterlijk. "
    "Is de site niet meer bij te werken, traag of onleesbaar voor zoekmachines, dan is opnieuw "
    "bouwen de goedkopere keuze. De kosteloze scan bepaalt welke van de twee het is."),
   ("Verlies ik mijn positie in Google als ik een nieuwe site laat maken?",
    "Niet als het goed gebeurt. Elke oude URL die verdwijnt krijgt een permanente redirect naar "
    "de opvolger, pagina's die verkeer opleveren gaan mee, en na livegang wordt gecontroleerd "
    "of alles weer geïndexeerd wordt. Zonder dat plan raakt u wél waarde kwijt; dat is de "
    "meest voorkomende schade bij een nieuwe site."),
   ("Kan mijn huidige domein blijven?",
    "Ja. Uw domein blijft van u en gaat gewoon mee. Ook uw e-mailadressen op dat domein blijven "
    "werken; die staan los van de website."),
   ("Wat kost het verbeteren van een bestaande website?",
    "Verbeterwerk gaat op uurbasis vanaf \u20ac65 exclusief btw, altijd na een akkoord vooraf over "
    "wat er gedaan wordt. Wat er nodig is, komt uit de scan. Blijkt daaruit dat opnieuw bouwen "
    "verstandiger is, dan zeggen we dat, ook al is verbeteren voor ons de kleinere opdracht."),
   ("Hoe weet ik of mijn site technisch verouderd is?",
    "Signalen die er meestal op wijzen: hij laadt traag, op een telefoon klopt de opmaak niet, "
    "u kunt zelf niets aanpassen zonder hulp, er zit geen koppeling met agenda of CRM in, of u "
    "krijgt meldingen over updates die niemand doet. De scan maakt daar een oordeel van met "
    "zeventien controlepunten."),
   ("Gaan mijn teksten en foto's mee?",
    "Wat klopt en werkt gaat mee. Teksten worden hergebruikt of herschreven, niet weggegooid "
    "omdat het nieuw moet lijken. Beeldmateriaal van uw eigen werk of zaak neemt u gewoon mee."),
   ("Hoe lang ligt mijn site eruit tijdens de overstap?",
    "Niet. De nieuwe site wordt naast de bestaande gebouwd en gaat pas live als hij af en "
    "gecontroleerd is. Het omzetten zelf is een kwestie van minuten."),
 ],
 "routes": ('Verder lezen: <a class="tekstlink" href="../scan/">laat eerst uw huidige site '
            'beoordelen</a>, <a class="tekstlink" href="../website-laten-maken/">wat een nieuwe '
            'website kost en hoe het loopt</a>, <a class="tekstlink" href="../websites/">alles '
            'over websites en leadmachines</a> of <a class="tekstlink" href="../vindbaarheid/">'
            'hoe vindbaarheid werkt</a>.'),
 "cta": ("Laat eerst uw huidige website beoordelen.",
  "Zeventien controlepunten, beoordeeld door een mens, binnen \u00e9\u00e9n werkdag. U hoort wat werkt, "
  "wat weg kan, en of opnieuw bouwen \u00fcberhaupt nodig is. Blijkt verbeteren te volstaan, dan "
  "zeggen we dat.",
  "Vraag de scan aan", "scan/",
  "Of bespreek uw situatie", "contact/?over=websites"),
},

# =========================================================================
"website-laten-maken": {
 "titel": "Website laten maken: kosten en werkwijze",
 "naam": "Website laten maken",
 "beschrijving": ("Wat kost een website laten maken en hoe lang duurt het? Vanafprijzen vanaf "
                  "€795, het traject en wat u zelf aanlevert, zonder offertegesprek vooraf."),
 "h1": "Een website laten maken,<br>zonder verrassingen achteraf.",
 "lede": ("Wat het kost, hoe lang het duurt, wat u zelf moet aanleveren en waaraan u een "
          "goede bouwer herkent. Alles op één pagina, voordat u met iemand belt."),
 "spoor": "meer-klanten",
 "ouder": "websites",
 "vraag": "Wat kost het om een website te laten maken?",
 "antwoord": ("Een professionele website laten maken kost bij Capital BB eenmalig vanaf €795 "
              "exclusief btw voor een compacte site tot vijf pagina's, vanaf €1.595 voor een "
              "conversiegerichte site tot tien pagina's, vanaf €2.995 voor uitgesproken "
              "maatwerkdesign tot vijftien pagina's, en vanaf €4.945 zodra er eigen "
              "functionaliteit of koppelingen bij komen. Wat de prijs bepaalt is het aantal "
              "pagina's, de mate van maatwerk in het ontwerp en het aantal koppelingen met "
              "systemen die u al gebruikt. Onderhoud is daarna een keuze, vanaf €39 per maand, "
              "geen voorwaarde."),
 "wel": [
   "U wilt vooraf weten wat het kost, in plaats van na drie gesprekken",
   "U wilt zien wat u krijgt voordat u iets uitgeeft",
   "U wilt dat aanvragen ergens landen, niet in een vergeten postvak",
   "U wilt later kunnen koppelen aan een agenda, CRM of telefonie",
 ],
 "niet": [
   "U zoekt de goedkoopste site die er is; een bouwpakket is dan sneller",
   "U wilt alles zelf blijven bouwen en beheren",
   "U verwacht een gegarandeerd aantal aanvragen; dat belooft niemand eerlijk",
 ],
 "secties": [
   ("Wat bepaalt de prijs van een website?",
    "Vier dingen, en geen daarvan is hoe het gesprek loopt. Wie u een prijs noemt zonder "
    "deze vier te kennen, gokt.",
    [
     "<b>Omvang.</b> Vijf pagina's is een ander gebouw dan vijftien. Het aantal pagina's "
     "bepaalt de tekst, het ontwerp en de controle.",
     "<b>Mate van maatwerk.</b> Een verzorgde opzet binnen een bestaand designsysteem kost "
     "minder dan een ontwerp dat vanaf nul op uw merk wordt gemaakt.",
     "<b>Functionaliteit.</b> Een contactformulier is standaard. Offerteflows, "
     "afsprakenmodules, voorraad of een klantportaal zijn dat niet.",
     "<b>Koppelingen.</b> Een eenvoudige koppeling begint bij €295, een standaard "
     "API-koppeling bij €650, een complexe koppeling bij €1.250, exclusief btw.",
    ]),
   ("Hoe lang duurt het?",
    "Eerlijk antwoord: dat hangt vooral van ú af. De bouw is planbaar; het aanleveren van "
    "teksten, foto's en feedback is dat meestal niet. Daarom noemen wij pas een doorlooptijd "
    "als duidelijk is wat er gebouwd wordt, in plaats van een termijn te beloven die van uw "
    "aanlevering afhangt.",
    [
     "U ziet eerst een werkend voorstel, niet een offerte van zes kantjes",
     "Na uw akkoord start de volledige bouw, tegen de afgesproken prijs",
     "Vertraging komt in de praktijk bijna altijd uit het wachten op inhoud",
     "Wat u niet zelf kunt aanleveren, schrijven of maken wij, in overleg",
    ]),
   ("Wat moet u zelf aanleveren?",
    "Minder dan u denkt. De structuur maken wij altijd; de kennis over uw vak moet van u "
    "komen.",
    [
     "Wat u verkoopt, aan wie, en waarin u zich onderscheidt",
     "Uw prijzen of tarieven, voor zover u die wilt tonen",
     "Beeldmateriaal van uw werk, uw zaak of uzelf; ontbreekt dat, dan bespreken we een route",
     "Toegang tot uw domein, en tot een boekings- of agendasysteem als dat gekoppeld wordt",
     "Eén persoon die beslist. Vier meningen zonder beslisser kost meer tijd dan geld",
    ]),
   ("Waaraan herkent u een goede bouwer?",
    "Dit zijn de vragen die u aan iedere partij zou moeten stellen, ook aan ons.",
    [
     "Krijgt u iets te zien voordat u betaalt, of pas een offerte?",
     "Staat de prijs op de site, of hangt hij van het gesprek af?",
     "Blijft u eigenaar van uw domein, teksten en gegevens?",
     "Is onderhoud een keuze of een voorwaarde om de site te mogen houden?",
     "Kan de site later gekoppeld worden aan een CRM, agenda of telefonie?",
     "Wordt er vooraf gecontroleerd op mobiel gedrag, contrast en laadgewicht?",
     "Belooft iemand u een positie in Google? Dan weet u genoeg.",
    ]),
 ],
 "tabel": ("Route", "Wat dat in de praktijk betekent", [
   ("Zelf bouwen in een websitebouwer",
    "€0 tot een paar tientjes per maand. U bent zelf de bouwer, tekstschrijver en beheerder. "
    "Werkt prima voor een visitekaartje, zelden voor een site die aanvragen moet opleveren."),
   ("Een freelancer met een thema",
    "Vaak €500 tot €1.500. Ziet er verzorgd uit, maar de opbouw volgt het thema in plaats van "
    "uw verkoopverhaal, en koppelen kan meestal beperkt."),
   ("Een bureau met een vast traject",
    "Doorgaans vanaf enkele duizenden euro's, met een offertegesprek voordat u iets ziet."),
   ("Capital BB",
    "Vanaf €795 eenmalig, u ziet eerst een werkend voorstel, en wat u kiest bepaalt de prijs. "
    "Bevalt het voorstel niet, dan kost het niets."),
 ]),
 "prijs": ("De prijzen op een rij",
   "Basis €795, Premium €1.595, Signature €2.995 en maatwerk vanaf €4.945, allemaal eenmalig "
   "en exclusief btw. Betaling in drie delen: 40% bij opdracht, 40% na goedkeuring van het "
   "ontwerp en 20% voor livegang. Onderhoud daarna vanaf €39 per maand, en dat is een keuze."),
 "faq": [
   ("Wat kost het om een website te laten maken?",
    "Bij Capital BB eenmalig vanaf €795 exclusief btw voor het Basis-pakket tot vijf "
    "pagina's, vanaf €1.595 voor Premium tot tien pagina's, vanaf €2.995 voor Signature tot "
    "vijftien pagina's, en vanaf €4.945 voor maatwerk met eigen functionaliteit en "
    "koppelingen."),
   ("Moet ik eerst een offertegesprek in?",
    "Nee. De vanafprijzen staan open op de prijzenpagina, en u ziet eerst een werkend "
    "voorstel voordat u iets uitgeeft. Bevalt dat voorstel niet, dan kost het u niets."),
   ("Kan ik mijn bestaande domein behouden?",
    "Ja. U blijft eigenaar van uw domein, uw teksten, uw beeldmateriaal en uw gegevens. Het "
    "overzetten van een bestaand domein hoort bij de livegang."),
   ("Wat als ik nog geen teksten of foto's heb?",
    "Dan schrijven wij de teksten op basis van wat u vertelt, en bespreken we een route voor "
    "beeld. U leest alles na voordat het live gaat, en wij zetten geen claims op uw site die "
    "u niet kunt waarmaken."),
   ("Is onderhoud verplicht?",
    "Nee. Onderhoud is een keuze, vanaf €39 per maand voor hosting, monitoring, beveiliging, "
    "back-ups en updates. Zonder onderhoud blijft de site gewoon van u."),
   ("Wat als mijn huidige site eigenlijk goed genoeg is?",
    "Dan zeggen wij dat. De Website Performance Scan is bedoeld om vast te stellen wat werkt, "
    "wat weg kan en of opnieuw bouwen überhaupt nodig is. Verbeteren is vaak goedkoper dan "
    "vervangen."),
 ],
 "cta": ("Vraag een voorstel aan.",
  "U ziet eerst een werkend concept: aanklikbaar, in uw eigen kleuren, met uw eigen "
  "teksten. Bevalt het niet, dan kost het u niets en zit u nergens aan vast.",
  "Vraag een voorstel aan", "contact/?over=websites",
  "Of laat eerst uw huidige site beoordelen", "scan/"),
 "routes": ('Verder lezen: <a class="tekstlink" href="../websites/">alles over websites en '
            'leadmachines</a>, <a class="tekstlink" href="../werk/">gebouwd werk bekijken</a>, '
            '<a class="tekstlink" href="../prijzen/#websites">alle prijzen naast elkaar</a> of '
            '<a class="tekstlink" href="../werkwijze/">lees hoe een traject loopt</a>.'),
},

# =========================================================================
"website-voor-startende-ondernemer": {
 "titel": "Website voor startende ondernemers",
 "naam": "Website voor startende ondernemers",
 "beschrijving": ("Net gestart en nog geen website? Wat u wél en niet nodig heeft in het "
                  "eerste jaar, wat het kost vanaf €795, en hoe u voorkomt dat u over een jaar "
                  "opnieuw moet bouwen."),
 "h1": "Net gestart?<br>Bouw niet meteen alles.",
 "lede": ("In het eerste jaar heeft u geen tien pagina's nodig. U heeft er drie nodig die "
          "kloppen, en een site die later mee kan groeien zonder verbouwing."),
 "spoor": "meer-klanten",
 "ouder": "websites",
 "vraag": "Wat heeft een startende ondernemer echt nodig aan een website?",
 "antwoord": ("Een startende ondernemer heeft in het eerste jaar meestal genoeg aan een "
              "compacte site van drie tot vijf pagina's: wat u doet en voor wie, waarom "
              "iemand u zou vertrouwen, en één duidelijke manier om contact op te nemen of "
              "een afspraak te maken. Dat kost bij Capital BB eenmalig vanaf €795 exclusief "
              "btw. Belangrijker dan de omvang is dat de site later uit te breiden en te "
              "koppelen is, zodat u over een jaar niet opnieuw hoeft te beginnen."),
 "wel": [
   "U bent net ingeschreven of korter dan een jaar bezig",
   "U wilt serieus overkomen zonder er duizenden euro's tegenaan te gooien",
   "U weet nog niet precies hoe uw aanbod zich gaat ontwikkelen",
   "U wilt niet vastzitten aan een lang contract",
 ],
 "niet": [
   "U heeft al een lopend bedrijf met bestaande systemen; dan past de gewone route beter",
   "U wilt vanaf dag één een webshop met voorraad en betalingen",
   "U zoekt iemand die uw marketing overneemt; wij bouwen het systeem, niet uw campagnes",
 ],
 "secties": [
   ("Wat er in het eerste jaar wél toe doet",
    "Bezoekers die net van u gehoord hebben, zoeken drie dingen. Alles wat daar niet aan "
    "bijdraagt, kan wachten.",
    [
     "<b>Duidelijkheid.</b> Binnen vijf seconden moet er staan wat u doet en voor wie.",
     "<b>Vertrouwen.</b> Een gezicht, een naam, een KvK-nummer en echte contactgegevens doen "
     "meer dan een pagina vol beloftes.",
     "<b>Eén duidelijke actie.</b> Bellen, appen of een afspraak maken. Niet vier knoppen "
     "die elkaar beconcurreren.",
     "<b>Mobiel.</b> Vrijwel al uw eerste bezoekers komen op een telefoon binnen.",
    ]),
   ("Wat kan wachten",
    "Dit is geen bezuiniging, het is volgorde. Deze onderdelen zijn pas zinvol als u weet wat "
    "werkt.",
    [
     "Een blog of kennisbank: waardevol, maar alleen als u het volhoudt",
     "Tien dienstpagina's voordat u weet welke dienst het meest oplevert",
     "Een CRM voordat u genoeg klanten heeft om het bij te houden",
     "Een AI-medewerker voordat de telefoon regelmatig overgaat",
     "Doorlopende SEO voordat de site überhaupt af is",
    ]),
   ("Voorkom dat u over een jaar opnieuw begint",
    "De duurste website is de website die u na twaalf maanden weggooit. Dat gebeurt bijna "
    "altijd door dezelfde drie oorzaken.",
    [
     "Het domein staat op naam van de bouwer in plaats van op uw naam",
     "De site zit vast in een pakket waar u niet uit kunt exporteren",
     "Er kan niets aan gekoppeld worden, dus elke groeistap vraagt een nieuwe site",
    ]),
   ("Hoe het bij Capital BB loopt",
    "Dezelfde werkwijze als bij elk ander traject, ook bij het kleinste pakket.",
    [
     "U vertelt wat u doet en voor wie; wij maken de structuur",
     "U krijgt eerst een werkend voorstel te zien, geen offerte",
     "Bevalt het niet, dan kost het u niets",
     "Na akkoord wordt gebouwd tegen de afgesproken prijs, in drie termijnen",
     "Groeien kan later: extra pagina's, een CRM, koppelingen, een AI-medewerker",
    ]),
 ],
 "tabel": None,
 "prijs": ("Wat het kost om te beginnen",
   "Het Basis-pakket kost eenmalig vanaf €795 exclusief btw: tot vijf pagina's, responsive, "
   "een contactformulier, een technische SEO-basis en één correctieronde. Betaling in drie "
   "delen: 40% bij opdracht, 40% na goedkeuring van het ontwerp en 20% voor livegang. "
   "Onderhoud is daarna optioneel vanaf €39 per maand; u zit nergens aan vast."),
 "faq": [
   ("Wat kost een website voor een startende ondernemer?",
    "Vanaf €795 eenmalig exclusief btw voor het Basis-pakket: tot vijf pagina's, responsive, "
    "contactformulier, technische SEO-basis en één correctieronde. Betaling gaat in drie "
    "delen."),
   ("Kan ik klein beginnen en later uitbreiden?",
    "Ja, en dat is zelfs de bedoeling. Er kunnen later pagina's bij, en de site kan gekoppeld "
    "worden aan een CRM, een agenda of een AI-medewerker zonder dat hij opnieuw gebouwd moet "
    "worden."),
   ("Ik heb nog geen logo of huisstijl. Kan dat?",
    "Ja. Kleur, typografie en opbouw worden dan in het traject bepaald, op basis van uw vak "
    "en uw positie. U hoeft niet eerst naar een ander bureau voor een huisstijl."),
   ("Zit ik vast aan een contract?",
    "Nee. De website is een eenmalige opdracht. Onderhoud is een los abonnement dat u kunt "
    "nemen of laten; alleen systemen zoals CRM en Business OS hebben een minimale looptijd "
    "van 24 maanden."),
   ("Wie is eigenaar van de site en het domein?",
    "U. Uw domein, uw teksten, uw beeldmateriaal en uw gegevens blijven van u, ook als u "
    "geen onderhoud afneemt."),
   ("Heb ik als starter al SEO nodig?",
    "Een technische basis wel, en die zit in elk pakket. Een doorlopend SEO-abonnement is in "
    "het eerste jaar meestal nog niet aan de orde; eerst moet er iets staan om vindbaar te "
    "maken."),
 ],
 "cta": ("Vertel wat u gaat doen.",
  "U hoeft nog geen huisstijl, teksten of foto's te hebben. Wat u doet en voor wie is "
  "genoeg om een eerste voorstel te bouwen.",
  "Leg uw plan voor", "contact/?over=websites",
  "Of bekijk eerst de prijzen", "prijzen/"),
 "routes": ('Verder lezen: <a class="tekstlink" href="../website-laten-maken/">wat een website '
            'laten maken kost en hoe het loopt</a>, <a class="tekstlink" href="../websites/">'
            'alles over websites en leadmachines</a> of '
            '<a class="tekstlink" href="../prijzen/#websites">alle prijzen naast elkaar</a>.'),
},

# =========================================================================
"ai-telefoniste": {
 "titel": "AI-telefoniste die uw telefoon opneemt",
 "naam": "AI-telefoniste",
 "beschrijving": ("Een AI-telefoniste neemt op als u niet kunt, beantwoordt vragen en plant "
                  "afspraken in uw agenda. Wat hij wel en niet doet, en wat het kost vanaf "
                  "€750 inrichting."),
 "h1": "De telefoon gaat.<br>Er wordt opgenomen.",
 "lede": ("Een AI-telefoniste neemt op wanneer u dat niet kunt: buiten werktijd, tijdens een "
          "klus, of als u al in gesprek bent. Hij kent uw diensten, uw agenda en uw grenzen."),
 "spoor": "meer-klanten",
 "ouder": "ai-medewerkers",
 "vraag": "Wat doet een AI-telefoniste precies?",
 "antwoord": ("Een AI-telefoniste is een digitale medewerker die uw inkomende telefoongesprekken "
              "aanneemt wanneer u zelf niet opneemt. Hij beantwoordt veelgestelde vragen over "
              "uw diensten, prijzen, openingstijden en beschikbaarheid, plant afspraken in uw "
              "eigen agenda op tijden die u vrijgeeft, verbindt door of maakt een "
              "terugbelverzoek zodra het onderwerp buiten zijn grenzen valt, en legt elk "
              "gesprek vast in uw CRM. Bij Capital BB kost de inrichting vanaf €750 exclusief "
              "btw, plus verbruik voor telefonieminuten en AI-gebruik."),
 "wel": [
   "Uw telefoon gaat regelmatig over terwijl u niet kunt opnemen",
   "Veel bellers stellen dezelfde vragen: kan ik terecht, wat kost het, tot hoe laat bent u open",
   "U werkt met afspraken en heeft een agenda die gekoppeld kan worden",
   "U wilt buiten werktijd bereikbaar zijn zonder zelf op te nemen",
 ],
 "niet": [
   "Elk gesprek is uniek en vraagt vakinhoudelijke afweging",
   "U krijgt nauwelijks telefoon; dan is een goede website- en WhatsApp-route zinniger",
   "U verwacht dat hij álles overneemt; een AI-telefoniste hoort begrensd te zijn",
 ],
 "secties": [
   ("Wat hij wel doet",
    "Alles wat u hem meegeeft, en niets daarbuiten. Die grens leggen we vooraf samen vast; "
    "dat is de belangrijkste stap in de inrichting.",
    [
     "Opnemen met uw eigen begroeting en een stem die u kiest",
     "Vragen beantwoorden over diensten, prijzen, openingstijden en beschikbaarheid",
     "Afspraken inplannen, verzetten en bevestigen in uw eigen agenda",
     "Een aanvraag kwalificeren voordat hij bij u terechtkomt",
     "Doorverbinden, direct of als terugbelverzoek met de context erbij",
     "Elk gesprek samenvatten en vastleggen op de klantkaart in het CRM",
    ]),
   ("Wat hij bewust niet doet",
    "Een AI die alles probeert, gaat op enig moment gokken. Daarom is hij begrensd.",
    [
     "Korting geven of over prijzen onderhandelen",
     "Uitzonderingen toezeggen die u zelf zou willen beoordelen",
     "Klachten afhandelen",
     "Doen alsof hij een mens is; dat vertellen we gewoon als iemand ernaar vraagt",
     "Antwoord geven op iets wat hij niet zeker weet, in plaats van het door te zetten",
    ]),
   ("Hoe het doorschakelen werkt",
    "Uw nummer blijft uw nummer. U bepaalt zelf wanneer de AI-telefoniste aan zet is.",
    [
     "Alleen als u niet binnen een aantal keer overgaan opneemt",
     "Alleen buiten uw openingstijden",
     "Alleen als u al in gesprek bent",
     "Altijd, als u de telefoon volledig wilt laten aannemen",
     "U kunt op elk moment zelf opnemen; er verandert niets aan uw toestel",
    ]),
   ("Wat er gebeurt na het gesprek",
    "Een gesprek dat nergens landt, is alsnog een gemiste klant. Daarom hangt de telefoniste "
    "aan de rest van het systeem.",
    [
     "De afspraak staat direct in uw agenda, de klant heeft een bevestiging",
     "Er is een klantkaart met naam, contactgegevens en een gespreksverslag",
     "Een terugbelverzoek krijgt een prioriteit mee, zodat u weet wat eerst moet",
     "Vervolgacties, zoals een herinnering of een offerte, kunnen automatisch lopen",
    ]),
 ],
 "tabel": ("Alternatief", "Wat dat in de praktijk betekent", [
   ("Voicemail",
    "Kost niets en levert bijna niets op: de meeste bellers hangen op zonder in te spreken."),
   ("Een antwoordservice",
    "Er neemt een mens op, maar die kent uw vak niet, kan niet in uw agenda plannen en geeft "
    "meestal alleen een terugbelnotitie door."),
   ("Een collega die ertussendoor opneemt",
    "Werkt, tot het druk wordt. Dan wordt er niet opgenomen of wordt de klant afgeraffeld."),
   ("Een AI-telefoniste",
    "Neemt altijd op, kent uw diensten en tarieven, plant in uw eigen agenda, draagt over "
    "wanneer het moet en legt alles vast in het CRM."),
 ]),
 "prijs": ("Wat het kost",
   "Inrichting vanaf €750 eenmalig, exclusief btw: uitvragen, instructies, stem, koppelingen "
   "en het bijstellen in de eerste periode. Daarbovenop komt verbruik voor telefonieminuten "
   "en AI-gebruik, dat apart wordt doorbelast in plaats van in een vast bedrag verwerkt. "
   "Hoeveel dat is, hangt af van het aantal gesprekken en hun lengte. Gekoppeld aan een "
   "CRM-abonnement vanaf €159 per maand wordt de telefoniste onderdeel van uw systeem in "
   "plaats van een losse tool."),
 "faq": [
   ("Wat kost een AI-telefoniste?",
    "De inrichting begint bij €750 eenmalig exclusief btw. Daarnaast betaalt u verbruik voor "
    "telefonieminuten en AI-gebruik; dat wordt apart doorbelast, zodat u ziet waar het geld "
    "heen gaat."),
   ("Kan ik mijn eigen telefoonnummer houden?",
    "Ja. Uw bestaande nummer wordt doorgeschakeld, en u bepaalt wanneer: alleen als u niet "
    "opneemt, alleen buiten werktijd, alleen bij in gesprek, of altijd."),
   ("Merkt de beller dat hij met een AI praat?",
    "Dat verzwijgen wij niet. Als iemand ernaar vraagt, zegt de telefoniste dat hij een "
    "digitale assistent is. Doen alsof er een mens zit, levert op termijn alleen boze klanten "
    "op."),
   ("Wat gebeurt er als hij een vraag niet begrijpt?",
    "Dan gaat hij niet gokken. Hij zegt dat hij het laat uitzoeken en zet het door als "
    "terugbelverzoek of doorverbinding, met de context van het gesprek erbij."),
   ("Kan hij afspraken in mijn agenda zetten?",
    "Ja, rechtstreeks, en alleen op tijden die u vrijgeeft, met de duur die bij de dienst "
    "hoort. De klant krijgt een bevestiging."),
   ("Hoe zit het met persoonsgegevens?",
    "Er wordt alleen vastgelegd wat nodig is om de vraag af te handelen: naam, "
    "contactgegevens, de afspraak en een gespreksverslag. Dat komt in uw eigen CRM, en u "
    "blijft eigenaar van die gegevens. Wat wordt bewaard en hoe lang, leggen we vast voordat "
    "de telefoniste in gebruik gaat."),
   ("Werkt dit ook voor WhatsApp en e-mail?",
    "Ja, maar niet als eerste. We beginnen bij telefonie, omdat daar de meeste gesprekken "
    "verloren gaan. Zodra dat staat, kunnen WhatsApp, chat en e-mail erbij."),
 ],
 "cta": ("Test het op uw eigen telefoon.",
  "Noem één gesprek dat u deze week miste. Wij werken uit wat een AI-telefoniste daarin "
  "had gezegd, welke vraag hij had gesteld en wat er in uw agenda was komen te staan.",
  "Leg één gemiste oproep voor", "contact/?over=ai-medewerkers",
  "Of bekijk wat het kost", "prijzen/"),
 "routes": ('Verder lezen: <a class="tekstlink" href="../ai-medewerkers/">alles over '
            'AI-medewerkers en AI-telefonie</a>, <a class="tekstlink" href="../crm/">het CRM '
            'waarin de gesprekken landen</a> of <a class="tekstlink" href="../prijzen/#doorlopend">'
            'alle prijzen naast elkaar</a>.'),
},

# =========================================================================
"maatwerk-crm-laten-maken": {
 "titel": "Maatwerk-CRM of een standaardpakket?",
 "naam": "Maatwerk CRM laten maken",
 "beschrijving": ("Wanneer heeft u een maatwerk-CRM nodig en wanneer volstaat een "
                  "standaardpakket? De vijf signalen, de afweging en de kosten vanaf €159 per "
                  "maand plus inrichting."),
 "h1": "Maatwerk-CRM,<br>of gewoon een pakket?",
 "lede": ("De meeste bedrijven hebben geen maatwerk nodig. Sommige wel, en die merken het "
          "meestal aan dezelfde signalen. Hier staat welke dat zijn."),
 "spoor": "slimmer-werken",
 "ouder": "crm",
 "vraag": "Wanneer heeft een bedrijf een maatwerk-CRM nodig?",
 "antwoord": ("Een maatwerk-CRM is zinvol zodra uw verkoop- of dossierproces structureel "
              "afwijkt van wat standaardpakketten aanbieden, zodra u belangrijke stappen "
              "buiten het systeem om in Excel of WhatsApp blijft doen, of zodra u meerdere "
              "abonnementen betaalt om onderdelen aan elkaar te knopen die in één omgeving "
              "hadden gekund. Is dat niet het geval, dan is een standaardpakket vrijwel altijd "
              "goedkoper en sneller. Bij Capital BB begint een op uw proces ingericht CRM bij "
              "€159 per maand plus €395 eenmalige inrichting, exclusief btw."),
 "wel": [
   "Uw proces heeft stappen die geen enkel pakket standaard kent",
   "Uw team blijft naast het CRM in Excel of WhatsApp werken",
   "U betaalt meerdere abonnementen om onderdelen te koppelen",
   "U wilt uw website, telefonie en opvolging in één keten hebben",
 ],
 "niet": [
   "U bent net begonnen en heeft nog geen vast proces; dan is maatwerk te vroeg",
   "Een standaardpakket dekt uw proces en het wordt daadwerkelijk gebruikt",
   "U zoekt vooral goedkoop; een pakket per gebruiker is dan lastig te verslaan",
 ],
 "secties": [
   ("De vijf signalen dat standaard niet meer volstaat",
    "Eén signaal is geen reden om over te stappen. Drie of meer wel.",
    [
     "<b>Schaduwadministratie.</b> Naast het CRM leeft er een Excel-bestand dat eigenlijk de "
     "waarheid is.",
     "<b>Verplichte omwegen.</b> Uw team vult velden in die niet kloppen, omdat het pakket "
     "geen betere plek biedt.",
     "<b>Koppelstapels.</b> U betaalt voor drie tussenlagen om twee systemen te laten praten.",
     "<b>Onzichtbare fases.</b> De belangrijkste stap in uw verkoop staat nergens in het "
     "systeem, dus niemand kan hem bewaken.",
     "<b>Rapportage met de hand.</b> Elke maand exporteren en samenvoegen om te weten waar u "
     "staat.",
    ]),
   ("Wat 'maatwerk' hier wel en niet betekent",
    "Maatwerk betekent niet dat alles vanaf nul wordt geprogrammeerd. Dat zou onnodig duur "
    "zijn en jaren duren.",
    [
     "Wél: uw eigen fases, velden, rollen, rechten en opvolgmomenten",
     "Wél: koppelingen met uw website, telefonie, agenda en boekhouding",
     "Wél: schermen en dashboards die tonen wat uw mensen echt nodig hebben",
     "Niet: een eigen databaseplatform bouwen omdat het kan",
     "Niet: functionaliteit die alleen bestaat omdat een concurrent hem heeft",
    ]),
   ("Hoe het traject loopt",
    "Eerst uittekenen, dan pas inrichten. Een CRM dat het proces van de bouwer volgt in "
    "plaats van dat van het bedrijf, wordt niet gebruikt.",
    [
     "Uw verkoop- of dossierflow uittekenen zoals hij echt gaat, inclusief uitzonderingen",
     "Een ingerichte omgeving met uw eigen fases te zien krijgen, voordat u beslist",
     "Bestaande klantgegevens migreren uit Excel, een oud CRM of de boekhouding",
     "Koppelen met website, e-mail, telefonie en agenda",
     "Invoeren, uitleggen en in de eerste weken bijstellen",
    ]),
   ("Wat er misgaat als u te vroeg of te laat overstapt",
    "Allebei komt voor, en allebei kost geld.",
    [
     "Te vroeg: u legt een proces vast dat nog verandert, en bouwt het volgend jaar opnieuw",
     "Te laat: uw gegevens staan zo verspreid dat de migratie het duurste onderdeel wordt",
     "Te groot beginnen: modules die niemand gebruikt, en een team dat afhaakt",
     "Te klein beginnen: binnen een half jaar weer een koppeling erbij plakken",
    ]),
 ],
 "tabel": ("Route", "Wat dat in de praktijk betekent", [
   ("Excel of een gedeeld document",
    "Gratis en vertrouwd. Geen herinneringen, geen historie per klant, en twee mensen "
    "overschrijven elkaar."),
   ("Een standaard CRM-pakket",
    "Snel te starten en goedkoop per gebruiker. U past uw proces aan het pakket aan, en "
    "koppelen kost vaak extra abonnementen."),
   ("Een CRM op maat ingericht door Capital BB",
    "Uw eigen fases en velden, gekoppeld aan website en telefonie, vanaf €159 per maand plus "
    "€395 inrichting. Uit te breiden naar een Business OS zonder over te stappen."),
   ("Volledig zelf laten programmeren",
    "Alles kan, maar u betaalt ook voor alles wat allang bestaat, inclusief het onderhoud "
    "daarvan."),
 ]),
 "prijs": ("Wat het kost",
   "CRM Start €159 per maand plus €395 inrichting, tot vijf gebruikers. CRM Groei €269 per "
   "maand plus €695, tot vijftien gebruikers, met offertes, automatische opvolging, "
   "rapportages en één koppeling. CRM Pro €495 per maand plus €1.250, tot 35 gebruikers, met "
   "klantportaal, meerdere pipelines en maatwerkdashboards. Alles exclusief btw. Extra "
   "koppelingen vanaf €295, datamigratie vanaf €295, een extra dashboard vanaf €395. "
   "Systemen hebben een minimale looptijd van 24 maanden en zijn daarna maandelijks "
   "opzegbaar; na de looptijd kunt u het systeem overnemen tegen zes maandtermijnen."),
 "faq": [
   ("Wat kost een maatwerk-CRM?",
    "Bij Capital BB begint een op uw proces ingericht CRM bij €159 per maand plus €395 "
    "eenmalige inrichting, exclusief btw. Meer gebruikers, meer koppelingen en meer maatwerk "
    "brengen u naar CRM Groei (€269 plus €695) of CRM Pro (€495 plus €1.250)."),
   ("Wat is het verschil met een standaardpakket?",
    "Bij een standaardpakket past u uw proces aan het systeem aan; hier gebeurt het "
    "omgekeerde. De fases, velden en opvolgmomenten volgen uw eigen verkoop- of dossierflow, "
    "en koppelingen met uw website en telefonie horen erbij in plaats van dat ze extra "
    "abonnementen kosten."),
   ("Kunnen onze bestaande gegevens mee?",
    "Ja. Gegevens uit Excel, een bestaand CRM of een boekhoudpakket worden gemigreerd, "
    "inclusief historie voor zover die exporteerbaar is. Datamigratie begint bij €295 "
    "exclusief btw."),
   ("Hoe lang duurt de invoering?",
    "Dat hangt af van het aantal gebruikers, het aantal koppelingen en de staat van uw "
    "bestaande gegevens. Wij geven een doorlooptijd af zodra uw proces is uitgetekend, niet "
    "ervoor."),
   ("Blijven wij eigenaar van onze gegevens?",
    "Ja. U blijft eigenaar en kunt exporteren. Na de minimale looptijd van 24 maanden is het "
    "maandelijks opzegbaar, en u kunt het systeem overnemen tegen zes maandtermijnen."),
   ("Kunnen we later doorgroeien naar een Business OS?",
    "Ja, zonder over te stappen. Een Business OS voegt projecten, planning, uren, medewerkers "
    "en documenten toe aan dezelfde omgeving."),
 ],
 "cta": ("Twijfelt u nog tussen maatwerk en een pakket?",
  "Leg uw proces voor, dan zeggen wij eerlijk welke kant het op moet. Volstaat een "
  "standaardpakket, dan hoort u dat, ook al verkopen wij het andere.",
  "Plan een CRM-demo", "contact/?over=crm",
  "Of bekijk de CRM-prijzen", "prijzen/"),
 "routes": ('Verder lezen: <a class="tekstlink" href="../crm/">alles over CRM voor '
            'verkoopopvolging</a>, <a class="tekstlink" href="../business-os/">bekijk een '
            'Business OS in de praktijk</a>, <a class="tekstlink" href="../automatisering/">'
            'lees hoe bedrijfsprocessen worden geautomatiseerd</a> of '
            '<a class="tekstlink" href="../prijzen/#crm">alle prijzen naast elkaar</a>.'),
},

# =========================================================================
"bedrijfsprocessen-automatiseren": {
 "titel": "Bedrijfsprocessen automatiseren: waar begint u?",
 "naam": "Bedrijfsprocessen automatiseren",
 "beschrijving": ("Welke bedrijfsprocessen kunt u automatiseren, hoe kiest u het eerste en wat "
                  "kost het vanaf €295 per koppeling? Een praktische afweging, geen "
                  "tooloverzicht."),
 "h1": "Begin bij één proces.<br>Niet bij een plan.",
 "lede": ("Bedrijven die alles tegelijk willen automatiseren, komen zelden verder dan de "
          "inventarisatie. Hier staat hoe u het eerste proces kiest en wat het oplevert."),
 "spoor": "slimmer-werken",
 "ouder": "automatisering",
 "vraag": "Welke bedrijfsprocessen kun je automatiseren?",
 "antwoord": ("Automatiseren loont bij werk dat vaak terugkomt en volgens vaste regels "
              "verloopt: bevestigingen en herinneringen versturen, facturen en "
              "betaalherinneringen, reviewverzoeken na afronding, aanvragen van de website "
              "doorzetten naar het CRM, urenregistratie, werkbonnen, planning en interne "
              "meldingen. Werk waarbij elke keer een eigen afweging nodig is, hoort bij een "
              "mens te blijven. Bij Capital BB begint een losse koppeling bij €295 eenmalig; "
              "een bedrijfssysteem dat een heel proces digitaliseert begint bij €219 per maand "
              "plus €695 inrichting, exclusief btw."),
 "wel": [
   "Dezelfde gegevens worden in twee of drie systemen overgetypt",
   "Er gaan wekelijks berichten uit die iemand met de hand verstuurt",
   "Planning of werkbonnen leven in Excel en WhatsApp tegelijk",
   "U merkt dat handwerk niet meeschaalt met de groei",
 ],
 "niet": [
   "Het werk komt een paar keer per jaar voor; dan verdient de bouw zich nooit terug",
   "Het proces verandert nog elke maand; eerst vastzetten, dan automatiseren",
   "Elke situatie vraagt een eigen beoordeling; dat is geen proces maar vakwerk",
 ],
 "secties": [
   ("Hoe u het eerste proces kiest",
    "Drie vragen, en het antwoord staat er meestal binnen tien minuten. Niet het meest "
    "ingewikkelde proces, maar het meest vermoeiende.",
    [
     "<b>Hoe vaak komt het voor?</b> Dagelijks of wekelijks werk verdient zich terug; "
     "maandelijks werk zelden.",
     "<b>Hoeveel tijd kost het per keer?</b> Vermenigvuldig dat met de frequentie; dat is uw "
     "budget.",
     "<b>Wat kost het als het misgaat?</b> Een vergeten bevestiging kost een klant, een "
     "vergeten factuur kost rente.",
     "<b>Verloopt het volgens vaste regels?</b> Zo niet, dan automatiseert u uw eigen "
     "onduidelijkheid.",
    ]),
   ("Wat er concreet geautomatiseerd wordt",
    "Dit is geen tooloverzicht maar wat er in de praktijk het vaakst uit het handwerk gaat.",
    [
     "Aanvragen van de website die rechtstreeks als lead in het CRM landen",
     "Bevestigingen en herinneringen voor afspraken, per e-mail, sms of WhatsApp",
     "Facturen en betaalherinneringen die volgen uit een afgeronde opdracht",
     "Reviewverzoeken op het moment dat het werk klaar is",
     "Werkbonnen en uren die in één handeling worden vastgelegd",
     "Gegevens die van het CRM naar de boekhouding gaan, zonder overtypen",
     "Interne meldingen als iets te lang blijft liggen",
    ]),
   ("Waarom automatiseringen mislukken",
    "Bijna nooit door de techniek. Vrijwel altijd door één van deze vier.",
    [
     "<b>De uitzonderingen zijn vergeten.</b> Op papier klopte het proces; in de praktijk "
     "wijkt één op de vijf gevallen af.",
     "<b>Er is geen terugvalroute.</b> Valt een koppeling uit, dan verdwijnt het werk in "
     "stilte in plaats van dat iemand een melding krijgt.",
     "<b>Te veel tegelijk.</b> Vijf processen naast elkaar, en niemand weet meer welke stap "
     "waar hoort.",
     "<b>Niemand is eigenaar.</b> Als een pakket verandert en er is geen beheerder, ligt het "
     "stil tot iemand het toevallig merkt.",
    ]),
   ("Hoe Capital BB het aanpakt",
    "Één proces tegelijk, en het handwerk gaat er pas uit als het bewezen hetzelfde doet.",
    [
     "Het proces uittekenen zoals het echt gaat, inclusief de uitzonderingen",
     "De automatisering eerst naast het handwerk laten draaien",
     "Pas overzetten als het klopt, met een terugvalroute als er iets uitvalt",
     "Foutmeldingen naar u, niet naar uw klant",
     "Daarna het volgende proces, in plaats van een half jaar wachten op een groot project",
    ]),
 ],
 "tabel": ("Route", "Wat dat in de praktijk betekent", [
   ("Handmatig blijven doen",
    "Geen investering, maar de kosten groeien mee met uw omzet en de fouten ook."),
   ("Zelf koppelen met een automatiseringstool",
    "Werkt voor eenvoudige stappen. U bent zelf de beheerder; valt er iets stil, dan ligt het "
    "bij u."),
   ("Een standaardpakket dat 'het allemaal kan'",
    "Dekt tachtig procent en dwingt u de rest handmatig te blijven doen, meestal precies waar "
    "u zich onderscheidt."),
   ("Automatisering door Capital BB",
    "Ingericht op uw eigen proces inclusief uitzonderingen, met beheer, foutmeldingen en een "
    "terugvalroute. Vanaf €295 per koppeling."),
 ]),
 "prijs": ("Wat het kost",
   "Losse automatisering wordt per koppeling geprijsd: eenvoudige koppeling vanaf €295, "
   "standaard API-koppeling vanaf €650, complexe koppeling vanaf €1.250. Datamigratie vanaf "
   "€295, een extra dashboard vanaf €395, extra ontwikkeling op uurbasis vanaf €65 na "
   "voorafgaand akkoord. Een bedrijfssysteem dat een heel proces digitaliseert kost vanaf "
   "€219 per maand plus €695 inrichting; meerdere verbonden processen vanaf €379 plus €1.195, "
   "een compleet intern platform vanaf €699 plus €2.250. Alles exclusief btw."),
 "faq": [
   ("Welke processen kan ik het beste als eerste automatiseren?",
    "Het werk dat het vaakst terugkomt of het meest misgaat. Bevestigingen en herinneringen, "
    "het doorzetten van websiteaanvragen naar het CRM en facturatie na afronding zijn in de "
    "praktijk de drie die zich het snelst terugverdienen."),
   ("Wat kost het automatiseren van een bedrijfsproces?",
    "Een losse koppeling begint bij €295 eenmalig, een standaard API-koppeling bij €650 en "
    "een complexe koppeling bij €1.250, exclusief btw. Een heel proces digitaliseren als "
    "bedrijfssysteem begint bij €219 per maand plus €695 inrichting."),
   ("Moet ik mijn huidige software vervangen?",
    "Nee. Wat goed werkt, blijft. Een boekhoudpakket dat prima draait koppelen we liever dan "
    "dat we het vervangen."),
   ("Wat als een koppeling uitvalt?",
    "Dan hoort u dat, niet uw klant. Er zit een foutmelding en een terugvalroute op: het werk "
    "blijft klaarstaan tot de koppeling weer loopt, in plaats van stilletjes te verdwijnen."),
   ("Hoeveel tijd bespaar ik hiermee?",
    "Dat rekenen we vooraf door op uw eigen aantallen: hoe vaak komt het werk terug en hoe "
    "lang duurt het nu. Wij zetten geen percentage op een pagina dat wij niet kunnen "
    "aantonen, en als de rekensom niet uitkomt zeggen we dat voordat u iets uitgeeft."),
   ("Kan dit ook zonder dat wij een CRM hebben?",
    "Ja. Losse koppelingen tussen bestaande systemen kunnen op zichzelf staan. Wel geldt: hoe "
    "meer losse systemen, hoe meer koppelwerk, en op enig moment is één omgeving goedkoper."),
 ],
 "cta": ("Welk proces kiest u als eerste?",
  "Noem het werk dat het vaakst terugkomt of het meest misgaat. Wij rekenen op uw eigen "
  "aantallen door wat het nu kost, en zeggen het als het zich niet terugverdient.",
  "Leg één proces voor", "contact/?over=automatisering",
  "Of bekijk gebouwd werk", "werk/"),
 "routes": ('Verder lezen: <a class="tekstlink" href="../automatisering/">alles over '
            'automatisering en bedrijfssystemen</a>, <a class="tekstlink" href="../crm/">bekijk '
            'CRM voor verkoopopvolging</a>, <a class="tekstlink" href="../business-os/">bekijk '
            'een Business OS in de praktijk</a> of '
            '<a class="tekstlink" href="../prijzen/#automatisering">alle prijzen naast elkaar</a>.'),
},

}


# ===========================================================================
# CONTENTBACKLOG. Voorgestelde pagina's die bewust nog niet gepubliceerd zijn,
# met de reden en wat er nodig is om ze wél te maken. Liever vijf pagina's die
# iets toevoegen dan tien die elkaar de vindbaarheid afsnoepen.
# ===========================================================================
BACKLOG = [
 ("/website-laten-maken-mkb/",
  "Overlapt vrijwel volledig met /website-laten-maken/. De zoekvraag is dezelfde, alleen met "
  "een doelgroep ervoor.",
  "Publiceren zodra er een eigen invalshoek is die de hoofdpagina niet dekt: bijvoorbeeld "
  "websites voor bedrijven die al een CRM, boekhoudpakket of planningssysteem draaien, met "
  "de koppelingen als kern van het verhaal."),
 ("/crm-systeem-mkb/",
  "De dienstpagina /crm/ richt zich al expliciet op mkb en verkoopteams; een tweede pagina "
  "voor dezelfde zoekvraag zou zichzelf beconcurreren.",
  "Alleen zinvol als /crm/ zich verbreedt en deze pagina de mkb-invalshoek overneemt, of als "
  "er genoeg eigen materiaal is over een specifieke teamgrootte of sector."),
 ("/business-os-mkb/",
  "Idem: /business-os/ richt zich al op groeiende mkb-bedrijven.",
  "Publiceren zodra er een gebouwd Business OS is dat als case getoond mag worden; dan draagt "
  "de pagina bewijs in plaats van herhaling."),
 ("/seo-en-geo-voor-bedrijven/",
  "De dienstpagina /vindbaarheid/ draagt deze titel al en beantwoordt dezelfde vraag.",
  "Losse pagina's per deelvraag zijn kansrijker dan een tweede overzichtspagina: bijvoorbeeld "
  "'Wat is GEO' als zelfstandig uitlegstuk, of 'AI-crawlers toegang geven' als technisch "
  "artikel."),
 ("/ai-medewerker-klantenservice/",
  "Overlapt sterk met /ai-telefoniste/, dat dezelfde oplossing beschrijft vanaf het kanaal "
  "waar de meeste gesprekken verloren gaan.",
  "Publiceren zodra er een ingerichte klantenservice-toepassing draait waarover concreet "
  "geschreven kan worden: welke vragen, welke kanalen, welke escalaties."),
 ("Branchepagina's (hypotheekadviseurs, autobedrijven, caravanbedrijven, salons, "
  "klusbedrijven, CRM voor verkooporganisaties)",
  "Er is voor deze branches wel materiaal (de demoreeks, het IJsseldal-designsysteem, de "
  "Jezz-Media-case), maar niet genoeg per branche om een pagina te vullen zonder een "
  "sjabloon met een vervangen branchenaam. Dat is precies wat er niet moet komen.",
  "Salons zijn gemaakt: /websites-voor-salons/, gebouwd op de elf demonstratiesites met "
  "echte boekingskoppelingen. Die pagina noemt de demo's ook expliciet demonstraties. "
  "Zodra de eerste echte salonklanten live staan, hoort daar een klantcase bij in "
  "_bron/cases.py met status 'klantcase'; dan kan de pagina van demonstratiebewijs naar "
  "klantbewijs. Hypotheekadviseurs zijn de logische volgende, met het IJsseldal-werk als "
  "basis, maar daarvoor is toestemming nodig om de praktijk bij naam te noemen."),
]

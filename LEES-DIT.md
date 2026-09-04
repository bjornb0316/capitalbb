# Capital BB, de site

Twintig pagina's, gebouwd uit één generator. De oude one-pager in `capital-bb\`
en de voorbeelden in `capital-bb-keuzes\` zijn hiermee vervangen; bewaren mag,
publiceren niet.

## Bekijken

```
python -m http.server 8330 --directory capital-bb-site
```

en dan http://localhost:8330. Dubbelklikken op een index.html werkt ook, maar
de links tussen pagina's verwachten een server of GitHub Pages.

## Zo zit hij in elkaar

De inhoud staat in vier bronbestanden in **`_bron\`**:

| Bestand | Wat erin staat |
|---|---|
| `inhoud.py` | Wat overal terugkomt: contact, prijzen, navigatie, de twee sporen, cases, de homepage-FAQ, de CTA's per pagina |
| `diensten.py` | De inhoudelijke verdieping van de zes dienstpagina's, plus de FAQ per dienst en de FAQ op /scan/ |
| `landing.py` | De koopintentiepagina's, en de contentbacklog van pagina's die bewust nog niet bestaan |
| `bouw.py` | De generator zelf: opmaak, structured data, sitemap, robots.txt, llms.txt |

Na een wijziging draai je:

```
python _bron/bouw.py
python _bron/controle.py
```

De eerste schrijft alle pagina's, de sitemap, robots.txt en llms.txt opnieuw.
De tweede controleert het resultaat en geeft exitcode 1 als er iets mis is. Je
bewerkt dus nooit een index.html met de hand; dat wordt bij de volgende bouw
overschreven.

De structuur is **probleemgestuurd aan de voorkant** (/meer-klanten en
/slimmer-werken als sporen op de homepage en in het menu), **dienstgestuurd
eronder** (/websites, /vindbaarheid, /ai-medewerkers, /crm, /automatisering,
/business-os), met daaronder **koopintentiepagina's** voor afgebakende
zoekvragen. Daarnaast /scan, /werk, /werkwijze, /prijzen, /contact en /privacy.

## De gereedschapskist in `_bron/`

| Script | Wat het doet |
|---|---|
| `bouw.py` | Bouwt alle pagina's, sitemap, robots.txt en llms.txt |
| `groeiplan.md` | 90-dagenplan voor autoriteit buiten de site om |
| `start-week-1-2.md` | Invulklare teksten: Bedrijfsprofiel, reviews, Search Console |
| `controle.py` | 22 controles op de gebouwde site; exitcode 1 bij een fout |
| `publiceer.py` | Zet `_site/` klaar met alleen publiceerbare bestanden |
| `mobiel.mjs` | Echte viewporttest op 390, 768 en 1440 via Chrome DevTools |
| `sleutel.py` | Zet de Web3Forms-sleutel en bouwt opnieuw |
| `indexnow.py` | Meldt gewijzigde pagina's aan bij Bing; proefdraait standaard |

De volgorde die er altijd toe doet:

```
python _bron/bouw.py
python _bron/controle.py
node _bron/mobiel.mjs      # site moet lokaal draaien op 8330
```

Lighthouse draaien kan met `npx lighthouse@12 http://localhost:8330/websites/`.
Voor Core Web Vitals volstaat meestal `mobiel.mjs` plus de meting in Search
Console zodra er echte bezoekers zijn; veldcijfers zeggen meer dan een
labscore.

## Wat `controle.py` nakijkt

JSON-LD geldig · geen dubbele `@id` · elke `@id`-verwijzing sluitend ·
zichtbaar kruimelpad gelijk aan BreadcrumbList · zichtbare FAQ letterlijk
gelijk aan FAQPage · canonicals · unieke titles en descriptions binnen de
lengtegrens · één H1 en geen gaten in de koppenhiërarchie · interne links
bestaan, met slash en zonder index.html · geen weespagina's · sitemap bevat
precies de indexeerbare pagina's · robots.txt intern consistent · llms.txt
verwijst alleen naar bestaande pagina's · alle prijzen gelijk aan `inhoud.py` ·
elke afbeelding heeft alt, width en height · lang, viewport en og-velden.

Draai hem na elke wijziging. Hij vangt precies de fouten die anders pas
maanden later in Search Console opduiken.

## Structured data: één graph, vaste identiteiten

Elke pagina draagt één JSON-LD-blok met één `@graph`. Daarin staan altijd
dezelfde vier entiteiten, met vaste ID's, zodat zoekmachines en AI-systemen
overal hetzelfde bedrijf zien:

```
https://capitalbb.nl/#organization    Organization + ProfessionalService
https://capitalbb.nl/#bjorn           Person, Björn Beerntsen
https://capitalbb.nl/#website         WebSite
https://capitalbb.nl/#logo            ImageObject
```

Daar komt per pagina bij: een `WebPage` (`<url>#webpage`), een
`BreadcrumbList` (`<url>#breadcrumb`), en op dienstpagina's een `Service`
(`<url>#service`) waarvan de `provider` naar `#organization` verwijst in plaats
van een nieuw inline bedrijf aan te maken.

De datum in `dateModified` en in de sitemap-`lastmod` komt uit één plek:
`GEWIJZIGD` bovenin `bouw.py`. Verhoog daar de datum van een pagina alleen als
de inhoud van díe pagina werkelijk is veranderd.

## Prijzen

Alle prijzen staan in `inhoud.py` en nergens anders als los getal. `controle.py`
controleert twee kanten op: elk bedrag op de site moet in `inhoud.py` staan, en
elke prijs uit `inhoud.py` moet ergens op de site zichtbaar zijn. Bedragen die
géén Capital BB-prijs zijn (de marktvergelijking op /website-laten-maken/)
staan als uitzondering in de witte lijst in `controle.py`.

## Publiceren gaat via GitHub Actions

Pages publiceerde eerder de hele repository vanaf de root van `main`. Daardoor
was `https://capitalbb.nl/_bron/inhoud.py` gewoon op te vragen. Dat is opgelost
met `.github/workflows/deploy.yml`: die bouwt de site, draait de controles, zet
alleen de publiceerbare bestanden in `_site/` en publiceert die map.

**Eenmalig instellen:** GitHub → repository → Settings → Pages → Build and
deployment → Source van *Deploy from a branch* naar **GitHub Actions**. Zolang
dat niet gebeurt, blijft de oude situatie bestaan en staat `_bron` nog online.

Faalt `controle.py` in de Action, dan stopt de deployment. Liever de oude site
online dan een nieuwe met kapotte structured data.

## Inhoud die per bestand ergens anders staat

| Bestand | Wat |
|---|---|
| `cases.py` | Het casemodel. Elke case heeft een verplichte status: klantcase, eigen-merk, demo of concept. Een `resultaat` zonder `bewijs` wordt geweigerd. Onderaan staat de aanleverchecklist voor nieuwe klanten. |
| `zoekintentie.py` | Welke pagina welke zoekvraag beantwoordt, en welke pagina's elkaar niet in de weg mogen zitten. Plus de beslismatrix van kandidaatpagina's. |
| `landing.py` | Koopintentiepagina's, de branchepagina voor salons, en de contentbacklog. |

## Dit moet handmatig in Cloudflare, buiten deze repository om

**1. Cloudflare blokkeert nu AI-crawlers, in strijd met wat de site wil.**
Cloudflare zet met "Managed robots.txt" een eigen blok bóven het bestand uit
deze repository. Daarin staan `Disallow: /` voor onder meer GPTBot, ClaudeBot,
Google-Extended, Applebot-Extended, Amazonbot, Bytespider, CCBot en
meta-externalagent, plus `Content-Signal: ai-train=no`. Dat is niet vanuit de
repository te overschrijven: een latere groep heft een eerdere `Disallow` niet
op. Wie wil dat AI-systemen de site mogen lezen, moet dit in het
Cloudflare-dashboard uitzetten bij **AI Crawl Control / robots.txt-beheer**.
Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, PerplexityBot en Claude-User
worden nu níet geblokkeerd; die konden altijd al lezen.

**2. `/_bron/` is publiek leesbaar.** `https://capitalbb.nl/_bron/inhoud.py`
geeft HTTP 200. robots.txt houdt crawlers weg maar blokkeert geen bezoekers.
Er staan geen wachtwoorden in, wel de volledige prijsopbouw en de bouwbron.
Op te lossen met een Cloudflare-regel die `/_bron/*` blokkeert, of door de
bronbestanden naar een aparte, niet-gepubliceerde repository te verhuizen.

**3. `https://capitalbb.nl/index.html` geeft HTTP 200 naast `/`.** GitHub Pages
kan dat niet redirecten. Een Cloudflare Redirect Rule van `/index.html` naar
`/` (301) ruimt dit duplicaat op. De canonical wijst al naar `/`, dus de schade
is beperkt; netter is het wel.

## De filmische hero

De zes onderdelen (Website, Leads, CRM, AI-medewerker, Automatisering,
Business OS) komen tijdens het scrollen uit de diepte en verbinden zich met
gouden draden. Dat is scrollgestuurd in moderne browsers; in oudere speelt
dezelfde opbouw vanzelf af zodra de hero in beeld is, en bij "verminderde
beweging" staat alles direct op zijn plek. De kop en de knoppen animeren
bewust niet mee: die staan er vanaf de eerste milliseconde.

## Conversie

- Elke pagina eindigt in een CTA die bij de intentie van díe pagina hoort. De
  scan is de primaire actie op /websites/ en /vindbaarheid/ en zakt elders naar
  de tweede plaats of maakt plaats voor iets relevanters. Zie
  `CTA_PER_PAGINA` in `inhoud.py` en `"cta"` per landingspagina in `landing.py`.
- Een CTA kan de dienst meegeven: `/contact/?over=crm` vult het vraagveld
  alvast in. De tekst komt uit `INTENTIES` in `inhoud.py`, nooit uit de URL
  zelf, en de bezoeker ziet en verstuurt hem zelf. De bezorging van het
  formulier is niet veranderd.
- Elke prijssectie heeft een directe actieknop eronder, met de juiste dienst.
- Op mobiel staat onderaan een vaste actiebalk, behalve op /scan en /contact
  zelf, want daar staat het formulier al.
- De scan heet Website Performance Scan en vraagt adres, naam en
  bereikbaarheid. Hoe het versturen werkt, staat hieronder.

## Formulieren

**Werkend en geverifieerd op 4 september 2026.** Beide formulieren zijn met een
echte inzending getest; contactformulier en scanformulier kwamen allebei aan in
bjorn@capitalbb.nl.

De verzending loopt via Web3Forms, want GitHub Pages heeft geen server die kan
mailen. De sleutel staat in `_bron/inhoud.py` bij `FORMULIER["sleutel"]`.

Sleutel wijzigen of wissen gaat het makkelijkst met:

```
python _bron/sleutel.py <nieuwe-sleutel>     # zetten, bouwen en controleren
python _bron/sleutel.py --wissen             # terug naar de mailroute
```

**Over de access key:** die staat zichtbaar in de HTML en dat hoort zo. Uit de
documentatie van Web3Forms: "Don't worry this can be public." Het is een
formuliersleutel, geen wachtwoord; iemand kan er hooguit formulieren mee naar
bjorn@capitalbb.nl sturen. Gebruik hem nooit voor iets anders.

**Domeinbeperking:** "Restrict to Domain" bestaat wel bij Web3Forms, maar is
een betaalde Pro-functie en is op het gratis plan niet beschikbaar. Wat er nu
tegen misbruik in zit: een eigen honeypot in de JS die de verzending blokkeert
voordat er iets weggaat, plus de server-side spamcontrole die Web3Forms zelf op
alle inzendingen draait. Komt er ooit echt spam binnen, dan is hCaptcha de
gratis volgende stap (wel een extern script, dus de privacyverklaring moet dan
mee).

Hoe het werkt:

- Inzendingen komen als e-mail binnen, met een leesbaar bericht plus de losse
  velden en de pagina waarvandaan het formulier is verstuurd.
- Heeft de bezoeker een e-mailadres achtergelaten, dan staat dat als
  `reply-to`, zodat je direct kunt antwoorden.
- Er zit een honeypot in (`botcheck`): een verborgen veld dat mensen nooit
  zien. Vult een bot hem in, dan wordt er niets verstuurd en ziet de bot een
  succesmelding.
- **Mislukt het versturen, dan valt het formulier terug op de mailroute.**
  Een lead gaat dus nooit verloren door een storing bij de verzenddienst.
  Welke terugval het is, staat in `FORMULIER["terugval"]` en is standaard
  e-mail.
- Na 15 seconden zonder antwoord wordt de verzending afgebroken en volgt
  diezelfde terugval, zodat niemand naar een dode knop zit te kijken. In een
  achtergrondtabblad kan die 15 seconden door de browser worden opgerekt; dat
  is geen probleem, want dan zit er ook niemand te wachten.
- Drie keer klikken of Enter levert één verzending op: het formulier houdt zelf
  bij dat het bezig is.
- De succesteksten en de privacyverklaring passen zich automatisch aan. Zolang
  de sleutel leeg is, zegt /privacy/ dat de site niets opslaat; zodra hij er
  is, beschrijft de pagina eerlijk dat het via Web3Forms naar de mailbox gaat
  en hoe lang het bewaard blijft. Zet nooit de een aan zonder de ander.

Gratis tot 250 inzendingen per maand. Wil je later liever een eigen route
(Cloudflare Worker + Resend), dan hoeft alleen de `fetch` in `js/site.js` te
veranderen; de rest van de opbouw blijft staan.

## WhatsApp

Op drie plekken:

- De zwevende bubbel rechtsonder, op elke pagina behalve /scan/ en /contact/.
- Een WhatsApp-knop onder elk CTA-blok, naast "of bel 06 14664161". Bewust een
  pil en geen derde `.btn`: het is een andere route, geen derde call to action.
- Onder het formulier op /scan/ en /contact/, waar de zwevende bubbel juist
  niet staat. Wie liever appt dan typt, hoeft daar niet te zoeken.

De tekst van het WhatsApp-bericht wordt per pagina meegegeven, zodat je meteen
ziet waar iemand vandaan komt.

## Publiceren

GitHub Desktop, `Add local repository`, deze map, publiceren zonder
"keep private". Let op: de map `_bron` wordt wél meegepubliceerd (zie het
Cloudflare-punt hierboven); `.nojekyll` schakelt de Jekyll-verwerking uit die
mappen met een underscore anders zou overslaan.

## Wat er nog niet in zit

- Een echte verzendroute voor formulieren (nu WhatsApp/mail-overdracht)
- Algemene voorwaarden
- Een foto van Björn; de Person-entiteit heeft daardoor geen `image`
- Bevestigde profielen om `sameAs` mee te vullen (LinkedIn, Google
  Bedrijfsprofiel). Zodra die er zijn: toevoegen in `_org_entiteit()`
- Een vestigingsadres in de structured data; nu alleen `areaServed: Nederland`
- Branchepagina's en vijf koopintentiepagina's: bewust nog niet gemaakt, met
  reden en plan in `BACKLOG` onderaan `_bron/landing.py`

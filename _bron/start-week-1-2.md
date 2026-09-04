# Week 1 en 2: invulklaar

Alles hieronder is kopieer-en-plak. Waar iets van jou moet komen staat
`[INVULLEN]`. Verzin niets in die velden waar je niet zeker van bent; een leeg
veld is beter dan een onjuist veld.

---

## 1. Google Bedrijfsprofiel

### Eerst dit beslissen: wel of geen adres tonen

Je werkt door heel Nederland en er is geen bevestigd bezoekadres. Kies dan
**servicegebied-bedrijf** (Service Area Business).

Belangrijk om te weten: Google vraagt **altijd** een adres om te verifiëren,
ook bij een servicegebied-bedrijf. Dat adres wordt dan **niet getoond** op je
profiel. Je thuisadres opgeven en verbergen is de gebruikelijke route voor
zzp'ers en kleine bedrijven. Wil je dat niet, dan is een Google
Bedrijfsprofiel geen optie, en dan vervalt ook het lokale pakket in Maps.

Ga naar https://business.google.com en kies "Bedrijf toevoegen".

### Invulvelden

| Veld | Wat invullen |
|---|---|
| Bedrijfsnaam | `Capital BB` |
| Categorie (hoofd) | `Websiteontwerper` |
| Categorieën (extra) | `Softwarebedrijf`, `Marketingbureau`, `Bedrijfsadviseur` |
| Adres | `[INVULLEN]` — en aanvinken dat je klanten bezoekt in plaats van andersom |
| Servicegebied | `Nederland`, of specifieker: `Arnhem`, `Duiven`, `Zevenaar`, `Doetinchem`, `Zutphen`, `Gelderland` |
| Telefoon | `06 14664161` |
| Website | `https://capitalbb.nl/` |
| Openingstijden | `[INVULLEN]` — zet liever niets dan iets wat niet klopt |

**Waarom niet de hoogst mogelijke categorie kiezen:** "Websiteontwerper" heeft
in Nederland veel zoekvolume en past bij wat de meeste klanten zoeken. De
extra categorieën vangen CRM en automatisering op. Meer dan vier categorieën
verwatert het profiel.

### Bedrijfsomschrijving (750 tekens, kopieer dit)

```
Capital BB bouwt de systemen achter een bedrijf: de website die aanvragen
oplevert, het CRM waarin die aanvragen landen, de AI-medewerker die opneemt
als u niet kunt, en de automatiseringen die het terugkerende werk overnemen.
Los af te nemen, maar gebouwd om samen te werken.

U werkt rechtstreeks met de bouwer. Geen accountmanager ertussen, geen
overdracht naar een team dat het gesprek niet heeft gevoerd.

De werkwijze is omgekeerd aan wat gebruikelijk is: u ziet eerst een werkend
voorstel en beslist daarna. Bevalt het niet, dan kost het u niets. Prijzen
staan open op de website, vanaf 795 euro voor een website en vanaf 159 euro
per maand voor een CRM.

Werkgebied: heel Nederland, op afstand of op locatie.
```

Dat is 741 tekens. Pas je iets aan, tel dan even na.

### Diensten toevoegen aan het profiel

Voeg deze los toe, elk met een korte omschrijving. Dit doet meer dan de meeste
mensen denken: Google matcht hierop bij specifieke zoekopdrachten.

| Dienst | Omschrijving |
|---|---|
| Website laten maken | Maatwerkwebsites die bezoekers omzetten in aanvragen en afspraken. Vanaf 795 euro eenmalig. |
| Webshop en leadmachine | Sites gebouwd rond één duidelijke aanvraagroute, gekoppeld aan agenda, CRM of WhatsApp. |
| CRM-systeem | Klanten, offertes en opvolging op één plek. Vanaf 159 euro per maand. |
| Bedrijfsprocessen automatiseren | Terugkerend werk en koppelingen tussen systemen. Vanaf 295 euro per koppeling. |
| AI-telefonie | Een digitale medewerker die opneemt als u niet kunt. Inrichting vanaf 750 euro. |
| SEO en vindbaarheid | Gevonden worden in Google en in AI-assistenten. Vanaf 149 euro per maand. |
| Online marketing | Advertenties, social media, content en e-mail. Prijs op aanvraag. |

### Foto's

Minimaal nodig: een logo en een omslagfoto. Google toont profielen met foto's
aanzienlijk vaker.

- Logo: gebruik `img/icoon-180.png` uit de repository
- Omslag: `[INVULLEN]` — een foto van jou aan het werk doet het beter dan een
  abstracte afbeelding
- Voeg later foto's toe van opgeleverd werk, met toestemming van de klant

**Geen beeldbankfoto's.** Die herkent iedereen, en ze doen precies het
tegenovergestelde van vertrouwen wekken.

---

## 2. Reviews vragen

### Wanneer

Op het moment dat iemand tevreden is, niet weken later. Dus: direct na
oplevering, of vlak nadat iets waar hij last van had is opgelost.

### De link

Zodra je profiel geverifieerd is, geeft Google je een korte reviewlink. Die
vind je in je Bedrijfsprofiel onder "Vraag om reviews". Zet hem hier neer
zodat je hem terugvindt: `[INVULLEN]`

### Bericht via WhatsApp of mail

```
Hoi [NAAM],

[Site/systeem] staat nu live en volgens mij loopt alles zoals het moet.

Mag ik je iets vragen? Capital BB is nog jong en reviews zijn zo'n beetje
het enige waar een nieuwe klant op af kan gaan. Als je een minuut hebt:

[REVIEWLINK]

Eerlijk is prima, ook als er iets beter kon. Daar heb ik meer aan dan aan
vijf sterren zonder tekst.

Bedankt,
Björn
```

**Waarom deze toon werkt:** je vraagt om hulp in plaats van om een gunst, je
geeft een reden, en je nodigt uit tot eerlijkheid. Dat laatste levert
paradoxaal genoeg betere reviews op, omdat mensen dan daadwerkelijk iets
opschrijven in plaats van alleen sterren aan te tikken.

### Wat je niet doet

- Geen reviews vragen aan mensen die geen klant waren
- Niets weggeven in ruil voor een review; dat is tegen de regels van Google
  en het is te zien
- Niet alle reviews tegelijk laten schrijven; vijf reviews op één dag ziet er
  gekocht uit. Spreid het

### Reageren

Reageer op elke review, ook op een matige. Kort, geen verkooppraat. Bij een
kritische review: erken wat er misging, zeg wat je hebt gedaan, en bied aan
het verder op te pakken. Toekomstige klanten lezen vooral hóe je reageert.

---

## 3. Search Console en Bing koppelen

### Google Search Console

1. Ga naar https://search.google.com/search-console
2. Kies **Domein** (niet URL-voorvoegsel) en vul `capitalbb.nl` in
3. Google geeft een TXT-record. Zet dat in Cloudflare: **DNS** → **Add
   record** → Type `TXT`, Name `@`, Content = de waarde van Google
4. Klik op verifiëren in Search Console
5. Ga naar **Sitemaps** en dien in: `sitemap.xml`

Waarom "Domein" en niet "URL-voorvoegsel": dan zitten www, non-www, http en
https allemaal in één property en hoef je niet vier keer hetzelfde te doen.

### Bing Webmaster Tools

1. Ga naar https://www.bing.com/webmasters
2. Kies **Import from Google Search Console**. Dat scheelt de hele
   verificatie
3. Controleer dat de sitemap is meegekomen

Bing voedt Copilot. Overslaan is zonde.

### Daarna, tegen mij zeggen

Zodra beide gekoppeld zijn, kan ik de nulmeting vullen en maandelijks
vergelijken. Zonder toegang zijn dat lege kolommen.

---

## 4. Wat ik van jou nodig heb om verder te kunnen

Zet hier de antwoorden neer, dan verwerk ik ze in één keer in
`_bron/inhoud.py` en de structured data.

| Wat | Waarvoor | Antwoord |
|---|---|---|
| LinkedIn-URL bedrijf | `sameAs` in het schema | `[INVULLEN]` |
| LinkedIn-URL persoonlijk | Person-entiteit | `[INVULLEN]` |
| Google Bedrijfsprofiel-URL | `sameAs`, sterkste bevestiging | `[INVULLEN]` |
| Facebook-URL | `sameAs` | `[INVULLEN]` |
| Instagram-URL | `sameAs` | `[INVULLEN]` |
| Vestigingsadres | Bepaalt of een lokale pagina eerlijk kan | `[INVULLEN]` |
| Adres tonen of verbergen | Servicegebied-bedrijf of niet | `[INVULLEN]` |
| Statutaire KvK-naam | `legalName` in het schema | `[INVULLEN]` |
| Foto van jou | `/wie/` en de Person-entiteit | `[INVULLEN]` |
| Vanafprijs online marketing | De enige dienst zonder prijs | `[INVULLEN]` |
| GA4 meet-ID (`G-...`) | Alleen als je wilt meten | `[INVULLEN]` |

**Over dat laatste:** je koos eerder Google Analytics. Bedenk dat dat een
cookiebanner betekent op elke pagina. Cloudflare Web Analytics is gratis,
cookieloos en heeft geen banner nodig, maar meet geen conversies. Wil je
alsnog switchen, zeg het dan voordat je een GA4-property aanmaakt.

---

## 5. Nulmeting

Vul dit in zodra Search Console veertien dagen data heeft. Eerder heeft het
geen zin, want dan meet je vooral de indexering zelf.

Datum van meting: `[INVULLEN]`

| KPI | Bron | Nulmeting |
|---|---|---|
| Organische vertoningen per maand | Search Console | |
| Organische klikken per maand | Search Console | |
| Non-branded vertoningen | Search Console, "capital bb" uitgefilterd | |
| Positie op "website laten maken" | Search Console | |
| Positie op "crm systeem mkb" | Search Console | |
| Positie op "ai telefoniste" | Search Console | |
| Geïndexeerde pagina's | Search Console, dekkingsrapport | |
| Contactformulieren per maand | Mailbox | |
| Scan-aanvragen per maand | Mailbox | |
| Google-reviews | Bedrijfsprofiel | |
| AI-vermeldingen | Handmatige controle, zie groeiplan.md | |

**Kijk vooral naar non-branded.** In het begin komt bijna al het verkeer
binnen op je eigen naam. Dat zijn mensen die je al kenden; dat is geen groei.

---

## Volgorde, als je het in één ochtend wilt doen

1. Google Bedrijfsprofiel aanmaken en omschrijving plakken (20 min)
2. Search Console koppelen via het TXT-record in Cloudflare (10 min)
3. Bing importeren uit Search Console (5 min)
4. De twee Cloudflare-instellingen uit het stappenplan (10 min)
5. Twee reviewberichten versturen (5 min)
6. De tabel bij punt 4 invullen en aan mij geven (10 min)

De verificatie van het Bedrijfsprofiel duurt daarna nog een paar dagen; dat
loopt vanzelf.

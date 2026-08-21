# Capital BB, de site

Dit is de definitieve site: veertien pagina's, gebouwd volgens jouw keuzes van
21 augustus. De oude one-pager in `capital-bb\` en de voorbeelden in
`capital-bb-keuzes\` zijn hiermee vervangen; bewaren mag, publiceren niet.

## Bekijken

```
python -m http.server 8330 --directory capital-bb-site
```

en dan http://localhost:8330. Dubbelklikken op een index.html werkt ook, maar
de links tussen pagina's verwachten een server of GitHub Pages.

## Zo zit hij in elkaar

Alle inhoud staat in **`_bron\inhoud.py`**: teksten, prijzen, contactgegevens,
navigatie. Eén bestand. Na een wijziging draai je:

```
python _bron/bouw.py
```

en alle veertien pagina's, de sitemap, robots.txt en llms.txt worden opnieuw
geschreven. Je bewerkt dus nooit een index.html met de hand; dat wordt bij de
volgende bouw overschreven.

De structuur is wat je vroeg: **probleemgestuurd aan de voorkant**
(/meer-klanten en /slimmer-werken als sporen op de homepage en in het menu),
**dienstgestuurd eronder** (/websites, /vindbaarheid, /ai-medewerkers, /crm,
/automatisering, /business-os als eigen landingspagina's voor SEO, GEO en
advertenties). Daarnaast /scan, /werk, /werkwijze, /prijzen en /contact.

## Dit moet je invullen voor livegang

In `_bron\inhoud.py`, bovenaan, het blok `CONTACT`. Telefoon, WhatsApp
(internationaal, zonder plus: `31612345678`), e-mail en domein. Daarna
`python _bron/bouw.py`. Zolang het leeg is weigeren de formulieren met een
nette melding en staat er een gouden waarschuwing in de voettekst.

Het domein staat op **capitalbb.nl** als aanname. Wordt het anders: pas het aan
in `CONTACT["domein"]` en bouw opnieuw; alle canonieken, de sitemap en llms.txt
draaien mee.

## De filmische hero

De zes onderdelen (Website, Leads, CRM, AI-medewerker, Automatisering,
Business OS) komen tijdens het scrollen uit de diepte en verbinden zich met
gouden draden. Dat is scrollgestuurd in moderne browsers; in oudere speelt
dezelfde opbouw vanzelf af zodra de hero in beeld is, en bij "verminderde
beweging" staat alles direct op zijn plek. De kop en de knoppen animeren
bewust niet mee: die staan er vanaf de eerste milliseconde.

## Conversie

- Elke pagina eindigt in hetzelfde dubbele CTA-blok: kennismaking plus scan.
- Elke prijssectie heeft een directe actieknop eronder.
- Op mobiel staat onderaan een vaste actiebalk met beide acties, behalve op
  /scan en /contact zelf, want daar staat het formulier al.
- De scan heet Website Performance Scan en vraagt adres, naam en
  bereikbaarheid. Versturen opent WhatsApp of mail met alles er al in.

## Publiceren

GitHub Desktop, `Add local repository`, deze map, publiceren zonder
"keep private". De map `_bron` wordt door GitHub Pages genegeerd (naam begint
met een underscore) en staat in robots.txt op Disallow.

## Wat er nog niet in zit

- Echte beelden op /werk (de case staat er geanonimiseerd in, als compositie
  in de IJsseldal-kleuren, geen schermafbeelding)
- Privacyverklaring, algemene voorwaarden, KvK-nummer
- Een echte verzendroute voor formulieren (nu WhatsApp/mail-overdracht)

# het autobedrijf Automotive — onofficieel verkoopconcept

Deze Capital BB-demo impliceert geen opdracht, samenwerking of goedkeuring door Het autobedrijf.

## Starten

`npm ci`, `npm run dev`, `npm run build` en `npm start`.

## Voorraad

`data/inventory.json` bevat een volledige gedateerde kopie van de officiële openbare voorraad: 42 voertuigen met 1.477 fotoreferenties bij deze revisie. `npm run sync:inventory` haalt alle voorraadpagina’s, details en fotofeeds opnieuw op. De import stopt bij ontbrekende voertuigen of lege galerijen en vervangt de vorige kopie pas nadat de hele import is geslaagd. Voer daarna een build/deployment uit. Dit is geen continu gesynchroniseerde voorraadkoppeling.

Elke auto heeft een eigen statische route, complete galerij, vergroting met toetsenbordbediening, specificaties, uitrusting, bronadvertentie en gerichte aanvraagflow. Voertuigfoto’s zijn ongewijzigde bronbeelden; Next Image optimaliseert ze op aanvraag. Prijzen van €1 worden als prijs op aanvraag getoond. Exclusief-btw-prijzen zijn gemarkeerd. Zoek-, merk-, brandstof-, carrosserie-, transmissie- en budgetfilters, sortering, paginering en lokale favorieten werken in de showroom.

## Concept en privacy

Formulieren verzenden en bewaren geen persoonsgegevens. Favorieten blijven in de lokale browseropslag. Echte telefoongesprekken, e-mails, routeplanning en bronadvertenties kunnen via expliciete links worden geopend. De site heeft geen toegevoegde analytics of marketingtrackers. De privacy/conceptpagina beschrijft dit. Robots.txt blokkeert indexering.

## Cinematische hero

Desktop gebruikt de nabewerkte H.264-video. Telefoons en touchapparaten gebruiken 154 videoframes met native sticky-positionering en een begrensde beeldcache. Introductietekst verdwijnt na de eerste 10% en de afsluitende caption verschijnt pas na 88%; het midden blijft vrij. Verminderde beweging toont een stil beeld.

Nachtelijke sfeerfoto’s zijn met AI nabewerkt; originele bronbestanden blijven behouden. Team- en werkplaatsbeelden zijn afkomstig uit de officiële website. Geen voertuigfoto’s zijn generatief veranderd.

## Voor een officiële ingebruikname

Laat het autobedrijf voorraadactualisering, beeldgebruik, definitieve teksten, contactafhandeling, hosting en voorwaarden bevestigen. Koppel daarna de afgesproken voorraadfeed en daadwerkelijke aanvraagverwerking. De huidige deployment blijft een onofficieel verkoopconcept.

## Validatie en afhankelijkheden

`npm test` controleert of alle bronvoertuigen aanwezig zijn, ids en routes uniek zijn, galerijen en bronverwijzingen volledig zijn en prijs-/btw-regels behouden blijven. Alle 1.477 fotolinks zijn op bereikbaarheid gecontroleerd bij deze revisie. De browsercontrole doorloopt zoeken, filters, favorieten, paginering, galerij, toetsenbordbediening en de voertuiggebonden demo-aanvraag.

PostCSS is via een npm-override op de compatibele versie 8.5.30 gezet om de kwetsbare transitieve versie uit Next.js 15 te vervangen. De productie-audit meldt geen bekende kwetsbaarheden na deze wijziging. De build is ermee geverifieerd.

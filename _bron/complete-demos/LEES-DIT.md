# Volledige, geanonimiseerde conceptdemo’s

De werkpagina embedt de volledige websites uit `/demos/`, met hun eigen teksten,
navigatie, scrollanimaties en intakeflows. De knoppen schakelen tussen echte
websites; er staan geen losse videospelers meer in het portfolio.

`advies/` en `automotive/` bevatten de bewerkbare Next.js-bronnen. Hun
`next.config` exporteert statisch met een eigen basePath onder `/demos/`.
De installatie-demo is statische HTML, CSS en JavaScript; de volledige bron
staat direct in `/demos/installatie/`.

Voor een nieuwe Next.js-bouw: installeer de vastgelegde dependencies, kopieer
de openbare assets uit de overeenkomstige `/demos/`-map naar `public/` (zonder
`_next`, HTML en routepayloads), en voer `npm run build` uit. Kopieer de inhoud
van `out/` naar de overeenkomstige `/demos/`-map. Behoud daarbij de retourlink
naar het portfolio. De normale hoofdsitegenerator verandert de demo’s niet.

De demo’s zijn noindex en de aanvraagflows verzenden niets. Klantnamen,
bedrijfsnamen en directe contactverwijzingen zijn vervangen. De twee
installatiefilms en de automotive-film behouden hun volledige camerabeweging;
de bedrijfsnaam op werkkleding en gevel is lokaal uit de film verwijderd.
Mobiele automotive-frames en eindbeelden zijn uit diezelfde film afgeleid.

Controleer na wijzigingen altijd de echte keuzes, subpagina’s, formulieren,
desktop- en mobiele scrollweergave en de iframe-wisselaar op `/werk/`.

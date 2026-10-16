# Onafhankelijk adviseur · twee websiteconcepten

Demo met twee volledige websiteconcepten voor Onafhankelijk financieel advies, plus een interne startpagina om ze te vergelijken.

| Route | Wat |
|---|---|
| `/` | Interne startpagina: previews, scopevergelijking, prijzen (alleen hier), contentstatus |
| `/variant-1` | Filmisch, warm en persoonlijk. Kort kennismakingsformulier |
| `/variant-2` | Ruimtelijk en interactief. Begeleide intake met vertakkingen |

Elke variant heeft de subpagina's `jouw-situatie`, `over-adviseur`, `werkwijze` en `kennismaken`.

## Starten

Vereist Node 20 of nieuwer.

```bash
npm install
npm run build
npm start          # http://localhost:3000
```

Voor ontwikkelen: `npm run dev`. Controles: `npm run typecheck` en `npm test`.

## Belangrijk voor de demo

- Formulieren **versturen niets**. Na afronden zie je "Zo ontvangt de adviseur de hulpvraag": een voorbeeld van de inbox.
- Er wordt niets opgeslagen (geen localStorage, geen cookies voor contactgegevens).
- Alle pagina's hebben `noindex` (meta én `X-Robots-Tag`-header).
- De knop **Conceptdemo** linksonder zet demonotities aan of uit (bewaard per tabblad).
- Er is geen gegenereerde de adviseur: op elke plek staat "Foto van de adviseur toevoegen".

## Structuur

- `content/` alle teksten en gegevens (`paul.ts`, `situations.ts`, `faq.ts`, `source-status.ts`, `assets.ts`)
- `lib/` intake- en validatielogica zonder React, getest in `tests/`
- `components/` per variant, plus gedeelde navigatie, formulieren, huismodel en motion
- `components/motion/config.ts` centrale animatiewaarden
- `scripts/` Playwright-controles: `e2e.mjs`, `verify.mjs`, `deliver-shots.mjs`

## Beelden toevoegen

Zet bestanden in `public/assets/` en vul de paden in `content/assets.ts`. Zolang een veld `null` is, toont de site de getekende plaatshouder. Zie `docs/ASSETS.md`.

## Publiceren (alleen op verzoek)

Alle routes zijn statisch. Voor GitHub Pages (bijv. bjornb0316.github.io) kan `output: "export"` in `next.config.mjs` worden gezet. De `X-Robots-Tag`-header werkt dan niet; de `noindex`-metatag blijft wel staan.

export type SituationId = "kopen" | "ondernemer" | "overwaarde" | "complex";

export type Situation = {
  id: SituationId;
  /** Vraag zoals die rond de woning verschijnt (variant 1, scène 2). */
  question: string;
  /** Korte uitleg onder de vraag. */
  answer: string;
  /** Kaarttitel en ondertitel (variant 2). */
  cardTitle: string;
  cardText: string;
  /** Hoofdstuk op de pagina Jouw situatie. */
  chapter: {
    title: string;
    recognition: string[];
    approach: string;
  };
  /** Wat het woningmodel in variant 2 laat zien. */
  houseCaption: string;
};

export const situations: Situation[] = [
  {
    id: "ondernemer",
    question: "Een hypotheek als ondernemer?",
    answer:
      "Je inkomen vertelt niet altijd het hele verhaal van je onderneming. Bespreek met de adviseur wat jouw situatie vraagt.",
    cardTitle: "Hypotheek als ondernemer",
    cardText: "Jouw plannen en onderneming bespreken.",
    chapter: {
      title: "Ondernemen en wonen",
      recognition: [
        "Je onderneemt al een tijd, of je staat op het punt om te starten.",
        "Je vraagt je af hoe er naar jouw inkomen wordt gekeken.",
        "Je wilt weten wat er nodig is voordat je een woonstap zet.",
      ],
      approach:
        "De adviseur neemt de tijd om jouw onderneming en plannen te begrijpen, en bespreekt welke vragen er bij een hypotheek voor ondernemers spelen.",
    },
    houseCaption: "Ruimte voor jouw onderneming en woonplannen",
  },
  {
    id: "kopen",
    question: "Een volgende woning op het oog?",
    answer:
      "Of het je eerste woning is of een volgende stap: het helpt om vooraf te weten welke vragen er spelen.",
    cardTitle: "Een woning kopen",
    cardText: "Eerste woning of een volgende stap.",
    chapter: {
      title: "Een woning kopen",
      recognition: [
        "Je zoekt je eerste woning of bent toe aan een volgende.",
        "Je hebt al iets op het oog, of je oriënteert je nog.",
        "Je wilt weten waar je rekening mee moet houden.",
      ],
      approach:
        "De adviseur bespreekt met je wat je wilt bereiken en welke stappen bij jouw situatie horen, van oriëntatie tot het vervolg.",
    },
    houseCaption: "Een woning die past bij jouw volgende stap",
  },
  {
    id: "overwaarde",
    question: "Overwaarde voor een nieuwe stap?",
    answer:
      "Verbouwen, verduurzamen of een andere woonstap. Onderzoek met de adviseur wat bij jouw wensen past.",
    cardTitle: "Overwaarde benutten",
    cardText: "Onderzoeken wat bij jouw wensen past.",
    chapter: {
      title: "Overwaarde benutten",
      recognition: [
        "Je woning is in waarde gestegen en je hebt plannen.",
        "Je denkt aan verbouwen, verduurzamen of een andere woonstap.",
        "Je wilt weten welke vragen daarbij horen.",
      ],
      approach:
        "De adviseur kijkt samen met je naar je wensen en bespreekt welke mogelijkheden je kunt onderzoeken.",
    },
    houseCaption: "Jouw plannen voor de woning centraal",
  },
  {
    id: "complex",
    question: "Een situatie die extra uitzoekwerk vraagt?",
    answer:
      "Een bijzondere werkvorm, een veranderde situatie of een aanvraag die vastliep. Vertel wat er speelt.",
    cardTitle: "Een complexe situatie",
    cardText: "Ruimte voor een vraag die extra aandacht vraagt.",
    chapter: {
      title: "Een situatie die extra aandacht vraagt",
      recognition: [
        "Je inkomen of werkvorm vraagt om extra uitleg.",
        "Een eerdere aanvraag liep vast, of je situatie is veranderd.",
        "Er spelen meerdere financiële vragen tegelijk.",
      ],
      approach:
        "Juist hier past de adviseur zijn motto. Hij neemt de tijd om uit te zoeken wat jouw situatie vraagt en bespreekt eerlijk welke routes er zijn.",
    },
    houseCaption: "Overzicht wanneer er meer tegelijk speelt",
  },
];

export const situationById = (id: string | null | undefined) =>
  situations.find((s) => s.id === id) ?? null;

export const isSituationId = (v: unknown): v is SituationId =>
  v === "kopen" || v === "ondernemer" || v === "overwaarde" || v === "complex";

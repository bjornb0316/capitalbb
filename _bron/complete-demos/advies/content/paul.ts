// Zakelijke basis voor beide varianten.
// Bron: #demo-contact (geraadpleegd 13-10-2026).
// Alles wat hier staat, staat ook in content/source-status.ts met zijn verificatiestatus.

export const paul = {
  name: "Onafhankelijk adviseur",
  firstName: "De adviseur",
  company: "Onafhankelijk financieel advies",
  role: "Onafhankelijk financieel adviseur",
  place: "Nederland",
  motto: "Kan niet, ken ik niet.",
  mottoLines: ["Kan niet,", "ken ik niet."] as const,
  network: "het adviesnetwerk",
  focus:
    "Complexe financiële vraagstukken voor particulieren en ondernemers, met persoonlijke begeleiding van begin tot eind.",
  contact: {
    phoneDisplay: "Demo — geen telefoonnummer",
    phoneHref: "#demo-contact",
    whatsappHref: "#demo-contact",
    email: "demo@example.invalid",
  },
  // Concepttekst; de adviseur keurt de definitieve formulering goed.
  introV1:
    "Bij een financiële vraag wil je weten waar je aan toe bent. Ik neem de tijd om jouw situatie te begrijpen, de mogelijkheden te onderzoeken en je te begeleiden bij de volgende stap.",
  introV2:
    "Vertel me wat er speelt. Dan kunnen we samen bepalen wat een passende volgende stap is.",
  intakeQuote: "Vertel me waar je staat. Dan hebben we een goed vertrekpunt.",
  // Er is nog geen goedgekeurde foto. Zet hier het pad zodra de adviseur er een aanlevert.
  portrait: { src: "/demos/advies/assets/paul/paul-profile.jpg", alt: "Onafhankelijk financieel adviseur" } as null | { src: string; alt: string },
} as const;

export const process = [
  {
    n: 1,
    title: "Vertel jouw verhaal",
    text: "We bespreken je situatie, wensen en vragen.",
    detail:
      "Je vertelt waar je staat en wat je wilt bereiken. Er is ruimte voor de dingen die niet in een standaardformulier passen.",
  },
  {
    n: 2,
    title: "Onderzoek de mogelijkheden",
    text: "De adviseur kijkt welke aanpak bij jouw situatie past.",
    detail:
      "De adviseur zet op een rij wat jouw situatie vraagt en welke routes er zijn. Je krijgt uitleg in begrijpelijke taal.",
  },
  {
    n: 3,
    title: "Zet de volgende stap",
    text: "Je krijgt uitleg en begeleiding bij het vervolg.",
    detail:
      "Je beslist zelf of en hoe je verder wilt. Kies je voor een vervolg, dan begeleidt de adviseur je bij de stappen die daarbij horen.",
  },
] as const;

export const expectations = [
  {
    title: "Ruimte voor jouw situatie",
    text: "Je hoeft niet in een hokje te passen. Het gesprek begint bij wat er bij jou speelt.",
  },
  {
    title: "Begrijpelijke uitleg",
    text: "Je krijgt helder uitgelegd welke vragen belangrijk zijn en waarom.",
  },
  {
    title: "Een duidelijke vervolgstap",
    text: "Na het gesprek weet je wat er nodig is om verder te gaan, en beslis je zelf of je dat wilt.",
  },
] as const;

export const nav = [
  { slug: "jouw-situatie", label: "Jouw situatie" },
  { slug: "over-adviseur", label: "Over de adviseur" },
  { slug: "werkwijze", label: "Werkwijze" },
  { slug: "kennismaken", label: "Kennismaken" },
] as const;

export const primaryCta = "Vertel de adviseur jouw situatie";

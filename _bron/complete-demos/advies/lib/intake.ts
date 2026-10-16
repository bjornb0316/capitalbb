// Begeleide intake (variant 2) en kort formulier (variant 1).
// Pure logica zonder React, zodat de vertakkingen met tests te controleren zijn.

import {
  type ContactPref,
  type Errors,
  LIMITS,
  required,
  validateContact,
  validateDeadline,
} from "./validation.ts";

export type SituationId = "kopen" | "ondernemer" | "overwaarde" | "complex";
export type Option = { value: string; label: string };

export const timingOptions: Option[] = [
  { value: "orienteren", label: "Ik oriënteer me" },
  { value: "maanden", label: "Binnen enkele maanden" },
  { value: "kort", label: "Op korte termijn" },
  { value: "deadline", label: "Er speelt een deadline" },
  { value: "onbekend", label: "Weet ik nog niet" },
];

export const contactOptions: { value: ContactPref; label: string; hint: string }[] = [
  { value: "email", label: "Per e-mail", hint: "De adviseur mailt je terug" },
  { value: "telefoon", label: "Telefonisch", hint: "De adviseur belt je" },
];

/* ------------------------------------------------------------------ */
/* Variant 2: vertakkingen                                             */
/* ------------------------------------------------------------------ */

export type ChoiceQuestion = { key: BranchKey; label: string; options: Option[] };
export type TextQuestion = { label: string; hint: string };

export type BranchKey =
  | "kopenStap"
  | "kopenWoning"
  | "ondernemerDuur"
  | "ondernemerWens"
  | "overwaardeDoel"
  | "complexWat";

export const BRANCH_KEYS: Record<SituationId, BranchKey[]> = {
  kopen: ["kopenStap", "kopenWoning"],
  ondernemer: ["ondernemerDuur", "ondernemerWens"],
  overwaarde: ["overwaardeDoel"],
  complex: ["complexWat"],
};

export const branches: Record<
  SituationId,
  { context: ChoiceQuestion[]; wish: ChoiceQuestion[]; story: TextQuestion; contextTitle: string; wishTitle: string }
> = {
  kopen: {
    contextTitle: "Waar sta je?",
    context: [
      {
        key: "kopenStap",
        label: "Welke stap wil je zetten?",
        options: [
          { value: "eerste", label: "Mijn eerste woning" },
          { value: "volgende", label: "Een volgende woning" },
          { value: "onbekend", label: "Weet ik nog niet" },
        ],
      },
      {
        key: "kopenWoning",
        label: "Heb je al een woning op het oog?",
        options: [
          { value: "ja", label: "Ja" },
          { value: "nee", label: "Nee" },
          { value: "orienteren", label: "Ik ben nog aan het oriënteren" },
        ],
      },
    ],
    wishTitle: "Jouw hulpvraag",
    wish: [],
    story: {
      label: "Wat wil je met de adviseur bespreken?",
      hint: "Bijvoorbeeld je mogelijkheden, maandlasten of een bijzondere situatie.",
    },
  },
  ondernemer: {
    contextTitle: "Jouw onderneming",
    context: [
      {
        key: "ondernemerDuur",
        label: "Hoe lang onderneem je?",
        options: [
          { value: "<1", label: "Minder dan één jaar" },
          { value: "1-3", label: "Eén tot drie jaar" },
          { value: ">3", label: "Langer dan drie jaar" },
          { value: "start", label: "Ik ben van plan te starten" },
          { value: "toelichten", label: "Dat licht ik liever toe" },
        ],
      },
    ],
    wishTitle: "Jouw woonstap",
    wish: [
      {
        key: "ondernemerWens",
        label: "Welke woonstap wil je bespreken?",
        options: [
          { value: "kopen", label: "Een woning kopen" },
          { value: "bestaand", label: "Mijn bestaande hypotheek bekijken" },
          { value: "overwaarde", label: "Overwaarde" },
          { value: "anders", label: "Een andere vraag" },
        ],
      },
    ],
    story: {
      label: "Wat maakt jouw situatie belangrijk voor het gesprek?",
      hint: "Je hoeft hier geen inkomen of omzet te noemen. Vertel in je eigen woorden wat er speelt.",
    },
  },
  overwaarde: {
    contextTitle: "Jouw plannen",
    context: [
      {
        key: "overwaardeDoel",
        label: "Waarvoor wil je de mogelijkheden onderzoeken?",
        options: [
          { value: "verbouwen", label: "Verbouwen of verduurzamen" },
          { value: "woonstap", label: "Een andere woonstap" },
          { value: "ruimte", label: "Meer financiële ruimte bespreken" },
          { value: "anders", label: "Anders / nog oriënteren" },
        ],
      },
    ],
    wishTitle: "Jouw wens",
    wish: [],
    story: { label: "Wat wil je graag bereiken?", hint: "Een paar zinnen is genoeg." },
  },
  complex: {
    contextTitle: "Wat speelt er?",
    context: [
      {
        key: "complexWat",
        label: "Wat speelt er?",
        options: [
          { value: "werkvorm", label: "Mijn inkomen of werkvorm vraagt extra uitleg" },
          { value: "vastgelopen", label: "Een aanvraag is vastgelopen" },
          { value: "veranderd", label: "Mijn persoonlijke situatie is veranderd" },
          { value: "meerdere", label: "Er zijn meerdere financiële vragen" },
          { value: "zelf", label: "Ik licht het liever zelf toe" },
        ],
      },
    ],
    wishTitle: "Jouw verhaal",
    wish: [],
    story: {
      label: "Vertel kort wat de adviseur moet weten.",
      hint: "Deel hier nog geen documenten, medische of andere gevoelige gegevens.",
    },
  },
};

export type IntakeV2 = {
  situation: SituationId | "";
  branch: Partial<Record<BranchKey, string>>;
  story: string;
  timing: string;
  deadlineDate: string;
  deadlineNote: string;
  name: string;
  contactPref: ContactPref | "";
  email: string;
  phone: string;
};

export const emptyIntake = (situation: SituationId | "" = ""): IntakeV2 => ({
  situation,
  branch: {},
  story: "",
  timing: "",
  deadlineDate: "",
  deadlineNote: "",
  name: "",
  contactPref: "",
  email: "",
  phone: "",
});

/** Vaste stapvolgorde: de voortgang springt nooit achteruit door een vertakking. */
export const STEPS = [
  { id: "situatie", label: "Situatie" },
  { id: "context", label: "Context" },
  { id: "wens", label: "Hulpvraag" },
  { id: "timing", label: "Timing" },
  { id: "contact", label: "Contact" },
  { id: "controle", label: "Controle" },
] as const;
export type StepId = (typeof STEPS)[number]["id"];

/**
 * Wisselt de hoofdsituatie. Verwijdert alleen antwoorden die bij de oude
 * situatie hoorden; toelichting, timing en contact blijven staan.
 */
export function changeSituation(
  data: IntakeV2,
  next: SituationId,
): { data: IntakeV2; removed: BranchKey[] } {
  if (data.situation === next) return { data, removed: [] };
  const keep = new Set(BRANCH_KEYS[next]);
  const removed: BranchKey[] = [];
  const branch: IntakeV2["branch"] = {};
  for (const [k, v] of Object.entries(data.branch) as [BranchKey, string][]) {
    if (keep.has(k)) branch[k] = v;
    else if (v) removed.push(k);
  }
  return { data: { ...data, situation: next, branch }, removed };
}

const choiceError = "Maak een keuze om verder te gaan.";

export function validateStep(step: StepId, d: IntakeV2): Errors {
  const e: Errors = {};
  const b = d.situation ? branches[d.situation] : null;
  switch (step) {
    case "situatie":
      if (!d.situation) e.situation = "Kies de situatie die het best bij je past.";
      break;
    case "context":
      b?.context.forEach((q) => {
        if (!d.branch[q.key]) e[q.key] = choiceError;
      });
      break;
    case "wens":
      b?.wish.forEach((q) => {
        if (!d.branch[q.key]) e[q.key] = choiceError;
      });
      if (!required(d.story)) e.story = "Vertel in een paar woorden wat je wilt bespreken.";
      else if (d.story.length > LIMITS.story) e.story = `Gebruik maximaal ${LIMITS.story} tekens.`;
      break;
    case "timing":
      if (!d.timing) e.timing = "Kies wanneer je de volgende stap wilt zetten.";
      Object.assign(e, validateDeadline(d.timing, d.deadlineDate));
      break;
    case "contact":
      Object.assign(e, validateContact(d));
      break;
    case "controle":
      for (const s of STEPS.slice(0, 5)) Object.assign(e, validateStep(s.id, d));
      break;
  }
  return e;
}

/** Eerste stap met een fout, of null als alles klopt. */
export function firstInvalidStep(d: IntakeV2): StepId | null {
  for (const s of STEPS.slice(0, 5)) if (Object.keys(validateStep(s.id, d)).length) return s.id;
  return null;
}

/* ------------------------------------------------------------------ */
/* Variant 1: kort formulier                                           */
/* ------------------------------------------------------------------ */

export const v1Topics: Option[] = [
  { value: "kopen", label: "Woning kopen" },
  { value: "ondernemer", label: "Hypotheek als ondernemer" },
  { value: "overwaarde", label: "Overwaarde" },
  { value: "complex", label: "Complexe situatie" },
  { value: "anders", label: "Anders / eerst kennismaken" },
];

export type FormV1 = {
  name: string;
  topic: string;
  story: string;
  timing: string;
  deadlineDate: string;
  deadlineNote: string;
  contactPref: ContactPref | "";
  email: string;
  phone: string;
};

export const emptyFormV1 = (topic = ""): FormV1 => ({
  name: "",
  topic,
  story: "",
  timing: "",
  deadlineDate: "",
  deadlineNote: "",
  contactPref: "",
  email: "",
  phone: "",
});

/** Volgorde waarin velden in het formulier staan; gebruikt voor focus op de eerste fout. */
export const V1_FIELD_ORDER = ["topic", "story", "timing", "deadlineDate", "name", "contactPref", "email", "phone"];

export function validateV1(f: FormV1): Errors {
  const e: Errors = {};
  const c = validateContact(f);
  if (c.name) e.name = c.name;
  if (!f.topic) e.topic = "Kies een onderwerp.";
  if (!required(f.story)) e.story = "Vertel kort wat je wilt bereiken.";
  else if (f.story.length > LIMITS.story) e.story = `Gebruik maximaal ${LIMITS.story} tekens.`;
  if (!f.timing) e.timing = "Kies wanneer je de volgende stap wilt zetten.";
  Object.assign(e, validateDeadline(f.timing, f.deadlineDate));
  if (c.contactPref) e.contactPref = c.contactPref;
  if (c.email) e.email = c.email;
  if (c.phone) e.phone = c.phone;
  return e;
}

export const labelOf = (opts: Option[], v: string) => opts.find((o) => o.value === v)?.label ?? "";

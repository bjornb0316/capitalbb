// Validatie voor beide formulieren. Bewust vergevingsgezind: spaties, streepjes
// en haakjes in Nederlandse nummers zijn prima.

export type ContactPref = "email" | "telefoon";
export type Errors = Record<string, string>;

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

export function normalizePhone(raw: string): string {
  return raw.replace(/[\s\-().]/g, "");
}

export function isValidEmail(v: string): boolean {
  return EMAIL_RE.test(v.trim());
}

/** Accepteert 06 12345678, +31 6 1234 5678, 0031-10-1234567, 010 123 45 67. */
export function isValidPhone(v: string): boolean {
  const n = normalizePhone(v.trim());
  if (/^0[1-9]\d{8}$/.test(n)) return true; // nationaal
  if (/^(\+|00)31[1-9]\d{8}$/.test(n)) return true; // Nederland internationaal
  if (/^(\+|00)[1-9]\d{7,14}$/.test(n)) return true; // buitenland, ruim
  return false;
}

export const LIMITS = { name: 80, story: 1200, deadlineNote: 300 } as const;

export function required(v: string | undefined | null): boolean {
  return typeof v === "string" && v.trim().length > 0;
}

/** Contactvalidatie, gedeeld door variant 1 en 2. */
export function validateContact(input: {
  name: string;
  contactPref: ContactPref | "";
  email: string;
  phone: string;
}): Errors {
  const e: Errors = {};
  if (!required(input.name)) e.name = "Vul je naam in.";
  else if (input.name.trim().length > LIMITS.name) e.name = `Gebruik maximaal ${LIMITS.name} tekens.`;

  if (!input.contactPref) e.contactPref = "Kies hoe de adviseur contact met je kan opnemen.";

  const wantsEmail = input.contactPref === "email";
  const wantsPhone = input.contactPref === "telefoon";

  if (wantsEmail && !required(input.email)) e.email = "Vul je e-mailadres in, zodat de adviseur je kan mailen.";
  else if (required(input.email) && !isValidEmail(input.email))
    e.email = "Dit e-mailadres lijkt niet compleet. Controleer het, bijvoorbeeld naam@voorbeeld.nl.";

  if (wantsPhone && !required(input.phone)) e.phone = "Vul je telefoonnummer in, zodat de adviseur je kan bellen.";
  else if (required(input.phone) && !isValidPhone(input.phone))
    e.phone = "Dit telefoonnummer lijkt niet compleet. Bijvoorbeeld 06 12 34 56 78.";

  return e;
}

export function validateDeadline(timing: string, date: string): Errors {
  const e: Errors = {};
  if (timing === "deadline" && date) {
    const d = new Date(date + "T00:00:00");
    if (Number.isNaN(d.getTime())) e.deadlineDate = "Kies een geldige datum.";
  }
  return e;
}

// Bouwt de "Zo ontvangt de adviseur de hulpvraag"-weergave. Verstuurt niets:
// er is in deze demo bewust geen netwerkverzoek of opslag.

import {
  type FormV1,
  type IntakeV2,
  branches,
  contactOptions,
  labelOf,
  timingOptions,
  v1Topics,
} from "./intake.ts";

export type SummaryRow = { label: string; value: string };
export type SummaryGroup = { id: string; title: string; step?: string; rows: SummaryRow[] };

const situationLabels: Record<string, string> = {
  kopen: "Een woning kopen",
  ondernemer: "Hypotheek als ondernemer",
  overwaarde: "Overwaarde benutten",
  complex: "Een complexe situatie",
};

export function formatDate(iso: string): string {
  if (!iso) return "";
  const d = new Date(iso + "T00:00:00");
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleDateString("nl-NL", { day: "numeric", month: "long", year: "numeric" });
}

function timingRows(timing: string, date: string, note: string): SummaryRow[] {
  const rows: SummaryRow[] = [{ label: "Wanneer", value: labelOf(timingOptions, timing) }];
  if (timing === "deadline") {
    if (date) rows.push({ label: "Datum", value: formatDate(date) });
    if (note.trim()) rows.push({ label: "Toelichting deadline", value: note.trim() });
  }
  return rows;
}

function contactRows(d: { name: string; contactPref: string; email: string; phone: string }): SummaryRow[] {
  const rows: SummaryRow[] = [
    { label: "Naam", value: d.name.trim() },
    { label: "Voorkeur", value: contactOptions.find((o) => o.value === d.contactPref)?.label ?? "" },
  ];
  if (d.email.trim()) rows.push({ label: "E-mail", value: d.email.trim() });
  if (d.phone.trim()) rows.push({ label: "Telefoon", value: d.phone.trim() });
  return rows;
}

export function summarizeV1(f: FormV1): SummaryGroup[] {
  return [
    { id: "onderwerp", title: "Onderwerp", rows: [{ label: "Onderwerp", value: labelOf(v1Topics, f.topic) }] },
    { id: "toelichting", title: "Wat wil je bereiken?", rows: [{ label: "Toelichting", value: f.story.trim() }] },
    { id: "timing", title: "Timing", rows: timingRows(f.timing, f.deadlineDate, f.deadlineNote) },
    { id: "contact", title: "Contact", rows: contactRows(f) },
  ];
}

export function summarizeV2(d: IntakeV2): SummaryGroup[] {
  const b = d.situation ? branches[d.situation] : null;
  const branchRows = (qs: NonNullable<typeof b>["context"]) =>
    qs.map((q) => ({ label: q.label, value: labelOf(q.options, d.branch[q.key] ?? "") })).filter((r) => r.value);

  const situationRows: SummaryRow[] = [{ label: "Situatie", value: situationLabels[d.situation] ?? "" }];
  if (b) situationRows.push(...branchRows(b.context));

  const planRows: SummaryRow[] = b ? branchRows(b.wish) : [];
  const groups: SummaryGroup[] = [{ id: "situatie", title: "Jouw situatie", step: "situatie", rows: situationRows }];
  if (planRows.length) groups.push({ id: "plannen", title: "Jouw plannen", step: "wens", rows: planRows });
  groups.push(
    {
      id: "bijzonderheden",
      title: "Bijzonderheden",
      step: "wens",
      rows: [{ label: b?.story.label ?? "Toelichting", value: d.story.trim() }],
    },
    { id: "timing", title: "Timing", step: "timing", rows: timingRows(d.timing, d.deadlineDate, d.deadlineNote) },
    { id: "contact", title: "Contact", step: "contact", rows: contactRows(d) },
  );
  return groups;
}

/** Korte, menselijke onderwerpregel zoals de adviseur die in zijn inbox zou zien. */
export function subjectLine(name: string, topicLabel: string): string {
  const first = name.trim().split(/\s+/)[0] ?? "";
  return `Nieuwe kennismakingsvraag${first ? ` van ${first}` : ""}${topicLabel ? ` · ${topicLabel}` : ""}`;
}

export { situationLabels };

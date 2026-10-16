"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import {
  type FormV1,
  V1_FIELD_ORDER,
  contactOptions,
  emptyFormV1,
  labelOf,
  timingOptions,
  v1Topics,
  validateV1,
} from "@/lib/intake";
import { LIMITS } from "@/lib/validation";
import { subjectLine, summarizeV1 } from "@/lib/demo-submission";
import { RadioPills, TextArea, TextField, focusFirst } from "./fields";
import { InboxPreview } from "./InboxPreview";
import { isSituationId } from "@/content/situations";
import { paul } from "@/content/paul";
import type { Errors } from "@/lib/validation";

/**
 * Variant 1: kort kennismakingsformulier met goede context.
 * Valideert bij verzenden; antwoorden blijven staan bij fouten.
 * Er wordt niets verstuurd: de afronding is een demoweergave.
 */
export function IntakeV1({ aside, base = "/variant-2" }: { aside: React.ReactNode; base?: string }) {
  const [f, setF] = useState<FormV1>(() => emptyFormV1());
  const [errors, setErrors] = useState<Errors>({});
  const [submitted, setSubmitted] = useState(false);
  const [done, setDone] = useState(false);
  const summaryRef = useRef<HTMLDivElement>(null);
  const doneRef = useRef<HTMLHeadingElement>(null);

  // Onderwerp mag via de URL worden voorgeselecteerd (geen persoonsgegevens).
  useEffect(() => {
    const o = new URLSearchParams(window.location.search).get("onderwerp");
    if (o && (isSituationId(o) || o === "anders")) setF((p) => (p.topic ? p : { ...p, topic: o }));
  }, []);

  const set = <K extends keyof FormV1>(k: K, v: FormV1[K]) => {
    setF((p) => {
      const next = { ...p, [k]: v };
      // Na een eerste verzendpoging worden fouten bijgewerkt zodra ze zijn opgelost.
      if (submitted) setErrors((e) => pruneResolved(e, validateV1(next)));
      return next;
    });
  };

  const onSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
    const errs = validateV1(f);
    setErrors(errs);
    if (Object.keys(errs).length) {
      focusFirst(V1_FIELD_ORDER, errs);
      return;
    }
    setDone(true);
  };

  useEffect(() => {
    if (done) {
      window.scrollTo({ top: 0 });
      doneRef.current?.focus();
    }
  }, [done]);

  if (done) {
    const groups = summarizeV1(f);
    return (
      <div className="container v1-done">
        <div className="v1-done__head">
          <h1 ref={doneRef} tabIndex={-1}>
            Je demoaanvraag staat klaar.
          </h1>
          <p className="v1-done__notice" role="status">
            Dit is een conceptdemo. Er is niets naar de adviseur verstuurd.
          </p>
          <div className="v1-done__mine" style={{ marginTop: "2.5rem" }}>
            <h2 className="v1-done__section-title">Jouw gegevens</h2>
            <dl>
              <div>
                <dt>Naam</dt>
                <dd>{f.name}</dd>
              </div>
              <div>
                <dt>Onderwerp</dt>
                <dd>{labelOf(v1Topics, f.topic)}</dd>
              </div>
              <div>
                <dt>Toelichting</dt>
                <dd>{f.story}</dd>
              </div>
              <div>
                <dt>Timing</dt>
                <dd>{labelOf(timingOptions, f.timing)}</dd>
              </div>
              <div>
                <dt>Contactvoorkeur</dt>
                <dd>{contactOptions.find((c) => c.value === f.contactPref)?.label}</dd>
              </div>
              <div>
                <dt>Contactgegevens</dt>
                <dd>{[f.email, f.phone].filter(Boolean).join("\n")}</dd>
              </div>
            </dl>
          </div>
          <div className="v1-done__actions">
            <button type="button" className="btn btn--ghost" onClick={() => setDone(false)}>
              Gegevens aanpassen
            </button>
            <Link href={base} className="btn btn--primary">
              Terug naar de homepage
            </Link>
          </div>
        </div>
        <InboxPreview
          title="Zo ontvangt de adviseur de hulpvraag"
          subject={subjectLine(f.name, labelOf(v1Topics, f.topic))}
          groups={groups}
        />
      </div>
    );
  }

  const errorCount = Object.keys(errors).length;

  return (
    <div className="container v1-contact__grid">
      {aside}
      <form className="v1-form" noValidate onSubmit={onSubmit} aria-labelledby="v1-form-title">
        <h2 id="v1-form-title" className="sr-only">
          Kennismakingsformulier
        </h2>
        <div ref={summaryRef} role="alert" aria-live="assertive">
          {submitted && errorCount > 0 && (
            <p className="v1-form__errors">
              {errorCount === 1 ? "Eén veld vraagt nog aandacht." : `${errorCount} velden vragen nog aandacht.`} Je
              antwoorden zijn bewaard.
            </p>
          )}
        </div>

        <div className="v1-form__section">
          <p className="v1-form__section-title">
            <span>01</span> Jouw vraag
          </p>
          <RadioPills
            id="topic"
            legend="Waar gaat je vraag over?"
            options={v1Topics}
            value={f.topic}
            onChange={(v) => set("topic", v)}
            error={errors.topic}
          />
          <div style={{ marginTop: "1.75rem" }}>
            <TextArea
              id="story"
              label="Wat wil je bereiken?"
              hint="Vertel kort wat er speelt en welke vraag je aan de adviseur wilt stellen. Deel hier nog geen documenten of gevoelige identificatiegegevens."
              value={f.story}
              onChange={(v) => set("story", v)}
              error={errors.story}
              max={LIMITS.story}
            />
          </div>
        </div>

        <div className="v1-form__section">
          <p className="v1-form__section-title">
            <span>02</span> Timing
          </p>
          <RadioPills
            id="timing"
            legend="Wanneer wil je de volgende stap zetten?"
            options={timingOptions}
            value={f.timing}
            onChange={(v) => set("timing", v)}
            error={errors.timing}
          />
          {f.timing === "deadline" && (
            <div className="v1-form__reveal">
              <TextField
                id="deadlineDate"
                type="date"
                label="Om welke datum gaat het?"
                optional
                value={f.deadlineDate}
                onChange={(v) => set("deadlineDate", v)}
                error={errors.deadlineDate}
              />
              <TextArea
                id="deadlineNote"
                label="Wat speelt er rond die datum?"
                optional
                rows={3}
                value={f.deadlineNote}
                onChange={(v) => set("deadlineNote", v)}
                max={LIMITS.deadlineNote}
              />
            </div>
          )}
        </div>

        <div className="v1-form__section">
          <p className="v1-form__section-title">
            <span>03</span> Contact
          </p>
          <TextField
            id="name"
            label="Je naam"
            autoComplete="name"
            value={f.name}
            onChange={(v) => set("name", v)}
            error={errors.name}
            maxLength={LIMITS.name}
          />
          <div style={{ marginTop: "1.75rem" }}>
            <RadioPills
              id="contactPref"
              legend="Hoe wil je dat de adviseur contact opneemt?"
              options={contactOptions}
              value={f.contactPref}
              onChange={(v) => set("contactPref", v as FormV1["contactPref"])}
              error={errors.contactPref}
            />
          </div>
          <div style={{ marginTop: "1.75rem", display: "grid", gap: "1.75rem" }}>
            <TextField
              id="email"
              type="email"
              label="E-mailadres"
              optional={f.contactPref !== "email"}
              autoComplete="email"
              inputMode="email"
              value={f.email}
              onChange={(v) => set("email", v)}
              error={errors.email}
            />
            <TextField
              id="phone"
              type="tel"
              label="Telefoonnummer"
              optional={f.contactPref !== "telefoon"}
              autoComplete="tel"
              inputMode="tel"
              value={f.phone}
              onChange={(v) => set("phone", v)}
              error={errors.phone}
            />
          </div>
        </div>

        <div className="v1-form__submit">
          <button type="submit" className="btn btn--primary">
            Bekijk mijn demoaanvraag
          </button>
          <p className="small">Conceptdemo: je gegevens worden niet verzonden of opgeslagen.</p>
          <p className="small">
            Liever direct contact? Bel{" "}
            <a className="link" href={paul.contact.phoneHref}>
              {paul.contact.phoneDisplay}
            </a>
            .
          </p>
        </div>
      </form>
    </div>
  );
}

function pruneResolved(current: Errors, fresh: Errors): Errors {
  const out: Errors = {};
  for (const k of Object.keys(current)) if (fresh[k]) out[k] = fresh[k];
  return out;
}

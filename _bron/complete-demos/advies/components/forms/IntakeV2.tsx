"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import {
  type IntakeV2 as Data,
  type StepId,
  STEPS,
  branches,
  changeSituation,
  contactOptions,
  emptyIntake,
  firstInvalidStep,
  labelOf,
  timingOptions,
  validateStep,
} from "@/lib/intake";
import { LIMITS, type Errors } from "@/lib/validation";
import { situationLabels, subjectLine, summarizeV2 } from "@/lib/demo-submission";
import { isSituationId, situationById, type SituationId } from "@/content/situations";
import { paul } from "@/content/paul";
import { HouseModel } from "@/components/house/HouseModel";
import { PortraitSlot } from "@/components/contact/PortraitSlot";
import { SituationCards } from "@/components/variant-2/SituationCards";
import { RadioPills, TextArea, TextField, focusFirst } from "./fields";
import { InboxPreview } from "./InboxPreview";
import { Arrow } from "@/components/contact/icons";

const stepTitles: Record<StepId, string> = {
  situatie: "Welke situatie past het best bij jou?",
  context: "",
  wens: "",
  timing: "Wanneer wil je de volgende stap zetten?",
  contact: "Hoe kan de adviseur je bereiken?",
  controle: "Dit wil je met de adviseur bespreken",
};

/** Veldvolgorde per stap, voor focus op de eerste fout. */
function fieldOrder(step: StepId, d: Data): string[] {
  const b = d.situation ? branches[d.situation] : null;
  switch (step) {
    case "situatie":
      return ["situation"];
    case "context":
      return b ? b.context.map((q) => q.key) : [];
    case "wens":
      return [...(b ? b.wish.map((q) => q.key) : []), "story"];
    case "timing":
      return ["timing", "deadlineDate"];
    case "contact":
      return ["name", "contactPref", "email", "phone"];
    default:
      return [];
  }
}

/**
 * Variant 2: begeleide intake met conditionele vervolgvragen.
 * Alle antwoorden blijven in het geheugen van deze pagina. Er wordt niets verstuurd.
 */
export function IntakeV2() {
  const [d, setD] = useState<Data>(() => emptyIntake());
  const [stepIdx, setStepIdx] = useState(0);
  const [errors, setErrors] = useState<Errors>({});
  const [notice, setNotice] = useState<string | null>(null);
  const [returnToReview, setReturnToReview] = useState(false);
  const [done, setDone] = useState(false);
  const [preview, setPreview] = useState<SituationId | null>(null);
  const heading = useRef<HTMLHeadingElement>(null);
  const [sumOpen, setSumOpen] = useState(false);
  useEffect(() => setSumOpen(window.matchMedia("(min-width: 1024px)").matches), []);
  const firstRender = useRef(true);

  const step = STEPS[stepIdx].id;
  const b = d.situation ? branches[d.situation] : null;

  // Situatie van de homepagekaart of de situatiepagina overnemen en direct verder.
  useEffect(() => {
    const s = new URLSearchParams(window.location.search).get("situatie");
    if (isSituationId(s)) {
      setD((p) => (p.situation ? p : { ...p, situation: s }));
      setStepIdx(1);
    }
  }, []);

  // Focus naar de staptitel bij iedere stapwissel (niet bij eerste weergave).
  useEffect(() => {
    if (firstRender.current) {
      firstRender.current = false;
      return;
    }
    heading.current?.focus({ preventScroll: true });
    const top = heading.current?.closest(".v2-intake")?.getBoundingClientRect().top ?? 0;
    if (top < 0 || top > window.innerHeight * 0.4) window.scrollTo({ top: window.scrollY + top - 90 });
  }, [stepIdx, done]);

  const update = (patch: Partial<Data>) => {
    setD((p) => ({ ...p, ...patch }));
    setErrors((e) => {
      const n = { ...e };
      for (const k of Object.keys(patch)) delete n[k];
      return n;
    });
  };
  const setBranch = (k: string, v: string) => {
    setD((p) => ({ ...p, branch: { ...p.branch, [k]: v } }));
    setErrors((e) => {
      const n = { ...e };
      delete n[k];
      return n;
    });
  };

  const chooseSituation = (s: SituationId) => {
    const { data, removed } = changeSituation(d, s);
    setD(data);
    setErrors({});
    if (removed.length) {
      setNotice(
        `Je situatie is gewijzigd naar “${situationLabels[s]}”. We hebben de vervolgvragen daarop aangepast. Je toelichting, timing en contactgegevens zijn bewaard.`,
      );
    }
  };

  const go = (idx: number) => {
    setErrors({});
    setStepIdx(idx);
  };

  const next = () => {
    const errs = validateStep(step, d);
    if (Object.keys(errs).length) {
      setErrors(errs);
      focusFirst(fieldOrder(step, d), errs);
      return;
    }
    if (step !== "situatie" && step !== "context") setNotice(null);
    if (returnToReview) {
      const bad = firstInvalidStep(d);
      if (bad) return go(STEPS.findIndex((s) => s.id === bad));
      setReturnToReview(false);
      return go(5);
    }
    go(stepIdx + 1);
  };

  const back = () => go(Math.max(0, stepIdx - 1));

  const edit = (id: string) => {
    setReturnToReview(true);
    go(STEPS.findIndex((s) => s.id === id));
  };

  const finish = () => {
    const bad = firstInvalidStep(d);
    if (bad) {
      setReturnToReview(true);
      const idx = STEPS.findIndex((s) => s.id === bad);
      go(idx);
      setErrors(validateStep(bad, d));
      return;
    }
    setDone(true);
  };

  const houseState = done ? "done" : d.situation || "idle";
  const groups = summarizeV2(d);

  if (done) {
    return (
      <div className="v2-intake v2-intake--done">
        <div className="v2-intake__main">
          <p className="v2-kicker">Afgerond</p>
          <h1 ref={heading} tabIndex={-1} className="v2-intake__title">
            Je verhaal staat overzichtelijk klaar.
          </h1>
          <p className="v2-intake__notice v2-intake__notice--demo" role="status">
            Dit is een conceptdemo. Je gegevens zijn niet naar de adviseur verstuurd.
          </p>
          <div className="v2-intake__done-house" aria-hidden="true">
            <HouseModel state="done" intro={false} tilt={false} />
          </div>
          <div className="v2-intake__actions">
            <button type="button" className="btn btn--ghost" onClick={() => setDone(false)}>
              Antwoorden bekijken
            </button>
            <Link href="/variant-3" className="btn btn--primary">
              Terug naar de homepage
            </Link>
          </div>
        </div>
        <div className="v2-intake__side">
          <InboxPreview
            title="Zo ontvangt de adviseur jouw hulpvraag"
            subject={subjectLine(d.name, situationLabels[d.situation] ?? "")}
            intro="Gestructureerd via de begeleide intake. Geen financiële berekening of uitkomst."
            groups={groups}
          />
        </div>
      </div>
    );
  }

  const title =
    step === "context" ? (b?.contextTitle ?? "") : step === "wens" ? (b?.wishTitle ?? "") : stepTitles[step];

  return (
    <div className="v2-intake">
      <div className="v2-intake__main">
        <h1 className="v2-intake__h1">Kennismaken met de adviseur</h1>
        <Progress current={stepIdx} onJump={(i) => i < stepIdx && go(i)} />

        <form
          noValidate
          onSubmit={(e) => {
            e.preventDefault();
            if (step === "controle") finish();
            else next();
          }}
          aria-labelledby="intake-step-title"
        >
          <p className="v2-intake__stepline" aria-hidden="true">
            Stap {stepIdx + 1} van {STEPS.length} · {STEPS[stepIdx].label}
          </p>
          <h2 id="intake-step-title" ref={heading} tabIndex={-1} className="v2-intake__title">
            <span className="sr-only">
              Stap {stepIdx + 1} van {STEPS.length}:{" "}
            </span>
            {title}
          </h2>

          {notice && (step === "context" || step === "situatie") && (
            <p className="v2-intake__notice" role="status">
              {notice}
            </p>
          )}

          {step !== "situatie" && step !== "controle" && d.situation && (
            <p className="v2-intake__chosen">
              <span>
                Situatie: <strong>{situationLabels[d.situation]}</strong>
              </span>
              <button type="button" className="v2-intake__link" onClick={() => go(0)}>
                Wijzigen
              </button>
            </p>
          )}

          <div className="v2-intake__body" key={step}>
            {step === "situatie" && (
              <SituationCards
                name="intake-situatie"
                value={d.situation}
                onChange={chooseSituation}
                onPreview={setPreview}
                invalid={!!errors.situation}
                describedBy={errors.situation ? "situation-error" : undefined}
                legend={<span className="sr-only">{stepTitles.situatie}</span>}
              />
            )}
            {step === "situatie" && errors.situation && (
              <p id="situation-error" className="field__error" style={{ marginTop: "0.75rem" }}>
                {errors.situation}
              </p>
            )}

            {step === "context" &&
              b?.context.map((q, i) => (
                <div key={q.key} style={{ marginTop: i ? "2rem" : 0 }}>
                  <RadioPills
                    id={q.key}
                    legend={q.label}
                    options={q.options}
                    value={d.branch[q.key] ?? ""}
                    onChange={(v) => setBranch(q.key, v)}
                    error={errors[q.key]}
                  />
                </div>
              ))}

            {step === "wens" && b && (
              <>
                {b.wish.map((q) => (
                  <div key={q.key} style={{ marginBottom: "2rem" }}>
                    <RadioPills
                      id={q.key}
                      legend={q.label}
                      options={q.options}
                      value={d.branch[q.key] ?? ""}
                      onChange={(v) => setBranch(q.key, v)}
                      error={errors[q.key]}
                    />
                  </div>
                ))}
                <TextArea
                  id="story"
                  label={b.story.label}
                  hint={b.story.hint}
                  value={d.story}
                  onChange={(v) => update({ story: v })}
                  error={errors.story}
                  max={LIMITS.story}
                />
              </>
            )}

            {step === "timing" && (
              <>
                <RadioPills
                  id="timing"
                  legend={<span className="sr-only">{stepTitles.timing}</span>}
                  options={timingOptions}
                  value={d.timing}
                  onChange={(v) => update({ timing: v })}
                  error={errors.timing}
                />
                {d.timing === "deadline" && (
                  <div className="v2-intake__reveal">
                    <TextField
                      id="deadlineDate"
                      type="date"
                      label="Om welke datum gaat het?"
                      optional
                      value={d.deadlineDate}
                      onChange={(v) => update({ deadlineDate: v })}
                      error={errors.deadlineDate}
                    />
                    <TextArea
                      id="deadlineNote"
                      label="Wat speelt er rond die datum?"
                      optional
                      rows={3}
                      value={d.deadlineNote}
                      onChange={(v) => update({ deadlineNote: v })}
                      max={LIMITS.deadlineNote}
                    />
                  </div>
                )}
              </>
            )}

            {step === "contact" && (
              <div style={{ display: "grid", gap: "1.75rem" }}>
                <TextField
                  id="name"
                  label="Je naam"
                  autoComplete="name"
                  value={d.name}
                  onChange={(v) => update({ name: v })}
                  error={errors.name}
                  maxLength={LIMITS.name}
                />
                <RadioPills
                  id="contactPref"
                  legend="Hoe wil je dat de adviseur contact opneemt?"
                  options={contactOptions}
                  value={d.contactPref}
                  onChange={(v) => update({ contactPref: v as Data["contactPref"] })}
                  error={errors.contactPref}
                />
                <TextField
                  id="email"
                  type="email"
                  label="E-mailadres"
                  optional={d.contactPref !== "email"}
                  autoComplete="email"
                  inputMode="email"
                  value={d.email}
                  onChange={(v) => update({ email: v })}
                  error={errors.email}
                />
                <TextField
                  id="phone"
                  type="tel"
                  label="Telefoonnummer"
                  optional={d.contactPref !== "telefoon"}
                  autoComplete="tel"
                  inputMode="tel"
                  value={d.phone}
                  onChange={(v) => update({ phone: v })}
                  error={errors.phone}
                />
              </div>
            )}

            {step === "controle" && (
              <div className="v2-review">
                {groups.map((g) => (
                  <section key={g.id} className="v2-review__group" aria-labelledby={`rv-${g.id}`}>
                    <div className="v2-review__head">
                      <h3 id={`rv-${g.id}`}>{g.title}</h3>
                      <button
                        type="button"
                        className="v2-intake__link"
                        onClick={() => g.step && edit(g.step)}
                        aria-label={`${g.title} wijzigen`}
                      >
                        Wijzigen
                      </button>
                    </div>
                    <dl>
                      {g.rows.map((r) => (
                        <div key={r.label}>
                          <dt>{r.label}</dt>
                          <dd>{r.value}</dd>
                        </div>
                      ))}
                    </dl>
                  </section>
                ))}
              </div>
            )}
          </div>

          <div className="v2-intake__nav">
            {stepIdx > 0 && (
              <button type="button" className="btn btn--ghost" onClick={back}>
                Vorige
              </button>
            )}
            <button type="submit" className="btn btn--primary">
              {step === "controle"
                ? "Bekijk mijn demoaanvraag"
                : returnToReview
                  ? "Terug naar controle"
                  : step === "situatie" && d.situation
                    ? "Ga verder met deze situatie"
                    : "Volgende"}
              <Arrow />
            </button>
          </div>
          {step === "controle" && (
            <p className="small v2-intake__fine">Conceptdemo: er wordt niets verzonden of opgeslagen.</p>
          )}
        </form>
      </div>

      <aside className="v2-intake__side" aria-label="Jouw voortgang en samenvatting">
        <div className="v2-intake__house" aria-hidden="true">
          <HouseModel state={houseState} preview={step === "situatie" ? preview : null} intro={false} tilt={false} />
          <p className="v2-intake__caption">
            {situationById(d.situation || preview)?.houseCaption ?? "Jouw situatie geeft de woning vorm"}
          </p>
        </div>
        <details className="v2-intake__summary" open={sumOpen} onToggle={(e) => setSumOpen((e.target as HTMLDetailsElement).open)}>
          <summary>Jouw antwoorden tot nu toe</summary>
          <SummaryList d={d} />
        </details>
        <div className="v2-intake__paul">
          <PortraitSlot />
          <p>“{paul.intakeQuote}”</p>
        </div>
      </aside>
    </div>
  );
}

function SummaryList({ d }: { d: Data }) {
  const rows: [string, string][] = [];
  if (d.situation) rows.push(["Situatie", situationLabels[d.situation]]);
  const b = d.situation ? branches[d.situation] : null;
  b?.context.concat(b.wish).forEach((q) => {
    const v = labelOf(q.options, d.branch[q.key] ?? "");
    if (v) rows.push([q.label, v]);
  });
  if (d.story.trim()) rows.push(["Toelichting", d.story.trim().slice(0, 90) + (d.story.trim().length > 90 ? "…" : "")]);
  if (d.timing) rows.push(["Timing", labelOf(timingOptions, d.timing)]);
  if (d.name.trim()) rows.push(["Naam", d.name.trim()]);
  if (d.contactPref) rows.push(["Contact", contactOptions.find((c) => c.value === d.contactPref)!.label]);
  if (!rows.length) return <p className="small v2-intake__empty">Je antwoorden verschijnen hier.</p>;
  return (
    <dl className="v2-intake__sumlist">
      {rows.map(([k, v]) => (
        <div key={k}>
          <dt>{k}</dt>
          <dd>{v}</dd>
        </div>
      ))}
    </dl>
  );
}

function Progress({ current, onJump }: { current: number; onJump: (i: number) => void }) {
  return (
    <nav aria-label="Voortgang" className="v2-progress">
      <ol role="list">
        {STEPS.map((s, i) => {
          const state = i < current ? "done" : i === current ? "current" : "todo";
          return (
            <li key={s.id} data-state={state}>
              {i < current ? (
                <button type="button" onClick={() => onJump(i)} aria-label={`Terug naar stap ${i + 1}: ${s.label}`}>
                  <span className="v2-progress__n">{i + 1}</span>
                  <span className="v2-progress__label">{s.label}</span>
                </button>
              ) : (
                <span aria-current={i === current ? "step" : undefined}>
                  <span className="v2-progress__n">{i + 1}</span>
                  <span className="v2-progress__label">{s.label}</span>
                </span>
              )}
            </li>
          );
        })}
      </ol>
    </nav>
  );
}

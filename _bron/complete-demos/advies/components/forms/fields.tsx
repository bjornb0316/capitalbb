"use client";

import type { ReactNode } from "react";
import type { Option } from "@/lib/intake";

export function FieldError({ id, msg }: { id: string; msg?: string }) {
  if (!msg) return null;
  return (
    <p id={id} className="field__error">
      {msg}
    </p>
  );
}

const describe = (...ids: unknown[]) =>
  (ids.filter((x) => typeof x === "string" && x) as string[]).join(" ") || undefined;

export function TextField({
  id,
  label,
  value,
  onChange,
  error,
  hint,
  optional,
  type = "text",
  autoComplete,
  inputMode,
  maxLength,
}: {
  id: string;
  label: ReactNode;
  value: string;
  onChange: (v: string) => void;
  error?: string;
  hint?: ReactNode;
  optional?: boolean;
  type?: string;
  autoComplete?: string;
  inputMode?: React.HTMLAttributes<HTMLInputElement>["inputMode"];
  maxLength?: number;
}) {
  return (
    <div className="field">
      <label htmlFor={id} className="field__label">
        {label} {optional && <span className="field__optional">(optioneel)</span>}
      </label>
      {hint && (
        <p id={`${id}-hint`} className="field__hint">
          {hint}
        </p>
      )}
      <input
        id={id}
        name={id}
        className="input"
        type={type}
        value={value}
        autoComplete={autoComplete}
        inputMode={inputMode}
        maxLength={maxLength}
        aria-invalid={error ? true : undefined}
        aria-describedby={describe(hint && `${id}-hint`, error && `${id}-error`)}
        onChange={(e) => onChange(e.target.value)}
      />
      <FieldError id={`${id}-error`} msg={error} />
    </div>
  );
}

export function TextArea({
  id,
  label,
  value,
  onChange,
  error,
  hint,
  max,
  optional,
  rows = 5,
}: {
  id: string;
  label: ReactNode;
  value: string;
  onChange: (v: string) => void;
  error?: string;
  hint?: ReactNode;
  max: number;
  optional?: boolean;
  rows?: number;
}) {
  const left = max - value.length;
  return (
    <div className="field">
      <label htmlFor={id} className="field__label">
        {label} {optional && <span className="field__optional">(optioneel)</span>}
      </label>
      {hint && (
        <p id={`${id}-hint`} className="field__hint">
          {hint}
        </p>
      )}
      <textarea
        id={id}
        name={id}
        className="input"
        rows={rows}
        value={value}
        maxLength={max}
        aria-invalid={error ? true : undefined}
        aria-describedby={describe(hint && `${id}-hint`, error && `${id}-error`, `${id}-count`)}
        onChange={(e) => onChange(e.target.value)}
      />
      <p id={`${id}-count`} className="field__count" aria-live={left < 100 ? "polite" : "off"}>
        Nog {left} tekens
      </p>
      <FieldError id={`${id}-error`} msg={error} />
    </div>
  );
}

/** Radiogroep als keuzepillen. Eerste input krijgt het id voor focus bij fouten. */
export function RadioPills({
  id,
  legend,
  options,
  value,
  onChange,
  error,
  hint,
  name,
}: {
  id: string;
  legend: ReactNode;
  options: Option[];
  value: string;
  onChange: (v: string) => void;
  error?: string;
  hint?: ReactNode;
  name?: string;
}) {
  return (
    <fieldset aria-describedby={describe(hint && `${id}-hint`, error && `${id}-error`)}>
      <legend className="fieldset__legend">{legend}</legend>
      {hint && (
        <p id={`${id}-hint`} className="field__hint" style={{ marginTop: "-0.4rem", marginBottom: "0.75rem" }}>
          {hint}
        </p>
      )}
      <div className="pills" aria-invalid={error ? true : undefined}>
        {options.map((o, i) => (
          <label key={o.value} className="pill">
            <input
              type="radio"
              id={i === 0 ? id : undefined}
              name={name ?? id}
              value={o.value}
              checked={value === o.value}
              onChange={() => onChange(o.value)}
            />
            <span>{o.label}</span>
          </label>
        ))}
      </div>
      <div style={{ marginTop: error ? "0.6rem" : 0 }}>
        <FieldError id={`${id}-error`} msg={error} />
      </div>
    </fieldset>
  );
}

/** Focus op het eerste foutieve veld, in formuliervolgorde. */
export function focusFirst(order: string[], errors: Record<string, string>) {
  const first = order.find((k) => errors[k]);
  if (!first) return;
  requestAnimationFrame(() => {
    const el = document.getElementById(first);
    el?.focus();
    el?.scrollIntoView({
      block: "center",
      behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth",
    });
  });
}

"use client";

import type { SituationId } from "@/content/situations";
import { situations } from "@/content/situations";

const glyph: Record<SituationId, React.ReactNode> = {
  kopen: (
    <svg viewBox="0 0 48 48" aria-hidden="true">
      <path d="M8 22 24 9l16 13v18H8z" />
      <path d="M20 40V29h8v11" />
    </svg>
  ),
  ondernemer: (
    <svg viewBox="0 0 48 48" aria-hidden="true">
      <path d="M6 22 20 11l14 11v18H6z" />
      <path d="M34 26h9v14h-9" />
      <path d="M37 31h3" />
    </svg>
  ),
  overwaarde: (
    <svg viewBox="0 0 48 48" aria-hidden="true">
      <path d="M16 22 30 11l14 11v18H16z" />
      <path d="M4 28h12v12H4z" strokeDasharray="3 3" />
    </svg>
  ),
  complex: (
    <svg viewBox="0 0 48 48" aria-hidden="true">
      <path d="M10 24 24 13l14 11" />
      <path d="M12 28v12h24V28" />
      <rect x="6" y="6" width="7" height="7" rx="1.5" />
      <rect x="37" y="8" width="6" height="6" rx="1.5" />
    </svg>
  ),
};

/**
 * Grote keuzekaarten als toegankelijke radiogroep.
 * Gedeeld door de homepage (scène V2-02) en stap 1 van de intake.
 */
export function SituationCards({
  value,
  onChange,
  onPreview,
  name = "situatie",
  legend,
  invalid,
  describedBy,
}: {
  value: SituationId | "";
  onChange: (v: SituationId) => void;
  onPreview?: (v: SituationId | null) => void;
  name?: string;
  legend: React.ReactNode;
  invalid?: boolean;
  describedBy?: string;
}) {
  return (
    <fieldset className="v2-cards" aria-invalid={invalid || undefined} aria-describedby={describedBy}>
      <legend className="v2-cards__legend">{legend}</legend>
      <div className="v2-cards__grid">
        {cardOrder.map((id) => situations.find((x) => x.id === id)!).map((s, i) => (
          <label
            key={s.id}
            className="v2-card"
            data-checked={value === s.id}
            onPointerEnter={() => onPreview?.(s.id)}
            onPointerLeave={() => onPreview?.(null)}
          >
            <input
              type="radio"
              name={name}
              value={s.id}
              checked={value === s.id}
              onChange={() => onChange(s.id)}
              onFocus={() => onPreview?.(s.id)}
              onBlur={() => onPreview?.(null)}
            />
            <span className="v2-card__n" aria-hidden="true">
              0{i + 1}
            </span>
            <span className="v2-card__glyph">{glyph[s.id]}</span>
            <span className="v2-card__title">{s.cardTitle}</span>
            <span className="v2-card__text">{s.cardText}</span>
            <span className="v2-card__check" aria-hidden="true" />
          </label>
        ))}
      </div>
    </fieldset>
  );
}

export const cardOrder: SituationId[] = ["kopen", "ondernemer", "overwaarde", "complex"];

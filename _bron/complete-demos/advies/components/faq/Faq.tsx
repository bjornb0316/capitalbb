"use client";

import { useId, useState } from "react";
import { faq as defaultFaq } from "@/content/faq";

type Item = { q: string; a: string };

/** Toegankelijke accordeon. Gedeeld door beide varianten, stijl via className. */
export function Faq({ items = defaultFaq, className = "" }: { items?: readonly Item[]; className?: string }) {
  const [open, setOpen] = useState<number | null>(0);
  const uid = useId();
  return (
    <ul role="list" className={`faq ${className}`}>
      {items.map((it, i) => {
        const isOpen = open === i;
        return (
          <li key={it.q} className="faq__item" data-open={isOpen}>
            <h3 className="faq__q">
              <button
                type="button"
                aria-expanded={isOpen}
                aria-controls={`${uid}-${i}`}
                id={`${uid}-b${i}`}
                onClick={() => setOpen(isOpen ? null : i)}
              >
                <span>{it.q}</span>
                <span className="faq__icon" aria-hidden="true" />
              </button>
            </h3>
            <div id={`${uid}-${i}`} role="region" aria-labelledby={`${uid}-b${i}`} className="faq__a" hidden={!isOpen}>
              <p>{it.a}</p>
            </div>
          </li>
        );
      })}
    </ul>
  );
}

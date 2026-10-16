"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import { useDemo } from "./DemoContext";

export function DemoBadge({ other }: { other: { href: string; label: string } }) {
  const [open, setOpen] = useState(false);
  const { notes, setNotes } = useDemo();
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!open) return;
    const onDown = (e: PointerEvent) => {
      if (!ref.current?.contains(e.target as Node)) setOpen(false);
    };
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    document.addEventListener("pointerdown", onDown);
    document.addEventListener("keydown", onKey);
    return () => {
      document.removeEventListener("pointerdown", onDown);
      document.removeEventListener("keydown", onKey);
    };
  }, [open]);

  return (
    <div className="demo-badge" ref={ref}>
      <button
        type="button"
        className="demo-badge__toggle"
        aria-expanded={open}
        aria-controls="demo-panel"
        onClick={() => setOpen((v) => !v)}
      >
        <span className="demo-badge__dot" aria-hidden="true" />
        <span className="demo-badge__label">Conceptdemo</span>
      </button>
      {open && (
        <div id="demo-panel" className="demo-badge__panel">
          <p>
            <strong>Dit is een conceptdemo</strong> voor Onafhankelijk adviseur. Formulieren versturen niets en de site
            wordt niet geïndexeerd.
          </p>
          <label className="switch">
            <input type="checkbox" checked={notes} onChange={(e) => setNotes(e.target.checked)} />
            Toon redactionele notities
          </label>
          <div className="demo-badge__links">
            <Link href="/">Overzicht concepten</Link>
            <Link href={other.href}>{other.label}</Link>
          </div>
        </div>
      )}
    </div>
  );
}

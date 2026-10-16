"use client";

import Link from "next/link";
import { useEffect, useRef } from "react";
import { nav, paul, primaryCta } from "@/content/paul";

/** Menu-overlay met focus-trap; Escape sluit, focus keert terug naar de menuknop. */
export function MobileMenu({ base, pathname, onClose }: { base: string; pathname: string; onClose: () => void }) {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = ref.current!;
    const focusables = () =>
      Array.from(el.querySelectorAll<HTMLElement>("a[href], button:not([disabled])")).filter(
        (n) => n.offsetParent !== null,
      );
    focusables()[0]?.focus();
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";

    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        e.preventDefault();
        onClose();
        return;
      }
      if (e.key !== "Tab") return;
      const f = focusables();
      if (!f.length) return;
      const first = f[0];
      const last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    };
    document.addEventListener("keydown", onKey);
    return () => {
      document.removeEventListener("keydown", onKey);
      document.body.style.overflow = prevOverflow;
    };
  }, [onClose]);

  return (
    <div ref={ref} id="mobiel-menu" className="mobile-menu" role="dialog" aria-modal="true" aria-label="Menu">
      <div className="mobile-menu__top">
        <Link href={base} className="brand" onClick={onClose}>
          <span className="brand__name">{paul.name}</span>
          <span className="brand__sub">Financieel adviseur · {paul.place}</span>
        </Link>
        <button type="button" className="menu-button" onClick={onClose}>
          Sluiten
        </button>
      </div>
      <nav aria-label="Hoofdmenu">
        <ul role="list">
          <li>
            <Link href={base} aria-current={pathname === base ? "page" : undefined} onClick={onClose}>
              Home <span aria-hidden="true">→</span>
            </Link>
          </li>
          {nav.map((n) => (
            <li key={n.slug}>
              <Link
                href={`${base}/${n.slug}`}
                aria-current={pathname === `${base}/${n.slug}` ? "page" : undefined}
                onClick={onClose}
              >
                {n.label} <span aria-hidden="true">→</span>
              </Link>
            </li>
          ))}
        </ul>
      </nav>
      <div className="mobile-menu__contact">
        <Link href={`${base}/kennismaken`} className="btn btn--light" onClick={onClose}>
          {primaryCta}
        </Link>
        <a href={paul.contact.phoneHref} className="btn btn--outline-light">
          Bel de adviseur · {paul.contact.phoneDisplay}
        </a>
        <p className="small">
          Of mail naar{" "}
          <a className="link" href={`mailto:${paul.contact.email}`}>
            {paul.contact.email}
          </a>
        </p>
      </div>
    </div>
  );
}

"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { nav, paul, primaryCta } from "@/content/paul";
import { MobileMenu } from "./MobileMenu";
import { resetHeroOverlay } from "./heroOverlay";

/**
 * Header blijft even hoog in beide toestanden (geen springende hoogte).
 * Transparant zolang het element [data-hero-sentinel] nog in beeld is.
 */
export function Header({ base }: { base: string }) {
  const pathname = usePathname();
  const [overlay, setOverlay] = useState(false);
  const [sceneOverlay, setSceneOverlay] = useState(true);
  const [open, setOpen] = useState(false);
  const menuButton = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    resetHeroOverlay();
    setSceneOverlay(true);
    const onScene = (e: Event) => setSceneOverlay((e as CustomEvent<boolean>).detail);
    window.addEventListener("hero-overlay", onScene);
    return () => window.removeEventListener("hero-overlay", onScene);
  }, [pathname]);

  useEffect(() => {
    const sentinel = document.querySelector("[data-hero-sentinel]");
    if (!sentinel) {
      setOverlay(false);
      return;
    }
    const io = new IntersectionObserver(([e]) => setOverlay(e.isIntersecting), {
      rootMargin: "-72px 0px 0px 0px",
    });
    io.observe(sentinel);
    return () => io.disconnect();
  }, [pathname]);

  useEffect(() => setOpen(false), [pathname]);

  const isCurrent = (slug: string) => pathname === `${base}/${slug}`;

  return (
    <>
      <a className="skip-link" href="#inhoud">
        Naar de inhoud
      </a>
      <header className="site-header" data-overlay={overlay && sceneOverlay && !open ? "true" : "false"}>
        <div className="container site-header__inner">
          <Link href={base} className="brand" aria-label={`${paul.name}, naar de startpagina`}>
            <span className="brand__name">{paul.name}</span>
            <span className="brand__sub">Financieel adviseur · {paul.place}</span>
          </Link>
          <nav className="site-nav" aria-label="Hoofdmenu">
            <ul role="list">
              {nav.map((n) => (
                <li key={n.slug}>
                  <Link href={`${base}/${n.slug}`} aria-current={isCurrent(n.slug) ? "page" : undefined}>
                    {n.label}
                  </Link>
                </li>
              ))}
            </ul>
          </nav>
          <div className="site-header__actions">
            <Link href={`${base}/kennismaken`} className="btn btn--primary btn--small btn--header">
              {primaryCta}
            </Link>
            <button
              ref={menuButton}
              type="button"
              className="menu-button"
              aria-expanded={open}
              aria-controls="mobiel-menu"
              onClick={() => setOpen(true)}
            >
              <span className="menu-button__icon" aria-hidden="true">
                <span />
                <span />
              </span>
              <span className="menu-button__label">Menu</span>
            </button>
          </div>
        </div>
      </header>
      {open && (
        <MobileMenu
          base={base}
          pathname={pathname}
          onClose={() => {
            setOpen(false);
            requestAnimationFrame(() => menuButton.current?.focus());
          }}
        />
      )}
    </>
  );
}

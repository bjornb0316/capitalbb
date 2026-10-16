"use client";

import { useLayoutEffect, useEffect, type RefObject, type DependencyList } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

if (typeof window !== "undefined") {
  gsap.registerPlugin(ScrollTrigger);
  ScrollTrigger.config({ ignoreMobileResize: true });
}

const useIso = typeof window !== "undefined" ? useLayoutEffect : useEffect;

/**
 * Eén scène = één container met een eigen gsap.matchMedia-context.
 * Alles wat de setup aanmaakt (tweens, ScrollTriggers, listeners via return)
 * wordt bij unmount of routewissel opgeruimd. Geen globale scrollhandlers.
 */
export function useScene(
  scope: RefObject<HTMLElement | null>,
  setup: (mm: gsap.MatchMedia, el: HTMLElement) => void,
  deps: DependencyList = [],
) {
  useIso(() => {
    const el = scope.current;
    if (!el) return;
    const mm = gsap.matchMedia(el);
    setup(mm, el);
    // Afbeeldingen die later laden veranderen hoogtes; daarna één refresh.
    const t = window.setTimeout(() => { ScrollTrigger.sort(); ScrollTrigger.refresh(); }, 300);
    return () => {
      window.clearTimeout(t);
      mm.revert();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);
}

export { gsap, ScrollTrigger };

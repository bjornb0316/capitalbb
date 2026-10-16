// Centrale bewegingsinstellingen. Alle scènes lezen hun waarden hier,
// zodat duur, easing en scrollafstanden op één plek worden afgesteld.

export const motion = {
  duration: {
    hover: 0.2, // 150–250 ms
    form: 0.32, // 250–400 ms
    reveal: 0.7, // 500–800 ms
    scene: 1.1, // max ~1200 ms
    intro: 1.0, // opening, 0,8–1,2 s
  },
  ease: {
    out: "power3.out",
    inOut: "power2.inOut",
    soft: "sine.inOut",
    // CSS-equivalent voor transities buiten GSAP
    css: "cubic-bezier(.22,.61,.36,1)",
  },
  parallax: {
    desktop: 1,
    tablet: 0.5,
    mobile: 0,
  },
  scroll: {
    // Bijlage A: 120–160 vh extra scrollafstand, dus 1,2–1,6 × viewporthoogte.
    v1HeroDistance: "+=140%",
    v1QuestionsDistance: "+=120%",
    v1ProcessDistance: "+=110%",
    v2ShapesDistance: "+=200%",
    scrub: 0.6,
  },
  pointer: {
    maxTiltDeg: 4,
  },
  // Breakpoints voor gsap.matchMedia
  mq: {
    desktop: "(min-width: 1024px) and (prefers-reduced-motion: no-preference)",
    tablet: "(min-width: 768px) and (max-width: 1023.98px) and (prefers-reduced-motion: no-preference)",
    mobile: "(max-width: 767.98px) and (prefers-reduced-motion: no-preference)",
    motionOk: "(prefers-reduced-motion: no-preference)",
    reduced: "(prefers-reduced-motion: reduce)",
    finePointer: "(hover: hover) and (pointer: fine)",
  },
} as const;

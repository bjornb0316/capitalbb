"use client";

import Link from "next/link";
import { useRef } from "react";
import { process } from "@/content/paul";
import { useScene, gsap } from "@/components/motion/useScene";
import { motion } from "@/components/motion/config";
import { Arrow } from "@/components/contact/icons";

const PATH = "M0 1 H1220";

/**
 * Scène V1-04: werkwijze als visuele reis. Een lijn verbindt drie hoofdstukken;
 * de actieve stap krijgt contrast en een lichtaccent reist mee.
 */
export function ProcessJourney({ showCta = true, detailed = false }: { showCta?: boolean; detailed?: boolean }) {
  const root = useRef<HTMLElement>(null);

  useScene(root, (mm, el) => {
    mm.add(motion.mq.motionOk, () => {
      const path = el.querySelector<SVGPathElement>(".v1-proc__path-draw")!;
      const dot = el.querySelector<SVGGElement>(".v1-proc__dot")!;
      const steps = gsap.utils.toArray<HTMLElement>(".v1-proc__step", el);
      const len = path.getTotalLength();
      gsap.set(path, { strokeDasharray: len, strokeDashoffset: len });
      const st = { p: 0 };
      const setActive = (p: number) => {
        const idx = p < 0.3 ? 0 : p < 0.7 ? 1 : 2;
        steps.forEach((s, i) => s.toggleAttribute("data-active", i === idx));
      };
      setActive(0);
      gsap.to(st, {
        p: 1,
        ease: "none",
        scrollTrigger: {
          trigger: el.querySelector(".v1-proc__stage"),
          start: "top 70%",
          end: "bottom 45%",
          scrub: motion.scroll.scrub,
        },
        onUpdate: () => {
          path.style.strokeDashoffset = String(len * (1 - st.p));
          const pt = path.getPointAtLength(len * st.p);
          dot.setAttribute("transform", `translate(${pt.x} ${pt.y})`);
          setActive(st.p);
        },
      });
      return () => steps.forEach((s) => s.removeAttribute("data-active"));
    });
  });

  return (
    <section ref={root} className="v1-proc section" aria-labelledby="v1-proc-title">
      <div className="container">
        <h2 id="v1-proc-title" className="h2 v1-proc__title">
          Een helder vertrekpunt.
          <br />
          Een persoonlijke volgende stap.
        </h2>
        <div className="v1-proc__stage">
          <svg className="v1-proc__line" viewBox="0 0 1220 2" preserveAspectRatio="none" aria-hidden="true">
            <path d={PATH} className="v1-proc__path-base" />
            <path d={PATH} className="v1-proc__path-draw" />
            <g className="v1-proc__dot" transform="translate(0 1)" />
          </svg>
          <ol role="list" className="v1-proc__steps">
            {process.map((s) => (
              <li key={s.n} className={`v1-proc__step v1-proc__step--${s.n}`}>
                <span className="v1-proc__n" aria-hidden="true">
                  {["I", "II", "III"][s.n - 1]}
                </span>
                <h3 className="h3">{s.title}</h3>
                <p>{s.text}</p>
                {detailed && <p className="v1-proc__detail">{s.detail}</p>}
              </li>
            ))}
          </ol>
        </div>
        {showCta && (
          <div className="v1-proc__cta">
            <Link href="/variant-2/werkwijze" className="btn btn--ghost">
              Bekijk de werkwijze <Arrow />
            </Link>
          </div>
        )}
      </div>
    </section>
  );
}

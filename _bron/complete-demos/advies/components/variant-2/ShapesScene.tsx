"use client";

import Link from "next/link";
import { useRef, useState } from "react";
import { situations } from "@/content/situations";
import Image from "next/image";
import { useScene, ScrollTrigger } from "@/components/motion/useScene";
import { motion } from "@/components/motion/config";
import { Arrow } from "@/components/contact/icons";

const order = ["kopen", "ondernemer", "overwaarde", "complex"] as const;

/**
 * Scène V2-03: wensen krijgen vorm. Desktop: korte pinned compositie waarin
 * de woning per situatie verandert. Mobiel: vier compacte vignetten.
 */
export function ShapesScene() {
  const root = useRef<HTMLElement>(null);
  const [active, setActive] = useState(0);

  useScene(root, (mm, el) => {
    mm.add(motion.mq.motionOk, () => {
      const st = ScrollTrigger.create({
        trigger: el.querySelector(".v2-shapes__pin"),
        start: "top top",
        pin: true,
        anticipatePin: 1,
        invalidateOnRefresh: true,
        refreshPriority: 10,
        end: () => `+=${window.innerHeight * 3.6}`,
        scrub: true,
        onUpdate: (self) => setActive(Math.min(3, Math.floor(self.progress * 4))),
      });
      return () => st.kill();
    });
  });

  const current = situations.find((s) => s.id === order[active])!;

  return (
    <section ref={root} className="v2-shapes" aria-labelledby="v2-shapes-title">
      <div className="v2-shapes__pin">
        <div className="container v2-shapes__grid">
          <div className="v2-shapes__text">
            <h2 id="v2-shapes-title" className="h2">
              Jouw situatie geeft richting aan het gesprek.
            </h2>
            <p className="lead">Met een paar gerichte vragen help je de adviseur begrijpen wat je wilt bereiken.</p>
            <ol role="list" className="v2-shapes__list">
              {order.map((id, i) => {
                const s = situations.find((x) => x.id === id)!;
                return (
                  <li key={id} data-active={i === active}>
                    <span className="v2-shapes__dot" aria-hidden="true" />
                    <span>
                      <strong>{s.cardTitle}</strong>
                      <span className="v2-shapes__cap">{s.houseCaption}</span>
                    </span>
                  </li>
                );
              })}
            </ol>
            <p className="v2-shapes__note small">Visuele metaforen, geen voorspelling van financiële mogelijkheden.</p>
            <Link href="/variant-3/kennismaken" className="btn btn--primary">
              Begin mijn kennismaking <Arrow />
            </Link>
          </div>
          <div className="v2-shapes__stage v2-blueprint" data-active={order[active]} >
            <Image src="/demos/advies/assets/paul/v2-exterior-unique.webp" alt="" width={1672} height={941} sizes="(min-width:1024px) 60vw,100vw" className="v2-blueprint__image" />
            <div className="v2-blueprint__focus" />
            <p className="v2-shapes__label">
              <span>{String(active + 1).padStart(2, "0")}</span> {current.houseCaption}
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

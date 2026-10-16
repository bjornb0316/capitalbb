"use client";

import Link from "next/link";
import { useId, useRef, useState } from "react";
import { assets } from "@/content/assets";
import { situations } from "@/content/situations";
import { SceneImage } from "@/components/house/SceneImage";
import { useScene, gsap } from "@/components/motion/useScene";
import { motion } from "@/components/motion/config";
import { Arrow } from "@/components/contact/icons";

/** Scène V1-02: financiële vragen verschijnen rond de woning. Eén vraag tegelijk open. */
export function QuestionsScene() {
  const root = useRef<HTMLElement>(null);
  const [open, setOpen] = useState<string | null>(null);
  const uid = useId();

  useScene(root, (mm, el) => {
    mm.add(motion.mq.motionOk, () => {
      const stage = el.querySelector<HTMLElement>(".v1-q__stage")!;
      const plates = gsap.utils.toArray<HTMLElement>(".v1-q__plate", stage);
      const intro = stage.querySelector<HTMLElement>(".v1-q__intro")!;
      const img = stage.querySelector<HTMLElement>(".v1-q__image")!;
      const tl = gsap.timeline({
        defaults: { ease: "power2.out" },
        scrollTrigger: {
          trigger: stage,
          start: "top 80%",
          end: 'bottom 75%',
          scrub: motion.scroll.scrub,
          anticipatePin: 1,
        },
      });
      tl.from(img, { scale: 1.08, duration: 0.3, ease: "none" }, 0);
      tl.from(intro, { autoAlpha: 0, y: 30, duration: 0.12 }, 0);
      plates.forEach((p, i) => tl.from(p, { autoAlpha: 0, y: 34, duration: 0.12 }, 0.12 + i * 0.13));
      // Afsluiting brengt de woning naar de achtergrond
    });
  });

  return (
    <section ref={root} className="v1-q" id="aanpak" aria-labelledby="v1-q-title">
      <div className="v1-q__stage">
        <div className="v1-q__image" aria-hidden="true">
          <SceneImage asset={assets.exteriorDesktop} kind="question" className="scene-fill" idp="q" />
          <p className="v1-q__image-caption">{open ? situations.find(s=>s.id===open)?.cardTitle : 'Ruimte voor jouw volgende stap.'}</p>
        </div>

        <div className="v1-q__intro">
          <h2 id="v1-q-title" className="h2">
            Niet iedere situatie past in een standaardplaatje.
          </h2>
          <p>
            Een eigen onderneming, een volgende woning of een vraag die extra aandacht vraagt. Het begint bij begrijpen
            wat jij wilt bereiken.
          </p>
        </div>

        <ul role="list" className="v1-q__plates">
          {situations.map((s, i) => {
            const isOpen = open === s.id;
            const panelId = `${uid}-${s.id}`;
            return (
              <li key={s.id} className={`v1-q__plate v1-q__plate--${i + 1}`} data-open={isOpen}>
                <h3>
                  <button
                    type="button"
                    aria-expanded={isOpen}
                    aria-controls={panelId}
                    onClick={() => setOpen(isOpen ? null : s.id)}
                  >
                    <span className="v1-q__num" aria-hidden="true">
                      0{i + 1}
                    </span>
                    <span className="v1-q__question">{s.question}</span>
                    <span className="v1-q__plus" aria-hidden="true" />
                  </button>
                </h3>
                <div id={panelId} className="v1-q__answer" hidden={!isOpen}>
                  <p>{s.answer}</p>
                  <Link href={`/variant-2/kennismaken?onderwerp=${s.id}`} className="text-link">
                    Bespreek mijn situatie <Arrow />
                  </Link>
                </div>
              </li>
            );
          })}
        </ul>
      </div>
    </section>
  );
}

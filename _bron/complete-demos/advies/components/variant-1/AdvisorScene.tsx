"use client";

import Link from "next/link";
import { useRef } from "react";
import { paul } from "@/content/paul";
import { PortraitNote, PortraitSlot } from "@/components/contact/PortraitSlot";
import { useScene, gsap } from "@/components/motion/useScene";
import { motion } from "@/components/motion/config";
import { Arrow } from "@/components/contact/icons";

/** Scène V1-03: de adviseur verschijnt. Eenvoudige mask-reveal van het portret. */
export function AdvisorScene() {
  const root = useRef<HTMLElement>(null);
  useScene(root, (mm, el) => {
    mm.add(motion.mq.motionOk, () => {
      const portrait = el.querySelector(".v1-paul__portrait");
      const lines = el.querySelectorAll("[data-line]");
      gsap.fromTo(
        portrait,
        { clipPath: "inset(14% 10% 14% 10%)", scale: 1.08 },
        {
          clipPath: "inset(0% 0% 0% 0%)",
          scale: 1,
          ease: "none",
          scrollTrigger: { trigger: portrait, start: "top 90%", end: "top 35%", scrub: motion.scroll.scrub },
        },
      );
      gsap.from(lines, {
        y: 30,
        autoAlpha: 0,
        stagger: 0.1,
        duration: motion.duration.reveal,
        ease: motion.ease.out,
        scrollTrigger: { trigger: el, start: "top 70%", once: true },
      });
    });
  });

  return (
    <section ref={root} className="v1-paul section" aria-labelledby="v1-paul-title">
      <div className="container v1-paul__grid">
        <h2 id="v1-paul-title" className="h2 v1-paul__title">
          <span data-line>Vertel me wat je wilt bereiken.</span> <span data-line>Ik kijk met je mee.</span>
        </h2>
        <div className="v1-paul__portrait-wrap">
          <PortraitSlot className="v1-paul__portrait" />

        </div>
        <div className="v1-paul__text">
          <p className="lead" data-line>
            {paul.introV1}
          </p>
          <p className="v1-paul__motto" data-line>
            “{paul.motto}”
          </p>
          <p className="v1-paul__meta caps" data-line>
            {paul.name} · {paul.role}
          </p>
          <div data-line>
            <Link href="/variant-2/over-adviseur" className="text-link">
              Meer over de adviseur <Arrow />
            </Link>
          </div>
          <PortraitNote />
        </div>
      </div>
    </section>
  );
}

"use client";

import { useRef, type ElementType, type ReactNode } from "react";
import { useScene, gsap } from "./useScene";
import { motion } from "./config";

/**
 * Rustige sectieonthulling. Inhoud staat altijd in de HTML; zonder JS of bij
 * verminderde beweging is alles direct zichtbaar.
 */
export function Reveal({
  children,
  as: Tag = "div",
  className,
  stagger = 0.08,
  y = 28,
  selector = "[data-reveal]",
}: {
  children: ReactNode;
  as?: ElementType;
  className?: string;
  stagger?: number;
  y?: number;
  selector?: string;
}) {
  const ref = useRef<HTMLElement>(null);
  useScene(ref, (mm, el) => {
    mm.add(motion.mq.motionOk, () => {
      const items = el.querySelectorAll(selector);
      const targets = items.length ? items : [el];
      gsap.from(targets, {
        y,
        autoAlpha: 0,
        duration: motion.duration.reveal,
        ease: motion.ease.out,
        stagger,
        scrollTrigger: { trigger: el, start: "top 82%", once: true },
      });
    });
  });
  return (
    <Tag ref={ref} className={className}>
      {children}
    </Tag>
  );
}

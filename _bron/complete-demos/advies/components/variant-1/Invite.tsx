"use client";

import Link from "next/link";
import { useRef } from "react";
import { assets } from "@/content/assets";
import { primaryCta } from "@/content/paul";
import { SceneImage } from "@/components/house/SceneImage";
import { Arrow } from "@/components/contact/icons";
import { useScene, gsap } from "@/components/motion/useScene";
import { motion } from "@/components/motion/config";

/** Scène V1-07: rustige afronding van de woningreis, binnen. */
export function Invite({
  title = "Wat wil jij mogelijk maken?",
  text = "Vertel kort waar je staat en wat je wilt bereiken. Dan hebben we een goed vertrekpunt voor een kennismaking.",
}: {
  title?: string;
  text?: string;
}) {
  const root = useRef<HTMLElement>(null);
  useScene(root, (mm, el) => {
    mm.add(motion.mq.motionOk, () => {
      gsap.fromTo(
        el.querySelector(".v1-invite__media .scene-fill"),
        { yPercent: -6, scale: 1.08 },
        {
          yPercent: 6,
          scale: 1.08,
          ease: "none",
          scrollTrigger: { trigger: el, start: "top bottom", end: "bottom top", scrub: true },
        },
      );
    });
  });
  return (
    <section ref={root} className="v1-invite" aria-labelledby="v1-invite-title">
      <div className="v1-invite__media" aria-hidden="true">
        <SceneImage asset={assets.interiorDesktop} kind="interior" className="scene-fill only-desktop" idp="inv-d" />
        <SceneImage
          asset={assets.interiorMobile ?? assets.interiorDesktop}
          kind="interior"
          className="scene-fill only-mobile"
          idp="inv-m"
        />
      </div>
      <div className="container v1-invite__wrap">
        <div className="v1-invite__card">
          <h2 id="v1-invite-title" className="h2">
            {title}
          </h2>
          <p className="lead">{text}</p>
          <Link href="/variant-2/kennismaken" className="btn btn--primary">
            {primaryCta} <Arrow />
          </Link>
        </div>
      </div>
    </section>
  );
}

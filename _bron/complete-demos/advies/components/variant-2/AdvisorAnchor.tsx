import Link from "next/link";
import { paul } from "@/content/paul";
import { PortraitNote, PortraitSlot } from "@/components/contact/PortraitSlot";
import { Reveal } from "@/components/motion/Reveal";
import { Arrow } from "@/components/contact/icons";

/** Scène V2-04: de adviseur als persoonlijk anker, naast een rustige uitsnede van het model. */
export function AdvisorAnchor({ cta = true }: { cta?: boolean }) {
  return (
    <section className="v2-paul section" aria-labelledby="v2-paul-title">
      <div className="container v2-paul__grid">
        <div className="v2-paul__visual">
          <PortraitSlot className="v2-paul__portrait" />
        </div>
        <Reveal className="v2-paul__text">
          <p className="v2-kicker" data-reveal>
            {paul.role} · {paul.place}
          </p>
          <h2 id="v2-paul-title" className="h2" data-reveal>
            Achter iedere vraag zit een persoonlijk verhaal.
          </h2>
          <p className="lead" data-reveal>
            {paul.introV2}
          </p>
          <blockquote className="v2-paul__motto" data-reveal>
            “{paul.motto}”
          </blockquote>
          {cta && (
            <div data-reveal>
              <Link href="/variant-3/over-adviseur" className="btn btn--ghost">
                Ontmoet de adviseur <Arrow />
              </Link>
            </div>
          )}
          <PortraitNote />
        </Reveal>
      </div>
    </section>
  );
}

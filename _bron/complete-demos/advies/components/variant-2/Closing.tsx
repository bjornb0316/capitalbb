import Link from "next/link";
import { expectations, primaryCta } from "@/content/paul";
import { Faq } from "@/components/faq/Faq";
import { SceneImage } from "@/components/house/SceneImage";
import { assets } from "@/content/assets";
import { EditorialNote } from "@/components/demo/DemoContext";
import { Reveal } from "@/components/motion/Reveal";
import { Arrow } from "@/components/contact/icons";

/** Scène V2-06: verwachtingen (zonder verzonnen bewijs), FAQ en afronding. */
export function Expect() {
  return (
    <section className="v2-exp section" aria-labelledby="v2-exp-title">
      <div className="container">
        <h2 id="v2-exp-title" className="h2 v2-exp__title">
          Wat je van een eerste gesprek mag verwachten
        </h2>
        <EditorialNote>
          Eigen reviews van de adviseur komen hier pas na verificatie, met bron en toestemming. Geen score afgeleid van
          het adviesnetwerk-netwerkcijfers.
        </EditorialNote>
        <Reveal as="ul" className="v2-exp__list">
          {expectations.map((x, i) => (
            <li key={x.title} data-reveal>
              <span className="v2-exp__n">{String(i + 1).padStart(2, "0")}</span>
              <h3 className="h3">{x.title}</h3>
              <p>{x.text}</p>
            </li>
          ))}
        </Reveal>
      </div>
    </section>
  );
}

export function FaqBlock({ title = "Eerst even weten waar je aan toe bent?" }: { title?: string }) {
  return (
    <section className="v2-faq section" aria-labelledby="v2-faq-title">
      <div className="container v2-faq__grid">
        <h2 id="v2-faq-title" className="h2">
          {title}
        </h2>
        <Faq className="v2-faq__list" />
      </div>
    </section>
  );
}

export function Closing({ title = "Jouw verhaal is het vertrekpunt." }: { title?: string }) {
  return (
    <section className="v2-close" aria-labelledby="v2-close-title">
      <div className="v2-close__backdrop" aria-hidden="true">
        <SceneImage asset={{src:'/demos/advies/assets/paul/v2-house-garden.webp',width:1280,height:720,alt:'Een open entree met zicht op een warme woonkamer'}} kind="exterior" className="scene-fill" idp="v2-close" />
      </div>
      <div className="container v2-close__inner">
        <div className="v2-close__text">
          <p className="v2-kicker">Een volgende stap begint met een gesprek</p>
          <h2 id="v2-close-title" className="v2-close__title">
            {title}
          </h2>
          <Link href="/variant-3/kennismaken" className="btn btn--accent">
            {primaryCta} <Arrow />
          </Link>
        </div>
      </div>
    </section>
  );
}

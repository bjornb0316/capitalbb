import type { Metadata } from "next";
import Link from "next/link";
import { situations } from "@/content/situations";
import Image from "next/image";
import { FaqBlock, Closing } from "@/components/variant-2/Closing";
import { Reveal } from "@/components/motion/Reveal";
import { Arrow } from "@/components/contact/icons";

export const metadata: Metadata = { title: "Jouw situatie" };
const chapterImages = {ondernemer:'/demos/advies/assets/paul/v2-house-interior.webp',kopen:'/demos/advies/assets/paul/v2-exterior-unique.webp',overwaarde:'/demos/advies/assets/paul/v2-house-garden.webp',complex:'/demos/advies/assets/paul/v2-exterior-unique.webp'};

export default function Page() {
  return (
    <>
      <section className="v2-page-hero">
        <div className="container">
          <div>
            <p className="v2-kicker">Jouw situatie</p>
            <h1>Vier situaties, één vertrekpunt.</h1>
            <p className="lead">
              Herken je jezelf? Lees wat er speelt en start de kennismaking direct met jouw situatie ingevuld. Staat je
              vraag er niet tussen, dan kun je die gewoon toelichten.
            </p>
          </div>
          <div className="v2-page-hero__art" aria-hidden="true">
            <Image src="/demos/advies/assets/paul/v2-exterior-unique.webp" alt="De moderne woning met lichte gevel en een open entree" width={1672} height={941} sizes="50vw" className="v2-editorial-image" />
          </div>
        </div>
      </section>
      <nav className="v2-sit-nav" aria-label="Situaties op deze pagina">
        <div className="container">
          <ul role="list">
            {situations.map((s) => (
              <li key={s.id}>
                <a href={`#${s.id}`}>{s.cardTitle}</a>
              </li>
            ))}
          </ul>
        </div>
      </nav>
      {situations.map((s, i) => (
        <section key={s.id} id={s.id} className="v2-chapter" aria-labelledby={`${s.id}-t`}>
          <div className="container v2-chapter__grid">
            <div className="v2-chapter__visual" aria-hidden="true">
              <Image src={chapterImages[s.id]} alt="" width={1672} height={941} sizes="(min-width:1024px) 45vw,100vw" className="v2-editorial-image" />
              <p className="v2-intake__caption">{s.houseCaption}</p>
            </div>
            <Reveal>
              <span className="v2-chapter__label" data-reveal>
                Situatie {i + 1}
              </span>
              <h2 id={`${s.id}-t`} className="h2" data-reveal>
                {s.chapter.title}
              </h2>
              <h3 data-reveal>Herken je dit?</h3>
              <ul className="v2-ticks" data-reveal>
                {s.chapter.recognition.map((r) => (
                  <li key={r}>{r}</li>
                ))}
              </ul>
              <h3 data-reveal>Zo pakt de adviseur het aan</h3>
              <p className="v2-chapter__approach" data-reveal>
                {s.chapter.approach}
              </p>
              <div className="v2-chapter__cta" data-reveal>
                <Link href={`/variant-3/kennismaken?situatie=${s.id}`} className="btn btn--primary">
                  Start met deze situatie <Arrow />
                </Link>
              </div>
            </Reveal>
          </div>
        </section>
      ))}
      <FaqBlock title="Vragen die vaak spelen" />
      <Closing />
    </>
  );
}

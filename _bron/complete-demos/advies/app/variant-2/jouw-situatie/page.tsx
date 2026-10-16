import type { Metadata } from "next";
import Link from "next/link";
import { situations } from "@/content/situations";
import { assets } from "@/content/assets";
import { SceneImage } from "@/components/house/SceneImage";
import { FaqSection } from "@/components/variant-1/FaqSection";
import { Invite } from "@/components/variant-1/Invite";
import { Reveal } from "@/components/motion/Reveal";
import { Arrow } from "@/components/contact/icons";

export const metadata: Metadata = { title: "Jouw situatie" };

export default function Page() {
  return (
    <>
      <section className="v1-page-hero">
        <div className="container">
          <p className="eyebrow">Jouw situatie</p>
          <h1>Iedere vraag begint bij een eigen verhaal.</h1>
          <p className="lead">
            Herken je jezelf in een van deze situaties? Lees wat er speelt en hoe de adviseur ermee aan de slag gaat. Staat
            jouw vraag er niet tussen, dan is dat geen probleem.
          </p>
          <nav aria-label="Situaties op deze pagina" className="v1-sit-index">
            {situations.map((s) => (
              <a key={s.id} href={`#${s.id}`}>
                {s.chapter.title}
              </a>
            ))}
          </nav>
        </div>
      </section>
      <div className="v1-band" aria-hidden="true">
        <SceneImage asset={assets.workspace} kind="workspace" className="scene-fill" idp="sit" />
      </div>
      <div className="container">
        {situations.map((s, i) => (
          <section
            key={s.id}
            id={s.id}
            className="v1-chapter"
            aria-labelledby={`${s.id}-t`}
            style={{ scrollMarginTop: "100px" }}
          >
            <div className="v1-chapter__grid">
              <div>
                <p className="v1-chapter__n" aria-hidden="true">
                  Situatie 0{i + 1}
                </p>
                <h2 id={`${s.id}-t`} className="h2">
                  {s.chapter.title}
                </h2>
                <p className="v1-chapter__q">{s.question}</p>
              </div>
              <Reveal>
                <h3 data-reveal>Herken je dit?</h3>
                <ul className="v1-checks" data-reveal>
                  {s.chapter.recognition.map((r) => (
                    <li key={r}>{r}</li>
                  ))}
                </ul>
                <div className="v1-chapter__approach" data-reveal>
                  <h3>Zo kijkt de adviseur mee</h3>
                  <p>{s.chapter.approach}</p>
                  <Link href={`/variant-2/kennismaken?onderwerp=${s.id}`} className="text-link">
                    Bespreek mijn situatie <Arrow />
                  </Link>
                </div>
              </Reveal>
            </div>
          </section>
        ))}
      </div>
      <FaqSection title="Vragen die vaak spelen" />
      <Invite
        title="Staat jouw situatie er niet tussen?"
        text="Vertel kort wat er speelt. Dan kijkt de adviseur met je mee wat een goede eerste stap is."
      />
    </>
  );
}

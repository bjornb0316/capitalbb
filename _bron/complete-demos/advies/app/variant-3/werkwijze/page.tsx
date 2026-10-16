import type { Metadata } from "next";
import { ProcessChapters } from "@/components/variant-2/ProcessChapters";
import { Closing, FaqBlock } from "@/components/variant-2/Closing";
import Image from "next/image";
import { EditorialNote } from "@/components/demo/DemoContext";
import { discussed, prepare, later } from "@/content/workflow";

export const metadata: Metadata = { title: "Werkwijze" };

export default function Page() {
  return (
    <>
      <section className="v2-page-hero">
        <div className="container">
          <div>
            <p className="v2-kicker">Werkwijze</p>
            <h1>Stap voor stap naar een helder vervolg.</h1>
            <p className="lead">
              Je vertelt je verhaal, de adviseur onderzoekt de mogelijkheden en jij beslist over de volgende stap.
            </p>
          </div>
          <div className="v2-page-hero__art" aria-hidden="true">
            <Image src="/demos/advies/assets/paul/v2-house-interior.webp" alt="Een rustige woonkamer voor een persoonlijk gesprek" width={1672} height={941} sizes="50vw" className="v2-editorial-image" />
          </div>
        </div>
      </section>
      <ProcessChapters detailed cta={false} title="Drie stappen" />
      <section className="section" aria-label="Details van de kennismaking">
        <div className="container">
          <div className="v2-prep">
            <div className="v2-prep__card">
              <h2>Wat we bespreken</h2>
              <ul className="v2-ticks">
                {discussed.map((d) => (
                  <li key={d}>{d}</li>
                ))}
              </ul>
            </div>
            <div className="v2-prep__card v2-prep__card--accent">
              <h2>Wat je kunt voorbereiden</h2>
              <ul className="v2-ticks">
                {prepare.map((d) => (
                  <li key={d}>{d}</li>
                ))}
              </ul>
              <p className="small" style={{ marginTop: "1rem" }}>
                Documenten zijn voor een eerste kennismaking niet nodig.
              </p>
            </div>
            <div className="v2-prep__card v2-prep__card--dark">
              <h2>Wat pas later wordt bepaald</h2>
              <ul className="v2-ticks">
                {later.map((d) => (
                  <li key={d}>{d}</li>
                ))}
              </ul>
            </div>
          </div>
          <EditorialNote>
            Kosten en vrijblijvendheid van het eerste gesprek pas vermelden na bevestiging door de adviseur.
          </EditorialNote>
        </div>
      </section>
      <FaqBlock />
      <Closing />
    </>
  );
}

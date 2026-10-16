import type { Metadata } from "next";
import { ProcessJourney } from "@/components/variant-1/ProcessJourney";
import { Invite } from "@/components/variant-1/Invite";
import { EditorialNote } from "@/components/demo/DemoContext";
import { discussed, prepare, later } from "@/content/workflow";

export const metadata: Metadata = { title: "Werkwijze" };

export default function Page() {
  return (
    <>
      <section className="v1-page-hero">
        <div className="container">
          <p className="eyebrow">Werkwijze</p>
          <h1>Zo zetten we samen de eerste stap.</h1>
          <p className="lead">
            Geen ingewikkeld traject vooraf. Je vertelt wat er speelt, de adviseur onderzoekt de mogelijkheden en jij beslist
            over het vervolg.
          </p>
        </div>
      </section>
      <ProcessJourney showCta={false} detailed />
      <section className="section" aria-label="Details van de kennismaking">
        <div className="container v1-prep">
          <div className="v1-prep__card">
            <h2>Wat we bespreken</h2>
            <ul className="v1-checks">
              {discussed.map((d) => (
                <li key={d}>{d}</li>
              ))}
            </ul>
          </div>
          <div className="v1-prep__card">
            <h2>Wat je kunt voorbereiden</h2>
            <ul className="v1-checks">
              {prepare.map((d) => (
                <li key={d}>{d}</li>
              ))}
            </ul>
            <p className="small" style={{ marginTop: "1rem", color: "var(--ink-soft)" }}>
              Documenten zijn voor een eerste kennismaking niet nodig.
            </p>
          </div>
          <div className="v1-prep__card v1-prep__card--dark">
            <h2>Wat pas later wordt bepaald</h2>
            <ul className="v1-checks">
              {later.map((d) => (
                <li key={d}>{d}</li>
              ))}
            </ul>
          </div>
        </div>
        <div className="container">
          <EditorialNote>
            Kosten en vrijblijvendheid van het eerste gesprek worden hier pas vermeld na bevestiging door de adviseur (het
            het adviesnetwerk-profiel noemt een gratis, vrijblijvend eerste gesprek).
          </EditorialNote>
        </div>
      </section>
      <Invite />
    </>
  );
}

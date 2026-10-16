import type { Metadata } from "next";
import { paul, expectations } from "@/content/paul";
import { AdvisorAnchor } from "@/components/variant-2/AdvisorAnchor";
import { Closing } from "@/components/variant-2/Closing";
import { EditorialNote } from "@/components/demo/DemoContext";

export const metadata: Metadata = { title: "Over de adviseur" };

export default function Page() {
  return (
    <>
      <section className="v2-page-hero">
        <div className="container">
          <div>
            <p className="v2-kicker">Over de adviseur</p>
            <h1>Kan niet, ken ik niet.</h1>
            <p className="lead">
              Ik ben {paul.name}, {paul.role.toLowerCase()} in {paul.place}. Ik help particulieren en ondernemers met
              financiële vragen, ook als die extra uitzoekwerk vragen.
            </p>
            <EditorialNote>
              Concepttekst; de adviseur keurt de definitieve formulering goed. Geen biografie of persoonlijke details
              toegevoegd.
            </EditorialNote>
          </div>
        </div>
      </section>
      <AdvisorAnchor cta={false} />
      <section className="section" style={{ paddingTop: 0 }} aria-labelledby="facts-t">
        <div className="container" style={{ display: "grid", gap: "2rem" }}>
          <h2 id="facts-t" className="h2">
            Zakelijk in het kort
          </h2>
          <dl className="v2-facts">
            <div>
              <dt>Rol</dt>
              <dd>{paul.role}</dd>
            </div>
            <div>
              <dt>Werkgebied</dt>
              <dd>{paul.place} en omgeving</dd>
            </div>
            <div>
              <dt>Aansluiting</dt>
              <dd>Aangesloten bij {paul.network}</dd>
            </div>
            <div>
              <dt>Aandacht voor</dt>
              <dd>Complexe vragen van particulieren en ondernemers</dd>
            </div>
          </dl>
          <h2 className="h2" style={{ marginTop: "2rem" }}>
            Wat je van de kennismaking mag verwachten
          </h2>
          <div className="v2-prep">
            {expectations.map((e, i) => (
              <div key={e.title} className={`v2-prep__card ${i === 1 ? "v2-prep__card--accent" : ""}`}>
                <h3 className="h3" style={{ marginBottom: "0.5rem" }}>
                  {e.title}
                </h3>
                <p>{e.text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
      <Closing />
    </>
  );
}

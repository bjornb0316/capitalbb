import type { Metadata } from "next";
import { paul, expectations } from "@/content/paul";
import { PortraitNote, PortraitSlot } from "@/components/contact/PortraitSlot";
import { Invite } from "@/components/variant-1/Invite";
import { EditorialNote } from "@/components/demo/DemoContext";

export const metadata: Metadata = { title: "Over de adviseur" };

export default function Page() {
  return (
    <>
      <section className="v1-page-hero">
        <div className="container">
          <p className="eyebrow">Over de adviseur</p>
          <h1>Persoonlijk, betrokken en oplossingsgericht.</h1>
        </div>
      </section>
      <section className="container" style={{ paddingBottom: "var(--section)" }} aria-label="Over Onafhankelijk adviseur">
        <div className="v1-about">
          <div className="v1-about__portrait">
            <PortraitSlot />
            <PortraitNote />
          </div>
          <div className="v1-about__body">
            <p className="v1-about__quote">“{paul.motto}”</p>
            <p className="lead" style={{ color: "var(--ink)" }}>
              Dat motto is geen slogan, maar een manier van werken. Ik ben {paul.name}, {paul.role.toLowerCase()} in{" "}
              {paul.place}. Ik richt me op financiële vragen van particulieren en ondernemers, ook als die niet
              vanzelfsprekend zijn.
            </p>
            <p>
              {paul.introV1} Je hebt één vast aanspreekpunt, van het eerste gesprek tot de vervolgstappen die bij jouw
              situatie horen.
            </p>
            <EditorialNote>
              Concepttekst in de ik-vorm. De adviseur keurt de definitieve formulering goed; geen biografische details
              toegevoegd.
            </EditorialNote>
            <dl className="v1-facts">
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
                <dd>Complexe financiële vragen van particulieren en ondernemers</dd>
              </div>
            </dl>
            <h2 className="h3" style={{ marginTop: "3rem" }}>
              Wat je van een kennismaking kunt verwachten
            </h2>
            <ul className="v1-checks" style={{ marginTop: "1rem" }}>
              {expectations.map((e) => (
                <li key={e.title}>
                  <span>
                    <strong>{e.title}.</strong> {e.text}
                  </span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </section>
      <Invite />
    </>
  );
}

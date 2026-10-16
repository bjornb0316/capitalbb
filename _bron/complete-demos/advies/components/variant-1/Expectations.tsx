import { expectations } from "@/content/paul";
import { Reveal } from "@/components/motion/Reveal";
import { EditorialNote } from "@/components/demo/DemoContext";

/** Scène V1-05 zonder geverifieerde reviews: eerlijk en concreet. */
export function Expectations() {
  return (
    <section className="v1-exp section" aria-labelledby="v1-exp-title">
      <div className="container v1-exp__grid">
        <div className="v1-exp__head">
          <h2 id="v1-exp-title" className="h2">
            Wat je van een eerste gesprek mag verwachten
          </h2>
          <EditorialNote>
            Zodra de adviseur eigen reviews aanlevert met toestemming en bron, komen hier maximaal drie korte ervaringen met
            een link naar de originele bron. het adviesnetwerk-netwerkcijfers worden niet als de adviseur zijn eigen score getoond.
          </EditorialNote>
        </div>
        <Reveal as="ul" className="v1-exp__list">
          {expectations.map((x, i) => (
            <li key={x.title} data-reveal>
              <span className="v1-exp__n caps">{String(i + 1).padStart(2, "0")}</span>
              <div>
                <h3 className="h3">{x.title}</h3>
                <p>{x.text}</p>
              </div>
            </li>
          ))}
        </Reveal>
      </div>
    </section>
  );
}

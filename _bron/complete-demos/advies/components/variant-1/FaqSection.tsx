import { Faq } from "@/components/faq/Faq";
import { EditorialNote } from "@/components/demo/DemoContext";

/** Scène V1-06: vragen. */
export function FaqSection({ title = "Eerst even weten waar je aan toe bent?" }: { title?: string }) {
  return (
    <section className="v1-faq section" aria-labelledby="v1-faq-title">
      <div className="container v1-faq__grid">
        <div className="v1-faq__head">
          <h2 id="v1-faq-title" className="h2">
            {title}
          </h2>
          <EditorialNote>
            Antwoorden zijn bewust terughoudend. Kosten, gespreksduur en beschikbaarheid pas noemen na bevestiging door
            de adviseur.
          </EditorialNote>
        </div>
        <Faq className="v1-faq__list" />
      </div>
    </section>
  );
}

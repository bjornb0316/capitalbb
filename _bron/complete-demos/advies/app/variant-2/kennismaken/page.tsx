import type { Metadata } from "next";
import { paul } from "@/content/paul";
import { IntakeV1 } from "@/components/forms/IntakeV1";
import { ContactOptions } from "@/components/contact/ContactOptions";
import { PortraitSlot } from "@/components/contact/PortraitSlot";

export const metadata: Metadata = { title: "Kennismaken" };

export default function Page() {
  return (
    <section className="v1-contact" aria-labelledby="v1-contact-title">
      <>
        <IntakeV1
          aside={
            <div className="v1-contact__aside">
              <p className="eyebrow" style={{ marginBottom: "1rem" }}>
                Kennismaken
              </p>
              <h1 id="v1-contact-title">Vertel de adviseur jouw situatie.</h1>
              <p className="lead">
                Een paar zinnen is genoeg. Dan heeft de adviseur een goed vertrekpunt voor een eerste gesprek.
              </p>
              <div className="v1-contact__mini">
                <PortraitSlot />
                <p>“{paul.intakeQuote}”</p>
              </div>
              <ContactOptions />
            </div>
          }
        />
      </>
    </section>
  );
}

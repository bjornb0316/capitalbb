import type { Metadata } from "next";
import { IntakeV2 } from "@/components/forms/IntakeV2";
import { ContactOptions } from "@/components/contact/ContactOptions";

export const metadata: Metadata = { title: "Kennismaken" };

export default function Page() {
  return (
    <div className="v2-intake-page">
      <div className="container">
        <>
          <IntakeV2 />
        </>
        <div style={{ maxWidth: 720, marginTop: "4rem" }}>
          <ContactOptions title="Liever direct contact met de adviseur?" />
        </div>
      </div>
    </div>
  );
}

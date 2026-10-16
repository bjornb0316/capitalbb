import { Header } from "@/components/navigation/Header";
import { Footer } from "@/components/navigation/Footer";
import { ContactBar } from "@/components/contact/ContactBar";
import { DemoBadge } from "@/components/demo/DemoBadge";
import { sansV1 } from "@/app/fonts";
import "@/styles/v1.css";

const base = "/variant-2";

export default function V1Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className={`theme-v1 ${sansV1.variable}`}>
      <Header base={base} />
      <main id="inhoud">{children}</main>
      <Footer base={base} />
      <ContactBar base={base} />
      <DemoBadge other={{ href: "/variant-3", label: "Naar variant 3" }} />
    </div>
  );
}

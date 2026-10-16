import { Header } from "@/components/navigation/Header";
import { Footer } from "@/components/navigation/Footer";
import { ContactBar } from "@/components/contact/ContactBar";
import { DemoBadge } from "@/components/demo/DemoBadge";
import { mono, sansV2 } from "@/app/fonts";
import "@/styles/v2.css";

const base = "/variant-3";

export default function V2Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className={`theme-v2 ${sansV2.variable} ${mono.variable}`}>
      <Header base={base} />
      <main id="inhoud">{children}</main>
      <Footer base={base} />
      <ContactBar base={base} />
      <DemoBadge other={{ href: "/variant-2", label: "Naar variant 2" }} />
    </div>
  );
}

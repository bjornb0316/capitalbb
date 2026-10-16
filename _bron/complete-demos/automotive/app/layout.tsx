import SiteFooter from "../components/SiteFooter";
import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {robots:{index:false,follow:false},title:"Het autobedrijf | Automotive Experience — Concept",description:"Onafhankelijk websiteconcept voor Autobedrijf het autobedrijf, gemaakt door Capital BB."};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="nl"><body><div className="concept">ONOFFICIEEL CONCEPT · CAPITAL BB · GEEN OFFICIËLE WEBSITE</div>{children}<SiteFooter/></body></html>}
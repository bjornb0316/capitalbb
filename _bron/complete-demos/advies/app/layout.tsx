import type { Metadata, Viewport } from "next";
import { Newsreader } from "next/font/google";
import { DemoProvider } from "@/components/demo/DemoContext";
import "./globals.css";
import "@/styles/revision.css";

// Newsreader: redactionele serif met optische maten (display licht, tekst stevig).
const serif = Newsreader({
  subsets: ["latin"],
  variable: "--font-serif",
  axes: ["opsz"],
  style: ["normal", "italic"],
  display: "swap",
});

export const metadata: Metadata = {
  title: { default: "Conceptdemo · Onafhankelijk adviseur", template: "%s · Onafhankelijk adviseur (conceptdemo)" },
  description: "Conceptdemo's voor Onafhankelijk financieel advies. Niet publiek.",
  robots: { index: false, follow: false, nocache: true, googleBot: { index: false, follow: false } },
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  viewportFit: "cover",
  themeColor: "#F2EEE7",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="nl" className={serif.variable}>
      <body>
        <DemoProvider>{children}</DemoProvider>
      </body>
    </html>
  );
}

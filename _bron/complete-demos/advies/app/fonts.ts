import { Geist, Geist_Mono, Instrument_Sans } from "next/font/google";

// Per variant geladen, zodat een pagina alleen de letters ophaalt die hij gebruikt.
export const sansV1 = Instrument_Sans({ subsets: ["latin"], variable: "--font-sans-v1", display: "swap" });
export const sansV2 = Geist({ subsets: ["latin"], variable: "--font-sans-v2", display: "swap" });
export const mono = Geist_Mono({ subsets: ["latin"], variable: "--font-mono", display: "swap", preload: false });

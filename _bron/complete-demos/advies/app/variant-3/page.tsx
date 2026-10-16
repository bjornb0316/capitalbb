import type { Metadata } from "next";
import { SpatialHero } from "@/components/variant-2/SpatialHero";

import { ShapesScene } from "@/components/variant-2/ShapesScene";
import { AdvisorAnchor } from "@/components/variant-2/AdvisorAnchor";
import { ProcessChapters } from "@/components/variant-2/ProcessChapters";
import { Closing, Expect, FaqBlock } from "@/components/variant-2/Closing";

export const metadata: Metadata = { title: "Wat wil jij mogelijk maken?" };

export default function V2Home() {
  return (
    <>
      <SpatialHero />

      <ShapesScene />
      <AdvisorAnchor />
      <ProcessChapters />
      <Expect />
      <FaqBlock />
      <Closing />
    </>
  );
}


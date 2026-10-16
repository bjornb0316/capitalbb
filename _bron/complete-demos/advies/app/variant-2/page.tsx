import type { Metadata } from "next";
import { HeroFilm } from "@/components/variant-1/HeroFilm";
import { QuestionsScene } from "@/components/variant-1/QuestionsScene";
import { AdvisorScene } from "@/components/variant-1/AdvisorScene";
import { ProcessJourney } from "@/components/variant-1/ProcessJourney";
import { Expectations } from "@/components/variant-1/Expectations";
import { FaqSection } from "@/components/variant-1/FaqSection";
import { Invite } from "@/components/variant-1/Invite";

export const metadata: Metadata = { title: "Kan niet, ken ik niet" };

export default function V1Home() {
  return (
    <>
      <HeroFilm />
      <QuestionsScene />
      <AdvisorScene />
      <ProcessJourney />
      <Expectations />
      <FaqSection />
      <Invite />
    </>
  );
}

"use client";

import Link from "next/link";
import { useState } from "react";
import { type SituationId, situationById } from "@/content/situations";
import Image from "next/image";
import { SituationCards } from "./SituationCards";
import { Arrow } from "@/components/contact/icons";

/** Scène V2-02: kies jouw situatie. Selectie verandert het woningmodel. */
export function SituationPicker() {
  const [value, setValue] = useState<SituationId | "">("");
  const [preview, setPreview] = useState<SituationId | null>(null);
  const chosen = situationById(value);
  const caption = situationById(value || preview);

  return (
    <section className="v2-pick section" id="jouw-route" aria-labelledby="v2-pick-title">
      <div className="container v2-pick__grid">
        <div className="v2-pick__left">
          <h2 id="v2-pick-title" className="h2">
            Kies jouw situatie
          </h2>
          <p className="lead">Kies wat het best past. Je kunt je keuze altijd nog aanpassen.</p>
          <SituationCards
            name="home-situatie"
            value={value}
            onChange={setValue}
            onPreview={setPreview}
            legend={<span className="sr-only">Welke situatie past het best bij jou?</span>}
          />
          <div className="v2-pick__next" data-visible={!!chosen} aria-live="polite">
            {chosen && (
              <>
                <p>
                  Gekozen: <strong>{chosen.cardTitle}</strong>
                </p>
                <Link href={`/variant-3/kennismaken?situatie=${chosen.id}`} className="btn btn--primary">
                  Ga verder met deze situatie <Arrow />
                </Link>
              </>
            )}
          </div>
        </div>
        <div className="v2-pick__stage only-desktop" aria-hidden="true">
          <div className="v2-pick__panel">
            <Image src="/demos/advies/assets/paul/v2-house-interior.webp" alt="Een warme woonkamer met ruimte voor nieuwe woonplannen" width={1672} height={941} sizes="50vw" className="v2-pick__life-image" />
            <div className="v2-pick__life-note" key={caption?.id || 'intro'}>
              <p className="v2-kicker">{caption ? caption.cardTitle : 'Jouw volgende hoofdstuk'}</p>
              <p className="v2-pick__caption">{caption ? caption.houseCaption : "Wat wil jij mogelijk maken?"}</p>
              <p>{caption ? caption.answer : 'Een woonwens begint bij jouw verhaal. Kies links wat er op dit moment bij je speelt.'}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

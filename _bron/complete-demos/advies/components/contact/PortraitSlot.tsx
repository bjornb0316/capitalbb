import { paul } from "@/content/paul";
import { EditorialNote } from "@/components/demo/DemoContext";

/** Echte foto van de adviseur zodra aangeleverd; tot die tijd een verzorgd, eerlijk vlak. */
export function PortraitSlot({
  className = "",
  sizes = "(min-width: 1024px) 40vw, 90vw",
}: {
  className?: string;
  sizes?: string;
}) {
  const p = paul.portrait;
  return (
    <figure className={`portrait-slot ${className}`}>
      {p ? (
        // eslint-disable-next-line @next/next/no-img-element
        <img src={p.src} alt={p.alt} sizes={sizes} />
      ) : (
        <>
          {/* Lege kadrering in plaats van een nepportret: silhouet van een kader en een eerlijke regel. */}
          <span className="portrait-slot__mono" aria-hidden="true">
            <svg viewBox="0 0 100 120" fill="none" stroke="currentColor" strokeWidth="0.8">
              <circle cx="50" cy="42" r="19" />
              <path d="M14 118c4-26 18-40 36-40s32 14 36 40" />
            </svg>
          </span>
          <figcaption className="portrait-slot__label">
            <span>Portret van de adviseur</span>
            <span>Volgt</span>
          </figcaption>
        </>
      )}
    </figure>
  );
}

export function PortraitNote() {
  return <EditorialNote>Geanonimiseerd websiteconcept van Capital BB.</EditorialNote>;
}

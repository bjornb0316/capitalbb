import Image from "next/image";
import type { Asset } from "@/content/assets";

type Kind = "exterior" | "entrance" | "interior" | "workspace" | "question";

/** Toont het goedgekeurde beeld of, zolang dat ontbreekt, een filmisch sfeerbeeld. */
export function SceneImage({
  asset,
  kind,
  mobile = false,
  className,
  priority = false,
  sizes = "100vw",
  idp: _idp,
}: {
  asset: Asset;
  kind: Kind;
  mobile?: boolean;
  className?: string;
  priority?: boolean;
  sizes?: string;
  idp?: string;
}) {
  if (asset)
    return (
      <Image
        className={className}
        src={asset.src}
        width={asset.width}
        height={asset.height}
        alt={asset.alt}
        priority={priority}
        sizes={sizes}
      />
    );
  // Sfeerbeeld (gerenderd uit components/house/Atmosphere.tsx via scripts/render-atmos.mjs)
  const name = kind === "interior" ? "interior" : kind === "workspace" ? "workspace" : "street";
  return (
    <>
      <Image
        className={className}
        src={`/demos/advies/assets/atmos/${name}.webp`}
        width={2400}
        height={1500}
        alt=""
        priority={priority}
        sizes={sizes}
        style={mobile ? { objectPosition: "68% 50%" } : undefined}
      />
      <span className={`${className ?? ""} atmos-grain`} aria-hidden="true" />
    </>
  );
}

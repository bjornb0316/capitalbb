import { useId } from "react";

/**
 * Sfeerbeelden voor variant 1 zolang er geen goedgekeurde fotografie is.
 * Bewust geen illustratie van een "huisje", maar filmisch licht:
 * - street: een rij Nederlandse woningen als silhouet tegen de avondlucht, verlichte ramen.
 * - interior: avondlicht dat door een raam op een gestucte wand valt.
 * - workspace: koeler ochtendlicht op een wand met de rand van een werktafel.
 * Korrel en vignet maken het beeld fotografisch in plaats van vlak.
 */

type Kind = "street" | "interior" | "workspace";

// Rij woningen: x, breedte, gootlijn, nok, type dak
const HOUSES: [number, number, number, number, "gable" | "step" | "flat"][] = [
  [560, 150, 610, 520, "gable"],
  [710, 170, 600, 500, "step"],
  [880, 160, 615, 525, "gable"],
  [1040, 190, 590, 480, "gable"],
  [1230, 150, 620, 540, "flat"],
  [1380, 180, 600, 505, "step"],
  [1560, 170, 612, 520, "gable"],
];

function roof(x: number, w: number, eave: number, peak: number, type: string) {
  const cx = x + w / 2;
  if (type === "gable") return `L${x} ${eave} L${cx} ${peak} L${x + w} ${eave}`;
  if (type === "flat") return `L${x} ${peak + 30} L${x + w} ${peak + 30}`;
  // trapgevel
  const s = w / 7;
  const h = (eave - peak) / 3;
  return [
    `L${x} ${eave}`,
    `L${x + s} ${eave}`,
    `L${x + s} ${eave - h}`,
    `L${x + 2 * s} ${eave - h}`,
    `L${x + 2 * s} ${eave - 2 * h}`,
    `L${x + 3 * s} ${eave - 2 * h}`,
    `L${x + 3 * s} ${peak}`,
    `L${x + 4 * s} ${peak}`,
    `L${x + 4 * s} ${eave - 2 * h}`,
    `L${x + 5 * s} ${eave - 2 * h}`,
    `L${x + 5 * s} ${eave - h}`,
    `L${x + 6 * s} ${eave - h}`,
    `L${x + 6 * s} ${eave}`,
    `L${x + w} ${eave}`,
  ].join(" ");
}

// Deterministisch "willekeurig" welke ramen branden.
const lit = (i: number, j: number) => (i * 7 + j * 3) % 5 === 0 || (i + j) % 7 === 3;

function Street({ id }: { id: string }) {
  const path = `M520 1000 ${HOUSES.map(([x, w, e, p, t]) => roof(x, w, e, p, t)).join(" ")} L1760 1000 Z`;
  const windows: { x: number; y: number; w: number; h: number; on: boolean; key: string }[] = [];
  HOUSES.forEach(([x, w, eave], i) => {
    const cols = w > 165 ? 3 : 2;
    const gap = w / (cols + 1);
    for (let r = 0; r < 3; r++) {
      for (let c = 0; c < cols; c++) {
        const ww = 26;
        const wh = r === 2 ? 64 : 48;
        windows.push({
          x: x + gap * (c + 1) - ww / 2,
          y: eave + 30 + r * 92,
          w: ww,
          h: wh,
          on: lit(i, r * 3 + c),
          key: `${i}-${r}-${c}`,
        });
      }
    }
  });
  return (
    <>
      <defs>
        <linearGradient id={`${id}sky`} x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stopColor="#0a131b" />
          <stop offset="0.38" stopColor="#1a2834" />
          <stop offset="0.6" stopColor="#3d4148" />
          <stop offset="0.74" stopColor="#7a5f4f" />
          <stop offset="0.86" stopColor="#b98256" />
          <stop offset="1" stopColor="#d79a62" />
        </linearGradient>
        <radialGradient id={`${id}sun`} cx="0.72" cy="0.72" r="0.45">
          <stop offset="0" stopColor="#f0b277" stopOpacity="0.55" />
          <stop offset="1" stopColor="#f0b277" stopOpacity="0" />
        </radialGradient>
        <filter id={`${id}glow`} x="-50%" y="-50%" width="200%" height="200%">
          <feGaussianBlur stdDeviation="16" />
        </filter>
        <filter id={`${id}soft`} x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="6" />
        </filter>
        <filter id={`${id}far`}>
          <feGaussianBlur stdDeviation="10" />
        </filter>
      </defs>
      <rect width="1600" height="1000" fill={`url(#${id}sky)`} />
      <rect width="1600" height="1000" fill={`url(#${id}sun)`} />
      {/* Verre bebouwing en bomen, onscherp */}
      <path
        d="M0 760 C120 700 220 720 300 690 C380 660 430 700 520 680 L640 690 L700 650 L760 690 L1600 700 L1600 1000 L0 1000Z"
        fill="#2b2a2c"
        opacity="0.75"
        filter={`url(#${id}far)`}
      />
      {/* Boom links, dichterbij en zacht */}
      <g filter={`url(#${id}soft)`} fill="#0d1216">
        <path d="M120 1000 L150 760 L170 760 L200 1000Z" />
        <ellipse cx="160" cy="610" rx="190" ry="210" />
        <ellipse cx="300" cy="700" rx="140" ry="150" />
        <ellipse cx="40" cy="720" rx="150" ry="170" />
      </g>
      {/* Rij woningen */}
      <g transform="translate(-160 0)">
        <path d={path} fill="#0b1014" filter={`url(#${id}soft)`} />
        {windows.map((w) =>
          w.on ? (
            <g key={w.key}>
              <rect x={w.x - 18} y={w.y - 18} width={w.w + 36} height={w.h + 36} fill="#f0a65c" opacity="0.42" filter={`url(#${id}glow)`} />
              <rect x={w.x} y={w.y} width={w.w} height={w.h} fill="#f7c888" opacity="0.85" filter={`url(#${id}soft)`} />
            </g>
          ) : (
            <rect key={w.key} x={w.x} y={w.y} width={w.w} height={w.h} fill="#1b2329" filter={`url(#${id}soft)`} />
          ),
        )}
      </g>
      {/* Straat en voorgrond */}
      <rect y="925" width="1600" height="75" fill="#07090b" opacity="0.55" filter={`url(#${id}soft)`} />
    </>
  );
}

function Light({ id, cool }: { id: string; cool?: boolean }) {
  const wallA = cool ? "#c9c6bf" : "#d8c3a6";
  const wallB = cool ? "#8e8b85" : "#9b7f62";
  const sun = cool ? "#fff6e6" : "#ffd9a3";
  // Raamvlakken als lichtval, schuin geprojecteerd
  const panes = [
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1],
  ];
  return (
    <>
      <defs>
        <linearGradient id={`${id}wall`} x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor={wallA} />
          <stop offset="1" stopColor={wallB} />
        </linearGradient>
        <radialGradient id={`${id}fall`} cx="0.62" cy="0.45" r="0.6">
          <stop offset="0" stopColor={sun} stopOpacity="0.35" />
          <stop offset="1" stopColor={sun} stopOpacity="0" />
        </radialGradient>
        <filter id={`${id}blur`}>
          <feGaussianBlur stdDeviation="10" />
        </filter>
        <filter id={`${id}leaf`}>
          <feGaussianBlur stdDeviation="16" />
        </filter>
      </defs>
      <rect width="1600" height="1000" fill={`url(#${id}wall)`} />
      <rect width="1600" height="1000" fill={`url(#${id}fall)`} />
      <g transform="translate(700 150) skewX(-24) skewY(6)" filter={`url(#${id}blur)`}>
        {panes.map(([c, r]) => (
          <rect key={`${c}${r}`} x={c * 250} y={r * 310} width="226" height="286" fill={sun} opacity="0.78" />
        ))}
      </g>
      {/* Schaduw van blad over de lichtval */}
      <g filter={`url(#${id}leaf)`} fill={cool ? "#77736c" : "#7a5e43"} opacity="0.55">
        <ellipse cx="1060" cy="260" rx="90" ry="40" transform="rotate(-30 1060 260)" />
        <ellipse cx="1150" cy="330" rx="70" ry="30" transform="rotate(20 1150 330)" />
        <ellipse cx="980" cy="380" rx="60" ry="26" transform="rotate(-50 980 380)" />
      </g>
      {/* Vloer of tafelrand */}
      {cool ? (
        <>
          <rect y="760" width="1600" height="240" fill="#2a2724" />
          <rect y="760" width="1600" height="6" fill="#4a4540" />
        </>
      ) : (
        <rect y="870" width="1600" height="130" fill="#5a4330" opacity="0.85" />
      )}
    </>
  );
}

export function Atmosphere({ kind, className, idp }: { kind: Kind; className?: string; idp?: string }) {
  const uid = (idp ?? "") + useId().replace(/[^a-zA-Z0-9]/g, "");
  return (
    <svg
      className={`atmos ${className ?? ""}`}
      viewBox="0 0 1600 1000"
      preserveAspectRatio="xMidYMid slice"
      aria-hidden="true"
      focusable="false"
    >
      <defs>
        <pattern id={`${uid}grain`} width="160" height="160" patternUnits="userSpaceOnUse">
          <image href="/demos/advies/assets/grain.png" width="160" height="160" />
        </pattern>
        <radialGradient id={`${uid}vig`} cx="0.5" cy="0.5" r="0.75">
          <stop offset="0.55" stopColor="#000" stopOpacity="0" />
          <stop offset="1" stopColor="#000" stopOpacity="0.55" />
        </radialGradient>
      </defs>
      {kind === "street" ? <Street id={uid} /> : <Light id={uid} cool={kind === "workspace"} />}
      <rect width="1600" height="1000" fill={`url(#${uid}vig)`} />
      <rect width="1600" height="1000" fill={`url(#${uid}grain)`} opacity="0.32" style={{ mixBlendMode: "overlay" }} />
    </svg>
  );
}

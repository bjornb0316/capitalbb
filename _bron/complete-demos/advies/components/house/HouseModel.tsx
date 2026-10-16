"use client";

import { createContext, useContext, useEffect, useId, useRef, type CSSProperties } from "react";
import { motion as cfg } from "@/components/motion/config";
import "@/styles/house.css";
import { PhotographicHouse, type PhotographicHouseProps } from './PhotographicHouse';

export function HouseModel(props: PhotographicHouseProps) { return <PhotographicHouse {...props} />; }

/**
 * Variant 2: woning als ruimtelijke compositie in isometrische SVG.
 * Lagen: grondvlak, omgeving, hoofdvolume, dak, ramen, entree,
 * werkruimte (ondernemer) en extra woonruimte (overwaarde).
 * Toestanden zijn visuele metaforen, geen voorspellingen.
 */

export type HouseState = "idle" | "kopen" | "ondernemer" | "overwaarde" | "complex" | "done";

type V3 = [number, number, number];
const S = 34;
const OX = 400;
const OY = 220;
const C = Math.cos(Math.PI / 6) * S;
const P = ([x, y, z]: V3) => `${(OX + (x - y) * C).toFixed(1)},${(OY + (x + y) * (S / 2) - z * S).toFixed(1)}`;
const poly = (...pts: V3[]) => pts.map(P).join(" ");
const pt = (v: V3) => P(v).split(",").map(Number) as [number, number];

/** Rechthoek op het voorvlak y = c. */
const onY = (y: number, x1: number, x2: number, z1: number, z2: number) =>
  poly([x1, y, z1], [x2, y, z1], [x2, y, z2], [x1, y, z2]);
/** Rechthoek op het zijvlak x = c. */
const onX = (x: number, y1: number, y2: number, z1: number, z2: number) =>
  poly([x, y1, z1], [x, y2, z1], [x, y2, z2], [x, y1, z2]);
const top = (z: number, x1: number, x2: number, y1: number, y2: number) =>
  poly([x1, y1, z], [x2, y1, z], [x2, y2, z], [x1, y2, z]);

// Unieke id's per instantie: meerdere modellen op één pagina, sommige verborgen.
const Ids = createContext({ glass: "", warm: "", soft: "" });

function Window({
  face,
  a,
  b,
  z1,
  z2,
  c,
  mullion = true,
  cls = "",
}: {
  face: "y" | "x";
  a: number;
  b: number;
  z1: number;
  z2: number;
  c: number;
  mullion?: boolean;
  cls?: string;
}) {
  const ids = useContext(Ids);
  const r = face === "y" ? onY(c, a, b, z1, z2) : onX(c, a, b, z1, z2);
  const mid = (a + b) / 2;
  const m1 = face === "y" ? pt([mid, c, z1]) : pt([c, mid, z1]);
  const m2 = face === "y" ? pt([mid, c, z2]) : pt([c, mid, z2]);
  return (
    <g className={`hm-window ${cls}`}>
      <polygon points={r} className="hm-glass" fill={`url(#${ids.glass})`} />
      <polygon points={r} className="hm-glow" fill={`url(#${ids.warm})`} />
      {mullion && <line x1={m1[0]} y1={m1[1]} x2={m2[0]} y2={m2[1]} className="hm-mullion" />}
      <polygon points={r} className="hm-frame" />
    </g>
  );
}

function Tree({ at, h = 2.2, r = 30, cls = "" }: { at: V3; h?: number; r?: number; cls?: string }) {
  const [bx, by] = pt(at);
  const [cx, cy] = pt([at[0], at[1], h]);
  return (
    <g className={`hm-tree ${cls}`}>
      <ellipse cx={bx} cy={by} rx={r * 0.8} ry={r * 0.32} className="hm-shadow" />
      <line x1={bx} y1={by} x2={cx} y2={cy + r * 0.4} className="hm-trunk" />
      <circle cx={cx} cy={cy} r={r} className="hm-canopy" />
      <circle cx={cx - r * 0.3} cy={cy - r * 0.3} r={r * 0.55} className="hm-canopy-hi" />
    </g>
  );
}

function VectorHouseModel({
  state = "idle",
  preview = null,
  intro = true,
  tilt = true,
  className = "",
  build,
  label = "Illustratie van een woning die verandert met de gekozen situatie",
}: {
  build?: 1 | 2 | 3;
  state?: HouseState;
  preview?: HouseState | null;
  intro?: boolean;
  tilt?: boolean;
  className?: string;
  label?: string;
}) {
  const wrap = useRef<HTMLDivElement>(null);
  const uid = useId().replace(/[^a-zA-Z0-9]/g, "");
  const ids = { glass: `${uid}g`, warm: `${uid}w`, soft: `${uid}s` };
  const shown = preview && state === "idle" ? preview : state;

  // Kleine pointerreactie op desktop (max. enkele graden). Geen reactie op touch.
  useEffect(() => {
    const el = wrap.current;
    if (!el || !tilt) return;
    const ok = window.matchMedia(`${cfg.mq.finePointer} and ${cfg.mq.motionOk}`);
    if (!ok.matches) return;
    let raf = 0;
    const max = cfg.pointer.maxTiltDeg;
    const onMove = (e: PointerEvent) => {
      const r = el.getBoundingClientRect();
      const nx = (e.clientX - (r.left + r.width / 2)) / (window.innerWidth / 2);
      const ny = (e.clientY - (r.top + r.height / 2)) / (window.innerHeight / 2);
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        el.style.setProperty("--ry", `${Math.max(-1, Math.min(1, nx)) * max}deg`);
        el.style.setProperty("--rx", `${Math.max(-1, Math.min(1, -ny)) * max * 0.6}deg`);
      });
    };
    const reset = () => {
      el.style.setProperty("--ry", "0deg");
      el.style.setProperty("--rx", "0deg");
    };
    window.addEventListener("pointermove", onMove, { passive: true });
    document.addEventListener("pointerleave", reset);
    return () => {
      cancelAnimationFrame(raf);
      window.removeEventListener("pointermove", onMove);
      document.removeEventListener("pointerleave", reset);
    };
  }, [tilt]);

  return (
    <div
      ref={wrap}
      className={`hm ${intro ? "hm--intro" : ""} ${className}`}
      data-state={shown}
      data-preview={preview && state === "idle" ? "true" : undefined}
      data-build={build}
      style={{ "--rx": "0deg", "--ry": "0deg" } as CSSProperties}
    >
      <Ids.Provider value={ids}>
        <svg viewBox="0 0 800 560" role="img" aria-label={label} className="hm__svg">
          <defs>
            <filter id={ids.soft} x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="14" />
            </filter>
            <linearGradient id={ids.glass} x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stopColor="#EEF4F1" />
              <stop offset="1" stopColor="#B9CCC6" />
            </linearGradient>
            <linearGradient id={ids.warm} x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stopColor="#FFE9B8" />
              <stop offset="1" stopColor="#F2C77D" />
            </linearGradient>
          </defs>

          {/* Grondvlak */}
          <g className="hm-layer hm-ground">
            <polygon
              points={top(0, -4.4, 10.6, -1.8, 7.8)}
              className="hm-ground-shadow"
              filter={`url(#${ids.soft})`}
              transform="translate(0 18)"
            />
            <polygon
              points={poly([-4.4, 7.8, 0], [10.6, 7.8, 0], [10.6, 7.8, -0.45], [-4.4, 7.8, -0.45])}
              className="hm-slab-front"
            />
            <polygon
              points={poly([10.6, -1.8, 0], [10.6, 7.8, 0], [10.6, 7.8, -0.45], [10.6, -1.8, -0.45])}
              className="hm-slab-side"
            />
            <polygon points={top(0, -4.4, 10.6, -1.8, 7.8)} className="hm-slab-top" />
            <polygon points={top(0.01, 3.55, 4.85, 4.2, 7.8)} className="hm-path" />
          </g>

          {/* Omgeving achter */}
          <g className="hm-layer hm-env hm-env--back">
            <Tree at={[9.2, -0.6, 0]} h={2.9} r={34} />
            <Tree at={[-3.4, 2.6, 0]} h={2.4} r={28} />
          </g>

          {/* Extra woonruimte (overwaarde): verschijnt als wens */}
          <g className="hm-layer hm-extension">
            <polygon points={onY(4, -3, 0, 0, 2.4)} className="hm-ext-glass" />
            <polygon points={top(2.4, -3, 0, 1.6, 4)} className="hm-ext-top" />
            <polygon points={onX(-3, 1.6, 4, 0, 2.4)} className="hm-ext-side" />
            <line {...lineProps([-1.5, 4, 0], [-1.5, 4, 2.4])} className="hm-ext-line" />
            <polygon points={onY(4, -3, 0, 0, 2.4)} className="hm-ext-outline" />
            <polygon points={top(2.4, -3, 0, 1.6, 4)} className="hm-ext-outline" />
          </g>

          {/* Hoofdvolume */}
          <g className="hm-layer hm-volume">
            <g className="hm-part hm-part--right">
              <polygon
                points={poly([6, 0, 0], [6, 4, 0], [6, 4, 4], [6, 2, 6.45], [6, 0, 4])}
                className="hm-wall-side"
              />
              <Window face="x" c={6} a={1.4} b={2.6} z1={4.3} z2={5.4} mullion={false} cls="hm-w-gable" />
              <Window face="x" c={6} a={0.8} b={2.4} z1={0.7} z2={1.95} />
            </g>
            <g className="hm-part hm-part--front">
              <polygon points={onY(4, 0, 6, 0, 4)} className="hm-wall-front" />
              <polygon points={onY(4, 0, 6, 0, 4)} className="hm-wall-light" fill={`url(#${ids.warm})`} />
              <Window face="y" c={4} a={0.6} b={2.6} z1={0.45} z2={1.95} cls="hm-w-living" />
              <Window face="y" c={4} a={0.8} b={2.2} z1={2.5} z2={3.45} />
              <Window face="y" c={4} a={3.8} b={5.2} z1={2.5} z2={3.45} />
            </g>
            {/* Entree */}
            <g className="hm-part hm-entrance">
              <polygon points={onY(4, 3.55, 4.4, 0, 2.05)} className="hm-door" />
              <Window face="y" c={4} a={4.5} b={4.85} z1={0} z2={2.05} mullion={false} cls="hm-w-side" />
              <polygon points={top(2.25, 3.35, 5.05, 4, 4.75)} className="hm-canopy-top" />
              <polygon points={onY(4.75, 3.35, 5.05, 2.12, 2.25)} className="hm-canopy-front" />
              <circle cx={pt([4.3, 4, 1.05])[0]} cy={pt([4.3, 4, 1.05])[1]} r="2.2" className="hm-handle" />
            </g>
          </g>

          {/* Dak */}
          <g className="hm-layer hm-roof">
            <polygon
              points={poly(
                [6.3, 2, 6.45],
                [6.3, -0.4, 3.75],
                [6.3, -0.4, 3.55],
                [6.3, 2, 6.22],
                [6.3, 4.4, 3.55],
                [6.3, 4.4, 3.75],
              )}
              className="hm-roof-edge"
            />
            <polygon
              points={poly([-0.3, 4.4, 3.75], [6.3, 4.4, 3.75], [6.3, 2, 6.45], [-0.3, 2, 6.45])}
              className="hm-roof-slope"
            />
            <polygon
              points={poly([-0.3, 4.4, 3.75], [6.3, 4.4, 3.75], [6.3, 4.4, 3.55], [-0.3, 4.4, 3.55])}
              className="hm-roof-fascia"
            />
            <line {...lineProps([-0.3, 2, 6.45], [6.3, 2, 6.45])} className="hm-roof-ridge" />
            {[1.2, 2.6, 4, 5.4].map((x) => (
              <line key={x} {...lineProps([x, 4.3, 3.85], [x, 2.15, 6.3])} className="hm-roof-seam" />
            ))}
          </g>

          {/* Werkruimte (ondernemer) */}
          <g className="hm-layer hm-workspace">
            <polygon points={onX(8.8, 1.2, 4, 0, 2.6)} className="hm-ws-side" />
            <polygon points={onY(4, 6, 8.8, 0, 2.6)} className="hm-ws-front" />
            <polygon points={top(2.6, 5.9, 8.95, 1.05, 4.15)} className="hm-ws-top" />
            <Window face="y" c={4} a={6.45} b={8.4} z1={0.5} z2={2.15} cls="hm-w-desk" />
            <Window face="x" c={8.8} a={1.8} b={3.3} z1={0.9} z2={2.0} mullion={false} />
          </g>

          {/* Omgeving voor */}
          <g className="hm-layer hm-env hm-env--front">
            <Tree at={[-2.6, 6.4, 0]} h={2.1} r={30} />
            <rect {...hedge([0.3, 5.1, 0], 92)} className="hm-hedge" />
            <rect {...hedge([5.6, 5.1, 0], 74)} className="hm-hedge" />
            <Tree at={[9.6, 6.6, 0]} h={1.5} r={20} cls="hm-tree--small" />
          </g>

          {/* Losse delen die samenkomen (complexe situatie) */}
          <g className="hm-layer hm-pieces" aria-hidden="true">
            {[
              [[-3.4, 6.8, 3.2], 0],
              [[9.8, 2.4, 4.4], 1],
              [[2.2, 7.6, 4.8], 2],
            ].map(([p, i]) => {
              const [x, y] = pt(p as V3);
              return (
                <rect
                  key={i as number}
                  x={x - 9}
                  y={y - 9}
                  width="18"
                  height="18"
                  rx="4"
                  className={`hm-piece hm-piece--${i}`}
                />
              );
            })}
          </g>

          {/* Afronding: rustige lichtring */}
          <g className="hm-layer hm-done" aria-hidden="true">
            <ellipse cx={pt([3, 2, 0])[0]} cy={pt([3, 2, 0])[1]} rx="330" ry="150" className="hm-halo" />
          </g>
        </svg>
      </Ids.Provider>
    </div>
  );
}

function lineProps(a: V3, b: V3) {
  const [x1, y1] = pt(a);
  const [x2, y2] = pt(b);
  return { x1, y1, x2, y2 };
}
function hedge(at: V3, w: number) {
  const [x, y] = pt(at);
  return { x: x - w / 2, y: y - 22, width: w, height: 30, rx: 15 };
}

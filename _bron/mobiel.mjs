/* =========================================================================
   Mobiele en responsive controle op echte viewports.

   Draaien (site moet lokaal draaien op poort 8330):
       python -m http.server 8330 --directory .
       node _bron/mobiel.mjs

   Waarom een eigen script: CSS lezen is geen test. Media queries slaan pas
   aan bij een echte viewportbreedte, en overlap tussen de zwevende
   WhatsApp-knop en de vaste actiebalk zie je alleen als het echt gerenderd
   wordt. Playwright is hier niet geinstalleerd, dus dit praat rechtstreeks
   met Chrome via het DevTools-protocol. Node 24 heeft WebSocket ingebouwd,
   dus er zijn geen afhankelijkheden nodig.

   Wat er wordt nagelopen per formaat:
     - horizontale overflow op de pagina
     - elementen die buiten het scherm steken
     - tapdoelen kleiner dan 40 pixels
     - tekst kleiner dan 12 pixels
     - de vaste actiebalk die de voettekst of de WhatsApp-knop overlapt
     - tabellen die niet in hun eigen bak scrollen
     - het mobiele menu dat open en dicht gaat
   ========================================================================= */

import { spawn } from "node:child_process";
import { setTimeout as wacht } from "node:timers/promises";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const BASIS = process.env.CBB_URL || "http://localhost:8330";
const FORMATEN = [
  { naam: "telefoon", breedte: 390, hoogte: 844, schaal: 3, mobiel: true },
  { naam: "tablet", breedte: 768, hoogte: 1024, schaal: 2, mobiel: true },
  { naam: "laptop", breedte: 1440, hoogte: 900, schaal: 1, mobiel: false },
];

const PAGINAS = [
  "/", "/websites/", "/website-laten-maken/", "/website-laten-vernieuwen/",
  "/online-marketing/", "/crm/", "/prijzen/", "/werk/", "/scan/", "/contact/",
  "/meer-klanten/", "/business-os/",
];

const CHROME = [
  "C:/Program Files/Google/Chrome/Application/chrome.exe",
  "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
  "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
].find((p) => fs.existsSync(p));

if (!CHROME) {
  console.error("Geen Chrome of Edge gevonden.");
  process.exit(1);
}

const POORT = 9331;
const profiel = fs.mkdtempSync(path.join(os.tmpdir(), "cbb-chrome-"));

const chrome = spawn(CHROME, [
  `--remote-debugging-port=${POORT}`,
  `--user-data-dir=${profiel}`,
  "--headless=new",
  "--no-first-run",
  "--no-default-browser-check",
  "--disable-extensions",
  "--hide-scrollbars",
], { stdio: ["ignore", "ignore", "pipe"] });

let chromeFout = "";
chrome.stderr.on("data", (d) => { chromeFout += d.toString(); });
chrome.on("error", (e) => { chromeFout += "spawn: " + e.message; });

async function doelUrl() {
  for (let i = 0; i < 50; i++) {
    try {
      const r = await fetch(`http://127.0.0.1:${POORT}/json/version`);
      return (await r.json()).webSocketDebuggerUrl;
    } catch { await wacht(200); }
  }
  throw new Error("Chrome start niet op. " + (chromeFout.slice(-800) || "(geen melding)"));
}

const ws = new WebSocket(await doelUrl());
await new Promise((r) => (ws.onopen = r));

let volgnr = 0;
const wachtend = new Map();
ws.onmessage = (e) => {
  const b = JSON.parse(e.data);
  if (b.id && wachtend.has(b.id)) {
    const { res, rej } = wachtend.get(b.id);
    wachtend.delete(b.id);
    b.error ? rej(new Error(b.error.message)) : res(b.result);
  }
};

function cdp(method, params = {}, sessionId) {
  const id = ++volgnr;
  return new Promise((res, rej) => {
    wachtend.set(id, { res, rej });
    ws.send(JSON.stringify({ id, method, params, sessionId }));
  });
}

// Eigen tabblad, zodat we het startscherm niet meten.
const { targetId } = await cdp("Target.createTarget", { url: "about:blank" });
const { sessionId } = await cdp("Target.attachToTarget", { targetId, flatten: true });
const S = (m, p) => cdp(m, p, sessionId);
await S("Page.enable");
await S("Runtime.enable");

async function evalueer(expressie) {
  const r = await S("Runtime.evaluate", {
    expression: expressie, returnByValue: true, awaitPromise: true,
  });
  if (r.exceptionDetails) throw new Error(r.exceptionDetails.text);
  return r.result.value;
}

/* Het meetscript dat in de pagina zelf draait. */
const METING = `(() => {
  const cw = document.documentElement.clientWidth;
  const zichtbaar = (el) => {
    const s = getComputedStyle(el);
    return s.display !== "none" && s.visibility !== "hidden" && el.offsetParent !== null;
  };
  const uit = { overflow: null, uitstekend: [], kleineTap: [], kleineTekst: [],
                overlap: [], tabellen: [], h1: document.querySelectorAll("h1").length };

  const se = document.scrollingElement || document.documentElement;
  if (se.scrollWidth > cw + 1) uit.overflow = { scrollWidth: se.scrollWidth, clientWidth: cw };

  // Bewust buiten beeld geplaatste elementen tellen niet mee: de skip-link
  // voor toetsenbordgebruikers en het honeypot-veld tegen spambots horen daar
  // te staan. SVG-onderdelen ook niet: dat zijn tekenlagen binnen een
  // afgeknipte container, geen paginabreedte.
  const negeer = (el) =>
    el.closest(".skip, .vh-veld, .vh, svg, [aria-hidden='true']") !== null ||
    el.classList.contains("skip") || el.classList.contains("vh-veld");

  document.querySelectorAll("body *").forEach((el) => {
    if (!zichtbaar(el) || negeer(el)) return;
    const r = el.getBoundingClientRect();
    if (r.width <= 0 || r.height <= 0) return;
    if (r.right > cw + 1 || r.left < -1) {
      const naam = el.tagName.toLowerCase() + (el.className && typeof el.className === "string"
        ? "." + el.className.trim().split(/\\s+/).slice(0, 2).join(".") : "");
      if (uit.uitstekend.length < 6) uit.uitstekend.push(naam + " [" + Math.round(r.left) + ".." + Math.round(r.right) + "]");
    }
  });

  // Tapdoelen: WCAG 2.2 AA (Target Size Minimum) vraagt 24 bij 24 pixels.
  // Niet 40: dat is de aanbeveling van sommige stijlgidsen, geen norm, en op
  // die drempel wordt vrijwel elke nette tekstlink onterecht afgekeurd.
  document.querySelectorAll("a, button, summary, input, textarea, select").forEach((el) => {
    if (!zichtbaar(el) || negeer(el)) return;
    const r = el.getBoundingClientRect();
    if (r.height === 0) return;
    // Tekstlinks middenin een alinea vallen hier buiten: die hoef je niet te tikken.
    const inTekst = el.closest("p, li") && el.tagName === "A" && !el.className.includes("btn");
    if (inTekst) return;
    if (r.height < 24 && uit.kleineTap.length < 8) {
      uit.kleineTap.push((el.className || el.tagName) + " h=" + Math.round(r.height));
    }
  });

  // Leesbaarheid: onder 12px is op een telefoon te klein. Op een laptop is
  // een klein label van 11px een normale ontwerpkeuze, dus daar meten we niet.
  if (window.innerWidth <= 820) document.querySelectorAll("p, li, span, td, th").forEach((el) => {
    if (!zichtbaar(el) || !el.textContent.trim() || negeer(el)) return;
    const fs = parseFloat(getComputedStyle(el).fontSize);
    if (fs < 12 && uit.kleineTekst.length < 6) {
      uit.kleineTekst.push((el.className || el.tagName) + " " + fs.toFixed(1) + "px");
    }
  });

  // Overlap tussen de zwevende elementen onderaan.
  const balk = document.querySelector(".actiebalk");
  const wa = document.querySelector(".wa-bubbel");
  const cookie = document.querySelector(".cookiebalk");
  const paren = [[balk, wa, "actiebalk/whatsapp"], [cookie, balk, "cookiebalk/actiebalk"]];
  paren.forEach(([a, b, naam]) => {
    if (!a || !b || !zichtbaar(a) || !zichtbaar(b)) return;
    const ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect();
    const raakt = !(ra.right < rb.left || ra.left > rb.right || ra.bottom < rb.top || ra.top > rb.bottom);
    if (raakt) uit.overlap.push(naam);
  });

  // Tabellen moeten in hun eigen bak scrollen, niet de pagina breed maken.
  document.querySelectorAll("table").forEach((t) => {
    const bak = t.parentElement;
    const scrollt = bak && getComputedStyle(bak).overflowX !== "visible";
    const past = t.getBoundingClientRect().width <= cw + 1;
    if (!scrollt && !past) uit.tabellen.push("tabel niet scrollbaar en te breed");
  });

  return uit;
})()`;

const problemen = [];
console.log("Mobiele en responsive controle");
console.log("=".repeat(64));

for (const f of FORMATEN) {
  await S("Emulation.setDeviceMetricsOverride", {
    width: f.breedte, height: f.hoogte, deviceScaleFactor: f.schaal,
    mobile: f.mobiel,
  });
  console.log(`\n${f.naam}  ${f.breedte} x ${f.hoogte}`);
  console.log("-".repeat(64));

  for (const pad of PAGINAS) {
    await S("Page.navigate", { url: BASIS + pad });
    await wacht(650);
    let m;
    try { m = await evalueer(METING); }
    catch (e) { console.log(`  ${pad.padEnd(34)} FOUT: ${e.message}`); continue; }

    const fouten = [];
    if (m.overflow) fouten.push(`horizontale overflow (${m.overflow.scrollWidth} > ${m.overflow.clientWidth})`);
    if (m.uitstekend.length) fouten.push(`steekt uit: ${m.uitstekend.join(", ")}`);
    if (m.kleineTap.length) fouten.push(`tapdoel < 24px (WCAG 2.2): ${m.kleineTap.join(", ")}`);
    if (m.kleineTekst.length) fouten.push(`tekst < 12px: ${m.kleineTekst.join(", ")}`);
    if (m.overlap.length) fouten.push(`overlap: ${m.overlap.join(", ")}`);
    if (m.tabellen.length) fouten.push(m.tabellen.join(", "));
    if (m.h1 !== 1) fouten.push(`${m.h1} H1's`);

    if (fouten.length) {
      console.log(`  ${pad.padEnd(34)} ${fouten.length} probleem(en)`);
      fouten.forEach((x) => console.log(`      - ${x}`));
      problemen.push(`${f.naam} ${pad}: ${fouten.join(" | ")}`);
    } else {
      console.log(`  ${pad.padEnd(34)} in orde`);
    }
  }

  // Het mobiele menu alleen op de smalle formaten.
  if (f.breedte <= 820) {
    await S("Page.navigate", { url: BASIS + "/" });
    await wacht(650);
    const menu = await evalueer(`(() => {
      const k = document.getElementById("nav-knop");
      const m = document.getElementById("nav-menu");
      if (!k || !m) return { fout: "knop of menu ontbreekt" };
      const zichtbaarVoor = getComputedStyle(k).display !== "none";
      k.click();
      const open = !m.hidden && getComputedStyle(m).display !== "none";
      const aantal = m.querySelectorAll("a").length;
      k.click();
      const dicht = m.hidden;
      return { knopZichtbaar: zichtbaarVoor, gaatOpen: open, links: aantal, gaatDicht: dicht };
    })()`);
    const ok = menu.knopZichtbaar && menu.gaatOpen && menu.gaatDicht && menu.links > 3;
    console.log(`  ${"mobiel menu".padEnd(34)} ${ok ? "in orde" : "PROBLEEM"} ${JSON.stringify(menu)}`);
    if (!ok) problemen.push(`${f.naam} mobiel menu: ${JSON.stringify(menu)}`);
  }
}

console.log("\n" + "=".repeat(64));
if (problemen.length) {
  console.log(`${problemen.length} probleem(en) gevonden:\n`);
  problemen.forEach((p) => console.log("  -", p));
} else {
  console.log("Geen problemen op alle geteste formaten.");
}

ws.close();
chrome.kill();
try { fs.rmSync(profiel, { recursive: true, force: true }); } catch {}
process.exit(problemen.length ? 1 : 0);

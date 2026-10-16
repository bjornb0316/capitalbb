import * as cheerio from "cheerio";
import type { TrustooCandidate, Extracted } from "./types.js";
const clean = (s: string) => s.replace(/\s+/g, " ").trim();
const field = <T>(v: T | null | undefined): Extracted<T> =>
  v === null || v === undefined || v === "" ? { value: null, state: "NOT_LISTED" } : { value: v, state: "FOUND" };
export function normalizeDutchPhone(input: string): string | null {
  const s = input.replace(/[^+\d]/g, "");
  const n = s.startsWith("+31") ? "0" + s.slice(3) : s.startsWith("0031") ? "0" + s.slice(4) : s;
  return /^0\d{9}$/.test(n) ? n : null;
}
export function parseTrustooProfiles(html: string, pageUrl: string, category: string, city: string): TrustooCandidate[] {
  const $ = cheerio.load(html);
  const results = new Map<string, TrustooCandidate>();
  // Candidate discovery from actual profile links, not unverified CSS class names.
  $('a[href]').each((_, a) => {
    const href = $(a).attr("href") || "";
    let url: URL;
    try { url = new URL(href, pageUrl); } catch { return; }
    if (!/(^|\.)trustoo\.nl$/i.test(url.hostname)) return;
    const parts = url.pathname.split("/").filter(Boolean);
    if (parts.length < 4 || !parts[3] || parts[3] === "schilder") return;
    const name = clean($(a).text()) || clean($(a).attr("title") || "");
    if (name.length < 3 || name.length > 140) return;
    const key = url.origin + url.pathname.replace(/\/$/, "");
    if (results.has(key)) return;
    const card = $(a).closest("article, li, [data-testid], .card");
    const text = clean(card.text());
    const phoneMatch = text.match(/(?:\+31|0031|0)[\s().-]?(?:\d[\s().-]?){9}/);
    const phone = phoneMatch ? normalizeDutchPhone(phoneMatch[0]) : null;
    results.set(key, {source:"trustoo",sourceUrl:key,companyName:field(name),city:field(city),
      phone:field(phone),website:field<string>(null),rating:field<number>(null),
      reviewCount:field<number>(null),category,collectedAt:new Date().toISOString(),websiteStatus:"UNVERIFIED"});
  });
  return [...results.values()];
}
export function nextPageCandidates(html: string, pageUrl: string): string[] {
  const $ = cheerio.load(html); const urls = new Set<string>();
  $('a[href]').each((_,a)=> {
    const label = clean($(a).text()).toLowerCase();
    const rel = ($(a).attr("rel") || "").toLowerCase();
    if (!/meer resultaten|volgende|toon meer/.test(label) && !rel.includes("next")) return;
    try { const u = new URL($(a).attr("href")!,pageUrl); if(u.origin===new URL(pageUrl).origin) urls.add(u.href); } catch {}
  });
  return [...urls];
}

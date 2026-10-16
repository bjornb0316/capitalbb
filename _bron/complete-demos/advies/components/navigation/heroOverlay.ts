// Kleine brug tussen een openingsscène en de header, zonder globale scrollhandler.
let current = true;
export function setHeroOverlay(v: boolean) {
  if (v === current) return;
  current = v;
  window.dispatchEvent(new CustomEvent("hero-overlay", { detail: v }));
}
export function resetHeroOverlay() {
  current = true;
}

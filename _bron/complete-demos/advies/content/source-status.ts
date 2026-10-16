// Interne contentlijst: wat is bevestigd, wat ontbreekt, wat moet de adviseur goedkeuren.
// Wordt getoond op de interne startpagina en in de demonotities.

export type SourceStatus = "bron" | "bevestigen" | "ontbreekt" | "concept";

export const sourceItems: { item: string; status: SourceStatus; note: string }[] = [
  { item: "Naam, rol en plaats (Nederland)", status: "bron", note: "het adviesnetwerk-adviseursprofiel." },
  { item: "Motto “Kan niet, ken ik niet”", status: "bron", note: "het adviesnetwerk-adviseursprofiel." },
  { item: "Aansluiting bij het adviesnetwerk", status: "bron", note: "het adviesnetwerk-adviseursprofiel. Officieel het adviesnetwerk-logo nog aanleveren; niet nagetekend." },
  { item: "Telefoon Demo — geen telefoonnummer en e-mail", status: "bevestigen", note: "Staan op het het adviesnetwerk-profiel. Bevestig dat de adviseur deze op zijn eigen site wil tonen." },
  { item: "WhatsApp", status: "bevestigen", note: "het adviesnetwerk-profiel noemt WhatsApp. Daarom alleen als secundaire route getoond." },
  { item: "Portretfoto van de adviseur", status: "ontbreekt", note: "Een rustig portretvlak (“Portret van de adviseur · volgt”) staat klaar op alle plekken; geen gegenereerd portret." },
  { item: "Eigen klantreviews", status: "ontbreekt", note: "het adviesnetwerk-scores zijn netwerkbreed en worden niet als de adviseur zijn eigen score getoond." },
  { item: "Kosten en vrijblijvendheid eerste gesprek", status: "bevestigen", note: "het adviesnetwerk-profiel noemt een gratis, vrijblijvend eerste gesprek. Pas tonen na bevestiging." },
  { item: "Zakelijke financieringen breder dan hypotheek", status: "ontbreekt", note: "Neutraal beschreven als hypotheekadvies voor ondernemers." },
  { item: "Kantooradres", status: "ontbreekt", note: "Niet getoond; geen eigen kantoor bevestigd." },
  { item: "Jaren ervaring, Credion-rol, reactietermijn", status: "ontbreekt", note: "Bewust weggelaten." },
  { item: "AFM-, KvK- en dienstverleningsdocumenten", status: "ontbreekt", note: "Footer krijgt deze links zodra ze zijn aangeleverd." },
  { item: "Introductieteksten van de adviseur", status: "concept", note: "Concepttekst uit het bouwplan; de adviseur keurt de formulering goed." },
  { item: "Privacyverklaring en verzenddienst formulieren", status: "ontbreekt", note: "Formulieren versturen niets in de demo." },
];

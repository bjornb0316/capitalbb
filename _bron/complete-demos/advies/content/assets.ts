// Beeldregister. Zodra een Higgsfield-beeld is goedgekeurd, zet het pad hier;
// tot die tijd tonen de scènes het tijdelijke posterbeeld (components/house/HousePoster).
// Herkomst per bestand: zie ASSETS.md.

export type Asset = { src: string; width: number; height: number; alt: string } | null;

export const assets = {
  exteriorDesktop: { src: '/demos/advies/assets/paul/exterior.webp', width: 1672, height: 941, alt: 'Sfeerbeeld van een Nederlandse woning met een warme verlichte entree' } as Asset,
  exteriorMobile: { src: '/demos/advies/assets/paul/exterior.webp', width: 1672, height: 941, alt: 'Een uitnodigende Nederlandse woning bij avondlicht' } as Asset,
  entrance: null as Asset,
  approachVideo: { src: '/demos/advies/assets/paul/approach-scroll.mp4', poster: '/demos/advies/assets/paul/approach-poster.jpg' } as null | { src: string; poster: string },
  approachVideoMobile: null as null | { src: string; poster: string },
  interiorDesktop: { src: '/demos/advies/assets/paul/interior.webp', width: 1672, height: 941, alt: 'Sfeerbeeld van een lichte Nederlandse woonkamer' } as Asset,
  interiorMobile: { src: '/demos/advies/assets/paul/interior.webp', width: 1672, height: 941, alt: 'Een warme woonkamer met natuurlijk licht' } as Asset,
  workspace: { src: '/demos/advies/assets/paul/interior.webp', width: 1672, height: 941, alt: 'Een rustige plek aan een houten tafel' } as Asset,
};

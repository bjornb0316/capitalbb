export type ExtractionState = "FOUND" | "NOT_LISTED" | "UNREADABLE";
export interface Extracted<T> { value: T | null; state: ExtractionState; }
export interface TrustooCandidate {
  source: "trustoo"; sourceUrl: string; companyName: Extracted<string>;
  city: Extracted<string>; phone: Extracted<string>; website: Extracted<string>;
  rating: Extracted<number>; reviewCount: Extracted<number>;
  category: string; collectedAt: string; websiteStatus: "UNVERIFIED";
}
export interface SearchTask { category: string; city: string; url: string; }

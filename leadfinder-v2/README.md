# Capital BB Leadfinder 2.0 — clean-room implementation

Independent source code under `leadfinder-v2/` on `feature/leadfinder-v2`. No legacy scraper code imported. This is an initial **unvalidated parser scaffold**, not a production scraper.

## Pipeline
Trustoo category + city search → result/profile URL discovery → profile data extraction → deduplication → phone enrichment → Google Search/Maps + Instagram/Facebook website verification → CRM. Missing website links on Trustoo are **not** evidence of no website.

## Current implementation
- TypeScript candidate contract and per-field FOUND / NOT_LISTED / UNREADABLE states.
- Profile-link discovery from HTML and basic NL phone normalization.
- Candidate pagination link detection for ordinary links.
- Website status remains UNVERIFIED by design.

## Not yet implemented or verified
- Real Trustoo DOM selectors, dynamic 'Toon meer resultaten', browser automation, complete profile extraction, enrichment, verification, persistence, CRM integration, and integration tests.
- No claim of working lead generation or verified Trustoo access.
- Do not merge into main or expose to sales team until end-to-end acceptance tests pass.

## Local setup
`npm install && npm run check` from this folder.

## Migration
Once `capitalbb-leadfinder` repository exists, copy only `leadfinder-v2/` into the new repository root. Keep the existing Capital BB main branch untouched.

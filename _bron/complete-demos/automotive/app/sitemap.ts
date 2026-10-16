export const dynamic = "force-static";
import type {MetadataRoute} from 'next';import {vehicles,inventory} from '../lib/inventory';
export default function sitemap():MetadataRoute.Sitemap{const base='https://autobedrijf-automotive.vercel.app';return ['/','/occasions','/werkplaats','/over-ons','/contact','/privacy',...vehicles.map(v=>'/occasions/'+v.slug)].map(route=>({url:base+route,lastModified:new Date(inventory.fetchedAt),changeFrequency:'weekly' as const,priority:route==='/'?1:.7}))}

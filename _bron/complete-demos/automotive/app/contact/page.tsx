import {Suspense} from 'react';
import InnerHeader from '../../components/InnerHeader';
import ContactFromQuery from '../../components/ContactFromQuery';
import {vehicles} from '../../lib/inventory';
export const metadata={title:'Contact & proefrit | Automotive — Concept'};
export default function Contact(){return <main className="inner-page"><InnerHeader section="IN CONTACT"/><Suspense fallback={<p>Contactformulier laden…</p>}><ContactFromQuery vehicles={vehicles.map(({id,title,slug})=>({id,title,slug}))}/></Suspense></main>}

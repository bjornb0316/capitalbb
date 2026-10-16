import Link from 'next/link';
import {ArrowLeft,ArrowUpRight} from 'lucide-react';
export default function InnerHeader({section}:{section:string}){return <header className="subnav complete-subnav"><Link href="/" className="brand">AUTOMOTIVE<small>BV / AUTOMOTIVE</small></Link><nav aria-label="Paginanavigatie"><Link href="/occasions">Voorraad</Link><Link href="/werkplaats">Werkplaats</Link><Link href="/over-ons">Ons verhaal</Link><Link href="/contact">Contact <ArrowUpRight size={14}/></Link></nav><span>{section}</span></header>}

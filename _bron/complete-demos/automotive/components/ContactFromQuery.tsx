'use client';
import {useSearchParams} from 'next/navigation';
import ContactExperience from './ContactExperience';
export default function ContactFromQuery({vehicles}:{vehicles:{id:string;title:string;slug:string}[]}){
 const query=useSearchParams();const vehicle=vehicles.find(v=>v.id===query.get('auto'));
 const subject=query.get('onderwerp')||'';
 return <ContactExperience vehicle={vehicle} initialSubject={['Proefrit','Inruil','Onderhoud','Algemene vraag'].includes(subject)?subject:vehicle?'Proefrit':'Algemene vraag'}/>;
}

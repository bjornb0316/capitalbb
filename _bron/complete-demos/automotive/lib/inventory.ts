import raw from '../data/inventory.json';
export type Vehicle = typeof raw.vehicles[number];
export type VehicleSummary = Pick<Vehicle,'id'|'slug'|'make'|'title'|'model'|'year'|'mileage'|'body'|'transmission'|'fuel'|'power'|'price'|'vatExcluded'> & {image:string;photoCount:number};
export const inventory=raw;
export const vehicles=raw.vehicles;
export const stockDate=new Intl.DateTimeFormat('nl-NL',{day:'numeric',month:'long',year:'numeric',timeZone:'Europe/Amsterdam'}).format(new Date(raw.fetchedAt));
export const summarize=(v:Vehicle):VehicleSummary=>({id:v.id,slug:v.slug,make:v.make,title:v.title,model:v.model,year:v.year,mileage:v.mileage,body:v.body,transmission:v.transmission,fuel:v.fuel,power:v.power,price:v.price,vatExcluded:v.vatExcluded,image:v.photos[0],photoCount:v.photos.length});
export const money=(price:number|null)=>price===null?'Prijs op aanvraag':new Intl.NumberFormat('nl-NL',{style:'currency',currency:'EUR',maximumFractionDigits:0}).format(price);
export const distance=(n:number)=>new Intl.NumberFormat('nl-NL').format(n)+' km';

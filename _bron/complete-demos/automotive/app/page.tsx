import {existsSync} from "node:fs";
import path from "node:path";
import {vehicles,summarize} from "../lib/inventory";
import HomeExperience from "../components/HomeExperience";
export default function Home(){
 return <HomeExperience featured={vehicles.filter(v=>v.price!==null&&v.photos.length>10).slice(0,3).map(summarize)} hasVideo={existsSync(path.join(process.cwd(),"public/media/autobedrijf-hero.mp4"))} hasPoster={existsSync(path.join(process.cwd(),"public/media/autobedrijf-poster.jpg"))}/>;
}

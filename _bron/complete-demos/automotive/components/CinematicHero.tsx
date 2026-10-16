"use client";
import {useEffect,useRef,useState} from "react";
import Link from "next/link";
import {ArrowUpRight,ArrowDown} from "lucide-react";

export default function CinematicHero({hasVideo,hasPoster}:{hasVideo:boolean;hasPoster:boolean}){
 const section=useRef<HTMLElement>(null),stage=useRef<HTMLDivElement>(null),video=useRef<HTMLVideoElement>(null),canvas=useRef<HTMLCanvasElement>(null);
 const [failed,setFailed]=useState(false);
 useEffect(()=>{
  const root=section.current,screen=stage.current,v=video.current,c=canvas.current;
  if(!root||!screen||!v||!c||!hasVideo)return;
  const ctx=c.getContext("2d");
  const mobile=window.matchMedia("(max-width: 800px), (pointer: coarse)"),reduced=window.matchMedia("(prefers-reduced-motion: reduce)");
  const frames=new Map<number,HTMLImageElement>(),pending=new Set<number>(),broken=new Set<number>();
  let disposed=false,raf=0,target=0,lastProgress=0,desktopLoaded=false;
  const schedule=()=>{if(!disposed&&!raf)raf=requestAnimationFrame(render);};
  const requestFrame=(index:number)=>{
   if(index<1||index>154||frames.has(index)||pending.has(index)||broken.has(index)||pending.size>=8)return;
   pending.add(index);
   const img=new Image();img.decoding="async";
   img.onload=()=>{
    pending.delete(index);if(disposed)return;
    frames.set(index,img);
    if(frames.size>24){const farthest=[...frames.keys()].sort((a,b)=>Math.abs(b-target)-Math.abs(a-target))[0];frames.delete(farthest);}
    if(mobile.matches)schedule();
   };
   img.onerror=()=>{pending.delete(index);broken.add(index);};
   img.src="/demos/automotive/media/journey/frame-"+String(index).padStart(3,"0")+".webp";
  };
  const render=()=>{
   raf=0;if(disposed)return;
   root.classList.toggle("is-reduced",reduced.matches);
   if(reduced.matches){screen.classList.remove("is-arrived","is-clear");return;}
   const box=root.getBoundingClientRect(),travel=root.offsetHeight-screen.offsetHeight;
   const progress=travel>0?Math.max(0,Math.min(1,-box.top/travel)):0;
   screen.style.setProperty("--journey",String(progress));
   screen.classList.toggle("is-arrived",progress>.88);
   screen.classList.toggle("is-clear",progress>.1&&progress<=.88);
   if(mobile.matches&&ctx){
    target=1+Math.round(progress*153);
    requestFrame(target);
    const direction=progress>=lastProgress?1:-1;
    for(let step=1;step<=4;step++){requestFrame(target+step*direction);requestFrame(target-step*direction);}
    const img=frames.get(target);
    if(img){
     const ratio=Math.min(window.devicePixelRatio||1,2),w=Math.round(screen.clientWidth*ratio),h=Math.round(screen.clientHeight*ratio);
     if(c.width!==w||c.height!==h){c.width=w;c.height=h;}
     const scale=Math.max(w/img.width,h/img.height),dw=img.width*scale,dh=img.height*scale;
     if(w/h<.85){
      ctx.fillStyle="#05090e";ctx.fillRect(0,0,w,h);
      ctx.save();ctx.globalAlpha=.24;ctx.filter="blur("+24*ratio+"px)";ctx.drawImage(img,(w-dw)*.45,(h-dh)*.5,dw,dh);ctx.restore();
      const frameHeight=w*img.height/img.width,top=h*.27;
      ctx.drawImage(img,0,top,w,frameHeight);
      ctx.strokeStyle="rgba(255,255,255,.18)";ctx.lineWidth=ratio;ctx.strokeRect(0,top,w,frameHeight);
     }else ctx.drawImage(img,(w-dw)*.45,(h-dh)*.5,dw,dh);
     c.dataset.frame=String(target);
    }
   }else if(!mobile.matches){
    if(!desktopLoaded){desktopLoaded=true;v.src="/demos/automotive/media/autobedrijf-hero-v2.mp4";v.load();}
    if(v.readyState>=1&&Number.isFinite(v.duration)&&!v.seeking){
     const time=progress*Math.max(0,v.duration-.05);if(Math.abs(v.currentTime-time)>.035)v.currentTime=time;
    }
   }
   lastProgress=progress;
  };
  const observer=new ResizeObserver(schedule);observer.observe(screen);
  window.addEventListener("scroll",schedule,{passive:true});window.addEventListener("resize",schedule);
  mobile.addEventListener("change",schedule);reduced.addEventListener("change",schedule);
  v.addEventListener("loadedmetadata",schedule);v.addEventListener("seeked",schedule);
  schedule();
  return()=>{disposed=true;cancelAnimationFrame(raf);observer.disconnect();window.removeEventListener("scroll",schedule);window.removeEventListener("resize",schedule);mobile.removeEventListener("change",schedule);reduced.removeEventListener("change",schedule);v.removeEventListener("loadedmetadata",schedule);v.removeEventListener("seeked",schedule);frames.clear();};
 },[hasVideo]);
 const poster=hasPoster?"/demos/automotive/media/autobedrijf-poster-v2.jpg":"/demos/automotive/media/autobedrijf-night-building.webp";
 return <section ref={section} className={`cinematic-journey ${!hasVideo?"is-still":""}`} aria-label="Ontdek het autobedrijf Automotive"><div ref={stage} className="video-hero" style={{backgroundImage:`url("${poster}")`}}>
  {hasVideo&&<><video ref={video} muted playsInline preload="auto" poster={poster} onError={()=>setFailed(true)} aria-hidden="true" tabIndex={-1}/><canvas ref={canvas} className="journey-canvas" aria-hidden="true"/></>}
  <div className="video-hero-overlay"/>
  <div className="video-hero-top"><span>FAMILIEBEDRIJF SINDS 1956</span><span>AUTOBEDRIJF / BEEK</span></div>
  <div className="video-hero-intro"><p>DRIE GENERATIES. ÉÉN PASSIE.</p><h1>EEN VERTROUWD ADRES.</h1><div className="hero-actions"><Link className="primary" href="/occasions">ONTDEK DE SHOWROOM <ArrowUpRight size={18}/></Link><Link href="/over-ons">ONS VERHAAL <ArrowUpRight size={18}/></Link></div></div>
  <div className="video-hero-arrival"><p>VAN WERKPLAATS NAAR SHOWROOM</p><h2>JOUW VOLGENDE HOOFDSTUK.</h2><Link href="/occasions">ONTDEK DE OCCASIONS <ArrowUpRight size={18}/></Link></div>
  <div className="video-hero-bottom"><span>01 / THE AUTOMOTIVE EXPERIENCE</span><a href="#ervaring">ONTDEK AUTOMOTIVE <ArrowDown size={16}/></a></div>
  {hasVideo&&<div className="journey-progress" aria-hidden="true"/>}{failed&&<span className="video-hero-fallback">SCROLL OM AUTOMOTIVE TE ONTDEKKEN</span>}
 </div></section>;
}

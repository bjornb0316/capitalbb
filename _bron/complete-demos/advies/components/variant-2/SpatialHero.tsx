"use client";

import Link from "next/link";
import { unlockScrollVideo } from "@/components/motion/unlockScrollVideo";
import Image from "next/image";
import { useEffect, useRef, useState } from "react";
import { paul } from "@/content/paul";
import { situations, type SituationId } from "@/content/situations";
import { Arrow } from "@/components/contact/icons";
import { useScene, gsap, ScrollTrigger } from "@/components/motion/useScene";
import { motion } from "@/components/motion/config";
import { setHeroOverlay } from "@/components/navigation/heroOverlay";

export function SpatialHero() {
  const root = useRef<HTMLElement>(null);
  const trigger = useRef<ScrollTrigger | null>(null);
  const [eligible,setEligible] = useState(false);
  const [ready,setReady] = useState(false);
  const [failed,setFailed] = useState(false);
  const [choice,setChoice] = useState<SituationId | ''>('');
  useEffect(() => {
    const query = window.matchMedia(motion.mq.motionOk);
    const update = () => setEligible(query.matches);
    update(); query.addEventListener('change',update);
    return () => query.removeEventListener('change',update);
  }, []);

  useScene(root, (mm,el) => {
    mm.add(motion.mq.motionOk, () => {
      const video = el.querySelector<HTMLVideoElement>('video');
      const pin = el.querySelector<HTMLElement>('.v2-cinema__pin')!;
      const opening = el.querySelector<HTMLElement>('.v2-cinema__content')!;
      const living = el.querySelector<HTMLElement>('.v2-journey__living')!;
      const chooser = el.querySelector<HTMLElement>('.v2-journey__choice')!;
      const shade = el.querySelector<HTMLElement>('.v2-cinema__shade')!;
      const signature = el.querySelector<HTMLElement>('.v2-cinema__signature')!;
      const exterior = el.querySelector<HTMLElement>('.v2-journey__exterior')!;
      const playhead = {progress:0};
      let raf = 0;
      const seek = () => {
        raf=0;
        if(video && !video.seeking && video.readyState>=2 && Number.isFinite(video.duration)) {
          const target=playhead.progress*Math.max(0,video.duration-.05);
          if(Math.abs(video.currentTime-target)>1/60) video.currentTime=target;
        }
      };
      const queueSeek=()=>{if(!raf) raf=requestAnimationFrame(seek);};
      const lockVideo=unlockScrollVideo(video,queueSeek);
      video?.addEventListener('loadeddata',queueSeek);
      video?.addEventListener('seeked',queueSeek);
      const tl=gsap.timeline({scrollTrigger:{trigger:pin,start:'top top',end:'+=260%',pin:true,refreshPriority:100,scrub:.65,anticipatePin:1,
        onUpdate:self=>setHeroOverlay(self.progress<.98),onLeave:()=>setHeroOverlay(false),onEnterBack:()=>setHeroOverlay(true)}});
      trigger.current=tl.scrollTrigger || null;
      if(video) {
        tl.to(playhead,{progress:1,duration:.78,ease:'none',onUpdate:queueSeek},0);
        tl.to(exterior,{autoAlpha:0,duration:.04,ease:'none'},0);
      }
      tl.to(opening,{autoAlpha:0,y:-35,duration:.15},.22);
      tl.to(signature,{autoAlpha:0,duration:.12},.22);
      tl.fromTo(living,{autoAlpha:0,y:28},{autoAlpha:1,y:0,duration:.14},.39);
      tl.to(living,{autoAlpha:0,y:-25,duration:.12},.65);
      tl.to(shade,{opacity:.8,duration:.15},.75);
      tl.fromTo(chooser,{autoAlpha:0,y:35},{autoAlpha:1,y:0,duration:.17},.79);
      tl.to({}, {duration:.3},.96);
      // Invisible scene controls stay outside keyboard focus until their scene appears.
      const syncFocus=()=>{ opening.inert=gsap.getProperty(opening,'opacity')===0; chooser.inert=Number(gsap.getProperty(chooser,'opacity'))<.1; };
      tl.eventCallback('onUpdate',syncFocus);
      syncFocus();
      return ()=>{lockVideo();cancelAnimationFrame(raf);video?.removeEventListener('loadeddata',queueSeek);video?.removeEventListener('seeked',queueSeek);opening.inert=false;chooser.inert=false;trigger.current=null;setHeroOverlay(true);};
    });
  },[eligible,failed]);

  const revealRoute=()=>{
    const st=trigger.current;
    if(st) window.scrollTo({top:st.start+(st.end-st.start)*.87,behavior:'smooth'});
    else document.getElementById('jouw-route')?.scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth'});
  };
  return <section ref={root} className="v2-hero v2-cinema v2-journey" aria-labelledby="v2-hero-title">
    <div className="v2-cinema__pin">
      <div data-hero-sentinel className="v1-hero__sentinel" aria-hidden="true" />
      <div className="v2-cinema__media" aria-hidden="true">
        <Image src="/demos/advies/assets/paul/v2-door-consistent-poster.jpg" alt="" fill sizes="100vw" className="v2-cinema__video only-desktop" />
        {eligible && !failed && <video src="/demos/advies/assets/paul/v2-door-consistent-scroll.mp4" poster="/demos/advies/assets/paul/v2-door-consistent-poster.jpg" muted playsInline preload="auto" className="v2-cinema__video" style={{opacity:ready?1:0}} onLoadedData={()=>setReady(true)} onError={()=>{setFailed(true);setReady(false);}} />}
        <div className="v2-journey__exterior"><Image src="/demos/advies/assets/paul/v2-door-consistent-poster.jpg" alt="" fill priority sizes="100vw" className="v2-cinema__poster" /></div>
        <div className="v2-cinema__shade" />
      </div>
      <div className="container v2-cinema__content">
        <h1 id="v2-hero-title" className="v2-hero__title">Wat wil jij <span>mogelijk maken?</span></h1>
        <p className="v2-hero__intro">Een volgende woning. Ruimte om te ondernemen. Een plan dat verder gaat dan de standaard.</p>
        <div className="v2-hero__actions"><button type="button" onClick={revealRoute} className="btn btn--primary">Ontdek jouw route <Arrow /></button><Link href="/variant-3/kennismaken" className="btn btn--outline-light">Maak direct kennis</Link></div>
      </div>
      <div className="v2-journey__living"><div className="v2-journey__mobile-room only-mobile" aria-hidden="true"><Image src="/demos/advies/assets/paul/v2-house-interior.webp" alt="" fill sizes="100vw" /></div><p>Ruimte voor wat jij<br />wilt bereiken.</p><span>Een persoonlijk verhaal.<br />Een aanpak die bij jou begint.</span></div>
      <div id="jouw-route" className="v2-journey__choice">
        <div className="v2-journey__choice-image" aria-hidden="true"><Image src="/demos/advies/assets/paul/v2-house-garden.webp" alt="" fill sizes="100vw" /></div>
        <div className="v2-journey__choice-inner">
          <h2>Wat wordt jouw<br /><span>volgende stap?</span></h2>
          <p>Kies wat er bij jou speelt. De adviseur kijkt met je mee.</p>
          <fieldset><legend className="sr-only">Welke situatie past bij jou?</legend><div className="v2-journey__routes">
            {(['kopen','ondernemer','overwaarde','complex'] as const).map((id,i)=>{const s=situations.find(x=>x.id===id)!;return <label key={id} data-selected={choice===id}><input type="radio" name="journey-situation" value={id} checked={choice===id} onChange={()=>setChoice(id)} /><span className="v2-journey__route-number">0{i+1}</span><span>{s.cardTitle}</span><Arrow /></label>;})}
          </div></fieldset>
          <div className="v2-journey__continue" aria-live="polite">{choice?<Link className="btn btn--primary" href={`/variant-3/kennismaken?situatie=${choice}`}>Vertel de adviseur jouw plannen <Arrow /></Link>:<span>Kies je situatie om verder te gaan.</span>}</div>
        </div>
      </div>
      <p className="v2-cinema__signature"><span>“{paul.motto}”</span><small>Onafhankelijk adviseur</small></p>
      <span className="v2-cinema__scroll" aria-hidden="true">Van jouw woonwens naar een persoonlijk gesprek <i /></span>
    </div>
  </section>;
}

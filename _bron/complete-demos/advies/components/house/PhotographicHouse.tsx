"use client";

import { useEffect, useRef, type CSSProperties } from 'react';
import Image from 'next/image';
import type { HouseState } from './HouseModel';
import '@/styles/photographic-house.css';

export type PhotographicHouseProps = {
  state?: HouseState; preview?: HouseState | null; intro?: boolean;
  tilt?: boolean; className?: string; build?: 1 | 2 | 3; label?: string;
};

/** A photographic diorama with real pointer response and explicit situation states.
 * This is layered imagery, not a WebGL scene or financial simulation. */
export function PhotographicHouse({state='idle', preview=null, intro=true, tilt=true, className='',build,label='Ruimtelijke woningillustratie'}:PhotographicHouseProps) {
  const root=useRef<HTMLDivElement>(null);
  const shown=state==='idle' && preview ? preview : state;
  useEffect(()=>{
    const el=root.current;
    if(!el || !tilt) return;
    const mq=window.matchMedia('(pointer:fine) and (prefers-reduced-motion:no-preference)');
    let frame=0;
    const reset=()=>{el.style.setProperty('--model-rx','0deg');el.style.setProperty('--model-ry','0deg');};
    const move=(event:PointerEvent)=>{
      if(!mq.matches) return;
      const box=el.getBoundingClientRect();
      const x=(event.clientX-box.left)/box.width-.5;
      const y=(event.clientY-box.top)/box.height-.5;
      cancelAnimationFrame(frame);
      frame=requestAnimationFrame(()=>{el.style.setProperty('--model-ry',`${x*7}deg`);el.style.setProperty('--model-rx',`${-y*4}deg`);});
    };
    el.addEventListener('pointermove',move,{passive:true});
    el.addEventListener('pointerleave',reset);
    mq.addEventListener('change',reset);
    return()=>{cancelAnimationFrame(frame);el.removeEventListener('pointermove',move);el.removeEventListener('pointerleave',reset);mq.removeEventListener('change',reset);};
  },[tilt]);
  return <div ref={root} className={`hm hm-photo ${intro?'hm-photo--intro':''} ${className}`} data-state={shown} data-build={build} style={{'--model-rx':'0deg','--model-ry':'0deg'} as CSSProperties}>
    <div className="hm-photo__scene">
      <Image src="/demos/advies/assets/paul/v2-exterior-unique.webp" alt={label} width={1672} height={941} sizes="(min-width:1024px) 55vw,90vw" className="hm-photo__image" priority={intro} />
      <div className="hm-photo__focus" aria-hidden="true" />
      <div className="hm-photo__outline" aria-hidden="true" />
    </div>
  </div>;
}

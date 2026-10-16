/* Native document scroll is the only timeline. Media never autoplays. */
(()=>{'use strict';
const root=document.documentElement,section=document.querySelector('.cinematic');if(!section)return;
const video=section.querySelector('video'),logo=document.querySelector('.shared-logo'),target=document.querySelector('.logo-target'),label=section.querySelector('.scene-label'),copy=section.querySelector('.final-copy'),positioning=section.querySelector('.positioning');
const reduced=matchMedia('(prefers-reduced-motion: reduce)'),portrait=matchMedia('(max-width:700px)'),clamp=v=>Math.max(0,Math.min(1,v));
let staticMode=reduced.matches||navigator.connection?.saveData,ready=false,seeking=false,requested=0,frame=0,mode='',timer,decodedEnd=false;
let displayedProgress=null,lastTick=0,snapProgress=false;
const styles=new Map(),css=(n,v)=>{if(styles.get(n)!==v){styles.set(n,v);root.style.setProperty(n,v);}};
function fallback(){staticMode=true;document.body.classList.add('static-mode');video.removeAttribute('src');video.load();ready=false;clearTimeout(timer);draw();}
function setup(){mode=portrait.matches?'mobile':'desktop';if(staticMode){fallback();return;}document.body.classList.remove('static-mode');video.poster=`${section.dataset.media}/${mode}-poster.webp`;video.src=`${section.dataset.media}/installatie-${mode}-scrub.mp4`;video.preload='auto';ready=false;seeking=false;decodedEnd=false;video.load();clearTimeout(timer);timer=setTimeout(()=>{if(!ready)fallback();},12000);}
function seek(){if(!ready||seeking)return;const t=Math.min(Math.round(requested*24)/24,video.duration-1/24);if(Math.abs(video.currentTime-t)<.018)return;seeking=true;video.currentTime=t;}
video.addEventListener('loadeddata',()=>{ready=true;clearTimeout(timer);schedule();});
video.addEventListener('seeked',()=>{seeking=false;decodedEnd=video.currentTime>=video.duration-1/24-.018;schedule();});
video.addEventListener('error',fallback);
function draw(now=performance.now()){frame=0;const box=section.getBoundingClientRect(),range=Math.max(1,section.offsetHeight-innerHeight),goal=clamp(-box.top/range);
// Soften discrete wheel steps in the visual timeline only; document scrolling stays native.
const dt=lastTick?Math.min(50,now-lastTick):16.67;lastTick=now;
if(displayedProgress===null||staticMode||snapProgress){displayedProgress=goal;snapProgress=false;}else displayedProgress+=(goal-displayedProgress)*(1-Math.exp(-dt/65));
if(Math.abs(goal-displayedProgress)<.00025)displayedProgress=goal;else schedule();
const p=displayedProgress,film=clamp(p/.78),end=p>=.78,finalReady=staticMode||decodedEnd,migrate=staticMode?1:finalReady?clamp((p-.88)/.08):0,a=target.getBoundingClientRect();
requested=ready?film*(video.duration-1/24):0;seek();
const small=portrait.matches,startW=small?142:Math.min(250,innerWidth*.19),startX=small?24:innerWidth*(innerWidth>1100?.18:.08),startY=small?innerHeight*.095:innerHeight*.21;
const opening=p<.13&&!staticMode,fade=staticMode?1:opening?1-clamp((p-.035)/.075):finalReady?clamp((p-.78)/.045):0;
const x=opening?(innerWidth-startW)/2:startX,y=opening?innerHeight*.3:startY;
css('--logo-x',`${x+(a.left-x)*migrate}px`);css('--logo-y',`${y+(a.top-y)*migrate}px`);css('--logo-w',`${startW+(a.width-startW)*migrate}px`);css('--logo-opacity',fade);
css('--header-alpha',migrate*.96);css('--header-line',migrate*.15);css('--opening-opacity',opening?fade:0);
const position=staticMode?0:finalReady?clamp((p-.96)/.03):0,show=staticMode?1:finalReady?clamp((p-.825)/.035)*(1-clamp((p-.925)/.025)):0;css('--copy-opacity',show);css('--copy-y',`${(1-show)*12}px`);css('--copy-visibility',show>0?'visible':'hidden');copy.inert=show===0;
css('--position-opacity',position);css('--position-visibility',position>0?'visible':'hidden');if(positioning)positioning.inert=position===0;
css('--video-opacity',staticMode?0:end&&decodedEnd?0:1);
const scene=staticMode?'Airco · Warmtepompen':film<.17?'01 / Techniek':film<.38?'02 / Architectuur':film<.60?'03 / Comfort':film<.8?'04 / Installatie':'05 / de installateur';if(label.textContent!==scene)label.textContent=scene;
const progress=p.toFixed(4),state=staticMode?'static':end&&decodedEnd?'dom':'film';if(section.dataset.progress!==progress)section.dataset.progress=progress;if(section.dataset.state!==state)section.dataset.state=state;
}
function schedule(){if(!frame)frame=requestAnimationFrame(draw);}
addEventListener('scroll',schedule,{passive:true});addEventListener('resize',schedule,{passive:true});addEventListener('pageshow',schedule);
portrait.addEventListener('change',()=>{if(mode!==(portrait.matches?'mobile':'desktop'))setup();schedule();});reduced.addEventListener('change',()=>{if(reduced.matches)fallback();});
document.querySelectorAll('.skip-film,.skip-content').forEach(a=>a.addEventListener('click',()=>{snapProgress=true;document.querySelector('#inhoud')?.focus({preventScroll:true});schedule();}));
setup();draw();
})();


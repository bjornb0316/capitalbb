"use client";

import Link from "next/link";
import { unlockScrollVideo } from "@/components/motion/unlockScrollVideo";
import { useEffect, useRef, useState } from "react";
import { assets } from "@/content/assets";
import { paul, primaryCta } from "@/content/paul";
import { SceneImage } from "@/components/house/SceneImage";
import { Arrow } from "@/components/contact/icons";
import { useScene, gsap } from "@/components/motion/useScene";
import { motion } from "@/components/motion/config";
import { setHeroOverlay } from "@/components/navigation/heroOverlay";

/**
 * Scène V1-01: de woning en het motto.
 * Desktop: korte pinned camerareis (140 vh extra scroll) richting de entree.
 * Mobiel en verminderde beweging: geen pin, korte beeldbeweging, normale doorloop.
 */
export function HeroFilm() {
  const root = useRef<HTMLElement>(null);
  const [videoEligible, setVideoEligible] = useState(false);
  const [videoFailed, setVideoFailed] = useState(false);
  const [videoReady, setVideoReady] = useState(false);
  const video = assets.approachVideo;
  const hasEntrance = !!assets.entrance && !video;
  useEffect(() => {
    const query = window.matchMedia(motion.mq.motionOk);
    const update = () => setVideoEligible(query.matches);
    update();
    query.addEventListener('change', update);
    return () => query.removeEventListener('change', update);
  }, []);

  useScene(root, (mm, el) => {
    mm.add(motion.mq.motionOk, () => {
      const pin = el.querySelector<HTMLElement>(".v1-hero__pin")!;
      const ext = el.querySelector<HTMLElement>(".v1-hero__layer--ext")!;
      const ent = el.querySelector<HTMLElement>(".v1-hero__layer--ent");
      const content = el.querySelector<HTMLElement>(".v1-hero__content")!;
      const hint = el.querySelector<HTMLElement>(".v1-hero__hint");
      const veil = el.querySelector<HTMLElement>(".v1-hero__veil")!;
      const interior = el.querySelector<HTMLElement>('.v1-hero__interior');
      const vid = el.querySelector<HTMLVideoElement>("video.v1-hero__video");
      const arrival = el.querySelector<HTMLElement>('.v1-hero__arrival');
      const caption = el.querySelector<HTMLElement>('.v1-hero__caption');

      const tl = gsap.timeline({
        defaults: { ease: "none" },
        scrollTrigger: {
          trigger: pin,
          start: "top top",
          end: motion.scroll.v1HeroDistance,
          pin: true,
          refreshPriority: 100,
          scrub: motion.scroll.scrub,
          anticipatePin: 1,
          // Header wordt ondoorzichtig zodra het openingsbeeld plaatsmaakt.
          onUpdate: (self) => setHeroOverlay(self.progress < 0.85),
          onLeave: () => setHeroOverlay(false),
          onEnterBack: () => setHeroOverlay(true),
        },
      });

      // 0–25%: buitenaanzicht blijft breed
      tl.to(ext, { scale: 1.04, duration: 0.25 }, 0);
      if (hint) tl.to(hint, { autoAlpha: 0, duration: 0.1 }, 0);

      let disposeVideo = () => {};
      if (vid) {
        // Video volgt de scroll; seeks worden via rAF beperkt.
        const playhead = { progress: 0 };
        let raf = 0;
        const seek = () => {
          raf = 0;
          const time = playhead.progress * (Number.isFinite(vid.duration) ? vid.duration : 0) * .999;
          if (!vid.seeking && Number.isFinite(vid.duration) && vid.readyState >= 2 && Math.abs(vid.currentTime - time) > 0.03) vid.currentTime = time;
        };
        const ready = () => seek();
        const lockVideo = unlockScrollVideo(vid, ready);
        vid.addEventListener('loadeddata', ready);
        vid.addEventListener('seeked', ready);
        disposeVideo = () => { lockVideo(); cancelAnimationFrame(raf); vid.removeEventListener('loadeddata', ready); vid.removeEventListener('seeked', ready); };
        tl.to(
          playhead,
          {
            duration: 0.6,
            progress: 1,
            onUpdate() {
              if (!raf) raf = requestAnimationFrame(seek);
            },
          },
          0.25,
        );
      } else {
        // 25–60%: beeld beweegt richting entree
        tl.to(ext, { scale: hasEntrance ? 1.55 : 2.25, duration: 0.35, ease: "power1.in" }, 0.25);
        if (ent && hasEntrance) {
          tl.fromTo(ent, { autoAlpha: 0, scale: 1.12 }, { autoAlpha: 1, scale: 1, duration: 0.22 }, 0.45);
        }
      }

      // 60–85%: titel verschuift rustig en maakt ruimte
      tl.to(content, { yPercent: -18, autoAlpha: 0, duration: 0.25, ease: "power1.in" }, 0.6);
      if (interior && !vid) tl.fromTo(interior, {autoAlpha:0,scale:1.08}, {autoAlpha:1,scale:1,duration:.25}, .72);
      // 85–100%: overgang naar scène 2
      tl.to(veil, { autoAlpha: 0.3, duration: 0.15 }, 0.85);
      if (caption) tl.to(caption, {autoAlpha:0,duration:.15}, .6);
      if (arrival) tl.fromTo(arrival, {autoAlpha:0,y:24}, {autoAlpha:1,y:0,duration:.16}, .9);
      tl.to({}, {duration:.25}, 1.06);
      return () => { disposeVideo(); setHeroOverlay(true); };
    });
  }, [videoFailed, videoEligible]);

  return (
    <section ref={root} className="v1-hero" aria-labelledby="v1-hero-title">
      <div className="v1-hero__pin">
        <div data-hero-sentinel className="v1-hero__sentinel" aria-hidden="true" />
        <div className="v1-hero__media">
          <div className="v1-hero__layer v1-hero__layer--ext">
            <SceneImage asset={video ? {src:video.poster,width:1280,height:720,alt:'Nederlandse woning aan een tuinpad, beginbeeld van de camerareis'} : assets.exteriorDesktop} kind="exterior" className="scene-fill cinema-media" priority idp="hero-d" />
            {video && videoEligible && !videoFailed && (
              <video
                className="v1-hero__video scene-fill cinema-media"
                style={{opacity: videoReady ? 1 : 0}}
                onLoadedData={() => setVideoReady(true)}
                onError={() => { setVideoFailed(true); setVideoReady(false); }}
                src={video.src}
                poster={video.poster}
                muted
                playsInline
                preload="auto"
                aria-hidden="true"
              />
            )}
            <SceneImage
              asset={assets.exteriorMobile}
              kind="exterior"
              mobile
              className="scene-fill only-mobile"
              priority
              idp="hero-m"
            />
          </div>
          {hasEntrance && (
            <div className="v1-hero__layer v1-hero__layer--ent only-desktop" aria-hidden="true">
              <SceneImage asset={assets.entrance} kind="entrance" className="scene-fill" idp="hero-e" />
            </div>
          )}
          <div className="v1-hero__shade" aria-hidden="true" />
          <div className="v1-hero__interior scene-fill cinema-media" aria-hidden="true">
            <SceneImage asset={assets.interiorDesktop} kind="interior" className="scene-fill" idp="hero-interior" />
          </div>
        </div>

        <div className="container v1-hero__content">
          <p className="v1-hero__eyebrow caps">
            Financieel adviseur · {paul.place}
          </p>
          <h1 id="v1-hero-title" className="display v1-hero__title">
            <span className="v1-hero__line">{paul.mottoLines[0]}</span>
            <span className="v1-hero__line">{paul.mottoLines[1]}</span>
          </h1>
          <p className="v1-hero__lead">
            Een financiële vraag die niet vanzelfsprekend is? Ik kijk met je mee naar de mogelijkheden.
          </p>
          <div className="v1-hero__actions">
            <Link href="/variant-2/kennismaken" className="btn btn--light">
              {primaryCta} <Arrow />
            </Link>
            <a href="#aanpak" className="btn btn--outline-light">
              Ontdek mijn aanpak
            </a>
          </div>
        </div>

        <div className="container v1-hero__meta only-desktop" aria-hidden="true">
          <span className="caps">{paul.name}</span>
          <span className="v1-hero__hint caps">
            <span />
            Scroll
          </span>
          <span className="caps">Aangesloten bij {paul.network}</span>
        </div>
        <div className="v1-hero__veil" aria-hidden="true" />
        <div className="v1-hero__arrival">
          <p>Vertel me wat je wilt bereiken.</p>
          <span>Ik kijk met je mee.</span>
          <Link href="/variant-2/kennismaken" className="btn btn--light">Vertel de adviseur jouw situatie <Arrow /></Link>
        </div>
        <p className="v1-hero__caption">Een volgende stap begint met jouw verhaal.<span>Persoonlijk. Onafhankelijk. Betrokken.</span></p>
      </div>
    </section>
  );
}

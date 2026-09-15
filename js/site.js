/* =========================================================================
   Gedrag van de Capital BB-site. Klein en zonder afhankelijkheden.
   Contactgegevens komen uit het data-attribuut dat bouw.py hier neerzet;
   er staat dus nergens een tweede kopie van een telefoonnummer.
   ========================================================================= */

(function () {
  "use strict";

  var CONTACT = window.CBB_CONTACT || { whatsapp: "", email: "", telefoon: "" };
  var stil = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* ---------------- Mobiel menu ---------------- */
  var knop = document.getElementById("nav-knop");
  var menu = document.getElementById("nav-menu");
  if (knop && menu) {
    knop.addEventListener("click", function () {
      var open = knop.getAttribute("aria-expanded") === "true";
      knop.setAttribute("aria-expanded", open ? "false" : "true");
      menu.hidden = open;
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        knop.setAttribute("aria-expanded", "false");
        menu.hidden = true;
      }
    });
  }

  /* ---------------- Hero-terugval ----------------
     Zonder scroll-driven animations speelt de montage op tijd, zodra hij
     in beeld is. Mét ondersteuning doet CSS het werk en gebeurt hier niets. */
  var montage = document.getElementById("montage");
  if (montage && !CSS.supports("animation-timeline: view()") && !stil.matches) {
    var kijker = new IntersectionObserver(function (entries, self) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          self.unobserve(e.target);
          montage.classList.add("speel");
        }
      });
    }, { threshold: 0.25 });
    kijker.observe(montage);
  }

  /* ---------------- Vaste actiebalk op mobiel ----------------
     Op de contact- en scanpagina zelf niet, want daar staat het formulier al. */
  var pad = location.pathname;
  var opDoel = /\/(contact|scan)\/?$/.test(pad.replace(/index\.html$/, ""));
  if (!opDoel) {
    var diep = document.querySelector('link[rel="stylesheet"]').getAttribute("href").indexOf("../") === 0 ? "../" : "";
    var balk = document.createElement("div");
    balk.className = "actiebalk";
    balk.innerHTML =
      '<a class="btn btn-ghost" href="' + diep + 'scan/">Gratis scan</a>' +
      '<a class="btn btn-gold" href="' + diep + 'contact/">Plan kennismaking</a>';
    document.body.appendChild(balk);
  }

  /* ---------------- Zwevende WhatsApp-knop ----------------
     Klein, merkeigen, en pas zichtbaar zodra de bezoeker voorbij de hero is:
     de filmische opening blijft schoon. Niet op de scan- en contactpagina,
     want daar staat het formulier al. */
  if (!opDoel && CONTACT.whatsapp) {
    var bubbel = document.createElement("a");
    bubbel.className = "wa-bubbel";
    bubbel.href = "https://wa.me/" + CONTACT.whatsapp + "?text=" +
      encodeURIComponent("Hoi Björn, ik heb een vraag.");
    bubbel.target = "_blank";
    bubbel.rel = "noopener";
    bubbel.setAttribute("aria-label", "Stuur een WhatsApp-bericht");
    bubbel.innerHTML =
      '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">' +
      '<path d="M12 3.5c-4.7 0-8.5 3.4-8.5 7.6 0 2.4 1.2 4.5 3.1 5.9l-.8 3.5 3.6-1.6c.8.2 1.7.4 2.6.4 4.7 0 8.5-3.4 8.5-7.6S16.7 3.5 12 3.5z" ' +
      'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>' +
      '<circle cx="8.6" cy="11.1" r="1.05" fill="currentColor"/>' +
      '<circle cx="12" cy="11.1" r="1.05" fill="currentColor"/>' +
      '<circle cx="15.4" cy="11.1" r="1.05" fill="currentColor"/></svg>';
    document.body.appendChild(bubbel);

    var eersteSectie = document.querySelector("main .sectie");
    if (eersteSectie) {
      var bubbelKijker = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          bubbel.classList.toggle("zichtbaar", e.isIntersecting || e.boundingClientRect.top < 0);
        });
      }, { threshold: 0 });
      bubbelKijker.observe(eersteSectie);
    } else {
      bubbel.classList.add("zichtbaar");
    }
  }

  /* ---------------- Meten en toestemming ----------------
     Google Analytics plaatst cookies, dus mag het pas laden nadat de bezoeker
     daar ja op heeft gezegd. Niet ervoor, en niet "tenzij hij nee zegt".

     De regels die hier zijn ingebouwd:
     - er wordt niets geladen en niets opgeslagen zolang er geen keuze is
     - weigeren staat even prominent als accepteren, en kost één klik
     - de keuze wordt lokaal bewaard, niet in een cookie van een derde
     - de keuze is later te wijzigen via de link in de voettekst
     - zonder meet-ID gebeurt er helemaal niets en is er geen banner */
  var META = window.CBB_META || { ga4: "" };
  var KEUZE = "cbb-meten";

  function keuzeLezen() {
    try { return localStorage.getItem(KEUZE); } catch (e) { return null; }
  }
  function keuzeSchrijven(v) {
    try { localStorage.setItem(KEUZE, v); } catch (e) { /* privémodus: dan per bezoek vragen */ }
  }

  function analyticsLaden() {
    if (!META.ga4 || window.__cbbGeladen) return;
    window.__cbbGeladen = true;
    var sc = document.createElement("script");
    sc.async = true;
    sc.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(META.ga4);
    document.head.appendChild(sc);
    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag("js", new Date());
    gtag("consent", "default", {
      ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied",
      analytics_storage: "granted"
    });
    gtag("config", META.ga4, { anonymize_ip: true });
  }

  /* Doelen meesturen, zodat zichtbaar wordt wat een bezoek oplevert en niet
     alleen hoeveel bezoeken er waren. Doet niets zonder toestemming. */
  function doel(naam, extra) {
    if (typeof window.gtag === "function") window.gtag("event", naam, extra || {});
  }
  window.CBBdoel = doel;

  function bannerTonen() {
    if (!META.ga4 || document.getElementById("cookiebalk")) return;
    var b = document.createElement("div");
    b.className = "cookiebalk";
    b.id = "cookiebalk";
    b.setAttribute("role", "dialog");
    b.setAttribute("aria-modal", "false");
    b.setAttribute("aria-label", "Cookievoorkeur");
    var diep = document.querySelector('link[rel="stylesheet"]').getAttribute("href").indexOf("../") === 0 ? "../" : "";
    b.innerHTML =
      '<p class="cookiebalk-tekst">Wij gebruiken statistieken om te zien welke pagina’s ' +
      'worden gelezen. Daar horen cookies bij, dus vragen wij het eerst. Zonder toestemming ' +
      'wordt er niets geladen en werkt de site gewoon. ' +
      '<a class="tekstlink" href="' + diep + 'privacy/">Lees wat er wordt gemeten</a>.</p>' +
      '<div class="cookiebalk-knoppen">' +
      '<button class="btn btn-ghost btn-sm" type="button" id="cookie-nee">Weigeren</button>' +
      '<button class="btn btn-gold btn-sm" type="button" id="cookie-ja">Accepteren</button>' +
      "</div>";
    document.body.appendChild(b);
    document.body.classList.add("cookie-open");
    document.getElementById("cookie-ja").addEventListener("click", function () {
      keuzeSchrijven("ja"); sluiten(); analyticsLaden();
    });
    document.getElementById("cookie-nee").addEventListener("click", function () {
      keuzeSchrijven("nee"); sluiten();
    });
    function sluiten() {
      b.remove();
      document.body.classList.remove("cookie-open");
    }
  }

  if (META.ga4) {
    var gekozen = keuzeLezen();
    if (gekozen === "ja") analyticsLaden();
    else if (gekozen !== "nee") bannerTonen();

    // Voettekstlink om de keuze te herzien.
    var herzien = document.getElementById("cookie-herzien");
    if (herzien) {
      herzien.hidden = false;
      herzien.addEventListener("click", function (e) {
        e.preventDefault();
        try { localStorage.removeItem(KEUZE); } catch (er) {}
        bannerTonen();
      });
    }
  }

  /* Klikken op WhatsApp, telefoon of mail tellen als conversie. Voor veel
     bezoekers is dat de echte actie; wie belt vult geen formulier in. Eén
     luisteraar op document, zodat ook knoppen meetellen die de JS pas later
     aan de pagina toevoegt. */
  document.addEventListener("click", function (e) {
    var a = e.target && e.target.closest ? e.target.closest("a[href]") : null;
    if (!a) return;
    var href = a.getAttribute("href") || "";
    if (href.indexOf("wa.me") > -1) {
      doel("whatsapp_klik", { plek: a.className || "link", pagina: location.pathname });
    } else if (href.indexOf("tel:") === 0) {
      doel("telefoon_klik", { pagina: location.pathname });
    } else if (href.indexOf("mailto:") === 0) {
      doel("mail_klik", { pagina: location.pathname });
    }
  }, true);

  /* ---------------- Formulieren ----------------
     Twee routes, in deze volgorde:

     1. Is er een verzendsleutel ingesteld (FORMULIER in _bron/inhoud.py), dan
        gaat de inzending als e-mail de deur uit via Web3Forms. De bezoeker
        hoeft niets meer te doen.
     2. Is die er niet, of mislukt de verzending, dan valt hij terug op het
        oude gedrag: WhatsApp of het mailprogramma openen met alles er al in.

     Die terugval is het punt. Een formulier dat stilletjes faalt kost een
     klant; hier houdt de bezoeker altijd een werkende route over. */
  var FORM = window.CBB_FORMULIER || { dienst: "", sleutel: "", ontvanger: "" };

  function bericht(onderwerp, waarden) {
    var regels = [onderwerp, ""];
    for (var k in waarden) {
      if (waarden[k]) regels.push(k.charAt(0).toUpperCase() + k.slice(1) + ": " + waarden[k]);
    }
    return regels.join("\n");
  }

  /* Terugval: de bezoeker verstuurt zelf, via zijn eigen mailprogramma of via
     WhatsApp. Welke van de twee staat in FORMULIER["terugval"] in
     _bron/inhoud.py en is standaard e-mail, want daar horen inzendingen te
     landen. WhatsApp blijft wel als losse knop op de pagina staan voor wie
     dat zelf liever heeft. */
  function zelfVersturen(onderwerp, waarden, klaarEl, melding) {
    var tekst = bericht(onderwerp, waarden);
    var viaMail = FORM.terugval !== "whatsapp" ? !!CONTACT.email : !CONTACT.whatsapp;
    if (viaMail) {
      window.location.href = "mailto:" + CONTACT.email +
        "?subject=" + encodeURIComponent(onderwerp) +
        "&body=" + encodeURIComponent(tekst);
    } else if (CONTACT.whatsapp) {
      window.open("https://wa.me/" + CONTACT.whatsapp + "?text=" + encodeURIComponent(tekst),
                  "_blank", "noopener");
    }
    if (klaarEl) {
      if (melding) klaarEl.textContent = melding;
      klaarEl.hidden = false;
    }
    doel("formulier_overgedragen", { route: viaMail ? "mail" : "whatsapp",
                                     pagina: location.pathname });
  }

  function verstuur(vorm, velden, foutEl, onderwerp, klaarEl) {
    /* Dubbel verzenden voorkomen. De knop wordt verderop uitgezet, maar met
       Enter of een snelle dubbelklik kan submit twee keer afgaan voordat dat
       gebeurt. Dan zou dezelfde aanvraag twee keer in de mailbox landen. */
    if (vorm.dataset.bezig === "ja") return;
    if (klaarEl) klaarEl.hidden = true;
    var oudVervolg = document.getElementById("scan-vervolg");
    if (vorm.id === "scanform" && oudVervolg) oudVervolg.hidden = true;

    var waarden = {};
    for (var k in velden) {
      var el = document.getElementById(velden[k]);
      waarden[k] = el ? el.value.trim() : "";
    }
    var leeg = Object.keys(velden).filter(function (k) {
      return k !== "vraag" && k !== "doel" && !waarden[k];
    });
    if (leeg.length) {
      foutEl.textContent = "Vul eerst alle velden in.";
      foutEl.hidden = false;
      return;
    }
    if (!FORM.sleutel && !CONTACT.whatsapp && !CONTACT.email) {
      foutEl.textContent = "Deze site is nog niet gekoppeld aan een verzendroute. " +
        "Vul CONTACT of FORMULIER in _bron/inhoud.py in en bouw opnieuw.";
      foutEl.hidden = false;
      return;
    }
    foutEl.hidden = true;

    /* Honeypot: is het verborgen veld ingevuld, dan was het een bot. We doen
       alsof het gelukt is en versturen niets. */
    var val = vorm.querySelector('input[name="botcheck"]');
    if (val && val.value) {
      if (klaarEl) klaarEl.hidden = false;
      return;
    }

    if (!FORM.sleutel) {
      zelfVersturen(onderwerp, waarden, klaarEl);
      return;
    }

    var knop = vorm.querySelector('button[type="submit"]');
    var knoptekst = knop ? knop.textContent : "";
    vorm.dataset.bezig = "ja";
    if (knop) { knop.disabled = true; knop.textContent = "Bezig met versturen…"; }

    var lading = {
      access_key: FORM.sleutel,
      subject: onderwerp + " — " + (waarden.bedrijf || waarden.website || waarden.naam || ""),
      from_name: waarden.naam || "Website",
      botcheck: "",
      // Los meegestuurd, zodat de mail leesbare regels heeft in plaats van
      // alleen een JSON-dump.
      bericht: bericht(onderwerp, waarden),
      pagina: location.href
    };
    for (var v in waarden) lading[v] = waarden[v];
    if (FORM.ontvanger) lading.to = FORM.ontvanger;
    // Antwoorden kan alleen als de bezoeker een e-mailadres achterliet.
    if (waarden.bereikbaar && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(waarden.bereikbaar)) {
      lading.replyto = waarden.bereikbaar;
    }

    /* Tijdslimiet. In de praktijk duurt het versturen enkele seconden, maar
       een bezoeker mag nooit eindeloos naar een uitgeschakelde knop kijken
       als de verzenddienst niet antwoordt. Na 15 seconden breken we af en
       valt hij terug op de mailroute, zodat de aanvraag alsnog aankomt. */
    var afbreken = null;
    var opties = {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify(lading)
    };
    if (typeof AbortController === "function") {
      afbreken = new AbortController();
      opties.signal = afbreken.signal;
      setTimeout(function () { afbreken.abort(); }, 15000);
    }

    fetch("https://api.web3forms.com/submit", opties).then(function (r) {
      if (!r.ok) throw new Error("Verzenden niet bevestigd");
      return r.json();
    }).then(function (d) {
      if (!d || d.success !== true) throw new Error(d && d.message ? d.message : "verzenden mislukt");
      vorm.dataset.bezig = "";
      if (knop) { knop.disabled = false; knop.textContent = knoptekst; }
      // De juiste tekst staat al in de HTML: het scanformulier zegt iets
      // anders dan het contactformulier. Hier alleen tonen, niet overschrijven.
      if (klaarEl) klaarEl.hidden = false;
      doel("formulier_verstuurd", { formulier: vorm.id, pagina: location.pathname });
      doel("generate_lead", { form_id: vorm.id, lead_source: "website", pagina: location.pathname });
      if (vorm.id === "scanform") {
        var vervolg = document.getElementById("scan-vervolg");
        if (vervolg) { vervolg.hidden = false; vervolg.focus(); }
      }
      vorm.reset();
    }).catch(function () {
      // Niet verloren laten gaan: alsnog de handmatige route aanbieden.
      vorm.dataset.bezig = "";
      if (knop) { knop.disabled = false; knop.textContent = knoptekst; }
      var route = (FORM.terugval !== "whatsapp" && CONTACT.email) ? "uw mailprogramma" : "WhatsApp";
      zelfVersturen(onderwerp, waarden, klaarEl,
        "Automatisch versturen lukte even niet. Uw bericht staat nu klaar in " + route +
        "; verstuur hem daar, dan komt hij alsnog aan.");
    });
  }

  var scanform = document.getElementById("scanform");
  if (scanform) {
    scanform.addEventListener("submit", function (e) {
      e.preventDefault();
      var invoer = document.getElementById("s-url").value.trim();
      var url = "";
      try {
        var parsed = new URL(/^https?:\/\//i.test(invoer) ? invoer : "https://" + invoer);
        if ((parsed.protocol === "https:" || parsed.protocol === "http:") && !parsed.username && !parsed.password && /^(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,63}$/i.test(parsed.hostname)) url = parsed.hostname.toLowerCase();
      } catch (error) {}
      var fout = document.getElementById("s-fout");
      if (!url) {
        fout.textContent = "Vul eerst het adres van uw website in.";
        fout.hidden = false;
        return;
      }
      var bereik = document.getElementById("s-bereik");
      var contact = bereik.value.trim();
      var emailGoed = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(contact);
      var telefoonGoed = /^\+?[\d\s().-]+$/.test(contact) && contact.replace(/\D/g, "").length >= 8 && contact.replace(/\D/g, "").length <= 15;
      if (!emailGoed && !telefoonGoed) {
        fout.textContent = "Vul een geldig e-mailadres of telefoonnummer in, zodat we u kunnen bereiken.";
        fout.hidden = false; bereik.focus(); return;
      }
      document.getElementById("s-url").value = url;
      verstuur(scanform,
        { website: "s-url", naam: "s-naam", bereikbaar: "s-bereik", doel: "s-doel" },
        fout, "Aanvraag Website Performance Scan",
        document.getElementById("s-klaar"));
    });
  }

  var contactform = document.getElementById("contactform");
  if (contactform) {
    /* Intentie meegeven vanaf een dienst-CTA: /contact/?over=crm vult het
       vraagveld alvast. De tekst komt uit een vaste lijst die de bouw hier
       neerzet, nooit uit de URL zelf, en de bezoeker ziet en verstuurt hem
       zelf. De bezorging van het formulier verandert niet. */
    var lijst = window.CBB_INTENTIES || {};
    var over = (location.search.match(/[?&]over=([a-z-]{1,32})(?:&|$)/) || [])[1];
    var vraagveld = document.getElementById("c-vraag");
    if (over && vraagveld && !vraagveld.value && lijst[over]) {
      vraagveld.value = lijst[over];
    }

    contactform.addEventListener("submit", function (e) {
      e.preventDefault();
      verstuur(contactform,
        { bedrijf: "c-bedrijf", naam: "c-naam", bereikbaar: "c-bereik", vraag: "c-vraag" },
        document.getElementById("c-fout"), "Aanvraag via de website",
        document.getElementById("c-klaar"));
    });
  }

  /* Directe contactlinks op de contactpagina. */
  var direct = document.getElementById("contact-direct");
  if (direct) {
    var h = "";
    if (CONTACT.telefoon) h += '<a href="tel:' + CONTACT.telefoon.replace(/\s/g, "") + '">Bel ' + CONTACT.telefoon + "</a>";
    if (CONTACT.whatsapp) h += '<a href="https://wa.me/' + CONTACT.whatsapp + '" rel="noopener">Stuur een WhatsApp</a>';
    if (CONTACT.email) h += '<a href="mailto:' + CONTACT.email + '">' + CONTACT.email + "</a>";
    direct.innerHTML = h;
  }
})();


/* Native scroll storytelling; all chapters remain readable without JavaScript. */
(function () {
  'use strict';
  var hero = document.querySelector('.cinema');
  var journey = document.querySelector('.journey');
  if (!hero || !journey) return;
  var reduced = matchMedia('(prefers-reduced-motion: reduce)');
  var chapters = Array.from(journey.querySelectorAll('.journey-chapter'));
  var scenes = Array.from(journey.querySelectorAll('.journey-scene'));
  var counter = journey.querySelector('.journey-current');
  var scheduled = false;
  var active = -1;
  journey.classList.add('is-scrolly');
  function paint() {
    scheduled = false;
    if (reduced.matches || innerWidth <= 700) {
      hero.style.removeProperty('--camera-scale');
      hero.style.removeProperty('--camera-y');
    } else {
      var distance = Math.min(1, Math.max(0, -hero.getBoundingClientRect().top / hero.offsetHeight));
      hero.style.setProperty('--camera-scale', String(1 + distance * .12));
      hero.style.setProperty('--camera-y', distance * 70 + 'px');
    }
    var line = innerHeight * (innerWidth <= 700 ? .62 : .52);
    var index = 0;
    chapters.forEach(function (chapter, i) {
      if (chapter.getBoundingClientRect().top <= line) index = i;
    });
    if (index !== active) {
      active = index;
      scenes.forEach(function (scene, i) { scene.classList.toggle('is-active', i === index); });
      chapters.forEach(function (chapter, i) { chapter.classList.toggle('is-active', i === index); });
      counter.textContent = String(index + 1).padStart(2, '0');
    }
    var first = chapters[0].getBoundingClientRect().top;
    var last = chapters[chapters.length - 1].getBoundingClientRect().top;
    var progress = Math.min(1, Math.max(0, (line - first) / Math.max(1, last - first)));
    journey.style.setProperty('--journey-progress', String(progress));
  }
  function schedule() { if (!scheduled) { scheduled = true; requestAnimationFrame(paint); } }
  addEventListener('scroll', schedule, { passive: true });
  addEventListener('resize', schedule, { passive: true });
  reduced.addEventListener('change', schedule);
  paint();
})();

/* Reveal once on entry; content stays visible without JS or with reduced motion. */
(function () {
  if (!document.body.classList.contains('home') || !('IntersectionObserver' in window)) return;
  var reduced = matchMedia('(prefers-reduced-motion: reduce)');
  if (reduced.matches) return;
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-revealed');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0, rootMargin: '0px 0px -30px 0px' });
  document.querySelectorAll('.home .spoor, .home .case-grid > *, .home .scan-grid > *, .home .faq-sectie .wrap > *, .home .cta-slot .cta-inhoud').forEach(function (element) {
    element.classList.add('reveal-ready');
    observer.observe(element);
  });
})();

/* Service content enters once; native details remain independently accessible. */
(function () {
  var page = document.querySelector('.dienst-editorial');
  if (!page || !('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) { if (entry.isIntersecting) { entry.target.classList.add('is-revealed'); observer.unobserve(entry.target); } });
  }, { rootMargin: '0px 0px -20px 0px' });
  page.querySelectorAll('.dienst-concept, .marketing-verhaal > *, .proces-baan li, .bouwt-item, .stapje, .dienstkaart').forEach(function (element) { element.classList.add('reveal-ready'); observer.observe(element); });
})();

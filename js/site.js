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

  /* ---------------- Formulieren ----------------
     Geen backend: het formulier opent WhatsApp of e-mail met de tekst er al
     in. Zonder ingevulde contactgegevens weigert het met een nette melding. */
  function verstuur(vorm, velden, foutEl, onderwerp, klaarEl) {
    var waarden = {};
    for (var k in velden) {
      var el = document.getElementById(velden[k]);
      waarden[k] = el ? el.value.trim() : "";
    }
    var leeg = Object.keys(velden).filter(function (k) {
      return k !== "vraag" && !waarden[k];
    });
    if (leeg.length) {
      foutEl.textContent = "Vul eerst alle velden in.";
      foutEl.hidden = false;
      return;
    }
    if (!CONTACT.whatsapp && !CONTACT.email) {
      foutEl.textContent = "Deze site is nog niet gekoppeld aan een telefoonnummer of " +
        "e-mailadres. Vul CONTACT in _bron/inhoud.py in en bouw opnieuw.";
      foutEl.hidden = false;
      return;
    }
    foutEl.hidden = true;

    var regels = [onderwerp, ""];
    for (var k2 in waarden) {
      if (waarden[k2]) regels.push(k2.charAt(0).toUpperCase() + k2.slice(1) + ": " + waarden[k2]);
    }
    var tekst = regels.join("\n");

    if (CONTACT.whatsapp) {
      window.open("https://wa.me/" + CONTACT.whatsapp + "?text=" + encodeURIComponent(tekst),
                  "_blank", "noopener");
    } else {
      window.location.href = "mailto:" + CONTACT.email +
        "?subject=" + encodeURIComponent(onderwerp) +
        "&body=" + encodeURIComponent(tekst);
    }
    // Succesmelding: het bericht is voorbereid, de bezoeker verstuurt zelf.
    if (klaarEl) klaarEl.hidden = false;
  }

  var scanform = document.getElementById("scanform");
  if (scanform) {
    scanform.addEventListener("submit", function (e) {
      e.preventDefault();
      var url = document.getElementById("s-url").value.trim()
        .replace(/^https?:\/\//i, "").replace(/\/.*$/, "").toLowerCase();
      var fout = document.getElementById("s-fout");
      if (url.length < 4 || url.indexOf(".") === -1) {
        fout.textContent = "Vul eerst het adres van uw website in.";
        fout.hidden = false;
        return;
      }
      document.getElementById("s-url").value = url;
      verstuur(scanform,
        { website: "s-url", naam: "s-naam", bereikbaar: "s-bereik" },
        fout, "Aanvraag Website Performance Scan",
        document.getElementById("s-klaar"));
    });
  }

  var contactform = document.getElementById("contactform");
  if (contactform) {
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

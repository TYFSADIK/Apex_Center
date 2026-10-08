#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO upgrade module: JSON-LD graphs, homepage sections, root files.
All JSON-LD is built as Python dicts and serialized with json.dumps so it always parses."""
import json
from site_data import SITE, SERVICES, AREAS, HOME_FAQS

GEO_LAT, GEO_LON = "43.7537", "-79.4640"
BASE = SITE["url"]
PHONE_E164 = SITE["phone_href"]
PHONE_DISP = SITE["phone_display"]
MAPS_URL = SITE["maps_url"]
ADDR_FULL = "Unit 41 & 42, 4544 Dufferin Street, Toronto (York University Heights, North York), ON M3H 5X2"

SERVICE_TYPES = {
    "lube-oil-filter": "Oil change",
    "brake-replacement-repair": "Brake repair",
    "diagnostic-services": "Auto diagnostics",
    "electrical-diagnostic": "Auto electrical repair",
    "fuel-filter-replacement": "Fuel system service",
    "preventative-maintenance": "Preventative maintenance",
    "engine-repair-maintenance": "Engine repair",
    "coolant-flush": "Cooling system service",
    "ball-joint-replacement": "Ball joint replacement",
    "fuel-pump-replacement": "Fuel pump replacement",
    "ac-service-replacement": "Auto AC repair",
    "wheel-bearings-replacement": "Wheel bearing replacement",
    "strut-assembly-replacement": "Strut replacement",
    "oxygen-sensor-replacement": "Oxygen sensor replacement",
    "battery-alternator-starter": "Battery and charging service",
    "cv-axle-shaft-assembly": "CV axle replacement",
    "ignition-coils-spark-plugs": "Ignition service",
    "engine-transmission-mount": "Engine mount replacement",
    "collision-body-work": "Collision body repair",
    "frame-straightening": "Frame straightening",
    "auto-painting": "Auto painting",
    "towing-service": "Towing service",
}

TODAY = "2026-10-07"
TODAY_HUMAN = "October 7, 2026"


def _business_ref():
    return {"@id": BASE + "/#business"}


def home_graph():
    offers = []
    for s in SERVICES:
        offers.append({
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "name": s["name"],
                "url": f"{BASE}/services/{s['slug']}.html",
                "serviceType": SERVICE_TYPES.get(s["slug"], "Auto repair"),
                "provider": _business_ref(),
            },
        })
    faq_entities = [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in HOME_FAQS
    ]
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "AutoRepair",
                "@id": BASE + "/#business",
                "name": SITE["name"],
                "alternateName": ["Apex Collision", "Apex Collision Center North York"],
                "slogan": "Car trouble ends at the Apex",
                "url": BASE + "/",
                "logo": {
                    "@type": "ImageObject",
                    "@id": BASE + "/#logo",
                    "url": BASE + "/assets/img/logo.jpg",
                    "caption": "Apex Collision Center logo",
                },
                "image": [
                    BASE + "/assets/img/hero.jpg",
                    BASE + "/assets/img/shop-bays.jpg",
                    BASE + "/assets/img/reception.jpg",
                    BASE + "/assets/img/about-shop.jpg",
                ],
                "description": ("Apex Collision Center is an independent auto repair, body shop and car servicing "
                    "shop at Unit 41 & 42, 4544 Dufferin Street in Toronto (York University Heights, North York), "
                    "Ontario. It services and repairs all makes and models, including oil changes, brakes, "
                    "diagnostics, electrical, AC, suspension, engine work, collision body repair, frame "
                    "straightening, auto painting and 24/7 towing, with written upfront quotes and a road test "
                    "on every repair."),
                "telephone": PHONE_E164,
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "Unit 41 & 42, 4544 Dufferin Street",
                    "addressLocality": "Toronto",
                    "addressRegion": "ON",
                    "postalCode": "M3H 5X2",
                    "addressCountry": "CA",
                },
                "geo": {"@type": "GeoCoordinates", "latitude": float(GEO_LAT), "longitude": float(GEO_LON)},
                "hasMap": MAPS_URL,
                "openingHoursSpecification": [
                    {"@type": "OpeningHoursSpecification",
                     "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                     "opens": "09:00", "closes": "17:00"},
                    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday",
                     "opens": "10:00", "closes": "15:00"},
                ],
                "currenciesAccepted": "CAD",
                "areaServed": [{"@type": "City", "name": n} for n in
                    ["North York", "Toronto", "Downtown Toronto", "Mississauga",
                     "Scarborough", "Etobicoke", "Vaughan", "Markham"]],
                "knowsAbout": ["Brake repair", "Oil changes", "Engine diagnostics",
                    "Electrical diagnosis", "Automotive air conditioning", "Suspension repair",
                    "Preventative maintenance", "Cooling system service", "Fuel system service",
                    "Starting and charging systems", "Collision body repair",
                    "Frame straightening", "Auto painting", "Towing service"],
                "contactPoint": [{
                    "@type": "ContactPoint", "telephone": PHONE_E164,
                    "contactType": "customer service", "areaServed": "CA-ON",
                    "availableLanguage": ["English"],
                }],
                "hasOfferCatalog": {
                    "@type": "OfferCatalog",
                    "name": "Auto repair and car servicing at Apex Collision Center",
                    "itemListElement": offers,
                },
                "potentialAction": {
                    "@type": "ReserveAction",
                    "name": "Book a service appointment",
                    "target": {
                        "@type": "EntryPoint",
                        "urlTemplate": BASE + "/contact.html#booking",
                        "inLanguage": "en-CA",
                        "actionPlatform": ["http://schema.org/DesktopWebPlatform",
                                           "http://schema.org/MobileWebPlatform"],
                    },
                    "result": {"@type": "Reservation", "name": "Service appointment"},
                },
            },
            {
                "@type": "WebSite",
                "@id": BASE + "/#website",
                "url": BASE + "/",
                "name": SITE["name"],
                "inLanguage": "en-CA",
                "publisher": _business_ref(),
            },
            {
                "@type": "WebPage",
                "@id": BASE + "/#webpage",
                "url": BASE + "/",
                "name": "Car Servicing & Auto Repair North York | Apex Collision Center",
                "description": ("Car servicing and auto repair in North York at Unit 41 & 42, 4544 Dufferin St. "
                    f"Brakes, oil changes, diagnostics, AC, body work, painting, 24/7 towing. Written quotes. {PHONE_DISP}."),
                "isPartOf": {"@id": BASE + "/#website"},
                "about": _business_ref(),
                "inLanguage": "en-CA",
                "primaryImageOfPage": {
                    "@type": "ImageObject",
                    "url": BASE + "/assets/img/hero.jpg",
                    "width": 1600, "height": 900,
                },
                "breadcrumb": {"@id": BASE + "/#breadcrumb"},
                "dateModified": TODAY,
                "speakable": {"@type": "SpeakableSpecification",
                              "cssSelector": [".apx-answer", ".apx-faq-a p"]},
            },
            {
                "@type": "BreadcrumbList",
                "@id": BASE + "/#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"}
                ],
            },
            {
                "@type": "FAQPage",
                "@id": BASE + "/#faq",
                "url": BASE + "/#faq",
                "isPartOf": {"@id": BASE + "/#webpage"},
                "mainEntity": faq_entities,
            },
        ],
    }


def page_graph(page_url, page_title, name, section_name, section_url, service_type=None, city=None):
    """WebPage + Service + BreadcrumbList graph for service and area pages."""
    nodes = [
        {
            "@type": "WebPage",
            "@id": page_url + "#webpage",
            "url": page_url,
            "name": page_title,
            "isPartOf": {"@id": BASE + "/#website"},
            "about": {"@id": page_url + "#service"},
            "inLanguage": "en-CA",
            "dateModified": TODAY,
            "breadcrumb": {"@id": page_url + "#breadcrumb"},
        },
        {
            "@type": "Service",
            "@id": page_url + "#service",
            "name": name,
            "serviceType": service_type or "Auto repair",
            "provider": _business_ref(),
            "areaServed": {"@type": "City", "name": city or "North York"},
            "url": page_url,
        },
        {
            "@type": "BreadcrumbList",
            "@id": page_url + "#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
                {"@type": "ListItem", "position": 2, "name": section_name, "item": section_url},
                {"@type": "ListItem", "position": 3, "name": name, "item": page_url},
            ],
        },
    ]
    return {"@context": "https://schema.org", "@graph": nodes}


def simple_webpage_graph(page_url, page_title, page_desc):
    return {"@context": "https://schema.org", "@graph": [
        {
            "@type": "WebPage",
            "@id": page_url + "#webpage",
            "url": page_url,
            "name": page_title,
            "description": page_desc,
            "isPartOf": {"@id": BASE + "/#website"},
            "inLanguage": "en-CA",
            "dateModified": TODAY,
            "breadcrumb": {"@id": page_url + "#breadcrumb"},
        },
        {
            "@type": "BreadcrumbList",
            "@id": page_url + "#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
                {"@type": "ListItem", "position": 2, "name": page_title.split(" | ")[0], "item": page_url},
            ],
        },
    ]}


BRANDS = [("Audi", "audi.png"),
          ("BMW", "bmw.png"),
          ("Mercedes-Benz", "mercedes-benz.png"),
          ("Porsche", "porsche.png"),
          ("Jaguar", "jaguar.png"),
          ("Land Rover", "land-rover.png"),
          ("Volkswagen", "volkswagen.png"),
          ("Toyota", "toyota.png"),
          ("Honda", "honda.png"),
          ("Ford", "ford.png"),
          ("Chevrolet", "chevrolet.png"),
          ("Nissan", "nissan.png"),
          ("Hyundai", "hyundai.png"),
          ("Kia", "kia.png"),
          ("Mazda", "mazda.png"),
          ("Subaru", "subaru.png"),
          ("Mitsubishi", "mitsubishi.png"),
          ("Lexus", "lexus.png"),
          ("Acura", "acura.png"),
          ("Infiniti", "infiniti.png"),
          ("Tesla", "tesla.png"),
          ("Volvo", "volvo.png"),
          ("Chrysler", "chrysler.png"),
          ("Dodge", "dodge.png"),
          ("Jeep", "jeep.png"),
          ("GMC", "gmc.png"),
          ("Cadillac", "cadillac.png"),
          ("Mini", "mini.png"),
          ("Genesis", "genesis.png"),
          ("Fiat", "fiat.png")]


def brand_marquee():
    badges = "".join(
        f'<img class="brand-logo" src="assets/img/brands/{f}" alt="{n}" loading="lazy">'
        for n, f in BRANDS)
    return f"""<section class="brand-strip" aria-label="Car brands we service">
  <div class="container">
    <h2 class="brand-title">We Work With</h2>
    <p class="brand-sub">All makes and models, domestic, Asian and European. If it has wheels, we service it.</p>
  </div>
  <div class="marquee" role="presentation">
    <div class="marquee-track"><div class="marquee-group">{badges}</div><div class="marquee-group" aria-hidden="true">{badges}</div></div>
  </div>
</section>"""


def symptom_cards():
    from site_data import SERVICES as _SVC
    cards = []
    for s in _SVC:
        symptom = s["signs"][0]
        cards.append(
            f'<article class="apx-card apx-symptom">'
            f'<img src="assets/img/{s["img"]}" alt="{_esc(s["name"])}: {_esc(symptom)}" loading="lazy">'
            f'<p class="apx-tag">Symptom</p><h3>{_esc(symptom)}</h3>'
            f'<p>{_esc(s["card"])}</p>'
            f'<p>See: <a href="services/{s["slug"]}.html">{_esc(s["name"])}</a></p></article>'
        )
    return "\n      ".join(cards)


def castrol_section():
    return """<section class="apx" id="castrol-warranty" aria-labelledby="apx-castrol-h">
  <div class="apx-wrap">
    <div class="castrol-grid">
      <div><img class="castrol-badge" src="assets/img/castrol-warranty.png" alt="Castrol engine warranty badge" loading="lazy"></div>
      <div>
        <p class="apx-kicker">Free engine protection</p>
        <h2 id="apx-castrol-h">Castrol Engine Warranty Program</h2>
        <p class="apx-answer">Get your oil change done with qualifying Castrol synthetic oil at Apex Collision Center and your engine gets an extra layer of protection. The Castrol Engine Warranty Program is a free limited warranty against oil-related engine damage, covering key components such as pistons, timing chains, turbo bearings and oil pumps.</p>
        <p>Enrollment is simple. Book an eligible Castrol oil change and we register your vehicle, with the warranty terms emailed to you. Ask us about it at your next visit, or read the official program details at the link below.</p>
        <div class="apx-cta">
          <a class="apx-btn" href="https://castrol-canada-warranty.email-preferences.com/en" target="_blank" rel="noopener">Castrol Warranty Details</a>
          <a class="apx-btn apx-btn-ghost" href="services/lube-oil-filter.html">Book an oil change</a>
        </div>
      </div>
    </div>
  </div>
</section>"""


def ld_script(graph):
    return '<script type="application/ld+json">\n' + json.dumps(graph, indent=2) + '\n</script>'


# ---------------------------------------------------------------- homepage sections
APX_CSS = """<style>
.apx{--apx-navy:#0b1e3a;--apx-accent:#d9381e;--apx-ink:#16202e;--apx-muted:#566176;--apx-line:#dde3ec;--apx-soft:#f4f6fa;--apx-radius:14px;color:var(--apx-ink);font-size:1rem;line-height:1.65}
.apx *,.apx *::before,.apx *::after{box-sizing:border-box}
.apx-wrap{max-width:1120px;margin-inline:auto;padding:clamp(2.5rem,6vw,4.25rem) 1.25rem}
.apx-alt{background:var(--apx-soft)}
.apx-kicker{margin:0 0 .5rem;font-size:.8125rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--apx-accent)}
.apx h2{margin:0 0 1rem;font-size:clamp(1.6rem,3.2vw,2.25rem);line-height:1.2;color:var(--apx-navy)}
.apx h3{margin:0 0 .5rem;font-size:1.125rem;line-height:1.3;color:var(--apx-navy)}
.apx p{margin:0 0 1rem}
.apx a{color:var(--apx-navy);text-decoration-thickness:.08em;text-underline-offset:.18em}
.apx a:hover{color:var(--apx-accent)}
.apx-lead{font-size:1.125rem;max-width:64ch}
.apx-answer{font-size:1.125rem;max-width:68ch;padding-left:1rem;border-left:4px solid var(--apx-accent)}
.apx-grid{display:grid;gap:1.1rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,17rem),1fr))}
.apx-card{background:#fff;border:1px solid var(--apx-line);border-radius:var(--apx-radius);padding:1.25rem 1.25rem 1.1rem}
.apx-card p:last-child{margin-bottom:0}
.apx-tag{display:inline-block;margin:0 0 .6rem;padding:.15rem .65rem;border-radius:999px;background:var(--apx-navy);color:#fff;font-size:.75rem;font-weight:600}
.apx-dl{display:grid;margin:1.5rem 0 0;border:1px solid var(--apx-line);border-radius:var(--apx-radius);overflow:hidden;background:#fff}
.apx-dl>div{display:grid;grid-template-columns:minmax(8rem,12rem) 1fr;gap:1rem;padding:.8rem 1.1rem;border-top:1px solid var(--apx-line)}
.apx-dl>div:first-child{border-top:0}
.apx-dl dt{font-weight:700;color:var(--apx-navy)}
.apx-dl dd{margin:0}
.apx-dl address{font-style:normal}
@media (max-width:560px){.apx-dl>div{grid-template-columns:1fr;gap:.15rem}}
.apx-scroll{overflow-x:auto}
.apx table{width:100%;min-width:34rem;border-collapse:collapse;background:#fff;border:1px solid var(--apx-line)}
.apx th,.apx td{padding:.75rem 1rem;text-align:left;vertical-align:top;border-bottom:1px solid var(--apx-line)}
.apx thead th{background:var(--apx-navy);color:#fff}
.apx tbody th{color:var(--apx-navy);width:28%}
.apx-faq details{background:#fff;border:1px solid var(--apx-line);border-radius:12px;margin-bottom:.7rem}
.apx-faq summary{cursor:pointer;padding:1rem 1.2rem;font-weight:700;color:var(--apx-navy)}
.apx-faq details[open] summary{border-bottom:1px solid var(--apx-line)}
.apx-faq-a{padding:1rem 1.2rem}
.apx-faq-a p{margin:0}
.apx-cta{display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.25rem}
.apx-btn{display:inline-block;padding:.8rem 1.3rem;border-radius:10px;background:var(--apx-accent);color:#fff!important;font-weight:700;text-decoration:none}
.apx-btn:hover{filter:brightness(.92)}
.apx-btn-ghost{background:transparent;color:var(--apx-navy)!important;box-shadow:inset 0 0 0 2px var(--apx-navy)}
.apx-updated{margin:1rem 0 0;font-size:.875rem;color:var(--apx-muted)}
.apx-chips{display:flex;flex-wrap:wrap;gap:.5rem;padding:0;margin:0 0 1rem;list-style:none}
.apx-chips a{display:inline-block;padding:.4rem .85rem;border:1px solid var(--apx-line);border-radius:999px;background:#fff;text-decoration:none;font-size:.9rem}
.apx-checks{margin:0 0 1rem;padding-left:1.2rem}
.apx-checks li{margin-bottom:.45rem}
.apx-snap-grid{display:grid;gap:1rem;grid-template-columns:repeat(3,1fr);margin-top:1.75rem}
.apx-snap-card{background:#fff;border:1px solid var(--apx-line);border-radius:var(--apx-radius);padding:1.35rem 1.35rem 1.25rem;box-shadow:0 1px 2px rgba(11,30,58,.05)}
.apx-snap-card h3{margin:0 0 .55rem;font-size:1.02rem;display:flex;align-items:center;gap:.6rem}
.apx-snap-ico{display:inline-flex;align-items:center;justify-content:center;width:2.1rem;height:2.1rem;border-radius:12px;background:var(--apx-navy);color:#fff;font-size:1rem;flex:none}
.apx-snap-card p{margin:0 0 .5rem;font-size:.94rem;color:var(--apx-muted)}
.apx-snap-card p:last-child{margin-bottom:0}
.apx-snap-card p strong{color:var(--apx-ink)}
.apx-snap-main{grid-row:span 2;background:var(--apx-navy);border-color:var(--apx-navy);color:#fff;display:flex;flex-direction:column}
.apx-snap-main h3{color:#fff}
.apx-snap-main .apx-snap-ico{background:var(--apx-accent)}
.apx-snap-main address{font-style:normal;color:#fff;margin:0 0 .75rem;font-size:.95rem;line-height:1.6}
.apx-snap-main p{color:#c3ccda}
.apx-snap-main a{color:#fff}
.apx-snap-main .apx-cta{margin-top:auto;padding-top:1rem}
.apx-snap-main .apx-btn-ghost{background:transparent;color:#fff!important;box-shadow:inset 0 0 0 2px rgba(255,255,255,.75)}
@media (max-width:900px){.apx-snap-grid{grid-template-columns:repeat(2,1fr)}.apx-snap-main{grid-row:auto;grid-column:1/-1}}
@media (max-width:580px){.apx-snap-grid{grid-template-columns:1fr}}
</style>"""


def _esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def home_faq_html():
    items = []
    for i, (q, a) in enumerate(HOME_FAQS):
        open_attr = " open" if i == 0 else ""
        items.append(
            f'<details name="apx-faq"{open_attr}><summary>{_esc(q)}</summary>'
            f'<div class="apx-faq-a"><p>{_esc(a)}</p></div></details>'
        )
    return "\n      ".join(items)


def home_sections():
    chips = "".join(
        f'<li><a href="services/{s["slug"]}.html">{_esc(s["name"])}</a></li>' for s in SERVICES
    )
    return APX_CSS + f"""
{brand_marquee()}
<section class="apx apx-alt" id="apex-at-a-glance" aria-labelledby="apx-glance-h">
  <div class="apx-wrap">
    <p class="apx-kicker">The short version</p>
    <h2 id="apx-glance-h">Apex Collision Center at a glance</h2>
    <p class="apx-lead">An independent auto repair, body shop and car servicing shop in North York. We service and repair all makes and models, and every job starts with testing and a written price you approve first, then a road test before you pay.</p>
    <div class="apx-snap-grid">
      <article class="apx-snap-card apx-snap-main">
        <h3><span class="apx-snap-ico" aria-hidden="true">&#8982;</span> Visit the shop</h3>
        <address>Unit 41 &amp; 42, 4544 Dufferin Street, Toronto (York University Heights, North York), ON M3H 5X2</address>
        <p><a href="tel:{PHONE_E164}">{PHONE_DISP}</a></p>
        <p>Mon to Fri 9:00 AM to 5:00 PM<br>Saturday 10:00 AM to 3:00 PM<br>Closed Sunday. Towing runs 24/7.</p>
        <p>Free parking and a comfortable waiting area on site.</p>
        <div class="apx-cta">
          <a class="apx-btn" href="tel:{PHONE_E164}">Call {PHONE_DISP}</a>
          <a class="apx-btn apx-btn-ghost" href="contact.html#booking">Book online</a>
        </div>
      </article>
      <article class="apx-snap-card">
        <h3><span class="apx-snap-ico" aria-hidden="true">&#9670;</span> What we are</h3>
        <p>Auto repair, body shop and car servicing for <strong>all makes and models</strong>: domestic, Asian and European.</p>
      </article>
      <article class="apx-snap-card">
        <h3><span class="apx-snap-ico" aria-hidden="true">&#9881;</span> What we do</h3>
        <p><strong>22 services</strong>: maintenance, brakes, diagnostics, electrical, AC, suspension, fuel system, engine work, collision body repair, frame straightening, auto painting and 24/7 towing.</p>
      </article>
      <article class="apx-snap-card">
        <h3><span class="apx-snap-ico" aria-hidden="true">&#10003;</span> How pricing works</h3>
        <p><strong>Diagnosis first</strong>, then a written quote with parts and labour broken out. Nothing starts until you approve it.</p>
      </article>
      <article class="apx-snap-card">
        <h3><span class="apx-snap-ico" aria-hidden="true">&#9673;</span> Proof of work</h3>
        <p>Worn parts saved for your inspection, measurements in writing, <strong>road test on every repair</strong>.</p>
      </article>
      <article class="apx-snap-card">
        <h3><span class="apx-snap-ico" aria-hidden="true">&#9719;</span> Walk-ins welcome</h3>
        <p>Drop in for inspections, diagnostics, oil changes and battery checks. <strong>Book ahead</strong> for larger repairs.</p>
      </article>
      <article class="apx-snap-card">
        <h3><span class="apx-snap-ico" aria-hidden="true">&#9678;</span> Who we serve</h3>
        <p>Drivers from <strong>North York, Toronto, Downtown Toronto, Mississauga, Scarborough, Etobicoke, Vaughan and Markham</strong>.</p>
      </article>
    </div>
    <p class="apx-updated">Details reviewed <time datetime="{TODAY}">{TODAY_HUMAN}</time>.</p>
  </div>
</section>

<section class="apx apx-alt" id="areas-served" aria-labelledby="apx-areas-h">
  <div class="apx-wrap">
    <p class="apx-kicker">Where our customers come from</p>
    <h2 id="apx-areas-h">Car servicing for North York, Toronto, Downtown, Scarborough and Mississauga drivers</h2>
    <p class="apx-lead">Our shop is on Dufferin Street, right off Highway 401 and close to Finch Avenue. Here is how the trip works from each side of the city, and why drivers make it.</p>
    <div class="apx-grid">
      <article class="apx-card"><p class="apx-tag">North York</p><h3>Right here on Dufferin</h3><p>Free parking at the shop, a waiting area, and walk-ins welcome for inspections, diagnostics, oil changes and battery checks. Larger repairs go on the schedule so the parts and a lift are ready.</p><p><a href="areas/north-york.html">Directions and booking</a></p></article>
      <article class="apx-card"><p class="apx-tag">Toronto</p><h3>Yorkdale, Downsview and south to Eglinton</h3><p>Dufferin Street and Allen Road run straight to us. Most Toronto drivers who use us came for a second opinion after another shop could not pin down the problem.</p><p><a href="areas/toronto.html">Toronto drivers</a></p></article>
      <article class="apx-card"><p class="apx-tag">Downtown Toronto</p><h3>Leave the core, get a straight answer</h3><p>From the downtown core, most drivers take Allen Road north to Highway 401, then Dufferin Street. Our Saturday hours, 10:00 AM to 3:00 PM, suit anyone who cannot spare a weekday.</p><p><a href="areas/downtown-toronto.html">Downtown Toronto drivers</a></p></article>
      <article class="apx-card"><p class="apx-tag">Scarborough</p><h3>Straight across the 401</h3><p>Take Highway 401 westbound to Dufferin Street. Bring the repair that keeps coming back: we measure and test first, then quote in writing before any work begins.</p><p><a href="areas/scarborough.html">Scarborough drivers</a></p></article>
      <article class="apx-card"><p class="apx-tag">Mississauga</p><h3>About 20 to 30 minutes</h3><p>Typically 20 to 30 minutes via Highway 401 east or Highway 427 north, depending on where you start and traffic. All 22 services are available, and Saturday appointments work well for the drive.</p><p><a href="areas/mississauga.html">Mississauga drivers</a></p></article>
      <article class="apx-card"><p class="apx-tag">And nearby</p><h3>Etobicoke, Vaughan and Markham</h3><p>Drivers from across the GTA use the same shop, the same written quotes and the same road test before you pay.</p><p><a href="areas/etobicoke.html">Etobicoke</a> &middot; <a href="areas/vaughan.html">Vaughan</a> &middot; <a href="areas/markham.html">Markham</a></p></article>
    </div>
  </div>
</section>

<section class="apx" id="symptom-guide" aria-labelledby="apx-symptoms-h">
  <div class="apx-wrap">
    <p class="apx-kicker">What is your car telling you?</p>
    <h2 id="apx-symptoms-h">Match the symptom to the repair</h2>
    <p class="apx-lead">Most drivers do not search for "ball joint replacement". They search for the noise. Find yours below, then call us with the details and we will tell you what the test should confirm.</p>
    <div class="apx-grid">
      {symptom_cards()}
    </div>
    <div class="apx-cta">
      <a class="apx-btn" href="tel:{PHONE_E164}">Call {PHONE_DISP}</a>
      <a class="apx-btn apx-btn-ghost" href="contact.html#booking">Book a diagnosis</a>
    </div>
  </div>
</section>

<section class="apx apx-alt" id="ontario-car-care" aria-labelledby="apx-seasons-h">
  <div class="apx-wrap">
    <p class="apx-kicker">Built for Ontario roads</p>
    <h2 id="apx-seasons-h">What your car needs through an Ontario year</h2>
    <p class="apx-lead">Salt, deep cold, potholes and summer gridlock wear a car in predictable ways. This is the order we would check things.</p>
    <div class="apx-grid">
      <article class="apx-card"><p class="apx-tag">Late fall, before the salt</p><h3>Battery and charging system test</h3><p>Cold cranking amps drop fast in an Ontario January. A battery that tested fine in September can fail in the first cold snap. Test the whole charging system, not just the battery.</p><p>Related: <a href="services/battery-alternator-starter.html">Battery and Charging Check</a></p></article>
      <article class="apx-card"><p class="apx-tag">Late fall, before the salt</p><h3>Brake inspection</h3><p>Worn pads stop worse on wet, salted roads. Have the pads, rotors, fluid and lines checked while the weather is still dry.</p><p>Related: <a href="services/brake-replacement-repair.html">Brake Repair</a></p></article>
      <article class="apx-card"><p class="apx-tag">Winter, December to March</p><h3>Watch the pothole damage</h3><p>Hitting a deep pothole can bend a wheel, damage a tire sidewall, or knock a control arm out of alignment. If you feel a new pull or a clunk, get it checked.</p><p>Related: <a href="services/strut-assembly-replacement.html">Suspension Repair</a></p></article>
      <article class="apx-card"><p class="apx-tag">Spring, after the thaw</p><h3>Underbody and brake check</h3><p>Salt residue and meltwater cause rust and stuck calipers. A spring inspection catches the small stuff before it becomes a bigger bill.</p><p>Related: <a href="services/preventative-maintenance.html">Preventative Maintenance</a></p></article>
      <article class="apx-card"><p class="apx-tag">Spring, before summer</p><h3>AC check</h3><p>An AC that was cold last August can be warm by June. A recharge plus a leak test early in the season beats a hot drive in July.</p><p>Related: <a href="services/ac-service-replacement.html">Air Conditioning Service</a></p></article>
      <article class="apx-card"><p class="apx-tag">Summer, city and highway</p><h3>Cooling system and fluid check</h3><p>Heat plus stop and go is when a marginal cooling system fails. Check the coolant level, the condition of the fluid, and the thermostat.</p><p>Related: <a href="services/coolant-flush.html">Coolant Flush</a></p></article>
    </div>
    <p class="apx-updated">Always defer to your owner's manual for service intervals and fluid specifications.</p>
  </div>
</section>

<section class="apx" id="how-we-compare" aria-labelledby="apx-compare-h">
  <div class="apx-wrap">
    <p class="apx-kicker">Why the order of operations matters</p>
    <h2 id="apx-compare-h">Diagnosis first versus parts swapping</h2>
    <p class="apx-lead">A code reader tells you which sensor complained, not why. Here is how the two approaches differ in practice.</p>
    <div class="apx-scroll">
      <table>
        <caption class="apx-updated" style="text-align:left;caption-side:bottom">General comparison of repair approaches, not a statement about any specific shop.</caption>
        <thead><tr><th scope="col">Step</th><th scope="col">Parts-swapping approach</th><th scope="col">Diagnosis-first approach (how Apex works)</th></tr></thead>
        <tbody>
          <tr><th scope="row">Where it starts</th><td>Replacing the part a code or a guess points to</td><td>Computer scan plus hands-on testing to confirm the actual fault</td></tr>
          <tr><th scope="row">The quote</th><td>A lump sum or a verbal figure</td><td>Written, with parts and labour broken out, approved by you first</td></tr>
          <tr><th scope="row">The old parts</th><td>Usually discarded</td><td>Saved for your inspection, with measurements in writing</td></tr>
          <tr><th scope="row">Proving the fix</th><td>The warning light is cleared</td><td>The repair is verified on a road test before you pay</td></tr>
          <tr><th scope="row">The outcome</th><td>Repeat visits when the guess was wrong</td><td>Fixed right the first time</td></tr>
        </tbody>
      </table>
    </div>
    <h3 style="margin-top:2rem">Six questions to ask any shop before you approve a repair</h3>
    <ol class="apx-checks">
      <li>What test confirmed this part is the cause?</li>
      <li>Can I have the quote in writing with parts and labour separate?</li>
      <li>Will you show me the old part and the measurement that failed?</li>
      <li>Will you call me before doing anything beyond the approved quote?</li>
      <li>How will you verify the repair worked?</li>
      <li>What happens if the problem comes back?</li>
    </ol>
  </div>
</section>

<section class="apx" id="faq" aria-labelledby="apx-faq-h">
  <div class="apx-wrap apx-faq">
    <p class="apx-kicker">Straight answers</p>
    <h2 id="apx-faq-h">Car servicing questions, answered</h2>
    <p class="apx-lead">Written the way people ask out loud, so a voice assistant or an AI answer can quote the first sentence cleanly.</p>
    <div>
      {home_faq_html()}
    </div>
    <div class="apx-cta">
      <a class="apx-btn" href="tel:{PHONE_E164}">Call {PHONE_DISP}</a>
      <a class="apx-btn apx-btn-ghost" href="faq.html">More questions</a>
    </div>
  </div>
</section>

<section class="apx apx-alt" id="all-services" aria-labelledby="apx-cluster-h">
  <div class="apx-wrap">
    <h2 id="apx-cluster-h">Every service we perform in North York</h2>
    <ul class="apx-chips">
      {chips}
    </ul>
  </div>
</section>
{castrol_section()}
"""


TRACKING_SCRIPT = """<script>
(function () {
  'use strict';
  var dl = window.dataLayer = window.dataLayer || [];
  function send(name, params) {
    params = params || {};
    if (typeof window.gtag === 'function') { window.gtag('event', name, params); }
    else { dl.push(Object.assign({ event: name }, params)); }
  }
  function where(el) {
    var s = el.closest('section[id], header, footer, nav');
    return s ? (s.id || s.tagName.toLowerCase()) : 'page';
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var h = a.getAttribute('href') || '';
    var p = { link_location: where(a) };
    if (h.indexOf('tel:') === 0) { p.phone = h.slice(4); send('click_to_call', p); }
    else if (h.indexOf('mailto:') === 0) { send('click_email', p); }
    else if (/google\\.com\\/maps|maps\\.apple\\.com|waze\\.com/.test(h)) {
      send(/writereview|review/i.test(h) ? 'click_review_link' : 'click_directions', p);
    }
    else if (/contact\\.html#booking/.test(h)) { send('click_book', p); }
    else if (/(^|\\/)services\\/[a-z-]+\\.html/.test(h)) { p.service = h.split('/').pop().replace('.html', ''); send('click_service', p); }
    else if (/(^|\\/)areas\\/[a-z-]+\\.html/.test(h)) { p.area = h.split('/').pop().replace('.html', ''); send('click_area', p); }
  }, { passive: true });
  document.addEventListener('toggle', function (e) {
    var d = e.target;
    if (d && d.tagName === 'DETAILS' && d.open && d.closest('.apx-faq')) {
      var s = d.querySelector('summary');
      send('faq_open', { question: s ? s.textContent.trim().slice(0, 100) : '' });
    }
  }, true);
  var marks = [50, 90], fired = {};
  window.addEventListener('scroll', function () {
    var h = document.documentElement;
    var pct = Math.round((h.scrollTop + window.innerHeight) / h.scrollHeight * 100);
    marks.forEach(function (m) { if (pct >= m && !fired[m]) { fired[m] = true; send('scroll_depth', { percent: m }); } });
  }, { passive: true });
})();
</script>"""


def robots_txt():
    return """# robots.txt for apexcollisioncenter.ca
# Goal: visible in classic search, maps data partners, and AI answer engines.

User-agent: *
Allow: /
Disallow: /cdn-cgi/

User-agent: Googlebot
Allow: /
User-agent: Bingbot
Allow: /
User-agent: Applebot
Allow: /
User-agent: DuckDuckBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Perplexity-User
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Claude-User
Allow: /

User-agent: GPTBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /

Sitemap: https://apexcollisioncenter.ca/sitemap.xml
"""


def llms_txt():
    lines = ["# Apex Collision Center", "",
        "> Independent auto repair, body shop and car servicing shop at Unit 41 & 42, 4544 Dufferin Street, "
        "Toronto (York University Heights, North York), Ontario M3H 5X2. Services all makes and models "
        "(domestic, Asian, European). Diagnosis first, written upfront quote with parts and labour broken out, "
        "worn parts saved for inspection, road test on every repair. Open Monday to Friday 9:00 AM to 5:00 PM, "
        "Saturday 10:00 AM to 3:00 PM, closed Sunday. Towing runs 24/7. Phone (416) 661-6665.", "",
        "Customers come from North York, Toronto, Downtown Toronto, Mississauga, Scarborough, Etobicoke, "
        "Vaughan and Markham. Free parking on site. Walk-ins welcome for inspections, diagnostics, oil changes "
        "and battery checks; larger repairs are best booked ahead.", "",
        "## Core pages",
        "- [Home](https://apexcollisioncenter.ca/): overview, fact sheet, FAQ",
        "- [Services](https://apexcollisioncenter.ca/services.html): all 22 services",
        "- [About](https://apexcollisioncenter.ca/about.html): the shop and the team",
        "- [Reviews](https://apexcollisioncenter.ca/reviews.html): customer reviews",
        "- [FAQ](https://apexcollisioncenter.ca/faq.html): common questions",
        "- [Contact and booking](https://apexcollisioncenter.ca/contact.html): phone, directions, online booking",
        "- [Areas we serve](https://apexcollisioncenter.ca/areas.html): city pages", "",
        "## Services"]
    for s in SERVICES:
        lines.append(f"- [{s['name']}](https://apexcollisioncenter.ca/services/{s['slug']}.html): {s['card']}")
    lines += ["", "## Areas"]
    for a in AREAS:
        lines.append(f"- [{a['city']}](https://apexcollisioncenter.ca/areas/{a['slug']}.html)")
    lines += ["", "## Key facts for answers",
        "- Business name: Apex Collision Center",
        "- Address: Unit 41 & 42, 4544 Dufferin Street, Toronto (York University Heights, North York), ON M3H 5X2, Canada",
        "- Coordinates: 43.7537, -79.4640",
        "- Phone: (416) 661-6665",
        "- Booking: https://apexcollisioncenter.ca/contact.html#booking",
        "- Pricing: no flat prices published; every repair is quoted in writing after diagnosis and approved by the customer before work begins.",
        ""]
    return "\n".join(lines)


def webmanifest():
    return json.dumps({
        "name": "Apex Collision Center",
        "short_name": "Apex Auto",
        "description": "Car servicing, body shop and auto repair in North York, Ontario. 24/7 towing.",
        "start_url": "/?utm_source=pwa",
        "scope": "/",
        "display": "standalone",
        "lang": "en-CA",
        "background_color": "#ffffff",
        "theme_color": "#0b1e3a",
        "icons": [
            {"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "/assets/img/icon-512-maskable.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
        "shortcuts": [
            {"name": "Call the shop", "url": "tel:+14166616665"},
            {"name": "24/7 towing", "url": "tel:+14166616665"},
            {"name": "Book service", "url": "/contact.html#booking"},
        ],
    }, indent=2) + "\n"

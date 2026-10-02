import os, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
PHONE = "786.417.2459"
TEL = "+17864172459"
PHONES = [("786.417.2459", "+17864172459"), ("786.417.3890", "+17864173890"), ("786.245.4545", "+17862454545")]
EMAIL = "keytoinsurance@hotmail.com"
ADDR = "2423 NW 97th Ave, Miami, FL 33172"
SITE = "https://www.thekeytoinsurance.com"

KEY = '<svg viewBox="0 0 48 48" fill="none" aria-hidden="true"><circle cx="16" cy="24" r="10" stroke="#e0a526" stroke-width="4"/><circle cx="16" cy="24" r="3" fill="#e0a526"/><path d="M26 24h18M38 24v8M32 24v6" stroke="#e0a526" stroke-width="4" stroke-linecap="round"/></svg>'
PHONE_ICO = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.6a1 1 0 0 1-.25 1z"/></svg>'

def ico(path):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'

ICONS = {
    "auto": ico('<path d="M5 16l1.5-5.2A2 2 0 0 1 8.4 9.4h7.2a2 2 0 0 1 1.9 1.4L19 16"/><path d="M3 16h18v3a1 1 0 0 1-1 1h-1.5a1 1 0 0 1-1-1v-1h-11v1a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><circle cx="7.5" cy="13.5" r=".6"/><circle cx="16.5" cy="13.5" r=".6"/>'),
    "home": ico('<path d="M3 11l9-7.5L21 11"/><path d="M5 9.5V20h14V9.5"/><path d="M10 20v-6h4v6"/>'),
    "flood": ico('<path d="M12 3c3 4 6 6.8 6 10.5a6 6 0 0 1-12 0C6 9.8 9 7 12 3z"/><path d="M9.5 14a2.5 2.5 0 0 0 2.5 2.5"/>'),
    "renters": ico('<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M9 21v-5h6v5"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2"/>'),
    "business": ico('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/><path d="M3 13h18"/>'),
    "life": ico('<path d="M12 21s-7.5-4.6-9.2-9.3C1.6 8.2 3.6 5 6.8 5c2 0 3.4 1 5.2 3 1.8-2 3.2-3 5.2-3 3.2 0 5.2 3.2 4 6.7C19.500 16.400 12 21 12 21z"/>'),
    "shield": ico('<path d="M12 3l8 3v6c0 4.500-3.300 8-8 9-4.700-1-8-4.500-8-9V6z"/><path d="M9 12l2.200 2.200L15.500 10"/>'),
    "people": ico('<circle cx="9" cy="8" r="3.500"/><path d="M2.500 20a6.500 6.500 0 0 1 13 0"/><path d="M16 4.500a3.500 3.500 0 0 1 0 7M18 14a6.500 6.500 0 0 1 3.500 6"/>'),
    "clock": ico('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
    "pin": ico('<path d="M12 21s7-6 7-11.500A7 7 0 0 0 5 9.500C5 15 12 21 12 21z"/><circle cx="12" cy="9.500" r="2.500"/>'),
}


LANG = "en"
def L(en, es):
    return es if LANG == "es" else en

KEYG = KEY.split(">", 1)[1].rsplit("</svg", 1)[0]

# Route table: key -> (english file, spanish file)
ROUTES = {
    "home": ("index.html", "index.html"),
    "auto": ("auto-insurance.html", "seguro-de-auto.html"),
    "homeins": ("home-insurance.html", "seguro-de-hogar.html"),
    "more": ("more-coverage.html", "mas-coberturas.html"),
    "about": ("about.html", "nosotros.html"),
    "contact": ("contact.html", "contacto.html"),
}
NAV_LABELS = {
    "home": ("Home", "Inicio"), "auto": ("Auto", "Auto"), "homeins": ("Home", "Hogar"),
    "more": ("More Coverage", "Más coberturas"), "about": ("About", "Nosotros"), "contact": ("Contact", "Contacto"),
}

def fname(key, lang=None):
    return ROUTES[key][1 if (lang or LANG) == "es" else 0]

def u(key, anchor=""):
    """Link from the current language's pages to another page in the same language."""
    return fname(key) + anchor

def assets():
    return "../assets/" if LANG == "es" else "assets/"

def alt_href(key):
    """Link to the same page in the other language."""
    if LANG == "en":
        return "es/" + fname(key, "es")
    return "../" + fname(key, "en")

def tel_btn(cls="btn btn-gold btn-lg", label=None):
    return f'<a class="{cls}" href="tel:{TEL}">{PHONE_ICO}{label or PHONE}</a>'

def shell(key, title, desc, body, schema=""):
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{fname(k)}"{cur if k == key else ""}>{L(*NAV_LABELS[k])}</a>' for k in ROUTES)
    en_url = f"{SITE}/" if key == "home" else f"{SITE}/{fname(key, 'en')}"
    es_url = f"{SITE}/es/" if key == "home" else f"{SITE}/es/{fname(key, 'es')}"
    canonical = es_url if LANG == "es" else en_url
    a = assets()
    toggle = (f'<a class="lang" href="{alt_href(key)}" hreflang="{"en" if LANG == "es" else "es"}" lang="{"en" if LANG == "es" else "es"}" '
              f'aria-label="{L("Ver en español", "View in English")}"><b>{"ES" if LANG == "es" else "EN"}</b> | {"EN" if LANG == "es" else "ES"}</a>')
    brand_svg = f'<svg viewBox="0 0 48 48"><rect width="48" height="48" rx="11" fill="#0c1f3a"/><g transform="translate(2 2) scale(.92)">{KEYG}</g></svg>'
    brand_svg2 = brand_svg.replace("#0c1f3a", "#14305a")
    cols_cov = [("auto", ""), ("homeins", ""), ("more", "#flood"), ("more", "#renters"), ("more", "#business"), ("more", "#life")]
    cov_names = [L("Auto Insurance", "Seguro de auto"), L("Home Insurance", "Seguro de hogar"), L("Flood", "Inundación"),
                 L("Renters", "Inquilinos"), L("Business", "Negocios"), L("Life", "Vida")]
    cov_links = "".join(f'<a href="{u(k, an)}">{n}</a>' for (k, an), n in zip(cols_cov, cov_names))
    return f'''<!DOCTYPE html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="es" href="{es_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{"es_US" if LANG == "es" else "en_US"}">
<meta name="theme-color" content="#0c1f3a">
<link rel="icon" href="{a}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{a}styles.css">
{schema}
</head>
<body>
<a class="skip" href="#main">{L("Skip to content", "Saltar al contenido")}</a>
<div class="topbar"><div class="wrap"><span>{ADDR}</span><span>{L("Call for a fast quote", "Llame para una cotización rápida")}: <a href="tel:{TEL}">{PHONE}</a></span></div></div>
<header class="site"><div class="wrap">
  <a class="brand" href="{fname("home")}" aria-label="The Key To Insurance, {L("home", "inicio")}">{brand_svg}<span><b>The Key To Insurance</b><small>Miami, Florida</small></span></a>
  <button class="menu-btn" aria-label="Menu" aria-expanded="false" aria-controls="nav"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
  <nav class="main" id="nav" aria-label="Main">{nav}{toggle}<a class="btn btn-gold" href="tel:{TEL}">{PHONE_ICO}{PHONE}</a></nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site"><div class="wrap">
  <div class="cols">
    <div><a class="brand" href="{fname("home")}">{brand_svg2}<span><b>The Key To Insurance</b><small>Miami, Florida</small></span></a>
      <p>{L("Local Miami agency helping families and business owners find the right coverage at a fair price.", "Agencia local de Miami que ayuda a familias y dueños de negocios a encontrar la cobertura correcta a un precio justo.")}</p></div>
    <div><h4>{L("Coverage", "Coberturas")}</h4>{cov_links}</div>
    <div><h4>{L("Company", "Empresa")}</h4><a href="{u("about")}">{L("About Us", "Nosotros")}</a><a href="{u("contact")}">{L("Contact", "Contacto")}</a><a href="{u("home", "#faq")}">{L("FAQ", "Preguntas frecuentes")}</a></div>
    <div><h4>{L("Get in touch", "Contáctenos")}</h4>{"".join(f'<a href="tel:{t}">{p}</a>' for p, t in PHONES)}<a href="mailto:{EMAIL}">{EMAIL}</a><span style="display:block;padding:4px 0">{ADDR}</span></div>
  </div>
  <div class="legal"><span>© 2026 The Key To Insurance. {L("All rights reserved.", "Todos los derechos reservados.")}</span><span>{L("Coverage, carriers and availability vary by policy and eligibility.", "La cobertura, las aseguradoras y la disponibilidad varían según la póliza y la elegibilidad.")}</span></div>
</div></footer>
<div class="callbar"><a class="c" href="tel:{TEL}">{L("Call now", "Llame ahora")}</a><a class="q" href="{u("contact", "#quote")}">{L("Get a quote", "Cotizar")}</a></div>
<script src="{a}script.js"></script>
</body>
</html>
'''

def form(default=""):
    opts = [("Auto", "Auto"), ("Home", "Hogar"), ("Flood", "Inundación"), ("Renters", "Inquilinos"),
            ("Business", "Negocios"), ("Life", "Vida"), ("Not sure yet", "No estoy seguro/a")]
    o = "".join(f'<option>{L(en, es)}</option>' for en, es in opts)
    opt = L("optional", "opcional")
    return f'''<form class="quote" id="quote-form">
  <div class="row"><div class="field"><label for="name">{L("Full name", "Nombre completo")}</label><input id="name" name="name" autocomplete="name" required></div>
  <div class="field"><label for="phone">{L("Phone", "Teléfono")}</label><input id="phone" name="phone" type="tel" autocomplete="tel" required></div></div>
  <div class="row"><div class="field"><label for="email">Email <span style="font-weight:400;color:var(--muted)">({opt})</span></label><input id="email" name="email" type="email" autocomplete="email"></div>
  <div class="field"><label for="coverage">{L("What do you need?", "¿Qué necesita?")}</label><select id="coverage" name="coverage">{o}</select></div></div>
  <div class="field"><label for="notes">{L("Anything we should know?", "¿Algo que debamos saber?")}</label><textarea id="notes" name="notes" placeholder="{L("Current carrier, renewal date, number of drivers, property address...", "Aseguradora actual, fecha de renovación, número de conductores, dirección de la propiedad...")}"></textarea></div>
  <input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
  <button class="btn btn-navy btn-lg" type="submit">{L("Request my quote", "Solicitar mi cotización")}</button>
  <p class="form-msg" role="status"></p>
  <p style="font-size:.88rem;color:var(--muted);margin:0">{L("Prefer to talk? Call", "¿Prefiere hablar? Llame al")} <a href="tel:{TEL}">{PHONE}</a>. {L("We'll never sell your information.", "Nunca venderemos su información.")}</p>
</form>'''

def cta(h=None):
    h = h or L("Ready for a quote? Just call.", "¿Listo para una cotización? Solo llame.")
    return f'''<section class="cta"><div class="wrap">
  <h2>{h}</h2><p class="lede" style="margin-inline:auto">{L("A real person answers, asks a few questions, and gets you options from our carriers.", "Una persona real le contesta, le hace algunas preguntas y le consigue opciones de nuestras aseguradoras.")}</p>
  <div class="hero-actions">{tel_btn(label=L("Call ", "Llame al ") + PHONE)}<a class="btn btn-ghost btn-lg" href="{u("contact", "#quote")}">{L("Request a call back", "Pida que le llamemos")}</a></div>
</div></section>'''

def testimonial_data():
    return [
        (L("I’ve been with this agency for years and they’ve always taken care of me. When I got into a car accident, I was nervous about the claims process, but they walked me through everything and made sure I was covered. It really felt like they had my back.",
           "Llevo años con esta agencia y siempre me han cuidado. Cuando tuve un accidente de auto, me daba nervios el proceso del reclamo, pero me guiaron en todo y se aseguraron de que estuviera cubierta. De verdad sentí que me respaldaban."),
         "Jenny Tome", L("Auto insurance client", "Clienta de seguro de auto")),
        (L("When we bought our first home, I had no idea what kind of coverage we needed. They explained it in a way that actually made sense and helped us find something affordable. We ended up moving our car insurance here too because the service has always been solid.",
           "Cuando compramos nuestra primera casa, no sabía qué cobertura necesitábamos. Nos lo explicaron de una forma que sí tenía sentido y nos ayudaron a encontrar algo accesible. Terminamos pasando también el seguro del carro aquí porque el servicio siempre ha sido excelente."),
         "Genevie Jacomino", L("Home insurance client", "Clienta de seguro de hogar")),
        (L("Running a small business, I don’t have time to deal with complicated insurance stuff. They set me up with a policy that fit my shop and anytime I need help, I get an answer right away. It’s nice knowing I can call and talk to a real person who knows me.",
           "Con un negocio pequeño, no tengo tiempo para lidiar con cosas complicadas de seguros. Me consiguieron una póliza que le queda bien a mi negocio y cada vez que necesito ayuda, recibo respuesta enseguida. Es bueno saber que puedo llamar y hablar con una persona real que me conoce."),
         "Andy Gonzalez", L("Business insurance client", "Cliente de seguro comercial")),
    ]

def testimonials(idx=(0, 1, 2)):
    data = testimonial_data()
    cards = "".join(f'''<figure class="card" style="margin:0">
  <div aria-label="{L("5 out of 5 stars", "5 de 5 estrellas")}" style="color:var(--gold);letter-spacing:3px;font-size:1.1rem;margin-bottom:12px">★★★★★</div>
  <blockquote style="margin:0;flex:1;font-size:1.02rem">“{html.escape(data[i][0])}”</blockquote>
  <figcaption style="margin-top:20px;font-weight:600;color:var(--navy)">{data[i][1]}<br><span style="font-weight:400;color:var(--muted);font-size:.9rem">{data[i][2]}</span></figcaption></figure>''' for i in idx)
    note = L("", '<p style="text-align:center;color:var(--muted);font-size:.85rem;margin:18px 0 0">Testimonios traducidos de su versión original en inglés.</p>')
    return f'<div class="cards">{cards}</div>{note}'

def faq(items):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)

CARRIER_LIST = ["Progressive", "Geico", "Bristol West", "Universal", "Citizens", "Ascendant", "Granada"]

def owner(show_checks=True):
    extra = f'''<ul class="checks">
      <li><b>{L("Independent.", "Independientes.")}</b> {L("We work for you, not one insurance company.", "Trabajamos para usted, no para una sola aseguradora.")}</li>
      <li><b>{L("Plain English.", "Español claro.")}</b> {L("No jargon, no pressure, no surprises at renewal.", "Sin jerga, sin presión y sin sorpresas en la renovación.")}</li>
      <li><b>{L("There when it counts.", "Presentes cuando importa.")}</b> {L("We help you through the claims process.", "Le ayudamos durante el proceso de reclamo.")}</li>
    </ul>''' if show_checks else ""
    return f'''<div class="owner">
  <figure class="owner-photo"><span class="initials" aria-hidden="true">AL</span><img src="{assets()}agatha-landaetta.jpg" alt="Agatha Landaetta, {L("owner of", "dueña de")} The Key To Insurance" loading="lazy" onerror="this.remove()"></figure>
  <div><span class="eyebrow">{L("Meet the owner", "Conozca a la dueña")}</span><h2>Agatha Landaetta</h2>
  <p class="lede">{L("Local, bilingual, and focused on simplifying insurance for Miami families and businesses. Agatha and our team compare multiple carriers to get you the right coverage and price.", "Local, bilingüe y enfocada en simplificar los seguros para las familias y los negocios de Miami. Agatha y nuestro equipo comparan varias aseguradoras para conseguirle la cobertura y el precio correctos.")}</p>
  {extra}{tel_btn("btn btn-navy", L("Call ", "Llame al ") + PHONE)}</div>
</div>'''

def stats():
    items = [("15+", L("Years serving Miami", "Años sirviendo a Miami")), (str(len(CARRIER_LIST)), L("Insurance carriers", "Aseguradoras")), ("24/7", L("Claims support", "Ayuda con reclamos"))]
    cells = "".join(f'<div><b>{n}</b><span>{l}</span></div>' for n, l in items)
    return f'<section class="stats" aria-label="{L("By the numbers", "En cifras")}"><div class="wrap">{cells}</div></section>'

def carrier_grid():
    tiles = "".join(f"<div>{c}</div>" for c in CARRIER_LIST) + f'<div class="more-tile">{L("Ask us about others", "Pregunte por otras")}</div>'
    return f'''<section class="block"><div class="wrap">
  <div class="head center"><span class="eyebrow">{L("Our carriers", "Nuestras aseguradoras")}</span><h2>{L("Top Florida insurers, one phone call.", "Las mejores aseguradoras de Florida, en una llamada.")}</h2>
  <p class="lede">{L("We work with trusted insurance companies to find you the best coverage at the best price.", "Trabajamos con aseguradoras de confianza para encontrarle la mejor cobertura al mejor precio.")}</p></div>
  <div class="tiles">{tiles}</div>
</div></section>'''

def carriers_pills(names):
    return '<div class="carriers">' + "".join(f"<span>{n}</span>" for n in names) + "</div>"

def write(name, content):
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

def pagehead(eyebrow, h1, lede="", actions=True):
    act = f'<div class="hero-actions">{tel_btn(label=L("Call ", "Llame al ") + PHONE)}<a class="btn btn-ghost btn-lg" href="{u("contact", "#quote")}">{L("Request a call back", "Pida que le llamemos")}</a></div>' if actions else ""
    lede_html = f'<p class="lede">{lede}</p>' if lede else ""
    return f'<section class="pagehead"><div class="wrap"><span class="eyebrow" style="color:var(--gold)">{eyebrow}</span><h1>{h1}</h1>{lede_html}{act}</div></section>'

def build(lang):
    global LANG
    LANG = lang
    pre = "es/" if lang == "es" else ""
    CALL = L("Call ", "Llame al ") + PHONE

    # ---------- HOME ----------
    HOME_FAQ = [
        (L("How fast can I get a quote?", "¿Qué tan rápido puedo recibir una cotización?"),
         L(f"Usually the same day, often while you’re on the phone. Call <a href='tel:{TEL}'>{PHONE}</a> and have your driver’s license, vehicle details or property address handy.",
           f"Normalmente el mismo día, muchas veces mientras habla por teléfono. Llame al <a href='tel:{TEL}'>{PHONE}</a> y tenga a mano su licencia de conducir, los datos del vehículo o la dirección de la propiedad.")),
        (L("Do you work with more than one insurance company?", "¿Trabajan con más de una aseguradora?"),
         L("Yes. As an independent agency we shop multiple carriers, including Progressive, Geico, Universal and Citizens, so you aren’t locked into one company’s price.",
           "Sí. Como agencia independiente comparamos varias aseguradoras, entre ellas Progressive, Geico, Universal y Citizens, para que no dependa del precio de una sola compañía.")),
        (L("Can you help if I’ve had accidents or tickets?", "¿Pueden ayudarme si he tenido accidentes o multas?"),
         L("Often, yes. Our carrier mix includes options for a range of driving records. Call us and we’ll tell you honestly what’s available.",
           "Muchas veces, sí. Nuestras aseguradoras incluyen opciones para distintos historiales de manejo. Llámenos y le diremos con honestidad qué hay disponible.")),
        (L("What does homeowners insurance cost in Florida?", "¿Cuánto cuesta el seguro de hogar en Florida?"),
         L("It varies a lot by roof age, construction, location and coverage. We’ll quote it side by side across carriers so you can see the real tradeoffs.",
           "Varía mucho según la edad del techo, la construcción, la ubicación y la cobertura. Le cotizamos varias aseguradoras lado a lado para que vea las diferencias reales.")),
        (L("Do I need flood insurance?", "¿Necesito seguro contra inundaciones?"),
         L(f"Standard homeowners policies don’t cover flood damage. In South Florida it’s worth a serious look whether or not your lender requires it. See our <a href='{u('more', '#flood')}'>flood coverage page</a>.",
           f"Las pólizas de hogar estándar no cubren daños por inundación. En el sur de Florida vale la pena considerarlo, lo exija o no su prestamista. Vea nuestra <a href='{u('more', '#flood')}'>página de cobertura contra inundaciones</a>.")),
        (L("What if I need to file a claim?", "¿Qué hago si necesito presentar un reclamo?"),
         L("Call us first. We’ll help you start the claim, explain what to expect, and follow up so it doesn’t fall through the cracks.",
           "Llámenos primero. Le ayudamos a iniciar el reclamo, le explicamos qué esperar y le damos seguimiento para que nada se pierda.")),
    ]
    schema = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"InsuranceAgency","name":"The Key To Insurance","url":"{SITE}/","telephone":"+1-786-417-2459","email":"{EMAIL}","knowsLanguage":["en","es"],"address":{{"@type":"PostalAddress","streetAddress":"2423 NW 97th Ave","addressLocality":"Miami","addressRegion":"FL","postalCode":"33172","addressCountry":"US"}},"areaServed":"Miami-Dade County, FL"}}</script>'''

    lines = [
        ("auto", L("Auto Insurance", "Seguro de auto"), L("Florida-required coverage and full protection, quoted across multiple carriers.", "Cobertura exigida en Florida y protección completa, cotizada con varias aseguradoras."), u("auto")),
        ("home", L("Home Insurance", "Seguro de hogar"), L("Protect your house, belongings and liability against hurricanes, fire and more.", "Proteja su casa, sus pertenencias y su responsabilidad ante huracanes, incendios y más."), u("homeins")),
        ("flood", L("Flood Insurance", "Seguro contra inundaciones"), L("Homeowners policies exclude flood. Close that gap before the next storm.", "Las pólizas de hogar excluyen las inundaciones. Cierre esa brecha antes de la próxima tormenta."), u("more", "#flood")),
        ("renters", L("Renters Insurance", "Seguro para inquilinos"), L("Affordable protection for your belongings and liability.", "Protección accesible para sus pertenencias y su responsabilidad."), u("more", "#renters")),
        ("business", L("Business Insurance", "Seguro comercial"), L("Coverage for shops, offices and contractors that fits how you actually operate.", "Cobertura para tiendas, oficinas y contratistas, adaptada a cómo opera realmente su negocio."), u("more", "#business")),
        ("life", L("Life Insurance", "Seguro de vida"), L("Peace of mind that your family is taken care of.", "La tranquilidad de saber que su familia está protegida."), u("more", "#life")),
    ]
    more = L("Learn more", "Más información")
    cards = "".join(f'<a class="card" href="{url}"><div class="ico">{ICONS[k]}</div><h3>{t}</h3><p>{d}</p><span class="more">{more}</span></a>' for k, t, d, url in lines)

    home_body = f'''
<section class="hero"><div class="wrap hero-grid">
  <div>
    <span class="eyebrow" style="color:var(--gold)">{L("Independent insurance agency · Miami", "Agencia de seguros independiente · Miami")}</span>
    <h1>{L("Insurance, handled by people who <em>pick up the phone.</em>", "Seguros atendidos por personas que <em>contestan el teléfono.</em>")}</h1>
    <p class="lede">{L("Auto, home, flood, business and more. We shop the carriers for you and explain your coverage in plain English.", "Auto, hogar, inundación, negocios y más. Comparamos las aseguradoras por usted y le explicamos su cobertura en español claro.")}</p>
    <div class="hero-actions">{tel_btn(label=CALL)}<a class="btn btn-ghost btn-lg" href="{u("contact", "#quote")}">{L("Request a call back", "Pida que le llamemos")}</a></div>
    <p class="hero-note">{L("Same-day quotes on most auto and home policies.", "Cotizaciones el mismo día en la mayoría de pólizas de auto y hogar.")}</p>
  </div>
  <aside class="callcard" aria-label="{L("Phone numbers", "Teléfonos")}">
    <h2>{L("Talk to us now", "Hable con nosotros ahora")}</h2><p style="color:var(--muted)">{L("Tap a number to call.", "Toque un número para llamar.")}</p>
    {"".join(f'<a class="num" href="tel:{t}"><small>{L("Main line", "Línea principal") if i == 0 else L("Alternate line", "Línea alterna")}</small>{p}</a>' for i, (p, t) in enumerate(PHONES))}
  </aside>
</div></section>

<div class="trust"><div class="wrap"><ul>
  <li>{ICONS["people"]}{L("Real people, no phone trees", "Personas reales, sin menús automáticos")}</li>
  <li>{ICONS["shield"]}{L("Multiple top carriers", "Varias aseguradoras de primer nivel")}</li>
  <li>{ICONS["clock"]}{L("Fast, same-day quotes", "Cotizaciones rápidas, el mismo día")}</li>
  <li>{ICONS["pin"]}{L("Local to Miami-Dade", "Local de Miami-Dade")}</li>
</ul></div></div>

<section class="block"><div class="wrap">
  <div class="head"><span class="eyebrow">{L("What we cover", "Qué cubrimos")}</span><h2>{L("The right coverage for the way you live.", "La cobertura correcta para su manera de vivir.")}</h2><p class="lede">{L("Start with auto and home, or protect everything under one roof with one agent who knows you.", "Comience con auto y hogar, o proteja todo bajo un mismo techo con una agente que lo conoce.")}</p></div>
  <div class="cards">{cards}</div>
</div></section>

<section class="block alt"><div class="wrap">
  <div class="head center"><span class="eyebrow">{L("How it works", "Cómo funciona")}</span><h2>{L("Three steps, usually one phone call.", "Tres pasos, normalmente una sola llamada.")}</h2></div>
  <div class="steps">
    <div class="step"><h3>{L("Tell us what you need", "Díganos qué necesita")}</h3><p>{L("A few quick questions about your car, home or business.", "Unas preguntas rápidas sobre su carro, su casa o su negocio.")}</p></div>
    <div class="step"><h3>{L("We compare carriers", "Comparamos aseguradoras")}</h3><p>{L("We shop our carriers so you see real options, not just one price.", "Consultamos nuestras aseguradoras para que vea opciones reales, no solo un precio.")}</p></div>
    <div class="step"><h3>{L("You choose and you’re covered", "Usted elige y queda cubierto")}</h3><p>{L("We explain the differences, you pick, and we handle the paperwork.", "Le explicamos las diferencias, usted decide y nosotros nos encargamos del papeleo.")}</p></div>
  </div>
</div></section>

<section class="block"><div class="wrap">{owner()}</div></section>

{stats()}

{carrier_grid()}

<section class="block alt"><div class="wrap">
  <div class="head center"><span class="eyebrow">{L("Client stories", "Opiniones de clientes")}</span><h2>{L("Why our clients stay.", "Por qué nuestros clientes se quedan.")}</h2></div>
  {testimonials()}
</div></section>

<section class="block" id="faq"><div class="wrap" style="max-width:820px">
  <div class="head center"><span class="eyebrow">{L("FAQ", "Preguntas frecuentes")}</span><h2>{L("Quick answers.", "Respuestas rápidas.")}</h2></div>
  {faq(HOME_FAQ)}
</div></section>
{cta()}
'''
    write(pre + fname("home"), shell("home",
          L("The Key To Insurance | Auto & Home Insurance in Miami, FL", "The Key To Insurance | Seguro de auto y hogar en Miami, FL"),
          L("Independent Miami insurance agency. Fast quotes on auto, home, flood, renters, business and life insurance. Call 786.417.2459.",
            "Agencia de seguros independiente en Miami. Cotizaciones rápidas de auto, hogar, inundación, inquilinos, negocios y vida. Llame al 786.417.2459."),
          home_body, schema))

    # ---------- AUTO ----------
    auto_faq = [
        (L("What auto insurance does Florida require?", "¿Qué seguro de auto exige Florida?"),
         L("Florida requires Personal Injury Protection (PIP) and Property Damage Liability. Most drivers want more, such as bodily injury liability, uninsured motorist and collision/comprehensive. We’ll walk through what makes sense for you.",
           "Florida exige Protección contra Lesiones Personales (PIP) y Responsabilidad por Daños a la Propiedad. La mayoría de los conductores quiere más, como responsabilidad por lesiones corporales, conductor sin seguro y cobertura de colisión e integral. Le explicamos qué le conviene.")),
        (L("Can I get coverage with a poor driving record?", "¿Puedo conseguir seguro con mal historial de manejo?"),
         L("Frequently. Carriers like Progressive, Geico and Bristol West serve a wide range of drivers. Call us for an honest read on your options.",
           "Con frecuencia, sí. Aseguradoras como Progressive, Geico y Bristol West atienden a una amplia variedad de conductores. Llámenos y le daremos una opinión honesta de sus opciones.")),
        (L("What do I need to get a quote?", "¿Qué necesito para recibir una cotización?"),
         L("Driver’s license number, vehicle year/make/model (or VIN), and your current policy info if you have it. A phone call is usually all it takes.",
           "Su número de licencia de conducir, el año, la marca y el modelo del vehículo (o el VIN) y los datos de su póliza actual, si tiene una. Normalmente basta con una llamada.")),
        (L("Can I pay monthly?", "¿Puedo pagar mensualmente?"),
         L("Most carriers offer several payment plans. We’ll show you the down payment and monthly cost for each option.",
           "La mayoría de las aseguradoras ofrece varios planes de pago. Le mostramos el pago inicial y el costo mensual de cada opción.")),
    ]
    bullets = lambda items: "".join(f"<li><b>{b}</b> {t}</li>" for b, t in items)
    auto_body = f'''
{pagehead(L("Auto insurance", "Seguro de auto"), L("Car insurance in Miami, shopped for you.", "Seguro de auto en Miami, comparado para usted."), L("One call, several carriers. Find coverage that fits your budget and your driving record.", "Una llamada, varias aseguradoras. Encuentre una cobertura que se ajuste a su presupuesto y a su historial de manejo."))}
<section class="block"><div class="wrap split">
  <div><h2>{L("Coverage options", "Opciones de cobertura")}</h2>
    <ul class="checks">{bullets([
        (L("Liability and PIP.", "Responsabilidad civil y PIP."), L("Florida’s required minimums, quoted at the best price.", "Los mínimos que exige Florida, al mejor precio.")),
        (L("Bodily injury liability.", "Lesiones corporales."), L("Higher limits to protect your savings.", "Límites más altos para proteger sus ahorros.")),
        (L("Collision and comprehensive.", "Colisión e integral."), L("Repairs after accidents, theft, flooding and storms.", "Reparaciones tras accidentes, robo, inundaciones y tormentas.")),
        (L("Uninsured motorist.", "Conductor sin seguro."), L("Protection from drivers with no coverage.", "Protección contra conductores sin cobertura.")),
        (L("Rental and roadside.", "Auto de alquiler y asistencia en carretera."), L("Add-ons that save you on bad days.", "Extras que le salvan en los días malos.")),
    ])}</ul></div>
  <div class="panel"><h3>{L("Our auto carriers", "Nuestras aseguradoras de auto")}</h3><p>{L("We compare quotes from:", "Comparamos cotizaciones de:")}</p>
    {carriers_pills(["Progressive", "Geico", "Bristol West"])}</div>
</div></section>
<section class="block alt"><div class="wrap">
  <div class="head"><span class="eyebrow">{L("Ways to save", "Cómo ahorrar")}</span><h2>{L("Lower your premium without cutting corners.", "Pague menos sin recortar protección.")}</h2></div>
  <div class="cards">
    <div class="card"><h3>{L("Bundle with home", "Combine con su hogar")}</h3><p>{L("Combining auto and home with one agent can unlock multi-policy savings.", "Combinar auto y hogar con una misma agente puede darle descuentos por varias pólizas.")}</p></div>
    <div class="card"><h3>{L("Review every renewal", "Revise cada renovación")}</h3><p>{L("Rates change. We re-shop your policy so loyalty never costs you.", "Las tarifas cambian. Volvemos a comparar su póliza para que la lealtad nunca le cueste.")}</p></div>
    <div class="card"><h3>{L("Right-size your deductible", "Ajuste su deducible")}</h3><p>{L("We’ll show how different deductibles change your price so you can choose.", "Le mostramos cómo cambia el precio con distintos deducibles para que usted elija.")}</p></div>
  </div>
</div></section>
<section class="block"><div class="wrap" style="max-width:820px"><div class="head center"><h2>{L("Auto insurance FAQ", "Preguntas sobre seguro de auto")}</h2></div>{faq(auto_faq)}</div></section>
{cta(L("Get your auto quote today.", "Pida hoy su cotización de auto."))}
'''
    write(pre + fname("auto"), shell("auto",
          L("Auto Insurance in Miami, FL | The Key To Insurance", "Seguro de auto en Miami, FL | The Key To Insurance"),
          L("Compare auto insurance from Progressive, Geico and Bristol West. Fast quotes from a local Miami agency. Call 786.417.2459.",
            "Compare seguros de auto de Progressive, Geico y Bristol West. Cotizaciones rápidas de una agencia local de Miami. Llame al 786.417.2459."), auto_body))

    # ---------- HOME INSURANCE ----------
    home_faq2 = [
        (L("What does homeowners insurance cover?", "¿Qué cubre el seguro de hogar?"),
         L("Typically your dwelling, other structures, personal belongings, loss of use and personal liability. Wind and hurricane coverage often comes with a separate deductible in Florida.",
           "Normalmente la vivienda, otras estructuras, sus pertenencias, gastos de vivienda temporal y responsabilidad civil. En Florida, la cobertura de viento y huracán suele tener un deducible aparte.")),
        (L("Does my policy cover flood?", "¿Mi póliza cubre inundaciones?"),
         L("No. Flood is excluded from standard homeowners policies and needs its own coverage. We can quote that too.",
           "No. Las inundaciones están excluidas de las pólizas de hogar estándar y necesitan su propia cobertura. También se la cotizamos.")),
        (L("Does roof age matter?", "¿Importa la edad del techo?"),
         L("Yes. Many Florida carriers look closely at roof age and condition. Tell us about yours up front so we can match you with the right carrier.",
           "Sí. Muchas aseguradoras de Florida revisan con cuidado la edad y el estado del techo. Cuéntenos del suyo desde el principio para encontrar la aseguradora adecuada.")),
        (L("My mortgage lender needs proof of insurance. Can you help?", "Mi prestamista hipotecario necesita prueba de seguro. ¿Pueden ayudarme?"),
         L("Yes. We provide evidence of insurance to your lender and can update it if your mortgage company changes.",
           "Sí. Le enviamos la prueba de seguro a su prestamista y la actualizamos si cambia su compañía hipotecaria.")),
    ]
    home_ins_body = f'''
{pagehead(L("Home insurance", "Seguro de hogar"), L("Protect your home, hurricane season and beyond.", "Proteja su hogar en temporada de huracanes y más allá."), L("Florida homeowners coverage explained clearly, and shopped across carriers so you get a fair price.", "Seguro de hogar en Florida explicado con claridad y comparado entre aseguradoras para que obtenga un precio justo."))}
<section class="block"><div class="wrap split">
  <div><h2>{L("What a good policy includes", "Qué incluye una buena póliza")}</h2>
    <ul class="checks">{bullets([
        (L("Dwelling coverage.", "Cobertura de la vivienda."), L("Rebuild your home after fire, wind or other covered loss.", "Reconstruya su casa tras un incendio, viento u otra pérdida cubierta.")),
        (L("Personal property.", "Pertenencias personales."), L("Furniture, electronics, clothing and more.", "Muebles, electrónicos, ropa y más.")),
        (L("Liability.", "Responsabilidad civil."), L("Protection if someone is injured on your property.", "Protección si alguien se lesiona en su propiedad.")),
        (L("Loss of use.", "Gastos de vivienda temporal."), L("Living expenses if you can’t stay home during repairs.", "Gastos de vida si no puede quedarse en casa durante las reparaciones.")),
        (L("Hurricane and wind.", "Huracán y viento."), L("Understand your separate hurricane deductible before you need it.", "Entienda su deducible de huracán antes de necesitarlo.")),
    ])}</ul></div>
  <div class="panel"><h3>{L("Our homeowners carriers", "Nuestras aseguradoras de hogar")}</h3><p>{L("We compare quotes from:", "Comparamos cotizaciones de:")}</p>
    {carriers_pills(["Universal", "Citizens", "Ascendant", "Granada"])}
    <p style="margin-top:20px;margin-bottom:0">{L("Need flood too?", "¿Necesita también inundación?")} <a href="{u("more", "#flood")}" style="color:var(--gold)">{L("See flood coverage →", "Vea la cobertura contra inundaciones →")}</a></p></div>
</div></section>
<section class="block alt"><div class="wrap">
  <div class="head center"><span class="eyebrow">{L("A client story", "Opinión de una clienta")}</span><h2>{L("First home? We’ll make it make sense.", "¿Su primera casa? Haremos que todo tenga sentido.")}</h2></div>
  <div style="max-width:720px;margin:auto">{testimonials((1,))}</div>
</div></section>
<section class="block"><div class="wrap" style="max-width:820px"><div class="head center"><h2>{L("Home insurance FAQ", "Preguntas sobre seguro de hogar")}</h2></div>{faq(home_faq2)}</div></section>
{cta(L("Get your home quote today.", "Pida hoy su cotización de hogar."))}
'''
    write(pre + fname("homeins"), shell("homeins",
          L("Home Insurance in Miami, FL | The Key To Insurance", "Seguro de hogar en Miami, FL | The Key To Insurance"),
          L("Homeowners insurance in Miami from Universal, Citizens, Ascendant and Granada, explained in plain English. Call 786.417.2459 for a quote.",
            "Seguro de hogar en Miami de Universal, Citizens, Ascendant y Granada, explicado con claridad. Llame al 786.417.2459 para una cotización."), home_ins_body))

    # ---------- MORE COVERAGE ----------
    def line(id_, k, title, text, bl, ask):
        li = "".join(f"<li>{b}</li>" for b in bl)
        alt = " alt" if id_ in ("renters", "life") else ""
        return f'''<section class="block{alt}" id="{id_}"><div class="wrap split">
  <div><div class="card" style="width:64px;height:64px;padding:0;align-items:center;justify-content:center;margin-bottom:18px;background:var(--navy);color:var(--gold)"><div style="width:30px;height:30px">{ICONS[k]}</div></div>
  <h2>{title}</h2><p class="lede">{text}</p>{tel_btn("btn btn-navy", ask)}</div>
  <div><ul class="checks">{li}</ul></div></div></section>'''

    more_body = f'''
{pagehead(L("More coverage", "Más coberturas"), L("Everything else worth protecting.", "Todo lo demás que vale la pena proteger."), L("Beyond auto and home, we can help with flood, renters, business and life insurance. Call and ask.", "Además de auto y hogar, le ayudamos con seguros de inundación, inquilinos, negocios y vida. Llame y pregunte."), actions=False)}
{line("flood", "flood", L("Flood Insurance", "Seguro contra inundaciones"),
      L("Homeowners policies don’t cover flood. In South Florida, a few inches of water can mean tens of thousands in damage.", "Las pólizas de hogar no cubren inundaciones. En el sur de Florida, unas pocas pulgadas de agua pueden significar decenas de miles de dólares en daños."),
      [L("Covers damage from rising water, storm surge and heavy rain", "Cubre daños por crecida de agua, marejada ciclónica y lluvias fuertes"),
       L("Often required by lenders in flood zones, and smart outside them too", "Con frecuencia lo exigen los prestamistas en zonas de inundación, y también es buena idea fuera de ellas"),
       L("Coverage for the structure and, optionally, your belongings", "Cobertura para la estructura y, opcionalmente, sus pertenencias"),
       L("Typically has a waiting period, so don’t wait for a storm warning", "Normalmente tiene un período de espera, así que no espere a una alerta de tormenta")],
      L("Ask about flood coverage", "Pregunte por inundaciones"))}
{line("renters", "renters", L("Renters Insurance", "Seguro para inquilinos"),
      L("Your landlord’s policy covers the building, not your stuff. Renters insurance is inexpensive and protects what you own.", "La póliza del dueño del edificio cubre la estructura, no sus cosas. El seguro para inquilinos es económico y protege lo que usted tiene."),
      [L("Personal property protection for theft, fire and covered damage", "Protección de sus pertenencias contra robo, incendio y daños cubiertos"),
       L("Liability coverage if a guest is injured or you damage someone else’s property", "Responsabilidad civil si un invitado se lesiona o usted daña propiedad ajena"),
       L("Additional living expenses if you’re displaced", "Gastos adicionales de vivienda si tiene que mudarse temporalmente"),
       L("Often required by apartment leases", "Con frecuencia lo exigen los contratos de alquiler")],
      L("Ask about renters coverage", "Pregunte por seguro de inquilinos"))}
{line("business", "business", L("Business Insurance", "Seguro comercial"),
      L("From shops and offices to contractors, we help match coverage to how your business really works.", "Desde tiendas y oficinas hasta contratistas, adaptamos la cobertura a cómo funciona realmente su negocio."),
      [L("General liability and property coverage", "Responsabilidad civil general y cobertura de propiedad"),
       L("Coverage tailored to your type of operation", "Cobertura adaptada a su tipo de operación"),
       L("Help with certificates of insurance for clients and landlords", "Ayuda con certificados de seguro para clientes y arrendadores"),
       L("A real person to call when something comes up", "Una persona real a quien llamar cuando surja algo")],
      L("Ask about business coverage", "Pregunte por seguro comercial"))}
{line("life", "life", L("Life Insurance", "Seguro de vida"),
      L("Make sure the people who depend on you are financially protected.", "Asegúrese de que las personas que dependen de usted estén protegidas financieramente."),
      [L("Term and permanent options explained clearly", "Opciones temporales y permanentes explicadas con claridad"),
       L("Coverage to protect income, mortgage and family needs", "Cobertura para proteger ingresos, hipoteca y necesidades familiares"),
       L("A no-pressure conversation about what level makes sense", "Una conversación sin presión sobre cuánta cobertura tiene sentido")],
      L("Ask about life coverage", "Pregunte por seguro de vida"))}
<section class="block alt"><div class="wrap"><div class="head center"><span class="eyebrow">{L("A client story", "Opinión de un cliente")}</span><h2>{L("Business owners count on us too.", "Los dueños de negocios también cuentan con nosotros.")}</h2></div>
<div style="max-width:720px;margin:auto">{testimonials((2,))}</div></div></section>
{cta(L("Not sure what you need? Let’s talk.", "¿No sabe qué necesita? Hablemos."))}
'''
    write(pre + fname("more"), shell("more",
          L("Flood, Renters, Business & Life Insurance | The Key To Insurance", "Seguro de inundación, inquilinos, comercial y vida | The Key To Insurance"),
          L("Flood, renters, business and life insurance from a local Miami independent agency. Call 786.417.2459.",
            "Seguros de inundación, inquilinos, comercial y de vida de una agencia independiente local de Miami. Llame al 786.417.2459."), more_body))

    # ---------- ABOUT ----------
    cards3 = [("people", L("People first", "Las personas primero"), L("Phone answered, questions welcomed, no pressure.", "Contestamos el teléfono, bienvenimos las preguntas y nunca presionamos.")),
              ("shield", L("Honest advice", "Consejo honesto"), L("We tell you what you need, and what you don’t.", "Le decimos lo que necesita y lo que no.")),
              ("clock", L("Fast and responsive", "Rápidos y atentos"), L("Quick quotes, quick answers, and real help when you file a claim.", "Cotizaciones rápidas, respuestas rápidas y ayuda real cuando presenta un reclamo."))]
    about_body = f'''
{pagehead(L("About us", "Nosotros"), L("Your neighborhood agency in Miami.", "Su agencia de barrio en Miami."), L("We started The Key To Insurance so people could talk to someone who knows them, not a call center.", "Fundamos The Key To Insurance para que las personas hablen con alguien que las conoce, no con un centro de llamadas."), actions=False)}
<section class="block"><div class="wrap split">
  <div><h2>{L("The idea is simple.", "La idea es sencilla.")}</h2>
    <p>{L("Insurance is confusing, and the stakes are high. Our job is to make it clear: figure out what you actually need, shop our carriers, and explain the options honestly.", "Los seguros son confusos y lo que está en juego es mucho. Nuestro trabajo es aclararlos: entender lo que realmente necesita, consultar nuestras aseguradoras y explicarle las opciones con honestidad.")}</p>
    <p>{L("Because we’re independent, we aren’t tied to a single company. That means we can find a fit for your budget, your driving record, your home and your business, and keep checking as things change.", "Como somos independientes, no dependemos de una sola compañía. Eso nos permite encontrar la opción que se ajuste a su presupuesto, su historial de manejo, su casa y su negocio, y seguir revisándola a medida que las cosas cambian.")}</p>
    <p>{L("Many of our clients have been with us for years and brought their family, friends and businesses along.", "Muchos de nuestros clientes llevan años con nosotros y han traído a su familia, amigos y negocios.")}</p></div>
  <div class="panel"><div class="big">{L("Your agent, your name", "Su agente sabe su nombre")}</div><p>{L("Call us and you’ll talk to someone who remembers you.", "Llámenos y hablará con alguien que lo recuerda.")}</p>
    {tel_btn("btn btn-gold", PHONE)}</div>
</div></section>
<section class="block alt"><div class="wrap">{owner(False)}</div></section>
{stats()}
<section class="block alt"><div class="wrap">
  <div class="head center"><span class="eyebrow">{L("What we stand for", "Lo que nos define")}</span><h2>{L("How we work.", "Cómo trabajamos.")}</h2></div>
  <div class="cards">{"".join(f'<div class="card"><div class="ico">{ICONS[k]}</div><h3>{t}</h3><p>{d}</p></div>' for k, t, d in cards3)}</div>
</div></section>
<section class="block"><div class="wrap"><div class="head center"><span class="eyebrow">{L("Client stories", "Opiniones de clientes")}</span><h2>{L("In their words.", "En sus palabras.")}</h2></div>{testimonials()}</div></section>
{cta()}
'''
    write(pre + fname("about"), shell("about",
          L("About Us | The Key To Insurance, Miami", "Nosotros | The Key To Insurance, Miami"),
          L("Meet The Key To Insurance, an independent Miami agency focused on honest advice and fast, friendly service.",
            "Conozca The Key To Insurance, una agencia independiente de Miami enfocada en consejo honesto y servicio rápido y amable."), about_body))

    # ---------- CONTACT ----------
    maps = "https://maps.google.com/?q=" + ADDR.replace(" ", "+")
    contact_body = f'''
{pagehead(L("Contact", "Contacto"), L("Call us, or we’ll call you.", "Llámenos, o nosotros lo llamamos."), L("The fastest way to a quote is the phone. Prefer a call back? Fill out the form.", "La forma más rápida de obtener una cotización es el teléfono. ¿Prefiere que le llamemos? Llene el formulario."), actions=False)}
<section class="block"><div class="wrap split" style="align-items:start">
  <div>
    <h2>{L("Reach us", "Cómo encontrarnos")}</h2>
    <ul class="contact-list">
      {"".join(f'<li><small>{L("Main line", "Línea principal") if i == 0 else L("Alternate line", "Línea alterna")}</small><a href="tel:{t}">{p}</a></li>' for i, (p, t) in enumerate(PHONES))}
      <li><small>Email</small><a href="mailto:{EMAIL}" style="font-size:1.1rem">{EMAIL}</a></li>
      <li><small>{L("Office", "Oficina")}</small><a href="{maps}" style="font-size:1.1rem">{ADDR}</a></li>
    </ul>
  </div>
  <div id="quote" class="card" style="padding:32px"><h2 style="font-size:1.6rem">{L("Request a call back", "Pida que le llamemos")}</h2>{form()}</div>
</div></section>
'''
    write(pre + fname("contact"), shell("contact",
          L("Contact & Free Quote | The Key To Insurance, Miami", "Contacto y cotización gratis | The Key To Insurance, Miami"),
          L("Call 786.417.2459 or request a callback for a free insurance quote. The Key To Insurance, 2423 NW 97th Ave, Miami, FL.",
            "Llame al 786.417.2459 o pida que le llamemos para una cotización de seguro gratis. The Key To Insurance, 2423 NW 97th Ave, Miami, FL."), contact_body))


build("en")
build("es")

write("assets/favicon.svg", f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="11" fill="#0c1f3a"/><g transform="translate(2 2) scale(.92)">{KEYG}</g></svg>')
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
urls = [f"{SITE}/" if k == "home" else f"{SITE}/{ROUTES[k][0]}" for k in ROUTES] + \
       [f"{SITE}/es/" if k == "home" else f"{SITE}/es/{ROUTES[k][1]}" for k in ROUTES]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{x}</loc></url>\n" for x in urls) + "</urlset>\n")
print("ok")

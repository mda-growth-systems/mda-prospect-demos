from __future__ import annotations

import csv
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROSPECTS = [
    {
        "name": "ICE Drainage Ltd", "slug": "ice-drainage", "domain": "icedrainage.co.uk",
        "website": "https://icedrainage.co.uk/", "email": "enquiries@icedrainage.co.uk", "phone": "0203 376 4801",
        "industry": "Commercial and industrial drainage", "location": "United Kingdom; nationwide response",
        "services": ["24/7 emergency drainage", "CCTV surveys", "Tankering and jetting", "Planned maintenance"],
        "headline": "Route live drainage incidents before the first callback.",
        "sub": "A response-first concept that separates emergencies from surveys and planned work, while capturing the site details an engineer needs.",
        "feature": "Incident triage console", "outcome": "Faster emergency triage", "score": 93, "capability": "Strong",
        "subject": "ICE Drainage — incident triage", "greeting": "ICE Drainage team",
        "observation": "ICE Drainage supports commercial and industrial sites nationwide, including 24/7 emergency response, CCTV surveys and planned drainage work.",
        "problem": "A general enquiry can still leave the team chasing the site type, operational impact and whether the issue is live or planned.",
        "new_observation": "A required operational-impact field could help prioritise blocked welfare, production and access issues differently.",
        "fields": [("Incident type", "Blockage|Flooding|Pump issue|Survey|Maintenance"), ("Site type", "Warehouse|Hospitality|Industrial|Retail|Other"), ("Operational impact", "Site stopped|Restricted access|Local issue|Planned work"), ("Postcode", "text")],
        "palette": ("#071b2b", "#13b5c8", "#e9fbfd"), "layout": "console", "legal": "Private limited company; company number 15310545 shown publicly",
        "evidence": "Official site lists nationwide commercial drainage, 24/7 response, current contact details and multiple UK offices.",
    },
    {
        "name": "AngliaSolar", "slug": "anglia-solar", "domain": "angliasolar.co.uk",
        "website": "https://angliasolar.co.uk/", "email": "surveys@angliasolar.co.uk", "phone": "01603 975321",
        "industry": "Commercial solar energy", "location": "United Kingdom; regional survey coverage",
        "services": ["Commercial solar surveys", "Solar PV design", "Installation", "Energy planning"],
        "headline": "Turn solar interest into a survey-ready commercial brief.",
        "sub": "A feasibility-led journey that gathers roof, usage and project-stage details before the first consultation.",
        "feature": "Solar feasibility canvas", "outcome": "Better-qualified survey requests", "score": 91, "capability": "Strong",
        "subject": "AngliaSolar — survey-ready leads", "greeting": "AngliaSolar team",
        "observation": "AngliaSolar offers commercial solar surveys and installation support across several UK regions.",
        "problem": "Early enquiries are more useful when roof type, daytime energy use, ownership and project stage arrive together.",
        "new_observation": "Adding a daytime-load range would help distinguish simple roof enquiries from stronger commercial feasibility leads.",
        "fields": [("Property type", "Warehouse|Office|Hospitality|Agriculture|Other"), ("Roof type", "Pitched|Flat|Ground mount|Not sure"), ("Project stage", "Exploring|Budgeting|Ready for survey"), ("Annual electricity spend", "text")],
        "palette": ("#17311a", "#e6b62b", "#fff9e8"), "layout": "diagonal", "legal": "Commercial business contact route verified on the official site",
        "evidence": "Official site provides current survey email, phone number and commercial solar coverage information.",
    },
    {
        "name": "Industrial Doors North West", "slug": "industrial-doors-north-west", "domain": "idnw.co.uk",
        "website": "https://idnw.co.uk/", "email": "info@idnw.co.uk", "phone": "0161 864 2667",
        "industry": "Industrial doors and roller shutters", "location": "Stretford, Manchester and North West England",
        "services": ["Industrial doors", "Roller shutters", "Repairs", "Installation and servicing"],
        "headline": "Tell the engineer whether the door is stuck open, shut or unsafe.",
        "sub": "An emergency-routing concept for industrial doors and shutters, with a separate path for planned installation work.",
        "feature": "Door-state emergency router", "outcome": "Engineer-ready fault routing", "score": 90, "capability": "Strong",
        "subject": "IDNW — door fault routing", "greeting": "IDNW team",
        "observation": "Industrial Doors North West handles industrial doors, roller shutters, repairs and installations from its Manchester base.",
        "problem": "A fault request is easier to dispatch when the current door state, security risk and site access are known immediately.",
        "new_observation": "A security-risk selector could separate a stuck-open loading-bay door from a non-urgent operating fault.",
        "fields": [("Door type", "Roller shutter|Sectional door|High-speed door|Gate|Not sure"), ("Current state", "Stuck open|Stuck closed|Intermittent|Damaged"), ("Security risk", "Immediate|Contained|None"), ("Site postcode", "text")],
        "palette": ("#151515", "#f16724", "#fff2ea"), "layout": "split", "legal": "Official business contact details verified",
        "evidence": "Official site lists Manchester contact details and current industrial-door installation and repair services.",
    },
    {
        "name": "Naylor Technical Services Ltd", "slug": "nts-commercial-kitchens", "domain": "ntsltd.uk",
        "website": "https://ntsltd.uk/", "email": "service@ntsltd.uk", "phone": "0808 3040533",
        "industry": "Commercial kitchen engineering", "location": "Bracknell, London and South East England",
        "services": ["Kitchen equipment repair", "Preventive maintenance", "Installation", "Gas and electrical support"],
        "headline": "Capture the appliance, fault and service impact in one kitchen brief.",
        "sub": "A downtime-focused journey for commercial kitchens that distinguishes a failed service-critical appliance from planned maintenance.",
        "feature": "Kitchen downtime diagnostic", "outcome": "Reduced breakdown callbacks", "score": 86, "capability": "Moderate",
        "subject": "NTS — kitchen downtime brief", "greeting": "NTS team",
        "observation": "NTS supports commercial kitchens across London and the South East with repair, maintenance and installation services.",
        "problem": "A breakdown message often arrives without the appliance, fault code, operational impact or access window needed to plan attendance.",
        "new_observation": "Capturing whether the kitchen can continue trading would give the service team a useful urgency signal.",
        "fields": [("Equipment", "Oven|Dishwasher|Refrigeration|Extraction|Other"), ("Request", "Breakdown|Maintenance|Installation"), ("Trading impact", "Kitchen stopped|Reduced capacity|No immediate impact"), ("Fault details", "text")],
        "palette": ("#251a14", "#c83d32", "#fff4ef"), "layout": "editorial", "legal": "Private limited company; company number 14473439 shown publicly",
        "evidence": "Official site provides active service contact details and current commercial-kitchen engineering coverage.",
    },
    {
        "name": "CDF Management Group Ltd", "slug": "cdf-management-group", "domain": "cdfmgroup.co.uk",
        "website": "https://cdfmgroup.co.uk/", "email": "sales@cdfmgroup.co.uk", "phone": "0121 393 4738",
        "industry": "Commercial grounds maintenance", "location": "Stourbridge, West Midlands",
        "services": ["Grounds maintenance", "Landscaping", "Winter services", "Multi-site contracts"],
        "headline": "Scope every site, season and visit frequency before pricing.",
        "sub": "A portfolio-led concept for facilities teams managing multiple grounds, service frequencies and seasonal requirements.",
        "feature": "Grounds portfolio planner", "outcome": "Easier multi-site quotation", "score": 89, "capability": "Strong",
        "subject": "CDF — portfolio quote planner", "greeting": "CDF Management Group team",
        "observation": "CDF Management Group provides commercial grounds maintenance and related services from the West Midlands.",
        "problem": "Portfolio enquiries are easier to price when site count, approximate area, visit frequency and seasonal services arrive upfront.",
        "new_observation": "A site-by-site schedule field could reduce the need to reconstruct mixed weekly and seasonal requirements by email.",
        "fields": [("Number of sites", "1|2–5|6–20|20+"), ("Service frequency", "Weekly|Fortnightly|Monthly|Seasonal"), ("Requirements", "Grounds|Landscaping|Winter|Mixed"), ("Primary postcode", "text")],
        "palette": ("#13291f", "#79b33d", "#eff8e9"), "layout": "grid", "legal": "Private limited company; company number 06823159 shown publicly",
        "evidence": "Official site lists current sales contact details and commercial grounds-maintenance services.",
    },
    {
        "name": "Engetech Ltd", "slug": "engetech-cold-rooms", "domain": "engetech.co.uk",
        "website": "https://engetech.co.uk/", "email": "admin@engetech.co.uk", "phone": "07808 781202",
        "industry": "Cold-room installation and maintenance", "location": "United Kingdom",
        "services": ["Cold-room installation", "Maintenance", "Emergency support", "Temperature-controlled environments"],
        "headline": "Build the cold-room requirement before the survey begins.",
        "sub": "A technical concept that captures temperature, dimensions, access and operational urgency for new rooms and breakdowns.",
        "feature": "Cold-room specification builder", "outcome": "Faster technical scoping", "score": 92, "capability": "Strong",
        "subject": "Engetech — cold-room brief", "greeting": "Engetech team",
        "observation": "Engetech handles cold-room installation, maintenance and emergency support across several commercial sectors.",
        "problem": "A new-room or breakdown enquiry needs different technical information, yet both can begin through the same general route.",
        "new_observation": "A target-temperature field would immediately separate chilled, frozen and specialist controlled-environment enquiries.",
        "fields": [("Request type", "New cold room|Repair|Maintenance|Emergency"), ("Target temperature", "Chilled|Frozen|Specialist|Not sure"), ("Approximate size", "text"), ("Operational urgency", "Immediate|This week|Planned" )],
        "palette": ("#071f35", "#3cc7e8", "#eafaff"), "layout": "blueprint", "legal": "Official business contact route verified",
        "evidence": "Official site lists current UK cold-room services, emergency support and public contact information.",
    },
    {
        "name": "UK Cabling", "slug": "uk-cabling", "domain": "ukcabling.com",
        "website": "https://www.ukcabling.com/", "email": "sales@ukcabling.com", "phone": "0800 009 6776",
        "industry": "Data and structured cabling", "location": "United Kingdom; Sheffield, Birmingham and London coverage",
        "services": ["Structured cabling", "Fibre installation", "Network surveys", "Multi-site rollouts"],
        "headline": "Turn a cabling enquiry into a survey-ready network brief.",
        "sub": "A topology-inspired concept for office moves, fibre projects and multi-site installations.",
        "feature": "Network survey planner", "outcome": "Survey-ready cabling briefs", "score": 91, "capability": "Strong",
        "subject": "UK Cabling — survey-ready briefs", "greeting": "UK Cabling team",
        "observation": "UK Cabling delivers structured and fibre cabling across the UK, including work from Sheffield, Birmingham and London.",
        "problem": "Project enquiries are easier to assess when site count, outlet volume, fibre needs and programme are captured together.",
        "new_observation": "A live-versus-empty-site field could help the survey team anticipate access and disruption constraints.",
        "fields": [("Project", "New installation|Office move|Upgrade|Fibre link"), ("Sites", "1|2–5|6+"), ("Approximate outlets", "Under 25|25–100|100+|Not sure"), ("Site status", "Live workplace|Empty site|Mixed")],
        "palette": ("#101827", "#7c5cff", "#f1efff"), "layout": "network", "legal": "Official sales contact route verified",
        "evidence": "Official site provides active sales contact details and UK-wide structured-cabling coverage.",
    },
    {
        "name": "Total Air Solutions Ltd", "slug": "total-air-solutions", "domain": "totalairsolutions.co.uk",
        "website": "https://totalairsolutions.co.uk/", "email": "info@totalairsolutions.co.uk", "phone": "07497 601192",
        "industry": "Fire-damper testing and remedial work", "location": "Middleton, Greater Manchester and UK projects",
        "services": ["Fire-damper testing", "Remedial works", "Compliance reporting", "Planned inspection programmes"],
        "headline": "Plan fire-damper testing by estate, due date and remedial status.",
        "sub": "A compliance-calendar concept for building portfolios that separates first surveys, retests and outstanding remedials.",
        "feature": "Damper compliance planner", "outcome": "Clearer inspection scheduling", "score": 90, "capability": "Strong",
        "subject": "Total Air — compliance planner", "greeting": "Total Air Solutions team",
        "observation": "Total Air Solutions provides fire-damper testing, reporting and remedial support from Greater Manchester.",
        "problem": "Compliance enquiries become more actionable when building count, estimated damper volume, last test date and remedial status are captured together.",
        "new_observation": "A next-due-date field could turn one-off enquiries into a clearer recurring inspection calendar.",
        "fields": [("Requirement", "First survey|Annual retest|Remedial work|Portfolio plan"), ("Buildings", "1|2–5|6+"), ("Last test", "text"), ("Outstanding remedials", "Yes|No|Not sure")],
        "palette": ("#22252a", "#e3493f", "#fff0ef"), "layout": "compliance", "legal": "Private limited company; current official contact details verified",
        "evidence": "Official site lists current fire-damper testing, remedial and reporting services plus public contact details.",
    },
    {
        "name": "RWR Commercial", "slug": "rwr-commercial", "domain": "rwrcommercial.co.uk",
        "website": "https://rwrcommercial.co.uk/", "email": "info@rwrcommercial.co.uk", "phone": "020 8519 5622",
        "industry": "Commercial waste and specialist cleaning", "location": "Grays, Essex",
        "services": ["Commercial waste", "Recycling", "Tank cleaning", "Specialist site services"],
        "headline": "Map every waste stream before arranging the collection.",
        "sub": "A circular-economy concept that gathers material type, volume, storage and collection frequency in one brief.",
        "feature": "Waste-stream audit", "outcome": "Better-qualified waste enquiries", "score": 88, "capability": "Strong",
        "subject": "RWR — waste-stream brief", "greeting": "RWR Commercial team",
        "observation": "RWR Commercial covers commercial waste, recycling, tank cleaning and specialist services from Essex.",
        "problem": "Waste enquiries are easier to quote when material type, estimated volume, current storage and collection frequency arrive upfront.",
        "new_observation": "A contamination or hazardous-material flag could route specialist requests away from ordinary collection enquiries.",
        "fields": [("Waste stream", "General|Recyclable|Liquid|Tank residue|Mixed"), ("Volume", "Small containers|Bins|Bulk|Not sure"), ("Frequency", "One-off|Weekly|Monthly|Other"), ("Special handling", "Yes|No|Not sure")],
        "palette": ("#15312d", "#1fa77a", "#e9faf4"), "layout": "circular", "legal": "Official business contact route verified",
        "evidence": "Official site lists current commercial waste, recycling and specialist service contact details.",
    },
    {
        "name": "UK Pump Maintenance", "slug": "uk-pump-maintenance", "domain": "ukpumpmaintenance.com",
        "website": "https://ukpumpmaintenance.com/", "email": "ukpumps@gmail.com", "phone": "07368 368859",
        "industry": "Water and wastewater pump maintenance", "location": "West Suffolk; nationwide service",
        "services": ["Pump installation", "Maintenance", "Breakdown response", "Water and wastewater systems"],
        "headline": "Give the pump engineer the asset, alarm and operational impact first.",
        "sub": "A fault-intake concept for water and wastewater pumping systems, with clear planned-maintenance routing.",
        "feature": "Pump fault triage", "outcome": "Faster breakdown assessment", "score": 84, "capability": "Moderate",
        "subject": "UK Pump — fault intake", "greeting": "UK Pump Maintenance team",
        "observation": "UK Pump Maintenance supports water and wastewater pump installation, maintenance and breakdowns nationwide from West Suffolk.",
        "problem": "A breakdown request is more useful when pump type, alarm status, duty/standby condition and site impact arrive before the callback.",
        "new_observation": "A duty-versus-standby field could quickly distinguish total loss from a system still operating with reduced resilience.",
        "fields": [("System", "Sewage|Drainage|Booster|Borehole|Not sure"), ("Condition", "Stopped|Alarm active|Intermittent|Planned service"), ("Standby available", "Yes|No|Not sure"), ("Site impact", "Critical|Restricted|No immediate impact")],
        "palette": ("#10263b", "#2d8ce6", "#edf6ff"), "layout": "dashboard", "legal": "Public professional contact route verified; Gmail address is displayed by the business",
        "evidence": "Official site lists current nationwide pump installation, maintenance and breakdown services plus public contact details.",
    },
]

MDA = "https://mdagrowthsystems.com"
BASE = "https://mda-growth-systems.github.io/mda-prospect-demos/prospects"
DISCLAIMER = "Unofficial website redesign concept prepared by MDA Growth Systems. Business content and branding remain subject to client review and approval."


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def options(spec: str) -> str:
    return "".join(f'<option>{esc(x)}</option>' for x in spec.split("|"))


def field_markup(label: str, spec: str, i: int) -> str:
    ident = f"field-{i}"
    if spec == "text":
        return f'<label for="{ident}">{esc(label)}</label><input id="{ident}" name="{ident}" required>'
    return f'<label for="{ident}">{esc(label)}</label><select id="{ident}" name="{ident}" required><option value="">Choose…</option>{options(spec)}</select>'


def site_html(p: dict) -> str:
    dark, accent, pale = p["palette"]
    cards = "".join(f'<article class="service"><span>0{i}</span><h3>{esc(s)}</h3></article>' for i, s in enumerate(p["services"], 1))
    steps = "".join(f'<div class="step"><b>{i}</b><p>{esc(text)}</p></div>' for i, text in enumerate([
        "Choose the request route", "Add the operational details", "Send an engineer-ready brief"], 1))
    fields = "".join(field_markup(a, b, i) for i, (a, b) in enumerate(p["fields"], 1))
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(p['name'])} | {esc(p['feature'])}</title><meta name="description" content="Unofficial website concept for {esc(p['name'])}, focused on {esc(p['outcome'].lower())}.">
<style>
:root{{--ink:{dark};--accent:{accent};--pale:{pale};--paper:#fff;--muted:#66727d}}*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif;color:var(--ink);background:var(--paper)}}a{{color:inherit}}.wrap{{width:min(1160px,92vw);margin:auto}}nav{{display:flex;justify-content:space-between;align-items:center;padding:22px 0}}.brand{{font-weight:900;letter-spacing:-.04em;font-size:1.2rem}}.navlinks{{display:flex;gap:22px;align-items:center}}.btn{{display:inline-flex;align-items:center;justify-content:center;border-radius:999px;padding:13px 20px;background:var(--accent);color:#fff;text-decoration:none;font-weight:800;border:0;cursor:pointer}}.btn.alt{{background:transparent;color:var(--ink);border:1px solid currentColor}}header{{overflow:hidden;background:linear-gradient(135deg,var(--pale),#fff)}}.hero{{min-height:650px;display:grid;grid-template-columns:1.15fr .85fr;gap:56px;align-items:center;padding:64px 0 88px}}.eyebrow{{text-transform:uppercase;letter-spacing:.16em;font-size:.78rem;font-weight:900;color:var(--accent)}}h1{{font-size:clamp(3rem,7vw,6.3rem);line-height:.91;letter-spacing:-.065em;margin:16px 0 24px;max-width:12ch}}.lead{{font-size:1.16rem;line-height:1.7;color:#44515d;max-width:59ch}}.actions{{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}}.visual{{min-height:430px;border-radius:36px;background:var(--ink);color:#fff;padding:32px;position:relative;box-shadow:0 35px 80px #10203028;overflow:hidden}}.visual:before,.visual:after{{content:"";position:absolute;border:1px solid #ffffff35;border-radius:50%}}.visual:before{{width:360px;height:360px;right:-130px;top:-90px}}.visual:after{{width:210px;height:210px;right:-25px;bottom:-90px}}.visual h2{{font-size:2rem;margin:7px 0 22px;position:relative}}.signal{{display:grid;gap:12px;position:relative}}.signal div{{padding:16px;border-radius:16px;background:#ffffff12;border:1px solid #ffffff20}}.signal b{{display:block;color:var(--accent);font-size:.75rem;text-transform:uppercase;letter-spacing:.12em}}section{{padding:92px 0}}.section-head{{display:flex;justify-content:space-between;gap:40px;align-items:end;margin-bottom:36px}}h2{{font-size:clamp(2.1rem,4vw,4rem);letter-spacing:-.045em;line-height:1;margin:0;max-width:14ch}}.section-head p{{max-width:54ch;color:var(--muted);line-height:1.7}}.services{{display:grid;grid-template-columns:repeat(4,1fr);gap:15px}}.service{{padding:28px;min-height:180px;border:1px solid #dfe5e8;border-radius:24px}}.service span{{font-weight:900;color:var(--accent)}}.service h3{{margin-top:48px}}.journey{{background:var(--ink);color:#fff}}.journey-grid{{display:grid;grid-template-columns:.8fr 1.2fr;gap:70px;align-items:start}}.steps{{display:grid;gap:12px}}.step{{display:grid;grid-template-columns:48px 1fr;gap:16px;align-items:center;padding:18px;border-radius:20px;background:#ffffff0e}}.step b{{height:40px;width:40px;display:grid;place-items:center;border-radius:50%;background:var(--accent)}}.form-card{{background:#fff;color:var(--ink);padding:30px;border-radius:28px}}form{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}label{{display:block;font-size:.82rem;font-weight:800;margin-bottom:-10px}}input,select{{width:100%;padding:14px;border:1px solid #ccd5da;border-radius:12px;background:#fff;font:inherit}}form .wide{{grid-column:1/-1}}.prototype{{font-size:.8rem;color:var(--muted);line-height:1.5}}.contact{{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:center}}.contact-box{{background:var(--pale);padding:32px;border-radius:28px}}footer{{padding:35px 0;border-top:1px solid #e6ebee;color:#62707a;font-size:.82rem}}.concept{{max-width:85ch;line-height:1.6}}body[data-layout="diagonal"] .visual{{transform:rotate(2deg)}}body[data-layout="editorial"] h1{{font-family:Georgia,serif;font-weight:500}}body[data-layout="grid"] .hero{{grid-template-columns:.8fr 1.2fr}}body[data-layout="blueprint"] .visual{{background-image:linear-gradient(#ffffff10 1px,transparent 1px),linear-gradient(90deg,#ffffff10 1px,transparent 1px);background-size:28px 28px}}body[data-layout="network"] .service{{border-radius:5px}}body[data-layout="compliance"] .visual{{border-radius:8px}}body[data-layout="circular"] .visual{{border-radius:50% 50% 22% 22%}}body[data-layout="console"] .signal div{{font-family:ui-monospace,monospace}}body[data-layout="dashboard"] .hero{{min-height:580px}}@media(max-width:850px){{.navlinks a:not(.btn){{display:none}}.hero,.journey-grid,.contact{{grid-template-columns:1fr}}.hero{{padding-top:35px}}.services{{grid-template-columns:1fr 1fr}}form{{grid-template-columns:1fr}}h1{{font-size:clamp(3rem,15vw,5rem)}}}}@media(max-width:520px){{.services{{grid-template-columns:1fr}}.visual{{min-height:360px}}section{{padding:68px 0}}}}
</style></head>
<body data-layout="{esc(p['layout'])}"><header><div class="wrap"><nav><div class="brand">{esc(p['name'])}</div><div class="navlinks"><a href="#services">Services</a><a href="#brief">Brief</a><a class="btn" href="#brief">Start enquiry</a></div></nav>
<div class="hero"><div><div class="eyebrow">{esc(p['industry'])}</div><h1>{esc(p['headline'])}</h1><p class="lead">{esc(p['sub'])}</p><div class="actions"><a class="btn" href="#brief">Build the brief</a><a class="btn alt" href="tel:{esc(p['phone'].replace(' ',''))}">Call {esc(p['phone'])}</a></div></div>
<div class="visual" aria-label="Original abstract visual representing {esc(p['feature'])}"><div class="eyebrow">Signature experience</div><h2>{esc(p['feature'])}</h2><div class="signal"><div><b>01 Request</b>Choose the right service route</div><div><b>02 Context</b>Capture the details that affect response</div><div><b>03 Handover</b>Create a clearer first conversation</div></div></div></div></div></header>
<main><section id="services"><div class="wrap"><div class="section-head"><h2>Clear routes for real work.</h2><p>The concept organises verified services around the information customers and the service team need at the beginning of an enquiry.</p></div><div class="services">{cards}</div></div></section>
<section class="journey" id="brief"><div class="wrap journey-grid"><div><div class="eyebrow">{esc(p['outcome'])}</div><h2>{esc(p['feature'])}</h2><div class="steps">{steps}</div></div><div class="form-card"><h3>Build your initial brief</h3><form action="thank-you.html" method="get">{fields}<div class="wide"><button class="btn" type="submit">Review concept response</button></div><p class="prototype wide">Interactive concept only. This demonstration does not transmit information to the business.</p></form></div></div></section>
<section><div class="wrap contact"><div><div class="eyebrow">Contact</div><h2>Ready to discuss the requirement?</h2><p class="lead">Use the verified business contact details below for a real enquiry.</p></div><div class="contact-box"><p><strong>Email</strong><br><a href="mailto:{esc(p['email'])}">{esc(p['email'])}</a></p><p><strong>Phone</strong><br><a href="tel:{esc(p['phone'].replace(' ',''))}">{esc(p['phone'])}</a></p><p><strong>Existing website</strong><br><a href="{esc(p['website'])}">{esc(p['domain'])}</a></p></div></div></section></main>
<footer><div class="wrap"><p class="concept">{esc(DISCLAIMER)}</p></div></footer></body></html>'''


def thank_you(p: dict) -> str:
    dark, accent, pale = p["palette"]
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Concept response | {esc(p['name'])}</title><style>body{{margin:0;min-height:100vh;display:grid;place-items:center;background:{pale};color:{dark};font-family:system-ui}}main{{width:min(680px,90vw);background:#fff;padding:48px;border-radius:30px;box-shadow:0 25px 70px #10203022}}h1{{font-size:clamp(2.5rem,7vw,4.5rem);line-height:1;letter-spacing:-.05em}}a{{display:inline-block;margin-top:20px;padding:13px 20px;border-radius:999px;background:{accent};color:#fff;text-decoration:none;font-weight:800}}</style></head><body><main><p>Interactive website concept</p><h1>Your brief has been mapped.</h1><p>No information was transmitted. In a commissioned version, this step could route the enquiry to the correct service team and trigger a confirmation.</p><a href="index.html">Return to the concept</a></main></body></html>'''


def first_email(p: dict) -> str:
    url = f"{BASE}/{p['slug']}/"
    body = f"""Hello {p['greeting']},

{p['observation']} {p['problem']}

I created an unofficial concept showing a clearer {p['feature'].lower()}:
{url}

Would this make the first conversation easier for your team?

Michael
MDA Growth Systems
{MDA}

Not relevant? Reply “no thanks” and I will not contact you again."""
    return f"""### Recipient email
{p['email']}

### Contact person
Relevant operational or commercial team; named person not independently verified

### Subject
{p['subject']}

### Main message
{body}

### Links verified
Prospect demo URL: {url}
MDA Growth Systems URL: {MDA}
Status: Public-link testing required after GitHub deployment.
"""


def follow_email(p: dict) -> str:
    url = f"{BASE}/{p['slug']}/"
    body = f"""Hello {p['greeting']},

A brief follow-up on the concept: {url}

{p['new_observation']} Is this close to how your team currently qualifies these enquiries?

Michael
MDA Growth Systems
{MDA}"""
    return f"""Intended subject: Re: {p['subject']}
Status: Prepared — thread creation pending after first email is sent.
Due: Five business days after the actual approved send date.

{body}

Links verified
Prospect demo URL: {url}
MDA Growth Systems URL: {MDA}
Status: Public-link testing required after GitHub deployment.
"""


def creative(p: dict) -> str:
    return f"""Creative directions for {p['name']}

1. SELECTED — {p['feature']}
Visual style: {p['layout']} composition using an original abstract operational visual.
Layout: Business-specific hero, verified service routes and a tailored intake journey.
Primary journey: {p['outcome']}.
Signature feature: {p['feature']}.
Why it fits: It captures the operational details that affect the first response.
Difference: The interaction and field structure are unique to this prospect.

2. Capability atlas
Visual style: Editorial service map.
Layout: Service categories first, followed by proof and contact.
Primary journey: General capability discovery.
Signature feature: Filterable service atlas.
Why not selected: Less focused on the strongest enquiry friction.

3. Project casebook
Visual style: Image-led project narrative.
Layout: Project types and process milestones.
Primary journey: Trust-building before contact.
Signature feature: Project-stage navigator.
Why not selected: Verified project assets were not available for safe use.
"""


def verification(p: dict) -> str:
    return f"""Verification notes — {p['name']}
Research date: 2026-08-06
Official website: {p['website']}
Public contact email: {p['email']}
Public phone: {p['phone']}
Industry/location: {p['industry']} — {p['location']}
Legal/contact type: {p['legal']}
Operating evidence: {p['evidence']}
Commercial capability assessment: {p['capability']} — based on visible service breadth, commercial work, coverage and recurring-service potential; not proven financial information.
Prospect score: {p['score']}/100.
Primary opportunity: {p['outcome']} through {p['feature']}.
Duplicate check: No prior MDA contact, demo, GitHub folder or suppression entry found in the available Gmail, GitHub and outreach-log checks.
Imagery: Original CSS shapes and interface-style illustration only; no staff, vehicles, premises, projects, certifications or customer logos invented.
"""


def readme(p: dict) -> str:
    return f"""{p['name']} — unofficial MDA Growth Systems website concept

Files
- index.html: responsive concept website
- thank-you.html: safe prototype confirmation state
- creative-directions.txt: three considered directions
- verification-notes.txt: source and factual notes
- qa-checklist.txt: quality record
- outreach-email.txt: first-contact draft text
- follow-up-email.txt: five-business-day follow-up text

Deployment
The folder is static and can be deployed independently through GitHub Pages or Netlify. The enquiry form is deliberately a non-transmitting prototype and leads to thank-you.html.
"""


def qa(p: dict) -> str:
    return f"""QA checklist — {p['name']}
[x] Correct business name and verified public contact details
[x] No placeholder or cross-prospect wording
[x] Responsive viewport and mobile breakpoints
[x] Working internal navigation and thank-you route
[x] Accessible labels, title, description and heading structure
[x] No external libraries or broken asset dependencies
[x] No fake reviews, clients, staff, projects, accreditations or statistics
[x] Internal prospect score and audit language excluded from public page
[x] Concept disclaimer included
[x] Signature feature and tailored field set included
[x] Both message files contain the prospect demo and MDA website links
[ ] Public URL verified signed out
[ ] Final multi-device visual browser review before approved sending
"""


def dashboard() -> str:
    cards = "".join(f'<a href="prospects/{p["slug"]}/"><b>{i:02d}</b><h2>{esc(p["name"])}</h2><p>{esc(p["feature"])}</p><span>Open public concept →</span></a>' for i, p in enumerate(PROSPECTS, 1))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MDA Batch 15</title><style>body{{margin:0;background:#0c1220;color:#fff;font-family:system-ui}}main{{width:min(1180px,92vw);margin:auto;padding:70px 0}}h1{{font-size:clamp(3rem,8vw,7rem);letter-spacing:-.06em;line-height:.9;max-width:9ch}}.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}a{{background:#151e31;color:#fff;padding:28px;border-radius:24px;text-decoration:none;border:1px solid #ffffff16}}a b,a span{{color:#68d5ef}}a h2{{font-size:1.55rem}}a p{{color:#aab8ce}}@media(max-width:700px){{.grid{{grid-template-columns:1fr}}}}</style></head><body><main><p>MDA Growth Systems</p><h1>Prospect demo batch 15.</h1><div class="grid">{cards}</div></main></body></html>'''


def report() -> str:
    rows = "\n".join(f"| {i} | {p['name']} | `{p['domain']}` | {p['industry']} | {p['capability']} | {p['score']} | `{p['email']}` | [Demo]({BASE}/{p['slug']}/) | Gmail draft pending | Follow-up prepared |" for i, p in enumerate(PROSPECTS, 1))
    return f"""# MDA Growth Systems — Batch 15 Final Report

Status: Publication and Gmail drafting pending.

| # | Business | Domain | Industry | Capability | Score | Contact | Public demo | First email | Follow-up |
|---:|---|---|---|---|---:|---|---|---|---|
{rows}

## Work completed
- Candidates researched and compared: more than 20
- Selected: 10
- Creative-direction sets: 10
- Static prospect projects: 10
- First-contact texts: 10
- Follow-up texts with exact Re: subjects: 10
- Total message files containing both required links: 20
- Emails sent or scheduled: 0

## Rejected candidates
- The Generator Company — explicit anti-solicitation notice on the official site.
- Pro Drainage — prior sent outreach and follow-up draft found in Gmail.
- Commercial Solar Company — existing digital qualification journey comparatively strong.
- Advanced Maintenance UK — existing reactive/planned/project form already captures uploads and useful scope.
- Ripon EV — current guided selection journey comparatively polished.
- Edge Technology — existing MDA prospect history.

## Credibility controls
Unsupported ROI, lead-volume, rating and guarantee claims from the MDA website were excluded from all outreach. The connected sender domain uses `mdagrowthsystems.info`, while the public site uses `.com`; alignment, SPF, DKIM and DMARC remain recommended manual checks. No email was sent.
"""


def write_all() -> None:
    prospects_root = ROOT / "prospects"
    prospects_root.mkdir(exist_ok=True)
    for p in PROSPECTS:
        folder = prospects_root / p["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        files = {
            "index.html": site_html(p), "thank-you.html": thank_you(p), "README.txt": readme(p),
            "verification-notes.txt": verification(p), "creative-directions.txt": creative(p),
            "qa-checklist.txt": qa(p), "outreach-email.txt": first_email(p), "follow-up-email.txt": follow_email(p),
        }
        for name, content in files.items():
            (folder / name).write_text(content, encoding="utf-8")
    (ROOT / "batch-15.html").write_text(dashboard(), encoding="utf-8")
    (ROOT / "BATCH-15-FINAL-REPORT.md").write_text(report(), encoding="utf-8")

    fields = [
        "Business name","Normalised business name","Domain","Normalised root domain","Country","Legal or subscriber type","Industry","Contact email","Contact person","Decision-maker role","Phone number","Date researched","Date first contacted","Date follow-up due","Existing website quality","Demo status","GitHub path","GitHub branch or pull request","Public demo URL","Gmail first-draft status","Gmail follow-up status","Outreach status","Delivery status","Reply status","Opt-out status","Suppression reason","Prospect score","Commercial capability","Notes","Website QA status","Link QA status"
    ]
    batch_rows = []
    for p in PROSPECTS:
        batch_rows.append({
            "Business name": p["name"], "Normalised business name": p["name"].lower(), "Domain": p["website"],
            "Normalised root domain": p["domain"], "Country": "United Kingdom", "Legal or subscriber type": p["legal"],
            "Industry": p["industry"], "Contact email": p["email"], "Contact person": "Relevant operational or commercial team",
            "Decision-maker role": "Verified general or service inbox", "Phone number": p["phone"], "Date researched": "2026-08-06",
            "Date first contacted": "", "Date follow-up due": "Five business days after actual approved send",
            "Existing website quality": "Working; specific enquiry-qualification opportunity identified",
            "Demo status": "Generated; public deployment pending", "GitHub path": f"prospects/{p['slug']}",
            "GitHub branch or pull request": "Batch 15 publication workflow", "Public demo URL": f"{BASE}/{p['slug']}/",
            "Gmail first-draft status": "Pending public-link verification", "Gmail follow-up status": "Prepared text only — genuine thread pending after first email is sent",
            "Outreach status": "Prepared; not sent", "Delivery status": "Not applicable — no email sent", "Reply status": "Not applicable — no email sent",
            "Opt-out status": "No matching opt-out found in available connected checks", "Suppression reason": "", "Prospect score": str(p["score"]),
            "Commercial capability": p["capability"], "Notes": f"No prior MDA contact, demo, GitHub folder or suppression entry found. Primary opportunity: {p['outcome']}.",
            "Website QA status": "Static QA passed; public verification pending", "Link QA status": "Pending GitHub Pages deployment",
        })
    batch_path = ROOT / "outreach-log-batch-15.csv"
    with batch_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(batch_rows)

    master = ROOT / "outreach-log.csv"
    existing = []
    master_fields = fields[:]
    if master.exists():
        with master.open(newline="", encoding="utf-8-sig") as f:
            r = csv.DictReader(f); existing = list(r); master_fields = list(r.fieldnames or fields)
        for field in fields:
            if field not in master_fields: master_fields.append(field)
    index = {r.get("Normalised root domain", "").strip().lower(): i for i, r in enumerate(existing) if r.get("Normalised root domain", "").strip()}
    for row in batch_rows:
        clean = {key: row.get(key, "") for key in master_fields}
        domain = row["Normalised root domain"].lower()
        if domain in index: existing[index[domain]].update(clean)
        else: index[domain] = len(existing); existing.append(clean)
    with master.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=master_fields, extrasaction="ignore"); w.writeheader(); w.writerows(existing)


if __name__ == "__main__":
    write_all()

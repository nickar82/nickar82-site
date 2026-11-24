"""Builds the static nickar82.com site: python3 _build/build.py (run from the site root).
Shared header/footer live here; each page body is below. Output: plain .html files."""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YT = "https://www.youtube.com/@nickar82"
ITCH_SWRC = "https://nickar82.itch.io/swrc89"

NAV = [("Games", "/games/"), ("Apps", "/apps/"), ("Blog", "/blog/"), ("About", "/about/"), ("Press kit", "/press/")]


def page(path, title, desc, body, active=None):
    nav = "\n".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if active == label else ""}>{label}</a></li>'
        for label, href in NAV)
    full_title = "Nickar — Games · Apps · Utilities" if path == "index.html" else f"{title} — Nickar"
    out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://nickar82.com/assets/img/og.jpg">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0d0221">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/icon-32.png">
<link rel="apple-touch-icon" href="/assets/img/icon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<nav class="wrap" aria-label="Main">
<a class="brand" href="/"><img src="/assets/img/icon-32.png" alt="" width="30" height="30">NICKAR<span>'82</span></a>
<ul class="nav-links">
{nav}
</ul>
<a class="btn btn-pink" href="/games/" style="padding:10px 18px">Play</a>
</nav>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
<div class="wrap">
<div>
<a class="brand" href="/"><img src="/assets/img/icon-32.png" alt="" width="30" height="30">NICKAR<span>'82</span></a>
<small>© 2026 Nickar · Games · Apps · Utilities</small>
</div>
<div class="links">
<a href="{YT}" rel="noopener">YouTube</a>
<a href="{ITCH_SWRC}" rel="noopener">itch.io</a>
<a href="/blog/">Blog</a>
<a href="/press/">Press kit</a>
<a href="/privacy/">Privacy</a>
</div>
</div>
</footer>
</body>
</html>
"""
    dest = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(out)


# ---------- shared bits ----------
GAMES = [
    dict(slug="/games/swrc89/", name="Super World Road Challenge '89", status="Coming December 2026",
         text="16-bit arcade racing on real roads around the world, with split-screen couch co-op.",
         meta="Windows · Linux · Steam Deck · Android"),
    dict(slug=None, name="Mars Wars", status="In development",
         text="A synthwave space shooter — the remake of an old Nickar project, now with Star Fox-style flight.",
         meta="PC · Gamepad"),
    dict(slug=None, name="Ink Squadron", status="Android · Testing",
         text="Coming soon to Google Play.", meta="Android"),
]
APPS = [
    dict(icon="A", name="AimMap", platform="Android app",
         text="Point your phone at a building or landmark: the live camera and a rotating map with a view cone show you what it is.",
         price="Free · Pro €1.49", cta=None),
    dict(icon="C", name="ClipButton", platform="Windows utility",
         text="A button in any text box that lists everything you copied — up to 500 entries, with a hotkey and a dockable button.",
         price="Coming soon", cta=None),
    dict(icon="M", name="Media Tools", platform="Chrome extension",
         text="Save, zoom and control photos and videos on any site, straight into the folders you choose.",
         price="Coming soon", cta=None),
]
POSTS = [
    dict(slug="/blog/hello-world/", tag="News", title="Hello, world — nickar82.com is live",
         text="Why this site exists and what's coming next.", date="2026-11-24"),
]


def game_card(g):
    inner = f"""<div class="thumb">{html.escape(g['name'])}</div>
<div class="body"><span class="status">{g['status']}</span><h3>{html.escape(g['name'])}</h3><p>{g['text']}</p><span class="meta">{g['meta']}</span></div>"""
    return f'<a class="card" href="{g["slug"]}">{inner}</a>' if g["slug"] else f'<article class="card">{inner}</article>'


def app_card(a):
    btn = f'<a class="btn btn-line" href="{a["cta"]}">Get it</a>' if a["cta"] else '<span class="btn btn-soon">Soon</span>'
    return f"""<article class="card"><div class="body">
<div class="app-head"><div class="app-icon" aria-hidden="true">{a['icon']}</div><div><h3>{a['name']}</h3><span style="color:var(--cyan);font-size:14px">{a['platform']}</span></div></div>
<p>{a['text']}</p>
<div class="price-row"><span class="price">{a['price']}</span>{btn}</div>
</div></article>"""


def post_card(p):
    return f"""<a class="card" href="{p['slug']}"><div class="body"><span class="tag">{p['tag']} · {p['date']}</span><h3>{p['title']}</h3><p>{p['text']}</p></div></a>"""


YT_CTA = f"""<section class="wrap" style="padding-bottom:72px">
<div class="cta">
<div style="flex:1 1 360px"><h2>Insert coin: follow the devlog</h2>
<p>Trailers, devlogs and new releases land on YouTube first. Newsletter coming soon.</p></div>
<a class="btn btn-sun" href="{YT}" rel="noopener">Subscribe on YouTube</a>
</div>
</section>"""

# ---------- HOME ----------
page("index.html", "Home", "Nickar makes retro-spirited games, handy apps and small utilities — some free, some paid.", f"""
<section class="hero">
<div class="grid-floor" aria-hidden="true"></div>
<div class="hero-inner">
<h1 style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">Nickar Electronic Games '82</h1>
<img class="hero-logo" src="/assets/img/logo.webp" width="1600" height="900" alt="Nickar Electronic Games '82 — Games · Apps · Utilities" fetchpriority="high">
<p class="lead">Retro-spirited games, handy apps and small tools — made by one developer, with love for the 16-bit era.</p>
<div class="btn-row">
<a class="btn btn-sun" href="/games/">Browse games</a>
<a class="btn btn-cyan" href="/apps/">Apps &amp; utilities</a>
</div>
</div>
</section>

<section class="wrap section" aria-labelledby="feat">
<div class="feature">
<div class="media"><a href="/games/swrc89/" class="placeholder-art" style="text-decoration:none">SUPER WORLD ROAD CHALLENGE '89</a></div>
<div class="copy">
<p class="eyebrow">Featured · Coming December 2026</p>
<h2 id="feat" class="display">Super World Road Challenge '89</h2>
<p style="font-size:18px;margin:0 0 24px">A 16-bit arcade racer on real roads from around the world — including a 1:1 ring around Sithonia. Couch co-op, five cabrios, and a radio full of tunes.</p>
<div class="btn-row">
<a class="btn btn-pink" href="/games/swrc89/">See the game</a>
<a class="btn btn-line" href="{ITCH_SWRC}" rel="noopener">itch.io</a>
</div>
</div>
</div>
</section>

<section class="wrap section" style="padding-top:0" aria-labelledby="games-h">
<div class="section-head"><h2 id="games-h">Games</h2><a href="/games/">All games →</a></div>
<div class="cards">
{''.join(game_card(g) for g in GAMES)}
</div>
</section>

<section class="band" aria-labelledby="apps-h">
<div class="wrap section">
<div class="section-head"><h2 id="apps-h">Apps &amp; Utilities</h2><a href="/apps/">All apps →</a></div>
<div class="cards">
{''.join(app_card(a) for a in APPS)}
</div>
</div>
</section>

<section class="wrap section" aria-labelledby="blog-h">
<div class="section-head"><h2 id="blog-h">Devlog &amp; Blog</h2><a href="/blog/">All posts →</a></div>
<div class="cards">
{''.join(post_card(p) for p in POSTS)}
</div>
</section>
{YT_CTA}
""")

# ---------- GAMES ----------
page("games/index.html", "Games", "Games by Nickar — retro-spirited arcade games for PC and Android.", f"""
<section class="page-hero"><div class="wrap"><h1>Games</h1><p>Arcade games with a 16-bit heart. Free demos where possible, fair prices always.</p></div></section>
<section class="wrap section"><div class="cards">{''.join(game_card(g) for g in GAMES)}</div></section>
{YT_CTA}
""", active="Games")

# ---------- SWRC ----------
page("games/swrc89/index.html", "Super World Road Challenge '89",
     "Super World Road Challenge '89 — a 16-bit arcade racer on real roads. Coming December 2026 to Windows, Linux, Steam Deck and Android.", f"""
<section class="game-hero">
<div class="shade"><div class="wrap">
<p class="eyebrow">Racing · 1–2 players · Coming December 2026</p>
<h1>Super World Road Challenge '89</h1>
</div></div>
</section>

<div class="wrap two-col">
<div class="main">
<p style="font-size:20px;line-height:1.7;margin-top:0">Cruise real roads around the world in a 16-bit arcade racer. Pick one of five cabrios, tune the radio, and drive stages built at true scale — from a full ring around the Sithonia peninsula to coasts, forests, cities, deserts, snow and mountains.</p>
<div class="shots">
<div>[SCREENSHOT]</div><div>[SCREENSHOT]</div><div>[SCREENSHOT]</div><div>[SCREENSHOT]</div>
</div>
<h2 class="display" style="font-size:28px;margin:40px 0 12px">Features</h2>
<ul style="font-size:18px;line-height:1.9;padding-left:22px;margin:0">
<li>Stages built from real roads at true scale</li>
<li>Arcade, touring, championship and quick race modes</li>
<li>Split-screen couch co-op for two players</li>
<li>Five cabrios from different eras</li>
<li>Full gamepad support, km or miles</li>
<li>Hidden bonus tracks somewhere out of this world</li>
</ul>
<h2 class="display" style="font-size:28px;margin:40px 0 12px">Trailer</h2>
<p><a href="{YT}" rel="noopener">Watch the official trailer on YouTube →</a></p>
</div>
<aside aria-label="Get the game">
<div class="buy">
<p style="margin:0;color:var(--soft)">Price</p>
<p class="display" style="margin:0;font-size:40px;color:var(--yellow)">€8.99</p>
<a class="btn btn-sun" href="{ITCH_SWRC}" rel="noopener">Get it on itch.io</a>
<span class="btn btn-soon">Steam — coming soon</span>
<span class="btn btn-soon">GOG — coming soon</span>
<span class="btn btn-soon">Google Play — coming soon</span>
<hr>
<dl>
<dt>Release</dt><dd>December 2026</dd>
<dt>Platforms</dt><dd>Windows · Linux · Steam Deck · Android</dd>
<dt>Players</dt><dd>1–2 (local)</dd>
<dt>Developer</dt><dd>Nickar</dd>
</dl>
<a href="/press/">Press kit →</a>
</div>
</aside>
</div>
""", active="Games")

# ---------- APPS ----------
page("apps/index.html", "Apps & Utilities", "Android apps, Windows utilities and Chrome extensions by Nickar.", f"""
<section class="page-hero"><div class="wrap"><h1>Apps &amp; Utilities</h1><p>Small, focused tools for Android, Windows and Chrome — built because I needed them myself.</p></div></section>
<section class="wrap section"><div class="cards">{''.join(app_card(a) for a in APPS)}</div></section>
{YT_CTA}
""", active="Apps")

# ---------- BLOG ----------
page("blog/index.html", "Blog", "Devlogs, behind-the-scenes and how-tos from Nickar.", f"""
<section class="page-hero"><div class="wrap"><h1>Devlog &amp; Blog</h1><p>Process, mistakes and how-tos from making games and apps.</p></div></section>
<section class="wrap section"><div class="cards">{''.join(post_card(p) for p in POSTS)}</div></section>
""", active="Blog")

page("blog/hello-world/index.html", "Hello, world — nickar82.com is live", "The Nickar studio site is live.", f"""
<section class="page-hero"><div class="wrap"><p class="tag" style="margin:0 0 10px">News · 2026-11-24</p><h1>Hello, world — nickar82.com is live</h1></div></section>
<article class="wrap section prose">
<p>This is the new home of Nickar: the games, apps and small utilities I make, plus a devlog about how they get made.</p>
<p>First up is <a href="/games/swrc89/">Super World Road Challenge '89</a>, a 16-bit racer on real roads, coming in December 2026. After that: the Mars Wars remake, and a handful of tools for Android, Windows and Chrome.</p>
<p>Some things will be free, some paid — you'll be able to get them here or on the usual stores. Follow along on <a href="{YT}" rel="noopener">YouTube</a> for trailers and updates.</p>
<p><a href="/blog/">← All posts</a></p>
</article>
""", active="Blog")

# ---------- ABOUT ----------
page("about/index.html", "About", "About Nickar, an independent developer of games, apps and utilities.", f"""
<section class="page-hero"><div class="wrap"><h1>About Nickar</h1><p>One developer, a lot of synthwave, and a soft spot for 16-bit consoles.</p></div></section>
<article class="wrap section prose">
<p>Nickar is the studio name of Nikolaos Karazafeiris, an independent developer making retro-spirited games and practical little apps.</p>
<p>The games aim for the feel of late-80s and early-90s arcades and consoles. The apps and utilities start as tools I wanted for myself — and get released when they might be useful to you too.</p>
<h2>Find me</h2>
<ul>
<li><a href="{YT}" rel="noopener">YouTube — @nickar82</a></li>
<li><a href="https://nickar82.itch.io" rel="noopener">itch.io — nickar82</a></li>
<li>Email: [CONTACT EMAIL]</li>
</ul>
</article>
""", active="About")

# ---------- PRESS ----------
page("press/index.html", "Press kit", "Press kit for Nickar and Super World Road Challenge '89: logos, screenshots and facts.", f"""
<section class="page-hero"><div class="wrap"><h1>Press kit</h1><p>Logos, facts and media for press, streamers and YouTubers. Free to use when covering Nickar games.</p></div></section>
<article class="wrap section prose">
<h2 style="margin-top:0">Studio</h2>
<ul><li>Name: Nickar</li><li>Developer: Nikolaos Karazafeiris (solo)</li><li>Website: nickar82.com</li><li>Contact: [CONTACT EMAIL]</li></ul>
<h2>Logos</h2>
<p><a href="/assets/img/logo.webp" download>Nickar logo (1600×900)</a> · <a href="/assets/img/icon-512.png" download>Pixel “N” icon (512×512)</a></p>
<h2>Super World Road Challenge '89</h2>
<ul><li>Genre: 16-bit arcade racing</li><li>Platforms: Windows, Linux, Steam Deck, Android</li><li>Release: December 2026</li><li>Price: €8.99</li><li>Players: 1–2 local split screen</li></ul>
<p>Screenshots and trailer: [LINKS]</p>
</article>
""", active="Press kit")

# ---------- PRIVACY ----------
page("privacy/index.html", "Privacy", "Privacy policy for nickar82.com.", f"""
<section class="page-hero"><div class="wrap"><h1>Privacy</h1></div></section>
<article class="wrap section prose">
<p>nickar82.com does not use cookies, does not run ads and does not collect personal data.</p>
<p>The site loads fonts from Google Fonts, which receives your IP address when it serves them. Links to YouTube, itch.io and other stores lead to sites with their own privacy policies.</p>
<p>Privacy policies for individual apps are listed on each app's page. Questions: [CONTACT EMAIL].</p>
</article>
""")

# ---------- 404 ----------
page("404.html", "Game over", "Page not found.", """
<section class="hero" style="padding-bottom:160px"><div class="grid-floor" aria-hidden="true"></div>
<div class="hero-inner"><h1 class="display" style="font-size:64px;margin:40px 0 12px">GAME OVER</h1>
<p class="lead" style="margin-top:0">This page doesn't exist. Continue?</p>
<div class="btn-row"><a class="btn btn-sun" href="/">Continue ▸</a></div></div></section>
""")

print("built")

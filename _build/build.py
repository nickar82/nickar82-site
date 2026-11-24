"""Builds the static nickar82.com site: python3 _build/build.py (run from the site root).
Shared header/footer live here; each page body is below. Output: plain .html files."""
import os, html, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YT = "https://www.youtube.com/@nickar82"
LINKTREE = "https://linktr.ee/DJNickar"
TRAILER = "XggUQojWwqk"
GAMEPLAY = "9RpvdBLgC6g"
SWRC_COVER = "https://img.itch.zone/aW1nLzMyNjc2OTA4LnBuZw==/original/Gq25pS.png"
SWRC_SHOTS = ['https://img.itch.zone/aW1hZ2UvNTQyMzg4OC8zMjY3NjkyNy5qcGc=/original/eTc%2ByM.jpg', 'https://img.itch.zone/aW1hZ2UvNTQyMzg4OC8zMjY3NjkyNi5qcGc=/original/4gkXI4.jpg', 'https://img.itch.zone/aW1hZ2UvNTQyMzg4OC8zMjY3NjkyNS5qcGc=/original/a8btcV.jpg', 'https://img.itch.zone/aW1hZ2UvNTQyMzg4OC8zMjY3NjkyOC5qcGc=/original/EJbsL1.jpg', 'https://img.itch.zone/aW1hZ2UvNTQyMzg4OC8zMjY3NjkyNC5qcGc=/original/W1pj1L.jpg']
COFFEE = "https://buymeacoffee.com/nickar82p"
SOCIAL = [("YouTube", "https://www.youtube.com/@nickar82"), ("Instagram", "https://www.instagram.com/nickar_82"),
          ("X", "https://x.com/nickar82"), ("TikTok", "https://www.tiktok.com/@dj_nickar")]
STUDIO = "Nickar Electronic Games '82"
ITCH_SWRC = "https://nickar82.itch.io/swrc89"

NAV = [("Games", "/games/"), ("Apps", "/apps/"), ("Blog", "/blog/"), ("About", "/about/"), ("Press kit", "/press/")]


def page(path, title, desc, body, active=None):
    nav = "\n".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if active == label else ""}>{label}</a></li>'
        for label, href in NAV)
    full_title = f"{STUDIO} — Games · Apps · Utilities" if path == "index.html" else f"{title} — {STUDIO}"
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
<small>© 2026 {STUDIO} · Games · Apps · Utilities</small>
</div>
<div class="links">
{''.join(f'<a href="{u}" rel="noopener">{n}</a>' for n, u in SOCIAL)}
<a href="{ITCH_SWRC}" rel="noopener">itch.io</a>
<a href="{LINKTREE}" rel="noopener">More of me</a>
<a href="/blog/">Blog</a>
<a href="/press/">Press kit</a>
<a href="/privacy/">Privacy</a>
<a href="mailto:nickar82@gmail.com">Contact</a>
<a href="{COFFEE}" rel="noopener">☕ Buy me a coffee</a>
</div>
</div>
</footer>
</body>
</html>
"""
    # every external link opens in a new tab
    def ext(m):
        tag = m.group(0)
        if 'target=' not in tag:
            tag = tag[:-1] + ' target="_blank">'
        if 'rel=' not in tag:
            tag = tag[:-1] + ' rel="noopener">'
        return tag
    out = re.sub(r'<a\b[^>]*\bhref="https?://[^"]*"[^>]*>', ext, out)
    dest = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(out)


# ---------- shared bits ----------
GAMES = [
    dict(slug="/games/swrc89/", name="Super World Road Challenge '89", status="Out now on itch.io",
         text="Real roads. Real curves. Pure arcade. 32 stages rebuilt from real map data, with split-screen couch racing.",
         meta="Windows · Linux · Steam & Android coming", img=SWRC_COVER),
    dict(slug=None, name="Mars Wars", status="In development",
         text="A synthwave space shooter — the remake of an old Nickar project, now with Star Fox-style flight.",
         meta="PC · Gamepad", img=None),
    dict(slug=None, name="Ink Squadron: Paper Dogfight", status="Android · Closed testing",
         text="Draw your battle on paper! Dice dogfights, real-time waves and 1 VS 1 duels on a school notebook.",
         meta="Android · Coming to Google Play", img=None),
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
    thumb = f'<img class="thumb" src="{g["img"]}" alt="" loading="lazy" style="object-fit:cover;width:100%;padding:0">' if g.get("img") else f'<div class="thumb">{html.escape(g["name"])}</div>'
    inner = f"""{thumb}
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
<div class="btn-row"><a class="btn btn-sun" href="{YT}" rel="noopener">Subscribe on YouTube</a>
<a class="btn btn-line" href="{COFFEE}" rel="noopener">Buy me a coffee</a></div>
</div>
</section>"""

# ---------- HOME ----------
page("index.html", "Home", "Nickar Electronic Games '82 makes retro-spirited games, handy apps and small utilities — some free, some paid.", f"""
<section class="hero">
<div class="grid-floor" aria-hidden="true"></div>
<div class="hero-inner">
<h1 style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">Nickar Electronic Games '82</h1>
<img class="hero-logo" src="/assets/img/logo.webp" width="1600" height="900" alt="Nickar Electronic Games '82 — Games · Apps · Utilities" fetchpriority="high">
<p class="lead">Retro-spirited games, handy apps and small tools — made by one developer.</p>
<div class="btn-row">
<a class="btn btn-sun" href="/games/">Browse games</a>
<a class="btn btn-cyan" href="/apps/">Apps &amp; utilities</a>
</div>
</div>
</section>

<section class="wrap section" aria-labelledby="feat">
<div class="feature">
<div class="media"><iframe class="video" src="https://www.youtube-nocookie.com/embed/{TRAILER}" title="Super World Road Challenge '89 — trailer" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen></iframe></div>
<div class="copy">
<p class="eyebrow">Featured · Out now on itch.io</p>
<h2 id="feat" class="display">Super World Road Challenge '89</h2>
<p style="font-size:18px;margin:0 0 24px">Real roads. Real curves. Pure arcade. A 16-bit racer across 32 stages rebuilt from real map data — from the Amalfi coast to the Stelvio Pass, from Big Sur to the Karakoram Highway. Steam and Android coming soon.</p>
<div class="btn-row">
<a class="btn btn-sun" href="{ITCH_SWRC}" rel="noopener">Buy on itch.io — €8.99</a>
<a class="btn btn-line" href="/games/swrc89/">See the game</a>
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
SHOTS_HTML = "".join(f'<a href="{u}"><img src="{u}" alt="Super World Road Challenge \'89 screenshot {n}" loading="lazy" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:10px"></a>' for n, u in enumerate(SWRC_SHOTS, 1))
page("games/swrc89/index.html", "Super World Road Challenge '89",
     "Super World Road Challenge '89 — real roads, real curves, pure arcade. A 16-bit racer for Windows and Linux, out now on itch.io.", f"""
<section class="game-hero" style="background:#0d0221 url('{SWRC_COVER}') center/cover no-repeat">
<div class="shade"><div class="wrap">
<p class="eyebrow">Racing · 1–2 players · Out now on itch.io</p>
<h1>Super World Road Challenge '89</h1>
</div></div>
</section>

<div class="wrap two-col">
<div class="main">
<p style="font-size:22px;margin-top:0;color:var(--cream)"><strong>Real roads. Real curves. Pure arcade.</strong></p>
<p style="font-size:19px;line-height:1.7">A love letter to the arcade racers of the late 80s and early 90s — but every road is real. 32 stages were rebuilt from real map data, with true turns, hairpins, climbs and drops, from the Amalfi coast to the Stelvio Pass, from Big Sur to the Karakoram Highway. Pick your cabrio, tune the radio and hit the road with Iva, your co-driver, calling every bend ahead.</p>
<iframe class="video" src="https://www.youtube-nocookie.com/embed/{TRAILER}" title="Super World Road Challenge '89 — trailer" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen></iframe>
<h2 class="display" style="font-size:28px;margin:40px 0 16px">Screenshots</h2>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px">{SHOTS_HTML}</div>

<h2 class="display" style="font-size:28px;margin:40px 0 12px">Around the world in 32 stages</h2>
<ul style="font-size:18px;line-height:1.9;padding-left:22px;margin:0">
<li>Europe, the Americas, Asia-Pacific, Africa &amp; the Middle East — seven stages each</li>
<li>Four huge ring roads around Sithonia, Oahu, Jeju and the Cape Peninsula</li>
<li>Coastlines, deserts, forests, snowy passes, neon cities and tunnels</li>
<li>Day, sunset and night, with rain, fog, wind, storms and snow</li>
</ul>
<h2 class="display" style="font-size:28px;margin:40px 0 12px">Five cabrios</h2>
<p style="font-size:18px">A '91 Italian supercar, a '70 American muscle car, an '89 German cabrio, a '92 Japanese roadster and a '58 Italian classic — each with its own top speed, acceleration, braking and grip.</p>
<h2 class="display" style="font-size:28px;margin:40px 0 12px">Race your way</h2>
<ul style="font-size:18px;line-height:1.9;padding-left:22px;margin:0">
<li><strong>Time Attack</strong> — beat the clock from checkpoint to checkpoint</li>
<li><strong>Race</strong> — up to 7 AI rivals, each with their own car and driving style</li>
<li><strong>Elimination</strong> — the last car at every gate is out</li>
<li><strong>Chase</strong> — catch the rival who started ahead</li>
<li><strong>Championships</strong> — eleven cups, up to The Complete Challenge across all 32 stages</li>
<li><strong>1 VS 1 split screen</strong> — couch racing for two on one PC</li>
</ul>
<h2 class="display" style="font-size:28px;margin:40px 0 12px">Smash, boost, escape</h2>
<ul style="font-size:18px;line-height:1.9;padding-left:22px;margin:0">
<li>Takedowns: ram traffic, rivals and police until they spin out</li>
<li>Nitro cans for the long straights</li>
<li>Police chases when you pass a speed trap too fast</li>
<li>Burnout launches — hold brake and gas, let go, leave smoke behind</li>
</ul>
<h2 class="display" style="font-size:28px;margin:40px 0 12px">Pure 16-bit style</h2>
<p style="font-size:18px">Detailed pixel art, a CRT filter with scanlines, original synthwave and arcade music on the in-car radio, and a talkative co-driver with her own voice.</p>
<h2 class="display" style="font-size:28px;margin:40px 0 16px">Gameplay</h2>
<iframe class="video" src="https://www.youtube-nocookie.com/embed/{GAMEPLAY}" title="Super World Road Challenge '89 — gameplay" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen></iframe>
</div>
<aside aria-label="Get the game">
<div class="buy">
<p style="margin:0;color:var(--soft)">Price</p>
<p class="display" style="margin:0;font-size:40px;color:var(--yellow)">€8.99</p>
<a class="btn btn-sun" href="{ITCH_SWRC}" rel="noopener">Buy on itch.io</a>
<span class="btn btn-soon">Steam — coming soon</span>
<span class="btn btn-soon">GOG — coming soon</span>
<span class="btn btn-soon">Google Play — coming soon</span>
<hr>
<dl>
<dt>Status</dt><dd>Out now on itch.io</dd>
<dt>Platforms</dt><dd>Windows · Linux</dd>
<dt>Players</dt><dd>1–2 (local split screen)</dd>
<dt>Controls</dt><dd>Gamepad, keyboard, remapping</dd>
<dt>Language</dt><dd>English</dd>
<dt>DRM</dt><dd>DRM-free</dd>
<dt>Developer</dt><dd>Nickar Electronic Games '82</dd>
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
<p>First up is <a href="/games/swrc89/">Super World Road Challenge '89</a>, a 16-bit racer on real roads — out now on itch.io, with Steam and Android coming soon. After that: the Mars Wars remake, and a handful of tools for Android, Windows and Chrome.</p>
<p>Some things will be free, some paid — you'll be able to get them here or on the usual stores. Follow along on <a href="{YT}" rel="noopener">YouTube</a> for trailers and updates.</p>
<p><a href="/blog/">← All posts</a></p>
</article>
""", active="Blog")

# ---------- ABOUT ----------
page("about/index.html", "About", "About Nickar Electronic Games '82, an independent developer of games, apps and utilities.", f"""
<section class="page-hero"><div class="wrap"><h1>About Nickar Electronic Games '82</h1><p>One developer, a lot of synthwave, and a soft spot for 16-bit consoles.</p></div></section>
<article class="wrap section prose">
<p>Nickar Electronic Games '82 is the studio of Nikolaos Karazafeiris, an independent developer making retro-spirited games and practical little apps.</p>
<p>Music producer, game developer, graphics designer, photographer and more. The games aim for the feel of late-80s and early-90s arcades and consoles. The apps and utilities start as tools I wanted for myself — and get released when they might be useful to you too.</p>
<h2>Music</h2>
<p>As <strong>DJ Nickar</strong> I make music too — the album <em>Da Bass</em> is out now.</p>
<div class="btn-row"><a class="btn btn-line" href="http://tinyurl.com/DJNickarDaBassSp" rel="noopener">Da Bass on Spotify</a>
<a class="btn btn-line" href="http://tinyurl.com/DJ-NickarYTmusic" rel="noopener">Da Bass on YouTube Music</a></div>
<p>My AI music project <strong>AIchoes by DJ Nickar</strong> has its own channel:</p>
<p><a class="btn btn-cyan" href="https://www.youtube.com/@AIchoes" rel="noopener">AIchoes on YouTube</a></p>
<h2>Support my creations</h2>
<p>Many of my tools are free. If one of them helped you, a coffee keeps the next one coming.</p>
<p><a class="btn btn-sun" href="{COFFEE}" rel="noopener">☕ Buy me a coffee</a></p>
<h2>Find me</h2>
<ul>
<li><a href="{YT}" rel="noopener">YouTube — @nickar82</a></li>
<li><a href="https://www.instagram.com/nickar_82" rel="noopener">Instagram — @nickar_82</a></li>
<li><a href="https://x.com/nickar82" rel="noopener">X — @nickar82</a></li>
<li><a href="https://www.tiktok.com/@dj_nickar" rel="noopener">TikTok — @dj_nickar</a></li>
<li><a href="http://facebook.com/nick.kar82" rel="noopener">Facebook</a></li>
<li><a href="https://nickar82.itch.io" rel="noopener">itch.io — nickar82</a></li>
<li><a href="{LINKTREE}" rel="noopener">You can find more of me here — linktr.ee/DJNickar</a></li>
<li>Email: <a href="mailto:nickar82@gmail.com">nickar82@gmail.com</a></li>
</ul>
</article>
""", active="About")

# ---------- PRESS ----------
page("press/index.html", "Press kit", "Press kit for Nickar and Super World Road Challenge '89: logos, screenshots and facts.", f"""
<section class="page-hero"><div class="wrap"><h1>Press kit</h1><p>Logos, facts and media for press, streamers and YouTubers. Free to use when covering Nickar games.</p></div></section>
<article class="wrap section prose">
<h2 style="margin-top:0">Studio</h2>
<ul><li>Name: Nickar Electronic Games '82</li><li>Developer: Nikolaos Karazafeiris (solo)</li><li>Website: nickar82.com</li><li>Contact: <a href="mailto:nickar82@gmail.com">nickar82@gmail.com</a></li></ul>
<h2>Logos</h2>
<p><a href="/assets/img/logo.webp" download>Nickar logo (1600×900)</a> · <a href="/assets/img/icon-512.png" download>Pixel “N” icon (512×512)</a></p>
<h2>Super World Road Challenge '89</h2>
<ul><li>Genre: 16-bit arcade racing on real roads</li><li>Platforms: Windows, Linux (Steam and Android coming)</li><li>Released: November 2026 on itch.io</li><li>Price: €8.99</li><li>Players: 1–2 local split screen</li><li>Stages: 32, rebuilt from real map data</li></ul>
<p>Trailer: <a href="https://www.youtube.com/watch?v={TRAILER}">YouTube</a> · Gameplay: <a href="https://www.youtube.com/watch?v={GAMEPLAY}">YouTube</a> · Screenshots and store page: <a href="{ITCH_SWRC}">itch.io</a></p>
</article>
""", active="Press kit")

# ---------- PRIVACY ----------
page("privacy/index.html", "Privacy", "Privacy policy for nickar82.com.", f"""
<section class="page-hero"><div class="wrap"><h1>Privacy</h1></div></section>
<article class="wrap section prose">
<p>nickar82.com does not use cookies, does not run ads and does not collect personal data.</p>
<p>The site loads fonts from Google Fonts, which receives your IP address when it serves them. Links to YouTube, itch.io and other stores lead to sites with their own privacy policies.</p>
<p>Privacy policies for individual apps are listed on each app's page. Questions: <a href="mailto:nickar82@gmail.com">nickar82@gmail.com</a>.</p>
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

"""Builds the Know My PC website.

Edit the settings below, then run:  python build.py
It writes index.html, support.html, privacy.html, terms.html, sitemap.xml and
robots.txt next to this file (GitHub Pages serves them as-is).
"""

import datetime
import json
import os

# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------
SITE_URL = os.environ.get("KMP_SITE_URL", "https://knowmypc.app")
SUPPORT_EMAIL = os.environ.get("KMP_SUPPORT_EMAIL", "support@knowmypc.app")
CHECKOUT_URL = "https://buy.polar.sh/polar_cl_Z5MfJ5nniF9V287WZVeucoI9FtJk9AQQvbdxF32x2Yl"
PORTAL_URL = "https://polar.sh/raspinder-s/portal"
DOWNLOAD_URL = os.environ.get("KMP_DOWNLOAD_URL", "https://github.com/gitgill9/knowmypc/releases/latest/download/KnowMyPC-Setup.exe")
PRICE = "9.99"
TRIAL_DAYS = 14
REFUND_DAYS = 14
SELLER = "Raspinder S"
UPDATED = datetime.date.today().strftime("%B %-d, %Y")

HERE = os.path.dirname(os.path.abspath(__file__))

DOWNLOAD_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12"/><path d="M7 10l5 5 5-5"/><path d="M5 21h14"/></svg>'


def page(name, title, description, body, current="", head_extra=""):
    canonical = f"{SITE_URL}/" if name == "index" else f"{SITE_URL}/{name}.html"
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if key == current else ""}>{label}</a>'
        for key, href, label in [("features", "index.html#features", "Features"), ("pricing", "index.html#pricing", "Pricing"), ("support", "support.html", "Support")]
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Know My PC">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0e3b2e">
<link rel="icon" href="favicon.png" type="image/png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preload" href="fonts/adventor-bold.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="site.css">
{head_extra}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="board">
  <header class="wrap site-head">
    <a class="logo" href="index.html"><img src="img/icon.png" alt="" width="32" height="32">Know My PC</a>
    <nav aria-label="Main">{nav}<a class="btn primary" href="{DOWNLOAD_URL}">Download</a></nav>
  </header>
{body}
<footer class="board site-foot">
  <div class="wrap">
    <div class="cols">
      <div><a class="logo" href="index.html"><img src="img/icon.png" alt="" width="32" height="32">Know My PC</a>
        <p>Know why your Windows PC is slow, and what to do about it.</p></div>
      <nav aria-label="Footer"><a href="{DOWNLOAD_URL}">Download</a><a href="{CHECKOUT_URL}">Buy for ${PRICE}</a><a href="support.html">Support</a><a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a></nav>
      <nav aria-label="Legal"><a href="privacy.html">Privacy policy</a><a href="terms.html">Terms of sale</a><a href="{PORTAL_URL}">Manage your purchase</a></nav>
    </div>
    <p class="legal">© {datetime.date.today().year} {SELLER}. Payments are processed by Polar, our merchant of record. Windows is a trademark of Microsoft; Know My PC isn't affiliated with Microsoft.</p>
  </div>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------
PROBLEMS = [
    ("My PC is slow.", "overview", "Know My PC ranks what's slowing your PC down",
     "It watches every process, groups them under the app that started them, and ranks the likely causes from the last five minutes, with the evidence and a fix for each.",
     ["Shows which app, how much and for how long: “Chrome averaged 41% of your CPU (peak 68%)”",
      "Recognises Windows' own busy work, like Defender scans, updates and search indexing, and tells you when it'll finish by itself",
      "Ends a runaway app and everything it started, with one click"]),
    ("It lags when I play.", "history", "History shows exactly when it got bad",
     "Every slowdown is recorded with the apps responsible, so you can see it was Chrome and a Defender scan, not your game, that ate the headroom.",
     ["A 7-day CPU and memory timeline with overloads marked",
      "Game boost lowers other apps' priority while you play, then puts them back",
      "Suggestions drawn from your own slowdowns, not generic tips"]),
    ("My C: drive is full.", "storage", "Find the space, then get it back safely",
     "A map of your folders shows what's big at a glance. Know My PC knows where Windows hides space: update caches, temp files, WSL disks, game libraries, model files.",
     ["Shows which folders are safe to clear and which hold your own files",
      "Installed apps sorted by size, with one-click uninstall",
      "Only ever moves things to the Recycle Bin. Windows and Program Files are off-limits."]),
    ("It takes forever to start.", "startup", "See what starts with Windows, and switch it off",
     "Every startup app, which company made it, and whether it's using memory right now. Switching one off works exactly like Task Manager, and you can switch it back on anytime.",
     ["Apps for all users too: Windows asks for permission, and that's it",
      "Background services and scheduled tasks from other companies, listed separately"]),
]

FAQ = [
    ("Is it safe to use?",
     "Know My PC never ends Windows' own processes, never deletes anything permanently (it only moves files to the Recycle Bin), and won't touch the Windows or Program Files folders. Startup changes use the same switch Task Manager uses."),
    ("Windows says “Windows protected your PC” when I install it.",
     "That's SmartScreen, which warns about apps it hasn't seen many downloads of yet. Click <b>More info</b>, then <b>Run anyway</b>. The installer is the same file that's linked from this page."),
    ("Will it slow my PC down?",
     "It checks every 3 seconds by default, and you can make that 5 or 10 seconds in Settings. Know My PC appears in its own Apps list, so you can always see what it's using."),
    ("Which versions of Windows does it work on?",
     "Windows 11 and Windows 10 (64-bit). It uses Microsoft Edge WebView2, which Windows 11 already has; the installer adds it on Windows 10 if needed."),
    ("How does the free trial work?",
     f"Everything is unlocked for {TRIAL_DAYS} days, no account or card needed. If you buy, paste the license key from your receipt email into Settings → License."),
    ("Can I use it on more than one PC?",
     "Yes. Each license works on 2 PCs. To move it, open Settings → License → Move to another PC, then activate the key on the new one."),
    ("What if it doesn't help?",
     f"Email us within {REFUND_DAYS} days of buying and we'll refund you."),
    ("Is there a Mac version?",
     "No. Know My PC is built for Windows. On a Mac, iKnowMyMac does a similar job."),
]


def home():
    problems = "".join(f"""
    <section class="problem" aria-labelledby="p{i}">
      <div class="copy">
        <blockquote>{q}</blockquote>
        <h3 id="p{i}">{h}</h3>
        <p style="margin-top:10px">{p}</p>
        <ul>{"".join(f"<li>{x}</li>" for x in bullets)}</ul>
      </div>
      <div class="shot"><img src="img/{img}.webp" alt="Know My PC {img} screen" width="1920" height="1200" loading="lazy" decoding="async"></div>
    </section>""" for i, (q, img, h, p, bullets) in enumerate(PROBLEMS))

    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)

    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "SoftwareApplication",
                "name": "Know My PC",
                "operatingSystem": "Windows 10, Windows 11",
                "applicationCategory": "UtilitiesApplication",
                "description": "Finds out why your Windows PC is slow and how to fix it: ranked causes, slowdown history, storage, startup apps and developer tools.",
                "image": f"{SITE_URL}/img/overview.webp",
                "url": f"{SITE_URL}/",
                "downloadUrl": DOWNLOAD_URL,
                "offers": {"@type": "Offer", "price": PRICE, "priceCurrency": "USD", "url": CHECKOUT_URL},
            },
            {
                "@type": "FAQPage",
                "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a.replace("<b>", "").replace("</b>", "")}} for q, a in FAQ],
            },
        ],
    }
    head = f'<script type="application/ld+json">{json.dumps(ld)}</script>'

    body = f"""
  <div class="wrap hero">
    <div style="padding-bottom:64px">
      <h1>Know why your PC is slow.</h1>
      <p class="sub">Know My PC watches what your Windows PC is doing, tells you in plain English what's slowing it down, and helps you fix it.</p>
      <div class="ctas">
        <a class="btn primary" href="{DOWNLOAD_URL}">{DOWNLOAD_ICON}Download free trial</a>
        <a class="btn ghost" href="{CHECKOUT_URL}">Buy for ${PRICE}</a>
      </div>
      <ul class="facts"><li>{TRIAL_DAYS}-day free trial</li><li>One-time purchase</li><li>Works on 2 PCs</li><li>Windows 10 and 11</li></ul>
    </div>
    <div class="hero-shot"><img src="img/overview-dark.webp" alt="Know My PC ranking two causes of slowness: Google Chrome using 41% of the CPU, and a Defender scan" width="1920" height="1200" fetchpriority="high"></div>
  </div>
</div>

<main id="main">
  <div class="wrap problems" id="features">{problems}
  </div>

  <section class="board devs" aria-labelledby="dev-h">
    <div class="wrap grid">
      <div><h2 id="dev-h">Built for developers too</h2>
        <p>Know My PC knows what's running on a developer's PC: dev servers, coding agents, local models and the virtual machines behind WSL and Docker.</p></div>
      <dl>
        <dt>Ports</dt><dd>Every dev server, its project folder, and a warning when it's reachable from your network</dd>
        <dt>Coding agents</dt><dd>Claude Code, Codex, Aider and others, with processes they left running after the terminal closed</dd>
        <dt>Local AI</dt><dd>Models loaded in Ollama or LM Studio, and how much graphics memory they hold</dd>
        <dt>WSL and Docker</dt><dd>Distros, containers, and the VM that keeps your RAM until you cap it</dd>
      </dl>
    </div>
  </section>

  <section class="wrap privacy-sec" aria-labelledby="priv-h">
    <div><h2 id="priv-h">Your PC's data stays on your PC</h2>
      <p>No account and no tracking. History lives in a file on your own drive, and you can export or delete it anytime. Here is every connection Know My PC makes:</p></div>
    <div class="ledger">
      <div><b>License check</b><em>Weekly</em><span>Sends your license key to Polar to confirm it's valid. Nothing about your PC.</span></div>
      <div><b>Local AI status</b><em>This PC only</em><span>Asks Ollama and LM Studio on your own PC which models are loaded.</span></div>
      <div><b>Everything else</b><em>Never</em><span>Processes, files, history and settings never leave your PC.</span></div>
    </div>
  </section>

  <section class="wrap pricing" id="pricing" aria-labelledby="price-h">
    <div class="price-card">
      <div>
        <h2 id="price-h">One price. Yours to keep.</h2>
        <p class="price" style="margin-top:18px">${PRICE}<small>one-time, USD</small></p>
        <div class="ctas"><a class="btn solid" href="{CHECKOUT_URL}">Buy Know My PC</a><a class="btn outline" href="{DOWNLOAD_URL}">Try it free first</a></div>
        <p class="fine">Sales tax or VAT is added at checkout where it applies.</p>
      </div>
      <ul>
        <li>Every feature: diagnosis, history, storage, startup and developer tools</li>
        <li>Use it on 2 PCs</li>
        <li>{TRIAL_DAYS}-day free trial, no card needed</li>
        <li>{REFUND_DAYS}-day refund if it doesn't help</li>
        <li>No subscription and no account</li>
      </ul>
    </div>
  </section>

  <section class="wrap faq" aria-labelledby="faq-h">
    <div><h2 id="faq-h">Questions</h2><p class="fine" style="font-size:16px">Something else? <a href="support.html">Get help</a> or email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p></div>
    <div>{faq}</div>
  </section>
</main>
"""
    return page("index", "Know My PC: find out why your Windows PC is slow",
                "Know My PC shows what's slowing your Windows PC down, ranked with evidence and a fix for each. Slowdown history, storage, startup apps and Game boost. $9.99 one-time.",
                body, "features", head)


# ---------------------------------------------------------------------------
# Support
# ---------------------------------------------------------------------------
def doc(name, title, description, h1, lede, toc, article, current=""):
    aside = "".join(f'<a href="#{i}">{t}</a>' for i, t in toc)
    body = f"""
  <div class="wrap page-hero"><h1>{h1}</h1><p>{lede}</p></div>
</div>
<main id="main" class="wrap doc">
  <aside aria-label="On this page">{aside}</aside>
  <article>{article}</article>
</main>
"""
    return page(name, title, description, body, current)


def support():
    toc = [("contact", "Contact us"), ("license", "Licenses and purchases"), ("install", "Installing"), ("using", "Using Know My PC"), ("uninstall", "Uninstalling")]
    article = f"""
<div class="contact-card"><div><b>{SUPPORT_EMAIL}</b><span>Usually answered within 2 business days.</span></div><a class="btn solid" href="mailto:{SUPPORT_EMAIL}?subject=Know%20My%20PC%20help">Email support</a></div>

<h2 id="contact">Contact us</h2>
<p>Email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>. These help us answer in one reply:</p>
<ul>
  <li>Your Know My PC version (Settings → About) and Windows version</li>
  <li>What you expected, and what happened instead</li>
  <li>A screenshot, if something looks wrong</li>
  <li>For history questions, the file from Settings → History and data → Export JSON</li>
</ul>
<p>Never send your full license key or any passwords. The first and last four characters of a key are enough to find your order.</p>

<h2 id="license">Licenses and purchases</h2>
<h3>Where's my license key?</h3>
<p>It's in the receipt email from Polar, sent right after you buy. Check your spam folder. You can always find it again in the <a href="{PORTAL_URL}">customer portal</a>: enter the email you bought with.</p>
<h3>Activating</h3>
<ol><li>Open Know My PC and press <kbd>Ctrl</kbd> + <kbd>,</kbd> to open Settings.</li><li>Go to License, paste your key and click <strong>Activate</strong>.</li></ol>
<p>Activation needs an internet connection once. After that, Know My PC checks the key about once a week and keeps working offline.</p>
<h3>Moving to a new PC</h3>
<p>Each key works on 2 PCs. On the old PC, open Settings → License → <strong>Move to another PC</strong>, then activate the key on the new one. If the old PC is gone, you can remove it in the <a href="{PORTAL_URL}">customer portal</a>.</p>
<h3>Refunds and invoices</h3>
<p>Email us within {REFUND_DAYS} days of buying for a refund. Invoices and receipts are in the <a href="{PORTAL_URL}">customer portal</a>.</p>

<h2 id="install">Installing</h2>
<h3>“Windows protected your PC”</h3>
<p>SmartScreen shows this for apps it hasn't seen many downloads of yet. Click <strong>More info</strong>, then <strong>Run anyway</strong>. Only run installers you downloaded from this site.</p>
<h3>It says WebView2 is missing</h3>
<p>Windows 11 includes it. On Windows 10, install the <a href="https://developer.microsoft.com/microsoft-edge/webview2/">Microsoft Edge WebView2 Runtime</a>, then run the installer again.</p>

<h2 id="using">Using Know My PC</h2>
<h3>Windows asks for permission when I click something</h3>
<p>Some changes need administrator rights: closing a game that runs as administrator, or changing a startup app for all users. Know My PC asks Windows, and Windows asks you. Click <strong>Yes</strong> to continue.</p>
<h3>A game won't close</h3>
<p>Some anti-cheat systems block every other program from closing their game, even with administrator rights. Quit from inside the game or press <kbd>Alt</kbd> + <kbd>F4</kbd>.</p>
<h3>History is empty or has gaps</h3>
<p>History is recorded only while Know My PC is running. Turn on Settings → Window → <strong>Start with Windows</strong>, and set “When I close the window” to <strong>Keep watching</strong>.</p>
<h3>I don't get alerts</h3>
<p>Check that Overload alerts are on in Settings, and that Windows notifications are allowed for Know My PC (Windows Settings → System → Notifications). Alerts are held while a game is running unless you turn that off.</p>

<h2 id="uninstall">Uninstalling</h2>
<p>Open Windows Settings → Apps → Installed apps, find Know My PC and choose <strong>Uninstall</strong>. Your history and settings stay in <code>%LOCALAPPDATA%\\Know My PC</code> in case you reinstall; delete that folder to remove them too. Deactivate your license first (Settings → License → Move to another PC) if you'll use it elsewhere.</p>
"""
    return doc("support", "Support | Know My PC", "Get help with Know My PC: contact support, find or move your license key, install, and fix common problems.",
               "How can we help?", f"Answers to common questions, and a real person at {SUPPORT_EMAIL} for everything else.", toc, article, "support")


# ---------------------------------------------------------------------------
# Privacy & terms
# ---------------------------------------------------------------------------
def privacy():
    toc = [("summary", "In short"), ("app", "The app"), ("purchases", "Purchases"), ("site", "This website"), ("support-mail", "Support email"), ("rights", "Your choices"), ("changes", "Changes")]
    article = f"""
<p class="updated">Last updated {UPDATED}</p>
<h2 id="summary">In short</h2>
<p>Know My PC is built to keep your information on your PC. It has no account system and no analytics, and it doesn't sell or share data. This policy explains the few things that do leave your PC.</p>

<h2 id="app">The app</h2>
<p><strong>What stays on your PC.</strong> Know My PC reads information about running processes, memory, drives, startup items, services, scheduled tasks, installed apps and network ports so it can explain what's slowing your PC down. It stores your settings and a history of slowdowns in <code>%LOCALAPPDATA%\\Know My PC</code>. None of this is sent anywhere. You can export or delete it from Settings.</p>
<p><strong>License checks.</strong> When you activate a license, the app sends your license key and your PC's name (so you can tell your PCs apart in the customer portal) to Polar, our payment provider. About once a week it sends the key again to confirm it's still valid. No other information about your PC is included.</p>
<p><strong>Local connections.</strong> To show which AI models are loaded, the app asks Ollama and LM Studio on your own PC (<code>localhost</code>). These requests never leave your PC.</p>
<p><strong>Notifications.</strong> Overload alerts are Windows notifications created on your PC.</p>

<h2 id="purchases">Purchases</h2>
<p>Payments are handled by Polar Software, Inc. as merchant of record. Polar collects your email, payment and billing details to process the order, issue your license key and handle taxes. We receive your email address and order details from Polar to provide support. We never see your full card number. Polar's privacy policy is at <a href="https://polar.sh/legal/privacy">polar.sh/legal/privacy</a>.</p>

<h2 id="site">This website</h2>
<p>This site has no cookies, analytics or trackers. It's hosted on GitHub Pages, which may log your IP address for security and operations; see GitHub's privacy statement.</p>

<h2 id="support-mail">Support email</h2>
<p>If you email us, we use your message and address only to help you, and we keep it as long as needed to support your purchase.</p>

<h2 id="rights">Your choices</h2>
<p>You can delete the app's data anytime by clearing history in Settings or deleting the folder above. To access or delete purchase information, email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> and we'll handle it with Polar.</p>

<h2 id="changes">Changes</h2>
<p>If this policy changes, we'll update the date at the top. Questions: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p>
"""
    return doc("privacy", "Privacy policy | Know My PC", "Know My PC keeps your PC's data on your PC. What the app stores, the one connection it makes for license checks, and how purchases are handled.",
               "Privacy policy", "Your PC's data stays on your PC. Here's exactly what that means.", toc, article)


def terms():
    toc = [("license", "Your license"), ("trial", "Trial"), ("payments", "Payments and refunds"), ("use", "Using the software"), ("warranty", "No warranty"), ("liability", "Liability"), ("contact", "Contact")]
    article = f"""
<p class="updated">Last updated {UPDATED}</p>
<h2 id="license">Your license</h2>
<p>When you buy Know My PC, you get a personal, non-transferable license to use it on up to 2 PCs that you own or control. The software is licensed, not sold. You may not resell, share or publish license keys, or try to bypass the license check.</p>

<h2 id="trial">Trial</h2>
<p>You can use Know My PC free for {TRIAL_DAYS} days to decide whether it's right for you.</p>

<h2 id="payments">Payments and refunds</h2>
<p>Orders are processed by Polar Software, Inc., our merchant of record, which also handles sales tax and VAT. Prices are one-time and shown in US dollars. If Know My PC doesn't work for you, email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> within {REFUND_DAYS} days of purchase for a full refund. A refunded license key stops working.</p>

<h2 id="use">Using the software</h2>
<p>Know My PC can end processes, change startup items and move files to the Recycle Bin when you ask it to. Check what you're closing or removing first: save your work before ending an app, and back up anything important.</p>

<h2 id="warranty">No warranty</h2>
<p>Know My PC is provided “as is”, without warranties of any kind, to the fullest extent the law allows.</p>

<h2 id="liability">Liability</h2>
<p>To the fullest extent the law allows, our total liability for any claim relating to Know My PC is limited to the amount you paid for it. Nothing here limits rights you have under consumer law that can't be limited.</p>

<h2 id="contact">Contact</h2>
<p>{SELLER}, <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p>
"""
    return doc("terms", "Terms of sale | Know My PC", "The license terms, trial, payments and refund policy for Know My PC.",
               "Terms of sale", "Plain-English terms for buying and using Know My PC.", toc, article)


def main():
    pages = {"index": home(), "support": support(), "privacy": privacy(), "terms": terms()}
    for name, html in pages.items():
        with open(os.path.join(HERE, f"{name}.html"), "w", encoding="utf-8") as f:
            f.write(html)
    today = datetime.date.today().isoformat()
    urls = "".join(f"<url><loc>{SITE_URL}/{'' if n == 'index' else n + '.html'}</loc><lastmod>{today}</lastmod></url>" for n in pages)
    with open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    with open(os.path.join(HERE, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    # Empty .nojekyll makes GitHub Pages serve files as-is.
    open(os.path.join(HERE, ".nojekyll"), "w").close()
    print("Built", ", ".join(f"{n}.html" for n in pages), "for", SITE_URL)


if __name__ == "__main__":
    main()

"""Builds the Know My PC website.

Edit the settings below, then run:  python build.py
It writes index.html, support.html, privacy.html, terms.html, sitemap.xml and
robots.txt next to this file (GitHub Pages serves them as-is).
"""

import datetime
import json
import os

from guides import GUIDES

# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------
SITE_URL = os.environ.get("KMP_SITE_URL", "https://knowmypc.app")
SUPPORT_EMAIL = os.environ.get("KMP_SUPPORT_EMAIL", "support@knowmypc.app")
# Two plans: lifetime (one-time) and monthly (subscription). Same links as the app's license.rs.
CHECKOUT_URL = "https://buy.polar.sh/polar_cl_Z5MfJ5nniF9V287WZVeucoI9FtJk9AQQvbdxF32x2Yl"  # lifetime
CHECKOUT_MONTHLY_URL = ""  # TODO: the monthly product's checkout link from Polar
PORTAL_URL = "https://polar.sh/raspinder-s/portal"
DOWNLOAD_URL = os.environ.get("KMP_DOWNLOAD_URL", "https://knowmypc.app/download/KnowMyPC-Setup.exe")
PRICE = "29.99"  # lifetime
PRICE_MONTHLY = "4.99"
TRIAL_DAYS = 3
REFUND_DAYS = 14
SELLER = "Raspinder S"
# Dates shown on pages and in the sitemap. Change a page's date only when its
# content changes; Google treats dates that move on every build as fake freshness.
HOME_UPDATED = "2026-10-14"
SUPPORT_UPDATED = "2026-10-14"
PRIVACY_UPDATED = "2026-10-14"
TERMS_UPDATED = "2026-10-14"

HERE = os.path.dirname(os.path.abspath(__file__))

DOWNLOAD_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12"/><path d="M7 10l5 5 5-5"/><path d="M5 21h14"/></svg>'


def human_date(iso):
    return datetime.date.fromisoformat(iso).strftime("%B %-d, %Y")


def url_for(name):
    """Site-relative URL of a page: index -> /, support -> /support.html, fix/x -> /fix/x/."""
    if name == "index":
        return "/"
    if "/" in name or name == "fix":
        return f"/{name}/"
    return f"/{name}.html"


def page(name, title, description, body, current="", head_extra="", og_type="website", image_alt=""):
    canonical = SITE_URL + url_for(name)
    image_alt = image_alt or "Know My PC ranking what's slowing a Windows PC down"
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if key == current else ""}>{label}</a>'
        for key, href, label in [("features", "/#features", "Features"), ("pricing", "/#pricing", "Pricing"), ("fix", "/fix/", "Guides"), ("support", "/support.html", "Support")]
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Know My PC">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/img/og.png">
<meta property="og:image:alt" content="{image_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE_URL}/img/og.png">
<meta name="twitter:image:alt" content="{image_alt}">
<meta name="theme-color" content="#0e3b2e">
<link rel="icon" href="/img/icon.png" type="image/png" sizes="128x128">
<link rel="icon" href="/favicon.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preload" href="/fonts/adventor-bold.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="/site.css">
{head_extra}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="board">
  <header class="wrap site-head">
    <a class="logo" href="/"><img src="/img/icon.png" alt="" width="32" height="32">Know My PC</a>
    <nav aria-label="Main">{nav}<a class="btn primary" href="{DOWNLOAD_URL}">Download</a></nav>
  </header>
{body}
<footer class="board site-foot">
  <div class="wrap">
    <div class="cols">
      <div><a class="logo" href="/"><img src="/img/icon.png" alt="" width="32" height="32">Know My PC</a>
        <p>Know why your Windows PC is slow, and what to do about it.</p></div>
      <nav aria-label="Footer"><a href="{DOWNLOAD_URL}">Download</a><a href="/#pricing">Pricing</a><a href="/fix/">Fix guides</a><a href="/support.html">Support</a><a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a></nav>
      <nav aria-label="Legal"><a href="/privacy.html">Privacy policy</a><a href="/terms.html">Terms of sale</a><a href="{PORTAL_URL}">Manage your purchase</a></nav>
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
      "Ends a runaway app and everything it started, with one click"],
     "Know My PC showing two things slowing a PC down: Google Chrome using 41% of the CPU with a fix, and a Defender scan that usually finishes on its own"),
    ("It lags when I play.", "history", "History shows exactly when it got bad",
     "Every slowdown is recorded with the apps responsible, so you can see it was Chrome and a Defender scan, not your game, that ate the headroom.",
     ["A 7-day CPU and memory timeline with overloads marked",
      "Game boost lowers other apps' priority while you play, then puts them back",
      "The Graphics tab shows whether your graphics card or your processor is holding your game back",
      "Suggestions drawn from your own slowdowns, not generic tips"],
     "Know My PC History screen: a 24-hour CPU and memory chart with two slowdowns, each listing the apps responsible"),
    ("My C: drive is full.", "storage", "Find the space, then get it back safely",
     "A map of your folders shows what's big at a glance. Know My PC knows where Windows hides space: update caches, temp files, WSL disks, game libraries, model files.",
     ["Shows which folders are safe to clear and which hold your own files",
      "Installed apps sorted by size, with one-click uninstall",
      "Only ever moves things to the Recycle Bin. Windows and Program Files are off-limits."],
     "Know My PC Storage screen: space that is safe to clear, such as temp files and the Chrome cache, above a clickable map of folders"),
    ("It takes forever to start.", "startup", "See what starts with Windows, and switch it off",
     "Every startup app, which company made it, and whether it's using memory right now. Switching one off works exactly like Task Manager, and you can switch it back on anytime.",
     ["Apps for all users too: Windows asks for permission, and that's it",
      "Background services and scheduled tasks from other companies, listed separately"],
     "Know My PC Startup screen: startup apps with on/off switches, who made each one and how much memory it is using"),
]

NEW = [
    ("Updates itself", "When a new version is ready, you'll see a notice. One click installs it, and every update is signed so only real Know My PC releases install."),
    ("More health checks", "Spots a busy network, slow drive response, a processor held back by heat or power settings, slow startup, apps that crash or freeze, and drives that report problems."),
    ("Changes made, with Undo", "Settings → Changes made lists everything Know My PC changed on your PC. Startup and graphics changes undo with one click; files are in the Recycle Bin."),
    ("Every app has its own color", "Each app gets its own soft color in the Apps, Graphics and Developer lists, so you can follow it from one refresh to the next."),
    ("A welcome and a weekly summary", "A short tour when you first open it, and a weekly summary of your PC's slowdowns."),
    ("Faster, quieter, easier to get help", "Fixes now use Windows directly, it does less while hidden in the tray, and Copy support info puts everything we need in one paste."),
]

FAQ = [
    ("Is it safe to use?",
     "Know My PC never ends Windows' own processes, never deletes anything permanently (it only moves files to the Recycle Bin), and won't touch the Windows or Program Files folders. Startup changes use the same switch Task Manager uses, and Settings → Changes made lists everything it changed, with Undo."),
    ("Windows says “Windows protected your PC” when I install it.",
     "That's SmartScreen, which warns about apps it hasn't seen many downloads of yet. Click <b>More info</b>, then <b>Run anyway</b>. The installer is the same file that's linked from this page."),
    ("How do updates work?",
     "Know My PC checks for a new version once a day and shows a notice when one is ready. Nothing installs until you click <b>Update now</b>, and you can turn the checks off in Settings. Updates are included with both plans."),
    ("Will it slow my PC down?",
     "It checks every 3 seconds by default, and you can make that 5 or 10 seconds in Settings. Know My PC appears in its own Apps list, so you can always see what it's using."),
    ("Which versions of Windows does it work on?",
     "Windows 11 and Windows 10 (64-bit). It uses Microsoft Edge WebView2, which Windows 11 already has; the installer adds it on Windows 10 if needed."),
    ("How does the free trial work?",
     f"Everything is unlocked for {TRIAL_DAYS} days, no account or card needed. After that you can still see what's slowing your PC down; fixing it from the app needs a plan. When you buy, paste the license key from your receipt email into Settings → License."),
    ("Monthly or lifetime?",
     f"Monthly is ${PRICE_MONTHLY} a month and you can cancel any time; when it ends, fixes pause and the diagnosis keeps working. Lifetime is ${PRICE} once and yours to keep, with every update. Both work on 2 PCs. If you'd use it for more than six months, lifetime costs less."),
    ("How do I cancel my subscription?",
     f'Open the <a href="{PORTAL_URL}">customer portal</a>, enter the email you subscribed with, and cancel. You keep everything until the end of the month you paid for.'),
    ("Can I use it on more than one PC?",
     "Yes. Each license works on 2 PCs. To move it, open Settings → License → Move to another PC, then activate the key on the new one."),
    ("What if it doesn't help?",
     f"Email us within {REFUND_DAYS} days of buying lifetime, or of your first monthly payment, and we'll refund you."),
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
      <div class="shot"><img src="/img/{img}.webp" alt="{alt}" width="1920" height="1200" loading="lazy" decoding="async"></div>
    </section>""" for i, (q, img, h, p, bullets, alt) in enumerate(PROBLEMS))

    new_items = "".join(f"<li><b>{h}</b><span>{p}</span></li>" for h, p in NEW)
    guide_items = "".join(f'<li><a href="{url_for("fix/" + g["slug"])}"><b>{g["h1"]}</b><span>{g["summary"]}</span></a></li>' for g in GUIDES)
    faq = "".join(f"<details><summary><h3>{q}</h3></summary><p>{a}</p></details>" for q, a in FAQ)

    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "name": "Know My PC",
                "alternateName": ["knowmypc.app"],
                "url": f"{SITE_URL}/",
            },
            {
                "@type": "SoftwareApplication",
                "name": "Know My PC",
                "operatingSystem": "Windows 10, Windows 11",
                "applicationCategory": "UtilitiesApplication",
                "description": "Finds out why your Windows PC is slow and how to fix it: ranked causes, slowdown history, storage, startup apps and developer tools.",
                "image": f"{SITE_URL}/img/overview.webp",
                "url": f"{SITE_URL}/",
                "downloadUrl": DOWNLOAD_URL,
                "offers": [
                    {"@type": "Offer", "name": "Lifetime", "price": PRICE, "priceCurrency": "USD", "url": CHECKOUT_URL},
                    {"@type": "Offer", "name": "Monthly", "price": PRICE_MONTHLY, "priceCurrency": "USD", "url": CHECKOUT_MONTHLY_URL,
                     "priceSpecification": {"@type": "UnitPriceSpecification", "price": PRICE_MONTHLY, "priceCurrency": "USD", "billingDuration": "P1M"}},
                ],
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
        <a class="btn ghost" href="/#pricing">See pricing</a>
      </div>
      <ul class="facts"><li>{TRIAL_DAYS}-day free trial</li><li>${PRICE_MONTHLY}/month or ${PRICE} lifetime</li><li>Works on 2 PCs</li><li>Windows 10 and 11</li></ul>
    </div>
    <div class="hero-shot"><img src="/img/overview-dark.webp" alt="Know My PC ranking two causes of slowness: Google Chrome using 41% of the CPU, and a Defender scan" width="1920" height="1200" fetchpriority="high"></div>
  </div>
</div>

<main id="main">
  <div class="wrap problems" id="features">{problems}
  </div>

  <section class="wrap whats-new" id="new" aria-labelledby="new-h">
    <div><h2 id="new-h">New in version 0.2</h2><p>Know My PC keeps getting better, and updates are free.</p></div>
    <ul>{new_items}</ul>
  </section>

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
      <div><b>License check</b><em>Weekly, daily on monthly</em><span>Sends your license key to Polar to confirm it's valid. Nothing about your PC.</span></div>
      <div><b>Update check</b><em>Daily</em><span>Asks knowmypc.app whether a new version is out. Nothing about your PC is sent.</span></div>
      <div><b>Local AI status</b><em>This PC only</em><span>Asks Ollama and LM Studio on your own PC which models are loaded.</span></div>
      <div><b>Everything else</b><em>Never</em><span>Processes, files, history and settings never leave your PC.</span></div>
    </div>
  </section>

  <section class="wrap pricing" id="pricing" aria-labelledby="price-h">
    <div class="price-head">
      <h2 id="price-h">Try it free. Then pick a plan.</h2>
      <p>Everything is unlocked for {TRIAL_DAYS} days, no card needed. <a href="{DOWNLOAD_URL}">Download the free trial</a>.</p>
    </div>
    <div class="plans">
      <div class="price-card">
        <div>
          <h3>Monthly</h3>
          <p class="price">${PRICE_MONTHLY}<small>per month, USD</small></p>
          <div class="ctas"><a class="btn outline" href="{CHECKOUT_MONTHLY_URL}">Subscribe</a></div>
        </div>
        <ul>
          <li>Every feature: diagnosis, history, storage, startup and developer tools</li>
          <li>Use it on 2 PCs</li>
          <li>Cancel any time</li>
        </ul>
      </div>
      <div class="price-card best">
        <div>
          <h3>Lifetime <span class="tag">Best value</span></h3>
          <p class="price">${PRICE}<small>once, USD</small></p>
          <div class="ctas"><a class="btn solid" href="{CHECKOUT_URL}">Buy lifetime</a></div>
        </div>
        <ul>
          <li>Every feature, yours to keep</li>
          <li>Use it on 2 PCs</li>
          <li>Every future update included</li>
        </ul>
      </div>
    </div>
    <p class="fine plans-note">{REFUND_DAYS}-day refund if it doesn't help. No account needed. Sales tax or VAT is added at checkout where it applies.</p>
  </section>

  <section class="wrap home-guides" aria-labelledby="guides-h">
    <div><h2 id="guides-h">Common slowdowns, explained</h2><p class="fine" style="font-size:16px">Free guides to the usual suspects, whether or not you use Know My PC.</p></div>
    <ul class="guide-list">{guide_items}</ul>
  </section>

  <section class="wrap faq" aria-labelledby="faq-h">
    <div><h2 id="faq-h">Questions</h2><p class="fine" style="font-size:16px">Something else? <a href="/support.html">Get help</a> or email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p></div>
    <div>{faq}</div>
  </section>
</main>
"""
    return page("index", "Know My PC: find out why your Windows PC is slow",
                "See what's slowing your Windows PC down, ranked with the evidence and a fix for each. Slowdown history, storage, startup apps and Game boost.",
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
    toc = [("contact", "Contact us"), ("license", "Licenses and purchases"), ("install", "Installing and updating"), ("using", "Using Know My PC"), ("uninstall", "Uninstalling")]
    article = f"""
<div class="contact-card"><div><b>{SUPPORT_EMAIL}</b><span>Usually answered within 2 business days.</span></div><a class="btn solid" href="mailto:{SUPPORT_EMAIL}?subject=Know%20My%20PC%20help">Email support</a></div>

<h2 id="contact">Contact us</h2>
<p>Email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>. These help us answer in one reply:</p>
<ul>
  <li>The text from Settings → About → <strong>Copy support info</strong> (your version, Windows version and recent log lines; your license key isn't included)</li>
  <li>What you expected, and what happened instead</li>
  <li>A screenshot, if something looks wrong</li>
  <li>For history questions, the file from Settings → History and data → Export JSON</li>
</ul>
<p>Never send your full license key or any passwords. The first and last four characters of a key are enough to find your order.</p>

<h2 id="license">Licenses and purchases</h2>
<h3>Where's my license key?</h3>
<p>It's in the receipt email from Polar, sent right after you buy or subscribe. Check your spam folder. You can always find it again in the <a href="{PORTAL_URL}">customer portal</a>: enter the email you bought with.</p>
<h3>Activating</h3>
<ol><li>Open Know My PC and press <kbd>Ctrl</kbd> + <kbd>,</kbd> to open Settings.</li><li>Go to License, paste your key and click <strong>Activate</strong>.</li></ol>
<p>Activation needs an internet connection once. After that, Know My PC checks a lifetime key about once a week and a monthly key about once a day, and keeps working offline for a while (30 days for lifetime, 7 for monthly).</p>
<h3>Monthly subscriptions</h3>
<p>Your subscription renews every month. To change your card or cancel, open the <a href="{PORTAL_URL}">customer portal</a> and enter the email you subscribed with. When a subscription ends, fixes pause and Settings → License shows <strong>Subscription ended</strong>; seeing what's slowing your PC down still works. Renew it and Know My PC unlocks again by itself within a day, or right away with <strong>Check again</strong>. To switch to lifetime, buy it and paste the new key.</p>
<h3>Moving to a new PC</h3>
<p>Each key works on 2 PCs. On the old PC, open Settings → License → <strong>Move to another PC</strong>, then activate the key on the new one. If the old PC is gone, you can remove it in the <a href="{PORTAL_URL}">customer portal</a>.</p>
<h3>Refunds and invoices</h3>
<p>Email us within {REFUND_DAYS} days of buying lifetime, or of your first monthly payment, for a refund. Invoices and receipts are in the <a href="{PORTAL_URL}">customer portal</a>.</p>

<h2 id="install">Installing and updating</h2>
<h3>“Windows protected your PC”</h3>
<p>SmartScreen shows this for apps it hasn't seen many downloads of yet. Click <strong>More info</strong>, then <strong>Run anyway</strong>. Only run installers you downloaded from this site.</p>
<h3>It says WebView2 is missing</h3>
<p>Windows 11 includes it. On Windows 10, install the <a href="https://developer.microsoft.com/microsoft-edge/webview2/">Microsoft Edge WebView2 Runtime</a>, then run the installer again.</p>
<h3>Updating to a new version</h3>
<p>Know My PC checks for updates once a day and shows a notice when one is ready. Click <strong>Update now</strong> and it closes, updates and opens again by itself; your history, settings and license stay as they are. To check right away, open Settings → About → <strong>Check now</strong>. You can turn automatic checks off there too.</p>

<h2 id="using">Using Know My PC</h2>
<h3>Windows asks for permission when I click something</h3>
<p>Some changes need administrator rights: closing a game that runs as administrator, or changing a startup app for all users. Know My PC asks Windows, and Windows asks you. Click <strong>Yes</strong> to continue.</p>
<h3>Undoing a change</h3>
<p>Settings → <strong>Changes made</strong> lists everything Know My PC changed: apps it ended, startup apps it switched off, graphics settings and files it moved. Click <strong>Undo</strong> next to a startup or graphics change to put it back. Files it removed are in the Recycle Bin, where you can restore them.</p>
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
<p class="updated">Last updated {human_date(PRIVACY_UPDATED)}</p>
<h2 id="summary">In short</h2>
<p>Know My PC is built to keep your information on your PC. It has no account system and no analytics, and it doesn't sell or share data. This policy explains the few things that do leave your PC: license checks with Polar, our payment provider, and a daily check on knowmypc.app for new versions.</p>

<h2 id="app">The app</h2>
<p><strong>What stays on your PC.</strong> Know My PC reads information about running processes, memory, drives, startup items, services, scheduled tasks, installed apps and network ports so it can explain what's slowing your PC down. It stores your settings, a history of slowdowns, a list of the changes it made, and a small log of errors in <code>%LOCALAPPDATA%\\Know My PC</code>. None of this is sent anywhere. You can export or delete it from Settings.</p>
<p><strong>License checks.</strong> When you activate a license, the app sends your license key and your PC's name (so you can tell your PCs apart in the customer portal) to Polar, our payment provider. About once a week (once a day for a monthly subscription) it sends the key again to confirm it's still valid. No other information about your PC is included. If the check can't reach Polar, the app keeps working and tries again later. Your license key is stored encrypted, so only your Windows account on that PC can read it.</p>
<p><strong>Update checks.</strong> About once a day, and whenever you click Check now in Settings, the app downloads a small file from <code>knowmypc.app</code> that says what the newest version is. The request contains nothing about you or your PC beyond what any web request carries, such as your IP address. You can turn these checks off in Settings. If you choose to update, the installer is downloaded from the same site.</p>
<p><strong>Support info.</strong> Settings → About → Copy support info copies your app and Windows version, basic hardware details and recent log lines to your clipboard. Nothing is sent until you paste it into an email yourself. It never includes your license key.</p>
<p><strong>Local connections.</strong> To show which AI models are loaded, the app asks Ollama and LM Studio on your own PC (<code>localhost</code>). These requests never leave your PC.</p>
<p><strong>Notifications.</strong> Overload alerts are Windows notifications created on your PC.</p>

<h2 id="purchases">Purchases</h2>
<p>Payments are handled by Polar Software, Inc. as merchant of record. Polar collects your email, payment and billing details to process the order, issue your license key and handle taxes. We receive your email address and order details from Polar to provide support. We never see your full card number. Polar's privacy policy is at <a href="https://polar.sh/legal/privacy">polar.sh/legal/privacy</a>.</p>

<h2 id="site">This website</h2>
<p>This site has no cookies, analytics or trackers. It's hosted on GitHub Pages, which may log your IP address for security and operations, including when the app checks for updates; see GitHub's privacy statement.</p>

<h2 id="support-mail">Support email</h2>
<p>If you email us, we use your message and address only to help you, and we keep it as long as needed to support your purchase.</p>

<h2 id="rights">Your choices</h2>
<p>You can delete the app's data anytime by clearing history in Settings or deleting the folder above. To access or delete purchase information, email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> and we'll handle it with Polar.</p>

<h2 id="changes">Changes</h2>
<p>If this policy changes, we'll update the date at the top. Questions: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p>
"""
    return doc("privacy", "Privacy policy | Know My PC", "Know My PC keeps your PC's data on your PC. What the app stores, its license and update checks, and how purchases are handled.",
               "Privacy policy", "Your PC's data stays on your PC. Here's exactly what that means.", toc, article)


def terms():
    toc = [("license", "Your license"), ("trial", "Trial"), ("payments", "Payments and refunds"), ("use", "Using the software"), ("warranty", "No warranty"), ("liability", "Liability"), ("contact", "Contact")]
    article = f"""
<p class="updated">Last updated {human_date(TERMS_UPDATED)}</p>
<h2 id="license">Your license</h2>
<p>When you buy or subscribe to Know My PC, you get a personal, non-transferable license to use it on up to 2 PCs that you own or control. A lifetime license doesn't expire. A monthly license lasts while your subscription is active. The software is licensed, not sold. You may not resell, share or publish license keys, or try to bypass the license check.</p>

<h2 id="trial">Trial</h2>
<p>You can use Know My PC free for {TRIAL_DAYS} days to decide whether it's right for you. After the trial, the app keeps showing what's slowing your PC down; the actions that change your PC need a license.</p>

<h2 id="payments">Payments and refunds</h2>
<p>Orders are processed by Polar Software, Inc., our merchant of record, which also handles sales tax and VAT. Prices are shown in US dollars. There are two plans:</p>
<ul><li><strong>Monthly (${PRICE_MONTHLY} a month).</strong> Billed every month until you cancel. Cancel any time in the <a href="{PORTAL_URL}">customer portal</a>; you keep access until the end of the month you've paid for, and we don't refund partial months. When the subscription ends, the license key stops unlocking fixes.</li>
<li><strong>Lifetime (${PRICE} once).</strong> One payment, no renewals, including every future update of Know My PC.</li></ul>
<p>If Know My PC doesn't work for you, email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> within {REFUND_DAYS} days of buying lifetime, or of your first monthly payment, for a full refund. A refunded license key stops working. If you bought Know My PC before the monthly plan existed, your license is a lifetime license.</p>

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


# ---------------------------------------------------------------------------
# Fix guides (content lives in guides.py)
# ---------------------------------------------------------------------------
def guide(g):
    toc = [(i, h) for i, h, _ in g["sections"]]
    sections = "".join(f'\n<h2 id="{i}">{h}</h2>{html}' for i, h, html in g["sections"])
    related = "".join(f'<li><a href="{url_for("fix/" + o["slug"])}">{o["h1"]}</a></li>' for o in GUIDES if o is not g)
    article = f"""
<p class="updated">Published {human_date(g["published"])}{"" if g["updated"] == g["published"] else ", updated " + human_date(g["updated"])}. Steps are for Windows 11 and 10.</p>{sections}

<div class="contact-card" style="margin-top:48px"><div><b>See it live on your PC</b><span>{g["app"]}</span></div><a class="btn solid" href="{DOWNLOAD_URL}">{DOWNLOAD_ICON}Try it free for {TRIAL_DAYS} days</a></div>

<h2 id="related">More fixes</h2>
<ul>{related}</ul>
"""
    ld = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": g["h1"],
        "description": g["description"],
        "datePublished": g["published"],
        "dateModified": g["updated"],
        "author": {"@type": "Organization", "name": "Know My PC", "url": f"{SITE_URL}/"},
        "mainEntityOfPage": SITE_URL + url_for("fix/" + g["slug"]),
        "image": f"{SITE_URL}/img/og.png",
    }
    head = f'<script type="application/ld+json">{json.dumps(ld)}</script>'
    body = f"""
  <div class="wrap page-hero"><p class="crumb"><a href="/fix/">Fix guides</a></p><h1>{g["h1"]}</h1><p>{g["lede"]}</p></div>
</div>
<main id="main" class="wrap doc">
  <aside aria-label="On this page">{"".join(f'<a href="#{i}">{t}</a>' for i, t in toc + [("related", "More fixes")])}</aside>
  <article>{article}</article>
</main>
"""
    return page("fix/" + g["slug"], g["title"], g["description"], body, "fix", head, "article", g["h1"])


def guides_index():
    items = "".join(f'<li><a href="{url_for("fix/" + g["slug"])}"><b>{g["h1"]}</b><span>{g["summary"]}</span></a></li>' for g in GUIDES)
    body = f"""
  <div class="wrap page-hero"><h1>Why is my PC slow?</h1><p>Plain-English fixes for the things that slow Windows down most often: what each one is, whether it's safe to stop, and how to fix it yourself.</p></div>
</div>
<main id="main" class="wrap guides-page">
  <ul class="guide-list">{items}</ul>
</main>
"""
    return page("fix", "Why Is My PC Slow? Fixes for Common Windows Slowdowns",
                "Plain-English fixes for common Windows slowdowns: Vmmem, Antimalware Service Executable, Windows Update, search indexing, a full C: drive and busy ports.",
                body, "fix")


def not_found():
    items = "".join(f'<li><a href="{url_for("fix/" + g["slug"])}"><b>{g["h1"]}</b><span>{g["summary"]}</span></a></li>' for g in GUIDES)
    body = f"""
  <div class="wrap page-hero"><h1>Page not found</h1><p>That page doesn't exist or has moved. Try the <a href="/" style="color:var(--pad)">home page</a>, or one of these guides.</p></div>
</div>
<main id="main" class="wrap guides-page">
  <ul class="guide-list">{items}</ul>
</main>
"""
    html = page("404", "Page not found | Know My PC", "This page doesn't exist. Find out why your Windows PC is slow with Know My PC's guides.", body)
    # The 404 page has no canonical URL of its own and shouldn't be indexed.
    return html.replace(f'<link rel="canonical" href="{SITE_URL}/404.html">', '<meta name="robots" content="noindex">')


def main():
    pages = {"index": home(), "support": support(), "privacy": privacy(), "terms": terms(), "fix": guides_index()}
    for g in GUIDES:
        pages["fix/" + g["slug"]] = guide(g)
    for name, html in list(pages.items()) + [("404", not_found())]:
        path = os.path.join(HERE, name, "index.html") if url_for(name).endswith("/") and name != "index" else os.path.join(HERE, f"{name}.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
    # Each page's own date, so lastmod changes only when that page's content does.
    newest_guide = max(g["updated"] for g in GUIDES)
    lastmod = {"index": max(HOME_UPDATED, newest_guide), "support": SUPPORT_UPDATED, "privacy": PRIVACY_UPDATED, "terms": TERMS_UPDATED, "fix": newest_guide}
    lastmod.update({"fix/" + g["slug"]: g["updated"] for g in GUIDES})
    urls = "".join(f"<url><loc>{SITE_URL}{url_for(n)}</loc><lastmod>{lastmod[n]}</lastmod></url>" for n in pages)
    with open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    with open(os.path.join(HERE, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    # Empty .nojekyll makes GitHub Pages serve files as-is.
    open(os.path.join(HERE, ".nojekyll"), "w").close()
    print("Built", len(pages), "pages and 404.html for", SITE_URL)


if __name__ == "__main__":
    main()

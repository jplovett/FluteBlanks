#!/usr/bin/env python3
"""Generate the new Fluteblanks.com static site into ./new"""
import os, json

OUT = os.path.join(os.path.dirname(__file__), "site")
PHONE = "770-939-2603"
TEL = "tel:+17709392603"
EMAIL = "StateLarge@yahoo.com"

NAV = [("/", "Home"), ("/blanks", "Flute blanks"), ("/prices", "Wood prices"),
       ("/totems", "Totems & fetishes"), ("/shipping", "Shipping & ordering"),
       ("/about", "About"), ("/contact", "Contact")]

FONTS = ('<link rel="preload" href="/fonts/big-shoulders-display-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>'
         '<link rel="preload" href="/fonts/atkinson-hyperlegible-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>')


def page(path, title, desc, body, extra_js=""):
    nav = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{t}</a></li>' for h, t in NAV)
    foot_nav = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    full_title = "Fluteblanks.com" if path == "/" else f"{title} | Fluteblanks.com"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://fluteblanks.com/img/Fluteblank.jpg">
<link rel="icon" href="/img/kokopelli-still.png">
{FONTS}
<link rel="stylesheet" href="/site.css">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="/">
      <picture>
        <source srcset="/img/kokopelli-still.png" media="(prefers-reduced-motion: reduce)">
        <img src="/img/kokopelli-dance.webp" alt="" width="120" height="130">
      </picture>
      <span><span class="brand-name">Fluteblanks</span><span class="brand-by">by George Atkinson, Stone Mountain, GA</span></span>
    </a>
    <a class="head-call" href="{TEL}">Call {PHONE}</a>
    <button class="theme-toggle" type="button" aria-pressed="false">Dark theme</button>
    <nav class="site-nav" aria-label="Main"><ul>{nav}</ul></nav>
  </div>
</header>
<main id="main" class="wrap">
{body}
</main>
<footer class="site-foot">
  <div class="wrap">
    <address>
      <strong>Fluteblanks</strong>
      George Atkinson<br>
      5436 Rosser Rd., Stone Mountain, GA 30087<br>
      <a href="{TEL}">{PHONE}</a><br>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </address>
    <nav aria-label="Footer"><ul>{foot_nav}</ul></nav>
  </div>
</footer>
<script>
(function(){{
  var b=document.querySelector('.theme-toggle'), r=document.documentElement;
  function isDark(){{ return r.dataset.theme ? r.dataset.theme==='dark' : matchMedia('(prefers-color-scheme: dark)').matches; }}
  function sync(){{ var d=isDark(); b.textContent=d?'Light theme':'Dark theme'; b.setAttribute('aria-pressed', String(d)); }}
  b.addEventListener('click', function(){{ var next=isDark()?'light':'dark'; r.dataset.theme=next; try{{localStorage.setItem('theme',next)}}catch(e){{}} sync(); }});
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', sync);
  sync();
}})();
</script>
{extra_js}
</body>
</html>
"""


ORDER = f"""<div class="order">
  <a class="btn" href="{TEL}">Call {PHONE}</a>
  <a class="btn ghost" href="mailto:{EMAIL}">Email {EMAIL}</a>
</div>"""

DRAWING = """<div class="drawing">
  <figure>
    <img src="/img/Fluteblank.jpg" width="528" height="276"
         alt="Two square, one-piece flute blanks with the bore, blow hole and flue already cut">
    <ul class="dims" aria-label="Blank sizes">
      <li class="dim short">
        <div class="dim-line" aria-hidden="true"><span>15½ in</span></div>
        <p>5/8 in bore, key of C</p>
      </li>
      <li class="dim">
        <div class="dim-line" aria-hidden="true"><span>23 to 24 in</span></div>
        <p>3/4 or 7/8 in bore, keys of F#, G, G# or A</p>
      </li>
    </ul>
    <figcaption>One piece of solid wood, line bored. No glue joints.</figcaption>
  </figure>
</div>"""

pages = {}

# ---------------- Home ----------------
pages["index.html"] = page("/", "Home",
  "One-piece, line-bored flute blanks for Native American style flutes, by George Atkinson of Stone Mountain, GA.",
  f"""
<h1>One-piece, line-bored flute blanks</h1>
<p class="lede">Blanks for Native American style flutes, bored from a single piece of solid wood.
We cut the bore, blow hole, exit hole and flue. You finish the flute.</p>
{ORDER}
{DRAWING}
<div class="split">
  <div>
    <h2>The sound that brings people in</h2>
    <p>By whatever name you call them, Native Flutes, Native American Flutes, Native American Love Flutes,
    Native American Style Flutes, Indian Flutes, American Indian Flutes or Native American Courting Flutes,
    they all have that sweet haunting sound that appeals to most human beings.
    To listen to these flutes is a soothing, peaceful therapy, but to play one is a dose of powerful medicine
    for both mind and spirit. It is a tranquilizer for a troubled soul.</p>
    <p>Come in from a bad day at work, pick up a Native flute and play for 15 minutes. A peace will come over
    you and your whole countenance. Your mental outlook will improve. Once you experience this you'll need a
    daily dose of it.</p>
    <p>While an experienced musician will enjoy these flutes, they do not really require a musical background
    or training to enjoy and relax while playing one. These are not pianos with 88 keys and foot pedals.
    Anyone can pick up a flute and play one. The melodies come easily and naturally after a few moments.
    This is part of the relaxing magic of these wonderful instruments.</p>
  </div>
  <figure class="photo">
    <img src="/img/blankCloseUp.jpg" width="480" height="359" loading="lazy"
         alt="Close-up of four finished flutes showing the nest area and sound hole">
    <figcaption>The mouthpiece and nest area, up close.</figcaption>
  </figure>
</div>

<h2>A word about wood</h2>
<p>Every piece of wood is as unique as a fingerprint. Overall color and texture will remain the same, but the
blanks shown here may not be exactly what you see when your blanks arrive. Each blank is hand selected to the
highest standard to be representative of the wood that you select.</p>

<h2>How to buy</h2>
<p>We welcome calls at {PHONE} and email at <a href="mailto:{EMAIL}">{EMAIL}</a>.
We take payment through PayPal. Give us a call or send an email and we'll help you with the process.</p>
<p><a href="/blanks">See blank sizes and prices</a> or <a href="/prices">browse woods and prices</a>.</p>
""")

# ---------------- Blanks ----------------
pages["blanks.html"] = page("/blanks", "Flute blanks",
  "Line-bored, one-piece flute blanks in 15½ in and 23 to 24 in lengths. Sizes, bores, prices and what we cut for you.",
  f"""
<h1>Flute blanks</h1>
<p class="lede">Blanks for Native American style flutes, made from one piece of solid, select-grade wood.</p>
{DRAWING}
<div class="split">
  <div>
    <p>Our flute blanks are made from one piece of solid wood of select grade, mostly clear (no knots) lumber.
    Though mostly clear, some of the eastern cedar will have small tight knots that only add character to the wood.</p>
    <h2>Why one piece, line bored</h2>
    <p>Advantages over the traditional two-piece, glued-together flute blanks offered by others:</p>
    <ul class="plain">
      <li>No failed glue joints</li>
      <li>No glue squeeze-out</li>
      <li>No glue seams down the sides of the flute</li>
      <li>No possibility of air leaks</li>
      <li>Less construction time</li>
      <li>Less sanding time</li>
      <li>More consistent bore size</li>
      <li>Smooth bore inside</li>
      <li>No warping or twisting of the wood</li>
      <li>The wood grain is always matched on all sides</li>
    </ul>
  </div>
  <figure class="photo">
    <img src="/img/blankCloseUp.jpg" width="480" height="359" loading="lazy"
         alt="Close-up of four flutes showing the nest area, flue and true sound hole">
    <figcaption>The mouthpiece, up close.</figcaption>
  </figure>
</div>

<h2>What we cut for you</h2>
<p>We make the bore, the blow hole, the exit hole and the flue. We define the position and size of the
TSH (true sound hole) and cutting edge.</p>
<p>We take special orders and do custom work on request.</p>

<h2>Sizes and prices</h2>
<p>Pricing is for blanks in square form. You may mix sizes and woods to get the best price.</p>
<table class="cutlist">
  <caption>Blank sizes</caption>
  <thead><tr><th scope="col">Length and bore</th><th scope="col">Woods</th><th scope="col" class="num">3 blanks</th><th scope="col" class="num">16 or more</th></tr></thead>
  <tbody>
    <tr><th scope="row">15½ in, 5/8 in bore<br><span class="quiet">key of C</span></th><td>Black walnut, eastern cedar or other woods from the list</td><td class="num">$45.00</td><td class="num">$15.00 each</td></tr>
    <tr><th scope="row">23 to 24 in, 3/4 or 7/8 in bore<br><span class="quiet">keys of F#, G, G# or A</span></th><td>Mahogany, black walnut, eastern cedar or other woods from the list</td><td class="num">$54.00</td><td class="num">$15.00 each</td></tr>
  </tbody>
</table>
<p>We will round the outside of these blanks and leave a flat nest area for an additional charge of $5.00 each.</p>
<p>Shipping and handling is $18.00 for up to 10 blanks, UPS ground.</p>
<p><a href="/prices">See every wood and its price</a>.</p>
{ORDER}

<h2>Learning to make flutes</h2>
<p>We don't teach flute making here. There are several great books that teach flute making with photos
and drawings, including these:</p>
<ul class="plain">
  <li>Keith Stanford, <a href="http://www.cherrycows.com" rel="noopener">CherryCows.com</a></li>
  <li>Russ Wolf, <a href="mailto:rwolf@comcast.net">rwolf@comcast.net</a></li>
</ul>
""")

# ---------------- Prices ----------------
woods = [("American cherry", "18.00"), ("Black walnut", "15.00"), ("Box elder", "18.00"),
         ("Eastern cedar", "15.00"), ("Mahogany", "15.00"), ("Paulownia", "18.00"),
         ("Purpleheart", "20.00"), ("Sassafras", "15.00")]
rows = "".join(f'<tr><th scope="row">{w}</th><td class="num">${p}</td></tr>' for w, p in woods)
pages["prices.html"] = page("/prices", "Wood prices",
  "Flute blank prices by wood: cherry, walnut, box elder, eastern cedar, mahogany, paulownia, purpleheart and sassafras.",
  f"""
<h1>Wood prices</h1>
<p class="lede">Not every wood is available all the time. Please call for availability.</p>

<div class="split">
  <div>
    <table class="cutlist">
      <caption>23 to 24 in blanks, 3/4 or 7/8 in bore, square form</caption>
      <thead><tr><th scope="col">Wood</th><th scope="col" class="num">Per blank</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
    <p>Other mixed woods on request, if in stock. Larger quantities can lower the total price.</p>

    <table class="cutlist">
      <caption>15½ in blanks</caption>
      <thead><tr><th scope="col">Wood</th><th scope="col" class="num">Price</th></tr></thead>
      <tbody><tr><th scope="row">Black walnut, eastern cedar and other woods<br><span class="quiet">ask for the selection of woods on hand</span></th><td class="num">3 blanks, $45.00</td></tr></tbody>
    </table>
    <p class="quiet">5/8 in bore for the key of C; 6/8 in bore for the keys of G and A.</p>
  </div>
  <figure class="photo">
    <img src="/img/gallery/prd00.jpg" width="640" height="425" loading="lazy"
         alt="A row of flute blanks in different woods, from pale to dark red and purple">
    <figcaption>Some of the woods we work with.</figcaption>
  </figure>
</div>

<h2>Options</h2>
<ul class="plain">
  <li>Rounded on the outside with a flat nest area: add $6.00 each.</li>
  <li>We now bore 3/8, 5/8, 6/8 and 7/8 in. We drill these as they are ordered; please call for availability.</li>
</ul>
<p>Shipping and handling varies with distance (by area code) for USPS ground.
See <a href="/shipping">shipping and ordering</a>.</p>
{ORDER}
""")

# ---------------- Totems ----------------
groups = [
  ("Totems", [("T-1", [4, 5]), ("T-2", [6, 7]), ("T-3", [8, 9]), ("T-4", [10, 11]), ("T-5", [12, 13]),
              ("T-6", [14, 15]), ("T-7", [16, 17]), ("T-8", [18, 19]), ("T-9", [20, 21]),
              ("T-10", [22, 23]), ("T-11", [24, 25, 26, 27]), ("T-12", [28, 29])]),
  ("Stands and shelves", [("S-1", [30]), ("S-2", [31]), ("S-3", [32]), ("S-4", [33]),
                          ("S-5 and S-6", [1]), ("S-7", [3]), ("S-8", [2])]),
]
data, html_groups = {}, ""
for gname, items in groups:
    lis = ""
    for code, ids in items:
        key = code.replace(" ", "")
        data[key] = {"title": code, "photos": [f"/img/gallery/prd{i:02d}.jpg" for i in ids]}
        n = len(ids)
        count = f'<span class="count">{n} photos</span>' if n > 1 else ""
        alt = f"{'Totem' if code.startswith('T') else 'Stand'} {code}"
        lis += (f'<li><button type="button" data-item="{key}" aria-label="View {alt}, {n} photo{"s" if n > 1 else ""}">'
                f'<img src="/img/gallery/prd{ids[0]:02d}-grid.jpg" alt="{alt}" loading="lazy" width="420" height="420">'
                f'<span class="cap"><span class="code">{code}</span>{count}</span></button></li>')
    html_groups += f"<h2>{gname}</h2>\n<ul class=\"gallery\">{lis}</ul>\n"

viewer_js = """<dialog class="viewer" aria-labelledby="viewer-title">
  <div class="viewer-inner">
    <div class="viewer-top"><h2 class="viewer-title" id="viewer-title"></h2><button type="button" data-close>Close</button></div>
    <div class="viewer-stage"><img alt=""></div>
    <div class="viewer-bottom"><button type="button" data-prev>Previous photo</button><span class="viewer-count" aria-live="polite"></span><button type="button" data-next>Next photo</button></div>
  </div>
</dialog>
<script>
const ITEMS = """ + json.dumps(data) + """;
const dlg = document.querySelector('dialog.viewer');
const img = dlg.querySelector('.viewer-stage img'), title = dlg.querySelector('.viewer-title'), count = dlg.querySelector('.viewer-count');
const prev = dlg.querySelector('[data-prev]'), next = dlg.querySelector('[data-next]');
let cur = null, idx = 0;
function show() {
  const p = cur.photos;
  img.src = p[idx];
  img.alt = cur.title + (p.length > 1 ? ', photo ' + (idx + 1) + ' of ' + p.length : '');
  count.textContent = p.length > 1 ? `Photo ${idx + 1} of ${p.length}` : '';
  prev.disabled = idx === 0; next.disabled = idx === p.length - 1;
  prev.hidden = next.hidden = p.length < 2;
}
document.querySelectorAll('[data-item]').forEach(b => b.addEventListener('click', () => {
  cur = ITEMS[b.dataset.item]; idx = 0; title.textContent = cur.title; show(); dlg.showModal();
}));
prev.onclick = () => { if (idx > 0) { idx--; show(); } };
next.onclick = () => { if (idx < cur.photos.length - 1) { idx++; show(); } };
dlg.querySelector('[data-close]').onclick = () => dlg.close();
dlg.addEventListener('click', e => { if (e.target === dlg) dlg.close(); });
dlg.addEventListener('keydown', e => { if (e.key === 'ArrowLeft') prev.click(); if (e.key === 'ArrowRight') next.click(); });
</script>"""

pages["totems.html"] = page("/totems", "Totems & fetishes",
  "Hand-carved totems and fetishes sized for our flutes' nest area, plus flute stands and shelves.",
  f"""
<h1>Totems &amp; fetishes</h1>
<div class="split">
  <div>
    <p class="lede">Hand-carved totems that sit on the nest area of your flute. Since they are hand carved,
    no two are exactly alike.</p>
    <ul class="plain">
      <li>For the small key of high C flute: the small bear (smooth or rough), buffalo or roadrunner.</li>
      <li>For all of our other flutes: the larger bear (smooth or rough), eagle, buffalo (standing or resting),
      coyote, kokopelli, or bear with fish.</li>
    </ul>
    <p>The bases are designed to fit the nest area on our flutes and may not fit the nest area of other flutes.</p>
    <p><strong>Each totem is $7.00.</strong></p>
  </div>
  <figure class="photo">
    <a href="/img/totems.jpg"><img src="/img/totems-web.jpg" width="1400" height="1047" loading="lazy"
       alt="A group of hand-carved wooden totems: eagle head, bears, buffalo, roadrunner and coyote"></a>
    <figcaption>Select the photo to see it full size.</figcaption>
  </figure>
</div>
<p class="quiet">Select a piece to see it larger. Most totems have a second photo with a quarter for scale.</p>
{html_groups}
{ORDER}
""", viewer_js)

# ---------------- Shipping ----------------
pages["shipping.html"] = page("/shipping", "Shipping & ordering",
  "How to order flute blanks and totems, payment options and shipping policies.",
  f"""
<h1>Shipping &amp; ordering</h1>
<h2>Ordering</h2>
<p>Phone or email your order so we can give you a quote of the total price, including shipping and handling.</p>
<p>Payment can be made by postal money order or bank money order, or through PayPal. Through PayPal you can pay
with Mastercard, Visa or Discover, or use your PayPal account. Don't have one? You can
<a href="https://www.paypal.com/" rel="noopener">set up a free PayPal account</a>.</p>
{ORDER}

<h2>Shipping and handling</h2>
<ul class="plain">
  <li>Standard shipping in the continental US is USPS or UPS ground. FedEx is not available.</li>
  <li>There is a minimum charge of $18.00 for UPS ground. USPS charges vary by region.</li>
  <li>For example, one finished flute ships UPS for $18.00, and three finished flutes ship UPS for a total of $18.00.</li>
  <li>UPS cannot deliver to PO boxes.</li>
  <li>Orders received before 1 PM Eastern ship the same day. Orders received after 1 PM Eastern go out the next business day.</li>
  <li>We do not ship on weekends.</li>
  <li>Orders outside the US are billed for the actual shipping charges. All charges, including shipping, must be paid in U.S. dollars before shipment.</li>
</ul>
<p>Special shipping needs? Call {PHONE} or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
""")

# ---------------- About ----------------
pages["about.html"] = page("/about", "About",
  "Why we make one-piece, line-bored flute blanks, and our goal of quality blanks at reasonable prices.",
  f"""
<h1>About Fluteblanks</h1>
<div class="split">
  <div>
    <p class="lede">I have acquired a one-of-a-kind machine dedicated to building one-piece, line-bored flute blanks.</p>
    <p>The advantages of a line-bored, one-piece flute blank over the traditional two-piece, glued-together blank are many:</p>
    <ul class="plain">
      <li>No glue joints</li>
      <li>No glue squeeze-out</li>
      <li>No break in the wood grain on the sides of the flute</li>
      <li>No possibility of air leaks because of a failed glue joint</li>
      <li>Less construction time</li>
      <li>Less sanding time</li>
      <li>More consistent bore size</li>
      <li>No warping or twisting of blanks</li>
    </ul>
  </div>
  <figure class="photo">
    <img src="/img/Small_Blanks.jpg" width="457" height="221" loading="lazy" alt="Two square flute blanks">
  </figure>
</div>
<p>A good machine to line bore flutes is very expensive and not in reach of the average flute maker.
Since it takes a little less time to make a line-bored flute, the cost of the machine is offset. This lets us
give you all of the advantages above without charging any more for our products than our competitors charge.</p>
<p>Our goal is to make quality flute blanks available at reasonable prices. Our main focus is to provide flute
blanks for people who want to make flutes but don't have the tools it takes to make a good blank.</p>
<p>You will see from the posted prices that in most cases we can do the work and furnish the wood (mahogany,
black walnut and eastern red cedar) about as cheaply as you can do it yourself.</p>
<p>George Atkinson</p>
""")

# ---------------- Contact ----------------
pages["contact.html"] = page("/contact", "Contact",
  "Call, email or write to Fluteblanks, George Atkinson, Stone Mountain, GA.",
  f"""
<h1>Contact</h1>
<p class="lede">We welcome phone calls and email.</p>
<table class="cutlist">
  <caption class="skip">Contact details</caption>
  <tbody>
    <tr><th scope="row">Phone</th><td><a href="{TEL}">{PHONE}</a></td></tr>
    <tr><th scope="row">Email</th><td><a href="mailto:{EMAIL}">{EMAIL}</a></td></tr>
    <tr><th scope="row">Mail</th><td>George Atkinson<br>5436 Rosser Rd.<br>Stone Mountain, GA 30087</td></tr>
  </tbody>
</table>
{ORDER}
""")

# ---------------- 404 ----------------
pages["404.html"] = page("/404", "Page not found", "Page not found.",
  """<h1>That page has moved</h1>
<p class="lede">Fluteblanks.com has a new look. Everything from the old site is still here.</p>
<p><a href="/">Go to the home page</a>, or see <a href="/blanks">flute blanks</a>, <a href="/prices">wood prices</a>
and <a href="/totems">totems</a>.</p>""")

# ---------------- old URL redirects (Cloudflare Pages _redirects) ----------------
REDIRECTS = """/index.htm / 301
/Home.html / 301
/contents.htm / 301
/heading.htm / 301
/options.htm / 301
/footer.htm / 301
/postinfo.html / 301
/about_us.htm /about 301
/flute_blanks.htm /blanks 301
/blank_large.htm /blanks 301
/mouthPiece_large.htm /blanks 301
/wood_prices.htm /prices 301
/totems.htm /totems 301
/products/* /totems 301
/shipping.htm /shipping 301
/contact_us.htm /contact 301
/guestbook/* /contact 301
"""

os.makedirs(OUT, exist_ok=True)
for name, html in pages.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
with open(os.path.join(OUT, "_redirects"), "w") as f:
    f.write(REDIRECTS)
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write("User-agent: *\nAllow: /\n\nSitemap: https://fluteblanks.com/sitemap.xml\n")
urls = ["", "blanks", "prices", "totems", "shipping", "about", "contact"]
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "".join(f"  <url><loc>https://fluteblanks.com/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
print("built", sorted(os.listdir(OUT)))
